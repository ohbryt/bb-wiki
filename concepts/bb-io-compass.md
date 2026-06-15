---
title: BB-IO Compass — Clinical Genomics Decision-Support Test
created: 2026-06-15
updated: 2026-06-15
type: concept
tags: ["cancer", "biomarker", "dx", "clinical", "ai"]
sources:
  - 2026-06-15-keap1-nrf2-io-biomarker-companion-diagnostic  (sister query — full evidence base)
  - 2026-06-15-keap1-nrf2-metabolic-vulnerabilities  (sister query — mechanism)
  - https://pubmed.ncbi.nlm.nih.gov/39385035  (Skoulidis Nature 2024 POSEIDON)
  - https://pubmed.ncbi.nlm.nih.gov/36775193  (Alessi JTO 2023 1,285-pt validation)
  - https://pubmed.ncbi.nlm.nih.gov/40645185  (Galan-Cobo Cancer Cell 2025 HUDSON)
  - bb-io-compass-operations  (sibling — LIMS, validation, CLIA/CAP, revenue)
contradictions: []
---

# BB-IO Compass — Clinical Genomics Decision-Support Test

## 한 줄 정의
**BB-IO Compass** = NGS panel + PD-L1 IHC + TMB의 통합 companion-diagnostic 테스트. NSCLC 1st-line 면역항암제 regimen selection의 임상 의사결정 지원. Tier 1 (1st-line) → Tier 2 (alternative) → Tier 3 (acquired resistance) 의 3-tier 구조.

> **현재 작업 범위:** **Tier 1** 만. Tier 2/3는 12-18개월 / 24-36개월 로드맵.
> **구현 상세** (LIMS, validation plan, CLIA/CAP, revenue): → `[[bb-io-compass-operations]]`

---

## Tier 구조 (3-tier roadmap)

| Tier | Indication | Panel | Clinical decision | Time-to-report |
|---|---|---|---|---|
| **Tier 1** | 1st-line CIT eligibility, advanced NSCLC | **STK11 + KEAP1 + SMARCA4** NGS + PD-L1 IHC (22C3) + TMB | CIT 적합 여부 → 적합 시 표준 CIT, 부적합 시 Tier 2 또는 alternative regimen | 7-10 days |
| **Tier 2** | Tier 1 부적합 환자; alternative regimen selection | Tier 1 + **LKB1/KEAP1/KRAS triple + EMSY IHC + MTAP IHC** | Dual ICB (POSEIDON), ATRi + PD-L1 (HUDSON), PARP + STING, PRMT5i | 14-21 days |
| **Tier 3** | Acquired IO resistance at progression | Re-biopsy NGS panel: STK11, B2M, APC, MTOR, KEAP1, JAK1/2 + mIF TME + HLA-I | Switch to Tier 2 combo based on acquired mutation | 14-21 days |

---

## Tier 1 — Clinical Decision Matrix

| Patient profile | PD-L1 TPS | TMB | STK11 / KEAP1 / SMARCA4 | **BB-IO Compass output** |
|---|---|---|---|---|
| PD-L1 ≥50%, TMB-high, 3-gene WT | high | high | WT | **Standard CIT (pembrolizumab + chemo)** |
| PD-L1 1-49%, TMB-intermediate | intermediate | intermediate | WT | **CIT** (continued) |
| PD-L1 <1% or TMB-low, 3-gene WT | low | low | WT | **CIT + consider CIT intensification** |
| Any PD-L1, **STK11 or KEAP1 or SMARCA4 mutated** | any | any | MUT | **Refer to Tier 2** — POSEIDON dual ICB or ATRi combo |
| PD-L1 ≥50% + STK11/KEAP1 co-mut | high | any | MUT | **Skip single-agent pembrolizumab** — recommend CIT or Tier 2 |
| PD-L1 <1% + KEAP1 MUT | low | any | MUT | **Strong Tier 2 referral** (POSEIDON subset signal) |

> **Validation evidence:** Alessi JTO 2023 (1,285-pt multicenter, STK11/KEAP1/SMARCA4 WT = best CIT outcomes) + Skoulidis Nature 2024 (POSEIDON, STK11/KEAP1 → dual ICB benefit).

---

## Cross-references

- `[[bb-io-compass-operations]]` — **implementation spec** (LIMS, validation, CLIA/CAP, revenue, milestones)
- [[2026-06-15-keap1-nrf2-io-biomarker-companion-diagnostic]] — **evidence base** (8 BB-actionable angles)
- [[2026-06-15-keap1-nrf2-metabolic-vulnerabilities]] — **mechanism base** (6 angles, KEAP1 druggable axes)
- [[timesfm]] — TMB trajectory forecasting over treatment lines (XReg covariates: line, regimen, response)
- [[scgpt_deep_analysis]] — TME immunophenotyping (Tier 3) + tumor subpop identification
- [[ai-drug-discovery]] — Tier 2 combo screening (PRMT5i, PARPi, STING agonist)
- Sister genox-site (Korean consumer genomics) — different product (B2C longevity); BB-IO Compass is B2B clinical — **두 라인을 분리 운영**

---

## 4-섹션 판단 레이어

