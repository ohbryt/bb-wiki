---
title: Research Paper Format — GWAS-First 5-Stage Arc
created: 2026-06-16
updated: 2026-06-16
type: concept
tags: [concept, methodology, gwas, clinical, hypothesis]
related: [bb-io-compass, agentic_patterns_brownbiotech_mapping, livia_deep_analysis, scgpt_deep_analysis, oxphos-cancer-vulnerability]
sources: [raw/SLC7A2_Spears_JCI_2026_e173913, brown-biotech-paid-brief-gwas-first-recipe]
recipe: brown-biotech-paid-brief-gwas-first-recipe
---

# Research Paper Format — GWAS-First 5-Stage Arc

> **한 줄 요약:** "임상 anchor (GWAS) → regulatory overlay → cross-species conservation → causal perturbation → mechanism + drug anchor" 5단계로 evidence를 single narrative로 수렴시키는 translational research 포맷. Spears et al. *JCI* 2026 (SLC7A2)에서 추출, Brown Biotech Paid Brief 표준 템플릿으로 박제.

## 왜 이 포맷이 BB에 중요한가

Brown Biotech의 SoI positioning — *"데이터베이스가 아니라 추론을 판다"* — 의 가장 깔끔한 academic reference가 이 5-stage arc입니다. GWAS hit이라는 **human evidence anchor**가 1페이지 안에 들어와야, decision-maker (CEO, investor, pharma BD)가 30초 안에 "이게 사람에게도 relevant한가" 판단할 수 있습니다. Standard wet-lab 논문 (mechanism-first open)은 5–10페이지를 읽어야 임상 relevance가 보입니다 — decision friction이 너무 큽니다.

## 5-Stage Arc 정의

| # | Stage | Evidence Type | Figure 예시 |
|---|---|---|---|
| 1 | **Clinical Anchor (GWAS)** | Human genetic association, P < 10⁻⁸ | LocusZoom plot |
| 2 | **Regulatory / Functional Overlay** | ATAC-seq, ChIP-seq, eQTL, 3D chromatin | Multi-track integrative genomics viewer |
| 3 | **Cross-Species Conservation** | 2+ species expression / phenotype | Phylogenetic expression heatmap |
| 4 | **Causal Perturbation** | Genetic KO + pharmacologic + rescue (2+ orthogonal systems) | KO vs WT phenotype plots |
| 5 | **Mechanism + Drug Anchor** | Pathway diagram + existing/clinical drug | Single integrative model figure |

**핵심:** Stage 5의 single diagram이 Stage 1–4의 모든 evidence를 수렴시켜야 함. "GWAS hit = causal gene = mechanism = therapeutic node"의 1-line equation.

## Spears et al. *JCI* 2026 적용 — 단계별 매핑

| Stage | Evidence | Fig / Location |
|---|---|---|
| 1 | EXTEND 코호트 (n=7,159) HbA1c GWAS — SLC7A2 intron 1 rs142010226, rs2517232, **P < 10⁻¹⁵** | Fig 2A, p.4 |
| 2 | Pasquali 2014 ATAC + Miguel-Escalada 2019 ChIP — MAFB/FOXA2 footprint ~1 kb from SNP | Fig 2B |
| 3 | Human (GTEx + Brissova 2018), mouse (DiGruccio 2016), zebrafish (Tarifeno-Saldivia 2017) — SLC7A2 α>β 3-6x | Fig 1D–F |
| 4 | (a) Slc7a2⁻/⁻ mouse: GCGR mAb α proliferation 66%↓, (b) CRISPR zebrafish α cell # WT, (c) shRNA αTC1-6 65%↓ | Fig 3, 4, 5 |
| 5 | SLC7A2 → Arg influx → mTORC1 → SLC38A5 → α proliferation. **Drug anchor: GCGR mAb (Lilly Ab-4, Phase 1/2)** | Fig 8 (model) |

