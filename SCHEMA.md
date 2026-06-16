---
title: Wiki Schema
created: 2026-06-14
updated: 2026-06-14
type: schema
tags: [meta]
---

# Brown Biotech Wiki Schema

> LLM-Wiki × Brown Biotech 도메인 규칙.
> Karpathy의 LLM-Wiki 3-레이어 구조 + Brown Biotech의 14 query family taxonomy 결합.

## 도메인

**Brown Biotech Longevity & Refractory Disease Research Wiki**
- Longevity, anti-aging, refractory cancer, idiopathic pulmonary fibrosis (IPF), MASH/MASLD, sarcopenia, senescence, NAAA, peptide therapeutics, anti-aging cosmetics
- Drug discovery (ARP v27), clinical translation, AI/ML methods for biology, paid research briefs

## 3-레이어 구조

```
bb-wiki/
├── SCHEMA.md           ← 이 파일. 규칙 + 태그 분류
├── index.md            ← 페이지 카탈로그 (섹션별)
├── log.md              ← 시계열 액션 로그 (append-only, 500 entry 넘으면 회전)
├── README.md           ← 운영 가이드 (3-checkpoint, daily/weekly 룰)
├── raw/                ← Layer 1: 불변 소스 (PDF, arXiv, 외부 자료)
├── concepts/           ← Layer 2: 개념/메커니즘/경로 페이지
├── entities/           ← Layer 2: 인물/기관/저널/화합물/타깃/데이터셋
├── comparisons/        ← Layer 2: 양대비 분석
├── queries/            ← Layer 2: 에세이급 답변 (재사용 가치 있음)
├── assets/             ← 그림, 다이어그램 (raw에서 인용)
├── scripts/            ← 운영 도구 (ingest, lint, sync)
└── _archive/           ← 더 이상 쓰이지 않는 페이지
```

**Layer 1 (raw/):** 불변. 에이전트는 읽기만 함. 수정/이동 금지. 보정은 Layer 2 페이지에 기록.
**Layer 2 (wiki):** 에이전트/사용자 공동 소유. 생성, 업데이트, 교차참조는 자유.
**Layer 3 (schema):** 규칙. 이 파일. 도메인 확장 시 먼저 업데이트.

## 컨벤션

- **파일명:** lowercase, hyphens, no spaces (예: `oxphos-cancer-vulnerability.md`)
- **모든 페이지 = YAML frontmatter 필수:** `title, created, updated, type, tags, sources`
- **모든 페이지는 최소 2개 outbound `[[wikilinks]]` 필수** (고아 페이지 방지)
- **업데이트 시 `updated` 날짜 갱신** (staleness 추적)
- **모든 신규 페이지는 `index.md` 에 등록**
- **모든 액션은 `log.md` 에 append**
- **모든 concept/entity 페이지 = 4-섹션 판단 레이어 필수** (아래 참조)

## 4-섹션 판단 레이어 (mandatory)

> An Lab 에세이의 핵심: "AI 요약은 답이 아니라 자료. 학생이 자기 질문을 세우는 자리."
> 모든 concept/entity 페이지 하단에 다음 4섹션을 둠.

### 1. Source Quotes
- 원문에서 직접 인용 (원문 충실)
- 각 인용은 `[[raw/.../source.pdf#page=X]]` 또는 DOI/PMID 링크
- 1-3개 인용으로 제한 — 요약이 아니라 증거

### 2. My Interpretation
- "이 페이지에서 내가 어디까지 말할 수 있는가"
- AI 요약과 구별되는 **사용자/Demios의 해석**
- 추측은 추측으로 명시 ("~로 추정", "~일 가능성")
- **빈칸을 두는 용기** — 모르면 "모름"이라고 적기

### 3. Open Questions
- **학생이 자기 질문을 세우는 순간** (An Lab 에세이)
- 다음에 읽을 논문 / 다음 실험 / 다음 검증 포인트
- `[[queries/...]]` 페이지로 발전할 수 있음
- 0개여도 됨 — "지금은 질문이 없다"도 유효한 상태

