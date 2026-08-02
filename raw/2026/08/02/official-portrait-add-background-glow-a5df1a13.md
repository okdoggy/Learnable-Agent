---
schema_version: '1.0'
scenario_id: raw-20260802-backglow01
title_ko: Radial Gradient에서 Subject를 빼 인물 뒤에만 따뜻한 글로우 배치
status: validated
source:
  type: official
  publisher: Adobe
  author: Brian Matiash
  url: https://www.adobe.com/learn/lightroom-cc/web/advanced-lightroom-masking
  published_at: '2025-12-18'
  accessed_at: '2026-08-02T14:23:08Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait
  condition:
  - flat-background-light
  - subject-overlap
  - outdoor-portrait
  intent:
  - add-background-glow
  - preserve-subject-clarity
  - warm-background
method:
  steps:
  - tool: Lightroom Masking
    parameter: 인물 주위와 뒤쪽 배경을 덮는 Radial Gradient를 그린다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Dehaze
    parameter: Dehaze를 왼쪽으로 이동해 부드러운 glow를 만든다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking
    parameter: radial gradient에서 AI가 선택한 Subject를 Subtract한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Radial Gradient
    parameter: 필요하면 radial gradient를 이동하되 Subject 제외 상태를 유지한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Color
    parameter: Temperature를 높여 glow를 따뜻하게 만든다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking
    parameter: Amount로 완성된 glow 효과의 전체 강도를 조절한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mask display
    parameter: White on Black overlay로 radial 영역에서 인물이 잘 제외됐는지 확인한다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 배경 glow를 만드는 radial adjustment가 인물까지 덮으면 피사체가 흐려지므로 Subject를 Subtract해 빛이 인물 뒤를 감싸는 형태로 제한한다.
- negative Dehaze와 높은 Temperature를 함께 써 부드럽고 따뜻한 배경광 인상을 만든다.
collection:
  collector_version: 1.0.0
  content_sha256: a5df1a13c800405eb07c5d6c690cb795e7bd8dc1e90f3f07c9fb0770a0f7040d
  collected_at: '2026-08-02T14:23:08Z'
---

# Radial Gradient에서 Subject를 빼 인물 뒤에만 따뜻한 글로우 배치

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

야외 인물 사진에서 피사체 뒤 배경에 따뜻하고 부드러운 광원을 더하고 싶지만 haze가 인물의 선명도까지 떨어뜨리는 경우에 사용한다.

## 촬영/작업 순서

1. 인물과 뒤쪽 배경을 감싸는 Radial Gradient를 만든다.
2. Dehaze를 음의 방향으로 조정해 부드러운 glow를 만든다.
3. 같은 마스크에서 Subtract Subject로 인물을 제외한다.
4. radial 위치를 다듬고 Temperature로 색을 따뜻하게 한 뒤 Amount로 전체 강도를 맞춘다.
5. White on Black overlay로 인물의 제외 상태를 검증한다.

## 추천 시작값 / 조작값

- Lightroom Masking / 인물 주위와 뒤쪽 배경을 덮는 Radial Gradient를 그린다: 원문 정성 표현(수치 추정 없음)
- Lightroom Dehaze / Dehaze를 왼쪽으로 이동해 부드러운 glow를 만든다: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking / radial gradient에서 AI가 선택한 Subject를 Subtract한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Radial Gradient / 필요하면 radial gradient를 이동하되 Subject 제외 상태를 유지한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Color / Temperature를 높여 glow를 따뜻하게 만든다: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking / Amount로 완성된 glow 효과의 전체 강도를 조절한다: 원문 정성 표현(수치 추정 없음)
- Lightroom mask display / White on Black overlay로 radial 영역에서 인물이 잘 제외됐는지 확인한다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 먼저 glow의 위치와 크기를 잡은 뒤 Subject 제외 경계가 머리카락과 몸 주위에서 자연스러운지 확인한다.
- gradient를 이동해도 Subject가 계속 제외되는지 overlay로 재확인한다.
- Amount를 낮췄다 올리며 배경광이 느껴지되 인물 주변에 인공적인 후광이 두드러지지 않는 지점을 찾는다.

## 주의할 점

- Subject를 빼지 않으면 negative Dehaze가 피부와 의상까지 흐리게 만든다.
- Temperature와 negative Dehaze를 과도하게 적용하면 배경이 탁하거나 인공적인 halo처럼 보일 수 있다.
- 원문은 Dehaze, Temperature, Amount의 정확한 값을 제시하지 않았다.

## 확실성과 근거

- 배경 glow를 만드는 radial adjustment가 인물까지 덮으면 피사체가 흐려지므로 Subject를 Subtract해 빛이 인물 뒤를 감싸는 형태로 제한한다.
- negative Dehaze와 높은 Temperature를 함께 써 부드럽고 따뜻한 배경광 인상을 만든다.

Radial Gradient, negative Dehaze, Subtract Subject, Temperature와 Amount 조절은 Adobe가 인물 예제로 직접 시연했다. 효과의 미적 강도와 가장 자연스러운 위치는 사진별 판단 영역이다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/advanced-lightroom-masking
- 접근일: 2026-08-02
