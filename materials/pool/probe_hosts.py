"""英国（data.gov.uk）・スイス（opendata.swiss）が Actions から HTTP 403 になる原因を調べる（2026-10-28 Claude）。

API の住所の候補 × 名乗り方（User-Agent）ごとに、状態コード・返ってきた形・本文の先頭だけを記録する。データの中身は保存しない。
ブラウザのふりはしない（名乗り方は道具の名前と連絡先だけ）。
  python -I materials/pool/probe_hosts.py materials/pool/probe/hosts_YYYYMMDD.json
"""
import json
import sys
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

UK_RES = "5c3531f1-5e8a-4db1-9a83-af463020ded5"   # b049 で 403 になった表の 1 つ
UK_PKG = "financial-transactions-data-advantage_west_midlands_march_2011"
TARGETS = [
    ("uk", "https://data.gov.uk/api/3/action/package_search?rows=1"),
    ("uk", f"https://data.gov.uk/api/3/action/resource_show?id={UK_RES}"),
    ("uk", f"https://data.gov.uk/api/3/action/package_show?id={UK_PKG}"),
    ("uk", "https://data.gov.uk/api/action/package_search?rows=1"),
    ("uk", "https://ckan.publishing.service.gov.uk/api/3/action/package_search?rows=1"),
    ("uk", f"https://ckan.publishing.service.gov.uk/api/3/action/resource_show?id={UK_RES}"),
    ("uk", f"https://ckan.publishing.service.gov.uk/api/3/action/package_show?id={UK_PKG}"),
    ("swiss", "https://opendata.swiss/api/3/action/organization_list"),
    ("swiss", "https://opendata.swiss/api/3/action/package_search?rows=1"),
    ("swiss", "https://ckan.opendata.swiss/api/3/action/organization_list"),
    ("swiss", "https://ckan.opendata.swiss/api/3/action/package_search?rows=1"),
]
AGENTS = {
    "pool_discover": "jitsuris-train-pool-discover/1.0 (metadata only)",
    "fetch_rows": "jitsuris-train-s11/1.0 (source and license recorded)",
    "with_contact": "jitsuris-train/1.0 (research; +https://github.com/hehohahifu83-cmyk/jitsuris-train)",
    "none": None,
}


def probe(url, agent):
    headers = {"Accept": "application/json"}
    if agent:
        headers["User-Agent"] = agent
    t = time.monotonic()
    try:
        with urlopen(Request(url, headers=headers), timeout=30) as resp:
            body = resp.read(400)
            out = {"status": resp.status, "final_url": resp.geturl(), "content_type": resp.headers.get("Content-Type")}
    except HTTPError as e:
        body = e.read(400) if e.fp else b""
        out = {"status": e.code, "content_type": e.headers.get("Content-Type") if e.headers else None,
               "server": e.headers.get("Server") if e.headers else None}
    except (URLError, TimeoutError, OSError) as e:
        body, out = b"", {"status": None, "error": f"{type(e).__name__}: {e}"[:200]}
    out["seconds"] = round(time.monotonic() - t, 2)
    text = body.decode("utf-8", "replace")
    out["json_success"] = None
    if text.lstrip().startswith("{"):
        try:
            out["json_success"] = json.loads(text + ("" if text.rstrip().endswith("}") else "")).get("success")
        except ValueError:
            out["json_success"] = "truncated"
    out["head"] = " ".join(text.split())[:160]
    return out


def main(argv=None):
    path = (argv or sys.argv[1:])[0]
    rows = []
    for site, url in TARGETS:
        for name, agent in AGENTS.items():
            r = {"site": site, "url": url, "agent": name, **probe(url, agent)}
            rows.append(r)
            print(site, r["status"], name, url)
            time.sleep(1)
    doc = {"created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "created_by": "materials/pool/probe_hosts.py", "rows": rows}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


if __name__ == "__main__":
    main()
