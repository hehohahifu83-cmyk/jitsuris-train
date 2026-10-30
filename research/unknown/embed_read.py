"""embed_nn.json（本体の中で近い教材の列）を読む（2026-10-30 Claude）。
誤った列ごとに、近い 10 列に付いた教材の種類（teacher）の多数を、本体の答え・正解と比べる。
  本体の答えと同じ → その教材の列から覚えた（どの出どころ・どの列かを並べる）
  正解と同じ → 近い教材は正しく付いているのに、本体はその列を誤った（近さでは説明できない）
出力：research/unknown/embed_read.md
使い方：python research/unknown/embed_read.py（不明 73 列）
　　　　python research/unknown/embed_read.py research/fixes/embed_wrong.json research/fixes/wrong.jsonl research/fixes/embed_wrong_read.md（言い切って誤った列）
"""
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    args = sys.argv[1:]
    src = args[0] if args else os.path.join(HERE, "embed_nn.json")
    tsrc = args[1] if len(args) > 1 else os.path.join(HERE, "columns.jsonl")
    out = args[2] if len(args) > 2 else os.path.join(HERE, "embed_read.md")
    d = json.load(open(src, encoding="utf-8"))
    truth = {json.loads(l)["id"]: json.loads(l) for l in open(tsrc, encoding="utf-8")}
    kinds, src_for_wrong, rows = Counter(), Counter(), []
    for t in d["targets"]:
        c = truth[t["id"]]
        tv = Counter(n["teacher"] for n in t["neighbors"])
        top, n = tv.most_common(1)[0]
        m = t["model"]
        if m == c["truth"]:
            k = "0 本体の 1 位はこの形では正しい"
        elif tv[m] >= 5:
            k = "A 近い教材の多く（5 列以上）に本体の答えと同じ種類が付いている＝その教材から覚えた"
            for nb in t["neighbors"]:
                if nb["teacher"] == m:
                    src_for_wrong[nb["src"]] += 1
        elif tv[c["truth"]] >= 5:
            k = "B 近い教材の多くは正解の種類なのに、本体は別の種類と答えた"
        elif tv[m] >= 1:
            k = "C 近い教材は割れていて、本体の答えの種類も混ざる"
        else:
            k = "D 近い教材に本体の答えの種類が 1 つもない"
        kinds[k] += 1
        rows.append((k, t, c, tv))
    L = ["# 本体の中で近い教材の列（`research/unknown/embed_read.py`。もとは `embed_nn.json`）", "",
         f"- {d['note']}。教材 {d['train_rows']} 列、{d['seconds']} 秒", "", "| 分け | 列 |", "|---|---:|"]
    L += [f"| {k} | {n} |" for k, n in sorted(kinds.items())]
    L += ["", "## A の列で、本体の答えと同じ種類が付いていた近い教材の出どころ", "", "| 出どころ | 列（延べ） |", "|---|---:|"]
    L += [f"| {s} | {n} |" for s, n in src_for_wrong.most_common()]
    L += ["", "| 分け | id | 見出し | 正解 | 本体 | 近い 10 列の種類 | いちばん近い 3 列（出どころ・列名・種類・近さ） |", "|---|---|---|---|---|---|---|"]
    for k, t, c, tv in sorted(rows, key=lambda x: x[0]):
        nb = "; ".join(f"{n['src']} {n['header'][:22]}={n['teacher']} {n['sim']}" for n in t["neighbors"][:3]).replace("|", "/")
        L.append(f"| {k[0]} | {t['id']} | {c['header'][:28].replace('|', '/')} | {c['truth']} | {t['model']} | {', '.join(f'{a} {b}' for a, b in tv.most_common(3))} | {nb} |")
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:20]))


if __name__ == "__main__":
    main()
