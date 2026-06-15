---
title: Livia Deep Analysis
created: 2026-06-14
updated: 2026-06-14
type: concept
tags: ["longevity", "fibrosis", "naaa", "peptide", "biostat", "ai"]
sources:
  - raw/LIVIA_Deep_Analysis.md
contradictions: []
---

# LIVIA: a browser-based tool for assessing and visualizing predicted protein interactions — Deep Analysis

**Authors:** Ah-Ram Kim¹, Norbert Perrimon¹,²
¹ Department of Genetics, Blavatnik Institute, Harvard Medical School, Boston, MA, USA
² Howard Hughes Medical Institute, Harvard Medical School, Boston, MA, USA
**Correspondence:** ah-ram_kim@hms.harvard.edu, perrimon@genetics.med.harvard.edu
**Venue:** bioRxiv preprint, posted 2026-05-10 (not peer-reviewed)
**DOI:** [10.64898/2026.05.01.721633](https://doi.org/10.64898/2026.05.01.721633)
**Type:** Software/tool paper (3pp main + 1 supp fig)
**AI disclosure:** Used Claude (Opus 4.6/4.7) for code and copyediting — authors reviewed all
**Funding:** NIH NIGMS P41 GM132087, NIH NIAMS R01 AR057352, NRF Korea (2021R1A6A3A14039622), HHMI
**Code:** [github.com/flyark/LIVIA](https://github.com/flyark/LIVIA) (MIT) | Batch CLI: [github.com/flyark/AFM-LIS](https://github.com/flyark/AFM-LIS)
**LIVIA app:** [flyark.github.io/LIVIA](https://flyark.github.io/LIVIA)
**Added to Brown Biotech:** 2026-06-09 (Notion: Active Projects DB, Type=Content, Priority=Low)
**PDF:** `/Users/ocm/.hermes/cache/documents/doc_79f750c932c1_2026.05.01.721633v1.full.pdf`

---

## 1. 핵심 요지 (TL;DR)

LIVIA (Local Interaction Visualization and Analysis)는 **브라우저 단독** (static web app, server 없음)으로 6개 예측 플랫폼 — AlphaFold-Multimer, AlphaFold3, ColabFold, Boltz-1/2, Chai-1, OpenFold3 — 의 결과를:

1. **자동 포맷 감지** (filename + data structure)
2. **통합 파싱** (ZIP archive 그대로 로드 가능)
3. **국소 신뢰도 지표 계산** — LIS / cLIS / iLIS (AFM-LIS framework) + ipSAE / actifpTM / ipTM
4. **인터랙티브 시각화** — PAE/LIS/cLIS heatmap, LIR 패널 (sequence + linear contact map), residue-level pLDDT 차트, Mol* 3D viewer
5. **스크립트 export** — ChimeraX / PyMOL (color scheme 반영)
6. **추가 모듈** — FlyPredictome 검색, Ortholog lookup, Monomer Subdomain 분석, AFDB dimer 직접 fetch

장점: **순수 client-side → 데이터 미유출 (제약/제조 IP 친화적)**, 6개 플랫폼 통합, iLIS 단일 점수로 빠른 triage → ipSAE/actifpTM 정밀 분석 위계.

## 2. 방법론(Method) — 알고리즘 검토

### 2.1 핵심 지표 정의

| 지표 | 정의 | 임계값 |
|---|---|---|
| **LIS** | PAE ≤ 12 Å인 inter-chain 잔기쌍의 local interaction probability 평균 | PAE ≤ 12 Å |
| **cLIS** | LIS + Cβ ≤ 8 Å (접촉 필터) | Cβ ≤ 8 Å |
| **iLIS** | LIS · cLIS 결합 단일 점수 | — |
| **LIR** | PAE ≤ 12 Å인 interface residue | — |
| **cLIR** | LIR + Cβ ≤ 8 Å | — |
| **ipSAE** | Dunbrack 2025 재구현 | (인용만) |
| **actifpTM** | Varga 2025 재구현 | (인용만) |
| **ipTM** | 플랫폼 보고값 | 비교 reference |

### 2.2 알고리즘 평가

**✅ 장점**
- PAE 행렬 + Cβ 거리만으로 계산 — 추가 MSA/dock 불필요
- 플랫폼 간 동일 지표 비교 가능 (한 모델 = 한 metric set)
- 모델 다중 출력 시 평균 ± SD overlay (불확실성 표현)

**⚠️ 우려 1 — 임계값의 정당성 부족**
- **PAE ≤ 12 Å, Cβ ≤ 8 Å** 두 임계값 모두 **자기그룹의 AFM-LIS 논문(Ref 8, 11)** 에서 가져옴
- 본 논문에서 empirical sweep / sensitivity analysis 없음
- "Recommended iLIS threshold" 언급하나(About page only), 그 값의 ROC/precision-recall 근거 미제시
- 임계값이 다른 예측 플랫폼(AF3 vs Boltz-1)에 동일하게 적용 가능한지 cross-platform calibration 없음

**⚠️ 우려 2 — AFM-LIS 자기 인용**
- LIVIA는 **AFM-LIS framework (Kim 2024, 2026) 기반 도구** — 동일 1저자
- LIS/cLIS 자체의 **독립 벤치마크가 본 논문에 없음**
- "LIVIA가 AFM-LIS를 구현했다"는 사실과 "AFM-LIS가 정확하다"는 주장은 **별개** — 후자는 본 논문이 검증한 게 아님

## 3. 검증(Validation) — 이 논문의 가장 큰 약점

### 3.1 무엇이 "검증"으로 제시되는가

**단일 illustrative case:** Drosophila TRiC/CCT chaperonin (8 subunit + αTub67C, 9 chain, 4,795 잔기).

**관찰 1:** 기질 결합 시 LIR/cLIS가 apo보다 풍부
- apo: pTM 0.58 / ipTM 0.55
- αTub67C-bound: pTM 0.71 / ipTM 0.69
- βTub56D-bound: pTM 0.74 / ipTM 0.73

**관찰 2:** CCT1 C-말단 (543–557) 이 기질과 contact
- 사람 cryo-EM (Gestaut 2022) 의 "fulcrum" 가설과 일치
- 평균화 기반 cryo-EM 은 C-tail 의 intrinsically disordered 성격 때문에 누락 가능

### 3.2 명백한 격차

| 결여 | 영향 |
|---|---|
| ❌ **Ground-truth benchmark** (PDB crystal complex, EVC/BM5, DockQ) | Interface recall/precision 정량화 불가 |
| ❌ **Cross-tool 비교** (PAEViewer, ClusPro, FoldDock, ChimeraX 내장) | 우위 입증 불가 |
| ❌ **다양한 PPI 유형** (transient / obligate / homo / hetero / antibody-antigen) | 일반화 가능성 미검증 |
| ❌ **다양한 플랫폼 head-to-head** (AF3 vs Boltz-2 vs Chai-1) | "platform-agnostic" 주장 미입증 |
| ❌ **Negative controls** (실제로 상호작용 안하는 pair) | FPR 추정 불가 |
| ❌ **Cross-species 일반화** | Drosophila 예시 1개 → 사람/포유류 미검증 |

→ **"validation" 이라기보다 "demonstration"**. 같은 그룹의 다른 논문 (2024 AFM-LIS) 에서 일부 정량 검증이 있었을 가능성은 있으나, 본 LIVIA 논문은 그것을 계승하지 않음.

### 3.3 단일 신규 생물학적 claim

- **CCT1 C-말단이 α/β-tubulin 과 직접 contact** (Drosophila, AF3)
- 사람 cryo-EM (Gestaut 2022) 이 CCT2/CCT6 C-tail 은 봤지만 CCT1 은 "averaging" 으로 누락 가능성을 시사
- **이건 falsifiable prediction** — 점突变 (CCT1 C-tail truncation) + in vitro tubulin folding assay 로 검증 가능
- **본 논문은 in silico 만 보고, in vitro / in vivo 검증 0** — wet-lab 협업 opportunity

## 4. 성능(Performance) 평가

| 조건 | 시간 | 메모리 |
|---|---|---|
| p53–MDM2 (2 chain, ~400 res, 5 models) | **1–4 s** | — |
| Drosophila CCT+αTub67C (9 chain, 4,795 res, 5 models) | **~30 s** | **peak ~3.3 GB** |

**⚠️ 하드웨어 편향:** "Apple M3 MAX" — best-case. 일반 연구실 laptop (8–16 GB RAM) 에서는 3.3 GB peak 가 9-chain 한계선일 수 있음. 16-subunit 같은 더 큰 complex 는 현재 사양으로 안 돌아갈 가능성.

**✅ 순수 클라이언트 사이드** — 데이터 업로드 없음, IP/보안 친화적. 제약 산업에서 의미 큼.

## 5. 재현성(Reproducibility)

**✅ 강점**
- Source: github.com/ﬂyark/LIVIA, MIT license
- 데이터: 6개 플랫폼별 p53–MDM2 예시 내장
- 배치 처리용 `lis.py` CLI (github.com/ﬂyark/AFM-LIS) 별도 제공
- Static web — 버전 핀 가능

**⚠️ 우려**
- "Recommended iLIS threshold" 가 About page 에만 있음 — 논문 본문 미기재 → 인용 시 추적 어려움
- AFDB dimer module 은 AFDB API 의존 — AFDB schema 변경 시 깨질 수 있음
- Browser compatibility 는 Chrome/Firefox/Safari 언급, **mobile 미언급**

## 6. Novelty & Positioning

| 차원 | 평가 |
|---|---|
| 알고리즘 novelty | **낮음** — AFM-LIS 재구현, 신규 metric 없음 |
| 통합 novelty | **중간** — 6 플랫폼 자동 감지 + 한 화면 = 진짜 가치 |
| 시각화 novelty | **중간–높음** — circular contact map, LIR-focused 3D default |
| 생태계 novelty | **중간** — AFDB dimer 직접 fetch, Drosophila/Predictome 통합 |
| **Overall** | **Tool paper, not method paper**. Software Eng 관점 contribution |

vs 기존 도구:
- **PAEViewer** (Evan et al.) — PAE 시각화만, LIS/cLIS 없음
- **ChimeraX** — 수동 인터페이스 분석, 자동 metric 없음
- **FoldDock / ClusPro** — docking 도구, AF 결과 평가용 아님
- **AlphaPulldown / ColabFold** — prediction 도구, evaluation 아님

→ **"AF 결과를 평가/시각화하는 표준 도구" 자리를 노림** — 성공 여부는 adoption 에 달림.

## 7. 종합 강점 / 약점

### 🟢 강점
1. 6 플랫폼 통합 + 자동 감지 — 실사용성 큼
2. 순수 client-side, 데이터 미유출 — 제약/제조 IP 보호
3. iLIS 단일 점수로 빠른 triage → ipSAE/actifpTM 으로 정밀 분석 위계 명확
4. New bio claim (CCT1–tubulin contact) — Drosophila chaperonin 분야에 검증 가능한 가설 제시

### 🔴 약점
1. **독립 validation 0** — 같은 그룹의 AFM-LIS framework 를 인용만 함, LIVIA 자체의 F1/precision-recall 없음
2. **임계값 (12 Å, 8 Å) 정당화 부족** — sensitivity analysis 없음
3. **단일 예시 검증** — Drosophila CCT 하나만
4. **Cross-platform calibration 없음** — AF3 와 Boltz-2 가 같은 threshold 로 정확한지 미확인
5. **AFDB dimer 1.7M homodimer 만** — heterodimer 는 "future work"
6. **AI 사용 공개는 적절하나**, 코드 일부가 Claude 생성 — 정확성 peer-review 안 됨
7. **저널 투고 전 preprint** — peer review 통과 시 인용 가치 ↑

## 8. Brown Biotech 연관성

| 트랙 | 매치 | 코멘트 |
|---|---|---|
| **ARP v27 drug discovery** | 🟡 간접 | PPI 평가 단계에서 사용 가능. NAAA, fibrosis 타깃의 predicted complex 검증 |
| **Peptide service** | ⚪ 없음 | — |
| **Paid Briefs / biostatx** | ⚪ 없음 | — |
| **PRISM RAG ingest** | 🟡 가능 | AF 평가 도구로 자주 인용될 가능성 — bioRxiv 정식 출판 후 ingest 권장 |
| **Inventa (Korean AI research)** | ⚪ 없음 | — |
| **14 query families 매치** | **0/14** | — |

**결론:** BB 직접 포트폴리오와는 거리 있음. 단, "AF 결과의 신뢰도 평가"는 모든 구조 기반 discovery의 보편적 필요 — 도구 자체를 RAG 에 넣어두면 ARP-v27 PPI 모듈의 품질 검증에 indirect 도움.

## 9. BB Follow-up 잠재 아이디어

1. **ARP v27 NAAA / fibrosis 타깃 평가** — NAAA (6DXX) 또는 fibrosis 관련 단백질의 predicted complex 평가 시 LIVIA 사용 → IP 보호 + 빠른 인터페이스 분석
2. **Peptide service 시각화 결과물** — 고객에게 PPI visualization 결과물 제공 → 프리미엄 티어 차별화
3. **AFDB dimer 1.7M 분석** — Paid Briefs "Repurposing opportunities in dimer interfaces" 상품화 가능성 탐색
4. **Drosophila 중심** — FlyPredictome 모듈은 BB 포커스 아님, 그러나 ortholog lookup 은 사람/포유류 확장 가능

## 10. 인용 추천 시점

- bioRxiv preprint → 정식 peer-reviewed 출판 시까지 BB 내부 reference 로만 사용
- 출판 후: ARP v27 PPI 평가 워크플로우 / Paid Briefs 의 "AF 신뢰도 평가" 섹션에 인용
- "Brown Biotech 의 AF 평가 표준 도구" 로 채택 검토 시 LIVIA + ipSAE + actifpTM 3-툴 비교 평가 진행 권장

---

## 11. 핵심 takeaway (1문장)

**"훌륭한 통합 도구지만, 방법론 검증은 부족 — bioRxiv 정식 출판 시점에 cross-platform benchmark 추가되어야 인용 가치 ↑."**

---

*Created 2026-06-09 by Demis (Brown Biotech paper intake workflow, Track A).*
*Notion page: https://app.notion.com/p/LIVIA-browser-based-tool-for-assessing-predicted-PPIs-Kim-Perrimon-2026-379f273533a481208456c7eaecbc46ac*


## 4-섹션 판단 레이어

### 1. Source Quotes

- "LIVIA is a browser-based, single-page web application that runs entirely on the client side — no installation, no data upload, no server." — Kim & Perrimon 2026, bioRxiv 10.64898/2026.05.01.721633, §Abstract
- "Six structure-prediction platforms supported: AlphaFold-Multimer, AlphaFold3, ColabFold, Boltz-1/2, Chai-1, OpenFold3" — Kim & Perrimon 2026, §1 Introduction
- "iLIS = LIS · cLIS, providing a single composite score for rapid triage before detailed ipSAE/actifpTM analysis" — Kim & Perrimon 2026, §2.1 LIS/cLIS/iLIS definitions
- "Client-side processing ensures proprietary sequences never leave the user's machine" — implicit from static web app architecture, §Methods
- 원문 PDF: [[raw/LIVIA_Deep_Analysis.pdf]] (또는 79f750c932c1_2026.05.01.721633v1.full.pdf, /Users/ocm/.hermes/cache/documents/)

### 2. My Interpretation

- **Client-side (data never leaves browser)** = 제약·제조 IP 친화적. BB가 Paid Brief 작성 시 고객 target sequence를 다룰 때 데이터 유출 우려 해소 → **BB 워크플로우에 자연스럽게 끼워넣을 수 있는 형태**
- 6개 플랫폼 통합 + iLIS 단일 점수 triage = ARP v27의 docking 단계 validation tool로 활용 가능 (BB의 primary drug discovery engine과 complementary)
- bioRxiv preprint, peer-review 미통과 → tool 자체는 production-grade (MIT license, GitHub release)지만 **인용/의존은 보수적으로**
- Harvard Perrimon lab = *Drosophila* genetics의 정점 — domain expertise가 모델 생물에 강함, **인간/포유류 적용은 별도 검증 필요**
- **BB의 IPF/Crohn's/fibrosis 도메인** (CTHRC1+ fibroblast 등) 에는 protein interaction prediction이 직접 relevant — FRET/BRET 검증 디자인에 활용 가능

### 3. Open Questions

- LIVIA 가 human/mammalian proteome 에서도 AFM-LIS framework가 동일한 정확도를 보이는가? (Fly data 기반 validation — mammalian transferability 확인 필요)
- iLIS > 0.6 같은 임계값이 실제 hit rate와 어떻게 correlate하는가? — **false positive rate가 experimentally calibrated 되어 있는지 검증 필요**
- BB의 target-specific protein-protein interaction 예측 (예: NAAA dimer 구조, OUD-related receptor heterodimer) 에 적용한 PoC case가 있는가? — 아직 없음
- 6개 플랫폼 결과의 **consensus scoring** 이 가능한가? (현재는 단일 플랫폼 결과 표시, ensemble score는 미지원 추정)
- ipSAE/actifpTM 의 reference (Dunbrack 2025, Varga 2025) 가 BB portfolio 의 다른 program 에서도 cross-validated 되었는지?

### 4. Contradictions

- **현재 없음** — 신규 페이지.
- **잠재 충돌 후보**: 만약 mammalian transferability 가 낮다는 데이터가 나오면 → Fly-validated 도구를 BB mammalian target 에 그대로 쓰는 workflow에 flag

## 관련 페이지

- [[naaa-chembl2419814]] — NAAA program, protein-ligand interaction (LIVIA 의 PPI prediction 과 complementary)
- [[scgpt_deep_analysis]] — single-cell AI for biology, 같은 "AI for biology" 카테고리
- [[arp27_vs_claw_ai_lab_analysis]] — BB 의 drug discovery AI 인프라, LIVIA 가 끼어들 자리
- [[oxphos-cancer-vulnerability]] — BB 의 OXPHOS program, protein complex prediction 에 LIVIA 활용 가능
- raw/LIVIA_Deep_Analysis.md (원본 deep-dive)

