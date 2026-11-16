"""方法 T1 の入力の長さの見積り（2026-11-17 Claude。教材庫の検証の行だけを使う。G4 は見ない）。
  python research/table_reading/rowctx_lengths.py → research/table_reading/rowctx_lengths.json
今の決まり（encoder_context の ROWCTX_*）で、題名つきの入力の文の文字数を、同じ行の値なし／ありで比べる。
手元にトークナイザーが無いので文字数で見積もる。本当のトークンの数・切り詰めの率は学習の記録（finetune_exp の token lengths の行）で確かめる。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import glob  # noqa: E402
import encoder_context as ec  # noqa: E402
from exp7 import load_real  # noqa: E402
from pool_families import split_val_by_family  # noqa: E402


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl")))
    rel = [os.path.relpath(f, ROOT) for f in files]
    os.chdir(ROOT)
    pool = load_real(tuple(rel))
    _, val = split_val_by_family(pool, salt="jitsuris-poolval-v2", mod=8)
    recs = [json.loads(line) for f in rel for line in open(f, encoding="utf-8") if line.strip()]
    for d in recs:
        d["header"] = d["header"].lstrip("﻿")
    rcx, why = ec.row_context_map(recs)
    units = ec.unit_context_map(pool)
    titles = json.load(open("materials/pool/titles.json", encoding="utf-8"))
    for t, ttl in titles.items():
        units[t] = units.get(t, "") + ec.TITLE_SEP + ttl
    a = ec.attach_unit_context(val, units, None)
    b = ec.attach_unit_context(val, units, None, rcx)
    la = [len(ec.format_encoder_text(r, "query: ", title=True)) for r in a]
    lb = [len(ec.format_encoder_text(r, "query: ", title=True, row_ctx=True)) for r in b]
    with_ctx = sum(ec.ROW_SEP in r[4] for r in b)
    out = {"rows": len(val), "tables": len({r[4] for r in val}), "rows_with_row_context": with_ctx, "share_with_row_context": round(with_ctx / len(val), 4),
           "not_aligned_tables_in_pool": len(why),
           "chars_without": {"mean": round(sum(la) / len(la), 1), "p50": pct(la, .5), "p95": pct(la, .95), "max": max(la)},
           "chars_with": {"mean": round(sum(lb) / len(lb), 1), "p50": pct(lb, .5), "p95": pct(lb, .95), "max": max(lb)},
           "spec": {"version": ec.ROWCTX_VERSION, "rows": ec.ROWCTX_ROWS, "max_cols": ec.ROWCTX_MAX_COLS, "max_cell": ec.ROWCTX_MAX_CELL, "max_header": ec.ROWCTX_MAX_HEADER}}
    json.dump(out, open(os.path.join(ROOT, "research", "table_reading", "rowctx_lengths.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
