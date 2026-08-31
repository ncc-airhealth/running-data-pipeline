# 3. 데이터 획득·처리

공식 출처에서 데이터를 획득하고 분석에 사용할 형태로 처리해요.

## 완료 조건

다음 조건을 모두 만족하면 데이터 획득·처리가 끝나요.

- [ ] 정한 출처·버전·범위에 해당하는 데이터가 `data/`에 저장됨
- [ ] 처리 결과의 파일 수, 스키마, 행 수, 시간·공간 범위 등 데이터별 검증 항목을 통과함
- [ ] 코드로 획득·처리했다면 `scripts/process.py`와 `scripts/process.py.lock`으로 결과를 다시 만들 수 있음
- [ ] Xet/LFS로 관리할 파일에 `.gitattributes` 추적 속성이 적용됨

## 규칙

- 데이터 파일은 저장소의 `data/`에 저장하세요.
- 압축 파일 안에 다른 압축 파일을 넣지 마세요.
- 원본의 의미와 정밀도를 유지하고, 값이나 좌표계를 임의로 보정하지 마세요.
- 다운로드 주소, 원본 버전, 조회 시점 등 다시 획득하는 데 필요한 정보를 처리 코드에 남기세요.

## 작업 전 확인

- 공식 출처와 이용 조건을 확인하세요.
- 획득할 버전, 시간·공간 범위, 예상 파일을 정하세요.
- 예상 데이터 크기, 개별 파일 크기, 파일 수, 폴더별 항목 수를 최신 [Storage limits](https://huggingface.co/docs/hub/storage-limits)와 대조하세요.
- `data/`, `.git/lfs/objects`, Hugging Face Hub 캐시, Xet 캐시가 각각 공간을 사용하므로 로컬 여유 공간을 확인하세요.

## 데이터 획득·처리

데이터를 코드로 자동 획득하거나 처리한다면 [`scripts/process.py` 예시](#scriptsprocesspy-예시)를 참고하여 `scripts/process.py`를 작성하고 실행하세요.
코드로 처리하기 어려운 경우에는 수행한 방법과 검증 결과를 기록하고 직접 작업해도 돼요.

처리 후 데이터별 검증 항목을 실행하세요.
검증 항목에는 파일 누락, 스키마, 행 수, 중복, 결측, 값 범위, 시간·공간 범위 중 해당하는 내용을 포함하세요.

### Python 스크립트 작성 및 실행

다음 규칙에 따라 Python 스크립트를 작성하세요.

- 주석과 docstring은 한국어로 작성하세요.
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)를 따르세요.
- `if __name__ == "__main__":` 블록에서 `main()`을 호출하세요.
- [PEP 723](https://peps.python.org/pep-0723/) 형식으로 스크립트 상단에 의존성을 작성하세요.

`uv`로 의존성 잠금 파일을 생성하고 잠긴 의존성으로 스크립트를 실행하세요.

```bash
uv lock --script scripts/process.py
uv lock --check --script scripts/process.py
uv run --frozen --script scripts/process.py
```

### 지리공간 의존성

지리공간 처리 코드는 시스템에 설치된 GDAL·GEOS·PROJ에 의존하지 않고 실행할 수 있어야 해요.
DuckDB의 공간 기능은 잠긴 DuckDB 버전과 호환되는 `core` 저장소의 `spatial` 확장을 사용하세요.
필요한 드라이버나 기능이 Python wheel과 DuckDB 확장에 없다면 작업 전에 사용자와 대안을 정하세요.

### Xet/LFS 추적

Hugging Face가 만든 `.gitattributes`에 데이터 파일 형식이 없으면 파일 확장자별로 정확한 패턴을 추가하세요.
예를 들어 `git xet track "*.parquet"`처럼 지정하고, 작은 텍스트나 메타데이터 파일까지 포괄하는 패턴은 피하세요.

대표 파일마다 다음 명령어를 실행하세요.

```bash
git check-attr filter -- "data/<file>"
```

결과가 `unspecified`이면 해당 파일은 Xet/LFS로 추적되지 않아요.

## `scripts/process.py` 예시

### 예시 1: 데이터 다운로드

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx", "tqdm"]
# ///

from pathlib import Path

import httpx
from tqdm import tqdm

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
YEARS = [2000, 2005, 2010, 2015, 2020]


def main() -> None:
    """데이터 다운로드."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for year in tqdm(YEARS, desc="downloading"):
        _download_single_data(year)


def _download_single_data(year: int) -> None:
    """한 연도의 원본 데이터를 다운로드."""
    with httpx.Client() as client:
        ...


if __name__ == "__main__":
    main()
```

### 예시 2: 데이터 처리

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "huggingface-hub",
#   "polars",
# ]
# ///

import os
from pathlib import Path

import polars as pl
from huggingface_hub import snapshot_download

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
NAMESPACE = os.environ["NCCA_HF_NAMESPACE"]
SOURCE_DATASET = "<source-dataset-name>"
SOURCE_REVISION = "<commit-sha>"


def main() -> None:
    """데이터 처리."""
    src_dir = snapshot_download(
        repo_id=f"{NAMESPACE}/{SOURCE_DATASET}",
        repo_type="dataset",
        revision=SOURCE_REVISION,
        allow_patterns="*.csv",
    )
    dfs = [pl.read_csv(f) for f in Path(src_dir).rglob("*.csv")]
    df = pl.concat(dfs, how="vertical_relaxed")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.write_parquet(DATA_DIR / "items.parquet")


if __name__ == "__main__":
    main()
```

# AI 추가 지침

- 예시 코드를 그대로 적용하지 말고 실제 입력 형식, 출력 구조, 검증 기준을 먼저 확인하세요.
- 입력 버전을 임의로 선택하거나 최신 버전으로 바꾸지 마세요.
- 다시 실행할 때는 기존 파일을 검사하고 누락되었거나 유효하지 않은 파일만 획득·처리하세요.
- 오래 걸리는 작업에는 현재 단계와 진행률을 표시하세요.
- 원본을 바꾸거나 덮어쓰는 작업은 복구 방법을 확인한 뒤 사용자에게 승인받으세요.
