---
schema_version: '1.0'
scenario_id: raw-20260806-adjuststack01
title_ko: 조정 레이어의 클리핑을 구분해 합성 전체 밝기를 비파괴 보정
status: validated
source:
  type: official
  publisher: Adobe Photoshop Learn
  author: Dani Beaumont
  url: https://www.adobe.com/learn/photoshop/web/edit-photos-adjustment-layers
  published_at: '2025-12-17'
  accessed_at: '2026-08-06T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Photoshop on the web
scenario:
  subject: layered-photo-composite
  condition:
  - multi-layer-composite
  - uneven-overall-brightness
  intent:
  - nondestructive-tonal-correction
  - preserve-editability
method:
  steps:
  - tool: Photoshop Adjustment Layers
    parameter: 현재 최상단 레이어 위에 Brightness/Contrast 조정 레이어를 추가한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Clip Adjustment Layer
    parameter: 전체 하위 스택을 보정할 때는 클리핑을 끄고, 바로 아래 한 레이어만 보정할 때만 켠다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Brightness/Contrast Properties
    parameter: 이미지를 보며 Brightness를 조절하고 이후 Properties에서 다시 다듬는다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 조정 레이어는 원본 픽셀을 바꾸지 않아 설정을 다시 열고 전후를 비교하거나 여러 보정을 쌓을 수 있다.
- 클리핑 상태를 구분하면 전체 합성을 고치려다 한 요소만 바뀌는 오류를 피할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 5619ab4327fc27692094413049582a9d86e37705e289094c979ab2495087a9a1
  collected_at: '2026-08-06T00:00:00Z'
---

# 조정 레이어의 클리핑을 구분해 합성 전체 밝기를 비파괴 보정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

여러 레이어로 구성한 사진 합성에서 전체 밝기를 바꾸려는데 특정 오브젝트 레이어만 밝아지는 경우에 사용한다.

## 촬영/작업 순서

1. Layers 패널에서 현재 최상단 레이어를 선택한다.
2. Adjustment Layers에서 Brightness/Contrast를 추가한다.
3. 전체 스택 보정이 목적이면 Clip Adjustment Layer가 꺼져 있는지 확인한다.
4. Brightness를 조절한 뒤 조정 레이어를 켜고 끄며 전후를 비교한다.
5. 필요하면 조정 레이어의 Properties를 다시 열어 값을 재조정한다.

## 추천 시작값 / 조작값

- Photoshop Adjustment Layers / 현재 최상단 레이어 위에 Brightness/Contrast 조정 레이어를 추가한다: 원문 정성 표현(수치 추정 없음)
- Clip Adjustment Layer / 전체 하위 스택을 보정할 때는 클리핑을 끄고, 바로 아래 한 레이어만 보정할 때만 켠다: 원문 정성 표현(수치 추정 없음)
- Brightness/Contrast Properties / 이미지를 보며 Brightness를 조절하고 이후 Properties에서 다시 다듬는다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 조정 레이어가 어느 레이어 위에 놓였는지 먼저 확인한다.
- 클리핑을 끈 상태에서 아래 모든 레이어의 밝기가 함께 변하는지 관찰한다.
- 단일 요소만 보정해야 할 때에만 클리핑을 켜고 결과 범위를 다시 확인한다.

## 주의할 점

- 전체 합성 보정에서 클리핑이 켜져 있으면 바로 아래 레이어에만 효과가 적용된다.
- 조정 레이어의 위치가 달라지면 영향을 받는 하위 레이어 범위도 달라질 수 있다.

## 확실성과 근거

- 조정 레이어는 원본 픽셀을 바꾸지 않아 설정을 다시 열고 전후를 비교하거나 여러 보정을 쌓을 수 있다.
- 클리핑 상태를 구분하면 전체 합성을 고치려다 한 요소만 바뀌는 오류를 피할 수 있다.

Adobe 공식 튜토리얼이 조정 레이어 추가, 클리핑 상태에 따른 적용 범위, Properties 재조정을 직접 설명한다. 장면별 Brightness 수치는 제시되지 않아 정성 절차만 기록했다.

## 출처

- 원문 URL: https://www.adobe.com/learn/photoshop/web/edit-photos-adjustment-layers
- 접근일: 2026-08-06
