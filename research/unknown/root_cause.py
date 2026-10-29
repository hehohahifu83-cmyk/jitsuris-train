"""不明・重大になった列の原因の切り分け（2026-10-29 Claude。オーナー方針「新しいことをする前に徹底的に原因を突き止める」）。
列ごとに 3 つを並べる：①本体 C2 の 1 位は正解か（本体が分かっていないのか、決め方の段が止めたのか）②どの段が何の理由で止めたか
③同じ形の列が C2 の学習の教材（b001〜b014）にあったか、あればどの種類が付いていたか（rules_draft の規則で同じ形を探す）。
出力：research/unknown/root_cause.md・root_cause.jsonl
使い方：python research/unknown/root_cause.py
"""
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
import re  # noqa: E402
import unicodedata  # noqa: E402

import guard as G  # noqa: E402
import recheck as R  # noqa: E402
import verifier_eval as E  # noqa: E402
from rules_draft import RULES, decide, present  # noqa: E402

# 正解の見直しが要る列（claude_reasoning.py の NOTES で「正解を見直す」とした列の陣の id）
REVIEW = {"b017-0327","b016-0014","b017-0332","b062-0264","b017-0051"}  # u0012・u0171・u0239・u0306・u0192


def mechanism(c, rid):
    """不明になった仕組みを 1 つ選ぶ（上から順に当てる）。どれもコードや教材で確かめた原因（findings の「原因」の節）。"""
    h, vals = c["header"], c["values"]
    nf = [unicodedata.normalize("NFKC", v) for v in vals]
    reason = c["guard_reason"] or c["base_reason"] or c["veto_reason"] or ""
    split = re.sub(r"([a-z])([A-Z])", r"\1 \2", h).replace("_", " ")
    if c["truth"] in R.cue_types(split, c.get("unit", "")) and c["truth"] not in R.cue_types(h, c.get("unit", "")):
        return "M1 英語の手がかりが下線・大文字つなぎの列名で当たらない（recheck の語の境目）"
    if any("」" in v for v in nf) or "」" in unicodedata.normalize("NFKC", h):
        return "M2 文字化けの £（｣）を recheck・通貨の手がかりが読めない"
    if reason == "date_value_evidence_low" and c["model_top1_is_truth"]:
        return "M3 見張りの日付の値の形・列名の語が足りない（1900 年より前の年・週・2024-M04・Excel の日付の数など）"
    if rid == "B":
        return "M4 教材にない形（識別子の URI。教材の URI はリンクだけ＝other）"
    if rid == "C" or re.search(r"energieverbrauch|energy (use|consumption)", h, re.I):
        return "M5 教材の付け方の食い違い（電力量・エネルギー：b005・b014 は quantity、b006・b007・b011 は other）"
    if not present(vals):
        return "M8 値がすべて欠けの記号（[x]・.・NA）"
    if re.fullmatch(r"(value|wert|obs_value)", h.strip(), re.I):
        return "M7 汎用の値の列で、単位・指標の列の値が決め方に渡っていない"
    if rid and rid.startswith("D"):
        return "M6 手がかりの辞書にドイツ語がない"
    if reason.startswith("cue_conflict") and c.get("unit") and not R.cue_types(h, "") & {"amount", "rate", "quantity"}:
        return "M12 表全体の単位の列（UNIT: %）を、値でない列（コード・年）にも当てて手がかりがぶつかる"
    if re.search(r"cost cent(re|er)", h, re.I):
        return "M13 金額の語（cost）が部署の番号の列名（Cost Centre）に当たって手がかりがぶつかる"
    if reason.startswith("verifier:") and (R.cue_types(h, c.get("unit", "")) - {reason.split(":")[1]}):
        return "M14 検査役が列名の強い手がかりを見ずに下げる"
    if c["id"] in REVIEW:
        return "M9 正解の見直しが要る"
    if c["model_top1_is_truth"]:
        return "M10 本体は正しいが、決め方の段が止めた（ほかの理由）"
    return "M11 本体が誤り（ほかの理由）"

TRAIN = tuple(f"b{n:03d}" for n in range(1, 15))   # C2 の学習（FT_POOL=1、2026-10-25 run 40202377192）


