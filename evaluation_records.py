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
                 guarded_prediction: str, top3: list[dict[str, Any]],
                 decision_reason: str | None = None) -> dict[str, Any]:
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
        "decision_reason": decision_reason,
        # Legacy field retained for existing readers; it always means the scored final label.
        "prediction": str(guarded_prediction),
        "outcome": outcome,
        "critical": bool(critical),
        "top3": top3,
    }


def summarize_records(records: Iterable[dict[str, Any]]) -> dict[str, int | float]:
    rows = list(records)
    counts: Counter[str] = Counter()
    critical = 0
    for row in rows:
        truth = str(row["truth"])
        prediction = str(row.get("guarded_prediction", row.get("prediction", "unknown")))
        expected = classify_outcome(truth, prediction)
        outcome = str(row.get("outcome", expected))
        if outcome not in VALID_OUTCOMES:
            raise ValueError(f"invalid evaluation outcome: {outcome}")
        if outcome != expected:
            raise ValueError(f"evaluation outcome does not match truth/prediction: {outcome} != {expected}")
        expected_critical = (outcome == "wrong" and truth in NUMERIC
                             and prediction in NUMERIC and truth != prediction)
        if bool(row.get("critical", expected_critical)) != expected_critical:
            raise ValueError("critical flag does not match scored truth/prediction")
        counts[outcome] += 1
        critical += int(expected_critical)
    correct, wrong, unknown = counts["correct"], counts["wrong"], counts["unknown"]
    n = correct + wrong + unknown
    return {
        "correct": correct,
        "wrong": wrong,
        "unknown": unknown,
        "critical": critical,
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
