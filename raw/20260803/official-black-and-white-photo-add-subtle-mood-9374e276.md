---
schema_version: '1.0'
scenario_id: raw-20260803-monotint01
title_ko: 흑백 사진에 절제된 단일 Global tint 더하기
status: validated
source:
  type: official
  publisher: Adobe
  author: Kenneth Hines Jr.
  url: https://www.adobe.com/learn/lightroom-cc/web/adjust-photo-tone-with-color-grading
  published_at: '2025-12-18'
  accessed_at: '2026-08-03T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: black-and-white-photo
  condition:
  - monochrome
  - creative-tint
  intent:
  - add-subtle-mood
  - retain-monochrome-reading
method:
  steps:
  - tool: Adobe Lightroom Color Grading
    parameter: Reset 3-Way로 Shadows, Midtones, Highlights 조정을 비움
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom Color Grading
    parameter: Global에서 원하는 단일 Hue 선택
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom Color Grading
    parameter: 흑백으로 읽히는 범위의 낮은 Global Saturation
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 흑백 이미지는 미세한 tint의 배치를 관찰하기 쉽고 Global은 전체 이미지에 하나의 분위기 색을 일관되게 얹을 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 9374e276f52089965206402c67ff6401f043041f279c9a8350d15899cea8b13e
  collected_at: '2026-08-03T00:00:00Z'
---

# 흑백 사진에 절제된 단일 Global tint 더하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

흑백 사진의 명암 구조는 유지하면서 화면 전체에 매우 약한 색조로 분위기를 더하고 싶을 때 사용한다.

## 촬영/작업 순서

1. 기존 3-Way 색보정이 있으면 Reset 3-Way로 제거해 Global 효과를 분리한다.
2. Global에서 원하는 Hue를 선택한다.
3. Saturation을 낮게 올리며 사진이 여전히 흑백으로 인식되는지 확인한다.
4. 전후 비교로 단일 tint가 명암과 주제를 방해하지 않는지 점검한다.

## 추천 시작값 / 조작값

- Adobe Lightroom Color Grading / Reset 3-Way로 Shadows, Midtones, Highlights 조정을 비움: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom Color Grading / Global에서 원하는 단일 Hue 선택: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom Color Grading / 흑백으로 읽히는 범위의 낮은 Global Saturation: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Hue를 바꿔 분위기를 비교하되 Saturation은 작은 변화로 유지한다.
- 필요하면 Global Luminance로 tint가 명암 인상을 바꾸는 정도를 살핀다.

## 주의할 점

- 채도가 높아져 흑백 사진보다 단색 컬러 사진처럼 보이지 않게 한다.
- 3-Way 조정과 Global 조정이 겹친 상태에서 효과의 원인을 혼동하지 않는다.

## 확실성과 근거

- 흑백 이미지는 미세한 tint의 배치를 관찰하기 쉽고 Global은 전체 이미지에 하나의 분위기 색을 일관되게 얹을 수 있다.

Reset 3-Way, Global green tint, 낮은 채도로 흑백 인상을 유지하는 절차는 Adobe 튜토리얼이 직접 시연했다. 정확한 채도 수치는 제시되지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/adjust-photo-tone-with-color-grading
- 접근일: 2026-08-03
