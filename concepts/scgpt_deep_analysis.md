---
title: Scgpt Deep Analysis
created: 2026-06-14
updated: 2026-06-14
type: concept
tags: ["mash", "longevity", "frailty", "fibrosis", "senescence", "biostat", "ai"]
sources:
  - raw/scGPT_Deep_Analysis.md
contradictions: []
---

# scGPT — Foundation Model for Single-Cell Multi-Omics
## Cui, Wang, Maan, Pang, Luo, Duan & Wang — Nature Methods 2024
## DOI: 10.1038/s41592-024-02201-0

**Paper:** "scGPT: toward building a foundation model for single-cell multi-omics using generative AI"
**Authors:** Haotian Cui¹²³⁸, Chloe Wang¹²³⁸, Hassaan Maan¹³⁴, Kuan Pang²³, Fengning Luo²³, Nan Duan⁵, Bo Wang¹²³⁴⁶⁷
**Affiliations:** ¹University of Toronto, ²Vector Institute, ³Toronto General Hospital Research Institute, ⁴Peter Munk Cardiac Centre, ⁵Microsoft Research, ⁶AI Hub, ⁷Department of Computer Science
**Date:** Published online 26 February 2024 (print August 2024, Vol 21, pp 1470–1480)
**Code:** https://github.com/bowang-lab
**Source PDF:** `/Users/ocm/.hermes/cache/documents/doc_78d3553e9224_s41592-024-02201-0.pdf`

---

## 1. Executive Summary

**scGPT** is a generative pretrained transformer for single-cell biology, trained on **33 million human cells** from the CELLxGENE collection (51 organs/tissues, 441 studies). Following the LLM paradigm (BERT-style masked prediction + GPT-style generative pretraining), scGPT distills transferable representations of genes and cells that can be fine-tuned for **5 downstream tasks**: cell type annotation, multi-batch integration, multi-omic integration, perturbation response prediction, and gene regulatory network (GRN) inference.

**Why this matters for Brown Biotech:** This is **the canonical single-cell foundation model** (Nature Methods 2024) and the most direct technical reference for ARP v27's planned "Foundation Model" engine component. scGPT's pretrain→fine-tune paradigm mirrors the same architectural pattern ARP v27 should adopt for its own drug-discovery foundation model. Published Feb 2024 — still fresh as of June 2026.

---

## 2. Architecture

### 2.1 Input Representation
scGPT takes three components per cell:
1. **Gene tokens** — gene names as unique integer indices (analogous to words in NLG)
2. **Expression values** — continuous read counts (for scRNA-seq) or chromatin accessibility (for scATAC-seq)
3. **Condition tokens** — meta-information (perturbation status, batch, modality)

**Batch tokens** are cell-level vectors repeated to length M; **modality tokens** indicate RNA vs ATAC vs protein. Both use standard embedding layers.

### 2.2 Transformer Backbone
- Stacked transformer layers with multi-head attention
- Standard PyTorch embedding layers: `embg` (gene), `embc` (condition)
- Element-wise sum of gene token + expression + condition embeddings
- Masked-attention map: attention only between known genes and the query unknown gene (causal-mask design adapted from GPT decoders for non-sequential omics)
- Inference: generate all genome-wide gene expression conditioned on a "cell prompt" of known genes

### 2.3 Pretraining Objective
Two tasks (mirroring BERT + GPT):
- **Masked language modeling** — predict expression values at randomly masked gene positions (GEP — Gene Expression Prediction; MSE loss on masked positions)
- **Generative pretraining** — generate unknown gene expression from known gene "prompts"

The combined objective is what allows scGPT to learn gene–gene coexpression patterns in a context-aware way.

---

## 3. Pretraining Data

