---
schema_version: '1.0'
scenario_id: raw-20260807-skintex15
title_ko: Facial Skin 마스크에서 부드러움과 그레인으로 자연스러운 피부 질감 유지
status: validated
source:
  type: official
  publisher: Adobe Lightroom Learn
  author: Kristina Sherk
  url: https://www.adobe.com/learn/lightroom-cc/web/ai-portrait-mask-lightroom
  published_at: '2025-12-18'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait
  condition:
  - portrait
  - visible-skin-texture
  - ai-person-mask-available
  intent:
  - natural-skin-smoothing
  - retain-texture
  - local-retouch
method:
  steps:
  - tool: Lightroom Masking > People > Facial Skin
    parameter: Facial Skin mask Texture
    value: -20
    unit: Lightroom slider
    reported_as: exact
  - tool: Lightroom Masking > People > Facial Skin
    parameter: Facial Skin mask Clarity
    value: -25
    unit: Lightroom slider
    reported_as: exact
  - tool: Lightroom Masking > People > Facial Skin
    parameter: Facial Skin mask Grain
    value: 15
    unit: Lightroom slider
    reported_as: exact
  - tool: Lightroom Masks panel
    parameter: 마스크 Eye 아이콘으로 전후 비교
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Texture와 Clarity 감소로 피부를 부드럽게 하되 Grain을 추가해 실제 피부처럼 보이는 질감을 일부 유지한다.
- 얼굴 특징을 별도 마스크로 두면 피부 보정이 눈썹·눈·입술 보정과 섞이지 않는다.
collection:
  collector_version: 1.0.0
  content_sha256: 44f7af794309f9ac82b5e41eb446e50f7356efe8c88e9ede075c97e74810b522
  collected_at: '2026-08-07T00:00:00Z'
---

# Facial Skin 마스크에서 부드러움과 그레인으로 자연스러운 피부 질감 유지

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

Lightroom의 자동 인물 마스크를 사용할 수 있는 인물 사진에서 피부의 거친 미세 대비를 줄이면서도 과도하게 매끈한 인상을 피하고 싶을 때 사용한다.

## 촬영/작업 순서

1. 편집 모드에서 Masking을 열고 People 분석이 끝날 때까지 기다린다.
2. 대상 인물의 Facial Skin을 선택하고 다른 얼굴 특징과 합치지 않은 독립 마스크를 만든다.
3. Texture와 Clarity를 원문 시작값으로 낮춘 다음 Grain을 추가한다.
4. 개별 전후와 전체 전후를 모두 비교하고 피부가 인공적으로 보이면 보정 강도를 줄인다.

## 추천 시작값 / 조작값

- Lightroom Masking > People > Facial Skin / Facial Skin mask Texture: -20 Lightroom slider
- Lightroom Masking > People > Facial Skin / Facial Skin mask Clarity: -25 Lightroom slider
- Lightroom Masking > People > Facial Skin / Facial Skin mask Grain: 15 Lightroom slider
- Lightroom Masks panel / 마스크 Eye 아이콘으로 전후 비교: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- People에서 인물을 고르고 Facial Skin을 독립 마스크로 생성한다.
- Effects에서 Texture를 -20, Clarity를 -25로 낮춰 피부의 거친 미세 대비를 완화한다.
- Grain을 +15로 올려 사라진 질감 일부를 복원한다.
- 개별 마스크와 전체 마스크의 Eye 아이콘을 번갈아 켜 피부 질감이 자연스러운지 검토한다.

## 주의할 점

- Texture와 Clarity를 낮춘 뒤 Grain을 되돌려도 피부가 플라스틱처럼 보일 수 있으므로 마스크의 Eye 아이콘으로 전후를 확인한다.
- Facial Skin 자동 선택이 머리카락·눈·입술을 침범하지 않았는지 확대해 확인하고 필요하면 선택을 수정한다.

## 확실성과 근거

- Texture와 Clarity 감소로 피부를 부드럽게 하되 Grain을 추가해 실제 피부처럼 보이는 질감을 일부 유지한다.
- 얼굴 특징을 별도 마스크로 두면 피부 보정이 눈썹·눈·입술 보정과 섞이지 않는다.

Adobe 튜토리얼이 Facial Skin 마스크의 Texture -20, Clarity -25, Grain +15를 직접 제시한다. 자연스러움 판단과 선택 경계 점검은 이미지별 관찰이 필요한 적용 해석이다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/ai-portrait-mask-lightroom
- 접근일: 2026-08-07
