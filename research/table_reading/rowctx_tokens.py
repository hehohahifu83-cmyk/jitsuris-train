"""方法 T1 の入力のトークンでの残り方（2026-11-17 Claude、Codex の点検 3。教材庫の検証の行だけ。G4 は見ない）。
  python research/table_reading/rowctx_tokens.py <トークナイザーのディレクトリか HF の名前> <revision> → research/table_reading/rowctx_tokens.json
control-256（同じ行なし）と T1-256（同じ行あり）の両方で、L24 と同じ入力の設定（FT_CTX_UNIT=1・FT_TITLE=1、FT_VALPROF・FT_VALSEL・FT_UNITX・FT_AUG なし、
接頭辞 "query: "。2026-11-17 Codex の再点検で ctx_unit を足した v2）で学習と同じ文（format_encoder_text）を作り、
トークンの数・256 での切り詰めの率と、どの部分が 256 の中に残るかを数える。
「残る」の定義：その部分の最後の文字までが、特別なトークン 2 つを引いた 254 トークンの中に入る（「始まり」は区切りの直後まで）。
部分：値まで・題名・同じ行の 1 行目・2 行目・同じ表の列名の一覧の始まり／全部・同じ表の単位列の値（全部、ある行だけ）。
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

MAX = 256


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def kept(offsets, end_char):
    """文字の位置 end_char までが MAX トークンの中に入るか（特別なトークン 2 つぶんを引く）。"""
    n = sum(1 for a, b in offsets if b > 0 and a < end_char)
    return n <= MAX - 2


def main():
    from transformers import AutoTokenizer
    name, rev = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else None)
    tok = AutoTokenizer.from_pretrained(name, revision=rev, use_fast=True)
    os.chdir(ROOT)
    files = sorted(glob.glob("materials/pool/batch_*.jsonl"))
    pool = load_real(tuple(files))
    lf = "materials/pool/labelfix_v24.jsonl,materials/pool/labelfix_g24_b3.jsonl,materials/pool/labelfix_g24_sheet.jsonl,materials/pool/labelfix_g24_pool.jsonl"
    pool, _ = ec.apply_label_fix(pool, lf.split(","))   # L24 と同じ付け直し（S・unknown にした列は外す）
    _, val = split_val_by_family(pool, salt="jitsuris-poolval-v2", mod=8)
    recs = [json.loads(line) for f in files for line in open(f, encoding="utf-8") if line.strip()]
    for d in recs:
        d["header"] = d["header"].lstrip("﻿")
    rcx, why = ec.row_context_map(recs, allowed={(str(r[4]), str(r[0])) for r in pool})
    units = ec.unit_context_map(pool)
    for t, ttl in json.load(open("materials/pool/titles.json", encoding="utf-8")).items():
        units[t] = units.get(t, "") + ec.TITLE_SEP + ttl
    out = {"diagnostic_version": "v2", "input_flags": {"FT_CTX_UNIT": "1", "FT_TITLE": "1", "FT_VALPROF": None, "FT_VALSEL": None, "FT_UNITX": None, "FT_AUG": None,
           "prefix": "query: "}, "tokenizer": name, "revision": rev, "max_length": MAX, "rows": len(val), "spec": {"version": ec.ROWCTX_VERSION, "rows": ec.ROWCTX_ROWS,
           "max_cols": ec.ROWCTX_MAX_COLS, "max_cell": ec.ROWCTX_MAX_CELL, "max_header": ec.ROWCTX_MAX_HEADER}}
    for arm, rc in (("control-256", None), ("T1-256", rcx)):
        rows = ec.attach_unit_context(val, units, None, rc)
        texts = [ec.format_encoder_text(r, "query: ", ctx_unit=True, title=True, row_ctx=rc is not None) for r in rows]
        enc = tok(texts, add_special_tokens=False, return_offsets_mapping=True)
        lens = [len(x) for x in enc["input_ids"]]
        res = {"tokens": {"mean": round(sum(lens) / len(lens), 1), "p50": pct(lens, .5), "p95": pct(lens, .95), "max": max(lens)},
               "truncated_at_256": round(sum(n > MAX - 2 for n in lens) / len(lens), 4), "truncated_at_160": round(sum(n > 158 for n in lens) / len(lens), 4)}
        segs = {"値まで": " | 値: ", "題名": " | 表の題名: ", "同じ行": " | 同じ行: ", "同じ表の列": " | 同じ表の列: "}
        UNIT = " | 同じ表の単位列の値: "
        cnt = {k: [0, 0] for k in ("値まで（全部）", "題名（全部）", "同じ行の 1 行目（全部）", "同じ行の 2 行目（全部）", "同じ表の列（始まり）",
                                    "同じ表の列（全部）", "単位列の値（全部）")}
        for t, off in zip(texts, enc["offset_mapping"]):
            def mark(key, end):
                cnt[key][1] += 1
                cnt[key][0] += kept(off, end)
            i_v, i_t, i_r, i_s = (t.find(segs[k]) for k in segs)
            after_v = min(x for x in (i_t, i_r, i_s) if x >= 0)
            mark("値まで（全部）", after_v)
            if i_t >= 0:
                mark("題名（全部）", min(x for x in (i_r, i_s) if x > i_t))
            if i_r >= 0:
                body = t[i_r + len(segs["同じ行"]):i_s]
                first = body.split(" / ")[0]
                mark("同じ行の 1 行目（全部）", i_r + len(segs["同じ行"]) + len(first))
                if " / " in body:
                    mark("同じ行の 2 行目（全部）", i_s)
            mark("同じ表の列（始まり）", i_s + len(segs["同じ表の列"]))
            i_u = t.find(UNIT, i_s)
            mark("同じ表の列（全部）", i_u if i_u >= 0 else len(t))
            if i_u >= 0:
                mark("単位列の値（全部）", len(t))
        res["kept_within_256"] = {k: {"rows": v[1], "kept": v[0], "share": round(v[0] / v[1], 4) if v[1] else None} for k, v in cnt.items()}
        res["rows_with_row_context"] = sum(ec.ROW_SEP in r[4] for r in rows)
        out[arm] = res
    out["tables_not_aligned"] = len(why)
    json.dump(out, open("research/table_reading/rowctx_tokens.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
