---
schema_version: '1.0'
scenario_id: raw-20260806-paintersoft01
title_ko: Clarity 감소와 저불투명 Gaussian Blur로 회화적 부드러움 통합
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/painterly-photo-recipe-actually-works-900080
  published_at: '2026-02-06'
  accessed_at: '2026-08-06T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom and Adobe Photoshop
scenario:
  subject: soft-light-photo
  condition:
  - suitable-soft-light
  - visible-texture
  - detail-to-preserve
  intent:
  - painterly-softness
  - controlled-diffusion
  - preserve-readability
method:
  steps:
  - tool: Adobe Lightroom Clarity
    parameter: 로컬 대비를 낮춰 부드러움을 더하되 장면 구조가 무너지지 않게 줄인다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Photoshop Layer
    parameter: 이미지 레이어를 복제한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Gaussian Blur
    parameter: 복제 레이어에 장면과 피사체 크기에 맞는 절제된 반경으로 적용한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Layer Opacity
    parameter: 블러가 별도 효과로 보이지 않고 원본에 통합될 때까지 복제 레이어 불투명도를 낮춘다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Blend Mode
    parameter: 일반 합성과 다른 빛 번짐이 필요한 경우 Lighten을 시험한다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Lightroom의 Clarity 감소는 로컬 대비를 낮춰 직접적인 부드러움을 만든다.
- 복제 레이어의 Gaussian Blur와 낮은 불투명도는 원본 디테일을 남긴 채 확산 효과를 섞을 수 있다.
- Lighten 혼합 모드는 일반적인 배경 흐림과 다른 렌더링을 실험할 선택지를 제공한다.
collection:
  collector_version: 1.0.0
  content_sha256: ae0695925d9b241abd5be8ed3c2b087658a8b630ce594dd7f0b84370ffe44b4d
  collected_at: '2026-08-06T00:00:00Z'
---

# Clarity 감소와 저불투명 Gaussian Blur로 회화적 부드러움 통합

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

이미 부드러운 빛과 질감을 가진 사진에 필터처럼 노골적이지 않은 회화적 확산감을 더할 때 사용한다.

## 촬영/작업 순서

1. Lightroom에서 Clarity를 정성적으로 낮추며 피사체 구조와 질감을 확인한다.
2. Photoshop으로 옮겨 이미지 레이어를 복제한다.
3. 복제 레이어에 과하지 않은 Gaussian Blur를 적용한다.
4. 복제 레이어 불투명도를 낮춰 블러가 원본과 자연스럽게 섞이게 한다.
5. 필요하면 Lighten blend mode를 비교해 더 적합한 빛 번짐을 선택한다.

## 추천 시작값 / 조작값

- Adobe Lightroom Clarity / 로컬 대비를 낮춰 부드러움을 더하되 장면 구조가 무너지지 않게 줄인다: 원문 정성 표현(수치 추정 없음)
- Adobe Photoshop Layer / 이미지 레이어를 복제한다: 원문 정성 표현(수치 추정 없음)
- Gaussian Blur / 복제 레이어에 장면과 피사체 크기에 맞는 절제된 반경으로 적용한다: 원문 정성 표현(수치 추정 없음)
- Layer Opacity / 블러가 별도 효과로 보이지 않고 원본에 통합될 때까지 복제 레이어 불투명도를 낮춘다: 원문 정성 표현(수치 추정 없음)
- Blend Mode / 일반 합성과 다른 빛 번짐이 필요한 경우 Lighten을 시험한다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 전체 보기에서 분위기를 확인한 뒤 확대 보기에서 눈, 피부, 재질 등 핵심 디테일이 남아 있는지 점검한다.
- Gaussian Blur 반경보다 먼저 불투명도를 낮춰 효과의 존재감이 튀지 않는지 확인한다.
- 근접 피사체에서는 더 보수적으로 적용하고, 레이어를 끄고 켜며 저렴한 필터처럼 보이지 않는지 비교한다.

## 주의할 점

- 원문은 Gaussian Blur를 작은 픽셀 범위에서 쓰라고 설명하지만 정확한 반경 수치는 제시하지 않으므로 임의 숫자를 고정하지 않는다.
- 과도한 Clarity 감소와 블러는 디테일을 뭉개고 사진을 흐물흐물하게 만들 수 있다.
- 특히 클로즈업은 과도한 확산이 인공적이고 값싼 효과처럼 보이기 쉽다.
- 촬영 빛이 맞지 않는 사진을 이 보정만으로 구제하려 하지 않는다.

## 확실성과 근거

- Lightroom의 Clarity 감소는 로컬 대비를 낮춰 직접적인 부드러움을 만든다.
- 복제 레이어의 Gaussian Blur와 낮은 불투명도는 원본 디테일을 남긴 채 확산 효과를 섞을 수 있다.
- Lighten 혼합 모드는 일반적인 배경 흐림과 다른 렌더링을 실험할 선택지를 제공한다.

Fstoppers가 Clarity 감소, 레이어 복제, Gaussian Blur, 불투명도 감소, Lighten 시험 순서를 직접 설명한다. 정확한 Clarity·반경·불투명도 값은 제시되지 않아 모두 정성 단계로 보존했다.

## 출처

- 원문 URL: https://fstoppers.com/education/painterly-photo-recipe-actually-works-900080
- 접근일: 2026-08-06
