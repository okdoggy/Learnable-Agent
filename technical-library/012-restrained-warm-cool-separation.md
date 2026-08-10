---
schema_version: '1.0'
number: 12
technical_id: restrained-warm-cool-separation
title_ko: 피부와 광원 관계를 보존하는 절제된 온냉 색 분리
summary_ko: 기본 색을 안정시킨 뒤 피사체·배경·명도 영역 또는 국소 광원에 따뜻함과 차가운 보색을 절제해 배치하고 보호 영역과 광원 방향을 검증한다.
version: 1.0.2
status: active
supported_tools:
- remaster
- lut
- generate_ai
confidence: 0.95
raw_scenario_ids:
- raw-20260802-vintageback01
- raw-20260802-warmlight01
- raw-20260803-complementgrade01
- raw-20260809-complementgrade
- raw-20260810-warmwin
source_urls:
- https://fstoppers.com/education/how-color-grade-photos-lightroom-using-complementary-colors-902459
- https://fstoppers.com/education/how-edit-portrait-skin-tones-lightroom-902830
- https://fstoppers.com/education/how-get-natural-looking-studio-light-901630
- https://www.adobe.com/learn/lightroom-cc/web/correct-white-balance
reviewed_at: '2026-08-10'
created_by: hermes-llm
---

# 피부와 광원 관계를 보존하는 절제된 온냉 색 분리

기본 색을 안정시킨 뒤 피사체·배경·명도 영역 또는 국소 광원에 따뜻함과 차가운 보색을 절제해 배치하고 보호 영역과 광원 방향을 검증한다.

## 적용 조건

- 피사체와 배경 또는 하이라이트와 그림자 사이에 따뜻함·차가움의 색 분리를 만들어 깊이를 강화할 때 적용한다.
- 중립 교정 후 보색 그레이드나 촬영된 혼합 색온도를 보존·강화할 때 적용한다.
- 차가운 황혼 건축의 창문처럼 제한된 영역에 따뜻한 광원을 만들고 주변의 차가운 분위기를 보존할 때 적용한다.

## 기술 절차

1. 노출과 기본 화이트 밸런스를 먼저 안정시키되 의도적인 혼합 색온도는 보존한다.
2. 피사체와 배경, 명도 영역 또는 국소 광원별로 따뜻한 색과 차가운 보색의 역할을 정한다.
3. 피부·주요 피사체·창문 등 목표 영역만 따뜻하게 하고 배경·그림자는 상대적으로 차갑게 유지한다.
4. 국소 광원은 영역을 정확히 제한하고 밝기와 색온도를 함께 조절해 실제 발광 관계를 만든다.
5. 서로 다른 변형을 보존하고 휴식 후 비교해 가장 절제된 적합안을 고른다.
6. 전체 화면과 경계 확대에서 색 효과가 피사체보다 먼저 보이지 않고 주변으로 번지지 않는지 검증한다.

## 파라미터 가이드

- 2700 K 키 라이트와 5600 K 카메라 화이트 밸런스는 특정 촬영 사례이며 후처리 고정값으로 환산하지 않는다.
- LUT와 색온도 조정은 낮은 강도에서 시작해 피부·중립색·광원 방향을 확인하며 올린다.
- 30분 휴식은 한 보색 그레이딩 사례의 최소값으로만 보존한다.
- 황혼 창문 사례의 Temp·Tint·Exposure는 수치가 없으므로 주변 외벽과 하늘이 변하지 않고 내부 발광으로 읽히는 최소 강도로 결정한다.

## 판단 근거

- 촬영 단계의 혼합 색온도, 배경 국소 냉각, 톤 영역별 보색 그레이드가 같은 깊이 원리를 독립적으로 뒷받침한다.
- 새 Adobe 공식 근거는 인물 외에도 차가운 건축 환경 속 제한된 따뜻한 광원으로 원리가 재사용됨을 보강한다.
- LUT·Remaster·Generate AI로 실행 가능하고 인물·스튜디오·풍경·건축에 재사용성이 높다.

## 주의사항

- 피부색을 차갑게 오염시키거나 경계에 색 띠를 만들지 않는다.
- 자동 화이트 밸런스로 의도적인 혼합 색온도까지 상쇄하지 않는다.
- 보색 채도를 과도하게 높이거나 특정 조합을 모든 사진에 강제하지 않는다.
- 창문 국소광이 창틀·벽·하늘로 새거나 주변 조명과 모순되는 밝기를 만들지 않는다.

## 충돌 및 예외

- 흑백에 가까운 단일 tint 의도에서는 온냉 양극 분리보다 낮은 채도의 전역 색조가 더 적합하다.
- 실제 주변광이 따뜻한 장면에서는 차가운 배경을 억지로 만들지 않는다.

## raw 근거

- raw-20260802-vintageback01
- raw-20260802-warmlight01
- raw-20260803-complementgrade01
- raw-20260809-complementgrade
- raw-20260810-warmwin
