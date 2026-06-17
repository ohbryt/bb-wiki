---
title: Harness Engineering
created: 2026-06-17
updated: 2026-06-17
type: concept
tags: ["ai", "methodology"]
sources:
  - https://github.com/wquguru/harness-books
  - companion-skill: arp-v27-harness
related:
  - claw_ai_lab_brief
  - agi-to-asi-pathways-bb-context
  - agentic_patterns_brownbiotech_mapping
contradictions: []
---

# Harness Engineering

> AI 모델이 위험한 이유는 가끔 틀려서가 아니라, **틀렸을 때를 처리할 구조가 없는 시스템**이 위험하다.
> — `wquguru/harness-books`, Book 1 Ch9

**Source:** [`wquguru/harness-books`](https://github.com/wquguru/harness-books) (2.5k ⭐, GitHub, 2026)
- **Book 1**: *Harness Engineering: A Design Guide to Claude Code* — Claude Code 런타임 구조 분석
- **Book 2**: *The Harness Design Philosophies of Claude Code and Codex* — 두 시스템 비교

## What it is

코드 생성 AI를 "똑똑한 도구"가 아니라 **제약·실행·복구·검증·조직 규칙을 가진 시스템**으로 다루는 학문/공학. 단순한 프롬프트 엔지니어링을 넘어서, **7개 기관 (prompt · query loop · tool 권한 · context 거버넌스 · 오류 복구 · 다중 에이전트 검증 · 팀 제도)** 의 결합으로 모델의 불안정성을 시스템 차원에서 흡수한다.

핵심 질문:
1. 불안정한 모델의 출력을 어떻게 시스템 안에 묶어둘 것인가
2. 실수가 발생했을 때 시스템은 어떻게 복구되는가
3. 누가, 어떤 구조로, 최종 책임을 지는가

## The 10 Principles (canonical, Book 1 Ch9)

| # | Principle | 한 줄 |
|---|---|---|
| 1 | Models are unstable components, not teammates | 신뢰는 시스템이 아니라 모델에 기대지 않음 |
| 2 | Prompt is part of the control plane | 프롬프트는 persona가 아니라 제어 신호 |
| 3 | Query loop is the heartbeat | continuous execution loop가 runtime의 본체 |
| 4 | Tools are managed execution interfaces | 도구는 권한·중단·로깅이 붙은 인터페이스 |
| 5 | Context is working memory, not a dump | 컨텍스트는 거버넌스 대상 (compact는 예산) |
| 6 | Error paths are main paths | 오류 경로는 first-class, post-incident patch 아님 |
| 7 | Recovery should optimize for continuation | recap보다 continuation 우선 |
| 8 | Multi-agent partitions uncertainty | research / impl / verify / synthesis를 별도 컨테이너로 |
| 9 | Verification must be independent | 검증은 별도 role, ideally 독립 owner |
| 10 | Team institutions > personal tricks | layered CLAUDE.md · hooks · skills · transcripts |

## BB Coverage Map (Book 1 챕터 ↔ BB 인프라)

| Book 1 | BB 컴포넌트 | Status |
|---|---|---|
| Ch2 Prompt is control plane | `agent/prompt_builder.py` + skin engine + command registry | ✅ |
| Ch3 Query loop heartbeat | `run_agent.py` 동기 루프 + max_iterations + iteration_budget | ✅ |
| Ch4 Tools/permissions/interrupts | `tools/approval.py` + toolset 시스템 | ✅ |
| Ch5 Context/memory/compact | `context_compressor.py` + `prompt_caching.py` + MEMORY + AGENTS.md | ✅ |
| Ch6 Errors and recovery | `brown-biotech-cron-silent-failure-diagnostics` skill | ✅ |
| Ch7 Multi-agent & verification | 4-agent pipeline + feature factory + Soft-SVeRL rubric | ✅ |
| Ch8 Team adoption | skills hub + claude-mirror command pack | ✅ |
| Ch9 Ten principles | `arp-v27-harness/SKILL.md` canonical checklist | ✅ (new 2026-06-17) |

## Anti-slogan

> "모델이 똑똑하길 기다리지 말고, 시스템이 안전하길 만들어라."

## BB Paid Brief / ARP v27 연결

- **ARP v27 Verify mode (Soft-SVeRL)** = Principle 9 (independent verification)의 구현 — partial-credit graded verdict
- **4-agent pipeline** = Principle 8 (multi-agent partitions uncertainty)의 구현 — research / impl / verify / synthesis 분리
- **Paid Brief (₩2M~8M)** = Principle 10 (team institutions)의 구현 — 개인 노하우를 institutional artifact로 변환
- **bb-wiki (4-섹션 판단 레이어)** = Principle 2 (prompt is control plane)의 구현 — AI 요약과 사용자 voice를 강제 분리

## Source Quotes

1. "Harness Engineering asks how systems can still behave like engineering systems when models themselves are not reliable." — Book 1 Ch9.11
   Source: `https://github.com/wquguru/harness-books/blob/main/book1-claude-code/locales/en/chapter-09-ten-principles.md`
2. "Models may speak like teammates, but they do not automatically gain teammate-grade stability, accountability, or sustained judgment. The earlier this is acknowledged, the earlier systems grow permission boundaries, recovery paths, verification gates, and rollback ability." — Book 1 Ch9.1
3. "Complexity remains complexity, but judgment is still required. Teams carry principles forward, not function names from one source version." — Book 1 Ch9 (intro)

## My Interpretation

BB는 이 책이 제시하는 harness 패턴의 **작동하는 구현 사례**다. 9/9 챕터 매핑이 成立하며, 특히 다음 3가지가 BB의 차별화 지점:

1. **독립 verification (Principle 9)** — Soft-SVeRL checklist의 partial-credit reward는 다른 harness (Claude Code / Codex) 가 제공하지 않는 graded verdict 기능. "Verified by ARP v27" 배지 + completeness pricing이 곧 Paid Briefs의 moat.
2. **컨텍스트 거버넌스 (Principle 5)** — bb-wiki의 4-섹션 판단 레이어 (Source Quotes / My Interpretation / Open Questions / Contradictions) 는 단순한 compact가 아니라 **"AI 요약과 사용자 voice의 강제 분리"**. An Lab (Korea Univ., 2026-06-13) pedagogy의 BB 구현.
3. **팀 제도 (Principle 10)** — skill hub + claude-mirror command pack + Notion operating hub는 layered CLAUDE.md의 BB 구현. 개인의 트릭을 institutional artifact로 변환.

## Open Questions

- **Book 2 비교 분석**: Claude Code vs Codex — BB는 어떤 디자인 결정을 차용해야 하는가? (특히 Codex의 "policy language" + sandbox 우선 접근)
- **Principle 7 audit**: BB의 silent-failure diagnostic이 "recovery should optimize for continuation" 원칙을 만족하는지? 현재는 failure detection 위주, continuation logic은 부족할 가능성
- **Principle 8 컨테이너 수**: 4-agent (plan / impl / verify / synthesize) 가 최적인가, 6-agent (plan / critique / verify / council / synthesize / audit) 로 확장 여지가 있는가?
- **Control plane의 정의**: BB의 "control plane"이 `prompt_builder.py`만인가, 아니면 Notion operating hub + cron scheduler + skill registry까지 포함하는가?
- **Principle 5 한계**: bb-wiki의 4-섹션이 강제되면, 빠른 research pulse 같은 lightweight content와 충돌하지 않는가? (현재 별도 research-pulse sidecar로 분리 중 — 정당화 필요)

## Contradictions

- [[claw_ai_lab_brief]] — Claw AI Lab은 "5-layer pyramid" (IDEA → PLAN → CODE → EXPERIMENT → WRITING) 로 harness를 표현하지만, 이 책은 "10 principles" 로 표현. 동일 개념의 다른 표상 — 5 layer는 **시간적 순서**, 10 principles는 **공간적 기관**. 직교가 아니라 보완.
- [[agi-to-asi-pathways-bb-context]] — DeepMind의 4 ASI pathway 중 Pathway 4 (multi-agent coordination) 는 harness engineering이 필요한 영역. BB는 Pathway 3 (recursive self-improvement) + 4에 집중하므로 두 framework는 직교가 아니라 **중첩**.
