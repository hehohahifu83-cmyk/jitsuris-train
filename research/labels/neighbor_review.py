"""陣・出どころをまたいだ近い教材の列の見直し（2026-10-30 Claude。懸念点 4・原因 4）。
本体が誤った列（言い切って誤った 175 列 research/fixes/embed_wrong.json、不明の M11 73 列 research/unknown/embed_nn.json）ごとに、
本体の中で近い教材の列のうち本体の誤った答えと同じ種類が付いた列（誤りを教えた列）を上位 3 列まで並べる。
Claude が誤った列ごとに「教材の付け方が v2.2 と違う（付け直す）」か「意味が違う列で教材は正しい」かを決める（neighbor_decisions.jsonl）。
  python research/labels/neighbor_review.py   → neighbor_review.md
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


def flat(v, n=40):
    return " ".join(str(v).split())[:n]


def main():
    truth = {}
    for l in open(os.path.join(ROOT, "research", "fixes", "wrong.jsonl"), encoding="utf-8"):
        r = json.loads(l)
        truth[r["id"]] = (r["truth"], r["header"], r.get("values5", []))
    for l in open(os.path.join(ROOT, "research", "unknown", "root_cause.jsonl"), encoding="utf-8"):
        r = json.loads(l)
        truth.setdefault(r["id"], (r["truth"], r["header"], r.get("values5", [])))
    ts = json.load(open(os.path.join(ROOT, "research", "fixes", "embed_wrong.json"), encoding="utf-8"))["targets"] + \
        json.load(open(os.path.join(ROOT, "research", "unknown", "embed_nn.json"), encoding="utf-8"))["targets"]
    seen, rows = set(), []
    for t in ts:
        if t["id"] in seen:
            continue
        seen.add(t["id"])
        tr, h, v = truth[t["id"]]
        teach = [n for n in t["neighbors"] if n["teacher"] == t["model"]][:3]
        rows.append((f"{tr}→{t['model']}", t["id"], h, v, teach))
    rows.sort(key=lambda x: (x[0], x[2]))
    L = ["# 近い教材の列の見直し（誤った列ごとに、誤りを教えた近い教材の列を上位 3 列）", "", "形式：正解→本体の答え｜誤った列｜その値 ／ 教材の列（出どころ・付けた種類・近さ）", ""]
    cur = None
    for k, (pair, i, h, v, teach) in enumerate(rows):
        if pair != cur:
            L += ["", f"## {pair}", ""]
            cur = pair
        L.append(f"- R{k + 1:03d} {i}「{flat(h)}」: {' / '.join(flat(x, 18) for x in v[:5])}")
        for n in teach:
            L.append(f"    - {n['src']}「{flat(n['header'])}」{n['teacher']} {n['sim']:.2f}: {' / '.join(flat(x, 18) for x in n['values'][:4])}")
    open(os.path.join(HERE, "neighbor_review.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(len(rows), "列")


if __name__ == "__main__":
    main()
