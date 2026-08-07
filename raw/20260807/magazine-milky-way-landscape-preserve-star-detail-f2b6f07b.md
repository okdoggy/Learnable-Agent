---
schema_version: '1.0'
scenario_id: raw-20260807-milkyway01
title_ko: 평평하고 노이즈 많은 Milky Way RAW를 별 디테일을 보존해 완성하기
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Michael Bonocore; workflow by Matt Suess
  url: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
  published_at: '2026-06-24'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: DxO PureRAW; Adobe Lightroom; Nik Color Efex; Adobe Photoshop
scenario:
  subject: milky-way-landscape
  condition:
  - flat-noisy-raw
  - high-dynamic-range-night-scene
  - light-pollution-glow
  intent:
  - preserve-star-detail
  - recover-milky-way-structure
  - blend-sky-and-foreground-naturally
method:
  steps:
  - tool: Camera ISO
    parameter: 일반적인 Milky Way 하늘 노출의 ISO 상한
    value: 6400
    unit: ISO
    reported_as: exact
  - tool: Camera ISO
    parameter: 노이즈 제거 시험용 시연 파일의 ISO
    value: 12800
    unit: ISO
    reported_as: exact
  - tool: DxO PureRAW
    parameter: 현상 전 untouched RAW를 Preview and Process로 확인하고 별 보존을 우선해 DeepPRIME 3와 Standard Lens Sharpness
      사용
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom Develop
    parameter: Adobe Landscape를 기초로 modest Contrast와 Clarity, 약한 Dehaze를 적용
    value: null
    unit: null
    reported_as: qualitative
  - tool: Nik Color Efex ClearView
    parameter: ClearView의 통상 시작 강도
    value: 12
    unit: slider
    reported_as: exact
  - tool: Nik Color Efex
    parameter: ClearView, 소량의 Glamour Glow, Remove Color Cast, Tonal Contrast 순서로 필터 스택 구성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Zoom inspection
    parameter: 모든 조정을 100% 확대에서 전후 비교
    value: 100
    unit: percent
    reported_as: exact
  - tool: Adobe Photoshop Sky Replacement
    parameter: 하늘과 전경을 별도로 보정한 뒤 Photoshop Sky Replacement로 결합하고 능선 경계를 feather
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 노이즈가 있는 RAW를 대비·선명도보다 먼저 정리하면 현상 과정에서 입자가 강화되는 것을 줄일 수 있다.
- 별 디테일을 보존하기 위해 가장 강한 노이즈 제거보다 덜 공격적인 모드를 선택하고 약간의 입자를 허용한다.
- 하늘과 땅의 노출 범위가 한 장에 담기 어려우면 각각 적정 노출한 두 프레임이 한 장의 타협된 노출보다 낫다.
- 국부 그라디언트와 선택 색 보정은 실제 air glow와 Milky Way core를 보존하면서 도시광과 과도한 전역 채도를 억제한다.
collection:
  collector_version: 1.0.0
  content_sha256: f2b6f07bd2860b2ccb9a66514b689a4dcc54fbbc1632404f0b1dc754a0a81bb0
  collected_at: '2026-08-07T00:00:00Z'
---

# 평평하고 노이즈 많은 Milky Way RAW를 별 디테일을 보존해 완성하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

Milky Way와 어두운 전경의 밝기 차이가 크고 고감도 RAW에 노이즈가 많지만 별의 크기와 실제 air glow를 보존해야 하는 야경에 사용한다.

## 촬영/작업 순서

1. 한 프레임의 유효 범위를 넘는 장면은 짧고 고감도인 하늘 노출과 더 긴 전경 노출로 나눠 촬영하며 전경은 Milky Way와 경쟁하지 않도록 다소 어둡게 유지한다.
2. 샤프닝이나 대비를 넣기 전에 untouched RAW를 PureRAW에서 미리 보고 처리하며 별 보존을 우선한다.
3. Lightroom에서 Adobe Landscape를 기초로 화이트 밸런스를 Milky Way core의 약간 노랑-마젠타 느낌에 맞추고 Contrast, Clarity, Dehaze를 절제해 적용한다.
4. 도시광에는 radial gradient로 Highlights를 낮추고 위쪽 하늘에는 위에서 아래로 linear gradient를 내려 시선을 core 쪽으로 유도한다.
5. Color Efex에서 ClearView, 아주 적은 Glamour Glow, Remove Color Cast, Tonal Contrast 순으로 쌓고 모든 변화를 100%에서 확인한다.
6. air glow는 전역 Saturation 대신 Color Mask로 샘플링해 선택적으로 조정한다.
7. 전경은 하늘을 무시하고 별도 사진처럼 보정하며 Natural Ground와 AI Object Selection으로 색과 디테일을 국부 조정한다.
8. 완성한 하늘과 전경을 Photoshop에서 결합하고 산 또는 능선 경계를 자연스럽게 feather한다.

