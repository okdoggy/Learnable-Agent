---
schema_version: '1.0'
scenario_id: raw-20260807-objectexposure01
title_ko: Object 마스크를 빼고 더해 과노출 전경 바위만 균형 보정
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
  subject: landscape
  condition:
  - overbright-foreground
  - ai-object-selection
  intent:
  - local-exposure-balance
  - mask-refinement
method:
  steps:
  - tool: Object mask
    parameter: 과도하게 밝은 전경 바위를 느슨하게 브러시해 AI 객체 선택 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Exposure
    parameter: 선택된 바위만 독립적으로 어둡게 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Subtract > Object
    parameter: 너무 어두워진 바위 부분을 다시 브러시해 기존 마스크에서 제외
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 전역 노출을 건드리지 않고 과도하게 밝은 전경만 낮추면 장면 전체의 명암 관계를 보존할 수 있다.
- AI 선택이 넓게 잡힌 부분은 Subtract로 제거해 바위 사이의 노출 균형을 되찾는다.
collection:
  collector_version: 1.0.0
  content_sha256: a9b1a557297949f1a55f53bb5c547bf1e1016bc9e611f073aeb0db6445d8e0bc
  collected_at: '2026-08-07T00:00:00Z'
---

# Object 마스크를 빼고 더해 과노출 전경 바위만 균형 보정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

풍경 사진에서 전경 바위 일부만 지나치게 밝고 주변 바위는 이미 적정하거나 어두워 전역 Exposure 조정이 부적합할 때 사용한다.

## 촬영/작업 순서

1. Masking 패널에서 새 Object 마스크를 만든다.
2. 과도하게 밝은 바위를 느슨하게 칠해 Lightroom이 객체 경계를 해석하도록 한다.
3. 선택 영역의 Exposure를 낮추고 주변 바위와의 밝기 균형을 확인한다.
4. 마스크가 이미 어두운 바위까지 포함해 그 부분이 과도하게 내려가면 Subtract에서 Object를 선택하고 제외할 부분을 브러시한다.
5. 마스크 오버레이와 개별 마스크의 Eye 전후 보기를 사용해 선택 범위와 보정 효과를 확인한다.

## 추천 시작값 / 조작값

- Object mask / 과도하게 밝은 전경 바위를 느슨하게 브러시해 AI 객체 선택 생성: 원문 정성 표현(수치 추정 없음)
- Exposure / 선택된 바위만 독립적으로 어둡게 조정: 원문 정성 표현(수치 추정 없음)
- Subtract > Object / 너무 어두워진 바위 부분을 다시 브러시해 기존 마스크에서 제외: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 객체 선택을 만든 뒤 먼저 마스크 경계를 확인한다.
- Exposure를 낮춘 뒤 전경 내부의 밝기 편차를 관찰한다.
- 과도하게 어두워진 구간을 Subtract로 제외하고 다시 전후 비교한다.

## 주의할 점

- AI Object 선택은 너무 넓거나 좁을 수 있으므로 생성 직후 오버레이를 검사한다.
- 정성적으로 낮추는 보정이며 원문에 Exposure의 정확한 수치는 제시되지 않았다.
- 전경 전체를 일괄 감광하지 말고 이미 어두운 부분은 마스크에서 제외한다.

## 확실성과 근거

- 전역 노출을 건드리지 않고 과도하게 밝은 전경만 낮추면 장면 전체의 명암 관계를 보존할 수 있다.
- AI 선택이 넓게 잡힌 부분은 Subtract로 제거해 바위 사이의 노출 균형을 되찾는다.

Adobe 공식 튜토리얼이 Object 마스크로 밝은 바위를 선택해 Exposure를 낮추고, 너무 어두워진 부분을 Subtract > Object로 제외하는 순서를 직접 설명한다. 보정량은 원문에 수치가 없어 정성적으로만 기록했다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/masking-basics-lightroom-web
- 접근일: 2026-08-07
