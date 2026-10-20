"""独立評価：学習で保存した重み（FT_KEEP=1 の ft_out_jobN）を、学習の束の外にある主セットに当てる（2026-10-21）。

- ラベルは予測が終わってから読む（predict と score を分ける）。blind は読まない。主セットの値は出力に書かない。
- 同じ（主セット, 重み）の組は 1 回しか予測しない（台帳 ledger.jsonl）。やり直すときは --repeat-reason に理由を書き、台帳に残す。
- 重みは check_trained_model.py と同じ検査（manifest の SHA-256 との照合）を通ったものだけ使う。前置き（"query: " など）・max_length・単位列の文脈は、その重みの manifest から読む。
- 採点の出力は slice_eval.py・compare_models.py がそのまま読める形（<run>_probs_<dataset>_ft.json）。

使い方：
  python evaluate_independent.py predict --set <主セット.json> --checkpoint <ft_out_jobN> --out <予測.json> [--ledger eval_reports/independent/ledger.jsonl] [--device cpu] [--repeat-reason 理由]
  python evaluate_independent.py score --preds <予測.json> --labels <ラベル.json> --out-dir <出力先> --run job1 [--dataset independent_main] [--seed 1]

主セットの形（schema_version 1）：
  {"schema_version": 1, "set_id": "…", "columns": [{"id": "c001", "table": "t01", "source": "yokohama", "language": "ja",
    "header": "…", "values": ["…", … 先頭の 5 件], "siblings": ["同じ表の他の列の見出し", …], "unit": "同じ表の単位列の短い例（無ければ空）"}]}
ラベルの形：{"c001": "date", …}（id → ラベル。ラベルを付けた人ごとに別ファイル）
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
from collections import Counter

SCHEMA = 1
EVAL_MAX_LENGTH = 128


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def read_json(path):
    return json.loads(read_bytes(path).decode("utf-8"))


def normalized_header(value):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value)).strip()).casefold()


# ---------------------------------------------------------------- 主セット

def load_set(path):
    """主セットを読み、(中身, ファイルの SHA-256) を返す。形が違えば ValueError。"""
    raw = read_bytes(path)
    data = json.loads(raw.decode("utf-8"))
    if data.get("schema_version") != SCHEMA:
        raise ValueError(f"主セットの schema_version が {SCHEMA} でない：{data.get('schema_version')}")
    columns = data.get("columns")
    if not isinstance(columns, list) or not columns:
        raise ValueError("columns が空")
    seen = set()
    for c in columns:
        cid = c.get("id")
        if not cid or cid in seen:
            raise ValueError(f"id が無い／重複している：{cid!r}")
        seen.add(cid)
        if not str(c.get("header", "")).strip():
            raise ValueError(f"{cid}：header が空")
        if not isinstance(c.get("values"), list) or not c["values"]:
            raise ValueError(f"{cid}：values が空")
        if not isinstance(c.get("siblings", []), list):
            raise ValueError(f"{cid}：siblings が配列でない")
    return data, sha256_bytes(raw)


def rows_of(set_data):
    """学習・評価と同じ行の形 (見出し, 値, ラベル, 同じ表の見出し, 単位列の例)。ラベルの場所は空（ここでは読まない）。"""
    return [(str(c["header"]), [str(v) for v in c["values"]], "", [str(s) for s in c.get("siblings") or []], str(c.get("unit") or ""))
            for c in set_data["columns"]]


# ---------------------------------------------------------------- 重みの検査と設定

def checkpoint_info(checkpoint_dir):
    """重みを check_trained_model.py と同じ検査にかけ、manifest から前置き・max_length などを読む。問題があれば ValueError。"""
    import check_trained_model as C
    res = C.check(checkpoint_dir, require_manifest=True)
    if not res["ok"]:
        raise ValueError("重みの検査に通らない：" + " / ".join(res["problems"]))
    manifest = read_json(os.path.join(checkpoint_dir, "manifest.json"))
    extra = manifest.get("extra") or {}
    env = (manifest.get("run") or {}).get("env") or {}
    labels = read_json(os.path.join(checkpoint_dir, "labels.json"))
    return {
        "dir": checkpoint_dir,
        "weights_sha256": res["weights_sha256"],
        "model": (manifest.get("model") or {}).get("hf_repo_id"),
        "hf_revision": ((manifest.get("model") or {}).get("hf_revision") or {}).get("revision"),
        "model_type": extra.get("model_type"),
        "prefix": extra.get("prefix", ""),
        "max_length": int(extra.get("max_length") or EVAL_MAX_LENGTH),
        "ctx_unit": str(env.get("FT_CTX_UNIT", "")) == "1",
        "seed": (manifest.get("run") or {}).get("seed"),
        "labels": labels,
        "train_commit": manifest.get("commit"),
    }


def texts_of(rows, info):
    """モデルに入れる文字列（学習・評価と同じ encoder_context.format_encoder_text）。"""
    from encoder_context import format_encoder_text
    return [format_encoder_text(r, info["prefix"], ctx_unit=info["ctx_unit"]) for r in rows]


def infer_torch(checkpoint_dir, texts, info, device="cpu", batch_size=32):
    """保存した重みで確率を出す（学習の評価と同じ：truncation・max_length・fp32）。(確率の配列, 秒) を返す。"""
    import numpy as np
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(checkpoint_dir, local_files_only=True)
    if info.get("model_type") == "modernbert":
        tok.model_input_names = ["input_ids", "attention_mask"]      # 学習時と同じ（ModernBERT は token_type_ids を受け取らない）
    model = AutoModelForSequenceClassification.from_pretrained(checkpoint_dir, local_files_only=True)
    if model.config.num_labels != len(info["labels"]):
        raise ValueError("重みの分類器の次元と labels.json が合わない")
    model.to(device).eval()
    out, start = [], time.time()
    with torch.no_grad():
        for i in range(0, len(texts), batch_size):
            enc = tok(texts[i:i + batch_size], truncation=True, max_length=info["max_length"], padding=True, return_tensors="pt")
            enc = {k: v.to(device) for k, v in enc.items()}
            out.append(torch.softmax(model(**enc).logits.float(), -1).cpu().numpy())
    return np.vstack(out), time.time() - start


def make_predictions(set_data, rows, probs, labels):
    """確率 → 守りを通した判断（train3.decide_with_details）。ラベルは使わない。"""
    import numpy as np
    from train3 import decide_with_details
    details = decide_with_details(labels, probs, rows)
    top = np.argsort(probs, axis=1)[:, ::-1][:, :3]
    out = []
    for i, (col, detail) in enumerate(zip(set_data["columns"], details)):
        out.append({"id": col["id"], "column": normalized_header(col["header"]),
                    "raw_prediction": detail["raw_prediction"], "guarded_prediction": detail["guarded_prediction"],
                    "decision_reason": detail["decision_reason"],
                    "top3": [{"label": labels[int(j)], "probability": round(float(probs[i, j]), 6)} for j in top[i]]})
    return out


# ---------------------------------------------------------------- 台帳（同じ組を 2 回予測しない）

def ledger_entries(path):
    if not path or not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def check_ledger(path, set_sha256, weights_sha256, repeat_reason=None):
    """同じ（主セット, 重み）が台帳にあれば、理由なしでは拒む。理由があれば通し、reason つきで台帳に残す。戻り値＝台帳に書く reason（無ければ None）。"""
    seen = [e for e in ledger_entries(path) if e.get("set_sha256") == set_sha256 and e.get("weights_sha256") == weights_sha256]
    if seen and not repeat_reason:
        raise ValueError(f"この（主セット, 重み）はすでに予測済み（{seen[0].get('created_utc')}）。やり直すなら --repeat-reason に理由を書く")
    return repeat_reason if seen else None


def append_ledger(path, entry):
    if not path:
        return
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False, separators=(",", ":")) + "\n")


# ---------------------------------------------------------------- 予測

def predict(set_path, checkpoint_dir, out_path, ledger_path=None, device="cpu", repeat_reason=None, infer=None):
    """予測を作って out_path に書く。infer は試験用の差し替え（(checkpoint, texts, info) → (確率, 秒)）。"""
    set_data, set_sha = load_set(set_path)
    info = checkpoint_info(checkpoint_dir)
    reason = check_ledger(ledger_path, set_sha, info["weights_sha256"], repeat_reason)
    rows = rows_of(set_data)
    texts = texts_of(rows, info)
    if infer is None:
        probs, seconds = infer_torch(checkpoint_dir, texts, info, device)
    else:
        probs, seconds = infer(checkpoint_dir, texts, info)
    if len(probs) != len(rows):
        raise ValueError("確率の行数が主セットの列数と違う")
    preds = make_predictions(set_data, rows, probs, info["labels"])
    created = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    doc = {"schema_version": SCHEMA, "set_id": set_data.get("set_id"), "set_sha256": set_sha, "created_utc": created,
           "checkpoint": {k: info[k] for k in ("weights_sha256", "model", "hf_revision", "model_type", "prefix", "max_length", "ctx_unit", "seed", "train_commit")},
           "labels": info["labels"], "device": device,
           "timing": {"columns": len(rows), "seconds": round(float(seconds), 3), "ms_per_column": round(1000 * float(seconds) / len(rows), 3)},
           "rows": preds}
    body = json.dumps(doc, ensure_ascii=False, separators=(",", ":")) + "\n"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(body)
    append_ledger(ledger_path, {"set_sha256": set_sha, "weights_sha256": info["weights_sha256"], "preds_sha256": sha256_bytes(body.encode("utf-8")),
                                "created_utc": created, "preds": out_path, "repeat_reason": reason})
    return doc


# ---------------------------------------------------------------- 採点

def score(preds_path, labels_path, out_dir, run, dataset="independent_main", seed="1"):
    """予測にラベルを結びつけて、training と同じ形の記録を書く。ラベルがそろっていない・知らないラベルならエラー。"""
    from evaluation_records import assert_metrics_match, build_record, is_issue
    from llm_baseline import score_real
    raw = read_bytes(preds_path)
    doc = json.loads(raw.decode("utf-8"))
    label_raw = read_bytes(labels_path)
    truth = json.loads(label_raw.decode("utf-8"))
    ids = [r["id"] for r in doc["rows"]]
    missing = [i for i in ids if i not in truth]
    extra = sorted(set(truth) - set(ids))
    if missing or extra:
        raise ValueError(f"ラベルの id が予測と合わない：ラベルなし {missing[:5]}（{len(missing)} 件）／予測なし {extra[:5]}（{len(extra)} 件）")
    known = set(doc["labels"])
    unknown_labels = sorted({truth[i] for i in ids} - known)
    if unknown_labels:
        raise ValueError(f"重みが知らないラベルがある：{unknown_labels}")
    records = [build_record(index=i, dataset=dataset, seed=seed, condition="微調整だけ", column=r["column"], truth=truth[r["id"]],
                            guarded_prediction=r["guarded_prediction"], top3=r["top3"], decision_reason=r["decision_reason"])
               for i, r in enumerate(doc["rows"])]
    metrics = score_real([r["guarded_prediction"] for r in records], [r["truth"] for r in records])
    assert_metrics_match(records, metrics)
    meta = {"schema_version": 3, "test": dataset, "dataset": dataset, "seed": str(seed), "condition": "微調整だけ", "condition_id": "ft"}
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"{run}_probs_{dataset}_ft.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps({**meta, "rows": records}, ensure_ascii=False, separators=(",", ":")) + "\n")
    with open(os.path.join(out_dir, f"{run}_errors_{dataset}_ft.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps({**meta, "errors": [r for r in records if is_issue(r)]}, ensure_ascii=False, separators=(",", ":")) + "\n")
    link = {"run": run, "dataset": dataset, "set_id": doc.get("set_id"), "set_sha256": doc.get("set_sha256"),
            "preds_sha256": sha256_bytes(raw), "labels_sha256": sha256_bytes(label_raw), "checkpoint": doc["checkpoint"],
            "timing": doc.get("timing"), "device": doc.get("device"), "counts": dict(Counter(r["outcome"] for r in records)),
            "n": len(records), "acc": metrics.get("acc_all")}
    with open(os.path.join(out_dir, f"{run}_independent_manifest.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps(link, ensure_ascii=False, indent=1) + "\n")
    return link


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("predict")
    p.add_argument("--set", required=True)
    p.add_argument("--checkpoint", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--ledger", default="eval_reports/independent/ledger.jsonl")
    p.add_argument("--device", default="cpu")
    p.add_argument("--repeat-reason", default=None)
    s = sub.add_parser("score")
    s.add_argument("--preds", required=True)
    s.add_argument("--labels", required=True)
    s.add_argument("--out-dir", required=True)
    s.add_argument("--run", required=True)
    s.add_argument("--dataset", default="independent_main")
    s.add_argument("--seed", default="1")
    a = ap.parse_args(argv)
    if a.cmd == "predict":
        doc = predict(a.set, a.checkpoint, a.out, a.ledger, a.device, a.repeat_reason)
        print(json.dumps({k: doc[k] for k in ("set_id", "set_sha256", "checkpoint", "timing")}, ensure_ascii=False, indent=1))
    else:
        print(json.dumps(score(a.preds, a.labels, a.out_dir, a.run, a.dataset, a.seed), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
