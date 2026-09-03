# 4. STAC 메타데이터 작성

데이터의 주요 정보가 누락되는 것을 방지하고 메타데이터를 체계적으로 관리하기 위해 STAC 스펙에 맞춰 `data/collection.json`을 작성해요.

자유 형식으로 작성할 때 발생할 수 있는 누락을 막고, 공간·시간 범위, 데이터 스키마, 제공처, 라이선스 등 필수 정보를 표준 규격에 따라 빠짐없이 기록해요.

## 세부 절차

1. 메타데이터 템플릿을 준비하세요.
   - [STAC 메타데이터 규격](./knowledge/stac-spec.md)을 확인하세요.
   - [Collection 템플릿](../assets/collection-template.json)을 복사해 `data/collection.json` 파일을 만드세요.
     ```bash
     cp skills/ncca-datarepo-manual/assets/collection-template.json data/collection.json
     ```

2. 메타데이터 필수 항목을 빠짐없이 작성하세요.
   - 각 필드의 상세 형식과 기준은 [STAC 메타데이터 규격](./knowledge/stac-spec.md)을 참고하세요. 더 넓은 필드 확장이 필요하다면 [STAC Specification 공식 문서](https://stacspec.org/en/about/stac-spec/)를 함께 참고할 수 있어요.
   - **`id`**: 데이터셋 이름(`kebab-case`)을 입력하세요.
   - **`description`**: 데이터의 목적, 생성 과정, 주요 변수를 설명하세요.
   - **`extent`**:
     - `spatial.bbox`: WGS84 좌표 기준 `[min_lon, min_lat, max_lon, max_lat]` 범위를 기입하세요.
     - `temporal.interval`: `[["시작일시", "종료일시"]]` (ISO 8601 UTC)를 기입하세요.
   - **`license`**: [SPDX 라이선스 식별자](https://spdx.org/licenses/)를 입력하세요.
   - **`providers`**: 원천 데이터 제공 기관(`licensor`)과 NCCA Pipeline(`processor`, `host`)을 명시하세요.

3. 메타데이터 유효성을 검증하세요.
   - [검토 코드 예시](../assets/data-review-example.py)를 참고해 `scripts/review.py`를 작성하고 실행하세요.
     ```bash
     uv lock --script scripts/review.py
     uv run --frozen --script scripts/review.py
     ```
   - STAC 규격 스키마 검증을 통과하고, 필수 필드 누락이 없는지 확인하세요.

## 완료 조건

다음 조건을 모두 만족하면 메타데이터 작성이 끝나요.

- [ ] `data/collection.json`이 STAC 1.1.0 규격을 통과함
- [ ] 공간 범위(bbox)와 시간 범위(interval)가 실제 데이터와 일치함
- [ ] 라이선스 및 원천 제공자 정보가 올바르게 기입됨
- [ ] 템플릿의 빈 값이나 임시 문자열(`""`)이 남아 있지 않고 필수 정보가 누락 없이 기록됨

> **AI 추가 지침**
>
> - 공간·시간 범위와 라이선스 정보는 임의로 추정하지 말고 실제 데이터와 공식 출처를 기반으로 작성할 것
> - `collection.json` 내부의 링크는 반드시 로컬 상대 경로를 사용하고, 루트 Collection에는 `self` 링크를 추가하지 말 것

---
다음 작업: [5. 저장소 설명 문서 작성](./5-write-dataset-card.md)