### 4. Contradictions
- 다른 wiki 페이지와 충돌하는 주장
- 충돌하는 페이지로 `[[wikilinks]]` + frontmatter `contradictions: [page-name]`
- 사용자 검토 필요 플래그

## 태그 분류

### 도메인 태그 (BB 14 query family 미러 + 확장)

| 태그 | 의미 | 출처 쿼리 패밀리 |
|---|---|---|
| `#mash` | MASH/MASLD/NASH, lipid metabolism, DGAT1/2 | MASH Liver Atlas & DGAT2 |
| `#oxphos` | Mitochondrial vulnerability, OXPHOS dependency | OXPHOS & Mito |
| `#ferroptosis` | Lipid peroxidation, GPX4 | Ferroptosis |
| `#sarcopenia` | Muscle aging, snRNA-seq, FAPs | Sarcopenia Single-Cell |
| `#longevity` | Cross-tissue aging, hallmarks | Aging Muscle Atlas |
| `#frailty` | Proteomic+metabolomic aging | Frailty Multi-Omics |
| `#fibrosis` | FAPs, IPF, CTHRC1+, spatial | Muscle/Lung Fibrosis Spatial |
| `#naaa` | N-acylethanolamine acid amidase | BB drug discovery |
| `#peptide` | Therapeutic peptides | peptide-service |
| `#senescence` | Senolytics, D+Q, pioglitazone | Senescence & Senolytic |
| `#cachexia` | PEBP4/KEAP1/NRF2 muscle wasting | PEBP4 paper lineage |
| `#cancer` | Refractory cancer therapeutics | BB drug discovery |
| `#ipf` | Idiopathic pulmonary fibrosis | Lung Fibrosis Spatial |
| `#cosmetics` | Anti-aging cosmetics | BB line |
| `#biostat` | biostatx, statistical methods | biostatx |
| `#ai` | AI/ML for biology | ARP v27, SoI |
| `#synthesis` | Chemistry, drug synthesis | ARP v27 |
| `#clinical` | Clinical trials, translational | BB clinical pipeline |
| `#biomarker` | Predictive / prognostic biomarker, companion diagnostic | genox-site (BB-IO Compass) |
| `#dx` | In-vitro diagnostic, LDT, CLIA/CAP lab | genox-site (BB-IO Compass) |

### 메타 태그

| 태그 | 용도 |
|---|---|
| `#entity` | 인물/기관/저널/화합물/타깃/데이터셋 |
| `#concept` | 개념/메커니즘/경로 |
| `#comparison` | 양대비 분석 |
| `#contradiction` | 충돌 주장 |
| `#open-question` | 미해결 질문 (해당 페이지가 주로 다룸) |
| `#hypothesis` | 가설 (검증 미완) |
| `#todo` | 후속 액션 필요 |
| `#archive` | 아카이브 후보 (검토 후 이동) |

### Sub-domain 태그 (보조 분류)

> 14 query family 아래에 위치. 페이지가 primary 태그와 함께 가질 수 있음.

| 태그 | 의미 | 상위 도메인 |
|---|---|---|
| `#mitochondria` | 미토콘드리아 (전반) | `#oxphos` |
| `#drug-discovery` | 약물 발견 일반 (ARP v27 컨텍스트) | 다수 |
| `#anti-fibrotic` | 항섬유화 작용 | `#ipf`, `#fibrosis`, `#mash` |
| `#endocannabinoid` | Endocannabinoid 시스템 (NAAA, MGLL, CB1/2) | `#naaa` |
| `#anti-inflammatory` | 항염증 작용 | 다수 |
| `#senolytic` | 세노리틱 (senolysis) | `#senescence` |
| `#mitophagy` | 미토파지 | `#oxphos`, `#longevity` |
| `#autophagy` | autophagy 일반 | `#longevity` |
| `#apoptosis` | apoptosis | `#cancer`, `#senescence` |
| `#transcriptomics` | snRNA-seq, scRNA-seq | `#ai`, 다수 |
| `#spatial` | Spatial transcriptomics (Visium, Xenium) | `#fibrosis`, `#cancer` |
| `#metabolomics` | Metabolomics | `#longevity`, `#frailty` |
| `#cryo-em` | Cryo-EM 구조 | `#synthesis` |
| `#docking` | Molecular docking | `#synthesis`, `#ai` |
| `#methodology` | Research methodology / format / framework | 다수 |
| `#gwas` | GWAS, human genetic association | `#clinical`, `#ai` |

