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
NAMESPACE = os.environ.get("NCCA_HF_NAMESPACE", "ncca-pipeline")
SOURCE_DATASET = "<source-dataset-name>"
SOURCE_REVISION = "<commit-sha>"


def main() -> None:
    """데이터 처리 및 변환."""
    output_path = DATA_DIR / "items.parquet"
    if _is_valid_output(output_path):
        return

    # 외부 또는 상위 데이터셋 저장소로부터 소스 데이터 확보 (필요시)
    src_dir = snapshot_download(
        repo_id=f"{NAMESPACE}/{SOURCE_DATASET}",
        repo_type="dataset",
        revision=SOURCE_REVISION,
        allow_patterns="*.csv",
    )
    dfs = [pl.read_csv(f) for f in Path(src_dir).rglob("*.csv")]
    df = pl.concat(dfs, how="vertical_relaxed")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.write_parquet(output_path)


def _is_valid_output(output_path: Path) -> bool:
    """기존 Parquet 출력의 유효성을 확인."""
    if not output_path.is_file():
        return False
    try:
        pl.scan_parquet(output_path).collect_schema()
    except (OSError, pl.exceptions.PolarsError):
        return False
    return True


if __name__ == "__main__":
    main()
