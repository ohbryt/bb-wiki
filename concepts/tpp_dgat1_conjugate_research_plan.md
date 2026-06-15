---
title: Tpp Dgat1 Conjugate Research Plan
created: 2026-06-14
updated: 2026-06-14
type: concept
tags: ["mash", "oxphos", "ferroptosis", "cancer"]
sources:
  - raw/TPP_DGAT1_Conjugate_Research_Plan.md
contradictions: []
---

# TPP-DGAT1 Conjugate: Mitochondrial-Targeted Cancer Therapy
## Research Plan & Strategic Analysis (2026-06-03)

---

## 1. Executive Summary

**Concept:** Conjugate a DGAT1 inhibitor to a triphenylphosphonium (TPP) cation to create a mitochondrial-targeted cancer therapeutic that induces ferroptosis via lipid droplet depletion.

**Key Innovation:** Dual-mechanism drug design combining:
- **TPP+** → selective accumulation in cancer cell mitochondria (~100-500x via membrane potential)
- **DGAT1 inhibition** → blocks lipid droplet formation → ferroptosis sensitization
- **Mitochondrial localization** → direct disruption of lipid metabolism at source

---

## 2. Scientific Rationale

### 2.1 Why DGAT1 for cancer?
**DGAT1 (Diacylglycerol Acyltransferase 1)** catalyzes the final step in triglyceride synthesis, forming lipid droplets (LDs).

**Key 2026 publications:**
- **Cancer Res 2026 (May 14)**: "DGAT1 Inhibition Induces Ferroptosis and Enhances Cancer..."
  - Mechanism: DGAT1 inhibition → ↓LD accumulation → ↑lipid peroxidation → mitochondrial dysfunction
  - DGAT1 KO increased ferroptotic cell death (DGAT2 KO did not)
- **FASEB J 2025 (Aug)**: "DGAT1 Inhibition Enhances Olaparib-Induced Lipotoxic Apoptosis"
  - DGAT1 inhibition + PARP inhibitor (Olaparib) → synergistic in prostate cancer
  - Olaparib alone ↑LD formation (protective feedback) → DGAT1i reverses this
- **Nature 2024 (Jan)**: "Cell cycle arrest induces lipid droplet formation and confers..."
  - iDGAT1/2 restored erastin-induced ferroptosis under cell cycle inhibition
- **Kinsenoside study 2025**: Natural product suppresses DGAT1 → triggers ferroptosis

### 2.2 Why TPP conjugation?
**TPP (Triphenylphosphonium):**
- Delocalized lipophilic cation: [P+(C6H5)3]
- Accumulates 100-1000x in mitochondria (driven by -150 to -180 mV membrane potential)
- Cancer cells have **hyperpolarized mitochondria** (~-220 mV vs -150 mV in normal cells) → **selective accumulation**
- Used in clinical-stage compounds: MitoQ, Mito-VitE, SkQ1
- Linker length n=2-10 alkyl chain controls lipophilicity and matrix localization

### 2.3 Why combine them?
**Synergistic mechanisms:**
1. **Mitochondrial DGAT1 localization**: DGAT1 is also found in mitochondrial-associated membranes (MAMs)
2. **Localized LD depletion**: Mitochondrial targeting concentrates DGAT1 inhibition where lipids are most dangerous
3. **Enhanced ferroptosis**: TPP+ drives mitochondrial ROS → DGAT1i prevents LD-based lipid sequestration
4. **Tumor selectivity**: Cancer cell mitochondrial hyperpolarization amplifies TPP+ accumulation

---

## 3. Competitive Landscape

### 3.1 DGAT1 Inhibitors (clinical-stage)

| Drug | Company | IC50 | Status | Cancer indication |
|------|---------|------|--------|------------------|
| **AZD7687** | AstraZeneca | 80 nM | Ph1 (2013) - failed for obesity, never tried in cancer | N/A (repurpose opportunity) |
| **PF-04457845** | Pfizer | nM | Preclinical (FAHHP target) | Pain |
| **LCQ908** | Novartis | nM | Ph2 - obesity, diabetes | N/A |
| **A-922500** | Abbott | nM | Preclinical | Dyslipidemia |

