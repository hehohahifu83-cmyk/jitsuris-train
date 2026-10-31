"""在庫の取り出しで落ちた表の、ファイルの取り方の診断（2026-11-01 Claude）。
b091〜b097 の corpus_log.json の誤り（csv 403・xls 405・datastore 403 で CSV/XLS が別ホスト）から、各種類 最大 15 表を選び、
CKAN の resource_show でファイルの URL を得て、名乗り方（User-Agent）と Accept を変えて GET し、状態コードと転送先のホストだけを記録する。
データの中身は保存しない（先頭 512 バイトを読んで捨てる）。名乗りはどれも正直なもの（ブラウザのふりはしない）。
  python -I research/fetch_diag/probe_downloads.py → research/fetch_diag/probe.json・probe.md
"""
import collections
import json
import os
import re
import time
import urllib.request
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
UAS = {
    "now": {"User-Agent": "jitsuris-train-s11/1.0 (source and license recorded)"},
    "now+accept": {"User-Agent": "jitsuris-train-s11/1.0 (source and license recorded)", "Accept": "*/*"},
    "contact": {"User-Agent": "jitsuris-train/1.0 (+https://github.com/hehohahifu83-cmyk/jitsuris-train; open data research)", "Accept": "*/*"},
    "python": {},
}
BASES = {"data.gov.uk": "https://data.gov.uk/api/3/action/", "open.canada.ca": "https://open.canada.ca/data/api/3/action/",
         "data.gov.au": "https://data.gov.au/data/api/3/action/"}


def kind(err):
    if "xls: HTTP 405" in err or "xlsx: HTTP 405" in err:
        return "xls405"
    if "csv: HTTP 403" in err:
        return "csv403"
    m = re.search(r"file: (\w+) on", err)
    if m and m.group(1) in ("CSV", "XLS", "XLSX"):
        return "ds403_" + m.group(1).lower()
    return None


def get(url, headers):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=40) as r:
            r.read(512)
            return r.status, urlparse(r.geturl()).hostname
    except HTTPError as e:
        return e.code, urlparse(e.geturl() or url).hostname
    except (URLError, TimeoutError, OSError) as e:
        return type(e).__name__, None


def main():
    picked = collections.defaultdict(list)
    for b in ("b091", "b092", "b093", "b094", "b095", "b097"):
        p = os.path.join(ROOT, "materials", "pool", "work", b, "corpus_log.json")
        ad = {x["n"]: x for x in json.load(open(os.path.join(ROOT, "materials", "pool", "work", b, "adopted.json")))["adopted"]}
        for t in json.load(open(p))["tables"]:
            k = kind(t.get("error", "")) if t.get("status") == "error" else None
            if k and len(picked[k]) < 15 and ad.get(t["n"], {}).get("host") in BASES:
                picked[k].append(ad[t["n"]])
    out = []
    for k, items in picked.items():
        for it in items:
            base = BASES[it["host"]]
            try:
                with urllib.request.urlopen(urllib.request.Request(base + "resource_show?" + urlencode({"id": it["resource_id"]}),
                                                                   headers=UAS["now"]), timeout=40) as r:
                    res = json.loads(r.read())["result"]
                url = res.get("url") or ""
            except Exception as e:  # noqa: BLE001
                out.append({"kind": k, "host": it["host"], "error": f"resource_show {type(e).__name__}"})
                continue
            row = {"kind": k, "catalog": it["host"], "file_host": urlparse(url).hostname, "scheme": urlparse(url).scheme,
                   "format": res.get("format")}
            for name, h in UAS.items():
                time.sleep(1.0)
                row[name] = get(url, h)
            out.append(row)
            print(row, flush=True)
    json.dump(out, open(os.path.join(HERE, "probe.json"), "w"), indent=1)
    L = ["# 取り出しで落ちた表のファイルの取り方の診断（`research/fetch_diag/probe_downloads.py`。状態コードだけ）", "",
         "| 種類 | カタログ | ファイルのホスト | 形式 | " + " | ".join(UAS) + " |", "|---|---|---|---|" + "---|" * len(UAS)]
    for r in out:
        L.append(f"| {r['kind']} | {r.get('catalog', r.get('host'))} | {r.get('scheme', '')}://{r.get('file_host', '')} | {r.get('format', r.get('error', ''))} | "
                 + " | ".join(f"{r[n][0]}→{r[n][1]}" if n in r else "" for n in UAS) + " |")
    agg = collections.Counter((r["kind"], n, str(r[n][0])) for r in out for n in UAS if n in r)
    L += ["", "## まとめ（種類・名乗り・状態 → 数）", ""] + [f"- {k} / {n} / {s}：{c}" for (k, n, s), c in sorted(agg.items())]
    open(os.path.join(HERE, "probe.md"), "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
