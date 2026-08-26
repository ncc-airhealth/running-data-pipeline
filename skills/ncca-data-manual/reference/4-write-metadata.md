# 4. 메타데이터 작성·개선

데이터에 대해 조사⋅검토하고 STAC 메타데이터를 기록해주세요.

## 완료 조건

다음의 조건들을 모두 만족하는 경우, [README 작성·개선](reference/5-write-dataset-card.md)으로 넘어갑니다.

- [ ] `data/collection.json`이 작성되어 있다.
- [ ] 데이터에 대한 모든 암묵지가 STAC 메타데이터에 반영되어 있다.
- [ ] STAC Static Metadata가 유효하다.

## 메타데이터 작성 규칙

현재 다루는 데이터셋에 대한 정보를 일관성 있게 관리하기 위해 [STAC](https://stacspec.org/)을 기반으로 메타데이터를 작성합니다.STAC 메타데이터 작성 세부 규칙은 다음과 같습니다.

- [STAC 1.1.0](https://github.com/radiantearth/stac-spec/tree/v1.1.0) 을 따른다.
- [Static Catalogs](https://github.com/radiantearth/stac-spec/blob/v1.1.0/best-practices.md#static-catalogs) 방식으로 `data/` 경로에 JSON으로 저장한다.
- [Self-contained with Assets](https://github.com/radiantearth/stac-spec/blob/v1.1.0/best-practices.md#self-contained-catalogs) 방식으로 데이터와 메타데이터를 참조한다.
- collection metadata는 `data/collection.json`에 저장한다. (1개만 허용)
- STAC Core 또는 참조한 Extension의 필드만 허용한다.
- Hugging Face 데이터셋 저장소 루트에 Collection 메타데이터 파일인  하나만 배치

## 작업 순서

[# 완료 조건](##-완료-조건)을 만족할 때까지 1-4단계를 반복한다.

### 1. Extension 선정

[List of STAC Extensions](https://github.com/stac-extensions/stac-extensions.github.io/blob/main/README.md#list-of-stac-extensions)에서 데이터의 도메인에 맞는 Extension을 선정해주세요.

> [!IMPORTANT] 필수 extension
> - 공통: [processing](https://github.com/stac-extensions/processing)
> - GIS: [projection](https://github.com/stac-extensions/projection)
> - Tabular: [table](https://github.com/stac-extensions/table) (GIS Vector 데이터 포함)
> - Raster: [raster](https://github.com/stac-extensions/raster) 또는 [electro-optical](https://github.com/stac-extensions/eo)

### 2. 메타데이터 뼈대 준비

- [Collection JSON Metadata 뼈대](reference/collection-backbone.json)를 참고하여 `data/collection.json`을 준비합니다.
- 필요한 경우(데이터가 시간·공간 단위로 분할된 경우),  Item JSON Metadata도 준비합니다.
- [### 1. Extension 선정](###-1.-Extension-선정)에서 선정한 Extension을 `extensions` 필드에 반영합니다.
- 각 Extension의 공식 스펙을 참고하여 `data/collection.json`에 필요한 필드를 추가합니다.

### 3. STAC 메타데이터 작성

- [### 2. 메타데이터 뼈대 준비](###-2.-메타데이터-뼈대-준비)에서 준비한 Collection/Item JSON Metadata의 각 필드를 작성합니다. 
- 필요한 경우, 공식문서, 웹페이지, 연구자료 등 관련된 자료를 조사⋅검토합니다.
- 필요한 경우, `scripts/explore.py`를 생성하여 `data/`의 데이터를 조사⋅검토합니다.

> [!NOTE] 처리 방법 기록
> 데이터의 수집·처리 과정을`processing:lineage` 필드에 자세히 기록해주세요. 다른 사람이 재현할 수 있도록 자세히 작성합니다.


### 4. STAC 메타데이터 검증

`scripts/explore.py`를 생성하여 STAC 메타데이터를 검증합니다.
(아래의 예시 코드에서 필요한 검증 로직을 추가해주세요.)

```python
from pathlib import Path
from pystac import Collection

c = Collection.from_file("data/collection.json")
c.validate_all()

assets = []
for a in c.assets.values():
    assets.append(a)
for i in c.get_items(recursive=True):
    for a in i.assets.values():
        assets.append(a)
for a in assets:
    href = a.get_absolute_href()
    if not Path(href).is_file():
        raise FileNotFoundError(href)
```

# AI 추가 지침

- 라이선스와 제공자의 역할, 원본 출처가 불분명하면 임의로 채우지 않고 필요한 근거를 사용자에게 요청합니다.
