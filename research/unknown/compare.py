"""不明になった列の調査：先生 2 人（ChatGPT・Grok）の答えを、正解・今の仕組みの段と突き合わせる（2026-10-29 Claude）。
入力：columns.jsonl・sheet_index.json・answers_chatgpt/・answers_grok/
出力：research/unknown/compare.md（集計）・research/unknown/compare.jsonl（1 行＝1 列。正解・2 人の答え・段・本体の答え）
使い方：python research/unknown/compare.py
"""
import glob
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
NUMERIC = {"date", "amount", "quantity", "rate", "id"}
SCORED = 2852  # 新しい陣 8 つの採点列（summary.md）
TARGET = 0.10
WHO = ("chatgpt", "grok")


def load_answers(who):
    out = {}
    for p in sorted(glob.glob(os.path.join(HERE, f"answers_{who}", "sheet_*.tsv"))):
        for line in open(p, encoding="utf-8"):
            f = line.rstrip("\n").split("\t")
            if len(f) >= 2 and f[0].startswith("u"):
                out[f[0]] = {"label": f[1].strip(), "cue": f[2].strip() if len(f) > 2 else "", "memo": f[3].strip() if len(f) > 3 else ""}
    return out


def answered(lab):
    return lab not in ("unknown", "S", "")


def tally(pairs):
    """pairs：(答え, 正解)。答えた数・正しい・重大（正解が数字の種類で取り違え）・ほかの誤り。"""
    n = ok = crit = wrong = 0
    for a, t in pairs:
        if not answered(a):
            continue
        n += 1
        if a == t:
            ok += 1
        elif t in NUMERIC:
            crit += 1
        else:
            wrong += 1
    return n, ok, crit, wrong


def cell(pairs, total):
    n, ok, crit, wrong = tally(pairs)
    acc = f"{ok / n:.1%}" if n else "—"
    return f"{n}/{total} | {ok} | {acc} | {crit} | {wrong}"


