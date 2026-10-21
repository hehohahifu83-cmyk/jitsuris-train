"""独立評価の集計（S6-5、指示役 Claude、2026-10-21）。evaluate_independent.py score の出力から、
SEALED_EVAL_PROTOCOL.md 第 5・6 章の表（表単位ブートストラップの区間・層別・判定）を作る。

- 入力は score の出力（<run>_probs_<dataset>_ft.json）だけ。ラベルは非公開の置き場で score したものを渡す。
- 出力は集計だけ（列ごとのラベル・列 ID・値は書かない）。公開リポジトリの bench/ に置いてよい形。
- 見出しの既知／未知は、重みを作った学習コミットの encoder_exp の学習行で決める（--train-headers に
  {"pairs": [[見出し, ラベル], …], "headers": [見出し, …]} を渡す。作り方は末尾の再現の手順）。

使い方：
  python independent_report.py --set <主セット.json> --train-headers <train_headers.json>
    --labels 名前=<ラベル.json> … --scored 名前=<基準線の置き場>,<候補の置き場> …（--labels と同じ名前・同じ順）
    --primary 裁定後 --baseline E5-base --candidate mmBERT-small [--jobs job1,job2,job3] [--reps 10000] [--out bench/….md]
"""
from __future__ import annotations

import argparse
import json
import os
import random
from collections import Counter, defaultdict

from evaluation_records import NUMERIC
from slice_eval import SLICES, normalized_header

OK = {"correct", "other_ok"}
CRIT = ("date", "amount", "quantity", "rate", "id")


def load_scored(dir_, jobs, dataset="independent_main"):
    out = {}
    for job in jobs:
        with open(os.path.join(dir_, f"{job}_probs_{dataset}_ft.json"), encoding="utf-8") as fh:
            out[job] = json.load(fh)["rows"]
    return out


def attach(rows, kept_ids):
    """score は除外した列を飛ばして index を振るので、除外後の id の並びで結び直す。"""
    if len(rows) != len(kept_ids):
        raise ValueError("score の行数とラベルの採点対象の数が合わない")
    return {i: r for i, r in zip(kept_ids, rows)}


def ok_rate(rows):
    return sum(r["outcome"] in OK for r in rows) / len(rows) if rows else float("nan")


def pct(x, d=1):
    return "—" if x != x else f"{100 * x:.{d}f}%"


