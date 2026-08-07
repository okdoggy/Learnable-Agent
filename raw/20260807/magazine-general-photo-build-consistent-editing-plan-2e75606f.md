---
schema_version: '1.0'
scenario_id: raw-20260807-editplan01
title_ko: 감정적 의도에서 시작하는 Lightroom 5단계 편집 계획
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; workflow by Sean Dalton
  url: https://fstoppers.com/education/stop-guessing-lightroom-and-start-editing-plan-901827
  published_at: '2026-04-24'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: general-photo
  condition:
  - editing-without-direction
  - preset-mismatch
  - color-fatigue
  intent:
  - build-consistent-editing-plan
  - match-visual-mood
  - know-when-to-stop
method:
  steps:
  - tool: Creative intention
    parameter: 보정 전에 사진이 전달해야 할 감정을 문장으로 정함
    value: null
    unit: null
    reported_as: qualitative
  - tool: Workflow stages
    parameter: Prepare, Light, Color, Detail and Effects, Fine-tune의 5단계 순서로 편집
    value: 5
    unit: stages
    reported_as: exact
  - tool: Light and Tone Curve
    parameter: Blacks를 낮추고 Whites를 올린 뒤 Tone Curve의 S-curve로 명암 분리 강화
    value: null
    unit: null
    reported_as: qualitative
  - tool: Color Grading
    parameter: 전역 White Balance 대신 Color Grading에서 중간톤·하이라이트에 온기, 그림자에 파랑을 추가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Final review
    parameter: 시간을 두고 다시 보기, 최초 의도와 대조, 시각 감각이 좋은 타인에게 의견 받기의 3가지 완료 검사
    value: 3
    unit: tests
    reported_as: exact
rationale_ko:
- 편집 전에 감정을 정하면 무작위 slider 조작이나 preset 의존 대신 각 조정을 같은 시각적 목적에 연결할 수 있다.
- 빛과 색을 단계별로 분리하면 문제가 생겼을 때 어느 단계에서 의도와 어긋났는지 진단하기 쉽다.
- 중간톤·하이라이트의 온기와 그림자의 파랑은 전역 화이트 밸런스보다 통제된 색 대비를 만든다.
- 휴식과 외부 의견은 오래 본 뒤 생기는 색 피로와 판단 둔화를 보완한다.
collection:
  collector_version: 1.0.0
  content_sha256: 2e75606f61e77e487ba89bbfc5f626bd674288ae5b68273b03832fe1714b7572
  collected_at: '2026-08-07T00:00:00Z'
---

# 감정적 의도에서 시작하는 Lightroom 5단계 편집 계획

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

preset을 적용한 뒤 무엇이 잘못됐는지 진단하기 어렵거나 패널 사이를 무작위로 오가며 사진의 분위기가 흔들릴 때 사용한다.

## 촬영/작업 순서

1. 조정 전에 사진이 어떤 감정을 전달해야 하는지 정한다.
2. 이미지 준비 단계에서 crop 등 기초 구성을 정리한다.
3. 빛 단계에서 Blacks를 낮추고 Whites를 올린 뒤 S-curve로 의도에 맞는 명암을 만든다.
4. 색 단계에서 전역 화이트 밸런스를 임의로 따뜻하게 하지 않고 중간톤·하이라이트와 그림자에 서로 다른 색 방향을 준다.
5. detail과 effects를 처리한 뒤 전체 결과를 fine-tune한다.
6. 완료 전에 잠시 사진에서 벗어났다가 돌아와 최초 감정과 일치하는지 확인하고, 여전히 확신이 없으면 시각 감각이 좋은 사람의 의견을 구한다.

## 추천 시작값 / 조작값

- Creative intention / 보정 전에 사진이 전달해야 할 감정을 문장으로 정함: 원문 정성 표현(수치 추정 없음)
- Workflow stages / Prepare, Light, Color, Detail and Effects, Fine-tune의 5단계 순서로 편집: 5 stages
- Light and Tone Curve / Blacks를 낮추고 Whites를 올린 뒤 Tone Curve의 S-curve로 명암 분리 강화: 원문 정성 표현(수치 추정 없음)
- Color Grading / 전역 White Balance 대신 Color Grading에서 중간톤·하이라이트에 온기, 그림자에 파랑을 추가: 원문 정성 표현(수치 추정 없음)
- Final review / 시간을 두고 다시 보기, 최초 의도와 대조, 시각 감각이 좋은 타인에게 의견 받기의 3가지 완료 검사: 3 tests

## 보정 루틴

- 각 단계가 시작 전에 정한 감정에 기여하는지 확인하고 그렇지 않은 조정은 되돌린다.
- 빛 단계에서는 Blacks, Whites와 S-curve를 따로 과장하지 말고 함께 만들어내는 명암을 본다.
- 색 단계에서는 따뜻한 중간톤·하이라이트와 푸른 그림자가 의도한 색 대비를 만드는지 확인한다.
- 오래 본 뒤에는 즉시 확정하지 말고 휴식 후 다시 평가해 색 피로를 줄인다.

## 주의할 점

- preset이 분위기와 맞지 않는데도 출발점으로 고정하면 원인을 진단하기 어렵다.
- Blacks, Whites와 S-curve를 과도하게 겹치면 명암이 지나치게 강해질 수 있다.
- 따뜻함과 파랑의 정확한 강도는 원문에 수치가 없으므로 임의로 정량화하지 않는다.
- 다른 사람의 의견은 최초 의도를 대체하는 규칙이 아니라 불확실할 때의 보조 검사다.

## 확실성과 근거

- 편집 전에 감정을 정하면 무작위 slider 조작이나 preset 의존 대신 각 조정을 같은 시각적 목적에 연결할 수 있다.
- 빛과 색을 단계별로 분리하면 문제가 생겼을 때 어느 단계에서 의도와 어긋났는지 진단하기 쉽다.
- 중간톤·하이라이트의 온기와 그림자의 파랑은 전역 화이트 밸런스보다 통제된 색 대비를 만든다.
- 휴식과 외부 의견은 오래 본 뒤 생기는 색 피로와 판단 둔화를 보완한다.

Fstoppers 기사가 Sean Dalton의 5단계 순서와 3가지 완료 검사를 명시하고, surf 사진의 Blacks·Whites·S-curve 및 Color Grading 방향을 설명한다. 정확한 슬라이더 값은 제공하지 않았다.

## 출처

- 원문 URL: https://fstoppers.com/education/stop-guessing-lightroom-and-start-editing-plan-901827
- 접근일: 2026-08-07
