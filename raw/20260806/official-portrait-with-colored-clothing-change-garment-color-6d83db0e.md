---
schema_version: '1.0'
scenario_id: raw-20260806-hueexclude01
title_ko: 특정 색상만 바꾼 뒤 마스크로 피부의 동색 영역 제외
status: validated
source:
  type: official
  publisher: Adobe Photoshop Learn
  author: Dani Beaumont
  url: https://www.adobe.com/learn/photoshop/web/edit-photos-adjustment-layers
  published_at: '2025-12-17'
  accessed_at: '2026-08-06T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Photoshop on the web
scenario:
  subject: portrait-with-colored-clothing
  condition:
  - shared-color-between-subject-elements
  - selective-color-change
  intent:
  - change-garment-color
  - protect-skin-tone
method:
  steps:
  - tool: Hue/Saturation Adjustment Layer
    parameter: '피사체 레이어 위에 추가하고 Master 대신 바꿀 색상 범위(예: Reds)를 선택한다'
    value: null
    unit: null
    reported_as: qualitative
  - tool: Hue
    parameter: 대상 색이 원하는 방향으로 바뀔 때까지 조절한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adjustment Layer Mask
    parameter: 검정 브러시 또는 Subtract로 얼굴·손 등 원래 색을 유지할 영역에서 효과를 숨긴다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask correction
    parameter: 너무 많이 뺀 곳은 흰색 브러시 또는 Add로 효과를 다시 드러낸다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 색상 범위 기반 Hue 변경은 의상 색을 빠르게 바꾸지만 같은 계열의 피부나 다른 물체도 함께 바뀔 수 있다.
- 조정 레이어 마스크에서 검정은 효과를 숨기고 흰색은 드러내므로 원본 픽셀을 손상하지 않고 예외 영역을 정리할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 6d83db0efeb9abb4e03f0f1a0940881530d20b5612361ac13851aa0dcd4064ca
  collected_at: '2026-08-06T00:00:00Z'
---

# 특정 색상만 바꾼 뒤 마스크로 피부의 동색 영역 제외

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

인물의 빨간 재킷처럼 특정 색만 바꾸려 했는데 얼굴이나 손 등 비슷한 색 영역까지 함께 변할 때 사용한다.

## 촬영/작업 순서

1. 피사체가 있는 레이어를 선택하고 Hue/Saturation 조정 레이어를 추가한다.
2. Master가 아니라 대상에 해당하는 색상 범위를 선택한다.
3. Hue를 움직여 의상 색을 변경한다.
4. 조정 레이어 마스크를 선택하고 검정 브러시 또는 Subtract로 피부 영역의 효과를 제거한다.
5. 경계를 지나치게 지웠다면 흰색 브러시 또는 Add로 마스크를 복구한다.

## 추천 시작값 / 조작값

- Hue/Saturation Adjustment Layer / 피사체 레이어 위에 추가하고 Master 대신 바꿀 색상 범위(예: Reds)를 선택한다: 원문 정성 표현(수치 추정 없음)
- Hue / 대상 색이 원하는 방향으로 바뀔 때까지 조절한다: 원문 정성 표현(수치 추정 없음)
- Adjustment Layer Mask / 검정 브러시 또는 Subtract로 얼굴·손 등 원래 색을 유지할 영역에서 효과를 숨긴다: 원문 정성 표현(수치 추정 없음)
- Mask correction / 너무 많이 뺀 곳은 흰색 브러시 또는 Add로 효과를 다시 드러낸다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 먼저 의상에서 목표 색 변화가 충분한지 확인한다.
- 얼굴, 손, 머리카락과 배경에서 같은 계열 색이 우연히 변했는지 확대해 확인한다.
- 넓은 영역은 적당히 큰 브러시로 정리하고 가장자리에서는 브러시 크기를 줄인다.
- 마스크 썸네일과 최종 이미지를 번갈아 보며 누락과 과도한 제외를 수정한다.

## 주의할 점

- 색상 범위 선택만으로는 동일 계열의 피부색과 배경색을 자동으로 보호하지 못한다.
- 검정과 흰색의 마스크 역할을 반대로 사용하면 의도한 영역이 사라지거나 다시 나타난다.
- 브러시가 경계를 넘어가면 Undo 또는 Add로 즉시 복구한다.

## 확실성과 근거

- 색상 범위 기반 Hue 변경은 의상 색을 빠르게 바꾸지만 같은 계열의 피부나 다른 물체도 함께 바뀔 수 있다.
- 조정 레이어 마스크에서 검정은 효과를 숨기고 흰색은 드러내므로 원본 픽셀을 손상하지 않고 예외 영역을 정리할 수 있다.

Adobe 공식 튜토리얼이 Reds 예시, Hue 변경, 피부에 번진 효과를 마스크의 Subtract/Add로 수정하는 절차를 직접 제시한다. Hue 수치와 브러시 크기는 명시하지 않아 추정하지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/photoshop/web/edit-photos-adjustment-layers
- 접근일: 2026-08-06
