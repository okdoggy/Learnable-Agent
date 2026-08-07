---
schema_version: '1.0'
number: 7
technical_id: diagnostic-tonal-shaping-and-endpoints
title_ko: 명도 진단과 끝점 확인을 통한 선택적 톤 설계
summary_ko: 색을 잠시 배제한 명도 진단과 클리핑 확인으로 톤 문제를 찾고, 필요한 명도 구간에만 대비를 재구축하거나 압축한다.
version: 1.0.0
status: active
supported_tools:
- remaster
confidence: 0.9
raw_scenario_ids:
- raw-20260807-endclip12
- raw-20260807-harshskin01
- raw-20260807-lrvhelp01
- raw-20260807-tonerebuild01
source_urls:
- https://fstoppers.com/education/lightrooms-tone-curve-explained-every-trick-need-know-902177
- https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
- https://petapixel.com/2025/05/18/5-advanced-lightroom-techniques-to-change-how-you-see-and-edit-photos/
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 명도 진단과 끝점 확인을 통한 선택적 톤 설계

색을 잠시 배제한 명도 진단과 클리핑 확인으로 톤 문제를 찾고, 필요한 명도 구간에만 대비를 재구축하거나 압축한다.

## 적용 조건

- 전역 Contrast만으로 원하는 명도 구간을 통제하기 어렵거나 검정·흰색 끝점이 불명확한 사진에 적용한다.
- 색이 강해 명도 불균형을 판단하기 어려운 사진에 적용한다.

## 기술 절차

1. 기본 노출을 정리한 뒤 필요하면 임시 흑백 진단으로 색 지각의 영향을 제거한다.
2. 히스토그램과 화면에서 검정·흰색 끝점 및 명도 불균형을 확인한다.
3. 필요한 명도 구간만 곡선 또는 하이라이트·그림자 조정으로 재구성한다.
4. 이미 대비가 강한 영역은 하이라이트를 낮추고 그림자를 올려 압축한다.
5. 진단 보기를 해제하고 최종 색·명암·중요 디테일을 다시 확인한다.

## 파라미터 가이드

- 전체 이미지 Saturation -100과 진단 프리셋 Amount 200%는 해당 Lightroom 진단 사례의 값이다.
- 검정·흰색 끝점의 약 1~2% 클리핑은 근거가 제시한 시작점이며 중요한 하이라이트·암부가 있으면 더 보수적으로 조정한다.
- 곡선 좌표와 Amount 수치는 원문에 없으므로 명도 구간과 피사체 구조를 보며 정성적으로 결정한다.

## 판단 근거

- PetaPixel의 흑백 명도 진단과 Fstoppers의 끝점 미리보기·Tone Curve 사례가 진단 후 조정 원칙을 독립적으로 뒷받침한다.
- 눈대중 전역 Contrast의 실패를 줄이고 Remaster의 명도 파라미터 선택을 더 일관되게 만든다.

## 주의사항

- 흑백 진단 화면은 점검용이며 최종 색 결과를 대체하지 않는다.
- 1~2% 클리핑은 절대 규칙이 아니라 중요 디테일을 보존하는 조건 아래의 시작점이다.
- 역 S-curve나 평탄화를 과도하게 적용하면 입체감과 생동감이 사라질 수 있다.

## 충돌 및 예외

- 평평한 시작 이미지에는 선택적 대비 재구축이 필요하지만 이미 거친 한낮 피부에는 일반 S-curve 대신 대비 압축이 필요하다.

## raw 근거

- raw-20260807-lrvhelp01
- raw-20260807-tonerebuild01
- raw-20260807-endclip12
- raw-20260807-harshskin01
