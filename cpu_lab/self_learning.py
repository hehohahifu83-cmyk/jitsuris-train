#!/usr/bin/env python3
"""Safe CPU active-learning loop for Jitsuris column-type models.

Pool rows are unlabeled public/synthetic columns. The model ranks uncertain,
diverse rows for human review; only independently verified labels are replayed
into training. Fixed evaluation sets are never accepted as pool inputs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path

BLOCKED = re.compile(r"blind[_ -]?set|(?:^|[/_. -])set[_ -]?(?:3|5|7)(?:$|[/_. -])|evaluation|holdout|test", re.I)
REQUIRED_POOL = {"id", "header", "values", "source", "license", "split", "privacy_checked"}


def _read_jsonl(path: Path):
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line_no}: expected a JSON object")
        rows.append(row)
    return rows


def _check_pool(path: Path, rows):
    if BLOCKED.search(str(path)):
        raise ValueError("evaluation, test, blind_set*, and sets 3/5/7 are forbidden")
    ids = set()
    for i, row in enumerate(rows, 1):
        missing = REQUIRED_POOL - row.keys()
        if missing:
            raise ValueError(f"row {i}: missing {', '.join(sorted(missing))}")
        if row["split"] not in ("unlabeled", "train"):
            raise ValueError(f"row {i}: pool split must be unlabeled or train")
        if row["privacy_checked"] is not True:
            raise ValueError(f"row {i}: privacy_checked must be true")
        if not str(row["source"]).strip() or not str(row["license"]).strip():
            raise ValueError(f"row {i}: source and license are required")
        if any(BLOCKED.search(str(row.get(k, ""))) for k in ("id", "source", "source_url", "dataset", "split")):
            raise ValueError(f"row {i}: evaluation data or prohibited set reference")
        if "label" in row or "truth" in row:
            raise ValueError(f"row {i}: pool must not contain labels")
        if row["id"] in ids:
            raise ValueError(f"row {i}: duplicate id {row['id']!r}")
        ids.add(row["id"])
        if not isinstance(row["values"], list) or not row["values"]:
            raise ValueError(f"row {i}: values must be a non-empty list")
        if not isinstance(row.get("context", []), list):
            raise ValueError(f"row {i}: context must be a list")


def _load_model(model_path: str):
    try:
        import torch
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        from encoder_context import format_encoder_text
    except ImportError as exc:
        raise RuntimeError("install project CPU training dependencies before scoring") from exc
    torch.set_num_threads(max(1, int(__import__("os").environ.get("FT_CPU_THREADS", "2"))))
    model = AutoModelForSequenceClassification.from_pretrained(model_path).cpu().eval()
    tok = AutoTokenizer.from_pretrained(model_path)
    labels_path = Path(model_path) / "labels.json"
    labels = json.loads(labels_path.read_text(encoding="utf-8"))
    if len(labels) != model.config.num_labels:
        raise ValueError("labels.json does not match model output dimension")
    return torch, model, tok, labels, format_encoder_text


def _entropy(probs):
    return -sum(p * math.log(max(p, 1e-12)) for p in probs)


def select(args):
    pool_path = Path(args.pool)
    pool = _read_jsonl(pool_path)
    _check_pool(pool_path, pool)
    if not pool:
        raise ValueError("pool is empty")
    torch, model, tok, labels, format_text = _load_model(args.model)
    texts = [format_text((r["header"], r["values"], "other", r.get("context", []), r.get("unit_context", "")),
                         prefix="query: " if "e5" in args.model.lower() else "", ctx_unit=bool(r.get("unit_context"))) for r in pool]
    ranked = []
    with torch.inference_mode():
        for start in range(0, len(texts), args.batch_size):
            batch = tok(texts[start:start + args.batch_size], truncation=True, max_length=128, padding=True, return_tensors="pt")
            logits = model(**batch).logits.float()
            for offset, p in enumerate(torch.softmax(logits, dim=-1).tolist()):
                row = pool[start + offset]
                order = sorted(range(len(p)), key=lambda j: p[j], reverse=True)
                top = [{"label": labels[j], "probability": round(p[j], 6)} for j in order[:3]]
                margin = p[order[0]] - p[order[1]] if len(order) > 1 else p[order[0]]
                ranked.append({"row": row, "top": top, "entropy": _entropy(p), "margin": margin, "predicted": labels[order[0]]})
    # Uncertainty first; cycle across predicted labels and suppress near-duplicate headers.
    ranked.sort(key=lambda x: (-x["entropy"], x["margin"], str(x["row"]["id"])))
    chosen, label_counts, fingerprints = [], {}, set()
    remaining = list(ranked)
    while remaining and len(chosen) < args.budget:
        eligible = [x for x in remaining if re.sub(r"\W+", " ", str(x["row"]["header"]).casefold()).strip() not in fingerprints]
        if not eligible:
            break
        item = max(eligible, key=lambda x: (x["entropy"] + 0.2 / (1 + label_counts.get(x["predicted"], 0)), x["margin"], str(x["row"]["id"])))
        remaining.remove(item)
        row = item["row"]
        fp = re.sub(r"\W+", " ", str(row["header"]).casefold()).strip()
        label = item["predicted"]
        item["review"] = {"status": "pending", "label": "", "reviewer": "", "verified": False}
        item["query_score"] = round(item["entropy"] + 0.2 / (1 + label_counts.get(label, 0)), 6)
        chosen.append(item)
        fingerprints.add(fp)
        label_counts[label] = label_counts.get(label, 0) + 1
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for item in chosen:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"review queue: {len(chosen)} / {len(pool)} candidates -> {out}")


def approve(args):
    queue_path = Path(args.reviewed)
    if BLOCKED.search(str(queue_path)):
        raise ValueError("evaluation, test, blind_set*, and sets 3/5/7 are forbidden")
    rows = _read_jsonl(queue_path)
    if not rows:
        raise ValueError("review queue is empty")
    approved, seen = [], set()
    for i, item in enumerate(rows, 1):
        row = item.get("row", {})
        review = item.get("review", {})
        if review.get("status") != "approved" or review.get("verified") is not True:
            continue
        label = str(review.get("label", "")).strip()
        reviewer = str(review.get("reviewer", "")).strip()
        if not label or not reviewer:
            raise ValueError(f"row {i}: approved label requires label and reviewer")
        if row.get("split") not in ("train", "unlabeled") or not row.get("privacy_checked"):
            raise ValueError(f"row {i}: invalid provenance/privacy metadata")
        if any(BLOCKED.search(str(row.get(k, ""))) for k in ("id", "source", "source_url", "dataset", "split")):
            raise ValueError(f"row {i}: prohibited source")
        if row.get("id") in seen:
            raise ValueError(f"row {i}: duplicate approved id")
        seen.add(row.get("id"))
        approved.append({
            "id": row["id"], "header": row["header"], "values": row["values"],
            "label": label, "context": row.get("context", []), "unit_context": row.get("unit_context", ""),
            "source": row["source"], "license": row["license"], "split": "train",
            "privacy_checked": True, "reviewer": reviewer, "verified": True,
        })
    if not approved:
        raise ValueError("no rows have explicit, verified approval")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for row in approved:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"verified training rows: {len(approved)} -> {out} (sha256 {digest})")


def load_approved_replay(path: str, allowed_labels):
    """Return trainer tuple rows only from reviewed, traceable CPU-lab records."""
    p = Path(path)
    rows = _read_jsonl(p)
    if BLOCKED.search(str(p)):
        raise ValueError("refusing evaluation/test data as replay training data")
    result, seen = [], set()
    for i, row in enumerate(rows, 1):
        if row.get("split") != "train" or row.get("verified") is not True or not row.get("reviewer"):
            raise ValueError(f"replay row {i} is not human-verified training data")
        if row.get("privacy_checked") is not True or not row.get("source") or not row.get("license"):
            raise ValueError(f"replay row {i} has incomplete provenance/privacy metadata")
        if any(BLOCKED.search(str(row.get(k, ""))) for k in ("id", "source", "split")):
            raise ValueError(f"replay row {i} references a forbidden evaluation source")
        if row.get("label") not in allowed_labels:
            raise ValueError(f"replay row {i} has a label absent from the base training set")
        if row.get("id") in seen:
            raise ValueError(f"replay row {i} duplicates an id")
        seen.add(row.get("id"))
        result.append((row["header"], row["values"], row["label"], row.get("context", []), row.get("unit_context", "")))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(required=True)
    p = sub.add_parser("select", help="rank uncertain/diverse unlabeled columns for review")
    p.add_argument("--model", required=True, help="saved Jitsuris/Hugging Face sequence-classification candidate")
    p.add_argument("--pool", required=True, help="JSONL unlabeled public/synthetic columns")
    p.add_argument("--out", required=True)
    p.add_argument("--budget", type=int, default=100)
    p.add_argument("--batch-size", type=int, default=32)
    p.set_defaults(func=select)
    p = sub.add_parser("approve", help="export only human-verified labels as replay training JSONL")
    p.add_argument("--reviewed", required=True, help="review queue with explicit review.status/label/reviewer/verified")
    p.add_argument("--out", required=True)
    p.set_defaults(func=approve)
    args = parser.parse_args()
    if getattr(args, "budget", 1) < 1 or getattr(args, "batch_size", 1) < 1:
        parser.error("budget and batch size must be positive")
    try:
        args.func(args)
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
