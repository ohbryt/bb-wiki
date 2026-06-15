---
title: TimesFM — Time Series Foundation Model
created: 2026-06-15
updated: 2026-06-15
type: concept
tags: ["ai", "biostat", "longevity", "transcriptomics", "metabolomics", "drug-discovery"]
sources:
  - https://github.com/google-research/timesfm
  - https://arxiv.org/abs/2310.10688
  - https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6
contradictions: []
---

# TimesFM — Google's Time Series Foundation Model
## Das, Kong, Sen, Zhou (Google Research) — ICML 2024 (arXiv 2310.10688)

**Paper:** "A decoder-only foundation model for time-series forecasting" (ICML 2024)
**Latest model:** **TimesFM 2.5** (200M params, 16k context, continuous quantile head)
**License:** Apache 2.0 (open)
**GitHub:** https://github.com/google-research/timesfm · ⭐ 20.8k / 2k forks / 326 commits
**Install:** `pip install timesfm[torch]` · `pip install timesfm[xreg]` (covariates)
**Checkpoints:** https://huggingface.co/google/timesfm-2.5-200m-pytorch
**In Google 1P:** BigQuery ML · Google Sheets · Vertex Model Garden

---

## 1. Executive Summary

**TimesFM** is a **decoder-only transformer** (LLM-style) pretrained on **>100B time points** of public + synthetic time-series data for **zero-shot point + quantile forecasting**. It is the canonical **time-series foundation model** — analogous to how scGPT/Stack are the canonical single-cell FMs.

**Why this matters for Brown Biotech:** Most BB lanes (peptide-service PK/PD, biostatx longitudinal analysis, strict-omics time-course RNA-seq, fibrosis/IPF progression, longevity biomarker tracking) involve **time-series data**. Until TimesFM, every project needed a custom ARIMA / Prophet / state-space pipeline. Now: one foundation model with `forecast(horizon=N, inputs=...)` API + optional covariates (XReg) + quantile head. This is the **direct tech analog of scGPT/Stack** but for the temporal axis.

**Latest version (2.5, Sept 2025):** 200M params (down from 500M), 16k context (up from 2048), optional 30M continuous quantile head for up to 1k horizon, frequency indicator removed, XReg covariate support (Oct 2025), LoRA fine-tuning example (Apr 2026), agent skill `SKILL.md` (Mar 2026).

---

## 2. Architecture

### 2.1 Input representation
- Continuous-valued time series (no tokenization)
- **Patched** input — each time-step becomes a sub-series token (similar to vision transformer patches)
- Optional: `frequency` hint removed in 2.5 (model infers)

### 2.2 Transformer backbone
- **Decoder-only** (GPT-style causal mask), stacked transformer layers
- TPU/GPU-trained; PyTorch + Flax + Apple Silicon backends
- 200M params, 16k context length

### 2.3 Output
- **Point forecast** (mean) for `horizon` time-steps
- **Continuous quantile forecast** (10th–90th, 10 quantiles) via optional 30M quantile head
- Optional **covariates via XReg** (linear regression on top of frozen backbone) — Oct 2025

### 2.4 Fine-tuning (Apr 2026)
- LoRA via HuggingFace Transformers + PEFT
- Preserves backbone, adapts to domain distribution
- `timesfm-forecasting/examples/finetuning/`

---

## 3. Where TimesFM sits in the BB stack

| BB lane | Current approach | TimesFM opportunity |
|---|---|---|
| **peptide-service** | Manual PK/PD modeling, ADMET external API | Zero-shot PK curve + covariate (dose, age) via XReg |
| **biostatx** | Mixed-effects models, custom R/Python scripts | Foundation baseline + uncertainty (quantile head) before domain model |
| **strict-omics** | Time-course DESeq2 + manual trajectory | Time-series foundation baseline; covariate = treatment arm |
| **genox-site** | Ad-hoc longitudinal analysis | Cohort trajectory prediction with uncertainty |
| **research-intelligence** | Static TrueSkill tournament | Time-varying paper-citation trajectory forecasting |
| **business-pipeline** | Manual capacity / revenue forecasting | Lab throughput + ticket volume forecasting (meta-time-series) |

**Key insight for BB:** The XReg covariate support (Oct 2025) is the *biotech-relevant* upgrade — let the foundation model learn general temporal patterns, then add **known covariates (dose, treatment, age, cohort)** as a lightweight linear head on top. This is the right architecture for clinical/lab data where you have small N but rich metadata.

---

## 4. Caveats and limitations

- **Pretraining data** is mostly economic/web/energy time-series (not biomedical). Zero-shot on lab/clinical data may be weaker than domain-tuned classical models (ETS, Prophet).
- **Context limit** is 16k — fine for biomarker streams, problematic for whole-genome expression matrices per gene.
- **No built-in irregular sampling handling** — needs preprocessing for clinical time-points that are not equally spaced.
- **LoRA fine-tuning** is the recommended path for biomedical adaptation (per Apr 2026 release), not full fine-tune.
- **Production integration** via Vertex Model Garden (managed) or self-hosted PyTorch/Flax.

---

## 5. Code pattern (canonical)

