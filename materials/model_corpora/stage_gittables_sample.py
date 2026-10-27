#!/usr/bin/env python3
"""Stage a small, license-filtered GitTables sample as Jitsuris label sheets.

This is a quarantine/staging importer. It never writes materials/pool/batch_*.jsonl.
Raw archive bytes are held only in memory and are not committed.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
import time
import zipfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parents[2]
INVENTORY = ROOT / "materials/model_corpora/gittables_1m_v0.0.6_inventory_20261027.json"
REQUEST = ROOT / "materials/model_corpora/gittables_sample.request"
WORK_ROOT = ROOT / "materials/pool/work"

# Small, permissive SPDX subset for this pilot. Per-table license metadata is retained.
ALLOWED_SPDX = {
    "mit", "apache-2.0", "bsd-2-clause", "bsd-3-clause", "cc-by-4.0",
    "cc0-1.0", "isc", "mpl-2.0",
}
PII_HEADER = re.compile(
    r"(^|[^a-z0-9])(e-?mail|phone|telephone|mobile|fax|ssn|social security|"
    r"passport|national id|personal id|first name|last name|full name|given name|"
    r"family name|person name|contact name|username|user name|patient|client|customer|"
    r"employee|student|home address|street address|postal address|postcode|zip code|"
    r"date of birth|birth date)([^a-z0-9]|$)", re.I
)
PII_VALUE = re.compile(
    r"(?:[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,})|"
    r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)|"
    r"(?<!\d)\+?\d[\d ().-]{8,}\d(?!\d)",
    re.I,
)
PERSON_RECORD_PATH = re.compile(
    r"(patient|employee|student|customer|contact|user[-_ ]?record|person[-_ ]?record|"
    r"obituar|birth[-_ ]?record|court[-_ ]?record|immigration[-_ ]?record|"
    r"complaint|case[-_ ]?file|criminal|offender|beneficiar)", re.I
)


def fail(message: str, out_dir: Path | None = None) -> None:
    if out_dir is not None:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "ingest_error.json").write_text(
            json.dumps({"status": "error", "message": message}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    raise SystemExit(message)


def read_request(path: Path) -> dict:
    req = json.loads(path.read_text(encoding="utf-8"))
    batch = str(req.get("batch", ""))
    topic = str(req.get("topic", ""))
    limit = req.get("max_tables", 20)
    if not re.fullmatch(r"b0[0-9]{2}", batch):
        raise ValueError("batch must use b0NN format")
    if not re.fullmatch(r"[a-z0-9_]+", topic):
        raise ValueError("topic must contain lowercase letters, digits, and underscores")
    if not isinstance(limit, int) or not (1 <= limit <= 20):
        raise ValueError("max_tables must be between 1 and 20")
    return {"batch": batch, "topic": topic, "max_tables": limit}


def download(url: str, expected_bytes: int, expected_md5: str) -> bytes:
    last_error = None
    for attempt in range(5):
        try:
            req = Request(url, headers={"User-Agent": "Jitsuris-training-material-review/1.0"})
            with urlopen(req, timeout=180) as response:
                data = response.read(expected_bytes + 1)
            if len(data) != expected_bytes:
                raise ValueError(f"archive size mismatch: expected {expected_bytes}, got {len(data)}")
            actual = hashlib.md5(data).hexdigest()
            if actual.lower() != expected_md5.lower():
                raise ValueError(f"archive MD5 mismatch: expected {expected_md5}, got {actual}")
            return data
        except (HTTPError, URLError, TimeoutError, OSError, ValueError) as exc:
            last_error = str(exc)
            if attempt < 4:
                time.sleep(min(5 * (2 ** attempt), 30))
    raise RuntimeError(f"official Zenodo download failed after 5 attempts: {last_error}")


def canonical_url(url: str) -> str:
    p = urlparse(str(url or "").strip())
    host = (p.hostname or "").lower()
    path = unquote(p.path or "")
    parts = [x for x in path.split("/") if x]
    if host == "raw.githubusercontent.com" and len(parts) >= 4:
        # Treat raw and blob links to the same repository path as a duplicate.
        host, parts = "github.com", parts[:2] + parts[3:]
    elif host == "github.com" and len(parts) >= 5 and parts[2] in ("blob", "raw"):
        parts = parts[:2] + parts[4:]
    return f"{host}/{'/'.join(parts)}".lower()


def known_table_urls() -> set[str]:
    urls: set[str] = set()
    pool = ROOT / "materials/pool"
    for path in list(pool.glob("batch_*.jsonl")) + list((ROOT / "materials").glob("real_*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            for key in ("table", "resource_page"):
                value = row.get(key)
                if value:
                    urls.add(canonical_url(value))
    prov = ROOT / "independent_eval/results/main/provenance.json"
    if prov.exists():
        for table in json.loads(prov.read_text(encoding="utf-8")).get("tables", []):
            for key in ("resource_url", "request_url"):
                if table.get(key):
                    urls.add(canonical_url(table[key]))
    return urls


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def license_record(meta: dict) -> tuple[str, dict]:
    raw = meta.get("license") or {}
    if isinstance(raw, dict) and isinstance(raw.get("license"), dict):
        raw = raw["license"]
    if not isinstance(raw, dict):
        return "", {}
    spdx = str(raw.get("spdx_id") or "").strip().lower()
    return spdx, raw


def publisher_from_url(url: str) -> str:
    p = urlparse(url)
    parts = [x for x in p.path.split("/") if x]
    if p.hostname in ("github.com", "raw.githubusercontent.com") and len(parts) >= 2:
        owner_repo = f"{parts[0]}/{parts[1]}"
        return "github:" + owner_repo.lower()
    return "github:unknown"


def get_weak_annotations(meta: dict, column: str) -> dict:
    out = {}
    for key in (
        "dbpedia_semantic_column_types", "dbpedia_syntactic_column_types",
        "schema_semantic_column_types", "schema_syntactic_column_types",
    ):
        value = (meta.get(key) or {}).get(column)
        if value:
            out[key] = value
    return out


def safe_columns(table, meta: dict) -> tuple[list[dict], dict]:
    names = list(table.column_names)
    if len(names) != len(set(names)):
        return [], {"reason": "duplicate_headers", "dropped_pii_headers": 0, "dropped_pii_values": 0}
    safe_names, headers_dropped, value_dropped = [], 0, 0
    columns = {}
    for name in names:
        if PII_HEADER.search(str(name)):
            headers_dropped += 1
            continue
        values = [as_text(v).strip() for v in table[name].to_pylist()]
        nonempty = [v for v in values if v]
        if not nonempty:
            continue
        if any(PII_VALUE.search(v) for v in nonempty[:50]):
            value_dropped += 1
            continue
        safe_names.append(name)
        columns[name] = nonempty
    if len(safe_names) < 2 or headers_dropped + value_dropped >= max(2, len(names) // 2):
        return [], {
            "reason": "too_few_safe_columns",
            "dropped_pii_headers": headers_dropped,
            "dropped_pii_values": value_dropped,
        }
    rows = []
    source_url = str(meta.get("table_csv_url") or "")
    publisher = publisher_from_url(source_url)
    language = "en" if all(ord(ch) < 128 for name in safe_names for ch in str(name)) else "und"
    for name in safe_names:
        values = columns[name][:5]
        if not values:
            continue
        context = [str(x) for x in safe_names if x != name][:8]
        rows.append({
            "source": "world:gittables-v0.0.6",
            "language": language,
            "table": source_url,
            "resource_page": source_url,
            "publisher": publisher,
            "pool": "train",
            "license": str((meta.get("license") or {}).get("license", {}).get("spdx_id") or ""),
            "unit": "",
            "header": str(name),
            "values": values,
            "context": context,
            "gittables_table_id": meta.get("table_id"),
            "gittables_topic": meta.get("table_domain", {}),
            "gittables_weak_labels_present": bool(get_weak_annotations(meta, str(name))),
        })
    return rows, {
        "reason": "",
        "dropped_pii_headers": headers_dropped,
        "dropped_pii_values": value_dropped,
    }


def main() -> int:
    out_dir = None
    try:
        req = read_request(REQUEST)
        batch = req["batch"]
        out_dir = WORK_ROOT / batch
        if out_dir.exists():
            raise ValueError(f"{out_dir} already exists; use a new batch id")
        out_dir.mkdir(parents=True)
        inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
        filename = f"{req['topic']}_tables_licensed.zip"
        entry = next((f for f in inventory.get("files", []) if f.get("name") == filename), None)
        if not entry:
            raise ValueError(f"topic archive not found in verified inventory: {filename}")
        expected_md5 = str(entry["checksum"]).removeprefix("md5:")
        archive = download(entry["official_content_url"], int(entry["size_bytes"]), expected_md5)
        known = known_table_urls()
        selected, table_records, excluded = [], [], []
        with zipfile.ZipFile(io.BytesIO(archive)) as zf:
            members = sorted(
                (x for x in zf.infolist() if x.filename.lower().endswith(".parquet") and not x.is_dir()),
                key=lambda x: hashlib.sha256(x.filename.encode("utf-8")).hexdigest(),
            )
            for member in members:
                if len(selected) >= req["max_tables"]:
                    break
                if member.file_size > 50_000_000:
                    excluded.append({"file": member.filename, "reason": "parquet_over_50mb"})
                    continue
                try:
                    blob = zf.read(member)
                    table = pq.read_table(io.BytesIO(blob))
                    raw_meta = (table.schema.metadata or {}).get(b"gittables")
                    if not raw_meta:
                        excluded.append({"file": member.filename, "reason": "missing_gittables_metadata"})
                        continue
                    meta = json.loads(raw_meta.decode("utf-8"))
                    source_url = str(meta.get("table_csv_url") or "")
                    spdx, raw_license = license_record(meta)
                    if not source_url or not spdx:
                        excluded.append({"file": member.filename, "reason": "missing_source_or_spdx"})
                        continue
                    if spdx not in ALLOWED_SPDX:
                        excluded.append({"file": member.filename, "reason": "license_outside_pilot_allowlist", "spdx_id": spdx})
                        continue
                    if PERSON_RECORD_PATH.search(urlparse(source_url).path):
                        excluded.append({"file": member.filename, "reason": "personal_record_source_path", "source_url": source_url})
                        continue
                    if canonical_url(source_url) in known:
                        excluded.append({"file": member.filename, "reason": "exact_source_url_already_in_pool", "source_url": source_url})
                        continue
                    col_rows, screening = safe_columns(table, meta)
                    if not col_rows:
                        excluded.append({"file": member.filename, "reason": screening["reason"], "source_url": source_url})
                        continue
                    digest = hashlib.sha256(blob).hexdigest()
                    table_id = meta.get("table_id")
                    license_info = {
                        "spdx_id": spdx,
                        "name": raw_license.get("name", ""),
                        "url": raw_license.get("url", ""),
                        "key": raw_license.get("key", ""),
                    }
                    # Keep provenance and original weak annotations out of the label sheet.
                    annotations = {
                        col: get_weak_annotations(meta, col)
                        for col in table.column_names if get_weak_annotations(meta, col)
                    }
                    table_record = {
                        "n": len(selected) + 1,
                        "table_id": table_id,
                        "source_url": source_url,
                        "publisher": publisher_from_url(source_url),
                        "license": license_info,
                        "rows": int(table.num_rows),
                        "columns": int(table.num_columns),
                        "parquet_sha256": digest,
                        "archive_member": member.filename,
                        "dropped_pii_headers": screening["dropped_pii_headers"],
                        "dropped_pii_values": screening["dropped_pii_values"],
                        "anonymized_columns": meta.get("anonymized_columns", []),
                        "weak_annotations": annotations,
                    }
                    for row in col_rows:
                        row["license"] = spdx
                        row["source_license"] = license_info
                        row["table_sha256"] = digest
                        row["gittables_archive"] = filename
                    selected.extend(col_rows)
                    table_records.append(table_record)
                except Exception as exc:
                    excluded.append({"file": member.filename, "reason": f"parse_error:{type(exc).__name__}"})
        if not table_records:
            reason_counts = {
                reason: sum(1 for item in excluded if item["reason"] == reason)
                for reason in sorted({item["reason"] for item in excluded})
            }
            extension_counts = {}
            for member in zf.infolist():
                if member.is_dir():
                    continue
                suffix = Path(member.filename).suffix.lower() or "(no extension)"
                extension_counts[suffix] = extension_counts.get(suffix, 0) + 1
            diagnostic = {
                "status": "error",
                "message": "no tables passed source, license, deduplication, and privacy filters",
                "topic_archive": filename,
                "archive_member_count": len(zf.infolist()),
                "parquet_member_count": len(members),
                "archive_extensions": extension_counts,
                "excluded_count": len(excluded),
                "excluded_summary": reason_counts,
                "excluded_examples": [
                    {
                        "file": Path(item["file"]).name,
                        "reason": item["reason"],
                        **({"spdx_id": item["spdx_id"]} if item.get("spdx_id") else {}),
                    }
                    for item in excluded[:12]
                ],
            }
            (out_dir / "ingest_error.json").write_text(
                json.dumps(diagnostic, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            raise SystemExit(
                "RuntimeError: no tables passed filters; see ingest_error.json for aggregate reasons"
            )
        write_jsonl(out_dir / "corpus.jsonl", selected)
        (out_dir / "source_manifest.json").write_text(
            json.dumps({
                "status": "staged_for_independent_labeling",
                "batch": batch,
                "dataset": "GitTables 1M v0.0.6",
                "dataset_doi": "10.5281/zenodo.6517052",
                "topic_archive": filename,
                "archive_size_bytes": int(entry["size_bytes"]),
                "archive_md5": expected_md5,
                "dataset_license_page": "https://gittables.github.io/",
                "selected_table_count": len(table_records),
                "selected_column_count": len(selected),
                "selected_tables": table_records,
                "excluded_count": len(excluded),
                "excluded_summary": {
                    reason: sum(1 for x in excluded if x["reason"] == reason)
                    for reason in sorted({x["reason"] for x in excluded})
                },
                "license_allowlist": sorted(ALLOWED_SPDX),
                "test_benchmark_included": False,
            }, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        adopted = {
            "schema_version": 1,
            "batch": batch,
            "decided_by": "GitTables v0.0.6 staging importer; per-table SPDX allowlist; no final pool import",
            "decided_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "candidate_count": len(members),
            "adopted": [
                {
                    "n": i,
                    "publisher_id": t["publisher"],
                    "resource_url": t["source_url"],
                    "title": t["archive_member"],
                    "platform": "gittables",
                    "host": "github.com",
                    "resource_id": str(t["table_id"]),
                    "access": "parquet",
                    "license": t["license"]["spdx_id"],
                }
                for i, t in enumerate(table_records, 1)
            ],
            "dropped": {"license_privacy_source_or_duplicate_filter": len(excluded)},
        }
        (out_dir / "adopted.json").write_text(json.dumps(adopted, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        report = {
            "status": "label_sheets_pending",
            "batch": batch,
            "topic": req["topic"],
            "tables": len(table_records),
            "columns": len(selected),
            "excluded_tables": len(excluded),
            "archive_md5_verified": True,
            "only_allowlisted_per_table_licenses": True,
            "exact_source_url_dedup": True,
            "raw_archive_committed": False,
        }
        (out_dir / "ingest_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False))
        return 0
    except Exception as exc:
        fail(f"{type(exc).__name__}: {exc}", out_dir)
    return 1


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
