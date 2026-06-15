#!/usr/bin/env python3
"""
bb-wiki ingest_deep_dive.py
============================

arp-v27/literature 의 기존 deep-dive .md 파일을 bb-wiki 페이지로 변환.

Usage:
    python3 scripts/ingest_deep_dive.py <source.md> [--type concept|entity|comparison] [--dry-run]
    python3 scripts/ingest_deep_dive.py --batch [--limit N] [--dry-run]

동작:
1. 소스 .md 읽기
2. 파일명/내용에서 페이지 type 추론 (concept/entity/comparison)
3. YAML frontmatter 자동 생성
4. 4-섹션 판단 레이어가 없으면 템플릿 삽입 (사용자가 나중에 채움)
5. 적절한 폴더에 저장 (concepts/, entities/, comparisons/)
6. index.md 업데이트
7. log.md 에 append
"""
from __future__ import annotations  # Python 3.9 호환
import argparse
import datetime
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional

WIKI_ROOT = Path("/Users/ocm/openclaw/workspace/bb-wiki")
RAW_DIR = WIKI_ROOT / "raw"
SCRIPTS_DIR = WIKI_ROOT / "scripts"

# 4-섹션 판단 레이어 (mandatory). h2 또는 h3 모두 허용
JUDGMENT_LAYER_SECTION_NAMES = [
    "1. Source Quotes",
    "2. My Interpretation",
    "3. Open Questions",
    "4. Contradictions",
]
JUDGMENT_LAYER_REGEX = re.compile(
    r"^#{2,3}\s*(?:" + "|".join(re.escape(n) for n in JUDGMENT_LAYER_SECTION_NAMES) + r")",
    re.MULTILINE,
)

JUDGMENT_LAYER_TEMPLATE = """

## 4-섹션 판단 레이어

### 1. Source Quotes

<!-- 원문에서 직접 인용. 각 인용은 raw/ 파일 경로 또는 DOI/PMID 링크 -->
<!-- 예: "원문 abstract에서 '...'" — raw/scGPT_Deep_Analysis.md 참조 -->

### 2. My Interpretation

<!-- 이 페이지에서 어디까지 말할 수 있는가 -->
<!-- AI 요약과 구별되는 Demios / 사용자의 해석 -->
<!-- 추측은 추측으로 명시 -->

### 3. Open Questions

<!-- 다음에 읽을 논문 / 다음 실험 / 다음 검증 포인트 -->
<!-- An Lab 에세이의 "자기 질문을 세우는 순간" -->

### 4. Contradictions

<!-- 다른 wiki 페이지와 충돌 -->
<!-- frontmatter 에 `contradictions: [page-name]` 추가 -->
"""


def detect_type(filepath: Path) -> str:
    """파일명/내용으로 페이지 type 추론."""
    name = filepath.stem.lower()
    if any(kw in name for kw in ["vs", "comparison", "compare"]):
        return "comparison"
    if any(kw in name for kw in ["deep_analysis", "review", "integration"]):
        return "concept"
    # default: concept
    return "concept"


def detect_tags(content: str) -> list:
    """내용에서 BB 도메인 태그 추출."""
    text = content.lower()
    tag_keywords = {
        "#mash": ["mash", "masld", "nash", "dgat", "lipid metabolism"],
        "#oxphos": ["oxphos", "mitochondri", "electron transport", "mito "],
        "#ferroptosis": ["ferroptosis", "gpx4", "lipid peroxidation"],
        "#sarcopenia": ["sarcopenia", "muscle aging", "fap", "satellite cell"],
        "#longevity": ["longevity", "aging", "hallmarks"],
        "#frailty": ["frailty", "multi-omic"],
        "#fibrosis": ["fibrosis", "fibr", "cthrc1"],
        "#naaa": ["naaa", "n-acylethanolamine", "peb", "palmitoylethanolamide"],
        "#peptide": ["peptide", "amino acid sequence"],
        "#senescence": ["senescen", "senolytic", "d+q", "pioglitazone"],
        "#cachexia": ["cachexia", "muscle wasting", "pebp4"],
        "#cancer": ["cancer", "tumor", "carcinoma", "leukemia"],
        "#ipf": ["ipf", "idiopathic pulmonary", "bleomycin"],
        "#biostat": ["biostat", "statistics", "p-value"],
        "#ai": ["ai ", "machine learning", "deep learning", "neural", " llm", "gpt"],
    }
    tags = []
    for tag, kws in tag_keywords.items():
        if any(kw in text for kw in kws):
            tags.append(tag.lstrip("#"))
    return tags if tags else ["meta"]


def extract_title(filepath: Path) -> str:
    """파일명에서 사람이 읽기 좋은 title 생성."""
    name = filepath.stem
    # snake_case → Title Case
    title = name.replace("_", " ").replace("-", " ").title()
    return title


def has_judgment_layer(content: str) -> bool:
    """4-섹션 판단 레이어가 이미 있는지 검사 (모든 4섹션)."""
    return len(JUDGMENT_LAYER_REGEX.findall(content)) >= 4


def build_frontmatter(title: str, type_: str, tags: list, source_filename: str) -> str:
    """YAML frontmatter 생성."""
    today = datetime.date.today().isoformat()
    tags_yaml = ", ".join(f'"{t}"' for t in tags)
    return f"""---
title: {title}
created: {today}
updated: {today}
type: {type_}
tags: [{tags_yaml}]
sources:
  - raw/{source_filename}
contradictions: []
---

"""


