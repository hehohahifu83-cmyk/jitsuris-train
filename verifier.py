"""検査役（verifier v1、2026-10-25 Claude。オーナー指示「本体とは別観点から調べるタイプのAIにできるならそれで実行してくれ」
「不明なものは再検査するルールは有効なままにしておいてくれ」）。

本体（E5-base）は列名・値・同じ表の列名を文章として読む。検査役は**列名を読まない**。値の並びだけ（数の大きさ・桁・小数・
符号・日付や時刻として読めるか・文字の形）から種類の確率を出す、小さなロジスティック回帰（係数は JSON、数百 KB）。
列名に引きずられた本体の取り違え（例：「件数」の列を番号と言う、年の列を数量と言う）を、値の側から見つける。

判定の順番（recheck v1 はそのまま有効）：見張り（guard）→ 言い切りの検査と不明の再検査（recheck.apply_table）→ 検査役。
検査役は種類を付けない（言い切りを「不明」に下げるだけ）。下げる条件：
  本体の答え L が数字の種類（date・amount・quantity・rate・id）で、検査役の L の確率が tau 未満、
  かつ検査役の 1 位が L 以外の数字の種類（＝値から見ると別の数字の種類）。
tau は陣を 1 つずつ外して決める（verifier_eval.py、結果 bench/verifier_v1.md）。
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
    """係数の JSON（export で作る）を読んで確率を出す。numpy だけで動く（ブラウザ版は同じ計算を JavaScript で書く）。"""

    def __init__(self, coef, intercept, labels, mean, scale, tau):
        import numpy as np
        self.W = np.asarray(coef, dtype="float32")
        self.b = np.asarray(intercept, dtype="float32")
        self.labels = list(labels)
        self.mean = np.asarray(mean, dtype="float32")
        self.scale = np.asarray(scale, dtype="float32")
        self.tau = float(tau)

    @classmethod
    def load(cls, path="models/verifier_v1.json"):
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(d["coef"], d["intercept"], d["labels"], d["mean"], d["scale"], d["tau"])

    def proba(self, values_list):
        import numpy as np
        X = (matrix(values_list) - self.mean) / self.scale
        z = X @ self.W.T + self.b
        z -= z.max(axis=1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(axis=1, keepdims=True)


def veto(label: str, p_row, labels, tau: float):
    """本体（と recheck）の答え label を、検査役の確率 p_row で見直す → (判定, 理由)。種類は付けない。"""
    if label not in NUMERIC or label not in labels:
        return label, None
    L = {c: i for i, c in enumerate(labels)}
    top = labels[int(max(range(len(labels)), key=lambda i: p_row[i]))]
    if p_row[L[label]] < tau and top in NUMERIC and top != label:
        return "unknown", f"verifier:{top}"
    return label, None


def apply_after_recheck(decisions, values_list, verifier: "Verifier", tau: float | None = None):
    """recheck.apply_table の結果 [(判定, 理由)] に検査役を重ねる。recheck が付けた種類（再検査で戻した列）も同じに見る。"""
    P = verifier.proba(values_list)
    t = verifier.tau if tau is None else tau
    out = []
    for (lab, why), p in zip(decisions, P):
        new, why2 = veto(lab, p, verifier.labels, t)
        out.append((new, why2) if why2 else (lab, why))
    return out
