# Wiki Log

> 시계열 액션 로그. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: create, ingest, update, query, lint, archive, delete, link

## [2026-06-15] create | KEAP1-NRF2 metabolic vulnerabilities query
- Type: query
- Created: queries/2026-06-15-keap1-nrf2-metabolic-vulnerabilities.md
- Source: PubMed filter (126 hits, 2018-2026, English) — top 8 by relevance
- Tags: #cancer #drug-discovery #ai #longevity
- Cross-references: timesfm (time-course RNA-seq), scgpt (NRF2-high subpop), ai-drug-discovery (HO-1 FPembed screen)
- 4-섹션: Source Quotes (8 abstracts) / My Interpretation (5 axes, 4 drug repurposable) / Open Questions (5) / Contradictions (none)
- 6 BB-actionable angles: CsA/PPIA, NADH-reductive 13% responder, GCLC/ferroptosis, LKB1×KEAP1/SHMT, HO-1/cisplatin, p62 hub
- 4 seed PMIDs cited (17020408, 20534738/PMC2920733, PMC6133308, PMC10189287)
- Companion: [[timesfm]] (XReg covariates for time-course), [[scgpt_deep_analysis]] (NRF2-high subpop), [[ai-drug-discovery]] (FPembed for HO-1)

## [2026-06-15] create | KEAP1-NRF2 IO biomarker & companion diagnostic query (sister)
- Type: query
- Created: queries/2026-06-15-keap1-nrf2-io-biomarker-companion-diagnostic.md
- Source: PubMed filter (298 hits, 2018-2026, English) — top 20 retrieved, top 8 by IO-relevance
- Tags: #cancer #biomarker #drug-discovery #ai
- Cross-references: 2026-06-15-keap1-nrf2-metabolic-vulnerabilities (sister), timesfm, scgpt_deep_analysis, ai-drug-discovery, arp27_vs_claw_ai_lab_analysis
- 4-섹션: Source Quotes (7 quotes) / My Interpretation (2024-2025 inflection, KEAP1 reframing, 9 total drug targets, GLS bridge) / Open Questions (8) / Contradictions (4)
- 8 BB-actionable companion-diagnostic / combo angles: POSEIDON dual ICB, MTAP-PRMT5, EMSY-PARP/STING, ATRi-LKB1, re-biopsy panel, 3-gene exclusion, glutaminase-ICB, neoadjuvant CIT exclusion
- **Product candidate identified: 3-tier "BB-IO Compass" diagnostic** (Tier 1: STK11/KEAP1/SMARCA4 exclusion + PD-L1 + TMB, Tier 2: LKB1/KEAP1/KRAS + EMSY + MTAP, Tier 3: re-biopsy resistance panel)
- Ancher papers: Skoulidis Nature 2024 (POSEIDON), Galan-Cobo Cancer Cell 2025 (HUDSON), Ricciuti JCO 2024 + JAMA Oncol 2025, Alessi JTO 2023
- Sister: [[2026-06-15-keap1-nrf2-metabolic-vulnerabilities]] (mechanism → drug axis)
- Combined drug axis count: 6 (q#1) + 4 (q#2 new) = **9 actionable drug targets**

## [2026-06-15] create | BB-IO Compass product spec (Tier 1 LDT)
- Type: concept (product spec, two pages — main + operations)
- Created: concepts/bb-io-compass.md (102 lines) + concepts/bb-io-compass-operations.md (181 lines)
- Tags added to SCHEMA: `#biomarker`, `#dx`
- **First Brown Biotech clinical product** (vs research services)
- Tier 1: STK11 + KEAP1 + SMARCA4 NGS + PD-L1 IHC (22C3) + TMB → 1st-line CIT decision in NSCLC
- 3-tier roadmap: Tier 1 (1st-line) → Tier 2 (alternative) → Tier 3 (acquired resistance)
- Path: LDT under CLIA + CAP, MVP 12 months, revenue Year 1 $0.5-1M, Year 3 $3-5M
- Pharma partnership anchor: AZN (POSEIDON, durvalumab+tremelimumab) — STK11/KEAP1 subset = BB Tier 1 directly validated
- Pricing: $1,000/test (Medicare CPT 81445 + 88360 + 81479 + professional), 600-800 tests break-even
- CAPEX: $650-900K (Year 1); OPEX: $550K/yr
- Cross-references: 2026-06-15-keap1-nrf2-io-biomarker-companion-diagnostic (evidence base), 2026-06-15-keap1-nrf2-metabolic-vulnerabilities (mechanism), timesfm, scgpt_deep_analysis, ai-drug-discovery
- Sister genox-site (Korean consumer genomics, B2C longevity) — BB-IO Compass 는 B2B clinical → **두 라인 분리 운영**
- 4-섹션: both pages (main + operations) — split to keep each <200 lines
- Decision matrix: 6 patient profiles × 4 biomarkers → clear CIT vs Tier 2 referral
- Lab location TBD: US (Boston/SD) vs Korea (Seoul) vs dual-track — Open Question

## [2026-06-15] create | TimesFM concept page
- Type: concept
- Created: concepts/timesfm.md
- Source: https://github.com/google-research/timesfm (manual ingest, GitHub repo not paper)
- Tags: #ai #biostat #longevity #transcriptomics #metabolomics #drug-discovery
- Cross-references: scgpt_deep_analysis (single-cell FM complement), aurora_deep_analysis (FM family), arp27_vs_claw_ai_lab_analysis
- 4-섹션: Source Quotes (README 3 quotes) / My Interpretation (XReg + LoRA 패턴이 BB에 fit) / Open Questions (3) / Contradictions (none)
- Companion sidecar: public/content/research-pulse/2026-06-15-timesfm.md

> 500 entry 도달 시 `log-YYYY.md`로 회전.

## [2026-06-14] create | Brown Biotech LLM-Wiki 초기화
- Wiki path: `/Users/ocm/openclaw/workspace/bb-wiki/`
- Domain: Longevity, refractory disease, drug discovery, peptide, AI/ML for biology
- Structure: SCHEMA.md, index.md, log.md, raw/, concepts/, entities/, comparisons/, queries/, assets/, scripts/, _archive/
- Schema: BB 14 query family + meta tags, 4-section judgment layer mandatory
- PoC pages: 3 (oxphos-cancer-vulnerability, naaa-chembl2419814, naaa-vs-mgll-inhibitors)
- Symlinks:
  - `raw/` → `/Users/ocm/openclaw/workspace/arp-v27/literature/` (41 files, immutable source layer)
  - `~/Documents/Obsidian Vault/brown-biotech` → `/Users/ocm/openclaw/workspace/bb-wiki/` (Obsidian browsing)
- Scripts: `scripts/ingest_deep_dive.py`, `scripts/wiki_lint.py`
- Paper intake workflow patched: Track F (Wiki compound) added
- Inspired by: An Lab @ Korea University, "사유와 탐구, 책임의 주체로 오는 당신을 기다리며" (2026-06-13)

## [2026-06-14] ingest | arp-v27 deep-dive 일괄 ingest (10 .md)
- 5 신규: MASH_Review_Deep_Integration, SSR_Likert_SyntheticConsumers_Deep_Analysis, TPP_DGAT1_Conjugate_Research_Plan, scGPT_Deep_Analysis, turbovec_TurboQuant_Analysis
- 5 idempotent (재처리): ARP27_vs_Claw, AURORA, Agentic_Patterns, Claw_AI_Lab_Brief, LIVIA
- Total wiki pages: 13 (3 curated + 10 ingested)
- Lint: 0 errors, 13 warnings (8 wikilink + 5 split), 5 info (orphan) — 모두 Dr. OCM 판단 레이어 채우기로 해소

## [2026-06-14] update | 4-섹션 판단 레이어 샘플 작성 (2 pages)
- `concepts/livia_deep_analysis.md` — Source Quotes 5 + My Interpretation 5 + Open Questions 5 + Contradictions 1 + 5 cross-links
- `comparisons/arp27_vs_claw_ai_lab_analysis.md` — Source Quotes 5 + My Interpretation 5 + Open Questions 5 + Contradictions 1 + 5 cross-links
- 두 페이지 모두 lint warnings 0건 (An Lab pedagogy 입증)

## [2026-06-14] go | bb-wiki v1.0.0 — Checkpoint 3 (Go/No-go) APPROVED
- Status: **LIVE / daily 운영 모드 진입**
- Path: `/Users/ocm/openclaw/workspace/bb-wiki/`
- Track F: brown-biotech-paper-intake-workflow 의 A/B/C/D/E 에 추가됨
- Skill `bb-wiki` 등록: `~/.hermes/skills/brown-biotech/bb-wiki/SKILL.md`
- Obsidian 브라우징: `~/Documents/Obsidian Vault/brown-biotech`
- Daily rhythm: 새 paper → `python3 scripts/ingest_deep_dive.py` → 4-섹션 placeholder → Dr. OCM 채우기
- Weekly rhythm (Friday): `python3 scripts/wiki_lint.py --strict` → wikilink/split/stale 정리

## [2026-06-14] ingest | ARP27_vs_Claw_AI_Lab_Analysis.md
- Type: comparison
- Created: comparisons/arp27_vs_claw_ai_lab_analysis.md
- Source: raw/ARP27_vs_Claw_AI_Lab_Analysis.md

## [2026-06-14] ingest | AURORA_Deep_Analysis.md
- Type: concept
- Created: concepts/aurora_deep_analysis.md
- Source: raw/AURORA_Deep_Analysis.md

## [2026-06-14] ingest | Agentic_Patterns_BrownBiotech_Mapping.md
- Type: concept
- Created: concepts/agentic_patterns_brownbiotech_mapping.md
- Source: raw/Agentic_Patterns_BrownBiotech_Mapping.md

## [2026-06-14] ingest | Claw_AI_Lab_Brief.md
- Type: concept
- Created: concepts/claw_ai_lab_brief.md
- Source: raw/Claw_AI_Lab_Brief.md

## [2026-06-14] ingest | LIVIA_Deep_Analysis.md
- Type: concept
- Created: concepts/livia_deep_analysis.md
- Source: raw/LIVIA_Deep_Analysis.md

## [2026-06-14] ingest | ARP27_vs_Claw_AI_Lab_Analysis.md
- Type: comparison
- Created: comparisons/arp27_vs_claw_ai_lab_analysis.md
- Source: raw/ARP27_vs_Claw_AI_Lab_Analysis.md

## [2026-06-14] ingest | AURORA_Deep_Analysis.md
- Type: concept
- Created: concepts/aurora_deep_analysis.md
- Source: raw/AURORA_Deep_Analysis.md

## [2026-06-14] ingest | Agentic_Patterns_BrownBiotech_Mapping.md
- Type: concept
- Created: concepts/agentic_patterns_brownbiotech_mapping.md
- Source: raw/Agentic_Patterns_BrownBiotech_Mapping.md

## [2026-06-14] ingest | Claw_AI_Lab_Brief.md
- Type: concept
- Created: concepts/claw_ai_lab_brief.md
- Source: raw/Claw_AI_Lab_Brief.md

## [2026-06-14] ingest | LIVIA_Deep_Analysis.md
- Type: concept
- Created: concepts/livia_deep_analysis.md
- Source: raw/LIVIA_Deep_Analysis.md

## [2026-06-14] ingest | MASH_Review_Deep_Integration.md
- Type: concept
- Created: concepts/mash_review_deep_integration.md
- Source: raw/MASH_Review_Deep_Integration.md

## [2026-06-14] ingest | SSR_Likert_SyntheticConsumers_Deep_Analysis.md
- Type: concept
- Created: concepts/ssr_likert_syntheticconsumers_deep_analysis.md
- Source: raw/SSR_Likert_SyntheticConsumers_Deep_Analysis.md

## [2026-06-14] ingest | TPP_DGAT1_Conjugate_Research_Plan.md
- Type: concept
- Created: concepts/tpp_dgat1_conjugate_research_plan.md
- Source: raw/TPP_DGAT1_Conjugate_Research_Plan.md

## [2026-06-14] ingest | scGPT_Deep_Analysis.md
- Type: concept
- Created: concepts/scgpt_deep_analysis.md
- Source: raw/scGPT_Deep_Analysis.md

## [2026-06-14] ingest | turbovec_TurboQuant_Analysis.md
- Type: concept
- Created: concepts/turbovec_turboquant_analysis.md
- Source: raw/turbovec_TurboQuant_Analysis.md
