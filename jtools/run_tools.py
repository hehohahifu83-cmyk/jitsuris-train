"""道具をまとめて決まった順で呼ぶ（2026-11-01 Claude。IMPROVEMENT_PLAN 9.5「呼び方の決まり」）。

モデルは道具を選ばない。プログラムが毎回同じ順で全部の道具を呼び、結果を列ごとの dict と短い文にする。
文は本体の入力に足す候補・見張りの材料（どちらに使うかは、1 回に 1 要因の決まりで事前記録してから測る）。
外と通信しない。JS 版 run_tools.mjs と同じ結果にする（jtools/fixtures.json）。

  python jtools/run_tools.py <corpus.jsonl> [表の URL]   → 表ごとに列の結果を表示（確かめ用）
順番：1 値の読み取り（read_value）→ 2 番号の検査数字（check_digits）→ 3 表の計算の整合（table_arith、行のそろった値があるときだけ）。
辞書（table_dictionary.py）と値の統計（value_profile.py）は前からある道具で、ここでは呼ばない（すでに評価・入力の段にある）。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jtools import check_digits as CD  # noqa: E402
from jtools import read_value as RV  # noqa: E402
from jtools import table_arith as TA  # noqa: E402

TAG_TEXT = {"product_result": "他の2列の積", "factor": "積の因数", "sum_result": "他の2列の和", "addend": "和の項",
            "tax_included": "税込", "tax_base": "税抜", "tax_amount": "税額", "ratio_result": "比率の結果", "ratio_part": "比率の分子",
            "ratio_whole": "比率の分母", "same_as_other": "他の列と同じ値", "one_side_pair": "片側だけの組"}
CD_TEXT = {"corp_jp": "法人番号", "invoice_jp": "インボイス番号", "gtin": "JAN/EAN", "isbn": "ISBN", "iban": "IBAN", "luhn16": "カード番号の形",
           "lgcode_jp": "団体コード", "postcode_jp": "郵便番号(日)", "postcode_uk": "郵便番号(英)", "postcode_ca": "郵便番号(加)", "postcode_us": "ZIP"}


def run_table(columns) -> list:
    """columns：[{"header": 列名, "values": 列の値（5 つなど）, "rows": 行をそろえた値（任意）}]。列ごとの結果の並びを返す。"""
    out = []
    for c in columns:
        vals = c.get("rows") or c.get("values") or []
        out.append({"read": RV.column_summary(vals), "ids": CD.column_summary(vals), "arith": []})
    with_rows = [i for i, c in enumerate(columns) if c.get("rows")]
    if len(with_rows) >= 2 and len({len(columns[i]["rows"]) for i in with_rows}) == 1:
        tags = TA.column_tags([{"header": columns[i].get("header", ""), "rows": columns[i]["rows"]} for i in with_rows])
        for i, t in zip(with_rows, tags):
            out[i]["arith"] = t
    for r in out:
        r["text"] = to_text(r)
    return out


def _pct(c: int, n: int) -> str:
    return f"{(200 * c + n) // (2 * n)}%"   # 四捨五入（整数だけで計算。JS と同じ）


def to_text(r) -> str:
    """結果を短い文にする（決まった順・決まった語）。何も無ければ空の文字列。"""
    parts = []
    rd = r["read"]
    n = rd["n"]
    if n:
        for k, name in (("date", "日付"), ("time", "時刻"), ("number", "数")):
            if rd[k] * 2 >= n:
                parts.append(f"{name}{_pct(rd[k], n)}")
                break
        if rd["currency"] and rd["number"] * 2 >= n:   # 通貨・単位は、数が半分以上の列だけ
            parts.append(f"通貨{rd['currency']}")
        if rd["unit"] and rd["number"] * 2 >= n:
            parts.append(f"単位{rd['unit']}")
        if rd["era"] * 2 >= n:
            parts.append("和暦")
        if rd["kanji"] * 2 >= n:
            parts.append("漢数字")
        if rd["neg"]:
            parts.append(f"負{_pct(rd['neg'], n)}")
    m = r["ids"].get("n", 0)
    for k in CD.SCHEMES:
        if m >= 3 and r["ids"].get(k, 0) * 5 >= m * 4:   # 違う値が 3 つ以上で、その 8 割以上
            parts.append(CD_TEXT[k])
    parts += [TAG_TEXT[t] for t in r["arith"]]
    return " ".join(parts)


def _main():
    path = sys.argv[1]
    want = sys.argv[2] if len(sys.argv) > 2 else None
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
    tables = {}
    for r in rows:
        tables.setdefault(r["table"], []).append(r)
    for url, cols in tables.items():
        if want and url != want:
            continue
        res = run_table([{"header": c["header"], "values": c.get("values"), "rows": c.get("row_values")} for c in cols])
        print("##", url)
        for c, r in zip(cols, res):
            print(f"  {str(c['header'])[:40]:40}  {r['text']}")


if __name__ == "__main__":
    _main()