## 추천 시작값 / 조작값

- Camera ISO / 일반적인 Milky Way 하늘 노출의 ISO 상한: 6400 ISO
- Camera ISO / 노이즈 제거 시험용 시연 파일의 ISO: 12800 ISO
- DxO PureRAW / 현상 전 untouched RAW를 Preview and Process로 확인하고 별 보존을 우선해 DeepPRIME 3와 Standard Lens Sharpness 사용: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom Develop / Adobe Landscape를 기초로 modest Contrast와 Clarity, 약한 Dehaze를 적용: 원문 정성 표현(수치 추정 없음)
- Nik Color Efex ClearView / ClearView의 통상 시작 강도: 12 slider
- Nik Color Efex / ClearView, 소량의 Glamour Glow, Remove Color Cast, Tonal Contrast 순서로 필터 스택 구성: 원문 정성 표현(수치 추정 없음)
- Zoom inspection / 모든 조정을 100% 확대에서 전후 비교: 100 percent
- Adobe Photoshop Sky Replacement / 하늘과 전경을 별도로 보정한 뒤 Photoshop Sky Replacement로 결합하고 능선 경계를 feather: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- ClearView는 +12 부근을 출발점으로 삼되 별 주변 윤곽이 생기기 전에 낮춘다.
- Glamour Glow는 잔여 노이즈와 별의 딱딱함을 아주 약하게 줄이는 용도로만 사용한다.
- Tonal Contrast는 Milky Way 구조가 많은 중간톤을 중심으로 조절하고 밝은 별과 고대비 경계의 링을 100%에서 검사한다.
- 각 조정이 되살리는 구조보다 노이즈를 더 많이 드러내기 시작하면 강도를 되돌린다.
- 성공한 필터 순서는 preset으로 저장해 반복성을 확보한다.

## 주의할 점

- 기사에는 DxO 협찬 사실이 명시되어 있으므로 제품 선택의 독립성에 한계가 있다.
- 가장 강한 DeepPRIME XD3는 심한 노이즈를 매끈하게 만들 수 있지만 별을 부드럽게 만들 위험이 있다.
- Hard Lens Sharpness와 초기 RAW sharpening은 노이즈와 별을 과장해 별을 부푼 점처럼 만들 수 있다.
- 과도한 Clarity, Contrast, Dehaze는 노이즈와 별 주변 링을 되살린다.
- 전역 Saturation은 실제 녹색·마젠타 air glow를 네온색처럼 만들 수 있다.
- 자동 하늘 선택과 합성 경계는 산 능선에 halo나 이음새를 남길 수 있다.

## 확실성과 근거

- 노이즈가 있는 RAW를 대비·선명도보다 먼저 정리하면 현상 과정에서 입자가 강화되는 것을 줄일 수 있다.
- 별 디테일을 보존하기 위해 가장 강한 노이즈 제거보다 덜 공격적인 모드를 선택하고 약간의 입자를 허용한다.
- 하늘과 땅의 노출 범위가 한 장에 담기 어려우면 각각 적정 노출한 두 프레임이 한 장의 타협된 노출보다 낫다.
- 국부 그라디언트와 선택 색 보정은 실제 air glow와 Milky Way core를 보존하면서 도시광과 과도한 전역 채도를 억제한다.

PetaPixel 기사는 Matt Suess의 촬영·편집 순서와 ISO 6400 상한, 시연 ISO 12,800, ClearView 약 +12, 100% 검사 값을 직접 제시한다. 다만 협찬 기사이며 장면별 노출 시간과 다른 슬라이더 수치는 제공하지 않아 추정하지 않았다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-07
