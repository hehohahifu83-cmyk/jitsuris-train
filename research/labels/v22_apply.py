"""LABEL_GUIDE v2.2 の付け直し（research/labels/v22_decisions.jsonl の change）を教材に入れる（2026-10-30 Claude）。
- 教材庫（materials/pool/batch_<陣>.jsonl）：ラベルと teacher を直し、manifest の数と SHA-256 を直す（学習が読む）
- 同じ列を work/<陣>/set.json の id で materials/pool/label_review/claude_decisions.jsonl に足す（開発用の採点 pool_bench が読む）
- 英国・業務の表の教材（materials/real_labels*.jsonl）：ラベルと teacher を直す
直す前のラベルが記録と違えば止める（2 回動かしても同じ結果になる：直し済みの行は飛ばす）。
  python research/labels/v22_apply.py
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "materials"))
from pipeline import POOL, manifest, read_jsonl, save_manifest, sha256, work, write_jsonl  # noqa: E402

HERE = Path(__file__).resolve().parent
REVIEW = ROOT / "materials" / "pool" / "label_review" / "claude_decisions.jsonl"


def main():
    decs = [d for d in read_jsonl(HERE / "v22_decisions.jsonl") if d["decision"] == "change"]
    by_file = defaultdict(list)
    for d in decs:
        by_file[d["file"]].append(d)
    # 採点の付け直しは後の行が勝つ（pool_bench._relabel）。今の付け直しと違う列だけ足す
    have = {r["id"]: r["label"] for r in read_jsonl(REVIEW) if r["decision"] == "change"}
    review_add, m = [], manifest()
    for name, ds in sorted(by_file.items()):
        path = (POOL if name.startswith("batch_") else ROOT / "materials") / name
        rows = read_jsonl(path)
        changed = 0
        for d in ds:
            r = rows[d["line"]]
            if r.get("header") != d["header"]:
                raise SystemExit(f"{name}:{d['line']}：列名が記録と違う")
            if r["label"] != d["label"]:
                if r["label"] != d["from"]:
                    raise SystemExit(f"{name}:{d['line']}：直す前のラベルが記録と違う（{r['label']}）")
                r["label"], r["teacher"] = d["label"], d["decided_by"]
                changed += 1
            if name.startswith("batch_"):
                b = name[len("batch_"):-len(".jsonl")]
                w = work(b)
                corpus = read_jsonl(w / "corpus.jsonl")
                ids = [c["id"] for c in json.load(open(w / "set.json", encoding="utf-8"))["columns"]]
                hits = [k for k, c in enumerate(corpus) if c["table"] == r["table"] and c["header"] == r["header"] and c["values"] == r["values"]]
                if len(hits) != 1:
                    raise SystemExit(f"{name}:{d['line']}：作業の corpus の行が {len(hits)} 行当たる")
                sid = ids[hits[0]]
                if have.get(sid) != d["label"]:
                    review_add.append({"id": sid, "decision": "change", "label": d["label"], "reason": d["reason"], "decided_by": d["decided_by"]})
                    have[sid] = d["label"]
        write_jsonl(path, rows)
        if name.startswith("batch_") and changed:
            b = name[len("batch_"):-len(".jsonl")]
            e = next(x for x in m["batches"] if x["batch"] == b)
            e["labels"], e["sha256"] = dict(Counter(x["label"] for x in rows)), sha256(path)
            e["note"] = (e.get("note", "") + f"／2026-10-30 LABEL_GUIDE v2.2 の付け直し：{changed} 列").lstrip("／")
        print(name, "直した", changed)
    save_manifest(m)
    with open(REVIEW, "a", encoding="utf-8") as f:
        for x in review_add:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print("採点の付け直しに足した", len(review_add))


if __name__ == "__main__":
    main()
