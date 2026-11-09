"""F1（評価の陣）を作る（2026-11-09 Claude）。事前記録 bench/g24fix_prereg_20261104.md・bench/fixj_prereg_20261109.md。

封印セット #2・#3（sealed2.py・sealed3.py）と同じ道で作る（目で選ばない）。**値は開かない**：このスクリプトは値を表示しない。
公開元は hold で登録した F1 の組織だけ（research/f1/f1_orgs.py）。

  adopt   hold の候補（materials/pool_discover.py --national --pool hold の出力）→ materials/pool/work/f1/adopted.json
          1 公開元 15 表まで（教材庫と同じ、事前記録の決定）。ハッシュの順
  freeze  取り出した corpus.jsonl → independent_eval/results/f1/f1.json・provenance.json
          1 表 10 列まで（ハッシュの順）・同じ見出しの組は 2 表まで。**学習にある見出しの上限（封印セットの 20%）は付けない**：
          F1 は v2.4（施設の名称）の効き目を測る陣で、名称の列は学習にもある見出しなので、上限を付けると測りたい列が落ちる。
          1 公開元の割合の上限も付けない（鯖江市が大きいことは、結果を公開元・ポータルごとにも書いて扱う、事前記録の決定）。
          凍結のあと、ラベル（先生 2 人の独立の答え）を付ける。

使い方：python independent_eval/f1.py adopt --candidates materials/pool/candidates_f1_*.json
        python independent_eval/f1.py freeze
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import sealed2 as S2

ROOT = S2.ROOT
SET_ID = "f1-20261109-v1"
POOL = "hold"
WORK = ROOT / "materials" / "pool" / "work" / "f1"
OUT = ROOT / "independent_eval" / "results" / "f1"
SALT = "jitsuris-f1-v1"
TABLES_PER_PUBLISHER = 15
COLS_PER_TABLE = 10
SAME_HEADERS_TABLES = 2


def h(s):
    return hashlib.sha256(f"{SALT}|{s}".encode("utf-8")).hexdigest()


def f1_publishers():
    """F1 に入れると決めた公開元（自治体コードか、コードの無い組の ID）。research/f1/f1_orgs.json。"""
    rows = json.load(open(ROOT / "research" / "f1" / "f1_orgs.json", encoding="utf-8"))["rows"]
    return {r["code"] or r["publisher_id"] for r in rows if r["f1"]}


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
    outside = [c for c in cands if str(c.get("publisher_id")) not in allowed]
    if outside:
        raise SystemExit(f"F1 に入れると決めていない公開元の候補がある：{sorted({c.get('publisher_id') for c in outside})[:5]}")
    urls, rids = S2.known_resources()
    for w in ("sealed2", "sealed3"):
        p = ROOT / "materials" / "pool" / "work" / w / "adopted.json"
        if p.exists():
            for x in json.load(open(p, encoding="utf-8"))["adopted"]:
                urls.add(x["resource_url"]); rids.add(x.get("resource_id"))
    S2.SALT = SALT
    adopted, why = S2.adopt(cands, S2.pools(), urls, rids, pool=POOL, per_publisher=TABLES_PER_PUBLISHER)
    WORK.mkdir(parents=True, exist_ok=True)
    doc = {"schema_version": 1, "batch": "f1", "pool": POOL, "set_id": SET_ID, "decided_by": "independent_eval/f1.py adopt（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "candidates": [str(Path(f).as_posix()) for f in a.candidates],
           "candidate_count": len(cands), "dropped": dict(why), "adopted": adopted, "values_viewed": False}
    (WORK / "adopted.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"adopted {len(adopted)}/{len(cands)} tables from {len({x['publisher_id'] for x in adopted})} publishers; dropped {dict(why)}")


def cmd_freeze(a):
    corpus = WORK / "corpus.jsonl"
    rows = [json.loads(line) for line in open(corpus, encoding="utf-8") if line.strip()]
    pool_of = S2.pools()
    bad = [r for r in rows if pool_of.get(r.get("publisher")) != POOL or r.get("publisher") not in f1_publishers()]
    if bad:
        raise SystemExit(f"F1 の公開元でない行がある：{len(bad)}")
    adopted = {x["resource_url"]: x for x in json.load(open(WORK / "adopted.json", encoding="utf-8"))["adopted"]}
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
        out_cols.append({"id": f"f1-{k:04d}", "table": tid[r["table"]], "source": r["publisher"], "language": r.get("language", "ja"),
                         "header": r["header"], "values": r["values"][:5] or [""], "siblings": r.get("context") or [],
                         "unit": units.get(r["table"], "")})
    OUT.mkdir(parents=True, exist_ok=True)
    set_path = OUT / "f1.json"
    set_path.write_text(json.dumps({"schema_version": 1, "set_id": SET_ID, "columns": out_cols}, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    sel = [rows[i] for i in cols]
    th = S2.training_headers()
    prov = {"schema_version": 1, "set_id": SET_ID, "frozen_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "set_path": "independent_eval/results/f1/f1.json", "set_sha256": hashlib.sha256(set_path.read_bytes()).hexdigest(),
            "column_count": len(cols), "table_count": len(tables), "publisher_count": len({r["publisher"] for r in sel}),
            "columns_per_publisher": dict(Counter(r["publisher"] for r in sel).most_common()),
            "known_header_share": round(sum(S2.norm(r["header"]) in th for r in sel) / len(sel), 4) if sel else 0,
            "selection": dict(stats), "corpus_sha256": hashlib.sha256(corpus.read_bytes()).hexdigest(),
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
    sub.add_parser("freeze")
    a = ap.parse_args(argv)
    {"adopt": cmd_adopt, "freeze": cmd_freeze}[a.cmd](a)


if __name__ == "__main__":
    main()
