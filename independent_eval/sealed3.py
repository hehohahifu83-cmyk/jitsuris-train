"""封印セット #3 を作る（2026-10-25 Claude。specs/SEALED_EVAL_PROTOCOL.md 第 3・4 章 段 0。合格判定に使う）。

#2（sealed2.py）と同じ規則で選ぶ（目で選ばない）。**値は開かない**：このスクリプトは値を表示しない。数えるのは見出し・表・公開元・言語だけ。
#2 からの違い（オーナー指示 2026-10-25「全体の0.2%でいい」「8〜10%を目指そう」。凍結の前に決めた）：
- 公開元は eval3 だけ（#2 の eval2 と重ならない）
- 列は 1,800 以上（採点 1,500 列以上で「重大 0.2% 以下」を測るため）。取り出せない表があるので、採用は 1 公開元 20 表まで
- 検査役 v2（verifier.py の table_features）が使う、表の行の順にそろった値（最大 20 行）・行の番号・表の行数を、選ばなかった列も含めて
  `table_rows.json` に残す（モデルの入力の `sealed3.json` は #2 と同じ形。値は先頭 5 つ）

  adopt   eval3 の候補（materials/pool_discover.py --pool eval3 の出力）→ materials/pool/work/sealed3/adopted.json
  freeze  取り出した corpus.jsonl → independent_eval/results/sealed3/sealed3.json・table_rows.json・provenance.json。
          凍結したら取り出しの corpus は消す（値の置き場を results/sealed3/ だけにする）

使い方：python independent_eval/sealed3.py adopt --candidates materials/pool/candidates_eval3_*.json
        python independent_eval/sealed3.py freeze
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import sealed2 as S2

ROOT = S2.ROOT
SET_ID = "sealed3-20261025-v1"
POOL = "eval3"
WORK = ROOT / "materials" / "pool" / "work" / "sealed3"
OUT = ROOT / "independent_eval" / "results" / "sealed3"
SALT = "jitsuris-sealed3-v1"
TABLES_PER_PUBLISHER = 20
MIN_COLUMNS = 1800
MAX_ROWS = 20


def _use_salt():
    """sealed2 の選び方（select・h）を #3 の塩で使う。"""
    S2.SALT = SALT


