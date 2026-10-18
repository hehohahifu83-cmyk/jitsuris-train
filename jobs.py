"""Kaggle の依頼（args.txt）を「並べて流す仕事」に分ける。torch に依存しない純粋な関数だけ。

書き方：  <モデル> <周数> FT_xxx=値 … ++ FT_yyy=値 … ++ …
- 「++」で区切ると仕事が増える。GPU 1 枚につき 1 つの仕事を同時に流し（Kaggle の T4 は 2 枚）、枚数を超えた分は空いた GPU から順に流す。
- 2 つめ以降の仕事は、モデル・周数・FT_ の設定を 1 つめから引き継ぐ。変えたいものだけ書けばよい（同じ名前を書けば上書き）。
  引き継ぎたくない設定は `FT_名前=`（値なし）で外す（環境変数ごと無くなり、既定に戻る）。周数を変えたいときは数字を 1 つ書く。モデルは変えられない。
- FT_ で始まる語は、すべて環境変数として学習側に渡す（以前は一部の名前しか渡らず、FT_SEED などが無視されていた）。
- 仕事の数は MAX_JOBS まで。
"""
from __future__ import annotations

import re

ENV_TOKEN = re.compile(r"^(FT_[A-Z0-9_]+)=(.*)$")
SEPARATOR = "++"
MAX_JOBS = 8  # 1 回の依頼に並べられる仕事の数（GPU の枚数を超えた分は順番待ち）


def split_jobs(tokens, max_jobs=MAX_JOBS):
    """語の並び → 仕事のリスト [{'args': [モデル, 周数...], 'env': {...}}, ...]。env は引き継ぎを済ませた最終の設定。"""
    groups, cur = [], []
    for t in tokens:
        if t == SEPARATOR:
            groups.append(cur); cur = []
        else:
            cur.append(t)
    groups.append(cur)
    if len(groups) > max_jobs:
        raise ValueError(f"仕事の数は {max_jobs} まで（今は {len(groups)} 個）")

    def parse(group):
        args, env = [], {}
        for t in group:
            m = ENV_TOKEN.match(t)
            if m:
                env[m.group(1)] = m.group(2)
            else:
                args.append(t)
        return args, env

    def effective(env):
        return {k: v for k, v in env.items() if v != ""}   # 値なし（FT_X=）は「外す」の意味

    first_args, first_env = parse(groups[0])
    if not first_args:
        raise ValueError("1 つめの仕事にモデルがない")
    first_env = effective(first_env)
    jobs = [{"args": first_args, "env": first_env}]
    for g in groups[1:]:
        args, own = parse(g)
        if len(args) > 1 or (args and not re.fullmatch(r"\d+(\.\d+)?", args[0])):
            raise ValueError(f"2 つめ以降の仕事に書けるのは FT_ の設定と周数だけ：{args}")
        job_args = list(first_args)
        if args:
            if len(job_args) < 2:
                job_args.append(args[0])
            else:
                job_args[1] = args[0]
        merged = dict(first_env)
        merged.update(own)
        jobs.append({"args": job_args, "env": effective(merged)})
    return jobs


def describe(specs, i):
    """見出し用の短い説明。1 つめは設定すべて、2 つめ以降は 1 つめとの違いだけ。"""
    env = specs[i]["env"]
    if i == 0:
        return " ".join(f"{k}={v}" for k, v in env.items()) or "（設定なし）"
    base = specs[0]["env"]
    diff = [f"{k}={v}" for k, v in env.items() if base.get(k) != v] + [f"{k}=（外す）" for k in base if k not in env]
    if specs[i]["args"][1:] != specs[0]["args"][1:]:
        diff.insert(0, "周数=" + " ".join(specs[i]["args"][1:]))
    return "仕事1との違い：" + (" ".join(diff) if diff else "なし")


def job_environment(base_env, job, index, n_gpu, pin=True):
    """仕事ごとの環境変数。index は流す GPU の番号（0 から）。GPU があれば 1 つの仕事に 1 枚だけ見せる。pin=False なら全部見せる。"""
    env = dict(base_env)
    env.update(job["env"])
    if n_gpu > 0 and pin:
        env["CUDA_VISIBLE_DEVICES"] = str(index % n_gpu)
    return env


# ---- 実際に流す部分（Kaggle の run.py から使う）----
import os
import shutil
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
    """仕事を流して全部の終了を待つ。返すのは仕事ごとの終了コードの並び（依頼の並びの順）。

    同時に流すのは GPU の枚数まで（GPU が無ければ 1 つずつ）。枚数を超えた仕事は、空いた GPU から順に流す。
    仕事が 1 つなら root で直接流し、2 つ以上なら root/jobN の中で流す（出力が上書きし合わない）。
    2 つ以上のときは、仕事が終わるたびに学習済みモデル（ft_out）を消す（ディスクを使い切らないため。評価と確率の一覧は残る）。
    1 つの仕事が失敗しても、残りの仕事は流し続ける。
    """
    if len(specs) == 1:
        wd = prepare_workdir(root, 0, 1)
        env = job_environment(base_env, specs[0], 0, n_gpu, pin=False)
        return [subprocess.Popen([sys.executable, os.path.join(root, script), *specs[0]["args"]], env=env, cwd=wd).wait()]
    workers = max(1, min(n_gpu, len(specs)))
    pin = workers > 1
    codes = [None] * len(specs)
    lock = threading.Lock()
    nxt = [0]

    def take():
        with lock:
            i = nxt[0]
            if i >= len(specs):
                return None
            nxt[0] += 1
            return i

    def worker(gpu):
        while True:
            i = take()
            if i is None:
                return
            label = f"仕事{i + 1}"
            wd = None
            try:
                wd = prepare_workdir(root, i, len(specs))
                env = job_environment(base_env, specs[i], gpu, n_gpu, pin=pin)
                sys.stdout.write(f"[{label}] 開始（GPU {gpu if pin else '全部'}）{describe(specs, i)}\n"); sys.stdout.flush()
                p = subprocess.Popen([sys.executable, os.path.join(root, script), *specs[i]["args"]], env=env, cwd=wd,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
                _pump(p, label)
                p.stdout.close()
                codes[i] = p.wait()
            except Exception as e:   # 起動できない・読めないなど
                sys.stdout.write(f"[{label}] 流せなかった：{e!r}\n"); sys.stdout.flush()
                codes[i] = 1
            finally:
                if wd:
                    shutil.rmtree(os.path.join(wd, "ft_out"), ignore_errors=True)
                sys.stdout.write(f"[{label}] 終了（終了コード {codes[i]}）\n"); sys.stdout.flush()

    threads = [threading.Thread(target=worker, args=(g,)) for g in range(workers)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return codes