- **33 million human cells** from CELLxGENE (https://cellxgene.cziscience.com)
- **51 organs / tissues, 441 studies**
- Normal (non-disease) conditions only
- UMAP visualization of 10% sample (3.3M cells) shows clean cell-type clusters

---

## 4. Downstream Tasks & Benchmarks

### 4.1 Cell Type Annotation
- **Setup:** Fine-tune classifier head on scGPT cell embeddings
- **Dataset:** hPancreas (human pancreas)
- **Result:** Achieved ~0.85 accuracy; high precision across all cell types
- **Comparison:** scGPT constantly outperformed TOSICA and scBERT across accuracy, precision, recall, macro F1 (Fig. 2j)
- **Generalization:** Works for rare cell types (>50 cells in reference partition)

### 4.2 Perturbation Response Prediction
- **Datasets:** Adamson (87 one-gene perturbations), Norman (131 two-gene + 105 one-gene), Replogle (1,823 one-gene)
- **Result:** Outperformed GEARS and linear regression baseline by **5–20% margins** (Pearson Δ metric)
- **Key:** scGPT can predict responses to **unseen perturbations** (Norman combinatorial space = 210 combinations, 39 known, 171 predicted)
- **Clustering validation:** Predicted expression clusters align with dominant gene in each perturbation combination (e.g., KLF1+ perturbations cluster together)

### 4.3 Multi-Batch Integration
- **Dataset:** PBMC 10k (3 batches) — scGPT works **without fine-tuning** (highlights pretraining generalizability)
- **Dataset:** Perirhinal cortex — scGPT competitive with all baselines
- **Metric:** AvgBIO score = mean of NMIcell, ARIcell, ASWcell
- **Result:** Competitive on all integration metrics, strong biological conservation

### 4.4 Multi-Omic Integration (scRNA + scATAC)
- **Comparison:** scGLUE and Seurat v.4
- **Result:** scGPT is **the only method** that successfully integrates all three data modalities (RNA + ATAC + protein) with batch correction
- **Key:** scMoMat benchmark — superior batch correction

### 4.5 Gene Regulatory Network (GRN) Inference
- Dataset-level and cell-state-specific GRN inference
- Gene attention weights → identify co-regulated gene modules
- Validated against known pathways (CD14+ monocyte markers etc., Fig. 5b)

---

## 5. Code & Model Availability

- **GitHub:** https://github.com/bowang-lab (Bo Wang lab, U Toronto)
- **Model:** Pretrained checkpoints available
- **Pipeline:** Pretrain + 5 fine-tuning pipelines (cell type, batch, multi-omic, perturbation, GRN)
- **Prerequisite:** CELLxGENE API (https://chanzuckerberg.github.io/cellxgene-census/python-api.html)

---

## 6. Brown Biotech Integration

### 6.1 ARP v27 — "Foundation Model" Engine
This is the most direct reference for ARP v27's foundation-model track. Key adoption points:
- **Pretrain→fine-tune paradigm** mirrors what ARP v27 should do for its own target-specific foundation model
- **5 downstream tasks map to ARP v27's daily outputs** (cell-type annotation, perturbation prediction, multi-omic integration are core to anti-fibrotic / senolytic / KRAS pipeline)
- **Gene-token vocabulary** — ARP v27 should adopt a similar gene-vocab approach for cross-target knowledge sharing

### 6.2 Paid Briefs — Single-Cell Service
- scGPT's pretrained cell embeddings can power a "single-cell cell-type annotation" paid brief (₩2M~8M)
- For Brown Biotech clients without bioinformatics infrastructure, scGPT-based cell-type annotation + cluster marker identification = ready-made deliverable
- Lead time: 2 weeks (scGPT inference + marker analysis + interpretation)

### 6.3 biostatx — Production Single-Cell Pipeline
- Adopt scGPT as default cell-type annotation backend (replaces Seurat-only pipeline)
- For clients with multi-omic data (RNA + ATAC), use scGPT's multi-omic integration (outperforms scGLUE)
- For perturbation screens (e.g., Brown Biotech's own Sargassum japonica screens), use scGPT perturbation prediction

### 6.4 PRISM RAG Ingest
- Paper ingested 2026-06-07: 85 chunks, FAISS index grew from 659 → 744 vectors
- Future queries about "single-cell foundation model", "perturbation prediction", "cell type annotation" will retrieve this paper

### 6.5 Cross-Reference: Geneformer
- Geneformer (Theodoris et al. 2023) is scGPT's direct predecessor — also transformer-based, but uses gene-rank instead of expression values
- scGPT is more general (5 tasks vs Geneformer's focus on cardiac/GRN)
- Both are now standard references for ARP v27's foundation model design

---

## 7. Brown Biotech Action Items

| # | Action | Owner | Timeline |
|---|--------|-------|----------|
| 1 | Test scGPT inference on Brown Biotech's existing Sargassum japonica dataset (CMap repurposing DEGs) | ARP v27 | 2 weeks |
| 2 | Build scGPT-based paid brief SKU: "Single-Cell Cell-Type Annotation" ₩2M~5M | Dr. OCM + Demis | 4 weeks |
| 3 | Adopt scGPT multi-omic integration for spatial transcriptomics service (FFPE Xenium + snRNA-seq) | biostatx | 6 weeks |
| 4 | Update ARP v27 TPP_DGAT1_24Month_Plan.md to cite scGPT in Foundation Model section | Demis | 1 week |
| 5 | Add scGPT to PRISM RAG (done 2026-06-07, 85 chunks) | Demis | ✓ done |

---

## 8. Limitations (Author-Acknowledged)

- Pretraining on **normal cells only** — disease-state fine-tuning required
- Performance on rare cell types (<50 cells) degrades
- Foundation model size (likely ~100M params) requires GPU for fine-tuning
- No comparison to scFoundation (Hao et al. 2024) or GeneCompass (Yang et al. 2024) — these newer models may outperform on specific tasks

---

## 9. Citation

Cui, H., Wang, C., Maan, H. *et al.* scGPT: toward building a foundation model for single-cell multi-omics using generative AI. *Nat Methods* **21**, 1470–1480 (2024). https://doi.org/10.1038/s41592-024-02201-0

---

**Status:** First-pass deep-dive. 2026-06-07. Cross-references:
- `arp-v27/reports/2026-06-07_HitFamilyAnalysis.md` (5 query families matched)
- `arp-v27/literature/AURORA_Deep_Analysis.md` (single-cell + aging comparison)
- `arp-v27/literature/MASH_Review_Deep_Integration.md` (MASH atlas parallel)
- `arp-v27/docs/TPP_DGAT1_24Month_Plan.md` (Foundation Model track to update)


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

