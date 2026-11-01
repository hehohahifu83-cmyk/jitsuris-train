"""道具 3：表の計算の整合（IMPROVEMENT_PLAN 9.5「表の計算の整合」W3b、2026-11-01 Claude）。

同じ表の数の列の組で、行ごとに計算が成り立つかを見る。AI は使わない。外と通信しない。JS 版 table_arith.mjs と同じ結果にする。
入力は行をそろえた値（corpus の row_values。同じ表の列は row_index が同じ）。値は read_value で読む（千円などの倍率は掛けない＝書いてある数で比べる）。

見る関係（a・b・c は別の列。使える行が 5 以上で、その 8 割以上で成り立つ）：
  same      a ≈ b             （同じ値の列。ほかの関係の邪魔をするので先に見つけて、3 列の関係からは外す）
  one_side  a と b のどちらか片方だけが 0 でない行が 9 割以上（借方・貸方、収入・支出の組の候補）
  tax       b ≈ a × (1 + r)   （端数の丸めだけ許す。r は 10%・8%・5%・7.7%・8.1%・19%・20%・7%）
  share     b ≈ a × r         （同じ r。税の額）。tax・share は b が 10 以上の行だけ成り立つと数える（小さな小数の偶然を避ける）
  product   c ≈ a × b         （単価 × 数量 ＝ 金額）
  sum       c ≈ a + b         （税抜 ＋ 税 ＝ 税込、小計の足し算）
  ratio     c ≈ a ÷ b × 100   （率 ＝ 部分 ÷ 全体 × 100。言い換えを避けて、部分が全体以下の向きを採る）
2 列の組は same → one_side → tax・share の順で最初の 1 つ、3 列の組は product → sum → ratio の順で最初の 1 つだけを書く。
割合は整数の数（ok・rows）で返す（Python と JS で丸めが違わないように）。

返り値：relations(columns) → 関係の並び（決まった順）。columns は [{"header": 列名, "rows": 行の値の並び}]（rows は同じ長さ）。
       column_tags(columns) → 列ごとの役目の並び（名前の順）。
"""
from __future__ import annotations

try:
    from jtools.read_value import read_value
except ImportError:   # jtools/ を直に動かすとき
    from read_value import read_value

TAX_RATES = (0.10, 0.08, 0.05, 0.077, 0.081, 0.19, 0.20, 0.07)
MIN_ROWS = 5
MAX_COLS = 40


def _num(v):
    r = read_value(v)
    return r["value"] if r["kind"] == "number" else None


def _enough(ok: int, n: int) -> bool:   # 8 割以上
    return n >= MIN_ROWS and ok * 5 >= n * 4


def close(x: float, y: float) -> bool:
    """丸めの差を許す：差が 0.01 以内、y の 0.5% 以内、または 1 以内（y が 100 以上のとき。円の端数）。"""
    d = abs(x - y)
    if d <= 0.01 or d <= abs(y) * 0.005:
        return True
    return abs(y) >= 100 and d <= 1.0


def close_round(x: float, y: float) -> bool:
    """税の計算用（きつい）：端数の丸めだけを許す。y が 100 以上なら 1 以内、それ未満なら 0.01 ＋ |y| の 0.05% 以内。"""
    d = abs(x - y)
    return d <= 1.0 if abs(y) >= 100 else d <= 0.01 + abs(y) * 0.0005


def _numeric_columns(columns):
    out = []
    for i, c in enumerate(columns):
        vals = [_num(v) for v in c["rows"]]
        got = [v for v in vals if v is not None]
        nonempty = sum(1 for v in c["rows"] if str(v if v is not None else "").strip() != "")
        if len(got) >= MIN_ROWS and len(got) * 5 >= nonempty * 4 and len(set(got)) >= 2:
            out.append((i, vals))
        if len(out) >= MAX_COLS:
            break
    return out


def _count(rows, fn):
    """rows：値の組。どれも数で、最後の値が 0 でない行だけを使う。(成り立った行, 使えた行)。"""
    ok = n = 0
    for r in rows:
        if any(v is None for v in r) or r[-1] == 0:
            continue
        n += 1
        if fn(*r):
            ok += 1
    return ok, n


