---
schema_version: '1.0'
scenario_id: raw-20260802-vintageback01
title_ko: 빈티지 렌즈의 씻긴 배경을 마스크로 복원하고 온도 분리
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/how-edit-portrait-skin-tones-lightroom-902830
  published_at: '2026-06-09'
  accessed_at: '2026-08-02T00:00:00Z'
  original_language: en
device:
  capture_device: Canon 100mm vintage lens
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait-background
  condition:
  - washed-out-background
  - vintage-lens-portrait
  intent:
  - restore-background-contrast
  - warm-cool-separation
method:
  steps:
  - tool: Background mask
    parameter: 배경 선택
    value: null
    unit: null
    reported_as: qualitative
  - tool: Background mask
    parameter: 배경 Exposure와 Clarity 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Subtract Radial Gradient
    parameter: 배경 선택에서 radial gradient를 빼 피사체 쪽 빛 유지
    value: null
    unit: null
    reported_as: qualitative
  - tool: Color adjustment
    parameter: 피부는 따뜻하게 두고 배경 냉각
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 배경만 선택적으로 복원하면 피사체의 피부와 빛을 보존할 수 있다.
- 따뜻한 피사체와 차가운 배경의 분리는 깊이와 가독성을 높인다.
collection:
  collector_version: 1.0.0
  content_sha256: 5a0d3b5a98b553db1e31dec378d79a7c4234aa4db59780720e0da68725d9d1a6
  collected_at: '2026-08-02T00:00:00Z'
---

# 빈티지 렌즈의 씻긴 배경을 마스크로 복원하고 온도 분리

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

오래된 렌즈로 촬영한 인물 사진에서 배경이 씻긴 듯 흐리고 피사체와 분리가 약할 때 선택적으로 대비와 색온도를 정리한다.

## 촬영/작업 순서

1. 배경 마스크를 만든다.
2. 배경의 노출과 선명도를 조정한다.
3. 방사형 그라디언트를 빼 피사체 쪽 빛을 남긴다.
4. 배경은 차갑게, 피부는 따뜻하게 유지한다.

## 추천 시작값 / 조작값

- Background mask / 배경 선택: 원문 정성 표현(수치 추정 없음)
- Background mask / 배경 Exposure와 Clarity 조정: 원문 정성 표현(수치 추정 없음)
- Subtract Radial Gradient / 배경 선택에서 radial gradient를 빼 피사체 쪽 빛 유지: 원문 정성 표현(수치 추정 없음)
- Color adjustment / 피부는 따뜻하게 두고 배경 냉각: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 마스크 전후로 배경의 씻긴 느낌과 피사체 분리를 비교한다.
- 피부는 따뜻하게 유지되고 배경만 차가워졌는지 확인한다.
- 방사형으로 남긴 빛이 피사체에 자연스럽게 집중되는지 점검한다.

## 주의할 점

- Background 마스크가 피사체를 침범하지 않는지 확인한다.
- 배경의 Exposure와 Clarity를 과도하게 보정하면 오래된 렌즈 특유의 분위기가 사라질 수 있다.
- 차가운 배경과 따뜻한 피부의 분리가 부자연스러운 색 경계로 보이지 않게 조절한다.

## 확실성과 근거

- 배경만 선택적으로 복원하면 피사체의 피부와 빛을 보존할 수 있다.
- 따뜻한 피사체와 차가운 배경의 분리는 깊이와 가독성을 높인다.

Fstoppers 기사가 오래된 Canon 100mm 렌즈의 씻긴 배경을 Background 마스크, radial gradient 빼기, 배경 냉각으로 보정하는 과정을 설명한다. 수치는 제공하지 않는다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-edit-portrait-skin-tones-lightroom-902830
- 접근일: 2026-08-02
