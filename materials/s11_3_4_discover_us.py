#!/usr/bin/env python3
"""S11 3.4 US Data.gov publisher registration and metadata-only discovery."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from independent_eval.allocation import add_assignment, load_allocation, validate_allocation  # noqa: E402

API_ROOT = "https://catalog.data.gov/api/3/action"
PORTAL = "https://catalog.data.gov"
HOST = "catalog.data.gov"
DATE = "2026-10-22"
PAGE_SIZE = 1000
NYC_ORG_HINT = re.compile(r"(?:^|[-_])(?:nyc|new-york-city|city-of-new-york)(?:$|[-_])", re.I)


def publisher_id(org_id: str) -> str:
    value = str(org_id).strip().lower()
    if not value or ":" in value:
        raise ValueError(f"invalid Data.gov organization id: {org_id!r}")
    value = re.sub(r"[^a-z0-9_-]+", "-", value).strip("-_")
    if not value:
        raise ValueError(f"invalid Data.gov organization id: {org_id!r}")
    return f"us_datagov_{value}"


def _request_json(url: str, retries: int = 4) -> dict:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != HOST:
        raise ValueError("request host is outside the Data.gov catalog allowlist")
    for attempt in range(retries):
        req = Request(url, headers={
            "User-Agent": "jitsuris-s11-metadata-discovery/1.0",
            "Accept": "application/json",
        })
        try:
            with urlopen(req, timeout=40) as response:
                raw = response.read(8_000_001)
                if len(raw) > 8_000_000:
                    raise RuntimeError("organization-list response exceeded safety cap")
                return json.loads(raw.decode("utf-8-sig"))
        except HTTPError as exc:
            if exc.code not in {408, 425, 429, 500, 502, 503, 504} or attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
        except (TimeoutError, URLError, OSError):
            if attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
    raise RuntimeError("Data.gov organization-list request retries exhausted")


def _action(action: str, params: dict) -> object:
    url = f"{API_ROOT}/{action}?{urlencode(params)}"
    payload = _request_json(url)
    if not payload.get("success"):
        raise RuntimeError(f"Data.gov CKAN action failed: {action}")
    return payload.get("result")


def organization_ids() -> list[str]:
    result: list[str] = []
    offset = 0
    while True:
        page = _action("organization_list", {
            "all_fields": "false",
            "limit": PAGE_SIZE,
            "offset": offset,
        })
        if not isinstance(page, list) or any(not isinstance(x, str) for x in page):
            raise RuntimeError("organization_list did not return a list of names")
        result.extend(x.strip() for x in page if x.strip())
        if len(page) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
        time.sleep(0.15)
    clean = sorted(set(result))
    if not clean:
        raise RuntimeError("organization_list returned no organizations")
    return clean


def register_publishers(allocation_path: Path, source_path: Path) -> dict:
    allocation = load_allocation(allocation_path)
    orgs = organization_ids()
    aliases = allocation.setdefault("aliases", {})
    source_records = []
    for org in orgs:
        pid = publisher_id(org)
        if NYC_ORG_HINT.search(org):
            canonical = "nyc"
            prior = aliases.get(pid)
            if prior not in (None, canonical):
                raise ValueError(f"conflicting existing alias for {pid}")
            aliases[pid] = canonical
            source_records.append({
                "organization_id": org,
                "publisher_id": pid,
                "canonical_publisher_id": canonical,
                "pool": "main",
                "alias_reason": "New York City is a protected main source; do not search this organization.",
            })
        else:
            allocation = add_assignment(allocation, pid, DATE)
            record = next(x for x in allocation["publishers"] if x["publisher_id"] == pid)
            source_records.append({
                "organization_id": org,
                "publisher_id": pid,
                "canonical_publisher_id": pid,
                "pool": record["pool"],
            })
    validate_allocation(allocation)
    allocation_path.write_text(json.dumps(allocation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = Counter(x["pool"] for x in source_records)
    source = {
        "schema_version": 1,
        "collected_date": DATE,
        "purpose": "S11 3.4 non-Japanese table candidates; US Data.gov publisher registration before dataset metadata",
        "method": "Official Data.gov CKAN organization_list(all_fields=false), paginated with limit/offset; publisher IDs only. No dataset metadata queried in this stage.",
        "portal": {
            "portal_id": "us_datagov",
            "portal_url": PORTAL,
            "organization_list_url": f"{API_ROOT}/organization_list?all_fields=false",
            "publisher_count": len(source_records),
            "pool_counts": dict(sorted(counts.items())),
            "dataset_metadata_queried": False,
            "data.gov_api_scope": "legacy CKAN endpoint; metadata only, no dataset contents",
            "publishers": source_records,
        },
    }
    source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    searchable_train = sum(x["pool"] == "train" for x in source_records)
    return {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalogue": PORTAL,
        "publisher_ids_registered": len(source_records),
        "train_publishers": searchable_train,
        "eval2_publishers": counts.get("eval2", 0),
        "eval3_publishers": counts.get("eval3", 0),
        "main_aliases_excluded": counts.get("main", 0),
        "dataset_metadata_queried": False,
        "publisher_ids": [x["publisher_id"] for x in source_records],
    }


def self_test() -> None:
    assert publisher_id("us-census-bureau") == "us_datagov_us-census-bureau"
    assert NYC_ORG_HINT.search("city-of-new-york")
    assert NYC_ORG_HINT.search("nyc-open-data")
    assert not NYC_ORG_HINT.search("new-york-state")
    print("S11 3.4 US Data.gov publisher registration self-test passed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--mode", choices={"register"})
    args = parser.parse_args(argv)
    if args.self_test:
        self_test()
        return 0
    if args.mode != "register":
        parser.error("--mode register or --self-test is required")
    report = register_publishers(
        ROOT / "independent_eval/allocation.json",
        ROOT / "independent_eval/allocation_sources_us_datagov_20261022.json",
    )
    out = ROOT / "materials/s11_3_4_us_registration_20261022.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Data.gov publishers registered={report['publisher_ids_registered']} "
        f"train={report['train_publishers']}; no dataset metadata queried"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