### 1. Source Quotes
- Skoulidis F et al. _Nature_ 2024 (PMID 39385035): _"loss of Keap1 was the strongest genomic predictor of dual ICB efficacy — confirmed in several mouse models of Kras-driven NSCLC"_
- Alessi JV et al. _J Thorac Oncol_ 2023 (PMID 36775193, 1,285 pts): _"the presence of an STK11, KEAP1, or SMARCA4 mutation was associated with significantly worse ORR, mPFS, and mOS to CIT"_
- Galan-Cobo A et al. _Cancer Cell_ 2025 (PMID 40645185): _"LKB1/KEAP1-deficient NSCLC patients demonstrate enhanced benefits to the ATRi ceralasertib plus durvalumab"_
- Ricciuti B et al. _J Clin Oncol_ 2024 (PMID 38207230): _"acquired loss-of-function mutations in STK11, B2M, APC, MTOR, KEAP1, and JAK1/2"_
- CMS CLIA '88 + CAP Molecular Pathology checklist (regulatory framework)

### 2. My Interpretation
- **2024-2025 의 KEAP1 biomarker literature inflection** (POSEIDON, HUDSON, 1,285-pt CIT, JCO acquired resistance) 가 Tier 1 제품의 market timing 을 결정 — 지금 안 하면 Foundation Medicine / Tempus / Caris 가 18개월 안에 비슷한 패널 FDA 승인.
- **3-gene exclusion panel 의 simplicity 가 강점** — 5개 biomarker (3 NGS + PD-L1 + TMB) 만으로 명확한 decision tree. FoundationOne CDx 의 300+ gene 대비 **focused, fast (<10 day), cheap ($1K)** positioning.
- **LDT-first 전략** — PMA 5-7년, 510(k) 2-3년, LDT 6-12개월. Foundation Medicine 가 2011 년 같은 경로로 FoundationOne launch → 후속 PMA.
- **Revenue 의 핵심 driver 는 pharma partnership** — 9 actionable drug target (q#1 6 + q#2 4) 의 combo clinical trial 에 BB-IO Compass 가 **stratification biomarker** → per-test royalty + co-development funding.
- **BB 의 경쟁 우위** — 14 query family × ARP v27 drug discovery stack 과의 통합. Foundation Medicine 은 "diagnostic only"지만 BB 는 "diagnostic + drug discovery feedback loop" — Tier 2 의 alternative regimen 후보 약물을 ARP v27 stack 으로 동시 진행.

### 3. Open Questions
- ⭐ CLIA lab 의 physical location — Seoul vs US (Boston/SD) vs 둘 다?
- ⭐ iChroGene partnership 의 clinical Dx 확장 — consumer → clinical upgrade 의향?
- ⭐ CMS MolDx 의 coverage decision — Z-code (Palmetto) or unique test ID 필요
- ⭐ TMB panel size 의 trade-off — 1.5 Mb (Tier 1) vs 3 Mb (Tier 1 + context) → FoundationOne CDx 비교 검증
- ⭐ Pharma partnership 의 first target — AZN (POSEIDON) vs Merck (pembrolizumab CIT) vs BMS (nivolumab) — 가장 IO-mutated 환자 많은 regimen 의 sponsor
- `[[comparisons/bb-io-compass-vs-foundation-one]]` — competitive landscape (deferred)
- `[[entities/clia-cap-accreditation-process]]` — regulatory entity (deferred)
- [[bb-io-compass-operations]] 의 Open Questions 참조 (구현 단계)

### 4. Contradictions
- **KEAP1/STK11 = "negative prognostic" (2018-2022) vs "predictive positive for dual ICB" (Skoulidis 2024)** — regimen-specific reframing. BB-IO Compass output 은 "mutated = bad" 가 아니라 "mutated = refer to Tier 2 testing" — 이게 제품의 가치.
- **PD-L1 IHC 단독의 stratification 한계** — Alessi 2023 의 STK11/KEAP1/SMARCA4 mutation 은 PD-L1 TPS 와 independent prognostic factor. **PD-L1 만으로는 부족** — 3-gene panel 이 더해주는 정보.
- **TMB 의 standardization** — FoundationOne CDx vs F1CDx (FMI) vs in-house pipeline 상이. BB Tier 1 의 TMB 는 in-house → FoundationOne concordance validation 이 **first 50-pt comparison** 의 critical step.
- **NGS panel 의 3-gene focused vs comprehensive** — FoundationOne 300+ gene vs BB Tier 1 3 gene + hotspot. trade-off: 빠르고 cheap 하지만 BRCA1/2, HRD, MSI 등 다른 actionable biomarker 놓침 → Tier 2 에서 comprehensive 확장.
- **Tissue scarcity** — NSCLC FFPE 양이 제한적. Tier 1 (3 gene + IHC) 이 comprehensive panel 보다 sample-efficient — advantage.

---

**Status:** First-pass product spec. 2026-06-15. Tier 1 only — Tier 2/3 are roadmap.
**Path to launch:** LDT under CLIA + CAP, MVP 12 months, revenue Year 1 $0.5-1M, Year 3 $3-5M.
**Strategic value:** First Brown Biotech **clinical product** (vs research services). Direct path to pharma partnership + 9 actionable drug target validation cohort.
**Saved in:** `/Users/ocm/openclaw/workspace/bb-wiki/concepts/bb-io-compass.md` + `[[bb-io-compass-operations]]`
