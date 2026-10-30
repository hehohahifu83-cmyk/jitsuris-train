"""割れている組の見直し：ChatGPT の答え（answers/split_NNN.tsv）を、組（split_groups.jsonl）の列と突き合わせる（2026-10-30 Claude）。
  python research/labels/split_review.py   → split_review.md（今のラベルから変えた列の全部と、変えなかった列の抜き取り 40 列）
"""
import csv
import glob
import hashlib
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def flat(v, n=60):
    return " ".join(str(v).split())[:n]


def load():
    gs = {g["gid"]: g for g in (json.loads(l) for l in open(os.path.join(HERE, "split_groups.jsonl"), encoding="utf-8"))}
    out = []
    for p in sorted(glob.glob(os.path.join(HERE, "answers", "split_*.tsv"))):
        for r in csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"):
            g = gs[r["gid"]]
            c = g["columns"][int(r["col"]) - 1]
            out.append({"gid": r["gid"], "col": int(r["col"]), "batch": g["batch"], "header": g["header"], "line": c["line"], "now": c["label"],
                        "chatgpt": r["label"].strip(), "reason": r.get("reason", ""), "values": c["values"], "context": c["context"],
                        "group": g["labels"], "table": c["table"]})
    return out


def main():
    rows = load()
    changed = [r for r in rows if r["chatgpt"] != r["now"]]
    same = sorted([r for r in rows if r["chatgpt"] == r["now"]], key=lambda r: hashlib.sha256(f"{r['gid']}-{r['col']}".encode()).hexdigest())[:40]
    L = [f"# 割れている組の見直し：裁定（答え {len(rows)} 列・変えた {len(changed)} 列）", "", f"変えた先：{dict(Counter(r['chatgpt'] for r in changed))}", ""]
    for title, rs in (("変えた列", changed), ("変えなかった列の抜き取り", same)):
        L += [f"## {title}", ""]
        for k, r in enumerate(rs, 1):
            L.append(f"- {'C' if title == '変えた列' else 'K'}{k:03d} {r['gid']} {r['batch']}「{flat(r['header'], 30)}」組 {r['group']}：{r['now']} → **{r['chatgpt']}**")
            L.append(f"    - 値：{' / '.join(flat(v, 22) for v in r['values'][:6])}　同じ表：{'・'.join(flat(x, 14) for x in r['context'][:6])}")
            L.append(f"    - 理由：{flat(r['reason'], 120)}")
    open(os.path.join(HERE, "split_review.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(len(rows), len(changed))


if __name__ == "__main__":
    main()
