#!/usr/bin/env python3
"""Compare BODIK package_search query behavior using train publishers only.

Metadata-only diagnostic: it reads package_search result counts and dataset titles,
never resources, datastore rows, or files.
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
API = "https://data.bodik.jp/api/3/action"
QUERIES = {
    "broad_current": "統計 OR 人口 OR 世帯 OR 年齢 OR 産業 OR 事業所 OR 観光 OR 農業 OR 農林 OR 漁業 OR 水産 OR 医療 OR 保健 OR 福祉 OR 教育 OR 学校 OR 指数 OR 就業 OR 生産",
    "single_statistics": "統計",
    "single_population": "人口",
}


def fetch(org: str, label: str, query: str) -> dict:
    params = {"q": query, "fq": f"organization:{org}", "rows": 5, "start": 0}
    url = f"{API}/package_search?{urlencode(params)}"
    if urlparse(url).hostname != "data.bodik.jp":
        raise ValueError("BODIK host allowlist rejected request")
    req = Request(url, headers={"User-Agent": "jitsuris-s11-search-diagnostic/1.0", "Accept": "application/json"})
    try:
        with urlopen(req, timeout=12) as resp:
            payload = json.loads(resp.read(2_000_001).decode("utf-8-sig"))
        result = payload.get("result") or {}
        packages = result.get("results") or []
        return {
            "publisher_id": org, "query": label, "http_status": 200,
            "success": bool(payload.get("success")),
            "total_count": result.get("count"),
            "titles": [str(p.get("title") or p.get("name") or "")[:200] for p in packages],
            "error": None,
        }
    except HTTPError as exc:
        return {"publisher_id": org, "query": label, "http_status": exc.code,
                "success": False, "total_count": None, "titles": [], "error": f"HTTP {exc.code}"}
    except (TimeoutError, URLError, OSError, ValueError, json.JSONDecodeError) as exc:
        return {"publisher_id": org, "query": label, "http_status": None,
                "success": False, "total_count": None, "titles": [],
                "error": type(exc).__name__}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-json", type=Path, required=True)
    args = parser.parse_args()
    allocation = json.loads((ROOT / "independent_eval/allocation.json").read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "independent_eval/allocation_sources_20261021.json").read_text(encoding="utf-8"))
    pools = {str(p["publisher_id"]): p["pool"] for p in allocation.get("publishers", [])}
    bodik = next(s for s in sources["sources"] if s["portal_id"] == "bodik")
    assigned = set(str(x) for x in bodik["organization_names"])
    orgs = ["142018", "410004", "143839", "422029"]
    for org in orgs:
        if org not in assigned or pools.get(org) != "train":
            raise SystemExit(f"diagnostic publisher is not preassigned BODIK train: {org}")
    results = []
    for org in orgs:
        for label, query in QUERIES.items():
            results.append(fetch(org, label, query))
            time.sleep(0.4)
    out = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "stage": "package_search_metadata_diagnostic",
        "scope": "4 preassigned BODIK train publishers; package_search title/count metadata only",
        "resource_files_read": False, "datastore_rows_requested": 0, "cell_values_saved": False,
        "results": results,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("BODIK package_search diagnostic complete")
    for row in results:
        print(f"{row['publisher_id']} {row['query']} status={row['http_status']} total={row['total_count']} error={row['error']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
