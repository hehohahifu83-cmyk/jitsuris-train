"""C3u と C3a を比べる（事前記録 bench/c3u_prereg_20261029.md、2026-10-29 Claude）。
両方とも単位の例を作り直した入力（dev1029u の set）。C3a は今の予測に、単位の例が変わった 183 列だけ unitfix1029 の予測を重ねる。
決め方：recheck v1 → 検査役 v2（τ 0.05）→ rho 0.8 → 通貨の手がかりの無い金額は不明。新しい陣 8 つ。
使い方：python research/c3u_eval.py [--out ...]
"""
import argparse
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402
from verifier_c1 import TAU  # noqa: E402
from research.merge.merge_eval import with_pred  # noqa: E402

BATCHES = ("b015", "b016", "b017", "b060", "b062", "b063", "b064", "b065")
TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))
RHO = 0.8
WORK = os.path.join(ROOT, "materials", "pool", "work")


def rows_of(path):
    return {r["id"]: r for r in json.load(open(path, encoding="utf-8"))["rows"]}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--models", nargs="+", default=["c3a", "c3u"])   # 2026-10-29：C3s も同じ道具で測る（dev1029u/pred_<model>_seed1.json）
    a = ap.parse_args(argv)
    labels = list(V.LABELS)
    train = [c for b in TRAIN for c in E.load_batch(b)]
    ok = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[ok], np.array([c["truth"] for c in train])[ok])
    unit = {c["id"]: c.get("unit", "") for c in json.load(open(os.path.join(WORK, "dev1029u", "set.json"), encoding="utf-8"))["columns"]}
    fix_a = rows_of(os.path.join(WORK, "unitfix1029", "pred_c3a_seed1.json"))
    other = {m: rows_of(os.path.join(WORK, "dev1029u", f"pred_{m}_seed1.json")) for m in a.models if m != "c3a"}
    L = ["### 結果（`research/c3u_eval.py`、単位を直した入力・直した決め方）", "", "| 本体 | 陣 | 結果 | 不明 | 重大 |", "|---|---|---|---|---:|"]
    tot, crit = {}, {}
    for model in a.models:
        allte, alld = [], []
        for b in BATCHES:
            te, _ = with_pred(E.load_batch(b), os.path.join(WORK, b, "pred_c3a_seed1.json"))
            for c in te:
                c["unit"] = unit.get(c["id"], c.get("unit", ""))
                src = (fix_a if model == "c3a" else other[model]).get(c["id"])
                if model != "c3a" and src is None:
                    raise SystemExit(f"{model} の予測に無い列：{c['id']}")
                if src is not None:
                    c["pred"], c["top3"] = src["guarded_prediction"], src["top3"]
            P = np.zeros((len(te), len(labels)), dtype="float32")
            p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
            for j, lab in enumerate(mv.classes_):
                P[:, labels.index(lab)] = p[:, j]
            idx = list(range(len(te)))
            fin = E.combine(E.base_decisions(te), P, np.zeros(len(te)), labels, TAU, None, idx)
            d = []
            for k in idx:
                cand = V.candidate(fin[k][0], fin[k][1], te[k]["pred"], te[k]["top3"], te[k]["header"], P[k], labels, RHO)
                d.append(V.amount_cue_veto(cand if cand else fin[k][0], te[k]["header"], te[k]["unit"], te[k]["values"]))
            s = E.score(d, te)
            L.append(f"| {model} | {b} | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
            allte += te; alld += d
        s = E.score(alld, allte)
        tot[model] = s
        crit[model] = [f"{c['batch']} {c['header'][:28]}（正 {c['truth']} → {x}）" for c, x in zip(allte, alld) if E.score([x], [c])["critical"]]
        L.append(f"| **{model}** | **合計** | {E.fmt(s)} | {s['unknown'] / s['n']:.1%} | {s['critical'] / s['n']:.2%} |")
    cand = a.models[-1]
    a3, u3 = tot["c3a"], tot[cand]
    r1 = u3["critical"] <= a3["critical"]
    da = (u3["correct"] / u3["n"] - a3["correct"] / a3["n"]) * 100
    du = (u3["unknown"] / u3["n"] - a3["unknown"] / a3["n"]) * 100
    r2 = da >= 1.5 or du <= -1.5
    base = r1 and da >= -0.5
    L += ["", "- 重大の列：" + "／".join(f"{m} {crit[m] or 'なし'}" for m in a.models),
          f"- 判定：規則 1 {'○' if r1 else '×'}（{a3['critical']}→{u3['critical']}）、規則 2 {'○' if r2 else '×'}（正 {da:+.1f}・不明 {du:+.1f} ポイント）→ "
          f"**{cand} を{'採る' if r1 and r2 else '採らない'}**（相手 C3a）"
          + (f"／銀の回の土台に使う条件（重大が C3a 以下・正解率の下がり 0.5 以内）{'○ → 土台は C3u' if base else '× → 土台は C3a'}" if cand == "c3u" else "")]
    print("\n".join(L))
    if a.out:
        with open(a.out, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(L) + "\n")


if __name__ == "__main__":
    main()
