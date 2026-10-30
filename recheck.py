"""見張りのあとの 2 段の検査（2026-10-25 Claude。オーナー指示「重大な間違いをゼロにできるまでは商品化は視野に入れない」「不明にしたものを再検査する規則も付けろ」）。

1. 言い切りの検査：数字の種類（日付・金額・数量・率・番号）と言い切る前に、根拠がそろっているかを見る。そろっていなければ「不明」に下げる
   - 値に根拠がない（空か同じ値ばかり）のに、列名にもその種類の手がかりがない
   - 列名・単位が別の数字の種類を強く示している（例：「〜量」「(t)」なのに金額）
   - 列名が年・年度だけ（2020、R5、FY2021）で、単位の手がかりがない（LABEL_GUIDE v1.4・v1.7 では unknown）
   - 確率が低い（1 位 < t_low）のに、列名にその種類の手がかりがない
2. 不明の再検査：不明になった列（見張りが不明にした列と 1. で下げた列）を、列名・単位・同じ表の列名で調べ直す
   - 列名・単位の強い手がかりがちょうど 1 つの種類を示し、その種類がモデルの上位 3 つに入っていれば、その種類にする
   - 日付は見張り v11 の列名の規則（guard.header_date_ok）が通れば日付にする
   - どれにも当たらなければ不明のまま

学習はしない（規則だけ）。入力は見張りの判定・上位 3 つの確率・列の中身。
"""
from __future__ import annotations

import re
import unicodedata

NUMERIC = {"date", "amount", "quantity", "rate", "id"}

# 強い手がかり（列名・単位の文字列に現れたら、その種類を強く示す）。語の境目は英字だけで見る
CUES = {
    "amount": [r"円", r"千円", r"万円", r"金額", r"予算", r"決算", r"費用", r"経費", r"料金", r"手数料", r"単価", r"価格", r"収入", r"支出", r"歳入", r"歳出",
               r"給与", r"賃金", r"報酬", r"税額", r"\$", r"€", r"£", r"R\$", r"\bUSD\b", r"\bEUR\b", r"\bamount\b", r"\bcost", r"\bprice", r"\brevenue",
               r"\bexpend", r"\bspend", r"\bpayment", r"\bsalar", r"\bwage", r"\bbudget", r"\bfee\b", r"\bfees\b", r"\bvalor\b", r"\bdespesa", r"\breceita",
               r"\bremunera", r"\bdollars?\b", r"\beuros?\b"],
    "quantity": [r"人数", r"件数", r"世帯数", r"戸数", r"台数", r"回数", r"冊数", r"箇所数", r"人口", r"世帯", r"（人）", r"\(人\)", r"（件）", r"\(件\)", r"（t）",
                 r"\(t\)", r"（ｔ）", r"\(ｔ\)", r"（kg）", r"\(kg\)", r"（冊）", r"（台）", r"（回）", r"（戸）", r"数量", r"排出量", r"搬入量", r"搬出量", r"回収量",
                 r"収集量", r"\bcount\b", r"\bnumber of\b", r"\bnum_", r"\bqty\b", r"\bquantity", r"\bpopulation\b", r"\bcases\b", r"\btonnes?\b",
                 r"\btons?\b", r"\bpersons?\b", r"\bpeople\b", r"\bhouseholds?\b", r"\bvisitors?\b", r"\bnumero de\b", r"\bqtd_?", r"#\s*of\b", r"\bno_of_", r"\bno\.? of\b"],
    "rate": [r"％", r"%", r"率", r"割合", r"比率", r"構成比", r"前年比", r"比$", r"比\s*[（(]", r"\bpercent", r"\bratio\b", r"\brate\b", r"\bshare\b", r"\bpct\b", r"\bproportion"],
    "id": [r"コード$", r"番号$", r"ＩＤ$", r"\bID$", r"_ID$", r"\bid$", r"\bcode$", r"\bno\.?$", r"\bnumber$", r"\bcodigo\b", r"\bnum_?processo"],
    "date": [r"年月日", r"日付", r"日時", r"年度$", r"\bdate\b", r"\bdata\b", r"\bdatetime\b", r"\btimestamp\b", r"\byear\b", r"\bmonth\b"],
}
# 弱めて扱う語：「料金」「金額」でも「件数」がある列は件数（例：「手数料の件数」）。2 つ以上の種類が出たら手がかりなし
_PERIOD_HEADER = re.compile(r"^\s*(\d{1,2}\s*月|(19|20)\d{2}(年度?|年)?|(19|20)\d{2}\s*[-/~～]\s*\d{2,4}|FY\s*\d{2,4}|[RHS]\s*\d{1,2}|令和\s*\d+年?度?|平成\s*\d+年?度?|昭和\s*\d+年?度?)\s*$", re.I)
_COMPILED = {k: [re.compile(p, re.I) for p in v] for k, v in CUES.items()}
# 軸の列の列名（F4）。確かめる陣 15 陣で正しい +2・重大 ±0（research/fixes/confirm.md）
_DIM_HEADER = re.compile(r"^(statistic|statistic label|tlist\(.*\)|c\d+v\d+|year|jahr|annee|année|quarter|quartal|month|monat|mois|week|woche|semaine|"
                         r"period|periode|période|time_period|temporal|date|datum|geo\w*|region|kanton|canton|gemeinde|unit|einheit)$", re.I)