**한 figure (Fig 8)에 5 stage 전부 통합** — 이게 format의 정점.

## BB 적용 — 어디에 어떻게 쓰나

### 1. Paid Brief (₩2M–8M deliverable) — 1-page brief

5 paragraph 압축:
- ¶1: Stage 1 (clinical anchor)
- ¶2: Stage 2 (regulatory overlay)
- ¶3: Stage 3 (conservation)
- ¶4: Stage 4 (causal)
- ¶5: Stage 5 (mechanism + drug anchor + CTA)

**Length:** 1 page. **Figures:** ≤ 5. **Verification:** citation chain, read aloud, "what did I miss?"

### 2. ARP v27 target evaluation card

`brown-biotech-arp-v27-harness` 출력 카드의 5-섹션 구조. **Evidence weight ladder** (T1–T5) 명시:

| Tier | Source | Weight |
|---|---|---|
| T1 | Human GWAS P < 10⁻¹⁵, n > 100K / Phase 3 | ★★★★★ |
| T2 | Human GWAS P < 10⁻⁸ / Phase 1–2 | ★★★★ |
| T3 | Multi-species KO + rescue / functional genomics | ★★★ |
| T4 | Single-species KO / in vitro | ★★ |
| T5 | Computational prediction alone | ★ |

**T1 evidence가 Stage 1에 없으면 recipe 발동 금지** → 다른 arc 검토.

### 3. BB-IO Compass / clinical product spec

`[[bb-io-compass]]` (NSCLC CIT, Tier 1 LDT)는 본질적으로 **Stage 1 + Stage 2 + Stage 5** 의 clinical product version. POSEIDON trial data (Stage 1) + STK11/KEAP1/SMARCA4 genomic biomarker evidence (Stage 2) + clinical decision node (Stage 5). 3–4–5 stage (causal perturbation, conservation)는 clinical Dx에는 약함 — 진단이 아니라 치료 평가이므로.

### 4. SoI reasoning layer reference output

이 5-stage arc는 SoI의 **canonical output shape**. BB-IO Compass spec, Paid Brief, ARP v27 card 모두 이 형식으로 수렴 가능.

## 언제 이 포맷을 쓰면 안 되는가

### 1. T1 evidence가 없을 때

GWAS hit이 weak (P > 10⁻⁸)거나 n < 10,000 → Stage 1 부재 → 다른 arc (preclinical-first) 사용.

### 2. Cross-species evidence가 안 맞을 때

Stage 3에서 species divergence가 본질 (예: 인간 특이적 immunity, 마우스 특이적 metabolism) → conservation 단계 skip, 4-stage arc로 진행.

### 3. Drug anchor가 전혀 없을 때

Stage 5의 therapeutic integration이 비어있으면 brief가 academic paper로 회귀. Rare disease / novel pathway / non-druggable target → **biological insight** frame으로 전환, 단 diagram은 같음.

### 4. Pure method / tooling 논문

cs.AI / cs.LG / assay development / algorithm paper — GWAS anchor 자체가 없음. **대신** "benchmark-first" 또는 "method-application-first" arc 사용 (별도 페이지로 발전 가능).

---

## 4-섹션 판단 레이어

### 1. Source Quotes

> "Two single nucleotide polymorphisms (SNPs) have been identified within the first intron of SLC7A2 that are associated with hemoglobin A1c (HbA1c) levels. rs142010226 (chr 8, 17367112:A/G) and rs2517232 (chr 8, 17367421:A/G) are both strongly associated (P < 10⁻¹⁵) with HbA1c in the EXTEND human cohort, which consists of 1,395 diabetic and 5,764 non-diabetic individuals of European ancestry."
> — Spears et al., *J Clin Invest* 2026;136(12):e173913, p.4 (Results §"SLC7A2 is associated with HbA1c in humans")

