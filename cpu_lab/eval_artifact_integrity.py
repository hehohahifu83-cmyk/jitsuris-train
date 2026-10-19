"""Fail-closed validation for paired Jitsuris evaluation report artifacts."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

DATASETS = ("dev220", "general", "business", "business2", "japan_procurement")
CONDITIONS = ("sparse", "ft", "blend50", "blend60", "blend70")
SEEDS = ("1", "2")
FILE_RE = re.compile(r"job([12])_probs_(dev220|general|business|business2|japan_procurement)_(sparse|ft|blend50|blend60|blend70)\.json\Z")
ERROR_FILE_RE = re.compile(r"job[12]_errors_(?:dev220|general|business|business2|japan_procurement)_(?:sparse|ft|blend50|blend60|blend70)\.json\Z")


def is_reported_error(row: dict) -> bool:
    truth, prediction = row["truth"], row["prediction"]
    if truth == "other":
        return prediction not in ("other", "unknown")
    return prediction == "unknown" or prediction != truth


def _row_key(row: dict) -> tuple:
    return (row["index"], row["column"], row["truth"], row["prediction"])


def validate_report_dir(root: Path, *, datasets=DATASETS, seeds=SEEDS, conditions=CONDITIONS) -> dict:
    """Validate completeness, uniqueness, labels, outcomes, and errors/probs parity."""
    root = Path(root)
    if not root.is_dir():
        raise ValueError(f"report directory does not exist: {root}")
    probs = sorted(p for p in root.glob("job*_probs_*.json") if FILE_RE.fullmatch(p.name))
    found = {}
    expected = {(seed, ds, condition) for seed in map(str, seeds)
                for ds in datasets for condition in conditions}
    identity = {}
    errors_checked = 0
    for path in probs:
        match = FILE_RE.fullmatch(path.name)
        job, dataset, filename_condition = match.groups()
        obj = json.loads(path.read_text(encoding="utf-8"))
        seed, condition = str(obj.get("seed")), obj.get("condition_id")
        key = (seed, dataset, condition)
        if condition != filename_condition or obj.get("dataset") != dataset:
            raise ValueError(f"filename/metadata mismatch: {path.name}")
        if seed != job[-1]:
            raise ValueError(f"job/seed mismatch: {path.name}")
        if key in found:
            raise ValueError(f"duplicate report: {path.name}")
        if not isinstance(obj.get("rows"), list):
            raise ValueError(f"rows missing or malformed: {path.name}")
        seen = set()
        expected_error_rows = []
        for row in obj["rows"]:
            if not isinstance(row, dict) or not {"index", "column", "truth", "prediction", "outcome", "critical"} <= row.keys():
                raise ValueError(f"malformed row in {path.name}")
            rid = row["index"]
            if rid in seen:
                raise ValueError(f"duplicate row index {rid}: {path.name}")
            seen.add(rid)
            truth, pred = row["truth"], row["prediction"]
            if truth == "other":
                expected_outcome = "other_ok" if pred in ("other", "unknown") else "other_ng"
            elif pred == "unknown":
                expected_outcome = "unknown"
            elif pred == truth:
                expected_outcome = "correct"
            else:
                expected_outcome = "wrong"
            if row["outcome"] != expected_outcome:
                raise ValueError(f"outcome/label mismatch in {path.name}, row {rid}")
            if row["critical"] and expected_outcome != "wrong":
                raise ValueError(f"critical flag on non-error in {path.name}, row {rid}")
            identity_key = (dataset, rid)
            signature = (row["column"], truth)
            if identity_key in identity and identity[identity_key] != signature:
                raise ValueError(f"row identity/truth differs across conditions: {identity_key}")
            identity[identity_key] = signature
            if is_reported_error(row):
                expected_error_rows.append(_row_key(row))
        error_path = root / path.name.replace("_probs_", "_errors_")
        if not error_path.is_file():
            raise ValueError(f"missing paired error report: {error_path.name}")
        err = json.loads(error_path.read_text(encoding="utf-8"))
        if (str(err.get("seed")) != seed or err.get("dataset") != dataset
                or err.get("condition_id") != condition):
            raise ValueError(f"error report metadata mismatch: {error_path.name}")
        listed = err.get("errors")
        if not isinstance(listed, list):
            raise ValueError(f"errors missing or malformed: {error_path.name}")
        actual_error_rows = [_row_key(row) for row in listed]
        if Counter(actual_error_rows) != Counter(expected_error_rows):
            raise ValueError(f"errors/probs rows differ: {error_path.name}")
        errors_checked += 1
        found[key] = len(obj["rows"])
    missing = expected - set(found)
    extra = set(found) - expected
    if missing or extra:
        raise ValueError(f"report matrix mismatch; missing={sorted(missing)}, extra={sorted(extra)}")
    return {"reports": len(found), "rows": sum(found.values()), "paired_error_files": errors_checked,
            "unique_dataset_rows": len(identity), "matrix": sorted(found)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report_dir", type=Path)
    parser.add_argument("--datasets", default=",".join(DATASETS))
    parser.add_argument("--seeds", default=",".join(SEEDS))
    parser.add_argument("--conditions", default=",".join(CONDITIONS))
    args = parser.parse_args()
    result = validate_report_dir(args.report_dir,
        datasets=tuple(args.datasets.split(",")), seeds=tuple(args.seeds.split(",")),
        conditions=tuple(args.conditions.split(",")))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
