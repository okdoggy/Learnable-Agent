---
schema_version: '1.0'
scenario_id: raw-20260805-intersectlight01
title_ko: Intersect 마스크로 풍경과 건축의 빛 방향 제한
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; Mickey Pullen
  url: https://fstoppers.com/lightroom/intersect-masks-control-youre-missing-lightroom-721432
  published_at: '2026-01-07'
  accessed_at: '2026-08-05T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: landscape-or-architecture
  condition:
  - broad-mask-spill
  - directional-light
  intent:
  - precise-local-light
  - natural-light-shaping
method:
  steps:
  - tool: Lightroom Masking
    parameter: 자동 선택이나 넓은 그라디언트로 조정할 기본 영역 구성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Intersect
    parameter: 두 번째 마스크와 겹치는 부분만 남겨 조정 범위 제한
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Radial or Linear Gradient
    parameter: Intersect와 결합해 빛이 특정 방향에서 들어오는 형태로 조명 구성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Brush
    parameter: 넓거나 지능형 선택으로 구조를 만든 뒤 필요한 경계만 절제해 정리
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Intersect는 두 마스크의 겹침만 유지하므로 넓은 자동 선택을 손으로 다시 칠하지 않고도 필요한 방향과 범위로 제한할 수 있다.
- 풍경과 건축 사진에서 그라디언트의 모양을 겹침으로 다듬으면 빛의 출처가 한쪽에 있는 것처럼 자연스러운 방향성을 만들 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 0f56bfb729231be1fa31e8c229961984b5e49741fc063e1bda5b839d15167344
  collected_at: '2026-08-05T00:00:00Z'
---

# Intersect 마스크로 풍경과 건축의 빛 방향 제한

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

하늘, 피사체 또는 넓은 그라디언트 마스크가 목표 영역 밖으로 번지고, 브러시로 복잡하게 지우지 않으면서 빛의 방향을 정밀하게 만들고 싶을 때 사용한다.

## 촬영/작업 순서

1. 자동 마스크나 큰 그라디언트로 기본 선택을 만든다.
2. 두 번째 방사형 또는 선형 그라디언트와 Intersect해 겹치는 범위만 남긴다.
3. 노출이나 색 조정이 실제 광원 방향과 맞는지 전체 화면에서 확인한다.
4. 경계의 작은 누락만 확대해 브러시로 정리한다.
5. 마스크 핀이 판단을 방해하면 숨기고 최종 효과가 자연스러운지 평가한다.

## 추천 시작값 / 조작값

- Lightroom Masking / 자동 선택이나 넓은 그라디언트로 조정할 기본 영역 구성: 원문 정성 표현(수치 추정 없음)
- Lightroom Intersect / 두 번째 마스크와 겹치는 부분만 남겨 조정 범위 제한: 원문 정성 표현(수치 추정 없음)
- Lightroom Radial or Linear Gradient / Intersect와 결합해 빛이 특정 방향에서 들어오는 형태로 조명 구성: 원문 정성 표현(수치 추정 없음)
- Lightroom Brush / 넓거나 지능형 선택으로 구조를 만든 뒤 필요한 경계만 절제해 정리: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 오버레이로 실제 겹침 영역을 확인한 뒤 조정값을 적용한다.
- 서로 다른 톤이나 색이 필요한 떨어진 영역은 하나의 마스크에 묶지 않고 별도 마스크로 나눈다.
- 확대 상태에서 경계를 검사하고 축소 상태에서 빛의 방향과 전체 자연스러움을 재확인한다.

## 주의할 점

- Intersect와 Add, Subtract를 혼동하면 의도하지 않은 영역이 남거나 사라질 수 있다.
- 서로 다른 보정이 필요한 영역을 한 마스크에 넣으면 슬라이더 변경이 모두에 동시에 적용된다.
- 복잡한 브러시 획을 늘리기 전에 자동 선택과 그라디언트의 겹침으로 해결 가능한지 확인한다.

## 확실성과 근거

- Intersect는 두 마스크의 겹침만 유지하므로 넓은 자동 선택을 손으로 다시 칠하지 않고도 필요한 방향과 범위로 제한할 수 있다.
- 풍경과 건축 사진에서 그라디언트의 모양을 겹침으로 다듬으면 빛의 출처가 한쪽에 있는 것처럼 자연스러운 방향성을 만들 수 있다.

출처가 Intersect의 겹침 유지 원리와 방사형·선형 그라디언트를 결합한 방향성 조명, 확대 경계 검사, 별도 마스크 분리 원칙을 직접 설명한다. 구체적 보정 강도는 제시되지 않아 수치화하지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/intersect-masks-control-youre-missing-lightroom-721432
- 접근일: 2026-08-05
