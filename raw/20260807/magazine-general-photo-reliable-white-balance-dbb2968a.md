---
schema_version: '1.0'
scenario_id: raw-20260807-exposurewb
title_ko: 저노출 RAW는 화이트 밸런스보다 노출을 먼저 교정
status: validated
source:
  type: magazine
  publisher: Fstoppers
  author: Alex Cooke
  url: https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
  published_at: '2026-04-18'
  accessed_at: '2026-08-07T00:00:00Z'
  original_language: en
device:
  capture_device: Leica camera (demonstrated example)
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: general-photo
  condition:
  - underexposed-raw
  - misleading-color-at-low-exposure
  intent:
  - reliable-white-balance
  - correct-global-exposure
  - avoid-color-misjudgment
method:
  steps:
  - tool: Lightroom Exposure
    parameter: 화이트 밸런스를 판단할 수 있을 정도로 전체 노출을 먼저 교정
    value: null
    unit: null
    reported_as: qualitative
  - tool: Lightroom White Balance
    parameter: 노출 교정 후 Temperature와 Tint로 화이트 밸런스 판단
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 저노출 상태에서는 색의 외관이 어둠의 영향을 받아 화이트 밸런스 판단이 왜곡될 수 있다.
- 적정 밝기를 먼저 확보하면 색온도와 색조의 실제 편향을 더 의미 있게 평가할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: dbb2968a67ee8f80f778a051d6c134803cc4eae606aab762aff8a5822f1e302f
  collected_at: '2026-08-07T00:00:00Z'
---

# 저노출 RAW는 화이트 밸런스보다 노출을 먼저 교정

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

저노출 RAW의 색이 이상해 보여 화이트 밸런스를 바로 움직이고 싶지만, 어두운 밝기 자체가 색 판단을 흐릴 수 있는 상황에 사용한다.

## 촬영/작업 순서

1. 원본이 어두운 상태에서는 화이트 밸런스 결정을 보류한다.
2. Exposure를 먼저 올려 장면의 실제 톤과 색이 읽히도록 한다.
3. 그 다음 Temperature와 Tint를 조정한다.
4. 노출과 화이트 밸런스를 함께 다시 확인하되 순서는 노출 판단을 우선한다.

## 추천 시작값 / 조작값

- Lightroom Exposure / 화이트 밸런스를 판단할 수 있을 정도로 전체 노출을 먼저 교정: 원문 정성 표현(수치 추정 없음)
- Lightroom White Balance / 노출 교정 후 Temperature와 Tint로 화이트 밸런스 판단: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 먼저 전체 Exposure를 조정해 장면의 주요 피사체와 중간톤이 판단 가능한 밝기가 되게 한다.
- 밝기가 안정된 뒤 Temperature와 Tint를 살펴 실제 색편향과 의도한 분위기를 구분한다.
- 화이트 밸런스를 조정한 뒤 노출이 다시 부자연스러워 보이는지 왕복 검토한다.

## 주의할 점

- 어두운 상태에서 색감을 먼저 판단하면 실제보다 차갑거나 따뜻하다고 오판할 수 있다.
- 노출을 먼저 올릴 때 하이라이트 클리핑과 노이즈 증가를 함께 확인한다.
- 노출 보정 뒤에도 중립 기준이 없는 장면은 화이트 밸런스를 장면 의도와 피부색 등으로 교차 검토한다.

## 확실성과 근거

- 저노출 상태에서는 색의 외관이 어둠의 영향을 받아 화이트 밸런스 판단이 왜곡될 수 있다.
- 적정 밝기를 먼저 확보하면 색온도와 색조의 실제 편향을 더 의미 있게 평가할 수 있다.

Fstoppers 기사에서 Serge Ramelli가 저노출 Leica 파일을 예로 들어 노출을 먼저 맞춘 뒤 화이트 밸런스를 판단하는 순서를 직접 시연한다. 기사에는 이 단계의 고정 수치가 없으므로 모든 값은 정성 단계로 기록했다.

## 출처

- 원문 URL: https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
- 접근일: 2026-08-07
