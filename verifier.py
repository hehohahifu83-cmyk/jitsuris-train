"""検査役（verifier v1、2026-10-25 Claude。オーナー指示「本体とは別観点から調べるタイプのAIにできるならそれで実行してくれ」
「不明なものは再検査するルールは有効なままにしておいてくれ」）。

本体（E5-base）は列名・値・同じ表の列名を文章として読む。検査役は**列名を読まない**。値の並びだけ（数の大きさ・桁・小数・
符号・日付や時刻として読めるか・文字の形）から種類の確率を出す、小さな木のモデル（勾配ブースティング。木は JSON に書き出し、numpy だけで動く）。
ロジスティック回帰も比べた（bench/verifier_v1.md）。
列名に引きずられた本体の取り違え（例：「件数」の列を番号と言う、年の列を数量と言う）を、値の側から見つける。

判定の順番（recheck v1 はそのまま有効）：見張り（guard）→ 言い切りの検査と不明の再検査（recheck.apply_table）→ 検査役。
検査役は種類を付けない（言い切りを「不明」に下げるだけ）。下げる条件：
  本体の答え L が数字の種類（date・amount・quantity・rate・id）で、検査役の L の確率が tau 未満、
  かつ検査役の 1 位が L 以外の数字の種類（＝値から見ると別の数字の種類）。
tau は陣を 1 つずつ外して決める（verifier_eval.py、結果 bench/verifier_v1.md）。

候補つきの要確認（オーナー指示「より効果的と思われる方だ」2026-10-25）：不明の列のうち、自信が足りないだけで止めた列
（見張りの不明・low_confidence_no_cue・amount_without_cue・rate_without_cue）は、本体の 1 位と検査役の 1 位が同じ数字の種類で、
検査役の確率が rho 以上なら、その種類を「候補」として添える。判定は不明のまま（言い切りではない。製品では「要確認：たぶん〇〇」と見せる）。
列名が年・月だけの列（recheck.period_header）と、列名・単位が別の種類を示す列（cue_conflict）などには候補を付けない。
"""
from __future__ import annotations

import json
import math
import re
import unicodedata
from pathlib import Path

NUMERIC = ("date", "amount", "quantity", "rate", "id")
LABELS = ("account", "address", "amount", "category", "date", "email", "id", "org", "other", "phone", "product", "quantity",
          "rate", "tax_class", "text")
G_DIM = 1024        # 値の「形」の文字のかたまり（数字→9・英字→a/A。漢字・かなはそのまま）
MAX_VALUES = 20
JUNK = {"", "nan", "none", "null", "na", "n/a", "-", "－", "―", "*", "＊", "…", "."}

_NUM = re.compile(r"^[+\-−▲△]?\s*[¥$€£]?\s*[+\-−]?\d[\d,，]*(\.\d+)?\s*(%|％|円|千円|万円|ドル|人|件|t|kg|m|km)?$", re.I)
_DATE_PATS = [re.compile(p) for p in (
    r"^(1[6-9]|20)\d{2}[-/.年](0?[1-9]|1[0-2])([-/.月](0?[1-9]|[12]\d|3[01])日?)?([ T]\d{1,2}:\d{2}(:\d{2})?(\.\d+)?)?(Z|[+-]\d{2}:?\d{2})?$",
    r"^(0?[1-9]|[12]\d|3[01])[-/.](0?[1-9]|1[0-2])[-/.](1[6-9]|20)?\d{2}$",
    r"^(0?[1-9]|1[0-2])[-/.](0?[1-9]|[12]\d|3[01])[-/.](1[6-9]|20)\d{2}$",
    r"^(R|H|S|令和|平成|昭和)\s*\d{1,2}([年.\-/]\s*\d{1,2}(月|[.\-/]\d{1,2}日?)?)?年?度?$",
    r"^(1[6-9]|20)\d{2}\s*[-/]\s*\d{2,4}$",
    r"^(1[6-9]|20)\d{2}(0[1-9]|1[0-2])((0[1-9]|[12]\d|3[01]))?$",
    r"^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[- ]?\d{2,4}$",
    r"^\d{1,2}[- ](jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*([- ]\d{2,4})?$",
    r"^(fy|q[1-4])\s*\d{2,4}$|^\d{4}\s*q[1-4]$|^q[1-4]$",
)]
_TIME = re.compile(r"^\d{1,2}:\d{2}(:\d{2})?(\.\d+)?\s*(am|pm)?$", re.I)
_PHONE = re.compile(r"^\(?\+?\d{1,4}\)?[\s\-]?\d{1,4}[\s\-]\d{2,4}[\s\-]?\d{0,4}$")
_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)
_CODE = re.compile(r"^(?=.*\d)(?=.*[A-Za-z])[A-Za-z0-9_\-./]+$")


