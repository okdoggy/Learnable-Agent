---
schema_version: '1.0'
scenario_id: raw-20260810-warmwin
title_ko: 황혼 건축 사진의 창문에 따뜻한 실내광 만들기
status: validated
source:
  type: official
  publisher: Adobe
  author: Adobe
  url: https://www.adobe.com/learn/lightroom-cc/web/correct-white-balance
  published_at: '2026-06-11'
  accessed_at: '2026-08-10T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: architecture
  condition:
  - dusk
  - cool-ambient-light
  - dark-windows
  intent:
  - simulate-warm-window-light
  - preserve-cool-surroundings
method:
  steps:
  - tool: Brush mask
    parameter: 창문 크기에 맞춘 Brush로 밝힐 영역을 칠하고 O 키로 빨간 마스크 오버레이를 확인
    value: null
    unit: null
    reported_as: qualitative
  - tool: Local white balance
    parameter: 선택된 창문을 따뜻한 화이트 밸런스로 이동하도록 Temp와 Tint를 증가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Local exposure
    parameter: 실내에서 빛이 나는 것처럼 보이도록 선택 영역의 Exposure를 증가
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 차가운 황혼 외부와 따뜻한 창문 빛의 색 대비를 만들면 건물 내부 조명이 켜진 듯한 효과를 낼 수 있다.
- 국소 마스크를 사용하면 외부의 차가운 색조를 보존할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 73d6f454260f25d58bbd4c7ab0b75413e77332d5110deaf49d47aed607617cde
  collected_at: '2026-08-10T00:00:00Z'
---

# 황혼 건축 사진의 창문에 따뜻한 실내광 만들기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

차가운 황혼에 촬영한 건축 사진에서 어두운 창문만 따뜻하고 밝게 만들어 실내 조명이 켜진 듯 보이게 할 때 사용한다.

## 촬영/작업 순서

1. 차가운 저녁빛이 남아 있는 건축 사진을 연다.
2. Brush 크기를 창문에 맞추고 창문 내부만 칠한다.
3. O 키로 마스크 오버레이를 켜고 선택 범위를 검사한다.
4. 마스크 안에서 Temp와 Tint를 올려 따뜻하게 만든 뒤 Exposure를 올린다.
5. 같은 효과가 필요한 다른 창을 칠하거나, 다른 세기가 필요하면 새 Brush 조정을 만든다.

## 추천 시작값 / 조작값

- Brush mask / 창문 크기에 맞춘 Brush로 밝힐 영역을 칠하고 O 키로 빨간 마스크 오버레이를 확인: 원문 정성 표현(수치 추정 없음)
- Local white balance / 선택된 창문을 따뜻한 화이트 밸런스로 이동하도록 Temp와 Tint를 증가: 원문 정성 표현(수치 추정 없음)
- Local exposure / 실내에서 빛이 나는 것처럼 보이도록 선택 영역의 Exposure를 증가: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 차가운 황혼 배경은 유지하고 창문 영역만 국소적으로 따뜻하고 밝게 만든다.
- 마스크 오버레이를 켜서 창틀과 벽에 보정이 새지 않았는지 확인한다.
- 다른 창에는 같은 설정을 재사용하되, 밝기나 색이 달라야 하면 별도 Brush 조정을 만든다.

## 주의할 점

- 마스크가 창문 밖 벽이나 하늘로 번지면 인공적인 색 번짐이 생기므로 빨간 오버레이로 경계를 확인한다.
- Adobe Stock 연습 파일을 다른 용도로 사용할 때는 별도 라이선스 조건을 확인한다.

## 확실성과 근거

- 차가운 황혼 외부와 따뜻한 창문 빛의 색 대비를 만들면 건물 내부 조명이 켜진 듯한 효과를 낼 수 있다.
- 국소 마스크를 사용하면 외부의 차가운 색조를 보존할 수 있다.

Adobe 공식 튜토리얼이 Brush 마스크, Temp·Tint, Exposure의 적용 순서와 목적을 직접 설명한다. 구체적인 슬라이더 수치는 제시되지 않아 모두 정성 단계로 보존했다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/correct-white-balance
- 접근일: 2026-08-10
