---
schema_version: '1.0'
scenario_id: raw-20260802-skyvariance01
title_ko: Point Color와 Sky 마스크로 불균일한 하늘색 완화
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
  subject: landscape-sky
  condition:
  - uneven-sky-color
  - polarized-sky
  intent:
  - harmonize-sky-color
  - selective-color-correction
method:
  steps:
  - tool: Masking > Sky
    parameter: AI로 하늘 영역 선택
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color Eyedropper
    parameter: 가장 어두운 파랑과 가장 밝은 파랑의 중간색을 샘플링
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color
    parameter: Variance를 왼쪽으로 이동
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color
    parameter: Luminance를 필요하면 약간 감소
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color
    parameter: Saturation을 필요하면 소폭 증가
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Variance를 줄이면 표본과 비슷한 색들의 차이가 완화된다.
- Sky 마스크를 함께 쓰면 같은 계열 색을 가진 지상 물체까지 바뀌는 것을 막을 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 89c8987d0a853ea7f3752061d888c9f599bbcd3e91cdf888890460b31652c278
  collected_at: '2026-08-02T00:00:00Z'
---

# Point Color와 Sky 마스크로 불균일한 하늘색 완화

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

편광 필터나 태양 위치 때문에 풍경 사진의 파란 하늘이 구간별로 진하고 옅게 갈라졌을 때 색 차이를 자연스럽게 줄인다.

## 촬영/작업 순서

1. 기본 보정을 마친 뒤 Sky 마스크로 하늘을 분리한다.
2. Point Color로 파랑 범위의 중간색을 잡는다.
3. Variance를 낮춰 파랑을 통일하고 필요하면 밝기와 채도를 조정한다.

## 추천 시작값 / 조작값

- Masking > Sky / AI로 하늘 영역 선택: 원문 정성 표현(수치 추정 없음)
- Point Color Eyedropper / 가장 어두운 파랑과 가장 밝은 파랑의 중간색을 샘플링: 원문 정성 표현(수치 추정 없음)
- Point Color / Variance를 왼쪽으로 이동: 원문 정성 표현(수치 추정 없음)
- Point Color / Luminance를 필요하면 약간 감소: 원문 정성 표현(수치 추정 없음)
- Point Color / Saturation을 필요하면 소폭 증가: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 마스킹 패널 상단의 Eye 아이콘으로 전후를 비교한다.
- 하늘이 지나치게 균일하거나 과포화되지 않았는지 확인한다.

## 주의할 점

- Variance를 오른쪽으로 이동하면 파란색 차이가 커져 불균일한 하늘이 더 두드러질 수 있다.
- 마스크 오버레이로 하늘 선택 범위를 확인한다.

## 확실성과 근거

- Variance를 줄이면 표본과 비슷한 색들의 차이가 완화된다.
- Sky 마스크를 함께 쓰면 같은 계열 색을 가진 지상 물체까지 바뀌는 것을 막을 수 있다.

Adobe 공식 튜토리얼이 Sky 마스크, 중간 밝기의 파란색 샘플링, Variance 감소 순서를 직접 설명한다. 나머지 조정량은 수치가 없어 정성값으로 기록했다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/precise-color-adjustments
- 접근일: 2026-08-02
