"""D2 で L が伸びた原因を確かめる（2026-10-31 Claude。オーナー「この結果の原因を確かめ」）。

決める陣の同じ列で、A（種子 1〜3）と L（種子 1〜3）の正誤を並べ、
  1. 3 本中の正しい本数の差が 2 以上の「安定して変わった列」を、正解・本体の 1 位の移り・列名の形（v24 の KIND×CODE）・言語・陣・先生で分ける。
  2. 種子のゆれの基準：6 本を 3 本ずつに分ける 10 通りすべてで同じ数を出し、A/L の分け方がどこにあるかを見る（並べ替えの基準）。
  3. 重大の列を書き出す。
  python research/d2_why/analyze.py → research/d2_why/findings_data.md
"""
import collections
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research"))
sys.path.insert(0, os.path.join(ROOT, "research", "labels"))
import d1_eval as D  # noqa: E402
from v24_targets import KIND, CODE  # noqa: E402

F = os.path.join(ROOT, "materials", "pool", "work", "d1dec")
RUNS = {"A1": "pred_d1_job1", "A2": "pred_d1_job2", "A3": "pred_d2_job1", "L1": "pred_d2_job2", "L2": "pred_d2_job3", "L3": "pred_d2_job4"}


def main():
    per = json.load(open(os.path.join(ROOT, "research", "d2_eval_decide_per_column.json"), encoding="utf-8"))
    base = D.load_side("decide")
    cols = {c["id"]: c for cs in base.values() for c in cs if c["id"] in per["A1"]}
    raw = {}
    for n, f in RUNS.items():
        rows = {r["id"]: r for r in json.load(open(os.path.join(F, f + ".json"), encoding="utf-8"))["rows"]}
        raw[n] = {k: rows[k]["raw_prediction"] for k in cols}
    final_t = {b: (D.B.WORK / b / "sheets" / "answers_final").exists() for b in D.BATCHES}
    names = list(RUNS)
    okn = lambda grp, k: sum(per[n][k] == "ok" for n in grp)  # noqa: E731

    def stable(ga, gb):
        up = [k for k in cols if okn(gb, k) - okn(ga, k) >= 2]
        dn = [k for k in cols if okn(ga, k) - okn(gb, k) >= 2]
        return up, dn

    A, L = names[:3], names[3:]
    up, dn = stable(A, L)
    out = ["# D2 の原因の数字（`research/d2_why/analyze.py`）", "", f"- 採点 {len(cols)} 列。安定して変わった列＝3 本中の正しい本数の差が 2 以上。", "",
           f"## 1. A→L で安定して変わった列：良くなった {len(up)}・悪くなった {len(dn)}（差 {len(up) - len(dn):+d}）", ""]
    # 並べ替えの基準
    null = []
    for g in itertools.combinations(names, 3):
        if "A1" not in g:
            continue   # 鏡の分け方を 1 回だけ
        h = [n for n in names if n not in g]
        u, d = stable(list(g), h)
        null.append((g, len(u) - len(d), sum(okn(h, k) - okn(g, k) for k in cols)))
    out += ["### 種子のゆれの基準（6 本を 3 本ずつに分ける 10 通り。差＝後ろの 3 本 − 前の 3 本）", "", "| 前の 3 本 | 安定した差（列） | 正しいの合計の差（本×列） |", "|---|---:|---:|"]
    for g, s, t in sorted(null, key=lambda x: -abs(x[1])):
        out.append(f"| {'・'.join(g)} | {s:+d} | {t:+d} |")
    out.append("")

    def table(ks, title):
        out.extend([f"### {title}", ""])
        for lab, fn in (("正解", lambda k: cols[k]["truth"]),
                        ("本体の 1 位（A の多数 → L の多数）", lambda k: collections.Counter(raw[n][k] for n in A).most_common(1)[0][0] + "→" + collections.Counter(raw[n][k] for n in L).most_common(1)[0][0]),
                        ("列名が KIND×CODE（v24 の形）", lambda k: str(bool(KIND.search(cols[k]["header"]) and CODE.search(cols[k]["header"])))),
                        ("言語", lambda k: cols[k]["language"]), ("陣", lambda k: cols[k]["batch"]),
                        ("正解の先生", lambda k: "Claude 裁定（answers_final）" if final_t[cols[k]["batch"]] else "ChatGPT（抜き取り裁定のみ）")):
            c = collections.Counter(fn(k) for k in ks)
            out.append(f"- {lab}：" + "、".join(f"{a} {b}" for a, b in c.most_common()))
        out.append("")
        out.extend(["| id | 列名 | 値（先頭 5） | 正解 | A の 1 位 | L の 1 位 | A 正 | L 正 |", "|---|---|---|---|---|---|---:|---:|"])
        for k in sorted(ks):
            c = cols[k]
            out.append(f"| {k} | {c['header'][:40]} | {' / '.join(v[:15] for v in c['values5'][:5])} | {c['truth']} | "
                       f"{','.join(raw[n][k] for n in A)} | {','.join(raw[n][k] for n in L)} | {okn(A, k)} | {okn(L, k)} |")
        out.append("")

    table(up, "良くなった列")
    table(dn, "悪くなった列")
    out += ["## 2. 重大の列（数値どうしの言い切りの誤り）", "", "| 名前 | id | 列名 | 正解 | 最終 |", "|---|---|---|---|---|"]
    for n in names:
        for k, v in per[n].items():
            if v == "crit":
                out.append(f"| {n} | {k} | {cols[k]['header'][:40]} | {cols[k]['truth']} | {raw[n][k]}（本体） |")
    # KIND×CODE の列全体での正しい
    kc = [k for k in cols if KIND.search(cols[k]["header"]) and CODE.search(cols[k]["header"])]
    out += ["", f"## 3. 列名が KIND×CODE の列（{len(kc)} 列）とそれ以外での正しい（3 本の平均）", "", "| 範囲 | 列 | A | L | 差（列） |", "|---|---:|---:|---:|---:|"]
    for lab, ks in (("KIND×CODE", kc), ("それ以外", [k for k in cols if k not in kc])):
        a = sum(okn(A, k) for k in ks) / 3
        l = sum(okn(L, k) for k in ks) / 3
        out.append(f"| {lab} | {len(ks)} | {a:.1f} | {l:.1f} | {l - a:+.1f} |")
    for t in ("id", "category"):
        ks = [k for k in cols if cols[k]["truth"] == t]
        a = sum(okn(A, k) for k in ks) / 3
        l = sum(okn(L, k) for k in ks) / 3
        out.append(f"| 正解 {t} | {len(ks)} | {a:.1f} | {l:.1f} | {l - a:+.1f} |")
    open(os.path.join(HERE, "findings_data.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
