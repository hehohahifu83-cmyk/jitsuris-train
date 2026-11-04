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
# 2026-11-01 Claude：新しい評価の陣 E4 の公開元の候補（E1〜E3・主セット・教材庫と重ならない公開元を探す）。
# 出力の名前に e4 が入っているときだけこちらを使う。状態コードと本文の先頭 160 文字だけを残す。
TARGETS_E4 = [
    ("osaka", "https://data.city.osaka.lg.jp/api/3/action/package_search?rows=1"),
    ("osaka", "https://data.bodik.jp/api/3/action/organization_show?id=271004"),
    ("osaka", "https://www.city.osaka.lg.jp/contents/wdu020/opendata/"),
    ("shizuoka", "https://opendata.pref.shizuoka.jp/api/3/action/package_search?rows=1"),
    ("fukuoka_city", "https://ckan.odp.jig.jp/api/3/action/package_search?rows=1"),
    ("austria", "https://www.data.gv.at/katalog/api/3/action/package_search?rows=1"),
    ("berlin", "https://datenregister.berlin.de/api/3/action/package_search?rows=1"),
    ("berlin", "https://daten.berlin.de/api/3/action/package_search?rows=1"),
    ("govdata_de", "https://ckan.govdata.de/api/3/action/package_search?rows=1"),
    ("france", "https://www.data.gouv.fr/api/1/datasets/?page_size=1"),
    ("france", "https://tabular-api.data.gouv.fr/api/resources/"),
    ("luxembourg", "https://data.public.lu/api/1/datasets/?page_size=1"),
    ("paris", "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets?limit=1"),
    ("us_datagov", "https://catalog.data.gov/api/3/action/package_search?rows=1"),
    ("ontario", "https://data.ontario.ca/api/3/action/package_search?rows=1"),
    ("alberta", "https://open.alberta.ca/api/3/action/package_search?rows=1"),
    ("queensland", "https://www.data.qld.gov.au/api/3/action/package_search?rows=1"),
    ("nsw", "https://data.nsw.gov.au/data/api/3/action/package_search?rows=1"),
    ("singapore", "https://api-production.data.gov.sg/v2/public/api/datasets?page=1"),
]
# 2026-11-04 Claude：新しい陣 F1・C1・E4（bench/g24fix_prereg_20261104.md・bench/scrc_prereg_draft_20261104.md）の公開元の数を数える。
# 出力の名前に orgs が入っているときだけ。11-01 の調べで Actions から届いた CKAN のサイトの組織の一覧（名前・題名・データセットの数）だけを残す。
# データセット・表の中身・値は取らない。
ORG_HOSTS = [
    ("jig_jp", "https://ckan.odp.jig.jp"),
    ("sendai", "https://data.city.sendai.jp"),   # 2026-11-04 ChatGPT の候補（ai-bridge messages/20261104-0904_…）
    ("kanazawa", "https://catalog-data.city.kanazawa.ishikawa.jp"),
    ("berlin", "https://datenregister.berlin.de"),
    ("govdata_de", "https://ckan.govdata.de"),
    ("ontario", "https://data.ontario.ca"),
    ("alberta", "https://open.alberta.ca"),
    ("queensland", "https://www.data.qld.gov.au"),
    ("nsw", "https://data.nsw.gov.au/data"),
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


def get_json(url):
    req = Request(url, headers={"Accept": "application/json", "User-Agent": AGENTS["with_contact"]})
    with urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def count_orgs():
    """組織の一覧を頁ごとに取る（organization_list、all_fields）。名前・題名・package_count だけを残す。"""
    out = []
    for site, base in ORG_HOSTS:
        orgs, err, offset = [], None, 0
        while True:
            url = f"{base}/api/3/action/organization_list?all_fields=true&limit=25&offset={offset}"
            try:
                d = get_json(url)
            except (HTTPError, URLError, TimeoutError, OSError, ValueError) as e:
                err = f"{type(e).__name__}: {e}"[:200]
                break
            res = d.get("result") or []
            for o in res:
                orgs.append({"name": o.get("name"), "title": (o.get("title") or "")[:80], "package_count": o.get("package_count")})
            if not res or offset > 20000:   # all_fields は 1 回 25 件まで（CKAN の既定の上限）。空になるまでめくる
                break
            offset += len(res)
            time.sleep(0.3)
        n_pkg = sum(o["package_count"] or 0 for o in orgs)
        print(site, len(orgs), "orgs", n_pkg, "datasets", err or "")
        out.append({"site": site, "base": base, "n_orgs": len(orgs), "n_orgs_with_data": sum(1 for o in orgs if (o["package_count"] or 0) > 0),
                    "n_datasets": n_pkg, "error": err, "orgs": orgs})
        time.sleep(1)
    return out


def main(argv=None):
    path = (argv or sys.argv[1:])[0]
    if "orgs" in path:
        doc = {"created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "created_by": "materials/pool/probe_hosts.py（orgs）",
               "metadata_only": True, "hosts": count_orgs()}
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        return
    rows = []
    e4 = "e4" in path
    for site, url in (TARGETS_E4 if e4 else TARGETS):
        for name, agent in AGENTS.items():
            if e4 and name not in ("pool_discover", "with_contact"):
                continue
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
