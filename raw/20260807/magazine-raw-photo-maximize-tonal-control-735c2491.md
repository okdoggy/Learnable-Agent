---
schema_version: '1.0'
scenario_id: raw-20260807-linearprofile01
title_ko: Linear Camera Profile로 최종 감마와 톤 응답을 직접 설계하기
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Vlad Moldovean
  url: https://petapixel.com/2026/06/14/how-to-leverage-linear-camera-profiles-in-your-editing-workflow/
  published_at: '2026-06-14'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom; Adobe DNG Profile Editor
scenario:
  subject: raw-photo
  condition:
  - difficult-highlight-rolloff
  - strong-tonal-shaping
  - filmic-rendering
  intent:
  - maximize-tonal-control
  - preserve-color-separation
  - customize-gamma-response
method:
  steps:
  - tool: Adobe DNG Profile Editor
    parameter: 해당 카메라 RAW를 DNG로 내보내고 DNG Profile Editor의 Tone Curve를 linear로 설정해 프로필 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: White Balance
    parameter: 강한 색 편향이 있으면 Linear Camera Profile 적용 전에 White Balance 설정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Basic tonal controls
    parameter: Linear Camera Profile 적용 후 Exposure, Blacks, Whites로 클리핑 없이 히스토그램을 균형 있게 배치
    value: null
    unit: null
    reported_as: qualitative
  - tool: Masking > Luminance Range > Tone Curve
    parameter: 전체 범위를 포함하는 Luminance Range의 Select All mask 안에서 맞춤 gamma tone curve 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask stack
    parameter: 색 보정 후 최종 gamma mask가 마스크 스택 상단에서 마지막에 적용되도록 새 Select All mask에 곡선을 복사
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Linear Camera Profile은 센서의 기존 데이터를 더 평평하게 렌더링해 최종 감마와 대비를 편집자가 직접 설계하게 한다.
- 최종 S-curve 아래에서 색과 국부광을 다루면 깊은 그림자와 밝은 하이라이트의 과도한 채도를 줄이고 중간톤에 자연스럽게 활기를 모을 수 있다.
- 이 방식은 동적 범위를 늘리는 것이 아니라 기존 데이터의 톤 응답 제어를 바꾸는 것이다.
collection:
  collector_version: 1.0.0
  content_sha256: 735c2491dbbec94d9a7f62cb76440d331f9f2b2a561d7488ea97b627787f88b9
  collected_at: '2026-08-07T00:00:00Z'
---

# Linear Camera Profile로 최종 감마와 톤 응답을 직접 설계하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

표준 카메라 프로필보다 하이라이트 롤오프, 색 분리와 강한 S-curve의 질감을 세밀하게 제어해야 하는 RAW 사진에 사용한다.

## 촬영/작업 순서

1. 정기적으로 쓰는 카메라의 RAW를 DNG로 내보내 Linear Camera Profile을 만든 뒤 Lightroom에 가져온다.
2. 국부 노출 문제를 먼저 파악하고 강한 색 편향이 있으면 화이트 밸런스를 설정한다.
3. Linear Camera Profile로 전환한 뒤 Exposure, Blacks, Whites를 이용해 히스토그램을 중앙에 가깝게 균형 잡고 양 끝의 클리핑을 피한다.
4. 필요할 때 Shadows와 Highlights로 세부를 회복하되 인공적인 HDR 인상이 생기기 전에 멈춘다.
5. 전체 이미지를 포함하는 Luminance Range 마스크 안에서 의도에 맞는 gamma curve를 만든다.
6. Color Response Curves, 화이트 밸런스, 컬러 휠과 HSL로 룩을 만든 후 국부 마스크를 추가한다.
7. 마스크가 많아졌다면 gamma curve를 새 Select All mask로 옮겨 최종 단계에서 적용되게 한다.

## 추천 시작값 / 조작값

- Adobe DNG Profile Editor / 해당 카메라 RAW를 DNG로 내보내고 DNG Profile Editor의 Tone Curve를 linear로 설정해 프로필 생성: 원문 정성 표현(수치 추정 없음)
- White Balance / 강한 색 편향이 있으면 Linear Camera Profile 적용 전에 White Balance 설정: 원문 정성 표현(수치 추정 없음)
- Basic tonal controls / Linear Camera Profile 적용 후 Exposure, Blacks, Whites로 클리핑 없이 히스토그램을 균형 있게 배치: 원문 정성 표현(수치 추정 없음)
- Masking > Luminance Range > Tone Curve / 전체 범위를 포함하는 Luminance Range의 Select All mask 안에서 맞춤 gamma tone curve 생성: 원문 정성 표현(수치 추정 없음)
- Mask stack / 색 보정 후 최종 gamma mask가 마스크 스택 상단에서 마지막에 적용되도록 새 Select All mask에 곡선을 복사: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 프로필 적용 직후 회색이고 어두워 보이는 상태를 실패로 판단하지 말고 히스토그램과 클리핑을 기준으로 기초 톤을 만든다.
- 최종 감마 아래에서 색 그라데이션과 국부광을 다듬고, 필요하면 곡선을 새 최상단 마스크에 복사해 처리 순서를 정리한다.
- 표준 프로필 결과와 비교해 추가 시간과 복잡성이 실제 품질 향상으로 이어지는 사진에만 유지한다.

## 주의할 점

- Linear Camera Profile은 카메라의 동적 범위를 늘리지 않는다.
- Shadows와 Highlights를 과도하게 밀면 인공적인 HDR 인상이 생길 수 있다.
- Lightroom은 마스크를 드래그해 재정렬할 수 없어 복잡한 스택의 처리 순서를 주의해야 한다.
- 일반 사진에는 표준 프로필이 더 빠르고 충분할 수 있다.
- 원문에 슬라이더 수치가 없으므로 정성적 시작점만 기록한다.

## 확실성과 근거

- Linear Camera Profile은 센서의 기존 데이터를 더 평평하게 렌더링해 최종 감마와 대비를 편집자가 직접 설계하게 한다.
- 최종 S-curve 아래에서 색과 국부광을 다루면 깊은 그림자와 밝은 하이라이트의 과도한 채도를 줄이고 중간톤에 자연스럽게 활기를 모을 수 있다.
- 이 방식은 동적 범위를 늘리는 것이 아니라 기존 데이터의 톤 응답 제어를 바꾸는 것이다.

PetaPixel의 저자 설명이 프로필 생성, 화이트 밸런스 선행, 기초 톤, Select All gamma mask, 색 보정과 최종 마스크 순서를 구체적으로 제시한다. 개별 곡선 모양과 강도는 사진 및 예술적 의도에 의존한다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/14/how-to-leverage-linear-camera-profiles-in-your-editing-workflow/
- 접근일: 2026-08-07
