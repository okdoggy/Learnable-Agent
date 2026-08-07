---
schema_version: '1.0'
scenario_id: raw-20260804-localdehaze01
title_ko: 안개 낀 원경만 선택해 Dehaze와 Vibrance를 국소 적용
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/photoshop/photoshop-2026s-dehaze-tool-more-powerful-think-901680
  published_at: '2026-04-16'
  accessed_at: '2026-08-04T00:00:40Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Photoshop 2026
scenario:
  subject: hazy-landscape-background
  condition:
  - atmospheric-haze
  - distant-background
  - landscape
  intent:
  - recover-background-definition
  - localized-color-enhancement
  - preserve-atmospheric-depth
method:
  steps:
  - tool: Object Selection
    parameter: hover mode로 안개 낀 배경 피사체 선택
    value: null
    unit: null
    reported_as: qualitative
  - tool: Clarity and Dehaze adjustment layer
    parameter: 선택 영역 마스크 안에서 Dehaze를 오른쪽으로 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Layers
    parameter: Alt 또는 Option 드래그로 기존 마스크를 Color and Vibrance 레이어에 복사
    value: null
    unit: null
    reported_as: qualitative
  - tool: Color and Vibrance adjustment layer
    parameter: 복사한 마스크 안에서 Vibrance 증가
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 안개가 낀 원경에만 Dehaze를 제한하면 전경과 하늘을 과도하게 변화시키지 않고 필요한 분리감만 회복할 수 있다.
- 같은 마스크로 Vibrance를 적용하면 원경의 정의와 색 강화 범위가 정확히 일치한다.
collection:
  collector_version: 1.0.0
  content_sha256: bb69b6bfc456d246f03aabdbf281fef4deb1664cfc1cf82847c301b871c10836
  collected_at: '2026-08-04T00:00:40Z'
---

# 안개 낀 원경만 선택해 Dehaze와 Vibrance를 국소 적용

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

산이나 열대 풍경의 원경에 대기 안개가 끼어 분리감과 색이 약하지만 전경과 하늘의 자연스러운 분위기는 유지해야 할 때 사용한다.

## 촬영/작업 순서

1. Object Selection의 hover mode로 안개 낀 산 같은 배경 요소가 강조될 때 클릭해 선택한다.
2. 선택 상태에서 Clarity and Dehaze adjustment layer를 만들어 선택을 자동으로 마스크로 전환한다.
3. 마스크 안에서 Dehaze를 오른쪽으로 움직여 원경의 분리감과 정의를 회복한다.
4. Color and Vibrance adjustment layer를 추가한다.
5. 기존 산 마스크를 새 조정 레이어로 복사하고 그 안에서 Vibrance를 올린다.
6. 전체 장면과 비교해 날씨가 바뀐 듯 과장되지 않는 수준으로 되돌려 조정한다.

## 추천 시작값 / 조작값

- Object Selection / hover mode로 안개 낀 배경 피사체 선택: 원문 정성 표현(수치 추정 없음)
- Clarity and Dehaze adjustment layer / 선택 영역 마스크 안에서 Dehaze를 오른쪽으로 조정: 원문 정성 표현(수치 추정 없음)
- Layers / Alt 또는 Option 드래그로 기존 마스크를 Color and Vibrance 레이어에 복사: 원문 정성 표현(수치 추정 없음)
- Color and Vibrance adjustment layer / 복사한 마스크 안에서 Vibrance 증가: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 마스크 가장자리가 산 능선과 주변 하늘을 자연스럽게 분리하는지 확인한다.
- Dehaze 전후의 원근감과 대기 깊이를 비교한다.
- 색 강화는 Saturation보다 Vibrance를 우선 검토해 이미 높은 채도의 색을 보호한다.
- 동일 영역에 색을 더할 때 새로 선택하지 않고 검증된 마스크를 복사해 정합성을 유지한다.

## 주의할 점

- 강한 Dehaze를 전체 이미지에 적용하면 대기감이 사라지고 무거운 결과가 될 수 있다.
- 효과가 강하면 실제와 다른 날씨에서 촬영한 것처럼 보일 수 있다.
- 자동 선택 마스크가 원경 밖까지 포함하지 않았는지 오버레이로 확인해야 한다.

## 확실성과 근거

- 안개가 낀 원경에만 Dehaze를 제한하면 전경과 하늘을 과도하게 변화시키지 않고 필요한 분리감만 회복할 수 있다.
- 같은 마스크로 Vibrance를 적용하면 원경의 정의와 색 강화 범위가 정확히 일치한다.

출처가 Object Selection hover mode, 선택 기반 Clarity and Dehaze 레이어, 마스크 복사, 같은 영역의 Vibrance 증가를 직접 설명한다. 슬라이더의 정확한 수치는 제시되지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/photoshop/photoshop-2026s-dehaze-tool-more-powerful-think-901680
- 접근일: 2026-08-04