def _fnv(s: str) -> int:
    h = 0x811C9DC5
    for b in s.encode("utf-8"):
        h ^= b
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h


def clean_values(values) -> list[str]:
    out = []
    for v in values or []:
        s = unicodedata.normalize("NFKC", str(v)).strip()
        if s.lower() in JUNK:
            continue
        out.append(s)
        if len(out) >= MAX_VALUES:
            break
    return out


def to_float(s: str):
    t = s.replace(",", "").replace("，", "").replace("−", "-").replace("▲", "-").replace("△", "-")
    t = re.sub(r"^[+]?([¥$€£])", "", t).strip()
    t = re.sub(r"\s*(%|円|千円|万円|ドル|人|件|t|kg|m|km)$", "", t, flags=re.I)
    try:
        return float(t)
    except ValueError:
        return None


def shape(s: str) -> str:
    s = re.sub(r"[0-9]", "9", s)
    s = re.sub(r"[A-Z]", "A", s)
    s = re.sub(r"[a-z]", "a", s)
    s = re.sub(r"9{4,}", "9999", s)
    s = re.sub(r"a{4,}", "aaaa", s)
    s = re.sub(r"A{4,}", "AAAA", s)
    return s[:24]


def _mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def _std(xs):
    if len(xs) < 2:
        return 0.0
    m = _mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / len(xs))


def dense_features(values) -> list[float]:
    """値だけから作る数の特徴（列名は読まない）。"""
    vs = clean_values(values)
    n = len(vs)
    if n == 0:
        return [1.0] + [0.0] * (DENSE_DIM - 1)
    nums = [to_float(v) if _NUM.match(v) else None for v in vs]
    fl = [x for x in nums if x is not None]
    fn = len(fl) / n
    ints = [x for x in fl if float(x).is_integer()]
    absx = [abs(x) for x in fl]
    lg = [math.log10(a + 1.0) for a in absx]
    dec = [len(v.split(".")[-1]) if "." in v and to_float(v) is not None else 0 for v in vs]
    intlen = [len(re.sub(r"\D", "", v.split(".")[0])) for v, x in zip(vs, nums) if x is not None]
    lens = [len(v) for v in vs]
    distinct = len(set(vs)) / n
    years = sum(1 for x in fl if float(x).is_integer() and 1800 <= x <= 2100) / n
    in01 = sum(1 for x in fl if 0 <= x <= 1) / n
    zero_one = sum(1 for v in vs if v in ("0", "1")) / n
    sorted_inc = 1.0 if len(fl) == n and n >= 3 and all(b > a for a, b in zip(fl, fl[1:])) else 0.0
    f = [
        0.0, math.log(n + 1), distinct, fn, len(ints) / n, sum(1 for x in fl if x < 0) / n,
        _mean(lg), _std(lg), max(lg) if lg else 0.0, min(lg) if lg else 0.0,
        _mean(dec), max(dec), sum(1 for d in dec if d == 2) / n, sum(1 for d in dec if d >= 3) / n,
        _mean(intlen), _std(intlen), 1.0 if intlen and len(set(intlen)) == 1 else 0.0,
        sum(1 for v in vs if re.match(r"^0\d", v)) / n,
        sum(1 for v in vs if any(p.match(v.lower()) for p in _DATE_PATS)) / n,
        sum(1 for v in vs if _TIME.match(v)) / n, years, in01, zero_one,
        sum(1 for v in vs if "%" in v or "％" in v) / n,
        sum(1 for v in vs if re.search(r"[¥$€£]|円|ドル|R\$", v)) / n,
        sum(1 for v in vs if re.search(r"[A-Za-z]", v)) / n,
        sum(1 for v in vs if re.search(r"[぀-ヿ一-鿿]", v)) / n,
        sum(1 for v in vs if _CODE.match(v)) / n,
        sum(1 for v in vs if _PHONE.match(v)) / n,
        sum(1 for v in vs if _EMAIL.match(v)) / n,
        sum(1 for v in vs if v.startswith("http")) / n,
        sum(1 for v in vs if " " in v) / n,
        math.log(_mean(lens) + 1), _std(lens) / (_mean(lens) + 1),
        sum(1 for x in ints if x != 0 and x % 1000 == 0) / n, sum(1 for x in ints if x != 0 and x % 10 == 0) / n,
        sum(1 for x in fl if x == 0) / n, sorted_inc,
        sum(1 for v in vs if "," in v and to_float(v) is not None) / n,
        1.0 if fl and max(absx) < 100 else 0.0, 1.0 if fl and max(absx) >= 1e6 else 0.0,
        sum(1 for x in fl if -180 <= x <= 180 and not float(x).is_integer() and len(str(x)) > 7) / n,
    ]
    return f


