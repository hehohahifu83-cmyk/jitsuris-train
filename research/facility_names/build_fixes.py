"""LABEL_GUIDE v2.4 の付け直しのファイルを作る（2026-11-01 Claude、オーナー「やれ」）。教材庫・評価の陣のファイルは書き換えない。

  python research/facility_names/build_fixes.py
    → materials/pool/labelfix_g24_b3.jsonl        B3 の 42 行の裁定（research/b3_review/final.tsv）のうち、labelfix_v24 を当てた後でも違う行
    → materials/pool/labelfix_g24_sheet.jsonl     施設の名称 386 行の裁定（final.tsv）のうち教材庫の 200 行で、今と違う行
    → research/labels/facility_v24/eval_decisions.jsonl
                                                  評価の陣（D1・E1/E2・E3）の v2.4 版の正解（d1_eval.label_fixes の形。古い正解は消さない）
  教材庫の残りの施設の名称の列（pool_sheet.tsv、2,223 行）は、先生 2 人の答えの裁定のあとで labelfix_g24_pool.jsonl にする。

学習で使うとき：FT_LABELFIX=materials/pool/labelfix_v24.jsonl,materials/pool/labelfix_g24_b3.jsonl,materials/pool/labelfix_g24_sheet.jsonl,…
（apply_label_fix は (表, 列名) と元のラベルが合う行だけ付け直す。後のファイルが勝つ）
"""
import csv, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "bench"))
POOL = os.path.join(ROOT, "materials", "pool")
READING = re.compile(r"(カナ|かな|ｶﾅ|フリガナ|ふりがな|よみ|読み|英字|英語|ローマ字|通称)")


def norm(h):
    return str(h).replace("\n", " ").strip()


def pool_index():
    idx = {}
    for p in sorted(glob.glob(os.path.join(POOL, "batch_*.jsonl"))):
        f = os.path.basename(p)
        for i, line in enumerate(open(p, encoding="utf-8")):
            idx[f"{f[6:-6]}#{i}"] = (f, i, json.loads(line))
    return idx


def v24_effective():
    fx = {}
    for line in open(os.path.join(POOL, "labelfix_v24.jsonl"), encoding="utf-8"):
        d = json.loads(line)
        if d["decision"] == "change":
            fx[(d["table"], norm(d["header"]))] = d["label"]
    return fx


def write(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(os.path.relpath(path, ROOT), len(rows))


def main():
    idx = pool_index()
    v24 = v24_effective()
    # B3
    out = []
    for x in csv.DictReader(open(os.path.join(ROOT, "research", "b3_review", "final.tsv"), encoding="utf-8"), delimiter="\t"):
        f, i, r = idx[x["id"]]
        eff = v24.get((r["table"], norm(r["header"])), r["label"])
        if eff != x["label_final"]:
            out.append({"file": f, "line": i, "rule": "B3_kind_code", "header": r["header"], "table": r["table"], "values": r["values"][:5],
                        "from": eff, "decision": "change", "label": x["label_final"],
                        "reason": "LABEL_GUIDE v2.4 B3（ChatGPT の答え・Claude の確かめ、research/b3_review/final.tsv）", "decided_by": "chatgpt+claude-g24-20261101"})
    write(os.path.join(POOL, "labelfix_g24_b3.jsonl"), out)
    # 施設の名称：386 行のうち教材庫の 200 行
    fin = list(csv.DictReader(open(os.path.join(HERE, "final.tsv"), encoding="utf-8"), delimiter="\t"))
    out = []
    for x in fin:
        if x["set"] != "train" or x["label_final"] == x["label_now"]:
            continue
        f, i, r = idx[x["id"]]
        out.append({"file": f, "line": i, "rule": "B10_facility_name", "header": r["header"], "table": r["table"], "values": r["values"][:5],
                    "from": r["label"], "decision": "change", "label": x["label_final"],
                    "reason": "LABEL_GUIDE v2.4 B10（research/facility_names/final.tsv）" + (f"：{x['note']}" if x["note"] else ""), "decided_by": "chatgpt+claude-g24-20261101"})
    write(os.path.join(POOL, "labelfix_g24_sheet.jsonl"), out)
    # 評価の陣：同じ陣の同じ表・同じ列名の列と、その読み・英字・通称の列に当てる
    import d1_counts
    ev = [x for x in fin if x["set"] != "train"]
    by_batch = {}
    for x in ev:
        b, i = x["id"].split("#")
        by_batch.setdefault(b, []).append((int(i), x))
    out = []
    for b, items in sorted(by_batch.items()):
        corpus, labels = d1_counts.batch_rows(b)
        sets = json.load(open(os.path.join(POOL, "work", b, "set.json"), encoding="utf-8"))["columns"]
        for i, x in items:
            c0 = corpus[i]
            base = norm(c0["header"])
            for j, (c, l) in enumerate(zip(corpus, labels)):
                if c["table"] != c0["table"]:
                    continue
                h = norm(c["header"])
                same = h == base or (READING.search(h) and h.startswith(base[:2]) and l["label"] == labels[i]["label"])
                if not same or l["label"] not in ("org", "address", "unknown"):
                    continue
                if l["label"] != x["label_final"]:
                    out.append({"id": sets[j]["id"], "current": l["label"], "decision": x["label_final"], "by": "chatgpt+claude-g24",
                                "reason": f"LABEL_GUIDE v2.4 B10（final.tsv {x['no']}）" + ("" if h == base else "：読み・英字・通称の列は名前の列に合わせる")})
    seen, uniq = set(), []
    for d in out:
        if d["id"] not in seen:
            seen.add(d["id"]); uniq.append(d)
    write(os.path.join(ROOT, "research", "labels", "facility_v24", "eval_decisions.jsonl"), uniq)


if __name__ == "__main__":
    main()
