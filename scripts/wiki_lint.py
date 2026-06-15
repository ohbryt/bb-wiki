#!/usr/bin/env python3
"""
bb-wiki wiki_lint.py
====================

bb-wiki 의 건강 상태 검증. SCHEMA.md 규칙 준수 여부 자동 점검.

Usage:
    python3 scripts/wiki_lint.py [--strict] [--fix-frontmatter]

검사 항목:
1. Frontmatter validation (모든 wiki 페이지)
2. Outbound wikilinks >= 2 (per page)
3. 4-섹션 판단 레이어 (concept/entity 필수)
4. Index completeness (모든 페이지가 index.md에 등록)
5. Broken wikilinks
6. Orphan pages (no inbound links)
7. Stale content (updated > 90일)
8. Page size (200줄 초과)
9. Tag audit (분류 외 태그)
10. Log rotation (> 500 entries)
"""
import argparse
import datetime
import re
import sys
from pathlib import Path
from collections import defaultdict

WIKI_ROOT = Path("/Users/ocm/openclaw/workspace/bb-wiki")
WIKI_PAGES = WIKI_ROOT / "concepts"
ENTITY_PAGES = WIKI_ROOT / "entities"
COMPARISON_PAGES = WIKI_ROOT / "comparisons"
QUERY_PAGES = WIKI_ROOT / "queries"

ALL_PAGE_DIRS = [WIKI_PAGES, ENTITY_PAGES, COMPARISON_PAGES, QUERY_PAGES]
SCHEMA_PATH = WIKI_ROOT / "SCHEMA.md"
INDEX_PATH = WIKI_ROOT / "index.md"
LOG_PATH = WIKI_ROOT / "log.md"

REQUIRED_FRONTMATTER = {"title", "created", "updated", "type", "tags", "sources"}
# 4-섹션 판단 레이어. h2(##) 또는 h3(###) 모두 허용
JUDGMENT_LAYER_SECTION_NAMES = [
    "1. Source Quotes",
    "2. My Interpretation",
    "3. Open Questions",
    "4. Contradictions",
]
JUDGMENT_LAYER_PATTERNS = [
    re.compile(r"^#{2,3}\s*" + re.escape(name), re.MULTILINE)
    for name in JUDGMENT_LAYER_SECTION_NAMES
]
STALENESS_DAYS = 90
MAX_PAGE_LINES = 200
LOG_ROTATION_THRESHOLD = 500


def load_schema_tags() -> set:
    """SCHEMA.md 에서 태그 분류 추출."""
    if not SCHEMA_PATH.exists():
        return set()
    content = SCHEMA_PATH.read_text(encoding="utf-8")
    # `#tag` 형식 추출
    return set(re.findall(r"`#([a-z0-9-]+)`", content))