> "Our work connects arginine signaling to glutamine signaling by showing Slc7a2⁻/⁻ mice lack the increased expression of the glutamine transporter, Slc38a5... when glucagon signaling is interrupted. SLC38A5 is associated with mTOR-mediated increased proliferation, which we show is SLC7A2 dependent."
> — Spears et al., 2026, p.10 (Discussion)

> "Finally, we demonstrated that Slc7a2 expression is required for the upregulation of Slc38a5 expression following interrupted glucagon signaling. Together, these studies reveal a conserved role for the arginine transporter SLC7A2 in amino acid–regulated islet cell biology."
> — Spears et al., 2026, p.2 (Introduction, hypothesis closure)

### 2. My Interpretation

이 포맷의 진짜 힘은 **순서의 inversion**입니다. 일반 translational 논문은 "in vitro hit → in vivo validation → patient sample → GWAS correlation → 임상시사점"인데, 이 논문은 **"EXTEND GWAS hit (n=7,159, P<10⁻¹⁵) → ATAC/ChIP overlay → 3 species conservation → mouse/zebrafish/cell line 3-system KO → single pathway model + GCGR mAb anchor"** 로 정반대. 1페이지 안에 "왜 사람에게 중요한가" 답합니다.

**이게 Paid Brief와 academic paper의 본질적 차이:**
- Academic paper = "what we did"
- Paid Brief = "why this matters to you (decision-maker)"

GWAS-first 5-stage arc는 **decision-maker가 30초 안에 first-pass 판단**할 수 있게 하는 format입니다. Brown Biotech가 SoI layer로 "추론을 파는" 이유와 정확히 매핑됩니다.

**Brown Biotech-specific adaptation:**
- 5 paragraph = 1 page (academic은 5–10 pages)
- Drug anchor mandatory (academic은 optional discussion)
- CTA at end (academic에는 없음)
- Evidence weight ladder 명시 (academic은 implicit)

**T1 evidence가 없는 brief는 발동하지 않는다** — 이게 가장 중요한 gate. GWAS P > 10⁻⁸, n < 10K, Phase 1 데이터 없음 → 다른 arc (preclinical-first, mechanism-first) 검토.

### 3. Open Questions

- **Q1.** Brown Biotech가 받은 페이퍼들 중 GWAS-first format을 따르는 비율은? `brown-biotech-paper-intake-workflow` skill의 Track E 결과와 교차 분석 필요. (예: scGPT는 mechanism-first open, LIVIA는 tool-first, 이 SLC7A2 페이퍼만 GWAS-first)
- **Q2.** BB-IO Compass (NSCLC CIT) 의 brief output도 이 5-stage arc로 재구성할 수 있는가? POSEIDON trial data가 Stage 1, STK11/KEAP1/SMARCA4 functional genomics가 Stage 2, KEAP1-NRF2 pathway model이 Stage 5. **실험:** bb-io-compass 페이지를 이 template으로 다시 써보고, 1-page version 만들기.
- **Q3.** Drug anchor가 없는 brief (예: novel target, rare disease) — 4-stage 변형 (1, 2, 3, 4) 만으로 meaningful한가? 아니면 별도 "biological insight-first" arc가 필요한가?
- **Q4.** Cross-species evidence가 본질적으로 안 맞는 case (e.g. 인간 특이적 neuro pathway) — format을 어떻게 degrade해야 하는가?
- **Q5.** 이 5-stage arc가 cs.AI / method 논문에도 적용 가능한 변형이 있는가? "Benchmark-first" arc가 가능한지 — 별도 page 또는 별도 recipe로 박제. (예: [[agi-to-asi-pathways-bb-context]] — strategic context 우선 framing)
- **Q6.** Paid Brief 클라이언트가 "T1 evidence 없는데 brief 해달라"고 하면 어떻게 거절/리다이렉트? Decision-grade quality bar 명문화 필요.
- **Q7.** 이 포맷을 "BB-IO Compass / Paid Brief / ARP v27 card" 3종 deliverable에 표준 적용했을 때, 일관성 vs deliverable-specific tone balance 어떻게?

