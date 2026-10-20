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
# 汎用の並び（2026-10-20）：仕事の数・種子・試験の名前が上の組み合わせに限られない実行（学習率の探索・検証モード・3 種子の比較など）。
# 1 つ 1 つのファイルの検査（結果の意味・重大の印・誤りの一覧との一致・行の重複なし）は同じ。揃っているべき組み合わせだけが違う。
GENERIC_FILE_RE = re.compile(r"(job\d+|report)_probs_([a-z0-9_]+)_(sparse|ft|blend50|blend60|blend70)\.json\Z")
ERROR_FILE_RE = re.compile(r"job[12]_errors_(?:dev220|general|business|business2|japan_procurement)_(?:sparse|ft|blend50|blend60|blend70)\.json\Z")
NUMERIC_LABELS = {"date", "amount", "quantity", "rate", "id"}


def is_reported_error(row: dict) -> bool:
    truth, prediction = row["truth"], row["prediction"]
    if truth == "other":
        return prediction not in ("other", "unknown")
    return prediction == "unknown" or prediction != truth


def _row_key(row: dict) -> tuple:
    return (row["index"], row["column"], row["truth"], row["prediction"])


def detect_layout(root: Path) -> str:
    """paired＝仕事1・2 が種子 1・2 で開発用220 を評価した従来の対の設計。それ以外は generic。"""
    root = Path(root)
    seeds = []
    for job in ("job1", "job2"):
        p = root / f"{job}_probs_dev220_ft.json"
        if not p.is_file():
            return "generic"
        try:
            seeds.append(str(json.loads(p.read_text(encoding="utf-8")).get("seed")))
        except (OSError, ValueError):
            return "generic"
    return "paired" if seeds == ["1", "2"] else "generic"


def validate_report_dir(root: Path, *, datasets=DATASETS, seeds=SEEDS, conditions=CONDITIONS, layout="paired") -> dict:
    """Validate completeness, uniqueness, labels, outcomes, and errors/probs parity.

    layout="paired"（既定）：従来どおり、仕事1・2＝種子1・2 × 5 試験 × 条件がすべて揃っているか。
    layout="generic"：存在する (仕事, 試験) ごとに、条件がすべて揃っているか。1 つも無ければ失敗。
    layout="auto"：detect_layout が決める。
    """
    if layout == "auto":
        layout = detect_layout(root)
    if layout not in ("paired", "generic"):
        raise ValueError(f"unknown layout: {layout}")
    root = Path(root)
    if not root.is_dir():
        raise ValueError(f"report directory does not exist: {root}")
    file_re = FILE_RE if layout == "paired" else GENERIC_FILE_RE
    probs = sorted(p for p in root.glob("*_probs_*.json") if file_re.fullmatch(p.name))
    if layout == "generic" and not probs:
        raise ValueError("no probs report found")
    found = {}
    expected = {(seed, ds, condition) for seed in map(str, seeds)
                for ds in datasets for condition in conditions}
    identity = {}
    errors_checked = 0
    for path in probs:
        match = file_re.fullmatch(path.name)
        job, dataset, filename_condition = match.groups()
        obj = json.loads(path.read_text(encoding="utf-8"))
        seed, condition = str(obj.get("seed")), obj.get("condition_id")
        key = (seed, dataset, condition) if layout == "paired" else (job, dataset, condition)
        if condition != filename_condition or obj.get("dataset") != dataset:
            raise ValueError(f"filename/metadata mismatch: {path.name}")
        if layout == "paired" and seed != job[-1]:
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
            row_meta = {"dataset": dataset, "seed": seed, "condition": condition}
            if any(field in row and str(row[field]) != expected_value
                   for field, expected_value in row_meta.items()):
                raise ValueError(f"row metadata mismatch in {path.name}")
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
            expected_critical = (expected_outcome == "wrong" and truth in NUMERIC_LABELS
                                 and pred in NUMERIC_LABELS and truth != pred)
            if bool(row["critical"]) != expected_critical:
                raise ValueError(f"critical flag/labels mismatch in {path.name}, row {rid}")
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
    if layout == "paired":
        missing = expected - set(found)
        extra = set(found) - expected
    else:   # generic：存在する (仕事, 試験) ごとに全条件が揃っているか。余分な条件は許さない
        pairs = {(job, dataset) for job, dataset, _ in found}
        expected = {(job, dataset, condition) for job, dataset in pairs for condition in conditions}
        missing = expected - set(found)
        extra = set(found) - expected
    if missing or extra:
        raise ValueError(f"report matrix mismatch; missing={sorted(missing)}, extra={sorted(extra)}")
    return {"layout": layout, "reports": len(found), "rows": sum(found.values()), "paired_error_files": errors_checked,
            "unique_dataset_rows": len(identity), "matrix": sorted(found)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report_dir", type=Path)
    parser.add_argument("--datasets", default=",".join(DATASETS))
    parser.add_argument("--seeds", default=",".join(SEEDS))
    parser.add_argument("--conditions", default=",".join(CONDITIONS))
    parser.add_argument("--layout", choices=("paired", "generic", "auto"), default="paired")
    args = parser.parse_args()
    result = validate_report_dir(args.report_dir,
        datasets=tuple(args.datasets.split(",")), seeds=tuple(args.seeds.split(",")),
        conditions=tuple(args.conditions.split(",")), layout=args.layout)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
