#!/usr/bin/env python3
"""Grouped validation-only experiments for W2 and W6.

Reads one preregistered FT_VAL=1 run and the corresponding training-side label
rows. It never reads fixed evaluation, sealed, blind, or independent-set files.
Only aggregate metrics are written.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold, GroupShuffleSplit


RUN_ID = "39496935773"
JOB = "job2"  # FT_LR=3e-5, seed 1
DATASETS = {
    "val_general": ("materials/real_labels.jsonl",),
    "val_business": ("materials/real_labels_biz.jsonl",),
    "val_business2": ("materials/real_labels_biz2.jsonl", "materials/real_labels_direct.jsonl"),
    "val_japan_procurement": ("materials/real_labels_jp.jsonl", "materials/real_labels_jp2.jsonl"),
}
LABELS = (
    "account", "address", "amount", "category", "date", "email", "id", "org",
    "other", "person", "phone", "product", "quantity", "rate", "tax_class", "text",
)
NUMERIC = {"date", "amount", "quantity", "rate", "id"}
THRESHOLDS = (0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.98, 0.99)
RISK_TARGET = 0.05
RISK_DELTA = 0.05


def normalize_header(value: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(value)).strip()).casefold()


def is_test_table(table: str) -> bool:
    return int(hashlib.md5(table.encode("utf-8")).hexdigest(), 16) % 5 == 0


def is_val_table(table: str) -> bool:
    return int(hashlib.md5(f"jitsuris-val-v1:{table}".encode("utf-8")).hexdigest(), 16) % 8 == 0


def load_expected_rows(repo_root: Path) -> dict[str, list[tuple[str, str, str]]]:
    expected: dict[str, list[tuple[str, str, str]]] = {}
    for dataset, paths in DATASETS.items():
        records: list[tuple[str, str, str]] = []
        for rel in paths:
            path = repo_root / rel
            if not path.is_file():
                if dataset in {"val_business2", "val_japan_procurement"} and len(paths) > 1 and rel.endswith(("real_labels_direct.jsonl", "real_labels_jp2.jsonl")):
                    continue
                raise FileNotFoundError(path)
            with path.open(encoding="utf-8") as fh:
                for line in fh:
                    row = json.loads(line)
                    table = str(row["table"])
                    if not is_test_table(table) and is_val_table(table):
                        records.append((normalize_header(str(row["header"]).lstrip("\ufeff")), str(row["label"]), table))
        expected[dataset] = records
    return expected


def load_validation_rows(repo_root: Path, run_dir: Path) -> list[dict]:
    if run_dir.name != RUN_ID:
        raise ValueError(f"only the preregistered validation run {RUN_ID} is permitted")
    manifest_path = run_dir / f"{JOB}_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    env = manifest.get("run", {}).get("env", {})
    if manifest.get("extra", {}).get("eval_mode") != "validation" or env.get("FT_VAL") != "1":
        raise ValueError("run manifest does not identify FT_VAL=1 validation-only outputs")
    if env.get("FT_LR") != "3e-5" or str(env.get("FT_SEED")) != "1":
        raise ValueError("run manifest is not the preregistered E5-base LR=3e-5, seed-1 job")

    expected = load_expected_rows(repo_root)
    all_rows: list[dict] = []
    for dataset, exp in expected.items():
        path = run_dir / f"{JOB}_probs_{dataset}_ft.json"
        if not path.is_file():
            if not exp:
                continue
            raise FileNotFoundError(path)
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("dataset") != dataset or payload.get("condition_id") != "ft" or str(payload.get("seed")) != "1":
            raise ValueError(f"unexpected metadata in {path.name}")
        saved = payload.get("rows", [])
        if len(saved) != len(exp):
            raise ValueError(f"row count does not match source validation split in {path.name}")
        for i, (record, (header, truth, table)) in enumerate(zip(saved, exp)):
            if record.get("index") != i or (record.get("column"), record.get("truth")) != (header, truth):
                raise ValueError(f"row order/label mismatch in {path.name}; refusing to analyze")
            top3 = record.get("top3", [])
            if not top3 or any(item.get("label") not in LABELS for item in top3):
                raise ValueError(f"invalid top-3 probabilities in {path.name}")
            probs = np.zeros(len(LABELS), dtype=float)
            for item in top3:
                p = float(item["probability"])
                if not math.isfinite(p) or p < 0 or p > 1:
                    raise ValueError(f"invalid probability in {path.name}")
                probs[LABELS.index(item["label"])] = p
            if any(float(top3[j]["probability"]) < float(top3[j + 1]["probability"]) for j in range(len(top3) - 1)):
                raise ValueError(f"top-3 probabilities are not ordered in {path.name}")
            all_rows.append({
                "dataset": dataset,
                "table": table,
                "group": f"{dataset}::{table}",
                "position": i,
                "header": header,
                "truth": truth,
                "raw": str(record.get("raw_prediction")),
                "guarded": str(record.get("guarded_prediction")),
                "top3": top3,
                "probs": probs,
                "top1_conf": float(top3[0]["probability"]),
            })
    if not all_rows:
        raise ValueError("no validation rows loaded")
    return all_rows


def build_features(rows: list[dict]) -> np.ndarray:
    by_group: dict[str, list[int]] = defaultdict(list)
    for i, row in enumerate(rows):
        by_group[row["group"]].append(i)
    features = []
    for i, row in enumerate(rows):
        peers = [j for j in by_group[row["group"]] if j != i]
        if peers:
            mean_peers = np.mean([rows[j]["probs"] for j in peers], axis=0)
            max_peers = np.max([rows[j]["probs"] for j in peers], axis=0)
        else:
            mean_peers = max_peers = np.zeros(len(LABELS), dtype=float)
        ordinal = by_group[row["group"]].index(i)
        n = len(by_group[row["group"]])
        position = (ordinal / (n - 1)) if n > 1 else 0.5
        top3_mass = float(sum(item["probability"] for item in row["top3"]))
        features.append(np.concatenate((row["probs"], mean_peers, max_peers, [position, math.log1p(n), max(0.0, 1.0 - top3_mass)])))
    return np.asarray(features, dtype=float)


def classify(truth: str, prediction: str) -> str:
    if truth == "other":
        return "other_ok" if prediction in {"unknown", "other"} else "other_ng"
    if prediction in {"unknown", "other"}:
        return "unknown"
    return "correct" if prediction == truth else "wrong"


def records_for(rows: list[dict], predictions: list[str]) -> list[dict]:
    out = []
    for row, prediction in zip(rows, predictions):
        p = "unknown" if prediction == "other" else prediction
        outcome = classify(row["truth"], p)
        out.append({
            "truth": row["truth"],
            "guarded_prediction": p,
            "outcome": outcome,
            "critical": outcome == "wrong" and row["truth"] in NUMERIC and p in NUMERIC and p != row["truth"],
            "column": row["header"],
        })
    return out


def score(records: list[dict]) -> dict:
    counts = Counter(r["outcome"] for r in records)
    n = len(records)
    known_n = counts["correct"] + counts["wrong"] + counts["unknown"]
    return {
        "n": n,
        "ok": counts["correct"] + counts["other_ok"],
        "ok_rate": (counts["correct"] + counts["other_ok"]) / max(n, 1),
        "acc_known": counts["correct"] / max(known_n, 1),
        "answered_precision": counts["correct"] / max(counts["correct"] + counts["wrong"], 1),
        "wrong": counts["wrong"],
        "unknown": counts["unknown"],
        "other_ng": counts["other_ng"],
        "critical": sum(r["critical"] for r in records),
    }


def calibration_metrics(probability: np.ndarray, correct: np.ndarray) -> dict:
    eps = 1e-12
    p = np.clip(probability, eps, 1 - eps)
    bins = np.array_split(np.argsort(p), min(10, max(1, len(p))))
    ece = sum(len(ix) / max(len(p), 1) * abs(float(p[ix].mean()) - float(correct[ix].mean())) for ix in bins if len(ix))
    return {
        "brier": float(np.mean((p - correct) ** 2)),
        "log_loss": float(-np.mean(correct * np.log(p) + (1 - correct) * np.log(1 - p))),
        "ece_10_equal_count": float(ece),
    }


def fit_binary_temperature(probability: np.ndarray, correct: np.ndarray) -> float:
    p = np.clip(probability, 1e-6, 1 - 1e-6)
    logits = np.log(p / (1 - p))
    y = np.asarray(correct, dtype=float)

    def objective(log_t: float) -> float:
        z = np.clip(logits / math.exp(log_t), -40, 40)
        q = 1.0 / (1.0 + np.exp(-z))
        q = np.clip(q, 1e-12, 1 - 1e-12)
        return float(-np.mean(y * np.log(q) + (1 - y) * np.log(1 - q)))

    result = minimize_scalar(objective, bounds=(math.log(0.05), math.log(20.0)), method="bounded")
    if not result.success:
        raise RuntimeError("temperature fit failed")
    return float(math.exp(result.x))


def apply_binary_temperature(probability: np.ndarray, temperature: float) -> np.ndarray:
    p = np.clip(np.asarray(probability, dtype=float), 1e-6, 1 - 1e-6)
    logits = np.log(p / (1 - p)) / float(temperature)
    return 1.0 / (1.0 + np.exp(-np.clip(logits, -40, 40)))


def hoeffding_table_risk_bound(losses: list[float], family_size: int = len(THRESHOLDS), delta: float = RISK_DELTA) -> float:
    """UCB for mean per-table answered critical-class error loss in [0,1]."""
    if not losses:
        return 1.0
    margin = math.sqrt(math.log(family_size / delta) / (2 * len(losses)))
    return min(1.0, float(np.mean(losses)) + margin)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    repo_root = Path(argv[0]).resolve() if argv else Path(__file__).resolve().parents[1]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    run_dir = repo_root / "eval_reports" / "runs" / RUN_ID
    rows = load_validation_rows(repo_root, run_dir)
    groups = np.asarray([row["group"] for row in rows])
    y = np.asarray([row["truth"] for row in rows])
    X = build_features(rows)

    # W2: cross-validated table-context meta-classifier. Folds never split a table.
    w2_predictions = [""] * len(rows)
    for train_idx, test_idx in GroupKFold(n_splits=5).split(X, y, groups):
        model = LogisticRegression(C=1.0, max_iter=3000, solver="lbfgs")
        model.fit(X[train_idx], y[train_idx])
        for idx, pred in zip(test_idx, model.predict(X[test_idx])):
            w2_predictions[int(idx)] = str(pred)
    if any(not p for p in w2_predictions):
        raise AssertionError("W2 did not produce an out-of-fold prediction for every validation row")

    os.environ["FT_VAL"] = "1"
    os.environ["FT_REAL_FRAC"] = "1.0"
    import slice_eval
    train_pairs, train_headers = slice_eval.train_sets_from_encoder_exp()
    slices = [slice_eval.slice_of(row["header"], row["truth"], train_pairs, train_headers) for row in rows]
    base_records = records_for(rows, [row["guarded"] for row in rows])
    w2_records = records_for(rows, w2_predictions)
    all_ix = list(range(len(rows)))
    unknown_ix = [i for i, part in enumerate(slices) if part == "未知見出し"]
    w2 = {
        "method": "5-fold GroupKFold by (dataset, source table); LogisticRegression C=1 on base top-3 probabilities, same-table peer mean/max probabilities, normalized column position and table length",
        "groups": len(set(groups)),
        "rows": len(rows),
        "all_baseline_guarded": score([base_records[i] for i in all_ix]),
        "all_oof_reranker": score([w2_records[i] for i in all_ix]),
        "unknown_header_rows": len(unknown_ix),
        "unknown_header_baseline_guarded": score([base_records[i] for i in unknown_ix]),
        "unknown_header_oof_reranker": score([w2_records[i] for i in unknown_ix]),
    }
    w2["unknown_header_ok_delta_pp"] = 100 * (w2["unknown_header_oof_reranker"]["ok_rate"] - w2["unknown_header_baseline_guarded"]["ok_rate"])
    w2["critical_delta"] = w2["unknown_header_oof_reranker"]["critical"] - w2["unknown_header_baseline_guarded"]["critical"]

    # W6: cross-fitted binary top-1 temperature. This calibrates correctness of the
    # saved top-1 only; top-3 files do not retain enough scores for full 16-way TS.
    raw_p = np.asarray([row["top1_conf"] for row in rows], dtype=float)
    raw_correct = np.asarray([row["raw"] == row["truth"] for row in rows], dtype=float)
    oof_q = np.zeros(len(rows), dtype=float)
    temps = []
    group_cv = GroupKFold(n_splits=5)
    for train_idx, test_idx in group_cv.split(raw_p.reshape(-1, 1), raw_correct, groups):
        t = fit_binary_temperature(raw_p[train_idx], raw_correct[train_idx])
        temps.append(t)
        oof_q[test_idx] = apply_binary_temperature(raw_p[test_idx], t)
    w6_temp = {
        "method": "5-fold group cross-fit; binary one-vs-rest top-1 temperature from saved top-1 probability and correctness",
        "rows": len(rows),
        "group_count": len(set(groups)),
        "temperature_median": float(np.median(temps)),
        "temperature_range": [float(min(temps)), float(max(temps))],
        "raw_top1_calibration": calibration_metrics(raw_p, raw_correct),
        "oof_calibrated_top1": calibration_metrics(oof_q, raw_correct),
        "top1_accuracy_rate": float(raw_correct.mean()),
        "full_16_class_temperature_available": False,
        "reason": "saved artifacts contain only top-3 probabilities, not the complete 16-class vector/logits",
    }

    # LTT-style exploratory risk selection at the table level. Fit T on one set of
    # tables, choose a threshold on disjoint tables, and use a Hoeffding UCB for the
    # bounded mean per-table selective loss. No formal pass is claimed for pooled
    # per-column risk; that would require a max-answered-columns assumption.
    split = GroupShuffleSplit(n_splits=1, test_size=0.30, random_state=20261021)
    fit_idx, cal_idx = next(split.split(raw_p.reshape(-1, 1), raw_correct, groups))
    risk_t = fit_binary_temperature(raw_p[fit_idx], raw_correct[fit_idx])
    cal_q = apply_binary_temperature(raw_p[cal_idx], risk_t)
    cal_records = records_for([rows[i] for i in cal_idx], [rows[i]["guarded"] for i in cal_idx])
    cal_rows = [rows[i] for i in cal_idx]
    cal_groups = [rows[i]["group"] for i in cal_idx]
    risks = []
    for tau in THRESHOLDS:
        per_table: dict[str, list[int]] = defaultdict(lambda: [0, 0])
        for local_i, source_i in enumerate(cal_idx):
            row = rows[int(source_i)]
            # The selective rule only abstains on the five numeric output labels.
            if row["truth"] not in NUMERIC or row["guarded"] not in NUMERIC or cal_q[local_i] < tau:
                continue
            per_table[row["group"]][1] += 1
            if row["guarded"] != row["truth"]:
                per_table[row["group"]][0] += 1
        losses = [wrong / answered if answered else 0.0 for wrong, answered in per_table.values()]
        # Empty-answer tables contribute zero selective loss, so include every
        # calibration table in the denominator of this conservative table metric.
        loss_map = {g: (v[0] / v[1] if v[1] else 0.0) for g, v in per_table.items()}
        losses = [loss_map.get(g, 0.0) for g in set(cal_groups)]
        ucb = hoeffding_table_risk_bound(losses)
        accepted = sum(v[1] for v in per_table.values())
        wrong = sum(v[0] for v in per_table.values())
        risks.append({"threshold": tau, "answered_critical": accepted, "wrong_answered_critical": wrong,
                      "empirical_answered_error_rate": wrong / accepted if accepted else None,
                      "mean_per_table_loss": float(np.mean(losses)) if losses else None,
                      "table_loss_ucb_95_bonferroni": ucb,
                      "certifies_target": ucb <= RISK_TARGET})
    eligible = [x for x in risks if x["certifies_target"]]
    chosen = max(eligible, key=lambda x: x["threshold"]) if eligible else None
    # Empirical threshold curve on all OOF confidence scores is descriptive only.
    base_unknown_rate = sum(row["guarded"] in {"unknown", "other"} for row in rows) / len(rows)
    curve = []
    for tau in THRESHOLDS:
        answered_numeric_ix = [i for i, q in enumerate(oof_q)
                               if rows[i]["guarded"] in NUMERIC and q >= tau]
        critical_ix = [i for i in answered_numeric_ix if rows[i]["truth"] in NUMERIC]
        wrong_critical = sum(rows[i]["guarded"] != rows[i]["truth"] for i in critical_ix)
        rejected_numeric = sum(row["guarded"] in NUMERIC and oof_q[i] < tau for i, row in enumerate(rows))
        unknown_after = sum(row["guarded"] in {"unknown", "other"} for row in rows) + rejected_numeric
        other_false_answers = sum(row["truth"] == "other" and row["guarded"] in NUMERIC and oof_q[i] >= tau for i, row in enumerate(rows))
        unknown_rate = unknown_after / max(len(rows), 1)
        curve.append({
            "threshold": tau,
            "answered_critical": len(critical_ix),
            "wrong_answered_critical": int(wrong_critical),
            "empirical_answered_error_rate": wrong_critical / len(critical_ix) if critical_ix else None,
            "unknown_truth_numeric_false_answers": int(other_false_answers),
            "overall_unknown_rate": unknown_rate,
            "unknown_increase_pp": 100 * (unknown_rate - base_unknown_rate),
        })
    w6_selective = {
        "risk_target": RISK_TARGET,
        "confidence_level": 1 - RISK_DELTA,
        "risk_unit": "mean table-level selective loss among true critical-class rows; rows within a source table are kept together",
        "calibration_split": {"fit_tables": len(set(groups[fit_idx])), "threshold_calibration_tables": len(set(groups[cal_idx]))},
        "thresholds_tested": list(THRESHOLDS),
        "table_level_certificate_candidates": risks,
        "selected_threshold": chosen,
        "certified_policy_found": chosen is not None,
        "unconstrained_empirical_curve_on_oof_predictions": curve,
        "baseline_overall_unknown_rate": base_unknown_rate,
        "limitation": "table-level bound is conservative and does not certify pooled per-column risk; saved probabilities are top-3 only",
    }

    report = {
        "schema_version": 1,
        "created_utc": "2026-10-21",
        "validation_run": RUN_ID,
        "job": JOB,
        "scope": "training-side FT_VAL=1 only; fixed tests, independent main, sealed sets, and blind sets excluded",
        "source_alignment": {"checked": True, "row_count": len(rows), "table_groups": len(set(groups)), "datasets": {k: sum(row["dataset"] == k for row in rows) for k in DATASETS}},
        "w2_same_table_reranker": w2,
        "w6_temperature": w6_temp,
        "w6_selective_threshold": w6_selective,
    }
    output = repo_root / "bench" / "w2_w6_validation_20261021.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
