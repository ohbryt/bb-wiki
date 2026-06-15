---
title: Arp27 Vs Claw Ai Lab Analysis
created: 2026-06-14
updated: 2026-06-14
type: comparison
tags: ["ai"]
sources:
  - raw/ARP27_vs_Claw_AI_Lab_Analysis.md
contradictions: []
---

# ARP v27 vs Claw AI Lab vs Multi-Agent Research 경쟁 분석

**Date:** 2026-06-06
**Author:** Brown Biotech ARP v27 team
**Context:** Claw AI Lab (arXiv 2605.22662, 21 May 2026) 영감을 drug discovery 도메인에 이식

## 1. 시스템 비교 매트릭스

| 시스템 | 날짜 | 도메인 | 핵심 기여 | Mode 수 | Anti-fab | Sandbox | Empirical Eval | 도메인 적응 |
|--------|------|--------|----------|---------|----------|---------|----------------|-------------|
| **AI Scientist v1** (Lu et al. 2024) | 2024-08 | AI research | First end-to-end automated discovery | 1 (single pipeline) | ❌ | ❌ | AI conf papers | general |
| **AI Scientist v2** (Yamada et al. 2025) | 2025-04 | AI research | Agentic tree search | 1 (tree) | ❌ | ❌ | workshop-level | general |
| **AgentLaboratory** (Schmidgall et al. 2025) | 2025 | Multi-domain | LLM as research assistant | 3 phases | ❌ | ❌ | EMNLP findings | general |
| **AI Co-Scientist** (Gottweis et al. 2025) | 2025-02 | Scientific | Multi-agent debate, tournament | tournament | ❌ | ❌ | biotech use cases | scientific |
| **Robin** (Ghareeb et al. 2025) | 2025-05 | Automation | Multi-agent scientific discovery | 1 | ❌ | ❌ | biotech tasks | scientific |
| **DeepResearcher** (Zheng et al. 2025) | 2025-12 | Web research | RL-based real environment | 1 | ❌ | ❌ | EMNLP benchmark | web |
| **AutoResearchClaw** (Liu et al. 2026) | 2026 | AI research | Hidden prompt-to-paper pipeline | 1 | ❌ | ❌ | 4 topics | general |
| **Claw AI Lab** (Wu et al. 2026) | 2026-05 | AI research | Lab-native, Claw-Code Harness, 5 layers, 3 modes | **3 (Explore/Discussion/Reproduce)** | ✅ | ✅ | 4 topics | **general + AI** |
| **ARP v27 / PRISM** (Brown Biotech 2026) | 2026 | **Drug discovery** | ZIP-RC + IOA self-critique, 3 engines, 5 diseases × 33 targets | 1 (sequential) | ❌ → **구현 중** | ❌ → **구현 중** | internal | **drug discovery** |

## 2. Claw AI Lab vs ARP v27 — Detail

### 2.1 아키텍처

```
Claw AI Lab (5 layer pyramid):        ARP v27 (현재):
  IDEA       — multi-agent debate       Discovery (RAG + ZIP)
  PLANNING   — tasks/milestones         → (없음 — sequential)
  CODING     — Claw-Code Harness        → (없음)
  EXPERIMENT — compute + metrics         Validate (Bayesian ranking)
  WRITING    — outline → manuscript      Report (Notion)

Cross-layer feedback: ✅                Cross-layer feedback: ❌
```

### 2.2 5-Dimension 비교

| Dimension | Claw | ARP v27 | Gap |
|-----------|------|---------|-----|
| **Compression/Context** | Token-aware, AST, shell pattern | RAG + MedGemma + Qwen | ARP 약간 우위 (의·생명 도메인) |
| **Routing/Mode selection** | 3 modes (Explore/Discussion/Reproduce) | Sequential | **큰 갭** — 3 modes 미구현 |
| **Memory/Persistence** | Session memory, artifact inspection | Notion DB | 동등 |
| **Verification/Anti-fab** | Anti-fabrication, NaN/Inf, smoke tests | 없음 | **큰 갭** — 이제 구현 중 |
| **Tool integration** | 6 tools (bash/read/write/edit/glob/grep) | 4 MCP tools (pubmed/fetch/mfds/tournament) | **큰 갭** — 16 tools 확장 중 |

### 2.3 Reproducibility (가장 큰 격차)

| 측면 | Claw | ARP v27 |
|------|------|---------|
| Reproduce mode | ✅ (Topic 4에서 +5.0) | ❌ |
| 외부 paper claim 검증 | ✅ | ❌ |
| **Paid brief 차별화 가능** | — | ✅ 가능 ("Verified by ARP v27") |

