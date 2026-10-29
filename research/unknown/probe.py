"""本体が誤った列（root_cause の M11）が、入力のどこに引っ張られて誤ったかを本体に直接聞く（2026-10-30 Claude）。
列ごとに入力を 1 か所だけ変えた形を作り、同じ C2 種子 1 で予測する（題名は入れない＝今までの予測の形）。
  v0：そのまま ／ h：列名を意味のない「x」に ／ s：同じ表の列名を外す ／ c：値を整える（千の区切り・末尾の 0 を外し、欠けの記号を除いて、足りなければ表の後ろの行の値で埋める）
どの形で本体の 1 位が変わるかで、列名・同じ表の列名・値の形のどれが誤りを生んだかが分かる。
  python research/unknown/probe.py make   → materials/pool/work/probe1030/set.json（予測の依頼：run … pred_c2_seed1.json c2）
  python research/unknown/probe.py read   → research/unknown/probe.md
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from rules_draft import present  # noqa: E402

OUT = os.path.join(ROOT, "materials", "pool", "work", "probe1030")
VARIANTS = ("v0", "h", "s", "c")


def clean(v):
    v = v.strip()
    if re.fullmatch(r"[-+]?\d{1,3}(,\d{3})+(\.\d+)?", v):
        v = v.replace(",", "")
    if re.fullmatch(r"[-+]?\d+\.\d+", v):
        v = v.rstrip("0").rstrip(".")
    return v


def make():
    rc = [json.loads(l) for l in open(os.path.join(HERE, "root_cause.jsonl"), encoding="utf-8")]
    ids = [r["id"] for r in rc if r["mechanism"].startswith("M11")]
    sets = {}
    for b in sorted({i[:4] for i in ids}):
        for c in json.load(open(os.path.join(ROOT, "materials", "pool", "work", b, "set.json"), encoding="utf-8"))["columns"]:
            sets[c["id"]] = c
    import verifier_eval as E
    full = {}
    for b in sorted({i[:4] for i in ids}):
        for c in E.load_batch(b):
            full[c["id"]] = [str(v) for v in c["values"]]
    cols = []
    for i in ids:
        c = sets[i]
        cv = [clean(v) for v in present(c["values"])]
        if len(cv) < 5:
            cv += [clean(v) for v in present(full.get(i, [])) if clean(v) not in cv][:5 - len(cv)]
        for var in VARIANTS:
            d = dict(c, id=f"{i}~{var}")
            if var == "h":
                d["header"] = "x"
            elif var == "s":
                d["siblings"] = []
            elif var == "c":
                d["values"] = cv or c["values"]
            cols.append(d)
    os.makedirs(OUT, exist_ok=True)
    json.dump({"schema_version": 1, "set_id": "label-assist-probe1030", "columns": cols}, open(os.path.join(OUT, "set.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(ids)} 列 × {len(VARIANTS)} 形 = {len(cols)}")


def read():
    pred = {r["id"]: r for r in json.load(open(os.path.join(OUT, "pred_c2_seed1.json"), encoding="utf-8"))["rows"]}
    truth = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}
    ids = sorted({k.split("~")[0] for k in pred})
    top = lambda k: (pred[k]["top3"][0]["label"], pred[k]["top3"][0]["probability"])
    rows, cause = [], Counter()
    for i in ids:
        t = truth[i]["truth"]
        v0 = top(f"{i}~v0")[0]
        flips = [var for var in ("h", "s", "c") if top(f"{i}~{var}")[0] != v0]
        fixed = [var for var in ("h", "s", "c") if top(f"{i}~{var}")[0] == t]
        if v0 == t:
            k = "そのままで正しい（M11 は決め方の段の前の本体の答えと違う）"
        elif "h" in fixed:
            k = "列名を消すと正しくなる＝列名に引っ張られた"
        elif "c" in fixed:
            k = "値を整えると正しくなる＝値の形に引っ張られた"
        elif "s" in fixed:
            k = "同じ表の列名を外すと正しくなる＝同じ表の列名に引っ張られた"
        elif flips:
            k = "1 か所変えると答えは変わるが、正しくはならない"
        else:
            k = "どこを 1 か所変えても答えが変わらない"
        cause[k] += 1
        rows.append((k, i, truth[i]["header"], t, [top(f"{i}~{var}") for var in VARIANTS]))
    L = ["# 本体に直接聞く：入力を 1 か所変えると答えはどう変わるか（`research/unknown/probe.py`）", "",
         "同じ C2 種子 1・題名なし。本体が誤った 73 列（M11）。v0 そのまま／h 列名を「x」に／s 同じ表の列名を外す／c 値を整える", "",
         "| 分け | 列 |", "|---|---:|"]
    L += [f"| {k} | {n} |" for k, n in cause.most_common()]
    L += ["", "| 分け | id | 見出し | 正解 | v0 | h | s | c |", "|---|---|---|---|---|---|---|---|"]
    for k, i, h, t, tops in sorted(rows):
        L.append(f"| {k[:12]} | {i} | {str(h)[:28].replace('|', '/')} | {t} | " + " | ".join(f"{a} {p:.2f}" for a, p in tops) + " |")
    open(os.path.join(HERE, "probe.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:14]))


if __name__ == "__main__":
    make() if sys.argv[1:] == ["make"] else read()
