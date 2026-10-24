"""公開データの教材から個人名を消す（2026-10-24 Claude）。

公開データの表でも、人の名前（施設の管理者・営業者・議員など）が入った列は教材庫に入れない（materials/pool/README.md「守ること」）。
取り出しの段の列名の検査をすり抜けたものを、ラベル（先生・裁定・モデルのどれかが person）で見つけて消す。
- 確定した陣（batch_*.jsonl）：person の行を取り除き、manifest.json の列数・種類・SHA-256 を直す
- 作業の置き場（work/<陣>/corpus.jsonl・set.json・sheets/*.md）：行は残して値だけを消す（行の番号・ラベルとの対応を崩さない）
- 消したものは materials/pool/redactions.json に記録する（値は書かない）

使い方：python materials/redact_person.py [--batches b003 b004 b006]
git の履歴には残るので、履歴から消すかはオーナーが決める。
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
from pipeline import POOL, manifest, read_jsonl, save_manifest, sha256, work, write_jsonl  # noqa: E402

MARK = "［個人名のため削除］"


def person_rows(w):
    """作業の置き場で、先生・裁定・モデルのどれかが person の行の番号。"""
    rows = set()
    if (w / "labels_chatgpt.jsonl").exists():
        rows |= {i for i, x in enumerate(read_jsonl(w / "labels_chatgpt.jsonl")) if x.get("label") == "person"}
    if (w / "decisions.jsonl").exists():
        rows |= {d["i"] for d in read_jsonl(w / "decisions.jsonl") if d.get("label") == "person"}
    if (w / "pred_e5base_seed1.json").exists() and (w / "set.json").exists():
        cols = json.loads((w / "set.json").read_text(encoding="utf-8"))["columns"]
        by = {r["id"]: r for r in json.loads((w / "pred_e5base_seed1.json").read_text(encoding="utf-8"))["rows"]}
        rows |= {i for i, c in enumerate(cols) if by.get(c["id"], {}).get("guarded_prediction") == "person"}
    return sorted(rows)


def redact_work(batch):
    w = work(batch)
    if not (w / "corpus.jsonl").exists():
        return []
    corpus = read_jsonl(w / "corpus.jsonl")
    rows = person_rows(w)
    secrets = set()
    for i in rows:
        c = corpus[i]
        secrets |= {str(v) for v in c.get("values", []) + c.get("row_values", []) if str(v).strip() and str(v) != MARK}
        c["values"] = [MARK] * len(c.get("values", []))
        if "row_values" in c:
            c["row_values"] = [MARK] * len(c["row_values"])
        c["redacted"] = "person"
    if rows:
        write_jsonl(w / "corpus.jsonl", corpus)
        p = w / "set.json"
        if p.exists():
            s = json.loads(p.read_text(encoding="utf-8"))
            for i in rows:
                s["columns"][i]["values"] = [MARK] * len(s["columns"][i].get("values", []))
            p.write_text(json.dumps(s, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
        for md in sorted((w / "sheets").glob("sheet_*.md")) if (w / "sheets").exists() else []:
            t = md.read_text(encoding="utf-8")
            t2 = t
            for v in sorted(secrets, key=len, reverse=True):
                for form in {v, v[:40], v[:39] + "…"}:
                    if len(form) >= 2:
                        t2 = t2.replace(form, MARK)
            if t2 != t:
                md.write_text(t2, encoding="utf-8")
    return [{"batch": batch, "where": "work", "row": i, "table": corpus[i]["table"], "header": corpus[i]["header"]} for i in rows]


def redact_batch(batch, m):
    f = POOL / f"batch_{batch}.jsonl"
    if not f.exists():
        return []
    rows = read_jsonl(f)
    keep = [r for r in rows if r.get("label") != "person"]
    gone = [r for r in rows if r.get("label") == "person"]
    if not gone:
        return []
    write_jsonl(f, keep)
    for b in m["batches"]:
        if b["batch"] == batch:
            b["columns"] = len(keep)
            b["labels"] = dict(Counter(r["label"] for r in keep))
            b["sha256"] = sha256(f)
            b["redacted_person"] = b.get("redacted_person", 0) + len(gone)
    return [{"batch": batch, "where": "pool", "table": r["table"], "header": r["header"]} for r in gone]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches", nargs="+", default=[p.name[len("batch_"):-len(".jsonl")] for p in sorted(POOL.glob("batch_*.jsonl"))])
    a = ap.parse_args(argv)
    m = manifest()
    done = []
    for b in a.batches:
        done += redact_batch(b, m)
        done += redact_work(b)
    save_manifest(m)
    log_path = POOL / "redactions.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {"note": "個人名のため消した列（値は書かない）", "items": []}
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    log["items"] += [dict(x, redacted_utc=now, reason="person") for x in done]
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"消した：教材庫 {sum(1 for x in done if x['where'] == 'pool')} 行、作業の置き場 {sum(1 for x in done if x['where'] == 'work')} 行")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
