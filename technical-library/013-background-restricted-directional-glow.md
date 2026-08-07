---
schema_version: '1.0'
number: 13
technical_id: background-restricted-directional-glow
title_ko: 피사체를 보호하는 배경 제한 방향성 글로우
summary_ko: 부드러운 글로우를 하늘·배경에만 배치하고 피사체를 보호해 실제 광원 방향과 맞는 역광 분리를 만든다.
version: 1.0.0
status: active
supported_tools:
- generate_ai
confidence: 0.9
raw_scenario_ids:
- raw-20260802-backglow01
- raw-20260803-subjectlight01
- raw-20260807-skybacklit
source_urls:
- https://fstoppers.com/education/how-make-your-subject-pop-using-lightroom-and-photoshop-902810
- https://fstoppers.com/lightroom/10-lightroom-secrets-will-change-how-edit-photos-901713
- https://www.adobe.com/learn/lightroom-cc/web/advanced-lightroom-masking
reviewed_at: '2026-08-07'
created_by: hermes-llm
---

# 피사체를 보호하는 배경 제한 방향성 글로우

부드러운 글로우를 하늘·배경에만 배치하고 피사체를 보호해 실제 광원 방향과 맞는 역광 분리를 만든다.

## 적용 조건

- 인물 뒤 배경이 평평하거나 실제 역광이 없어 피사체 분리를 위한 부드러운 광원 중심이 필요한 경우에 적용한다.
- 글로우가 피사체 표면을 평평하게 덮지 않고 하늘·배경 영역에만 머물러야 하는 경우에 적용한다.

## 기술 절차

1. 기존 광원 방향과 글로우가 있어야 할 배경 위치를 정한다.
2. 배경 또는 하늘에 부드러운 원형 광원 중심과 감쇠를 만든다.
3. 피사체 영역을 글로우 적용 범위에서 제외한다.
4. 필요하면 밝기·온기·약한 확산을 더해 실제 역광처럼 보이게 한다.
5. 피사체 경계의 wraparound 효과, halo, 씻긴 디테일을 확대와 전체 화면에서 확인한다.

## 파라미터 가이드

- 정확한 밝기·색·Dehaze 수치는 원문에 없으므로 실제 광원처럼 보이는 최소 강도로 조절한다.
- 피사체 보호를 우선하고 글로우 중심에서 바깥으로 부드럽게 감쇠시킨다.
- 색은 장면의 기존 광원과 화이트 밸런스에 맞춘다.

## 판단 근거

- Adobe 공식의 Subject 제외 Radial Gradient와 Fstoppers의 Sky 교차 역광 사례가 배경 제한 글로우 원리를 독립적으로 뒷받침한다.
- 피사체 분리 효과가 크고 Generate AI lighting-weather로 직접 실행 가능하며, 피사체 위 번짐이라는 대표 실패를 예방한다.

## 주의사항

- 글로우가 피사체 얼굴과 의상 위에 덮이면 디테일과 대비가 씻겨 나간다.
- 기존 그림자와 모순되는 위치·색의 인공 광원을 만들지 않는다.
- Dehaze 감소와 밝기 상승을 과도하게 사용하면 회색 안개 띠와 클리핑이 생길 수 있다.

## 충돌 및 예외

- 이미 강한 실제 역광과 lens flare가 있는 장면에는 추가 글로우가 중복되어 부자연스러울 수 있다.

## raw 근거

- raw-20260802-backglow01
- raw-20260807-skybacklit
- raw-20260803-subjectlight01
