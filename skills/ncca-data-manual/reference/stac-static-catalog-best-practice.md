# STAC Static Catalog 메타데이터 작성 매뉴얼

메타데이터 작성 매뉴얼입니다.

## Why STAC?

[STAC](https://stacspec.org/)을 사용하면 데이터의 공간·시간 범위와 관련 파일을 일관된 구조로 기록할 수 있습니다.

## 규칙

- 메타데이터는 [STAC 1.1.0](https://github.com/radiantearth/stac-spec/tree/v1.1.0) 기반으로 작성
- [Static Catalogs](https://github.com/radiantearth/stac-spec/blob/v1.1.0/best-practices.md#static-catalogs) 방식으로 데이터셋 저장소에 JSON으로 저장
- [Self-contained with Assets](https://github.com/radiantearth/stac-spec/blob/v1.1.0/best-practices.md#self-contained-catalogs) 방식으로 데이터와 메타데이터를 참조
- 데이터의 도메인에 맞는 [STAC Extension](https://github.com/stac-extensions/stac-extensions.github.io/blob/main/README.md)을 선택하여 적용
- STAC Core 또는 참조한 Extension의 필드만 허용
- Hugging Face 데이터셋 저장소 루트에 Collection 메타데이터 파일인 `collection.json` 하나만 배치

## 작업 순서

### 1. Collection의 STAC Core 필드 작성

먼저 `collection.json`을 작성합니다.

출처, 라이선스, 공간·시간 범위 등 데이터에 대한 정보를 조사·검토하여 Collection 메타데이터를 작성해 주세요. ([STAC Collection Spec](https://github.com/radiantearth/stac-spec/blob/v1.1.0/collection-spec/collection-spec.md) 참고)

| 필드 | 설명 |
| --- | --- |
| `id` | 저장소의 데이터셋 이름과 동일하게 설정. |
| `description` | 데이터의 대상, 범위와 가공 수준을 짧고 구체적으로 설명. |
| `license` | 실제 이용 조건에 맞는 SPDX 식별자나 STAC 명세에서 허용하는 값을 사용. |
| `providers` | `producer`, `processor`, `licensor`, `host` 중 실제 역할만 기록. |
| `extent.spatial.bbox` | 모든 Item의 bbox를 포함해야 함. WGS 84 좌표를 경도·위도 순서로 기록. |
| `extent.temporal.interval` | 모든 Item의 시간 범위를 포함. 시작 또는 끝을 알 수 없을 때만 그 값을 `null`로 설정. |

### 2. Collection의 STAC Extension 필드 작성

[STAC Extensions](https://github.com/stac-extensions/stac-extensions.github.io/blob/main/README.md)에서 데이터에 맞는 STAC Extension을 선택하고, 해당 Extension의 필드를 작성해 주세요.

### 3. Item 작성

데이터가 시간·공간 단위로 분할된 경우 Item으로 묶어서 저장합니다.
[STAC Item Specification](https://github.com/radiantearth/stac-spec/blob/v1.1.0/item-spec/item-spec.md)을 참고하여 작성해 주세요.

### 4. 검증

아래 코드를 `uv run --with pystac python -c '...'`의 `...` 자리에 넣어 실행하거나 `process.py`의 `validate()` 함수에 포함하여 STAC JSON 스키마와 Asset 파일 경로를 검증해 주세요.

```python
from pathlib import Path
from pystac import Collection

c = Collection.from_file("collection.json")
c.validate_all()
assets = []
for a in c.assets.values():
    assets.append(a)
for item in c.get_items(recursive=True):
    for a in item.assets.values():
        assets.append(a)
for a in assets:
    href = a.get_absolute_href()
    if not Path(href).is_file():
        raise FileNotFoundError(href)
```

## 참고 문서

- [STAC Specification](https://github.com/radiantearth/stac-spec)
- [STAC Best Practices](https://github.com/radiantearth/stac-spec/blob/v1.1.0/best-practices.md)
- [STAC Extensions](https://stac-extensions.github.io/)
- [PySTAC](https://pystac.readthedocs.io/)

# AI 추가 지침

- 스키마 검증 통과와 메타데이터 내용의 정확성을 구분해 보고합니다.
- 라이선스와 제공자의 역할, 원본 출처가 불분명하면 임의로 채우지 않고 필요한 근거를 사용자에게 요청합니다.
