#!/usr/bin/env python3
"""Discover candidate open tables for an independent evaluation set.

Discovery emits metadata and safe header names only. It never writes sample values,
labels, blind-set contents, or raw source files. A reviewed allowlist is required
before the separate extraction stage is implemented and run.
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
MANIFEST_PATH = ROOT / "independent_eval" / "manifest.json"
OUT = ROOT / "independent_eval" / "results" / "discovery"
MAX_PREFIX = 512 * 1024
MAX_PACKAGE_ROWS = 2000
MAX_CKAN_RESOURCES = 240
MAX_NYC_IDS = 240
NYC_TERMS = ("summary", "statistics", "annual", "monthly", "counts", "population",
             "education", "transport", "environment", "budget", "sales")
TITLE_DENY = re.compile(
    r"(complaint|service request|incident|crash|collision|violation|inspection record|"
    r"employee|payroll|personnel|contact|telephone|email|住所|所在地|氏名|電話|メール|"
    r"個人|申請者|利用者|患者|児童生徒名|職員名)",
    re.I,
)
HEADER_DENY = re.compile(
    r"(^|[^a-z])(?:name|first|middle|last|full|person|individual|employee|student|"
    r"patient|customer|applicant|owner|contact|email|e-mail|phone|telephone|mobile|"
    r"address|street|block|postcode|postal|zip|latitude|longitude|coordinate|"
    r"account|member|licensee|complainant|requestor|reporter|url|free.?text|comment|"
    r"narrative|description|remark|note|detail|memo|ssn|dob|birth.?date|"
    r"住所|所在地|番地|町名|丁目|街区|郵便|氏名|名前|担当者|申請者|利用者|"
    r"連絡先|メール|電話|携帯|患者|児童|生徒|職員|従業員|生年月日|座標|緯度|経度)"
    r"($|[^a-z])",
    re.I,
)
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE_RE = re.compile(r"(?<!\w)(?:\+?\d[\d .()/-]{7,}\d)(?!\w)")
POSTAL_RE = re.compile(r"(?<!\d)(?:〒?\s*\d{3}-?\d{4}|\d{5}(?:-\d{4})?)(?!\d)")
STREET_RE = re.compile(
    r"\b\d{1,6}\s+[A-Z0-9.' -]{2,40}\s+(?:ST|STREET|AVE|AVENUE|RD|ROAD|BLVD|BOULEVARD|DR|DRIVE|LN|LANE)\b",
    re.I,
)
UNIT_RE = re.compile(
    r"^(?:unit|units|uom|unit of measure|measurement unit|単位|単位名|"
    r"(?:amt|amount)[-_ ]units?(?:[_ -].*)?)$", re.I
)

def http_bytes(url: str, limit: int | None = None) -> bytes:
    headers = {"User-Agent": "ai-bridge-independent-eval/1.0"}
    if limit is not None:
        headers["Range"] = f"bytes=0-{limit - 1}"
    req = Request(url, headers=headers)
    with urlopen(req, timeout=35) as resp:
        return resp.read((limit + 1) if limit is not None else 25_000_001)

def json_get(url: str):
    raw = http_bytes(url, 5_000_000)
    return json.loads(raw.decode("utf-8-sig"))

def normalize_header(value: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value)).strip()).casefold()

def blocked_title(title: str) -> bool:
    return bool(TITLE_DENY.search(title or ""))

def blocked_header(header: str) -> bool:
    return bool(HEADER_DENY.search(normalize_header(header)))

def sensitive_value(value: str) -> bool:
    value = str(value or "").strip()
    return bool(value and (EMAIL_RE.search(value) or PHONE_RE.search(value) or
                           POSTAL_RE.search(value) or STREET_RE.search(value)))

def read_csv_prefix(raw: bytes):
    decoded = None
    for encoding in ("utf-8-sig", "utf-8", "cp932", "utf-16"):
        try:
            decoded = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    if decoded is None:
        return None
    try:
        dialect = csv.Sniffer().sniff(decoded[:4096], delimiters=",\t;")
        delimiter = dialect.delimiter
    except csv.Error:
        delimiter = ","
    try:
        rows = list(csv.reader(io.StringIO(decoded), delimiter=delimiter))
    except csv.Error:
        return None
    # Require a recognizable first header row. Skip tables with preambles rather
    # than guessing, so discovery cannot silently misidentify the data columns.
    header_index = next((i for i, row in enumerate(rows[:5])
                         if len(row) >= 10 and len({c.strip() for c in row if c.strip()}) >= 8), None)
    if header_index is None:
        return None
    headers = [str(x).strip().lstrip("\ufeff") for x in rows[header_index]]
    body = [r for r in rows[header_index + 1:] if len(r) >= len(headers)]
    if len(body) < 5:
        return None
    return headers, body[:5]

def safe_headers(headers, rows):
    kept = []
    for i, name in enumerate(headers):
        if not name or blocked_header(name):
            continue
        vals = [str(row[i]).strip() for row in rows[:5] if i < len(row)]
        if not any(vals) or all(not v for v in vals):
            continue
        if any(sensitive_value(v) for v in vals):
            continue
        kept.append(name)
    return kept

def host_allowed(url: str, allowed_hosts: list[str]) -> bool:
    try:
        host = (urlparse(url).hostname or "").lower()
        return urlparse(url).scheme == "https" and any(
            host == d or host.endswith("." + d) for d in allowed_hosts
        )
    except Exception:
        return False

def ckan_packages(source):
    found = {}
    for license_id in source["license_ids"]:
        start = 0
        while start < MAX_PACKAGE_ROWS:
            query = urlencode({"fq": f"license_id:{license_id}", "rows": 100, "start": start,
                               "sort": "metadata_modified desc"})
            obj = json_get(source["api"] + "/package_search?" + query)
            if not obj.get("success"):
                break
            result = obj.get("result", {})
            page = result.get("results", [])
            for pkg in page:
                if pkg.get("state") == "active" and pkg.get("license_id") in source["license_ids"]:
                    found[pkg.get("id") or pkg.get("name")] = pkg
            start += len(page)
            if not page or start >= int(result.get("count", 0)):
                break
    return list(found.values())

def candidate_from_csv(source, title, dataset_id, resource_id, url, license_meta,
                       catalog_url, updated, size, source_extra=None):
    try:
        raw = http_bytes(url, MAX_PREFIX)
        parsed = read_csv_prefix(raw)
    except Exception as exc:
        return None
    if not parsed:
        return None
    headers, rows = parsed
    usable = safe_headers(headers, rows)
    if len(usable) < 10:
        return None
    return {
        "source_id": source["id"],
        "language": source["language"],
        "dataset_id": dataset_id,
        "resource_id": resource_id,
        "title": title,
        "catalog_url": catalog_url,
        "resource_url": url,
        "license": license_meta,
        "metadata_updated": updated or "",
        "resource_bytes": size,
        "header_count": len(headers),
        "safe_header_count": len(usable),
        "safe_headers": usable,
        "sample_rows_available": 5,
        "sample_values_written": False,
        "sample_safety": "first five rows scanned for contact/address patterns; values omitted",
        "manual_review_required": True,
        **(source_extra or {}),
    }

def discover_ckan(source):
    packages = ckan_packages(source)
    resources = []
    for pkg in packages:
        title = str(pkg.get("title") or pkg.get("name") or "")
        if blocked_title(title):
            continue
        org = (pkg.get("organization") or {}).get("title", "")
        license_meta = {
            "id": pkg.get("license_id", ""),
            "title": pkg.get("license_title", ""),
            "url": pkg.get("license_url", ""),
            "verification": "individual CKAN dataset metadata; exact accepted license_id",
        }
        for res in pkg.get("resources", []):
            if str(res.get("format") or "").strip().lower() != "csv":
                continue
            url = str(res.get("url") or "")
            if not host_allowed(url, source["allowed_hosts"]):
                continue
            try:
                size = int(res.get("size") or 0)
            except (TypeError, ValueError):
                size = 0
            if size > 50_000_000:
                continue
            resources.append((pkg, res, title, org, license_meta, size))
    resources.sort(key=lambda x: (normalize_header(x[2]), x[1].get("id", "")))
    out = []
    for pkg, res, title, org, license_meta, size in resources[:MAX_CKAN_RESOURCES]:
        candidate = candidate_from_csv(
            source, title, pkg.get("id") or pkg.get("name"), res.get("id"),
            res.get("url"), license_meta,
            source["catalog"] + (pkg.get("name") or ""),
            res.get("last_modified") or pkg.get("metadata_modified"), size,
            {"publisher": org}
        )
        if candidate:
            out.append(candidate)
    return out, len(packages)

def discover_nyc(source):
    ids = {}
    for term in NYC_TERMS:
        query = urlencode({"q": term, "search_context": source["domain"],
                           "domains": source["domain"], "limit": 100})
        try:
            obj = json_get("https://api.us.socrata.com/api/catalog/v1?" + query)
        except Exception:
            continue
        for item in obj.get("results", []):
            resource = item.get("resource") or {}
            dataset_id = resource.get("id")
            if dataset_id and re.fullmatch(r"[a-z0-9-]{4}-[a-z0-9-]{4}", dataset_id):
                ids[dataset_id] = resource
    candidates = []
    for dataset_id, listing in sorted(ids.items())[:MAX_NYC_IDS]:
        title = str(listing.get("name") or "")
        if blocked_title(title):
            continue
        try:
            meta = json_get(f"https://{source['domain']}/api/views/{dataset_id}.json")
            cols = meta.get("columns") or []
            headers = [str(c.get("fieldName") or c.get("name") or "").strip() for c in cols]
            if len(headers) < 10:
                continue
            names = [x for x in headers if x and not blocked_header(x)]
            if len(names) < 10:
                continue
            # Ask for five rows from the canonical SODA endpoint. The values stay
            # in memory and are scanned for obvious contact/address patterns only.
            sample_raw = http_bytes(
                f"https://{source['domain']}/resource/{dataset_id}.csv?$limit=5", MAX_PREFIX
            )
            parsed = read_csv_prefix(sample_raw)
            if not parsed:
                # SODA query results already contain headers; parse directly.
                text = sample_raw.decode("utf-8-sig", errors="replace")
                rows = list(csv.reader(io.StringIO(text)))
                if len(rows) < 6:
                    continue
                headers, body = rows[0], rows[1:6]
                if len(headers) < 10 or len(body) < 5:
                    continue
                usable = safe_headers(headers, body)
            else:
                headers, body = parsed
                usable = safe_headers(headers, body)
            if len(usable) < 10:
                continue
            candidates.append({
                "source_id": source["id"],
                "language": source["language"],
                "dataset_id": dataset_id,
                "resource_id": dataset_id,
                "title": title,
                "catalog_url": f"https://{source['domain']}/dataset/{dataset_id}",
                "resource_url": f"https://{source['domain']}/resource/{dataset_id}.csv",
                "license": {
                    "id": "NYC Open Data public-dataset policy",
                    "title": "No registration, license, or use restriction under NYC Open Data policy; verify dataset-provider terms.",
                    "url": "https://www.nyc.gov/opendata/get-started/FAQs",
                    "verification": "source-level FAQ and Local Law 11; individual provider terms still require review",
                },
                "metadata_updated": str(meta.get("rowsUpdatedAt") or ""),
                "resource_bytes": None,
                "header_count": len(headers),
                "safe_header_count": len(usable),
                "safe_headers": usable,
                "sample_rows_available": 5,
                "sample_values_written": False,
                "sample_safety": "first five rows scanned for contact/address patterns; values omitted",
                "publisher": str(meta.get("attribution") or ""),
                "manual_review_required": True,
            })
        except Exception:
            continue
    return candidates

def self_test():
    assert normalize_header("  Ｍonth\t ") == "month"
    assert blocked_header("Email Address")
    assert blocked_header("住所")
    assert not blocked_header("Population Total")
    assert sensitive_value("sample@example.org")
    assert sensitive_value("555-010-2020")
    sample = b"Month,Population,Total,Rate,Area,Class,Year,Value,Group,Measure\n" + \
             b"2025,1,2,3,4,5,6,7,8,9\n2025,1,2,3,4,5,6,7,8,9\n" + \
             b"2025,1,2,3,4,5,6,7,8,9\n2025,1,2,3,4,5,6,7,8,9\n2025,1,2,3,4,5,6,7,8,9\n"
    parsed = read_csv_prefix(sample)
    assert parsed and len(parsed[0]) == 10 and len(parsed[1]) == 5
    assert len(safe_headers(parsed[0], parsed[1])) == 10
    print("self-test: passed")

def main(argv):
    if argv and argv[0] == "self-test":
        self_test()
        return 0
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("stage") != "discovery":
        raise SystemExit("Discovery only: review candidates and add a frozen allowlist before extraction.")
    OUT.mkdir(parents=True, exist_ok=True)
    all_candidates = []
    source_counts = []
    for source in manifest["sources"]:
        if source["kind"] == "ckan":
            candidates, scanned = discover_ckan(source)
        else:
            candidates, scanned = discover_nyc(source), None
        candidates.sort(key=lambda c: (c["dataset_id"], c["resource_id"] or ""))
        all_candidates.extend(candidates)
        source_counts.append({
            "source_id": source["id"], "language": source["language"],
            "datasets_scanned": scanned, "candidates": len(candidates)
        })
    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "manifest_sha256": hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest(),
        "stage": "discovery_only",
        "criteria": manifest["goals"],
        "source_counts": source_counts,
        "candidate_count": len(all_candidates),
        "sample_values_written": False,
        "labels_written": False,
        "blind_sets_read": False,
        "candidates": all_candidates,
    }
    path = OUT / "candidates.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# 独立評価主セット候補（発見段階）", "",
        "値・ラベル・生CSVは保存していません。これは確定評価セットではなく、各データセットの一次確認と見出しレビュー用の候補一覧です。", "",
        f"- 取得日時 UTC: {result['created_at_utc']}",
        f"- 候補表: {len(all_candidates)}",
        f"- 目標: {manifest['goals']['min_tables']} 表以上 / {manifest['goals']['min_columns']} 列以上 / 4出典以上 / 2言語以上",
        "- 5件入力、全CSVハッシュ、学習見出しとの重複は、候補を人手で確認してから別工程で行います。",
        "- ラベルは別ファイルにし、学習束へ入れません。",
        "", "| 出典 | 言語 | CSV候補（安全ヘッダー10以上） |",
        "|---|---|---:|"
    ]
    for item in source_counts:
        lines.append(f"| {item['source_id']} | {item['language']} | {item['candidates']} |")
    lines += ["", "## 次の確認", "",
              "各候補の表題・公開元・個別ライセンス・安全ヘッダー・初期5行の個人情報検査を確認し、採用する30表以上を allowlist として固定します。その後にCSV本体を取得してSHA-256を記録し、入力だけを非公開で保存します。", ""]
    (OUT / "candidates.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"discovery: {len(all_candidates)} candidates; values/labels/raw CSV not persisted")

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
