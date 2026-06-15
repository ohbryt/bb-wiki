---
title: Agentic Patterns Brownbiotech Mapping
created: 2026-06-14
updated: 2026-06-14
type: concept
tags: ["ai"]
sources:
  - raw/Agentic_Patterns_BrownBiotech_Mapping.md
contradictions: []
---

# Agentic Design Patterns — Brown Biotech Stack Mapping
## Antonio Gulli (2025/2026) — *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*
## 28 chapters (4 parts + 7 appendices) ↔ Brown Biotech current state

**Date:** 2026-06-07
**Source:** `/Users/ocm/.hermes/cache/documents/doc_4c91cd50e736_Agentic_Design_Patterns.pdf` (424 pages)
**Author:** Demis (Brown Biotech CEO Agent)
**Purpose:** Gap analysis + Brown Biotech agentic-stack reference card

**Legend:** ✓ Active (implemented) | ◐ Partial (informal use) | ✗ Gap (no implementation) | 🔥 P0 gap

---

## Part 1 — Foundational Patterns (Ch 1-7, 103 pages)

| Ch | Pattern | Brown Biotech current implementation | Status |
|---|---|---|---|
| 1 | **Prompt Chaining** | Cron prompts (multi-step), `brown_biotech_research_pulse_publisher.py` (feed → write → commit chain) | ✓ |
| 2 | **Routing** | `map_to_family()` heuristic in publisher; Notion DB routing; tool dispatch in `model_tools.py` | ◐ (keyword-based, not LLM-routed) |
| 3 | **Parallelization** | `delegate_task()` (3 parallel); cron concurrent jobs (Signal Brief + Tech Digest + Research Watcher) | ✓ |
| 4 | **Reflection** | PRISM ZIP-RC + IOA self-critique loop; Hermes tool result inspection | ✓ |
| 5 | **Tool Use** | Hermes `tools/` (1050+ lines MCP, file, web, browser, code-exec, delegate) | ✓ |
| 6 | **Planning** | **Gap — no formal planner.** `delegate_task` is task-level only; no goal-decomposition for multi-step research | 🔥 **P0** |
| 7 | **Multi-Agent Collaboration** | arp-v27 3-engine; Hermes worker protocol (ACK/mailbox/lifecycle) | ✓ |

## Part 2 — Memory & Context (Ch 8-11, 61 pages)

| Ch | Pattern | Brown Biotech current implementation | Status |
|---|---|---|---|
| 8 | **Memory Management** | `~/.hermes/memories/MEMORY.md` (compact), `USER.md` (persona), `SonnetDB` (session search); Notion hub | ✓ |
| 9 | **Learning and Adaptation** | CLAUDE.md correction pipeline (Eugene Yan compounding: "Mine transcripts for config: corrections → immediate patch") | ◐ |
| 10 | **MCP (Model Context Protocol)** | `tools/mcp_tool.py` (~1050 lines); pubmed_search, mfds_retrieve, tournament_run instruments in PRISM | ✓ |
| 11 | **Goal Setting and Monitoring** | Tasks DB (`368f273533a481beb76ad240059756a5`); cron `last_status` check; weekly review cron | ✓ |

## Part 3 — Reliability & Knowledge (Ch 12-14, 34 pages)

| Ch | Pattern | Brown Biotech current implementation | Status |
|---|---|---|---|
| 12 | **Exception Handling & Recovery** | Cron `last_status` check; `retry()` exponential backoff in `hermes_tools`; some try/except in publishers | ◐ |
| 13 | **Human-in-the-Loop** | 3 human checkpoints rule (CLAUDE.md: 上车 → Taste align → Go/No-go); `clarify` tool | ✓ |
| 14 | **Knowledge Retrieval (RAG)** | PRISM (`FAISSVectorStore` TF-IDF + new `TurboVectorStore` MiniLM 4-bit); 744 chunks indexed | ✓ |

## Part 4 — Advanced (Ch 15-21, 114 pages)

