---
schema_version: '1.0'
scenario_id: raw-20260802-linearprofile01
title_ko: 선형 카메라 프로필 아래에서 색보정하고 최종 감마 곡선으로 마무리
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Vlad Moldovean
  url: https://petapixel.com/2026/06/14/how-to-leverage-linear-camera-profiles-in-your-editing-workflow/
  published_at: '2026-06-14'
  accessed_at: '2026-08-02T14:23:08Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom; Adobe DNG Profile Editor
scenario:
  subject: raw-photo
  condition:
  - high-dynamic-range
  - filmic-color-grade
  - linear-camera-profile
  intent:
  - control-tonal-response
  - smooth-color-transitions
  - custom-highlight-rolloff
method:
  steps:
  - tool: 카메라 촬영 설정
    parameter: 중립적인 인카메라 picture profile로 미리보기와 live histogram의 대비 왜곡을 줄인다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Adobe DNG Profile Editor
    parameter: 카메라 RAW에서 내보낸 DNG의 Tone Curve를 linear로 설정하고 카메라별 프로필을 내보낸다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom 로컬 마스크
    parameter: 프로필 전환 전에 국부 노출 문제를 먼저 보정한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom White Balance
    parameter: 강한 색 편향이 있으면 선형 프로필을 적용하기 전에 화이트 밸런스를 맞춘다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Profile
    parameter: 제작한 linear camera profile로 전환한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Basic
    parameter: 히스토그램을 보며 Exposure, Blacks, Whites로 밝기와 검정점·흰점을 배치하되 clipping을 피한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Basic
    parameter: 필요할 때 Shadows와 Highlights로 디테일을 회복하되 HDR처럼 보이지 않게 한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking
    parameter: 사진 전체를 포함하는 Select All 마스크 안에서 부드러운 custom gamma curve를 만든다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom mask tone curve
    parameter: 톤 그라데이션을 지키도록 가능한 적은 control point로 매끄럽게 구성한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Color
    parameter: custom gamma curve가 만들어진 뒤 Color Response Curves, color wheels와 HSL로 주 색보정을 진행한다
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Effects와 로컬 마스크
    parameter: grain, 미세한 lens-sharpness falloff, 국부 빛과 색 재형성을 마지막에 더한다
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 평평한 선형 응답 아래에서 노출과 색을 다듬고 마지막에 감마 대비를 부여하면 강한 대비가 거칠어지는 위험을 줄이고 색 전이를 더 자연스럽게 제어할 수 있다는 저자의 실험 기반 워크플로다.
- 이 방식은 센서의 실제 dynamic range를 늘리는 것이 아니라 이미 기록된 톤의 렌더링 순서를 편집자가 직접 구성하도록 한다.
collection:
  collector_version: 1.0.0
  content_sha256: d8a60eb2ecbe0c8a55442d8902fb6ae6679c257b082c544d9a7eb458446f28cc
  collected_at: '2026-08-02T14:23:08Z'
---

# 선형 카메라 프로필 아래에서 색보정하고 최종 감마 곡선으로 마무리

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

표준 Lightroom 프로필보다 하이라이트 shoulder, 중간톤 색 분리, 영화적인 대비를 세밀하게 설계해야 하는 RAW 사진에 적용한다.

## 촬영/작업 순서

1. 촬영 시 중립적인 picture profile로 미리보기와 histogram을 확인한다.
2. 카메라마다 선형 프로필을 한 번 만들고 Lightroom에 가져온다.
3. 원본의 국부 노출과 강한 색 편향을 먼저 정리한 뒤 선형 프로필로 전환한다.
4. Exposure, Blacks, Whites를 히스토그램 기준으로 배치하고 필요한 범위에서 Shadows와 Highlights를 보완한다.
5. 전체 선택 마스크의 tone curve로 최종 감마 곡선을 만든 뒤 그 아래 단계에서 주 색보정을 완성한다.
6. grain과 국부 마스크를 더하고, 마스크 순서가 꼬였으면 감마 곡선을 새 Select All 마스크로 옮겨 마지막 처리 단계가 되게 한다.

## 추천 시작값 / 조작값

