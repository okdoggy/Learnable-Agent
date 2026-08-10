---
schema_version: '1.0'
scenario_id: raw-20260810-mwdenoise
title_ko: 고ISO 은하수 RAW에서 별을 보존하는 선행 노이즈 제거
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Michael Bonocore / Matt Suess
  url: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
  published_at: '2026-06-24'
  accessed_at: '2026-08-10T00:00:00Z'
  original_language: en
device:
  capture_device: Camera capable of RAW capture
  editing_device: null
  software: DxO PureRAW / Adobe Lightroom
scenario:
  subject: milky-way-raw
  condition:
  - high-iso
  - star-field
  - raw-noise
  intent:
  - reduce-noise
  - preserve-star-detail
  - avoid-oversharpening
method:
  steps:
  - tool: DxO PureRAW Preview and Process
    parameter: 대비·sharpening·창의적 현상 전에 미현상 RAW를 처리
    value: null
    unit: null
    reported_as: qualitative
  - tool: DeepPRIME mode
    parameter: DeepPRIME XD3와 DeepPRIME 3를 사진별로 비교하고 별 보존을 우선해 선택
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lens Sharpness
    parameter: 야간 하늘의 Lens Sharpness 시작값
    value: Standard
    unit: null
    reported_as: exact
  - tool: Zoom inspection
    parameter: 결과를 100% 확대해 별 디테일과 잔여 grain 확인
    value: 100
    unit: percent
    reported_as: exact
rationale_ko:
- 노이즈를 대비와 sharpening 전에 처리하면 증폭된 입자와 싸우지 않고 깨끗한 현상 기반을 만들 수 있다.
- 천체사진에서는 완전한 매끈함보다 별의 미세 구조 보존이 더 중요할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 647be8e83c8ff6465dc53024e0c7967d9718e342f58a209a84f540d30d40c7a8
  collected_at: '2026-08-10T00:00:00Z'
---

# 고ISO 은하수 RAW에서 별을 보존하는 선행 노이즈 제거

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

평평하고 노이즈가 많은 은하수 RAW를 현상할 때, 별의 미세 구조를 뭉개지 않으면서 후속 색·대비 작업용 기반을 만들고자 할 때 사용한다.

## 촬영/작업 순서

1. 창의적 현상 전의 RAW를 DxO PureRAW에서 연다.
2. Preview and Process로 사진별 결과를 비교한다.
3. 강한 XD3가 별을 무디게 하면 덜 공격적인 DeepPRIME 3와 약간의 grain을 선택한다.
4. Lens Sharpness를 Standard로 유지한다.
5. 처리 결과를 Lightroom에서 100%로 검사한 뒤 창의적 현상을 시작한다.

## 추천 시작값 / 조작값

- DxO PureRAW Preview and Process / 대비·sharpening·창의적 현상 전에 미현상 RAW를 처리: 원문 정성 표현(수치 추정 없음)
- DeepPRIME mode / DeepPRIME XD3와 DeepPRIME 3를 사진별로 비교하고 별 보존을 우선해 선택: 원문 정성 표현(수치 추정 없음)
- Lens Sharpness / 야간 하늘의 Lens Sharpness 시작값: Standard
- Zoom inspection / 결과를 100% 확대해 별 디테일과 잔여 grain 확인: 100 percent

## 보정 루틴

- 미현상 RAW를 먼저 PureRAW로 보내 사진별 Preview and Process를 연다.
- DeepPRIME 모드를 비교하고 별이 무뎌지지 않는 덜 공격적인 결과를 선택한다.
- Lens Sharpness는 Standard에서 시작한다.
- 정리된 파일을 Lightroom으로 돌려보낸 뒤에만 대비와 색 작업을 시작한다.
- 100% 확대에서 별의 미세 구조와 남은 grain의 균형을 확인한다.

## 주의할 점

- 창의적 대비나 sharpening을 먼저 적용하면 노이즈가 파일에 강조되어 후속 제거가 어려워질 수 있다.
- 강한 denoise 모드는 섬세한 별을 부드럽게 만들 수 있다.
- Lens Sharpness Hard는 노이즈까지 날카롭게 하고 별을 인공적으로 보이게 할 수 있다.
- 노이즈를 완전히 없애기보다 별 디테일을 위해 약간의 grain을 허용한다.

## 확실성과 근거

- 노이즈를 대비와 sharpening 전에 처리하면 증폭된 입자와 싸우지 않고 깨끗한 현상 기반을 만들 수 있다.
- 천체사진에서는 완전한 매끈함보다 별의 미세 구조 보존이 더 중요할 수 있다.

Matt Suess가 시연한 DxO PureRAW 중심의 별 사진 전처리 절차와 선택 기준을 기사가 직접 전달한다. 특정 사진마다 적합 모드가 다르다고 명시되어 일률적 수치로 일반화하지 않았다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-10
