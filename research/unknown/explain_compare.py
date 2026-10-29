"""ChatGPT の説明（explain/answers_chatgpt/）と Claude の推論（explain/claude_reasoning.jsonl）・正解を突き合わせ、C3 の判断のルールの候補をまとめる（2026-10-29 Claude）。
規則の下書き（rules_draft.py）を新しい陣 8 つの採点列すべて（final_c21.jsonl）に当て、今答えている列を誤らせないかも数える。
出力：explain/compare.md
使い方：python research/unknown/explain_compare.py
"""
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "explain")
sys.path.insert(0, HERE)
from rules_draft import NUMERIC, RULES, decide, guard_name_numeric  # noqa: E402

FIELDS = {"種類": "label", "決め手": "cue", "前回の答えを変えるか": "change", "①列名・単位の語から読めること": "f1", "②表の題名から読めること": "f2",
          "③同じ表の列名から読めること": "f3", "④値の形から読めること": "f4", "迷った種類と、それを退けた理由": "rivals",
          "自信が低い・決められないなら、その理由と、何があれば決められたか": "missing", "規則にするなら": "rule", "確信": "conf"}


def parse_answers():
    """`## x0001` の見出しごとに `- 項目：中身` を読む。項目名は先頭一致（「規則にするなら（…）：」も読む）。"""
    out = {}
    for p in sorted(glob.glob(os.path.join(OUT, "answers_chatgpt", "explain_*.md"))):
        key = None
        for line in open(p, encoding="utf-8"):
            m = re.match(r"^##\s+([xe]\d{4})\b", line)
            if m:
                key = m.group(1)
                out[key] = {}
                continue
            m = re.match(r"^-\s*([^：:]+?)(?:（[^）]*）)?\s*[：:]\s*(.*)$", line.rstrip("\n"))
            if key and m:
                name = next((v for k, v in FIELDS.items() if m.group(1).strip().startswith(k)), None)
                if name:
                    out[key][name] = m.group(2).strip()
    return out


def label_of(s):
    m = re.search(r"\b(account|address|amount|category|date|email|id|org|other|person|phone|product|quantity|rate|tax_class|text|unknown|S)\b", s or "")
    return m.group(1) if m else ""


def crit(a, t):
    return a != t and a in NUMERIC and t in NUMERIC


def harm_section():
    """規則の下書きを採点列すべてに当てる。不明の列には A〜G、言い切った列には G8 と「規則が別の種類を示す」数を見る。"""
    rows = [json.loads(l) for l in open(os.path.join(HERE, "final_c21.jsonl"), encoding="utf-8")]
    unk = [r for r in rows if r["final"] == "unknown"]
    ans = [r for r in rows if r["final"] != "unknown"]
    L = ["## 規則の下書きを新しい陣 8 つの採点列すべてに当てる（決める陣での参考値）", "",
         f"- 採点列 {len(rows)}：今の答え 正しい {sum(r['final'] == r['truth'] for r in rows)}・不明 {len(unk)}・重大 {sum(crit(r['final'], r['truth']) for r in rows)}", ""]
    by = defaultdict(lambda: Counter())
    newlab = {}
    for r in unk:
        lab, rid = decide(r["header"], r["unit"], r["values"], r["siblings"])
        if lab:
            newlab[r["id"]] = lab
            by[rid]["n"] += 1
            by[rid]["ok"] += lab == r["truth"]
            by[rid]["crit"] += crit(lab, r["truth"])
    # 言い切った列：規則が別の種類を示したら（G10 の候補）、今の答えが正しいか
    dis = defaultdict(lambda: Counter())
    for r in ans:
        lab, rid = decide(r["header"], r["unit"], r["values"], r["siblings"])
        if lab and lab != r["final"]:
            dis[rid]["n"] += 1
            dis[rid]["final_ok"] += r["final"] == r["truth"]
            dis[rid]["rule_ok"] += lab == r["truth"]
            dis[rid]["rule_crit"] += crit(lab, r["truth"])
    g8 = Counter()
    for r in ans:
        g, gid = guard_name_numeric(r["final"], r["header"], r["values"])
        if gid:
            g8["n"] += 1
            g8["was_ok"] += r["final"] == r["truth"]
            g8["to_ok"] += g == r["truth"]
    L += ["### 不明の列に当てる", "", "| 規則 | 種類 | 当たった列 | 正しい | 重大 |", "|---|---|---:|---:|---:|"]
    lab_of = {r[0]: r[1] for r in RULES}
    for rid in sorted(by):
        c = by[rid]
        L.append(f"| {rid} | {lab_of.get(rid, '')} | {c['n']} | {c['ok']} | {c['crit']} |")
    ok = sum(newlab[r["id"]] == r["truth"] for r in unk if r["id"] in newlab)
    cr = sum(crit(newlab[r["id"]], r["truth"]) for r in unk if r["id"] in newlab)
    after = len(unk) - len(newlab)
    L += ["", f"- 合わせて {len(newlab)} 列が答えになる（正しい {ok}・重大 {cr}）。不明 {len(unk)} → {after}（{after / len(rows):.1%}）", "",
          "### 言い切った列で、規則が別の種類を示すもの（言い切った答えにも規則を当てる段＝G10 を足すかの判断）", "",
          "| 規則 | 列 | 今の答えが正しい | 規則の種類が正しい | 規則の種類なら重大 |", "|---|---:|---:|---:|---:|"]
    for rid in sorted(dis):
        c = dis[rid]
        L.append(f"| {rid} | {c['n']} | {c['final_ok']} | {c['rule_ok']} | {c['rule_crit']} |")
    L += ["", f"- G8（名前の種類なのに値が数字だけ）：当たった {g8['n']} 列。今の答えが正しかった {g8['was_ok']}（これを不明・id に下げると損）・下げた先が正しい {g8['to_ok']}", ""]
    return L


