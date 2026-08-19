# STAC Static Catalog json metadata 작성 지침

STAC Collection 또는 Item 메타데이터(JSON) 작성 지침이다.

- Static Catalog best practice를 따르는 것이 권장된다.
- relative asset href를 필수 적용한다.

## relative asset href 예시

Asset `href`는 Asset을 선언한 STAC JSON 파일을 기준으로 계산한다.

```text
collection.json  -> data/a.parquet     : "href": "data/a.parquet"
items/a.json     -> data/a.parquet     : "href": "../data/a.parquet"
```

## 체크리스트

STAC metadata(Collection 또는 Item)는 체크리스트의 조건을 모두 만족해야한다.

### 작성

- [ ] Dataset Repository 하나와 STAC Collection 하나가 대응한다.
- [ ] STAC JSON은 `process.py`가 자동 생성하지 않고 별도로 작성하거나 수정했다.
- [ ] placeholder, 예시 기본값, 임시 범위가 남아 있지 않다.

### 형식

- [ ] 모든 STAC JSON의 `stac_version`이 `1.1.0`이다.
- [ ] extension schema URL과 버전이 정확하다.
- [ ] 적용한 extension이 데이터 특성과 필드 의미에 맞다.

### 내용

- [ ] Collection에는 데이터셋의 공통 의미와 전체 범위만 기록했다.
- [ ] Item에는 개별 시공간 단위와 고유 정보만 기록했다.
- [ ] Asset에는 파일의 내용, 형식과 역할이 드러난다.
- [ ] 공간·시간 범위가 실제 데이터와 Item 범위를 포함한다.
- [ ] `providers`, `license`, 출처 Link가 확인한 근거와 맞다.
- [ ] 구조화할 수 있는 정보는 STAC core 또는 extension 필드에 기록했다.
- [ ] 알 수 없는 정보는 추정값으로 채우지 않고 한계로 기록했다.

### 경로와 링크

- [ ] 모든 Asset `href`가 Asset을 선언한 STAC JSON 파일 기준 상대 경로다.
- [ ] 모든 Asset 상대 경로가 실제 파일로 해석된다.
- [ ] Collection과 Item의 링크가 올바른 대상을 가리킨다.
- [ ] Link의 `rel`과 `type`이 대상의 관계와 media type에 맞다.

### 검증

- [ ] 인간 검토자가 STAC JSON과 대표 Asset을 함께 열어 확인했다.
- [ ] PySTAC schema 검증이 Collection과 연결된 모든 Item에서 통과한다.

## reference

- [STAC Specification](https://stacspec.org/en)
- [STAC Catalog and Collection Best Practices](https://github.com/radiantearth/stac-best-practices/blob/main/best-practices-catalog-and-collection.md)
- [STAC Extensions](https://stac-extensions.github.io/)
