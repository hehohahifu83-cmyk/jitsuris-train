"""D1 の b066〜b083 の ChatGPT のラベルの抜き取り（2026-10-31 Claude。事前記録 d1_prereg_20261030.md の追記）。

  python research/d1_audit.py make    # 各陣のグループの 10%（少なくとも 10）を選び、答えを伏せたシートを research/d1_audit/ に書く
  python research/d1_audit.py compare # research/d1_audit/answers_bNNN.tsv（Claude）と ChatGPT の答えを比べる

選び方：random.Random("d1-audit|bNNN") でグループを選ぶ（ラベル・予測は見ない）。
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
import label_sheets  # noqa: E402
from pipeline import read_jsonl, work  # noqa: E402

OUT = ROOT / "research" / "d1_audit"
# b083 は Claude が ChatGPT の答えを見て全部確かめ済み（2026-10-31 11:05）なので抜き取りに入れない
BATCHES = [f"b{n:03d}" for n in range(66, 82)]
RATE, MIN = 0.10, 10


def sample(batch):
    groups = json.loads((work(batch) / "sheets" / "groups.json").read_text(encoding="utf-8"))["groups"]
    k = min(len(groups), max(MIN, round(len(groups) * RATE)))
    return groups, sorted(random.Random(f"d1-audit|{batch}").sample(range(len(groups)), k))


def cmd_make(_a):
    OUT.mkdir(parents=True, exist_ok=True)
    for b in BATCHES:
        groups, idx = sample(b)
        corpus = read_jsonl(work(b) / "corpus.jsonl")
        chosen = [groups[i] for i in idx]
        text = label_sheets.render_sheet(1, chosen, corpus, 1, "v2.3").replace(
            f"`answers/sheet_001.tsv`", f"`research/d1_audit/answers_{b}.tsv`")
        (OUT / f"sample_{b}.md").write_text(f"<!-- {b}：{len(chosen)}/{len(groups)} グループ -->\n" + text, encoding="utf-8")
        print(b, len(chosen), "/", len(groups))


def cmd_compare(_a):
    total = wrong = 0
    lines = ["# D1 の抜き取り：ChatGPT と Claude の比べ（b066〜b083）", "", "| 陣 | 抜き取り | 一致 | 食い違い |", "|---|---:|---:|---:|"]
    diffs = []
    for b in BATCHES:
        groups, idx = sample(b)
        f = OUT / f"answers_{b}.tsv"
        if not f.exists():
            continue
        d = work(b) / "sheets"
        gpt, p1 = label_sheets.read_answers(d, groups, "chatgpt")
        mine = dict(l.split("\t") for l in f.read_text(encoding="utf-8").split("\n") if "\t" in l)
        mine = {k: v.strip() for k, v in mine.items() if v.strip()}
        ids = [groups[i]["group"] for i in idx]
        miss = [g for g in ids if g not in mine]
        if miss or p1:
            raise SystemExit(f"{b}: 答えが足りない {miss[:5]} {p1[:2]}")
        dis = [(g, gpt.get(g), mine[g]) for g in ids if gpt.get(g) != mine[g]]
        total += len(ids); wrong += len(dis)
        lines.append(f"| {b} | {len(ids)} | {len(ids) - len(dis)} | {len(dis)} |")
        diffs += [(b, *x) for x in dis]
    lines.append(f"| 計 | {total} | {total - wrong} | {wrong} |")
    lines += ["", "| 陣 | グループ | ChatGPT | Claude |", "|---|---|---|---|"] + [f"| {b} | {g} | {x} | {y} |" for b, g, x, y in diffs]
    text = "\n".join(lines) + "\n"
    (OUT / "compare.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["make", "compare"])
    a = ap.parse_args()
    {"make": cmd_make, "compare": cmd_compare}[a.cmd](a)
