"""止める段の直し（F1b・F3・F6・G1〜G4）の E2 での 1 回だけの測り（2026-11-01 Claude。事前記録 bench/stopfix_prereg_20261101.md。予測の前に書いた）。

  python research/stopfix_eval.py [予測のフォルダ（試し用。書き出さない）]   → research/stopfix_eval_E2.md
形（各 3 本、L＝D2 run 41192849082 job2〜4 の予測 pred_d2e_job2〜4、辞書は frozen_d3＝今の製品）：
  P   ＝ 今の製品（見張り → recheck F4・F8 → 検査役 v2 → rho 0.8 → 辞書 → 通貨の手がかり）
  P+G ＝ P ＋ F1b・F3・F6・G1・G2・G3・G4（research/fixes/fixes.py）
"""
import hashlib, json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import d1_eval as D, d2_eval as D2, reserve_eval as R  # noqa: E402
ROOT = D.ROOT
G = ("F1b", "F3", "F6", "G1", "G2", "G3", "G4")
SEEDS = (1, 2, 3)
PRED = {1: "pred_d2e_job2.json", 2: "pred_d2e_job3.json", 3: "pred_d2e_job4.json"}
ARMS = {"P": (), "P+G": G}


def main():
    want = open(os.path.join(ROOT, "bench", "stopfix_prereg_20261101.md"), encoding="utf-8").read()
    got = hashlib.sha256(open(os.path.join(ROOT, "research", "fixes", "fixes.py"), "rb").read()).hexdigest()
    if got not in want:
        raise SystemExit("research/fixes/fixes.py が事前記録の SHA と違う")
    f, sha = R.DICTS["K"]
    if hashlib.sha256(open(os.path.join(ROOT, "materials", "dictionary", f), "rb").read()).hexdigest() != sha:
        raise SystemExit("辞書が凍結したものと違う")
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", f); D.EF._DICT.clear()
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "materials", "pool", "work", "e2")
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = R.load("E2")
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
    L = ["# 止める段の直しの E2 での 1 回だけの測り（`research/stopfix_eval.py`）", "",
         f"- 事前記録 `bench/stopfix_prereg_20261101.md`。採点 {n} 列。正解は 2 人のラベルの裁定（answers_final）。fixes.py SHA-256 {got}。", "",
         "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ARMS:
        m = mean[arm]
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f"{arm}{s}"][1]) for s in SEEDS) + " |")
    p2 = {f"A{s}": per[f"P{s}"] for s in SEEDS} | {f"L{s}": per[f"P+G{s}"] for s in SEEDS}
    lo, hi = D2.pooled_boot(p2, tables)
    d_ok, d_crit, d_wrong, checks, ok = D2.verdict({"A": mean["P"], "L": mean["P+G"]}, lo)
    mk = lambda b: "○" if b else "×"  # noqa: E731
    L += ["", "## 決まり 1〜4", "", f"- 1. 正しい {d_ok:+.2f} {mk(checks[0])}", f"- 2. 重大 {d_crit:+d} {mk(checks[1])}",
          f"- 3. ほかの誤り {d_wrong:+.2f} {mk(checks[2])}", f"- 4. 90% 区間 {lo:+.2f}〜{hi:+.2f} {mk(checks[3])}",
          f"- **判定：{'確かめられた（採る）' if ok else '確かめられなかった'}**", "", "## 直しが変えた列（3 本）", "", "| 本 | id | 列名 | 正解 | P | P+G |", "|---|---|---|---|---|---|"]
    for s in SEEDS:
        a, b = raw[f"P{s}"], raw[f"P+G{s}"]
        for k in sorted(a):
            if a[k][0] != b[k][0]:
                L.append(f"| {s} | {k} | {str(a[k][2])[:35]} | {a[k][1]} | {a[k][0]} | {b[k][0]} |")
    text = "\n".join(L) + "\n"
    if len(sys.argv) > 1:
        print(text); return
    open(os.path.join(HERE, "stopfix_eval_E2.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, "stopfix_eval_E2_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(text)


if __name__ == "__main__":
    main()
