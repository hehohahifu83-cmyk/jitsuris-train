#!/usr/bin/env python3
"""Freeze and extract a small, licensed independent evaluation set.

Discovery remains metadata-only. This command downloads only allowlisted public
resources, keeps the first five rows in memory, validates only the selected
columns, and writes the schema-v1 set plus source/hash provenance. It never
writes labels, full source files, or blind-set contents.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST_PATH = ROOT / "independent_eval" / "allowlist.json"
REQUEST_PATH = ROOT / "independent_eval" / "extract.request"
CANDIDATES_PATH = ROOT / "independent_eval" / "results" / "discovery" / "candidates.json"
MANIFEST_PATH = ROOT / "independent_eval" / "manifest.json"
CORPUS_PATH = ROOT / "materials" / "real_corpus_jp2.jsonl"
OUT_DIR = ROOT / "independent_eval" / "results" / "main"
SET_PATH = OUT_DIR / "independent_main.json"
PROVENANCE_PATH = OUT_DIR / "provenance.json"
ATTRIBUTION_PATH = OUT_DIR / "ATTRIBUTION.md"
MAX_RESPONSE_BYTES = 25_000_000
REQUIRED_ROWS = 5

EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE_RE = re.compile(r"(?<!\w)(?:\+?\d[\d .()/-]{7,}\d)(?!\w)")
POSTAL_RE = re.compile(r"(?<!\d)(?:〒?\s*\d{3}-?\d{4}|\d{5}(?:-\d{4})?)(?!\d)")
STREET_RE = re.compile(
    r"\b\d{1,6}\s+[A-Z0-9.' -]{2,40}\s+(?:ST|STREET|AVE|AVENUE|RD|ROAD|BLVD|BOULEVARD|DR|DRIVE|LN|LANE)\b",
    re.I,
)


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def read_json(path: Path):
    return json.loads(read_bytes(path).decode("utf-8"))


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    payload = b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
    return hashlib.sha1(payload).hexdigest()


def normalize_header(value: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value)).strip()).casefold()


def sensitive_value(value: str) -> bool:
    value = str(value or "").strip()
    return bool(
        value
        and (
            EMAIL_RE.search(value)
            or PHONE_RE.search(value)
            or POSTAL_RE.search(value)
            or STREET_RE.search(value)
        )
    )


def source_policy(manifest: dict) -> dict[str, dict]:
    return {str(item["id"]): item for item in manifest.get("sources", [])}


def normalize_url(value: str) -> str:
    parsed = urlparse(str(value))
    return parsed._replace(query="", fragment="").geturl().rstrip("/").lower()


def verify_frozen_plan():
    allow_raw = read_bytes(ALLOWLIST_PATH)
    allow = json.loads(allow_raw.decode("utf-8"))
    candidates_raw = read_bytes(CANDIDATES_PATH)
    candidates = json.loads(candidates_raw.decode("utf-8"))
    manifest = read_json(MANIFEST_PATH)
    corpus_raw = read_bytes(CORPUS_PATH)

    if allow.get("schema_version") != 1 or allow.get("status") != "frozen":
        raise ValueError("allowlist schema/status is not frozen v1")
    if allow.get("candidate_file_git_blob_sha1") != git_blob_sha1(candidates_raw):
        raise ValueError("candidate metadata changed after review; refresh and re-review before extraction")
    if allow.get("training_corpus_git_blob_sha1") != git_blob_sha1(corpus_raw):
        raise ValueError("training corpus changed after overlap review; re-run overlap review before extraction")
    if candidates.get("sample_values_written") is not False:
        raise ValueError("discovery metadata unexpectedly contains sample values")
    if candidates.get("labels_written") is not False or candidates.get("blind_sets_read") is not False:
        raise ValueError("discovery safety flags are not clean")
    if allow.get("blind_sets_read") is not False or allow.get("labels", {}).get("stored") is not False:
        raise ValueError("allowlist says labels or blind data were used")

    source_specs = source_policy(manifest)
    candidate_index = {
        (str(item.get("source_id")), str(item.get("dataset_id")), str(item.get("resource_id"))): item
        for item in candidates.get("candidates", [])
    }
    corpus_rows = [
        json.loads(line)
        for line in corpus_raw.decode("utf-8").splitlines()
        if line.strip()
    ]
    if len(corpus_rows) != int(allow.get("training_corpus_records", -1)):
        raise ValueError("training corpus record count changed after review")

    table_ids = set()
    resource_ids = set()
    dataset_ids = set()
    sources = set()
    languages = set()
    all_urls = []
    expected_columns = 0
    reviewed_tables = []

    for table in allow.get("tables", []):
        tid = str(table.get("table_id", ""))
        source_id = str(table.get("source_id", ""))
        dataset_id = str(table.get("dataset_id", ""))
        resource_id = str(table.get("resource_id", ""))
        key = (source_id, dataset_id, resource_id)
        if not tid or tid in table_ids:
            raise ValueError(f"table id missing/duplicate: {tid}")
        if key in resource_ids:
            raise ValueError(f"source resource is duplicated: {tid}")
        table_ids.add(tid)
        resource_ids.add(key)
        dataset_ids.add((source_id, dataset_id))
        sources.add(source_id)
        languages.add(str(table.get("language", "")))

        candidate = candidate_index.get(key)
        if candidate is None:
            raise ValueError(f"allowlisted source resource not found in reviewed candidate metadata: {tid}")
        if table.get("resource_url") != candidate.get("resource_url"):
            raise ValueError(f"resource URL changed after review: {tid}")
        if table.get("catalog_url") != candidate.get("catalog_url"):
            raise ValueError(f"catalog URL changed after review: {tid}")
        if table.get("title") != candidate.get("title"):
            raise ValueError(f"dataset title changed after review: {tid}")
        if table.get("language") != candidate.get("language"):
            raise ValueError(f"dataset language changed after review: {tid}")
        candidate_license = candidate.get("license") or {}
        if table.get("license_id") != candidate_license.get("id"):
            raise ValueError(f"dataset license changed after review: {tid}")
        if candidate.get("sample_values_written") is not False or candidate.get("labels_written") is not False:
            raise ValueError(f"discovery candidate safety flags are not clean: {tid}")
        if "[有償]" in str(candidate.get("title", "")) or re.search(r"\bpaid\b", str(candidate.get("title", "")), re.I):
            raise ValueError(f"paid candidate is blocked: {tid}")

        spec = source_specs.get(source_id)
        if not spec:
            raise ValueError(f"source is missing from manifest: {source_id}")
        url = str(table.get("resource_url", ""))
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.hostname:
            raise ValueError(f"resource URL must be HTTPS: {tid}")
        if spec.get("kind") == "socrata":
            if source_id != "nyc" or parsed.hostname != spec.get("domain"):
                raise ValueError(f"NYC resource host mismatch: {tid}")
            if parsed.path.rstrip("/") != f"/resource/{dataset_id}.csv":
                raise ValueError(f"NYC resource path does not match dataset id: {tid}")
            if table.get("license_id") != "NYC Open Data public-dataset policy":
                raise ValueError(f"NYC dataset policy marker missing: {tid}")
        else:
            if table.get("license_id") not in set(spec.get("license_ids") or []):
                raise ValueError(f"dataset is outside the accepted individual license ids: {tid}")
            allowed_hosts = set(spec.get("allowed_hosts") or [])
            if parsed.hostname not in allowed_hosts:
                raise ValueError(f"resource host is outside the source allowlist: {tid}")

        headers = table.get("selected_headers")
        if not isinstance(headers, list) or not headers or len(headers) > 10:
            raise ValueError(f"selected heading count is outside 1..10: {tid}")
        if len({normalize_header(h) for h in headers}) != len(headers):
            raise ValueError(f"duplicate selected heading: {tid}")
        safe = {normalize_header(h) for h in candidate.get("safe_headers") or []}
        if any(normalize_header(h) not in safe for h in headers):
            raise ValueError(f"selected heading was not safety-scanned in discovery: {tid}")
        expected_columns += len(headers)
        all_urls.append(url)
        reviewed_tables.append((table, candidate))

    if len(table_ids) < 30 or expected_columns < 300 or len(sources) < 4 or len(languages) < 2:
        raise ValueError("frozen plan is below minimum table, column, source, or language counts")
    overlap = {
        normalize_url(item.get("table", ""))
        for item in corpus_rows
    }.intersection(normalize_url(url) for url in all_urls)
    if overlap:
        raise ValueError(f"selected source URL overlaps training corpus: {len(overlap)}")
    if int(allow.get("exact_resource_url_overlap_count", -1)) != 0:
        raise ValueError("allowlist does not record a zero training URL overlap")

    summary = {
        "tables": len(table_ids),
        "columns": expected_columns,
        "sources": len(sources),
        "languages": len(languages),
        "datasets": len(dataset_ids),
        "exact_training_url_overlaps": 0,
    }
    if allow.get("selection_summary") != {
        "tables": summary["tables"],
        "columns": summary["columns"],
        "sources": summary["sources"],
        "languages": summary["languages"],
        "datasets": summary["datasets"],
    }:
        raise ValueError("allowlist selection summary does not match the frozen resources")
    return allow, allow_raw, candidates, candidates_raw, manifest, corpus_rows, reviewed_tables, summary


def csv_header_and_first_rows(raw: bytes, table_id: str):
    decoded = None
    for encoding in ("utf-8-sig", "utf-8", "cp932", "utf-16"):
        try:
            decoded = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    if decoded is None:
        raise ValueError(f"{table_id}: source CSV encoding is unsupported")
    try:
        dialect = csv.Sniffer().sniff(decoded[:4096], delimiters=",\t;")
        delimiter = dialect.delimiter
    except csv.Error:
        delimiter = ","

    reader = csv.reader(io.StringIO(decoded), delimiter=delimiter)
    header = None
    for _ in range(5):
        row = next(reader, None)
        if row is None:
            break
        cleaned = [str(value).strip().lstrip("\ufeff") for value in row]
        if len(cleaned) >= 10 and len({value for value in cleaned if value}) >= 8:
            header = cleaned
            break
    if header is None:
        raise ValueError(f"{table_id}: no recognizable header in first five records")

    samples = []
    for row in reader:
        if len(row) >= len(header):
            samples.append([str(value) for value in row[: len(header)]])
            if len(samples) == REQUIRED_ROWS:
                break
    if len(samples) != REQUIRED_ROWS:
        raise ValueError(f"{table_id}: source returned fewer than five data rows")
    return header, samples


def download_table(table: dict, allowed_hosts: set[str]):
    url = str(table["resource_url"])
    if table["source_id"] == "nyc":
        url = url + "?" + urlencode({"$limit": str(REQUIRED_ROWS)})
    request = Request(
        url,
        headers={"User-Agent": "jitsuris-independent-eval/1.0 (source and license recorded)"},
    )
    try:
        with urlopen(request, timeout=60) as response:
            final_url = response.geturl()
            final_host = urlparse(final_url).hostname
            if final_host not in allowed_hosts:
                raise ValueError(f"{table['table_id']}: download redirected outside the reviewed host allowlist")
            raw = response.read(MAX_RESPONSE_BYTES + 1)
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError(f"{table['table_id']}: source download failed ({type(exc).__name__})") from None
    if len(raw) > MAX_RESPONSE_BYTES:
        raise ValueError(f"{table['table_id']}: source response exceeds the reviewed size limit")
    return url, raw


def set_record_id(index: int) -> str:
    return f"c{index:03d}"


def write_json(path: Path, data) -> bytes:
    raw = (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return raw


def make_attribution(allow: dict, provenance_tables: list[dict]) -> str:
    lines = [
        "# 独立評価主セットの出典",
        "",
        f"- セット ID: {allow['set_id']}",
        "- 収録: 各表で固定した列の先頭5データ行。元データ全体は収録せず、ラベルも含みません。",
        "- 変更: 選択列・先頭5行の抽出。個別の出典・ライセンス・版・SHA-256 は下表と provenance.json に記録しています。",
        "- 統合セットに一括のライセンスを付けず、各データに記載された条件を適用します。",
        "",
        "## 出典・ライセンス",
        "",
        "| 表 | 出典・データセット | ライセンス表示 | リソース |",
        "| --- | --- | --- | --- |",
    ]
    for item in provenance_tables:
        title = str(item["title"]).replace("|", "\\|")
        publisher = str(item.get("publisher") or item["source_id"]).replace("|", "\\|")
        catalog = item["catalog_url"]
        resource = item["resource_url"]
        if item["source_id"] == "nyc":
            license_text = "NYC Open Data public-dataset policy; source/version retained"
        else:
            license_text = f"{item.get('license_title') or item.get('license_id')} ({item.get('license_id')})"
        lines.append(
            f"| {item['table_id']} | {publisher}: [{title}]({catalog}) | {license_text} | [CSV]({resource}) |"
        )
    lines.extend(
        [
            "",
            "## 利用条件の確認先",
            "",
        ]
    )
    for source_id, review in allow.get("source_review", {}).items():
        lines.append(f"- {source_id}: {review['policy_url']}")
        if review.get("law_url"):
            lines.append(f"  NYC source/version rule: {review['law_url']}")
    lines.extend(
        [
            "",
            "NYC Open Data の公式 FAQ は利用制限なしと説明しています。市のオープンデータ法は、第三者による公開時に出典・版・変更内容を明示できるとしています。本セットは出典・リソース・取得スナップショットのハッシュを残し、列と先頭5行だけを抽出した変更を記録します。",
            "",
            "このファイルは、元データの権利・条件を置き換えません。各行のデータセットに表示された利用条件と出典を確認してください。",
            "",
        ]
    )
    return "\n".join(lines)


def run_self_test():
    assert sensitive_value("person@example.com")
    assert sensitive_value("+1 (212) 555-0199")
    assert sensitive_value("100 Main Street")
    assert sensitive_value("10001")
    assert not sensitive_value("2026-10-20T12:00:00")
    headings = [f"h{i}" for i in range(10)]
    rows = [headings] + [[f"v{r}-{c}" for c in range(10)] for r in range(5)]
    fixture = ("\n".join(",".join(row) for row in rows)).encode("utf-8")
    parsed_headers, sample_rows = csv_header_and_first_rows(fixture, "self-test")
    assert parsed_headers == headings and len(sample_rows) == 5
    print("SELF_TEST_OK privacy-patterns=4 csv-rows=5; values omitted")


def main(dry_run: bool = False):
    allow, allow_raw, candidates, candidates_raw, manifest, corpus_rows, reviewed_tables, summary = verify_frozen_plan()
    if dry_run:
        print(
            "DRY_RUN_OK "
            + " ".join(f"{key}={value}" for key, value in summary.items())
            + f" candidate_git_blob={git_blob_sha1(candidates_raw)}"
        )
        return

    request = read_json(REQUEST_PATH)
    if request.get("set_id") != allow.get("set_id"):
        raise ValueError("extract.request set_id does not match the frozen allowlist")
    if request.get("candidate_file_git_blob_sha1") != allow.get("candidate_file_git_blob_sha1"):
        raise ValueError("extract.request candidate pin does not match the frozen allowlist")
    if SET_PATH.exists() or PROVENANCE_PATH.exists() or ATTRIBUTION_PATH.exists():
        raise ValueError("main set already exists; refusing to replace a frozen evaluation snapshot")

    source_specs = source_policy(manifest)
    columns = []
    provenance_tables = []
    column_number = 0
    created_utc = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

    for table, _candidate in reviewed_tables:
        spec = source_specs[table["source_id"]]
        allowed_hosts = set(spec.get("allowed_hosts") or [])
        if spec.get("kind") == "socrata":
            allowed_hosts = {str(spec["domain"])}
        request_url, raw = download_table(table, allowed_hosts)
        headers, sample_rows = csv_header_and_first_rows(raw, table["table_id"])

        normalized = {}
        for index, header in enumerate(headers):
            normalized.setdefault(normalize_header(header), []).append(index)
        positions = {}
        actual_headers = {}
        for expected in table["selected_headers"]:
            matches = normalized.get(normalize_header(expected), [])
            if len(matches) != 1:
                raise ValueError(f"{table['table_id']}: selected heading missing/ambiguous: {expected}")
            positions[expected] = matches[0]
            actual_headers[expected] = headers[matches[0]]

        for expected in table["selected_headers"]:
            position = positions[expected]
            values = [str(row[position]).strip() for row in sample_rows]
            if not any(value for value in values):
                raise ValueError(f"{table['table_id']}: selected heading has no nonempty examples: {expected}")
            for value in values:
                if len(value) > 500:
                    raise ValueError(f"{table['table_id']}: selected example exceeds 500 characters: {expected}")
                if sensitive_value(value):
                    raise ValueError(f"{table['table_id']}: sample safety pattern found in selected heading: {expected}")
            siblings = [
                actual_headers[name]
                for name in table["selected_headers"]
                if name != expected
            ]
            column_number += 1
            columns.append(
                {
                    "id": set_record_id(column_number),
                    "table": table["table_id"],
                    "source": table["source_id"],
                    "language": table["language"],
                    "header": actual_headers[expected],
                    "values": values,
                    "siblings": siblings,
                    "unit": "",
                }
            )

        policy = allow["source_review"][table["source_id"]]
        provenance_tables.append(
            {
                "table_id": table["table_id"],
                "source_id": table["source_id"],
                "language": table["language"],
                "dataset_id": table["dataset_id"],
                "resource_id": table["resource_id"],
                "title": table["title"],
                "publisher": table.get("publisher", ""),
                "catalog_url": table["catalog_url"],
                "resource_url": table["resource_url"],
                "request_url": request_url,
                "license_id": table["license_id"],
                "license_title": table.get("license_title", ""),
                "license_url": table.get("license_url", ""),
                "policy_url": policy["policy_url"],
                "metadata_updated": table.get("metadata_updated", ""),
                "selected_headers": [actual_headers[name] for name in table["selected_headers"]],
                "download_sha256": sha256_bytes(raw),
                "sample_data_rows": REQUIRED_ROWS,
                "redistribution_review": "source terms checked; only selected headings and first five rows retained",
            }
        )

    set_data = {
        "schema_version": 1,
        "set_id": allow["set_id"],
        "columns": columns,
    }
    set_raw = (json.dumps(set_data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")

    # Validate the exact same schema consumed by independent evaluation.
    sys.path.insert(0, str(ROOT))
    from evaluate_independent import load_set

    SET_PATH.parent.mkdir(parents=True, exist_ok=True)
    SET_PATH.write_bytes(set_raw)
    loaded, loaded_sha = load_set(SET_PATH)
    if loaded_sha != sha256_bytes(set_raw) or len(loaded["columns"]) != len(columns):
        raise ValueError("schema-v1 validation did not preserve the frozen set")

    provenance = {
        "schema_version": 1,
        "set_id": allow["set_id"],
        "created_utc": created_utc,
        "frozen_at_jst": allow["frozen_at_jst"],
        "candidate_file_git_blob_sha1": allow["candidate_file_git_blob_sha1"],
        "training_corpus": {
            "path": allow["training_corpus_file"],
            "git_blob_sha1": allow["training_corpus_git_blob_sha1"],
            "records": len(corpus_rows),
            "exact_resource_url_overlap_count": 0,
        },
        "allowlist_sha256": sha256_bytes(allow_raw),
        "set_path": str(SET_PATH.relative_to(ROOT)),
        "set_sha256": loaded_sha,
        "table_count": len(provenance_tables),
        "column_count": len(columns),
        "labels_written": False,
        "blind_sets_read": False,
        "raw_source_files_written": False,
        "tables": provenance_tables,
    }
    write_json(PROVENANCE_PATH, provenance)
    ATTRIBUTION_PATH.write_text(make_attribution(allow, provenance_tables), encoding="utf-8")

    print(
        "EXTRACTION_OK "
        f"set_id={allow['set_id']} tables={len(provenance_tables)} columns={len(columns)} "
        f"set_sha256={loaded_sha} allowlist_sha256={provenance['allowlist_sha256']} "
        "labels=none raw_csv=none blind_sets=unread"
    )


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        run_self_test()
    else:
        main(dry_run="--dry-run" in sys.argv)
