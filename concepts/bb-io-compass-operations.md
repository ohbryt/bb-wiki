---
title: BB-IO Compass Operations — LIMS, Validation, CLIA/CAP, Revenue, Milestones
created: 2026-06-15
updated: 2026-06-15
type: concept
tags: ["dx", "biomarker", "clinical", "ai"]
sources:
  - bb-io-compass  (parent — clinical context)
  - 2026-06-15-keap1-nrf2-io-biomarker-companion-diagnostic  (sister query — evidence)
contradictions: []
---

# BB-IO Compass Operations
> LIMS workflow · analytical & clinical validation · CLIA/CAP regulatory pathway · revenue model · MVP milestones

> **Parent page:** `[[bb-io-compass]]` (clinical context, decision matrix, 3-tier roadmap)
> **This page:** implementation details only — Tier 1 LDT launch.

---

## Tier 1 — Technical Pipeline

### 1. Wet lab
- **Sample:** FFPE tumor + matched peripheral blood (germline control, optional)
- **NGS:** Targeted hybrid-capture panel — 3 genes (STK11, KEAP1, SMARCA4) + hotspot regions (KRAS, EGFR, ALK, ROS1, BRAF, MET, ERBB2, RET, NTRK1/2/3) for context
- **IHC:** PD-L1 22C3 pharmDx (Dako) — TPS scoring by trained pathologist
- **TMB:** Calculated from NGS panel (~1.5 Mb coding region) — internally validated against FoundationOne CDx
- **Specimen requirements:** ≥20% tumor cellularity, ≥50 ng DNA
- **Platform:** Illumina NextSeq 550/2000 (preferred) or MiSeq (low-throughput)

### 2. Bioinformatics
- **Alignment:** BWA-MEM → GATK best-practices
- **Variant calling:** Mutect2 (somatic) + VarDict + in-house consensus
- **CNV:** GATK CNV + panel-of-normals
- **TMB:** Custom pipeline (synonymous + non-synonymous, filtered for driver passengers)
- **HLA typing:** xHLA or HLA-LA
- **QC:** Coverage ≥500× median per gene; ≥100× at all 3 target genes; FFPE deamination filter (UDG treatment recommended)
- **Turnaround:** 5-7 days wet lab + 1-2 days bioinformatics

### 3. Report
- **PDF clinical report** — 4 sections: Specimen QC / Variant results (Tier 1 genes + context) / PD-L1 TPS / TMB / **Decision recommendation** (cited: Alessi 2023, Skoulidis 2024, NCCN v.X.2026)
- **Tiered result:** 3-gene WT = "eligible for standard CIT"; mutated = "refer to Tier 2 (BB-IO Compass Tier 2) or consult clinical genomics"
- **Machine-readable:** JSON + HL7 FHIR Genomics Report (CDC CEDAR, GA4GH)

---

## LIMS Workflow (end-to-end)

```
[Order]         →   [Accession]    →   [Wet lab]      →   [Bioinformatics]  →   [Review]    →   [Report]
                                                                                (pathologist    (PDF + FHIR
 Oncologist        LIMS order        Sample QC           Alignment,           + clinical      JSON to EHR
 + EMR              entry:           → DNA/RNA          variant call,         geneticist
 integration        patient ID,      extraction,         TMB, HLA,             sign-out)
 (HL7 ORM)          ICD-10,          library             PD-L1 image
                    payer,           prep, NGS           analysis
                    specimen         run, IHC slide
                    tracking         scoring
                    barcode
```

**LIMS stack (recommended for BB):**
- **Open-source core:** MOLGENIS / LabKey / cBioPortal for in-house data warehouse
- **Production-grade:** CloudLIMS (~$300-500/mo) or LabVantage
- **EMR integration:** HL7 v2 ORM (order) → ORU (result), FHIR Genomics for structured data
- **Sample tracking:** 2D barcode at accession; chain-of-custody logged at each step
- **QA:** Bio-Rad Unity Real-Time QC + monthly proficiency testing (CAP PPT)

---

## Validation Plan (CLIA/CAP-aligned)

### Analytical validation (before clinical use)
| Parameter | Acceptance criterion | Sample size |
|---|---|---|
| **Accuracy** | ≥95% concordance with orthogonal method (FoundationOne, Caris) | 50 pos + 50 neg |
| **Precision (reproducibility)** | ≥95% agreement between runs/operators/instruments | 20 samples × 3 runs × 3 operators |
| **Limit of detection (LoD)** | ≥95% detection at 5% VAF for SNV; 10% for indel | 20 samples spiked at 5%, 2% VAF |
| **Analytical sensitivity** | ≥95% at ≥20% tumor cellularity | 30 samples across cellularity range |
| **Analytical specificity** | ≥99% (no false positives) | 50 WT samples |
| **FFPE artifact tolerance** | UDG-treated vs untreated comparison | 20 FFPE samples |
| **PD-L1 IHC concordance** | ≥90% with reference lab (Dako 22C3) | 30 cases, blinded |

