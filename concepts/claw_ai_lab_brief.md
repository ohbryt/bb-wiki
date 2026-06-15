---
title: Claw Ai Lab Brief
created: 2026-06-14
updated: 2026-06-14
type: concept
tags: ["ai"]
sources:
  - raw/Claw_AI_Lab_Brief.md
contradictions: []
---

# Claw AI Lab — Paper Brief

**원본:** Wu et al. 2026, "Claw AI Lab: An Autonomous Multi-Agent Research Team"
**arXiv:** [2605.22662v1](https://arxiv.org/abs/2605.22662) (21 May 2026)
**Authors:** Fan Wu, Cheng Chen, Zhenshan Tan, Dingcheng Gao, Lanyun Zhu, Tianrun Chen, Deheng Ye, Taiyu Zhang, Qi Zhu, Yi Tan, Deyi Ji, Xinzhen Xu, Yanyu Qian, Guosheng Lin, Fayao Liu
**Affiliations:** NTU, A*STAR, Moxin Technology, NUIST, THU, USTC
**GitHub:** https://github.com/Claw-AI-Lab/Claw-AI-Lab

## 1. 핵심 주제

Lab-native autonomous research platform — 단일 prompt로 full research team 인스턴스화, customizable roles, collaborative workflows, real-time monitoring, artifact inspection, rollback/resume, unified dashboard. 단순 prompt-to-paper pipeline이 아니라 **interactive AI laboratory**로의 전환.

## 2. 아키텍처 — 5 Layer Pyramid

```
Layer 5: WRITING      → Outline, figures, draft, review → final manuscript
Layer 4: EXPERIMENT   → Compute & storage, metric & logs
Layer 3: CODING       → Read & Understand, Tools Call, Coding, Test → Finalize
Layer 2: PLANNING     → Decompose ideas → tasks/milestones → "Good Enough?" loop
Layer 1: IDEA         → Multi-agent discussion, parallel proposals → consensus
```

Cross-layer feedback: 실험 실패 → plan revise, 반복 실패 → idea revisit.

## 3. Claw-Code Harness (가장 큰 기여)

> "Claw-Code Harness, which connects local codebases, datasets, and checkpoints to runnable experiments and feeds execution artifacts back into the research loop."

핵심 기능:
- **Local asset inspection** — codebases, datasets, checkpoints read
- **Agentic coding loop** — controlled tools: bash, read, write, edit, glob, grep
- **Sandboxed workspace** — per-task isolation
- **Read-only Python controller** — time-budget enforcement, metric reporting, result finalization, NaN/Inf detection
- **Smoke tests + anti-fabrication** — fake metric / placeholder / mock detection

성능: AutoResearchClaw 대비 +15.5 ~ +16.5 (3 topics), +5.0 (reproduction), ChatGPT/Gemini 양 evaluator 일관.

## 4. 3 Modes

| Mode | Use |
|------|-----|
| **Explore** | 아이디어 발산 |
| **Discussion** | Multi-agent debate, consensus |
| **Reproduce** | 기존 논문 reproducibility 검증 (가장 차별화) |

## 5. Model Stack (실험)

- **Main + coding:** GPT-5.4
- **Figures:** Gemini-3-Pro-Image-Preview
- **Fallback:** Qwen3.5-Plus / Qwen-Plus
- **Baseline (AutoResearchClaw):** GPT-5.4 + Gemini-2.5-Pro-Flash-Image + GPT-4o/mini

## 6. Brown Biotech 대비

| 측면 | Claw AI Lab | ARP v27 |
|------|-------------|---------|
| 도메인 | General AI research (5 case studies) | Drug discovery (5 diseases × 33 targets) |
| Backend integration | bash + 파일 system | ChEMBL, PubMed, GEO, OpenAlex (예정) |
| Reproducibility | Reproduce mode | 없음 — **Verify mode로 이식 필요** |
| Anti-fabrication | Yes (read-only controller) | 없음 — **harness에 구현** |
| Cross-layer feedback | Yes | 없음 (sequential) |
| Human checkpoint | Real-time monitoring + rollback | Notion (수동) |
| 평가 방법 | 6-dim LLM judge | internal only |

## 7. Take-aways for ARP v27

1. **DrugDiscoveryHarness 패턴** — Claw-Code Harness를 drug discovery 도메인으로 변환 (16 tools)
2. **Anti-fabrication** — citation integrity, SMILES validity, plausible IC50/docking ranges
3. **5-layer pipeline** — ARP v27은 현재 Discovery→Validate→Report, Idea+Plan+Code layer 추가 필요
4. **Verify mode = 핵심 차별화** — paid-brief에 "Verified by ARP v27" 마크
5. **Sandbox** — Docker container per target, time-budget, metric recording

## 8. 인용 시

Wu, F. et al. (2026). *Claw AI Lab: An Autonomous Multi-Agent Research Team.* arXiv:2605.22662.

PDF: `literature/Claw_AI_Lab_Wu2026_arXiv_2605.22662.pdf`
상세 분석: `literature/ARP27_vs_Claw_AI_Lab_Analysis.md`
Harness 구현: `integration/harness/`


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

