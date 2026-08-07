---
schema_version: '1.0'
scenario_id: raw-20260805-spotheal01
title_ko: 빈 보정 레이어의 Spot Healing으로 작은 결함 제거
status: validated
source:
  type: official
  publisher: Adobe Photoshop Learn
  author: Dani Beaumont; Seán Duggan; Gabriela Iancu
  url: https://www.adobe.com/learn/photoshop/web/remove-objects-from-your-photos
  published_at: '2025-12-17'
  accessed_at: '2026-08-05T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Photoshop on the web
scenario:
  subject: photo-small-imperfection
  condition:
  - small-spot
  - dust-or-blemish
  intent:
  - nondestructive-retouch
  - remove-small-distraction
method:
  steps:
  - tool: Photoshop Layer
    parameter: 빈 Retouching 레이어를 만들어 원본과 보정을 분리
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Spot Healing Brush
    parameter: Sample all layers를 켜 아래 사진에서 샘플하고 빈 레이어에만 결과 적용
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Spot Healing Brush Size
    parameter: 브러시를 결함보다 약간 크게 설정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Spot Healing Brush
    parameter: 작은 점은 한 번 클릭하고 불규칙한 자국은 경계를 따라 드래그
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Spot Healing Brush는 주변 디테일을 자동으로 골라 질감, 톤, 색을 섞으므로 먼지·여드름·작은 긁힘을 빠르게 정리할 수 있다.
- 빈 레이어에 보정하면 파일을 다시 열어도 수정하거나 폐기하기 쉽다.
collection:
  collector_version: 1.0.0
  content_sha256: d7776effae1e298b61d190f0e83e019007b243c45d67e93607a119b0dc808bc9
  collected_at: '2026-08-05T00:00:00Z'
---

# 빈 보정 레이어의 Spot Healing으로 작은 결함 제거

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

사진의 먼지, 여드름, 작은 긁힘이나 가느다란 자국을 원본 픽셀을 직접 바꾸지 않고 빠르게 지울 때 사용한다.

## 촬영/작업 순서

1. 사진 위에 빈 레이어를 만들고 Retouching으로 이름을 지정한다.
2. Spot Healing Brush에서 Sample all layers를 활성화한다.
3. 브러시를 결함보다 약간 크게 맞춘다.
4. 작은 점은 클릭하고 길거나 불규칙한 자국은 그 위를 따라 짧게 칠한다.
5. 보정 레이어를 전환해 주변 질감과 자연스럽게 섞였는지 확인한다.

## 추천 시작값 / 조작값

- Photoshop Layer / 빈 Retouching 레이어를 만들어 원본과 보정을 분리: 원문 정성 표현(수치 추정 없음)
- Photoshop Spot Healing Brush / Sample all layers를 켜 아래 사진에서 샘플하고 빈 레이어에만 결과 적용: 원문 정성 표현(수치 추정 없음)
- Photoshop Spot Healing Brush Size / 브러시를 결함보다 약간 크게 설정: 원문 정성 표현(수치 추정 없음)
- Photoshop Spot Healing Brush / 작은 점은 한 번 클릭하고 불규칙한 자국은 경계를 따라 드래그: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 보정 레이어를 껐다 켜 원본과 비교한다.
- 주변 질감·톤·색이 자연스럽게 이어지는지 100%에 가까운 확대에서 확인한다.
- 결과가 어색하면 보정 레이어에서 해당 부분만 지우고 더 작은 브러시로 다시 처리한다.

## 주의할 점

- 결함보다 지나치게 큰 브러시는 주변의 유효한 질감까지 바꿀 수 있다.
- 불규칙한 결함을 한 번에 넓게 칠하기보다 주변 경계를 보며 짧게 처리한다.
- 원본 레이어에 직접 보정하지 않는다.

## 확실성과 근거

- Spot Healing Brush는 주변 디테일을 자동으로 골라 질감, 톤, 색을 섞으므로 먼지·여드름·작은 긁힘을 빠르게 정리할 수 있다.
- 빈 레이어에 보정하면 파일을 다시 열어도 수정하거나 폐기하기 쉽다.

Adobe 공식 튜토리얼이 빈 레이어, Sample all layers, 결함보다 약간 큰 브러시, 작은 점 클릭과 불규칙 결함 드래그를 직접 설명한다. 브러시 크기의 정확한 수치는 제시되지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/photoshop/web/remove-objects-from-your-photos
- 접근일: 2026-08-05
