# `process.py` 작성 매뉴얼

`process.py`는 자동으로 데이터를 수집하거나 처리하는 스크립트입니다.

## 입력과 출력 먼저 정하기

코드를 작성하기 전에 아래 항목을 검토해 주세요.

| 항목 | 기록할 내용 | 예시 |
| --- | --- | --- |
| 원본 출처 | 기관명과 원본 페이지 또는 저장소 | 서울 열린데이터광장 건물 데이터 |
| 입력 식별자 | 저장소 ID 또는 원본 파일명 | `<namespace>/<source-dataset>` |
| 입력 버전 | 커밋 SHA, 공식 버전 또는 취득 시각 | `0123456789abcdef...` |
| 라이선스 | 원본 이용 조건과 가공·재배포 가능 여부 | CC BY 4.0, 재배포 가능 |
| 처리 규칙 | 필터, 좌표 변환, 컬럼 변경, 결합 방식 | EPSG:5179에서 EPSG:4326으로 변환 |
| 출력 경로 | 저장소 루트 기준 상대 경로 | `items/seoul-2024/data.parquet` |
| 검증 기준 | 파일 수, 행 수, 스키마, 공간 조건 | 25개 파일, `geometry` 결측 없음 |

## 작성 규칙

코드를 작성할 때 다음 규칙을 지켜 주세요.

- 코드로 재현할 수 있는 작업만 `process.py`에 작성하고, 사람이 직접 한 작업은 `README.md`에 기록
- 원본 데이터의 라이선스와 재배포 조건을 확인한 뒤에만 원본 또는 가공 데이터를 저장소에 추가
- 스크립트 상단에 [PEP 723](https://peps.python.org/pep-0723/) 메타데이터 작성
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)를 따름
- 동일한 입력과 의존성에서 같은 결과가 나오도록 데이터 저장소, 파일, 버전 또는 취득 시점을 상수로 고정
- STAC 메타데이터는 별도로 작성
- `process.py`에서는 STAC JSON을 생성하거나 수정하지 않고 생성된 데이터와 기존 STAC JSON만 검증
- `main()` 함수는 `process()`, `explore()`, `validate()`를 순서대로 호출
  - `process()`: 데이터 처리
  - `explore()`: 생성된 데이터를 출력
  - `validate()`: 생성된 데이터와 STAC JSON을 검증
  - 그 밖의 함수 이름에는 `_` 접두사를 붙임

## `validate()`의 최소 검증 항목

`validate()`는 아래 항목을 검사하고, 하나라도 실패하면 예외를 일으킵니다.

- 정한 출력 경로에 파일이 있는지
- 파일 수·행 수·스키마·공간 조건이 사전에 정한 검증 기준과 일치하는지
- STAC Collection과 Item JSON이 PySTAC 스키마 검증을 통과하는지
- STAC의 모든 로컬 Link와 Asset의 `href`가 실제 파일을 가리키는지
- Item의 공간·시간 범위와 Asset 정보가 생성된 데이터와 일치하는지

## 실행 규칙

