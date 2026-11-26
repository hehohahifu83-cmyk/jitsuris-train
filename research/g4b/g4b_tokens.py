"""G4b の上での T1 の入力の切り詰め（2026-11-26 Claude。予測と同じ文で数えるだけ。決まりは変えない）。
  python research/g4b/g4b_tokens.py <T1 の重みのディレクトリ> <出力.json>
evaluate_independent の予測と同じ道（model_rows_of → with_titles → with_row_contexts → texts_of）で文を作り、
重みのトークナイザーで、256 で切れる率と、同じ行の 1・2 行目・同じ表の列名の一覧・単位列の値が全部残る率を数える。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import evaluate_independent as ev  # noqa: E402


def boundaries(row, info):
    """文の区間の終わりを、生の文の中の区切りの文字を探さずに作る（2026-11-26 Codex の点検 3）。
    同じ行の文なしの文（format_encoder_text の同じ関数）と、同じ行の文の各行（render_row_context と同じ式）から組み立て、
    組み立てた文が予測の文と同じことを確かめる。値の中に「 / 」「 | 同じ表の列: 」があっても取り違えない。"""
    import encoder_context as ec
    unit_full = str(row[4] or "")
    base_unit, sep, row_text = unit_full.partition(ec.ROW_SEP)
    plain = ec.format_encoder_text(row[:4] + (base_unit,), info["prefix"], ctx_unit=info["ctx_unit"], val_profile=info.get("val_profile", False), title=True)
    # 同じ表の列名の区間と単位列の区間（format_encoder_text と同じ式）は文の最後にある
    context = row[3] if len(row) > 3 and row[3] else []
    sib = f" | 同じ表の列: {', '.join(str(x)[:20] for x in context[:12])}"
    unit = base_unit.partition(ec.TITLE_SEP)[0]
    unit_seg = f" | 同じ表の単位列の値: {str(unit)[:240]}" if info["ctx_unit"] and unit else ""
    if not plain.endswith(sib + unit_seg):
        raise SystemExit("同じ行の文なしの文の終わりが、同じ表の列名と単位列の区間と合わない")
    head = plain[:len(plain) - len(sib) - len(unit_seg)]
    out = {"row1_end": None, "row2_end": None}
    if row_text:
        seg0 = " | 同じ行: "
        parts = row_text.split(" / ")   # 下で行の数と長さを、文脈から作り直したものと照らす
        text = head + seg0 + row_text + sib + unit_seg
        out["row_lens"] = None
        out["head"] = len(head) + len(seg0)
        out["row_text"] = row_text
    else:
        text = head + sib + unit_seg
    out["text"] = text
    start_sib = len(text) - len(sib) - len(unit_seg)
    out["siblings_end"] = start_sib + len(sib)
    out["unit_end"] = len(text) if unit_seg else None
    return out


def row_ends(b, ctx, header):
    """同じ行の 1・2 行目の終わり（render_row_context と同じ式で各行を作り、つないだものが文の同じ行の部分と同じことを確かめる）。"""
    import encoder_context as ec
    keep = [i for i, h in enumerate(ctx["headers"]) if h != str(header)][:ec.ROWCTX_MAX_COLS]
    rows = ["; ".join(f"{ctx['headers'][i][:ec.ROWCTX_MAX_HEADER]}={str(r[i]).strip()[:ec.ROWCTX_MAX_CELL]}" for i in keep) for r in ctx["rows"]]
    if " / ".join(rows) != b["row_text"]:
        raise SystemExit("同じ行の部分を文脈から作り直したものと文が違う")
    b["row1_end"] = b["head"] + len(rows[0])
    b["row2_end"] = b["head"] + len(rows[0]) + 3 + len(rows[1]) if len(rows) > 1 else None
    return b


def main():
    ck, out = sys.argv[1], sys.argv[2]
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(ck, use_fast=True)
    info = ev.checkpoint_info(ck)
    set_data, _ = ev.load_set(os.path.join(ROOT, "independent_eval", "results", "g4b", "g4b.json"))
    rows = ev.model_rows_of(set_data, info)
    rows = ev.with_titles(rows, set_data, json.load(open(os.path.join(ROOT, "independent_eval", "results", "g4b", "titles.json"), encoding="utf-8")))
    rows, meta = ev.with_row_contexts(rows, set_data, info)
    texts = ev.texts_of(rows, info, title=True)
    mx = int(info["max_length"])
    enc = tok(texts, add_special_tokens=False, return_offsets_mapping=True)
    def kept(off, end):
        return sum(1 for a, b in off if b > 0 and a < end) <= mx - 2
    cnt = {k: [0, 0] for k in ("同じ行の 1 行目（全部）", "同じ行の 2 行目（全部）", "同じ表の列（全部）", "単位列の値（全部）")}
    tables = [c.get("table") or "" for c in set_data["columns"]]
    for r, t, off, tb in zip(rows, texts, enc["offset_mapping"], tables):
        b = boundaries(r, info)
        if "row_text" in b:
            b = row_ends(b, set_data["row_context"][tb], r[0])
        if b["text"] != t:
            raise SystemExit("区間を作り直した文が予測の文と違う")
        if b["row1_end"] is not None:
            cnt["同じ行の 1 行目（全部）"][1] += 1
            cnt["同じ行の 1 行目（全部）"][0] += kept(off, b["row1_end"])
        if b["row2_end"] is not None:
            cnt["同じ行の 2 行目（全部）"][1] += 1
            cnt["同じ行の 2 行目（全部）"][0] += kept(off, b["row2_end"])
        cnt["同じ表の列（全部）"][1] += 1
        cnt["同じ表の列（全部）"][0] += kept(off, b["siblings_end"])
        if b["unit_end"] is not None:
            cnt["単位列の値（全部）"][1] += 1
            cnt["単位列の値（全部）"][0] += kept(off, b["unit_end"])
    lens = sorted(len(x) for x in enc["input_ids"])
    res = {"max_length": mx, "columns": len(texts), "row_context": meta, "tokens_mean": round(sum(lens) / len(lens), 1), "tokens_p95": lens[int(.95 * len(lens))],
           "truncated": round(sum(n > mx - 2 for n in lens) / len(lens), 4),
           "kept": {k: {"rows": v[1], "kept": v[0], "share": round(v[0] / v[1], 4) if v[1] else None} for k, v in cnt.items()}}
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
