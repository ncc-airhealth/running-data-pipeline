# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx", "tqdm"]
# ///

from pathlib import Path

import httpx
from tqdm import tqdm

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
YEARS = [2020, 2021, 2022, 2023]


def main() -> None:
    """원천 데이터 다운로드."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for year in tqdm(YEARS, desc="downloading"):
        _download_single_data(year)


def _download_single_data(year: int) -> None:
    """한 연도의 원본 데이터를 다운로드."""
    output_path = DATA_DIR / f"{year}.csv"
    if _is_valid_output(output_path):
        return

    raise NotImplementedError(
        f"{year}년 데이터를 내려받는 요청과 저장 로직을 구현하세요."
    )


def _is_valid_output(output_path: Path) -> bool:
    """기존 출력의 유효성을 확인."""
    if not output_path.is_file():
        return False
    raise NotImplementedError(
        f"실제 파일 형식에 맞는 유효성 검사를 구현하세요: {output_path}"
    )


if __name__ == "__main__":
    main()