def main():
    train_hits = defaultdict(Counter)
    for b in TRAIN:
        for c in E.load_batch(b):
            if not c.get("truth"):
                continue
            lab, rid = decide(c["header"], c.get("unit"), [str(v) for v in c["values"][:8]], c.get("context") or [])
            if rid and rid != "conflict":
                train_hits[rid][c["truth"]] += 1
    cols = [json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")]
    rows = []
    for c in cols:
        lab, rid = decide(c["header"], c.get("unit"), c["values"], c["siblings"])
        reason = c["guard_reason"] or c["base_reason"] or c["veto_reason"]
        th = train_hits.get(rid, Counter()) if rid and rid != "conflict" else Counter()
        if c["model_top1_is_truth"]:
            cause = "決め方の段が止めた（本体は正しい）"
        elif not rid or rid == "conflict":
            cause = "本体が誤り・形の規則なし"
        elif th[c["truth"]] >= 3:
            cause = "本体が誤り・同じ形は教材にあった"
        else:
            cause = "本体が誤り・同じ形が教材にない"
        rows.append({"id": c["id"], "header": c["header"], "truth": c["truth"], "stage": c["stage"], "reason": reason,
                     "model_top1": c["model_top3"][0][0], "model_top1_ok": c["model_top1_is_truth"], "rule": rid, "rule_label": lab,
                     "train_same_form": dict(th), "cause": cause})
    for r, c in zip(rows, cols):
        r["mechanism"] = mechanism(c, r["rule"])
    with open(os.path.join(HERE, "root_cause.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    L = ["# 不明・重大の原因の切り分け（`research/unknown/root_cause.py`）", "",
         "- 対象：新しい陣 8 つの不明 329 列。本体 C2 の学習の教材は b001〜b014。「同じ形」は `rules_draft.py` の規則が当たる列", "",
         "## 原因の大分け", "", "| 原因 | 列 |", "|---|---:|"]
    L += [f"| {k} | {n} |" for k, n in Counter(r["cause"] for r in rows).most_common()]
    L += ["", "## 仕組みごと（上から順に当てて 1 つ選ぶ）", "", "| 仕組み | 列 | うち本体は正しい | 正解の種類 |", "|---|---:|---:|---|"]
    for m, n in sorted(Counter(r["mechanism"] for r in rows).items()):
        xs = [r for r in rows if r["mechanism"] == m]
        L.append(f"| {m} | {n} | {sum(r['model_top1_ok'] for r in xs)} | {', '.join(f'{a} {b}' for a, b in Counter(r['truth'] for r in xs).most_common(4))} |")
    L += ["", "## 本体は正しいのに止めた列：段と理由", "", "| 段 | 理由 | 列 | 正解の種類 |", "|---|---|---:|---|"]
    ok = [r for r in rows if r["model_top1_ok"]]
    for (st, rs), n in Counter((r["stage"], r["reason"]) for r in ok).most_common():
        t = Counter(r["truth"] for r in ok if r["stage"] == st and r["reason"] == rs)
        L.append(f"| {st} | {rs} | {n} | {', '.join(f'{a} {b}' for a, b in t.most_common())} |")
    L += ["", "## 本体が誤った列：本体の 1 位と正解", "", "| 本体の 1 位 | 正解 | 列 |", "|---|---|---:|"]
    L += [f"| {a} | {b} | {n} |" for (a, b), n in Counter((r["model_top1"], r["truth"]) for r in rows if not r["model_top1_ok"]).most_common(15)]
    L += ["", "## 規則の形ごと：不明の列と、学習の教材（b001〜b014）での同じ形", "", "| 規則 | 種類 | 不明の列 | うち本体は正しい | 教材の同じ形（付いていた種類） |", "|---|---|---:|---:|---|"]
    lab_of = {r[0]: r[1] for r in RULES}
    for rid in sorted({r["rule"] for r in rows if r["rule"] and r["rule"] != "conflict"}):
        xs = [r for r in rows if r["rule"] == rid]
        th = train_hits.get(rid, Counter())
        L.append(f"| {rid} | {lab_of.get(rid, '')} | {len(xs)} | {sum(r['model_top1_ok'] for r in xs)} | {', '.join(f'{a} {b}' for a, b in th.most_common()) or 'なし'} |")
    open(os.path.join(HERE, "root_cause.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
