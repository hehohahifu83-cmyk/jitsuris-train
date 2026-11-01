"""在庫の陣 E1 の 1 回だけの測り（2026-11-01 Claude。事前記録 bench/valuefix_prereg_20261101.md。予測の前に書いた）。

  python research/reserve_eval.py [E1] [予測のフォルダ（試し用。書き出さない）]   → research/reserve_eval_E1.md
形（各 3 本）：
  L＋K   ＝ L（D2 run 41192849082 job2〜4、予測 pred_d2e_job2〜4）＋ 辞書 frozen_d3
  L＋K2  ＝ 同じ予測 ＋ 辞書 frozen_v2
  L′＋K2 ＝ L′（£ の直し、回収 run 41226755937 job1〜3、予測 pred_lv_job1〜3）＋ 辞書 frozen_v2
正解は各陣の answers_final（2 人のラベルの裁定、research/labels/reserve_20261101）。採点の範囲・製品の形・決まり 1〜4 は D2・D3・確かめる陣と同じ。
"""
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d1_eval as D  # noqa: E402
import d2_eval as D2  # noqa: E402

ROOT = D.ROOT
DICTS = {"K": ("frozen_d3.jsonl", "08a227016f1ad94ccf5e3408626c1e72358540761f70ef26343de9139a6f4a45"),
         "K2": ("frozen_v2.jsonl", "0e1c07f5402e4ba984152c78b1bad79812a718d5ac323da883cfa65e2bedcc34")}
SEEDS = (1, 2, 3)
PRED = {"L": {1: "pred_d2e_job2.json", 2: "pred_d2e_job3.json", 3: "pred_d2e_job4.json"},
        "LV": {1: "pred_lv_job1.json", 2: "pred_lv_job2.json", 3: "pred_lv_job3.json"}}
ARMS = {"L+K": ("L", "K"), "L+K2": ("L", "K2"), "LV+K2": ("LV", "K2")}
PAIRS = (("LV+K2", "L+K2", "主な問い：教材の £ の直しの効き目"), ("L+K2", "L+K", "辞書 v2 の効き目"))


def load(side):
    sys.path.insert(0, os.path.join(ROOT, "bench"))
    import d1_counts
    sp = json.load(open(os.path.join(ROOT, "bench", "reserve_split_20261101.json"), encoding="utf-8"))
    out = {}
    for b in sp["batches"]:
        w = D.B.WORK / b
        corpus, labels = d1_counts.batch_rows(b)
        sets = json.load(open(w / "set.json", encoding="utf-8"))["columns"]
        cols = []
        for i, (c, l, s) in enumerate(zip(corpus, labels, sets)):
            if sp["publishers"][c.get("publisher") or c.get("source", "?")] != side:
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
    side = sys.argv[1] if len(sys.argv) > 1 else "E1"
    folder = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "materials", "pool", "work", side.lower())
    for k, (f, sha) in DICTS.items():
        if hashlib.sha256(open(os.path.join(ROOT, "materials", "dictionary", f), "rb").read()).hexdigest() != sha:
            raise SystemExit(f"辞書 {k} が凍結したものと違う")
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    base = load(side)
    res, per, raw = {}, {}, {}
    for arm, (pk, dk) in ARMS.items():
        os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", DICTS[dk][0])
        D.EF._DICT.clear()
        for s in SEEDS:
            D.EF._PCACHE.clear()
            p = {}
            res[f"{arm}{s}"] = D.EF.run(D.with_job(base, os.path.join(folder, PRED[pk][s])), mv, labels, D.PRODUCT + ("K",), per=p)
            per[f"{arm}{s}"] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
            raw[f"{arm}{s}"] = p
    if len({r[0] for r in res.values()}) != 1:
        raise SystemExit("採点列の数が形で違う")
    first = f"{next(iter(ARMS))}1"
    tables = {c["id"]: (c["batch"], c["table"]) for cols in base.values() for c in cols if c["id"] in per[first]}
    mean = {arm: {"ok": sum(100 * res[f"{arm}{s}"][1] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
                  "unk": sum(100 * res[f"{arm}{s}"][2] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
                  "crit": sum(res[f"{arm}{s}"][3] for s in SEEDS),
                  "wrong": sum(100 * res[f"{arm}{s}"][4] / res[f"{arm}{s}"][0] for s in SEEDS) / 3} for arm in ARMS}
    n = res[first][0]
    L = [f"# 在庫の陣 {side} の 1 回だけの測り（`research/reserve_eval.py`）", "",
         f"- 事前記録 `bench/valuefix_prereg_20261101.md`。採点 {n} 列。正解は 2 人のラベルの裁定（answers_final）。", "",
         "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ARMS:
        m = mean[arm]
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f"{arm}{s}"][1]) for s in SEEDS) + " |")
    L += ["", "## 決まり 1〜4", "", "| 比べ | 1. 正しい | 2. 重大 | 3. ほか < 正しい | 4. 90% 区間 | 判定 | 良く／悪く（固有の列） |", "|---|---|---|---|---|---|---|"]
    mk = lambda b: "○" if b else "×"  # noqa: E731
    for new, old, what in PAIRS:
        p2 = {f"A{s}": per[f"{old}{s}"] for s in SEEDS} | {f"L{s}": per[f"{new}{s}"] for s in SEEDS}
        lo, hi = D2.pooled_boot(p2, tables)
        d_ok, d_crit, d_wrong, checks, ok = D2.verdict({"A": mean[old], "L": mean[new]}, lo)
        okn = lambda a, k: sum(per[f"{a}{s}"][k] == "ok" for s in SEEDS)  # noqa: E731
        up = sum(1 for k in per[first] if okn(new, k) - okn(old, k) >= 2)
        dn = sum(1 for k in per[first] if okn(old, k) - okn(new, k) >= 2)
        L.append(f"| {new} 対 {old}（{what}） | {d_ok:+.2f} {mk(checks[0])} | {d_crit:+d} {mk(checks[1])} | {d_wrong:+.2f} {mk(checks[2])} | "
                 f"{lo:+.2f}〜{hi:+.2f} {mk(checks[3])} | {'**確かめられた**' if ok else '確かめられなかった'} | {up}／{dn} |")
    uk = [c for cols in base.values() for c in cols if c["id"] in per[first] and str(c.get("language")) != "ja" and c["truth"] == "amount"
          and c["batch"] in ("b091", "b092", "b093", "b105", "b106", "b107")]
    L += ["", "## 読むだけ：英国の陣の金額の列（正しい、3 本の合計）", ""]
    for arm in ARMS:
        L.append(f"- {arm}：{sum(per[f'{arm}{s}'][c['id']] == 'ok' for s in SEEDS for c in uk)} / {3 * len(uk)}")
    text = "\n".join(L) + "\n"
    if len(sys.argv) > 2:
        print(text)
        return
    open(os.path.join(HERE, f"reserve_eval_{side}.md"), "w", encoding="utf-8").write(text)
    json.dump(per, open(os.path.join(HERE, f"reserve_eval_{side}_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(text)


if __name__ == "__main__":
    main()
