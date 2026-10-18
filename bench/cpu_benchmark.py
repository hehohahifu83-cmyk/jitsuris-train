"""Repeatable CPU benchmark for FT token caching and thread counts."""
from __future__ import annotations

import os
import re
import statistics
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "bench" / "cpu-runs"
ORDER = (("A1", 0, "full"), ("B1", 1, "full"), ("C1", 1, "half"),
         ("C2", 1, "half"), ("B2", 1, "full"), ("A2", 0, "full"))


def parse_run(stdout: str) -> tuple[float, float, list[float]]:
    rows = re.findall(r"\| 学習 ([0-9.]+)秒・評価 ([0-9.]+)秒 \|", stdout)
    losses = [float(x) for x in re.findall(r"^step_loss \d+ ([0-9.]+)$", stdout, re.M)]
    if not rows:
        raise ValueError("benchmark output did not contain train/eval timing")
    return float(rows[-1][0]), float(rows[-1][1]), losses


def compare_losses(a: list[float], b: list[float]) -> bool:
    return len(a) >= 20 and len(b) >= 20 and [round(x, 3) for x in a[:20]] == [round(x, 3) for x in b[:20]]


def main() -> int:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    available = int(subprocess.check_output([sys.executable, "-c", "from cpu_speed import available_cpu_count; print(available_cpu_count())"], cwd=ROOT, text=True).strip())
    thread_counts = {"full": available, "half": max(1, available // 2)}
    results: dict[str, tuple[float, float, list[float]]] = {}
    for name, cache, thread_key in ORDER:
        env = os.environ.copy()
        env.update({"FT_CPU_CACHE": str(cache), "FT_CPU_THREADS": str(thread_counts[thread_key]),
                    "FT_LIMIT": "1500", "FT_SEED": "1", "FT_EVAL": "dev220", "FT_TRACE_LOSS": "20"})
        print(f"Starting {name}: cache={cache}, threads={thread_counts[thread_key]}", flush=True)
        log_path = LOG_DIR / f"{name}.log"
        with log_path.open("w", encoding="utf-8") as log:
            proc = subprocess.Popen([sys.executable, "finetune_exp.py", "intfloat/multilingual-e5-small", "1"], cwd=ROOT,
                                    env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
            output_lines = []
            assert proc.stdout is not None
            for line in proc.stdout:
                print(f"[{name}] {line}", end="", flush=True)
                log.write(line); log.flush(); output_lines.append(line)
            code = proc.wait()
        output = "".join(output_lines)
        if code:
            raise SystemExit(f"{name} failed with exit code {code}")
        results[name] = parse_run(output)
        print(f"{name}: train={results[name][0]:.1f}s eval={results[name][1]:.1f}s threads={thread_counts[thread_key]}", flush=True)

    loss_checks = {"A1/B1": compare_losses(results["A1"][2], results["B1"][2]),
                   "A2/B2": compare_losses(results["A2"][2], results["B2"][2])}
    groups = {"A cache off/full threads": [results["A1"][0], results["A2"][0]],
              "B cache on/full threads": [results["B1"][0], results["B2"][0]],
              "C cache on/half threads": [results["C1"][0], results["C2"][0]]}
    means = {k: statistics.mean(v) for k, v in groups.items()}
    noise = max(max(v) - min(v) for v in groups.values())
    base = means["A cache off/full threads"]
    cache_gain = base - means["B cache on/full threads"]
    cache_pct = 100 * cache_gain / base if base else 0
    decision = "速くなった" if cache_pct >= 10 and cache_gain > noise and all(loss_checks.values()) else "差なし／判定保留"
    lines = ["# CPU training benchmark", "", f"Runner CPUs: {available}; threads full={thread_counts['full']}, half={thread_counts['half']}",
             "Settings: e5-small, 1 epoch, first 1500 training rows, FT_SEED=1, dev220 evaluation only.",
             "Timings exclude model loading; training and evaluation are reported separately.", "",
             "| Run | Cache | Threads | Train seconds | Eval seconds |", "|---|---:|---:|---:|---:|"]
    for name, cache, thread_key in ORDER:
        train_s, eval_s, _ = results[name]
        lines.append(f"| {name} | {cache} | {thread_counts[thread_key]} | {train_s:.1f} | {eval_s:.1f} |")
    lines += ["", "## First 20 loss checks", "", "| Pair | Same to 3 decimals |", "|---|---|"]
    lines += [f"| {pair} | {'yes' if same else 'no'} |" for pair, same in loss_checks.items()]
    lines += ["", "## Cache comparison", "", f"A mean: {base:.1f}s; B mean: {means['B cache on/full threads']:.1f}s; measured gain: {cache_pct:.1f}%.",
              f"Largest two-run spread among groups: {noise:.1f}s. Decision: **{decision}**.",
              "", "Evaluation time is shown separately and is not included in the training comparison."]
    (ROOT / "bench" / "cpu_benchmark_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
