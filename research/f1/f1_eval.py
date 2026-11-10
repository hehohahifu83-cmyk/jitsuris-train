"""F1（評価の陣）の 1 回だけの測り（2026-11-10 Claude。予測の前に書いて SHA を事前記録に固定する）。
事前記録：bench/g24fix_prereg_20261104.md（L24＋G 対 L＋G）・bench/fixj_prereg_20261109.md（見張り＋G 対 見張り＋G＋J）。

  python research/f1/f1_eval.py --labels <ai-bridge>/labels/f1/final.jsonl [--dry]   → research/f1/f1_eval.md・f1_eval_per_column.json

形（製品の形は E1〜E3 と同じ：見張り（G は guard.py に入っている）→ recheck → 検査役 v2 → rho → 辞書 frozen_d3 → 通貨の手がかり。
research/hfix_eval.py の P と同じ道。採点の範囲も同じ：正解が unknown・S・other・person の列は数えない）：
  L+G    ＝ L（D2 run 41192849082 の job2〜4、種子 1〜3）の予測
  L24+G  ＝ L24（run 41735353926 の job1〜3、種子 1〜3）の予測
  +J     ＝ 見張りが date を date_value_evidence_low で止め、G でも戻らない列で、値の 5 割以上が今の決まりか直し J で日付に読めれば date を残す
           （research/guard_dates/fix_j.py の j_keeps_date。値は corpus の行の値ぜんぶ）
決まり 1〜4（D2・E1〜E3 と同じ。research/d2_eval.verdict）：
  主：L24+G 対 L+G。4 の引き直しは公開元（g24fix の事前記録）。
  J：主の判定で採った方の土台（L24 を採れば L24、採らなければ L）で、+G 対 +G+J。4 の引き直しは表（fixj の事前記録）。もう一方の土台は読むだけ。
読むだけ（採否に使わない）：施設の名称の列（列名に「名称」「施設名」を含む）の正しい数、address・org の取り違え、不明の割合、公開元・ポータルごとの正しい。
"""
import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (ROOT, os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes"), os.path.join(ROOT, "independent_eval")):
    sys.path.insert(0, p)
import d1_eval as D  # noqa: E402
import d2_eval as D2  # noqa: E402
import reserve_eval as R  # noqa: E402
import f1 as F  # noqa: E402
from research.guard_dates import fix_j as J  # noqa: E402

LABELS_SHA = "dfc983a8718b07290682292019fc19ad6364aa2ca15dda6feb8cd63f65a1fd1d"
SET_SHA = "e660d46aba65fef87b5a725ac7ef0a2338f37ac89738a7ff9c74177e3507b0d9"
FIXJ_SHA = "05eca45c56e99e0a342ac4da30684806b687261e99a158214540eadc7e9b057a"
PRED_DIR = os.path.join(ROOT, "independent_eval", "predictions_f1")
SEEDS = (1, 2, 3)
PRED = {"L": {1: "pred_l_job2.json", 2: "pred_l_job3.json", 3: "pred_l_job4.json"},
        "L24": {1: "pred_l24_job1.json", 2: "pred_l24_job2.json", 3: "pred_l24_job3.json"}}
PORTAL = {"ckan.odp.jig.jp": "ODP", "data.odp.jig.jp": "ODP", "catalog-data.city.kanazawa.ishikawa.jp": "金沢", "data.city.sendai.jp": "仙台"}
JUNK = D.B.JUNK


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_f1(labels_path):
    """F1 の列（f1.json の順）。値は corpus の行の値ぜんぶ（f1.json は 5 つまで）。f1.py の select で corpus の行に戻す。"""
    set_path = os.path.join(ROOT, "independent_eval", "results", "f1", "f1.json")
    if sha(set_path) != SET_SHA:
        raise SystemExit("f1.json が凍結のものと違う")
    if sha(labels_path) != LABELS_SHA:
        raise SystemExit("確定ラベルの SHA が事前記録と違う")
    truth = {d["id"]: d["label"] for d in map(json.loads, open(labels_path, encoding="utf-8"))}
    cols5 = json.load(open(set_path, encoding="utf-8"))["columns"]
    rows = [json.loads(line) for line in open(F.WORK / "corpus.jsonl", encoding="utf-8") if line.strip()]
    picked, _ = F.select(rows)
    if len(picked) != len(cols5):
        raise SystemExit("corpus の選び直しが f1.json と合わない")
    out = []
    for c, i in zip(cols5, picked):
        r = rows[i]
        if r["header"] != c["header"]:
            raise SystemExit(f"{c['id']}: 列名が corpus と合わない")
        vals = [str(v) for v in (r.get("row_values") or r["values"]) if str(v).strip() not in JUNK] or [str(v) for v in c["values"]]
        out.append({"batch": "f1", "i": i, "id": c["id"], "table": c["table"], "header": str(c["header"]),
                    "values5": [str(v) for v in c["values"]], "values": vals, "context": [str(x) for x in c.get("siblings") or []],
                    "unit": str(c.get("unit") or ""), "language": c.get("language", ""), "truth": truth[c["id"]], "adjudicated": True,
                    "teacher": truth[c["id"]], "publisher": r["publisher"], "portal": PORTAL.get(r["table"].split("/")[2], r["table"].split("/")[2]),
                    "tab": {"rows": r.get("row_values") or r["values"], "row_index": r.get("row_index"), "total": r.get("datastore_total")}})
    return {"f1": out}


def with_j(data):
    """直し J：見張りが date を date_value_evidence_low で止め、G（fixes.date_ok）でも戻らない列だけ、J で日付に読めれば date。"""
    D.EF.FX._G4[0] = True   # G（F3・G4）の日付の判定を入れた date_ok
    res = {}
    for b, cols in data.items():
        te = []
        for c in cols:
            if (c.get("guard_reason") == "date_value_evidence_low" and c.get("top3") and c["top3"][0]["label"] == "date"
                    and c["pred"] != "date" and not D.EF.FX.date_ok(c["header"], c["values5"]) and J.j_keeps_date(c["values"])):
                c = dict(c, pred="date")
            te.append(c)
        res[b] = te
    return res


def run_arm(base, mv, labels, model, seed, j):
    data = D.with_job(base, os.path.join(PRED_DIR, PRED[model][seed]))
    if j:
        data = with_j(data)
    D.EF._PCACHE.clear()
    p = {}
    res = D.EF.run(data, mv, labels, D.PRODUCT + ("K",), per=p)
    return res, p


def mean_of(res, arm):
    return {"ok": sum(100 * res[f"{arm}{s}"][1] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
            "unk": sum(100 * res[f"{arm}{s}"][2] / res[f"{arm}{s}"][0] for s in SEEDS) / 3,
            "crit": sum(res[f"{arm}{s}"][3] for s in SEEDS),
            "wrong": sum(100 * res[f"{arm}{s}"][4] / res[f"{arm}{s}"][0] for s in SEEDS) / 3}


def judge(per, res, a, b, cluster):
    """b が a より良いかを決まり 1〜4 で。cluster：列 id → 引き直しの単位。"""
    p2 = {f"A{s}": per[f"{a}{s}"] for s in SEEDS} | {f"L{s}": per[f"{b}{s}"] for s in SEEDS}
    lo, hi = D2.pooled_boot(p2, cluster)
    d_ok, d_crit, d_wrong, checks, ok = D2.verdict({"A": mean_of(res, a), "L": mean_of(res, b)}, lo)
    return {"d_ok": d_ok, "d_crit": d_crit, "d_wrong": d_wrong, "lo": lo, "hi": hi, "checks": checks, "adopt": ok}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", required=True)
    ap.add_argument("--dry", action="store_true", help="書き出さない（試し）")
    a = ap.parse_args(argv)
    if sha(os.path.join(ROOT, "research", "guard_dates", "fix_j.py")) != FIXJ_SHA:
        raise SystemExit("fix_j.py が事前記録の SHA と違う")
    f, dsha = R.DICTS["K"]
    if sha(os.path.join(ROOT, "materials", "dictionary", f)) != dsha:
        raise SystemExit("辞書が凍結したものと違う")
    os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", f)
    D.EF._DICT.clear()
    labels = list(D.V.LABELS)
    train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    base = load_f1(a.labels)
    cols = {c["id"]: c for c in base["f1"]}
    res, per, raw = {}, {}, {}
    for model in ("L", "L24"):
        for j in (False, True):
            arm = model + ("+G+J" if j else "+G")
            for s in SEEDS:
                r, p = run_arm(base, mv, labels, model, s, j)
                res[f"{arm}{s}"], raw[f"{arm}{s}"] = r, p
                per[f"{arm}{s}"] = {k: D.outcome(v[0], v[1]) for k, v in p.items()}
    if len({r[0] for r in res.values()}) != 1:
        raise SystemExit("採点列の数が形で違う")
    n = res["L+G1"][0]
    by_pub = {k: cols[k]["publisher"] for k in per["L+G1"]}
    by_tab = {k: cols[k]["table"] for k in per["L+G1"]}
    main_v = judge(per, res, "L+G", "L24+G", by_pub)
    jb = "L24" if main_v["adopt"] else "L"
    other = "L" if jb == "L24" else "L24"
    j_v = judge(per, res, f"{jb}+G", f"{jb}+G+J", by_tab)
    j_other = judge(per, res, f"{other}+G", f"{other}+G+J", by_tab)
    mk = lambda b: "○" if b else "×"  # noqa: E731
    L = ["# F1 の 1 回だけの測り（`research/f1/f1_eval.py`）", "",
         f"- 事前記録 `bench/g24fix_prereg_20261104.md`・`bench/fixj_prereg_20261109.md`。採点 {n} 列（正解が unknown・S・other・person の列を除く）。",
         f"- 正解：先生 2 人（Claude・Codex）の独立のラベルの裁定。SHA-256 {LABELS_SHA}。**留保**：Codex のラベルの前に Claude の内訳と境目の方針が連絡箱で見えていた（ai-bridge `labels/f1/adjudication.md`）。",
         "- F1 は日本の 3 ポータル（ODP の自治体・金沢市・仙台市）だけ。日本の自治体全般への汎化は言えない。", "",
         "| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |", "|---|---:|---:|---:|---:|---|"]
    for arm in ("L+G", "L24+G", "L+G+J", "L24+G+J"):
        m = mean_of(res, arm)
        L.append(f"| {arm} | {m['ok']:.2f}% | {m['unk']:.2f}% | {m['crit']} | {m['wrong']:.2f}% | " + "・".join(str(res[f'{arm}{s}'][1]) for s in SEEDS) + " |")

    def block(title, v):
        return ["", f"## {title}", "", f"- 1. 正しい {v['d_ok']:+.2f} {mk(v['checks'][0])}", f"- 2. 重大 {v['d_crit']:+d} {mk(v['checks'][1])}",
                f"- 3. ほかの誤り {v['d_wrong']:+.2f} {mk(v['checks'][2])}", f"- 4. 90% 区間 {v['lo']:+.2f}〜{v['hi']:+.2f} {mk(v['checks'][3])}",
                f"- **判定：{'確かめられた（採る）' if v['adopt'] else '確かめられなかった'}**"]
    L += block("主：L24+G 対 L+G（公開元で引き直す）", main_v)
    L += block(f"直し J：{jb}+G 対 {jb}+G+J（表で引き直す。主の判定で採った土台）", j_v)
    L += block(f"読むだけ：{other}+G 対 {other}+G+J", j_other)
    L += ["", "## 読むだけ（採否に使わない）", "", "| 形 | 施設の名称の列の正しい | address→org | org→address | ODP | 金沢 | 仙台 |", "|---|---:|---:|---:|---:|---:|---:|"]
    fac = [k for k in per["L+G1"] if re.search(r"名称|施設名", cols[k]["header"])]
    for arm in ("L+G", "L24+G"):
        okf = sum(per[f"{arm}{s}"][k] == "ok" for s in SEEDS for k in fac) / 3
        ao = sum(raw[f"{arm}{s}"][k][1] == "address" and raw[f"{arm}{s}"][k][0] == "org" for s in SEEDS for k in raw[f"{arm}{s}"]) / 3
        oa = sum(raw[f"{arm}{s}"][k][1] == "org" and raw[f"{arm}{s}"][k][0] == "address" for s in SEEDS for k in raw[f"{arm}{s}"]) / 3
        port = []
        for pn in ("ODP", "金沢", "仙台"):
            ks = [k for k in per["L+G1"] if cols[k]["portal"] == pn]
            port.append(f"{100 * sum(per[f'{arm}{s}'][k] == 'ok' for s in SEEDS for k in ks) / (3 * len(ks)):.1f}%（{len(ks)}）" if ks else "—")
        L.append(f"| {arm} | {okf:.1f}/{len(fac)} | {ao:.1f} | {oa:.1f} | " + " | ".join(port) + " |")
    L += ["", "### 公開元ごとの正しい（L+G → L24+G、3 本の平均）", "", "| 公開元 | 列 | L+G | L24+G |", "|---|---:|---:|---:|"]
    pubs = defaultdict(list)
    for k in per["L+G1"]:
        pubs[cols[k]["publisher"]].append(k)
    for pb, ks in sorted(pubs.items(), key=lambda x: -len(x[1])):
        f = lambda arm: 100 * sum(per[f"{arm}{s}"][k] == "ok" for s in SEEDS for k in ks) / (3 * len(ks))  # noqa: E731
        L.append(f"| {pb} | {len(ks)} | {f('L+G'):.1f}% | {f('L24+G'):.1f}% |")
    L += ["", "## 直し J が変えた列（3 本）", "", "| 土台 | 本 | id | 列名 | 正解 | +G | +G+J |", "|---|---|---|---|---|---|---|"]
    for model in ("L", "L24"):
        for s in SEEDS:
            x, y = raw[f"{model}+G{s}"], raw[f"{model}+G+J{s}"]
            for k in sorted(x):
                if x[k][0] != y[k][0]:
                    L.append(f"| {model} | {s} | {k} | {str(x[k][2])[:30]} | {x[k][1]} | {x[k][0]} | {y[k][0]} |")
    text = "\n".join(L) + "\n"
    print(text)
    if a.dry:
        return
    open(os.path.join(HERE, "f1_eval.md"), "w", encoding="utf-8").write(text)
    json.dump({k: v for k, v in per.items()}, open(os.path.join(HERE, "f1_eval_per_column.json"), "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    main()
