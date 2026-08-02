---
schema_version: '1.0'
scenario_id: raw-20260802-vflatbounce01
title_ko: 움브렐러와 V-flat 이중 반사로 자연스러운 스튜디오광 만들기
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/how-get-natural-looking-studio-light-901630
  published_at: '2026-04-14'
  accessed_at: '2026-08-02T00:00:00Z'
  original_language: en
device:
  capture_device: Sony a7R V
  editing_device: null
  software: Photoshop
scenario:
  subject: studio-portrait
  condition:
  - studio-portrait
  - soft-even-light
  intent:
  - natural-looking-studio-light
  - even-background
method:
  steps:
  - tool: Large umbrella
    parameter: 대형 움브렐러 지름
    value: 6
    unit: ft
    reported_as: exact
  - tool: Umbrella and V-flat
    parameter: 움브렐러를 피사체 대신 흰 V-flat으로 향하게 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Side V-flats
    parameter: 피사체 양옆 V-flat으로 스필과 대비 제어
    value: null
    unit: null
    reported_as: qualitative
  - tool: Camera
    parameter: aperture
    value: 7
    unit: f-number
    reported_as: exact
  - tool: Camera
    parameter: shutter speed
    value: 1/160
    unit: s
    reported_as: exact
rationale_ko:
- 움브렐러의 넓은 빛을 V-flat에 다시 반사하면 창문광 같은 부드럽고 고른 조명이 만들어진다.
- 측면 V-flat은 추가 광원 없이 스필을 통제하고 얼굴 형태를 남긴다.
collection:
  collector_version: 1.0.0
  content_sha256: 417f88225c70bbbe8ac4d276dc0779602091b08744e71bf0fcae7b29b56519cd
  collected_at: '2026-08-02T00:00:00Z'
---

# 움브렐러와 V-flat 이중 반사로 자연스러운 스튜디오광 만들기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

스튜디오 인물 사진에서 그림자는 절제하되 얼굴이 평평해지지 않고, 배경까지 자연스럽게 고른 창문광 같은 조명이 필요할 때 사용한다.

## 촬영/작업 순서

1. 대형 움브렐러를 흰 V-flat 쪽으로 향하게 한다.
2. 반사된 빛이 피사체와 배경을 함께 비추게 배치한다.
3. 피사체 양옆 V-flat으로 스필과 형태를 조절한다.
4. 테스트 촬영으로 얼굴 입체감과 배경 균일도를 확인한다.

## 추천 시작값 / 조작값

- Large umbrella / 대형 움브렐러 지름: 6 ft
- Umbrella and V-flat / 움브렐러를 피사체 대신 흰 V-flat으로 향하게 배치: 원문 정성 표현(수치 추정 없음)
- Side V-flats / 피사체 양옆 V-flat으로 스필과 대비 제어: 원문 정성 표현(수치 추정 없음)
- Camera / aperture: 7 f-number
- Camera / shutter speed: 1/160 s

## 보정 루틴

- 테스트 촬영에서 얼굴 그림자가 부드럽지만 입체감이 남는지 확인한다.
- 배경이 별도 조명 없이도 고르게 이어져 보이는지 점검한다.
- 스필이 과하면 측면 V-flat 위치를 조정한다.

## 주의할 점

- 움브렐러를 피사체에 직접 향하면 의도한 이중 반사 방식과 다른 빛이 된다.
- 측면 V-flat으로 스필을 통제하되 얼굴의 입체감을 없앨 만큼 평평하게 만들지 않는다.
- f/7과 1/160초는 해당 세션의 기록값이며 다른 광량에서 그대로 복사할 고정값이 아니다.

## 확실성과 근거

- 움브렐러의 넓은 빛을 V-flat에 다시 반사하면 창문광 같은 부드럽고 고른 조명이 만들어진다.
- 측면 V-flat은 추가 광원 없이 스필을 통제하고 얼굴 형태를 남긴다.

Fstoppers 기사가 Prince Meyson의 약 6피트 움브렐러와 흰 V-flat 반사 구조, 측면 V-flat, 촬영 설정을 직접 설명한다.

## 출처

- 원문 URL: https://fstoppers.com/education/how-get-natural-looking-studio-light-901630
- 접근일: 2026-08-02
