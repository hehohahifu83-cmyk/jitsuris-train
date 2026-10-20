"""学習・推論の計算資源と、入力の切り詰め率を、各仕事の manifest から表にする。2026-10-21。

使い方：
  python resource_table.py --group mmBERT-small=eval_reports/runs/39502740378:job1,job2,job3 \
                           --group E5-base=eval_reports/runs/39506074807:job1,job2,job3 --out bench/resources_mmbert_vs_e5base.md

読むのは manifest の timing（train_loop_seconds・peak_gpu_gib・inference_seconds・inference_rows）と
extra.token_stats（n・max_length・truncated）だけ。ラベル・予測・値は読まない。
推論の時間は、その学習を走らせた GPU（Kaggle の T4。評価は fp32）での値で、利用者の端末での速さではない。
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import compare_models as C


def parse_group(spec):
    """'名前=置き場:job1,job2' → (名前, 置き場, [job1, job2])。"""
    try:
        name, rest = spec.split("=", 1)
        folder, jobs = rest.rsplit(":", 1)
    except ValueError:
        raise SystemExit(f"--group は 名前=置き場:job1,job2 の形で書いてください：{spec}")
    jobs = [j.strip() for j in jobs.split(",") if j.strip()]
    if not name.strip() or not folder.strip() or not jobs:
        raise SystemExit(f"--group の名前・置き場・仕事のどれかが空です：{spec}")
    return name.strip(), folder.strip(), jobs


def load_manifest(folder, job):
    path = os.path.join(folder, f"{job}_manifest.json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def job_numbers(manifest, label=""):
    """1 つの仕事から、表に使う数だけを取り出す。足りない項目は理由つきで止める。"""
    timing = manifest.get("timing") or {}
    stats = (manifest.get("extra") or {}).get("token_stats") or {}
    need = ("train_loop_seconds", "peak_gpu_gib", "inference_seconds", "inference_rows")
    missing = [k for k in need if timing.get(k) is None]
    if missing or not stats:
        raise ValueError(f"{label} の manifest に必要な項目がありません：{missing or 'token_stats'}")
    sets = {}
    for name, seconds in timing["inference_seconds"].items():
        rows = timing["inference_rows"].get(name)
        if not rows:
            raise ValueError(f"{label} の {name} の行数がありません")
        stat = stats.get(name) or {}
        sets[name] = {"rows": rows, "ms_per_row": seconds / rows * 1000, "truncated_rate": stat.get("truncated_rate"), "max_length": stat.get("max_length")}
    train = stats.get("train") or {}
    return {"train_s": timing["train_loop_seconds"], "peak_gpu_gib": timing["peak_gpu_gib"],
            "amp": (manifest.get("amp") or {}).get("mode"), "amp_fallback": (manifest.get("amp") or {}).get("fallback_step"),
            "train_truncated_rate": train.get("truncated_rate"), "train_rows": train.get("n"), "sets": sets}


def spread(xs, digits=1):
    m, sd, lo, hi = C.mean_sd(xs)
    return f"{m:.{digits}f} ±{sd:.{digits}f}（{lo:.{digits}f}〜{hi:.{digits}f}）"


def render(groups, title="計算資源と入力の切り詰め（manifest から）"):
    """groups: [(名前, [job_numbers の結果, …])]"""
    names = [g[0] for g in groups]
    lines = [f"# {title}", "",
             "平均 ±標準偏差（最小〜最大）は仕事（種子）ごとの値から。推論の時間は学習を走らせた GPU（Kaggle の T4・評価は fp32）での値で、利用者の端末での速さではない。",
             "切り詰め率は、学習と同じ入力文を、その学習が使ったトークナイザで数えた、最大トークン数を超えて切られた行の割合（仕事ごとに同じ値になる）。", "",
             "## 学習", "", "| 項目 | " + " | ".join(names) + " |", "|---|" + "---|" * len(names)]
    rows = [("学習ループの秒数", lambda js: spread([j["train_s"] for j in js], 0)),
            ("GPU メモリの最大（GiB）", lambda js: spread([j["peak_gpu_gib"] for j in js], 2)),
            ("混合精度（fp16 の止まり）", lambda js: "・".join(sorted({str(j["amp"]) for j in js})) + ("（途中で fp32 に戻った仕事あり）" if any(j["amp_fallback"] is not None for j in js) else "（戻りなし）")),
            ("学習行の切り詰め率", lambda js: spread([100 * j["train_truncated_rate"] for j in js], 1) + " %" if all(j["train_truncated_rate"] is not None for j in js) else "—")]
    for label, fn in rows:
        lines.append(f"| {label} | " + " | ".join(fn(g[1]) for g in groups) + " |")
    set_names = list(groups[0][1][0]["sets"])
    for g in groups:
        for job in g[1]:
            if list(job["sets"]) != set_names:
                raise ValueError("群のあいだで試験の並びが違います")
    lines += ["", "## 推論と切り詰め（試験ごと）", "", "| 試験（行数） | " + " | ".join(f"{n}：1 行あたり ms" for n in names) + " | " + " | ".join(f"{n}：切り詰め率" for n in names) + " |",
              "|---|" + "---|" * (2 * len(names))]
    for s in set_names:
        rows_n = groups[0][1][0]["sets"][s]["rows"]
        ms = [spread([j["sets"][s]["ms_per_row"] for j in g[1]], 2) for g in groups]
        tr = []
        for g in groups:
            rates = [j["sets"][s]["truncated_rate"] for j in g[1]]
            tr.append(spread([100 * r for r in rates], 1) + " %" if all(r is not None for r in rates) else "—")
        lines.append(f"| {s}（{rows_n}） | " + " | ".join(ms) + " | " + " | ".join(tr) + " |")
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", action="append", required=True, help="名前=置き場:job1,job2,job3")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    groups = []
    for spec in a.group:
        name, folder, jobs = parse_group(spec)
        groups.append((name, [job_numbers(load_manifest(folder, j), f"{name}/{j}") for j in jobs]))
    text = render(groups)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
