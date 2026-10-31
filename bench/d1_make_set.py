"""D1 の決める陣（または確かめる陣）の set を作る（2026-10-31 Claude）。予測の前。ラベルは読まない。

b066〜b090 の各陣の set.json から、公開元（corpus の publisher）が `bench/d1_split_20261031.json` の側に入る列だけをつなぐ。
表の題名の対応（adopted.json の title。学習の materials/pool/titles.json と同じ作り方）も同じフォルダに書く。
  python bench/d1_make_set.py decide materials/pool/work/d1dec
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "materials" / "pool" / "work"
BATCHES = [f"b{n:03d}" for n in range(66, 91) if n != 82]


def read_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def main(argv=None):
    side, out = (argv or sys.argv[1:])[:2]
    assert side in ("decide", "confirm")
    split_path = ROOT / "bench" / "d1_split_20261031.json"
    split = json.loads(split_path.read_text(encoding="utf-8"))["publishers"]
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    cols, titles, sources = [], {}, []
    for b in BATCHES:
        w = WORK / b
        s = json.loads((w / "set.json").read_text(encoding="utf-8"))["columns"]
        corpus = read_jsonl(w / "corpus.jsonl")
        assert len(s) == len(corpus) and all(x["table"] == y["table"] for x, y in zip(s, corpus)), b
        by_url = {a["resource_url"]: a.get("title", "") for a in json.loads((w / "adopted.json").read_text(encoding="utf-8"))["adopted"]}
        n = 0
        for c, r in zip(s, corpus):
            p = r.get("publisher") or r.get("source", "?")
            if split[p] != side:
                continue
            cols.append(c)
            n += 1
            t = by_url.get(r.get("resource_page")) or by_url.get(r["table"]) or ""
            if t:
                titles[r["table"]] = t
        if n:
            sources.append(b)
    doc = {"schema_version": 1, "set_id": f"d1-{side}-20261031", "columns": cols}
    (out / "set.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "titles.json").write_text(json.dumps(titles, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    (out / "sources.json").write_text(json.dumps({"sources": sources, "side": side,
                                                   "split_sha256": hashlib.sha256(split_path.read_bytes()).hexdigest()}, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{side}: {len(cols)} columns from {len(sources)} batches, {len(titles)} titled tables")


if __name__ == "__main__":
    main()