### Clinical validation (before LDT launch)
- **Retrospective cohort:** 200 advanced NSCLC 1st-line CIT patients with banked FFPE + clinical outcomes
- **Primary endpoint:** BB-IO Compass Tier 1 recommendation concordance with actual regimen + outcome (ORR, PFS)
- **Secondary endpoint:** Time-to-decision (target <10 days from order to report)
- **Prospective registry:** 500-pt multi-site registry (Track F post-2026 H2) — clinical utility evidence for FDA submission / payer coverage

### Regulatory pathway
- **Initial launch:** **LDT (Laboratory-Developed Test)** under CLIA '88 + CAP accreditation — NY State CLEP if applicable
- **CLIA certification:** Apply within 6 months of launch (CMS Form 855, CLIA-116)
- **CAP accreditation:** College of American Pathologists — Biorepository, Molecular Pathology, Cytogenetics checklists
- **Future FDA pathway:** 510(k) if predicate exists (FoundationOne CDx) → de novo/PMA if novel. Target: PMA submission 2028 after prospective registry matures.

---

## Revenue Model

### Reimbursement (US market, 2026)
| Test component | CPT code | 2026 Medicare rate |
|---|---|---|
| **NGS panel (3 genes + hotspot context)** | 81445 (targeted solid tumor NGS) | $598 |
| **PD-L1 IHC 22C3** | 88360 | $120 |
| **TMB calculation** | 81479 (unlisted molecular) | $200-300 |
| **Professional component** (pathologist + clinical geneticist sign-out) | 88381 / 96041 | $80-150 |
| **Total per test** | | **$1,000-1,200 per patient** |

### Pricing strategy
- **Medicare/payer:** $1,000/test (cost + 30% margin, sustainable)
- **Self-pay / international:** $1,500-2,000
- **Pharma partnership (companion Dx co-dev):** $2-5M upfront + per-test royalty (GNE/AZN/Merck precedent for IO companion Dx)

### Unit economics (BB lab scale)
- **CAPEX (Year 1):** NGS sequencer $250-500K + lab buildout $200K + LIMS $50K + validation $150K = **$650-900K**
- **OPEX (annual):** Reagents $200K + labor (2 FTE @ $150K loaded) + LIMS/maintenance $50K = **$550K/yr**
- **Break-even:** 600-800 tests/yr (depending on payer mix)
- **Year 3 target:** 3,000-5,000 tests/yr → $3-5M revenue, 40-50% EBITDA margin

---

## MVP Milestones (Tier 1 only, 18-month plan)

| Month | Milestone | Deliverable |
|---|---|---|
| **M0 (now)** | Product spec + evidence base | `[[bb-io-compass]]` + this page ✅ |
| **M1-M2** | Lab space + equipment procurement | Sequencer installed, CLIA application filed |
| **M3-M4** | Wet lab SOPs + LIMS configuration | Draft SOPs (extraction, library prep, sequencing, IHC) |
| **M5-M6** | Bioinformatics pipeline build | BWA-MEM + Mutect2 + TMB pipeline validated |
| **M7-M9** | Analytical validation (per table above) | Validation report (50+ samples) |
| **M10-M11** | Retrospective clinical validation (200 pts) | Concordance report with outcomes |
| **M12** | **Tier 1 LDT launch** | First clinical report; NY CLEP submission |
| **M13-M15** | CAP accreditation, EMR integration | CAP certificate, HL7 ORM/ORU live |
| **M16-M18** | Multi-site registry launch (5 sites) | First interim data |
| **M18+** | Tier 2 development (LKB1/KEAP1/KRAS triple + EMSY IHC + MTAP IHC) | Tier 2 product spec |

---

## 4-섹션 판단 레이어

### 1. Source Quotes
- CLIA '88 regulations: 42 CFR §493 — Laboratory Requirements (CLIA quality standards, personnel qualifications, PT, QC, QA)
- CAP Molecular Pathology checklist 2026 ed. — NGS validation requirements (analytical sensitivity, specificity, LoD, reportable range, reference range)
- CMS MolDx LCD L38027 (next-generation sequencing for solid tumors) — coverage criteria
- FDA "Use of Public Human Genetic Variant Databases to Support Clinical Validity for Genetic and Genomic-Based In Vitro Diagnostics" (2018 guidance)
- NCCN NSCLC Guidelines v.X.2026 — PD-L1, TMB, and emerging biomarkers for CIT selection
- CPT code 81445 description: "Targeted genomic sequence analysis panel, solid organ neoplasm, DNA analysis, 5-50 genes"

