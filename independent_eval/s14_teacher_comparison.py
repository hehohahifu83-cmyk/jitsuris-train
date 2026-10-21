"""Aggregate S14 teacher-label/model comparisons without exposing row-level data.

Inputs may contain column samples and private labels. This module reads only ids,
labels, and saved guarded predictions; its report contains aggregate counts/rates.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

SET_ID = "independent-main-20261021-v1"
UNSCORED = {"unknown", "S"}
SUPPORTED_LABELS = {
    "date", "amount", "quantity", "rate", "id", "org", "person", "product",
    "account", "tax_class", "text", "category", "email", "phone", "address",
    "other", "unknown", "S",
}


def label_ok(prediction: str, truth: str) -> bool:
    """Use evaluation scoring: unknown is a correct abstention for truth=other."""
    return prediction in {"other", "unknown"} if truth == "other" else prediction == truth


def _validate_labels(truth: dict[str, str], labels: dict[str, str], name: str) -> None:
    if set(labels) != set(truth):
        raise ValueError(f"{name} label IDs do not match adjudicated IDs")
    if any(value not in SUPPORTED_LABELS for value in labels.values()):
        raise ValueError(f"{name} contains an unsupported label")


def summarize(
    truth: dict[str, str],
    teachers: dict[str, dict[str, str]],
    models: dict[str, list[dict[str, str]]],
) -> dict[str, Any]:
    if not truth or any(value not in SUPPORTED_LABELS for value in truth.values()):
        raise ValueError("adjudicated labels are empty or contain unsupported values")
    for name, labels in teachers.items():
        _validate_labels(truth, labels, name)
    all_ids = set(truth)
    scored = [row_id for row_id, value in truth.items() if value not in UNSCORED]
    excluded = Counter(value for value in truth.values() if value in UNSCORED)
    for model_name, seeds in models.items():
        if not seeds:
            raise ValueError(f"{model_name} has no saved prediction files")
        for seed in seeds:
            if set(seed) != all_ids:
                raise ValueError(f"{model_name} prediction IDs do not match labels")

    teacher_names = list(teachers)
    if len(teacher_names) != 2:
        raise ValueError("S14 expects exactly the Claude and ChatGPT first-label files")
    first_a, first_b = (teachers[name] for name in teacher_names)
    agree = [row_id for row_id in scored if first_a[row_id] == first_b[row_id]]
    disagree = [row_id for row_id in scored if first_a[row_id] != first_b[row_id]]
    if len(agree) + len(disagree) != len(scored):
        raise AssertionError("agreement partition does not cover scored columns")

    teacher_accuracy = {}
    for name, labels in teachers.items():
        correct = sum(label_ok(labels[row_id], truth[row_id]) for row_id in scored)
        teacher_accuracy[name] = {"correct": correct, "total": len(scored), "rate": correct / len(scored)}

    model_rates: dict[str, Any] = {}
    error_overlap: dict[str, Any] = {name: {} for name in teachers}
    groups = {"overall": scored, "agree": agree, "disagree": disagree}
    for model_name, seeds in models.items():
        by_group = {}
        for group_name, group_ids in groups.items():
            if not group_ids:
                by_group[group_name] = {"mean_rate": None, "per_seed_rates": []}
                continue
            rates = [
                sum(label_ok(seed[row_id], truth[row_id]) for row_id in group_ids) / len(group_ids)
                for seed in seeds
            ]
            by_group[group_name] = {
                "mean_rate": sum(rates) / len(rates),
                "per_seed_rates": rates,
            }
        model_rates[model_name] = by_group

        for teacher_name, labels in teachers.items():
            teacher_correct_model_wrong = []
            both_wrong = []
            for seed in seeds:
                teacher_correct_model_wrong.append(sum(
                    label_ok(labels[row_id], truth[row_id])
                    and not label_ok(seed[row_id], truth[row_id])
                    for row_id in scored
                ))
                both_wrong.append(sum(
                    not label_ok(labels[row_id], truth[row_id])
                    and not label_ok(seed[row_id], truth[row_id])
                    for row_id in scored
                ))
            error_overlap[teacher_name][model_name] = {
                "teacher_correct_model_wrong_per_seed": teacher_correct_model_wrong,
                "teacher_correct_model_wrong_mean": sum(teacher_correct_model_wrong) / len(seeds),
                "both_wrong_per_seed": both_wrong,
                "both_wrong_mean": sum(both_wrong) / len(seeds),
            }

    return {
        "set_id": SET_ID,
        "total": len(all_ids),
        "scored": len(scored),
        "excluded": dict(sorted(excluded.items())),
        "teacher_agreement": len(agree),
        "teacher_disagreement": len(disagree),
        "teacher_accuracy": teacher_accuracy,
        "model_rates": model_rates,
        "error_overlap": error_overlap,
        "seed_count": {name: len(seeds) for name, seeds in models.items()},
    }


def _read_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_labels(path: str | Path) -> dict[str, str]:
    obj = _read_json(path)
    if not isinstance(obj, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in obj.items()):
        raise ValueError("label file must be a JSON object of IDs to labels")
    return obj


def load_predictions(path: str | Path) -> dict[str, str]:
    obj = _read_json(path)
    if obj.get("schema_version") != 1 or obj.get("set_id") != SET_ID:
        raise ValueError("prediction file has an unexpected schema or set")
    if "v9.1" not in obj.get("available_guard_versions", []):
        raise ValueError("prediction file does not contain Guard v9.1")
    result = {}
    for row in obj.get("rows", []):
        row_id = row.get("id")
        predictions = row.get("guard_predictions")
        if not isinstance(row_id, str) or row_id in result or not isinstance(predictions, dict):
            raise ValueError("prediction rows have invalid or duplicate IDs")
        guarded = predictions.get("v9.1")
        if not isinstance(guarded, dict) or not isinstance(guarded.get("guarded_prediction"), str):
            raise ValueError("prediction row is missing the v9.1 guarded result")
        result[row_id] = guarded["guarded_prediction"]
    if not result:
        raise ValueError("prediction file has no rows")
    return result


def _pct(value: float | None) -> str:
    return "—" if value is None else f"{100 * value:.1f}%"


def render_report(result: dict[str, Any]) -> str:
    teachers = result["teacher_accuracy"]
    models = result["model_rates"]
    overlap = result["error_overlap"]
    teacher_names = list(teachers)
    model_names = list(models)
    lines = [
        "# S14：先生の初回ラベルとモデルの比較",
        "",
        f"セット：`{result['set_id']}`。初回ラベルと裁定後ラベルは非公開の `ai-bridge/labels/` に保持し、この報告には列ID・列名・値・個別ラベルを含めない。",
        f"全{result['total']}列のうち、裁定後ラベルが unknown の{result['excluded'].get('unknown', 0)}列と S の{result['excluded'].get('S', 0)}列を採点から除外。採点対象は{result['scored']}列。",
        "OK は正解、または正解が other の列で unknown と答えた場合。先生とモデルに同じ基準を適用した。モデルは保存済み予測の Guard v9.1 を使用し、再推論していない。",
        "",
        "## 先生の初回ラベル",
        "",
        "| 初回ラベル | OK 列 | 採点対象 | OK 率 |",
        "|---|---:|---:|---:|",
    ]
    for name in teacher_names:
        s = teachers[name]
        lines.append(f"| {name} | {s['correct']} | {s['total']} | {_pct(s['rate'])} |")
    lines += [
        "",
        "裁定後ラベルはこの2つの初回ラベルを照合して作られているため、先生のOK率は高く出る可能性があるため、独立な能力測定ではない。",
        "",
        "## モデルのOK率（種子平均）",
        "",
        f"| 層 | 列 | {' | '.join(model_names)} |",
        "|---|---:|" + "---:|" * len(model_names),
        f"| 全採点対象 | {result['scored']} | " + " | ".join(_pct(models[m]['overall']['mean_rate']) for m in model_names) + " |",
        f"| 先生2人の初回ラベルが一致 | {result['teacher_agreement']} | " + " | ".join(_pct(models[m]['agree']['mean_rate']) for m in model_names) + " |",
        f"| 先生2人の初回ラベルが不一致 | {result['teacher_disagreement']} | " + " | ".join(_pct(models[m]['disagree']['mean_rate']) for m in model_names) + " |",
        "",
        "初回ラベルの不一致は5列だけなので、その層のモデル率は参考値で、安定した性能比較には使えない。",
        "",
        "## 先生とモデルの誤りの重なり",
        "",
        "件数は3種子で数えた後の平均。列が種子間で重複している可能性があるため、固有列数ではない。",
        "",
        "| 初回ラベル | モデル | 先生OK・モデル誤り（平均件/種子） | 両方誤り（平均件/種子） |",
        "|---|---|---:|---:|",
    ]
    for teacher_name in teacher_names:
        for model_name in model_names:
            s = overlap[teacher_name][model_name]
            lines.append(
                f"| {teacher_name} | {model_name} | "
                f"{s['teacher_correct_model_wrong_mean']:.1f} | {s['both_wrong_mean']:.1f} |"
            )
    lines += [
        "",
        "## 解釈と次の確認",
        "",
        f"この測り方では先生の初回ラベルは{_pct(teachers[teacher_names[0]]['rate'])}・{_pct(teachers[teacher_names[1]]['rate'])}、モデルは全体で"
        + "・".join(_pct(models[m]['overall']['mean_rate']) for m in model_names)
        + "。モデルは先生の初回ラベルのOK率に届いていない。裁定の循環があるため差を独立ベンチマークと同じ強さで扱わず、能力差の参考値とする。",
        "封印セットの列は教材に使わない。先生OK・モデル誤りの傾向は学習側の候補で同じ分析をしてから教材化を検討する。",
        "",
        "入力：主セット #1 の保存済み予測（E5-base run 39506074807、mmBERT-small run 39502740378、各 job1〜3）と非公開ラベル3ファイル。予測の再実行なし。",
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create aggregate-only S14 teacher/model comparison.")
    parser.add_argument("--adjudicated", required=True)
    parser.add_argument("--claude", required=True)
    parser.add_argument("--chatgpt", required=True)
    parser.add_argument("--e5-base", nargs=3, required=True, metavar=("JOB1", "JOB2", "JOB3"))
    parser.add_argument("--mmbert-small", nargs=3, required=True, metavar=("JOB1", "JOB2", "JOB3"))
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)

    truth = load_labels(args.adjudicated)
    teachers = {"Claude": load_labels(args.claude), "ChatGPT": load_labels(args.chatgpt)}
    models = {
        "E5-base": [load_predictions(path) for path in args.e5_base],
        "mmBERT-small": [load_predictions(path) for path in args.mmbert_small],
    }
    result = summarize(truth, teachers, models)
    report = render_report(result)
    Path(args.out).write_text(report, encoding="utf-8")
    print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
