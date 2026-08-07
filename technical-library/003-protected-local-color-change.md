---
schema_version: '1.0'
number: 3
technical_id: protected-local-color-change
title_ko: 공간·색 교차 선택과 보호 영역을 이용한 국소 색 교체
summary_ko: 대상의 공간적 선택과 색 범위를 교차하고 피부·배경의 동색 영역을 제외해 특정 물체의 색만 안전하게 바꾼다.
version: 1.0.0
status: active
supported_tools:
- generate_ai
confidence: 0.88
raw_scenario_ids:
- raw-20260802-subjectcolor01
- raw-20260806-hueexclude01
source_urls:
- https://www.adobe.com/learn/lightroom-cc/web/advanced-lightroom-masking
- https://www.adobe.com/learn/photoshop/web/edit-photos-adjustment-layers
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 공간·색 교차 선택과 보호 영역을 이용한 국소 색 교체

대상의 공간적 선택과 색 범위를 교차하고 피부·배경의 동색 영역을 제외해 특정 물체의 색만 안전하게 바꾼다.

## 적용 조건

- 의상·장비·배경에 같은 계열 색이 반복되지만 그중 특정 대상의 색만 바꿔야 할 때 적용한다.
- 피부나 주변 물체의 동색 영역을 보호하면서 국소 색을 교체할 때 적용한다.

## 기술 절차

1. 먼저 색을 바꿀 대상의 공간적 영역을 선택한다.
2. 그 영역 안에서 목표 색 범위를 다시 제한해 교집합을 만든다.
3. 색상·채도·명도를 조정해 목표 색으로 이동한다.
4. 피부·손·배경처럼 같은 색이지만 보호해야 하는 영역은 제외한다.
5. 전체 화면과 확대 화면에서 경계, 반사광, 재질감이 자연스러운지 확인한다.

## 파라미터 가이드

- 색 교체량은 목표 색이 자연스럽게 보이는 범위에서 조절하고 피부색과 배경색의 불변성을 우선한다.
- 선택 범위는 대상의 공간적 범위와 색상 범위의 교집합으로 좁힌다.
- 원문에 고정 Hue 수치가 없으므로 장면별 정성 방향으로 결정한다.

## 판단 근거

- Lightroom의 Subject와 Color Range 교차 및 Photoshop의 Hue/Saturation 마스크 사례가 같은 원리를 독립적으로 보여 준다.
- 색상만 기준으로 한 전역 변경의 대표적 실패를 방지하며 의상·제품·그래픽 편집에 재사용성이 높다.
- Generate AI의 precise-object-edit로 대상과 보호 영역을 동시에 명시해 실행할 수 있다.

## 주의사항

- 색 범위만으로 선택하면 피부나 배경의 같은 색까지 함께 바뀔 수 있다.
- 공간 선택만으로는 대상 내부의 다른 색까지 영향을 받을 수 있으므로 두 조건을 함께 확인한다.
- 경계의 잔색과 반사광이 새 색과 모순되지 않는지 점검한다.

## 충돌 및 예외

- 조명색이나 반사로 생긴 자연스러운 색 변이까지 완전히 균일화하면 재질과 입체감이 사라질 수 있다.

## raw 근거

- raw-20260802-subjectcolor01
- raw-20260806-hueexclude01
