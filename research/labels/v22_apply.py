"""LABEL_GUIDE v2.2 の付け直し（research/labels/v22_decisions.jsonl の change）を教材に入れる（2026-10-30 Claude）。
- 教材庫（materials/pool/batch_<陣>.jsonl）：ラベルと teacher を直し、manifest の数と SHA-256 を直す（学習が読む）
- 同じ列を work/<陣>/set.json の id で materials/pool/label_review/claude_decisions.jsonl に足す（開発用の採点 pool_bench が読む）
- 英国・業務の表の教材（materials/real_labels*.jsonl）：ラベルと teacher を直す
直す前のラベルが記録と違えば止める（2 回動かしても同じ結果になる：直し済みの行は飛ばす）。
  python research/labels/v22_apply.py [決めたことのファイル（既定 v22_decisions.jsonl）]
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


def locate(rows, d):
    """記録の列の行の番号。行の番号・列名（・表・値）が合えばその行、合わなければ表・列名・値で探す（前に外した行で番号がずれた陣）。"""
    k = d["line"]
    ok = lambda r: r.get("header") == d["header"] and ("table" not in d or r.get("table") == d["table"]) and ("values" not in d or r.get("values") == d["values"])
    if k < len(rows) and ok(rows[k]):
        return k
    if "table" not in d:
        if k < len(rows) and rows[k].get("header") != d["header"]:
            raise SystemExit(f"{d['file']}:{k}：列名が記録と違う")
        return k if k < len(rows) else None
    hits = [i for i, r in enumerate(rows) if ok(r)]
    if len(hits) > 1:
        raise SystemExit(f"{d['file']}:{k}：記録の列に当たる行が {len(hits)} 行")
    return hits[0] if hits else None


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "v22_decisions.jsonl"
    decs = [d for d in read_jsonl(HERE / src) if d["decision"] == "change"]
    by_file = defaultdict(list)
    for d in decs:
        by_file[d["file"]].append(d)
    # 採点の付け直しは後の行が勝つ（pool_bench._relabel）。今の付け直しと違う列だけ足す
    have = {r["id"]: r["label"] for r in read_jsonl(REVIEW) if r["decision"] == "change"}
    review_add, m = [], manifest()
    for name, ds in sorted(by_file.items()):
        path = (POOL if name.startswith("batch_") else ROOT / "materials") / name
        rows = read_jsonl(path)
        changed, drop = 0, set()
        for d in ds:
            k = locate(rows, d)
            if k is None:
                if d["label"] == "unknown":   # 前に動かしたときに外した列
                    continue
                raise SystemExit(f"{name}:{d['line']}：記録の列が見つからない")
            r = rows[k]
            if d["label"] == "unknown":
                # 決められない列は確定した陣に入れない（label_review/apply.py と同じ）。採点の付け直しには unknown として残す
                drop.add(k)
                changed += 1
            elif r["label"] != d["label"]:
                if r["label"] != d["from"]:
                    raise SystemExit(f"{name}:{d['line']}：直す前のラベルが記録と違う（{r['label']}）")
                r["label"], r["teacher"] = d["label"], d["decided_by"]
                changed += 1
            if name.startswith("batch_") and (work(name[len("batch_"):-len(".jsonl")]) / "corpus.jsonl").exists():   # 作業の陣のない教材（jp3）は採点に出ない
                b = name[len("batch_"):-len(".jsonl")]
                w = work(b)
                corpus = read_jsonl(w / "corpus.jsonl")
                ids = [c["id"] for c in json.load(open(w / "set.json", encoding="utf-8"))["columns"]]
                hits = [k for k, c in enumerate(corpus) if c["table"] == r["table"] and c["header"] == r["header"] and c["values"] == r["values"]]
                if len(hits) != 1:
                    raise SystemExit(f"{name}:{d['line']}：作業の corpus の行が {len(hits)} 行当たる")
                sid = ids[hits[0]]
                if have.get(sid) != d["label"]:   # unknown も採点の付け直しに入れる（pool_bench は unknown を採点しない）
                    review_add.append({"id": sid, "decision": "change", "label": d["label"], "reason": d["reason"], "decided_by": d["decided_by"]})
                    have[sid] = d["label"]
        rows = [r for k, r in enumerate(rows) if k not in drop]
        write_jsonl(path, rows)
        if name.startswith("batch_"):
            # manifest は中身から作り直す（途中で止まって直しだけが入った陣も、次に動かしたとき合わせる）
            b = name[len("batch_"):-len(".jsonl")]
            e = next((x for x in m["batches"] if x["batch"] == b), None)
            if e is None:
                print(name, "は manifest にない")
                continue
            if e["sha256"] != sha256(path):
                n = sum(x.get("teacher") == ds[0]["decided_by"] for x in rows)
                e["columns"], e["labels"], e["sha256"] = len(rows), dict(Counter(x["label"] for x in rows)), sha256(path)
                e["note"] = (e.get("note", "") + f"／2026-10-30 LABEL_GUIDE の付け直し（{src}）：{n} 列").lstrip("／")
        print(name, "直した", changed, "（外した", len(drop), "）")
    save_manifest(m)
    with open(REVIEW, "a", encoding="utf-8") as f:
        for x in review_add:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print("採点の付け直しに足した", len(review_add))


if __name__ == "__main__":
    main()
