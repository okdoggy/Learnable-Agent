---
schema_version: '1.0'
scenario_id: raw-20260807-skybrush50
title_ko: Sky 마스크에 50% Density 브러시를 더해 밝은 언덕 균형 맞추기
status: validated
source:
  type: official
  publisher: Adobe Learn
  author: Seán Duggan
  url: https://www.adobe.com/learn/lightroom-cc/web/edit-part-photo-lightroom-cc
  published_at: '2025-12-18'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: landscape
  condition:
  - bright-hills
  - dramatic-sky
  - uneven-landscape-tones
  intent:
  - balance-tones
  - preserve-cloud-highlights
  - refine-ai-mask
method:
  steps:
  - tool: Lightroom Auto
    parameter: 전체 사진의 기본 상태를 개선하는 Auto 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking > Sky
    parameter: AI로 하늘 영역 선택
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Sky mask > Exposure
    parameter: 하늘을 약간 어둡게 하도록 Exposure를 왼쪽으로 이동
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Sky mask > Highlights
    parameter: 밝은 구름이 지나치게 어두워지지 않도록 Highlights 증가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Sky mask > Add > Brush
    parameter: 기존 Sky 마스크에 Brush 구성 요소 추가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Brush > Density
    parameter: 언덕에는 기존 하늘 보정의 절반 강도만 전달하도록 Density 설정
    value: 50
    unit: percent
    reported_as: exact
  - tool: Lightroom Brush
    parameter: 밝은 언덕의 위쪽 부분만 브러시로 칠해 약하게 어둡게 처리
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 하늘의 Exposure를 낮춘 뒤 Highlights를 올리면 전체 하늘은 더 극적으로 만들면서 밝은 구름의 광도를 보존할 수 있다.
- 기존 Sky 마스크에 Brush를 추가하면 같은 보정 방향을 인접 언덕에 별도 강도로 확장할 수 있다.
- Density를 약 50%로 낮추면 언덕이 하늘과 동일한 강도로 어두워지는 것을 피할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 1a2bd4cc20fbaad47d99fef28ad3ffe4dc54198fca76ef1d95b7e372ea09093d
  collected_at: '2026-08-07T00:00:00Z'
---

# Sky 마스크에 50% Density 브러시를 더해 밝은 언덕 균형 맞추기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

풍경에서 하늘을 어둡게 해 극적인 분위기를 만들었지만 인접한 먼 언덕이 상대적으로 너무 밝고, 하늘과 동일한 강도의 감광을 언덕에 적용하면 과도해질 때 사용한다.

## 촬영/작업 순서

1. Auto로 전체 사진의 기본 톤을 먼저 정리한다.
2. Sky 마스크를 만들고 Exposure를 약간 낮춰 하늘을 어둡게 한다.
3. Highlights를 올려 밝은 구름 부분이 지나치게 어두워지지 않도록 보존한다.
4. 결과를 평가해 특히 오른쪽 먼 언덕의 과도한 밝기를 확인한다.
5. 새 마스크 대신 기존 Sky 마스크에서 Add > Brush를 선택한다.
6. 브러시 Density를 약 50%로 낮추고 언덕 위쪽만 칠해 기존 하늘 보정을 약한 강도로 확장한다.
7. Sky 1과 Brush 1의 개별 오버레이를 확인해 각 구성 요소가 의도한 영역을 제어하는지 검증한다.

## 추천 시작값 / 조작값

- Lightroom Auto / 전체 사진의 기본 상태를 개선하는 Auto 조정: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking > Sky / AI로 하늘 영역 선택: 원문 정성 표현(수치 추정 없음)
- Lightroom Sky mask > Exposure / 하늘을 약간 어둡게 하도록 Exposure를 왼쪽으로 이동: 원문 정성 표현(수치 추정 없음)
- Lightroom Sky mask > Highlights / 밝은 구름이 지나치게 어두워지지 않도록 Highlights 증가: 원문 정성 표현(수치 추정 없음)
- Lightroom Sky mask > Add > Brush / 기존 Sky 마스크에 Brush 구성 요소 추가: 원문 정성 표현(수치 추정 없음)
- Lightroom Brush > Density / 언덕에는 기존 하늘 보정의 절반 강도만 전달하도록 Density 설정: 50 percent
- Lightroom Brush / 밝은 언덕의 위쪽 부분만 브러시로 칠해 약하게 어둡게 처리: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 하늘 감광 뒤 구름의 밝은 영역이 뭉개지는지 먼저 보고 Highlights로 균형을 되찾는다.
- 언덕 보정은 Density 50%를 시작점으로 삼아 기존 조정이 전 강도로 전달되지 않게 한다.
- 브러시 Size와 Feather를 경계 크기와 전환에 맞추고, 구성 요소별 썸네일 위에 포인터를 올려 오버레이를 확인한다.
- 전체 전후 비교에서 하늘의 극적 효과와 언덕의 자연스러운 밝기 연결이 함께 유지되는지 점검한다.

## 주의할 점

- AI Sky 마스크가 장면 전체 균형을 자동으로 해결한다고 가정하지 말고 결과를 평가한다.
- 언덕에 하늘과 같은 감광을 전 강도로 적용하면 부자연스럽게 어두워질 수 있으므로 낮은 Density를 사용한다.
- Feather가 너무 낮으면 하늘과 언덕 경계에 눈에 띄는 전환이 생길 수 있다.
- 원문은 Density 약 50% 외의 Exposure, Highlights, Size, Feather 수치를 제시하지 않았다.

## 확실성과 근거

- 하늘의 Exposure를 낮춘 뒤 Highlights를 올리면 전체 하늘은 더 극적으로 만들면서 밝은 구름의 광도를 보존할 수 있다.
- 기존 Sky 마스크에 Brush를 추가하면 같은 보정 방향을 인접 언덕에 별도 강도로 확장할 수 있다.
- Density를 약 50%로 낮추면 언덕이 하늘과 동일한 강도로 어두워지는 것을 피할 수 있다.

Adobe Learn 튜토리얼이 Auto, Sky 감광, Highlights 보존, 기존 Sky 마스크에 Brush 추가, Density 약 50%, 언덕 위쪽 도색 및 구성 요소별 오버레이 확인을 직접 설명한다. Exposure·Highlights·브러시 Size·Feather는 정성적으로만 제시되어 수치화하지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/edit-part-photo-lightroom-cc
- 접근일: 2026-08-07
