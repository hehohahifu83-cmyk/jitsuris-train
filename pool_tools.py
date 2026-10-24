"""学習し直さずにジツリスの判定を良くする道具と、その効き目の比べ方（2026-10-24 Claude）。

試す場は pool_bench.py（教材庫 b006〜b011。今のモデルが見ていない列）。確率は pool-bench.yml が出す npz（列 × 見方 × 種類）。
どの道具も「決め方を選ぶ陣」と「確かめる陣」を分ける（1 陣ずつ外して決め、外した陣で測る＝leave-one-batch-out）。

道具：
1. 何通りかの見方の平均（tta）：1 列を値の選び方・同じ表の列の並びを変えて k 通り読み、確率を平均する
2. 表全体の 2 回目の判定（table_pass）：1 回目の確率に、同じ表のほかの列の確率（平均・最大）を足して、小さなロジスティック回帰で判定し直す
   （例：同じ表に amount が並ぶ表の「数量」は quantity、など）
3. 言い切りを控える基準（abstain）：数字の種類（date・amount・quantity・rate・id）を答えるとき、1 位の確率が T 未満なら「不明」にする
4. 迷う表を先に選ぶ（select）：見方の間で答えが割れる・1 位の確率が低い列の多い表から、ラベル付けに回す
採点は llm_baseline.score_real と同じ（正解・誤り・不明・重大＝数字の種類どうしの取り違え）。判定の見張り（guard）は train3.decide_with_details（既定の版）。
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from collections import defaultdict

import numpy as np

import pool_bench as B

NUMERIC = {"date", "amount", "quantity", "rate", "id"}


# ---------------------------------------------------------------- 読み込み

def load_probs(pattern="eval_reports/pool_bench/probs_v*_b*.npz"):
    """npz（陣ごと）を読み、{"陣:id": (見方, 種類) の確率} と種類の並びを返す。"""
    probs, labels = {}, None
    for f in sorted(glob.glob(pattern)):
        z = np.load(f, allow_pickle=False)
        lab = [str(x) for x in z["labels"]]
        if labels is None:
            labels = lab
        elif lab != labels:
            raise ValueError(f"{f}：種類の並びが違う")
        for k, p in zip(z["ids"], z["probs"]):
            probs[str(k)] = p.astype("float32")
    return probs, labels


def from_top3(cols, labels):
    """npz が無いときの代わり：保存済みの上位 3 つから確率を作る（残りは均等）。見方は 1 通り。"""
    L = {c: i for i, c in enumerate(labels)}
    out = {}
    for c in cols:
        p = np.zeros(len(labels), dtype="float32")
        for t in c["top3"]:
            p[L[t["label"]]] = t["probability"]
        rest = max(0.0, 1.0 - p.sum())
        p[p == 0] = rest / max(1, (p == 0).sum())
        out[f"{c['batch']}:{c['id']}"] = p[None, :]
    return out


def rows_for_guard(cols):
    return [(c["header"], c["values5"], "", c["context"], c["unit"]) for c in cols]


def judge(labels, P, cols):
    from train3 import decide_with_details
    return [d["guarded_prediction"] for d in decide_with_details(labels, P, rows_for_guard(cols))]


def score(pred, cols):
    """正解が決まっている列だけを採点。正解が unknown の列への言い切りも数える。"""
    from llm_baseline import score_real
    keep = [(p, c["truth"]) for p, c in zip(pred, cols) if c["truth"] and c["truth"] not in B.NOT_USED]
    s = score_real([p for p, _ in keep], [t for _, t in keep])
    s["asserted_unknown"] = sum(1 for p, c in zip(pred, cols) if c["truth"] == "unknown" and p not in ("unknown", "other"))
    s["n_unknown_truth"] = sum(1 for c in cols if c["truth"] == "unknown")
    return s


def fmt(s):
    return (f"正 {s['acc_all']:.2%}（{s['correct']}/{s['n']}）・誤 {s['wrong']}・不明 {s['unknown']}・重大 {s['critical']}・"
            f"その他見送り {s['other_ok']}/{s['other_ok'] + s['other_ng']}・unknown への言い切り {s['asserted_unknown']}/{s['n_unknown_truth']}")


# ---------------------------------------------------------------- 1. 見方の平均

def tta(P_views, k):
    """(列, 見方, 種類) → 先頭 k 通りの平均（0 番目は今の入力そのもの）。"""
    return P_views[:, :k, :].mean(axis=1)


# ---------------------------------------------------------------- 2. 表全体の 2 回目の判定

def table_features(P, cols):
    """各列：自分の確率・同じ表のほかの列の確率の平均と最大・表の列数（対数）。"""
    by_t = defaultdict(list)
    for i, c in enumerate(cols):
        by_t[(c["batch"], c["table"])].append(i)
    n, k = P.shape
    mean_o, max_o, size = np.zeros((n, k)), np.zeros((n, k)), np.zeros((n, 1))
    for idx in by_t.values():
        sub = P[idx]
        tot = sub.sum(axis=0)
        for j, i in enumerate(idx):
            if len(idx) > 1:
                mean_o[i] = (tot - sub[j]) / (len(idx) - 1)
                max_o[i] = np.delete(sub, j, axis=0).max(axis=0)
            size[i] = np.log1p(len(idx))
    return np.hstack([np.log(np.clip(P, 1e-6, 1)), mean_o, max_o, size])


def table_pass_fit(P, cols, labels, C=1.0):
    from sklearn.linear_model import LogisticRegression
    X = table_features(P, cols)
    y = [c["truth"] for c in cols]
    m = [i for i, t in enumerate(y) if t and t not in B.NOT_USED and t in labels]
    lr = LogisticRegression(C=C, max_iter=3000)
    lr.fit(X[m], [y[i] for i in m])
    return lr


def table_pass_apply(lr, P, cols, labels, mix=1.0):
    """2 回目の確率を元の種類の並びに戻す（学習に出てこなかった種類は 1 回目の確率のまま）。mix は 2 回目の重み。"""
    Q = lr.predict_proba(table_features(P, cols))
    out = P.copy()
    idx = [labels.index(c) for c in lr.classes_]
    sub = out[:, idx].sum(axis=1, keepdims=True)
    new = np.zeros_like(out)
    new[:, idx] = Q * sub
    rest = [j for j in range(len(labels)) if j not in idx]
    new[:, rest] = out[:, rest]
    return mix * new + (1 - mix) * P


# ---------------------------------------------------------------- 3. 言い切りを控える基準

def abstain(labels, P, pred, T):
    top = P.max(axis=1)
    return [("unknown" if (p in NUMERIC and t < T) else p) for p, t in zip(pred, top)]


# ---------------------------------------------------------------- 4. 迷う表を先に選ぶ

def uncertainty(P_views):
    """列ごとの迷いの大きさ：1 −（平均の 1 位の確率）＋ 見方の間で 1 位が割れた割合。"""
    mean = P_views.mean(axis=1)
    top1 = mean.max(axis=1)
    arg = P_views.argmax(axis=2)
    split = 1.0 - (arg == mean.argmax(axis=1)[:, None]).mean(axis=1)
    return (1.0 - top1) + split


def capture_curve(unc, wrong, fracs=(0.1, 0.2, 0.3)):
    """迷いの大きい順に列を見たとき、全部の誤りのうち何割を見つけられるか。"""
    order = np.argsort(-unc)
    tot = max(1, wrong.sum())
    return {f: float(wrong[order[: int(len(order) * f)]].sum() / tot) for f in fracs}


# ---------------------------------------------------------------- 比べる

def compare(probs, labels, cols, out_md=None):
    batches = sorted({c["batch"] for c in cols})
    ids = [f"{c['batch']}:{c['id']}" for c in cols]
    PV = np.stack([probs[i] for i in ids])            # (列, 見方, 種類)
    n_views = PV.shape[1]
    lines = [f"# 教材庫で道具を試した結果（{', '.join(batches)}・{len(cols)} 列・見方 {n_views} 通り）", "",
             "今のモデル（E5-base 種子 1）は教材庫を見ていない。学習はしていない（推論と集計だけ）。決め方は 1 陣ずつ外して決め、外した陣で測った。", ""]
    base_pred = judge(labels, PV[:, 0, :], cols)
    agree = sum(p == c["pred"] for p, c in zip(base_pred, cols)) / len(cols)
    lines.append(f"- 0 番目の見方の判定と保存済みの予測の一致：{agree:.2%}（100% でなければ入力の作り方がずれている）")
    lines += ["", "| 方法 | 結果 |", "|---|---|", f"| 今のまま（見方 1） | {fmt(score(base_pred, cols))} |"]
    for k in range(2, n_views + 1):
        lines.append(f"| 見方 {k} 通りの平均 | {fmt(score(judge(labels, tta(PV, k), cols), cols))} |")
    best_k = n_views
    P1 = tta(PV, best_k)
    # 2. 表全体の 2 回目（1 陣ずつ外して学ぶ）
    for src_name, P_src in (("見方 1", PV[:, 0, :]), (f"見方 {best_k}", P1)):
        P2 = np.zeros_like(P_src)
        for b in batches:
            tr = [i for i, c in enumerate(cols) if c["batch"] != b]
            te = [i for i, c in enumerate(cols) if c["batch"] == b]
            lr = table_pass_fit(P_src[tr], [cols[i] for i in tr], labels)
            P2[te] = table_pass_apply(lr, P_src[te], [cols[i] for i in te], labels)
        lines.append(f"| {src_name}＋表全体の 2 回目 | {fmt(score(judge(labels, P2, cols), cols))} |")
    # 3. 言い切りを控える（T を外した陣以外で、重大を半分にする最小の T として決める）
    P3 = P2
    pred3 = judge(labels, P3, cols)
    chosen = {}
    final = list(pred3)
    for b in batches:
        tr = [i for i, c in enumerate(cols) if c["batch"] != b]
        te = [i for i, c in enumerate(cols) if c["batch"] == b]
        sub_cols = [cols[i] for i in tr]
        base_crit = score([pred3[i] for i in tr], sub_cols)["critical"]
        T_pick = 0.0
        for T in [round(0.40 + 0.02 * j, 2) for j in range(30)]:
            s = score(abstain(labels, P3[tr], [pred3[i] for i in tr], T), sub_cols)
            if s["critical"] <= base_crit / 2:
                T_pick = T
                break
        chosen[b] = T_pick
        for i, p in zip(te, abstain(labels, P3[te], [pred3[i] for i in te], T_pick)):
            final[i] = p
    lines.append(f"| ＋言い切りを控える（数字の種類で 1 位 < T なら不明。T は陣ごとに {sorted(set(chosen.values()))}） | {fmt(score(final, cols))} |")
    # 4. 迷う列を先に選ぶ
    wrong = np.array([1 if (c["truth"] and c["truth"] not in B.NOT_USED and p != c["truth"] and p not in ("unknown", "other")) else 0
                      for p, c in zip(base_pred, cols)])
    cap = capture_curve(uncertainty(PV), wrong)
    rnd = {f: f for f in cap}
    lines += ["", "## 迷う列を先に選ぶ（今のままの判定の誤りのうち、何割を先に見つけられるか）", "",
              "| 見る割合 | 迷いの大きい順 | でたらめな順 |", "|---|---:|---:|"]
    lines += [f"| {int(f * 100)}% | {v:.1%} | {rnd[f]:.0%} |" for f, v in cap.items()]
    text = "\n".join(lines) + "\n"
    if out_md:
        os.makedirs(os.path.dirname(out_md), exist_ok=True)
        open(out_md, "w", encoding="utf-8").write(text)
    return text


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches", default=",".join(B.BENCH_BATCHES))
    ap.add_argument("--top3", action="store_true", help="npz の代わりに保存済みの上位 3 つで試す（見方 1 通り）")
    ap.add_argument("--out", default="bench/pool_tools.md")
    a = ap.parse_args(argv)
    cols = B.load_bench(a.batches.split(","))
    if a.top3:
        labels = json.load(open(f"materials/pool/work/{cols[0]['batch']}/pred_e5base_seed1.json", encoding="utf-8"))["labels"]
        probs = from_top3(cols, labels)
    else:
        probs, labels = load_probs()
        cols = [c for c in cols if f"{c['batch']}:{c['id']}" in probs]
    print(compare(probs, labels, cols, a.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