def parse_frontmatter(content: str) -> dict:
    """YAML frontmatter 파싱 (간이 버전)."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end < 0:
        return {}
    fm = content[3:end].strip()
    result = {}
    for line in fm.split("\n"):
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip()
    return result


def get_outbound_wikilinks(content: str) -> list:
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def get_inbound_wikilinks(page_stem: str, all_pages: dict) -> list:
    """특정 페이지를 가리키는 inbound wikilink 수집."""
    inbounds = []
    for stem, content in all_pages.items():
        if stem == page_stem:
            continue
        if f"[[{page_stem}]]" in content:
            inbounds.append(stem)
    return inbounds


def line_count(content: str) -> int:
    return len([l for l in content.split("\n") if l.strip()])


def days_since(date_str: str) -> int:
    try:
        d = datetime.date.fromisoformat(date_str.strip())
        return (datetime.date.today() - d).days
    except (ValueError, AttributeError):
        return 0


def load_all_pages() -> dict:
    """stem → content dict."""
    pages = {}
    for d in ALL_PAGE_DIRS:
        if not d.exists():
            continue
        for fpath in d.glob("*.md"):
            pages[fpath.stem] = fpath.read_text(encoding="utf-8")
    return pages


def main():
    parser = argparse.ArgumentParser(description="bb-wiki lint checker")
    parser.add_argument("--strict", action="store_true", help="Strict mode (warnings become errors)")
    parser.add_argument("--fix-frontmatter", action="store_true", help="Auto-add missing frontmatter fields")
    args = parser.parse_args()

    issues = {"error": [], "warning": [], "info": []}
    schema_tags = load_schema_tags()
    pages = load_all_pages()

    if not pages:
        print("⚠️  No wiki pages found. Run ingest_deep_dive.py first.\n")
        sys.exit(0)

    print(f"🔍 Linting {len(pages)} pages...\n")

    # === 1. Frontmatter validation ===
    for stem, content in pages.items():
        fm = parse_frontmatter(content)
        if not fm:
            issues["error"].append(f"[{stem}] Missing frontmatter")
            continue
        missing = REQUIRED_FRONTMATTER - set(fm.keys())
        if missing:
            issues["error"].append(f"[{stem}] Frontmatter missing fields: {missing}")

    # === 2. Outbound wikilinks >= 2 ===
    for stem, content in pages.items():
        out = get_outbound_wikilinks(content)
        if len(out) < 2:
            issues["warning"].append(
                f"[{stem}] Only {len(out)} outbound [[wikilinks]] (minimum 2 recommended)"
            )

    # === 3. 4-섹션 판단 레이어 (concept/entity 필수) ===
    for stem, content in pages.items():
        fm = parse_frontmatter(content)
        page_type = fm.get("type", "")
        if page_type in ("concept", "entity"):
            for pattern, name in zip(JUDGMENT_LAYER_PATTERNS, JUDGMENT_LAYER_SECTION_NAMES):
                if not pattern.search(content):
                    issues["warning"].append(
                        f"[{stem}] Missing 4-섹션: '{name}' (h2 or h3)"
                    )

    # === 4. Index completeness ===
    if INDEX_PATH.exists():
        index_content = INDEX_PATH.read_text(encoding="utf-8")
        for stem in pages:
            if f"[[{stem}]]" not in index_content:
                issues["warning"].append(
                    f"[{stem}] Not in index.md — add under appropriate section"
                )

    # === 5. Broken wikilinks ===
    for stem, content in pages.items():
        for link in get_outbound_wikilinks(content):
            link_stem = link.split("|")[0].strip()
            if link_stem not in pages:
                # raw/ 링크는 면제
                if not link_stem.startswith("raw/") and not link_stem.startswith("file:"):
                    issues["info"].append(
                        f"[{stem}] [[{link_stem}]] points to non-existent page"
                    )

    # === 6. Orphan pages (no inbound links) ===
    for stem in pages:
        inbounds = get_inbound_wikilinks(stem, pages)
        # frontmatter `sources: [raw/...]` 도 inbound 으로 인정
        fm = parse_frontmatter(pages[stem])
        source_links = fm.get("sources", "")
        if not inbounds and "raw/" not in source_links:
            issues["info"].append(
                f"[{stem}] Orphan page (no inbound [[wikilinks]] from other wiki pages)"
            )

    # === 7. Stale content (updated > 90일) ===
    for stem, content in pages.items():
        fm = parse_frontmatter(content)
        updated = fm.get("updated", "")
        if updated and days_since(updated) > STALENESS_DAYS:
            issues["warning"].append(
                f"[{stem}] Stale: updated {updated} ({days_since(updated)} days ago)"
            )

    # === 8. Page size ===
    for stem, content in pages.items():
        lc = line_count(content)
        if lc > MAX_PAGE_LINES:
            issues["warning"].append(
                f"[{stem}] {lc} lines (>{MAX_PAGE_LINES}) — consider splitting"
            )

    # === 9. Tag audit ===
    for stem, content in pages.items():
        fm = parse_frontmatter(content)
        tags_str = fm.get("tags", "[]")
        # 매우 단순한 파싱
        page_tags = re.findall(r'"([a-z0-9-]+)"', tags_str) or re.findall(r"'([a-z0-9-]+)'", tags_str)
        if not page_tags:
            page_tags = re.findall(r"\[?([a-z0-9-]+)\]?", tags_str)
        for t in page_tags:
            if schema_tags and t not in schema_tags and t not in ("meta", "entity", "concept", "comparison", "open-question", "hypothesis", "todo", "archive", "contradiction"):
                issues["info"].append(
                    f"[{stem}] Tag '{t}' not in SCHEMA.md taxonomy"
                )

    # === 10. Log rotation ===
    if LOG_PATH.exists():
        log_content = LOG_PATH.read_text(encoding="utf-8")
        entry_count = log_content.count("## [")
        if entry_count > LOG_ROTATION_THRESHOLD:
            issues["warning"].append(
                f"[log.md] {entry_count} entries (>{LOG_ROTATION_THRESHOLD}) — consider rotating"
            )

    # === Report ===
    n_err = len(issues["error"])
    n_warn = len(issues["warning"])
    n_info = len(issues["info"])

    if n_err == 0 and n_warn == 0 and n_info == 0:
        print("✅ LINT PASSED — wiki is healthy.\n")
        sys.exit(0)

    if issues["error"]:
        print(f"❌ ERRORS ({n_err}):")
        for i in issues["error"]:
            print(f"  • {i}")
    if issues["warning"]:
        print(f"\n⚠️  WARNINGS ({n_warn}):")
        for i in issues["warning"]:
            print(f"  • {i}")
    if issues["info"]:
        print(f"\n💡 INFO ({n_info}):")
        for i in issues["info"]:
            print(f"  • {i}")

    print(f"\n📊 Summary: {n_err} errors, {n_warn} warnings, {n_info} info")
    if args.strict and (n_err or n_warn):
        sys.exit(1)
    print()


if __name__ == "__main__":
    main()