### 4. Contradictions

- **vs. [[scgpt_deep_analysis]] (Cui et al. 2024, Nature Methods)** — scGPT는 foundation model paper이므로 method-first open ("we developed a foundation model for single-cell biology..."). GWAS anchor 없음. **포맷이 다른 이유 명확:** model architecture를 selling point로 내세우면 mechanism-first가 자연스러움. 이 5-stage arc는 **target / disease** 중심 deliverable에 적용. **conflict 아님, scope 다름.**
- **vs. [[livia_deep_analysis]] (Kim & Perrimon 2026)** — LIVIA는 browser-based PPI tool. Tool-first open ("LIVIA is a browser-based agentic framework..."). Wet-lab researcher 대상이라 client-side / privacy 강조. **scope 다름.**
- **vs. [[claw_ai_lab_brief]]** — Claw AI Lab paper는 5-layer pyramid를 제시하는 framework paper. Stage 1 (clinical anchor) 없음. **scope 다름.**
- **vs. SSR paper ([[ssr_likert_syntheticconsumers_deep_analysis]], Maier et al. 2025)** — SSR은 non-bio methodology. GWAS anchor가 stat. (Bayesian rating validation) 로 대체. **다른 도메인에서 Stage 1 변형 가능** — "regulatory / validation anchor"로 일반화하면 cross-domain 사용 가능.
- **vs. [[oxphos-cancer-vulnerability]]** — OXPHOS 페이지는 curated (4-섹션 완전). 이 format 페이지보다 5일 먼저 작성. OXPHOS 페이지는 target-list 형식 (multi-target 평가), 이 페이지는 single-format 형식 (recipe). **mutually reinforcing.**
- **vs. [[agentic_patterns_brownbiotech_mapping]]** — Agentic design patterns 페이지는 multi-pattern (ReAct, Reflection, ToT 등) coverage map. 이 페이지는 **research narrative** format으로, agentic pattern과 orthogonal. Recipe 자체는 agentic design pattern의 일종으로 분류 가능 (Anthropic "Workflow patterns" 중 "Prompt Chaining"의 변형).

---

## 🏷 태그 / 분류

- **도메인:** `#clinical` (translational research), `#gwas` (human genetic evidence)
- **Sub-domain:** `#methodology` (research format)
- **메타:** `#concept`, `#hypothesis` (BB-IO Compass reformat 가능성)
- **Informal labels (page-specific, not in SCHEMA):** `format`, `decision-ready`, `paid-brief`

## 🔗 Cross-references

- **Recipe (reusable):** `brown-biotech-paid-brief-gwas-first-recipe` skill
- **Conceptual siblings:**
  - `[[bb-io-compass]]` — clinical product, Stage 1+2+5
  - `[[scgpt_deep_analysis]]` — method-first contrast
  - `[[livia_deep_analysis]]` — tool-first contrast
  - `[[oxphos-cancer-vulnerability]]` — multi-target eval, curated
  - `[[agentic_patterns_brownbiotech_mapping]]` — agentic design pattern taxonomy
  - `[[ssr_likert_syntheticconsumers_deep_analysis]]` — non-bio methodology (Stage 1 variant)
- **Workflow:**
  - `brown-biotech-paper-intake-workflow` skill — Track E = "full pattern" = this format
- **Raw source:** [[raw/SLC7A2_Spears_JCI_2026_e173913]] (or PDF at `/Users/ocm/.hermes/cache/documents/doc_7ab6248e14d7_173913_1_20260529155328_covered_4fa089109ce452e764bbb8648b44a723.pdf`)

---

> **Last updated:** 2026-06-16 | **Format spec version:** 1.0.0 | **Source paper:** Spears et al., *JCI* 2026;136(12):e173913
