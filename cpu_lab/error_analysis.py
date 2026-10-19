#!/usr/bin/env python3
"""Create a deterministic, evidence-first error audit from allowed eval reports.

The report separates observed errors from hypotheses. It never reads raw values,
training data, blind sets, or evaluation sets 3/5/7, and it never edits labels or
training inputs.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ALLOWED = {"dev220", "general", "business", "business2", "japan_procurement"}
FORBIDDEN = re.compile(r"blind_set|(?:^|[^a-z0-9])(?:set[_-]?)?(?:3|5|7)(?:[^a-z0-9]|$)", re.I)
VALID = re.compile(r"(?:(job[12]|report)_)?probs_(dev220|general|business|business2|japan_procurement)_(ft|blend70)\.json$")
NUMERIC = {"date", "amount", "quantity", "rate", "id"}


def confidence(row: dict) -> float | None:
    top = row.get("top3") or []
    try:
        return float(top[0]["probability"]) if top else None
    except (KeyError, TypeError, ValueError):
        return None


def load_reports(root: Path) -> list[dict]:
    if FORBIDDEN.search(str(root)):
        raise ValueError("refusing prohibited evaluation path")
    files = sorted(p for p in root.rglob("*.json") if VALID.fullmatch(p.name))
    selected = []
    for path in files:
        if FORBIDDEN.search(path.name):
            raise ValueError(f"refusing prohibited report filename: {path.name}")
        match = VALID.fullmatch(path.name)
        assert match
        seed, dataset, condition = match.groups()
        seed = seed[-1] if seed else "single"
        if dataset not in ALLOWED:
            raise ValueError(f"dataset not allowlisted: {dataset}")
        obj = json.loads(path.read_text(encoding="utf-8"))
        rows = obj.get("rows")
        if not isinstance(rows, list):
            raise ValueError(f"missing rows array: {path.name}")
        for row in rows:
            if not isinstance(row, dict) or not {"column", "truth", "prediction"} <= row.keys():
                raise ValueError(f"malformed report row: {path.name}")
            selected.append({
                "file": path.name, "seed": seed, "dataset": dataset,
                "condition": condition, "column": str(row["column"]),
                "truth": str(row["truth"]), "prediction": str(row["prediction"]),
                "decision_reason": str(row.get("decision_reason") or "none"),
                "critical": bool(row.get("critical", False)), "confidence": confidence(row),
            })
    return selected


def analyze(rows: list[dict]) -> str:
    if not rows:
        return "# 失敗分析\n\n許可された評価レポートが見つかりません。原因分析は未実施です。\n"

    totals = defaultdict(Counter)
    confusions = defaultdict(Counter)
    recurrent = defaultdict(set)
    high_unknown = []
    cases = []
    for r in rows:
        key = (r["dataset"], r["condition"], r["seed"])
        totals[key]["rows"] += 1
        if r["truth"] == "other":
            if r["prediction"] not in ("unknown", "other"):
                totals[key]["other_ng"] += 1
                cases.append(("other_ng", r))
            continue
        if r["prediction"] == "unknown":
            totals[key]["unknown"] += 1
            cases.append(("unknown", r))
            if r["confidence"] is not None and r["confidence"] >= 0.90:
                high_unknown.append(r)
        elif r["prediction"] != r["truth"]:
            totals[key]["wrong"] += 1
            if r["critical"]:
                totals[key]["critical"] += 1
            cases.append(("critical" if r["critical"] else "wrong", r))
            confusions[(r["dataset"], r["condition"])][(r["truth"], r["prediction"])] += 1
            normalized = re.sub(r"\s+", " ", r["column"].casefold()).strip()
            recurrent[(r["dataset"], r["condition"], normalized, r["truth"], r["prediction"])].add(r["seed"])

    lines = ["# ジツリス失敗分析（観測と仮説を分離）", "",
             f"生成日時 (UTC): {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
             f"使用ファイル数: {len({r['file'] for r in rows})} / 行数: {len(rows)}",
             "対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。", "",
             "## 観測結果", "",
             "| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown | other見落とし |",
             "|---|---|---:|---:|---:|---:|---:|---:|"]
    for (dataset, condition, seed), c in sorted(totals.items()):
        lines.append(f"| {dataset} | {condition} | {seed} | {c['rows']} | {c['wrong']} | {c['critical']} | {c['unknown']} | {c['other_ng']} |")

    lines += ["", "### 取り違えの頻度", ""]
    for (dataset, condition), counts in sorted(confusions.items()):
        top = ", ".join(f"{a}→{b}: {n}" for (a, b), n in counts.most_common(8)) or "なし"
        lines.append(f"- {dataset} / {condition}: {top}")

    repeated = [(k, v) for k, v in recurrent.items() if len(v) >= 2]
    lines += ["", "### seedをまたいで再発した誤り", ""]
    if repeated:
        for (dataset, condition, column, truth, pred), seeds in sorted(repeated):
            lines.append(f"- {dataset} / {condition}: `{column}`、{truth}→{pred}（{', '.join('seed ' + s for s in sorted(seeds))}）")
    else:
        lines.append("同じ列名・正解・予測の誤りは複数seedで確認されませんでした。")

    lines += ["", "### 全ての誤り・unknown（評価例。学習に転用しない）", "",
              "| 区分 | セット | 条件 | seed | 列名 | 正解 | 予測 | 理由 | 上位確率 | 重大 |",
              "|---|---|---|---:|---|---|---|---:|---:|"]
    for kind, r in sorted(cases, key=lambda item: (item[1]["dataset"], item[1]["condition"], item[1]["seed"], item[0], item[1]["column"].casefold())):
        col = r["column"].replace("|", "\\|").replace("`", "'")
        p = f"{r['confidence']:.4f}" if r["confidence"] is not None else "n/a"
        lines.append(f"| {kind} | {r['dataset']} | {r['condition']} | {r['seed']} | {col} | {r['truth']} | {r['prediction']} | {p} | {'yes' if r['critical'] else 'no'} |")

    reason_counts = Counter(r["decision_reason"] for _, r in cases if r["prediction"] == "unknown")
    lines += ["", "### unknown の判定理由", ""]
    if reason_counts:
        lines.extend(f"- {reason}: {count}件" for reason, count in sorted(reason_counts.items()))
    else:
        lines.append("unknown の行はありません。")

    lines += ["", "## 原因仮説（断定ではない）", ""]
    numeric_n = sum(n for (a, b), n in sum((c for (d, cond), c in confusions.items()), Counter()).items() if a in NUMERIC and b in NUMERIC)
    category_n = sum(n for (a, b), n in sum((c for (d, cond), c in confusions.items()), Counter()).items() if a == "category" or b == "category")
    lines.append(f"- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: {numeric_n}件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。")
    lines.append(f"- categoryを含む取り違え: {category_n}件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。")
    lines.append(f"- 高い上位確率（90%以上）なのに最終予測がunknown: {len(high_unknown)}件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。")
    lines += ["", "## 次の検証案", "",
              "1. 今回の失敗行や列名は学習データへコピーしない。教材を追加するときは評価データと独立した出典を使い、ラベル定義と根拠を監査する。",
              "2. 次の学習条件を選ぶ前に KAGGLE_LOG.md と FINETUNE_RESULTS.md を確認し、完了済みの条件を新規実験として重ねない。条件の選択と対照seedを実験計画書に記録する。",
              "3. 一回に一要因だけ変え、seed 1/2を揃える。固定5セットのaccuracy・errors・critical errors・unknowns・時間・最大GPUメモリを比較し、1.5ポイント未満は差なしとする。",
              "4. 失敗原因は仮説として扱う。改善を繰り返し確認するまで因果を断定せず、ラベル変更・自動疑似ラベル採用はしない。",
              "", "## 制約", "",
              "これは相関・再発パターンの監査で、因果の証明ではありません。出力JSONにない列値、同表全体、教材の重複/出典、前処理実体は確認していません。盲検データと禁止セットは検索・読込・学習に使用していません。", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    try:
        report = analyze(load_reports(args.reports))
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(report, encoding="utf-8")
        else:
            print(report, end="")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