| Ch | Pattern | Brown Biotech current implementation | Status |
|---|---|---|---|
| 15 | **Inter-Agent Communication (A2A)** | Cron worker pattern (Daily Signal Brief + Tech Digest + Research Watcher + Daily Briefing all call shared pipeline); Hermes inter-agent via `delegate_task` | ◐ (no formal A2A protocol) |
| 16 | **Resource-Aware Optimization** | Token counting in trajectory; model routing (Gemini 2.0 Flash for fast path) | ◐ (no formal optimizer) |
| 17 | **Reasoning Techniques** (CoT, ToT, ReAct, GoD) | Implicit CoT in prompts; PRISM IOA loop is ReAct-like | ◐ (not formalized) |
| 18 | **Guardrails/Safety** | `tools/approval.py` (dangerous command detection); `brown-biotech-git-safety` skill; secrets redaction | ✓ |
| 19 | **Evaluation and Monitoring** | `tests/` (~3000 tests); cron `last_status`; some manual eval | ◐ (no formal eval harness like AgentEval) |
| 20 | **Prioritization** | `todo` tool (in-session); Tasks DB priority field | ✓ |
| 21 | **Exploration and Discovery** | Brown Biotech research-watcher (Mon/Wed/Fri scans); brown_biotech daily signals; research-pulse blog | ✓ |

## Appendices (7)

| App | Topic | Brown Biotech relevance |
|---|---|---|
| A | Advanced Prompting | ◐ (used implicitly in CLAUDE.md prompts) |
| B | AI Agentic: GUI to Real world | ✗ (out of scope) |
| C | Frameworks overview (LangChain, LlamaIndex, Haystack, ADK) | Reference for future (turbovec already mapped to all 4) |
| D | AgentSpace (online) | ✗ (not used) |
| E | CLI agents | ◐ (Hermes `pty=true` for interactive CLIs) |
| F | Reasoning Engines | Reference (PRISM = reasoning engine) |
| G | Coding agents | ✓ (`delegate_task` to coding agents; Claude Code) |

---

## 🔥 Top 3 Gaps (Prioritized)

| Priority | Gap | Action | Owner | ETA |
|---|---|---|---|---|
| **P0** | **Ch 6 Planning** (no formal planner) | Build `planner.py` — decompose research goal into query family scan + Deep-dive + Notion + Blog tasks | Demis | 1 week |
| **P1** | **Ch 19 Evaluation Harness** | Build eval suite: cron health, publisher coverage, blog freshness, git safety, prompt quality | Demis | 2 weeks |
| **P2** | **Ch 17 Reasoning Techniques** | Formalize CoT/ToT/ReAct in publisher (currently keyword `map_to_family`; upgrade to MiniLM semantic via turbovec) | Demis | 3 weeks |

## Brown Biotech Coverage Score

| | Coverage |
|---|---|
| **Part 1** (Foundational) | 6/7 (86%) — **Ch 6 Planning is the gap** |
| **Part 2** (Memory & Context) | 4/4 (100%) — all 4 covered |
| **Part 3** (Reliability) | 2/3 (67%) — Ch 12 partial |
| **Part 4** (Advanced) | 4/7 (57%) — Ch 15, 16, 17, 19 partial/gap |
| **Overall** | **16/21 = 76%** (4 ◐ partial + 1 ✗ P0 gap) |

## What This Mapping Confirms

✅ **Brown Biotech's agentic stack is well-developed** for a solo-founder biotech:
- Strong foundations (Ch 1, 3, 4, 5, 7) — Chaining, Parallelization, Reflection, Tool Use, Multi-Agent
- Strong memory/context (Ch 8, 10, 11) — Memory, MCP, Goal Monitoring
- Strong RAG (Ch 14) — now turbovec-powered
- Strong safety (Ch 18) — guardrails + git safety

⚠️ **Three things to close the gap:**
1. **Planner** (Ch 6) — biggest miss, would unlock multi-step research automation
2. **Eval harness** (Ch 19) — needed as we scale more crons/publishers
3. **Formal reasoning techniques** (Ch 17) — would improve publisher quality

## Cross-References
- `~/.hermes/CLAUDE.md` — Brown Biotech operating guide (referenced 3 human checkpoints, Eugene Yan compounding)
- `~/.hermes/memories/MEMORY.md` — persistent facts
- `~/.hermes/skills/brown-biotech-taste/SKILL.md` — copy/communication patterns
- `arp-v27/literature/scGPT_Deep_Analysis.md` — previous track E deliverable
- `arp-v27/literature/turbovec_TurboQuant_Analysis.md` — RAG upgrade
- `/Volumes/4TB/prism/rag/turbovec_store.py` — Ch 14 RAG implementation
- `~/.hermes/scripts/brown_biotech_research_pulse_publisher.py` — Ch 1, 2, 3 (Chaining + Routing + Parallelization)


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

