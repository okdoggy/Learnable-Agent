---
schema_version: '1.0'
scenario_id: raw-20260807-aimaskbatch
title_ko: Subject·Sky AI 마스크를 사진 묶음에 복사해 각 이미지에서 재계산
status: validated
source:
  type: official
  publisher: Adobe Lightroom Help
  author: unknown
  url: https://helpx.adobe.com/lightroom/desktop/edit-photos/masking.html
  published_at: '2026-08-04'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom Desktop
scenario:
  subject: photo-series
  condition:
  - photo-series
  - similar-edit-intent
  - ai-subject-or-sky-mask
  intent:
  - batch-local-adjustments
  - consistent-series-edit
  - reduce-repetitive-masking
method:
  steps:
  - tool: Lightroom Masking
    parameter: 대표 사진에서 Select Subject 또는 Select Sky 마스크와 국소 조정 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Copy Edit Settings
    parameter: Copy Settings에서 Masking을 포함해 복사
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Paste to Entire Selection
    parameter: Filmstrip의 대상 사진 전체에 붙여넣기
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom AI Mask recalculation
    parameter: 각 사진에서 AI Subject 또는 Sky 선택 재계산
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- AI 마스크 설정은 고정 좌표를 단순 복사하지 않고 각 사진의 Subject 또는 Sky를 다시 분석하므로 연속 사진에 같은 보정 의도를 확장할 수 있다.
- 대표 이미지에서 보정을 설계한 뒤 일괄 적용하면 유사 촬영 세트의 반복 작업을 줄인다.
collection:
  collector_version: 1.0.0
  content_sha256: 9b9e7267bb695742e7bd2409208c2095596aa0224952cf3adfa10a931d643795
  collected_at: '2026-08-07T00:00:00Z'
---

# Subject·Sky AI 마스크를 사진 묶음에 복사해 각 이미지에서 재계산

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

같은 촬영 세트의 여러 사진에서 피사체 또는 하늘에 유사한 국소 보정을 반복해야 하지만 구도와 위치가 조금씩 달라 고정 마스크 복사가 맞지 않을 때 사용한다.

## 촬영/작업 순서

1. 세트를 대표하는 사진에서 AI 마스크와 보정 방향을 확정한다.
2. Masking을 포함한 편집 설정을 복사한다.
3. 대상 사진 묶음 전체에 붙여넣는다.
4. AI 재계산이 끝난 뒤 다양한 구도의 사진을 골라 경계와 강도를 검수한다.

## 추천 시작값 / 조작값

- Lightroom Masking / 대표 사진에서 Select Subject 또는 Select Sky 마스크와 국소 조정 생성: 원문 정성 표현(수치 추정 없음)
- Lightroom Copy Edit Settings / Copy Settings에서 Masking을 포함해 복사: 원문 정성 표현(수치 추정 없음)
- Lightroom Paste to Entire Selection / Filmstrip의 대상 사진 전체에 붙여넣기: 원문 정성 표현(수치 추정 없음)
- Lightroom AI Mask recalculation / 각 사진에서 AI Subject 또는 Sky 선택 재계산: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 대표 사진에서 Select Subject 또는 Select Sky 마스크를 만들고 국소 보정을 완료한다.
- Copy Edit Settings에서 Masking과 필요한 다른 설정을 선택해 복사한다.
- Filmstrip에서 대상 사진들을 선택하고 Paste to Entire Selection을 실행한다.
- Lightroom이 각 사진의 AI 마스크를 다시 계산한 뒤 서로 다른 구도와 피사체에서 경계를 표본 검수한다.

## 주의할 점

- AI Subject 또는 Sky 선택은 각 사진에서 다시 계산되므로 붙여넣기 후 경계를 표본 점검한다.
- AI 처리가 완료되지 않은 이미지는 최신 마스크가 반영되지 않은 채 내보낼 위험이 있으므로 처리 상태를 확인한다.
- 수동 Brush처럼 이미지 좌표에 고정된 마스크를 AI 재계산과 같은 방식으로 기대하지 않는다.

## 확실성과 근거

- AI 마스크 설정은 고정 좌표를 단순 복사하지 않고 각 사진의 Subject 또는 Sky를 다시 분석하므로 연속 사진에 같은 보정 의도를 확장할 수 있다.
- 대표 이미지에서 보정을 설계한 뒤 일괄 적용하면 유사 촬영 세트의 반복 작업을 줄인다.

Adobe 공식 도움말이 Subject 또는 Sky 마스크와 조정을 복사한 뒤 Paste to Entire Selection을 사용하면 각 대상 사진에서 AI 선택이 다시 계산된다고 직접 설명한다. 사진마다 생기는 선택 오류의 유형은 원문 원칙에 따른 실무적 주의다.

## 출처

- 원문 URL: https://helpx.adobe.com/lightroom/desktop/edit-photos/masking.html
- 접근일: 2026-08-07