def quantile(xs, q):
    xs = sorted(xs)
    k = (len(xs) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (k - lo)


class Model:
    def __init__(self, name, by_job):
        self.name, self.by_job = name, by_job   # job → {id: record}

    def rows(self, job, ids):
        return [self.by_job[job][i] for i in ids]

    def mean_ok(self, ids):
        return sum(ok_rate(self.rows(j, ids)) for j in self.by_job) / len(self.by_job)

    def mean_crit(self, ids):
        return sum(sum(r["critical"] for r in self.rows(j, ids)) for j in self.by_job) / len(self.by_job)


def bootstrap(models, ids, table_of, reps, seed=20261021):
    """表を復元抽出。各回で各モデルの（種子平均の）OK 率と差を記録。"""
    by_table = defaultdict(list)
    for i in ids:
        by_table[table_of[i]].append(i)
    tables = sorted(by_table)
    rng = random.Random(seed)
    stats = {m.name: [] for m in models}
    diffs = []
    for _ in range(reps):
        pick = [i for t in (rng.choice(tables) for _ in tables) for i in by_table[t]]
        vals = [m.mean_ok(pick) for m in models]
        for m, v in zip(models, vals):
            stats[m.name].append(v)
        diffs.append(vals[1] - vals[0])
    return stats, diffs


def coverage_at(model, ids, truth, target=0.99):
    """重大 5 種類：上位 1 の確率の下限 t を動かし、精度 ≥ target で答えられる正解 5 種類の列の割合（種子平均）。
    答え＝見張りの後の予測が 5 種類のどれかで、上位 1 の確率 ≥ t。精度＝答えのうち正解の割合。"""
    n_crit = sum(truth[i] in CRIT for i in ids)
    best = []
    for job in model.by_job:
        rows = [(model.by_job[job][i], truth[i]) for i in ids]
        answered = sorted(((r["top3"][0]["probability"], r["guarded_prediction"] == t, t in CRIT)
                           for r, t in rows if r["guarded_prediction"] in CRIT), reverse=True)
        cov, hit = 0.0, 0
        for k, (_, correct, _) in enumerate(answered, 1):
            hit += correct
            if hit / k >= target:
                cov = sum(c for _, c, _ in answered[:k]) / n_crit
        best.append(cov)
    return sum(best) / len(best)


def confusion(model, ids, truth):
    cols = CRIT + ("その他の種類", "不明")
    m = {t: Counter() for t in CRIT}
    for job in model.by_job:
        for i in ids:
            t = truth[i]
            if t not in CRIT:
                continue
            p = model.by_job[job][i]["guarded_prediction"]
            m[t][p if p in CRIT else ("不明" if p == "unknown" else "その他の種類")] += 1
    lines = [f"| 正解＼予測（{model.name}、{len(model.by_job)} 種子の合計） | " + " | ".join(cols) + " |",
             "|---|" + "---:|" * len(cols)]
    for t in CRIT:
        lines.append(f"| {t} | " + " | ".join(str(m[t][c]) for c in cols) + " |")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", required=True)
    ap.add_argument("--train-headers", required=True)
    ap.add_argument("--labels", action="append", required=True)
    ap.add_argument("--scored", action="append", required=True)
    ap.add_argument("--primary", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--jobs", default="job1,job2,job3")
    ap.add_argument("--reps", type=int, default=10000)
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    jobs = a.jobs.split(",")
    with open(a.set, encoding="utf-8") as fh:
        cols = json.load(fh)["columns"]
    meta = {c["id"]: c for c in cols}
    order = [c["id"] for c in cols]
    with open(a.train_headers, encoding="utf-8") as fh:
        th = json.load(fh)
    train_pairs = {tuple(p) for p in th["pairs"]}
    train_heads = set(th["headers"])
    labels = {}
    for spec in a.labels:
        name, path = spec.split("=", 1)
        with open(path, encoding="utf-8") as fh:
            labels[name] = json.load(fh)
    scored, manifests = {}, {}
    for spec in a.scored:
        name, dirs = spec.split("=", 1)
        base_dir, cand_dir = dirs.split(",")
        kept = [i for i in order if labels[name][i] not in ("unknown", "S")]
        scored[name] = (Model(a.baseline, {j: attach(r, kept) for j, r in load_scored(base_dir, jobs).items()}),
                        Model(a.candidate, {j: attach(r, kept) for j, r in load_scored(cand_dir, jobs).items()}), kept)
        manifests[name] = [{j: json.load(open(os.path.join(d, f"{j}_independent_manifest.json"), encoding="utf-8")) for j in jobs}
                           for d in (base_dir, cand_dir)]
    names = [s.split("=", 1)[0] for s in a.labels]
    teachers = [n for n in names if n != a.primary]
    agree = {i for i in order if len({labels[n][i] for n in teachers}) == 1} if len(teachers) >= 2 else set(order)
    table_of = {i: meta[i]["table"] for i in order}

    L = [f"# 独立評価の採点（{len(cols)} 列・出典 {'・'.join(sorted({c['source'] for c in cols}))}）", ""]
    L.append(f"基準線 {a.baseline}・候補 {a.candidate}、各 {len(jobs)} 種子（{', '.join(jobs)}）。OK＝正解、または正解が other で不明。"
             f"区間は表単位の復元抽出 {a.reps:,} 回（{len(set(table_of.values()))} 表）。値は種子の平均。")
    L.append("")

    # 1. 判定
    L += ["## 判定（事前登録の規則）", "",
          "| ラベル | 採点列 | 未知見出し列 | 未知見出し OK 率 基準線 | 候補 | 差（候補−基準線） | 差の 90% 区間 | 重大 基準線 | 候補 | 3 条件 |",
          "|---|---:|---:|---:|---:|---:|---|---:|---:|---|"]
    verdicts = {}
    boots = {}
    for name in names:
        base, cand, kept = scored[name]
        unseen = [i for i in kept if normalized_header(meta[i]["header"]) not in train_heads]
        stats, diffs = bootstrap([base, cand], unseen, table_of, a.reps)
        boots[name] = (unseen, stats, diffs)
        d = cand.mean_ok(unseen) - base.mean_ok(unseen)
        lo90, hi90 = quantile(diffs, 0.05), quantile(diffs, 0.95)
        cb, cc = base.mean_crit(kept), cand.mean_crit(kept)
        conds = (d >= 0.02, cc <= cb, lo90 > 0)
        verdicts[name] = all(conds)
        L.append(f"| {name} | {len(kept)} | {len(unseen)} | {pct(base.mean_ok(unseen))} | {pct(cand.mean_ok(unseen))} | {100 * d:+.1f} pt | "
                 f"{100 * lo90:+.1f}〜{100 * hi90:+.1f} pt | {cb:.1f} | {cc:.1f} | {'・'.join('○' if c else '×' for c in conds)} |")
    adopt = all(verdicts.values())
    L += ["", f"3 条件＝(1) 差 ≥ +2.0 pt、(2) 重大 候補 ≤ 基準線、(3) 差の 90% 区間の下限 > 0。"
          f"**結論：{a.candidate + ' を採る' if adopt else a.baseline + ' を残す'}**"
          f"（ラベル {len(names)} 通りの{'すべてで条件を満たす' if adopt else 'どれでも条件を満たさない' if not any(verdicts.values()) else 'あいだで結論が割れるため採らない'}）。", ""]

    # 2. 主ラベルの指標と 95% 区間
    base, cand, kept = scored[a.primary]
    unseen, stats, diffs = boots[a.primary]
    L += [f"## 主な指標（{a.primary}ラベル）", "",
          f"| 指標 | {a.baseline} | {a.candidate} |", "|---|---|---|"]
    L.append(f"| 未知見出しの OK 率（95% 区間） | {pct(base.mean_ok(unseen))}（{pct(quantile(stats[base.name], .025))}〜{pct(quantile(stats[base.name], .975))}） | "
             f"{pct(cand.mean_ok(unseen))}（{pct(quantile(stats[cand.name], .025))}〜{pct(quantile(stats[cand.name], .975))}） |")
    L.append(f"| 差の 95% 区間（候補−基準線） | | {100 * quantile(diffs, .025):+.1f}〜{100 * quantile(diffs, .975):+.1f} pt |")
    all_stats, _ = bootstrap([base, cand], kept, table_of, a.reps)
    L.append(f"| 全体の OK 率（95% 区間） | {pct(base.mean_ok(kept))}（{pct(quantile(all_stats[base.name], .025))}〜{pct(quantile(all_stats[base.name], .975))}） | "
             f"{pct(cand.mean_ok(kept))}（{pct(quantile(all_stats[cand.name], .025))}〜{pct(quantile(all_stats[cand.name], .975))}） |")
    n_crit = sum(labels[a.primary][i] in CRIT for i in kept)

    def per_seed(m, f):
        return [f(m.rows(j, kept)) for j in m.by_job]

    def fmt_seeds(xs):
        mean = sum(xs) / len(xs)
        return f"{mean:.1f}（{'・'.join(str(int(x)) for x in xs)}）"

    for label, f in (("重大な取り違え（件、種子ごと）", lambda rs: sum(r["critical"] for r in rs)),
                     ("誤断定（誤答＋その他の誤受理、件）", lambda rs: sum(r["outcome"] in ("wrong", "other_ng") for r in rs)),
                     ("不明（見送り、件）", lambda rs: sum(r["outcome"] == "unknown" for r in rs))):
        L.append(f"| {label} | {fmt_seeds(per_seed(base, f))} | {fmt_seeds(per_seed(cand, f))} |")
    L.append(f"| 重大の率（重大 5 種類の正解列 {n_crit} に対して） | {pct(base.mean_crit(kept) / n_crit)} | {pct(cand.mean_crit(kept) / n_crit)} |")
    L.append(f"| 重大 5 種類を精度 99% で答えられる割合（確率の下限を動かす） | {pct(coverage_at(base, kept, labels[a.primary]))} | {pct(coverage_at(cand, kept, labels[a.primary]))} |")
    n_unk = sum(labels[a.primary][i] == "unknown" for i in order)
    if n_unk:
        ua = [[manifests[a.primary][k][j]["unknown_asserted"] for j in jobs] for k in (0, 1)]
        L.append(f"| 正解が unknown の列（{n_unk}、採点の外）への言い切り（件、種子ごと） | {fmt_seeds(ua[0])} | {fmt_seeds(ua[1])} |")
    L.append("")

    # 3. 層別
    def strata():
        ss = [("見出し", s, [i for i in kept if (normalized_header(meta[i]["header"]), labels[a.primary][i]) in train_pairs] if s == SLICES[0]
               else [i for i in kept if normalized_header(meta[i]["header"]) in train_heads and (normalized_header(meta[i]["header"]), labels[a.primary][i]) not in train_pairs] if s == SLICES[1]
               else [i for i in kept if normalized_header(meta[i]["header"]) not in train_heads]) for s in SLICES]
        for src in sorted({meta[i]["source"] for i in kept}):
            ss.append(("出典", src, [i for i in kept if meta[i]["source"] == src]))
        for lang in sorted({meta[i]["language"] for i in kept}):
            ss.append(("言語", lang, [i for i in kept if meta[i]["language"] == lang]))
        ss.append(("先生の初回", "一致した列", [i for i in kept if i in agree]))
        ss.append(("先生の初回", "食い違った列", [i for i in kept if i not in agree]))
        for kind, _ in Counter(labels[a.primary][i] for i in kept).most_common():
            ss.append(("種類（正解）", kind, [i for i in kept if labels[a.primary][i] == kind]))
        return ss

    L += [f"## 層別（{a.primary}ラベル、OK 率と重大の件数は種子の平均）", "",
          f"| 区分 | 層 | 列 | {a.baseline} OK 率 | {a.candidate} OK 率 | 差 | {a.baseline} 重大 | {a.candidate} 重大 |",
          "|---|---|---:|---:|---:|---:|---:|---:|"]
    for group, name, ids in strata():
        if not ids:
            continue
        b, c = base.mean_ok(ids), cand.mean_ok(ids)
        L.append(f"| {group} | {name} | {len(ids)} | {pct(b)} | {pct(c)} | {100 * (c - b):+.1f} pt | {base.mean_crit(ids):.1f} | {cand.mean_crit(ids):.1f} |")
    L.append("")

    # 4. ラベルの人別
    L += ["## ラベルの人別（全体の OK 率・未知見出しの OK 率・重大、種子の平均）", "",
          f"| ラベル | 採点列 | {a.baseline} 全体 | {a.candidate} 全体 | {a.baseline} 未知見出し | {a.candidate} 未知見出し | {a.baseline} 重大 | {a.candidate} 重大 |",
          "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for name in names:
        b, c, k = scored[name]
        u = boots[name][0]
        L.append(f"| {name} | {len(k)} | {pct(b.mean_ok(k))} | {pct(c.mean_ok(k))} | {pct(b.mean_ok(u))} | {pct(c.mean_ok(u))} | {b.mean_crit(k):.1f} | {c.mean_crit(k):.1f} |")
    L.append("")

    # 5. 混同表
    L += [f"## 重大 5 種類の混同表（{a.primary}ラベル）", "", confusion(base, kept, labels[a.primary]), "", confusion(cand, kept, labels[a.primary]), ""]
    text = "\n".join(L) + "\n"
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
