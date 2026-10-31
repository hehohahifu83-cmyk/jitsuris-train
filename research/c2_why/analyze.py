"""C2 の原因の数字（2026-10-31 Claude。D2 のあと、土台 A＋L＝L 種子 1〜3 の予測、決める陣）。

最後に不明になった列を、止めた理由ごとに分け、本体の 1 位（top3[0]）をそのまま言い切ったら
正しい・重大（数字の種類どうし）・ほかの誤りのどれになるかを数える。理由ごとに「止めて得か損か」を見るため。
  python research/c2_why/analyze.py → research/c2_why/findings_data.md
"""
import collections
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
import d1_eval as D  # noqa: E402
import d2_eval as D2  # noqa: E402

F = os.path.join(ROOT, "materials", "pool", "work", "d1dec")


def main():
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm],
                       np.array([c["truth"] for c in train])[okm])
    base = D.load_side("decide")
    cnt = collections.defaultdict(collections.Counter)
    ex = collections.defaultdict(list)
    for name in ("L1", "L2", "L3"):
        D.EF._PCACHE.clear()
        data = D.with_job(base, os.path.join(F, D2.RUNS[name][2]))
        top = {c["id"]: c["top3"][0]["label"] for cs in data.values() for c in cs}
        p1 = {c["id"]: c["top3"][0]["probability"] for cs in data.values() for c in cs}
        greason = {c["id"]: c.get("guard_reason") for cs in data.values() for c in cs}
        per = {}
        D.EF.run(data, mv, labels, D.PRODUCT, per=per)
        for k, (final, truth, header, why, guarded, vals, unit) in per.items():
            if final != "unknown":
                continue
            r = str(why or greason[k] or "none")
            r = r.split(":")[0] if r.startswith(("verifier", "cue_conflict")) else r
            t = top[k]
            o = "ok" if t == truth else ("crit" if t in D.V.NUMERIC and truth in D.V.NUMERIC else "wrong")
            cnt[r][o] += 1
            if len(ex[r]) < 400:
                ex[r].append((name, k, header, truth, t, round(p1[k], 3), vals))
    L = ["# C2：不明になった列の理由と、本体の 1 位を言い切った場合（L 種子 1〜3 の合計、決める陣）", "",
         "| 止めた理由 | 不明の列（3 本の合計） | 1 位が正しい | 1 位が重大になる | 1 位がほかの誤り | 言い切ったときの差し引き（正しい − 重大×3 − ほか） |", "|---|---:|---:|---:|---:|---:|"]
    for r, c in sorted(cnt.items(), key=lambda x: -sum(x[1].values())):
        n = sum(c.values())
        L.append(f"| {r} | {n} | {c['ok']} | {c['crit']} | {c['wrong']} | {c['ok'] - 3 * c['crit'] - c['wrong']:+d} |")
    L += ["", "## 自信が足りないだけで止めた理由：本体の 1 位の種類 × 1 位の確率ごと（3 本の合計。正しい／重大／ほか）", "",
          "| 理由 | 1 位 | < 0.70 | 0.70〜0.80 | 0.80〜0.90 | 0.90〜0.95 | 0.95 以上 |", "|---|---|---|---|---|---|---|"]
    bins = (0.70, 0.80, 0.90, 0.95, 9)
    for r in ("low_confidence_no_cue", "amount_without_cue", "rate_without_cue", "date_value_evidence_low"):
        by = collections.defaultdict(lambda: [collections.Counter() for _ in bins])
        for e in ex.get(r, []):
            o = "ok" if e[4] == e[3] else ("crit" if e[4] in D.V.NUMERIC and e[3] in D.V.NUMERIC else "wrong")
            by[e[4]][next(i for i, b in enumerate(bins) if e[5] < b)][o] += 1
        for t, cs in sorted(by.items()):
            L.append(f"| {r} | {t} | " + " | ".join(f"{c['ok']}／{c['crit']}／{c['wrong']}" if c else "—" for c in cs) + " |")
    for r in sorted(ex, key=lambda x: -sum(cnt[x].values()))[:6]:
        L += ["", f"## {r}", "", "| 本 | id | 列名 | 正解 | 1 位 | 1 位の確率 | 値 |", "|---|---|---|---|---|---:|---|"]
        for e in ex[r]:
            L.append(f"| {e[0]} | {e[1]} | {str(e[2])[:30]} | {e[3]} | {e[4]} | {e[5]} | {' / '.join(v[:12] for v in e[6][:4])} |")
    open(os.path.join(HERE, "findings_data.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(l for l in L if not l.startswith("| L")))


if __name__ == "__main__":
    main()