def main():
    cols = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}
    index = json.load(open(os.path.join(HERE, "sheet_index.json"), encoding="utf-8"))["items"]
    ans = {w: load_answers(w) for w in WHO}
    rows = []
    for it in index:
        c = cols[it["id"]]
        g, k = ans["chatgpt"].get(it["u"]), ans["grok"].get(it["u"])
        top1 = c["model_top3"][0][0] if c["model_top3"] else None
        rows.append({"u": it["u"], "id": c["id"], "batch": c["batch"], "header": c["header"], "values": c["values"][:5], "title": c["title"],
                     "truth": c["truth"], "stage": c["stage"], "reason": c["guard_reason"] or c["base_reason"] or c["veto_reason"],
                     "model_top1": top1, "verifier_top": c["verifier_top"][0],
                     "chatgpt": g["label"] if g else "", "chatgpt_cue": g["cue"] if g else "", "chatgpt_memo": g["memo"] if g else "",
                     "grok": k["label"] if k else "", "grok_cue": k["cue"] if k else "", "grok_memo": k["memo"] if k else ""})
    with open(os.path.join(HERE, "compare.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    N = len(rows)
    missing = {w: sum(1 for r in rows if not r[w]) for w in WHO}
    head = "| | 答えた/全体 | 正しい | 正しい割合 | 重大 | ほかの誤り |\n|---|---|---:|---:|---:|---:|"
    agree = [r for r in rows if answered(r["chatgpt"]) and r["chatgpt"] == r["grok"]]
    L = ["# 不明になった列の調査：先生 2 人の突き合わせ（`research/unknown/compare.py`）", "",
         f"- 列 {N}（新しい陣 8 つ・採点 {SCORED} 列の不明）。答えの欠け：ChatGPT {missing['chatgpt']}・Grok {missing['grok']}",
         "- 重大＝正解が数字の種類（date・amount・quantity・rate・id）なのに別の種類と答えたもの（verifier_eval と同じ数え方）",
         f"- 合格線：不明 {TARGET:.0%} 以下＝{int(SCORED * TARGET)} 列以下。今 {N} 列なので **{N - int(SCORED * TARGET)} 列以上**を重大なしで答えにする必要がある", "",
         "## 先生ごと・組み合わせ", "", head,
         f"| ChatGPT | {cell([(r['chatgpt'], r['truth']) for r in rows], N)} |",
         f"| Grok | {cell([(r['grok'], r['truth']) for r in rows], N)} |",
         f"| 2 人一致（同じ種類を答えた） | {cell([(r['chatgpt'], r['truth']) for r in agree], N)} |",
         f"| 2 人一致かつ本体の 1 位も同じ | {cell([(r['chatgpt'], r['truth']) for r in agree if r['model_top1'] == r['chatgpt']], N)} |",
         f"| 2 人一致かつ検査役の 1 位も同じ | {cell([(r['chatgpt'], r['truth']) for r in agree if r['verifier_top'] == r['chatgpt']], N)} |",
         f"| 本体の 1 位（参考：不明にしなかったら） | {cell([(r['model_top1'] or '', r['truth']) for r in rows], N)} |", ""]
    both_unk = sum(1 for r in rows if not answered(r["chatgpt"]) and not answered(r["grok"]))
    one = sum(1 for r in rows if answered(r["chatgpt"]) != answered(r["grok"]))
    split = sum(1 for r in rows if answered(r["chatgpt"]) and answered(r["grok"]) and r["chatgpt"] != r["grok"])
    L += [f"- 2 人とも決められない：{both_unk}・片方だけ答えた：{one}・2 人とも答えて種類が分かれた：{split}・2 人一致：{len(agree)}", ""]

    L += ["## 不明にした段ごと（2 人一致の列）", "", "| 段 | 列 | 2 人一致 | うち正しい | 重大 | 本体の 1 位が正解 |", "|---|---:|---:|---:|---:|---:|"]
    for st, n in Counter(r["stage"] for r in rows).most_common():
        sub = [r for r in rows if r["stage"] == st]
        a = [r for r in sub if r in agree]
        _, ok, crit, _ = tally([(r["chatgpt"], r["truth"]) for r in a])
        L.append(f"| {st} | {n} | {len(a)} | {ok} | {crit} | {sum(r['model_top1'] == r['truth'] for r in sub)} |")
    L += ["", "## 理由ごと（2 人一致の列）", "", "| 理由 | 列 | 2 人一致 | うち正しい | 重大 |", "|---|---:|---:|---:|---:|"]
    for rs, n in Counter(r["reason"] for r in rows).most_common():
        a = [r for r in agree if r["reason"] == rs]
        _, ok, crit, _ = tally([(r["chatgpt"], r["truth"]) for r in a])
        L.append(f"| {rs} | {n} | {len(a)} | {ok} | {crit} |")
    L += ["", "## 正解の種類ごと", "", "| 正解 | 列 | ChatGPT 正しい | Grok 正しい | 2 人一致で正しい | 2 人とも決められない |", "|---|---:|---:|---:|---:|---:|"]
    for t, n in Counter(r["truth"] for r in rows).most_common():
        sub = [r for r in rows if r["truth"] == t]
        L.append(f"| {t} | {n} | {sum(r['chatgpt'] == t for r in sub)} | {sum(r['grok'] == t for r in sub)} | {sum(r in agree and r['chatgpt'] == t for r in sub)} | "
                 f"{sum(not answered(r['chatgpt']) and not answered(r['grok']) for r in sub)} |")
    L += ["", "## 決め手ごと（2 人一致の列。ChatGPT の決め手で数える）", "", "| 決め手 | 2 人一致 | うち正しい | 重大 |", "|---|---:|---:|---:|"]
    for cue, n in Counter(r["chatgpt_cue"] for r in agree).most_common():
        a = [r for r in agree if r["chatgpt_cue"] == cue]
        _, ok, crit, _ = tally([(r["chatgpt"], r["truth"]) for r in a])
        L.append(f"| {cue} | {n} | {ok} | {crit} |")
    L += ["", "## 決め手ごと（答えた列の正しい割合）", "", "| 先生 | 決め手 | 答えた | 正しい | 重大 |", "|---|---|---:|---:|---:|"]
    for w in WHO:
        for cue, _ in Counter(r[w + "_cue"] for r in rows if answered(r[w])).most_common():
            n, ok, crit, _ = tally([(r[w], r["truth"]) for r in rows if r[w + "_cue"] == cue])
            L.append(f"| {w} | {cue} | {n} | {ok} | {crit} |")

    wrong = [r for r in agree if r["chatgpt"] != r["truth"]]
    L += ["", f"## 2 人一致なのに正解と違う列（{len(wrong)}。正解の付け間違いの疑いを含む）", "", "| u | id | 見出し | 値 | 正解 | 2 人 | 本体 1 位 |", "|---|---|---|---|---|---|---|"]
    for r in wrong:
        L.append(f"| {r['u']} | {r['id']} | {r['header'][:40]} | {' / '.join(v[:15] for v in r['values'][:3])} | {r['truth']} | {r['chatgpt']} | {r['model_top1']} |")
    open(os.path.join(HERE, "compare.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:20]))


if __name__ == "__main__":
    main()
