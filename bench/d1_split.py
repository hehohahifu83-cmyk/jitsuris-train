"""D1 の新しい陣（b066〜b090）を、公開元ごとに「決める陣」と「確かめる陣」に分ける（2026-10-31 Claude）。

事前記録 `bench/d1_prereg_20261030.md`「確かめる陣」：予測を出す前に、公開元の名前の SHA-256 で決める。
決まり：sha256(公開元の名前, UTF-8) の 16 進の値を 2 で割った余りが 0 → decide（決める陣）、1 → confirm（確かめる陣）。
1 つの公開元の列はすべて同じ側に入る（同じ公開元の似た表が両側に分かれない）。ラベル・予測は使わない。

  python bench/d1_split.py [--from 66] [--to 90] [--out bench/d1_split_20261031.md] [--json bench/d1_split_20261031.json]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "bench"))
import d1_counts  # noqa: E402
from d1_counts import NOT_USED, table_lang, work  # noqa: E402


def half(publisher: str) -> str:
    return "decide" if int(hashlib.sha256(publisher.encode("utf-8")).hexdigest(), 16) % 2 == 0 else "confirm"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="lo", type=int, default=66)
    ap.add_argument("--to", dest="hi", type=int, default=90)
    ap.add_argument("--out")
    ap.add_argument("--json")
    a = ap.parse_args(argv)

    count = defaultdict(Counter)   # half → 言語ごとの採点できる列
    pubs = defaultdict(Counter)    # 公開元 → 採点できる列
    for n in range(a.lo, a.hi + 1):
        b = f"b{n:03d}"
        if not (work(b) / "corpus.jsonl").exists():
            continue
        corpus, labels = d1_counts.batch_rows(b)
        tables = defaultdict(list)
        for r, l in zip(corpus, labels):
            tables[r["table"]].append((r, l["label"]))
        for items in tables.values():
            lg = table_lang([r for r, _ in items])
            for r, lab in items:
                p = r.get("publisher") or r.get("source", "?")
                pubs[p][lg] += 0
                if lab in NOT_USED:
                    continue
                count[half(p)][lg] += 1
                pubs[p][lg] += 1

    mapping = {p: half(p) for p in sorted(pubs)}
    out = [f"# D1 の決める陣・確かめる陣の分け方（b{a.lo:03d}〜b{a.hi:03d}）", "",
           "`python bench/d1_split.py` で作った。公開元の名前の SHA-256 を 2 で割った余り 0 → 決める陣、1 → 確かめる陣（予測の前に決めた）。",
           "数は陣ごとの今のラベル（ChatGPT の答え。無い陣は Claude の答え）で、裁定の前。", "",
           "| 側 | 公開元 | 採点できる | en | ja | defr |", "|---|---:|---:|---:|---:|---:|"]
    for h in ("decide", "confirm"):
        c = count[h]
        out.append(f"| {h} | {sum(1 for v in mapping.values() if v == h)} | {sum(c.values())} | {c['en']} | {c['ja']} | {c['defr']} |")
    text = "\n".join(out) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    if a.json:
        Path(a.json).write_text(json.dumps({"rule": "sha256(publisher) % 2: 0 decide, 1 confirm", "batches": [a.lo, a.hi],
                                            "publishers": mapping}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