def main():
    mine = {json.loads(l)["key"]: json.loads(l) for l in open(os.path.join(OUT, "claude_reasoning.jsonl"), encoding="utf-8")}
    ans = parse_answers()
    L = ["# 重大・不明になった列：ChatGPT の説明と Claude の推論の突き合わせ（`research/unknown/explain_compare.py`）", "",
         f"- シートの列 {len(mine)}。ChatGPT の説明が届いた列 {sum(k in ans for k in mine)}", ""]
    L += harm_section()
    got = [k for k in mine if k in ans]
    if got:
        rows = []
        for k in got:
            m, a = mine[k], ans[k]
            g = label_of(a.get("label"))
            rows.append((k, m, a, g))
        tab = Counter()
        for k, m, a, g in rows:
            tab[(m["group"], "chatgpt_ok")] += g == m["truth"]
            tab[(m["group"], "claude_ok")] += m["claude"] == m["truth"]
            tab[(m["group"], "same")] += g == m["claude"]
            tab[(m["group"], "chatgpt_crit")] += crit(g, m["truth"])
            tab[(m["group"], "chatgpt_unknown")] += g in ("unknown", "S", "")
            tab[(m["group"], "n")] += 1
            tab[(m["group"], "changed")] += (a.get("change") or "").startswith("変える")
        L += ["## ChatGPT と Claude", "", "| 組 | 列 | ChatGPT 正しい | Claude 正しい | 2 人同じ | ChatGPT 重大 | ChatGPT 決めない | 前回から変えた |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
        for grp in ("misses", "unknown"):
            if tab[(grp, "n")]:
                L.append(f"| {grp} | {tab[(grp, 'n')]} | {tab[(grp, 'chatgpt_ok')]} | {tab[(grp, 'claude_ok')]} | {tab[(grp, 'same')]} | {tab[(grp, 'chatgpt_crit')]} | "
                         f"{tab[(grp, 'chatgpt_unknown')]} | {tab[(grp, 'changed')]} |")
        # ChatGPT は正しく決めたが Claude の規則では決まらない列＝新しい規則（H）の材料
        new = [(k, m, a, g) for k, m, a, g in rows if g == m["truth"] and m["claude"] != m["truth"]]
        L += ["", f"## 新しい規則の材料：ChatGPT は正しく、Claude の規則では決まらない列（{len(new)}）", "",
              "| 番号 | 見出し | 正解 | ChatGPT の決め手 | ChatGPT の「規則にするなら」 | 何があれば決められたか |", "|---|---|---|---|---|---|"]
        for k, m, a, g in new:
            L.append(f"| {k} | {m['header'][:40].replace('|', '/')} | {m['truth']} | {a.get('cue', '')} | {a.get('rule', '').replace('|', '/')[:200]} | {a.get('missing', '').replace('|', '/')[:120]} |")
        # 規則ごとに ChatGPT の説明が支えるか
        L += ["", "## Claude の規則ごとの、ChatGPT の判断", "", "| 規則 | 当たった列 | ChatGPT も同じ種類 | ChatGPT は別の種類（列） |", "|---|---:|---:|---|"]
        byr = defaultdict(list)
        for k, m, a, g in rows:
            if m["rule"]:
                byr[m["rule"]].append((k, m, g))
        for rid in sorted(byr):
            xs = byr[rid]
            L.append(f"| {rid} | {len(xs)} | {sum(g == m['claude'] for _, m, g in xs)} | {', '.join(f'{k}:{g}' for k, m, g in xs if g != m['claude'])} |")
        bad = [(k, m, a, g) for k, m, a, g in rows if g != m["truth"] and g not in ("unknown", "S", "")]
        L += ["", f"## ChatGPT が誤った列の説明（{len(bad)}。規則にすると誤る考え方）", "", "| 番号 | 見出し | 正解 | ChatGPT | 迷った種類と退けた理由 | ④値の形 | Claude の推論 |", "|---|---|---|---|---|---|---|"]
        for k, m, a, g in bad:
            L.append(f"| {k} | {m['header'][:40].replace('|', '/')} | {m['truth']} | {g} | {a.get('rivals', '').replace('|', '/')[:160]} | {a.get('f4', '').replace('|', '/')[:100]} | {m['note'].replace('|', '/')[:120]} |")
        unk = [(k, m, a) for k, m, a, g in rows if g in ("unknown", "S", "")]
        miss = Counter()
        for k, m, a in unk:
            t = a.get("missing", "")
            for w, pat in (("単位の列の値", r"単位|einheit|unit"), ("表の題名", r"題名|タイトル"), ("同じ表のほかの列の値", r"ほかの列|他の列|同じ表"), ("通貨", r"通貨|記号"), ("略語の意味", r"略|意味")):
                miss[w] += bool(re.search(pat, t))
        L += ["", f"## ChatGPT が決めなかった列（{len(unk)}）で「何があれば決められたか」に出た語", "", "| 足りないもの | 列 |", "|---|---:|"]
        L += [f"| {w} | {n} |" for w, n in miss.most_common()]
    open(os.path.join(OUT, "compare.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
