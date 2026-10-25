"""検査役（verifier.py）の学習と効き目の測り方（2026-10-25 Claude）。学習は CPU の木のモデル（勾配ブースティング）だけ（Kaggle の GPU は使わない）。--model lr でロジスティック回帰と比べられる。

場：教材庫 b001〜b013（本体＝学習前の版 31・E5-base 種子 1 の予測 pred_e5base_seed1.json。本体はどの陣の列も見ていない）。
正解は pool_bench.load_batch と同じ（裁定・一致の列。捨てた列は除く）。
1. 陣を 1 つずつ外して検査役を学び、外した陣の確率を出す（leave-one-batch-out。検査役も外した陣を見ていない）
2. tau も陣を 1 つずつ外して決める：ほかの陣で「下げた列のうち本体が本当に間違っていた割合」が 50% 以上になる最大の tau
3. 比べる：見張りだけ／＋recheck v1（t＝0.95）／＋recheck v1＋検査役
最後に全部の陣で学び直し、係数を models/verifier_v1.json に書く（tau は全部の陣で同じ規則で決める）。
使い方：python verifier_eval.py [--out bench/verifier_v1.md] [--export models/verifier_v1.json]
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


def load_batch(b):
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


def fmt(s):
    return f"正 {s['acc_all']:.1%}・誤 {s['wrong']}・不明 {s['unknown']}・**重大 {s['critical']}**（採点 {s['n']}）"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="bench/verifier_v1.md")
    ap.add_argument("--export", default="models/verifier_v1.json")
    ap.add_argument("--model", default="hgb", choices=("hgb", "lr"))
    a = ap.parse_args(argv)
    global MODEL
    MODEL = a.model
    cols = [c for b in BATCHES for c in load_batch(b)]
    base = base_decisions(cols)
    guard_only = [(c["pred"], None) for c in cols]
    labels = list(V.LABELS)
    X = V.matrix([c["values"] for c in cols])
    trainable = np.array([bool(c["truth"]) and c["truth"] in labels for c in cols])
    y = np.array([c["truth"] if t else "" for c, t in zip(cols, trainable)])
    batch = np.array([c["batch"] for c in cols])
    P = np.zeros((len(cols), len(labels)), dtype="float32")
    for b in BATCHES:
        tr = trainable & (batch != b)
        lr, mean, scale = fit(X[tr], y[tr])
        te = batch == b
        p = lr.predict_proba((X[te] - mean) / scale)
        full = np.zeros((te.sum(), len(labels)), dtype="float32")
        for j, c in enumerate(lr.classes_):
            full[:, labels.index(c)] = p[:, j]
        P[te] = full
        print("fold", b, "done", flush=True)
    # 検査役だけの正解率（値だけでどこまで当たるか）
    acc_v = float(np.mean([labels[int(np.argmax(P[k]))] == y[k] for k in np.where(trainable)[0]]))
    # tau を陣ごとに外して決め、外した陣に当てる
    final, taus = [None] * len(cols), {}
    for b in BATCHES:
        others = [k for k in range(len(cols)) if batch[k] != b]
        t = pick_tau(P, labels, base, cols, others)
        taus[b] = t
        for k in np.where(batch == b)[0]:
            final[k] = V.veto(base[k][0], P[k], labels, t)
            if final[k][1] is None:
                final[k] = base[k]
    sg, sb, sf = score([d[0] for d in guard_only], cols), score([d[0] for d in base], cols), score([d[0] for d in final], cols)
    vc = vetoed(final, base, cols)
    # 種類の組ごとに残った重大
    def crit_pairs(pred):
        c = Counter()
        for p, col in zip(pred, cols):
            t = col["truth"]
            if t in V.NUMERIC and p in V.NUMERIC and p != t:
                c[f"{t}→{p}"] += 1
        return c
    cb, cf = crit_pairs([d[0] for d in base]), crit_pairs([d[0] for d in final])
    # tau の曲線（全部の陣を合わせて。tau を選んだあとの参考）
    curve = []
    for t in TAUS:
        fin = [V.veto(base[k][0], P[k], labels, t) for k in range(len(cols))]
        fin = [f if f[1] else base[k] for k, f in enumerate(fin)]
        s = score([d[0] for d in fin], cols)
        pr, n = precision(vetoed(fin, base, cols))
        curve.append((t, s, n, pr))
    per_batch = []
    for b in BATCHES:
        ks = [k for k in range(len(cols)) if batch[k] == b]
        s1 = score([base[k][0] for k in ks], [cols[k] for k in ks])
        s2 = score([final[k][0] for k in ks], [cols[k] for k in ks])
        per_batch.append((b, taus[b], s1, s2))
    # 全部の陣で学び直して書き出す
    lr, mean, scale = fit(X[trainable], y[trainable])
    tau_all = pick_tau(P, labels, base, cols, list(range(len(cols))))
    meta = {"version": "v1", "labels": labels, "dense_dim": V.DENSE_DIM, "g_dim": V.G_DIM, "tau": tau_all,
            "trained_on": list(BATCHES), "n_train": int(trainable.sum())}
    if MODEL == "hgb":
        meta.update(V.export_hgb(lr, labels))
    else:
        coef = np.zeros((len(labels), X.shape[1]), dtype="float32")
        icp = np.full(len(labels), -30.0, dtype="float32")
        for j, c in enumerate(lr.classes_):
            coef[labels.index(c)] = lr.coef_[j]
            icp[labels.index(c)] = lr.intercept_[j]
        meta.update({"kind": "lr", "coef": [[round(float(x), 5) for x in row] for row in coef], "intercept": [round(float(x), 5) for x in icp],
                     "mean": [round(float(x), 6) for x in mean], "scale": [round(float(x), 6) for x in scale]})
    # 書き出した JSON で同じ確率が出るかを確かめる（numpy だけの推論 ＝ ブラウザ版の手本）
    chk = V.Verifier(json.loads(json.dumps(meta)))
    sub = np.where(trainable)[0][:300]
    p_sk = lr.predict_proba((X[sub] - mean) / scale)
    p_js = chk.proba([cols[k]["values"] for k in sub])[:, [labels.index(c) for c in lr.classes_]]
    meta_diff = float(np.abs(p_sk - p_js).max())
    if meta_diff > 1e-3:
        raise SystemExit(f"書き出した検査役の確率が合わない（最大の差 {meta_diff}）")
    with open(a.export, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, separators=(",", ":"))
    L = ["# 検査役 v1（値だけを見る別の観点の AI、2026-10-25 Claude。`verifier.py`・`verifier_eval.py`）", "",
         "オーナー指示：「本体とは別観点から調べるタイプのAIにできるならそれで実行してくれ」「不明なものは再検査するルールは有効なままにしておいてくれ」。",
         "", "## 仕組み",
         "- 本体（E5-base）は列名・値・同じ表の列名を文章として読む。**検査役は列名を読まず、値の並びだけ**（数の大きさ・桁・小数・符号・日付や時刻として読めるか・文字の形）から種類の確率を出す小さな木のモデル（勾配ブースティング 200 回。CPU で学習。GPU は使っていない）",
         "- 順番：見張り → **recheck v1（言い切りの検査と不明の再検査。そのまま有効）** → 検査役。検査役は種類を付けず、言い切りを「不明」に下げるだけ",
         "- 下げる条件：本体の答えが数字の種類（date・amount・quantity・rate・id）で、検査役のその種類の確率が tau 未満、かつ検査役の 1 位が別の数字の種類",
         f"- tau の決め方（事前に固定）：ほかの陣で「下げた列のうち本体が本当に間違っていた割合」が {MIN_PRECISION:.0%} 以上になる最大の tau（候補 {', '.join(map(str, TAUS))}）",
         "", "## 場",
         f"- 教材庫 b001〜b013（{len(cols):,} 列）。本体は学習前の版 31（E5-base 種子 1）で、どの陣の列も見ていない。検査役と tau は**陣を 1 つずつ外して**学び・決め、外した陣で測った",
         "- recheck v1 の規則は b003〜b012 を見ずに作ったが、教材庫の検証（第 1 段）で作ったので、ここでの recheck の数字はやや甘くない（作るのに使っていない）",
         "", "## 結果（陣を外して測った数字を合わせたもの）",
         "| 判定 | 結果 |", "|---|---|",
         f"| 見張りだけ | {fmt(sg)} |", f"| ＋ recheck v1 | {fmt(sb)} |", f"| ＋ recheck v1 ＋ 検査役 | {fmt(sf)} |", "",
         f"- 検査役が下げた列 {sum(vc.values())}：本体が正しかった {vc['was_correct']}・重大な誤り {vc['was_critical']}・ほかの誤り {vc['was_wrong']}・正解が決められない列 {vc['truth_unknown']}",
         f"- 検査役だけの正解率（値だけで種類を当てる、参考）：{acc_v:.1%}",
         f"- 陣ごとの tau：{', '.join(f'{b} {t}' for b, t in taus.items())}",
         "", "### 残った重大（種類の組、多い順）", "| 組 | recheck v1 まで | ＋検査役 |", "|---|---:|---:|"]
    for k, v in cb.most_common(15):
        L.append(f"| {k} | {v} | {cf.get(k, 0)} |")
    L += ["", "### 陣ごと", "| 陣 | tau | recheck v1 まで | ＋検査役 |", "|---|---:|---|---|"]
    for b, t, s1, s2 in per_batch:
        L.append(f"| {b} | {t} | {fmt(s1)} | {fmt(s2)} |")
    L += ["", "### tau の曲線（参考。全部の陣を合わせて、tau を固定したとき）", "| tau | 結果 | 下げた列 | 当たり（本体が誤り） |", "|---:|---|---:|---:|"]
    for t, s, n, pr in curve:
        L.append(f"| {t} | {fmt(s)} | {n} | {pr:.0%} |")
    L += ["", "## 書き出し",
          f"- 全部の陣（{int(trainable.sum()):,} 列）で学び直したモデル：`{a.export}`（{MODEL}、tau＝{tau_all}。書き出した JSON の確率と sklearn の確率の最大の差 {meta_diff:.1e}）。`verifier.Verifier.load()` と `verifier.apply_after_recheck()` で使う",
          "- **注意**：ここでの数字は教材庫（正解は ChatGPT と Claude の裁定）での数字。本当に重大が減るかは、封印セット #3 で事前登録して測る",
          "", "## 再現", "`python3 verifier_eval.py`（scikit-learn が要る）。試験 `python3 -m unittest tests.test_verifier`"]
    open(a.out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(fmt(sg)); print(fmt(sb)); print(fmt(sf)); print(vc, taus, tau_all, acc_v)


if __name__ == "__main__":
    main()
