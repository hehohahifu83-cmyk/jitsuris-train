"""新しい評価の陣 E3（b112〜b123）を固定する（2026-11-01 Claude。ラベル・予測の前に決めて固定する。事前記録 bench/hfix_prereg_20261101.md）。
規則：b112〜b123 の列のうち、表（table の URL）が前の陣（b001〜b111）に一度でも出たものは外す。残りを全部 E3 にする。
ラベルも列の値も読まない（表の URL・公開元・言語・列の数だけ）。
  python bench/e3_split.py split                          → bench/e3_split_20261101.json（一度書いたら上書きしない）
  python bench/e3_split.py make materials/pool/work/e3     → set.json・titles.json・sources.json
"""
from __future__ import annotations

import collections
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "materials" / "pool" / "work"
SPLIT = ROOT / "bench" / "e3_split_20261101.json"
E3_BATCHES = [f"b{n:03d}" for n in range(112, 124)]


def read_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def seen_tables():
    seen = set()
    for n in range(1, 112):
        p = WORK / f"b{n:03d}" / "corpus.jsonl"
        if p.exists():
            seen |= {r["table"] for r in read_jsonl(p)}
    return seen


def split():
    if SPLIT.exists():
        raise SystemExit(f"{SPLIT} はもうある（上書きしない）")
    bs = [b for b in E3_BATCHES if (WORK / b / "corpus.jsonl").exists()]
    missing = [b for b in E3_BATCHES if b not in bs]
    seen = seen_tables()
    dropped, kept, count, pubs = set(), set(), collections.Counter(), collections.Counter()
    for b in bs:
        for r in read_jsonl(WORK / b / "corpus.jsonl"):
            if r["table"] in seen:
                dropped.add(r["table"]); continue
            kept.add(r["table"])
            count[r.get("language", "?")] += 1
            pubs[r.get("publisher") or r.get("source", "?")] += 1
    doc = {"rule": "b112-b123, tables already in b001-b111 excluded", "batches": bs, "missing_batches": missing,
           "dropped_tables": sorted(dropped), "tables": len(kept), "columns": dict(sorted(count.items())),
           "publishers": dict(sorted(pubs.items()))}
    SPLIT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("E3", sum(count.values()), dict(count), "tables", len(kept), "dropped", len(dropped), "missing", missing)


def make(out):
    doc = json.loads(SPLIT.read_text(encoding="utf-8"))
    drop = set(doc["dropped_tables"])
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
            if r["table"] in drop:
                continue
            cols.append(c)
            n += 1
            t = by_url.get(r.get("resource_page")) or by_url.get(r["table"]) or ""
            if t:
                titles[r["table"]] = t
        if n:
            sources.append(b)
    (out / "set.json").write_text(json.dumps({"schema_version": 1, "set_id": "E3-20261101", "columns": cols}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "titles.json").write_text(json.dumps(titles, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    (out / "sources.json").write_text(json.dumps({"sources": sources, "side": "E3", "split_sha256": hashlib.sha256(SPLIT.read_bytes()).hexdigest()},
                                                 ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"E3: {len(cols)} columns from {len(sources)} batches, {len(titles)} titled tables")


if __name__ == "__main__":
    a = sys.argv[1:]
    split() if a[0] == "split" else make(a[1])
