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
    for r in rows:
        key = (r["dataset"], r["condition"], r["seed"])
        totals[key]["rows"] += 1
        if r["truth"] == "other":
            continue
        if r["prediction"] == "unknown":
            totals[key]["unknown"] += 1
            if r["confidence"] is not None and r["confidence"] >= 0.90:
                high_unknown.append(r)
        elif r["prediction"] != r["truth"]:
            totals[key]["wrong"] += 1
            if r["critical"]:
                totals[key]["critical"] += 1
            confusions[(r["dataset"], r["condition"])][(r["truth"], r["prediction"])] += 1
            normalized = re.sub(r"\s+", " ", r["column"].casefold()).strip()
            recurrent[(r["dataset"], r["condition"], normalized, r["truth"], r["prediction"])].add(r["seed"])

    lines = ["# ジツリス失敗分析（観測と仮説を分離）", "",
             f"生成日時 (UTC): {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
             f"使用ファイル数: {len({r['file'] for r in rows})} / 行数: {len(rows)}",
             "対象は dev220 / general / business / business2 / japan_procurement のみ。列名・正解・予測・上位確率だけを集計し、列の値は読み込んでいません。", "",
             "## 観測結果", "",
             "| 評価セット | 条件 | seed | 行数 | 誤り | 重大誤り | unknown |",
             "|---|---|---:|---:|---:|---:|---:|"]
    for (dataset, condition, seed), c in sorted(totals.items()):
        lines.append(f"| {dataset} | {condition} | {seed} | {c['rows']} | {c['wrong']} | {c['critical']} | {c['unknown']} |")

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

    lines += ["", "## 原因仮説（断定ではない）", ""]
    numeric_n = sum(n for (a, b), n in sum((c for (d, cond), c in confusions.items()), Counter()).items() if a in NUMERIC and b in NUMERIC)
    category_n = sum(n for (a, b), n in sum((c for (d, cond), c in confusions.items()), Counter()).items() if a == "category" or b == "category")
    lines.append(f"- 数値系クラス間（date/amount/quantity/rate/id）の取り違え: {numeric_n}件。列名の数値語・単位・周辺列の手掛かりのどれが不足したかはこの出力だけでは特定できません。次の教材候補は、評価例を流用せず、同じ値形式でラベルの違いを説明できる独立した出典つき対照例です。")
    lines.append(f"- categoryを含む取り違え: {category_n}件。有限分類語と数量/ID/自由文の境界、またはラベル定義との不一致が仮説です。元データとラベル根拠を別途監査するまで修正しません。")
    lines.append(f"- 高い上位確率（90%以上）なのに最終予測がunknown: {len(high_unknown)}件。確率出力とabstain/guard後の結果の差、またはラベル定義の曖昧さを調べる対象です。閾値はこの集計だけでは変更しません。")
    lines += ["", "## 次の検証案", "",
              "1. 今回の失敗行は学習データへコピーしない。出典独立の公開/合成教材を、ラベル定義と根拠付きで監査してから使う。",
              "2. GPUの基準条件は維持し、次の比較では訓練時の表現拡張（FT_AUG=1）だけを追加する。seed 1/2を両条件で比較する。",
              "3. 固定5セットのaccuracy・errors・critical errors・unknownsに加え、時間・最大GPUメモリを回収する。1.5ポイント未満は差なしとする。",
              "4. 原因が確定したとみなすのは、同じ失敗パターンの再検査と改善の再現が取れた場合だけ。ラベル変更・自動自己ラベル採用はしない。",
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
