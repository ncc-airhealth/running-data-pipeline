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
    raise NotImplementedError(
        f"{year}년 데이터를 내려받는 요청과 저장 로직을 구현하세요."
    )


if __name__ == "__main__":
    main()
