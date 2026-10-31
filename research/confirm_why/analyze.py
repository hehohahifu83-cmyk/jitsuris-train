"""確かめる陣の誤りの原因（2026-10-31 Claude。オーナー「結果が出たら間違えたものの原因をつきとめ辞書の強化によって改善しそうなものを見つけろ」）。

測り（research/confirm_eval.py）のあとに読む。ここで見つけたことで辞書を変えたら、その辞書はこの陣では測らない（新しい陣で測る）。
今の形 L＋K（種子 1〜3）で、最後に正しくなかった列を、固有の列ごとにまとめる：
  - 本体の 1 位・上位 3 つ・確率、止めた理由、辞書が当たったか
  - 辞書が届きうるか（迷い＝不明か 1 位 < 0.95、かつ正解が上位 3 つ）
  - 1 位 → 正解 の組、言語、陣
  python research/confirm_why/analyze.py → research/confirm_why/errors.md・errors.jsonl
"""
import collections
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
sys.path.insert(0, ROOT)
import d1_eval as D  # noqa: E402
import table_dictionary as TD  # noqa: E402

F = os.path.join(ROOT, "materials", "pool", "work", "d1conf")
FIXES = os.path.join(ROOT, "research", "labels", "consistency_20261031", "decisions.jsonl")
DICT = os.path.join(ROOT, "materials", "dictionary", "frozen_d3.jsonl")
PRED = {1: "pred_d2_job2.json", 2: "pred_d2_job3.json", 3: "pred_d2_job4.json"}


def main():
    os.environ["JITSURIS_DICT"] = DICT
    dic = TD.Dictionary.load(DICT)
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    base = D.load_side("confirm", D.label_fixes(FIXES))
    cols = {c["id"]: c for cs in base.values() for c in cs}
    per, rows = {}, {}
    for s, f in PRED.items():
        D.EF._PCACHE.clear()
        p = {}
        D.EF.run(D.with_job(base, os.path.join(F, f)), mv, labels, D.PRODUCT + ("K",), per=p)
        per[s] = p
        rows[s] = {r["id"]: r for r in json.load(open(os.path.join(F, f), encoding="utf-8"))["rows"]}
    out = []
    for k in per[1]:
        finals = [per[s][k][0] for s in PRED]
        truth = per[1][k][1]
        nbad = sum(f != truth for f in finals)
        if nbad == 0:
            continue
        c = cols[k]
        top = [rows[s][k]["top3"] for s in PRED]
        t1 = collections.Counter(t[0]["label"] for t in top).most_common(1)[0][0]
        in3 = sum(truth in [x["label"] for x in t] for t in top)
        doubt = sum(per[s][k][0] == "unknown" or rows[s][k]["top3"][0]["probability"] < 0.95 for s in PRED)
        kind = collections.Counter("unk" if f == "unknown" else ("crit" if f in D.V.NUMERIC and truth in D.V.NUMERIC else "wrong")
                                   for f in finals if f != truth).most_common(1)[0][0]
        out.append({"id": k, "batch": c["batch"], "language": c["language"], "header": c["header"], "values": c["values"][:8],
                    "siblings": c["context"][:10], "table": c["table"], "truth": truth, "finals": finals, "bad": nbad, "kind": kind,
                    "top1": t1, "top3": [[x["label"], round(x["probability"], 3)] for x in top[0]], "truth_in_top3": in3,
                    "doubt": doubt, "reason": str(per[1][k][3] or ""), "dict_hits": dic.lookup(c["header"], c["values"])})
    out.sort(key=lambda x: (-x["bad"], x["id"]))
    with open(os.path.join(HERE, "errors.jsonl"), "w", encoding="utf-8") as fh:
        for o in out:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    n = len(per[1])
    reach = [o for o in out if o["truth_in_top3"] >= 2 and o["doubt"] >= 2]
    conf = [o for o in out if o["truth_in_top3"] >= 2 and o["doubt"] < 2]
    out3 = [o for o in out if o["truth_in_top3"] < 2]
    L = ["# 確かめる陣の誤りの原因（L＋K、種子 1〜3。`research/confirm_why/analyze.py`）", "",
         f"- 採点 {n} 列のうち、1 本でも正しくなかった固有の列 {len(out)}（3 本とも {sum(o['bad'] == 3 for o in out)}）。",
         f"- 辞書が届きうる（3 本中 2 本以上で、迷い かつ 正解が上位 3）：{len(reach)} 列。本体が自信をもって誤り：{len(conf)} 列。正解が上位 3 に無い：{len(out3)} 列。", "",
         "## 1 位 → 正解（届きうる列）", ""]
    for (a, b), m in collections.Counter((o["top1"], o["truth"]) for o in reach).most_common(25):
        L.append(f"- {a} → {b}：{m}")
    L += ["", "## 止めた理由（届きうる列、種子 1）", ""]
    for r, m in collections.Counter(o["reason"].split(":")[0] or "（なし）" for o in reach).most_common(15):
        L.append(f"- {r}：{m}")
    L += ["", "## 言語", ""] + [f"- {a}：{m}" for a, m in collections.Counter(o["language"] for o in out).most_common()]
    for title, grp in (("届きうる列", reach), ("本体が自信をもって誤り", conf), ("正解が上位 3 に無い", out3)):
        L += ["", f"## {title}", "", "| id | 列名 | 値 | 兄弟の列 | 正解 | 最終（3 本） | 上位 3（種子 1） | 理由 | 辞書 |", "|---|---|---|---|---|---|---|---|---|"]
        for o in grp:
            esc = lambda s: str(s).replace("|", "/").replace("\n", " ")  # noqa: E731
            L.append(f"| {o['id']} | {esc(o['header'])[:35]} | {' ・ '.join(esc(v)[:16] for v in o['values'][:5])} | {' ・ '.join(esc(x)[:18] for x in o['siblings'][:5])} | "
                     f"{o['truth']} | {','.join(o['finals'])} | {', '.join(f'{a}{p:.2f}' for a, p in o['top3'])} | {o['reason'][:28]} | {','.join(i for _, i in o['dict_hits'])} |")
    open(os.path.join(HERE, "errors.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:40]))


if __name__ == "__main__":
    main()