def _pair(i, a, j, b):
    ok, n = _count(zip(a, b), close)
    if _enough(ok, n):
        return {"rel": "same", "cols": [i, j], "ok": ok, "rows": n}
    pairs = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
    if len(pairs) >= MIN_ROWS:
        one = sum(1 for x, y in pairs if (x == 0) != (y == 0))
        if one * 10 >= len(pairs) * 9 and any(x != 0 for x, _ in pairs) and any(y != 0 for _, y in pairs):
            return {"rel": "one_side", "cols": [i, j], "ok": one, "rows": len(pairs)}
    for p, x, q, y in ((i, a, j, b), (j, b, i, a)):
        for r in TAX_RATES:
            ok, n = _count(zip(x, y), lambda u, v: u != 0 and abs(v) >= 10 and close_round(u * (1 + r), v))
            if _enough(ok, n):
                return {"rel": "tax", "cols": [p, q], "rate": r, "ok": ok, "rows": n}
            ok, n = _count(zip(x, y), lambda u, v: u != 0 and abs(v) >= 10 and close_round(u * r, v))
            if _enough(ok, n):
                return {"rel": "share", "cols": [p, q], "rate": r, "ok": ok, "rows": n}
    return None


def _part_le_whole(x, w) -> bool:
    use = [(u, v) for u, v in zip(x, w) if u is not None and v is not None and v != 0]
    return len(use) > 0 and sum(1 for u, v in use if abs(u) <= abs(v)) * 5 >= len(use) * 4


def _triple(cols3):
    """3 列（番号の小さい順）の組で、product → sum → ratio の最初の 1 つ。"""
    ids = sorted(cols3)
    for k in ids:
        p, q = [x for x in ids if x != k]
        ok, n = _count(zip(cols3[p], cols3[q], cols3[k]), lambda x, y, z: x != 0 and y != 0 and close(x * y, z))
        if _enough(ok, n):
            return {"rel": "product", "cols": [p, q, k], "ok": ok, "rows": n}
    for k in ids:
        p, q = [x for x in ids if x != k]
        ok, n = _count(zip(cols3[p], cols3[q], cols3[k]), lambda x, y, z: x != 0 and y != 0 and close(x + y, z))
        if _enough(ok, n):
            return {"rel": "sum", "cols": [p, q, k], "ok": ok, "rows": n}
    found = []
    for k in ids:
        p, q = [x for x in ids if x != k]
        for part, whole in ((p, q), (q, p)):
            ok, n = _count(zip(cols3[part], cols3[whole], cols3[k]), lambda u, w, z: w != 0 and close(u / w * 100, z))
            if _enough(ok, n):
                found.append(({"rel": "ratio", "cols": [part, whole, k], "ok": ok, "rows": n}, _part_le_whole(cols3[part], cols3[whole])))
    if not found:
        return None
    return next((f for f, good in found if good), found[0][0])


def relations(columns) -> list:
    cols = _numeric_columns(columns)
    out, same = [], set()
    for x in range(len(cols)):
        for y in range(x + 1, len(cols)):
            (i, a), (j, b) = cols[x], cols[y]
            r = _pair(i, a, j, b)
            if r:
                out.append(r)
                if r["rel"] == "same":
                    same.add(j)
    usable = [(i, v) for i, v in cols if i not in same]
    for x in range(len(usable)):
        for y in range(x + 1, len(usable)):
            for z in range(y + 1, len(usable)):
                r = _triple({usable[x][0]: usable[x][1], usable[y][0]: usable[y][1], usable[z][0]: usable[z][1]})
                if r:
                    out.append(r)
    return out


ROLE = {"product": ("factor", "factor", "product_result"), "sum": ("addend", "addend", "sum_result"),
        "tax": ("tax_base", "tax_included"), "share": ("tax_base", "tax_amount"), "ratio": ("ratio_part", "ratio_whole", "ratio_result"),
        "same": ("same_as_other", "same_as_other"), "one_side": ("one_side_pair", "one_side_pair")}


def column_tags(columns) -> list:
    tags = [set() for _ in columns]
    for r in relations(columns):
        for idx, role in zip(r["cols"], ROLE[r["rel"]]):
            tags[idx].add(role)
    return [sorted(t) for t in tags]
