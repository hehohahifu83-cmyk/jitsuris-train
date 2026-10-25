"""辞書が教材庫（b001〜b014）でどう当たるかを測る（2026-10-26 Claude）。辞書を作る材料には使わない（物差しだけ）。

- 列ごとに、空でない値のうち辞書に完全一致する割合（NFKC・前後の空白を除く）。0.6 以上を「辞書の列」とする
- 辞書の列の正解の種類を数え、見分け方（README）の根拠にする。自治体コードは 6 桁で検査数字が合う割合も見る
使い方：python materials/dict/measure.py > 結果
"""
import json
import os
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "materials" / "dict"))
import verifier_eval as E  # noqa: E402
from fetch_dict import check_digit_jp  # noqa: E402

D = Path(__file__).resolve().parent
BATCHES = tuple(f"b{n:03d}" for n in range(1, 15))


def norm(v):
    return unicodedata.normalize("NFKC", str(v)).strip().casefold()


def load(name):
    p = D / f"{name}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def main():
    jp = load("jp_municipalities")
    dicts = {
        "日本の自治体名": {norm(r["city"]) for r in jp if r["city"]} | {norm(r["pref"]) for r in jp},
        "米国の郡・市": {norm(r["name"]) for r in load("us_counties") + load("us_places")},
        "国名・国コード": {norm(x) for r in load("countries") for x in (r["name"], r["alpha2"], r["alpha3"])},
        "通貨コード": {norm(r["code"]) for r in load("currencies")},
        "ブラジルの市": {norm(r["name"]) for r in load("br_municipios")},
    }
    cols = [c for b in BATCHES for c in E.load_batch(b)]
    for name, words in dicts.items():
        if not words:
            print(f"## {name}：辞書なし")
            continue
        hit = Counter()
        ex = {}
        for c in cols:
            vals = [norm(v) for v in c["values"] if str(v).strip()]
            if len(vals) < 3:
                continue
            share = sum(v in words for v in vals) / len(vals)
            if share >= 0.6:
                t = c["truth"] or "（決めない）"
                hit[t] += 1
                ex.setdefault(t, []).append(c["header"][:20])
        print(f"## {name}（{len(words)} 語）：辞書の列 {sum(hit.values())}")
        for t, n in hit.most_common():
            print(f"  {t}: {n}  例 {ex[t][:6]}")
    # 自治体コードの検査数字
    hit = Counter()
    for c in cols:
        vals = [norm(v) for v in c["values"] if str(v).strip()]
        six = [v for v in vals if len(v) == 6 and v.isdigit()]
        if len(vals) >= 3 and len(six) / len(vals) >= 0.8:
            okd = sum(check_digit_jp(v[:5]) == int(v[5]) for v in six) / len(six)
            hit[(c["truth"] or "（決めない）", "検査数字が合う" if okd >= 0.95 else "合わない")] += 1
    print("## 6 桁の数字の列（自治体コードの検査数字）")
    for k, n in sorted(hit.items(), key=lambda x: -x[1]):
        print(f"  {k}: {n}")


if __name__ == "__main__":
    main()
