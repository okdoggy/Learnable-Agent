---
schema_version: '1.0'
scenario_id: raw-20260802-landscapemask01
title_ko: Landscape 자동 마스크로 등대 풍경의 요소별 시선 정리
status: validated
source:
  type: official
  publisher: Adobe
  author: Glyn Dewis
  url: https://www.adobe.com/learn/lightroom-cc/web/ai-masking-for-landscape-photos
  published_at: '2025-12-18'
  accessed_at: '2026-08-02T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: lighthouse-landscape
  condition:
  - multi-element-landscape
  - uneven-horizon
  intent:
  - selective-landscape-edit
  - emphasize-main-subject
method:
  steps:
  - tool: Profile
    parameter: Adaptive Color로 변경 후 Amount 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Crop > Auto
    parameter: 수평선 자동 보정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Masking > Landscape
    parameter: Sky, Mountains, Architecture, Water를 독립 마스크로 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Sky mask
    parameter: Dehaze와 Clarity 증가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mountains mask
    parameter: Exposure 소폭 감소, Texture 증가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Architecture mask
    parameter: Clarity 증가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Water mask
    parameter: Highlights 소폭 감소, Clarity 증가
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 요소별 마스크는 각 부분을 시각적 역할에 맞게 조절하게 한다.
- 암석을 약간 어둡게 하고 등대 선명도를 높이면 주 피사체로 시선이 모인다.
collection:
  collector_version: 1.0.0
  content_sha256: 4950070829d30b2530d0c14fb2abd489cb46c4e642d1a58d869843623a533c28
  collected_at: '2026-08-02T00:00:00Z'
---

# Landscape 자동 마스크로 등대 풍경의 요소별 시선 정리

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

하늘, 산과 암석, 건축물, 물이 함께 있는 풍경에서 각 요소를 독립적으로 다듬고 주 피사체를 강조한다.

## 촬영/작업 순서

1. 프로필과 수평선을 정리한다.
2. Landscape 분석으로 독립 마스크를 만든다.
3. 요소별 명암과 디테일을 조정하고 전후 비교한다.

## 추천 시작값 / 조작값

- Profile / Adaptive Color로 변경 후 Amount 조정: 원문 정성 표현(수치 추정 없음)
- Crop > Auto / 수평선 자동 보정: 원문 정성 표현(수치 추정 없음)
- Masking > Landscape / Sky, Mountains, Architecture, Water를 독립 마스크로 생성: 원문 정성 표현(수치 추정 없음)
- Sky mask / Dehaze와 Clarity 증가: 원문 정성 표현(수치 추정 없음)
- Mountains mask / Exposure 소폭 감소, Texture 증가: 원문 정성 표현(수치 추정 없음)
- Architecture mask / Clarity 증가: 원문 정성 표현(수치 추정 없음)
- Water mask / Highlights 소폭 감소, Clarity 증가: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 개별 마스크의 Eye 아이콘으로 보정을 확인한다.
- 전체 전후를 비교하고 등대가 충분히 강조되는지 점검한다.

## 주의할 점

- 자동 마스크 오버레이를 확인한다.
- Clarity, Texture, Dehaze를 과도하게 적용하지 않는다.
- Separate Masks를 유지한다.

## 확실성과 근거

- 요소별 마스크는 각 부분을 시각적 역할에 맞게 조절하게 한다.
- 암석을 약간 어둡게 하고 등대 선명도를 높이면 주 피사체로 시선이 모인다.

Adobe 공식 튜토리얼이 요소별 독립 마스크와 보정 방향을 직접 설명한다. 정확한 수치는 없어 정성값으로 기록했다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/ai-masking-for-landscape-photos
- 접근일: 2026-08-02
