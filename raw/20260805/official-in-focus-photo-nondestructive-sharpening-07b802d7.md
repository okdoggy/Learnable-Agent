---
schema_version: '1.0'
scenario_id: raw-20260805-smartsharpen01
title_ko: Smart Filter와 Unsharp Mask로 비파괴 선명화
status: validated
source:
  type: official
  publisher: Adobe Photoshop Learn
  author: Jan Kabili
  url: https://www.adobe.com/learn/photoshop/web/sharpen-a-photo
  published_at: '2026-04-13'
  accessed_at: '2026-08-05T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Photoshop
scenario:
  subject: in-focus-photo
  condition:
  - needs-output-sharpening
  intent:
  - nondestructive-sharpening
  - protect-smooth-areas
method:
  steps:
  - tool: Photoshop Zoom
    parameter: evaluation scale
    value: 100
    unit: percent
    reported_as: exact
  - tool: Photoshop Smart Filters
    parameter: 사진 레이어를 Filter > Convert for Smart Filters로 Smart Object로 변환
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Unsharp Mask
    parameter: Amount와 Radius를 일시적으로 과장해 halo를 확인한 뒤 Radius와 Amount를 자연스러운 수준으로 낮춤
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Unsharp Mask
    parameter: Threshold를 낮게 시작하고 저대비 영역 보호가 필요하면 올리되 필요한 디테일 제외 여부 확인
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Smart Filter Mask
    parameter: 하늘, 입자, 매끈한 표면 등 선명화가 불필요한 영역을 마스크로 보호
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Unsharp Mask는 초점이 맞은 디테일의 명암 경계를 강화해 체감 선명도를 높인다.
- Smart Filter로 적용하면 설정을 다시 열어 수정할 수 있어 원본 레이어를 보존한다.
- Threshold보다 마스크를 활용하면 저대비 영역을 보호하면서 필요한 세부를 더 선택적으로 유지할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 07b802d7ad8d84c660a1a48880f28a7476750e720434b2b59acaac85a76292f3
  collected_at: '2026-08-05T00:00:00Z'
---

# Smart Filter와 Unsharp Mask로 비파괴 선명화

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

초점이 맞은 사진의 기존 디테일을 자연스럽게 강조하되, 하늘·입자·매끈한 표면까지 거칠어지지 않도록 비파괴 방식으로 선명화할 때 사용한다.

## 촬영/작업 순서

1. 사진을 100% 확대해 중요한 경계를 기준으로 평가한다.
2. 사진 레이어를 Smart Filters용 Smart Object로 변환한다.
3. Unsharp Mask를 열고 Amount, Radius, Threshold를 조정한다.
4. Preview를 껐다 켜며 원본과 효과를 비교한다.
5. 결과가 자연스러우면 적용하고, 필요 시 Smart Filter를 다시 열어 수정한다.
6. 불필요한 영역은 Smart Filter 마스크로 보호한다.

## 추천 시작값 / 조작값

- Photoshop Zoom / evaluation scale: 100 percent
- Photoshop Smart Filters / 사진 레이어를 Filter > Convert for Smart Filters로 Smart Object로 변환: 원문 정성 표현(수치 추정 없음)
- Photoshop Unsharp Mask / Amount와 Radius를 일시적으로 과장해 halo를 확인한 뒤 Radius와 Amount를 자연스러운 수준으로 낮춤: 원문 정성 표현(수치 추정 없음)
- Photoshop Unsharp Mask / Threshold를 낮게 시작하고 저대비 영역 보호가 필요하면 올리되 필요한 디테일 제외 여부 확인: 원문 정성 표현(수치 추정 없음)
- Photoshop Smart Filter Mask / 하늘, 입자, 매끈한 표면 등 선명화가 불필요한 영역을 마스크로 보호: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Amount와 Radius를 잠시 크게 올려 halo가 형성되는 방식을 확인한 후 Radius와 Amount를 순서대로 낮춘다.
- Threshold를 올렸을 때 필요한 세부까지 빠지는지 검사한다.
- 최종 판단은 100% 배율에서 하고 밝거나 어두운 윤곽이 두드러지지 않는지 확인한다.

## 주의할 점

- 선명화는 흐릿하거나 초점이 벗어난 사진을 복구하지 못한다.
- 100%가 아닌 축소 화면만 보고 판단하지 않는다.
- Radius와 Amount를 과도하게 적용해 밝고 어두운 halo가 눈에 띄지 않게 한다.
- Threshold를 높이면 원치 않는 입자를 보호할 수 있지만 필요한 디테일도 제외될 수 있다.

## 확실성과 근거

- Unsharp Mask는 초점이 맞은 디테일의 명암 경계를 강화해 체감 선명도를 높인다.
- Smart Filter로 적용하면 설정을 다시 열어 수정할 수 있어 원본 레이어를 보존한다.
- Threshold보다 마스크를 활용하면 저대비 영역을 보호하면서 필요한 세부를 더 선택적으로 유지할 수 있다.

Adobe 공식 튜토리얼이 100% 평가, Smart Filter 변환, Unsharp Mask의 Amount·Radius·Threshold 조정, Preview 비교, 마스크 보호를 직접 설명한다. 구체적 Amount·Radius 값은 제시되지 않아 기록하지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/photoshop/web/sharpen-a-photo
- 접근일: 2026-08-05
