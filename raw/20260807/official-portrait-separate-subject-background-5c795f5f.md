---
schema_version: '1.0'
scenario_id: raw-20260807-adobeperson01
title_ko: 어두운 인물은 밝히고 배경은 낮춰 자연스럽게 분리하기
status: validated
source:
  type: official
  publisher: Adobe
  author: Glyn Dewis
  url: https://www.adobe.com/learn/lightroom-cc/web/masking-basics-lightroom-web
  published_at: '2026-03-18'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom on the web
scenario:
  subject: portrait
  condition:
  - underexposed-person
  - busy-or-bright-background
  intent:
  - separate-subject-background
  - correct-local-exposure
method:
  steps:
  - tool: Masking > People > Entire Person
    parameter: Entire Person mask를 선택하고 인물에만 Exposure를 올림
    value: null
    unit: null
    reported_as: qualitative
  - tool: Masking > Background
    parameter: 별도 Background mask를 만들고 배경만 어둡게 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask visibility
    parameter: Eye 아이콘으로 각 마스크의 기여도를 전후 비교
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 인물과 배경을 상반된 방향으로 국부 보정하면 전체 사진을 일괄 밝히지 않고도 피사체 분리를 만들 수 있다.
- People 마스크는 피부·얼굴·머리카락·의상 또는 인물 전체를 구분할 수 있어 보정 범위를 제한한다.
collection:
  collector_version: 1.0.0
  content_sha256: 5c795f5f2e8eed436ee0960eb161cb69a13425288febb83f13a70105bd99f998
  collected_at: '2026-08-07T00:00:00Z'
---

# 어두운 인물은 밝히고 배경은 낮춰 자연스럽게 분리하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

인물이 노출 부족이지만 사진 전체를 밝히면 배경까지 과도하게 밝아지는 인물 사진에서 사용한다.

## 촬영/작업 순서

1. People 감지 결과에서 Entire Person을 선택해 인물 마스크를 만든다.
2. 인물 마스크의 Exposure를 올려 피사체만 밝힌다.
3. 별도의 Background 마스크를 생성해 배경을 어둡게 한다.
4. 각 마스크의 Eye 아이콘을 전환해 분리 효과가 자연스러운지 비교한다.

## 추천 시작값 / 조작값

- Masking > People > Entire Person / Entire Person mask를 선택하고 인물에만 Exposure를 올림: 원문 정성 표현(수치 추정 없음)
- Masking > Background / 별도 Background mask를 만들고 배경만 어둡게 조정: 원문 정성 표현(수치 추정 없음)
- Mask visibility / Eye 아이콘으로 각 마스크의 기여도를 전후 비교: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 인물의 피부와 의상 하이라이트가 손상되지 않는 범위에서 노출을 올린다.
- 배경은 인물보다 덜 주목될 정도로만 어둡게 하며 경계의 부자연스러운 띠를 관찰한다.
- 각 마스크를 끄고 켜며 한쪽 보정이 과도하게 결과를 지배하지 않는지 확인한다.

## 주의할 점

- 인물과 배경의 밝기 차이를 과장하면 오려 붙인 듯한 결과가 될 수 있다.
- AI가 인물의 머리카락이나 의상 가장자리를 놓칠 수 있으므로 마스크 오버레이를 확인한다.
- 원문은 Exposure의 정확한 수치를 제시하지 않았다.

## 확실성과 근거

- 인물과 배경을 상반된 방향으로 국부 보정하면 전체 사진을 일괄 밝히지 않고도 피사체 분리를 만들 수 있다.
- People 마스크는 피부·얼굴·머리카락·의상 또는 인물 전체를 구분할 수 있어 보정 범위를 제한한다.

Adobe 공식 튜토리얼이 Entire Person의 Exposure 상승과 별도 Background 마스크의 어둡게 조정을 직접 설명한다. 구체 강도와 경계 보정은 이미지에 따라 결정해야 한다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/masking-basics-lightroom-web
- 접근일: 2026-08-07
