"""保存済みチェックポイントを学習なしで再評価し、旧確率と照合する。"""
from __future__ import annotations
import json, os, re, unicodedata
from pathlib import Path
from typing import Any

DATASETS = ("dev220", "general", "business", "business2", "japan_procurement")
CONDITIONS = {"ft": 1.0, "blend70": 0.7}
TOLERANCE = 0.005

def find_checkpoint(root: str | Path) -> Path:
    root = Path(root)
    found = []
    for labels in root.rglob("labels.json"):
        p = labels.parent
        has_weights = any((p / name).is_file()
                          for name in ("model.safetensors", "pytorch_model.bin"))
        has_weights = has_weights or bool(list(p.glob("model-*.safetensors")))
        if (p / "config.json").is_file() and has_weights:
            found.append(p)
    found = sorted(set(found))
    if len(found) != 1:
        raise RuntimeError(f"expected exactly one complete checkpoint; found {found}")
    return found[0]

def compare_rows(prior: list[dict[str, Any]], current: list[dict[str, Any]],
                 tolerance: float = TOLERANCE) -> dict[str, Any]:
    if len(prior) != len(current):
        raise AssertionError(f"row count changed: {len(prior)} != {len(current)}")
    max_drift, mismatches = 0.0, []
    for i, (old, new) in enumerate(zip(prior, current)):
        old_pred = old.get("guarded_prediction", old.get("prediction"))
        new_pred = new.get("guarded_prediction", new.get("prediction"))
        if (old.get("truth") != new.get("truth") or old.get("column") != new.get("column")
                or old_pred != new_pred):
            mismatches.append({"index": i, "kind": "row_identity_or_decision"})
            continue
        a, b = old.get("top3") or [], new.get("top3") or []
        if not a or not b or a[0].get("label") != b[0].get("label"):
            mismatches.append({"index": i, "kind": "top1_label"})
            continue
        if len(a) != len(b):
            mismatches.append({"index": i, "kind": "top3_length"})
            continue
        # Rank probabilities should match, but lower ranks may swap when their
        # probabilities are effectively tied at CPU/BLAS rounding precision.
        drift = max((abs(float(x["probability"]) - float(y["probability"]))
                     for x, y in zip(a, b)), default=0.0)
        max_drift = max(max_drift, drift)
        if drift > tolerance:
            mismatches.append({"index": i, "kind": "probability_drift", "max_drift": drift})
    return {"rows": len(prior), "max_probability_drift": max_drift,
            "tolerance": tolerance, "mismatches": mismatches, "passed": not mismatches}

def one_report(root: Path, dataset: str, condition: str) -> Path:
    expected = f"job1_probs_{dataset}_{condition}.json"
    hits = sorted(root.rglob(expected))
    if len(hits) != 1:
        raise RuntimeError(f"expected exactly one prior report {expected}; found {hits}")
    return hits[0]

