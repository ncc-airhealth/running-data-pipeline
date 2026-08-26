# 4. 메타데이터 작성·개선

데이터에 대해 조사·검토하고 STAC 메타데이터를 기록해 주세요.

## 완료 조건

다음 조건을 모두 만족하면 이 단계를 완료하고 `SKILL.md`의 다음 미완료 단계로 넘어갑니다.

- [ ] `data/collection.json`이 작성되어 있다.
- [ ] 데이터에 대한 모든 암묵지가 STAC 메타데이터에 반영되어 있다.
- [ ] STAC Static Metadata가 유효하다.
- [ ] 모든 데이터 파일이 Collection Asset 또는 Item Asset으로 참조되어 있다.

## 메타데이터 작성 규칙

현재 다루는 데이터셋에 대한 정보를 일관성 있게 관리하기 위해 [STAC](https://stacspec.org/)을 기반으로 메타데이터를 작성합니다. STAC 메타데이터 작성 세부 규칙은 다음과 같습니다.

- [STAC 1.1.0](https://github.com/radiantearth/stac-spec/tree/v1.1.0)을 따른다.
- [Static Catalogs](https://github.com/radiantearth/stac-spec/blob/v1.1.0/best-practices.md#static-catalogs) 방식으로 `data/` 경로에 JSON으로 저장한다.
- [Self-contained with Assets](https://github.com/radiantearth/stac-spec/blob/v1.1.0/best-practices.md#self-contained-catalogs) 방식으로 데이터와 메타데이터를 참조한다.
- Collection 메타데이터는 `data/collection.json`에 저장한다. (1개만 허용)
- STAC Core 또는 참조한 Extension의 필드만 허용한다.
- 하나의 파일로 설명하는 데이터는 Collection Asset으로 참조한다.
- 시간·공간 단위로 분할된 데이터는 Item Asset으로 참조하고 Collection에서 각 Item을 연결한다.

## 작업 순서

[완료 조건](#완료-조건)을 만족할 때까지 1~4단계를 반복한다.

### 1. Extension 선정

[List of STAC Extensions](https://github.com/stac-extensions/stac-extensions.github.io/blob/main/README.md#list-of-stac-extensions)에서 데이터의 도메인에 맞는 Extension을 선정해 주세요.

> [!IMPORTANT] 필수 Extension
> - 공통: [processing](https://github.com/stac-extensions/processing)
> - GIS: [projection](https://github.com/stac-extensions/projection)
> - Tabular: [table](https://github.com/stac-extensions/table) (GIS Vector 데이터 포함)
> - Raster: [raster](https://github.com/stac-extensions/raster) 또는 [electro-optical](https://github.com/stac-extensions/eo)

### 2. 메타데이터 뼈대 준비

- [Collection JSON 메타데이터 뼈대](collection-backbone.json)를 참고하여 `data/collection.json`을 준비합니다.
- 필요한 경우(데이터가 시간·공간 단위로 분할된 경우) Item JSON 메타데이터도 준비합니다.
- 선정한 Extension을 `stac_extensions` 필드에 반영합니다.
- 각 Extension의 공식 스펙을 참고하여 `data/collection.json`에 필요한 필드를 추가합니다.

### 3. STAC 메타데이터 작성

- [2. 메타데이터 뼈대 준비](#2-메타데이터-뼈대-준비)에서 준비한 Collection/Item JSON 메타데이터의 각 필드를 작성합니다.
- 필요한 경우 공식 문서, 웹페이지, 연구 자료 등 관련 자료를 조사·검토합니다.
- 필요한 경우 `scripts/explore.py`를 생성하여 `data/`의 데이터를 조사·검토합니다.

> [!NOTE] 처리 방법 기록
> 수집·처리 정보는 `collection-backbone.json`의 `NCCA Pipeline` Provider에 기록합니다.

### 4. STAC 메타데이터 검증

`scripts/explore.py`를 생성하여 STAC 메타데이터를 검증합니다.
(아래 예시 코드에 필요한 검증 로직을 추가해 주세요.)

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["pystac"]
# ///

from pathlib import Path

from pystac import Collection

ROOT_DIR = Path(__file__).resolve().parents[1]

c = Collection.from_file(str(ROOT_DIR / "data/collection.json"))
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
- 뼈대의 빈 값이 남아 있거나 데이터 파일 참조가 누락되면 완료로 판단하지 않습니다.
