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
    for t, off in zip(texts, enc["offset_mapping"]):
        i_r, i_s = t.find(" | 同じ行: "), t.find(" | 同じ表の列: ")
        i_u = t.find(" | 同じ表の単位列の値: ", i_s)
        if i_r >= 0:
            body = t[i_r + 7:i_s]
            first = body.split(" / ")[0]
            cnt["同じ行の 1 行目（全部）"][1] += 1
            cnt["同じ行の 1 行目（全部）"][0] += kept(off, i_r + 7 + len(first))
            if " / " in body:
                cnt["同じ行の 2 行目（全部）"][1] += 1
                cnt["同じ行の 2 行目（全部）"][0] += kept(off, i_s)
        cnt["同じ表の列（全部）"][1] += 1
        cnt["同じ表の列（全部）"][0] += kept(off, i_u if i_u >= 0 else len(t))
        if i_u >= 0:
            cnt["単位列の値（全部）"][1] += 1
            cnt["単位列の値（全部）"][0] += kept(off, len(t))
    lens = sorted(len(x) for x in enc["input_ids"])
    res = {"max_length": mx, "columns": len(texts), "row_context": meta, "tokens_mean": round(sum(lens) / len(lens), 1), "tokens_p95": lens[int(.95 * len(lens))],
           "truncated": round(sum(n > mx - 2 for n in lens) / len(lens), 4),
           "kept": {k: {"rows": v[1], "kept": v[0], "share": round(v[0] / v[1], 4) if v[1] else None} for k, v in cnt.items()}}
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
