"""教材庫の候補を速く集める（2026-10-22 Claude）。メタデータだけ。値・ファイルは取らない。GitHub Actions で動かす。

- BODIK：allocation.json で train の組織（団体コード 6 桁）ごとに package_search を 1 回（rows=1000、足りなければ次の頁）。
  datastore_active のリソースだけを候補にする。列の定義は取り出しの段（fetch_rows.py）で読むので、ここでは問い合わせない。
- CKAN（2026-10-24）：allocation_sources_world の CKAN カタログのうち、allowed_hosts.json に Claude が足したホストで、train の組織ごとに BODIK と同じ探し方。
- Socrata：train の公開の場（world_socrata_<ホスト>）ごとにカタログ API（api.us.socrata.com/api/catalog/v1?domains=…）を 1〜数回。
- 1 つのデータセットから 1 リソース。題名から数字・年度を除いた形が同じ表は、公開元ごとに 1 つ（年度違いを重ねない）。
- 公開元ごとに最大 PER_PUBLISHER 表（教材庫全体の上限と同じ 15）。題名の規則・ライセンスの規則は pipeline.py と同じ。
出力は pipeline.py adopt がそのまま読む形（selected）。

使い方：python materials/pool_discover.py --out materials/pool/candidates_<日付>.json [--bodik] [--ckan] [--socrata] [--limit-publishers N]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
from pipeline import ALLOWED_LICENSES, PER_PUBLISHER_POOL, TITLE_DENY, allowed_ckan_hosts, normalize_license  # noqa: E402

PER_PUBLISHER = PER_PUBLISHER_POOL
HOSTS = {"data.bodik.jp", "api.us.socrata.com"} | allowed_ckan_hosts()
UA = {"User-Agent": "jitsuris-train-pool-discover/1.0 (metadata only)"}


def get_json(url, tries=4):
    host = urlparse(url).hostname or ""
    if urlparse(url).scheme != "https" or host not in HOSTS:
        raise ValueError(f"host not allowed: {host}")
    for attempt in range(tries):
        time.sleep(1.0 + 5.0 * attempt)
        try:
            with urlopen(Request(url, headers=UA), timeout=60) as resp:
                return json.loads(resp.read(50_000_001).decode("utf-8-sig"))
        except HTTPError as exc:
            if (exc.code in (403, 429) or exc.code >= 500) and attempt < tries - 1:
                continue
            raise RuntimeError(f"HTTP {exc.code}") from None


def title_key(title):
    """年度違いを同じ表とみなすための題名の形（数字・和暦・年度・年・月を除く）。"""
    t = re.sub(r"(令和|平成|昭和|R|H)\s*[0-9０-９元]+\s*(年度|年)?", "", str(title))
    t = re.sub(r"[0-9０-９]+", "", t)
    t = re.sub(r"(年度|年|月|版|第|号|期)", "", t)
    return re.sub(r"\s+", "", t).lower()


def bodik_candidates(train_orgs, limit=None):
    return ckan_candidates("data.bodik.jp", {org: org for org in train_orgs}, "bodik", limit)


def ckan_candidates(host, orgs, platform, limit=None):
    """CKAN の組織（organization_id → publisher_id）ごとに package_search。datastore のあるリソースだけを候補にする。"""
    out, stats = [], Counter()
    for org in sorted(orgs)[:limit]:
        pid = orgs[org]
        start, packages = 0, []
        try:
            while True:
                res = get_json(f"https://{host}/api/3/action/package_search?" + urlencode(
                    {"fq": f"organization:{org}", "rows": 1000, "start": start}))["result"]
                packages += res.get("results", [])
                start += 1000
                if start >= int(res.get("count") or 0):
                    break
        except Exception as exc:
            stats[f"search_failed:{str(exc)[:40]}"] += 1
            continue
        stats["publishers_searched"] += 1
        seen_titles, picked = set(), 0
        for pkg in sorted(packages, key=lambda p: p.get("metadata_modified") or "", reverse=True):
            if picked >= PER_PUBLISHER:
                break
            lic = normalize_license(pkg.get("license_id"))
            title = str(pkg.get("title") or "")
            if lic not in ALLOWED_LICENSES:
                stats["license"] += 1
                stats[f"license:{lic or '(none)'}"] += 1   # どのライセンスで落ちたかの内訳（規則を決めるため）
                continue
            if TITLE_DENY.search(title):
                stats["title_deny"] += 1
                continue
            key = title_key(title)
            if key in seen_titles:
                stats["same_title"] += 1
                continue
            res = next((r for r in pkg.get("resources", []) if r.get("datastore_active")), None)
            if not res:
                stats["no_datastore"] += 1
                continue
            seen_titles.add(key)
            picked += 1
            out.append({"publisher_id": pid, "pool": "train", "platform": platform, "title": title, "resource_name": res.get("name", ""),
                        "resource_url": f"https://{host}/dataset/{pkg.get('name')}/resource/{res['id']}", "resource_id": res["id"],
                        "license": {"id": lic}, "datastore_available": True, "safe_headers": []})
        stats["tables"] = len(out)
    return out, stats


def socrata_candidates(train_hosts, limit=None):
    out, stats = [], Counter()
    for host in sorted(train_hosts)[:limit]:
        try:
            res = get_json("https://api.us.socrata.com/api/catalog/v1?" + urlencode({"domains": host, "only": "dataset", "limit": 200}))
        except Exception as exc:
            stats[f"catalog_failed:{str(exc)[:40]}"] += 1
            continue
        stats["publishers_searched"] += 1
        pid = "world_socrata_" + re.sub(r"[.-]", "_", host)
        seen_titles, picked = set(), 0
        for item in res.get("results", []):
            if picked >= PER_PUBLISHER:
                break
            r, meta = item.get("resource", {}), item.get("metadata", {})
            title = str(r.get("name") or "")
            lic = normalize_license(meta.get("license") or "")
            if lic not in ALLOWED_LICENSES:
                stats["license"] += 1
                continue
            if TITLE_DENY.search(title):
                stats["title_deny"] += 1
                continue
            if len(r.get("columns_name") or []) < 3:
                stats["few_columns"] += 1
                continue
            key = title_key(title)
            if key in seen_titles:
                stats["same_title"] += 1
                continue
            seen_titles.add(key)
            picked += 1
            out.append({"publisher_id": pid, "pool": "train", "platform": "socrata", "title": title, "resource_id": r.get("id"),
                        "catalog_url": item.get("permalink") or f"https://{host}/d/{r.get('id')}",
                        "resource_url": item.get("permalink") or f"https://{host}/d/{r.get('id')}",
                        "license": {"id": lic}, "datastore_available": True,
                        "safe_headers": [str(c) for c in (r.get("columns_name") or [])][:10]})
        stats["tables"] = len(out)
    return out, stats


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--bodik", action="store_true")
    ap.add_argument("--ckan", action="store_true")
    ap.add_argument("--socrata", action="store_true")
    ap.add_argument("--limit-publishers", type=int)
    a = ap.parse_args(argv)
    pubs = json.load(open(ROOT / "independent_eval" / "allocation.json", encoding="utf-8"))["publishers"]
    train = {p["publisher_id"] for p in pubs if p["pool"] == "train"}
    selected, stats = [], {}
    if a.bodik:
        orgs = {p for p in train if re.fullmatch(r"\d{6}", p)}
        c, stats["bodik"] = bodik_candidates(orgs, a.limit_publishers)
        selected += c
    if a.ckan:
        src = json.load(open(ROOT / "independent_eval" / "allocation_sources_world_20261022.json", encoding="utf-8"))
        allowed = allowed_ckan_hosts()
        stats["ckan"] = {}
        for cat in src["catalogues"]:
            if cat.get("platform") != "ckan" or cat.get("domain") not in allowed:
                continue
            orgs = {p["organization_id"]: p["publisher_id"] for p in cat.get("publisher_ids", []) if p["publisher_id"] in train}
            if not orgs:
                continue
            c, stats["ckan"][cat["domain"]] = ckan_candidates(cat["domain"], orgs, "ckan", a.limit_publishers)
            selected += c
    if a.socrata:
        hosts = set()
        for p in train:
            if p.startswith("world_socrata_"):
                hosts.add(p[len("world_socrata_"):])   # 下で catalog の domain と突き合わせるため、仮に _ のまま
        # _ を . に戻した形で引き、結果の permalink のホストで publisher を決め直す
        real_hosts = {h.replace("_", ".") for h in hosts}
        c, stats["socrata"] = socrata_candidates(real_hosts, a.limit_publishers)
        selected += [x for x in c if x["publisher_id"] in train]
    doc = {"schema_version": 1, "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "tool": "materials/pool_discover.py",
           "metadata_only": True, "values_saved": False, "stats": stats, "selected": selected}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"selected {len(selected)} tables from {len({x['publisher_id'] for x in selected})} publishers; {json.dumps(stats, ensure_ascii=False)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
