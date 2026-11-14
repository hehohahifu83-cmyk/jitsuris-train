"""G3 の金額の列が不明になる原因の調べ（2026-11-14 Claude。読むだけ。正解・予測・決まりは変えない）。
L24+G（製品の形）の 3 本について、正解 amount・quantity・rate の列ごとに、本体の答え（見張りのあと）・最終の答え・理由を並べ、
どの段で不明になったかを数える。採点の道具 research/g3/g3_eval.py の関数をそのまま使う（同じ環境の照合つき）。

  python research/g3/amount_unknown.py --labels <ai-bridge>/labels/g3/final.jsonl → research/g3/amount_unknown.md・.json
"""
import argparse
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g3_eval as E  # noqa: E402
import numpy as np  # noqa: E402


def stage(tr):
    """最後に不明へ落とした段（2026-11-14 Codex の点検で直した。理由の文字は最初に止めた段の理由で、最後の段ではない）。
    tr：本体（見張りのあと）→ 再確認・検査役（f）→ rho → 辞書 → 末尾の通貨確認 の各段の答え。"""
    if tr["final"] != "unknown":
        return "答えた"
    if tr["dict"] != "unknown":
        return "末尾の通貨確認（amount_cue_veto）"
    if tr["rho"] != "unknown":
        return "辞書"
    if tr["f"] != "unknown":
        return "rho"
    r = str(tr["f_reason"] or "")
    if tr["pred"] == "unknown":
        return "本体・見張り"
    if r.startswith("verifier"):
        return "検査役"
    return "再確認"


class Trace:
    """eval_fixes.run の 1 列ごとの段の答えを、呼ばれた順に記録する（V.candidate・辞書・amount_cue_veto を包む）。"""
    def __init__(self):
        self.rows = []

    def __enter__(self):
        V, EF = E.D.EF.V, E.D.EF
        self._c, self._v, self._d = V.candidate, V.amount_cue_veto, EF._dictionary
        rows = self.rows

        def cand(label, why, *a, **k):
            out = self._c(label, why, *a, **k)
            rows.append({"f": label, "f_reason": why, "rho": out if out else label})
            return out

        class Dic:
            def __init__(s, d):
                s.d = d

            def apply(s, lab, *a, **k):
                out = s.d.apply(lab, *a, **k)
                rows[-1]["dict"] = out[0]
                return out
        orig_dict = self._d

        def veto(lab, *a, **k):
            out = self._v(lab, *a, **k)
            rows[-1].setdefault("dict", lab)
            rows[-1]["final"] = out
            return out
        V.candidate, V.amount_cue_veto = cand, veto
        EF._dictionary = lambda: Dic(orig_dict())

    def __exit__(self, *a):
        V, EF = E.D.EF.V, E.D.EF
        V.candidate, V.amount_cue_veto, EF._dictionary = self._c, self._v, self._d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", required=True)
    a = ap.parse_args()
    got = {"python": "%d.%d" % sys.version_info[:2], "sklearn": E.sklearn.__version__, "numpy": np.__version__, "scipy": E.scipy.__version__}
    if got != E.ENV:
        raise SystemExit(f"採点の環境が違う：{got}")
    f, dsha = E.R.DICTS["K"]
    os.environ["JITSURIS_DICT"] = os.path.join(E.ROOT, "materials", "dictionary", f)
    E.D.EF._DICT.clear()
    labels = list(E.D.V.LABELS)
    train = [c for b in E.D.A.TRAIN for c in E.D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.D.E.fit(np.hstack([E.D.V.matrix([c["values"] for c in train]), E.D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = E.load_g3(a.labels)
    cols = {c["id"]: c for c in base["g3"]}
    E.check_predictions([c["id"] for c in base["g3"]])
    rows, cnt = [], defaultdict(Counter)
    for s in E.SEEDS:
        t = Trace()
        with t:
            res, p = E.run(base, mv, labels, "L24", s, False, False)
        if len(t.rows) != len(p):
            raise SystemExit("段の記録の数が採点の列の数と合わない")
        for (k, v), tr in zip(p.items(), t.rows):
            final, truth, header, reason, pred = v[0], v[1], v[2], v[3], v[4]
            if tr["final"] != final:
                raise SystemExit(f"{k}: 段の記録の最終の答えが採点と違う")
            tr["pred"] = pred
            if truth not in ("amount", "quantity", "rate"):
                continue
            st = stage(tr)
            first = "答えた" if tr["f"] != "unknown" else ("本体・見張り" if pred == "unknown" else ("検査役" if str(tr["f_reason"] or "").startswith("verifier") else "再確認（" + (str(tr["f_reason"] or "").split(":")[0] or "理由なし") + "）"))
            cnt[truth][st] += 1
            rows.append({"seed": s, "id": k, "table": cols[k]["table"], "publisher": cols[k]["publisher"], "header": header, "unit": cols[k]["unit"],
                         "values5": cols[k]["values5"], "truth": truth, "pred": pred, "f": tr["f"], "rho": tr["rho"], "dict": tr["dict"], "final": final,
                         "reason": str(reason), "first_stop": first, "stage": st})
            cnt["first:" + truth][first] += 1
    L = ["# G3：数の列が不明になる段（L24+G、3 本の合計。`research/g3/amount_unknown.py`、読むだけ）", ""]
    for t in ("amount", "quantity", "rate"):
        n = sum(cnt[t].values())
        L += [f"## 正解 {t}（{n // 3} 列 × 3 本）", "", "最後に不明へ落とした段：", "", "| 段 | 数 | 割合 |", "|---|---:|---:|"]
        L += [f"| {k} | {v} | {100 * v / n:.1f}% |" for k, v in cnt[t].most_common()]
        L += ["", "最初に止めた段（rho で戻ったあと末尾でまた止まったものも、最初の段で数える）：", "", "| 段 | 数 |", "|---|---:|"]
        L += [f"| {k} | {v} |" for k, v in cnt["first:" + t].most_common()]
        L.append("")
    L += ["## 正解 amount で不明になった列（本 1）", "", "| id | 表 | 列名 | 単位 | 値（5 つまで） | 本体 | 最初に止めた段 | rho | 最後の段 |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["seed"] == 1 and r["truth"] == "amount" and r["final"] == "unknown":
            L.append(f"| {r['id']} | {r['table']} | {str(r['header'])[:30]} | {r['unit'][:12]} | {' / '.join(v[:12] for v in r['values5'][:5])} | {r['pred']} | {r['first_stop']} | {r['rho']} | {r['stage']} |")
    out = "\n".join(L).replace("\n|", "\n|") + "\n"
    open(os.path.join(HERE, "amount_unknown.md"), "w", encoding="utf-8").write(out)
    json.dump(rows, open(os.path.join(HERE, "amount_unknown.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(out[:6000])


if __name__ == "__main__":
    main()