def _norm(s) -> str:
    return unicodedata.normalize("NFKC", str(s or "")).replace("\n", " ").strip()


_BAND = re.compile(r"(以上|未満|超|以下|～|〜|~)|\d[\d,.]*\s*[-–]\s*[$€£¥]?\s*\d")


def cue_types(header, unit="") -> set:
    """列名と単位の文字列に現れた強い手がかりの種類の集合。番号・日付の手がかりは列名だけで見る（単位の列の値「Number」などで誤らないため）。
    区切りの列名（「100万円以上200万円未満」「0-4」）は区分ごとの数なので手がかりにしない。"""
    h = _norm(header)
    if _BAND.search(h):
        return set()
    # 2026-10-30（F4、オーナー「1はいい」）：縦持ちの表の単位の列（UNIT: %）は値の列のためのもの。軸の列（STATISTIC・TLIST・年・四半期・地域など）には当てない
    u = "" if _DIM_HEADER.match(h) else _norm(unit)
    hits = set()
    for k, pats in _COMPILED.items():
        targets = (h,) if k in ("id", "date") else (h, u)
        if any(p.search(t) for p in pats for t in targets if t):
            hits.add(k)
    # 「〜数」で終わる列名は数量（「人数」「件数」以外も：開館日数・定員数）。ただし「指数」は除く
    if re.search(r"数(\s*[（(].*[)）])?$", h) and not re.search(r"指数|係数|倍数|号数|番号|頁数", h):
        hits.add("quantity")
    return hits


def single_cue(header, unit="") -> str | None:
    hits = cue_types(header, unit)
    # 率と数量が同時に出たら率（「人口比率」「件数の割合」）、id は列名の末尾だけなので他と同時なら他を優先
    if "rate" in hits and hits - {"rate"} <= {"quantity", "amount"}:
        return "rate"
    hits = hits - {"id"} if len(hits) > 1 else hits
    return next(iter(hits)) if len(hits) == 1 else None


_EMPTY = ("", "-", "－", "―", "…", "nan", "None", "NULL")


def _values_without_evidence(values) -> bool:
    """値が空か欠けばかり（数の種類を決める根拠にならない）。
    2026-10-30（bench/root_cause_fixes_prereg_20261030.md の F8、オーナー「1はいい」）：0 ばかりの列は根拠なしにしない。
    b013・b014 で決めたときは損 4・得 1 だったが、新しい陣（0 ばかりの件数の列が多い）では損だけで、確かめる陣 15 陣で正しい +4・重大 ±0。"""
    return not [v for v in values if _norm(v) not in _EMPTY]


def _numeric_share(values) -> float:
    vals = [_norm(v) for v in values if _norm(v) not in _EMPTY]
    if not vals:
        return 0.0
    ok = sum(bool(re.fullmatch(r"[-+△▲]?[\$€£¥R]*\s*[\d,.]+\s*(円|%|％|人|件|t)?", v)) for v in vals)
    return ok / len(vals)


def _as_float(v):
    try:
        return float(_norm(v).replace(",", ""))
    except ValueError:
        return None


def period_header(header) -> bool:
    return bool(_PERIOD_HEADER.match(_norm(header)))


