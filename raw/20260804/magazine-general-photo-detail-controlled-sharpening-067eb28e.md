---
schema_version: '1.0'
scenario_id: raw-20260804-detailsharp01
title_ko: Lightroom Detail 패널에서 진단 오버레이로 전역 샤프닝 시작점 설정
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
  subject: general-photo-detail
  condition:
  - raw-development
  - global-sharpening
  - detail-evaluation
  intent:
  - controlled-sharpening
  - target-structural-detail
  - avoid-guessing
method:
  steps:
  - tool: Detail panel sharpening
    parameter: Radius를 끝까지 낮춤
    value: null
    unit: null
    reported_as: qualitative
  - tool: Detail panel sharpening
    parameter: Detail을 끝까지 올림
    value: null
    unit: null
    reported_as: qualitative
  - tool: Detail panel sharpening
    parameter: Masking 권장 시작 범위의 하한
    value: 30
    unit: slider value
    reported_as: exact
  - tool: Detail panel sharpening
    parameter: Masking 권장 시작 범위의 상한
    value: 70
    unit: slider value
    reported_as: exact
  - tool: Detail panel sharpening
    parameter: Amount 권장 시작 범위의 하한
    value: 40
    unit: slider value
    reported_as: exact
  - tool: Detail panel sharpening
    parameter: Amount 권장 시작 범위의 상한
    value: 90
    unit: slider value
    reported_as: exact
  - tool: Detail panel sharpening
    parameter: Alt를 누른 채 Masking과 Detail의 진단 오버레이를 확인
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Radius, Detail, Masking, Amount의 역할을 나누고 진단 오버레이로 실제 적용 구조를 보면 Amount 하나를 임의로 높이는 것보다 의도적인 전역 샤프닝이 가능하다.
- Masking을 먼저 정리하면 평탄한 영역의 불필요한 선명화 위험을 줄일 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 067eb28efce9a14c3ef8df6db1d30be868d7b4042385610598e6800b75f7743d
  collected_at: '2026-08-04T00:00:40Z'
---

# Lightroom Detail 패널에서 진단 오버레이로 전역 샤프닝 시작점 설정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

사진 전체의 선명도를 무작정 Amount 하나로 올리지 않고 구조와 세부가 있는 영역을 보면서 반복 가능한 시작점을 만들고 싶을 때 사용한다.

## 촬영/작업 순서

1. Detail 패널에서 Radius를 끝까지 낮추고 Detail을 끝까지 올린다.
2. Masking을 원문이 제시한 약 30–70 범위에서 사진 구조에 맞게 정한다.
3. Amount를 약 40–90 범위에서 필요한 선명도에 맞게 정한다.
4. Masking과 Detail을 움직일 때 Alt를 눌러 진단 오버레이를 보고 어떤 구조가 대상이 되는지 확인한다.
5. 전체 화면과 확대 화면에서 노이즈와 윤곽의 과장을 점검한 뒤 시작값을 사진별로 수정한다.

## 추천 시작값 / 조작값

- Detail panel sharpening / Radius를 끝까지 낮춤: 원문 정성 표현(수치 추정 없음)
- Detail panel sharpening / Detail을 끝까지 올림: 원문 정성 표현(수치 추정 없음)
- Detail panel sharpening / Masking 권장 시작 범위의 하한: 30 slider value
- Detail panel sharpening / Masking 권장 시작 범위의 상한: 70 slider value
- Detail panel sharpening / Amount 권장 시작 범위의 하한: 40 slider value
- Detail panel sharpening / Amount 권장 시작 범위의 상한: 90 slider value
- Detail panel sharpening / Alt를 누른 채 Masking과 Detail의 진단 오버레이를 확인: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Alt 오버레이에서 중요한 구조가 포함되고 평탄한 영역이 불필요하게 강조되지 않는지 확인한다.
- Amount를 올리기 전에 Masking으로 적용 대상을 정리한다.
- 질감이 필요한 특정 부위만 더 선명해야 하면 전역값을 더 올리지 말고 로컬 마스크를 별도로 고려한다.

## 주의할 점

- 제시 범위는 반복 가능한 시작점이지 모든 사진의 고정 정답이 아니다.
- 평탄한 하늘이나 피부까지 전역 샤프닝하면 노이즈와 거친 질감이 두드러질 수 있다.
- 초점이 벗어났거나 사라진 세부를 샤프닝으로 복원할 수는 없다.

## 확실성과 근거

- Radius, Detail, Masking, Amount의 역할을 나누고 진단 오버레이로 실제 적용 구조를 보면 Amount 하나를 임의로 높이는 것보다 의도적인 전역 샤프닝이 가능하다.
- Masking을 먼저 정리하면 평탄한 영역의 불필요한 선명화 위험을 줄일 수 있다.

출처가 Radius 최저, Detail 최고, Masking 약 30–70, Amount 약 40–90 및 Alt 진단 오버레이를 직접 제시한다. 범위의 경계값은 원문의 수치를 그대로 분리해 기록했고 Radius와 Detail은 수치 없이 정성 표현으로 보존했다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/lightrooms-4-sharpening-methods-and-when-use-each-one-901105
- 접근일: 2026-08-04
