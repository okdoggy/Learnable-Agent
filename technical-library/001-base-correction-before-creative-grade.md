---
schema_version: '1.0'
number: 1
technical_id: base-correction-before-creative-grade
title_ko: 창의적 색보정 전 기본 노출·화이트 밸런스 안정화
summary_ko: 창의적 LUT나 스타일 보정 전에 노출·화이트 밸런스·기본 톤을 안정시키고, 저노출에서는 노출을 먼저 판단해 색 오판을 줄이는 순서 기술이다.
version: 1.0.0
status: active
supported_tools:
- remaster
- lut
confidence: 0.9
raw_scenario_ids:
- raw-20260803-complementgrade01
- raw-20260804-filmpreset01
- raw-20260805-intentedit01
- raw-20260807-editplan01
- raw-20260807-etherealedit01
- raw-20260807-exposurewb
source_urls:
- https://fstoppers.com/education/how-color-grade-photos-lightroom-using-complementary-colors-902459
- https://fstoppers.com/education/how-make-digital-photos-look-film-lightroom-902358
- https://fstoppers.com/education/lightroom-settings-behind-hazy-ethereal-photography-style-901341
- https://fstoppers.com/education/stop-guessing-lightroom-and-start-editing-plan-901827
- https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 창의적 색보정 전 기본 노출·화이트 밸런스 안정화

창의적 LUT나 스타일 보정 전에 노출·화이트 밸런스·기본 톤을 안정시키고, 저노출에서는 노출을 먼저 판단해 색 오판을 줄이는 순서 기술이다.

## 적용 조건

- 저노출이거나 화이트 밸런스가 불안정한 RAW를 창의적 색보정·필름풍·몽환적 스타일로 마무리할 때 적용한다.
- 여러 사진에 일관된 룩을 적용하되 장면별 노출과 색 편차가 있는 경우에 적용한다.

## 기술 절차

1. 편집 의도와 최종 분위기를 먼저 문장으로 정한다.
2. 저노출이면 노출을 먼저 회복해 실제 색을 판단할 수 있게 하고, 그 밖의 경우에도 기본 노출과 화이트 밸런스를 먼저 안정시킨다.
3. 하이라이트·그림자·검정·흰색의 기본 톤 관계를 정리한다.
4. 그 뒤 LUT 또는 색보정으로 창의적 분위기를 더한다.
5. 전후 비교와 휴식 후 재검토로 색 적응과 과보정을 확인하고 장면별로 강도를 미세 조정한다.

## 파라미터 가이드

- 노출과 화이트 밸런스는 고정 수치를 만들지 말고 주요 피사체와 중간톤이 읽히는 지점에서 결정한다.
- LUT나 스타일 강도는 장면 고유의 색과 명암이 유지되는 범위에서 낮게 시작해 올린다.
- 원문이 제시한 특정 프리셋 방향은 장면별 출발점이며 모든 사진에 동일한 수치로 고정하지 않는다.

## 판단 근거

- 기본 교정과 창의적 그레이드를 분리하면 노출·색 편향을 스타일로 잘못 보상하는 실패를 줄인다.
- 서로 다른 기사와 작업 흐름에서 기본 노출·화이트 밸런스 선행과 장면별 프리셋 조정이 반복되어 재사용 가치가 높다.
- Remaster와 LUT의 실행 순서로 직접 연결할 수 있다.

## 주의사항

- 저노출 파일에서 노출을 올릴 때 하이라이트 클리핑과 노이즈 증가를 함께 확인한다.
- 화이트 밸런스와 기본 톤이 불안정한 상태에서 LUT 강도만 높이면 색 편향과 대비 문제가 확대될 수 있다.
- 프리셋이나 LUT는 완성값이 아니라 장면별 미세 조정의 출발점으로 사용한다.

## 충돌 및 예외

- 일반적인 순서는 기본 노출과 화이트 밸런스를 창의적 그레이드보다 먼저 정리하는 것이지만, 저노출 RAW에서는 색 판단 자체가 어둠에 왜곡되므로 노출을 화이트 밸런스보다 먼저 판단한다.

## raw 근거

- raw-20260807-exposurewb
- raw-20260803-complementgrade01
- raw-20260807-etherealedit01
- raw-20260804-filmpreset01
- raw-20260805-intentedit01
- raw-20260807-editplan01
