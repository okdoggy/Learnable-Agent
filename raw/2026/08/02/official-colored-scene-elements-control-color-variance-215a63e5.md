---
schema_version: '1.0'
scenario_id: raw-20260802-pointcolor01
title_ko: Point Color 중간색 샘플로 유사 색의 통일감 또는 대비 제어
status: validated
source:
  type: official
  publisher: Adobe
  author: Seán Duggan
  url: https://www.adobe.com/learn/lightroom-cc/web/precise-color-adjustments
  published_at: '2026-03-18'
  accessed_at: '2026-08-02T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: colored-scene-elements
  condition:
  - subtle-color-variation
  - similar-colors-across-scene
  intent:
  - control-color-variance
  - selective-color-styling
method:
  steps:
  - tool: Edit
    parameter: 초기 기본 보정 적용
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color Eyedropper
    parameter: 대상 색 범위의 어두운 값과 밝은 값 사이 중간색 샘플링
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color
    parameter: 유사 색을 통일하려면 Variance를 왼쪽으로 이동
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color
    parameter: 유사 색 차이를 강조하려면 Variance를 오른쪽으로 이동
    value: null
    unit: null
    reported_as: qualitative
  - tool: Masking
    parameter: 영향 범위를 제한해야 하면 마스크 결합
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 중간색을 기준으로 잡으면 대상 범위의 밝고 어두운 변형을 함께 다루기 쉽다.
- Variance 방향으로 비슷한 색을 통일하거나 차이를 강조할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 215a63e5552e65f3746bc6c6f2e106279ee4908bc1ea1ba88d7c06c87765c9fc
  collected_at: '2026-08-02T00:00:00Z'
---

# Point Color 중간색 샘플로 유사 색의 통일감 또는 대비 제어

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

잔디처럼 한 대상 안에 비슷하지만 미묘하게 다른 색들이 섞여 있을 때 색을 더 균일하게 만들거나 반대로 차이를 강조한다.

## 촬영/작업 순서

1. 기본 보정 후 대상 색 범위의 중간색을 샘플링한다.
2. Hue, Saturation, Luminance와 범위를 조정한다.
3. Variance 방향으로 색 통일 또는 대비를 정한다.
4. 불필요한 영역까지 바뀌면 마스크로 제한한다.

## 추천 시작값 / 조작값

- Edit / 초기 기본 보정 적용: 원문 정성 표현(수치 추정 없음)
- Point Color Eyedropper / 대상 색 범위의 어두운 값과 밝은 값 사이 중간색 샘플링: 원문 정성 표현(수치 추정 없음)
- Point Color / 유사 색을 통일하려면 Variance를 왼쪽으로 이동: 원문 정성 표현(수치 추정 없음)
- Point Color / 유사 색 차이를 강조하려면 Variance를 오른쪽으로 이동: 원문 정성 표현(수치 추정 없음)
- Masking / 영향 범위를 제한해야 하면 마스크 결합: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Variance를 양쪽으로 움직여 통일과 분리 중 의도에 맞는 방향을 확인한다.
- 다른 영역의 유사 색이 변했는지 전후 비교하고 필요하면 마스크로 제한한다.

## 주의할 점

- 전역 Point Color는 비슷한 색의 나무 등 의도하지 않은 영역도 바꿀 수 있으므로 필요하면 마스크를 결합한다.
- 표본을 가장 어둡거나 밝은 극단에서 고르지 않는다.

## 확실성과 근거

- 중간색을 기준으로 잡으면 대상 범위의 밝고 어두운 변형을 함께 다루기 쉽다.
- Variance 방향으로 비슷한 색을 통일하거나 차이를 강조할 수 있다.

Adobe 공식 튜토리얼이 잔디 예제로 중간색 샘플과 Variance 양방향 효과를 직접 설명한다. 정확한 슬라이더 값은 없다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/precise-color-adjustments
- 접근일: 2026-08-02
