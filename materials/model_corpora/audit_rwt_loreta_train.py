#!/usr/bin/env python3
"""Metadata-only rights preflight for the pinned RWT-RuTaBERT train split.

This tool verifies LoReTA train shard Git blob IDs and emits page/table IDs plus
reconstructed Wikipedia page links. It never writes cell text, source labels,
or answer sheets. A successful run is not rights clearance and does not permit
staging.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY = ROOT / "materials/model_corpora/rights_approved_sources.json"
SOURCE_ID = "rwt_loreta_rutabert"
TABLE_ID = re.compile(r"^(?:dataset/)?Dataset/data/(?P<page_id>[0-9]+)/table_(?P<offset>[0-9]+)$")
REQUIRED_COLUMNS = {"table_id", "column_id", "label_id", "label", "column_data"}
OUTPUT_COLUMN_FIELDS = [
    "table_id", "page_id", "table_offset", "column_id", "wikipedia_page_url",
    "snapshot_date", "rights_status", "source_label_excluded",
]


def git_blob_sha(path: Path) -> str:
    size = path.stat().st_size
    digest = hashlib.sha1()
    digest.update(f"blob {size}\0".encode("ascii"))
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_source_record(registry_path: Path) -> dict:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    matches = [item for item in registry.get("held_sources", []) if item.get("id") == SOURCE_ID]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one held-source record for {SOURCE_ID}")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("loreta_root", type=Path, help="Local LoReTA checkout at the pinned revision")
    parser.add_argument("output_dir", type=Path, help="Local directory for metadata-only audit files")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()

    record = load_source_record(args.registry)
    if record.get("status") != "rights_hold_metadata_audit_only":
        raise ValueError("This script is only for metadata audit; check the held-source state.")
    train_dir = (args.loreta_root / "dataset/cta_dataset/train").resolve()
    if train_dir.name != "train" or not train_dir.is_dir():
        raise ValueError("Expected dataset/cta_dataset/train under the LoReTA checkout.")

    expected = {Path(item["path"]).name: item for item in record["train_shards"]}
    actual = {path.name: path for path in train_dir.glob("*.csv")}
    if set(actual) != set(expected):
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        raise ValueError(f"Train shard set mismatch; missing={missing}, extra={extra}")

    for name, path in actual.items():
        spec = expected[name]
        if path.stat().st_size != spec["size_bytes"] or git_blob_sha(path) != spec["blob_sha"]:
            raise ValueError(f"Pinned source mismatch: {name}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    column_path = args.output_dir / "rwt_train_column_source_index.csv.gz"
    page_path = args.output_dir / "rwt_train_source_pages.csv"
    page_ids: set[int] = set()
    table_ids: set[str] = set()
    total_rows = 0

    with gzip.open(column_path, "wt", encoding="utf-8", newline="") as compressed:
        writer = csv.DictWriter(compressed, fieldnames=OUTPUT_COLUMN_FIELDS)
        writer.writeheader()
        for name in sorted(expected, key=lambda value: int(re.search(r"data_(\d+)\.csv$", value).group(1))):
            with actual[name].open("r", encoding="utf-8-sig", newline="") as source:
                reader = csv.DictReader(source)
                fields = set(reader.fieldnames or [])
                if not REQUIRED_COLUMNS.issubset(fields):
                    raise ValueError(f"Unexpected schema in {name}: {sorted(fields)}")
                for line_number, row in enumerate(reader, start=2):
                    raw_id = row.get("table_id", "")
                    match = TABLE_ID.fullmatch(raw_id)
                    if match is None:
                        raise ValueError(f"Invalid table_id in {name}:{line_number}")
                    try:
                        column_id = int(row["column_id"])
                    except (TypeError, ValueError) as error:
                        raise ValueError(f"Invalid column_id in {name}:{line_number}") from error
                    if column_id < 0:
                        raise ValueError(f"Negative column_id in {name}:{line_number}")
                    page_id = int(match.group("page_id"))
                    offset = int(match.group("offset"))
                    page_ids.add(page_id)
                    table_ids.add(raw_id)
                    total_rows += 1
                    writer.writerow({
                        "table_id": raw_id,
                        "page_id": page_id,
                        "table_offset": offset,
                        "column_id": column_id,
                        "wikipedia_page_url": f"https://ru.wikipedia.org/?curid={page_id}",
                        "snapshot_date": "2021-09-13 (verify exact revision)",
                        "rights_status": "rights_hold_page_review_required",
                        "source_label_excluded": True,
                    })

    with page_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=["page_id", "wikipedia_page_url", "rights_status"])
        writer.writeheader()
        for page_id in sorted(page_ids):
            writer.writerow({
                "page_id": page_id,
                "wikipedia_page_url": f"https://ru.wikipedia.org/?curid={page_id}",
                "rights_status": "rights_hold_page_review_required",
            })

    summary = {
        "source_id": SOURCE_ID,
        "LoReTA_commit": record["pinned_commit"],
        "train_rows": total_rows,
        "unique_tables": len(table_ids),
        "unique_pages": len(page_ids),
        "test_rows_read": 0,
        "raw_values_written": False,
        "weak_labels_written": False,
        "label_sheets_created": False,
        "rights_status": "rights_hold",
        "outputs": [column_path.name, page_path.name],
    }
    (args.output_dir / "rwt_train_rights_audit_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"rwt preflight failed: {error}", file=sys.stderr)
        raise SystemExit(2)
