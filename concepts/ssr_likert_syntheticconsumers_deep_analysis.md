---
title: Ssr Likert Syntheticconsumers Deep Analysis
created: 2026-06-14
updated: 2026-06-14
type: concept
tags: ["longevity", "peptide", "biostat", "ai"]
sources:
  - raw/SSR_Likert_SyntheticConsumers_Deep_Analysis.md
contradictions: []
---

# Semantic Similarity Rating (SSR): LLM 합성 소비자가 인간 Purchase Intent를 재현하는가 — Deep Analysis

**Title:** LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings
**Authors:** Benjamin F. Maier, Ulf Aslak, Luca Fiaschi, Nina Rismal, Kemble Fletcher, Christian C. Luhmann, Robbie Dow, Kli Pappas, Thomas V. Wiecki
**Affiliations:** PyMC Labs (Berlin, Germany) + Colgate-Palmolive Company (New York, NY, USA)
**arXiv:** [2510.08338v3](https://arxiv.org/abs/2510.08338) [cs.AI], posted 2025-10-27
**Pages:** 28 (main + appendix), 4.2 MB
**Code:** [github.com/pymc-labs/semantic-similarity-rating](https://github.com/pymc-labs/semantic-similarity-rating)
**PDF:** `/Users/ocm/.hermes/cache/documents/doc_16d262afe046_2510.08338v3.pdf`
**BB relevance (primary domain):** **LOW** — consumer research / marketing methodology paper, not life sciences
**BB relevance (transferable methodology):** **MEDIUM-HIGH** — SSR framework is generalizable to BB's SoI reasoning layer, peptide-service concept testing, and ARP v27 synthetic expert panels
**Added to Brown Biotech:** 2026-06-13 — Notion Active Projects DB ✅ (page `37ef2735-33a4-81dd-a9d6-d46ee5d32440`), PRISM RAG ✅ (66 chunks, index 744→810), brownbio.tech sidecar post ✅ (`2026-06-13-ssr.md`)

---

## 1. 핵심 요지 (TL;DR)

**Problem:** LLM에게 Likert 척도(1–5) 직접 응답을 요구하면, 응답 분포가 극단적으로 좁아지고 (regression to mean, typically '3'), 인간 데이터의 넓은 분산을 재현하지 못함. 기존 synthetic consumer 연구의 "fundamental limit"으로 여겨졌음.

**Solution — Semantic Similarity Rating (SSR):**
1. LLM에게 **자유 텍스트** 응답을 생성하게 함 ("I'm somewhat interested. If it works well...")
2. 텍스트 → embedding (text-embedding-3-small)
3. 5개 reference anchor 문장 (1~5 각 Likert 점수당 하나) 과의 **cosine similarity** 계산
4. Similarity를 probability mass function (pmf) 으로 변환 → 분포 보존

**Key result:** Colgate-Palmolive의 57개 personal care product survey (9,300명 인간 응답) 기준:
| Method | Correlation attainment ρ | KS similarity K^xy |
|---|---|---|
| Direct Likert (DLR) | 80% | 0.26–0.39 |
| Follow-up Likert (FLR) | 85% (GPT-4o) | 0.72 |
| **SSR (Gem-2f)** | **90%** | **0.80** |
| **SSR (GPT-4o)** | **90.2%** | **0.88** |
| LightGBM (supervised baseline) | 65% | 0.80 |
| Human test-retest ceiling | 100% | (by construction) |

→ **제로샷 LLM + SSR > 감독 학습 LightGBM** — 300회 random split, 통계적으로 유의 (p<10⁻²⁰)

**핵심 인사이트:** Likert 응답의 문제는 LLM 자체가 아니라 *elicitation 방식*. 텍스트로 우회 후 임베딩 유사도로 매핑하면 분산과 순위 모두 복원 가능. 추가로 **합성 소비자가 인간보다 더 정교한 정성 피드백** 제공 (합성 응답이 "ease of use" vs "side effects" 같은 양자택일 트레이드오프를 명시).

---

## 2. 방법론 (Method) — 알고리즘 검토

### 2.1 SSR 의 수학적 구조

**Likelihood mapping (Eq. 7-8):**

$$p_{\tilde{c},i}(r) \propto \gamma(\sigma_{r,i}, t_{\tilde{c}}) - \gamma(\sigma_{\ell,i}, t_{\tilde{c}}) + \epsilon\delta_{\ell,r}$$

- $\gamma$ = cosine similarity between response embedding and anchor embedding
- $\ell$ = reference set 내 minimum similarity anchor
- $\epsilon$ = floor parameter (논문에서 $\epsilon = 0$; 즉 minimum similarity = zero probability)
- $m = 6$ reference sets averaged → final pmf

**Temperature lever (Eq. 9):** $p(r, T) \propto p(r)^{1/T}$, $T=1$ 기본값. Appendix C 의 sweep 결과 — $T=1$ 이 합리적 default 이지만 local optimum 존재.

### 2.2 Reference Anchor Set 설계 (Appendix C.1)

5개 anchor × 6 set = 30개의 짧은 도메인-독립 진술:

| Likert | Anchor 예시 (재구성) |
|---|---|
| 1 | "It's rather unlikely I'd buy it." |
| 3 | "I'm on the fence about it." |
| 5 | "It's very likely I'd buy it." |

Anchor 들은 **의도적으로 generic** — 특정 제품군(oral care, deodorant 등) 에 종속되지 않음. 2, 4 anchor 는 인접 anchor 의 semantic midpoint.

### 2.3 평가 지표 (Section 3.3 / App. A.3)

**Distributional similarity:** $K^{xy} = E[KS\,sim_s] = 1 - E[KS\,dist_s]$ over 57 surveys.

**Concept ranking similarity:** Pearson $R^{xy} = corr[PI^x, PI^y]$ — mean purchase intent 의 제품 간 순위 보존.

**Correlation attainment (핵심 신규 지표):**
$$\rho = \frac{E[R^{xy}]}{E[R^{xx}]}$$

$R^{xx}$ = 인간을 2,000회 random split (test/control half) 한 상관. 인간 데이터의 좁은 분포(E[PI]=4.0, σ=0.1)로 인해 raw $R^{xy}$ 가 1.0 에 도달하는 것은 noise 때문에 불가능. 따라서 $\rho$ 는 "이론적 최대 대비 실제 달성률" — **human test-retest reliability에 analog한 synthetic metric**.

---

## 3. 결과 (Results) — 무엇이 작동했나

### 3.1 Method 별 성능 (T_LLM = 0.5, image stimulus)

| | GPT-4o ρ | GPT-4o K^xy | Gem-2f ρ | Gem-2f K^xy |
|---|---|---|---|---|
| DLR | 81.7% | 0.26 | 80% | 0.39 |
| FLR | 84.7% | 0.72 | 90% | 0.59 |
| SSR | **90.2%** | **0.88** | **90%** | **0.80** |

→ SSR 이 **두 모델 모두에서** ρ 와 K^xy 를 동시에 끌어올림. DLR 의 좁은 분포 (always '3') 와 FLR 의 분산 회귀 문제가 모두 해결됨.

### 3.2 Demographic conditioning 의 효과

**인구통계 attribute 를 persona prompt 에 포함할 때** (vs 빼고 generic system prompt):

- **Age:** GPT-4o 가 인간의 concave 패턴 (젊은/노년 낮음, 중년 최고) 을 정확히 재현
- **Income:** 예산 압박 persona → 낮은 PI; "in danger" wording (level 2) 에 GPT-4o 극도로 민감
- **Gender / region / ethnicity:** 재현 약함 (Fig. 8)
- **Demographics 제거 시:** ρ 92% → 50% (K^xy 는 0.91 로 유지)

→ **분포는 맞지만 신호는 약함**. Persona 의 detail 수준이 product-level signal 추출에 필수.

### 3.3 LightGBM 베이스라인 (App. D)

300회 random split, 5 demographic + 3 concept feature:

| | ρ (5-fold mean ± SE) | K^xy |
|---|---|---|
| LightGBM (in-sample) | 64.6 ± 1.0% | 0.797 |
| FLR (zero-shot) | 83.2 ± 0.7% | 0.716 |
| SSR (zero-shot) | **88.3 ± 0.7%** | **0.883** |

→ **제로샷 LLM + SSR 이 감독 학습 LightGBM 을 압도**. LLM 의 semantic product understanding 이 단순 feature 기반 학습을 능가. 이는 synthetic survey 의 실용적 의의 — **학습 데이터 없이도 즉시 deploy 가능**.

### 3.4 다른 question 으로의 일반화

"How relevant was the concept?" (PI 가 아닌 relevance):
- Gem-2f SSR: ρ = 82%, K^xy = 0.81
- Gem-2f FLR: ρ = 91%, K^xy = 0.62

→ SSR 은 reference set 만 새로 정의하면 다른 Likert construct 로 확장 가능 (수렴이 빠른 plug-and-play).

### 3.5 정성 피드백의 부수 효과 (App. E)

인간 응답은 보통 한 줄 ("Just the steps and how it tells you what it was for"). 합성 응답은 다중 차원의 trade-off 를 명시:
- "The ease of use and [...] safety are appealing, but I'd want to know more about its effectiveness and any potential side effects."
- "It seems a bit too high-end for my needs and budget."

→ **Likert 숫자 + 정성 rationale 동시 산출** — 정성 분석을 위한 추가 survey 가 필요 없어짐. 합성 응답은 **positivity bias 가 더 적음** (인간보다 넓은 dynamic range).

---

## 4. 방법론 한계 (Methodological Limitations) — 가장 긴 섹션

### 4.1 Reference statement set 의 의존성 (가장 큰 caveat)

> "The reference sets created herein were **manually optimized for the 57 surveys** subject to this study, which means it remains elusive how well they would perform for other surveys." — §5 Discussion

- Reference anchor 가 hand-crafted → 본 데이터셋에 **over-tuned**
- Cross-survey (different product domain, different language) 일반화 미검증
- Auto-generated reference sets (LLM 이 anchor 자체를 만듦) — 제안만, 실증 없음

**영향:** SSR 의 90% ρ 가 *이 57개 personal care survey* 에 한정된 결과일 가능성. B2B 산업재, 의료, 서비스 등 다른 도메인에서는 anchor 재설계 필요.

### 4.2 Embedding model 종속성

- **유일하게 테스트된 임베딩:** OpenAI `text-embedding-3-small`
- `text-embedding-3-large` 도 "virtually unchanged" — 그러나 1개 vendor 에 종속
- Cosine similarity 외 metric (Euclidean, dot product, learned metric) 미비교
- **Cross-lingual anchor 매핑** 미언급 — 한국어/일본어/중국어 시장 적용 시 anchor 도 재설계 필요

### 4.3 Demographic 일반화의 불완전성

성공:
- ✅ Age (concave pattern)
- ✅ Income (budgetary stress)
- ✅ Concept category (Cat. I–IV)
- ✅ Price tier (Tier 1–5)
- ✅ Source (Source A vs B 선호)

실패:
- ❌ Gender
- ❌ Region (dwelling)
- ❌ Ethnicity (9개 survey 만 해당)
- ❌ Cross-product interaction terms

→ Persona conditioning 이 **"신호는 약하지만 분포는 맞음"** 의 trade-off 를 가짐. 특정 subgroup 의사결정에 synthetic panel 을 쓰는 것은 위험.

### 4.4 Training data domain coupling — 본질적 한계

> "The reason our approach succeeds in oral care products [...] is likely that the model has been exposed to abundant human discussions of these categories in its training corpus (e.g., online forums and consumer reviews). **For domains where such background knowledge is sparse or absent, SSR will not conjure valid consumer preferences.**" — §5

- LLM training data 에 광범위한 consumer review 가 있는 도메인 (personal care, food, electronics) → SSR 신뢰
- **희소 도메인** (B2B 산업재, 신제품 카테고리, niche clinical product) → hallucination 위험
- Cold-start 문제: 신규 카테고리에서는 synthetic panel 의 validity 가 보장되지 않음

### 4.5 시뮬레이션 vs 실제 구매 행동의 괴리

> "synthetic consumers cannot fully capture the real-world contingencies of purchasing behavior, such as **budget constraints, cultural context, or marketing exposure**." — §5

- LLM 의 "income" persona 는 budget constraint 의 인지적 표현일 뿐, 실제 wallet constraint 아님
- Marketing exposure / advertising / distribution channel 효과 미반영
- 5-point Likert PI ≠ 실제 conversion probability (Jamieson & Bass 1989 의 conversion coefficient 가 별개)

### 4.6 "Narrow ceiling" 통계적 artifact

인간 데이터: $E[PI^x] = 4.0$, $\sigma = 0.1$ — **극도로 좁은 분포**. 따라서 test-retest reliability $R^{xx}$ 도 ceiling 이 낮음. $\rho = 90\%$ 의 절대적 의미는 약함 — 만약 인간 PI 분포가 $\sigma = 0.5$ 였다면 $\rho$ 가 60% 만 나와도 절대적 성능은 더 높을 수 있음.

→ **본 결과는 "personal care + 5pt Likert + 좁은 인간 분포" 라는 매우 specific 한 조건 하의 최적화** — 일반화 해석 시 주의.

### 4.7 단일 LLM 패밀리 의존

- GPT-4o + Gemini-2.0-flash 만 production test
- o3, Claude, Llama 비교 시도했으나 "초기 실험에서 일관성 부족" 으로 배제
- 모델 업데이트 시 anchor 재검증 필요 (anchor 가 hand-tuned)
- Open-source LLM (Llama 3, Mistral) 에서의 재현성 미검증

---

## 5. 재현 가능성 (Reproducibility) — 코드는 공개, 데이터는 폐쇄

### 5.1 ✅ 공개 자산

- **Code:** [github.com/pymc-labs/semantic-similarity-rating](https://github.com/pymc-labs/semantic-similarity-rating) — Python package, pip install 가능
- **Algorithm:** 수식 Eq. 7-9 + App. C.2 full implementation
- **Reference sets:** 6 sets, 5 anchors = 30 진술 — App. C.1 에 명시
- **Prompts:** App. A.4 + App. B 에서 system prompt, user prompt, follow-up prompt 전문 공개

### 5.2 ❌ 비공개 자산

- **57개 survey 원본:** Colgate-Palmolive proprietary → 외부 연구자 재현 불가
- **9,300 human response:** 비공개
- **Product concept images:** 일부만 App. B 에 surrogate example (Fig. 5, AURAFOAM)
- **Demographic distribution:** summary statistics 만 공개

### 5.3 재현 가능성 평가

| Layer | Status |
|---|---|
| 알고리즘 | ✅ 완전 재현 가능 |
| Reference anchors | ✅ 재현 가능 |
| Synthetic panel 생성 | ✅ 다른 도메인에서도 재현 가능 |
| **Human baseline 비교** | ❌ **Colgate-Palmolive data 없이는 검증 불가** |
| Cross-domain transfer | ❓ 미검증 (논문에서도 인정) |

→ **방법론은 재현 가능, 결과는 부분 재현 가능**. 독자는 본 알고리즘을 자기 survey data 에 적용해 *상대적* 성능 비교는 가능, *절대적* ρ 90% 는 검증 불가.

### 5.4 확장성 (Scaling properties)

논문에서 보고하지 않지만 본질적 한계:
- **Cost:** 9,300 synthetic consumer × 57 survey = ~530,000 LLM call. GPT-4o 기준 ~$5,000~15,000 (추정)
- **Latency:** SSR 은 2-stage (free-text + embedding similarity) — DLR 의 ~3배 소요
- **Embedder cache:** anchor embedding 은 1회 계산 후 재사용 가능 → marginal cost 는 free-text generation 만

---

## 6. BB 포트폴리오 적합성 (Brown Biotech Portfolio Fit)

### 6.1 직접 적용 (Direct applicability)

| BB Project | SSR 적용 | 강도 |
|---|---|---|
| **Anti-aging cosmetics** (BB 현재 제품 카테고리) | ✅ 직접 — Colgate-Palmolive 과 동일 도메인 (personal care). 신규 concept 의 synthetic focus group 으로 활용 가능 | 🟢 **HIGH** |
| **Peptide service** (peptide-service.vercel.app) | ✅ 적용 가능 — peptide formulation concept test 시 synthetic expert panel (endocrinologist + consumer 동시). 다만 training data sparsity (rare peptide) 우려 | 🟡 MEDIUM |
| **Paid Briefs** (decision-ready research) | ✅ methodology reference — "LLM 의 reasoning vs human expert" 의 정량적 correlation attainment 측정 framework. Brief 신뢰성 마케팅에 활용 | 🟡 MEDIUM |
| **biostatx** | 🟡 weak — 통계 도구 자체는 SSR 과 무관, 단 *synthetic patient data* 생성 시 anchor set 재설계로 적용 가능 | ⚪ LOW |

### 6.2 간접 / 방법론 전이 (Methodology transfer)

| BB capability | SSR 로 강화 가능한 부분 |
|---|---|
| **SoI (System of Intelligence)** — "reasoning layer" positioning | SSR 은 **literal implementation of "reasoning layer"** — raw LLM output (텍스트) → structured signal (Likert pmf) 로 변환. BB SoI 마케팅 자료에 case study 로 활용 |
| **ARP v27** — synthetic clinical expert panel | 현재 ARP v27 의 expert persona 가 5-point scale 로 일관성 있게 평가하는지 검증하는 데 SSR 의 correlation attainment framework 직접 적용. **현재 ARP 평가가 DLR 의 narrow distribution 문제** 를 겪고 있다면 즉시 개선 여지 |
| **Inventa (Korean-localized research partner)** | 한국어 anchor set 재설계 + KR consumer review corpus training 된 모델 (HyperClova, Naver CLOVA X) 에서 SSR 재현 → 한국 시장 synthetic panel 의 first mover |

### 6.3 "Brown Biotech 가 인용할 만한 핵심 1줄"

> "Likert 응답의 문제는 LLM 자체가 아니라 elicitation 방식이다. 텍스트로 우회 후 임베딩 유사도로 매핑하면 합성 panel 이 인간 test-retest reliability 의 90% 까지 도달한다 — 단, LLM training data 가 해당 도메인을 충분히 cover 하는 경우에 한해."

이는 BB 의 SoI positioning 과 정확히 일치 — "도구(LLM) 를 파는 게 아니라 추론(reasoning layer) 을 판다" 가 SSR 의 literal embodiment.

### 6.4 즉시 실행 가능 action item (Dr. OCM 승인 시)

1. **Peptide service 의 concept test 에 SSR 적용** — peptide-service.vercel/app 의 intake 후속으로 "synthetic end-user panel" 5-point satisfaction survey → BB 자체 product 의 human baseline 과 비교
2. **Inventa 의 한국어 anchor set 설계** — Personal care / peptide efficacy / trust 3개 construct, 5 anchor × 3 set = 15 진술. KR 모델 (CLOVA X) 에서 SSR 재현 검증
3. **ARP v27 의 synthetic expert panel 평가** — 현재 expert persona 의 평가 narrow distribution 을 SSR 로 재설계, correlation attainment 정량 측정
4. **brownbio.tech blog post:** "왜 LLM 은 Likert 1~5 에 답하지 못하는가" — SSR 방법론을 BB SoI positioning 의 사례 연구로

---

## 7. 인용 가이드 (Citation)

본 페이퍼를 BB 자료에서 인용할 때:

```
Maier, B. F., Aslak, U., Fiaschi, L., Rismal, N., Fletcher, K., 
Luhmann, C. C., Dow, R., Pappas, K., & Wiecki, T. V. (2025). 
LLMs Reproduce Human Purchase Intent via Semantic Similarity 
Elicitation of Likert Ratings. arXiv:2510.08338v3 [cs.AI].
```

핵심 통계 인용 시:
- "90% correlation attainment": GPT-4o SSR, image stimulus, T_LLM=0.5
- "90% of human test-retest reliability": 본문 claim, Fig. 2A.iii
- "KS similarity 0.88": GPT-4o SSR, mean over 57 surveys
- "제로샷이 LightGBM 감독학습 능가": App. D, ρ 88.3% vs 64.6%, p < 10⁻²⁰

---

## 8. 연관 페이퍼 (Related Work — 인용 정리)

| Ref | Paper | BB relevance |
|---|---|---|
| Argyle 2023 (Pol. Analysis) | "Out of one, many" — demographic persona LLM simulation | 🟡 methodology reference |
| Bisbee 2024 (Pol. Analysis) | "Synthetic replacements for human survey data" — LLM 의 한계 명시 | 🟡 SSR 이 답하는 문제 |
| Brand 2024 (HBS WP) | "Using LLMs for market research" | 🟡 direct competitor to SSR |
| Li 2024 (Marketing Science) | Open completions → brand similarity | 🟡 SSR 의 predecessor |
| Argyle, Salecha 2024 | LLM social desirability bias | 🔴 SSR 이 우회하는 issue |

→ **SSR 은 synthetic consumer literature 의 명확한 improvement** — narrow distribution problem 을 정량적으로 해결한 첫 systematic study.

---

## 9. Open Questions / Follow-up

1. **Cross-cultural replication** — 동일 anchor set 이 KR / JP / EU market 에서도 90% ρ 유지? (BB Inventa 와 직결)
2. **Multi-modal anchor** — text-only vs image-only vs multimodal anchor 의 비교
3. **Domain-specific embedding** — `text-embedding-3-small` 대신 personal care / clinical / B2B domain-specific encoder 사용 시 ρ 개선 여부
4. **Dynamic anchor generation** — LLM 이 anchor 자체를 만들고, 인간 소량 data 로 fine-tune (DPO or RLHF) 하는 hybrid 방법
5. **Longitudinal panel** — 동일 synthetic consumer 가 6개월 후 재평가 시 일관성 (실제 인간은 brand fatigue, learning effect)
6. **Cost-benefit frontier** — Human n=300 panel vs synthetic n=10,000 panel 의 (cost, ρ, downstream decision quality) Pareto curve

---

## 10. "What did I miss?" (Dr. OCM Checkpoint)

이 분석에서 빠진 것:

- **Bias 측면의 deep dive** — 본 paper 는 positivity bias, acquiescence bias 를 *다루지 않음* (인용만). SSR 이 이런 human bias 를 얼마나 재현/완화하는지 정량 데이터 없음
- **Hallucination risk** — §5 에서 언급만, 정량 평가 없음. Synthetic response 가 factual claim (예: "sulfate-free, prebiotic hydration") 을 그럴듯하게 fabricate 하는지 측정 필요
- **Ethical framing** — synthetic consumer 가 *실제 인간* survey 참여를 대체할 때의 informed consent / IRBs / 마케팅 윤리 이슈는 본 paper 범위 외
- **Comparisons to commercial synthetic panel providers** (e.g., Persona by Delineate, Synthetic Users, OASIS) — 학술 SSR vs 상용 product 의 benchmark 비교 없음
- **2026년 후속 작업** — 본 paper 가 preprint (arXiv, peer-review 미확인) 인지, 동일 그룹의 follow-up 이 나왔는지 별도 확인 필요 (arxiv 2510.08338v3 latest)

→ 위 5개 항목 중 Dr. OCM 이 우선순위 표시 시 follow-up 분석 진행.


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