### 2. My Interpretation
- **LDT-first 가 정답** — PMA 5-7년, 510(k) 2-3년, LDT 6-12개월. Foundation Medicine 2011 같은 경로. CMS MolDx coverage 가 빠르게 (L38027 LCD) — 81445 의 $598 reimbursement 가 직접 cost-recovery.
- **Lab location 의 trade-off** — US (Boston/SD) 가 CLIA + payer reimbursement 면에서 유리하지만, 한국 (Seoul) 가 iChroGene partnership + Asian market 진입에 유리. **dual-track**: US lab M1-M12 (CLIA LDT) + Korea lab M6-M18 (iChroGene partnership + KFDA parallel).
- **LIMS 의 in-house vs SaaS** — 초기엔 CloudLIMS (~$400/mo), scale 후 자체 build ($200K+). 단, FoundationOne 과의 TMB concordance 검증 pipeline 은 자체 bioinformatics stack 필수.
- **Pharma partnership 의 first target** — AZN (POSEIDON, durvalumab+tremelimumab) 가 가장 명확한 co-development partner: POSEIDON 의 STK11/KEAP1 subset 이 BB Tier 1 의 directly validated indication. AZN 의 Tagrisso + Imfinzi + tremelimumab pipeline 에 BB-IO Compass 가 stratification biomarker.
- **Revenue 의 secondary driver** — 국내 시장 (Korea) 의 KFDA LDT 인허가 + iChroGene partnership. 한국은 NGS panel 의 coverage 가 다르지만, "항암제 선택" indication 으로 본인부담 시장 진입 가능. 1,000 tests × $800 (KRW 적용) = KRW 800M / yr.
- **CAP accreditation 의 우선순위** — CAP 가 payer requirement 라면 M12 launch 와 동시 필수. CMS 는 CLIA 면 sufficient 하지만, private payer (UnitedHealth, Aetna) 는 CAP required.
- **Risk:** Foundation Medicine / Tempus / Caris 가 18개월 안에 POSEIDON 기반 panel FDA 승인 시 BB 의 LDT market share 잠식. 그러나 BB 의 "research service + diagnostic" 통합 positioning 이 niche 우위.

### 3. Open Questions
- ⭐ CLIA lab physical location (Seoul / Boston / San Diego) — US-first vs Korea-first vs dual
- ⭐ iChroGene partnership renegotiation scope — consumer vs clinical
- ⭐ LIMS 자체 build vs SaaS (CloudLIMS) — scale timing
- ⭐ NY State CLEP 필요 여부 — NY 에 lab 있을 경우에만
- ⭐ CAP 동시 vs CLIA 후 — payer requirement 분석 필요
- ⭐ Multi-site registry 의 IRB / contracting — single-site IRB vs central IRB
- ⭐ Foundation Medicine 의 510(k) timeline — competitive intelligence
- ⭐ KFDA 인허가 pathway — LDT 인정 여부, IVD 등급
- `[[entities/clia-cap-accreditation-process]]` — regulatory entity page (deferred)
- `[[entities/cms-moldx-coverage-process]]` — payer coverage page (deferred)

### 4. Contradictions
- **3-gene panel 의 focused scope** — Foundation Medicine (300+ gene), Tempus (xT, 500+ gene) 와 달리 BB Tier 1 은 3 gene + hotspot. **advantage** (fast/cheap/clear) vs **disadvantage** (missed BRCA, HRD, MSI, etc.). 18개월 후 Tier 2 의 comprehensive panel 로 확장.
- **LDT 의 scalability** — LDT 는 single-lab validation, multi-site 는 각각 재검증 필요. Multi-site registry 는 high cost, low initial scale. 그러나 LDT 가 commercial scaling 의 fastest path.
- **NCCN guideline update timing** — Alessi 2023, Skoulidis 2024, Galan-Cobo 2025 가 NCCN guideline 에 들어가는 timing 이 미정. **First-mover risk** — guideline update 전 launch 시 adoption 이 standard-of-care 보다 slower.
- **CAP vs CLIA** — CMS 는 CLIA 면 sufficient, private payer 는 CAP required. 동시 신청이 cost-effective but operational burden 높음.

---

**Status:** Implementation spec. 2026-06-15. Tier 1 LDT launch target: M12.
**Path to launch:** LDT under CLIA + CAP, MVP 12 months, revenue Year 1 $0.5-1M, Year 3 $3-5M.
**Strategic value:** First Brown Biotech **clinical product** (vs research services). Direct pharma partnership + 9 actionable drug target validation cohort.
**Saved in:** `/Users/ocm/openclaw/workspace/bb-wiki/concepts/bb-io-compass-operations.md`