## 페이지 임계값 (Page Thresholds)

- **페이지 생성** — entity/concept가 2+ source에서 등장 OR 1 source에서 중추 역할
- **기존 페이지에 추가** — 기존 페이지의 entity/concept가 새 source에서 언급
- **페이지 생성하지 말 것** — 단순 언급 (각주/부수적), 도메인 외 주제
- **페이지 분할** — 200줄 초과 시 sub-topic으로 분리 + cross-link
- **페이지 아카이브** — 완전 대체됨 / 도메인 외 → `_archive/`로 이동, index에서 제거

## 타입별 페이지 구조

### Concept 페이지 (`concepts/<name>.md`)
- 한 줄 정의
- 현재 지식 상태 (current state)
- 핵심 메커니즘 / 경로
- 4-섹션 판단 레이어
- 관련 entity/comparison 페이지로 wikilink

### Entity 페이지 (`entities/<type>-<name>.md`)
- Overview / 정의
- 핵심 사실 + 날짜
- 다른 entity와의 관계
- 4-섹션 판단 레이어
- 원문 링크

### Comparison 페이지 (`comparisons/<topic>.md`)
- 비교 대상과 이유
- 비교 차원 (table 형식)
- 결론 / 종합
- 출처

### Query 페이지 (`queries/<date>-<topic>.md`)
- 질문 / 맥락
- 답변이 에세이급 (재사용 가치)
- 인용한 wiki 페이지
- 4-섹션 판단 레이어 (특히 Open Questions 강조)

## 업데이트 정책 (충돌 시)

1. 날짜 비교 — 최신 source가 우선 (단순 우세는 아님)
2. 진짜 충돌이면 두 주장 모두 날짜/source와 함께 명시
3. Frontmatter에 `contradictions: [page-name]` 표시
4. `wiki_lint.py` 가 사용자 검토 대상으로 플래그

## 운영 가이드 (3-체크포인트)

이 wiki는 Brown Biotech Feature Factory의 일부. **3 human checkpoint** 준수:

| # | Checkpoint | 트리거 | 게이트 |
|---|---|---|---|
| 1 | **上车** | 계획/드래프트 단계 끝 | 사용자 검토 후 build 시작 |
| 2 | **Taste align** | 첫 드래프트 출력 | 스타일/톤/voice 보정 후 반복 |
| 3 | **Go/No-go** | 출시 전 | 사용자 검증 후 ship |

> 다 하자 실행 중에도 #1, #3은 절대 스킵 안 함.

## Pitfalls

- **`raw/` 절대 수정 금지** — 보정은 Layer 2 페이지에
- **세션 시작 시 orientation 필수** — SCHEMA + index + 최근 log 30줄 먼저 읽기
- **index.md / log.md 갱신 스킵 금지** — 위키가 망가지는 주 원인
- **단순 언급에 페이지 만들지 말 것** — 임계값 엄수
- **교차참조 없는 페이지 만들지 말 것** — 고아 페이지 = 보이지 않는 페이지
- **Frontmatter 필수** — search/filter/staleness 추적의 기반
- **태그는 분류에서만** — 새 태그가 필요하면 SCHEMA.md 먼저 갱신
- **200줄 이내로 유지** — 분할 권장
- **10+ 기존 페이지 mass-update 전 확인**
- **log.md 500 entry 도달 시 회전** — `log-YYYY.md`로 rename
- **충돌은 명시적으로** — silently 덮어쓰지 말 것
