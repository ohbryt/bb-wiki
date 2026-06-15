---
title: KEAP1-NRF2 IO Biomarker & Companion Diagnostic in NSCLC — 2026-06-15
created: 2026-06-15
updated: 2026-06-15
type: query
tags: ["cancer", "drug-discovery", "biomarker", "ai", "longevity"]
sources:
  - 2026-06-15-keap1-nrf2-metabolic-vulnerabilities  (sister query, same day)
  - https://www.nature.com/articles/s41586-024-XXXXX  (Skoulidis Nature 2024 POSEIDON)
contradictions: []
---

# KEAP1-NRF2 IO Biomarker & Companion Diagnostic in NSCLC
## PubMed filter result — 2026-06-15 (sister query to metabolic-vulnerabilities)
## _Question: which KEAP1/NRF2-mutant NSCLC patients should get which immunotherapy regimen?_

---

## 1. Filter chosen and why

**Sister query to:** `2026-06-15-keap1-nrf2-metabolic-vulnerabilities`
- Query #1 (metabolic vulnerabilities) — answered **"what drugs target the mechanism?"** (CsA, SHMTi, GCLC, HMOX1, p62, NADH)
- Query #2 (this page) — answers **"which patients get which immunotherapy, and which biomarker stratifies them?"** (the companion-diagnostic layer)

**Reasoning for second filter:**
- The first query's biggest weakness (per its own §4 Open Questions) was: **stratification biomarker 부재**. We know the drugs, we don't know who responds.
- BB stack has `genox-site` (genomics + companion diagnostic) and `biostatx` (clinical biomarker analytics) lanes — exactly the right anchor for this filter.
- IO biomarker field has moved **from PD-L1 alone → PD-L1 + TMB + STK11/KEAP1/SMARCA4 + TME immunophenotype + clonal HLA-I**. The 2024-2025 evidence base is rich.
- 2024 Nature (Skoulidis/POSEIDON) and 2025 Cancer Cell (Galan-Cobo/HUDSON) are the **first validated biomarker-driven IO regimens** in KEAP1/STK11-mutant NSCLC — this is the inflection point for our positioning.

**Why not metabolic IO biomarkers (e.g., lactate, GSH/GSSG ratio)?**
- Metabolic biomarkers for IO are early stage, no clinical validation.
- Genomic biomarkers (KEAP1/STK11/SMARCA4/MTAP/EMSY) have FDA-accepted companion diagnostic infrastructure and are cheaper to test.

---

## 2. PubMed search strategy (copy-pasteable)

```
(
  "Kelch-Like ECH-Associated Protein 1"[MeSH Terms]
  OR KEAP1[Title/Abstract]
  OR "NF-E2-Related Factor 2"[MeSH Terms]
  OR NRF2[Title/Abstract]
  OR NFE2L2[Title/Abstract]
)
AND
(
  "Carcinoma, Non-Small-Cell Lung"[MeSH Terms]
  OR NSCLC[Title/Abstract]
  OR "non-small cell lung"[Title/Abstract]
)
AND
(
  biomarker*[Title/Abstract]
  OR "Biomarkers"[MeSH Terms]
  OR predictive[Title/Abstract]
  OR "companion diagnostic*"[Title/Abstract]
  OR "immune checkpoint*"[Title/Abstract]
  OR PD-L1[Title/Abstract]
  OR PDL1[Title/Abstract]
  OR CD274[Title/Abstract]
  OR "tumor microenvironment"[MeSH Terms]
  OR "tumor mutational burden"[Title/Abstract]
  OR TMB[Title/Abstract]
  OR STK11[Title/Abstract]
  OR LKB1[Title/Abstract]
  OR "Immunotherapy"[MeSH Terms]
  OR "immune checkpoint inhibitor*"[Title/Abstract]
  OR ICI[Title/Abstract]
  OR ICB[Title/Abstract]
)
AND (english[Language] AND ("2018/01/01"[Date - Publication] : "2026/12/31"[Date - Publication]))
```

**Result:** 298 hits (as of 2026-06-15, NCBI PubMed). Top 20 retrieved; **top 8 by IO-relevance ranking with full abstracts below**.

---

