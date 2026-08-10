---
schema_version: '1.0'
scenario_id: raw-20260809-airglowmask
title_ko: 은하수 사진의 광공해와 대기광을 국소 마스크로 분리 보정하기
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
  software: Adobe Lightroom, Nik Color Efex
scenario:
  subject: milky-way-sky
  condition:
  - light-pollution
  - night-sky
  - airglow
  intent:
  - control-local-brightness
  - preserve-natural-color
  - guide-attention
method:
  steps:
  - tool: Radial Gradient
    parameter: 마을 불빛처럼 밝은 광공해 영역을 덮는 타원형 마스크
    value: null
    unit: null
    reported_as: qualitative
  - tool: Highlights
    parameter: 광공해 마스크 내부의 밝은 부분을 낮춤
    value: null
    unit: null
    reported_as: qualitative
  - tool: Linear Gradient
    parameter: 프레임 위쪽에서 내려 상단 하늘을 어둡게 함
    value: null
    unit: null
    reported_as: qualitative
  - tool: Color Mask
    parameter: 녹색 대기광을 샘플링해 해당 색 띠만 분리
    value: null
    unit: null
    reported_as: qualitative
  - tool: Preview zoom
    parameter: 마스크 경계와 별 주변 아티팩트 검사
    value: 100
    unit: percent
    reported_as: exact
rationale_ko:
- 광공해와 대기광은 프레임 일부에만 존재하므로 전역 슬라이더보다 국소 마스크가 정상적인 하늘색과 별 디테일을 더 잘 보존한다.
- 색 범위를 분리하면 실제 녹색·마젠타 대기광을 전체 하늘의 과포화 없이 강화하거나 정리할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 3f65adf1fe828586ab3c5f37187521b86b986de1a0ff9b3d627837b6995250e4
  collected_at: '2026-08-09T00:00:00Z'
---

# 은하수 사진의 광공해와 대기광을 국소 마스크로 분리 보정하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

은하수 사진의 한쪽에 마을 불빛이 밝게 번지거나 녹색·마젠타 대기광이 있어, 전체 밤하늘을 손상하지 않고 해당 영역만 정리할 때 사용한다.

## 촬영/작업 순서

1. 기본 화이트 밸런스를 먼저 정하고 희미한 녹색·마젠타가 실제 대기광일 가능성을 확인한다.
2. 밝은 광공해 위에 Radial Gradient를 배치하고 Highlights를 낮춘다.
3. 필요하면 프레임 위에서 Linear Gradient를 내려 상단을 살짝 어둡게 한다.
4. 대기광의 대표 녹색 또는 마젠타를 Color Mask로 샘플링한다.
5. 분리된 색 띠만 약하게 조정하고 100% 보기에서 경계와 별을 점검한다.

## 추천 시작값 / 조작값

- Radial Gradient / 마을 불빛처럼 밝은 광공해 영역을 덮는 타원형 마스크: 원문 정성 표현(수치 추정 없음)
- Highlights / 광공해 마스크 내부의 밝은 부분을 낮춤: 원문 정성 표현(수치 추정 없음)
- Linear Gradient / 프레임 위쪽에서 내려 상단 하늘을 어둡게 함: 원문 정성 표현(수치 추정 없음)
- Color Mask / 녹색 대기광을 샘플링해 해당 색 띠만 분리: 원문 정성 표현(수치 추정 없음)
- Preview zoom / 마스크 경계와 별 주변 아티팩트 검사: 100 percent

## 보정 루틴

- 마스크 오버레이로 밝은 오염 영역과 대기광 색 띠가 정확히 선택됐는지 확인한다.
- 마을 불빛의 Highlights를 낮춘 뒤 전후 비교로 주변 별과 은하수 중심부가 불필요하게 어두워지지 않았는지 본다.
- 상단 Linear Gradient로 시선을 은하수 중심과 전경 쪽으로 유도하되 그라데이션 경계가 보이지 않게 조정한다.
- 색 마스크에서는 선택한 녹색 또는 마젠타 대기광만 약하게 조정하고 전체 하늘 채도는 유지한다.
- 100% 보기에서 산 경계 후광, 별 주변 링, 색 띠의 전기색 변화를 검사한다.

## 주의할 점

- 전역 Highlights나 Saturation으로 해결하면 정상적인 밤하늘까지 어두워지거나 자연스러운 대기광이 네온색으로 변할 수 있다.
- 자동 하늘 선택은 산 능선 주변에 후광을 남길 수 있으므로 경계를 확대 검사한다.
- Clarity와 Dehaze는 은하수 구조뿐 아니라 노이즈도 함께 강조하므로 국소 마스크 안에서도 절제한다.

## 확실성과 근거

- 광공해와 대기광은 프레임 일부에만 존재하므로 전역 슬라이더보다 국소 마스크가 정상적인 하늘색과 별 디테일을 더 잘 보존한다.
- 색 범위를 분리하면 실제 녹색·마젠타 대기광을 전체 하늘의 과포화 없이 강화하거나 정리할 수 있다.

원문은 마을 불빛에 Radial Gradient를 놓아 Highlights를 낮추고, 위쪽에서 Linear Gradient를 내려 상단 하늘을 어둡게 하며, 대기광은 색 마스크로 분리하라고 직접 설명한다. 구체적인 Highlights·Saturation 수치는 제시되지 않아 모두 정성 단계로 기록했다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/
- 접근일: 2026-08-09
