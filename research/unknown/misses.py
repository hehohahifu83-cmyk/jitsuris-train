"""今の製品の形（決め方つき）の最終の答えを全採点列で書き出す（--all）か、（audit.py と同じ段）で、新しい陣 8 つの採点列のうち「正解が数字の種類なのに、別の種類と言い切った列」を集める（2026-10-29 Claude）。
答えも数字の種類なら重大（score_real）。出力：research/unknown/misses.jsonl（正解を含む。先生は見ない）
使い方：python research/unknown/misses.py > research/unknown/misses.jsonl
　　　　python research/unknown/misses.py --all > research/unknown/final_c21.jsonl（採点列すべて：id・見出し・値・単位・同じ表の列名・正解・最終の答え）
"""
import sys, json, os
sys.path.insert(0, os.getcwd())
import research.unknown.audit as A
import numpy as np
V, E = A.V, A.E
labels = list(V.LABELS)
train = [c for b in A.TRAIN for c in E.load_batch(b)]
ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
for b in A.BATCHES:
    path = os.path.join(A.ROOT, "materials", "pool", "work", b, "pred_c2_seed1.json")
    te, _ = A.with_pred(E.load_batch(b), path)
    P = np.zeros((len(te), len(labels)), dtype="float32")
    p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
    for j, lab in enumerate(mv.classes_): P[:, labels.index(lab)] = p[:, j]
    base = E.base_decisions(te)
    fin = E.combine(base, P, np.zeros(len(te)), labels, A.TAU, None, list(range(len(te))))
    for k, c in enumerate(te):
        if not c["truth"] or c["truth"] in ("unknown", "S", "other", "person"): continue
        cand = V.candidate(fin[k][0], fin[k][1], c["pred"], c["top3"], c["header"], P[k], labels, A.RHO)
        lab = cand if cand else fin[k][0]
        final = V.amount_cue_veto(lab, c["header"], c.get("unit"), c["values"])
        if "--all" in sys.argv:
            print(json.dumps({"id": c["id"], "batch": b, "header": c["header"], "values": [str(v) for v in c["values"][:8]], "unit": c.get("unit") or "", "siblings": list(c.get("context") or [])[:12], "table": c["table"], "truth": c["truth"], "final": final}, ensure_ascii=False))
            continue
        if final != "unknown" and final != c["truth"] and c["truth"] in V.NUMERIC:
            print(json.dumps({"id": c["id"], "header": c["header"], "values": [str(v) for v in c["values"][:8]], "unit": c.get("unit"), "truth": c["truth"], "final": final, "pred": c["pred"], "cand": cand, "base": base[k], "fin": fin[k], "siblings": list(c.get("context") or [])[:12], "table": c["table"]}, ensure_ascii=False))