**Repurposing opportunity:** All failed in obesity/MASLD but never tested in cancer where the mechanism is now well-validated.

### 3.2 TPP-Conjugated Cancer Therapeutics

| Conjugate | Parent Drug | Cancer Type | Stage |
|-----------|-------------|-------------|-------|
| **MitoTam** | Tamoxifen | Breast cancer | Ph1/2 |
| **Mito-DCA** | Dichloroacetate | Various | Preclinical |
| **Mito-Metformin** | Metformin | Various | Preclinical |
| **MitoQ** | CoQ10 | Various | Approved (supplement) |
| **TPP-DOX** | Doxorubicin | Various | Preclinical |
| **TPP-Cisplatin** | Cisplatin | Various | Preclinical |

**No existing DGAT1-TPP conjugates identified in literature.** Novel IP space.

### 3.3 Mitochondrial Lipid Metabolism Targeting

- **LCL768** (LCL/Stanford): Ceramide-dependent mitophagy
- **Pt-LD complex** (RSC 2026): Photoinduced ferroptosis via LD targeting
- **MitoQ + Ferroptosis inducers** (multiple): Combinatorial approaches

---

## 4. Synthesis Feasibility

### 4.1 TPP Conjugation Chemistry
**Standard approach:** 
- Start with DGAT1 inhibitor containing amine, hydroxyl, or carboxylic acid handle
- Convert to NHS ester or tosylate
- React with TPP+-(CH2)n-NH2 (n=2-10)
- Purify by HPLC

**AZD7687 structure analysis** (likely amine handle available):
- AZD7687: 2-(4-(2-(3-chlorophenyl)-5-methyloxazole-4-carboxamido)phenyl)acetic acid
- Contains amide and carboxylic acid → both conjugatable
- Predicted conjugate: AZD7687-TPP via amide or ester linker

**Design rules for optimal TPP conjugates:**
| Parameter | Optimal range |
|-----------|--------------|
| LogP | 2-5 (excessive lipophilicity → non-specific binding) |
| Linker length | C2-C10 alkyl chain |
| TPP+ charge | 1+ (mono-TPP sufficient for mitochondrial targeting) |
| CLogP (TPP) | ~+2.5 to +4 (highly lipophilic cation) |
| MW | <800 Da preferred (Lipinski compliance) |

### 4.2 Alternative Cation Scaffolds
- **TAPY** (triazolyl pyridinium, Mar 2025): Higher cancer selectivity than TPP
- **Rhodamine B**: Established mitochondrial accumulation
- **Dibenzylammonium**: Lower lipophilicity, alternative profile

---

## 5. Patent Landscape

### 5.1 Key Patents to Consider
- **AstraZeneca DGAT1 inhibitors** (US8115015B2, US8211916B2): Composition of matter
- **TPP conjugation methods** (general - expired by now)
- **Mitochondrial drug delivery** (MitoQ - multiple)

### 5.2 Novel IP Opportunity
- **Specific conjugate of DGAT1 inhibitor + TPP+** with cancer indication
- **Combination with ferroptosis inducers** (e.g., erastin, RSL3)
- **Tumor-specific formulations** (nanoparticle, antibody-targeted)

---

## 6. Research Gaps & Opportunities

### 6.1 Knowledge Gaps
1. **No DGAT1-TPP conjugate** has been synthesized/characterized
2. **Mitochondrial DGAT1 localization** in cancer cells not well-mapped
3. **Optimal linker chemistry** for DGAT1 inhibitors unclear
4. **Tumor-specific mitochondrial potential** not validated across cancer types
5. **Resistance mechanisms** to TPP+ accumulation (P-glycoprotein efflux) need characterization

### 6.2 Strategic Opportunities
1. **First-in-class DGAT1-TPP conjugate** for ferroptosis-based cancer therapy
2. **Combination strategies** with KEAP1/NRF2 (our expertise), SLC7A11
3. **Tumor-selective ferroptosis** via cancer hyperpolarized mitochondria
4. **Repurposing failed DGAT1 inhibitors** (AZD7687) for oncology

---

## 7. Recommended ARP Integration

