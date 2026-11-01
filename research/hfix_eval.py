"""直し H（H1 種類のコード・H2 日付の形）の E3 での 1 回だけの測り（2026-11-01 Claude。事前記録 bench/hfix_prereg_20261101.md。予測の前に書いた）。

  python research/hfix_eval.py [予測のフォルダ（試し用。書き出さない）]   → research/hfix_eval_E3.md
形（各 3 本、L＝D2 run 41192849082 job2〜4 の予測 pred_d2e_job2〜4、辞書は frozen_d3＝今の製品、直し G は製品に入っている）：
  P   ＝ 今の製品
  P+H ＝ P ＋ H1・H2（research/fixes/fixes_h.py）
"""
import hashlib, json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import d1_eval as D, d2_eval as D2, reserve_eval as R  # noqa: E402
ROOT = D.ROOT
H = ("H1", "H2")
SEEDS = (1, 2, 3)
PRED = {1: "pred_d2e_job2.json", 2: "pred_d2e_job3.json", 3: "pred_d2e_job4.json"}
ARMS = {"P": (), "P+H": H}
PREREG = os.path.join(ROOT, "bench", "hfix_prereg_20261101.md")
SPLIT = os.path.join(ROOT, "bench", "e3_split_20261101.json")


def load_e3():
    """E3 の列（bench/e3_split.py の規則：前の陣に出た表を外す）。正解は各陣の answers_final（2 人の裁定）。"""
    sys.path.insert(0, os.path.join(ROOT, "bench"))
    import d1_counts
    sp = json.load(open(SPLIT, encoding="utf-8"))
    drop = set(sp["dropped_tables"])
    out = {}
    for b in sp["batches"]:
        w = D.B.WORK / b
        if not (w / "sheets" / "answers_final").exists():
            raise SystemExit(f"{b}: answers_final（裁定のあとの正解）がまだない")
        corpus, labels = d1_counts.batch_rows(b)
        sets = json.load(open(w / "set.json", encoding="utf-8"))["columns"]
        cols = []
        for i, (c, l, s) in enumerate(zip(corpus, labels, sets)):
            if c["table"] in drop:
                continue
            vals = [str(v) for v in (c.get("row_values") or c["values"]) if str(v).strip() not in D.B.JUNK] or [str(v) for v in s["values"]]
            cols.append({"batch": b, "i": i, "id": s["id"], "table": c["table"], "header": str(c["header"]),
                         "values5": [str(v) for v in s["values"]], "values": vals, "context": [str(x) for x in s.get("siblings") or []],
                         "unit": str(s.get("unit") or ""), "language": c.get("language", ""), "truth": l["label"], "adjudicated": True,
                         "teacher": l["label"],
                         "tab": {"rows": c.get("row_values") or c["values"], "row_index": c.get("row_index"), "total": c.get("datastore_total")}})
        if cols:
            out[b] = cols
    return out


def main():
    want = open(PREREG, encoding="utf-8").read()
    got = hashlib.sha256(open(os.path.join(ROOT, "research", "fixes", "fixes_h.py"), "rb").read()).hexdigest()
    if got not in want:
        raise SystemExit("research/fixes/fixes_h.py が事前記録の SHA と違う")
    f, sha = R.DICTS["K"]
    if hashlib.sha256(open(os.path.join(ROOT, "materials", "dictionary", f), "rb").read()).hexdigest() != sha:
        raise SystemExit("辞書が凍結したものと違う")
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", f); D.EF._DICT.clear()
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "materials", "pool", "work", "e3")
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = load_e3()
    res, per, raw = {}, {}, {}
    for arm, fx in ARMS.items():
        for s in SEEDS:
            D.EF._PCACHE.clear(); p = {}
            res[f"{arm}{s}"] = D.EF.run(D.with_job(base, os.path.join(folder, PRED[s])), mv, labels, D.PRODUCT + ("K",) + fx, per=p)
            per[f"{arm}{s}"] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}; raw[f"{arm}{s}"] = p
    if len({r[0] for r in res.values()}) != 1:
        raise SystemExit("採点列の数が形で違う")
    tables = {c["id"]: (c["batch"], c["table"]) for cols in base.values() for c in cols if c["id"] in per["P1"]}
    mean = {arm: {"ok": sum(100 * res[f"{arm}{s}"][1] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
                  "unk": sum(100 * res[f"{arm}{s}"][2] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
                  "crit": sum(res[f"{arm}{s}"][3] for s in SEEDS),
                  "wrong": sum(100 * res[f"{arm}{s}"][4] / res[f"{arm}{s}"][0] for s in SEEDS) / 3} for arm in ARMS}
    n = res["P1"][0]
    L = ["# 直し H の E3 での 1 回だけの測り（`research/hfix_eval.py`）", "",
         f"- 事前記録 `bench/hfix_prereg_20261101.md`。採点 {n} 列。正解は 2 人のラベルの裁定（answers_final）。fixes_h.py SHA-256 {got}。", "",
         "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ARMS:
        m = mean[arm]
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f"{arm}{s}"][1]) for s in SEEDS) + " |")
    p2 = {f"A{s}": per[f"P{s}"] for s in SEEDS} | {f"L{s}": per[f"P+H{s}"] for s in SEEDS}
    lo, hi = D2.pooled_boot(p2, tables)
    d_ok, d_crit, d_wrong, checks, ok = D2.verdict({"A": mean["P"], "L": mean["P+H"]}, lo)
    mk = lambda b: "○" if b else "×"  # noqa: E731
    L += ["", "## 決まり 1〜4", "", f"- 1. 正しい {d_ok:+.2f} {mk(checks[0])}", f"- 2. 重大 {d_crit:+d} {mk(checks[1])}",
          f"- 3. ほかの誤り {d_wrong:+.2f} {mk(checks[2])}", f"- 4. 90% 区間 {lo:+.2f}〜{hi:+.2f} {mk(checks[3])}",
          f"- **判定：{'確かめられた（採る）' if ok else '確かめられなかった'}**", "", "## 直しが変えた列（3 本）", "", "| 本 | id | 列名 | 正解 | P | P+H |", "|---|---|---|---|---|---|"]
    for s in SEEDS:
        a, b = raw[f"P{s}"], raw[f"P+H{s}"]
        for k in sorted(a):
            if a[k][0] != b[k][0]:
                L.append(f"| {s} | {k} | {str(a[k][2])[:35]} | {a[k][1]} | {a[k][0]} | {b[k][0]} |")
    text = "\n".join(L) + "\n"
    if len(sys.argv) > 1:
        print(text); return
    open(os.path.join(HERE, "hfix_eval_E3.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, "hfix_eval_E3_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(text)


if __name__ == "__main__":
    main()
