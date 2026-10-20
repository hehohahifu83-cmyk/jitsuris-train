"""学習率の探索の結果から、事前に固定した規則で学習率を選ぶ（2026-10-20）。compare_models.py・slice_eval.py の部品を使う。

使い方：
  python sweep_pick.py <置き場> --jobs job1,job2,job3,job4 [--lrs 5e-5,1e-4,2e-4,4e-4] [--cond ft] [--tie-pp 1.5] [--title 名前] [--out bench/lr_sweep_xxx.md]
例：
  python sweep_pick.py eval_reports/runs/<回収した実行の番号> --jobs job1,job2,job3,job4 --title "mmBERT-small 学習率の探索（検証・seed 1）" --out bench/lr_sweep_mmbert_small.md

規則（連絡箱 20261020-2259 で、結果を見る前に固定した）：
1. 指標＝検証4試験を合わせた『未知の見出し』の macro-F1（5行以上のクラスだけ）。
2. 最良から --tie-pp ポイント（既定 1.5。種子ぶれと同じ線）以内は同点。同点の中では、重大誤りの少ない方 → 誤断定の少ない方 → 小さい学習率。
3. fp32 への切り替え（manifest の amp.fallback_step）・manifest の status が completed でない・manifest なし・学習率が分からない仕事は候補から外し、理由を表に書く。
4. 最良が探索の端（最小か最大の学習率）なら、『外側へ 1 点足して再探索』と表示する（もう一方のモデルにも同数まで）。
学習率は各仕事の manifest（<job>_manifest.json の run.env.FT_LR）から読む。無ければ --lrs（仕事の並びの順）。
検証モードの結果を数えるので、この中で FT_VAL=1 を設定する。固定試験・blind は読まない。
"""
from __future__ import annotations

import json
import os
import sys

import compare_models as C
import slice_eval as S


def job_info(dir_, job, lrs_by_job=None):
    """仕事の manifest から学習率と、候補から外す理由を読む。"""
    path = os.path.join(dir_, f"{job}_manifest.json")
    manifest = None
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as fh:
            manifest = json.load(fh)
    lr = None
    if manifest:
        text = ((manifest.get("run") or {}).get("env") or {}).get("FT_LR")
        if text not in (None, ""):
            lr = float(str(text).strip())
    if lr is None and lrs_by_job:
        lr = lrs_by_job.get(job)
    problems = []
    if manifest is None:
        problems.append("manifest なし（学習率と完了を確かめられない）")
    else:
        if manifest.get("status") != "completed":
            problems.append(f"manifest の status が completed でない（{manifest.get('status')}）")
        amp = manifest.get("amp") or {}
        if amp.get("fallback_step") is not None:
            problems.append(f"fp16 から fp32 に切り替えた（step {amp['fallback_step']}）")
    if lr is None:
        problems.append("学習率が分からない（--lrs で指定）")
    return {"job": job, "lr": lr, "problems": problems}


def pick(rows, tie_pp=1.5):
    """rows: [{'job','lr','problems','unseen_macro_f1','critical','false_assert',…}]。選んだ行・最良の行・同点の行・端の印を返す。"""
    eligible = [r for r in rows if not r["problems"] and r["lr"] is not None and r["unseen_macro_f1"] == r["unseen_macro_f1"]]
    if not eligible:
        return {"chosen": None, "best": None, "tied": [], "edge": None}
    best = max(eligible, key=lambda r: (r["unseen_macro_f1"], -r["lr"]))
    tied = [r for r in eligible if best["unseen_macro_f1"] - r["unseen_macro_f1"] <= tie_pp / 100 + 1e-12]
    chosen = min(tied, key=lambda r: (r["critical"], r["false_assert"], r["lr"]))
    grid = sorted({r["lr"] for r in rows if r["lr"] is not None})
    edge = None
    if len(grid) > 1:
        edge = "low" if best["lr"] == grid[0] else "high" if best["lr"] == grid[-1] else None
    return {"chosen": chosen, "best": best, "tied": tied, "edge": edge}


def fmt_lr(lr):
    if lr is None:
        return "—"
    mantissa, exponent = f"{lr:e}".split("e")      # 1e-4 → '1.000000e-04' → 1e-4
    return f"{mantissa.rstrip('0').rstrip('.')}e{int(exponent)}"


