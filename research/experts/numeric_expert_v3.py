"""数字の専門家 v3（2026-10-26 Claude）。v2（bench/numeric_expert_v2.md）に辞書・値の強い手がかりを足す。

v2 の結果：難しい列（製品の形で不明になる列）では、木のモデルだけでは正しさが最大 87%（線 95% に届かない）。
ただし列名・単位の手がかりがある列では重大 0 だった → 手がかりを強くする。
強い手がかり（strong_cue）：値・列名・単位から機械で確かめられるもの
- id：6 桁の数字で全国地方公共団体コードの検査数字が 95% 以上合う（教材庫で採点できる列は id 100%。materials/dict/README.md）／13 桁で法人番号の検査数字が合う／14 桁で CNPJ の検査数字が合う
- amount：値の半分以上に通貨記号（¥・円・$・R$・€・£）、または列名・単位に 円・千円・百万円・$・R$・€・USD・BRL・JPY
- rate：値の半分以上に %、または列名・単位に %・％・率・割合・ratio・percent・taxa・percentual
戻し方の型：d＝強い手がかりと専門家の 1 位が同じで、それが本体の上位 3 つに入る／e＝強い手がかりが本体の上位 3 つに入る（専門家なし。辞書だけで足りるか）
線の決まりは v2 と同じ（b001〜b012 の製品の形で不明になった列だけで、戻した列の正しさ ≥ 95%・重大 ≤ 2%）
使い方：python research/experts/numeric_expert_v3.py [--out bench/numeric_expert_v3.md]
"""
from __future__ import annotations

import argparse
import os
import pickle
import re
import sys
import unicodedata

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "materials", "dict"))
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from fetch_dict import check_digit_jp  # noqa: E402
from research.experts.numeric_expert import NUM, Expert  # noqa: E402
from research.experts import numeric_expert_v2 as V2  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

CACHE = os.path.join(ROOT, "research", "experts", ".cache_v3_train.pkl")   # 陣を外した予測（重いので 1 回だけ計算）。git には入れない
TS = (0.0, 0.5, 0.7, 0.9, 0.95, 0.99)


def nv(v):
    return unicodedata.normalize("NFKC", str(v)).strip()


def houjin_ok(s):
    """法人番号（13 桁）：先頭が検査数字。下の 12 桁に右から 1・2 を交互に掛けた和を 9 で割った余り r、9−r。"""
    body = s[1:]
    t = sum(int(d) * (1 if i % 2 == 0 else 2) for i, d in enumerate(reversed(body)))
    return int(s[0]) == 9 - t % 9


def cnpj_ok(s):
    def dv(nums, ws):
        r = sum(int(n) * w for n, w in zip(nums, ws)) % 11
        return 0 if r < 2 else 11 - r
    w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    return dv(s[:12], w1) == int(s[12]) and dv(s[:13], [6] + w1) == int(s[13]) and len(set(s)) > 1


MONEY_V = re.compile(r"[¥$€£]|円|R\$")
MONEY_H = re.compile(r"円|千円|百万円|\$|R\$|€|\bUSD\b|\bBRL\b|\bJPY\b|\(\s*円\s*\)", re.I)
RATE_H = re.compile(r"%|％|率|割合|ratio|percent|taxa|percentual", re.I)


def strong_cue(c):
    vals = [nv(v) for v in c["values"] if nv(v)]
    if len(vals) < 3:
        return None
    digits = [re.sub(r"[-\s.\/]", "", v) for v in vals]
    for n, ok in ((6, lambda s: check_digit_jp(s[:5]) == int(s[5])), (13, houjin_ok), (14, cnpj_ok)):
        ds = [d for d in digits if len(d) == n and d.isdigit()]
        if len(ds) >= 0.8 * len(vals) and sum(ok(d) for d in ds) >= 0.95 * len(ds):
            return "id"
    hu = f"{c['header']} {c.get('unit', '')}"
    if sum(bool(MONEY_V.search(v)) for v in vals) >= 0.5 * len(vals) or MONEY_H.search(hu):
        return "amount"
    if sum("%" in v for v in vals) >= 0.5 * len(vals) or RATE_H.search(hu):
        return "rate"
    return None


def top3(c):
    return [t["label"] for t in (c["top3"] or [])][:3]


def rescue(kind, c, p):
    cue = strong_cue(c)
    if not cue or cue not in top3(c):
        return None
    if kind == "d" and NUM[int(p.argmax())] != cue:
        return None
    return cue


