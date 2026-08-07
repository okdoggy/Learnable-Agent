---
schema_version: '1.0'
scenario_id: raw-20260807-harshskin01
title_ko: 한낮의 거친 피부 명암을 역 S-curve와 Amount 블렌딩으로 압축
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/lightrooms-tone-curve-explained-every-trick-need-know-902177
  published_at: '2026-05-08'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait
  condition:
  - harsh-midday-light
  - high-skin-contrast
  intent:
  - soften-skin-light
  - compress-tonal-range
method:
  steps:
  - tool: Tone Curve
    parameter: 일반적인 S-curve와 반대로 하이라이트를 내리고 그림자를 올려 피부의 거친 명암 차이를 압축
    value: null
    unit: null
    reported_as: qualitative
  - tool: Amount
    parameter: 곡선 보정의 전체 강도를 블렌딩해 과한 보정을 줄임
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 이미 대비가 강한 한낮 피부에 일반 S-curve를 더하면 거친 빛이 강화될 수 있다.
- 하이라이트를 낮추고 그림자를 올리면 피부의 밝고 어두운 면 차이를 압축해 빛을 부드럽게 보이게 한다.
- Amount로 결과를 혼합하면 곡선의 최대 효과를 그대로 받아들이지 않고 장면에 맞는 강도로 조절할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 671af3f886ae2e6ae9a0c5f6fb52911d7d88e490907882576e97e3fa4033994e
  collected_at: '2026-08-07T00:00:00Z'
---

# 한낮의 거친 피부 명암을 역 S-curve와 Amount 블렌딩으로 압축

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

한낮의 강한 빛 때문에 인물 피부의 하이라이트와 그림자 차이가 지나치게 커서 일반적인 대비 증가가 오히려 피부를 더 거칠게 만드는 경우에 사용한다.

## 촬영/작업 순서

1. 피부에 이미 존재하는 하이라이트와 그림자의 강한 차이를 확인한다.
2. Tone Curve에서 일반 S-curve와 반대로 하이라이트 구간을 낮춘다.
3. 그림자 구간을 올려 명암 차이를 압축한다.
4. Amount 슬라이더로 보정 강도를 낮추거나 높여 원본과 자연스럽게 혼합한다.
5. 피부가 부드러워졌는지 확인하되 얼굴의 입체감이 사라지지 않도록 비교한다.

## 추천 시작값 / 조작값

- Tone Curve / 일반적인 S-curve와 반대로 하이라이트를 내리고 그림자를 올려 피부의 거친 명암 차이를 압축: 원문 정성 표현(수치 추정 없음)
- Amount / 곡선 보정의 전체 강도를 블렌딩해 과한 보정을 줄임: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 곡선 형태를 먼저 만든 뒤 Amount로 강도를 조절한다.
- 피부의 밝은 면이 눌리고 어두운 면이 열리는 정도를 함께 관찰한다.
- 보정 전후를 비교해 거친 빛만 줄고 얼굴 구조는 남았는지 확인한다.

## 주의할 점

- 기존 빛이 이미 강한데 습관적으로 S-curve를 적용하면 대비가 더 거칠어질 수 있다.
- 하이라이트와 그림자를 과도하게 압축하면 피부가 평면적으로 보일 수 있다.
- 원문에 곡선 좌표나 Amount의 정확한 수치는 제시되지 않았다.

## 확실성과 근거

- 이미 대비가 강한 한낮 피부에 일반 S-curve를 더하면 거친 빛이 강화될 수 있다.
- 하이라이트를 낮추고 그림자를 올리면 피부의 밝고 어두운 면 차이를 압축해 빛을 부드럽게 보이게 한다.
- Amount로 결과를 혼합하면 곡선의 최대 효과를 그대로 받아들이지 않고 장면에 맞는 강도로 조절할 수 있다.

Fstoppers 기사가 거친 한낮 피부에서 하이라이트를 내리고 그림자를 올리는 역 S-curve 방향과 Amount를 통한 강도 블렌딩을 직접 설명한다. 정확한 수치는 없어 정성적으로 기록했다.

## 출처

- 원문 URL: https://fstoppers.com/education/lightrooms-tone-curve-explained-every-trick-need-know-902177
- 접근일: 2026-08-07
