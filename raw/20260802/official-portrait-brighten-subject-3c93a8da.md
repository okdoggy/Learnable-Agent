---
schema_version: '1.0'
scenario_id: raw-20260802-mobilegraphic01
title_ko: Lightroom Mobile Quick Action 마스크를 확장해 인물과 고채도 배경 분리
status: validated
source:
  type: official
  publisher: Adobe
  author: Seán Duggan
  url: https://www.adobe.com/learn/lightroom-cc/web/ai-assisted-masking-lightroom-mobile
  published_at: '2026-01-12'
  accessed_at: '2026-08-02T14:23:08Z'
  original_language: en
device:
  capture_device: null
  editing_device: mobile device
  software: Adobe Lightroom mobile
scenario:
  subject: portrait
  condition:
  - mobile-editing
  - ai-subject-mask
  - creative-background
  intent:
  - brighten-subject
  - separate-background
  - create-graphic-color-contrast
method:
  steps:
  - tool: Lightroom mobile Quick Action
    parameter: Magic Wand가 제안한 Subject에서 Light preset을 적용하고 Amount로 강도를 맞춘다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mobile Masking
    parameter: Quick Action 뒤 생성된 AI subject mask를 열어 Exposure와 Contrast를 높이고 Saturation을 보완한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mobile Masking
    parameter: 별도의 Select Background AI mask를 만든다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mobile Light
    parameter: graphic한 high-key 배경을 위해 Exposure와 Contrast를 크게 높이고 Shadows를 약간 밝힌다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mobile Color
    parameter: 인물 의상색과 대비되는 파란색 계열의 background Hue를 탐색한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mobile Color
    parameter: Saturation, Temperature, Tint로 배경색의 강도와 색조를 미세 조정한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mobile comparison
    parameter: press and hold로 원본과 편집본을 반복 비교한다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Quick Action을 출발점으로 사용하면 자동 생성된 정교한 Subject mask를 이후 Masking 패널에서 세부 조정할 수 있다.
- 인물과 배경을 별도 AI 마스크로 나누면 피사체를 밝히면서 배경만 고명도·보색 계열로 바꿔 그래픽한 대비를 만들 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 3c93a8da5d4be35a3bd36f196c4d49c088cc1dbd467ef7b1164b408ace836390
  collected_at: '2026-08-02T14:23:08Z'
---

# Lightroom Mobile Quick Action 마스크를 확장해 인물과 고채도 배경 분리

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

모바일에서 인물을 빠르게 밝힌 뒤 배경을 현실적인 보정이 아닌 밝고 그래픽한 보색 스타일로 분리하려는 사진에 사용한다.

## 촬영/작업 순서

1. Magic Wand Quick Action의 Subject Light preset으로 인물을 먼저 밝히고 Amount를 조절한다.
2. Masking 패널에서 자동 생성된 Subject mask를 열어 Exposure, Contrast, Saturation을 세부 조정한다.
3. 새 Select Background mask를 만들고 red overlay로 적용 범위를 확인한다.
4. 배경의 Exposure와 Contrast를 높이고 Shadows를 조금 밝힌다.
5. 배경 Hue를 의상과 대비되는 방향으로 바꾸고 Saturation, Temperature, Tint로 마무리한다.
6. 길게 눌러 원본과 비교한 뒤 적용한다.

## 추천 시작값 / 조작값

- Lightroom mobile Quick Action / Magic Wand가 제안한 Subject에서 Light preset을 적용하고 Amount로 강도를 맞춘다: 원문 정성 표현(수치 추정 없음)
- Lightroom mobile Masking / Quick Action 뒤 생성된 AI subject mask를 열어 Exposure와 Contrast를 높이고 Saturation을 보완한다: 원문 정성 표현(수치 추정 없음)
- Lightroom mobile Masking / 별도의 Select Background AI mask를 만든다: 원문 정성 표현(수치 추정 없음)
- Lightroom mobile Light / graphic한 high-key 배경을 위해 Exposure와 Contrast를 크게 높이고 Shadows를 약간 밝힌다: 원문 정성 표현(수치 추정 없음)
- Lightroom mobile Color / 인물 의상색과 대비되는 파란색 계열의 background Hue를 탐색한다: 원문 정성 표현(수치 추정 없음)
- Lightroom mobile Color / Saturation, Temperature, Tint로 배경색의 강도와 색조를 미세 조정한다: 원문 정성 표현(수치 추정 없음)
- Lightroom mobile comparison / press and hold로 원본과 편집본을 반복 비교한다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Quick Action 직후 before/after를 비교하고 인물이 과하게 밝아지지 않았는지 본다.
- Subject와 Background mask의 overlay를 각각 확인해 경계 누락과 침범을 Add/Subtract로 보완한다.
- 배경색을 바꾼 뒤 의상색과의 대비가 의도대로 작동하는지 확인한다.
- press-and-hold 비교로 원본의 기준을 잃지 않았는지 점검하고 필요하면 mask Amount나 개별 control을 낮춘다.

## 주의할 점

- 이 배경 색변환은 자연스러운 색 교정이 아니라 의도적으로 과장한 그래픽 효과다.
- red overlay가 피사체를 침범하는지 반드시 확인한다.
- Depth Range mask는 portrait 또는 depth 정보를 기록한 기기 사진에서만 사용할 수 있다.
- 원문은 슬라이더의 정확한 수치를 제시하지 않았으므로 정성 표현만 기록한다.

## 확실성과 근거

- Quick Action을 출발점으로 사용하면 자동 생성된 정교한 Subject mask를 이후 Masking 패널에서 세부 조정할 수 있다.
- 인물과 배경을 별도 AI 마스크로 나누면 피사체를 밝히면서 배경만 고명도·보색 계열로 바꿔 그래픽한 대비를 만들 수 있다.

Quick Action이 만든 Subject mask의 후속 조정, 별도 Background mask, 고명도 배경과 보색 Hue 구성은 Adobe가 직접 시연했다. 파란색 선택은 예제의 붉은 치마와 대비시키기 위한 미적 선택이며 모든 인물 사진의 정답은 아니다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/ai-assisted-masking-lightroom-mobile
- 접근일: 2026-08-02
