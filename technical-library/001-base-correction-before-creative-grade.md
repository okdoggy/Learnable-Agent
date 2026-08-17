---
schema_version: '1.0'
number: 1
technical_id: base-correction-before-creative-grade
title_ko: 창의적 색보정 전 기본 노출·화이트 밸런스 안정화
summary_ko: 편집 의도를 먼저 정하고 기본 노출·화이트 밸런스·톤을 안정시킨 뒤 창의적 색보정을 적용하며, 변형 저장과 휴식 후 비교로 색 피로와 무작위 보정을 줄인다.
version: 1.0.1
status: active
supported_tools:
- lut
confidence: 0.93
raw_scenario_ids:
- raw-20260803-complementgrade01
- raw-20260804-filmpreset01
- raw-20260805-intentedit01
- raw-20260807-editplan01
- raw-20260807-etherealedit01
- raw-20260807-exposurewb
- raw-20260809-complementgrade
- raw-20260809-fivepassedit
source_urls:
- https://fstoppers.com/education/how-color-grade-photos-lightroom-using-complementary-colors-902459
- https://fstoppers.com/education/how-make-digital-photos-look-film-lightroom-902358
- https://fstoppers.com/education/lightroom-settings-behind-hazy-ethereal-photography-style-901341
- https://fstoppers.com/education/stop-guessing-lightroom-and-start-editing-plan-901827
- https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
reviewed_at: '2026-08-09'
created_by: hermes-llm
---

# 창의적 색보정 전 기본 노출·화이트 밸런스 안정화

편집 의도를 먼저 정하고 기본 노출·화이트 밸런스·톤을 안정시킨 뒤 창의적 색보정을 적용하며, 변형 저장과 휴식 후 비교로 색 피로와 무작위 보정을 줄인다.

## 적용 조건

- 저노출 또는 화이트 밸런스가 불안정한 사진을 창의적 색보정·필름풍·몽환적 스타일로 마무리할 때 적용한다.
- 프리셋과 슬라이더를 무작위로 시험해 결과가 일관되지 않거나 색 적응 때문에 과보정하기 쉬운 작업에 적용한다.

## 기술 절차

1. 최종 결과가 전달할 감정과 방향을 먼저 정한다.
2. 저노출이면 노출을 먼저 회복하고, 기본 노출과 화이트 밸런스를 안정시킨다.
3. 하이라이트·그림자·검정·흰색의 기본 톤 관계를 정리한다.
4. 그 뒤 LUT 또는 색보정으로 창의적 분위기를 더하고 변형을 보존한다.
5. 전후 비교와 휴식 후 재검토로 과보정을 확인하고 강도를 미세 조정한다.

## 파라미터 가이드

- 노출과 화이트 밸런스는 고정 수치를 만들지 말고 주요 피사체와 중간톤이 읽히는 지점에서 결정한다.
- LUT나 스타일 강도는 장면 고유의 색과 명암이 유지되는 범위에서 낮게 시작한다.
- 30분 휴식은 한 근거가 제시한 최소 재평가 시간이며 모든 작업의 절대 규칙으로 일반화하지 않는다.

## 판단 근거

- 기본 교정과 창의적 그레이드를 분리하면 노출·색 편향을 스타일로 잘못 보상하는 실패를 줄인다.
- 서로 다른 출처에서 편집 의도 선행, 기본 교정, 단계적 색보정, 휴식 후 비교가 반복되어 재사용성이 높다.
- Remaster와 LUT의 실행 순서로 직접 연결할 수 있다.

## 주의사항

- 저노출 파일의 노출 회복에서 하이라이트 클리핑과 노이즈 증가를 확인한다.
- 화이트 밸런스와 기본 톤이 불안정한 상태에서 LUT 강도만 높이지 않는다.
- 예시의 따뜻한 밝은 영역과 푸른 그림자를 모든 사진에 강제하지 않는다.

## 충돌 및 예외

- 저노출 RAW에서는 색 판단 자체가 어둠에 왜곡되므로 노출을 화이트 밸런스보다 먼저 판단한다.
- 사진의 기존 팔레트와 빛이 의도한 스타일을 지지하지 않으면 효과를 축소하거나 적용하지 않는다.

## raw 근거

- raw-20260807-exposurewb
- raw-20260803-complementgrade01
- raw-20260807-etherealedit01
- raw-20260804-filmpreset01
- raw-20260805-intentedit01
- raw-20260807-editplan01
- raw-20260809-complementgrade
- raw-20260809-fivepassedit
