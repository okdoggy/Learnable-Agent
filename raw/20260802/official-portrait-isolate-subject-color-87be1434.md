---
schema_version: '1.0'
scenario_id: raw-20260802-subjectcolor01
title_ko: Subject와 Color Range 교차로 인물 의상의 특정 색만 교체
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
  - repeated-color-in-background
  - colored-clothing
  - precise-color-selection
  intent:
  - isolate-subject-color
  - replace-garment-hue
  - protect-background-color
method:
  steps:
  - tool: Lightroom Masking
    parameter: Select Subject로 인물 전체를 기본 마스크로 선택한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking
    parameter: Subject mask 안에서 Intersect with Mask Using의 Color Range를 선택한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Color Range
    parameter: 변경하려는 의상 또는 장비의 색을 샘플링한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Color Range
    parameter: Refine으로 인물 안에서도 목표 색만 남도록 선택 범위를 좁힌다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Color
    parameter: Use Fine Adjustment를 끄고 Hue control로 선택 색을 원하는 hue로 교체한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mask display
    parameter: overlay로 배경의 비슷한 색과 인물의 다른 부위가 제외됐는지 확인한다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Color Range만 쓰면 배경의 비슷한 색도 함께 바뀔 수 있으므로 Subject와 교차해 후보 영역을 먼저 인물 내부로 제한한다.
- 그 안에서 Refine으로 목표 의상색을 좁히면 다른 색을 보호하면서 hue를 정밀하게 바꿀 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 87be1434ee7fe67a38314c2b9ffbd6286a10ab77750bbd34acb25470b8a8a785
  collected_at: '2026-08-02T14:23:08Z'
---

# Subject와 Color Range 교차로 인물 의상의 특정 색만 교체

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

인물의 의상이나 장비 색을 바꾸려는데 장면의 배경에도 비슷한 색이 있어 Color Range 단독 선택이 번지는 경우에 적용한다.

## 촬영/작업 순서

1. Select Subject로 인물을 선택한다.
2. Subject mask 메뉴에서 Intersect with Mask Using의 Color Range를 선택한다.
3. 목표 의상색을 샘플링하고 Refine으로 범위를 좁힌다.
4. Color 패널에서 Use Fine Adjustment를 끄고 Hue로 색을 교체한다.
5. overlay와 실제 이미지로 인물 밖의 유사 색이 보호되는지 검증한다.

## 추천 시작값 / 조작값

- Lightroom Masking / Select Subject로 인물 전체를 기본 마스크로 선택한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking / Subject mask 안에서 Intersect with Mask Using의 Color Range를 선택한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Color Range / 변경하려는 의상 또는 장비의 색을 샘플링한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Color Range / Refine으로 인물 안에서도 목표 색만 남도록 선택 범위를 좁힌다: 원문 정성 표현(수치 추정 없음)
- Lightroom Color / Use Fine Adjustment를 끄고 Hue control로 선택 색을 원하는 hue로 교체한다: 원문 정성 표현(수치 추정 없음)
- Lightroom mask display / overlay로 배경의 비슷한 색과 인물의 다른 부위가 제외됐는지 확인한다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Refine을 넓은 상태에서 시작해 목표 의상색의 명암 변형을 충분히 포함하는지 본다.
- 점차 범위를 좁히며 피부, 배경, 다른 의상이 빠지는 지점을 찾는다.
- Hue 변경 후 가장자리의 누락과 오염을 확대 확인하고 필요하면 샘플과 Refine을 다시 조정한다.

## 주의할 점

- Color Range를 지나치게 좁히면 의상 주름의 밝거나 어두운 부분이 누락될 수 있다.
- 범위를 너무 넓히면 인물 내부의 피부나 다른 소품색까지 바뀔 수 있다.
- Subject mask의 AI 경계가 부정확한 경우 Add나 Subtract로 먼저 보완해야 한다.
- 원문은 Refine과 Hue의 정확한 수치를 제시하지 않았다.

## 확실성과 근거

- Color Range만 쓰면 배경의 비슷한 색도 함께 바뀔 수 있으므로 Subject와 교차해 후보 영역을 먼저 인물 내부로 제한한다.
- 그 안에서 Refine으로 목표 의상색을 좁히면 다른 색을 보호하면서 hue를 정밀하게 바꿀 수 있다.

Subject와 Color Range의 Intersect, 색 샘플링, Refine, Hue 교체 과정은 Adobe가 붉은 gaiters와 microspikes 예제로 직접 설명한다. 다른 재질과 색에서 필요한 범위는 이미지에 따라 달라진다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/advanced-lightroom-masking
- 접근일: 2026-08-02
