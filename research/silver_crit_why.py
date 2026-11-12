"""前回の銀の学習（C3b・C3s）で重大が増えた原因を列ごとに分ける（2026-11-12 Claude。読むだけ。オーナー「銀教材をもう一度 Codex と共にチェックし、重大が増えた原因を特定してから学習」）。

  python research/silver_crit_why.py   → research/silver_crit_why.json と標準出力

C3 の採点（research/c3_eval.py）と同じ製品の形で、銀なし（c3a）と銀あり（c3b・c3s）の重大の列を、どの段で生まれたかで分ける：
  本体：本体の 1 位（raw）がすでに数の別の種類 → 見張り・recheck・検査役を通り抜けた
  rho ：検査役のあとは不明（や別の答え）だったのに、rho（不明を言い切りに戻す段）が数の種類に戻した
"""
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from verifier_c1 import TAU  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))
SETS = {"c3b": ("b015", "b016", "b017", "b060", "b062", "b063"), "c3s": ("b015", "b016", "b017", "b060", "b062", "b063", "b064", "b065")}


def main():
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    out = {}
    for silver, batches in SETS.items():
        rows = []
        for b in batches:
            res = {}
            for model in ("c3a", silver):
                path = os.path.join(ROOT, "materials", "pool", "work", b, f"pred_{model}_seed1.json")
                if not os.path.exists(path):
                    continue
                te, _ = with_pred(E.load_batch(b), path)
                raw = {r["id"]: r for r in json.load(open(path, encoding="utf-8"))["rows"]}
                P = np.zeros((len(te), len(labels)), dtype="float32")
                p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
                for j, lab in enumerate(mv.classes_):
                    P[:, labels.index(lab)] = p[:, j]
                fin = E.combine(E.base_decisions(te), P, np.zeros(len(te)), labels, TAU, None, list(range(len(te))))
                for k, c in enumerate(te):
                    d = fin[k]
                    cand = V.candidate(d[0], d[1], c["pred"], c["top3"], c["header"], P[k], labels, 0.7)
                    final = cand if cand else d[0]
                    crit = bool(c["truth"]) and c["truth"] in V.NUMERIC and final in V.NUMERIC and final != c["truth"]
                    res.setdefault(c["id"], {})[model] = {"truth": c["truth"], "header": str(c["header"])[:50], "raw": raw[c["id"]].get("raw_prediction"),
                                                          "guarded": c["pred"], "after_verifier": d[0], "final": final, "rho": bool(cand), "crit": crit}
            for cid, m in res.items():
                if silver in m and m[silver]["crit"]:
                    x = m[silver]
                    stage = "rho" if x["rho"] else ("本体" if x["raw"] == x["final"] else "後段")
                    rows.append({"batch": b, "id": cid, **x, "stage": stage, "c3a_final": m.get("c3a", {}).get("final"), "c3a_crit": m.get("c3a", {}).get("crit")})
        out[silver] = rows
        print(f"== {silver}：重大 {len(rows)} 列（c3a でも重大 {sum(bool(r['c3a_crit']) for r in rows)}）")
        for r in rows:
            print(f"  {r['batch']} {r['header']} | 正解 {r['truth']} | 本体 {r['raw']} → 見張り {r['guarded']} → 検査役 {r['after_verifier']} → 最終 {r['final']} | 段 {r['stage']} | c3a {r['c3a_final']}")
    json.dump(out, open(os.path.join(ROOT, "research", "silver_crit_why.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