def check_assert(pred, top3, values, header, unit="", t_low=0.0, siblings=None):
    """1. 言い切りの検査。数字の種類と言い切った列だけを見る。(判定, 理由 or None)。"""
    if pred not in NUMERIC:
        return pred, None
    cues = cue_types(header, unit)
    cue = single_cue(header, unit)
    p1 = top3[0]["probability"] if top3 else 1.0
    if pred in ("amount", "quantity", "rate") and _values_without_evidence(values) and pred not in cues:
        return "unknown", "no_value_evidence"
    if cue is not None and cue != pred and cue in NUMERIC and not (pred == "id" and cue in ("quantity",) and re.search(r"(コード|番号|\bid|\bcode|\bno\.?)$", _norm(header), re.I)):
        return "unknown", f"cue_conflict:{cue}"
    vals = [_norm(v) for v in values if _norm(v) not in _EMPTY]
    if period_header(header) and pred in ("amount", "quantity") and not (cues & {"amount", "quantity", "rate"}):
        return "unknown", "period_header_no_unit"
    if period_header(header) and pred == "date" and vals and all(re.fullmatch(r"\d{1,4}(\.0+)?", v) for v in vals) and \
            not any(1900 <= float(v) <= 2100 for v in vals):
        return "unknown", "period_header_counts"
    if pred == "amount" and _BAND.search(_norm(header)) and re.search(r"円|\$|€|£|income|万", _norm(header), re.I):
        return "unknown", "money_band_header"
    if pred == "amount" and siblings is not None and "amount" not in cues and \
            not any("amount" in cue_types(sb) for sb in siblings) and not re.search(r"円|\$|€|£|R\$", " ".join(vals)):
        return "unknown", "amount_without_cue"
    if pred == "rate" and "rate" not in cues and not any(("%" in v or "％" in v) for v in vals) and \
            any(_as_float(v) is not None and abs(_as_float(v)) > 1 for v in vals):
        return "unknown", "rate_without_cue"
    if pred == "amount" and "amount" not in cues and any(re.search(r"[.,]\d*[1-9]\d*$", v) and len(re.split(r"[.,]", v)[-1].rstrip("0")) >= 3 for v in vals):
        return "unknown", "amount_precision"
    if p1 < t_low and pred not in cues:
        return "unknown", "low_confidence_no_cue"
    return pred, None


def recheck_unknown(top3, values, header, unit="", header_date_ok=None):
    """2. 不明の再検査。(判定, 理由)。当たらなければ ("unknown", None)。"""
    cand = [t["label"] for t in (top3 or [])][:3]
    if header_date_ok is not None and "date" in cand and header_date_ok(header, values):
        return "date", "recheck:date_header"
    cue = single_cue(header, unit)
    if cue and cue in cand and not period_header(header) and not _values_without_evidence(values) and \
            (cue not in ("amount", "quantity", "rate") or _numeric_share(values) >= 0.6):
        return cue, f"recheck:cue_{cue}"
    return "unknown", None


def decide(guarded, top3, values, header, unit="", t_low=0.0, use_recheck=True, header_date_ok=None, siblings=None):
    """見張りの判定 → 2 段の検査のあとの判定と理由。siblings：同じ表のほかの列名（金額の手がかりを探す）。"""
    label, why = check_assert(guarded, top3, values, header, unit, t_low, siblings)
    if label == "unknown" and use_recheck:
        new, why2 = recheck_unknown(top3, values, header, unit, header_date_ok)
        if new != "unknown":
            # 1. で下げた種類に再検査で戻すのは、手がかりがその種類を示すときだけ（同じ矛盾で戻さない）
            if why and why.startswith("cue_conflict") and new == guarded:
                return "unknown", why
            return new, why2
    return label, why


def _shape(header) -> str:
    """列名の形：数字を # にした形（「男01」「男02」→「男#」）。"""
    return re.sub(r"[0-9]+", "#", _norm(header)).strip()


def apply_table(rows, t_low=0.0, header_date_ok=None):
    """1 つの表の列をまとめて検査する。rows：{"guarded", "top3", "values", "header", "unit"} の並び → [(判定, 理由)]。
    1 列ずつ 2 段の検査をしたあと、まだ不明の列は同じ表の「列名の形が同じ」列を見る：形が同じ列が 2 つ以上あり、全部が同じ種類と言い切っていて、
    その種類がこの列の上位 3 つに入り、値が数として読めるなら、その種類にする（列名が数字や日付だけの列は除く。LABEL_GUIDE v1.4・v1.7）。"""
    out = [decide(r["guarded"], r["top3"], r["values"], r["header"], r.get("unit", ""), t_low, True, header_date_ok,
                  r.get("siblings", [x["header"] for x in rows if x is not r])) for r in rows]
    shapes = [_shape(r["header"]) for r in rows]
    for i, (lab, why) in enumerate(out):
        if lab != "unknown" or not re.search(r"[^\W\d_]", shapes[i]) or period_header(rows[i]["header"]):
            continue
        same = [out[j][0] for j in range(len(rows)) if j != i and shapes[j] == shapes[i]]
        if len(same) < 2 or "unknown" in same or len(set(same)) != 1:
            continue
        cand = [t["label"] for t in (rows[i]["top3"] or [])][:3]
        lab2 = same[0]
        if lab2 in cand and (lab2 not in ("amount", "quantity", "rate") or _numeric_share(rows[i]["values"]) >= 0.6):
            out[i] = (lab2, "recheck:siblings")
    return out
