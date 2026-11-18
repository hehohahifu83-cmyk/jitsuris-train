"""G4（方法 T1 を測る未使用の海外の陣）を作る（2026-11-18 Claude。independent_eval/g3.py を元に書き直した）。
事前記録：bench/g4_prereg_20261118.md（凍結版）。**値は開かない**：このスクリプトは値を表示しない。

  adopt    候補（materials/pool_discover.py --national --pool hold --only-national open.alberta.ca --only-national ckan.govdata.de、語で絞らない）
           → materials/pool/work/g4/adopted.json（採用・控え・落とした理由）
  reserve  1 回目の取り出し（g4/corpus.jsonl・corpus_log.json）で行が取れなかった表だけ、同じ公開元の控えの 1 番目で置き換える
           → materials/pool/work/g4x/adopted.json（1 回だけ。控えも取れなければそこで打ち切り）
  freeze   corpus（g4 と g4x）→ independent_eval/results/g4/g4.json・provenance.json（row_context・row_context_none つき）
  verify   凍結したセットを corpus から作り直し、row_context と除外の決まりが合うかを確かめる（値は表示しない）

採用の決まり（順に、機械的に一意。先生のラベルや金額の多さでは選ばない）：
  1. 候補を落とす：公開元が hold でない／カタログが Alberta・GovData.de でない／G1〜G3 で表を採った公開元（USED_PROVENANCE の publisher）／
     ライセンスが許可の一覧にない／題名が個人の記録になりやすい（pipeline.TITLE_DENY）／datastore も同じ場の CSV も無い／取り出せる場でない／
     使い済みの資源（pipeline.known_resources と USED_WORKS の adopted の resource_url・resource_id）／使い済みのデータセット（(ホスト, dataset の名前) の組）
  2. 残りを h(resource_id)（無ければ h(resource_url)）の小さい順に並べる。同じ値なら resource_url の文字の順
  3. 同じデータセット（(ホスト, dataset の名前)）は最初の 1 表だけ
  4. 公開元ごとに先頭 TABLES_PER_PUBLISHER 表を採用、次の RESERVES_PER_PUBLISHER 表を控え
  5. 採用が MAX_TABLES を超えたら、h(resource_url) の小さい順に MAX_TABLES 表だけ残す（外れた表は控えにしない）
凍結の決まり：1 表 COLS_PER_TABLE 列まで（h(表|列名|corpus の番号) の順）、同じ列名の組（S2.norm の集合）の表は SAME_HEADERS_TABLES まで（h(表) の順）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import sealed2 as S2

ROOT = S2.ROOT
sys.path.insert(0, str(ROOT))
import encoder_context as EC  # noqa: E402
from pipeline import ALLOWED_LICENSES, TITLE_DENY, known_resources, license_id, platform_of  # noqa: E402

SET_ID = "g4-20261118-v1"
POOL = "hold"
WORK = ROOT / "materials" / "pool" / "work" / "g4"
WORK_X = ROOT / "materials" / "pool" / "work" / "g4x"
OUT = ROOT / "independent_eval" / "results" / "g4"
SALT = "jitsuris-g4-v1"
CATALOGS = ("alberta_cat", "govdata_cat")
TABLES_PER_PUBLISHER = 3
RESERVES_PER_PUBLISHER = 2
MAX_TABLES = 300
COLS_PER_TABLE = 10
SAME_HEADERS_TABLES = 2
USED_PROVENANCE = ("independent_eval/results/g1/provenance.json", "independent_eval/results/g2/provenance.json",
                   "independent_eval/results/g3/provenance.json")
USED_WORKS = ("sealed2", "sealed3", "f1", "g1", "g1x", "g2", "g2x", "g3", "g3x")
NONE_REASONS = {"列が無い", "同じ列名が 2 つ以上", "row_index が空の列がある", "列ごとに row_index が違う", "同じ行番号の重複",
                "row_values と row_index の長さが違う"}


def h(s):
    return hashlib.sha256(f"{SALT}|{s}".encode("utf-8")).hexdigest()


def sha_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def norm_pub(p):
    sys.path.insert(0, str(ROOT / "independent_eval"))
    import allocation as A
    return A.normalize_publisher_id(str(p))


def dataset_key(url):
    """(ホスト, dataset の名前)。CKAN の資源の URL（…/dataset/<名前>/resource/…）から。取れなければ None。"""
    u = urlparse(str(url or ""))
    m = re.search(r"/dataset/([^/]+)", u.path)
    return (u.hostname or "", m.group(1)) if m else None


def used_publishers():
    pubs = set()
    for f in USED_PROVENANCE:
        pubs |= {norm_pub(t["publisher"]) for t in json.load(open(ROOT / f, encoding="utf-8"))["tables"]}
    return pubs


def used_resources():
    urls, rids = known_resources()
    for w in USED_WORKS:
        p = ROOT / "materials" / "pool" / "work" / w / "adopted.json"
        if p.exists():
            for x in json.load(open(p, encoding="utf-8"))["adopted"]:
                urls.add(x["resource_url"])
                rids.add(x.get("resource_id"))
    datasets = {k for k in (dataset_key(u) for u in urls) if k}
    return urls, rids, datasets


def adopt_rule(cands, pool_of, used_pubs, known_urls, known_rids, known_datasets):
    """候補 → (採用, 控え（公開元 → 並び）, 落とした理由の数)。上の決まり 1〜5 の順。"""
    why, ok = Counter(), []
    for c in cands:
        url, rid, pub = c.get("resource_url") or "", c.get("resource_id"), norm_pub(c.get("publisher_id", ""))
        reason = None
        if pool_of.get(c.get("publisher_id")) != POOL or c.get("pool") != POOL:
            reason = "公開元が hold でない"
        elif pub.split(":")[0] not in CATALOGS:
            reason = "カタログが Alberta・GovData.de でない"
        elif pub in used_pubs:
            reason = "G1〜G3 で表を採った公開元"
        elif license_id(c) not in ALLOWED_LICENSES:
            reason = "ライセンスが許可の一覧にない"
        elif TITLE_DENY.search(f"{c.get('title', '')} {c.get('resource_name', '')}"):
            reason = "題名が個人の記録になりやすい表"
        elif not c.get("datastore_available") and c.get("access") != "csv":
            reason = "datastore も CSV も無い"
        elif platform_of(c)[0] is None or not rid:
            reason = "取り出せる場でない"
        elif url in known_urls or rid in known_rids:
            reason = "使い済みの資源"
        elif dataset_key(url) in known_datasets:
            reason = "使い済みのデータセット"
        if reason:
            why[reason] += 1
        else:
            ok.append(c)
    ok.sort(key=lambda c: (h(c.get("resource_id") or c.get("resource_url", "")), c.get("resource_url", "")))
    seen_ds, per_pub, adopted, reserves = set(), Counter(), [], defaultdict(list)
    for c in ok:
        ds = dataset_key(c.get("resource_url")) or ("", c.get("resource_url"))
        if ds in seen_ds:
            why["同じデータセットの 2 つ目より後"] += 1
            continue
        seen_ds.add(ds)
        pub = norm_pub(c["publisher_id"])
        plat, host = platform_of(c)
        rec = {"publisher_id": c["publisher_id"], "resource_url": c["resource_url"], "title": c.get("title", ""), "platform": plat, "host": host,
               "resource_id": c["resource_id"], "access": c.get("access") or "datastore", "license": license_id(c)}
        if per_pub[pub] < TABLES_PER_PUBLISHER:
            per_pub[pub] += 1
            adopted.append(rec)
        elif len(reserves[pub]) < RESERVES_PER_PUBLISHER:
            reserves[pub].append(rec)
        else:
            why[f"1 公開元 {TABLES_PER_PUBLISHER} 表＋控え {RESERVES_PER_PUBLISHER} 表まで"] += 1
    if len(adopted) > MAX_TABLES:
        keep = {x["resource_url"] for x in sorted(adopted, key=lambda x: (h(x["resource_url"]), x["resource_url"]))[:MAX_TABLES]}
        why[f"全体で {MAX_TABLES} 表まで"] += len(adopted) - MAX_TABLES
        adopted = [x for x in adopted if x["resource_url"] in keep]
    adopted = [dict(x, n=str(k + 1)) for k, x in enumerate(adopted)]
    pubs_in = {norm_pub(x["publisher_id"]) for x in adopted}
    reserves = {p: r for p, r in reserves.items() if p in pubs_in}
    return adopted, reserves, why


def cmd_adopt(a):
    out = WORK / "adopted.json"
    if out.exists():
        raise SystemExit("adopted.json がもうある（採用は 1 回だけ）")
    cands = []
    for f in a.candidates:
        cands += json.load(open(f, encoding="utf-8")).get("selected") or []
    urls, rids, datasets = used_resources()
    adopted, reserves, why = adopt_rule(cands, S2.pools(), used_publishers(), urls, rids, datasets)
    WORK.mkdir(parents=True, exist_ok=True)
    doc = {"schema_version": 1, "batch": "g4", "pool": POOL, "set_id": SET_ID, "decided_by": "independent_eval/g4.py adopt（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "candidates": [str(Path(f).as_posix()) for f in a.candidates],
           "candidates_sha256": {str(Path(f).as_posix()): sha_file(f) for f in a.candidates},
           "used_provenance_sha256": {f: sha_file(ROOT / f) for f in USED_PROVENANCE}, "used_publishers": len(used_publishers()),
           "candidate_count": len(cands), "dropped": dict(why), "adopted": adopted, "reserves": reserves, "values_viewed": False}
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"adopted {len(adopted)}/{len(cands)} tables from {len({x['publisher_id'] for x in adopted})} publishers; dropped {dict(why)}")


def fetched_tables(work):
    """取り出せた表（corpus.jsonl に行がある資源の resource_page・table）。"""
    got = set()
    p = work / "corpus.jsonl"
    if p.exists():
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                got.add(r.get("resource_page") or r["table"])
                got.add(r["table"])
    return got


def cmd_reserve(a):
    """1 回目に取れなかった表だけを、同じ公開元の控えの 1 番目で置き換える（1 回だけ。控えも取れなければ打ち切り）。"""
    out = WORK_X / "adopted.json"
    if out.exists():
        raise SystemExit("g4x/adopted.json がもうある（1 回だけ）")
    first = json.load(open(WORK / "adopted.json", encoding="utf-8"))
    got = fetched_tables(WORK)
    failed = [x for x in first["adopted"] if x["resource_url"] not in got]
    used = Counter()
    new = []
    for x in failed:
        pub = norm_pub(x["publisher_id"])
        res = first["reserves"].get(pub) or []
        if used[pub] < len(res):
            new.append(dict(res[used[pub]], n=str(len(first["adopted"]) + len(new) + 1), replaces=x["resource_url"]))
            used[pub] += 1
    doc = {"schema_version": 1, "batch": "g4", "pool": POOL, "set_id": SET_ID, "decided_by": "independent_eval/g4.py reserve（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "failed": len(failed), "adopted": new, "values_viewed": False}
    WORK_X.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"failed {len(failed)}; reserves {len(new)}")


def select(rows):
    """corpus の行 → 選んだ行の番号（表の順・表の中は corpus の順）と数えた記録。値は見ない。"""
    by_table = defaultdict(list)
    for i, r in enumerate(rows):
        by_table[r["table"]].append(i)
    stats = Counter()
    picked = {t: sorted(ix, key=lambda i: h(f"{t}|{rows[i]['header']}|{i}"))[:COLS_PER_TABLE] for t, ix in by_table.items()}
    stats["drop_over_10_columns"] = sum(len(ix) - len(picked[t]) for t, ix in by_table.items())
    keep, hset = [], Counter()
    for t in sorted(picked, key=lambda t: (h(t), t)):
        key = frozenset(S2.norm(rows[i]["header"]) for i in by_table[t])
        if hset[key] >= SAME_HEADERS_TABLES:
            stats["drop_same_headers"] += 1
            continue
        hset[key] += 1
        keep.append(t)
    order = {t: k for k, t in enumerate(keep)}
    cols = sorted((i for t in keep for i in picked[t]), key=lambda i: (order[rows[i]["table"]], i))
    return cols, stats


def load_rows():
    rows = [json.loads(line) for line in open(WORK / "corpus.jsonl", encoding="utf-8") if line.strip()]
    extra = WORK_X / "corpus.jsonl"
    if extra.exists():
        rows += [json.loads(line) for line in open(extra, encoding="utf-8") if line.strip()]
    for r in rows:
        r["header"] = str(r["header"]).lstrip("﻿")
    return rows


def build_set(rows):
    """corpus の行 → (セット, provenance の中身)。row_context はセットのその表の列（セットの順）だけで作る（許可された列の集合＝セットの列）。
    単位の欄もセットの列だけから作る（落とした列の値を戻さない）。"""
    cols, stats = select(rows)
    first = {}
    for k, i in enumerate(cols):
        first.setdefault(rows[i]["table"], k)
    tables = sorted(first, key=first.get)
    tid = {t: f"t{k + 1:03d}" for k, t in enumerate(tables)}
    sel = [rows[i] for i in cols]
    units = EC.unit_context_map([(r["header"], r["values"], "", r.get("context") or [], r["table"]) for r in sel])
    out_cols = []
    for k, r in enumerate(sel, 1):
        out_cols.append({"id": f"g4-{k:04d}", "table": tid[r["table"]], "source": r["publisher"], "language": r.get("language", ""),
                         "header": r["header"], "values": r["values"][:5] or [""], "siblings": r.get("context") or [],
                         "unit": units.get(r["table"], "")})
    by_t = defaultdict(list)
    for r in sel:
        by_t[r["table"]].append(r)
    row_context, row_context_none, row_index_sha = {}, {}, {}
    for t in tables:
        ctx, why = EC.table_row_context(t, by_t[t])
        if ctx is None:
            row_context_none[tid[t]] = why
        else:
            row_context[tid[t]] = ctx
        row_index_sha[tid[t]] = hashlib.sha256(json.dumps([r.get("row_index") for r in by_t[t]]).encode("utf-8")).hexdigest()
    doc = {"schema_version": 1, "set_id": SET_ID, "columns": out_cols, "row_context": row_context, "row_context_none": row_context_none}
    meta = {"stats": dict(stats), "tables": tables, "tid": tid, "row_index_sha256": row_index_sha,
            "row_context_version": EC.ROWCTX_VERSION, "row_context_none_reasons": dict(Counter(row_context_none.values())),
            "row_context_sha256": hashlib.sha256(json.dumps(row_context, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()}
    return doc, meta, sel


def check_set(doc, rows):
    """凍結したセットを corpus から作り直して照合する（値は表示しない）。違えば SystemExit。"""
    again, _, sel = build_set(rows)
    if again != doc:
        raise SystemExit("セットを corpus から作り直したものと凍結したものが違う")
    tables = {c["table"] for c in doc["columns"]}
    if set(doc["row_context"]) & set(doc["row_context_none"]) or set(doc["row_context"]) | set(doc["row_context_none"]) != tables:
        raise SystemExit("どの表も row_context か row_context_none のどちらか 1 つだけ、になっていない")
    bad = {v for v in doc["row_context_none"].values() if v not in NONE_REASONS}
    if bad:
        raise SystemExit(f"row_context_none の理由が決まった一覧にない：{len(bad)} 種")
    heads = defaultdict(list)
    for c in doc["columns"]:
        heads[c["table"]].append(c["header"])
    for t, ctx in doc["row_context"].items():
        if ctx["headers"] != heads[t]:
            raise SystemExit(f"{t}：文脈の列がセットの列と違う")
        for h_ in ctx["headers"]:
            EC.check_row_context(ctx, h_)
    # セットの列にない値が row_context に入っていない（文脈の値は、そのセットの列の corpus の row_values の中の値だけ）
    vals = defaultdict(set)
    for r in sel:
        vals[r["header"]].update(str(v) for v in r.get("row_values") or [])
    for ctx in doc["row_context"].values():
        for row in ctx["rows"]:
            for hd, v in zip(ctx["headers"], row):
                if v not in vals[hd]:
                    raise SystemExit("row_context にセットの列の行に無い値がある")
    return True


def cmd_freeze(a):
    rows = load_rows()
    pool_of = S2.pools()
    used = used_publishers()
    bad = [r for r in rows if pool_of.get(r.get("publisher")) != POOL or norm_pub(r.get("publisher")) in used
           or norm_pub(r.get("publisher")).split(":")[0] not in CATALOGS]
    if bad:
        raise SystemExit(f"G4 の公開元でない行がある：{len(bad)}")
    doc, meta, sel = build_set(rows)
    OUT.mkdir(parents=True, exist_ok=True)
    set_path = OUT / "g4.json"
    set_path.write_text(json.dumps(doc, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    adopted = {x["resource_url"]: x for x in json.load(open(WORK / "adopted.json", encoding="utf-8"))["adopted"]}
    if (WORK_X / "adopted.json").exists():
        adopted |= {x["resource_url"]: x for x in json.load(open(WORK_X / "adopted.json", encoding="utf-8"))["adopted"]}
    page = {r["table"]: r.get("resource_page") or r["table"] for r in sel}
    corpus = WORK / "corpus.jsonl"
    extra = WORK_X / "corpus.jsonl"
    prov = {"schema_version": 1, "set_id": SET_ID, "frozen_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "set_path": "independent_eval/results/g4/g4.json", "set_sha256": sha_file(set_path),
            "column_count": len(doc["columns"]), "table_count": len(meta["tables"]), "publisher_count": len({r["publisher"] for r in sel}),
            "columns_per_catalog": dict(Counter(norm_pub(r["publisher"]).split(":")[0] for r in sel)),
            "tables_per_catalog": dict(Counter(norm_pub(next(r["publisher"] for r in sel if r["table"] == t)).split(":")[0] for t in meta["tables"])),
            "selection": meta["stats"], "corpus_sha256": sha_file(corpus), "corpus_extra_sha256": sha_file(extra) if extra.exists() else None,
            "row_context_version": meta["row_context_version"], "row_context_sha256": meta["row_context_sha256"],
            "row_context_tables": len(doc["row_context"]), "row_context_none_reasons": meta["row_context_none_reasons"],
            "row_index_sha256": meta["row_index_sha256"],
            "labels_written": False, "values_viewed": False, "predictions_made": False,
            "tables": [{"table_id": meta["tid"][t], "publisher": next(r["publisher"] for r in sel if r["table"] == t), "resource_url": t,
                        "resource_page": page[t], "title": (adopted.get(page[t]) or adopted.get(t) or {}).get("title", ""),
                        "license": next(r.get("license", "") for r in sel if r["table"] == t)} for t in meta["tables"]]}
    (OUT / "provenance.json").write_text(json.dumps(prov, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    titles = {x["table_id"]: x["title"] for x in prov["tables"] if x["title"]}
    (OUT / "titles.json").write_text(json.dumps(titles, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    check_set(doc, rows)
    print(json.dumps({k: v for k, v in prov.items() if k not in ("tables", "row_index_sha256")}, ensure_ascii=False))


def cmd_verify(a):
    doc = json.load(open(OUT / "g4.json", encoding="utf-8"))
    check_set(doc, load_rows())
    print("ok")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("adopt")
    p.add_argument("--candidates", nargs="+", required=True)
    sub.add_parser("reserve")
    sub.add_parser("freeze")
    sub.add_parser("verify")
    a = ap.parse_args(argv)
    {"adopt": cmd_adopt, "reserve": cmd_reserve, "freeze": cmd_freeze, "verify": cmd_verify}[a.cmd](a)


if __name__ == "__main__":
    main()
