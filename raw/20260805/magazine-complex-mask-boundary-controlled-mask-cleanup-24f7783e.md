---
schema_version: '1.0'
scenario_id: raw-20260805-brushcontrol01
title_ko: Flow·Density·중앙 샘플을 구분해 마스크 경계 정리
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke; Mickey Pullen
  url: https://fstoppers.com/lightroom/intersect-masks-control-youre-missing-lightroom-721432
  published_at: '2026-01-07'
  accessed_at: '2026-08-05T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: complex-mask-boundary
  condition:
  - mask-edge-gaps
  - local-dodge-burn
  intent:
  - controlled-mask-cleanup
  - natural-local-adjustment
method:
  steps:
  - tool: Lightroom Masking Brush Flow
    parameter: 반복 획에서 보정이 쌓이는 속도는 Flow로 조절
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking Brush Density
    parameter: 반복해 칠해도 적용될 최대 강도는 Density로 제한
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking Brush Feather
    parameter: 자연스러운 dodge and burn에는 부드럽고 점진적인 브러시를 사용
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Auto Mask
    parameter: Auto Mask에서 중앙 샘플 지점을 목표 색과 경계 안쪽에 유지
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom Masking Brush
    parameter: 고립된 빈틈은 클릭, 직선은 shift-click, 곡선은 짧은 구간으로 정리
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- Flow는 누적 속도, Density는 최대 강도를 제어하므로 둘을 구분하면 반복 획으로 생기는 과도한 밝기 패치를 줄일 수 있다.
- 자동 또는 그라디언트 마스크의 큰 구조를 유지한 채 브러시를 경계 청소에만 쓰면 수작업 면적과 오류를 줄일 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 24f7783ee2862640ae54105ca3b296771b1f0125a5ca803137316129c55dabc9
  collected_at: '2026-08-05T00:00:00Z'
---

# Flow·Density·중앙 샘플을 구분해 마스크 경계 정리

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

자동 마스크나 그라디언트는 대체로 맞지만 나뭇가지 같은 복잡한 경계에 작은 빈틈과 번짐이 남고, 브러시 dodge and burn이 얼룩처럼 쌓일 때 사용한다.

## 촬영/작업 순서

1. 자동 선택이나 그라디언트로 큰 마스크 구조를 먼저 만든다.
2. 부드럽게 누적되는 브러시와 단단한 수정용 브러시의 동작을 구분해 준비한다.
3. Auto Mask의 중앙 샘플 지점을 목표 영역 안에 유지하며 작은 빈틈만 정리한다.
4. 직선과 곡선의 형태에 맞춰 클릭과 짧은 구간을 사용한다.
5. 확대와 전체 화면을 오가며 경계와 자연스러운 누적을 검사한다.

## 추천 시작값 / 조작값

- Lightroom Masking Brush Flow / 반복 획에서 보정이 쌓이는 속도는 Flow로 조절: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking Brush Density / 반복해 칠해도 적용될 최대 강도는 Density로 제한: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking Brush Feather / 자연스러운 dodge and burn에는 부드럽고 점진적인 브러시를 사용: 원문 정성 표현(수치 추정 없음)
- Lightroom Auto Mask / Auto Mask에서 중앙 샘플 지점을 목표 색과 경계 안쪽에 유지: 원문 정성 표현(수치 추정 없음)
- Lightroom Masking Brush / 고립된 빈틈은 클릭, 직선은 shift-click, 곡선은 짧은 구간으로 정리: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- Exposure를 일시적으로 과장하거나 오버레이를 켜 브러시 전환과 경계를 검사한다.
- 고립된 빈틈은 드래그보다 클릭으로 메우고 직선은 shift-click 구간으로, 곡선은 짧은 구간의 연속으로 정리한다.
- 확대 경계 검사 뒤 실제 보정 강도로 되돌려 얼룩과 패치가 보이지 않는지 확인한다.

## 주의할 점

- Flow와 Density를 같은 의미로 취급하지 않는다.
- Auto Mask에서는 브러시 원 전체가 아니라 중앙 샘플 지점이 선택을 이끄므로 중앙을 잘못 놓으면 마스크가 번질 수 있다.
- 곡선 경계를 긴 한 번의 획으로 따라가면 누출과 울퉁불퉁한 경계가 생기기 쉽다.

## 확실성과 근거

- Flow는 누적 속도, Density는 최대 강도를 제어하므로 둘을 구분하면 반복 획으로 생기는 과도한 밝기 패치를 줄일 수 있다.
- 자동 또는 그라디언트 마스크의 큰 구조를 유지한 채 브러시를 경계 청소에만 쓰면 수작업 면적과 오류를 줄일 수 있다.

출처가 Flow와 Density의 차이, Feather 비교, Auto Mask 중앙 샘플, 클릭·shift-click·짧은 구간 사용법을 직접 설명한다. 특정 권장 수치는 제시하지 않아 정성 단계로 기록했다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/intersect-masks-control-youre-missing-lightroom-721432
- 접근일: 2026-08-05
