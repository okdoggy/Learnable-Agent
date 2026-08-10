---
schema_version: '1.0'
scenario_id: raw-20260809-skyground01
title_ko: 은하수 하늘과 어두운 지상을 별도 노출로 촬영해 자연스럽게 합성하기
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Michael Bonocore; method by Matt Suess
  url: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
  published_at: '2026-06-24'
  accessed_at: '2026-08-09T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Camera, Adobe Lightroom, Adobe Photoshop
scenario:
  subject: milky-way-landscape
  condition:
  - dark-foreground
  - night
  - high-dynamic-range
  intent:
  - preserve-stars
  - clean-foreground
  - natural-night-blend
method:
  steps:
  - tool: Camera ISO
    parameter: 평소 은하수 하늘 촬영에서 사용하는 감도 상한
    value: 6400
    unit: ISO
    reported_as: exact
  - tool: Camera ISO
    parameter: 노이즈 감소 시험용 시연 파일의 감도
    value: 12800
    unit: ISO
    reported_as: exact
  - tool: Camera exposure
    parameter: 하늘은 짧은 고감도 노출로 촬영
    value: null
    unit: null
    reported_as: qualitative
  - tool: Camera exposure
    parameter: 매우 어두운 지상은 하늘보다 긴 노출로 별도 촬영
    value: null
    unit: null
    reported_as: qualitative
  - tool: Photoshop Sky Replacement
    parameter: 처리한 하늘과 지상을 합성하고 경계를 부드럽게 페더링
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 희미한 하늘과 어두운 지상은 필요한 노출이 달라 한 프레임에서 타협하기보다 별도 노출이 각 영역의 품질을 지키기 쉽다.
- 지상을 별도의 사진처럼 처리하면 은하수의 별 디테일을 훼손하지 않고 전경의 노이즈와 색 문제를 다룰 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: e1a2085c3a659a81d960a5078416c69076ca299ed809648132b2cd024b0f8865
  collected_at: '2026-08-09T00:00:00Z'
---

# 은하수 하늘과 어두운 지상을 별도 노출로 촬영해 자연스럽게 합성하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

은하수는 보이지만 전경이 매우 어두워 한 번의 노출로 별 디테일과 지상 정보를 동시에 확보하기 어려울 때 사용한다.

## 촬영/작업 순서

1. 현장에서 하늘은 별 흐림을 억제할 수 있는 짧은 고감도 노출로 촬영한다.
2. 카메라를 움직이지 않은 채 지상은 더 긴 노출로 별도 촬영한다.
3. 하늘과 지상을 각각 독립적으로 현상한다.
4. Photoshop에서 처리한 두 노출을 결합하고 능선 경계를 페더링한다.

## 추천 시작값 / 조작값

- Camera ISO / 평소 은하수 하늘 촬영에서 사용하는 감도 상한: 6400 ISO
- Camera ISO / 노이즈 감소 시험용 시연 파일의 감도: 12800 ISO
- Camera exposure / 하늘은 짧은 고감도 노출로 촬영: 원문 정성 표현(수치 추정 없음)
- Camera exposure / 매우 어두운 지상은 하늘보다 긴 노출로 별도 촬영: 원문 정성 표현(수치 추정 없음)
- Photoshop Sky Replacement / 처리한 하늘과 지상을 합성하고 경계를 부드럽게 페더링: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 하늘 프레임은 별과 은하수 구조를 기준으로 별도 현상하고, 지상 프레임은 땅의 질감과 색 번짐을 기준으로 별도 현상한다.
- Photoshop에서 처리한 하늘을 지상 노출에 배치하고 산이나 능선 경계를 부드럽게 페더링한다.
- 100% 보기에서 경계선의 이음새와 후광을 검사하고, 지상 밝기가 은하수보다 두드러지면 낮춘다.

## 주의할 점

- 하늘과 지상 경계의 마스크를 과도하게 단단하게 만들면 산 능선에 이음새나 후광이 생길 수 있다.
- 지상을 지나치게 밝히면 은하수와 시선 경쟁이 생기므로 야간 장면의 어두운 인상을 유지한다.
- ISO 6400은 저자가 평소 사용하는 상한으로 제시한 값이지 모든 카메라에 동일한 최적값은 아니다.

## 확실성과 근거

- 희미한 하늘과 어두운 지상은 필요한 노출이 달라 한 프레임에서 타협하기보다 별도 노출이 각 영역의 품질을 지키기 쉽다.
- 지상을 별도의 사진처럼 처리하면 은하수의 별 디테일을 훼손하지 않고 전경의 노이즈와 색 문제를 다룰 수 있다.

Matt Suess가 하늘은 짧은 고감도 노출, 매우 어두운 지상은 긴 노출로 따로 촬영하고 처리한 뒤 합성한다고 직접 설명했다. ISO 6400의 평소 상한과 시연 파일의 ISO 12,800은 원문에 명시되어 있다. 노출 시간과 조리개 값은 제시되지 않아 추정하지 않았다. 협찬 기사이므로 제품 우수성보다 노출 분리 원칙만 재사용 가능한 근거로 취급한다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-09
