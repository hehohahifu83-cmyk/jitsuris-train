"""C2 の直しを選ぶ段（2026-10-31 Claude）。決める陣・確かめる陣を使わずに、古い陣 23 個（b015〜b065、
research/fixes の DECIDE＋CONFIRM。予測は C2 種子 1＝教材庫 b014 までで学習、これらの陣は学習に入っていない）で、
自信が足りないだけで止めた列の内訳を数える。ここで決めた直しを事前記録に書き、決める陣（L の予測）で 1 回測る。
  python research/c2_why/select_old.py → research/c2_why/select_old.md
"""
import collections
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes")):
    sys.path.insert(0, p)
import d1_eval as D  # noqa: E402
import eval_fixes as EF  # noqa: E402

BINS = (0.70, 0.80, 0.90, 0.95, 9)


def main():
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    data = EF.load(EF.DECIDE + EF.CONFIRM)
    top = {c["id"]: (c["top3"][0]["label"], c["top3"][0]["probability"]) for cs in data.values() for c in cs}
    gr = {c["id"]: c.get("guard_reason") for cs in data.values() for c in cs}
    per = {}
    res = EF.run(data, mv, labels, D.PRODUCT, per=per)
    cnt = collections.defaultdict(collections.Counter)
    by = collections.defaultdict(lambda: [collections.Counter() for _ in BINS])
    for k, (final, truth, header, why, *_r) in per.items():
        if final != "unknown":
            continue
        r = str(why or gr[k] or "none")
        r = r.split(":")[0] if r.startswith(("verifier", "cue_conflict")) else r
        t, p = top[k]
        o = "ok" if t == truth else ("crit" if t in D.V.NUMERIC and truth in D.V.NUMERIC else "wrong")
        cnt[r][o] += 1
        by[(r, t)][next(i for i, b in enumerate(BINS) if p < b)][o] += 1
    n, ok, unk, crit, wrong = res
    L = ["# C2 を選ぶ段：古い陣 23 個（C2 種子 1 の予測。決める陣・確かめる陣は使わない）", "",
         f"- 製品の形（F4・F8）。採点 {n} 列：正しい {ok}・不明 {unk}・重大 {crit}・ほか {wrong}。", "",
         "| 止めた理由 | 不明 | 1 位が正しい | 重大になる | ほかの誤り |", "|---|---:|---:|---:|---:|"]
    for r, c in sorted(cnt.items(), key=lambda x: -sum(x[1].values())):
        L.append(f"| {r} | {sum(c.values())} | {c['ok']} | {c['crit']} | {c['wrong']} |")
    L += ["", "| 理由 | 1 位 | < 0.70 | 0.70〜0.80 | 0.80〜0.90 | 0.90〜0.95 | 0.95 以上 |", "|---|---|---|---|---|---|---|"]
    for (r, t), cs in sorted(by.items()):
        if r in ("low_confidence_no_cue", "amount_without_cue", "rate_without_cue", "date_value_evidence_low", "probability_below_threshold"):
            L.append(f"| {r} | {t} | " + " | ".join(f"{c['ok']}／{c['crit']}／{c['wrong']}" if c else "—" for c in cs) + " |")
    open(os.path.join(HERE, "select_old.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
