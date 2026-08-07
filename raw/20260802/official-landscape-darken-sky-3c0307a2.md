---
schema_version: '1.0'
scenario_id: raw-20260802-skygradient01
title_ko: Adaptive Sky에 Linear Gradient를 더해 산 능선의 어두운 경계 완화
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
  subject: landscape
  condition:
  - bright-sky
  - mountain-horizon
  - hard-mask-edge
  intent:
  - darken-sky
  - soften-horizon-transition
  - guide-viewer-attention
method:
  steps:
  - tool: Lightroom Masking
    parameter: Adaptive Sky로 하늘을 자동 선택한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Exposure
    parameter: 선택된 하늘의 Exposure를 낮춘다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking
    parameter: 기존 sky mask에 Add로 Linear Gradient를 추가해 horizon을 가로질러 아래쪽으로 드래그한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Linear Gradient
    parameter: 산까지 과도하게 어두워지지 않으면서 경계가 부드러워지는 범위로 gradient extent를 조정한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mask display
    parameter: White on Black overlay로 결합된 선택 영역과 전환부를 확인한다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- AI Sky mask만으로 노출을 낮추면 horizon에서 보정이 단단하게 끊길 수 있으므로 Linear Gradient를 Add해 어두움이 경계 너머로 조금 번지게 하면 더 자연스러운
  전환을 만든다.
- 하늘을 어둡게 해 시선을 프레임 아래쪽 풍경으로 유도한다.
collection:
  collector_version: 1.0.0
  content_sha256: 3c0307a2903d2dd7ee8fb9a9cf3fb2c545d08970a7b00adaaa66c1035173c885
  collected_at: '2026-08-02T14:23:08Z'
---

# Adaptive Sky에 Linear Gradient를 더해 산 능선의 어두운 경계 완화

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

산이나 능선이 있는 풍경에서 하늘만 어둡게 했을 때 horizon을 따라 인공적인 단단한 경계가 생기는 경우에 쓴다.

## 촬영/작업 순서

1. Adaptive Sky로 하늘을 선택하고 Exposure를 낮춘다.
2. 같은 마스크에 Add로 Linear Gradient를 결합해 horizon을 가로질러 아래로 드래그한다.
3. gradient의 길이와 위치를 산에 보정이 깊게 침범하지 않는 범위로 줄인다.
4. White on Black overlay로 Sky와 Gradient가 만든 최종 영역을 확인한다.

## 추천 시작값 / 조작값

- Lightroom Masking / Adaptive Sky로 하늘을 자동 선택한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Exposure / 선택된 하늘의 Exposure를 낮춘다: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking / 기존 sky mask에 Add로 Linear Gradient를 추가해 horizon을 가로질러 아래쪽으로 드래그한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Linear Gradient / 산까지 과도하게 어두워지지 않으면서 경계가 부드러워지는 범위로 gradient extent를 조정한다: 원문 정성 표현(수치 추정 없음)
- Lightroom mask display / White on Black overlay로 결합된 선택 영역과 전환부를 확인한다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- overlay를 켜고 horizon을 확대해 hard edge가 사라졌는지 본다.
- gradient가 산 아래까지 내려가 전경을 부자연스럽게 어둡게 하면 끝점을 위로 되돌린다.
- overlay를 끈 뒤 하늘의 명암이 자연스럽고 시선이 프레임 아래로 이동하는지 전후 비교한다.

## 주의할 점

- Linear Gradient를 너무 멀리 끌면 산과 전경에 하늘용 노출 감소가 과도하게 적용된다.
- 경계를 완전히 흐리려다 피사체 주변에 halo처럼 보이는 전환을 만들지 않도록 overlay와 실제 이미지를 함께 확인한다.
- 원문은 Exposure의 정확한 수치를 제시하지 않으므로 이미지별로 정성 조정한다.

## 확실성과 근거

- AI Sky mask만으로 노출을 낮추면 horizon에서 보정이 단단하게 끊길 수 있으므로 Linear Gradient를 Add해 어두움이 경계 너머로 조금 번지게 하면 더 자연스러운 전환을 만든다.
- 하늘을 어둡게 해 시선을 프레임 아래쪽 풍경으로 유도한다.

Adaptive Sky, Exposure 감소, Linear Gradient Add, White on Black 확인 순서는 Adobe 튜토리얼이 직접 시연한다. 최적 gradient 범위와 노출량은 장면에 따라 달라 수치로 일반화하지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/advanced-lightroom-masking
- 접근일: 2026-08-02
