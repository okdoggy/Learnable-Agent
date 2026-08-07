---
schema_version: '1.0'
number: 5
technical_id: natural-skin-tone-and-texture-preservation
title_ko: 피부색·질감·얼굴 구조를 보존하는 자연스러운 인물 보정
summary_ko: 노출·화이트 밸런스를 안정시킨 뒤 피부색 편차와 거친 명암을 줄이되 질감과 얼굴 구조, 정체성을 보존하는 인물 보정 기술이다.
version: 1.0.0
status: active
supported_tools:
- generate_ai
confidence: 0.92
raw_scenario_ids:
- raw-20260802-galleryskin01
- raw-20260802-skinvariance01
- raw-20260807-eyesclera
- raw-20260807-harshskin01
- raw-20260807-skintex15
source_urls:
- https://fstoppers.com/education/how-edit-portrait-skin-tones-lightroom-902830
- https://fstoppers.com/education/lightrooms-tone-curve-explained-every-trick-need-know-902177
- https://www.adobe.com/learn/lightroom-cc/web/ai-portrait-mask-lightroom
- https://www.adobe.com/learn/lightroom-cc/web/precise-color-adjustments
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 피부색·질감·얼굴 구조를 보존하는 자연스러운 인물 보정

노출·화이트 밸런스를 안정시킨 뒤 피부색 편차와 거친 명암을 줄이되 질감과 얼굴 구조, 정체성을 보존하는 인물 보정 기술이다.

## 적용 조건

- 홍조·혼합 조명·거친 명암·과도한 피부 질감이 보이는 인물 사진에 적용한다.
- 피부색을 고르게 하거나 부드럽게 하되 얼굴 정체성과 자연스러운 질감을 유지해야 할 때 적용한다.

## 기술 절차

1. 노출과 화이트 밸런스를 먼저 안정시켜 피부색 판단 기준을 만든다.
2. 피부만 의미적으로 선택하고 중간 피부색을 기준으로 과한 홍조나 색 편차를 줄인다.
3. 필요하면 Texture와 Clarity를 낮추되 소량의 그레인 또는 자연 질감을 남긴다.
4. 거친 한낮 명암은 하이라이트를 낮추고 그림자를 올리는 방향으로 압축하되 얼굴 구조를 보존한다.
5. 눈 흰자 등 세부는 별도 영역으로 매우 약하게 보정한다.
6. 확대와 전체 화면을 오가며 정체성, 모공·잔주름, 색 변화가 자연스러운지 확인한다.

## 파라미터 가이드

- Color Variance -50은 한 Adobe 예시의 참고점이며 모든 피부의 고정값이 아니다.
- Facial Skin의 Texture -20, Clarity -25, Grain 15는 해당 공식 예시의 출발점으로만 사용한다.
- Eye Sclera의 Exposure 0.2와 Temperature -4도 해당 공식 예시의 미세 조정값이며 인물별로 더 낮게 조절할 수 있다.
- 정확한 수치가 없는 피부색과 역 S-curve 조정은 자연스러운 변화와 얼굴 구조가 남는 범위에서 정성적으로 결정한다.

## 판단 근거

- Fstoppers와 여러 Adobe 공식 튜토리얼에서 피부색 기준 안정화, 국소 색 편차 완화, 질감 보존, 절제된 세부 보정이 반복된다.
- 인물 편집에서 가장 큰 실패인 색 왜곡과 과도한 스무딩을 동시에 예방한다.
- Generate AI identity-preserve 편집으로 실행 가능하다.

## 주의사항

- 색 편차와 질감을 완전히 제거하면 플라스틱처럼 보이고 정체성이 약해진다.
- 피부 마스크가 눈·입술·머리카락·의상까지 침범하지 않는지 확인한다.
- 눈 흰자 밝기와 냉각은 눈에 띄지 않을 정도로 제한한다.
- 역 S-curve로 명암을 과도하게 압축하면 얼굴 입체감이 사라진다.

## 충돌 및 예외

- 거친 한낮 피부에는 대비를 압축하는 방향이 유효하지만 평면광 얼굴에는 방향성 대비를 일부 보강해야 하므로 장면의 기존 명암 상태를 먼저 진단한다.

## raw 근거

- raw-20260802-galleryskin01
- raw-20260802-skinvariance01
- raw-20260807-skintex15
- raw-20260807-eyesclera
- raw-20260807-harshskin01
