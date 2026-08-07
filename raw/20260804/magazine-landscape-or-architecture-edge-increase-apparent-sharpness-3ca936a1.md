---
schema_version: '1.0'
scenario_id: raw-20260804-edgecontrast01
title_ko: 수평선이나 건축 경계 한쪽의 톤 차이로 체감 선명도 높이기
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/lightroom/lightrooms-4-sharpening-methods-and-when-use-each-one-901105
  published_at: '2026-03-26'
  accessed_at: '2026-08-04T00:00:40Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: landscape-or-architecture-edge
  condition:
  - hard-boundary
  - horizon
  - architecture-edge
  intent:
  - increase-apparent-sharpness
  - edge-definition
  - avoid-global-sharpening
method:
  steps:
  - tool: Gradient mask
    parameter: 하늘과 바다 또는 건물과 하늘의 단단한 경계 한쪽에 마스크 정렬
    value: null
    unit: null
    reported_as: qualitative
  - tool: Whites or Exposure
    parameter: 경계 한쪽의 Whites 또는 Exposure를 미세하게 올림
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 맞닿은 두 영역의 톤 차이를 미세하게 키우면 실제 샤프닝을 추가하지 않아도 경계가 더 또렷하게 인식된다.
- 전역 선명화 대신 경계 한쪽에 제한하면 다른 질감이 거칠어지는 것을 피할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 3ca936a1d2a3276139c64d261496a06ef463d55eb69c57f2f0e9789d8f455488
  collected_at: '2026-08-04T00:00:40Z'
---

# 수평선이나 건축 경계 한쪽의 톤 차이로 체감 선명도 높이기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

바다와 하늘의 수평선이나 건물과 하늘처럼 단단한 경계가 흐릿하게 느껴지지만 전역 샤프닝으로 전체 질감을 거칠게 만들고 싶지 않을 때 사용한다.

## 촬영/작업 순서

1. 선명하게 보이게 할 단단한 경계를 찾는다.
2. Gradient 마스크의 단단한 가장자리를 경계선과 정렬해 한쪽 영역만 겨냥한다.
3. Whites 또는 Exposure를 미세하게 올려 맞닿은 두 영역의 톤 분리를 키운다.
4. 마스크 표시를 끄고 전체 화면에서 경계가 자연스럽게 또렷해졌는지 확인한다.

## 추천 시작값 / 조작값

- Gradient mask / 하늘과 바다 또는 건물과 하늘의 단단한 경계 한쪽에 마스크 정렬: 원문 정성 표현(수치 추정 없음)
- Whites or Exposure / 경계 한쪽의 Whites 또는 Exposure를 미세하게 올림: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 보정 전후를 번갈아 보며 실제 디테일 증가가 아니라 톤 분리에 의한 시각 효과임을 확인한다.
- 경계 주변에 밝은 띠가 보이면 노출량이나 마스크 정렬을 되돌린다.
- 다른 질감 영역까지 선명도가 필요하면 별도의 샤프닝 방식과 목적별로 조합한다.

## 주의할 점

- 이 방법은 잃어버린 초점이나 세부를 복원하지 않는다.
- 톤 차이를 과하게 만들면 수평선이나 건물 윤곽에 인공적인 밝은 테두리가 생길 수 있다.
- 부드러운 안개 경계처럼 원래 단단하지 않은 윤곽에는 부자연스러울 수 있다.

## 확실성과 근거

- 맞닿은 두 영역의 톤 차이를 미세하게 키우면 실제 샤프닝을 추가하지 않아도 경계가 더 또렷하게 인식된다.
- 전역 선명화 대신 경계 한쪽에 제한하면 다른 질감이 거칠어지는 것을 피할 수 있다.

출처가 수평선 하단의 하늘 또는 건물과 하늘 경계에 마스크를 맞추고 Whites나 Exposure를 미세하게 높여 체감 선명도를 만드는 방법을 직접 설명한다. 정확한 조정 수치는 없다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/lightrooms-4-sharpening-methods-and-when-use-each-one-901105
- 접근일: 2026-08-04
