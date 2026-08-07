---
schema_version: '1.0'
scenario_id: raw-20260807-eyesclera
title_ko: Eye Sclera 마스크로 눈 흰자를 미세하게 밝히고 노란 기 중화
status: validated
source:
  type: official
  publisher: Adobe Lightroom Learn
  author: Kristina Sherk
  url: https://www.adobe.com/learn/lightroom-cc/web/ai-portrait-mask-lightroom
  published_at: '2025-12-18'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait
  condition:
  - portrait
  - yellow-eye-whites
  - ai-person-mask-available
  intent:
  - subtle-eye-brightening
  - neutralize-yellow-cast
  - natural-retouch
method:
  steps:
  - tool: Lightroom Masking > People > Eye Sclera
    parameter: Eye Sclera mask Exposure
    value: 0.2
    unit: EV-equivalent Lightroom slider
    reported_as: exact
  - tool: Lightroom Masking > People > Eye Sclera
    parameter: Eye Sclera mask Temperature
    value: -4
    unit: Lightroom slider
    reported_as: exact
  - tool: Lightroom Masks panel
    parameter: 눈에 띄지 않을 정도로만 냉각하고 전후 비교
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 눈 흰자를 조금 밝히고 약하게 냉각하면 노란 기를 완화할 수 있다.
- Eye Sclera를 독립 마스크로 두면 피부와 홍채에 영향을 주지 않고 강도를 검토할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 3bb99e64352d60ea37aceec9be0e393eec6108bcd2119a2b90b6ff95b6b60ad9
  collected_at: '2026-08-07T00:00:00Z'
---

# Eye Sclera 마스크로 눈 흰자를 미세하게 밝히고 노란 기 중화

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

인물 사진에서 눈 흰자가 약간 어둡거나 노랗게 보여 생기를 보완하되, 인위적인 새하얀 눈이나 푸른 눈으로 만들고 싶지 않을 때 사용한다.

## 촬영/작업 순서

1. Masking의 People에서 인물을 선택한다.
2. Eye Sclera를 별도 마스크로 생성한다.
3. Exposure와 Temperature를 원문이 제시한 미세한 시작값으로 조정한다.
4. 확대 화면과 전체 화면에서 냉색이 눈에 띄는지 검토하고 과하면 값을 원점 쪽으로 줄인다.

## 추천 시작값 / 조작값

- Lightroom Masking > People > Eye Sclera / Eye Sclera mask Exposure: 0.2 EV-equivalent Lightroom slider
- Lightroom Masking > People > Eye Sclera / Eye Sclera mask Temperature: -4 Lightroom slider
- Lightroom Masks panel / 눈에 띄지 않을 정도로만 냉각하고 전후 비교: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Eye Sclera를 다른 얼굴 특징과 분리된 마스크로 만든다.
- Exposure를 약 +0.20 올려 흰자를 조금 밝힌다.
- Temperature를 약 -4로 낮춰 노란 기를 매우 미세하게 중화한다.
- 마스크를 껐다 켜면서 밝기와 냉색이 보정 사실을 드러내지 않는지 확인한다.

## 주의할 점

- 눈 흰자가 눈에 띄게 파랗게 보일 정도로 Temperature를 낮추지 않는다.
- 자동 Eye Sclera 선택이 홍채·속눈썹·피부에 번졌는지 확대해서 확인한다.
- 노출 증가는 눈의 기존 하이라이트를 날리지 않는 범위에서 검토한다.

## 확실성과 근거

- 눈 흰자를 조금 밝히고 약하게 냉각하면 노란 기를 완화할 수 있다.
- Eye Sclera를 독립 마스크로 두면 피부와 홍채에 영향을 주지 않고 강도를 검토할 수 있다.

Adobe 튜토리얼은 Eye Sclera의 Exposure 약 +0.20과 Temperature 약 -4를 직접 제시하고, 파란색이 눈에 띄지 않도록 절제하라고 설명한다. 다른 사진에서의 최종 강도는 눈의 원래 색과 노출에 따라 달라진다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/ai-portrait-mask-lightroom
- 접근일: 2026-08-07
