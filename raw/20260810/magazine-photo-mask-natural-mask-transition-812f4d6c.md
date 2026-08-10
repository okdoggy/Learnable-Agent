---
schema_version: '1.0'
scenario_id: raw-20260810-maskedge
title_ko: 복잡한 AI 마스크 경계를 Feather와 Edge로 자연스럽게 다듬기
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke / Matt Kloskowski
  url: https://fstoppers.com/education/two-new-sliders-make-every-lightroom-mask-look-more-natural-903883
  published_at: '2026-08-06'
  accessed_at: '2026-08-10T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom / Lightroom Classic
scenario:
  subject: photo-mask
  condition:
  - ai-mask
  - complex-edge
  - visible-halo
  intent:
  - natural-mask-transition
  - remove-seams
  - reduce-manual-brushing
method:
  steps:
  - tool: Mask Feather
    parameter: Feather 조절 가능 범위
    value: 0–100
    unit: null
    reported_as: exact
  - tool: Mask Edge
    parameter: Edge 시작 위치
    value: 0
    unit: null
    reported_as: exact
  - tool: Mask Edge
    parameter: 선택 범위를 수축하려면 왼쪽, 확장하려면 오른쪽으로 Edge 이동
    value: null
    unit: null
    reported_as: qualitative
  - tool: AI mask refinement
    parameter: 실제 톤·밝기 조정을 먼저 적용한 후 보이는 경계에 맞춰 Feather와 Edge 조정
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 나뭇잎, 털, 수평선은 자동 선택이 완벽하기 어려우므로 대략 맞는 마스크를 실제 보정 상태에서 눈으로 블렌딩하는 편이 효율적이다.
- Feather는 딱딱한 전환을 완화하고 Edge는 선택 범위의 부족이나 과잉을 보정한다.
collection:
  collector_version: 1.0.0
  content_sha256: 812f4d6cfcea34334f0b2504189a885e173d7792c1bb3aa089497d49b74eea99
  collected_at: '2026-08-10T00:00:00Z'
---

# 복잡한 AI 마스크 경계를 Feather와 Edge로 자연스럽게 다듬기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

하늘, 피사체, 배경 등 AI 마스크가 나뭇가지·털·수평선 주변에 딱딱한 seam이나 halo를 만들 때 사용한다.

## 촬영/작업 순서

1. AI 기반 Subject, Sky, Background, People, Landscape 또는 Select Objects 마스크를 만든다.
2. 원하는 밝기나 톤 조정을 먼저 적용해 실제 경계 문제를 드러낸다.
3. 선택이 세부 영역에 덜 닿으면 Edge를 오른쪽으로 옮기고, 과하게 번지면 왼쪽으로 옮긴다.
4. 경계가 딱딱하면 Feather를 추가한다.
5. 최종 강도에서 확대해 자연스러운 전환인지 확인한다.

## 추천 시작값 / 조작값

- Mask Feather / Feather 조절 가능 범위: 0–100
- Mask Edge / Edge 시작 위치: 0
- Mask Edge / 선택 범위를 수축하려면 왼쪽, 확장하려면 오른쪽으로 Edge 이동: 원문 정성 표현(수치 추정 없음)
- AI mask refinement / 실제 톤·밝기 조정을 먼저 적용한 후 보이는 경계에 맞춰 Feather와 Edge 조정: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- AI 마스크를 만든 직후 완벽하게 다듬으려 하지 말고 먼저 의도한 밝기나 톤 조정을 적용한다.
- 경계 결함이 잘 보이도록 필요하면 보정을 잠시 강하게 해 seam을 확인한다.
- 선택이 짧으면 Edge를 오른쪽으로 확장하고, 딱딱한 전환은 Feather로 부드럽게 만든다.
- 최종 보정 강도로 돌아와 foliage, fur, skyline 경계를 눈으로 확인한다.

## 주의할 점

- Feather와 Edge를 임의의 극값으로 밀지 말고 실제 보정이 적용된 상태에서 경계를 보고 조절한다.
- Edge 확장은 인접 영역까지 보정을 침범시킬 수 있으므로 나뭇가지와 수평선을 확대 검사한다.
- Brush, Linear Gradient, Radial Gradient는 자체 feather 제어가 있어 이 새 Edge·Feather 대상에서 제외된다.

## 확실성과 근거

- 나뭇잎, 털, 수평선은 자동 선택이 완벽하기 어려우므로 대략 맞는 마스크를 실제 보정 상태에서 눈으로 블렌딩하는 편이 효율적이다.
- Feather는 딱딱한 전환을 완화하고 Edge는 선택 범위의 부족이나 과잉을 보정한다.

Fstoppers의 Alex Cooke가 Lightroom 교육자 Matt Kloskowski의 시연을 요약한 자료다. Feather 범위와 Edge 방향, 적용 순서, 지원 마스크 종류가 직접 명시되어 있다.

## 출처

- 원문 URL: https://fstoppers.com/education/two-new-sliders-make-every-lightroom-mask-look-more-natural-903883
- 접근일: 2026-08-10
