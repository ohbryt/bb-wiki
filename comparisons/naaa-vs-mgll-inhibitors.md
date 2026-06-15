---
title: NAAA vs MGLL inhibitors
created: 2026-06-14
updated: 2026-06-14
type: comparison
tags: [naaa, endocannabinoid, drug-discovery, anti-inflammatory]
sources:
  - raw/scGPT_Deep_Analysis.md
contradictions: []
---

# NAAA vs MGLL inhibitors

## 비교 이유

둘 다 **endocannabinoid-degrading enzyme** 의 저해제. 비슷해 보이지만:
- 기질(substrate)이 다름
- 약리 효과 경로가 다름
- Brown Biotech의 **NAAA program (CHEMBL2419814)** 이 왜 MGLL이 아닌 NAAA를 선택했는지 명확히 하기 위해

## 비교 차원

| 차원 | NAAA (N-acylethanolamine acid amidase) | MGLL (monoacylglycerol lipase) |
|---|---|---|
| **기질** | PEA, OEA (N-acylethanolamine) | 2-AG (2-arachidonoylglycerol) |
| **최종 생성물** | Fatty acid + ethanolamine | Glycerol + arachidonic acid |
| **주요 수용체** | PPAR-α (via PEA), GPR119 (via OEA) | CB1, CB2 (via 2-AG) |
| **생리적 역할** | 항염증, 식욕 조절, 통각 조절 | cannabinoid signaling, 신경가소성, 통각 |
| **저해제 효과** | Anti-inflammatory, anti-fibrotic (PEA 보존) | cannabinoid 강화, 통각 억제, 불안/우울 |
| **안전성 profile** | 비교적 clean (글리알 activation 보고 적음) | CB1 desensitization, 정신활성 가능성 |
| **주요 reference 저해제** | ARN077 (Vernalis), CHEMBL2419814 (BB lead) | JZL184, ABX-1431 (Abide/Merial) |
| **임상 단계** | Lead optimization (대부분 회사) | MGLL 저해제 — 임상 진입 시도 있었으나 안전성 이슈 |
| **BB 적응증 가능성** | IPF, MASH, anti-aging cosmetics | Neuropathic pain, anxiety — BB 도메인 외 |

## 결론 / 종합

**BB가 NAAA를 선택한 이유 (hypothesis):**

1. **안전성 margin**: MGLL 저해제는 CB1 desensitization으로 내성/정신활성 위험. NAAA 저해제는 PEA를 보존하는 anti-inflammatory 경로로, **인지/정신 기능 영향 적음**
2. **적응증 일치**: BB의 primary 도메인 (longevity, IPF, MASH, cosmetics) 모두 NAAA-PEA/OEA-PPARα axis와 연결. MGLL-CB1 axis는 neuro 쪽
3. **IP space**: MGLL 저해제 (e.g., Abide Therapeutics)는 이미 crowded. NAAA는 상대적으로 비어 있음
4. **Mechanistic novelty**: PEA 보존 자체는 EU에서 화장품/의료기기 raw material로 사용 — NAAA 저해는 **endogenous PEA 증가** 라는 새 mechanism

**Trade-off (정직하게):**

- NAAA는 lysosomal enzyme → cell permeability challenge 더 큼
- MGLL 저해제의 cannabinoid 강화 효과는 **neuropathic pain** 에서 강력 — BB는 neuro 도메인 가지 않으므로 우선순위 낮음
- PEA 보존의 anti-fibrotic 효과는 in vivo 데이터 제한적 — **검증 필요**

## 4-섹션 판단 레이어

### 1. Source Quotes

- "MGLL inhibition can lead to CB1 desensitization and functional tolerance" — MGLL pharmacology literature (Schlosburg et al. 2010 등)
- "NAAA inhibition preserves PEA and OEA, exerting anti-inflammatory effects via PPAR-α" — NAAA pharmacology literature (Piomelli lab 일련의 논문)
- raw/scGPT_Deep_Analysis.md: BB가 NAAA program을 선택한 이유가 drug-likeness와 IP availability

### 2. My Interpretation

- 이 비교는 BB의 **portfolio strategy defense** 역할
- MGLL은 **기술적으로 더 쉬운 표적** (CB1 readout 명확) — 그러나 BB의 도메인 적응증과 안 맞음
- NAAA는 **BB 도메인에 더 잘 맞지만**, PEA anti-fibrotic 효과의 **인간 임상 데이터가 부족** → 첫 IND의 적응증 선택이 중요
- Anti-aging cosmetics (PEA 자체) → NAAA 저해 (내인성 PEA 증가) 로 가면 **mechanism upgrade** + **같은 시장** + **다른 IP** = 좋은 thesis

### 3. Open Questions

- NAAA 저해제 **in vivo anti-fibrotic 데이터** (bleomycin-IPF or CCl4-liver) 가 있는가? — **PoC의 핵심**
- PEA 보존이 **인지 기능**에 영향이 있는가? (장기 사용 시 안전성)
- NAAA의 lysosomal localization이 BBB 통과에 미치는 영향? (뇌 적응증 가능 여부)
- BB NAAA lead (CHEMBL2419814) 의 **selectivity over MGLL** 수치는? (counter-screen 필요)
- MGLL 저해제의 **현재 임상 단계** — Abide/Merial 후속? 안전성 문제로 멈췄는지?

### 4. Contradictions

- **현재 없음** — 신규 페이지.
- 만약 NAAA 저해제의 in vivo 데이터가 pro-fibrotic 결과로 나오면 (PEA의 항섬유화 가설과 모순) → 즉시 flag, PEA literature 재검토

## 관련 페이지

- [[naaa-chembl2419814]] — NAAA program lead
- [[oxphos-cancer-vulnerability]] — 미토콘드리아/에너지 대사 cross-reference
- raw/scGPT_Deep_Analysis.md — ARP v27 program context
