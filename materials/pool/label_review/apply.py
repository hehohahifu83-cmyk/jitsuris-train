"""ラベルの掃除（強化案 B6）の Claude の裁定を教材庫に反映する（2026-10-25 Claude）。

- 入力：claude_decisions.jsonl（id・decision・label・reason）。id は work/<陣>/set.json の列の id
- 確定した陣（batch_<陣>.jsonl）：change は label を直し teacher を decided_by に、unknown は行を外す（確定した陣に unknown は入れない決まり）
- manifest.json の列数・種類の数・SHA-256 を直し、note に記録する
- 開発用の採点（pool_bench.load_batch）は同じファイルを読んで truth を差し替える（ここでは触らない）
使い方：python materials/pool/label_review/apply.py
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "materials"))
from pipeline import POOL, manifest, read_jsonl, save_manifest, sha256, work, write_jsonl  # noqa: E402

DEC = Path(__file__).with_name("claude_decisions.jsonl")


def main():
    by_batch = defaultdict(list)
    for d in read_jsonl(DEC):
        if d["decision"] == "change":
            by_batch[d["id"].split("-")[0]].append(d)
    m = manifest()
    for b, ds in sorted(by_batch.items()):
        w = work(b)
        corpus = read_jsonl(w / "corpus.jsonl")
        ids = [c["id"] for c in json.load(open(w / "set.json", encoding="utf-8"))["columns"]]
        rows = read_jsonl(POOL / f"batch_{b}.jsonl")
        drop, changed = set(), 0
        for d in ds:
            c = corpus[ids.index(d["id"])]
            hits = [k for k, r in enumerate(rows) if r["table"] == c["table"] and r["header"] == c["header"] and r["values"] == c["values"]]
            if len(hits) != 1:
                raise SystemExit(f"{d['id']}: 確定した陣の行が {len(hits)} 行当たる")
            k = hits[0]
            if d["label"] == "unknown":
                drop.add(k)
            else:
                rows[k]["label"], rows[k]["teacher"] = d["label"], d["decided_by"]
                changed += 1
        rows = [r for k, r in enumerate(rows) if k not in drop]
        write_jsonl(POOL / f"batch_{b}.jsonl", rows)
        e = next(x for x in m["batches"] if x["batch"] == b)
        e["columns"], e["labels"], e["sha256"] = len(rows), dict(Counter(r["label"] for r in rows)), sha256(POOL / f"batch_{b}.jsonl")
        e["note"] = (e.get("note", "") + f"／2026-10-25 ラベルの掃除（label_review）：直した {changed}・外した {len(drop)}").lstrip("／")
        print(b, "直した", changed, "外した", len(drop), "→", len(rows), "列")
    save_manifest(m)


if __name__ == "__main__":
    main()
