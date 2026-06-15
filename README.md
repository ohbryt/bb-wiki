---
title: bb-wiki 운영 가이드
created: 2026-06-14
updated: 2026-06-14
type: readme
tags: [meta]
---

# Brown Biotech Wiki (bb-wiki)

> An Lab LLM-Wiki pedagogy × Brown Biotech 도메인.
> **"AI는 정리를 빠르게 하지만, 판단은 사용자가 한다."**

## 한 줄 요약

Brown Biotech의 **persistent, interlinked knowledge base**. arp-v27/literature/ 의 41개 deep-dive + 신규 ingest를 **compounding knowledge**로 변환. Obsidian graph view로 시각화 가능. **4-섹션 판단 레이어**가 모든 페이지의 핵심.

## 위치 & 접근

| 경로 | 용도 |
|---|---|
| `/Users/ocm/openclaw/workspace/bb-wiki/` | Primary (canonical) |
| `~/Documents/Obsidian Vault/brown-biotech` | Obsidian 브라우징 (symlink) |
| `bb-wiki/raw/` | arp-v27/literature/ (immutable source layer, symlink) |

## Quick start

```bash
cd /Users/ocm/openclaw/workspace/bb-wiki

# 1. Lint — wiki 건강 상태
python3 scripts/wiki_lint.py

# 2. 신규 deep-dive 1개 ingest
python3 scripts/ingest_deep_dive.py /Users/ocm/openclaw/workspace/arp-v27/literature/SomePaper_Deep_Analysis.md --type concept

# 3. 배치 ingest (10개씩)
python3 scripts/ingest_deep_dive.py --batch --limit 10

# 4. Obsidian에서 열기
open "~/Documents/Obsidian Vault/brown-biotech"
```

## 구조

```
bb-wiki/
├── SCHEMA.md           ← 규칙 + 태그 분류 (single source of truth)
├── index.md            ← 페이지 카탈로그
├── log.md              ← 시계열 액션 로그
├── README.md           ← 이 파일
├── raw/                ← [symlink] arp-v27/literature — 불변 소스
├── concepts/           ← 개념/메커니즘/경로
├── entities/           ← 인물/기관/저널/화합물/타깃/데이터셋
├── comparisons/        ← 양대비 분석
├── queries/            ← 에세이급 답변
├── assets/             ← 그림, 다이어그램
├── scripts/
│   ├── ingest_deep_dive.py  ← deep-dive → wiki 페이지 변환
│   └── wiki_lint.py         ← 위키 건강 상태 점검
└── _archive/           ← 아카이브된 페이지
```

## 3-섹션 (또는 4-섹션) 판단 레이어

> An Lab 에세이의 핵심: "AI 요약은 답이 아니라 자료. 학생이 자기 질문을 세우는 자리."

**모든 concept/entity/comparison 페이지 하단에 4-섹션 필수:**

### 1. Source Quotes (원문 충실)
- 논문/원문에서 직접 인용
- 각 인용은 `[[raw/.../source.pdf]]` 또는 DOI/PMID 링크
- 1-3개로 제한

### 2. My Interpretation (Demios/사용자 해석)
- "이 페이지에서 어디까지 말할 수 있는가"
- AI 요약과 명확히 구분
- 추측은 추측으로 명시
- **모르면 "모름"이라고 적기** (빈칸 두는 용기)

### 3. Open Questions (자기 질문) ⭐
- 다음에 읽을 논문 / 다음 실험 / 다음 검증
- An Lab 에세이의 "학생이 자기 질문을 세우는 순간"
- `[[queries/...]]` 페이지로 발전 가능
- 0개여도 OK

### 4. Contradictions (충돌)
- 다른 wiki 페이지와 모순
- frontmatter `contradictions: [page-name]` 표시
- 사용자 검토 플래그

## 3-Checkpoint (Feature Factory)

Brown Biotech 운영 원칙 준수:

| # | Checkpoint | 트리거 | 게이트 |
|---|---|---|---|
| 1 | **上车** (Human Onboard) | 새 페이지/concept 만들기 전 | Dr. OCM 검토 |
| 2 | **Taste align** (Feedback) | 첫 draft / 4-섹션 채운 후 | 스타일/voice 보정 |
| 3 | **Go/No-go** (Validation) | 출판/공유 전 | 최종 검증 |

> "다 하자" 실행 중에도 **#1과 #3은 절대 스킵 안 함**.

## 일일/주간 운영 리듬

### Daily (5분)
- `python3 scripts/wiki_lint.py` — 위키 건강 확인
- 신규 page ingest 시 wikilinks 2+ 채우기
- 4-섹션 Open Questions 한 줄이라도 적기

### Weekly (Friday, 30분)
- `python3 scripts/wiki_lint.py` — strict mode
- 0 outbound wikilinks 페이지 정리
- 200줄 초과 페이지 split 검토
- Stale 페이지 (90일+) — update or archive
- index.md 정리

### Monthly (1시간)
- 새 태그가 등장하면 SCHEMA.md 분류 추가
- 아카이브 후보 검토
- 14 query family coverage 점검

## Pitfalls

- **`raw/` 절대 수정 금지** — 보정은 Layer 2 페이지에
- **세션 시작 시 orientation** — `SCHEMA.md` + `index.md` + 최근 `log.md` 30줄
- **wikilink 0인 페이지 = 안 보임** — 최소 2개 outbound 필수
- **frontmatter 누락 = lint error** — 자동 보충 가능하지만 의도 명시
- **태그는 SCHEMA 분류에서만** — 새 태그 필요 시 SCHEMA.md 먼저 갱신
- **200줄 초과 시 split** — 분할 + cross-link
- **충돌은 silently 덮어쓰지 말 것** — 명시적으로 표시
- **log.md 500 entry 도달 시 회전** — `log-YYYY.md`로 rename

## Integration

### Brown Biotech Stack 에서의 위치

```
arp-v27/literature/ (raw)  ──┐
                              ├─→  bb-wiki/ (Layer 2)
PRISM RAG (FAISS+turbovec) ──┤
                              │
Notion HQ ───────────────────────→  cross-reference
                              │
Obsidian Vault ────────────────→  그래프 시각화
```

### Paper Intake Workflow (Track F)

`brown-biotech-paper-intake-workflow` skill의 A/B/C/D/E 에 **F (Wiki compound)** 추가됨.

신규 페이퍼 받으면:
- A: deep-dive (arp-v27/literature/)
- F: bb-wiki 페이지 (4-섹션 판단 레이어)

### Daily Research Pulse 연동 (예정)

`brown_biotech_research_pulse_publisher.py` 가 publish 전 bb-wiki 의 cross-reference 자동 조회 → wiki 의 Open Questions 가 있으면 "다음 검증 포인트"로 mention.

## Inspiration

- **An Lab, "사유와 탐구, 책임의 주체로 오는 당신을 기다리며" (2026-06-13)** — Korea University, LLM-Wiki 대학원 수업 회고. 핵심 발췌:
  > "AI가 들어온 뒤 대학의 역할은 더 어려워졌다... 빠른 도구 곁에는 느리게 확인하는 사람이 필요하다."
- **Andrej Karpathy, LLM-Wiki gist (2024)** — 3-레이어 패턴, persistent compounding knowledge
- **Eugene Yan, "Compounding"** — knowledge가 자라나도록 시스템 설계

## 다음 단계 (로드맵)

- [ ] 41개 arp-v27/literature deep-dive 전부 ingest (batch)
- [ ] 14 query family × 1 concept 페이지 시드 (lifespan, MASH, IPF, sarcopenia 등)
- [ ] Daily research pulse publisher 와 bb-wiki 연동 (cross-reference 자동)
- [ ] Paid Brief 작성 시 bb-wiki 페이지 = source-of-truth
- [ ] Obsidian Dataview 쿼리 — research gap / stale pages 시각화
- [ ] 4-agent pipeline 의 Reviewer 단계에 wiki-lint 자동 gate
