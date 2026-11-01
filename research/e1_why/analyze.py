"""E1 の誤りと不明の原因（2026-11-01 Claude。オーナー「もっと細かく原因調査してからな」）。E1 は使い済み。調べるためだけで、採否には使わない。
L＋K2（L 3 本）と L′＋K2（L′ 3 本）の列ごとに、本体の 1 位・上位 3・確率、見張り・検査役などが止めた理由、最終の答えを並べ、
「不明」を、本体は当たっていたのに止めた（止めすぎ）と、本体も外れていた（止めて助かった）に分ける。
  python research/e1_why/analyze.py → research/e1_why/columns.jsonl・summary.md
"""
import collections, json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
import reserve_eval as R, d1_eval as D  # noqa: E402

def main():
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = R.load("E1"); cols = {c["id"]: c for cs in base.values() for c in cs}
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", R.DICTS["K2"][0]); D.EF._DICT.clear()
    out = []
    for arm, pk in (("L", "L"), ("LV", "LV")):
        for s in R.SEEDS:
            f = os.path.join(ROOT, "materials", "pool", "work", "e1", R.PRED[pk][s])
            rows = {r["id"]: r for r in json.load(open(f, encoding="utf-8"))["rows"]}
            D.EF._PCACHE.clear(); p = {}
            D.EF.run(D.with_job(base, f), mv, labels, D.PRODUCT + ("K",), per=p)
            for k, v in p.items():
                r, c = rows[k], cols[k]; t3 = r["top3"]
                out.append({"arm": arm, "seed": s, "id": k, "batch": c["batch"], "table": c["table"], "lang": c["language"],
                            "pub": "", "header": c["header"], "values": c["values5"][:5], "truth": v[1], "final": v[0],
                            "top1": t3[0]["label"], "p1": round(t3[0]["probability"], 3), "in3": v[1] in [x["label"] for x in t3[:3]],
                            "guarded": r["guarded_prediction"], "guard_reason": str(r.get("decision_reason") or ""), "stop": str(v[3] or "")})
    with open(os.path.join(HERE, "columns.jsonl"), "w", encoding="utf-8") as fh:
        for o in out: fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    L = ["# E1 の誤りと不明の原因（`research/e1_why/analyze.py`、使い済みの陣。採否には使わない）", ""]
    for arm in ("L", "LV"):
        A = [o for o in out if o["arm"] == arm]; n = len(A)
        cat = collections.Counter()
        for o in A:
            if o["final"] == o["truth"]: cat["正しい"] += 1
            elif o["final"] == "unknown":
                cat["不明・本体の 1 位は当たり（止めすぎ）" if o["top1"] == o["truth"] else ("不明・本体は外れ、正解は上位 3" if o["in3"] else "不明・本体は外れ、正解は上位 3 の外")] += 1
            else:
                cat["誤り・本体の 1 位のまま" if o["final"] == o["top1"] else "誤り・後の段で変えた"] += 1
        L += [f"## {arm}＋K2（3 本の合計 {n}）", ""] + [f"- {k}：{v}（{100*v/n:.1f}%）" for k, v in cat.most_common()] + [""]
        raw = sum(o["top1"] == o["truth"] for o in A)
        L.append(f"- 参考：本体の 1 位だけで答えたときの正しい {raw}（{100*raw/n:.1f}%）、最終 {cat['正しい']}（{100*cat['正しい']/n:.1f}%）")
        over = [o for o in A if o["final"] == "unknown" and o["top1"] == o["truth"]]
        L += ["", "### 止めすぎ：止めた理由（先頭の語）", ""] + [f"- {k}：{v}" for k, v in collections.Counter((o["stop"] or o["guard_reason"]).split(":")[0][:40] for o in over).most_common(12)]
        L += ["", "### 止めすぎ：正解の種類", ""] + [f"- {k}：{v}" for k, v in collections.Counter(o["truth"] for o in over).most_common()]
        L += ["", "### 止めすぎ：本体の確率", ""] + [f"- {k}：{v}" for k, v in sorted(collections.Counter(("≥0.95" if o["p1"] >= .95 else "0.8–0.95" if o["p1"] >= .8 else "0.5–0.8" if o["p1"] >= .5 else "<0.5") for o in over).items())]
        wr = [o for o in A if o["final"] not in ("unknown", o["truth"])]
        L += ["", "### 誤り：最終 → 正解（上位）", ""] + [f"- {a} → {b}：{v}" for (a, b), v in collections.Counter((o["final"], o["truth"]) for o in wr).most_common(15)]
        L += ["", "### 不明と誤りの言語", ""] + [f"- {k}：{v}" for k, v in collections.Counter(o["lang"] for o in A if o["final"] != o["truth"]).most_common()]
        L += ["", "### 不明と誤りが集まる表（上位 10）", ""] + [f"- {k[0]} {k[1][-55:]}：{v}" for k, v in collections.Counter((o["batch"], o["table"]) for o in A if o["final"] != o["truth"]).most_common(10)] + [""]
    open(os.path.join(HERE, "summary.md"), "w", encoding="utf-8").write("\n".join(L) + "\n"); print("\n".join(L))

if __name__ == "__main__":
    main()
