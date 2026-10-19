"""Canonical scored evaluation rows shared by model output and audits.

The classifier's raw top label and the post-decision label are kept separately.
All outcome counts follow llm_baseline.score_real semantics.
"""
from __future__ import annotations

from collections import Counter
from typing import Any, Iterable

NUMERIC = {"date", "amount", "quantity", "rate", "id"}
VALID_OUTCOMES = {"correct", "wrong", "unknown", "other_ok", "other_ng"}


def classify_outcome(truth: str, prediction: str) -> str:
    if truth == "other":
        return "other_ok" if prediction in {"unknown", "other"} else "other_ng"
    if prediction in {"unknown", "other"}:
        return "unknown"
    return "correct" if prediction == truth else "wrong"


def build_record(*, index: int, dataset: str, seed: int | str,
                 condition: str, column: str, truth: str,
                 guarded_prediction: str, top3: list[dict[str, Any]]) -> dict[str, Any]:
    raw_prediction = str(top3[0]["label"]) if top3 else None
    outcome = classify_outcome(str(truth), str(guarded_prediction))
    critical = (outcome == "wrong" and truth in NUMERIC
                and guarded_prediction in NUMERIC and truth != guarded_prediction)
    return {
        "index": int(index),
        "dataset": str(dataset),
        "seed": str(seed),
        "condition": str(condition),
        "column": str(column),
        "truth": str(truth),
        "raw_prediction": raw_prediction,
        "guarded_prediction": str(guarded_prediction),
        # Legacy field retained for existing readers; it always means the scored final label.
        "prediction": str(guarded_prediction),
        "outcome": outcome,
        "critical": bool(critical),
        "top3": top3,
    }


def summarize_records(records: Iterable[dict[str, Any]]) -> dict[str, int | float]:
    counts = Counter(str(row.get("outcome") or classify_outcome(
        str(row["truth"]), str(row.get("guarded_prediction", row["prediction"]))
    )) for row in records)
    invalid = set(counts) - VALID_OUTCOMES
    if invalid:
        raise ValueError(f"invalid evaluation outcomes: {sorted(invalid)}")
    correct, wrong, unknown = counts["correct"], counts["wrong"], counts["unknown"]
    n = correct + wrong + unknown
    return {
        "correct": correct,
        "wrong": wrong,
        "unknown": unknown,
        "critical": sum(bool(row.get("critical")) for row in records),
        "n": n,
        "acc_all": correct / max(n, 1),
        "answered": (correct + wrong) / max(n, 1),
        "precision": correct / max(correct + wrong, 1),
        "other_ok": counts["other_ok"],
        "other_ng": counts["other_ng"],
    }


def assert_metrics_match(records: list[dict[str, Any]], official: dict[str, Any]) -> None:
    observed = summarize_records(records)
    keys = ("correct", "wrong", "unknown", "critical", "n", "other_ok", "other_ng")
    mismatches = {key: (observed[key], official.get(key)) for key in keys
                  if observed[key] != official.get(key)}
    if mismatches:
        raise AssertionError(f"evaluation row outcomes do not match official metrics: {mismatches}")


def is_issue(record: dict[str, Any]) -> bool:
    outcome = record.get("outcome")
    if outcome is None:
        outcome = classify_outcome(
            str(record["truth"]),
            str(record.get("guarded_prediction", record.get("prediction", "unknown"))),
        )
    return outcome in {"wrong", "unknown", "other_ng"}
