# `process.py` 작성 지침.

## 의존성 고정 및 실행

코드 실행 전, `process.py.lock`을 생성하여 의존성을 기록 및 고정한다.

```bash
uv lock --script process.py
uv lock --check --script process.py
uv run --frozen --script process.py
```

## 코드 작성 Best Practice

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "duckdb==1.5.5",
#   "huggingface_hub==1.28.0",
#   "pystac==1.15.2",
#   "tqdm",
# ]
# ///

import os
from pathlib import Path

import duckdb
from huggingface_hub import snapshot_download
from pystac import Collection
from tqdm import tqdm

HF_NAMESPACE = os.environ["NCCA_HF_NAMESPACE"]
SOURCE_DATASET_ID = "<dataset-id>"
SOURCE_REVISION = "<commit-sha>"
ROOT_DIR = Path(__file__).parent

def main() -> None:
    """데이터 처리와 검증을 순서대로 실행한다."""
    process()
    validate()


def process() -> None:
    """원본 데이터를 캐시하고 처리한다."""
    source_dir = cache_source()
    process_source(source_dir)


def validate() -> None:
    """Collection과 연결된 STAC 객체를 검증한다."""
    collection = Collection.from_file(ROOT_DIR / "collection.json")
    collection.validate_all()


def cache_source() -> Path:
    """고정된 상위 데이터셋을 로컬 캐시에 저장한다."""
    print("[download] start")
    source_dir = Path(
        snapshot_download(
            repo_id=f"{HF_NAMESPACE}/{SOURCE_DATASET_ID}",
            repo_type="dataset",
            revision=SOURCE_REVISION,
        )
    )
    print(f"[download] done: {source_dir}")
    return source_dir


def process_one(con: duckdb.DuckDBPyConnection, src_path: Path) -> None:
    """원본 파일 하나를 처리한다."""
    ...


def process_source(source_dir: Path) -> None:
    """모든 원본 파일을 처리한다."""
    src_paths = sorted(source_dir.rglob("*.parquet"))
    if not src_paths:
        raise FileNotFoundError(f"Parquet 파일을 찾을 수 없습니다: {source_dir}")
    print(f"[process] start: {len(src_paths)} files")
    with duckdb.connect() as con:
        for src_path in tqdm(src_paths, desc="process", unit="file"):
            process_one(con, src_path)
    print("[process] done")


if __name__ == "__main__":
    main()
```

## 체크리스트

`process.py`는 체크리스트의 조건을 모두 만족해야한다.

### 라이브러리 의존성

- [ ] PEP 723 metadata가 유효하다.
- [ ] `의존성 고정 및 실행` 에서 의존성 관련 오류가 발생하지 않는다.

### 재현성

- [ ] 로컬 절대 경로와 대화형 입력에 의존하지 않는다.
- [ ] 다른 Hugging Face Dataset을 입력으로 사용하면 `repo_id`를 namespace와 Dataset ID로 만들고 upstream commit SHA를 고정한다.
- [ ] 실행 시각, 난수, 변경 가능한 외부 입력의 영향을 고정하거나 기록한다.

### 코드 품질

- [ ] 장시간 작업의 단계, 진행률, 남은 시간을 확인할 수 있다.
- [ ] 주석과 docstring은 한국어로 작성했다.
- [ ] `main()` 함수가 정의되어 있다.
- [ ] `main()`에는 `process()`와 `validate()` 호출만 포함한다.

### 처리 검증

- [ ] 처리할 수 없는 입력과 검증 실패 시 실행이 실패한다.
- [ ] `validate()`는 검증 실패를 감지하며 데이터와 메타데이터를 수정하지 않는다.
- [ ] 생성된 모든 파일을 실제로 열어 읽을 수 있다.
- [ ] 인간이 대표 Asset을 DuckDB, QGIS 등 적절한 도구로 직접 확인했다.
- [ ] 파일, 행, Feature, 밴드 등 누락된 정보가 없다.
- [ ] schema, 자료형, key, 결측값, 중복값을 데이터 특성에 맞게 확인했다.

### 도메인별 체크리스트

- [ ] `GIS Vector 데이터`가 주어진 경우, {CRS, geometry 유형, 유효성, 위상 관계}를 확인했다.
- [ ] `GIS Raster 데이터`가 주어진 경우, {CRS, 해상도, 밴드, datatype, nodata, scale, offset}을 확인했다.
