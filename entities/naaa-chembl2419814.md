---
title: CHEMBL2419814 (NAAA lead compound)
created: 2026-06-14
updated: 2026-06-14
type: entity
tags: [naaa, synthesis, drug-discovery, anti-fibrotic]
sources:
  - raw/scGPT_Deep_Analysis.md
contradictions: []
---

# CHEMBL2419814 (NAAA lead)

## 한 줄 정의

**CHEMBL2419814** — Brown Biotech ARP v27의 NAAA (N-acylethanolamine acid amidase) 저해제 가상 스크리닝에서 도출한 **lead compound**. Molecular docking에서 −13.0 kcal/mol binding affinity (PDB 6DXX).

## 핵심 사실

| 필드 | 값 |
|---|---|
| ChEMBL ID | CHEMBL2419814 |
| Target | NAAA (N-acylethanolamine acid amidase) |
| PDB | 6DXX |
| Docking score | **−13.0 kcal/mol** |
| Discovery path | ChEMBL + ZINC22 (20 candidates) → docking → top hit |
| Therapeutic hypothesis | Anti-fibrotic, anti-inflammatory (via PEA/OEA 보존) |
| Status | Lead (pre-IND 전) |

## 약물 정보

- **NAAA = N-acylethanolamine acid amidase**: PEA (palmitoylethanolamide), OEA (oleoylethanolamide) 분해 효소
- **NAAA 저해 = PEA/OEA 보존 = 항염증/항통각 효과**
- PEA는 PPAR-α agonism, OEA는 식욕 억제 + 항염증

## Brown Biotech Portfolio Fit

| Track | 활용 |
|---|---|
| **ARP v27 drug discovery** | Primary asset — NAAA program lead |
| **Refractory cancer therapeutics** | 직접 연결 약함 (NAAA는 지질-신경-면역 축) |
| **Anti-aging cosmetics** | PEA 자체는 이미 화장품 원료; CHEMBL2419814는 약물 후보 |
| **IPF / Fibrosis** | Anti-fibrotic angle 있음 — NAAA KO mice에서 fibrosis 감소 보고 (cross-check 필요) |
| **MASH/MASLD** | OEA → 식욕/지질 대사 연결, 가능성 |

## 4-섹션 판단 레이어

### 1. Source Quotes

- ARP v27 pipeline.py: `lead_compound = "CHEMBL2419814", docking_score = -13.0` (코드에서 직접 확인 필요)
- raw/scGPT_Deep_Analysis.md: NAAA program은 BB의 primary drug discovery program 중 하나
- (원문 quote: "−13.0 kcal/mol"는 exceptional docking score — 일반적 hit threshold는 −9 ~ −10)

### 2. My Interpretation

- Docking score −13.0은 **컴퓨테이ショナル 단계의 강한 시그널** — 그러나 **in vitro 검증 없이는 paper lead로 발표하면 안 됨**
- NAAA program은 BB의 **most-advanced drug discovery asset** (PoC 단계)
- Anti-fibrotic 적응증은 IPF/MASH 둘 다 가능 — 어느 쪽이 더 빠른 path to IND인가?
- PEA 자체가 EU에서 이미 화장품/의료기기 원료로 쓰임 → NAAA inhibitor는 PEA를 보존하는 다른 메커니즘

### 3. Open Questions

- In vitro NAAA enzyme assay (IC50) 결과가 있는가? 없다면 **가장 시급한 다음 step**
- Docking top hit 20개 중 왜 CHEMBL2419814가 lead로 선택되었는가? (selectivity? drug-likeness? synthetic accessibility?)
- Patent landscape: NAAA inhibitor IP는 누구手里에? (Vernalis/Pfizer의 ARN077 등 후속?)
- Anti-fibrotic PoC in vivo data가 있는가? (bleomycin-IPF 모델 or CCl4-liver 모델)
- Pro-drug 전략이 필요한가? (NAAA는 lysosomal enzyme — cellular uptake challenge)

### 4. Contradictions

- **현재 없음** — 신규 페이지.
- **잠재 충돌 후보**: 만약 NAAA 저해가 pro-fibrotic (역설적) 데이터를 만나면 — PEA의 항섬유화 효과와 모순 → 즉시 flag

## 관련 페이지

- [[oxphos-cancer-vulnerability]] — 미토콘드리아/에너지 대사 cross-reference
- [[naaa-vs-mgll-inhibitors]] — 다른 endocannabinoid-degrading enzyme 비교
- raw/TPP_DGAT1_Conjugate_Research_Plan.md — BB의 다른 drug discovery program
- raw/scGPT_Deep_Analysis.md — ARP v27 program context
