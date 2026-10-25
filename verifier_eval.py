"""検査役（verifier.py）の学習と効き目の測り方（2026-10-25 Claude）。学習は CPU の木のモデル（勾配ブースティング）だけ（Kaggle の GPU は使わない）。--model lr でロジスティック回帰と比べられる。

場：教材庫 b001〜b013（本体＝学習前の版 31・E5-base 種子 1 の予測 pred_e5base_seed1.json。本体はどの陣の列も見ていない）。
正解は pool_bench.load_batch と同じ（裁定・一致の列。捨てた列は除く）。
1. 陣を 1 つずつ外して検査役を学び、外した陣の確率を出す（leave-one-batch-out。検査役も外した陣を見ていない）
2. tau も陣を 1 つずつ外して決める：ほかの陣で「下げた列のうち本体が本当に間違っていた割合」が 50% 以上になる最大の tau
3. 比べる：見張りだけ／＋recheck v1（t＝0.95）／＋recheck v1＋検査役
最後に全部の陣で学び直し、係数を models/verifier_v1.json に書く（tau は全部の陣で同じ規則で決める）。
使い方：python verifier_eval.py [--out bench/verifier_v2.md] [--export models/verifier_v2.json]（v2：表の特徴と重大検知役を足した）
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

import numpy as np

import guard
import pool_bench as B
import recheck
import verifier as V
from llm_baseline import score_real

BATCHES = tuple(f"b{n:03d}" for n in range(1, 14))
TAUS = (0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5)
MIN_PRECISION = 0.5
RHOS = (0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.98, 0.99)
THS = (None, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)   # 重大検知役の線（None＝使わない）
MIN_CAND_ACC = 0.95   # 候補の正しい割合（正解が決められる列で）。これ以上になる最も小さい rho（事前に固定、2026-10-25）


def load_batch(b):
    """pool_bench.load_batch に、表の行の順にそろった値（row_values）・行の番号・表の行数を足す（v2 の table_features 用）。"""
    cols = _load_batch(b)
    corpus = B.read_jsonl(B.WORK / b / "corpus.jsonl")
    for c in cols:
        x = corpus[c["i"]]
        c["tab"] = {"rows": x.get("row_values") or x["values"], "row_index": x.get("row_index"), "total": x.get("datastore_total")}
    return cols


def table_matrix(cols):
    """列ごとの table_features（表ごとに計算し、cols の順に並べる）。"""
    T = np.zeros((len(cols), V.TABLE_DIM), dtype="float32")
    by = defaultdict(list)
    for k, c in enumerate(cols):
        by[(c["batch"], c["table"])].append(k)
    for ks in by.values():
        for k, f in zip(ks, V.table_features([cols[k]["tab"] for k in ks])):
            T[k] = f
    return T


def _load_batch(b):
    """pool_bench.load_batch。b003 は予測の行が 20 多い（取り出しのやり直し）ので id で合わせる。"""
    try:
        return B.load_batch(b)
    except ValueError:
        w = B.WORK / b
        pred = json.load(open(w / "pred_e5base_seed1.json", encoding="utf-8"))
        sets = json.load(open(w / "set.json", encoding="utf-8"))["columns"]
        by = {r["id"]: r for r in pred["rows"]}
        rows = [by[s["id"]] for s in sets]
        orig = B.json.load
        try:
            B.json.load = lambda f, **k: (dict(pred, rows=rows) if "pred_e5base" in getattr(f, "name", "") else orig(f, **k))
            return B.load_batch(b)
        finally:
            B.json.load = orig


def base_decisions(cols):
    """見張り（予測ファイルの guarded_prediction）→ recheck v1（表ごと、t＝0.95、見張り v11 の列名の日付の規則）。"""
    by = defaultdict(list)
    for k, c in enumerate(cols):
        by[(c["batch"], c["table"])].append(k)
    out = [None] * len(cols)
    for ks in by.values():
        rows = [{"guarded": cols[k]["pred"], "top3": cols[k]["top3"], "values": cols[k]["values5"], "header": cols[k]["header"],
                 "unit": cols[k]["unit"], "siblings": cols[k]["context"]} for k in ks]
        for k, d in zip(ks, recheck.apply_table(rows, 0.95, guard.header_date_ok)):
            out[k] = d
    return out


MODEL = "hgb"


def fit(X, y):
    """種類の確率を出すモデルを学ぶ → (モデル, 平均, 幅)。木のモデルは標準化しない（平均 0・幅 1 を返す）。"""
    if MODEL == "hgb":
        from sklearn.ensemble import HistGradientBoostingClassifier
        m = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.1, max_leaf_nodes=31, l2_regularization=1.0, random_state=0)
        m.fit(X, y)
        return m, np.zeros(X.shape[1], dtype="float32"), np.ones(X.shape[1], dtype="float32")
    from sklearn.linear_model import LogisticRegression
    mean = X.mean(axis=0)
    scale = X.std(axis=0) + 1e-3
    lr = LogisticRegression(C=0.5, max_iter=2000)
    lr.fit((X - mean) / scale, y)
    return lr, mean, scale


def score(pred, cols):
    keep = [(p, c["truth"]) for p, c in zip(pred, cols) if c["truth"] and c["truth"] not in B.NOT_USED and c["truth"] != "person"]
    return score_real([p for p, _ in keep], [t for _, t in keep])


def vetoed(final, base, cols):
    """検査役が下げた列の内訳：本体の答えが 正しい／重大な誤り／ほかの誤り／正解が決められない列。"""
    c = Counter()
    for f, b, col in zip(final, base, cols):
        if f[0] == b[0]:
            continue
        t = col["truth"]
        if not t or t in B.NOT_USED or t == "person":
            c["truth_unknown"] += 1
        elif b[0] == t:
            c["was_correct"] += 1
        elif t in V.NUMERIC:
            c["was_critical"] += 1
        else:
            c["was_wrong"] += 1
    return c


def precision(c):
    n = c["was_correct"] + c["was_critical"] + c["was_wrong"] + c["truth_unknown"]
    return (n - c["was_correct"]) / n if n else 1.0, n


def pick_tau(P, labels, base, cols, idx):
    best = TAUS[0]
    for t in TAUS:
        fin = [V.veto(base[k][0], P[k], labels, t) for k in idx]
        pr, n = precision(vetoed(fin, [base[k] for k in idx], [cols[k] for k in idx]))
        if pr >= MIN_PRECISION:
            best = t
    return best


def candidates(final, P, labels, cols, idx, rho):
    return {k: V.candidate(final[k][0], final[k][1], cols[k]["pred"], cols[k]["top3"], cols[k]["header"], P[k], labels, rho) for k in idx}


def cand_stats(cand, cols):
    """候補の数・正解が決められる列での正しい割合・重大（数字の種類どうしの取り違え）。"""
    n = ok = crit = scored = 0
    for k, c in cand.items():
        if c is None:
            continue
        n += 1
        t = cols[k]["truth"]
        if not t or t in B.NOT_USED or t == "person":
            continue
        scored += 1
        ok += c == t
        crit += t in V.NUMERIC and c != t
    return {"n": n, "scored": scored, "acc": ok / scored if scored else 1.0, "critical": crit}


def pick_rho(final, P, labels, cols, idx):
    for r in RHOS:
        if cand_stats(candidates(final, P, labels, cols, idx, r), cols)["acc"] >= MIN_CAND_ACC:
            return r
    return None


def fmt(s):
    return f"正 {s['acc_all']:.1%}・誤 {s['wrong']}・不明 {s['unknown']}・**重大 {s['critical']}**（採点 {s['n']}）"


def fit_risk(X, y):
    from sklearn.ensemble import HistGradientBoostingClassifier
    m = HistGradientBoostingClassifier(max_iter=300, learning_rate=0.05, max_leaf_nodes=15, l2_regularization=1.0,
                                       class_weight="balanced", random_state=0)
    return m.fit(X, y)


_VETO = {}


def _veto_all(base, P, labels, tau):
    key = (id(base), id(P), tau)
    if key not in _VETO:
        _VETO[key] = [V.veto(base[k][0], P[k], labels, tau) for k in range(len(base))]
    return _VETO[key]


def combine(base, P, R, labels, tau, th, idx):
    """検査役（tau）と重大検知役（th）を重ねた判定。どちらかが下げれば不明。"""
    out = {}
    va = _veto_all(base, P, labels, tau)
    for k in idx:
        f = va[k]
        if f[1]:
            out[k] = f
        elif th is not None and base[k][0] in V.NUMERIC and R[k] >= th:
            out[k] = ("unknown", "risk")
        else:
            out[k] = base[k]
    return out


def pick_combo(base, P, R, labels, cols, idx):
    """ほかの陣で「下げた列のうち本体が本当に間違っていた割合」が MIN_PRECISION 以上の組のうち、重大が最も少ない組（同じなら不明が少ない組）。"""
    best = None
    for t in TAUS:
        for h in THS:
            o = combine(base, P, R, labels, t, h, idx)
            fin = [o[k] for k in idx]
            pr, _ = precision(vetoed(fin, [base[k] for k in idx], [cols[k] for k in idx]))
            if pr < MIN_PRECISION:
                continue
            sc = score([d[0] for d in fin], [cols[k] for k in idx])
            key = (sc["critical"], sc["unknown"])
            if best is None or key < best[0]:
                best = (key, (t, h))
    return best[1] if best else (TAUS[0], None)


def risk_matrix(X, P, base, cols, labels):
    R = np.asarray([V.risk_features(P[k], d[0], d[1], cols[k]["top3"], labels) for k, d in enumerate(base)], dtype="float32")
    return np.hstack([X, R])


def crit_pairs(pred, cols):
    c = Counter()
    for p, col in zip(pred, cols):
        t = col["truth"]
        if t in V.NUMERIC and p in V.NUMERIC and p != t:
            c[f"{t}→{p}"] += 1
    return c


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="bench/verifier_v2.md")
    ap.add_argument("--export", default="models/verifier_v2.json")
    a = ap.parse_args(argv)
    cols = [c for b in BATCHES for c in load_batch(b)]
    base = base_decisions(cols)
    guard_only = [(c["pred"], None) for c in cols]
    labels = list(V.LABELS)
    X = np.hstack([V.matrix([c["values"] for c in cols]), table_matrix(cols)])
    trainable = np.array([bool(c["truth"]) and c["truth"] in labels for c in cols])
    y = np.array([c["truth"] if t else "" for c, t in zip(cols, trainable)])
    batch = np.array([c["batch"] for c in cols])
    ALL = list(range(len(cols)))
    # 1. 検査役 v2 を陣ごとに外して学ぶ
    P = np.zeros((len(cols), len(labels)), dtype="float32")
    for b in BATCHES:
        m, _, _ = fit(X[trainable & (batch != b)], y[trainable & (batch != b)])
        te = batch == b
        p = m.predict_proba(X[te])
        for j, c in enumerate(m.classes_):
            P[te, labels.index(c)] = p[:, j]
        print("fold", b, flush=True)
    acc_v = float(np.mean([labels[int(np.argmax(P[k]))] == y[k] for k in np.where(trainable)[0]]))
    # 2. 重大検知役を陣ごとに外して学ぶ（数字の種類と言い切った、正解が決められる列だけ）
    XR = risk_matrix(X, P, base, cols, labels)
    asserted = np.array([d[0] in V.NUMERIC for d in base])
    scored = np.array([bool(c["truth"]) and c["truth"] not in B.NOT_USED and c["truth"] != "person" for c in cols])
    yr = np.array([int(c["truth"] in V.NUMERIC and d[0] != c["truth"]) for c, d in zip(cols, base)])
    R = np.zeros(len(cols), dtype="float32")
    for b in BATCHES:
        m = fit_risk(XR[asserted & scored & (batch != b)], yr[asserted & scored & (batch != b)])
        te = asserted & (batch == b)
        R[te] = m.predict_proba(XR[te])[:, 1]
        print("risk fold", b, flush=True)
    # 3. tau・th・rho を陣ごとに外して決め、外した陣に当てる
    final, picks, rhos, cand = {}, {}, {}, {}
    for b in BATCHES:
        oth = [k for k in ALL if batch[k] != b]
        te = [k for k in ALL if batch[k] == b]
        t, h = pick_combo(base, P, R, labels, cols, oth)
        picks[b] = (t, h)
        final.update(combine(base, P, R, labels, t, h, te))
        fo = combine(base, P, R, labels, t, h, oth)
        fl = [fo.get(k, base[k]) for k in ALL]
        r = pick_rho(fl, P, labels, cols, oth)
        rhos[b] = r
        if r is not None:
            fl2 = [final.get(k, base[k]) for k in ALL]
            cand.update(candidates(fl2, P, labels, cols, te, r))
    fin = [final[k] for k in ALL]
    only_v = [V.veto(base[k][0], P[k], labels, picks[cols[k]["batch"]][0]) for k in ALL]
    only_v = [f if f[1] else base[k] for k, f in enumerate(only_v)]
    sg, sb, sv, sf = (score([d[0] for d in x], cols) for x in (guard_only, base, only_v, fin))
    vc = vetoed(fin, base, cols)
    cand = {k: c for k, c in cand.items() if fin[k][1] != "risk"}
    cs = cand_stats(cand, cols)
    sc = score([cand.get(k) or fin[k][0] for k in ALL], cols)
    cb, cv, cf = crit_pairs([d[0] for d in base], cols), crit_pairs([d[0] for d in only_v], cols), crit_pairs([d[0] for d in fin], cols)
    per_batch = [(b, picks[b], score([base[k][0] for k in ALL if batch[k] == b], [cols[k] for k in ALL if batch[k] == b]),
                  score([fin[k][0] for k in ALL if batch[k] == b], [cols[k] for k in ALL if batch[k] == b])) for b in BATCHES]
    # 4. 全部の陣で学び直して書き出す
    mv, mean, scale = fit(X[trainable], y[trainable])
    mr = fit_risk(XR[asserted & scored], yr[asserted & scored])
    tau_all, th_all = pick_combo(base, P, R, labels, cols, ALL)
    fa = combine(base, P, R, labels, tau_all, th_all, ALL)
    rho_all = pick_rho([fa[k] for k in ALL], P, labels, cols, ALL)
    meta = {"version": "v2", "table": True, "labels": labels, "dense_dim": V.DENSE_DIM, "g_dim": V.G_DIM, "table_dim": V.TABLE_DIM,
            "tau": tau_all, "rho": rho_all, "trained_on": list(BATCHES), "n_train": int(trainable.sum())}
    meta.update(V.export_hgb(mv, labels))
    if th_all is not None:
        meta["risk"] = {**V.export_hgb_binary(mr), "th": th_all, "risk_dim": V.RISK_DIM, "n_train": int((asserted & scored).sum())}
    # 書き出した JSON で同じ確率が出るかを表ごとに確かめる（numpy だけの推論 ＝ ブラウザ版の手本）
    chk = V.Verifier(json.loads(json.dumps(meta)))
    by_t = defaultdict(list)
    for k, c in enumerate(cols):
        by_t[(c["batch"], c["table"])].append(k)
    diffs, n_chk = [0.0], 0
    for ks in by_t.values():
        Xc = chk.inputs([cols[k]["values"] for k in ks], [cols[k]["tab"] for k in ks])
        pj = chk.proba(None, None, Xc)
        ps = np.zeros_like(pj)
        pp = mv.predict_proba(X[ks])
        for j, c in enumerate(mv.classes_):
            ps[:, labels.index(c)] = pp[:, j]
        diffs.append(float(np.abs(ps - pj).max()))
        if chk.risk:
            rows = [{"top3": cols[k]["top3"]} for k in ks]
            rj = chk.risk_proba(Xc, pj, [base[k] for k in ks], rows)
            XRk = np.hstack([X[ks], np.asarray([V.risk_features(ps[i], base[k][0], base[k][1], cols[k]["top3"], labels) for i, k in enumerate(ks)])])
            rs = np.where([base[k][0] in V.NUMERIC for k in ks], mr.predict_proba(XRk)[:, 1], 0.0)
            diffs.append(float(np.abs(rs - rj).max()))
        n_chk += len(ks)
        if n_chk >= 300:
            break
    meta_diff = max(diffs)
    if meta_diff > 1e-3:
        raise SystemExit(f"書き出した検査役の確率が合わない（最大の差 {meta_diff}）")
    with open(a.export, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, separators=(",", ":"))
    L = ["# 検査役 v2（値・表の中の関係を見る別の観点の AI ＋ 重大検知役、2026-10-25 Claude。`verifier.py`・`verifier_eval.py`）", "",
         "オーナー指示：「本体とは別観点から調べるタイプのAIにできるならそれで実行してくれ」「不明なものは再検査するルールは有効なままにしておいてくれ」"
         "「どんな方法でも良いが検査係の強化を続けてくれ」「途中でチャットGPTの案も聞いていいぞ」。v1 は `bench/verifier_v1.md`。", "",
         "## 仕組み",
         "- 順番：見張り → **recheck v1（言い切りの検査と不明の再検査。そのまま有効）** → 検査役 v2 と重大検知役（どちらかが下げれば不明）→ 不明の列に候補を添える",
         "- **検査役 v2**：列名を読まない。値の並び（v1）に、同じ表のほかの列・行の並び（表の中の位置・すぐ隣の 2〜8 列の和と等しいか＝合計の列・行の番号との相関・表の行数との比・ほかの数の列との相関）を足した木のモデル",
         "- **重大検知役**（ChatGPT の案 4）：数字の種類と言い切った列だけを見て「重大な誤りか」を当てる二値の木のモデル。入力は値・表の特徴、検査役の確率、本体の上位 3 つ、recheck の理由。"
         "**本体の確率を使うので、本体の版を変えたらその版の予測で作り直す**",
         f"- 決め方：tau（{', '.join(map(str, TAUS))}）と th（{', '.join(map(str, THS))}）の組を、ほかの陣で「下げた列のうち本体が本当に間違っていた割合」が {MIN_PRECISION:.0%} 以上の組のうち重大が最も少ない組にした（陣を 1 つずつ外して決め、外した陣で測った）。"
         "割合 50% の線は v1 で事前に決めたもの。重大が最も少ない組を選ぶのは v2 で足した",
         "- 検査役と重大検知役も陣を 1 つずつ外して学んだ。重大検知役の入力の検査役の確率は、陣を外して出した確率（学習側の陣の確率は外した陣も見たモデルのもの。わずかな漏れ）",
         "", "## 結果（教材庫 b001〜b013、本体は学習前の版 31。陣を外して測った数字を合わせたもの）",
         "| 判定 | 結果 |", "|---|---|",
         f"| 見張りだけ | {fmt(sg)} |", f"| ＋ recheck v1 | {fmt(sb)} |", f"| ＋ recheck v1 ＋ 検査役 v2 | {fmt(sv)} |",
         f"| ＋ recheck v1 ＋ 検査役 v2 ＋ 重大検知役 | {fmt(sf)} |", "",
         f"- 下げた列 {sum(vc.values())}：本体が正しかった {vc['was_correct']}・重大な誤り {vc['was_critical']}・ほかの誤り {vc['was_wrong']}・正解が決められない列 {vc['truth_unknown']}",
         f"- 検査役 v2 だけの正解率（値と表の中の関係だけで種類を当てる、参考）：{acc_v:.1%}（v1 は 84.5%）",
         f"- 陣ごとの (tau, th)：{', '.join(f'{b} {t}' for b, t in picks.items())}",
         "", "### 残った重大（種類の組）", "| 組 | recheck v1 まで | ＋検査役 v2 | ＋重大検知役 |", "|---|---:|---:|---:|"]
    for k, v in cb.most_common(15):
        L.append(f"| {k} | {v} | {cv.get(k, 0)} | {cf.get(k, 0)} |")
    L += ["", "## 候補つきの要確認（不明のまま、候補の答えを添える）",
          f"- rho の決め方（v1 と同じ、事前に固定）：ほかの陣で候補の正しい割合が {MIN_CAND_ACC:.0%} 以上になる最も小さい rho。陣ごとの rho：{', '.join(f'{b} {r}' for b, r in rhos.items())}",
          f"- 候補を付けた不明の列 **{cs['n']}**（不明 {sf['unknown']} のうち）。正解が決められる {cs['scored']} 列で**候補の正しい割合 {cs['acc']:.1%}**・候補の重大 {cs['critical']}",
          f"- 言い切りの数字は変わらない。参考：候補も答えに数えると {fmt(sc)}",
          "", "### 陣ごと", "| 陣 | (tau, th) | recheck v1 まで | ＋検査役 v2 ＋重大検知役 |", "|---|---|---|---|"]
    for b, t, s1, s2 in per_batch:
        L.append(f"| {b} | {t} | {fmt(s1)} | {fmt(s2)} |")
    L += ["", "## 比べたが入れなかったもの",
          "- 3 段目（1 回目の検査役の答えを同じ表のほかの列に配って 2 回目の判定）：正解率 87.6% だが、不明が同じくらいのところで重大が v2 より減らない（不明 2,940 で重大 27、v2 は 2,936 で 25）",
          "- 教材の量：v1 の正解率は 1/4・1/2・全部で 80.8%・82.8%・84.1%（教材が増えればまだ伸びる）",
          "", "## 書き出し",
          f"- 全部の陣で学び直したモデル：`{a.export}`（tau＝{tau_all}、th＝{th_all}、rho＝{rho_all}。書き出した JSON と sklearn の確率の最大の差 {meta_diff:.1e}）。"
          "`verifier.Verifier.load()` と `verifier.apply_after_recheck(..., rows=, table=)` で使う",
          "- **注意**：ここでの数字は教材庫（正解は ChatGPT と Claude の裁定）での数字。本当に重大が減るかは、変更を凍結して封印セット #3 で事前登録して測る。製品に入れる本体（C1 など）に合わせて重大検知役を作り直す",
          "", "## 再現", "`python3 verifier_eval.py`（scikit-learn が要る。CPU で約 30 分）。試験 `python3 -m unittest tests.test_verifier`"]
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(fmt(sg)); print(fmt(sb)); print(fmt(sv)); print(fmt(sf)); print(vc, picks, (tau_all, th_all, rho_all), acc_v); print("cand", cs); print(cf.most_common())


if __name__ == "__main__":
    main()