def run(checkpoint_root: str, prior_root: str, output_root: str) -> None:
    os.environ["FT_CTX_UNIT"] = "1"
    import gen, features
    gen.HARD_NUMERIC = 0.0
    features.USE_NUM2 = True
    import numpy as np, torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    from encoder_exp import rows, tests, text
    from train3 import mat, decide_with_details
    from llm_baseline import score_real
    from evaluation_records import assert_metrics_match, build_record, is_issue

    checkpoint = find_checkpoint(checkpoint_root)
    labels = json.loads((checkpoint / "labels.json").read_text(encoding="utf-8"))
    if labels != sorted(set(row[2] for row in rows)):
        raise ValueError("checkpoint labels do not match current training labels")
    tokenizer = AutoTokenizer.from_pretrained(checkpoint, local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(checkpoint, local_files_only=True)
    if model.config.num_labels != len(labels):
        raise ValueError("checkpoint classifier dimension does not match labels")
    model.to("cpu").eval()
    prefix = "query: "  # training run used multilingual-e5-base
    probs, batch_size = {}, 32
    with torch.inference_mode():
        for name, eval_rows in tests.items():
            chunks = []
            for start in range(0, len(eval_rows), batch_size):
                batch = eval_rows[start:start + batch_size]
                enc = tokenizer([text(row, prefix) for row in batch], truncation=True,
                                max_length=128, padding=True, return_tensors="pt")
                chunks.append(torch.softmax(model(**enc).logits.float(), -1).cpu().numpy())
            probs[name] = np.vstack(chunks)
    from sklearn.linear_model import LogisticRegression
    lr = LogisticRegression(C=8, max_iter=3000).fit(mat(rows), np.array([r[2] for r in rows]))
    if list(lr.classes_) != labels:
        raise ValueError("sparse baseline class order differs from checkpoint labels")
    names = {"開発用220": "dev220", "本物（一般）": "general",
             "本物（業務）": "business", "本物（業務2）": "business2",
             "本物（日本の調達）": "japan_procurement"}
    output, comparisons, metric_lines = Path(output_root), [], []
    output.mkdir(parents=True, exist_ok=True)
    for test_name, eval_rows in tests.items():
        dataset = names.get(test_name)
        if dataset not in DATASETS:
            raise RuntimeError(f"unexpected evaluation dataset: {test_name}")
        p_sparse = lr.predict_proba(mat(eval_rows))
        for condition, weight in CONDITIONS.items():
            p = weight * probs[test_name] + (1 - weight) * p_sparse
            details = decide_with_details(labels, p, eval_rows)
            top = np.argsort(p, axis=1)[:, ::-1][:, :3]
            records = []
            for i, (row, detail) in enumerate(zip(eval_rows, details)):
                top3 = [{"label": labels[int(j)], "probability": round(float(p[i, j]), 6)}
                        for j in top[i]]
                header = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(row[0])).strip()).casefold()
                records.append(build_record(index=i, dataset=dataset, seed="1",
                    condition=condition, column=header, truth=row[2],
                    guarded_prediction=detail["guarded_prediction"], top3=top3,
                    decision_reason=detail["decision_reason"]))
            metrics = score_real([r["guarded_prediction"] for r in records],
                                 [r["truth"] for r in records])
            assert_metrics_match(records, metrics)
            meta = {"schema_version": 3, "test": test_name, "dataset": dataset,
                    "seed": "1", "condition": condition, "condition_id": condition,
                    "source_run": 39241962638}
            (output / f"probs_{dataset}_{condition}.json").write_text(
                json.dumps({**meta, "rows": records}, ensure_ascii=False,
                           separators=(",", ":")) + "\n", encoding="utf-8")
            (output / f"errors_{dataset}_{condition}.json").write_text(
                json.dumps({**meta, "errors": [r for r in records if is_issue(r)]},
                           ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
            prior = one_report(Path(prior_root), dataset, condition)
            old = json.loads(prior.read_text(encoding="utf-8"))
            check = compare_rows(old.get("rows", []), records)
            check.update({"dataset": dataset, "condition": condition,
                          "prior_file": str(prior.relative_to(prior_root))})
            comparisons.append(check)
            if not check["passed"]:
                raise AssertionError(f"prior parity failed: {check}")
            metric_lines.append(f"| {dataset} | {condition} | {metrics['acc_all']:.1%} | "
                f"{metrics['wrong']} | {metrics['unknown']} | {metrics['critical']} | "
                f"{metrics['n']} | {check['max_probability_drift']:.6f} |")
    if len(comparisons) != 10:
        raise RuntimeError(f"expected 10 comparisons, got {len(comparisons)}")
    (output / "comparison.json").write_text(json.dumps(
        {"source_run": 39241962638, "tolerance": TOLERANCE, "comparisons": comparisons},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = ["# 保存済みモデルの推論評価（学習なし）", "",
        "- source checkpoint: Actions run 39241962638, job1, seed 1",
        "- training configuration: multilingual-e5-base, 2 epochs",
        "- fixed development datasets only; ft and blend70; 10 row-level comparisons",
        "- comparison includes row order, normalized header, truth, final decision, and top-1 label",
        "- lower top-3 ranks may swap only when rank-aligned probabilities stay within tolerance",
        f"- top-3 probabilities must differ by at most {TOLERANCE}",
        "- schema version 3 records include decision reasons; column values are not saved.",
        "", "| dataset | condition | accuracy | wrong | unknown | critical | n (truth other excluded) | max drift |",
        "|---|---:|---:|---:|---:|---:|---:|---:|", *metric_lines, "",
        "n excludes rows whose truth is other; all row records were included in parity checks.",
        "All ten comparisons passed."]
    (output / "CHECKPOINT_EVALUATION.md").write_text("\n".join(report) + "\n", encoding="utf-8")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--prior", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run(args.checkpoint, args.prior, args.output)
