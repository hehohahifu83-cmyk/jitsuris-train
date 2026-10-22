#!/usr/bin/env python3
"""S11 3.4 US Socrata publisher registration; publisher IDs only."""
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
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from independent_eval.allocation import add_assignment, load_allocation, validate_allocation  # noqa: E402

API = "https://api.us.socrata.com/api/catalog/v1"
HOST = "api.us.socrata.com"
DATE = "2026-10-22"
MAX_RESPONSE_BYTES = 20_000_000
COUNTRY_SUFFIXES = (".uk", ".ie", ".ca", ".au", ".nz")
NYC_DOMAIN = re.compile(r"(?:^|[.-])(?:nyc|new-york-city|cityofnewyork)(?:[.-]|$)", re.I)


def publisher_id(domain: str) -> str:
    host = str(domain).strip().lower().rstrip(".")
    if not re.fullmatch(r"[a-z0-9.-]+", host) or ".." in host:
        raise ValueError(f"invalid Socrata domain: {domain!r}")
    return "us_socrata_" + re.sub(r"[^a-z0-9]+", "-", host).strip("-")


def is_us_government_domain(domain: str) -> bool:
    host = str(domain).strip().lower().rstrip(".")
    if not host or any(host.endswith(suffix) for suffix in COUNTRY_SUFFIXES):
        return False
    return host.endswith(".gov") or host.endswith(".us")


def is_nyc_domain(domain: str) -> bool:
    return bool(NYC_DOMAIN.search(str(domain).strip().lower()))


def _request_json(url: str, retries: int = 4) -> dict:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != HOST:
        raise ValueError("request host is outside the Socrata Discovery API allowlist")
    for attempt in range(retries):
        req = Request(url, headers={
            "User-Agent": "jitsuris-s11-metadata-discovery/1.0",
            "Accept": "application/json",
        })
        try:
            with urlopen(req, timeout=40) as response:
                raw = response.read(MAX_RESPONSE_BYTES + 1)
                if len(raw) > MAX_RESPONSE_BYTES:
                    raise RuntimeError("publisher-list response exceeded safety cap")
                return json.loads(raw.decode("utf-8-sig"))
        except HTTPError as exc:
            if exc.code not in {408, 425, 429, 500, 502, 503, 504} or attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
        except (TimeoutError, URLError, OSError):
            if attempt + 1 == retries:
                raise
            time.sleep(1.0 + 2.0 * attempt)
    raise RuntimeError("Socrata Discovery API retries exhausted")


def domain_records() -> list[dict]:
    payload = _request_json(API + "/domains")
    entries = payload if isinstance(payload, list) else payload.get("results") or payload.get("domains") or []
    if not isinstance(entries, list):
        raise RuntimeError("Socrata domains endpoint did not return a list")
    cleaned: dict[str, int | None] = {}
    for item in entries:
        if not isinstance(item, dict):
            continue
        domain = str(item.get("domain") or item.get("thing") or item.get("name") or "").strip().lower().rstrip(".")
        if not domain or not is_us_government_domain(domain):
            continue
        count = item.get("count") or item.get("resourceCount") or item.get("resource_count")
        try:
            count = int(count) if count is not None else None
        except (TypeError, ValueError):
            count = None
        cleaned[domain] = count
    if not cleaned:
        raise RuntimeError("Socrata domains response contained no US government portals")
    return [{"domain": d, "catalog_asset_count": cleaned[d]} for d in sorted(cleaned)]


def register_publishers(allocation_path: Path, source_path: Path, report_path: Path) -> dict:
    allocation = load_allocation(allocation_path)
    domains = domain_records()
    source_records = []
    aliases = allocation.setdefault("aliases", {})
    for record in domains:
        domain = record["domain"]
        pid = publisher_id(domain)
        if is_nyc_domain(domain):
            canonical = "nyc"
            prior = aliases.get(pid)
            if prior not in (None, canonical):
                raise ValueError(f"conflicting existing NYC alias for {pid}")
            aliases[pid] = canonical
            source_records.append({
                **record,
                "publisher_id": pid,
                "canonical_publisher_id": canonical,
                "pool": "main",
                "alias_reason": "Protected New York City source; excluded before dataset search.",
            })
        else:
            allocation = add_assignment(allocation, pid, DATE)
            assigned = next(x for x in allocation["publishers"] if x["publisher_id"] == pid)
            source_records.append({
                **record,
                "publisher_id": pid,
                "canonical_publisher_id": pid,
                "pool": assigned["pool"],
            })
    validate_allocation(allocation)
    allocation_path.write_text(json.dumps(allocation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = Counter(x["pool"] for x in source_records)
    source = {
        "schema_version": 1,
        "collected_date": DATE,
        "purpose": "S11 3.4 non-Japanese table candidates; US Socrata publisher registration before dataset metadata",
        "method": "Socrata Discovery API /domains (portal domains and asset counts only); register US .gov/.us publishers before dataset search.",
        "portal": {
            "portal_id": "us_socrata",
            "portal_url": API,
            "domain_list_url": API + "/domains",
            "publisher_count": len(source_records),
            "pool_counts": dict(sorted(counts.items())),
            "dataset_metadata_queried": False,
            "data.gov_ckan_attempt": "legacy endpoint returned HTTP 404; no dataset metadata was obtained",
            "publishers": source_records,
        },
    }
    source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalogue": API,
        "publisher_ids_registered": len(source_records),
        "train_publishers": counts.get("train", 0),
        "eval2_publishers": counts.get("eval2", 0),
        "eval3_publishers": counts.get("eval3", 0),
        "main_aliases_excluded": counts.get("main", 0),
        "dataset_metadata_queried": False,
        "country_filter": "US government domains ending .gov or .us; UK, Ireland, Canada, Australia, and New Zealand suffixes excluded.",
        "publisher_ids_sample": [x["publisher_id"] for x in source_records[:25]],
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def self_test() -> None:
    assert publisher_id("data.example.gov") == "us_socrata_data-example-gov"
    assert is_us_government_domain("data.ca.gov")
    assert is_us_government_domain("opendata.city.us")
    assert not is_us_government_domain("data.gov.uk")
    assert not is_us_government_domain("data.gov.au")
    assert not is_us_government_domain("data.example.ca")
    assert is_nyc_domain("data.cityofnewyork.us")
    assert is_nyc_domain("data.nyc.gov")
    assert not is_nyc_domain("data.ny.gov")
    print("S11 3.4 US Socrata publisher registration self-test passed")


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
        ROOT / "independent_eval/allocation_sources_socrata_20261022.json",
        ROOT / "materials/s11_3_4_us_registration_20261022.json",
    )
    print(
        f"Socrata US publishers registered={report['publisher_ids_registered']} "
        f"train={report['train_publishers']}; no dataset metadata queried"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
