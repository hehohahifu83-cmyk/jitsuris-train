"""学習し直し 第 1 段（bench/pool_training_b014_20261025.md）の判定の計算（2026-10-25 Claude）。

- 検証（教材庫）：job<N>_probs_val_pool_ft.json の正解率（score_real の「正」＝other の列を除く）と重大。種子 2 つの平均
- 未知見出し macro-F1：検証（一般・業務・業務2・日本の調達）のうち、条件ごとの学習行に見出しがない列、slice_eval.macro_f1(min_support=5)
- 学習行は学習した時の教材（commit 18c3eb1）で作る（ラベルの掃除の前）。使い方：python research/pool_training_b014_judge.py <18c3eb1 の作業ツリー>
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import slice_eval as S  # noqa: E402

RUN = os.path.join(ROOT, "eval_reports", "runs", "40188966177")
JOBS = {"(a) C1 と同じ教材": (1, 5), "(b) b014 まで": (2, 6), "(c) ＋題名": (3, 7), "(d) ＋難しい列を重く": (4, 8)}
VALS = ("val_general", "val_business", "val_business2", "val_japan_procurement")


def heads(tree, extra):
    code = "import json, slice_eval as S; p, h = S.train_sets_from_encoder_exp(); print(json.dumps(sorted(h)))"
    env = {**os.environ, "FT_VAL": "1", "FT_POOL": "1", **extra}
    out = subprocess.run([sys.executable, "-c", code], cwd=tree, env=env, capture_output=True, text=True, timeout=1800)
    if out.returncode:
        raise SystemExit(out.stderr[-2000:])
    return set(json.loads(out.stdout.strip().splitlines()[-1]))


def rows(job, ds):
    return json.load(open(os.path.join(RUN, f"job{job}_probs_{ds}_ft.json"), encoding="utf-8"))["rows"]


def main(tree):
    H = {"a": heads(tree, {"FT_POOL_EXCLUDE": "b013,b014"}), "b": heads(tree, {})}
    print("| 条件 | 検証（教材庫）正解 | 重大 | 未知見出し macro-F1 | 未知見出し 列 |\n|---|---:|---:|---:|---:|")
    for name, js in JOBS.items():
        hs = H["a"] if name.startswith("(a)") else H["b"]
        acc = crit = f1 = 0.0
        n_unk = 0
        for j in js:
            c = S.count(rows(j, "val_pool"))
            acc += c["correct"] / (c["correct"] + c["wrong"] + c["unknown"]) / len(js)   # score_real の「正」（other の列を除く）
            crit += c["critical"] / len(js)
            unk = [r for ds in VALS for r in rows(j, ds) if S.normalized_header(r["column"]) not in hs]
            f1 += S.macro_f1(unk, min_support=5)[0] / len(js)
            n_unk = len(unk)
        print(f"| {name} | {acc:.1%} | {crit:.1f} | {f1:.1%} | {n_unk} |")


if __name__ == "__main__":
    main(sys.argv[1])
