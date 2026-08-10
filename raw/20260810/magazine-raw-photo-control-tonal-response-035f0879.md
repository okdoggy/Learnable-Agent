---
schema_version: '1.0'
scenario_id: raw-20260810-lineargrade
title_ko: 선형 카메라 프로파일과 사용자 감마 커브로 필름풍 RAW 그레이딩하기
status: validated
source:
  type: magazine
  publisher: PetaPixel
  author: Vlad Moldovean
  url: https://petapixel.com/2026/06/14/how-to-leverage-linear-camera-profiles-in-your-editing-workflow/
  published_at: '2026-06-14'
  accessed_at: '2026-08-10T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom / Adobe DNG Profile Editor
scenario:
  subject: raw-photo
  condition:
  - high-dynamic-range
  - custom-color-grading
  - filmic-look
  intent:
  - control-tonal-response
  - smooth-highlight-rolloff
  - preserve-color-separation
method:
  steps:
  - tool: DNG Profile Editor
    parameter: DNG Profile Editor의 Tone Curve를 linear로 설정해 카메라 전용 프로파일 생성 후 Lightroom에 가져오기
    value: linear
    unit: null
    reported_as: exact
  - tool: White Balance
    parameter: 강한 색조가 있으면 선형 프로파일 전환 전에 화이트 밸런스를 확정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Basic tone controls
    parameter: 선형 프로파일에서 히스토그램을 보며 Exposure, Blacks, Whites를 조정하고 양 끝 클리핑을 피함
    value: null
    unit: null
    reported_as: qualitative
  - tool: Mask Tone Curve
    parameter: 전체 이미지를 포함하는 Luminance Range Select All 마스크에 매끄러운 사용자 감마 커브 생성
    value: null
    unit: null
    reported_as: qualitative
  - tool: Custom gamma curve
    parameter: 필름풍은 넓은 shoulder, 현대적 렌더링은 중간 회색 근처 피벗의 완만한 S-curve 사용
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 기본 프로파일의 내장 감마 커브를 제거한 평평한 출발점은 하이라이트 롤오프와 톤 반응을 직접 설계할 여지를 준다.
- 색 작업 위에 감마 커브를 적용하면 대비와 채도가 주로 중간톤에 자연스럽게 분배될 수 있다는 것이 저자의 설명이다.
collection:
  collector_version: 1.0.0
  content_sha256: 035f08793e020ddb3d0e1b59e2ce203cae7535fb7f838e4d9175068afdfccfa2
  collected_at: '2026-08-10T00:00:00Z'
---

# 선형 카메라 프로파일과 사용자 감마 커브로 필름풍 RAW 그레이딩하기

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

표준 카메라 프로파일의 대비와 하이라이트 반응이 원하는 영화적 렌더링을 방해해 톤 반응을 직접 설계해야 할 때 사용한다.

## 촬영/작업 순서

1. 자주 쓰는 카메라 RAW를 DNG로 내보내 선형 Tone Curve 프로파일을 만들고 Lightroom에 설치한다.
2. 국소 노출 문제와 화이트 밸런스를 먼저 정리한다.
3. Linear Camera Profile로 바꾼 뒤 히스토그램을 기준으로 기본 노출과 흑백점을 잡는다.
4. 전체 이미지 Luminance Range 마스크에 적은 제어점으로 매끄러운 감마 커브를 만든다.
5. 색 응답 커브, 화이트 밸런스, color wheels, HSL 순으로 룩을 발전시키고 필요한 광원·색 마스크를 추가한다.

## 추천 시작값 / 조작값

- DNG Profile Editor / DNG Profile Editor의 Tone Curve를 linear로 설정해 카메라 전용 프로파일 생성 후 Lightroom에 가져오기: linear
- White Balance / 강한 색조가 있으면 선형 프로파일 전환 전에 화이트 밸런스를 확정: 원문 정성 표현(수치 추정 없음)
- Basic tone controls / 선형 프로파일에서 히스토그램을 보며 Exposure, Blacks, Whites를 조정하고 양 끝 클리핑을 피함: 원문 정성 표현(수치 추정 없음)
- Mask Tone Curve / 전체 이미지를 포함하는 Luminance Range Select All 마스크에 매끄러운 사용자 감마 커브 생성: 원문 정성 표현(수치 추정 없음)
- Custom gamma curve / 필름풍은 넓은 shoulder, 현대적 렌더링은 중간 회색 근처 피벗의 완만한 S-curve 사용: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 화이트 밸런스와 국소 노출 문제를 먼저 정리한 뒤 선형 프로파일로 전환한다.
- 히스토그램을 보며 Exposure, Blacks, Whites로 기본 분포를 잡는다.
- 전체 범위를 포함하는 Luminance Range 마스크에 부드러운 사용자 감마 커브를 만든다.
- 그 뒤 색 보정과 광원 재형성 마스크를 추가하고, 필요하면 감마 마스크를 스택 최상단에 다시 만들어 최종 변환처럼 작동시킨다.

## 주의할 점

- 선형 프로파일은 센서의 실제 다이내믹 레인지를 늘리지 않는다.
- Shadows와 Highlights를 과도하게 움직이면 인공적인 HDR 인상이 생긴다.
- 카메라별 프로파일이 필요하고 표준 프로파일보다 시간이 오래 걸리므로 최대 제어가 필요한 사진에 한정한다.
- 커브 제어점이 많거나 급격하면 그라데이션과 색 분리가 거칠어질 수 있다.

## 확실성과 근거

- 기본 프로파일의 내장 감마 커브를 제거한 평평한 출발점은 하이라이트 롤오프와 톤 반응을 직접 설계할 여지를 준다.
- 색 작업 위에 감마 커브를 적용하면 대비와 채도가 주로 중간톤에 자연스럽게 분배될 수 있다는 것이 저자의 설명이다.

저자 Vlad Moldovean이 자신의 Lightroom 처리 순서와 선형 프로파일 제작·적용 절차를 상세히 설명한 전문가 기고다. 효과 평가는 저자의 작업 경험에 근거하며 보편적 성능 보장은 아니다.

## 출처

- 원문 URL: https://petapixel.com/2026/06/14/how-to-leverage-linear-camera-profiles-in-your-editing-workflow/
- 접근일: 2026-08-10
