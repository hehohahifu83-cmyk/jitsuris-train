"""原因の確かめ：同じ C2 の重みで、入力に表の題名を入れたとき（pred_c2t_seed1.json）と入れないとき（pred_c2_seed1.json）を、
今の製品の形（audit.py と同じ段：見張り → recheck v1 → 検査役 v2 → rho 0.8 → 通貨の手がかり）に通して比べる（2026-10-30 Claude）。
**採るかどうかを決める試しではない**（題名を製品に入れるかは別の話。製品に来る CSV には題名がないことも多い）。
「不明・重大のうち、題名が入力に無いせいの分がどれだけあるか」を数える。
対象：題名ありの予測がある陣（dev1029＝b060・b062・b063、devt1517＝b015・b016・b017。題名の対応表は research/unknown/titles_all.json）
出力：research/unknown/title_check.md
使い方：python materials/pool/split_preds.py materials/pool/work/dev1029 pred_c2t_seed1.json && python research/unknown/title_check.py
"""
import json
import os
import sys
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
import research.unknown.audit as A  # noqa: E402

V, E = A.V, A.E
# dev1029（b060・b062・b063）と devt1517（b015・b016・b017。ChatGPT が表の題名で決めた列はすべてここ）。b064・b065 は題名ありの予測なし
BATCHES = tuple(b for b in ("b015", "b016", "b017", "b060", "b062", "b063") if os.path.exists(os.path.join(ROOT, "materials", "pool", "work", b, "pred_c2t_seed1.json")))


def finals(name, mv, labels):
    out = {}
    for b in BATCHES:
        path = os.path.join(ROOT, "materials", "pool", "work", b, name)
        te, _ = A.with_pred(E.load_batch(b), path)
        P = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
        for j, lab in enumerate(mv.classes_):
            P[:, labels.index(lab)] = p[:, j]
        base = E.base_decisions(te)
        E._VETO.clear()   # 検査役のためておく分は id() が鍵なので、前の陣・前の予測の結果を取り違えないよう毎回消す（2026-10-30）
        fin = E.combine(base, P, np.zeros(len(te)), labels, A.TAU, None, list(range(len(te))))
        for k, c in enumerate(te):
            if not c["truth"] or c["truth"] in ("unknown", "S", "other", "person"):
                continue
            cand = V.candidate(fin[k][0], fin[k][1], c["pred"], c["top3"], c["header"], P[k], labels, A.RHO)
            lab = cand if cand else fin[k][0]
            top = c["top3"][0]["label"] if c.get("top3") else None
            out[c["id"]] = {"truth": c["truth"], "final": V.amount_cue_veto(lab, c["header"], c.get("unit"), c["values"]), "top1": top, "header": c["header"]}
    return out


def tally(d):
    n = len(d)
    ok = sum(r["final"] == r["truth"] for r in d.values())
    unk = sum(r["final"] == "unknown" for r in d.values())
    crit = sum(r["final"] != r["truth"] and r["final"] in V.NUMERIC and r["truth"] in V.NUMERIC for r in d.values())
    top = sum(r["top1"] == r["truth"] for r in d.values())
    return n, ok, unk, crit, top


def main():
    labels = list(V.LABELS)
    train = [c for b in A.TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    a, b = finals("pred_c2_seed1.json", mv, labels), finals("pred_c2t_seed1.json", mv, labels)
    L = ["# 原因の確かめ：入力に表の題名を入れると不明・重大はどう変わるか（`research/unknown/title_check.py`）", "",
         "同じ C2 種子 1 の重み。題名なし＝今までの予測の形、題名あり＝学習（FT_TITLE=1）と同じ形。採るかを決める試しではない。", "",
         "| 予測 | 採点列 | 正しい | 不明 | 重大 | 本体の 1 位が正しい |", "|---|---:|---:|---:|---:|---:|"]
    for name, d in (("題名なし（今まで）", a), ("題名あり", b)):
        n, o, u, c, t = tally(d)
        L.append(f"| {name} | {n} | {o}（{o / n:.1%}） | {u}（{u / n:.1%}） | {c} | {t}（{t / n:.1%}） |")
    moves = Counter()
    for i in a:
        x, y = a[i], b[i]
        moves[("不明" if x["final"] == "unknown" else ("正" if x["final"] == x["truth"] else "誤"),
               "不明" if y["final"] == "unknown" else ("正" if y["final"] == y["truth"] else "誤"))] += 1
    L += ["", "## 列の動き（題名なし → 題名あり）", "", "| なし | あり | 列 |", "|---|---|---:|"]
    L += [f"| {p} | {q} | {n} |" for (p, q), n in sorted(moves.items())]
    unk_ids = {json.loads(l)["id"] for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}
    rc = {json.loads(l)["id"]: json.loads(l)["mechanism"] for l in open(os.path.join(HERE, "root_cause.jsonl"), encoding="utf-8")}
    fixed = Counter(rc[i].split(" ")[0] for i in unk_ids if i in b and b[i]["final"] == b[i]["truth"])
    L += ["", "## 不明だった列のうち、題名ありで正しくなった列（原因の仕組みごと）", "", "| 仕組み | 列 |", "|---|---:|"]
    L += [f"| {m} | {n} |" for m, n in fixed.most_common()]
    crit = [i for i in b if b[i]["final"] != b[i]["truth"] and b[i]["final"] in V.NUMERIC and b[i]["truth"] in V.NUMERIC]
    L += ["", f"## 題名ありで重大の列（{len(crit)}）", "", "| id | 見出し | 正解 | 題名あり | 題名なし |", "|---|---|---|---|---|"]
    L += [f"| {i} | {str(b[i]['header'])[:40]} | {b[i]['truth']} | {b[i]['final']} | {a[i]['final']} |" for i in crit]
    per = Counter()
    for i in a:
        bt = i[:4]
        per[(bt, "n")] += 1
        per[(bt, "unk_a")] += a[i]["final"] == "unknown"
        per[(bt, "unk_b")] += b[i]["final"] == "unknown"
        per[(bt, "ok_a")] += a[i]["final"] == a[i]["truth"]
        per[(bt, "ok_b")] += b[i]["final"] == b[i]["truth"]
    L += ["", "## 陣ごと（題名なし → 題名あり）", "", "| 陣 | 採点列 | 正しい | 不明 |", "|---|---:|---|---|"]
    L += [f"| {bt} | {per[(bt, 'n')]} | {per[(bt, 'ok_a')]} → {per[(bt, 'ok_b')]} | {per[(bt, 'unk_a')]} → {per[(bt, 'unk_b')]} |" for bt in BATCHES]
    worse = [i for i in a if a[i]["final"] == a[i]["truth"] and b[i]["final"] != b[i]["truth"]]
    L += ["", f"## 題名ありで正しくなくなった列（{len(worse)}）", "", "| id | 見出し | 正解 | 題名あり |", "|---|---|---|---|"]
    L += [f"| {i} | {str(a[i]['header'])[:40]} | {a[i]['truth']} | {b[i]['final']} |" for i in worse[:40]]
    open(os.path.join(HERE, "title_check.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:12]))


if __name__ == "__main__":
    main()
