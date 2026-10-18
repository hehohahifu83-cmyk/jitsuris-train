#!/usr/bin/env python3
"""Score a fixed, internally generated progress probe; never used for training."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from self_learning import _load_model, _read_jsonl


def score(model_path: str, probe_path: str, out_path: str) -> dict:
    rows = _read_jsonl(Path(probe_path))
    if not rows or any(r.get("split") != "progress_probe" or "target" not in r for r in rows):
        raise ValueError("expected labeled synthetic progress_probe rows")
    torch, model, tok, labels, format_text = _load_model(model_path)
    missing = sorted({r["target"] for r in rows} - set(labels))
    if missing:
        raise ValueError(f"probe labels are absent from model label map: {missing}")
    texts = [format_text((r["header"], r["values"], "other", r.get("context", []), r.get("unit_context", "")),
                         prefix="query: ",
                         ctx_unit=bool(r.get("unit_context"))) for r in rows]
    predictions = []
    with torch.inference_mode():
        for start in range(0, len(rows), 32):
            enc = tok(texts[start:start + 32], truncation=True, max_length=128, padding=True, return_tensors="pt")
            probs = torch.softmax(model(**enc).logits.float(), dim=-1).tolist()
            for row, p in zip(rows[start:start + 32], probs):
                pred = labels[max(range(len(p)), key=lambda i: p[i])]
                predictions.append({"id": row["id"], "target": row["target"], "prediction": pred,
                                    "correct": pred == row["target"]})
    correct = sum(int(x["correct"]) for x in predictions)
    result = {"model": model_path, "probe_path": probe_path, "probe_count": len(rows),
              "correct": correct, "accuracy": correct / len(rows), "errors": len(rows) - correct,
              "predictions": predictions}
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def compare(before_path: str, after_path: str, out_path: str) -> dict:
    before = json.loads(Path(before_path).read_text(encoding="utf-8"))
    after = json.loads(Path(after_path).read_text(encoding="utf-8"))
    if before["probe_count"] != after["probe_count"]:
        raise ValueError("probe size changed")
    before_rows = {x["id"]: x for x in before["predictions"]}
    after_rows = {x["id"]: x for x in after["predictions"]}
    if before_rows.keys() != after_rows.keys():
        raise ValueError("probe IDs changed")
    if any(before_rows[i]["target"] != after_rows[i]["target"] for i in before_rows):
        raise ValueError("probe gold labels changed")
    n = len(before_rows)
    delta = after["accuracy"] - before["accuracy"]
    improved = [i for i in before_rows if not before_rows[i]["correct"] and after_rows[i]["correct"]]
    regressed = [i for i in before_rows if before_rows[i]["correct"] and not after_rows[i]["correct"]]
    by_target = {}
    for target in sorted({x["target"] for x in before_rows.values()}):
        ids = [i for i, x in before_rows.items() if x["target"] == target]
        before_ok = sum(int(before_rows[i]["correct"]) for i in ids)
        after_ok = sum(int(after_rows[i]["correct"]) for i in ids)
        by_target[target] = {
            "count": len(ids), "before_correct": before_ok, "after_correct": after_ok,
            "before_accuracy": before_ok / len(ids), "after_accuracy": after_ok / len(ids),
            "delta_pp": (after_ok - before_ok) / len(ids) * 100,
            "improved_cases": [i for i in ids if not before_rows[i]["correct"] and after_rows[i]["correct"]],
            "regressed_cases": [i for i in ids if before_rows[i]["correct"] and not after_rows[i]["correct"]],
        }
    result = {"probe_count": n, "before_accuracy": before["accuracy"], "after_accuracy": after["accuracy"],
              "delta_pp": delta * 100, "errors_before": before["errors"], "errors_after": after["errors"],
              "improved_cases": improved, "regressed_cases": regressed, "by_target": by_target,
              "threshold_pp": 1.5,
              "result": "measurable_improvement" if delta * 100 >= 1.5 else
                        "measurable_regression" if delta * 100 <= -1.5 else "no_difference_under_1_5pp"}
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(required=True)
    s = sub.add_parser("score")
    s.add_argument("--model", required=True); s.add_argument("--probe", required=True); s.add_argument("--out", required=True)
    s.set_defaults(func=lambda a: score(a.model, a.probe, a.out))
    c = sub.add_parser("compare")
    c.add_argument("--before", required=True); c.add_argument("--after", required=True); c.add_argument("--out", required=True)
    c.set_defaults(func=lambda a: compare(a.before, a.after, a.out))
    args = p.parse_args()
    try:
        print(json.dumps(args.func(args), ensure_ascii=False))
    except (OSError, ValueError, KeyError, json.JSONDecodeError, RuntimeError) as exc:
        p.error(str(exc))


if __name__ == "__main__":
    main()
