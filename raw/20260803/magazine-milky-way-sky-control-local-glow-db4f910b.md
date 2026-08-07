---
schema_version: '1.0'
scenario_id: raw-20260803-milkylocal01
title_ko: 은하수의 광공해와 자연 대기광을 분리 보정
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
  software: Adobe Lightroom; Nik Color Efex
scenario:
  subject: milky-way-sky
  condition:
  - light-pollution
  - airglow
  - localized-cast
  intent:
  - control-local-glow
  - preserve-natural-color
method:
  steps:
  - tool: Adobe Lightroom
    parameter: 밝은 광공해 지역에 Radial Gradient를 두고 Highlights 감소
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe Lightroom
    parameter: 위에서 Linear Gradient를 내려 상단 하늘만 감광
    value: null
    unit: null
    reported_as: qualitative
  - tool: Nik Color Efex
    parameter: ClearView
    value: 12
    unit: approximate slider value
    reported_as: exact
  - tool: Nik Color Efex
    parameter: Color Mask로 원하는 녹색 띠를 샘플링해 해당 색만 조정
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 국소 마스크는 도시 불빛 때문에 밝아진 구역을 전체 하늘과 분리해 억제할 수 있다.
- 실제 녹색·자홍색 대기광까지 전역 보정으로 지우지 않고 해당 색만 보호하거나 다듬을 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: db4f910becd814df970e29bcf07e57e42d0461167dd98591bedee62074623c03
  collected_at: '2026-08-03T00:00:00Z'
---

# 은하수의 광공해와 자연 대기광을 분리 보정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

은하수 사진에 도시 광공해가 국소적으로 번지고 자연스러운 녹색·자홍색 대기광도 남아 있어 전역 보정이 적합하지 않을 때 사용한다.

## 촬영/작업 순서

1. 은하수 중심부의 약간 노랑·자홍 기운을 기준으로 화이트 밸런스를 잡고 녹색 또는 자홍색을 자동 중화하지 않는다.
2. 도시 불빛이 밝은 구역은 Radial Gradient로 선택해 Highlights를 줄인다.
3. 상단 하늘은 Linear Gradient로만 어둡게 해 시선을 은하수 중심과 전경으로 유도한다.
4. Color Mask로 실제 대기광 색을 샘플링해 해당 색만 조정한다.

## 추천 시작값 / 조작값

- Adobe Lightroom / 밝은 광공해 지역에 Radial Gradient를 두고 Highlights 감소: 원문 정성 표현(수치 추정 없음)
- Adobe Lightroom / 위에서 Linear Gradient를 내려 상단 하늘만 감광: 원문 정성 표현(수치 추정 없음)
- Nik Color Efex / ClearView: 12 approximate slider value
- Nik Color Efex / Color Mask로 원하는 녹색 띠를 샘플링해 해당 색만 조정: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- ClearView는 약 +12 부근에서 시작해 구조 회복과 별 외곽선 발생 사이를 비교한다.
- 전역 Saturation 대신 선택 색 보정을 사용하고 100% 확대에서 별과 능선의 링잉을 확인한다.

## 주의할 점

- 녹색과 자홍색이 항상 색편향인 것은 아니며 실제 airglow일 수 있다.
- ClearView와 전역 채도를 과하게 올리면 별에 외곽선이 생기고 대기광이 과장된다.
- 상단 그라디언트로 은하수 중심까지 함께 어둡게 만들지 않는다.

## 확실성과 근거

- 국소 마스크는 도시 불빛 때문에 밝아진 구역을 전체 하늘과 분리해 억제할 수 있다.
- 실제 녹색·자홍색 대기광까지 전역 보정으로 지우지 않고 해당 색만 보호하거나 다듬을 수 있다.

마스크 종류, 보정 방향, ClearView 약 +12, 자연 대기광 보호 원칙은 출처가 직접 제시했다. 다른 슬라이더의 정확한 수치는 제시되지 않았다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-03
