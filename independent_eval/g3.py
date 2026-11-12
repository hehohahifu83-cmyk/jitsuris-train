"""G3（金額・単位の列が多い海外の陣、直し M を測り直す）を作る（2026-11-12 Claude。independent_eval/g2.py を写した）。事前記録 bench/fixm_prereg_20261112.md の G3 の追記。

封印セット #2・#3（sealed2.py・sealed3.py）と同じ道で作る（目で選ばない）。**値は開かない**：このスクリプトは値を表示しない。
公開元は G1 と同じ 3 カタログの hold の組織のうち、G1 で表を採用した公開元を除いたものだけ（research/g3/g3_orgs.py）。

  adopt   hold の候補（materials/pool_discover.py --national --pool hold --only-national <G1 の 3 ホスト> --query <金額・単位の語> の出力）→ materials/pool/work/g3/adopted.json
          1 公開元 2 表まで・全体で 160 表まで（どちらもハッシュの順。組織が 309 と多いので、ラベルの量を抑える。事前記録の決定）
  freeze  取り出した corpus.jsonl → independent_eval/results/g3/g3.json・provenance.json
          1 表 10 列まで（ハッシュの順）・同じ見出しの組は 2 表まで。**学習にある見出しの上限（封印セットの 20%）は付けない**：
          F1 と同じ作り方にそろえる（L と L24 を同じ条件で比べる陣）。
          凍結のあと、ラベル（先生 2 人の独立の答え）を付ける。

使い方：python independent_eval/g3.py adopt --candidates materials/pool/candidates_g3_*.json
        python independent_eval/g3.py freeze
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import sealed2 as S2

ROOT = S2.ROOT
SET_ID = "g3-20261112-v1"
POOL = "hold"
WORK = ROOT / "materials" / "pool" / "work" / "g3"
OUT = ROOT / "independent_eval" / "results" / "g3"
SALT = "jitsuris-g3-v1"
TABLES_PER_PUBLISHER = 5   # 2026-11-12：候補が少ないので 2 → 5（採用の前）
MAX_TABLES = 320
COLS_PER_TABLE = 10
SAME_HEADERS_TABLES = 2


def h(s):
    return hashlib.sha256(f"{SALT}|{s}".encode("utf-8")).hexdigest()


def f1_publishers():
    """G3 に入れると決めた公開元（research/g3/g3_orgs.json。名前は F1 の道具と同じ関数名のまま）。"""
    sys.path.insert(0, str(ROOT / "independent_eval"))
    import allocation as A
    rows = json.load(open(ROOT / "research" / "g3" / "g3_orgs.json", encoding="utf-8"))["rows"]
    return {A.normalize_publisher_id(r["publisher_id"]) for r in rows if r["g1"]}   # 2026-11-12：G1 の公開元も入れる（表は G1 と重ならない。事前記録の追記）


def select(rows):
    """corpus の行 → 選んだ行の番号（表の順・表の中は corpus の順）と数えた記録。値は見ない。"""
    by_table = defaultdict(list)
    for i, r in enumerate(rows):
        by_table[r["table"]].append(i)
    stats = Counter()
    picked = {t: sorted(ix, key=lambda i: h(f"{t}|{rows[i]['header']}|{i}"))[:COLS_PER_TABLE] for t, ix in by_table.items()}
    stats["drop_over_10_columns"] = sum(len(ix) - len(picked[t]) for t, ix in by_table.items())
    keep, hset = [], Counter()
    for t in sorted(picked, key=h):
        key = frozenset(S2.norm(rows[i]["header"]) for i in by_table[t])
        if hset[key] >= SAME_HEADERS_TABLES:
            stats["drop_same_headers"] += 1
            continue
        hset[key] += 1
        keep.append(t)
    order = {t: k for k, t in enumerate(keep)}
    cols = sorted((i for t in keep for i in picked[t]), key=lambda i: (order[rows[i]["table"]], i))
    return cols, stats


def cmd_adopt(a):
    if (WORK / "adopted.json").exists():
        raise SystemExit("adopted.json がもうある（採用は 1 回だけ）")
    cands = []
    for f in a.candidates:
        cands += json.load(open(f, encoding="utf-8")).get("selected") or []
    allowed = f1_publishers()
    cands = [c for c in cands if str(c.get("publisher_id")) in allowed]   # G1 の公開元（と G3 でない組織）の候補は使わない
    urls, rids = S2.known_resources()
    for w in ("sealed2", "sealed3", "f1", "g1", "g1x", "g2", "g2x"):
        p = ROOT / "materials" / "pool" / "work" / w / "adopted.json"
        if p.exists():
            for x in json.load(open(p, encoding="utf-8"))["adopted"]:
                urls.add(x["resource_url"]); rids.add(x.get("resource_id"))
    S2.SALT = SALT
    adopted, why = S2.adopt(cands, S2.pools(), urls, rids, pool=POOL, per_publisher=TABLES_PER_PUBLISHER)
    if len(adopted) > MAX_TABLES:   # 全体の上限：表の URL のハッシュの順
        keep = {x["resource_url"] for x in sorted(adopted, key=lambda x: h(x["resource_url"]))[:MAX_TABLES]}
        why[f"全体で {MAX_TABLES} 表まで"] += len(adopted) - MAX_TABLES
        adopted = [dict(x, n=str(k + 1)) for k, x in enumerate(y for y in adopted if y["resource_url"] in keep)]
    WORK.mkdir(parents=True, exist_ok=True)
    doc = {"schema_version": 1, "batch": "g3", "pool": POOL, "set_id": SET_ID, "decided_by": "independent_eval/g3.py adopt（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "candidates": [str(Path(f).as_posix()) for f in a.candidates],
           "candidate_count": len(cands), "dropped": dict(why), "adopted": adopted, "values_viewed": False}
    (WORK / "adopted.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"adopted {len(adopted)}/{len(cands)} tables from {len({x['publisher_id'] for x in adopted})} publishers; dropped {dict(why)}")


EXTRA_PER_PUBLISHER = 4
EXTRA_TOTAL = 480
EXTRA_ADOPTED = ROOT / "materials" / "pool" / "work" / "g3x" / "adopted.json"


def cmd_adopt_extra(a):
    """足りない列を足す（2026-11-11、値を見る前・取り出しの数だけを見て決めた。事前記録の追記）。
    同じ候補から、1 公開元 5 表まで（ハッシュの順）で選び直し、もう採用した表は全部残して、新しい表を表の URL のハッシュの順に全体 320 表まで足す。
    新しい表だけを materials/pool/work/g3x/adopted.json に書く（取り出しは別に依頼し、g3x/corpus.jsonl を g3 の corpus.jsonl の後ろにつなぐ）。"""
    if EXTRA_ADOPTED.exists():
        raise SystemExit("g3x/adopted.json がもうある（1 回だけ）")
    first = json.load(open(WORK / "adopted.json", encoding="utf-8"))
    have = {x["resource_url"] for x in first["adopted"]}
    cands = []
    for f in first["candidates"]:
        cands += json.load(open(ROOT / f, encoding="utf-8")).get("selected") or []
    cands = [c for c in cands if str(c.get("publisher_id")) in f1_publishers()]
    urls, rids = S2.known_resources()
    for w in ("sealed2", "sealed3", "f1", "g1", "g1x", "g2", "g2x"):
        p = ROOT / "materials" / "pool" / "work" / w / "adopted.json"
        if p.exists():
            for x in json.load(open(p, encoding="utf-8"))["adopted"]:
                urls.add(x["resource_url"]); rids.add(x.get("resource_id"))
    S2.SALT = SALT
    wide, why = S2.adopt(cands, S2.pools(), urls, rids, pool=POOL, per_publisher=EXTRA_PER_PUBLISHER)
    new = sorted((x for x in wide if x["resource_url"] not in have), key=lambda x: h(x["resource_url"]))[:max(0, EXTRA_TOTAL - len(have))]
    new = [dict(x, n=str(len(have) + k + 1)) for k, x in enumerate(new)]
    doc = {"schema_version": 1, "batch": "g3", "pool": POOL, "set_id": SET_ID, "decided_by": "independent_eval/g3.py adopt-extra（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "candidates": first["candidates"],
           "rule": f"1 公開元 {EXTRA_PER_PUBLISHER} 表まで、全体 {EXTRA_TOTAL} 表まで（もう採用した {len(have)} 表は残す）", "adopted": new, "values_viewed": False}
    EXTRA_ADOPTED.parent.mkdir(parents=True, exist_ok=True)
    EXTRA_ADOPTED.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"extra {len(new)} tables from {len({x['publisher_id'] for x in new})} publishers")


def cmd_freeze(a):
    corpus = WORK / "corpus.jsonl"
    rows = [json.loads(line) for line in open(corpus, encoding="utf-8") if line.strip()]
    extra = EXTRA_ADOPTED.parent / "corpus.jsonl"
    if extra.exists():   # 足した表（adopt-extra）を後ろにつなぐ
        rows += [json.loads(line) for line in open(extra, encoding="utf-8") if line.strip()]
    pool_of = S2.pools()
    bad = [r for r in rows if pool_of.get(r.get("publisher")) != POOL or r.get("publisher") not in f1_publishers()]
    if bad:
        raise SystemExit(f"G3 の公開元でない行がある：{len(bad)}")
    adopted = {x["resource_url"]: x for x in json.load(open(WORK / "adopted.json", encoding="utf-8"))["adopted"]}
    if EXTRA_ADOPTED.exists():
        adopted |= {x["resource_url"]: x for x in json.load(open(EXTRA_ADOPTED, encoding="utf-8"))["adopted"]}
    cols, stats = select(rows)
    first = {}
    for k, i in enumerate(cols):
        first.setdefault(rows[i]["table"], k)
    tables = sorted(first, key=first.get)
    tid = {t: f"t{k + 1:03d}" for k, t in enumerate(tables)}
    from encoder_context import unit_context_map  # noqa: E402
    units = unit_context_map([(r["header"], r["values"], "", r.get("context") or [], r["table"]) for r in rows])
    out_cols = []
    for k, i in enumerate(cols, 1):
        r = rows[i]
        out_cols.append({"id": f"g3-{k:04d}", "table": tid[r["table"]], "source": r["publisher"], "language": r.get("language", "ja"),
                         "header": r["header"], "values": r["values"][:5] or [""], "siblings": r.get("context") or [],
                         "unit": units.get(r["table"], "")})
    OUT.mkdir(parents=True, exist_ok=True)
    set_path = OUT / "g3.json"
    set_path.write_text(json.dumps({"schema_version": 1, "set_id": SET_ID, "columns": out_cols}, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    sel = [rows[i] for i in cols]
    th = S2.training_headers()
    prov = {"schema_version": 1, "set_id": SET_ID, "frozen_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "set_path": "independent_eval/results/g3/g3.json", "set_sha256": hashlib.sha256(set_path.read_bytes()).hexdigest(),
            "column_count": len(cols), "table_count": len(tables), "publisher_count": len({r["publisher"] for r in sel}),
            "columns_per_publisher": dict(Counter(r["publisher"] for r in sel).most_common()),
            "known_header_share": round(sum(S2.norm(r["header"]) in th for r in sel) / len(sel), 4) if sel else 0,
            "selection": dict(stats), "corpus_sha256": hashlib.sha256(corpus.read_bytes()).hexdigest(), "corpus_extra_sha256": hashlib.sha256(extra.read_bytes()).hexdigest() if extra.exists() else None,
            "labels_written": False, "values_viewed": False, "predictions_made": False,
            "tables": [{"table_id": tid[t], "publisher": next(r["publisher"] for r in sel if r["table"] == t), "resource_url": t,
                        "title": adopted.get(t, {}).get("title", ""), "license": next(r.get("license", "") for r in sel if r["table"] == t)}
                       for t in tables]}
    (OUT / "provenance.json").write_text(json.dumps(prov, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in prov.items() if k not in ("tables", "columns_per_publisher")}, ensure_ascii=False))


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("adopt")
    p.add_argument("--candidates", nargs="+", required=True)
    sub.add_parser("adopt-extra")
    sub.add_parser("freeze")
    a = ap.parse_args(argv)
    {"adopt": cmd_adopt, "adopt-extra": cmd_adopt_extra, "freeze": cmd_freeze}[a.cmd](a)


if __name__ == "__main__":
    main()