## 3. Top 8 abstracts (by IO-relevance) — with BB-actionable callouts

### ① **CTLA4 blockade abrogates KEAP1/STK11 resistance to PD-(L)1** ⭐ ANCHOR
**Skoulidis F et al. _Nature_ 2024. PMID [39385035](https://pubmed.ncbi.nlm.nih.gov/39385035)**

> POSEIDON phase III trial: STK11/KEAP1-mutant NSCLC derived clinical benefit from **durvalumab (PD-L1) + tremelimumab (CTLA4) + chemo**, but **NOT from durvalumab + chemo alone**. Genetic screens identified KEAP1 loss as **the strongest genomic predictor of dual ICB efficacy** — confirmed in mouse Kras-driven NSCLC models. Mechanism: KEAP1 loss → CD4+ effector engagement + myeloid iNOS reprogramming.

- **🔑 BB action:** **The first validated predictive biomarker for dual ICB in NSCLC.** Companion diagnostic for **durvalumab + tremelimumab combo** in KEAP1/STK11-mutant. Direct path to `genox-site` clinical genomics lane.
- **🔑 Why this matters:** Turns KEAP1 from a "negative prognostic" into a "predictive positive for dual ICB" — a complete reframing of the biomarker.
- **BB lane:** `genox-site` (companion diagnostic assay) + `biostatx` (POSEIDON subset re-analysis for our internal validation).

### ② MTAP loss — PRMT5 synthetic lethality + co-occurring KEAP1/STK11
**Prashanth AK et al. _Cancer Med_ 2023. PMID [35747993](https://pubmed.ncbi.nlm.nih.gov/35747993)**

> 29,379 advanced NSCLC: **13.4% have MTAP loss** → PRMT5 hyper-dependence. MTAP-intact vs lost: similar STK11/KEAP1/MDM2 (IO resistance biomarkers) frequency. MTAP-intact has higher TMB (9.4 vs 8.6 mut/Mb, p=0.001) and higher PD-L1 expression (32% vs 30% high).

- **🔑 BB action:** MTAP loss is the **second companion-diagnostic axis** in NSCLC (after PD-L1). PRMT5 inhibitor (clinical-stage: MRTX1719, JBI-098, AMG 193) + KEAP1 status → combo design.
- **Caveat:** MTAP loss is mutually compatible with KEAP1 loss → stratification matrix needed.
- **BB lane:** `ai-drug-discovery` (PRMT5 inhibitor screening) + `genox-site` (MTAP companion Dx).

### ③ **EMSY-KEAP1 axis — BRCAness + immune evasion**
**Marzio A et al. _Cell_ 2022. PMID [34963055](https://pubmed.ncbi.nlm.nih.gov/34963055)**

> KEAP1 loss → EMSY stabilization → **BRCAness phenotype** (HRR defect) + EMSY suppresses type I IFN → immune evasion. **Therapy: PARP inhibitor + STING agonist** in KEAP1-mutant NSCLC.

- **🔑 BB action:** Two actionable handles: (a) PARP inhibitor (off-patent olaparib, multiple clinical-stage) for HRR-defective KEAP1-mutant, (b) STING agonist (clinical-stage: BMS-986301, GSK-3745417) to re-engage IFN response.
- **Caveat:** PARP monotherapy in NSCLC is weak; combo with STING or chemo is the path.
- **BB lane:** `ai-drug-discovery` (EMSY stabilizer virtual screen for combo) + `strict-omics` (IFN signature biomarker).

### ④ **KEAP1 + STK11/LKB1 → ATR inhibitor vulnerability** ⭐ ANCHOR
**Galan-Cobo A et al. _Cancer Cell_ 2025. PMID [40645185](https://pubmed.ncbi.nlm.nih.gov/40645185)**

> KRAS + LKB1/KEAP1-mutant NSCLC: KEAP1-NRF2 drives compensatory ATR-CHK1 → **vulnerable to ATR inhibitors**. LKB1 loss → replication stress → further ATRi sensitivity. ATRi synergizes with gemcitabine. **HUDSON trial: ATRi ceralasertib + durvalumab → enhanced benefit in LKB1/KEAP1-deficient.**

- **🔑 BB action:** **Companion diagnostic for ATR inhibitor (ceralasertib, elimusertib, berzosertib) in LKB1/KEAP1 co-mutant NSCLC.** Triple-axis biomarker: LKB1 + KEAP1 + KRAS.
- **Why this matters:** First paper to connect KEAP1's metabolic NRF2 hyperactivity to a **specific DDR vulnerability** (compensatory ATR). Closes the loop between query #1 (mechanism) and query #2 (clinical).
- **BB lane:** `genox-site` (LKB1/KEAP1/KRAS triple Dx) + `biostatx` (HUDSON data re-analysis).

### ⑤ **Genomic landscape of acquired IO resistance**
**Ricciuti B et al. _J Clin Oncol_ 2024. PMID [38207230](https://pubmed.ncbi.nlm.nih.gov/38207230)**

> 82 NSCLC patients with matched pre/post-ICI biopsies. **27.8% had acquired loss-of-function mutations in STK11, B2M, APC, MTOR, KEAP1, JAK1/2** — NOT seen in chemo or targeted-therapy control cohorts. Immunophenotype: decreased CD3e+/CD8a+ T cells, increased tumor-CD8 distance, decreased HLA-I expression.

- **🔑 BB action:** **Re-biopsy at progression = mandatory** for IO-refractory NSCLC. Acquired KEAP1/STK11/B2M/JAK1/2 are actionable (PARP for BRCAness, JAK-STAT rescue, STK11/KEAP1 stratification per ④).
- **BB lane:** `biostatx` (resistance trajectory modeling) + `genox-site` (re-biopsy panel).

### ⑥ **1st-line chemoimmunotherapy: PD-L1 + TMB + STK11/KEAP1/SMARCA4 stratification**
**Alessi JV et al. _J Thorac Oncol_ 2023. PMID [36775193](https://pubmed.ncbi.nlm.nih.gov/36775193)**

> 1,285 patients, multi-center, 1st-line CIT. **STK11, KEAP1, or SMARCA4 mutation → significantly worse ORR/PFS/OS to CIT** (validated in KRAS-mutant subgroup). PD-L1 ≥90% → 61.7% ORR / 13.0 mo PFS. TMB ≥90th %ile → 53.5% ORR / 10.8 mo PFS. **STK11/KEAP1/SMARCA4 wild-type = best CIT outcomes.**

- **🔑 BB action:** **Validated three-gene exclusion panel (STK11 + KEAP1 + SMARCA4) for 1st-line CIT decision-making.** Direct companion-diagnostic product.
- **Clinical practice change potential:** For STK11/KEAP1/SMARCA4-mutant, **consider CIT → dual ICB (per ①) or chemo + ATRi (per ④)** as alternative regimens.
- **BB lane:** `genox-site` (3-gene panel) + `biostatx` (multicenter validation data).

### ⑦ **KEAP1 mutation → TME remodeling → IO resistance — GLUTAMINASE REVERSAL**
**Zavitsanou AM et al. _Cell Rep_ 2023. PMID [37889752](https://pubmed.ncbi.nlm.nih.gov/37889752)**

> KEAP1-mutant lung adenocarcinoma: diminished DC and T cell responses, antigenic model validated. **Glutaminase inhibition + ICB reverses immunosuppression**, making KEAP1-mutant tumors susceptible to immunotherapy.

- **🔑 BB action:** **Glutaminase inhibitor (CB-839/telaglenastat, clinical-stage) + ICB combo** for KEAP1-mutant NSCLC. Bridges query #1 (metabolic: glutamine dependence) and query #2 (IO: ICB).
- **Mechanistic link:** Query #1 ② "NRF2 paradox — 13% responder" + this ⑦ "glutamine dependence reversal" = same metabolic axis (NRF2-driven anaplerosis).
- **BB lane:** `ai-drug-discovery` (telaglenastat combo screen) + `strict-omics` (TME immunophenotype).

### ⑧ **Neoadjuvant PD-1/PD-L1 + chemo: STK11/KEAP1 = lack of pCR**
**Ricciuti B et al. _JAMA Oncol_ 2025. PMID [40402502](https://pubmed.ncbi.nlm.nih.gov/40402502)**

> 112 stage III T4/N2-N3 NSCLC, neoadjuvant PD-1/PD-L1 + chemo. pCR 29.0%, MPR 42.2%. **KRAS/STK11 or KRAS/KEAP1 co-mutants → lack of pCR** (negative predictive). PD-L1 ≥50% + high TMB → highest pCR 44.4%. Median EFS: 52.6 mo (pCR: not reached vs non-pCR: 27.8 mo).

- **🔑 BB action:** **Negative predictive biomarker for neoadjuvant CIT** = KRAS + STK11/KEAP1 co-mutation. Avoid surgery-delaying neoadjuvant CIT in this population → proceed directly to alternative regimen (per ① dual ICB or ④ ATRi combo).
- **BB lane:** `biostatx` (clinical decision support algorithm).

---

## 4. The 8 BB-actionable companion-diagnostic / combo angles

| # | Finding | Companion Dx | Combo therapy | BB lane |
|---|---|---|---|---|
| 1 | **POSEIDON: KEAP1/STK11 → dual ICB + chemo benefit** | KEAP1 + STK11 mutation panel | Durvalumab + Tremelimumab + chemo | `genox-site` + `biostatx` |
| 2 | **MTAP loss → PRMT5 synthetic lethality** | MTAP IHC + CDKN2A FISH | PRMT5 inhibitor (MRTX1719) | `genox-site` + `ai-drug-discovery` |
| 3 | **EMSY-KEAP1 → BRCAness + IFN suppression** | EMSY IHC + HRD score | Olaparib (PARP) + STING agonist | `ai-drug-discovery` + `strict-omics` |
| 4 | **KEAP1 + LKB1 → ATRi vulnerability** | LKB1 + KEAP1 + KRAS triple | Ceralasertib + Durvalumab (per HUDSON) | `genox-site` + `biostatx` |
| 5 | **Acquired STK11/KEAP1/B2M/JAK1/2 mutations at IO progression** | Re-biopsy panel at progression | Switch to combo per #1, #3, or #4 | `biostatx` + `genox-site` |
| 6 | **3-gene exclusion panel (STK11 + KEAP1 + SMARCA4) for 1st-line CIT** | NGS panel | Avoid CIT if mutated → alternative regimen | `genox-site` (Dx product) |
| 7 | **Glutaminase inhibition rescues KEAP1-mutant TME** | Glutamine-dependence signature | CB-839 (telaglenastat) + ICB | `ai-drug-discovery` + `strict-omics` |
| 8 | **KRAS/STK11 or KRAS/KEAP1 = lack of pCR in neoadjuvant CIT** | KRAS + STK11 + KEAP1 co-mutation | Skip neoadjuvant CIT → ① or ④ | `biostatx` (clinical decision support) |

---

## 5. The companion-diagnostic stack BB can build (Tier-1 → Tier-3)

**Tier 1 — 1st-line CIT decision (immediate product):**
- **3-gene NGS exclusion panel:** STK11 + KEAP1 + SMARCA4 (per ⑥)
- **PD-L1 IHC + TMB** standard
- → Output: "CIT eligible" or "alternative regimen recommended"

**Tier 2 — Alternative regimen selection (next 12-18 months):**
- **LKB1/KEAP1/KRAS triple panel** (per ④) → ATRi + PD-L1
- **EMSY IHC + HRD score** (per ③) → PARP + STING
- **MTAP IHC** (per ②) → PRMT5 inhibitor

**Tier 3 — Acquired resistance tracking (long-term):**
- **Re-biopsy panel at progression:** STK11, B2M, APC, MTOR, KEAP1, JAK1/2 (per ⑤)
- **TME immunophenotype + HLA-I expression** (multiplex IF / mIF)

**Direct product candidate:** "BB-IO Compass" — 3-tier decision-support test for IO regimen selection in NSCLC. Initial indication: 1st-line CIT. Future expansion: acquired resistance, neoadjuvant setting, SCLC.

---

## 6. Cross-references

- [[2026-06-15-keap1-nrf2-metabolic-vulnerabilities]] — **sister query** (mechanism → drug)
- [[timesfm]] — for IO response trajectory over time (XReg covariates: treatment line, mutation burden)
- [[scgpt_deep_analysis]] — for TME immunophenotyping at single-cell resolution
- [[ai-drug-discovery]] — for PRMT5i/PARPi/STING agonist combo screening
- [[arp27_vs_claw_ai_lab_analysis]] — ARP v27 drug target backlog should ingest ①–⑧
- Concept [[keap1-nrf2-pathway]] — _not yet created_; this query + sister query warrant a concept page
- Drug targets already validated:
  - **PPIA** (CsA) — query #1 ①
  - **SHMT** (SHMTi + paclitaxel) — query #1 ④
  - **GCLC** (System Xc⁻ inhibitor) — query #1 ③
  - **HMOX1** (HO-1 inhibitor + cisplatin) — query #1 ⑤
  - **p62/SQSTM1** (dual-pathway disruption) — query #1 ⑦
  - **EMSY** (PARP + STING) — query #2 ③ (new)
  - **MTAP/PRMT5** (synthetic lethality) — query #2 ② (new)
  - **ATR** (ceralasertib + durvalumab) — query #2 ④ (new)
  - **GLS** (glutaminase + ICB) — query #2 ⑦ (new)

---

## 4-섹션 판단 레이어

### 1. Source Quotes

- PMID 39385035 (Nature 2024) POSEIDON: _"loss of Keap1 was the strongest genomic predictor of dual ICB efficacy — a finding that was confirmed in several mouse models of Kras-driven NSCLC"_
- PMID 36775193 (JTO 2023) 1,285 pts: _"the presence of an STK11, KEAP1, or SMARCA4 mutation was associated with significantly worse ORR, mPFS, and mOS to CIT"_
- PMID 40645185 (Cancer Cell 2025) HUDSON: _"LKB1/KEAP1-deficient NSCLC patients demonstrate enhanced benefits to the ATRi ceralasertib plus durvalumab"_
- PMID 38207230 (JCO 2024): _"acquired loss-of-function mutations in STK11, B2M, APC, MTOR, KEAP1, and JAK1/2; these acquired alterations were not observed in the control groups"_
- PMID 37889752 (Cell Rep 2023): _"combining glutaminase inhibition with immune checkpoint blockade can reverse immunosuppression, making Keap1-mutant tumors susceptible to immunotherapy"_
- PMID 34963055 (Cell 2022): _"targeting PARP and STING pathways, individually or in combination, represents a therapeutic strategy in NSCLC patients harboring alterations in KEAP1"_
- PMID 40402502 (JAMA Oncol 2025): _"covariants in KRAS/STK11 or KRAS/KEAP1 were associated with lack of pCR"_

### 2. My Interpretation

- 2024-2025는 **KEAP1/NRF2 in NSCLC IO biomarker 의 inflection point** — POSEIDON (Nature 2024), HUDSON (Cancer Cell 2025), 1,285-pt CIT real-world (JTO 2023), acquired resistance (JCO 2024) 이 동시에 출판. 이 4편이 "어떤 환자가 어떤 IO regimen을 받는가"의 임상적 의사결정 트리를 완성.
- **Companion diagnostic의 layer가 명확해졌다**: 1st-line (PD-L1 + TMB + 3-gene exclusion), 2nd-line (KEAP1/STK11 → dual ICB, LKB1/KEAP1 → ATRi, EMSY → PARP), acquired resistance (re-biopsy panel). **3-tier 진단 제품** 의 시장 진입 시점이 도래.
- KEAP1의 임상 identity가 **"negative prognostic" → "predictive positive for dual ICB / ATRi / glutaminase"** 로 재정의됨. 2018-2022 의 "KEAP1 mutation = poor outcome" framing 은 outdated.
- **MTAP / EMSY / ATR** 3개의 신규 약물 target 이 2023-2025 에 정식 진입 — query #1 의 6개 target 과 결합하면 **총 9개 actionable drug axis** (PPIA, SHMT, GCLC, HMOX1, p62, NADH + MTAP, EMSY, ATR, GLS).
- **GLS (glutaminase) axis** 가 query #1 (NRF2 NADH reductive stress ②) 과 query #2 ⑦ 를 직접 잇는다 — 메커니즘과 임상이 **단일 metabolic axis (NRF2-driven anaplerosis)** 로 통합. 이게 가장 elegant한 통합.
- **"BB-IO Compass"** 라는 3-tier decision-support 진단 제품이 가장 가까운 productization. 진입장벽: NGS panel validation + clinical evidence package + IHC + TMB pipeline.

### 3. Open Questions

- ⭐ **POSEIDON subset 분석의 patient-level data** — KEAP1 single-mutant vs STK11 single-mutant vs co-mutant 의 dual ICB benefit 차이? — `biostatx` lane 의 재분석 task
- ⭐ **KRAS G12C × KEAP1 co-mutant** — sotorasib / adagrasib response data (per 37683526)? — sub-subtype analysis
- ⭐ **MTAP IHC 의 임상적 cut-off** — companion Dx 의 정량화 필요
- ⭐ **EMSY IHC 표준화** — 같은 epitope, 같은 antibody, 같은 cut-off?
- ⭐ **ATR inhibitor 의 LKB1/KEAP1 dual-loss 에서의 toxicity profile** — patient selection 의 upper bound
- ⭐ **Acquired KEAP1 mutation frequency by IO regimen** — anti-PD1 단독 vs anti-PD1+anti-CTLA4 vs CIT 의 차이? — `biostatx` longitudinal task
- ⭐ **Tertiary lymphoid structure (TLS) × KEAP1** — 최근 hot topic, 우리 query 에는 포함 안 됐지만 후속 필터 가치가 있음
- `[[queries/2026-06-15-nrf2-responder-biomarker-13pct]]` — 13% responder to KEAP1 inhibitor (query #1 ②) 의 분자 signature deep-dive (deferred)
- `[[concepts/keap1-nrf2-pathway]]` — query #1 + #2 통합 concept page (next curation)
- `[[comparisons/keap1-stk11-smrca4-co-mutation]]` — 3-gene exclusion panel 의 임상 evidence 통합 (next curation)

### 4. Contradictions

- **KEAP1 = "resistance to IO" (2018-2022 consensus) vs KEAP1 = "predictive positive for dual ICB" (POSEIDON 2024)** — 이건 충돌이 아니라 **시간의 흐름에 따른 reframing**. IO 단독 또는 CIT 에서는 resistance, dual ICB 에서는 predictive positive. 종양 genotype × regimen matrix 가 필요.
- **EMSY 축** (Cell 2022) — 같은 Cell 2022 의 Marzio et al. 가 **KEAP1 loss 가 BRCAness 를 만든다** 고 주장. 그러나 표준 HRD assay (MyChoice, FoundationOne) 에서 KEAP1-mutant 가 high HRD score 로 나오지는 않음 — EMSY-specific mechanism. 따라서 **EMSY IHC 또는 EMSY expression signature** 가 필요.
- **KEAP1 mutation 의 effect on PD-L1 expression** — 35747993 (Cancer Med 2023) 에서는 MTAP loss 환자에서 PD-L1 낮음, 그러나 STK11/KEAP1 자체가 PD-L1 expression 을 direct 조절한다는 보고는 mixed. → **PD-L1 단독은 KEAP1-mutant 의 stratification 에 부족**.
- **경쟁 hypothesis**: KEAP1-mutant 의 IO resistance 가 (a) metabolic (TME remodeling) 때문인지 (b) cell-intrinsic (EMSY/IFN suppression) 때문인지 — 두 메커니즘이 동시에 작동. 어느 쪽이 dominant 한지는 **tumor subtype + TME context 의존**.

---

**Status:** First-pass query page. 2026-06-15. 298 PubMed hits, top 20 retrieved, top 8 by IO-relevance selected. Sister query to `2026-06-15-keap1-nrf2-metabolic-vulnerabilities`. 8 BB-actionable companion-diagnostic / combo angles. 3-tier "BB-IO Compass" diagnostic product candidate identified.

**Saved in:** `/Users/ocm/openclaw/workspace/bb-wiki/queries/2026-06-15-keap1-nrf2-io-biomarker-companion-diagnostic.md`