def cmd_adopt(a):
    if (WORK / "adopted.json").exists():
        raise SystemExit("adopted.json がもうある（採用は 1 回だけ）")
    _use_salt()
    cands = []
    for f in a.candidates:
        d = json.load(open(f, encoding="utf-8"))
        cands += d.get("selected") or []
    urls, rids = S2.known_resources()
    # #2 で使った表も除く（公開元が違うので重ならないはずだが、念のため URL で確かめる）
    s2 = ROOT / "materials" / "pool" / "work" / "sealed2" / "adopted.json"
    if s2.exists():
        for x in json.load(open(s2, encoding="utf-8"))["adopted"]:
            urls.add(x["resource_url"])
            rids.add(x.get("resource_id"))
    adopted, why = S2.adopt(cands, S2.pools(), urls, rids, pool=POOL, per_publisher=TABLES_PER_PUBLISHER)
    WORK.mkdir(parents=True, exist_ok=True)
    doc = {"schema_version": 1, "batch": "sealed3", "pool": POOL, "set_id": SET_ID, "decided_by": "independent_eval/sealed3.py adopt（規則だけ）",
           "decided_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "candidates": [str(Path(f).as_posix()) for f in a.candidates],
           "candidate_count": len(cands), "dropped": dict(why), "adopted": adopted, "values_viewed": False}
    (WORK / "adopted.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"adopted {len(adopted)}/{len(cands)} tables from {len({x['publisher_id'] for x in adopted})} publishers; dropped {dict(why)}")


def cmd_freeze(a):
    _use_salt()
    corpus = WORK / "corpus.jsonl"
    rows = [json.loads(line) for line in open(corpus, encoding="utf-8") if line.strip()]
    adopted = {x["resource_url"]: x for x in json.load(open(WORK / "adopted.json", encoding="utf-8"))["adopted"]}
    pool_of = S2.pools()
    bad = [r for r in rows if pool_of.get(r.get("publisher")) != POOL]
    if bad:
        raise SystemExit(f"{POOL} でない公開元の行がある：{len(bad)}")
    th = S2.training_headers()
    cols, stats = S2.select(rows, th)
    if len(cols) < MIN_COLUMNS and not a.allow_small:
        raise SystemExit(f"選んだ列が {len(cols)}（{MIN_COLUMNS} 未満）。候補を足して取り出し直す")
    first = {}
    for k, i in enumerate(cols):
        first.setdefault(rows[i]["table"], k)
    tables = sorted(first, key=first.get)
    tid = {t: f"t{k + 1:03d}" for k, t in enumerate(tables)}
    from encoder_context import unit_context_map  # noqa: E402
    units = unit_context_map([(r["header"], r["values"], "", r.get("context") or [], r["table"]) for r in rows])
    out_cols, col_of = [], {}
    for k, i in enumerate(cols, 1):
        r = rows[i]
        cid = f"s3-{k:04d}"
        col_of[i] = cid
        out_cols.append({"id": cid, "table": tid[r["table"]], "source": r["publisher"], "language": r.get("language", "ja"),
                         "header": r["header"], "values": r["values"][:5] or [""], "siblings": r.get("context") or [],
                         "unit": units.get(r["table"], "")})
    # 検査役 v2 の入力：選んだ表の全部の列（corpus の順）の、行の順にそろった値・行の番号・表の行数
    trows = {tid[t]: [] for t in tables}
    for i, r in enumerate(rows):
        if r["table"] in tid:
            trows[tid[r["table"]]].append({"column": col_of.get(i), "header": r["header"],
                                           "rows": (r.get("row_values") or r["values"])[:MAX_ROWS],
                                           "row_index": (r.get("row_index") or [])[:MAX_ROWS], "total": r.get("datastore_total")})
    OUT.mkdir(parents=True, exist_ok=True)
    set_path, tr_path = OUT / "sealed3.json", OUT / "table_rows.json"
    set_path.write_text(json.dumps({"schema_version": 1, "set_id": SET_ID, "columns": out_cols}, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    tr_path.write_text(json.dumps({"schema_version": 1, "set_id": SET_ID, "tables": trows}, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    sha = hashlib.sha256(set_path.read_bytes()).hexdigest()
    sel = [rows[i] for i in cols]
    ja = sum(S2.is_ja(r["header"]) or r.get("language") == "ja" for r in sel)
    prov = {"schema_version": 1, "set_id": SET_ID, "frozen_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "set_path": "independent_eval/results/sealed3/sealed3.json", "set_sha256": sha,
            "table_rows_path": "independent_eval/results/sealed3/table_rows.json", "table_rows_sha256": hashlib.sha256(tr_path.read_bytes()).hexdigest(),
            "column_count": len(cols), "table_count": len(tables), "publisher_count": len({r["publisher"] for r in sel}),
            "language": dict(Counter(r.get("language", "?") for r in sel)), "japanese_share": round(ja / len(sel), 4) if sel else 0,
            "known_header_share": round(sum(S2.norm(r["header"]) in th for r in sel) / len(sel), 4) if sel else 0,
            "max_publisher_share": round(max(Counter(r["publisher"] for r in sel).values()) / len(sel), 4) if sel else 0,
            "selection": dict(stats), "corpus_sha256": hashlib.sha256(corpus.read_bytes()).hexdigest(),
            "labels_written": False, "values_viewed": False, "blind_sets_read": False, "raw_source_files_written": False,
            "tables": [{"table_id": tid[t], "publisher": next(r["publisher"] for r in sel if r["table"] == t), "resource_url": t,
                        "title": adopted.get(t, {}).get("title", ""), "license": next(r.get("license", "") for r in sel if r["table"] == t)}
                       for t in tables]}
    (OUT / "provenance.json").write_text(json.dumps(prov, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in prov.items() if k != "tables"}, ensure_ascii=False))


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("adopt")
    p.add_argument("--candidates", nargs="+", required=True)
    p = sub.add_parser("freeze")
    p.add_argument("--allow-small", action="store_true")
    a = ap.parse_args(argv)
    {"adopt": cmd_adopt, "freeze": cmd_freeze}[a.cmd](a)


if __name__ == "__main__":
    main()
