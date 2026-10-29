"""不明になった列の調査（2026-10-29 Claude。オーナー「2から始めよう。チャットGPTとともに徹底的に調査してくれ、GLOCKも使っていい」）。
今の製品の形（本体 C2 種子 1 → 見張り → recheck v1 → 検査役 v2（τ 0.05）→ rho 0.8 → 通貨の手がかり）で、新しい陣 8 つの採点できる列のうち
最後が不明になった列を集め、どの段で不明になったかと、本体・検査役の答えを列ごとに記録する。
出力：research/unknown/columns.jsonl（1 行＝1 列。正解を含むので先生のシートには入れない）、research/unknown/summary.md
使い方：python research/unknown/audit.py
"""
import json
import os
import sys
from collections import Counter

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from verifier_c1 import TAU  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

BATCHES = ("b015", "b016", "b017", "b060", "b062", "b063", "b064", "b065")
TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))
RHO = 0.8
OUT = os.path.join(ROOT, "research", "unknown")


def main():
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    titles = json.load(open(os.path.join(ROOT, "materials", "pool", "titles.json"), encoding="utf-8"))
    rows, stage_n, truth_by_stage = [], Counter(), {}
    total = 0
    for b in BATCHES:
        path = os.path.join(ROOT, "materials", "pool", "work", b, "pred_c2_seed1.json")
        reason = {r["id"]: r.get("decision_reason") for r in json.load(open(path, encoding="utf-8"))["rows"]}
        te, _ = with_pred(E.load_batch(b), path)
        P = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
        for j, lab in enumerate(mv.classes_):
            P[:, labels.index(lab)] = p[:, j]
        idx = list(range(len(te)))
        base = E.base_decisions(te)
        fin = E.combine(base, P, np.zeros(len(te)), labels, TAU, None, idx)
        for k, c in enumerate(te):
            # 採点と同じ範囲（verifier_eval.score）：正解が other の列は「不明」が正しい見送りなので数えない。person も数えない
            if not c["truth"] or c["truth"] in ("unknown", "S", "other", "person"):
                continue
            total += 1
            cand = V.candidate(fin[k][0], fin[k][1], c["pred"], c["top3"], c["header"], P[k], labels, RHO)
            lab = cand if cand else fin[k][0]
            final = V.amount_cue_veto(lab, c["header"], c.get("unit"), c["values"])
            if final != "unknown":
                continue
            if lab != "unknown":
                stage = "通貨の手がかり"
            elif c["pred"] == "unknown":
                stage = "見張り（本体の段）"
            elif base[k][0] == "unknown":
                stage = "recheck"
            elif fin[k][1]:
                stage = "検査役"
            else:
                stage = "その他"
            vtop = labels[int(np.argmax(P[k]))]
            top3 = [(t["label"], round(t["probability"], 3)) for t in (c["top3"] or [])]
            rows.append({"id": c["id"], "batch": b, "table": c["table"], "title": titles.get(c["table"], ""), "header": c["header"],
                         "values": [str(v) for v in c["values"][:8]], "unit": c.get("unit", ""), "siblings": list(c.get("context") or [])[:12],
                         "truth": c["truth"], "stage": stage, "guard_reason": reason.get(c["id"]), "base_reason": base[k][1],
                         "veto_reason": fin[k][1], "model_top3": top3, "verifier_top": [vtop, round(float(P[k].max()), 3)],
                         "model_top1_is_truth": bool(top3) and top3[0][0] == c["truth"]})
            stage_n[stage] += 1
            truth_by_stage.setdefault(stage, Counter())[c["truth"]] += 1
    with open(os.path.join(OUT, "columns.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    top1 = sum(r["model_top1_is_truth"] for r in rows)
    reasons = Counter(r["guard_reason"] for r in rows if r["stage"] == "見張り（本体の段）")
    L = ["# 不明になった列の調査：集計（`research/unknown/audit.py`）", "",
         f"- 新しい陣 8 つ・本体 C2・今の製品の形。採点できる列 {total}、不明 {len(rows)}（{len(rows) / total:.1%}）",
         f"- 本体の 1 位が正解だった不明：{top1}（{top1 / len(rows):.0%}）＝本体は分かっていたのに、決め方の段で不明になった列", "",
         "| 不明にした段 | 列 | 正解の種類（多い順） |", "|---|---:|---|"]
    for s, n in stage_n.most_common():
        L.append(f"| {s} | {n} | {', '.join(f'{k} {v}' for k, v in truth_by_stage[s].most_common(6))} |")
    L += ["", "## 見張りの理由（本体の段で不明）", "", "| 理由 | 列 |", "|---|---:|"] + [f"| {k} | {v} |" for k, v in reasons.most_common(15)]
    open(os.path.join(OUT, "summary.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