- 카메라 촬영 설정 / 중립적인 인카메라 picture profile로 미리보기와 live histogram의 대비 왜곡을 줄인다: 원문 정성 표현(수치 추정 없음)
- Adobe DNG Profile Editor / 카메라 RAW에서 내보낸 DNG의 Tone Curve를 linear로 설정하고 카메라별 프로필을 내보낸다: 원문 정성 표현(수치 추정 없음)
- Lightroom 로컬 마스크 / 프로필 전환 전에 국부 노출 문제를 먼저 보정한다: 원문 정성 표현(수치 추정 없음)
- Lightroom White Balance / 강한 색 편향이 있으면 선형 프로필을 적용하기 전에 화이트 밸런스를 맞춘다: 원문 정성 표현(수치 추정 없음)
- Lightroom Profile / 제작한 linear camera profile로 전환한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Basic / 히스토그램을 보며 Exposure, Blacks, Whites로 밝기와 검정점·흰점을 배치하되 clipping을 피한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Basic / 필요할 때 Shadows와 Highlights로 디테일을 회복하되 HDR처럼 보이지 않게 한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking / 사진 전체를 포함하는 Select All 마스크 안에서 부드러운 custom gamma curve를 만든다: 원문 정성 표현(수치 추정 없음)
- Lightroom mask tone curve / 톤 그라데이션을 지키도록 가능한 적은 control point로 매끄럽게 구성한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Color / custom gamma curve가 만들어진 뒤 Color Response Curves, color wheels와 HSL로 주 색보정을 진행한다: 원문 정성 표현(수치 추정 없음)
- Lightroom Effects와 로컬 마스크 / grain, 미세한 lens-sharpness falloff, 국부 빛과 색 재형성을 마지막에 더한다: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 선형 프로필 적용 직후 이미지가 어둡고 평평해 보이는 것을 오류로 보지 말고 히스토그램으로 black/white point와 clipping을 확인한다.
- 필름풍이면 넓고 부드러운 highlight shoulder를, 현대적인 결과면 middle gray 부근을 pivot으로 한 절제된 S-curve를 설계한다.
- 색보정 후 gradient가 흐트러지면 custom gamma curve를 복사해 새 Select All 마스크에 붙여 mask stack의 마지막 단계로 재배치한다.
- 완성본에서 디테일이 보존되어 보이는지와 동시에 대비가 지나치게 평평하거나 HDR처럼 인공적이지 않은지 비교한다.

## 주의할 점

- 선형 프로필은 실제 센서 dynamic range를 늘리지 않는다.
- 카메라 모델마다 별도 프로필이 필요하며 표준 프로필보다 작업이 느리고 복잡하다.
- Shadows와 Highlights를 과도하게 조정하면 인공적인 HDR 인상이 생길 수 있다.
- Lightroom의 패널 표시 순서와 실제 처리 순서가 같지 않고, mask는 생성·stack 순서의 영향을 받으므로 최종 감마 위치를 점검한다.
- 대부분의 사진은 표준 프로필로 더 빠르게 완성할 수 있으므로 최대 톤 제어가 필요한 작업에 한정한다.

## 확실성과 근거

- 평평한 선형 응답 아래에서 노출과 색을 다듬고 마지막에 감마 대비를 부여하면 강한 대비가 거칠어지는 위험을 줄이고 색 전이를 더 자연스럽게 제어할 수 있다는 저자의 실험 기반 워크플로다.
- 이 방식은 센서의 실제 dynamic range를 늘리는 것이 아니라 이미 기록된 톤의 렌더링 순서를 편집자가 직접 구성하도록 한다.

선형 프로필 제작, 보정 순서, 전체 마스크의 감마 곡선, 마스크 처리 순서와 제한은 저자가 한 달 이상 매일 실험한 결과로 원문에 직접 설명했다. 특정 사진에 가장 적합한 곡선 모양과 미적 결과는 이미지와 의도에 따라 달라지며 수치 시작값은 원문이 제시하지 않아 기록하지 않았다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/14/how-to-leverage-linear-camera-profiles-in-your-editing-workflow/
- 접근일: 2026-08-02
