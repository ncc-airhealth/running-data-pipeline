---
type: Reference
title: STAC 메타데이터 규격
description: NCCA 데이터셋의 시공간 메타데이터를 표준화하기 위한 STAC Collection 작성 규약 및 사양이에요.
tags: [stac, metadata, geospatial, specification]
---

# STAC 메타데이터 규격

NCCA 데이터 파이프라인 프로젝트는 지리공간 및 시계열 데이터의 상호운용성과 검색 편의성을 높이기 위해 [STAC(SpatioTemporal Asset Catalog)](https://stacspec.org/) 표준을 채택하고 있어요.

모든 데이터셋 저장소의 `data/` 디렉터리에는 루트 메타데이터인 `collection.json`이 포함되어야 해요.

## 1. STAC Collection 기본 구조

STAC 1.1.0 규격을 기준으로 작성하며, 기본 구조는 다음과 같아요.

```json
{
  "stac_version": "1.1.0",
  "type": "Collection",
  "stac_extensions": [
    "https://stac-extensions.github.io/processing/v1.2.0/schema.json"
  ],
  "id": "<dataset-name>",
  "title": "<데이터셋 제목>",
  "description": "<데이터셋에 대한 상세 설명>",
  "keywords": ["air-quality", "pm25", "korea"],
  "license": "<SPDX 라이선스 식별자>",
  "extent": {
    "spatial": {
      "bbox": [[124.5, 33.0, 132.0, 38.9]]
    },
    "temporal": {
      "interval": [["2020-01-01T00:00:00Z", "2023-12-31T23:59:59Z"]]
    }
  },
  "providers": [
    {
      "name": "<원천 데이터 제공 기관>",
      "roles": ["licensor"],
      "url": "<제공 기관 URL>"
    },
    {
      "name": "NCCA Pipeline",
      "roles": ["host", "processor"],
      "url": "https://huggingface.co/ncca-pipeline"
    }
  ],
  "links": [
    {
      "rel": "license",
      "href": "<라이선스 링크>",
      "title": "<라이선스 이름>"
    }
  ]
}
```

## 2. 필수 필드 정의 및 작성 원칙

- **`id`**: 저장소 이름(`dataset-name`)과 동일하게 kebab-case로 작성해요.
- **`stac_version`**: `"1.1.0"` 이상을 사용해요.
- **`description`**: 데이터의 목적, 생성 과정, 주요 변수를 요약하여 작성해요.
- **`license`**: [SPDX 라이선스 식별자](https://spdx.org/licenses/)(예: `CC-BY-4.0`, `MIT`, `proprietary`)를 사용해요.
- **`extent`**:
  - **`spatial.bbox`**: 2D 좌표 기준 `[min_lon, min_lat, max_lon, max_lat]` 형식(WGS84, EPSG:4326)으로 기입해요.
  - **`temporal.interval`**: `[[시작일시, 종료일시]]` 형태(ISO 8601 UTC)로 기입해요. 현재도 갱신 중인 데이터라면 종료일시는 `null`로 지정할 수 있어요.
- **`providers`**: 원천 데이터 소유자(`licensor`)와 처리/배포 주체(`processor`, `host`)를 구분하여 명시해요.

## 3. 링크(Links) 작성 규칙

- **상대 경로 사용**: Collection 내부에서 Item이나 하위 파일을 참조할 때는 반드시 로컬 상대 경로(`href: "./items/..."`)를 사용하세요. (절대 경로 금지)
- **루트 self 링크 지양**: 최상위 `collection.json`에는 `rel: "self"` 링크를 강제하지 않으며, 이식성을 위해 생략하거나 상대 경로로 유지해요.
