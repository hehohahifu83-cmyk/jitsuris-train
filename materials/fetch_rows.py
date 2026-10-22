"""S11：採用した表から、行をそろえた値を取り出す（DATA_COLLECTION_PROTOCOL 第 2 章の row_values、2026-10-22 Claude）。

既存の fetch_real.py（列ごとに別々に値を選ぶ）は変えない。こちらは BODIK などの CKAN の datastore API から、
列の名前つきで行を取り、表ごとに同じ行を選んで各列に同じ順で保存する。GitHub Actions で動かす（取り出しの環境からの通信が要る）。

- 対象は採用の記録（materials/s11_*_adopted_*.json）の表だけ。公開元が allocation.json で train でなければ止める。
- 既存の学習の表・主セットの表と URL が同じなら止める。
- 列：見出しが個人・連絡先・自由記述（independent_eval/discover.py の HEADER_DENY）なら落とす。値に、メール・日本の電話番号・
  〒つき／NNN-NNNN の郵便番号・英語の番地が 1 つでもあれば、その列を落とす（日付や金額を電話・郵便と取り違えない狭い判定）。
  残った列のうち表の先頭から 10 列まで。
- 行：空でない値が多い行から、種を固定して最大 20 行（row_values・row_index）。values は従来と同じく列ごとの 5 値。
- 書くのは公開データの値と出典だけ。元の CSV は保存しない。

使い方：python materials/fetch_rows.py --adopted <採用.json> --out <corpus.jsonl> --log <log.json>
       python materials/fetch_rows.py --self-test
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import random
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "independent_eval"))
from discover import HEADER_DENY, normalize_header  # noqa: E402
sys.path.insert(0, str(ROOT / "materials"))
from pipeline import ALLOWED_LICENSES  # noqa: E402  採用の道具と同じライセンスの一覧

ALLOWED_HOSTS = {"data.bodik.jp"}   # 表ごとに、確かめたホストだけを足す（fetch_table）
MAX_COLUMNS = 10
MAX_ROWS = 20
FETCH_LIMIT = 1000
SEED = "jitsuris-s11-rows-v1"

EMAIL_RE = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
JP_PHONE_RE = re.compile(r"(?<!\d)(?:0\d{1,4}-\d{1,4}-\d{3,4}|0[5789]0\d{8}|0\d{9})(?!\d)")
INTL_PHONE_RE = re.compile(r"\+\d{1,3}[\s-]?\d[\d\s-]{6,}\d")
JP_POSTAL_RE = re.compile(r"〒\s*\d{3}-?\d{4}|(?<![\d-])\d{3}-\d{4}(?![\d-])")
STREET_RE = re.compile(r"\b\d{1,6}\s+[A-Z0-9.' -]{2,40}\s+(?:ST|STREET|AVE|AVENUE|RD|ROAD|BLVD|DR|DRIVE|LN|LANE)\b", re.I)


def sensitive_value(value) -> bool:
    v = unicodedata.normalize("NFKC", str(value or "")).strip()
    return bool(v and (EMAIL_RE.search(v) or JP_PHONE_RE.search(v) or INTL_PHONE_RE.search(v)
                       or JP_POSTAL_RE.search(v) or STREET_RE.search(v)))


def blocked_header(header) -> bool:
    return bool(HEADER_DENY.search(normalize_header(header)))


def _h(*parts) -> int:
    return int.from_bytes(hashlib.sha256("|".join(map(str, parts)).encode("utf-8")).digest()[:8], "big")


def pick_rows(records, columns, resource_id, k=MAX_ROWS):
    """空でない値が多い行を優先し、同点は種で決める。返すのは元の行の番号（昇順）。"""
    scored = []
    for idx, rec in enumerate(records):
        filled = sum(1 for c in columns if str(rec.get(c, "") or "").strip())
        scored.append((-filled, _h(SEED, resource_id, idx), idx))
    return sorted(idx for _, _, idx in sorted(scored)[:k])


def sample_values(records, column, resource_id, k=5):
    vals = [str(r.get(column, "") or "").strip() for r in records]
    vals = [v for v in vals if v]
    rng = random.Random(_h(SEED, resource_id, column))
    return rng.sample(vals, min(k, len(vals)))


def build_rows(meta, fields, records, total):
    """1 つの表から corpus の行（1 行＝1 列）を作る。落とした数は (行, 理由の数) で返す。"""
    rid = meta["resource_id"]
    reasons = {"header_denied": 0, "sensitive_value": 0, "empty": 0, "over_limit": 0}
    kept = []
    for name in fields:
        if blocked_header(name):
            reasons["header_denied"] += 1
            continue
        vals = [str(r.get(name, "") or "").strip() for r in records]
        if not any(vals):
            reasons["empty"] += 1
            continue
        if any(sensitive_value(v) for v in vals):
            reasons["sensitive_value"] += 1
            continue
        kept.append(name)
    if len(kept) > MAX_COLUMNS:
        reasons["over_limit"] = len(kept) - MAX_COLUMNS
        kept = kept[:MAX_COLUMNS]
    if len(kept) < 2 or len(records) < 5:
        return [], reasons
    idx = pick_rows(records, kept, rid)
    out = []
    for name in kept:
        out.append({
            "source": f"{meta.get('source_prefix', 'jp3')}:{meta['publisher_id']}",
            "language": meta.get("language", "ja"),
            "table": meta["download_url"],
            "resource_page": meta["resource_url"],
            "publisher": meta["publisher_id"],
            "pool": "train",
            "license": meta["license"],
            "header": str(name).strip().lstrip("﻿")[:60],
            "values": [v[:60] for v in sample_values(records, name, rid)],
            "context": [str(x)[:40] for x in kept if x != name][:20],
            "row_values": [str(records[i].get(name, "") or "").strip()[:60] for i in idx],
            "row_index": idx,
            "datastore_total": total,
            "fetched_utc": meta["fetched_utc"],
        })
    return out, reasons


def http_json(url, step="", tries=3):
    """1 回ごとに間を空け、403・429・5xx は待って 2 回までやり直す（サーバーの連続アクセスの制限に合わせる）。失敗は段の名前つきで返す。"""
    import time
    from urllib.error import HTTPError
    host = urlparse(url).hostname or ""
    if urlparse(url).scheme != "https" or host not in ALLOWED_HOSTS:
        raise ValueError(f"host not allowed: {host}")
    for attempt in range(tries):
        time.sleep(1.0 + 4.0 * attempt)
        try:
            with urlopen(Request(url, headers={"User-Agent": "jitsuris-train-s11/1.0 (source and license recorded)"}), timeout=60) as resp:
                if (urlparse(resp.geturl()).hostname or "") not in ALLOWED_HOSTS:
                    raise ValueError("redirected outside the allowed hosts")
                return json.loads(resp.read(30_000_001).decode("utf-8-sig"))
        except HTTPError as exc:
            if exc.code in (403, 429) or exc.code >= 500:
                if attempt < tries - 1:
                    continue
            raise RuntimeError(f"{step}: HTTP {exc.code}") from None



SOCRATA_LICENSES = {"PUBLIC_DOMAIN": "public-domain", "CC0_10": "cc0", "CC_30_BY": "cc-by-30", "CC_40_BY": "cc-by-4.0", "ODC_BY_10": "odc-by"}
SOCRATA_SKIP_TYPES = {"location", "point", "multipoint", "line", "multiline", "polygon", "multipolygon", "url", "photo", "document", "blob"}


def fetch_table(item, known):
    """採用の 1 行 → (meta, 列名, 行の dict のリスト, 全体の行数)。取り出し方は item["platform"]（無ければ bodik）。"""
    from pipeline import platform_of, normalize_license
    plat = item.get("platform") or "bodik"
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if plat in ("bodik", "ckan"):
        m = re.search(r"/resource/([0-9a-f-]{36})", item["resource_url"])
        if not m:
            raise ValueError("resource id not found in URL")
        rid = m.group(1)
        if plat == "ckan":
            check, host = platform_of({"resource_url": item["resource_url"]})
            if check != "ckan":
                raise ValueError(f"CKAN host not allowed: {host}")
            ALLOWED_HOSTS.add(host)
        base = item["resource_url"].split("/dataset/")[0] + "/api/3/action/"
        res = http_json(base + "resource_show?" + urlencode({"id": rid}), "resource_show")["result"]
        pkg = http_json(base + "package_show?" + urlencode({"id": res["package_id"]}), "package_show")["result"]
        lic = normalize_license(pkg.get("license_id"))
        if lic not in ALLOWED_LICENSES:
            raise ValueError(f"license not allowed: {pkg.get('license_id')}")
        download = res.get("url") or item["resource_url"]
        if download in known or item["resource_url"] in known:
            raise ValueError("URL overlaps the training corpus or the main set")
        ds = http_json(base + "datastore_search?" + urlencode({"resource_id": rid, "limit": FETCH_LIMIT}), "datastore_search")["result"]
        fields = [f["id"] for f in ds["fields"] if f["id"] != "_id"]
        meta = {"platform": plat, "resource_id": rid, "publisher_id": item["publisher_id"], "resource_url": item["resource_url"],
                "download_url": download, "license": lic, "fetched_utc": now,
                "source_prefix": "jp3" if plat == "bodik" else "world", "language": "ja" if plat == "bodik" else "en"}
        return meta, fields, ds["records"], ds.get("total")
    if plat == "socrata":
        check, host = platform_of({"platform": "socrata", "publisher_id": item["publisher_id"], "resource_id": item.get("resource_id"),
                                   "catalog_url": item["resource_url"]})
        if check != "socrata":
            raise ValueError("Socrata publisher and host do not match")
        ALLOWED_HOSTS.add(host)
        rid = item["resource_id"]
        view = http_json(f"https://{host}/api/views/{rid}.json", "views")
        lic = SOCRATA_LICENSES.get(str(view.get("licenseId") or "").upper()) or normalize_license((view.get("license") or {}).get("name"))
        if lic not in ALLOWED_LICENSES:
            raise ValueError(f"license not allowed: {view.get('licenseId') or (view.get('license') or {}).get('name')}")
        download = f"https://{host}/resource/{rid}.json"
        if download in known or item["resource_url"] in known:
            raise ValueError("URL overlaps the training corpus or the main set")
        cols = [c for c in view.get("columns", []) if c.get("fieldName") and not str(c["fieldName"]).startswith(":")
                and str(c.get("dataTypeName", "")).lower() not in SOCRATA_SKIP_TYPES]
        names = {c["fieldName"]: str(c.get("name") or c["fieldName"]).strip() for c in cols}
        recs = http_json(download + "?" + urlencode({"$limit": FETCH_LIMIT, "$order": ":id"}), "resource")
        records = [{names[k]: (v if isinstance(v, (str, int, float)) else "") for k, v in r.items() if k in names} for r in recs]
        meta = {"platform": plat, "resource_id": rid, "publisher_id": item["publisher_id"], "resource_url": item["resource_url"],
                "download_url": download, "license": lic, "fetched_utc": now, "source_prefix": "world", "language": "en"}
        return meta, [names[c["fieldName"]] for c in cols], records, None
    raise ValueError(f"unknown platform: {plat}")

def known_tables(exclude=None):
    urls = set()
    for f in glob.glob(str(ROOT / "materials" / "real_*.jsonl")) + glob.glob(str(ROOT / "materials" / "pool" / "batch_*.jsonl")):
        if exclude and Path(f).resolve() == Path(exclude).resolve():
            continue   # 作り直すときに自分の出力と重なりと見なさない
        for line in open(f, encoding="utf-8"):
            try:
                urls.add(json.loads(line).get("table", ""))
            except json.JSONDecodeError:
                pass
    prov = ROOT / "independent_eval" / "results" / "main" / "provenance.json"
    if prov.exists():
        for t in json.load(open(prov, encoding="utf-8")).get("tables", []):
            urls.update({t.get("resource_url", ""), t.get("request_url", "")})
    urls.discard("")
    return urls


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--adopted")
    ap.add_argument("--out")
    ap.add_argument("--log")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    adopted = json.load(open(a.adopted, encoding="utf-8"))
    pools = {p["publisher_id"]: p["pool"] for p in json.load(open(ROOT / "independent_eval" / "allocation.json", encoding="utf-8"))["publishers"]}
    known = known_tables(exclude=a.out)
    log = {"adopted": a.adopted, "started_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "tables": []}
    n_cols = 0
    with open(a.out, "w", encoding="utf-8") as fh:
        for item in adopted["adopted"]:
            entry = {"n": item["n"], "publisher_id": item["publisher_id"], "resource_url": item["resource_url"]}
            try:
                if pools.get(item["publisher_id"]) != "train":
                    raise ValueError("publisher is not in the train pool")
                meta, fields, records, total = fetch_table(item, known)
                rows, reasons = build_rows(meta, fields, records, total)
                for r in rows:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
                n_cols += len(rows)
                entry.update({"status": "ok" if rows else "skipped_too_small", "columns": len(rows), "dropped": reasons,
                              "fields": len(fields), "records_read": len(records), "total": total, "platform": meta["platform"]})
            except Exception as exc:  # 1 つの表の失敗で全体を止めない。理由を記録する
                entry.update({"status": "error", "error": f"{type(exc).__name__}: {str(exc)[:200]}"})
            log["tables"].append(entry)
    log["columns"] = n_cols
    log["ok_tables"] = sum(1 for t in log["tables"] if t.get("status") == "ok")
    json.dump(log, open(a.log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"tables ok {log['ok_tables']}/{len(log['tables'])}, columns {n_cols}")
    return 0


def self_test():
    assert sensitive_value("taro@example.jp")
    assert sensitive_value("03-1234-5678") and sensitive_value("09012345678") and sensitive_value("+81 3 1234 5678")
    assert sensitive_value("〒100-0001") and sensitive_value("100-0001")
    for ok in ("2021/04/01", "2021-04-01", "令和3年4月1日", "12345", "1,234,567", "20210401", "3.5%", "R3.4.1", "123-45"):
        assert not sensitive_value(ok), ok
    assert blocked_header("担当者名") and blocked_header("電話番号") and not blocked_header("契約金額（円）")
    recs = [{"a": str(i), "b": "" if i % 3 else str(i * 10), "c": f"x{i}"} for i in range(40)]
    meta = {"resource_id": "r1", "publisher_id": "142018", "resource_url": "u", "download_url": "d", "license": "cc-by-4.0", "fetched_utc": "t"}
    rows, reasons = build_rows(meta, ["a", "b", "c", "電話番号"], recs, 40)
    assert [r["header"] for r in rows] == ["a", "b", "c"] and reasons["header_denied"] == 1
    assert len({tuple(r["row_index"]) for r in rows}) == 1 and len(rows[0]["row_index"]) == MAX_ROWS
    filled_first = [i for i in rows[0]["row_index"] if recs[i]["b"]]
    assert len(filled_first) == 14, len(filled_first)   # b が空でない行（0,3,…,39 の 14 行）が先に選ばれる
    for r in rows:
        assert len(r["row_values"]) == MAX_ROWS and r["row_values"] == [str(recs[i][r["header"]] or "") for i in r["row_index"]]
    rows2, _ = build_rows(meta, ["a", "b", "c"], recs, 40)
    assert rows2 == rows   # 決定的
    rows3, reasons3 = build_rows(meta, ["a", "tel"], [{"a": "1", "tel": "03-1234-5678"}] * 6, 6)
    assert rows3 == [] and reasons3["sensitive_value"] == 1   # 残る列が 1 つなら表ごと使わない
    print("self-test ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
