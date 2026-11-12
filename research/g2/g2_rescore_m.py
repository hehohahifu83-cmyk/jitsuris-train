"""G2 の直し M の採点し直し（2026-11-13 Claude。Codex の G3 予測前の点検 1 を受けて）。
固定した g2_eval.py の run は RC.cue_types に M を足していたが、eval_fixes.run の FX.use が make_cue_types(fixes) で置き換えるため、
採点の中で M が効いていなかった（L24+G+M は L24+G と同じ処理）。保存した予測（新しい予測なし）・同じ正解・同じ決まりで、
M を make_cue_types の生成した関数に足す形に直して数え直す。g2_eval.py 自体と g2_eval.md は書き換えない（記録として残す）。

  python research/g2/g2_rescore_m.py --labels <ai-bridge>/labels/g2/final.jsonl > research/g2/g2_rescore_m.md
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g2_eval as E  # noqa: E402
import fixes as FX  # noqa: E402

assert FX is E.D.EF.FX


def run(base, mv, labels, model, s, with_m):
    data = E.D.with_job(base, os.path.join(E.PRED_DIR, E.PRED[model][s]))
    orig = FX.make_cue_types
    if with_m:
        def make_with_m(fixes):
            f = orig(fixes)
            return lambda h, u="": f(h, u) | E.FM.extra_cues(h, u)
        FX.make_cue_types = make_with_m
    try:
        E.D.EF._PCACHE.clear()
        p = {}
        res = E.D.EF.run(data, mv, labels, E.D.PRODUCT + ("K",), per=p)
    finally:
        FX.make_cue_types = orig
    return res, p


if __name__ == "__main__":
    E.run = run
    print("<!-- research/g2/g2_rescore_m.py の出力（M を直した採点し直し。固定した g2_eval.md は M が効いていない記録として残す） -->")
    E.main(sys.argv[1:] + ["--dry"])
