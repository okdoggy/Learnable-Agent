---
schema_version: '1.0'
scenario_id: raw-20260803-milkydenoise01
title_ko: 은하수 RAW를 현상 전에 절제해 노이즈 제거
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
  software: DxO PureRAW; Adobe Lightroom
scenario:
  subject: milky-way-raw
  condition:
  - high-iso-noise
  - star-field
  intent:
  - reduce-noise
  - preserve-star-detail
method:
  steps:
  - tool: DxO PureRAW
    parameter: 대비·선명도·샤프닝 전 untouched RAW 선처리
    value: null
    unit: null
    reported_as: qualitative
  - tool: DxO PureRAW
    parameter: 별 보존을 위해 DeepPRIME XD3보다 덜 공격적인 DeepPRIME 3 우선 비교
    value: null
    unit: null
    reported_as: qualitative
  - tool: DxO PureRAW
    parameter: Lens Sharpness
    value: Standard
    unit: null
    reported_as: exact
  - tool: Adobe Lightroom
    parameter: 검사 배율
    value: 100
    unit: percent
    reported_as: exact
rationale_ko:
- 대비나 샤프닝을 먼저 적용하면 노이즈가 두드러지고 거친 질감이 고착될 수 있으므로 RAW 정리부터 수행한다.
- 별밭에서는 최대 강도의 노이즈 제거보다 미세한 별 보존을 우선한다.
collection:
  collector_version: 1.0.0
  content_sha256: 3c254cd3d2396b85c1ea59585e67ee568c1bbf1839aab1e2d452b74e9c39df8e
  collected_at: '2026-08-03T00:00:00Z'
---

# 은하수 RAW를 현상 전에 절제해 노이즈 제거

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

고감도 은하수 RAW가 거칠지만 강한 노이즈 제거로 작은 별까지 사라질 위험이 있을 때 사용한다.

## 촬영/작업 순서

1. 현상과 창의적 보정을 시작하기 전에 원본 RAW를 PureRAW로 연다.
2. DeepPRIME 3과 XD3를 이미지별로 비교하되 별 보존에 유리한 덜 공격적인 처리를 우선한다.
3. Lens Sharpness는 Standard에서 시작한다.
4. Lightroom에서 100%로 확대해 작은 별, 밝은 별 테두리, 산 능선을 확인한다.

## 추천 시작값 / 조작값

- DxO PureRAW / 대비·선명도·샤프닝 전 untouched RAW 선처리: 원문 정성 표현(수치 추정 없음)
- DxO PureRAW / 별 보존을 위해 DeepPRIME XD3보다 덜 공격적인 DeepPRIME 3 우선 비교: 원문 정성 표현(수치 추정 없음)
- DxO PureRAW / Lens Sharpness: Standard
- Adobe Lightroom / 검사 배율: 100 percent

## 보정 루틴

- 노이즈 감소 전후를 비교해 별 개수가 줄거나 별이 번진 듯 보이면 강도를 낮춘다.
- 후속 Clarity·Dehaze·대비에서 노이즈가 다시 나타나는지 단계별로 확인한다.

## 주의할 점

- Hard 샤프닝은 노이즈를 날카롭게 하고 별을 인공적으로 보이게 할 수 있다.
- 노이즈를 완전히 없애려다 미세한 별 디테일을 잃지 않는다.
- 작은 미리보기만으로 판단하면 링잉과 별 손상을 놓칠 수 있다.

## 확실성과 근거

- 대비나 샤프닝을 먼저 적용하면 노이즈가 두드러지고 거친 질감이 고착될 수 있으므로 RAW 정리부터 수행한다.
- 별밭에서는 최대 강도의 노이즈 제거보다 미세한 별 보존을 우선한다.

처리 순서, DeepPRIME 3 선호 이유, Lens Sharpness Standard, 100% 검사는 출처가 직접 설명했다. 이미지별 최종 강도는 고정값으로 제시되지 않았다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-03