→ **Verify mode**가 Brown Biotech의 가장 큰 차별화 기회.

### 2.4 Harness layer

| 측면 | Claw-Code Harness | ARP v27 DrugDiscoveryHarness (신규) |
|------|-------------------|--------------------------------------|
| Tools | 6 (general) | 16 (drug-specific) |
| Sandbox | ✅ | ✅ (Docker, optional) |
| Time budget | ✅ | ✅ |
| NaN/Inf detection | ✅ | ✅ |
| Anti-fabrication | ✅ (general) | ✅ (drug-specific: SMILES, IC50, docking) |
| Metric recording | ✅ | ✅ (.prism_runs/{run_id}/metrics.jsonl) |
| Rollback | ✅ | ✅ (rollback_artifact tool) |
| Rollback granularity | One-click | Per-artifact SHA256 |

## 3. ARP v27 우선순위 (Claw에서 차용할 것)

### P0 (즉시, 4주)
- [x] **Harness skeleton** — `integration/harness/` (16 tool stubs, validators, controller, modes)
- [ ] **Backend 연결** — docking_verification_gate, keap1_dti_scorer 등 기존 integrator 연결
- [ ] **Docker sandbox image** — Dockerfile 작성됨, build + smoke test 필요
- [ ] **Anti-fabrication 운영** — paid-brief production pipeline에 integration

### P1 (4-8주)
- [ ] **5-layer pipeline** — Idea + Plan + Code layers 추가, cross-layer feedback loop
- [ ] **Notion live event stream** — agent 활동의 real-time dashboard
- [ ] **Verify mode 완성** — 외부 paper claim reproducibility 자동화 (Brown Biotech 차별화)
- [ ] **Citation validator** — 인용된 paper의 실제 claim 추출 + cross-check

### P2 (8-12주)
- [ ] **Rollback semantics** — layer별 snapshot, 1-click restore
- [ ] **Council mode 강화** — ZIP-RC + IOA loop을 Claw의 Discussion mode 패턴으로 재구조화
- [ ] **Council vs Verify A/B** — Brown Biotech 도메인에서 어떤 mode가 더 효과적인지 empirical eval
- [ ] **Public benchmark** — 5대 외부 multi-agent (AutoResearchClaw, AI Scientist v2, AgentLaboratory, Robin, Co-Scientist)와 drug discovery task에서 직접 비교

## 4. 전략적 함의

### 4.1 Brown Biotech 강점 (유지)
1. **도메인 특화** — drug discovery에 5년 노하우 + 실제 임상/제약 네트워크
2. **Notion 운영 허브** — daily triage, weekly review, paid-brief pipeline
3. **SoI 포지셔닝** — "reasoning layer" 판매 모델
4. **Anti-fabrication 필요성** — drug discovery에서 hallucinated IC50 / fake SMILES는 안전 위험 → Claw이 이미 강조했지만 drug-specific 구현은 미흡 → **Brown Biotech이 lead 가능**

### 4.2 Brown Biotech 약점 (해소)
1. **Harness layer 부재** → Claw이 앞서 있음 → **지금 구축 중**
2. **Reproduce mode 없음** → paid-brief 차별화 기회 → **Verify mode 구현**
3. **Empirical evaluation 약함** → 5 diseases × 33 targets의 internal만 → **외부 paper reproducibility 공개 benchmark**가 가장 효과적인 external validation

### 4.3 차별화 전략

| 전략 | ROI | 비고 |
|------|-----|------|
| **Verify mode paid-brief 통합** | ★★★★★ | reproducibility 보고서 = unique value |
| **Drug-specific anti-fabrication** | ★★★★★ | Claw general → 우리는 SMILES/IC50/docking |
| **5-layer pipeline + cross-layer feedback** | ★★★★ | 학습 loop 자동화 |
| **Public benchmark vs 4 multi-agent** | ★★★★ | marketing + research combo |
| **Council mode 강화** | ★★★ | ZIP-RC + IOA 이미 강력 |

## 5. Action Items

1. **(이번 주)** Harness backend 연결 — `docking_verification_gate`, `keap1_dti_scorer` 등 기존 integrator를 TOOL_REGISTRY backend로 등록
2. **(이번 주)** Docker image build + smoke test
3. **(다음 주)** Verify mode — 외부 paper reproducibility 자동화 (Rabbit Test)
4. **(2주 후)** 5-layer pipeline refactor 시작
5. **(1개월 후)** Public benchmark — AutoResearchClaw / AI Scientist v2 / AgentLaboratory / Robin / Co-Scientist vs ARP v27 on drug discovery task

## 6. References

