# /// script
# requires-python = ">=3.12"
# dependencies = ["pystac[validation]"]
# ///

import json
from pathlib import Path, PurePosixPath, PureWindowsPath
from urllib.parse import urlsplit

from pystac import Collection

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
STRUCTURAL_LINK_RELS = {"child", "collection", "item", "parent", "root"}


def main() -> None:
    """데이터와 STAC 메타데이터를 검토."""
    _review_data()
    _review_metadata()


def _review_data() -> None:
    """데이터별 검증 항목을 검토."""
    # 데이터 형식에 맞는 파일 존재, 스키마, 값 유효성 검증 로직 구현
    pass


def _review_metadata() -> None:
    """STAC 메타데이터와 Asset 경로를 검토."""
    collection_file = DATA_DIR / "collection.json"
    if not collection_file.is_file():
        raise FileNotFoundError(f"Collection 메타데이터 파일이 없습니다: {collection_file}")

    collection = Collection.from_file(str(collection_file))
    collection.validate_all()

    collection_href = collection.get_self_href()
    if collection_href is None:
        raise ValueError("Collection 메타데이터 파일의 경로를 확인할 수 없습니다.")

    collection_path = Path(collection_href).resolve()
    metadata_paths = {collection_path}
    for item in collection.get_items(recursive=True):
        item_href = item.get_self_href()
        if item_href is None:
            raise ValueError(f"Item 메타데이터 파일의 경로를 확인할 수 없습니다: {item.id}")
        metadata_paths.add(Path(item_href).resolve())

    asset_paths = _review_hrefs(metadata_paths, collection_path)

    data_paths = {path.resolve() for path in DATA_DIR.rglob("*") if path.is_file()}
    unreferenced_paths = data_paths - metadata_paths - asset_paths
    if unreferenced_paths:
        raise ValueError(f"메타데이터에서 참조하지 않은 파일: {unreferenced_paths}")


def _review_hrefs(metadata_paths: set[Path], collection_path: Path) -> set[Path]:
    """구조 링크와 Asset 경로를 검토."""
    asset_paths = set()
    for metadata_path in metadata_paths:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

        for link in metadata.get("links", []):
            rel = link.get("rel")
            href = link.get("href")
            if metadata_path == collection_path and rel == "self":
                raise ValueError("루트 Collection에는 self 링크를 사용하지 마세요.")
            if rel in STRUCTURAL_LINK_RELS:
                _resolve_local_file(metadata_path, href, f"{rel} 링크")

        for key, asset in metadata.get("assets", {}).items():
            asset_paths.add(
                _resolve_local_file(metadata_path, asset.get("href"), f"{key} Asset")
            )
    return asset_paths


def _resolve_local_file(metadata_path: Path, href: object, label: str) -> Path:
    """상대 경로가 가리키는 로컬 파일을 확인."""
    if not isinstance(href, str):
        raise ValueError(f"{label}의 href는 문자열이어야 합니다: {href}")

    parsed_href = urlsplit(href)
    posix_path = PurePosixPath(parsed_href.path)
    windows_path = PureWindowsPath(parsed_href.path)
    if (
        parsed_href.scheme
        or parsed_href.netloc
        or posix_path.is_absolute()
        or windows_path.is_absolute()
    ):
        raise ValueError(f"{label}에는 상대 경로를 사용하세요: {href}")

    resolved_path = (metadata_path.parent / parsed_href.path).resolve()
    if not resolved_path.is_file():
        raise FileNotFoundError(f"{label}가 가리키는 파일이 없습니다: {href}")
    return resolved_path


if __name__ == "__main__":
    main()
