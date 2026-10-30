"""言い切って誤った列（重大と、ほかの誤り）が、製品の形のどの段から出たかを分ける（2026-10-30 Claude。オーナー「全ての懸念点の原因が判明してから」）。
段：本体（見張りを通った本体の答え）→ recheck（言い切りの検査・不明の再検査・同じ表の列名の形）→ 検査役 → rho（不明を候補に戻す）→ 通貨の手がかり。
出力：research/fixes/wrong.jsonl・wrong.md（決める陣・確かめる陣）
使い方：python research/fixes/wrong.py
"""
import json
import os
import sys
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
import eval_fixes as EF  # noqa: E402

V, E, A = EF.V, EF.E, EF.A


def main():
    labels = list(V.LABELS)
    train = [c for b in A.TRAIN for c in E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    rows = []
    for setname, batches in (("決める陣", EF.DECIDE), ("確かめる陣", EF.CONFIRM)):
        for b, te in EF.load(batches).items():
            P = EF.probs(b, te, mv, labels, False)
            base = E.base_decisions(te)
            E._VETO.clear()
            fin = E.combine(base, P, np.zeros(len(te)), labels, A.TAU, None, list(range(len(te))))
            for k, c in enumerate(te):
                t = c["truth"]
                if not t or t in ("unknown", "S", "other", "person"):
                    continue
                cand = V.candidate(fin[k][0], fin[k][1], c["pred"], c["top3"], c["header"], P[k], labels, A.RHO)
                lab = cand if cand else fin[k][0]
                final = V.amount_cue_veto(lab, c["header"], c.get("unit"), c["values"])
                if final in ("unknown", t):
                    continue
                top1 = c["top3"][0]["label"] if c.get("top3") else None
                if cand:
                    origin = "rho（不明を候補に戻した）"
                elif base[k][1] and str(base[k][1]).startswith("recheck:"):
                    origin = f"recheck が不明から戻した（{base[k][1]}）"
                elif c["pred"] == final:
                    origin = "本体の答えがそのまま通った"
                else:
                    origin = f"そのほか（見張り {c['pred']}・recheck {base[k]}）"
                rows.append({"set": setname, "id": c["id"], "header": c["header"], "values5": c["values5"][:5], "truth": t, "final": final,
                             "critical": final in V.NUMERIC and t in V.NUMERIC, "origin": origin, "model_top1": top1,
                             "p1": c["top3"][0]["probability"] if c.get("top3") else None, "guard": c["pred"], "recheck": list(base[k]),
                             "verifier_top": labels[int(P[k].argmax())]})
    with open(os.path.join(HERE, "wrong.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    L = ["# 言い切って誤った列：どの段から出たか（`research/fixes/wrong.py`）", ""]
    for s in ("決める陣", "確かめる陣"):
        xs = [r for r in rows if r["set"] == s]
        L += [f"## {s}（誤り {len(xs)}、うち重大 {sum(r['critical'] for r in xs)}）", "", "| 出どころ | 列 | 重大 |", "|---|---:|---:|"]
        L += [f"| {o} | {n} | {sum(r['critical'] for r in xs if r['origin'] == o)} |" for o, n in Counter(r["origin"] for r in xs).most_common()]
        L += ["", "| 正解 → 答え | 列 |", "|---|---:|"]
        L += [f"| {a} → {b} | {n} |" for (a, b), n in Counter((r["truth"], r["final"]) for r in xs).most_common(15)]
        L.append("")
    open(os.path.join(HERE, "wrong.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
