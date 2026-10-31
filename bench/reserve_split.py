"""在庫（b091〜）を公開元の単位で E1・E2・E3 に分ける（2026-11-01 Claude。ラベル・予測の前に決めて固定する）。
ChatGPT（2026-11-01）：「14陣を開く前に、表・公開元を単位としてE1–E3の割当を固定し、同じ表・公開元を別セットへ分けないで」。
規則：sha256("jitsuris-reserve-v1|" + 公開元) を 3 で割った余り 0→E1、1→E2、2→E3。ラベルも列の値も読まない（公開元・言語・列の数だけ）。
  python bench/reserve_split.py split        → bench/reserve_split_20261101.json（一度書いたら上書きしない）
  python bench/reserve_split.py make E1 materials/pool/work/e1   → set.json・titles.json・sources.json
"""
from __future__ import annotations

import collections
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "materials" / "pool" / "work"
SPLIT = ROOT / "bench" / "reserve_split_20261101.json"
SALT = "jitsuris-reserve-v1|"


def batches():
    req = [l.split()[0] for l in open(ROOT / "materials" / "pool" / "auto_multi.request", encoding="utf-8")][1:]
    return [f"b{n:03d}" for n in range(91, 200) if (WORK / f"b{n:03d}" / "corpus.jsonl").exists() and f"b{n:03d}" not in req]


def read_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def side_of(pub):
    return "E" + str(int(hashlib.sha256((SALT + pub).encode("utf-8")).hexdigest(), 16) % 3 + 1)


def split():
    if SPLIT.exists():
        raise SystemExit(f"{SPLIT} はもうある（上書きしない）")
    bs = batches()
    pubs, count = {}, collections.Counter()
    for b in bs:
        for r in read_jsonl(WORK / b / "corpus.jsonl"):
            p = r.get("publisher") or r.get("source", "?")
            pubs[p] = side_of(p)
            count[(pubs[p], r.get("language", "?"))] += 1
    doc = {"rule": "sha256('jitsuris-reserve-v1|' + publisher) % 3: 0 E1, 1 E2, 2 E3", "batches": bs, "publishers": dict(sorted(pubs.items())),
           "columns": {f"{s}/{lang}": n for (s, lang), n in sorted(count.items())}}
    SPLIT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for s in ("E1", "E2", "E3"):
        print(s, sum(n for (x, _), n in count.items() if x == s), {lang: n for (x, lang), n in count.items() if x == s})


def make(side, out):
    doc = json.loads(SPLIT.read_text(encoding="utf-8"))
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    cols, titles, sources = [], {}, []
    for b in doc["batches"]:
        w = WORK / b
        s = json.loads((w / "set.json").read_text(encoding="utf-8"))["columns"]
        corpus = read_jsonl(w / "corpus.jsonl")
        assert len(s) == len(corpus) and all(x["table"] == y["table"] for x, y in zip(s, corpus)), b
        by_url = {a["resource_url"]: a.get("title", "") for a in json.loads((w / "adopted.json").read_text(encoding="utf-8"))["adopted"]}
        n = 0
        for c, r in zip(s, corpus):
            if doc["publishers"][r.get("publisher") or r.get("source", "?")] != side:
                continue
            cols.append(c)
            n += 1
            t = by_url.get(r.get("resource_page")) or by_url.get(r["table"]) or ""
            if t:
                titles[r["table"]] = t
        if n:
            sources.append(b)
    (out / "set.json").write_text(json.dumps({"schema_version": 1, "set_id": f"reserve-{side}-20261101", "columns": cols}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "titles.json").write_text(json.dumps(titles, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    (out / "sources.json").write_text(json.dumps({"sources": sources, "side": side, "split_sha256": hashlib.sha256(SPLIT.read_bytes()).hexdigest()},
                                                 ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{side}: {len(cols)} columns from {len(sources)} batches, {len(titles)} titled tables")


if __name__ == "__main__":
    a = sys.argv[1:]
    split() if a[0] == "split" else make(a[1], a[2])