[PEP 723](https://peps.python.org/pep-0723/) 메타데이터를 작성하고 잠금 파일을 생성하여 의존성을 기록한 뒤 실행해 주세요.

```bash
uv lock --script process.py
uv lock --check --script process.py
uv run --frozen --script process.py
```
`process.py`의 의존성을 바꿨다면 `process.py.lock`도 다시 생성해야 합니다.

## 참고 자료

- [uv에서 단일 파일 스크립트 실행 및 잠금](https://docs.astral.sh/uv/guides/scripts/)
- [Hugging Face Hub 다운로드](https://huggingface.co/docs/huggingface_hub/guides/download)
- [PySTAC](https://pystac.readthedocs.io/)

# AI 추가 지침

- 예시 코드를 그대로 적용하지 말고 저장소의 실제 입력 형식·출력 구조·검증 기준을 먼저 확인
- 입력 버전을 임의로 선택하거나 최신 버전으로 바꾸지 않음
- 원본 데이터의 라이선스와 재배포 조건을 확인하기 전에는 원본 또는 가공 데이터를 저장소에 추가하지 않음
- 기존 결과를 삭제하거나 전체 데이터를 다시 다운로드하기 전에 영향 범위와 복구 방법을 확인
- 검증을 통과할 목적으로 데이터를 임의로 보정하지 않음
- 실행하지 않은 검증은 완료로 표시하지 않음
- 코드에 토큰과 비밀번호를 넣지 않으며, 환경 변수 값이나 인증 정보가 로그에 출력되지 않는지 확인
- 오래 걸리는 작업에는 현재 단계와 진행률을 표시

# 코드 작성 예시

## 예시 1: 데이터 다운로드

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "httpx",
#   "polars",
#   "pystac",
#   "tqdm",
# ]
# ///

from pathlib import Path

import httpx
import polars as pl
import pystac
from tqdm import tqdm

ROOT_DIR = Path(__file__).resolve().parent
ITEMS_DIR = ROOT_DIR / "items"
YEARS = [2000, 2005, 2010, 2015, 2020]


def main() -> None:
    """데이터 다운로드·탐색·검증을 순서대로 실행합니다."""
    process()
    explore()
    validate()


def process() -> None:
    """연도별 원본 데이터를 다운로드합니다."""
    for year in tqdm(YEARS, desc="downloading"):
        _download_single_data(year)


def explore() -> None:
    """생성된 Parquet 파일의 일부를 출력합니다."""
    files = sorted(ITEMS_DIR.rglob("*.parquet"))
    for file in files:
        df = pl.read_parquet(file)
        print(df.head())


def validate() -> None:
    """STAC 메타데이터와 생성된 Parquet 파일을 검증합니다."""
    collection = pystac.Collection.from_file(ROOT_DIR / "collection.json")
    collection.validate_all()
    for file in ITEMS_DIR.rglob("*.parquet"):
        _validate_single_data(file)


def _download_single_data(year: int) -> None:
    """한 연도의 원본 데이터를 다운로드합니다.

    Args:
        year: 다운로드할 데이터의 기준 연도
    """
    ...


def _validate_single_data(file: Path) -> None:
    """Parquet 파일 하나의 스키마와 내용을 검증합니다.

    Args:
        file: 검증할 Parquet 파일의 경로

    Raises:
        ValueError: 파일이 검증 기준을 충족하지 못한 경우
    """
    ...


if __name__ == "__main__":
    main()
```

## 예시 2: 데이터 처리

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "huggingface-hub",
#   "polars",
#   "pystac",
# ]
# ///

from pathlib import Path

import polars as pl
import pystac
from huggingface_hub import snapshot_download

ROOT_DIR = Path(__file__).resolve().parent
ITEMS_DIR = ROOT_DIR / "items"
SOURCE_DATASET_ID = "<namespace>/<source-dataset>"
SOURCE_REVISION = "<commit-sha>"
SOURCE_PATTERN = "data/*.csv"
OUTPUT_FILE = ITEMS_DIR / "processed-data" / "processed-data.parquet"


def main() -> None:
    """데이터 처리·탐색·검증을 순서대로 실행합니다."""
    process()
    explore()
    validate()


def process() -> None:
    """고정된 입력 버전의 CSV 파일을 하나의 Parquet 파일로 변환합니다.

    Raises:
        FileNotFoundError: 입력 CSV 파일이 없는 경우
    """
    source_dir = Path(
        snapshot_download(
            repo_id=SOURCE_DATASET_ID,
            repo_type="dataset",
            revision=SOURCE_REVISION,
            allow_patterns=[SOURCE_PATTERN],
        )
    )
    source_files = sorted(source_dir.glob(SOURCE_PATTERN))
    if not source_files:
        raise FileNotFoundError(
            f"입력 파일을 찾을 수 없습니다: {SOURCE_PATTERN}"
        )

    data = pl.concat(
        [pl.read_csv(file) for file in source_files],
        how="vertical_relaxed",
    )
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    data.write_parquet(OUTPUT_FILE)


def explore() -> None:
    """처리한 데이터의 일부를 출력합니다."""
    print(pl.read_parquet(OUTPUT_FILE).head())


def validate() -> None:
    """출력 파일과 STAC 메타데이터를 검증합니다.

    Raises:
        FileNotFoundError: 출력 파일이 없는 경우
        ValueError: 출력 파일에 데이터가 없는 경우
    """
    if not OUTPUT_FILE.is_file():
        raise FileNotFoundError(f"출력 파일이 없습니다: {OUTPUT_FILE}")

    data = pl.read_parquet(OUTPUT_FILE)
    if data.is_empty():
        raise ValueError(f"출력 파일에 데이터가 없습니다: {OUTPUT_FILE}")

    collection = pystac.Collection.from_file(ROOT_DIR / "collection.json")
    collection.validate_all()


if __name__ == "__main__":
    main()
```
