"""古い陣の「種類のコード」の列の見直しの材料（2026-11-01 Claude。ChatGPT の意見 (d)「同じ意味の列だけを行ごとに見直す」）。
教材庫（materials/pool/batch_*.jsonl）で、列名が「種類の語＋コードの語尾」（research/fixes/fixes_h.py の type_code_header）の列を集める。
今のラベル（id・category など）と、LABEL_GUIDE v2.3 の B3 で付けたときのラベルを比べる欄つき。直すのはオーナーの承認のあと。
  python research/b3_review/collect.py → research/b3_review/sheet.tsv
"""
import csv, glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "research", "fixes"))
import fixes_h  # noqa: E402

out = []
for p in sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl"))):
    for i, line in enumerate(open(p, encoding="utf-8")):
        r = json.loads(line)
        if r.get("label") in ("id", "category") and fixes_h.type_code_header(r["header"]):
            out.append([f"{os.path.basename(p)[6:-6]}#{i}", str(r["header"]).replace("\n", " "), " | ".join(str(v)[:25] for v in r["values"][:5]),
                        ", ".join(str(x)[:15] for x in r.get("context", [])[:8]), r["label"], "", ""])
with open(os.path.join(HERE, "sheet.tsv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t")
    w.writerow(["id", "header", "values", "same_table_columns", "label_now", "label_b3", "reason"])
    w.writerows(out)
from collections import Counter
print(len(out), Counter(r[4] for r in out))