```python
import torch, numpy as np, timesfm

model = timesfm.TimesFM_2p5_200M_torch.from_pretrained(
    "google/timesfm-2.5-200m-pytorch"
)
model.compile(
    timesfm.ForecastConfig(
        max_context=1024,
        max_horizon=256,
        normalize_inputs=True,
        use_continuous_quantile_head=True,
        force_flip_invariance=True,
        infer_is_positive=True,
        fix_quantile_crossing=True,
    )
)
point_forecast, quantile_forecast = model.forecast(
    horizon=12,
    inputs=[np.linspace(0, 1, 100), np.sin(np.linspace(0, 20, 67))],
)
# point_forecast.shape    → (n_series, horizon)
# quantile_forecast.shape → (n_series, horizon, 10)  # mean + 10th–90th
```

---

## 6. Resources

- 📄 [arXiv:2310.10688](https://arxiv.org/abs/2310.10688) — ICML 2024 paper
- 💻 [github.com/google-research/timesfm](https://github.com/google-research/timesfm) — 20.8k stars, latest 2.5 (Jun 9, 2026)
- 🤗 [HF Collection](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6) — all checkpoints
- 📰 [Google Research blog](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
- 🧠 [SKILL.md](https://github.com/google-research/timesfm/tree/master/timesfm-forecasting) — agent skill (Mar 2026)
- 🛠 [timesfm-forecasting/examples/finetuning/](https://github.com/google-research/timesfm/tree/master/timesfm-forecasting/examples/finetuning) — LoRA example (Apr 2026)
- 📑 Brown Biotech sidecar: `public/content/research-pulse/2026-06-15-timesfm.md`

---

## 4-섹션 판단 레이어

### 1. Source Quotes

- `README.md` line 3: *"TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting."* (arXiv 2310.10688, ICML 2024)
- `README.md` lines 53–60: TimesFM 2.5 release notes — *"uses 200M parameters, down from 500M. supports up to 16k context length, up from 2048. supports continuous quantile forecast up to 1k horizon via an optional 30M quantile head. gets rid of the `frequency` indicator. has a couple of new forecasting flags."*
- `README.md` line 31: *"Added back the covariate support through XReg for TimesFM 2.5."* (Oct 29, 2025 update)

### 2. My Interpretation

- TimesFM 2.5의 **XReg covariate** (Oct 2025)가 BB에 가장 중요한 업그레이드 — 일반 시계열 패턴은 foundation model이 잡고, 도메인 covariate (dose, treatment arm, age)는 linear head로 더한다. 적은 N + 풍부한 메타데이터의 임상/랩 데이터에 맞는 구조.
- 200M은 작지만 적절 — decoder-only, patched input, 16k context로 메모리 효율이 높음. Self-host 가능 (단일 GPU로 fine-tune 가능).
- pretrained data가 **biomedical이 아님** → zero-shot이 항상 domain-tuned classical model을 이기지는 못한다. **Foundation baseline + LoRA fine-tune** 패턴이 정답. 일단 foundation이 어디서 실패하는지 확인하고, 그 failure mode에 대해 XReg + LoRA로 보정.
- BB의 **time-course 가 있는 거의 모든 lane**에 잠재력 있음. 즉시 value가 큰 곳: biostatx (cohort trajectory), strict-omics (treatment arm time-course), business-pipeline (lab throughput).
- **Foundation model 패러다임의 BB stack 내 위치:** scGPT/Stack이 single-cell 축의 foundation이라면, TimesFM은 temporal 축의 foundation. ARP v27이 drug-discovery FMs를 모으면, TimesFM은 그 stack의 **temporal 모듈**이 된다.

### 3. Open Questions

- ⭐ **BB 임상/랩 데이터 (e.g., IPF progression, biomarker trajectories) 에 zero-shot TimesFM vs classical Prophet/ARIMA → benchmark 만들기** — 첫 internal PoC로 적합
- ⭐ **LoRA fine-tune이 biomedical covariate (dose, treatment arm)에 잘 작동하는지 검증** — Google의 LoRA 예제는 economic data 기준
- **TimesFM이 irregular sampling (clinical time-point)을 잘 처리하는지** — 16k context는 등간격 가정일 가능성. 별도 전처리 + R/clinical preprocessing layer 필요할 수 있음
- **scGPT / TimesFM / FM scaling** — BB의 multi-omics 시간축 분석에 (scRNA-seq at t=0, t=4, t=8 weeks) 어떻게 결합하는가?
- **`/Users/ocm/openclaw/workspace/bb-wiki/queries/2026-06-15-fm-stack-positioning.md`** — FM stack의 BB 내 위치 정리를 essay-grade query 페이지로 발전시킬 것

### 4. Contradictions

- 현재까지 다른 페이지와 직접 충돌하는 주장 없음.
- 잠재적 충돌 후보: `scgpt_deep_analysis` 의 "single-cell FM이 BB의 canonical foundation model" 주장 — 이 페이지는 **temporal foundation model** (다른 축)로 추가되므로 충돌이 아니라 보완.

---

**Status:** First-pass concept page. 2026-06-15. Cross-references:
- `concepts/scgpt_deep_analysis` — single-cell FM (temporal axis = 互補)
- `concepts/aurora_deep_analysis` — AURORA cross-modality AI (FM family)
- `comparisons/arp27_vs_claw_ai_lab_analysis` — drug-discovery AI 비교 (TimesFM은 temporal 모듈로 추가)
- `public/content/research-pulse/2026-06-15-timesfm.md` — Brown Biotech sidecar (Korean summary)
