---
schema_version: '1.0'
scenario_id: raw-20260808-waterintersect01
title_ko: Water 마스크와 Radial Gradient 교차로 작은 폭포만 강조
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; tutorial by Christian Möhrle
  url: https://fstoppers.com/education/lightrooms-intersect-mask-tool-can-solve-edits-youve-been-doing-hard-way-903413
  published_at: '2026-07-09'
  accessed_at: '2026-08-08T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: landscape-water
  condition:
  - landscape-water
  - small-cascades
  - mixed-rock-water
  intent:
  - selective-detail
  - subject-emphasis
  - mask-spill-control
method:
  steps:
  - tool: Lightroom Landscape Mask
    parameter: Landscape 마스크에서 Water를 선택한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Radial Gradient
    parameter: 강조할 폭포·급류 위에 Radial Gradient를 배치한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Intersect
    parameter: Water 마스크와 Radial Gradient의 겹치는 영역만 남긴다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Texture, Clarity, Whites, Saturation
    parameter: 교차 영역의 물 디테일과 밝은 물결을 필요한 만큼 높인다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Landscape의 Water 의미 선택과 Radial Gradient의 공간 제한을 교차하면 주변 바위를 수동 브러시로 정리하지 않고도 작은 물길만 정밀하게 강조할 수 있다.
- 물의 질감·밝기·색을 국소적으로 올리면 주변 암석의 디테일을 과장하지 않으면서 폭포의 시각적 존재감을 높일 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 834eba36fbf375f3cd59cde005fdbaeaac9691234cf25f3e1d0088e5ee19aa23
  collected_at: '2026-08-08T00:00:00Z'
---

# Water 마스크와 Radial Gradient 교차로 작은 폭포만 강조

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

작은 폭포나 급류를 밝고 선명하게 강조하고 싶지만 일반 Radial Gradient가 주변 바위까지 함께 선택하는 풍경 사진에 사용한다.

## 촬영/작업 순서

1. Lightroom에서 Landscape 마스크를 만들고 Water 요소를 선택한다.
2. 강조할 폭포나 급류 위에 Radial Gradient를 놓는다.
3. 두 마스크를 Intersect해 물이면서 Radial Gradient 안에 있는 영역만 남긴다.
4. 교차 영역의 Texture, Clarity, Whites, Saturation을 장면에 맞춰 정성적으로 높인다.

## 추천 시작값 / 조작값

- Lightroom Landscape Mask / Landscape 마스크에서 Water를 선택한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Radial Gradient / 강조할 폭포·급류 위에 Radial Gradient를 배치한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Intersect / Water 마스크와 Radial Gradient의 겹치는 영역만 남긴다: 원문 정성 표현(수치 추정 없음)
- Lightroom Texture, Clarity, Whites, Saturation / 교차 영역의 물 디테일과 밝은 물결을 필요한 만큼 높인다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 마스크 오버레이로 AI가 식별한 Water 영역과 실제 물길이 일치하는지 먼저 점검한다.
- Radial Gradient를 작은 폭포와 급류에 맞춘 뒤 Landscape Water 마스크와 Intersect한다.
- 교차 영역에서 Texture와 Clarity로 물결의 구조를, Whites와 Saturation으로 시인성을 필요한 만큼만 높인다.
- 마스크를 켰다 껐다 하며 주변 바위의 디테일과 색이 변하지 않았는지 확인한다.

## 주의할 점

- Landscape의 Water 선택이 바위나 반사를 잘못 포함하는지 마스크 오버레이로 확인한다.
- Texture·Clarity·Whites·Saturation을 과도하게 올리면 물이 주변 광원과 분리되어 인공적으로 보일 수 있다.
- 이 기법은 물 전체가 아니라 Radial Gradient와 겹치는 폭포·급류 구간에만 적용한다.

## 확실성과 근거

- Landscape의 Water 의미 선택과 Radial Gradient의 공간 제한을 교차하면 주변 바위를 수동 브러시로 정리하지 않고도 작은 물길만 정밀하게 강조할 수 있다.
- 물의 질감·밝기·색을 국소적으로 올리면 주변 암석의 디테일을 과장하지 않으면서 폭포의 시각적 존재감을 높일 수 있다.

Fstoppers가 소개한 Christian Möhrle의 Lightroom 풍경 편집에서 Landscape의 Water 마스크와 Radial Gradient를 교차하고 Texture, Clarity, Whites, Saturation을 높이는 순서를 직접 설명한다. 구체적인 슬라이더 수치는 공개된 본문에 없어 정성 단계로 기록했다.

## 출처

- 원문 URL: https://fstoppers.com/education/lightrooms-intersect-mask-tool-can-solve-edits-youve-been-doing-hard-way-903413
- 접근일: 2026-08-08
