---
schema_version: '1.0'
scenario_id: raw-20260803-milkycapture01
title_ko: 은하수와 지상의 노출 범위를 분리해 각각 촬영
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Michael Bonocore; Matt Suess
  url: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
  published_at: '2026-06-24'
  accessed_at: '2026-08-03T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Camera capture workflow
scenario:
  subject: milky-way-landscape
  condition:
  - night-sky
  - high-dynamic-range
  - low-light
  intent:
  - preserve-star-detail
  - separate-sky-foreground
method:
  steps:
  - tool: 카메라
    parameter: 일반적인 은하수 감도 상한
    value: 6400
    unit: ISO
    reported_as: exact
  - tool: 카메라
    parameter: 별의 움직임과 디테일을 우선하는 짧은 셔터·높은 ISO의 하늘 노출
    value: null
    unit: null
    reported_as: qualitative
  - tool: 카메라
    parameter: 하늘과 별도로 수행하는 더 긴 지상 노출
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 하늘과 지상의 밝기 범위가 한 장의 노출을 넘으면 한 프레임을 타협하기보다 목적에 맞는 두 노출을 확보하는 편이 별과 전경을 각각 보존하기 쉽다.
collection:
  collector_version: 1.0.0
  content_sha256: eff6b21ecfddbe6b5d82be55da621e74beec0b96becc8b816b4462c206a1808f
  collected_at: '2026-08-03T00:00:00Z'
---

# 은하수와 지상의 노출 범위를 분리해 각각 촬영

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

은하수와 지상의 밝기 차이가 커서 한 번의 노출로 별 디테일과 전경 정보를 함께 확보하기 어려울 때 사용한다.

## 촬영/작업 순서

1. 은하수 하늘은 별의 선명도를 우선해 짧고 높은 감도의 노출로 촬영한다.
2. 카메라 위치와 구도를 유지한 채 지상은 더 긴 노출로 별도 촬영한다.
3. 후처리에서 하늘과 지상을 각각 최적화한 뒤 경계를 자연스럽게 합성한다.

## 추천 시작값 / 조작값

- 카메라 / 일반적인 은하수 감도 상한: 6400 ISO
- 카메라 / 별의 움직임과 디테일을 우선하는 짧은 셔터·높은 ISO의 하늘 노출: 원문 정성 표현(수치 추정 없음)
- 카메라 / 하늘과 별도로 수행하는 더 긴 지상 노출: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 두 RAW를 독립적으로 처리해 하늘 보정과 지상 보정이 서로 간섭하지 않게 한다.
- 합성 시 산 능선과 지평선 경계를 확대하고 페더링으로 이음새를 완화한다.

## 주의할 점

- 기사의 ISO 12,800 파일은 스트레스 테스트 사례이며 저자가 보통 사용하는 상한은 ISO 6400이라고 구분했다.
- 장면이 한 노출 범위 안에 들어오는 경우까지 무조건 합성할 필요는 없다.
- 합성 경계와 하늘·지상의 밝기 관계가 부자연스럽지 않은지 확인한다.

## 확실성과 근거

- 하늘과 지상의 밝기 범위가 한 장의 노출을 넘으면 한 프레임을 타협하기보다 목적에 맞는 두 노출을 확보하는 편이 별과 전경을 각각 보존하기 쉽다.

ISO 6400 상한과 하늘·지상 분리 촬영 원칙은 출처가 직접 설명했다. 셔터 시간과 조리개는 제시되지 않아 수치로 추정하지 않았다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-03
