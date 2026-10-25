"""封印セット #3 の採点（2026-10-25 Claude。事前登録 `independent_eval/PREREG_sealed3-20261025-v1.md` のとおりに読む）。

製品に入れる形を、予測ファイル（見張りの判定と上位 3 つ）にそのまま重ねる。モデルは回さない（予測は Actions で各重み 1 回だけ）。
  見張り（予測ファイルの guarded_prediction）→ recheck v1（recheck.apply_table、t＝0.95、見張り v11 の列名の日付の規則）
  → 検査役 v2（models/verifier_v2.json、tau＝0.05、重大検知役は使わない）→ 候補つきの不明を言い切りに戻す（rho_assert＝0.7）
採点は verifier_eval.score（llm_baseline.score_real と同じ。正解が unknown・S・person の列は数えない）。
重大の割合＝重大 ÷ 採点した列（不明と答えた列も分母に入る）。不明の割合＝不明 ÷ 採点した列。
ラベル（非公開）は ai-bridge/labels/ から読み、公開するのは集計だけ。

使い方：python independent_eval/sealed3_score.py --labels <裁定後のラベル.jsonl> --pred independent_eval/predictions_sealed3/<run_job>.json [--out bench/independent_eval_sealed3-20261025-v1.md]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import verifier as V  # noqa: E402
import verifier_eval as E  # noqa: E402

SET = ROOT / "independent_eval" / "results" / "sealed3" / "sealed3.json"
TABLE_ROWS = ROOT / "independent_eval" / "results" / "sealed3" / "table_rows.json"
VERIFIER = ROOT / "models" / "verifier_v2.json"
TAU, RHO_ASSERT = 0.05, 0.7
MAX_CRITICAL, MAX_UNKNOWN, MIN_SCORED = 0.002, 0.10, 1500


def upper_bound(k, n, conf=0.90):
    """二項の割合の上側の限界（片側 conf。Clopper-Pearson、二分法）。"""
    if n == 0:
        return 1.0
    lo, hi = k / n, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        # P(X <= k | p=mid)
        cdf = sum(math.comb(n, i) * mid ** i * (1 - mid) ** (n - i) for i in range(k + 1))
        lo, hi = (mid, hi) if cdf > 1 - conf else (lo, mid)
    return hi


def load(labels_path, pred_path):
    s = json.loads(SET.read_text(encoding="utf-8"))
    tr = json.loads(TABLE_ROWS.read_text(encoding="utf-8"))["tables"]
    pred = json.loads(Path(pred_path).read_text(encoding="utf-8"))
    by = {r["id"]: r for r in pred["rows"]}
    lab = {}
    for line in open(labels_path, encoding="utf-8"):
        if line.strip():
            x = json.loads(line)
            lab[x["id"]] = x["label"]
    cols = []
    for c in s["columns"]:
        t = tr[c["table"]]
        me = next(x for x in t if x["column"] == c["id"])
        cols.append({"batch": "sealed3", "id": c["id"], "table": c["table"], "header": c["header"], "values5": c["values"],
                     "values": V.clean_values(me["rows"]) or [str(v) for v in c["values"]], "context": c.get("siblings") or [],
                     "unit": c.get("unit") or "", "truth": lab.get(c["id"]), "pred": by[c["id"]]["guarded_prediction"],
                     "top3": by[c["id"]]["top3"], "tab_all": t, "language": c.get("language", "")})
    return s, cols, pred


def decide(cols, verifier):
    """製品の形の判定（表ごと）→ [(判定, 理由)]、各段の判定も返す。"""
    base = E.base_decisions(cols)
    by = defaultdict(list)
    for k, c in enumerate(cols):
        by[c["table"]].append(k)
    P = {}
    for t, ks in by.items():
        tab_all = cols[ks[0]]["tab_all"]
        vals = [V.clean_values(x["rows"]) for x in tab_all]
        tab = [{"rows": x["rows"], "row_index": x["row_index"], "total": x["total"]} for x in tab_all]
        pt = verifier.proba(vals, tab)
        pos = {x["column"]: i for i, x in enumerate(tab_all) if x["column"]}
        for k in ks:
            P[k] = pt[pos[cols[k]["id"]]]
    labels = verifier.labels
    after_v = [V.veto(base[k][0], P[k], labels, TAU) for k in range(len(cols))]
    after_v = [f if f[1] else base[k] for k, f in enumerate(after_v)]
    final = []
    for k, d in enumerate(after_v):
        c = V.candidate(d[0], d[1], cols[k]["pred"], cols[k]["top3"], cols[k]["header"], P[k], labels, RHO_ASSERT)
        final.append((c, "assert") if c else d)
    return base, after_v, final


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", required=True)
    ap.add_argument("--pred", required=True)
    ap.add_argument("--out", default="bench/independent_eval_sealed3-20261025-v1.md")
    a = ap.parse_args(argv)
    s, cols, pred = load(a.labels, a.pred)
    v = V.Verifier.load(VERIFIER)
    v.risk = None   # 重大検知役は使わない（事前登録）
    base, after_v, final = decide(cols, v)
    stages = [("見張りだけ", [(c["pred"], None) for c in cols]), ("＋ recheck v1", base), ("＋ 検査役 v2", after_v),
              ("＋ 候補を言い切りに戻す（製品の形）", final)]
    res = [(n, E.score([d[0] for d in x], cols)) for n, x in stages]
    sf = res[-1][1]
    n, crit, unk = sf["n"], sf["critical"], sf["unknown"]
    cr, ur = (crit / n if n else 1.0), (unk / n if n else 1.0)
    ub = upper_bound(crit, n)
    verdict = ("合格" if n >= MIN_SCORED and cr <= MAX_CRITICAL and ur <= MAX_UNKNOWN else
               "列が足りない（判定できない）" if n < MIN_SCORED else "不合格")
    crit_cols = [(c["id"], c["truth"], d[0]) for c, d in zip(cols, final) if c["truth"] in V.NUMERIC and d[0] in V.NUMERIC and d[0] != c["truth"]]
    L = [f"# 封印セット #3 の採点（{s['set_id']}、`independent_eval/sealed3_score.py`）", "",
         f"- 予測：`{Path(a.pred).name}`（重み {pred.get('checkpoint', {}).get('weights_sha256', '')}）",
         f"- ラベル：SHA-256 `{hashlib.sha256(Path(a.labels).read_bytes()).hexdigest()}`（非公開。公開するのは集計だけ）",
         f"- 検査役：`models/verifier_v2.json` SHA-256 `{hashlib.sha256(VERIFIER.read_bytes()).hexdigest()}`、tau＝{TAU}、rho_assert＝{RHO_ASSERT}、重大検知役なし",
         "", "| 判定 | 結果 |", "|---|---|"] + [f"| {nm} | {E.fmt(x)} |" for nm, x in res] + [
         "", f"## 判定（事前登録の線：採点 {MIN_SCORED} 列以上・重大 ≤ {MAX_CRITICAL:.1%}・不明 ≤ {MAX_UNKNOWN:.0%}）",
         f"- 採点した列 **{n}**、重大 **{crit}（{cr:.2%}、90% の上限 {ub:.2%}）**、不明 **{unk}（{ur:.1%}）** → **{verdict}**",
         f"- 残った重大の列（見直す。正解のラベルの誤りなら裁定の記録に LP 番号で残し、直した数字も併記する）：{', '.join(f'{i}（正解 {t} → {p}）' for i, t, p in crit_cols) or 'なし'}",
         "", "### 種類の組ごとの重大", "| 組 | " + " | ".join(nm for nm, _ in stages) + " |", "|---|" + "---:|" * len(stages)]
    cp = [E.crit_pairs([d[0] for d in x], cols) for _, x in stages]
    for k in sorted(set().union(*cp), key=lambda k: -cp[0].get(k, 0)):
        L.append(f"| {k} | " + " | ".join(str(c.get(k, 0)) for c in cp) + " |")
    lang = Counter(c["language"] for c in cols)
    L += ["", f"- 列の言語：{dict(lang)}"]
    Path(a.out).write_text("\n".join(L) + "\n", encoding="utf-8")
    for nm, x in res:
        print(nm, E.fmt(x))
    print(verdict, f"critical {cr:.4f} (ub {ub:.4f}) unknown {ur:.4f} n {n}")


if __name__ == "__main__":
    main()
