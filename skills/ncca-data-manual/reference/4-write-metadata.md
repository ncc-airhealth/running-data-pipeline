# 4. STAC 메타데이터 작성·개선

데이터를 조사·검토하고 SpatioTemporal Asset Catalog(STAC) 메타데이터를 작성해요.
데이터 소비자가 데이터를 검색하고 적합성을 판단하며 올바르게 해석하는 데 필요한 정보를 기록하세요.

## 완료 조건

다음 조건을 모두 만족하면 STAC 메타데이터 작성이 끝나요.

- [ ] `data/collection.json`이 STAC 1.1.0과 사용한 Extension의 스키마를 통과함
- [ ] `scripts/review.py`가 데이터별 검증 항목을 통과함
- [ ] 데이터의 의미, 범위, 구조, 품질, 출처, 라이선스가 근거와 일치함
- [ ] 모든 데이터 파일이 Collection Asset 또는 Item Asset으로 참조됨
- [ ] Collection과 Item의 구조 링크 및 Asset 경로가 유효함
- [ ] 템플릿의 빈 값과 임시 값이 남아 있지 않음
- [ ] `scripts/review.py`와 `scripts/review.py.lock`으로 검증을 다시 실행할 수 있음

## 메타데이터 작성 규칙

다음 규칙에 따라 메타데이터를 작성하세요.

- [STAC 1.1.0](https://github.com/radiantearth/stac-spec/tree/v1.1.0)을 따르세요.
- [Static Catalog 권장 사항](https://github.com/radiantearth/stac-best-practices/blob/main/best-practices-catalog-and-collection.md)을 따르세요.
- 데이터와 메타데이터를 함께 옮길 수 있는 self-contained Static Catalog로 작성하세요.
- 루트 Collection에는 `self` 링크를 추가하지 마세요.
- `item`, `child`, `parent`, `root`, `collection` 구조 링크와 로컬 Asset 경로에는 상대 경로를 사용하세요.
- `license`, `via`, `derived_from` 등 외부 자료를 가리키는 링크에는 절대 URL을 사용할 수 있어요.
- Collection은 하나만 만들고 `data/collection.json`에 저장하세요.
- STAC Core 또는 `stac_extensions`에서 선언한 Extension의 필드만 사용하세요.
- 하나의 파일이나 하나의 논리 단위로 설명하는 데이터는 Collection Asset으로 참조하세요.
- 시간·공간 단위로 나뉜 데이터는 Item Asset으로 참조하고 Collection에서 각 Item을 연결하세요.
- Item JSON의 파일 이름은 [데이터 획득·처리 단계에서 정한 네이밍 컨벤션](3-etl.md#파일-네이밍-컨벤션)을 따르세요.

## 작업 순서

[완료 조건](#완료-조건)을 만족할 때까지 다음 단계를 반복하세요.

### 1. Extension 선정

[List of STAC Extensions](https://github.com/stac-extensions/stac-extensions.github.io/blob/main/README.md#list-of-stac-extensions)에서 데이터 유형에 맞는 Extension을 선택하세요.

> [!IMPORTANT]
> 다음 Extension을 데이터 유형에 맞게 사용하세요.
>
> - 공통: [processing](https://github.com/stac-extensions/processing), [file](https://github.com/stac-extensions/file)
> - GIS: [projection](https://github.com/stac-extensions/projection)
> - Tabular: [table](https://github.com/stac-extensions/table) (GIS Vector 데이터 포함)
> - Raster: [raster](https://github.com/stac-extensions/raster) 또는 [electro-optical](https://github.com/stac-extensions/eo)

### 2. 메타데이터 템플릿 준비

- [Collection JSON 메타데이터 템플릿](../assets/collection-template.json)을 복사하여 `data/collection.json`을 준비하세요.
- 데이터가 시간·공간 단위로 나뉘면 Item JSON도 준비하세요.
- 선택한 Extension의 스키마 URL을 `stac_extensions`에 추가하세요.
- 각 Extension의 공식 명세를 확인하고 필요한 필드를 추가하세요.

### 3. STAC 메타데이터 작성

- 준비한 Collection과 Item의 각 필드 값을 작성하세요.
- 공식 문서, 웹페이지, 연구 자료와 실제 데이터를 근거로 사용하세요.
- STAC 생성 코드가 있다면 Collection과 Item JSON을 직접 수정하지 마세요. 생성 코드를 수정한 뒤 메타데이터를 다시 생성하고 검증하세요.
- Asset의 파일 크기와 체크섬은 File Info Extension의 `file:size`와 `file:checksum`으로 기록하세요.

### 4. 데이터·메타데이터 검토

[데이터 검토 코드 예시](../assets/data-review-example.py)를 참고하여 `scripts/review.py`를 작성하세요.
예시의 `NotImplementedError`를 실제 데이터 검증 코드로 바꾼 뒤 실행하세요.
데이터 조사 결과를 메타데이터에 반영하고 [완료 조건](#완료-조건)을 만족할 때까지 검토를 반복하세요.

`scripts/review.py`에서 다음 항목을 검증해야 해요.

- 데이터 파일 누락, 스키마, 행 수, 중복, 결측, 값 범위, 시간·공간 범위 중 해당하는 항목
- STAC 1.1.0과 사용한 Extension의 스키마
- 모든 데이터 파일의 Collection Asset 또는 Item Asset 참조 여부
- Collection과 Item의 구조 링크 및 Asset 경로

PEP 723 형식으로 `scripts/review.py`의 의존성을 작성하세요.
`uv`로 의존성 lock 파일을 생성하고 잠긴 의존성으로 검토를 실행하세요.

```bash
uv lock --script scripts/review.py
uv lock --check --script scripts/review.py
uv run --frozen --script scripts/review.py
```

# AI 추가 지침

- 라이선스, 제공자 역할, 원본 출처가 불분명하면 임의로 작성하지 말고 사용자에게 근거를 요청하세요.
- 템플릿의 빈 값이나 데이터 파일 참조 누락이 있으면 이 단계를 완료로 판단하지 마세요.
- 파이프라인 실행 방법보다 데이터의 의미, 범위, 구조, 품질, 출처를 우선 기록하세요.