def curve(prod, cols, PX, kind):
    rows = []
    for T in TS:
        n = ok = crit = 0
        for k, d in enumerate(prod):
            if d[0] != "unknown" or not V2.scored(cols[k]) or (kind == "d" and PX[k].max() < T):
                continue
            lab = rescue(kind, cols[k], PX[k])
            if not lab:
                continue
            n += 1
            ok += lab == cols[k]["truth"]
            crit += cols[k]["truth"] in NUM and lab != cols[k]["truth"]
        rows.append((T, n, ok / n if n else 1.0, crit))
        print(f"  kind {kind} T={T}: 戻す {n} 正しい {ok / n if n else 1:.3f} 重大 {crit}", flush=True)
        if kind == "e":
            break
    good = [r for r in rows if r[1] and r[2] >= 0.95 and r[3] <= 0.02 * r[1]]
    return (min(good, key=lambda r: r[0]) if good else None), rows


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="bench/numeric_expert_v3.md")
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in V2.TRAIN for c in E.load_batch(b)]
    if os.path.exists(CACHE):
        prod_tr, PX_tr = pickle.load(open(CACHE, "rb"))
    else:
        prod_tr = V2.product(train, V2.verifier_oof(train, labels), labels)
        PX_tr = V2.expert_oof(train)
        pickle.dump((prod_tr, PX_tr), open(CACHE, "wb"))
    picks, curves = {}, {}
    for k in ("d", "e"):
        picks[k], curves[k] = curve(prod_tr, train, PX_tr, k)
    print("picks", picks, flush=True)
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    Xtr = np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])
    mv, _, _ = E.fit(Xtr[ok], np.array([c["truth"] for c in train])[ok])
    te = []
    for b in V2.TEST:
        cs, _ = with_pred(E.load_batch(b), f"research/merge/preds/c1_{b}.json")
        te += cs
    Xte = np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)])
    Pte = np.zeros((len(te), len(labels)), dtype="float32")
    p = mv.predict_proba(Xte)
    for j, lab in enumerate(mv.classes_):
        Pte[:, labels.index(lab)] = p[:, j]
    prod = V2.product(te, Pte, labels)
    PX = Expert().fit([c for c in train if c["truth"] in NUM]).proba(te)
    L = ["# 数字の専門家 v3（辞書・値の強い手がかり。b013・b014、2026-10-26 Claude。`research/experts/numeric_expert_v3.py`）", "",
         "- 強い手がかり：検査数字（自治体コード・法人番号・CNPJ）→ id、通貨記号・列名の通貨 → amount、%・列名の率 → rate",
         "- 型 d＝強い手がかりと専門家の 1 位が同じで本体の上位 3 つに入る、型 e＝強い手がかりが本体の上位 3 つに入る（専門家なし）",
         "- 線は b001〜b012 の製品の形で不明になった列だけで選んだ（正しさ ≥ 95%・重大 ≤ 2%）。**開発用の数字**", "",
         "## 線を選んだ曲線（b001〜b012）", "| 型 | T | 戻す | 正しい | 重大 |", "|---|---:|---:|---:|---:|"]
    for k in ("d", "e"):
        L += [f"| {k} | {t} | {n} | {acc:.1%} | {cr} |" for t, n, acc, cr in curves[k]]
    L += ["", f"選んだ線：{picks}", "", "## b013・b014", "| 形 | 結果 | 不明 | 重大 | 戻した |", "|---|---|---:|---:|---:|"]
    s0 = E.score([d[0] for d in prod], te)
    L.append(f"| 今の製品の形 | {E.fmt(s0)} | {s0['unknown'] / s0['n']:.1%} | {s0['critical'] / s0['n']:.2%} | 0 |")
    for k in ("d", "e"):
        T = picks[k][0] if picks[k] else (0.9 if k == "d" else 0.0)
        out, back = [], 0
        for i, d in enumerate(prod):
            lab = rescue(k, te[i], PX[i]) if d[0] == "unknown" and (k == "e" or PX[i].max() >= T) else None
            out.append((lab, "dict_cue") if lab else d)
            back += bool(lab)
        s = E.score([d[0] for d in out], te)
        L.append(f"| ＋ 型 {k}（T={T}{'' if picks[k] else '・線なし、参考'}） | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} | {back} |")
        print(k, E.fmt(s), back, flush=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
