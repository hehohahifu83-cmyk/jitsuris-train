"""Kaggle の依頼（args.txt）を「並べて流す仕事」に分ける。torch に依存しない純粋な関数だけ。

書き方：  <モデル> <周数> FT_xxx=値 … ++ FT_yyy=値 …
- 「++」で区切ると、GPU 1 枚につき 1 つの仕事を同時に流す（Kaggle の T4 は 2 枚）。
- 2 つめ以降の仕事は、モデルと周数を 1 つめから引き継ぐ。変えられるのは FT_ の設定と（必要なら）周数だけ。モデルは同じ。
- FT_ で始まる語は、すべて環境変数として学習側に渡す（以前は一部の名前しか渡らず、FT_SEED などが無視されていた）。
"""
from __future__ import annotations

import re

ENV_TOKEN = re.compile(r"^(FT_[A-Z0-9_]+)=(.*)$")
SEPARATOR = "++"


def split_jobs(tokens, max_jobs=2):
    """語の並び → 仕事のリスト [{'args': [モデル, 周数...], 'env': {...}}, ...]。"""
    groups, cur = [], []
    for t in tokens:
        if t == SEPARATOR:
            groups.append(cur); cur = []
        else:
            cur.append(t)
    groups.append(cur)
    if len(groups) > max_jobs:
        raise ValueError(f"仕事の数は GPU の枚数 {max_jobs} まで（今は {len(groups)} 個）")

    def parse(group):
        args, env = [], {}
        for t in group:
            m = ENV_TOKEN.match(t)
            if m:
                env[m.group(1)] = m.group(2)
            else:
                args.append(t)
        return args, env

    first_args, first_env = parse(groups[0])
    if not first_args:
        raise ValueError("1 つめの仕事にモデルがない")
    jobs = [{"args": first_args, "env": first_env}]
    for g in groups[1:]:
        args, env = parse(g)
        if len(args) > 1 or (args and not re.fullmatch(r"\d+(\.\d+)?", args[0])):
            raise ValueError(f"2 つめ以降の仕事に書けるのは FT_ の設定と周数だけ：{args}")
        job_args = list(first_args)
        if args:
            if len(job_args) < 2:
                job_args.append(args[0])
            else:
                job_args[1] = args[0]
        jobs.append({"args": job_args, "env": env})
    return jobs


def job_environment(base_env, job, index, n_gpu, pin=True):
    """仕事ごとの環境変数。GPU があれば 1 つの仕事に 1 枚だけ見せる（番号は 0 から）。pin=False なら全部見せる。"""
    env = dict(base_env)
    env.update(job["env"])
    if n_gpu > 0 and pin:
        env["CUDA_VISIBLE_DEVICES"] = str(index % n_gpu)
    return env


# ---- 実際に流す部分（Kaggle の run.py から使う）----
import os
import subprocess
import sys
import threading


def prepare_workdir(root, index, total):
    """仕事が 1 つなら root のまま。2 つ以上なら root/jobN を作り、root の中身へのリンクを置く。
    出力（ft_out・FINETUNE_RESULTS.md・errors_*.json など）は各 jobN の中にできるので、仕事同士で上書きし合わない。"""
    if total == 1:
        return root
    d = os.path.join(root, f"job{index + 1}")
    os.makedirs(d, exist_ok=True)
    for name in os.listdir(root):
        if re.fullmatch(r"job\d+", name):
            continue
        link = os.path.join(d, name)
        if not os.path.lexists(link):
            os.symlink(os.path.join(root, name), link)
    return d


def _pump(proc, label):
    for line in proc.stdout:
        sys.stdout.write(f"[{label}] {line}")
        sys.stdout.flush()


def run_jobs(specs, script, base_env, root, n_gpu):
    """全部の仕事を同時に始めて、全部の終了を待つ。返すのは終了コードの並び。"""
    procs, pumps = [], []
    for i, spec in enumerate(specs):
        wd = prepare_workdir(root, i, len(specs))
        env = job_environment(base_env, spec, i, n_gpu, pin=len(specs) > 1)
        cmd = [sys.executable, os.path.join(root, script), *spec["args"]]
        if len(specs) == 1:
            procs.append(subprocess.Popen(cmd, env=env, cwd=wd))
        else:
            p = subprocess.Popen(cmd, env=env, cwd=wd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            procs.append(p)
            t = threading.Thread(target=_pump, args=(p, f"仕事{i + 1}"), daemon=True)
            t.start(); pumps.append(t)
    codes = [p.wait() for p in procs]
    for t in pumps:
        t.join(timeout=10)
    return codes
