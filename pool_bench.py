"""教材庫を「学習し直さずに道具の効き目を測る場」にする（2026-10-24 Claude。オーナー指示「ジツリスの学習力の向上」）。

なぜ使えるか：今のモデル（E5-base 種子 1、重み 38c5b344…）は教材庫ができる前に学習したので、教材庫の列は見ていない。
教材庫の各陣には、そのモデルの予測（pred_e5base_seed1.json）と、ChatGPT のラベル・Claude の裁定で決めた正解がある。

正解の決め方（work/<陣>/ のファイルから）：
- Claude が裁定した列（decisions.jsonl、抜き取りを含む）→ 裁定のラベル
- 先生とモデルが一致した列 → 先生のラベル
- 裁定しきれずに捨てた列（review.jsonl の dropped）→ 使わない（難しい列が少し抜けるので、正解率は実際より少し高めに出る）
- unknown・S → 正解が決められない列として別に数える

道具：
- infer：何通りかの「見方」（値の選び方・同じ表の列の並び）でモデルを回し、全部の確率を保存する（推論だけ。学習しない）
- 採点・比べ方は pool_tools.py
未見セット（blind_set*）・封印セット・独立主セットは読まない。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORK = ROOT / "materials" / "pool" / "work"
BENCH_BATCHES = ("b006", "b007", "b008", "b009", "b010", "b011")
JUNK = {"nan", "None", "", "NaN", "null", "NULL"}
NOT_USED = {"unknown", "S"}


def read_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def load_batch(batch: str) -> list[dict]:
    """陣の列を corpus の順に返す。各列：table・header・values（全部）・context・unit・pred（今のモデル）・truth・adjudicated。"""
    w = WORK / batch
    corpus = read_jsonl(w / "corpus.jsonl")
    labels = read_jsonl(w / "labels_chatgpt.jsonl")
    review = {r["i"]: r for r in read_jsonl(w / "review.jsonl")}
    dec = {d["i"]: d for d in read_jsonl(w / "decisions.jsonl")}
    sets = json.load(open(w / "set.json", encoding="utf-8"))["columns"]
    pred = json.load(open(w / "pred_e5base_seed1.json", encoding="utf-8"))
    if not (len(corpus) == len(labels) == len(sets) == len(pred["rows"])):
        raise ValueError(f"{batch}: corpus・ラベル・set・予測の行数が違う")
    out = []
    for i, (c, l, s, p) in enumerate(zip(corpus, labels, sets, pred["rows"])):
        if c["table"] != l["table"] or c["header"] != l["header"] or s["id"] != p["id"]:
            raise ValueError(f"{batch}: {i} 行目の対応がずれている")
        kind = review.get(i, {}).get("kind")
        if kind == "dropped":
            truth, adj = None, False
        elif i in dec:
            truth, adj = dec[i]["label"], kind == "to_review"
        else:
            truth, adj = l["label"], False
        vals = [str(v) for v in (c.get("row_values") or c["values"]) if str(v).strip() not in JUNK] or [str(v) for v in s["values"]]
        out.append({"batch": batch, "i": i, "id": s["id"], "table": c["table"], "header": str(c["header"]),
                    "values5": [str(v) for v in s["values"]], "values": vals, "context": [str(x) for x in s.get("siblings") or []],
                    "unit": str(s.get("unit") or ""), "language": c.get("language", ""), "truth": truth, "adjudicated": adj,
                    "teacher": l["label"], "pred": p["guarded_prediction"], "top3": p["top3"]})
    return out


def load_bench(batches=BENCH_BATCHES) -> list[dict]:
    rows = []
    for b in batches:
        rows += load_batch(b)
    return rows


def _rng(salt: str, key: str) -> random.Random:
    return random.Random(int(hashlib.sha256(f"{salt}:{key}".encode("utf-8")).hexdigest()[:16], 16))


def views(col: dict, n: int, salt: str = "jitsuris-tta-v1") -> list[tuple]:
    """1 列の n 通りの見方（行の形は学習と同じ (見出し, 値, ラベル, 同じ表の列, 単位)）。
    0 番目は今の予測と同じ入力（set の 5 値・同じ表の列の順のまま）。1 番目からは、取り出した値（最大 20）から 5 つを選び直し、同じ表の列の順も混ぜる。
    選び方は列の id と番号の SHA-256 だけで決める（毎回同じ）。"""
    base = (col["header"], list(col["values5"]), "", list(col["context"]), col["unit"])
    out = [base]
    vals = col["values"]
    for k in range(1, n):
        r = _rng(salt, f"{col['batch']}:{col['id']}:{k}")
        mode = k % 3
        if mode == 1 and len(vals) > 5:
            vs = r.sample(vals, 5)
        elif mode == 2:
            seen, vs = set(), []
            pool = list(vals); r.shuffle(pool)
            for v in pool:
                if v not in seen:
                    seen.add(v); vs.append(v)
            vs = vs[:5]
        else:
            vs = r.sample(vals, min(5, len(vals))) if vals else list(col["values5"])
        ctx = list(col["context"]); r.shuffle(ctx)
        out.append((col["header"], vs or list(col["values5"]), "", ctx, col["unit"]))
    return out


def infer(batches, n_views, checkpoint, out_path, device="cpu", limit=None):
    """全部の列 × n_views の確率を出して npz に保存する（float16）。推論だけで、重みは変えない。"""
    import numpy as np
    sys.path.insert(0, str(ROOT))
    import evaluate_independent as EI
    info = EI.checkpoint_info(checkpoint)
    cols = load_bench(batches)
    if limit:
        cols = cols[:limit]
    texts = []
    for c in cols:
        texts += EI.texts_of(views(c, n_views), info)
    probs, seconds = EI.infer_torch(checkpoint, texts, info, device)
    P = probs.reshape(len(cols), n_views, -1).astype("float16")
    np.savez_compressed(out_path, probs=P, ids=np.array([f"{c['batch']}:{c['id']}" for c in cols]), labels=np.array(info["labels"]))
    meta = {"batches": list(batches), "views": n_views, "columns": len(cols), "seconds": round(seconds, 1),
            "weights_sha256": info["weights_sha256"], "labels": info["labels"], "salt": "jitsuris-tta-v1"}
    Path(str(out_path) + ".json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False))


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("infer")
    p.add_argument("--batches", default=",".join(BENCH_BATCHES))
    p.add_argument("--views", type=int, default=8)
    p.add_argument("--checkpoint", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--device", default="cpu")
    p.add_argument("--limit", type=int)
    p = sub.add_parser("summary")
    p.add_argument("--batches", default=",".join(BENCH_BATCHES))
    a = ap.parse_args(argv)
    if a.cmd == "infer":
        infer(a.batches.split(","), a.views, a.checkpoint, a.out, a.device, a.limit)
    else:
        from collections import Counter
        rows = load_bench(a.batches.split(","))
        used = [r for r in rows if r["truth"] and r["truth"] not in NOT_USED]
        print(f"列 {len(rows)}・採点できる列 {len(used)}・裁定した列 {sum(r['adjudicated'] for r in used)}・今のモデルの正解 {sum(r['pred'] == r['truth'] for r in used) / len(used):.1%}")
        print(Counter(r["truth"] for r in used).most_common())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
