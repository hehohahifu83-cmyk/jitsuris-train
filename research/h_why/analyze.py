"""直し G を入れた今の製品で、使い済みの陣（E1・E2・決める陣・確かめる陣）に残る不明・誤りの一覧（2026-11-01 Claude。探索用、採否には使わない）。
  python research/h_why/analyze.py → research/h_why/columns.jsonl・summary.md
"""
import collections, json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
import reserve_eval as R, d1_eval as D  # noqa: E402

J3 = ["pred_d2_job2.json", "pred_d2_job3.json", "pred_d2_job4.json"]


def main():
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", R.DICTS["K"][0]); D.EF._DICT.clear()
    fx = D.label_fixes(os.path.join(ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl"))
    sets = {"E1": (R.load("E1"), "e1", [R.PRED["L"][s] for s in R.SEEDS]),
            "E2": (R.load("E2"), "e2", [R.PRED["L"][s] for s in R.SEEDS]),
            "decide": (D.load_side("decide", fx), "d1dec", J3),
            "confirm": (D.load_side("confirm", fx), "d1conf", J3)}
    rows, tot = [], {}
    for sname, (base, folder, preds) in sets.items():
        t = [0] * 5
        for s, f in enumerate(preds, 1):
            path = os.path.join(ROOT, "materials", "pool", "work", folder, f)
            if not os.path.exists(path):
                print("なし", path); continue
            D.EF._PCACHE.clear(); p = {}
            r = D.EF.run(D.with_job(base, path), mv, labels, D.PRODUCT + ("K",), per=p)
            t = [a + b for a, b in zip(t, r)]
            for k, v in p.items():
                o = D.outcome(v[0], v[1])
                if True:
                    rows.append({"set": sname, "seed": s, "id": k, "outcome": o, "final": v[0], "truth": v[1], "header": v[2],
                                 "reason": v[3], "pred": v[4], "values": v[5], "unit": v[6]})
        tot[sname] = t; print(sname, t, flush=True)
    with open(os.path.join(HERE, "columns.jsonl"), "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    L = ["# 直し G のあとに残る不明・誤り（`research/h_why/analyze.py`。使い済みの陣、探索用）", "",
         "| 陣 | 採点（3 本） | 正しい | 不明 | 重大 | ほか |", "|---|---:|---:|---:|---:|---:|"]
    L += [f"| {k} | {t[0]} | {t[1]} | {t[2]} | {t[3]} | {t[4]} |" for k, t in tot.items()]
    L += ["", "## 不明の理由（3 本・4 陣の合計。本体の 1 位が正解だった数）", "", "| 理由 | 不明 | うち本体の 1 位が正解 |", "|---|---:|---:|"]
    c1, c2 = collections.Counter(), collections.Counter()
    for r in rows:
        if r["outcome"] == "unk":
            key = str(r["reason"]).split(":")[0]; c1[key] += 1; c2[key] += r["pred"] == r["truth"]
    L += [f"| {k} | {v} | {c2[k]} |" for k, v in c1.most_common()]
    L += ["", "## 誤り（正解 → 答え）", "", "| 正解 → 答え | 出力 |", "|---|---:|"]
    c3 = collections.Counter(f"{r['truth']} → {r['final']}" for r in rows if r["outcome"] in ("wrong", "crit"))
    L += [f"| {k} | {v} |" for k, v in c3.most_common(25)]
    open(os.path.join(HERE, "summary.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
