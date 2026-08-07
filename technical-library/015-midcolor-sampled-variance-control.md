---
schema_version: '1.0'
number: 15
technical_id: midcolor-sampled-variance-control
title_ko: 중간색 샘플 기반 유사 색 편차 제어
summary_ko: 공간 영역을 제한한 뒤 목표 색 범위의 중간색을 샘플링하고 색 편차를 줄이거나 늘려 통일감과 대비를 제어한다.
version: 0.1.0
status: candidate
supported_tools:
- generate_ai
confidence: 0.74
raw_scenario_ids:
- raw-20260802-pointcolor01
- raw-20260802-skinvariance01
- raw-20260802-skyvariance01
source_urls:
- https://www.adobe.com/learn/lightroom-cc/web/precise-color-adjustments
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 중간색 샘플 기반 유사 색 편차 제어

공간 영역을 제한한 뒤 목표 색 범위의 중간색을 샘플링하고 색 편차를 줄이거나 늘려 통일감과 대비를 제어한다.

## 적용 조건

- 하늘·피부·소품처럼 유사 색 안의 편차를 줄이거나 반대로 차이를 강조해야 할 때 적용한다.
- 다른 영역을 건드리지 않고 목표 영역의 색 통일감만 조정해야 할 때 적용한다.

## 기술 절차

1. 먼저 색 편차를 조정할 공간 영역을 제한한다.
2. 목표 색 범위의 어두운 값과 밝은 값 사이 중간색을 샘플링한다.
3. 통일이 목적이면 색 편차를 줄이고, 재질·대비 강조가 목적이면 편차를 늘린다.
4. 필요하면 밝기와 채도를 소폭 보완한다.
5. 자연스러운 색 변화와 재질감이 남았는지 전후 비교한다.

## 파라미터 가이드

- 중간색은 목표 범위의 어두운 색과 밝은 색 사이에서 샘플링한다.
- 피부 Variance -50은 한 Adobe 예시의 균형점이며 모든 이미지의 고정값이 아니다.
- 하늘과 일반 소품의 Variance 방향은 통일하려면 감소, 차이를 강조하려면 증가로 사용하되 고정 수치는 만들지 않는다.

## 판단 근거

- Adobe 공식 튜토리얼이 일반 소품·편광 하늘·얼룩진 피부에 같은 중간색 샘플링과 Variance 원리를 적용한다.
- 색 균일화의 재사용성과 과도한 평탄화 방지 가치가 높다.
- 다만 세 raw가 한 원문 계열에 집중되고 지원 도구가 Variance 슬라이더를 직접 노출하지 않으므로 candidate로 보존한다.

## 주의사항

- Variance를 과도하게 줄이면 피부·하늘·재질의 자연스러운 색 변화가 사라진다.
- 중간색이 아닌 극단 색을 샘플링하면 목표 범위가 한쪽으로 치우칠 수 있다.
- 공간 마스크 없이 사용하면 주변의 유사 색도 함께 바뀔 수 있다.

## 충돌 및 예외

- 색 차이가 조명 방향과 재질을 설명하는 핵심 단서라면 통일보다 보존 또는 강조가 적합하다.

## raw 근거

- raw-20260802-pointcolor01
- raw-20260802-skyvariance01
- raw-20260802-skinvariance01
