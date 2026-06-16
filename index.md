---
title: Wiki Index
created: 2026-06-14
updated: 2026-06-14
type: index
tags: [meta]
---

# Brown Biotech Wiki Index

> 페이지 카탈로그. 섹션별로 정리. 50개 초과 시 sub-section 분리, 200개 초과 시 `_meta/topic-map.md` 작성.
> Last updated: 2026-06-15 | Total pages: 17 (PoC 3 + ingest 12 + query 2)

## Concepts

> 개념/메커니즘/경로. Brown Biotech 도메인의 중추 주제.

### ✍️ Curated (hand-written, judgment complete)

- [[oxphos-cancer-vulnerability]] — OXPHOS 의존성 + 암 세포 미토콘드리아 취약성
- [[livia_deep_analysis]] — LIVIA browser-based PPI tool (Kim & Perrimon 2026, client-side)

### 📥 Ingested (template 4-섹션, judgment pending)

- [[aurora_deep_analysis]] — AURORA cross-modality AI for longevity (Chen et al. 2026)
- [[scgpt_deep_analysis]] — scGPT foundation model for single-cell biology
- [[timesfm]] — TimesFM 2.5 time-series foundation model (Google Research, ICML 2024) — **temporal axis FM**
- [[research-paper-format-gwas-first]] — **GWAS-first 5-stage arc** (Spears et al. JCI 2026, SLC7A2) — clinical anchor → regulatory overlay → conservation → causal → mechanism + drug anchor. **BB Paid Brief 표준 template의 source**

### ✍️ Curated (hand-written, judgment complete)
- [[bb-io-compass]] — **product** — BB-IO Compass Tier 1 clinical genomics decision-support test (STK11/KEAP1/SMARCA4 + PD-L1 + TMB) for NSCLC 1st-line CIT. LDT under CLIA + CAP, 12-month MVP. **First BB clinical product**
- [[bb-io-compass-operations]] — **product sibling** — LIMS workflow, analytical & clinical validation, CLIA/CAP pathway, revenue model, 18-month milestones
- [[mash_review_deep_integration]] — MASH/MASLD review integration
- [[tpp_dgat1_conjugate_research_plan]] — TPP/DGAT1 conjugate research plan
- [[turbovec_turboquant_analysis]] — turbovec vector index (Codrai 2026)
- [[agentic_patterns_brownbiotech_mapping]] — Agentic design patterns × BB coverage
- [[claw_ai_lab_brief]] — Claw AI Lab 5-layer pyramid (Wu et al. 2026)
- [[ssr_likert_syntheticconsumers_deep_analysis]] — SSR / synthetic consumer validation

## Entities

> 인물/기관/저널/화합물/타깃/데이터셋.

- [[naaa-chembl2419814]] — NAAA lead compound (CHEMBL2419814, −13.0 kcal/mol)

## Comparisons

> 양대비 분석. "A vs B" 형태.

- [[naaa-vs-mgll-inhibitors]] — NAAA vs MGLL (endocannabinoid-degrading enzymes)
- [[arp27_vs_claw_ai_lab_analysis]] — ARP v27 (BB) vs Claw AI Lab — drug discovery AI 비교

## Queries

> 에세이급 답변. 재사용 가치가 있는 종합 분석 결과.

- [[2026-06-15-keap1-nrf2-metabolic-vulnerabilities]] — KEAP1-NRF2 metabolic vulnerabilities in NSCLC, 6 BB-actionable angles (PPIA/CsA, SHMT, GCLC, HMOX1, p62, NADH-reductive)
- [[2026-06-15-keap1-nrf2-io-biomarker-companion-diagnostic]] — **sister query** — KEAP1-NRF2 IO biomarker & companion diagnostic, 8 BB-actionable angles (POSEIDON dual ICB, MTAP-PRMT5, EMSY-PARP, ATRi-LKB1, 3-gene exclusion, glutaminase rescue) — **3-tier "BB-IO Compass" diagnostic product candidate**

---

## 🗂️ 도메인별 빠른 이동

| 도메인 | 태그 | 페이지 수 |
|---|---|---|
| Drug Discovery (NAAA) | `#naaa` | 2 |
| Mitochondrial / OXPHOS | `#oxphos` | 1 |
| AI/ML methods | `#ai` | 6 |
| MASH / MASLD | `#mash` | 1 |
| Refractory cancer | `#cancer` | 2 (KEAP1 query × 2) |
| **Clinical Dx (new)** | `#dx`, `#biomarker` | **2** (BB-IO Compass product spec) |
| Peptide | `#peptide` | 0 |
| IPF / Fibrosis | `#ipf`, `#fibrosis` | 0 |
| Sarcopenia / Aging Muscle | `#sarcopenia` | 0 |
| Senescence | `#senescence` | 0 |
| Cosmetics | `#cosmetics` | 0 |
| Biostat | `#biostat` | 0 |
| Longevity (cross-cutting) | `#longevity` | 0 |

## 📌 Onboarding

- 처음 왔다면: `README.md` → `SCHEMA.md` → 최근 `log.md` 30줄 → 도메인 페이지 순으로 읽기
- 새 source (논문/PDF/URL) 받았을 때: `python3 scripts/ingest_deep_dive.py <path> --type <concept|entity|comparison>`
- 위키 상태 점검: `python3 scripts/wiki_lint.py`
- 4-섹션 판단 레이어 채우기: 각 ingested page 의 4개 placeholder 직접 작성 (사용자 몫)

## 📊 Coverage (2026-06-14)

- **Curated pages (4-섹션 완전):** 3
- **Ingested pages (4-섹션 placeholder):** 10
- **Wikilink 2+ outbound:** 5 (3 curated + 2 hand-filled samples)
- **Pages needing wikilink (orphan):** 8 (Dr. OCM 채우기 대상)
- **Pages >200 lines (split 후보):** 5
- **Tags in SCHEMA taxonomy:** 32 (18 도메인 + 14 sub-domain)
