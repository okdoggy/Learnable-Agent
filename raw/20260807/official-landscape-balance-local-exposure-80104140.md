---
schema_version: '1.0'
scenario_id: raw-20260807-adobesky01
title_ko: 풍경의 밝은 전경과 하늘을 AI 마스크로 따로 균형 잡기
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
  subject: landscape
  condition:
  - bright-foreground-distraction
  - uneven-landscape-exposure
  - ai-mask-edge-error
  intent:
  - balance-local-exposure
  - preserve-natural-transitions
method:
  steps:
  - tool: Masking > Sky
    parameter: AI Sky mask를 선택하고 하늘에만 Clarity를 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Masking > Object
    parameter: 밝은 전경 바위를 느슨하게 칠해 Object mask로 식별한 뒤 Exposure를 낮춤
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask > Subtract > Object
    parameter: 과도하게 어두워진 바위 부분을 Subtract의 Object masking으로 제외
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask visibility
    parameter: Eye 아이콘으로 각 마스크의 전후 효과를 확인
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 전역 노출 변경 대신 하늘과 전경을 따로 보정하면 장면 전체의 균형을 유지하면서 시선을 분산시키는 밝은 요소를 억제할 수 있다.
- 자동 선택의 오차를 빼기 마스크로 정리하면 바위 경계와 명암이 자연스럽게 유지된다.
collection:
  collector_version: 1.0.0
  content_sha256: 80104140ed2bee96edc0834f46d5d5e151eb334a1bc63983ab7da617b6f7a6df
  collected_at: '2026-08-07T00:00:00Z'
---

# 풍경의 밝은 전경과 하늘을 AI 마스크로 따로 균형 잡기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

풍경 사진에서 하늘의 질감은 살리고 싶지만 밝은 전경 바위가 시선을 빼앗으며, 자동 마스크가 경계 일부를 잘못 포함한 경우에 사용한다.

## 촬영/작업 순서

1. 전체 노출을 먼저 관찰해 전역 조정보다 국부 보정이 필요한지 판단한다.
2. Sky mask를 만들어 하늘에만 필요한 선명도 보정을 적용한다.
3. 별도의 Object mask로 밝은 전경 바위를 선택하고 노출을 낮춘다.
4. 바위 일부가 지나치게 어두워지면 기존 마스크에서 Subtract를 선택해 해당 부분을 제외한다.
5. 마스크 이름을 정리하고 Eye 아이콘으로 각 보정의 전후를 비교한다.

## 추천 시작값 / 조작값

- Masking > Sky / AI Sky mask를 선택하고 하늘에만 Clarity를 조정: 원문 정성 표현(수치 추정 없음)
- Masking > Object / 밝은 전경 바위를 느슨하게 칠해 Object mask로 식별한 뒤 Exposure를 낮춤: 원문 정성 표현(수치 추정 없음)
- Mask > Subtract > Object / 과도하게 어두워진 바위 부분을 Subtract의 Object masking으로 제외: 원문 정성 표현(수치 추정 없음)
- Mask visibility / Eye 아이콘으로 각 마스크의 전후 효과를 확인: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 하늘 마스크의 오버레이가 실제 하늘과 일치하는지 확인한 뒤 Clarity를 정성적으로 조절한다.
- 전경의 밝기가 장면을 방해하지 않을 만큼만 Exposure를 낮추고 주변 바위와의 균형을 본다.
- 빼기 마스크 후 경계가 끊기거나 얼룩진 곳이 없는지 확대해 확인한다.

## 주의할 점

- AI 자동 선택은 보정하지 않아야 할 영역을 포함할 수 있으므로 오버레이를 반드시 확인한다.
- 전경을 과도하게 어둡게 만들면 바위 사이의 자연스러운 노출 균형이 깨진다.
- 원문은 Clarity와 Exposure의 정확한 수치를 제시하지 않았으므로 임의의 값으로 환산하지 않는다.

## 확실성과 근거

- 전역 노출 변경 대신 하늘과 전경을 따로 보정하면 장면 전체의 균형을 유지하면서 시선을 분산시키는 밝은 요소를 억제할 수 있다.
- 자동 선택의 오차를 빼기 마스크로 정리하면 바위 경계와 명암이 자연스럽게 유지된다.

Adobe 공식 튜토리얼이 Sky, Object, Subtract와 Eye 비교 순서를 직접 시연한다. 적용 강도는 원문에 수치가 없어 이미지별 관찰에 맡기는 정성적 절차로 기록했다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/masking-basics-lightroom-web
- 접근일: 2026-08-07
