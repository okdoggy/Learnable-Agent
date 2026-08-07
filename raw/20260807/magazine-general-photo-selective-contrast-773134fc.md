---
schema_version: '1.0'
scenario_id: raw-20260807-tonerebuild01
title_ko: 기본 톤을 평탄화한 뒤 Tone Curve로 필요한 구간의 대비 재구축
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/education/lightrooms-tone-curve-explained-every-trick-need-know-902177
  published_at: '2026-05-08'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: general-photo
  condition:
  - flat-starting-edit
  - global-contrast-too-blunt
  intent:
  - selective-contrast
  - tonal-depth
method:
  steps:
  - tool: Basic panel
    parameter: Contrast, Highlights, Whites, Blacks를 중앙 쪽으로 당겨 초기 톤 극단을 줄임
    value: null
    unit: null
    reported_as: qualitative
  - tool: Tone Curve point selector
    parameter: 사진의 원하는 명도 구간을 확인하고 해당 곡선 지점을 위로 올리거나 아래로 내려 선택적 대비를 재구성
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 기본 패널에서 초기 대비를 평탄화한 뒤 곡선으로 다시 만들면 전역 Contrast 슬라이더보다 대비가 나타날 명도 구간을 세밀하게 통제할 수 있다.
- 점 선택기는 특정 물체가 아니라 그 물체가 속한 명도 범위를 가리키므로 톤 구간 중심의 편집에 적합하다.
collection:
  collector_version: 1.0.0
  content_sha256: 773134fc507c36d1977368f503a4c6a2fc5a8db41b3bb50d3e2d089a18ecef53
  collected_at: '2026-08-07T00:00:00Z'
---

# 기본 톤을 평탄화한 뒤 Tone Curve로 필요한 구간의 대비 재구축

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

전역 Contrast 조정으로는 하이라이트·중간톤·그림자의 대비 위치를 원하는 대로 분리하기 어려워, 사진의 깊이와 펀치를 명도 구간별로 설계하려는 경우에 사용한다.

## 촬영/작업 순서

1. Basic 패널의 Contrast, Highlights, Whites, Blacks를 중앙 방향으로 조정해 기존 톤 극단을 완화한다.
2. Tone Curve에서 검정부터 흰색까지의 명도 분포를 확인한다.
3. 점 선택기로 사진 속 관심 명도 구간을 식별한다.
4. 그 구간을 밝히려면 곡선 지점을 올리고 어둡게 하려면 내리면서 대비를 재구축한다.
5. 전역 대비보다 필요한 구간에만 깊이와 펀치가 생겼는지 전후 비교한다.

## 추천 시작값 / 조작값

- Basic panel / Contrast, Highlights, Whites, Blacks를 중앙 쪽으로 당겨 초기 톤 극단을 줄임: 원문 정성 표현(수치 추정 없음)
- Tone Curve point selector / 사진의 원하는 명도 구간을 확인하고 해당 곡선 지점을 위로 올리거나 아래로 내려 선택적 대비를 재구성: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 평탄화 단계와 곡선 재구축 단계를 분리해 진행한다.
- 곡선 지점을 움직일 때 인접 명도 범위의 변화를 함께 관찰한다.
- 전체 사진의 절대적인 대비보다 의도한 명도 구간에 대비가 배치됐는지 확인한다.

## 주의할 점

- 점 선택기로 물체를 클릭해도 그 물체만 공간적으로 선택되는 것은 아니다.
- 원문은 각 슬라이더와 곡선 지점의 정확한 수치를 제시하지 않았다.
- 초기 평탄화를 과하게 적용하면 곡선 재구축 전 이미지가 지나치게 무기력해질 수 있으므로 최종 결과를 기준으로 판단한다.

## 확실성과 근거

- 기본 패널에서 초기 대비를 평탄화한 뒤 곡선으로 다시 만들면 전역 Contrast 슬라이더보다 대비가 나타날 명도 구간을 세밀하게 통제할 수 있다.
- 점 선택기는 특정 물체가 아니라 그 물체가 속한 명도 범위를 가리키므로 톤 구간 중심의 편집에 적합하다.

Fstoppers 기사에서 Ryan Breitkreutz가 기본 톤 극단을 중앙으로 당겨 평탄화한 뒤 Tone Curve로 대비를 선택적으로 재구축하는 기법을 설명한다. 수치는 제시되지 않아 모든 조정을 정성 값으로 보존했다.

## 출처

- 원문 URL: https://fstoppers.com/education/lightrooms-tone-curve-explained-every-trick-need-know-902177
- 접근일: 2026-08-07
