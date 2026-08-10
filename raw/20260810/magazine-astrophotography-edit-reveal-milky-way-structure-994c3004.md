---
schema_version: '1.0'
scenario_id: raw-20260810-mwcolor
title_ko: 은하수 구조와 실제 air glow를 살리는 절제된 국소 현상
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
  software: Adobe Lightroom / Nik Color Efex
scenario:
  subject: astrophotography-edit
  condition:
  - milky-way
  - light-pollution
  - residual-noise
  intent:
  - reveal-milky-way-structure
  - preserve-airglow
  - avoid-halos
method:
  steps:
  - tool: Lightroom Profile
    parameter: 기본 색 렌더링 프로파일
    value: Adobe Landscape
    unit: null
    reported_as: exact
  - tool: Lightroom Basic
    parameter: Dehaze와 Clarity를 적게 적용하고 필요하면 Saturation을 소폭 감소
    value: null
    unit: null
    reported_as: qualitative
  - tool: Local masks
    parameter: 마을 광공해에는 radial gradient로 highlights를 낮추고 상단 하늘에는 linear gradient로 어둡게 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Nik Color Efex ClearView
    parameter: ClearView 시작 강도
    value: 12
    unit: null
    reported_as: exact
  - tool: Nik Color Efex filter stack
    parameter: ClearView, 선택적 Glamour Glow, Remove Color Cast, Tonal Contrast 순으로 필터 구성
    value: ClearView > Glamour Glow > Remove Color Cast > Tonal Contrast
    unit: null
    reported_as: exact
  - tool: Zoom inspection
    parameter: 매 조정 후 before/after를 100% 확대 검사
    value: 100
    unit: percent
    reported_as: exact
rationale_ko:
- 전역 대비와 채도 대신 국소 마스크와 중간톤 중심 조정을 쓰면 실제 air glow와 은하수 핵의 색을 보존하면서 과장을 줄일 수 있다.
- ClearView를 절제하고 100%로 검사하면 별 외곽선과 halo가 생기는 지점을 조기에 발견할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 994c30041ce3556deb526a174c20fac02f5afdeae32e2b6d83213c3210ba66b5
  collected_at: '2026-08-10T00:00:00Z'
---

# 은하수 구조와 실제 air glow를 살리는 절제된 국소 현상

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

노이즈 정리가 끝난 은하수 파일에서 실제 밤하늘의 색과 별 디테일은 유지하면서 은하수 핵과 구조를 드러낼 때 사용한다.

## 촬영/작업 순서

1. Adobe Landscape 프로파일로 시작해 가벼운 대비와 clarity만 적용한다.
2. 은하수 핵이 지나치게 녹색이나 보라색이 되지 않도록 화이트 밸런스를 맞춘다.
3. Dehaze와 Clarity를 적게 사용하고 노이즈 증가를 비교한다.
4. 광공해와 상단 하늘을 국소 gradient로 제어한다.
5. Color Efex 필터를 정해진 순서로 쌓고 ClearView는 약 +12에서 시작한다.
6. air glow는 전역 채도가 아닌 Color Mask로 분리해 조정하고 100% 확대 검사한다.

## 추천 시작값 / 조작값

- Lightroom Profile / 기본 색 렌더링 프로파일: Adobe Landscape
- Lightroom Basic / Dehaze와 Clarity를 적게 적용하고 필요하면 Saturation을 소폭 감소: 원문 정성 표현(수치 추정 없음)
- Local masks / 마을 광공해에는 radial gradient로 highlights를 낮추고 상단 하늘에는 linear gradient로 어둡게 조정: 원문 정성 표현(수치 추정 없음)
- Nik Color Efex ClearView / ClearView 시작 강도: 12
- Nik Color Efex filter stack / ClearView, 선택적 Glamour Glow, Remove Color Cast, Tonal Contrast 순으로 필터 구성: ClearView > Glamour Glow > Remove Color Cast > Tonal Contrast
- Zoom inspection / 매 조정 후 before/after를 100% 확대 검사: 100 percent

## 보정 루틴

- Adobe Landscape에서 깨끗하고 정직한 기본 현상을 만든다.
- 은하수 핵의 화이트 밸런스를 자연스러운 황색·마젠타 사이로 맞추고 Dehaze와 Clarity를 적게 쓴다.
- 광공해와 상단 하늘은 각각 radial·linear gradient로 국소 조정한다.
- Color Efex에서 ClearView, 선택적 Glamour Glow, Remove Color Cast, Tonal Contrast 순으로 쌓는다.
- air glow는 Color Mask로 해당 색만 선택하고 매 단계 100% 전후 비교한다.

## 주의할 점

- Dehaze, Clarity, contrast는 은하수 구조와 함께 노이즈와 별 halo도 키울 수 있다.
- 전역 Saturation으로 air glow를 강화하면 하늘 전체가 네온처럼 과장될 수 있다.
- 작은 미리보기만 보지 말고 매 단계 100% 확대에서 밝은 별과 은하수 핵의 halo를 확인한다.
- 기사에는 DxO 후원이 공개되어 있으므로 제품 효과 주장은 해당 이해관계를 감안해 해석한다.

## 확실성과 근거

- 전역 대비와 채도 대신 국소 마스크와 중간톤 중심 조정을 쓰면 실제 air glow와 은하수 핵의 색을 보존하면서 과장을 줄일 수 있다.
- ClearView를 절제하고 100%로 검사하면 별 외곽선과 halo가 생기는 지점을 조기에 발견할 수 있다.

Matt Suess의 Lightroom 및 Color Efex 순서, ClearView 약 +12, 100% 검사, 국소 마스크 원칙을 기사가 직접 제시한다. 나머지 슬라이더는 정확한 수치 없이 절제해서 적용하라고 설명한다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-10
