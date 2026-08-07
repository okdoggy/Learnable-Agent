---
schema_version: '1.0'
scenario_id: raw-20260807-etherealedit01
title_ko: 에지 제한 샤프닝·Clarity 감소·그레인·끝점 페이드로 몽환적 톤 구축
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/lightroom-settings-behind-hazy-ethereal-photography-style-901341
  published_at: '2026-04-01'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: travel-landscape
  condition:
  - hazy-scene
  - soft-atmospheric-light
  intent:
  - ethereal-look
  - faded-tones
  - controlled-texture
method:
  steps:
  - tool: White Balance and Exposure
    parameter: 프리셋이나 스타일 보정 전에 이미지별 화이트 밸런스와 노출을 먼저 교정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Sharpening Masking
    parameter: 샤프닝을 주로 고대비 에지에 제한하는 시작 범위
    value: 80–90
    unit: Lightroom slider
    reported_as: exact
  - tool: Clarity
    parameter: 국부 대비를 낮춰 안개 낀 듯한 부드러움을 만드는 대략적 시작값
    value: -20
    unit: Lightroom slider
    reported_as: exact
  - tool: Grain Size
    parameter: 그레인 크기
    value: 50
    unit: Lightroom slider
    reported_as: exact
  - tool: Grain Amount
    parameter: 이미지에 따라 조절하는 그레인 양 범위
    value: 20–50
    unit: Lightroom slider
    reported_as: exact
  - tool: Tone Curve
    parameter: 검정 끝점을 올리고 흰색 끝점을 내려 순수 검정과 흰색을 각각 회색과 오프화이트로 페이드
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 화이트 밸런스와 노출을 먼저 맞춰야 이후 프리셋과 스타일 조정이 예측 가능한 기반에서 작동한다.
- 높은 Sharpening Masking은 넓고 매끈한 영역에 선명도가 되살아나는 것을 막고 에지 중심으로 제한한다.
- Clarity 감소, 의도적 그레인, 곡선 양 끝점 페이드가 함께 작동해 절대적인 검정·흰색과 과도한 미세 대비를 줄인다.
collection:
  collector_version: 1.0.0
  content_sha256: 17e03e8bd625990dcb6bd7382069331c85bbf2c22d8d7c2d8f83496284dc713f
  collected_at: '2026-08-07T00:00:00Z'
---

# 에지 제한 샤프닝·Clarity 감소·그레인·끝점 페이드로 몽환적 톤 구축

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

역광·측광과 안개·물보라 등으로 이미 부드러운 기반이 있는 여행 또는 풍경 사진을 Lightroom에서 흐릿하고 몽환적인 스타일로 일관되게 마무리할 때 사용한다.

## 촬영/작업 순서

1. 프리셋 적용 전에 사진별 White Balance와 Exposure를 교정한다.
2. Sharpening의 Masking을 80–90 정도로 설정해 샤프닝을 고대비 에지 위주로 제한한다.
3. Clarity를 약 -20에서 시작해 국부 대비를 부드럽게 한다.
4. Grain Size를 50으로 두고 Amount를 사진에 따라 20–50 범위에서 조절한다.
5. Tone Curve의 검정 끝점을 올리고 흰색 끝점을 내려 순수 검정과 순수 흰색을 페이드한다.
6. 반복 설정은 프리셋으로 저장하되 각 사진의 노출과 화이트 밸런스는 별도로 다시 맞춘다.

## 추천 시작값 / 조작값

- White Balance and Exposure / 프리셋이나 스타일 보정 전에 이미지별 화이트 밸런스와 노출을 먼저 교정: 원문 정성 표현(수치 추정 없음)
- Sharpening Masking / 샤프닝을 주로 고대비 에지에 제한하는 시작 범위: 80–90 Lightroom slider
- Clarity / 국부 대비를 낮춰 안개 낀 듯한 부드러움을 만드는 대략적 시작값: -20 Lightroom slider
- Grain Size / 그레인 크기: 50 Lightroom slider
- Grain Amount / 이미지에 따라 조절하는 그레인 양 범위: 20–50 Lightroom slider
- Tone Curve / 검정 끝점을 올리고 흰색 끝점을 내려 순수 검정과 흰색을 각각 회색과 오프화이트로 페이드: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 화이트 밸런스와 노출을 먼저 확정한 다음 스타일 보정을 쌓는다.
- 에지 샤프닝 제한과 Clarity 감소로 부드러움을 만들고 그레인을 추가해 질감을 통합한다.
- 마지막으로 Tone Curve 끝점을 페이드해 톤의 상한과 하한을 부드럽게 닫는다.
- 사진마다 그레인 Amount와 기본 노출·색 균형을 다시 점검한다.

## 주의할 점

- 원문의 Clarity -20은 대략적인 시작점이며 모든 사진의 고정 최종값이 아니다.
- Sharpening Masking, 그레인, Clarity 중 하나만 과하게 사용해 전체 효과를 대신하려 하지 않는다.
- 프리셋은 기본 노출과 화이트 밸런스 보정의 대체물이 아니다.
- 검정과 흰색 끝점을 과도하게 안쪽으로 이동하면 전체 대비가 지나치게 탁해질 수 있다.

## 확실성과 근거

- 화이트 밸런스와 노출을 먼저 맞춰야 이후 프리셋과 스타일 조정이 예측 가능한 기반에서 작동한다.
- 높은 Sharpening Masking은 넓고 매끈한 영역에 선명도가 되살아나는 것을 막고 에지 중심으로 제한한다.
- Clarity 감소, 의도적 그레인, 곡선 양 끝점 페이드가 함께 작동해 절대적인 검정·흰색과 과도한 미세 대비를 줄인다.

Fstoppers 기사가 Roman Fox의 정확한 시작 범위로 Sharpening Masking 약 80–90, Clarity 약 -20, Grain Size 50, Grain Amount 20–50을 제시하고 Tone Curve 양 끝점 페이드를 설명한다. 이 수치는 스타일의 시작점이며 이미지별 조정이 필요하다는 문맥도 함께 보존했다.

## 출처

- 원문 URL: https://fstoppers.com/education/lightroom-settings-behind-hazy-ethereal-photography-style-901341
- 접근일: 2026-08-07
