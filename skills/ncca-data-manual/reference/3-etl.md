# 3. 데이터 획득·처리

공식 출처에서 데이터를 획득하거나, 기존 데이터셋을 분석 가능한 형태로 처리해요.

## 완료 조건

다음 조건을 모두 만족하면 데이터 획득·처리가 끝나요.

- [ ] 지정된 출처·버전·범위에 해당하는 데이터가 `data/`에 저장됨
- [ ] 코드로 획득·처리했다면 `scripts/process.py`와 `scripts/process.py.lock`으로 결과를 재현할 수 있음

## 규칙

- 데이터 파일은 저장소의 `data/`에 저장하세요.
- 압축 파일 안에 다른 압축 파일을 넣지 마세요.
- 원본 압축파일을 해제해 배포할 때는 압축 해제 및 경로 정리 이외의 데이터 가공을 하지 마세요.
- 원본 데이터의 스냅샷을 저장할 때는 원본 데이터의 값, 정밀도, 좌표계를 변경하지 마세요.
- 데이터를 가공할 때는 정밀도 조정, 값 수정, 좌표계 변환의 목적과 근거를 기록하세요.
- 재현성을 확보하기 위해 데이터를 다시 획득하는 데 필요한 정보(다운로드 주소, 원본 버전, 조회 시점 등)를 문서 또는 코드에 남기세요.

## 작업 전 확인

- 공식 출처와 이용 조건을 확인하세요.
- 획득할 버전, 시간·공간 범위, 예상 파일을 정하세요.
- 예상 데이터 크기, 개별 파일 크기, 파일 수, 폴더별 항목 수를 최신 [Storage limits](https://huggingface.co/docs/hub/storage-limits)와 대조하세요.
- `data/`, `.git/lfs/objects`, Hugging Face Hub 캐시, Xet 캐시가 각각 공간을 사용하므로 로컬 여유 공간을 확인하세요.
- 데이터 구성을 파악한 뒤, 파일 이름만으로 데이터셋과 분할 단위를 구분할 수 있는 네이밍 컨벤션을 정하세요.

## 데이터 획득·처리

- 데이터를 코드로 자동 수집한다면, [수집 코드 예시](../assets/data-extraction-example.py)를 참고하여 `scripts/process.py`를 작성해주세요.
- 예시의 `NotImplementedError`를 실제 데이터 수집 코드로 바꾼 뒤 실행하세요.
- 데이터를 코드로 처리한다면, [처리 코드 예시](../assets/data-processing-example.py)를 참고하여 `scripts/process.py`를 작성해주세요.
- 코드로 처리하기 어려운 경우에는 수행한 방법을 기록하고 직접 작업해도 돼요.
- 잘못된 결과 생성을 즉시 막는 입력 형식이나 필수 필드 검사는 `scripts/process.py`에서 수행하세요.

> [!IMPORTANT] `scripts/process.py`의 재현성
> - 실행마다 동일한 결과를 산출해야 해요.
> - 기존 파일의 일회성 이동이나 이름 변경 등 작업은 금지에요.

> [!NOTE] 처리 방법 기록
> 처리방법에 대한 문서화는 `3. 데이터 획득·처리` 이후의 단계에서 수행해요.
> - 수집·처리 정보는 [Collection JSON 메타데이터 템플릿](../assets/collection-template.json)의 `NCCA Pipeline` Provider에 기록
> - 자동으로 다시 내려받을 수 없는 자료는 신청·전달 경로, 자료 식별자, 취득 시점을 Dataset Card 또는 `processing:lineage`에 기록

### Python 스크립트 작성 및 실행

다음 규칙에 따라 Python 스크립트를 작성하세요.

- 주석과 docstring은 [테크니컬 라이팅](technical-writing.md)을 따라 작성하세요.
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)를 따르세요.
- `if __name__ == "__main__":` 블록에서 `main()`을 호출하세요.
- [PEP 723](https://peps.python.org/pep-0723/) 형식으로 스크립트 상단에 의존성을 작성하세요.

스크립트 작성 후, `uv`로 의존성 lock 파일을 생성하고 스크립트를 실행하세요.

```bash
uv lock --script scripts/process.py
uv lock --check --script scripts/process.py
uv run --frozen --script scripts/process.py
```

### 지리공간 의존성

지리공간 처리 코드는 시스템에 설치된 GDAL·GEOS·PROJ에 의존하지 않고 실행할 수 있어야 해요.
DuckDB의 공간 기능은 잠긴 DuckDB 버전과 호환되는 `core` 저장소의 `spatial` 확장을 사용하세요.
필요한 드라이버나 기능이 Python wheel과 DuckDB 확장에 없다면 작업 전에 사용자와 대안을 정하세요.

> [!NOTE] Python wheel의 지리공간 의존성
> - Python 지리공간 라이브러리는 GDAL을 비롯한 네이티브 지리공간 라이브러리를 wheel에 포함하여 시스템에 설치된 라이브러리에 대한 의존을 줄이고 있어요.
> - [GeoPandas](https://geopandas.org/en/stable/getting_started/install.html)의 주요 의존성인 Shapely·Pyogrio·Pyproj의 wheel은 각각 GEOS·GDAL·PROJ를 포함하고, [Rasterio wheel](https://rasterio.readthedocs.io/en/latest/installation.html)도 libgdal과 관련 의존성을 포함해요.
> - 다만 wheel이 없는 플랫폼이나 Python 버전에서는 시스템 라이브러리로 빌드해야 하며, 일부 GDAL 드라이버와 PROJ 변환 그리드는 wheel에 포함되지 않을 수 있어요.

# AI 추가 지침

- 예시 코드를 그대로 적용하지 말고 실제 입력 형식과 출력 구조를 먼저 확인하세요.
- 입력 버전을 임의로 선택하거나 최신 버전으로 바꾸지 마세요.
- 다시 실행할 때는 기존 파일을 검사하고 누락되었거나 유효하지 않은 파일만 획득·처리하세요.
- 데이터 파일 네이밍 컨벤션은 업무 담당자에게 검토를 요청하세요.
- 원본을 바꾸거나 덮어쓰는 작업은 복구 방법을 확인한 뒤 사용자에게 승인받으세요.
