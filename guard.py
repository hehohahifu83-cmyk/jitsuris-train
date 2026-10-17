"""安全の見張り（値と食い違う答えは「不明」にする）。重大な誤り（日付・金額・数量・率・番号の取り違え）を減らすため。
Sherlock（KDD 2019）の「自信のないものは人に回す」の考え方。column-ai.js の guard と同じ。"""
from features import value_stats, STAT_NAMES

NUMERIC = {"date", "amount", "quantity", "rate", "id"}


def bad_ymd8(values):
    """8桁の数字が多いのに、年月日（19xx/20xx・1〜12月・1〜31日）として読めないものが半分以上"""
    import re
    v8 = [str(v).strip() for v in values if re.fullmatch(r"[0-9]{8}", str(v).strip())]
    ne = [v for v in values if str(v).strip()]
    if not ne or len(v8) < len(ne) / 2:
        return False
    ok = sum(v[:2] in ("19", "20") and 1 <= int(v[4:6]) <= 12 and 1 <= int(v[6:]) <= 31 for v in v8)
    return ok < len(v8) / 2


def guard(pred, probs_sorted, values):
    """pred：一番の答え。probs_sorted：[(種類, 確率)] の大きい順。values：値の一覧"""
    if pred == "other":  # 15種類のどれにも当たらない列（測定値・座標・URL など）は決めずに人に回す（v6〜）
        return "unknown"
    s = dict(zip(STAT_NAMES, value_stats(values))) if values else None
    has = s is not None and s["empty"] < 0.999
    if has:
        if pred == "date" and s["date"] + s["datetime"] < 0.5:
            return "unknown"
        if pred == "date" and bad_ymd8(values):  # 10160000 のような8桁のコードを日付と取り違えない（v7〜）
            return "unknown"
        if pred in ("amount", "quantity") and s["num"] < 0.5:
            return "unknown"
        if pred == "rate" and s["num"] + s["pct"] < 0.5:
            return "unknown"
    # 上位2つがどちらも数字の種類で、差が小さいときは決めない
    if len(probs_sorted) > 1:
        (a, pa), (b, pb) = probs_sorted[0], probs_sorted[1]
        if a in NUMERIC and b in NUMERIC and pa - pb < 0.25:
            return "unknown"
    return pred