def extract_existing_content(content: str) -> str:
    """기존 deep-dive의 핵심 내용만 추출 (frontmatter 제거 후)."""
    # 기존 YAML frontmatter 제거
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            content = content[end + 3 :].lstrip("\n")
    return content


def extract_wikilinks(content: str) -> list:
    """내용에서 [[wikilinks]] 추출."""
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def get_outbound_wikilinks(content: str) -> int:
    """[[wikilink]] 개수 카운트."""
    return len(re.findall(r"\[\[([^\]]+)\]\]", content))


def ingest(source_path: Path, type_: Optional[str] = None, dry_run: bool = False) -> Optional[Path]:
    """단일 deep-dive를 wiki 페이지로 변환. None if skipped."""
    if not source_path.exists():
        print(f"  ❌ Source not found: {source_path}")
        return None

    content = source_path.read_text(encoding="utf-8")
    title = extract_title(source_path)
    page_type = type_ or detect_type(source_path)
    tags = detect_tags(content)
    clean_content = extract_existing_content(content)

    # outbound wikilinks 부족 시 보충 placeholder
    if get_outbound_wikilinks(clean_content) < 2:
        # judgment layer 템플릿이 wikilink 추가 기회를 줌
        pass

    # 4-섹션 판단 레이어 없으면 템플릿 추가
    if not has_judgment_layer(clean_content):
        clean_content = clean_content.rstrip() + "\n" + JUDGMENT_LAYER_TEMPLATE + "\n"

    # frontmatter prepend
    frontmatter = build_frontmatter(title, page_type, tags, source_path.name)
    full_content = frontmatter + clean_content

    # 저장 경로 결정
    target_dir = WIKI_ROOT / {
        "concept": "concepts",
        "entity": "entities",
        "comparison": "comparisons",
    }[page_type]
    target_path = target_dir / f"{source_path.stem.lower()}.md"

    if dry_run:
        print(f"  [DRY] Would create: {target_path}")
        print(f"  [DRY] Type: {page_type} | Tags: {tags} | Title: {title}")
        return target_path

    target_path.write_text(full_content, encoding="utf-8")
    print(f"  ✓ Created: {target_path.relative_to(WIKI_ROOT)}")
    return target_path


def update_index(created_files: list) -> None:
    """index.md 업데이트 (Entities/Concepts/Comparisons 섹션)."""
    index_path = WIKI_ROOT / "index.md"
    content = index_path.read_text(encoding="utf-8")

    # 기존 페이지 목록 추출
    for fpath in created_files:
        rel = fpath.relative_to(WIKI_ROOT)
        stem = fpath.stem
        if "concepts/" in str(rel):
            section = "## Concepts"
        elif "entities/" in str(rel):
            section = "## Entities"
        elif "comparisons/" in str(rel):
            section = "## Comparisons"
        else:
            continue
        # wikilink 라인 추가 (중복 방지)
        link_line = f"- [[{stem}]] — (in-progress, see [[log]])"
        if link_line not in content:
            content = content.replace(section, f"{section}\n{link_line}", 1)

    index_path.write_text(content, encoding="utf-8")
    print(f"  ✓ Updated: index.md ({len(created_files)} entries)")


def update_log(actions: list) -> None:
    """log.md 에 액션 append."""
    log_path = WIKI_ROOT / "log.md"
    today = datetime.date.today().isoformat()
    new_entries = []
    for fname, page_type, target in actions:
        new_entries.append(
            f"\n## [{today}] ingest | {fname}\n"
            f"- Type: {page_type}\n"
            f"- Created: {target.relative_to(WIKI_ROOT)}\n"
            f"- Source: raw/{fname}"
        )
    with log_path.open("a", encoding="utf-8") as f:
        f.write("\n".join(new_entries) + "\n")
    print(f"  ✓ Updated: log.md ({len(actions)} entries)")


def main():
    parser = argparse.ArgumentParser(description="bb-wiki ingest_deep_dive.py")
    parser.add_argument("source", nargs="?", help="Source .md file path")
    parser.add_argument("--type", choices=["concept", "entity", "comparison"], help="Page type override")
    parser.add_argument("--batch", action="store_true", help="Batch ingest all arp-v27 deep-dives")
    parser.add_argument("--limit", type=int, default=10, help="Batch limit")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    actions = []

    if args.batch:
        # raw/ 의 모든 .md deep-dive 처리
        sources = sorted([p for p in RAW_DIR.glob("*.md") if p.stem not in ["SCHEMA", "index", "log"]])
        sources = sources[: args.limit]
        print(f"\n📥 Batch ingest: {len(sources)} sources\n")
        for src in sources:
            print(f"\n→ {src.name}")
            target = ingest(src, type_=args.type, dry_run=args.dry_run)
            if target:
                actions.append((src.name, args.type or detect_type(src), target))
    elif args.source:
        src = Path(args.source)
        print(f"\n📥 Ingest: {src.name}\n")
        target = ingest(src, type_=args.type, dry_run=args.dry_run)
        if target:
            actions.append((src.name, args.type or detect_type(src), target))
    else:
        parser.print_help()
        sys.exit(1)

    if actions and not args.dry_run:
        print()
        update_index([a[2] for a in actions])
        update_log(actions)
        print(f"\n✅ Ingest complete: {len(actions)} pages\n")
    elif args.dry_run:
        print(f"\n[DRY RUN] Would create {len(actions)} pages. Re-run without --dry-run.\n")


if __name__ == "__main__":
    main()
