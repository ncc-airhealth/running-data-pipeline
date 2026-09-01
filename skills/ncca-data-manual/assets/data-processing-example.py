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