def render(rows, result, title, tie_pp=1.5):
    lines = [f"# {title}", "",
             "規則は連絡箱 20261020-2259 で結果を見る前に固定したもの（sweep_pick.py の冒頭）。指標＝検証4試験を合わせた、未知の見出しの macro-F1（5行以上のクラスだけ）。", "",
             "| 仕事 | 学習率 | 候補 | 検証の行数 | 未知見出しの行数 | 未知見出し macro-F1 | 未知見出し正解率 | 全体 macro-F1 | 全体の正解率 | 重大誤り | 誤断定 | 不明 |",
             "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for r in sorted(rows, key=lambda r: (r["lr"] is None, r["lr"] or 0, r["job"])):
        status = "○" if not r["problems"] else "外す：" + "／".join(r["problems"])
        m = r.get("metrics") or {}
        lines.append(f"| {r['job']} | {fmt_lr(r['lr'])} | {status} | {m.get('n', '—')} | {m.get('unseen_n', '—')} | {C.pct(r['unseen_macro_f1'])} | {C.pct(m.get('unseen_acc', float('nan')))} | "
                     f"{C.pct(m.get('macro_f1', float('nan')))} | {C.pct(m.get('acc', float('nan')))} | {r['critical']} | {r['false_assert']} | {m.get('unknown', '—')} |")
    lines.append("")
    chosen, best = result["chosen"], result["best"]
    if chosen is None:
        lines += ["## 選択", "", "候補が無い（すべての仕事が外れたか、未知見出しの macro-F1 を計算できない）。原因を連絡箱に書き、自分で依頼し直さない。"]
        return "\n".join(lines) + "\n"
    lines += ["## 選択", "",
              f"- **選んだ学習率：{fmt_lr(chosen['lr'])}（{chosen['job']}）**",
              f"- 最良：{fmt_lr(best['lr'])}（{best['job']}）未知見出し macro-F1 {C.pct(best['unseen_macro_f1'])}。最良から {tie_pp:g} ポイント以内（同点）：" +
              "、".join(f"{fmt_lr(r['lr'])}（{C.pct(r['unseen_macro_f1'])}・重大 {r['critical']}・誤断定 {r['false_assert']}）" for r in sorted(result['tied'], key=lambda r: r['lr'])),
              "- 同点の中の選び方：重大誤りの少ない方 → 誤断定の少ない方 → 小さい学習率。"]
    if result["edge"]:
        side = "小さい側" if result["edge"] == "low" else "大きい側"
        lines.append(f"- **最良が探索の端（{side}）：外側へ 1 点足して再探索する**（もう一方のモデルにも同数まで）。")
    n = next((r["metrics"]["n"] for r in rows if r.get("metrics")), None)
    un = next((r["metrics"]["unseen_n"] for r in rows if r.get("metrics")), None)
    if n:
        lines.append(f"- 注意：検証は {n} 行（未知見出し {un} 行）、種子は 1 つ。分かるのは粗い不適合（学習不足・発散）までで、モデル同士の優劣を決める値ではない。")
    return "\n".join(lines) + "\n"


def build_rows(dir_, jobs, cond, train_pairs, train_headers, lrs_by_job=None, min_support=5):
    records = S.load_records(dir_, cond, jobs)
    if not records:
        raise ValueError(f"{dir_} に条件 {cond} の記録がない")
    rows = []
    for job in jobs:
        info = job_info(dir_, job, lrs_by_job)
        rs = C.job_records(records, job)
        if not rs:
            info["problems"].append("検証の記録なし（NaN などで評価まで届かなかった可能性）")
            info.update(unseen_macro_f1=float("nan"), critical=10 ** 9, false_assert=10 ** 9, metrics=None)
        else:
            m = C.job_metrics(rs, train_pairs, train_headers, min_support)
            info.update(unseen_macro_f1=m["unseen_macro_f1"], critical=m["critical"], false_assert=m["false_assert"], metrics=m)
        rows.append(info)
    return rows


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0].startswith("--"):
        print(__doc__)
        return 2
    dir_ = argv.pop(0)
    jobs, lrs, cond, tie_pp, title, out = None, None, "ft", 1.5, "学習率の探索", None
    while argv:
        a = argv.pop(0)
        if a == "--jobs":
            jobs = argv.pop(0).split(",")
        elif a == "--lrs":
            lrs = [float(x) for x in argv.pop(0).split(",")]
        elif a == "--cond":
            cond = argv.pop(0)
        elif a == "--tie-pp":
            tie_pp = float(argv.pop(0))
        elif a == "--title":
            title = argv.pop(0)
        elif a == "--out":
            out = argv.pop(0)
        else:
            raise SystemExit(__doc__)
    if not jobs:
        raise SystemExit("--jobs job1,job2,… を指定する")
    lrs_by_job = dict(zip(jobs, lrs)) if lrs else None
    os.environ["FT_VAL"] = "1"      # 検証モードの学習側の見出しで数える（encoder_exp を読む前に設定）
    pairs, heads = S.train_sets_from_encoder_exp()
    rows = build_rows(dir_, jobs, cond, pairs, heads, lrs_by_job)
    result = pick(rows, tie_pp)
    text = render(rows, result, title, tie_pp)
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(text)
    return 0 if result["chosen"] else 1


if __name__ == "__main__":
    sys.exit(main())
