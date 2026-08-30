# 3. 데이터 획득과 처리

데이터를 획득 또는 처리해 주세요.

## 완료 조건

다음 조건을 모두 만족하면 이 단계를 완료하고 `SKILL.md`의 다음 미완료 단계로 넘어갑니다.

- [ ] 현재 다루는 데이터셋 저장소에 저장해야 할 데이터가 모두 저장되었다.
- [ ] 데이터 파일에 대한 Xet/LFS 추적 속성이 활성화되어 있다.

## 규칙

- 데이터는 저장소의 `data/` 경로에 저장
- 압축 파일 안에 압축 파일을 포함하지 않음
- `.gitattributes`에서 데이터 파일 패턴을 지정하고 `git check-attr filter -- "data/<file>"`로 추적 속성 확인

## 작업 전 확인

- 예상 데이터 크기, 개별 파일 크기, 파일 수, 폴더별 항목 수를 최신 [Storage limits](https://huggingface.co/docs/hub/storage-limits)와 대조해 주세요.
- `data/`, `.git/lfs/objects`, Hugging Face Hub·Xet 캐시가 각각 저장공간을 사용하므로 로컬 여유공간을 확인해 주세요.

## 작업

데이터를 코드로 자동 수집 또는 처리한다면 [`scripts/process.py` 예시](#scriptsprocesspy-예시)를 참고하여 `scripts/process.py`를 작성하고 실행해 주세요.

데이터를 코드로 획득 또는 처리하기 어려운 경우 직접 수행해도 좋습니다.

### Python 스크립트 작성 및 실행

다음 규칙에 따라 Python 스크립트를 작성해 주세요.

- 주석과 docstring은 한국어로 작성
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)를 따름
- `if __name__ == "__main__":` 블록에서 `main()`을 호출
- [PEP 723](https://peps.python.org/pep-0723/) 스크립트 상단 의존성 메타데이터 작성

스크립트를 실행할 때 `uv`를 사용하여 의존성 잠금 파일(`process.py.lock`)을 생성하고 실행해 주세요.

```bash
uv lock --script scripts/process.py
uv lock --check --script scripts/process.py
uv run --frozen --script scripts/process.py
```

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
    dfs = [pl.read_csv(f) for f in Path(src_dir).rglob("**.csv")]
    df = pl.concat(dfs, how="vertical_relaxed")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.write_parquet(DATA_DIR / "items.parquet")


if __name__ == "__main__":
    main()
```

# AI 추가 지침

- 예시 코드를 그대로 적용하지 말고 저장소의 실제 입력 형식·출력 구조·검증 기준을 먼저 확인
- 입력 버전을 임의로 선택하거나 최신 버전으로 바꾸지 않음
- 재실행 시 기존 파일을 확인하고 누락되었거나 유효하지 않은 파일만 획득·처리
- 오래 걸리는 작업에는 현재 단계와 진행률을 표시