DENSE_DIM = 42


def features(values) -> tuple[list[float], dict[int, float]]:
    """(数の特徴, 値の形の文字のかたまりの疎な特徴)。"""
    d = dense_features(values)
    sp: dict[int, float] = {}
    vs = clean_values(values)
    for v in vs:
        s = "^" + shape(v) + "$"
        for k in (1, 2, 3):
            for i in range(len(s) - k + 1):
                j = _fnv(f"{k}:{s[i:i + k]}") % G_DIM
                sp[j] = sp.get(j, 0.0) + 1.0
    if vs:
        for j in sp:
            sp[j] = math.log1p(sp[j] / len(vs))
    return d, sp


def matrix(values_list):
    import numpy as np
    X = np.zeros((len(values_list), DENSE_DIM + G_DIM), dtype="float32")
    for r, vals in enumerate(values_list):
        d, sp = features(vals)
        X[r, :DENSE_DIM] = d
        for j, v in sp.items():
            X[r, DENSE_DIM + j] = v
    return X


class Verifier:
    """書き出した JSON（verifier_eval.py の export）を読んで確率を出す。numpy だけで動く（ブラウザ版は同じ計算を JavaScript で書く）。
    kind "hgb"：木の足し合わせ（種類ごとに baseline ＋ 各回の木の葉の値）→ softmax。kind "lr"：標準化 → 線形 → softmax。"""

    def __init__(self, d):
        import numpy as np
        self.kind = d.get("kind", "lr")
        self.labels = list(d["labels"])
        self.tau = float(d["tau"])
        self.rho = float(d["rho"]) if d.get("rho") is not None else None
        if self.kind == "hgb":
            self.baseline = np.asarray(d["baseline"], dtype="float64")
            self.trees = [[{k: np.asarray(v) for k, v in t.items()} for t in it] for it in d["trees"]]
        else:
            self.W = np.asarray(d["coef"], dtype="float32")
            self.b = np.asarray(d["intercept"], dtype="float32")
            self.mean = np.asarray(d["mean"], dtype="float32")
            self.scale = np.asarray(d["scale"], dtype="float32")

    @classmethod
    def load(cls, path="models/verifier_v1.json"):
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    @staticmethod
    def _tree(t, X):
        import numpy as np
        idx = np.zeros(len(X), dtype="int64")
        while True:
            go = ~t["leaf"][idx]
            if not go.any():
                return t["v"][idx]
            r = np.where(go)[0]
            n = idx[r]
            x = X[r, t["f"][n]]
            left = np.where(np.isnan(x), t["m"][n], x <= t["t"][n])
            idx[r] = np.where(left, t["l"][n], t["r"][n])

    def proba(self, values_list):
        import numpy as np
        X = matrix(values_list).astype("float64")
        if self.kind == "hgb":
            z = np.tile(self.baseline, (len(X), 1))
            for it in self.trees:
                for k, t in enumerate(it):
                    z[:, k] += self._tree(t, X)
        else:
            z = ((X - self.mean) / self.scale) @ self.W.T + self.b
        z -= z.max(axis=1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(axis=1, keepdims=True)


def export_hgb(model, labels):
    """sklearn の HistGradientBoostingClassifier → JSON にできる形。種類の並びは labels に合わせる（学習に無い種類は確率ほぼ 0）。"""
    classes = list(model.classes_)
    K = len(labels)
    base = [-30.0] * K
    b0 = model._baseline_prediction.ravel()
    for j, c in enumerate(classes):
        base[labels.index(c)] = float(b0[j]) if len(classes) > 2 else 0.0
    trees = []
    for it in model._predictors:
        row = [{"leaf": [True], "v": [0.0], "f": [0], "t": [0.0], "m": [True], "l": [0], "r": [0]} for _ in range(K)]
        for j, p in enumerate(it):
            nd = p.nodes
            row[labels.index(classes[j])] = {"leaf": [bool(x) for x in nd["is_leaf"]], "v": [round(float(x), 5) for x in nd["value"]],
                                             "f": [int(x) for x in nd["feature_idx"]], "t": [float(x) for x in nd["num_threshold"]],
                                             "m": [bool(x) for x in nd["missing_go_to_left"]], "l": [int(x) for x in nd["left"]],
                                             "r": [int(x) for x in nd["right"]]}
        trees.append(row)
    return {"kind": "hgb", "baseline": base, "trees": trees}


def veto(label: str, p_row, labels, tau: float):
    """本体（と recheck）の答え label を、検査役の確率 p_row で見直す → (判定, 理由)。種類は付けない。"""
    if label not in NUMERIC or label not in labels:
        return label, None
    L = {c: i for i, c in enumerate(labels)}
    top = labels[int(max(range(len(labels)), key=lambda i: p_row[i]))]
    if p_row[L[label]] < tau and top in NUMERIC and top != label:
        return "unknown", f"verifier:{top}"
    return label, None


SOFT_UNKNOWN = {None, "low_confidence_no_cue", "amount_without_cue", "rate_without_cue"}


def candidate(label: str, why, guarded: str, top3, header: str, p_row, labels, rho: float):
    """不明の列に添える候補（無ければ None）。種類は付けない（判定は不明のまま）。"""
    if label != "unknown" or not top3 or not (why in SOFT_UNKNOWN or guarded == "unknown"):
        return None
    import recheck
    if recheck.period_header(header):
        return None
    t = top3[0]["label"]
    if t not in NUMERIC or t not in labels:
        return None
    i = labels.index(t)
    if max(range(len(labels)), key=lambda j: p_row[j]) != i or p_row[i] < rho:
        return None
    return t


def apply_after_recheck(decisions, values_list, verifier: "Verifier", tau: float | None = None, rows=None, rho: float | None = None):
    """recheck.apply_table の結果 [(判定, 理由)] に検査役を重ねる → [(判定, 理由, 候補)]。recheck が付けた種類（再検査で戻した列）も同じに見る。
    rows（recheck に渡した {"guarded", "top3", "header"} の並び）を渡すと、不明の列に候補を添える。"""
    P = verifier.proba(values_list)
    t = verifier.tau if tau is None else tau
    r = getattr(verifier, "rho", None) if rho is None else rho
    out = []
    for k, ((lab, why), p) in enumerate(zip(decisions, P)):
        new, why2 = veto(lab, p, verifier.labels, t)
        lab2, why3 = (new, why2) if why2 else (lab, why)
        cand = None
        if rows is not None and r is not None:
            x = rows[k]
            cand = candidate(lab2, why3, x["guarded"], x["top3"], x["header"], p, verifier.labels, r)
        out.append((lab2, why3, cand))
    return out


# ---------------------------------------------------------------- v2：同じ表のほかの列・行の並びも見る（列名は読まない）

TABLE_DIM = 22


def _nums_aligned(values):
    out = []
    for v in values or []:
        s = unicodedata.normalize("NFKC", str(v)).strip()
        out.append(to_float(s) if s.lower() not in JUNK and _NUM.match(s) else None)
    return out


def _rank(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    for k, i in enumerate(order):
        r[i] = float(k)
    return r


def _corr(a, b):
    if len(a) < 3:
        return 0.0
    ma, mb = _mean(a), _mean(b)
    sa = math.sqrt(sum((x - ma) ** 2 for x in a))
    sb = math.sqrt(sum((x - mb) ** 2 for x in b))
    if sa == 0 or sb == 0:
        return 0.0
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb)


def table_features(table):
    """1 つの表の列 [{"rows": 行の順にそろった値, "row_index": 行の番号, "total": 表の行数}] → 列ごとの特徴の並び。
    見るもの：表の中の位置・ほかの数の列との関係（行ごとの合計・相関・大きさ）・行の番号との相関（番号は行の順に並びやすい）・表の行数との比。"""
    m = len(table)
    nums = [_nums_aligned(c.get("rows")) for c in table]
    numeric = [sum(1 for x in xs if x is not None) >= max(1, 0.6 * len(xs)) if xs else False for xs in nums]
    texty = []
    for c in table:
        vs = clean_values(c.get("rows"))
        texty.append(bool(vs) and sum(1 for v in vs if re.search(r"[^\W\d_]", v)) / len(vs) > 0.6 and len(set(vs)) / len(vs) > 0.9)
    out = []
    for j, c in enumerate(table):
        xs = nums[j]
        ri = [float(r) for r in (c.get("row_index") or range(len(xs)))][:len(xs)]
        total = float(c.get("total") or 0)
        pts = [(r, x) for r, x in zip(ri, xs) if x is not None]
        f = [math.log(m + 1), j / (m - 1) if m > 1 else 0.0, 1.0 if j == 0 else 0.0, 1.0 if j == m - 1 else 0.0,
             sum(numeric[:j] + numeric[j + 1:]) / max(1, m - 1), 1.0 if numeric[j] and not any(numeric[:j]) else 0.0,
             sum(texty[:j] + texty[j + 1:]) / max(1, m - 1)]
        if len(pts) >= 3:
            rr, xx = [p[0] for p in pts], [p[1] for p in pts]
            sp = _corr(_rank(rr), _rank(xx))
            srt = [x for _, x in sorted(pts)]
            inc = sum(1 for a, b in zip(srt, srt[1:]) if b > a) / (len(srt) - 1)
        else:
            sp, inc = 0.0, 0.0
        fx = [x for x in xs if x is not None]
        lt = math.log10(total + 1) if total else 0.0
        in_total = sum(1 for x in fx if total and 1 <= x <= total and float(x).is_integer()) / len(fx) if fx else 0.0
        mx = max(fx) if fx else 0.0
        ratio = math.log10((abs(mx) + 1) / (total + 1)) if total else 0.0
        # 行ごとの関係：ほかの数の列の合計と等しいか・行で一番大きいか・ほかの列との相関
        others = [k for k in range(m) if k != j and numeric[k]]
        eq_sum = row_max = n_rows = 0
        for r in range(len(xs)):
            if xs[r] is None:
                continue
            ov = [nums[k][r] for k in others if r < len(nums[k]) and nums[k][r] is not None]
            if len(ov) < 2:
                continue
            n_rows += 1
            # 合計の列：すぐ左かすぐ右に続く 2〜8 列の数の和と等しい（小計・合計の列は件数・金額であって番号ではない）
            tol = max(0.5, 0.005 * abs(xs[r]))
            hit = False
            for side in (range(j - 1, -1, -1), range(j + 1, m)):
                acc, cnt = 0.0, 0
                for k in side:
                    v = nums[k][r] if r < len(nums[k]) else None
                    if v is None or cnt >= 8:
                        break
                    acc += v
                    cnt += 1
                    if cnt >= 2 and abs(acc - xs[r]) <= tol:
                        hit = True
                        break
                if hit:
                    break
            eq_sum += hit
            row_max += xs[r] >= max(ov)
        cors = []
        for k in others:
            pa = [(math.copysign(math.log10(abs(a) + 1), a), math.copysign(math.log10(abs(b) + 1), b))
                  for a, b in zip(xs, nums[k]) if a is not None and b is not None]
            if len(pa) >= 4:
                cors.append(abs(_corr([p[0] for p in pa], [p[1] for p in pa])))
        own_lg = _mean([math.log10(abs(x) + 1) for x in fx]) if fx else 0.0
        sib_lg = _mean([math.log10(abs(x) + 1) for k in others for x in nums[k] if x is not None]) if others else 0.0
        f += [sp, inc, lt, in_total, ratio, eq_sum / n_rows if n_rows else 0.0, row_max / n_rows if n_rows else 0.0,
              1.0 if n_rows else 0.0, max(cors) if cors else 0.0, _mean(cors), 1.0 if cors else 0.0, own_lg - sib_lg,
              len(set(fx)) / len(fx) if fx else 0.0, 1.0 if fx and len(set(fx)) == len(fx) and in_total > 0.9 else 0.0,
              1.0 if total and fx and len(fx) == len(xs) else 0.0]
        assert len(f) == TABLE_DIM, len(f)
        out.append(f)
    return out
