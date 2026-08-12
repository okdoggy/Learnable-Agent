---
schema_version: '1.0'
number: 16
technical_id: restrained-monochrome-tint
title_ko: 명도 구조를 보존하는 절제된 단색 tint
summary_ko: 명도 구조를 먼저 보존한 뒤 채도를 낮추고 한 가지 tint를 절제해 더하여 색 경쟁 없이 단색 분위기를 만드는 기술이다.
version: 0.1.0
status: candidate
supported_tools:
- lut
confidence: 0.68
raw_scenario_ids:
- raw-20260803-monotint01
source_urls:
- https://www.adobe.com/learn/lightroom-cc/web/adjust-photo-tone-with-color-grading
reviewed_at: '2026-08-09'
created_by: hermes-llm
---

# 명도 구조를 보존하는 절제된 단색 tint

명도 구조를 먼저 보존한 뒤 채도를 낮추고 한 가지 tint를 절제해 더하여 색 경쟁 없이 단색 분위기를 만드는 기술이다.

## 적용 조건

- 컬러 경쟁을 줄이고 명도 구조 중심의 단색·근단색 분위기를 만들 때 적용한다.
- 순수 중립 흑백보다 장면의 정서를 지지하는 약한 전역 tint가 필요한 인물·풍경·그래픽 사진에 적용한다.

## 기술 절차

1. 기본 노출과 화이트 밸런스를 정리하고 명도 구조를 확인한다.
2. 채도를 낮춰 색 경쟁을 제거하되 주요 피사체의 명도 분리를 보존한다.
3. 장면의 정서를 지지하는 한 가지 tint 방향을 낮은 강도로 더한다.
4. 전체 화면과 확대 화면에서 피부·재질·하이라이트가 진흙빛이나 물든 흰색처럼 보이지 않는지 확인한다.
5. 중립 흑백 변형과 tint 변형을 비교해 색조가 실제로 기여할 때만 유지한다.

## 파라미터 가이드

- 먼저 채도를 낮춰 명도 구조를 확인하고 tint 강도는 색 효과보다 피사체가 먼저 읽히는 최소 수준에서 시작한다.
- Remaster의 saturation·temperature·tint 또는 검증된 LUT로 실행하되 원문의 편집기 수치를 임의 변환하지 않는다.
- 검정·흰색 끝점과 주요 중간톤 디테일이 유지되는지 전후 비교한다.

## 판단 근거

- 단일 tint는 온냉 양극 분리와 다른 독립적 스타일 원리이며 Remaster와 LUT로 직접 실행할 수 있다.
- 색 경쟁을 줄이면서 순수 흑백과 다른 정서를 만드는 재사용 가치가 있다.
- 현재 독립 근거가 한 raw에 집중되어 active gate를 넘지 않으므로 candidate로 보존한다.

## 주의사항

- 채도를 완전히 제거한 뒤 강한 tint를 덮어 중요한 재질과 피부의 명도 분리를 잃지 않는다.
- 단일 색조가 검정·흰색 끝점이나 중간톤 대비를 가리는지 확인한다.
- 원문에 없는 색상·강도 수치를 만들지 않는다.

## 충돌 및 예외

- 피사체와 배경의 온냉 분리가 핵심인 사진에는 단일 tint보다 영역별 보색 분리가 더 적합하다.
- 제품 색상이나 피부색의 정확한 재현이 목적이면 단색화 자체가 부적합하다.

## raw 근거

- raw-20260803-monotint01