### 7.1 New Integration Module
**File:** `arp-v27/integration/tpp_dgat1_conjugate.py`
- TPP-DGAT1 conjugate design rules
- Linker optimization
- Lipinski property calculation
- Cancer selectivity scoring

### 7.2 Connections to Existing Research
- **KEAP1/NRF2 axis** (primary project): NRF2 activation regulates ferroptosis resistance
  - TPP-DGAT1 may overcome NRF2-induced ferroptosis resistance
- **SLC7A11** (in-progress): Cystine transporter, ferroptosis marker
  - TPP-DGAT1 + SLC7A11 inhibition = dual ferroptosis induction
- **MASLD/NASH** (existing research): DGAT1 original indication
  - Repurposing strategy validated in metabolic disease
- **Avoid-ome screening** (recent integration): TPP-DGAT1 ADMET evaluation

### 7.3 Experimental Workflow
1. **In silico design**: AZD7687-TPP via amide linker
2. **Docking**: MitoQ-bound DGAT1 structure
3. **ADMET prediction**: Avoid-ome evaluation
4. **Synthesis**: TPP+-(CH2)6-NH2 conjugation
5. **In vitro validation**: 
   - Mitochondrial accumulation (fluorescence)
   - LD depletion (BODIPY staining)
   - Ferroptosis induction (C11-BODIPY lipid ROS)
   - Cell viability in cancer lines (PDAC, NSCLC, melanoma)
6. **In vivo**: PDX mouse models with cancer-specific mitochondrial potential

---

## 8. Key References

### 8.1 Critical Papers
1. **Cancer Res 2026.05.14** - DGAT1 Inhibition Induces Ferroptosis (FOUNDATIONAL)
2. **FASEB J 2025.08** - DGAT1 + Olaparib synergy
3. **Nature Commun 2024.01** - Cell cycle arrest + LD formation
4. **RSC Med Chem 2025.11** - TPP-based mitocans review
5. **Nat Reviews Cancer 2025.08** - Mitochondrial metabolism in cancer
6. **PMC6107715** - Mitochondrial-targeting anticancer conjugates review
7. **J Med Chem 2013.08** - DGAT1 inhibitor development review
8. **PMC12670399** - Lipophilic cations as MITACs (2025)

### 8.2 Key Companies
- **AstraZeneca**: AZD7687 (failed Ph1, available for licensing)
- **Novartis**: LCQ908 (Ph2)
- **Pfizer**: PF-04457845 (preclinical)
- **Abbott**: A-922500 (preclinical)
- **MitoQ Limited**: MitoQ platform technology
- **Novacea/Molecular Insight**: Mitochondrial cancer therapeutics

---

## 9. Next Steps

### 9.1 Immediate (Week 1-2)
- [ ] Synthesize AZD7687-TPP conjugate (via amide linker)
- [ ] In silico ADMET (via avoidome_evaluator.py)
- [ ] Docking analysis (DGAT1 + TPP moiety)
- [ ] Patent search detailed

### 9.2 Short-term (Month 1-3)
- [ ] SAR study of linker length (C2-C10)
- [ ] TAPY alternative comparison
- [ ] In vitro ferroptosis assays
- [ ] KEAP1/NRF2 axis interaction study

### 9.3 Long-term (Month 3-12)
- [ ] Lead optimization
- [ ] PK/PD studies
- [ ] In vivo efficacy (PDX models)
- [ ] Combination with KEAP1 activator or SLC7A11 inhibitor

---

## 10. Risk Assessment

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Mitochondrial potential too low in target cancer | Medium | Screen multiple cancer types; focus on hyperpolarized tumors |
| TPP+ efflux by P-gp | Medium | Test in MDR-negative lines first; co-formulate with P-gp inhibitors |
| Off-target toxicity to normal mitochondria | Medium | Use shorter linkers; consider TAPY alternative |
| DGAT1 in CNS limits use | Low | TPP+ does not cross BBB significantly |
| Competition from other lipid metabolism drugs | Medium | Combination strategy differentiates |

---

**Document Version:** 1.0  
**Date:** 2026-06-03  
**Status:** Research Plan v1 - Ready for execution  
**Next milestone:** AZD7687-TPP conjugate design + in silico ADMET (Week 1)


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

