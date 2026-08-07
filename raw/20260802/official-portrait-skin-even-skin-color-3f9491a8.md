---
schema_version: '1.0'
scenario_id: raw-20260802-skinvariance01
title_ko: Facial Skin 마스크와 Color Variance로 얼룩진 홍조 완화
status: validated
source:
  type: official
  publisher: Adobe
  author: Seán Duggan
  url: https://www.adobe.com/learn/lightroom-cc/web/precise-color-adjustments
  published_at: '2026-03-18'
  accessed_at: '2026-08-02T00:00:00Z'
  original_language: en
device:
  capture_device: null
  editing_device: null
  software: Adobe Lightroom
scenario:
  subject: portrait-skin
  condition:
  - blotchy-skin
  - sunburn-redness
  intent:
  - even-skin-color
  - retain-natural-variation
method:
  steps:
  - tool: Masking > People > Facial Skin
    parameter: 얼굴 피부 선택
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color Eyedropper
    parameter: 어두운 붉은 피부와 밝은 하이라이트 사이의 중간색을 샘플링
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color
    parameter: Variance
    value: -50
    unit: slider value
    reported_as: exact
  - tool: Point Color
    parameter: Luminance 증가
    value: null
    unit: null
    reported_as: qualitative
  - tool: Point Color
    parameter: Saturation 몇 포인트 감소
    value: null
    unit: null
    reported_as: qualitative
rationale_ko:
- 피부 마스크 안에서 유사 색 편차를 줄이면 주변 색을 건드리지 않고 홍조를 완화할 수 있다.
collection:
  collector_version: 1.0.0
  content_sha256: 3f9491a862fc88c2827f15dcb9138ece7962e3379aafde96254d48e2c2e51a43
  collected_at: '2026-08-02T00:00:00Z'
---

# Facial Skin 마스크와 Color Variance로 얼룩진 홍조 완화

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

얼굴에 햇볕 화상이나 붉은 얼룩처럼 피부색 편차가 두드러질 때 자연스러운 변화를 남기면서 균일하게 보정한다.

## 촬영/작업 순서

1. Facial Skin 마스크를 만든다.
2. 중간 피부색을 샘플링한다.
3. Variance를 낮춰 홍조를 줄이고 밝기와 채도를 마무리한다.

## 추천 시작값 / 조작값

- Masking > People > Facial Skin / 얼굴 피부 선택: 원문 정성 표현(수치 추정 없음)
- Point Color Eyedropper / 어두운 붉은 피부와 밝은 하이라이트 사이의 중간색을 샘플링: 원문 정성 표현(수치 추정 없음)
- Point Color / Variance: -50 slider value
- Point Color / Luminance 증가: 원문 정성 표현(수치 추정 없음)
- Point Color / Saturation 몇 포인트 감소: 원문 정성 표현(수치 추정 없음)

## 보정 루틴

- 붉은 얼룩이 줄되 자연스러운 피부 변화가 남는 지점을 찾는다.
- 얼굴 밝기와 채도를 보완한 뒤 전후 비교한다.

## 주의할 점

- Variance를 지나치게 줄이면 피부 고유의 색 변화가 사라져 인공적으로 보인다.
- Facial Skin 마스크 범위를 확인한다.

## 확실성과 근거

- 피부 마스크 안에서 유사 색 편차를 줄이면 주변 색을 건드리지 않고 홍조를 완화할 수 있다.

Adobe 공식 튜토리얼이 예시 균형점으로 약 -50을 제시한다. 모든 인물에 대한 고정값이 아니라 해당 예시의 참고값이다.

## 출처

- 원문 URL: https://www.adobe.com/learn/lightroom-cc/web/precise-color-adjustments
- 접근일: 2026-08-02
