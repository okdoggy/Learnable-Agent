---
schema_version: '1.0'
scenario_id: raw-20260808-dodgeburnplan01
title_ko: 전역 Gradient로 효과를 설계한 뒤 Brush 교차로 Dodge·Burn 배치
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
  subject: photo
  condition:
  - flat-light
  - directional-light-needed
  - local-tonal-shaping
  intent:
  - dodge-burn
  - natural-light-shaping
  - controlled-local-edit
method:
  steps:
  - tool: Lightroom Linear Gradient
    parameter: 화면 전체를 덮고 목표 Dodge 또는 Burn 효과가 보이도록 톤 값을 먼저 설정한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Brush
    parameter: 부드러운 Brush를 낮은 Flow로 설정한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Intersect
    parameter: Linear Gradient와 Brush의 겹치는 영역에만 조정을 제한한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Brush
    parameter: Burn은 장면에 이미 존재하는 그림자 영역을 중심으로 칠한다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 톤 변화의 크기를 화면 전체에서 먼저 설계하면 브러시를 칠하면서 슬라이더를 반복 수정하는 시행착오를 줄일 수 있다.
- Gradient와 Brush의 교차는 이미 정한 조정을 칠한 영역에만 드러내므로 빛의 방향과 배치를 분리해 제어하게 한다.
- 기존 그림자를 따라 Burn하면 장면의 원래 조명 논리를 보존해 인공적인 얼룩을 줄인다.
collection:
  collector_version: 1.0.0
  content_sha256: 3371b4d4170f416c9b85312fc6a9c8464e87b8b962bfdd5784d3c2e1a6704835
  collected_at: '2026-08-08T00:00:00Z'
---

# 전역 Gradient로 효과를 설계한 뒤 Brush 교차로 Dodge·Burn 배치

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

Lightroom에서 Dodge·Burn을 할 때 브러시를 칠하면서 슬라이더를 반복 수정하느라 명암 방향과 강도가 흔들리는 사진에 사용한다.

## 촬영/작업 순서

1. 전체 사진을 덮는 Linear Gradient를 만들고 원하는 밝힘 또는 어둡힘 값을 먼저 설정한다.
2. Linear Gradient를 부드러운 저 Flow Brush와 Intersect한다.
3. 효과를 받을 부분만 Brush로 칠해 설계한 톤 변화를 배치한다.
4. Burn은 원래 그림자인 영역을 중심으로 적용해 기존 빛의 논리를 유지한다.

## 추천 시작값 / 조작값

- Lightroom Linear Gradient / 화면 전체를 덮고 목표 Dodge 또는 Burn 효과가 보이도록 톤 값을 먼저 설정한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Brush / 부드러운 Brush를 낮은 Flow로 설정한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Intersect / Linear Gradient와 Brush의 겹치는 영역에만 조정을 제한한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Brush / Burn은 장면에 이미 존재하는 그림자 영역을 중심으로 칠한다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 화면 전체를 덮는 Linear Gradient에 Dodge 또는 Burn용 톤 값을 설정해 효과의 방향과 세기를 먼저 본다.
- Gradient와 부드러운 저 Flow Brush를 Intersect한다.
- Dodge는 기존 광원이 닿을 법한 곳에, Burn은 이미 그림자인 곳을 중심으로 천천히 칠한다.
- 마스크 표시와 전후 비교를 반복해 브러시 자국, 명암의 단절, 광원 방향의 모순을 점검한다.

## 주의할 점

- 브러시로 먼저 칠한 뒤 값을 찾는 방식으로 되돌아가지 말고, 전역 Gradient에서 효과의 크기를 먼저 판단한다.
- Burn은 원래 밝은 면을 무리하게 어둡히기보다 기존 그림자와 광원 방향을 따라야 자연스럽다.
- 낮은 Flow의 부드러운 Brush를 사용하고 반복 누적으로 경계나 얼룩이 생기지 않는지 확인한다.

## 확실성과 근거

- 톤 변화의 크기를 화면 전체에서 먼저 설계하면 브러시를 칠하면서 슬라이더를 반복 수정하는 시행착오를 줄일 수 있다.
- Gradient와 Brush의 교차는 이미 정한 조정을 칠한 영역에만 드러내므로 빛의 방향과 배치를 분리해 제어하게 한다.
- 기존 그림자를 따라 Burn하면 장면의 원래 조명 논리를 보존해 인공적인 얼룩을 줄인다.

Fstoppers가 소개한 Christian Möhrle의 워크플로는 Linear Gradient로 화면 전체에 목표 밝기 변화를 먼저 설정한 뒤, 낮은 Flow의 부드러운 Brush와 Intersect해 필요한 곳에만 적용하라고 직접 설명한다. 정확한 노출량과 Flow 수치는 본문에 없어 정성값으로 보존했다.

## 출처

- 원문 URL: https://fstoppers.com/education/lightrooms-intersect-mask-tool-can-solve-edits-youve-been-doing-hard-way-903413
- 접근일: 2026-08-08
