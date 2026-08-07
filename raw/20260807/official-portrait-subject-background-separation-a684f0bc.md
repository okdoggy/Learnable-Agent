---
schema_version: '1.0'
scenario_id: raw-20260807-portraitsplit01
title_ko: Entire Person과 Background 마스크로 저노출 인물과 배경을 독립 보정
status: validated
source:
  type: official
  publisher: Adobe Lightroom Learn
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
  - underexposed-subject
  - ai-people-detection
  intent:
  - subject-background-separation
  - local-exposure-balance
method:
  steps:
  - tool: People mask
    parameter: 검출된 인물에서 Entire Person을 선택해 인물 전체 마스크 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Exposure
    parameter: 인물 마스크의 노출을 올려 저노출 피사체만 밝게 보정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Background mask
    parameter: 별도 배경 마스크를 만들고 배경을 어둡게 조정
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 인물과 배경을 서로 다른 마스크로 분리하면 한쪽의 노출 보정이 다른 쪽에 의도치 않게 영향을 주는 것을 막을 수 있다.
- 저노출 인물을 밝히고 배경을 어둡게 하면 피사체와 배경의 시각적 분리를 강화할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: a684f0bcf0996cd5ab03b2eceaf52d8515158731b029a7cc8848402de3077fe3
  collected_at: '2026-08-07T00:00:00Z'
---

# Entire Person과 Background 마스크로 저노출 인물과 배경을 독립 보정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

인물은 저노출인데 배경은 상대적으로 밝아 전역 Exposure만으로는 두 영역을 함께 적절히 맞추기 어려운 인물 사진에 사용한다.

## 촬영/작업 순서

1. Masking의 People에서 해당 인물을 선택하고 Entire Person 마스크를 만든다.
2. 인물 마스크의 Exposure를 올려 피사체 밝기를 회복한다.
3. 새 Background 마스크를 별도로 생성한다.
4. 배경 마스크의 Exposure를 낮춰 인물과 배경의 밝기 관계를 정리한다.
5. 각 자동 마스크를 검사하고 누락 또는 과선택 영역은 Add나 Subtract로 보완한다.

## 추천 시작값 / 조작값

- People mask / 검출된 인물에서 Entire Person을 선택해 인물 전체 마스크 생성: 원문 정성 표현(수치 추정 없음)
- Exposure / 인물 마스크의 노출을 올려 저노출 피사체만 밝게 보정: 원문 정성 표현(수치 추정 없음)
- Background mask / 별도 배경 마스크를 만들고 배경을 어둡게 조정: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 인물 밝기를 먼저 맞춘 뒤 배경을 별도로 감광한다.
- 각 마스크의 Eye 아이콘으로 효과를 개별 비교한다.
- 경계나 겹침이 부자연스러우면 Add 또는 Subtract로 선택을 수정한다.

## 주의할 점

- People 및 Background 자동 마스크는 반드시 오버레이로 검사한다.
- Exposure 조정량은 원문에 정확한 수치가 없어 이미지에 맞춰 정성적으로 결정한다.
- 배경을 과도하게 어둡게 하면 인물 주변 경계가 인위적으로 보일 수 있다.

## 확실성과 근거

- 인물과 배경을 서로 다른 마스크로 분리하면 한쪽의 노출 보정이 다른 쪽에 의도치 않게 영향을 주는 것을 막을 수 있다.
- 저노출 인물을 밝히고 배경을 어둡게 하면 피사체와 배경의 시각적 분리를 강화할 수 있다.

Adobe 공식 튜토리얼이 Entire Person 마스크의 Exposure를 올리고 별도 Background 마스크를 어둡게 하는 사례를 직접 제시한다. 수치와 구체적인 최종 명암비는 제시하지 않아 기록하지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/masking-basics-lightroom-web
- 접근일: 2026-08-07
