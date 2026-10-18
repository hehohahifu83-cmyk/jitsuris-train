#!/usr/bin/env python3
"""Track whether each supplied CPU-lab material was actually used in training.

A receipt proves data flow and evaluation evidence; it cannot prove internal
representations or semantic acquisition by a neural network.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from self_learning import BLOCKED, _read_jsonl


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(pool_path: Path, pseudo_path: Path, source_model: str, out_path: Path) -> dict:
    pool, pseudo = _read_jsonl(pool_path), _read_jsonl(pseudo_path)
    if BLOCKED.search(str(pool_path)) or BLOCKED.search(str(pseudo_path)):
        raise ValueError("forbidden evaluation/test/blind data path")
    pool_by_id = {str(row.get("id")): row for row in pool}
    if len(pool_by_id) != len(pool):
        raise ValueError("pool IDs are not unique")
    accepted_by_id = {str(row.get("id")): row for row in pseudo}
    if len(accepted_by_id) != len(pseudo):
        raise ValueError("pseudo-label IDs are not unique")
    unknown = set(accepted_by_id) - set(pool_by_id)
    if unknown:
        raise ValueError(f"pseudo rows not present in the supplied pool: {sorted(unknown)[:3]}")
    items = []
    for row in pool:
        rid = str(row["id"])
        accepted = accepted_by_id.get(rid)
        if accepted and any(accepted.get(k) != row.get(k) for k in ("header", "values", "context", "unit_context", "source", "license")):
            raise ValueError(f"pseudo row {rid} does not match its source material")
        items.append({
            "material_id": rid,
            "status": "pseudo_label_candidate" if accepted else "not_selected_by_gate",
            "pseudo_label": accepted.get("label") if accepted else None,
            "verified": False if accepted else None,
            "training_status": "not_yet_run",
        })
    receipt = {
        "schema": "jitsuris-cpu-material-receipt-v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_model": source_model,
        "pool_path": str(pool_path),
        "pool_sha256": digest(pool_path),
        "pseudo_path": str(pseudo_path),
        "pseudo_sha256": digest(pseudo_path),
        "pool_count": len(pool),
        "pseudo_candidate_count": len(pseudo),
        "semantic_learning_claim": "not_assessed",
        "items": items,
        "seed_runs": [],
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return receipt


def mark_trained(receipt_path: Path, train_log: Path, seed: int, out_path: Path) -> dict:
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    log = train_log.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"CPU lab pseudo replay: (\d+) unverified rows", log)
    if not match:
        raise ValueError("training log does not confirm pseudo-material insertion")
    observed = int(match.group(1))
    expected = int(receipt["pseudo_candidate_count"])
    if observed != expected or expected < 1:
        raise ValueError(f"training log says {observed} rows; receipt expects {expected}")
    run = {"seed": seed, "status": "included_in_successful_training_process", "rows_confirmed": observed}
    receipt["seed_runs"] = [x for x in receipt["seed_runs"] if x.get("seed") != seed] + [run]
    for item in receipt["items"]:
        if item["status"] == "pseudo_label_candidate":
            item["training_status"] = "included_in_training"
    receipt["semantic_learning_claim"] = "not_assessed_until_probe_comparison"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--pool", required=True)
    p.add_argument("--pseudo", required=True)
    p.add_argument("--source-model", required=True)
    p.add_argument("--out", required=True)
    p.set_defaults(func=lambda a: prepare(Path(a.pool), Path(a.pseudo), a.source_model, Path(a.out)))
    p = sub.add_parser("mark-trained")
    p.add_argument("--receipt", required=True)
    p.add_argument("--train-log", required=True)
    p.add_argument("--seed", required=True, type=int)
    p.add_argument("--out", required=True)
    p.set_defaults(func=lambda a: mark_trained(Path(a.receipt), Path(a.train_log), a.seed, Path(a.out)))
    args = parser.parse_args()
    try:
        receipt = args.func(args)
        print(json.dumps({"pool_count": receipt["pool_count"], "pseudo_candidate_count": receipt["pseudo_candidate_count"],
                          "seed_runs": receipt["seed_runs"], "semantic_learning_claim": receipt["semantic_learning_claim"]},
                         ensure_ascii=False))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
