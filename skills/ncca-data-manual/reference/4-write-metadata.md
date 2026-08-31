# 4. STAC 메타데이터 작성·개선

데이터를 조사·검토하고 SpatioTemporal Asset Catalog(STAC) 메타데이터를 작성해요.
데이터 소비자가 데이터를 검색하고 적합성을 판단하며 올바르게 해석하는 데 필요한 정보를 기록하세요.

## 완료 조건

다음 조건을 모두 만족하면 STAC 메타데이터 작성이 끝나요.

- [ ] `data/collection.json`이 STAC 1.1.0과 사용한 Extension의 스키마를 통과함
- [ ] 데이터의 의미, 범위, 구조, 품질, 출처, 라이선스가 근거와 일치함
- [ ] 모든 데이터 파일이 Collection Asset 또는 Item Asset으로 참조됨
- [ ] Collection과 Item의 구조 링크 및 Asset 경로가 유효함
- [ ] 템플릿의 빈 값과 임시 값이 남아 있지 않음

## 메타데이터 작성 규칙

다음 규칙에 따라 메타데이터를 작성하세요.

- [STAC 1.1.0](https://github.com/radiantearth/stac-spec/tree/v1.1.0)을 따르세요.
- [Static Catalog 권장 사항](https://github.com/radiantearth/stac-best-practices/blob/main/best-practices-catalog-and-collection.md)을 따르세요.
- 데이터와 메타데이터를 함께 옮겨도 참조가 유지되도록 구조 링크와 Asset 경로에 상대 경로를 사용하세요.
- Collection은 하나만 만들고 `data/collection.json`에 저장하세요.
- STAC Core 또는 `stac_extensions`에서 선언한 Extension의 필드만 사용하세요.
- 하나의 파일이나 하나의 논리 단위로 설명하는 데이터는 Collection Asset으로 참조하세요.
- 시간·공간 단위로 나뉜 데이터는 Item Asset으로 참조하고 Collection에서 각 Item을 연결하세요.

## 작업 순서

[완료 조건](#완료-조건)을 만족할 때까지 다음 단계를 반복하세요.

### 1. Extension 선정

[List of STAC Extensions](https://github.com/stac-extensions/stac-extensions.github.io/blob/main/README.md#list-of-stac-extensions)에서 데이터 유형에 맞는 Extension을 선택하세요.

> [!IMPORTANT]
> 다음 Extension을 데이터 유형에 맞게 사용하세요.
>
> - 공통: [processing](https://github.com/stac-extensions/processing)
> - GIS: [projection](https://github.com/stac-extensions/projection)
> - Tabular: [table](https://github.com/stac-extensions/table) (GIS Vector 데이터 포함)
> - Raster: [raster](https://github.com/stac-extensions/raster) 또는 [electro-optical](https://github.com/stac-extensions/eo)

### 2. 메타데이터 뼈대 준비

- [Collection JSON 메타데이터 뼈대](collection-backbone.json)를 복사하여 `data/collection.json`을 준비하세요.
- 데이터가 시간·공간 단위로 나뉘면 Item JSON도 준비하세요.
- 선택한 Extension의 스키마 URL을 `stac_extensions`에 추가하세요.
- 각 Extension의 공식 명세를 확인하고 필요한 필드를 추가하세요.

### 3. STAC 메타데이터 작성

- 준비한 Collection과 Item의 각 필드를 작성하세요.
- 공식 문서, 웹페이지, 연구 자료와 실제 데이터를 근거로 사용하세요.
- 필요한 경우 `scripts/explore.py`를 만들어 데이터의 구조와 값을 조사하세요.

> [!NOTE] 처리 방법 기록
> 수집·처리 정보는 `collection-backbone.json`의 `NCCA Pipeline` Provider에 기록하세요.

### 4. STAC 메타데이터 검증

`scripts/explore.py`를 만들고 다음 예시를 바탕으로 STAC 메타데이터를 검증하세요.
실제 데이터의 파일 수, 스키마, 범위와 모든 데이터 파일의 역참조 검사도 추가하세요.

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["pystac"]
# ///

from pathlib import Path

from pystac import Collection

ROOT_DIR = Path(__file__).resolve().parents[1]


def main() -> None:
    """STAC 메타데이터와 Asset 경로를 검증."""
    collection = Collection.from_file(str(ROOT_DIR / "data/collection.json"))
    collection.validate_all()

    assets = list(collection.assets.values())
    for item in collection.get_items(recursive=True):
        assets.extend(item.assets.values())

    for asset in assets:
        href = asset.get_absolute_href()
        if href is None or not Path(href).is_file():
            raise FileNotFoundError(href)


if __name__ == "__main__":
    main()
```

# AI 추가 지침

- 라이선스, 제공자 역할, 원본 출처가 불분명하면 임의로 작성하지 말고 사용자에게 근거를 요청하세요.
- 템플릿의 빈 값이나 데이터 파일 참조 누락이 있으면 이 단계를 완료로 판단하지 마세요.
- 파이프라인 실행 방법보다 데이터의 의미, 범위, 구조, 품질, 출처를 우선 기록하세요.
