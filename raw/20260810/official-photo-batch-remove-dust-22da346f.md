---
schema_version: '1.0'
scenario_id: raw-20260810-dustbatch
title_ko: AI 센서 먼지 제거를 촬영 세트에 안전하게 일괄 적용하기
status: validated
source:
  type: official
  publisher: Adobe
  author: Glyn Dewis
  url: https://www.adobe.com/learn/lightroom-cc/web/ai-dust-removal-lightroom
  published_at: '2026-01-26'
  accessed_at: '2026-08-10T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom / Lightroom Classic
scenario:
  subject: photo-batch
  condition:
  - sensor-dust
  - batch-session
  - raw-editing
  intent:
  - remove-dust
  - batch-consistency
  - preserve-real-subjects
method:
  steps:
  - tool: Remove panel
    parameter: Visualize Spots를 활성화하고 Threshold를 사진에 맞게 조정
    value: null
    unit: null
    reported_as: qualitative
  - tool: AI Dust Removal
    parameter: Distraction Removal의 Dust를 선택하고 Apply 활성화
    value: Dust / Apply
    unit: null
    reported_as: exact
  - tool: Copy Edit Settings
    parameter: Copy Settings에서 Select None 후 Remove 섹션의 Dust만 선택해 복사
    value: Dust only
    unit: null
    reported_as: exact
  - tool: Batch editing
    parameter: Grid view에서 대상 범위를 선택해 Paste Edit Settings 적용
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- AI가 각 이미지의 센서 먼지를 독립적으로 분석하므로 동일 좌표를 단순 복사하는 방식보다 촬영 세트 처리에 적합하다.
- 먼지 제거를 먼저 하면 이후 영역 마스크의 재계산 가능성을 줄일 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 22da346f9c5f10b225a6af2784d60a9806ace1d974eb82ae5854e683f343c04d
  collected_at: '2026-08-10T00:00:00Z'
---

# AI 센서 먼지 제거를 촬영 세트에 안전하게 일괄 적용하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

같은 촬영에서 나온 여러 사진에 센서 먼지 자국이 반복되며, 실제 피사체 오검출을 통제하면서 빠르게 정리해야 할 때 사용한다.

## 촬영/작업 순서

1. 개별 사진의 Remove 패널에서 Visualize Spots와 Threshold로 먼지를 식별한다.
2. Distraction Removal의 Dust를 Apply하고 자동 결과를 검사한다.
3. 놓친 점은 수동 브러시로 지우고 새처럼 잘못 제거된 피사체는 해당 제거를 삭제한다.
4. Grid view로 전환해 Copy Settings에서 Dust만 복사한다.
5. 대상 사진 범위를 선택하고 Paste Edit Settings를 적용한 뒤 각 사진을 다시 검사한다.

## 추천 시작값 / 조작값

- Remove panel / Visualize Spots를 활성화하고 Threshold를 사진에 맞게 조정: 원문 정성 표현(수치 추정 없음)
- AI Dust Removal / Distraction Removal의 Dust를 선택하고 Apply 활성화: Dust / Apply
- Copy Edit Settings / Copy Settings에서 Select None 후 Remove 섹션의 Dust만 선택해 복사: Dust only
- Batch editing / Grid view에서 대상 범위를 선택해 Paste Edit Settings 적용: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Visualize Spots로 먼지 후보를 잘 보이게 한 뒤 AI Dust 제거를 적용한다.
- 원본 피사체 오검출과 누락을 확대 검사한다.
- Dust 항목만 복사해 촬영 세트에 붙여넣고 각 사진이 독립 분석되었는지 결과를 확인한다.

## 주의할 점

- AI가 먼 새 같은 실제 피사체를 먼지로 오인할 수 있으므로 자동 결과를 반드시 검사한다.
- 누락된 먼지는 수동 Remove로 보완하고, 잘못 지운 항목은 삭제하거나 결과를 Refresh한다.
- 특정 영역 AI 마스크보다 먼저 먼지 제거를 적용하지 않으면 기존 마스크가 다시 렌더링될 수 있다.

## 확실성과 근거

- AI가 각 이미지의 센서 먼지를 독립적으로 분석하므로 동일 좌표를 단순 복사하는 방식보다 촬영 세트 처리에 적합하다.
- 먼지 제거를 먼저 하면 이후 영역 마스크의 재계산 가능성을 줄일 수 있다.

Adobe 공식 튜토리얼이 단일 사진의 자동 먼지 제거, 오검출 수정, Dust 설정만 복사해 여러 사진에 적용하는 절차를 직접 제공한다. Threshold와 브러시 크기의 수치는 제시되지 않았다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/ai-dust-removal-lightroom
- 접근일: 2026-08-10
