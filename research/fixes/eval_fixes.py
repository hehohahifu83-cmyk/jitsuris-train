"""原因の直し（fixes.py の F1〜F8）を、今の製品の形（見張り → recheck v1 → 検査役 v2（τ）→ rho 0.8 → 通貨の手がかり）に重ねて測る（2026-10-30 Claude）。
決める陣（新しい陣 8 つ：原因を見つけた陣）と確かめる陣（conf1030 の 15 陣：C2 の学習にもしきい値決めにも使っていない）を分けて、
直しなし・直しを 1 つずつ・採った直しを全部、を並べる。事前記録：bench/root_cause_fixes_prereg_20261030.md
  python research/fixes/eval_fixes.py decide    → research/fixes/decide.md（決める陣）
  python research/fixes/eval_fixes.py confirm F1 F2 …  → research/fixes/confirm.md（確かめる陣。事前記録を commit してから 1 回だけ）
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
import recheck as R  # noqa: E402
import research.unknown.audit as A  # noqa: E402
import fixes as FX  # noqa: E402

V, E = A.V, A.E
DECIDE = ("b015", "b016", "b017", "b060", "b062", "b063", "b064", "b065")
CONFIRM = ("b019", "b020", "b022", "b023", "b024", "b025", "b026", "b035", "b036", "b050", "b053", "b054", "b055", "b056", "b057")


def load(batches):
    out = {}
    for b in batches:
        path = os.path.join(ROOT, "materials", "pool", "work", b, "pred_c2_seed1.json")
        te, _ = A.with_pred(E.load_batch(b), path)
        why = {r["id"]: r.get("decision_reason") for r in json.load(open(path, encoding="utf-8"))["rows"]}
        for c in te:
            c["guard_reason"] = why.get(c["id"])
        out[b] = te
    return out


_PCACHE = {}


def probs(b, te, mv, labels, f2):
    """検査役の確率。値が変わるのは F2 だけなので、(陣, F2) ごとに 1 回だけ計算する。"""
    key = (b, f2)
    if key not in _PCACHE:
        P = np.zeros((len(te), len(labels)), dtype="float32")
        p = mv.predict_proba(np.hstack([V.matrix([c["values"] for c in te]), E.table_matrix(te)]))
        for j, lab in enumerate(mv.classes_):
            P[:, labels.index(lab)] = p[:, j]
        _PCACHE[key] = P
    return _PCACHE[key]


def run(data, mv, labels, fixes, per=None):
    """直し fixes を入れた製品の形の最終の答え。採点の範囲（正解が unknown・S・other・person の列は数えない）で (n, 正しい, 不明, 重大, ほかの誤り)。
    per に dict を渡すと、列ごとの (最終の答え, 正解, 列名, 理由) を入れる。"""
    n = ok = unk = crit = wrong = 0
    with FX.use(fixes):
        for b, te0 in data.items():
            te = FX.fix_guard(FX.prepare(te0, fixes), fixes)
            P = probs(b, te, mv, labels, "F2" in fixes)
            base = E.base_decisions(te)
            E._VETO.clear()   # 検査役のためておく分は id() が鍵なので、使い回された番号で前の陣の結果を取り違えないよう毎回消す
            fin = E.combine(base, P, np.zeros(len(te)), labels, A.TAU, None, list(range(len(te))))
            for k, c in enumerate(te):
                if not c["truth"] or c["truth"] in ("unknown", "S", "other", "person"):
                    continue
                f = fin[k]
                if "F7" in fixes and f[1] and str(f[1]).startswith("verifier:") and R.single_cue(c["header"], c.get("unit", "")) == base[k][0]:
                    f = base[k]
                cand = V.candidate(f[0], f[1], c["pred"], c["top3"], c["header"], P[k], labels, A.RHO)
                lab = cand if cand else f[0]
                final = V.amount_cue_veto(lab, c["header"], c.get("unit"), c["values"])
                if per is not None:
                    per[c["id"]] = (final, c["truth"], c["header"], f[1] or base[k][1], c["pred"], [str(v) for v in c["values5"][:5]], c.get("unit", ""))
                n += 1
                if final == "unknown":
                    unk += 1
                elif final == c["truth"]:
                    ok += 1
                elif final in V.NUMERIC and c["truth"] in V.NUMERIC:
                    crit += 1
                else:
                    wrong += 1
    return n, ok, unk, crit, wrong


def table(rows):
    L = ["| 直し | 採点列 | 正しい | 不明 | 重大 | ほかの誤り |", "|---|---:|---:|---:|---:|---:|"]
    for name, (n, ok, unk, crit, wrong) in rows:
        L.append(f"| {name} | {n} | {ok}（{ok / n:.1%}） | {unk}（{unk / n:.1%}） | {crit} | {wrong} |")
    return L


def main():
    labels = list(V.LABELS)
    train = [c for b in A.TRAIN for c in E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    mode = sys.argv[1]
    if mode == "decide":
        data = load(DECIDE)
        rows = [("直しなし", run(data, mv, labels, ()))] + [(f, run(data, mv, labels, (f,))) for f in FX.ALL] + [("F1〜F8 全部", run(data, mv, labels, FX.ALL))]
        L = ["# 原因の直し：決める陣（新しい陣 8 つ）（`research/fixes/eval_fixes.py decide`）", "", "原因を見つけた陣なので、当てはまりは良く見える。採るかどうかは確かめる陣で決める（事前記録）。", ""] + table(rows)
        out = "decide.md"
    else:
        chosen = tuple(sys.argv[2:])
        data = load(CONFIRM)
        rows = [("直しなし", run(data, mv, labels, ()))] + [(f, run(data, mv, labels, (f,))) for f in chosen] + [("選んだ直し全部（" + "・".join(chosen) + "）", run(data, mv, labels, chosen))]
        L = ["# 原因の直し：確かめる陣（conf1030 の 15 陣）（`research/fixes/eval_fixes.py confirm`）", "", "事前記録 bench/root_cause_fixes_prereg_20261030.md の判定の規則で読む。", ""] + table(rows)
        out = "confirm.md"
    open(os.path.join(HERE, out), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