- Claw AI Lab: [arXiv 2605.22662](https://arxiv.org/abs/2605.22662)
- AI Scientist v1: arXiv 2408.06292
- AI Scientist v2: arXiv 2504.08066
- AgentLaboratory: EMNLP 2025 Findings
- AI Co-Scientist: arXiv 2502.18864
- Robin: arXiv 2505.13400
- DeepResearcher: EMNLP 2025
- AutoResearchClaw: https://github.com/aiming-lab/AutoResearchClaw
- UltraWorkers / Claw Code: https://github.com/ultraworkers/claw-code

---

*Last updated: 2026-06-06 by Brown Biotech ARP v27 team*


## 4-섹션 판단 레이어

### 1. Source Quotes

- "Claw AI Lab (Wu et al. 2026, arXiv 2605.22662) implements 5-layer pyramid: IDEA → PLANNING → CODING → EXPERIMENT → WRITING, with cross-layer feedback." — Claw AI Lab paper, §3 Architecture
- "ARP v27 (Brown Biotech 2026) currently uses sequential pipeline: Discovery (RAG + ZIP) → Validate (Bayesian ranking) → Report (Notion), with no cross-layer feedback." — internal analysis, §1
- "5-Dimension comparison: Routing/Mode selection — Claw has 3 modes (Explore/Discussion/Reproduce), ARP v27 has 1 (sequential). **큰 갭**." — internal analysis, §2.2
- "Verification/Anti-fabrication: Claw has Anti-fab, NaN/Inf detection, smoke tests. ARP v27 has none. **큰 갭** — 이제 구현 중." — internal analysis, §2.2
- "Reproduce mode in Claw showed +5.0 improvement on Topic 4" — Claw AI Lab paper, §Empirical Eval

### 2. My Interpretation

- **3-mode routing (Explore/Discussion/Reproduce)** = ARP v27 의 **가장 큰 단기 갭**. Drug discovery 도메인에서는 "explore targets" → "debate with experts" → "reproduce literature" 위계가 더 의미 있음
- **Anti-fabrication layer** = Paid Brief 작성 시 critical (₩2M~8M 의사결정 산출물에 hallucinated citation은 reputation kill)
- **Sandbox tool execution** = 현재 BB의 MCP tool 4개 (pubmed, fetch, mfds, tournament) 가 sandboxed container 에서 실행되지 않음 — hallucinated SQL/query 가 filesystem 을 건드릴 위험
- **5-layer pyramid 의 IDEA-PLANNING 분리** = BB에 없는 영역. ARP v27은 target list 가 hard-coded (14 query family), PLANNING layer 가 없음
- **Reproduce mode 의 +5.0** = BB가 drug discovery 에서 가장 활용 가치 있는 mode — Known paper reproduce → "우리 모델이 재현 가능한가" 검증

### 3. Open Questions

- ARP v27 에 Claw-style 3-mode routing 추가 시 drug discovery context-specific design 은? (Mode names 도 drug discovery 친화적으로: "Explore Targets" / "Discuss Mechanism" / "Validate Experiment"?)
- Anti-fab layer 의 BB-domain 구현 — citation hallucination detection + numerical sanity check (e.g., docking score > −15 kcal/mol = flag) 둘 다 필요?
- 16 tools 확장 중 (현재 4 MCP tools) — 우선순위는? (예: ChEMBL/PubChem direct query, BLAST, AlphaFold server, docking software)
- Claw AI Lab 의 "general + AI" 도메인 적응을 drug discovery 에 적용할 때 domain-specific knowledge base (PubMed, ChEMBL, ClinicalTrials) 의 injection 전략은?
- Sandbox 가 Docker container 면 reproducibility 가 좋아지지만, MCP tool 들이 in-container init 필요한 경우 cold-start latency — 1-2초 vs 5-10초 tradeoff

### 4. Contradictions

- **현재 없음** — 신규 페이지.
- **잠재 충돌 후보**: Claw AI Lab 의 "Topic 4: +5.0" 결과가 drug discovery 에는 transfer 안 된다면 (예: code generation 에 특화) → Claw 3-mode 의 drug discovery 적합성 재평가 필요

## 관련 페이지

- [[livia_deep_analysis]] — BB 의 protein interaction validation tool, ARP v27 의 validate 단계와 연결
- [[scgpt_deep_analysis]] — BB stack 의 single-cell AI component
- [[agentic_patterns_brownbiotech_mapping]] — BB의 agentic design patterns coverage (76%)
- [[claw_ai_lab_brief]] — Claw AI Lab 원본 brief, 5-layer architecture
- raw/ARP27_vs_Claw_AI_Lab_Analysis.md (원본 deep-dive)

