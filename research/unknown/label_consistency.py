"""教材の付け方の食い違いを探す（2026-10-29 Claude。原因の切り分けの続き）。
不明・重大になった列（columns.jsonl・misses.jsonl）の見出しの語ごとに、本体 C2 の学習の教材（b001〜b014）で同じ語を持つ列の種類と、
誰が決めたか（ChatGPT の初めのラベルのまま／Claude の裁定で変えた）・裁定の理由を並べる。
例：kWh の列は b005・b014 の裁定で quantity、b011 の裁定で「電力は測定値」として other（LABEL_GUIDE に電力の語はない）。
出力：research/unknown/label_consistency.md
使い方：python research/unknown/label_consistency.py
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
import pool_bench as B  # noqa: E402
import verifier_eval as E  # noqa: E402

TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))
STOP = {"the", "and", "for", "von", "der", "die", "des", "und", "per", "pro", "total", "all", "with", "from", "par", "les", "aux", "nach", "bis", "year", "sum"}


def tokens(h):
    h = re.sub(r"([a-z])([A-Z])", r"\1 \2", str(h or ""))
    return {t for t in re.split(r"[^0-9A-Za-zÀ-ÿ一-龥ぁ-んァ-ン]+", h.lower()) if len(t) >= 3 and not t.isdigit() and t not in STOP}


def main():
    train = []
    for b in TRAIN:
        w = B.WORK / b
        first = B.read_jsonl(w / "labels_chatgpt.jsonl")
        dec = {d["i"]: d for d in B.read_jsonl(w / "decisions.jsonl")}
        for c in E.load_batch(b):
            if not c.get("truth"):
                continue
            d = dec.get(c["i"], {})
            train.append({"b": b, "header": c["header"], "truth": c["truth"], "first": first[c["i"]].get("label"), "reason": d.get("reason", ""), "tok": tokens(c["header"])})
    by_tok = defaultdict(list)
    for t in train:
        for k in t["tok"]:
            by_tok[k].append(t)
    targets = [json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")]
    targets += [json.loads(l) for l in open(os.path.join(HERE, "misses.jsonl"), encoding="utf-8")]
    tok_new = defaultdict(Counter)
    for c in targets:
        for k in tokens(c["header"]):
            tok_new[k][c["truth"]] += 1
    L = ["# 教材の付け方の食い違い（`research/unknown/label_consistency.py`）", "",
         "- 不明・重大の列（新しい陣 8 つ、366 列）の見出しの語ごとに、本体 C2 の学習の教材（b001〜b014）で同じ語を持つ列の種類を並べた",
         "- **新しい陣と違う**＝教材でいちばん多い種類が、新しい陣の正解でいちばん多い種類と違う。**教材の中で割れる**＝教材で 2 つ以上の種類がそれぞれ 2 列以上かつ 2 番目が 20% 以上",
         "- 「裁定で変えた」＝ChatGPT の初めのラベルと確定の種類が違う（Claude の裁定・ラベルの掃除）", "",
         "| 語 | 新しい陣の正解 | 教材の種類 | 判定 | 教材で裁定で変えた例（初め→確定：理由） |", "|---|---|---|---|---|"]
    rows = []
    for k, new in tok_new.items():
        tr = by_tok.get(k, [])
        if len(tr) < 3:
            continue
        tc = Counter(t["truth"] for t in tr)
        top_new, top_tr = new.most_common(1)[0][0], tc.most_common(1)[0][0]
        split = len([1 for _, n in tc.items() if n >= 2]) >= 2 and tc.most_common(2)[1][1] / len(tr) >= 0.2
        flag = []
        if top_new != top_tr:
            flag.append("新しい陣と違う")
        if split:
            flag.append("教材の中で割れる")
        if not flag:
            continue
        changed = [t for t in tr if t["first"] and t["first"] != t["truth"]]
        ex = "; ".join(f"{t['b']} {str(t['header'])[:30]}：{t['first']}→{t['truth']}（{t['reason'][:40]}）" for t in changed[:3])
        rows.append((sum(new.values()), k, new, tc, flag, ex))
    for n, k, new, tc, flag, ex in sorted(rows, key=lambda x: -x[0]):
        L.append(f"| {k} | {', '.join(f'{a} {b}' for a, b in new.most_common(3))} | {', '.join(f'{a} {b}' for a, b in tc.most_common(4))} | {'・'.join(flag)} | {ex.replace('|', '/')} |")
    open(os.path.join(HERE, "label_consistency.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
