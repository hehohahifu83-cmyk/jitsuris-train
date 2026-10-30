"""LABEL_GUIDE v2.2 の決まりと違う付け方の教材の列を探す（2026-10-30 Claude）。
教材庫（materials/pool/batch_*.jsonl）と英国・業務の表の教材（materials/real_labels*.jsonl）を、列名・単位・値の語で引く。
ここでは候補を出すだけで、付け直すかは Claude が 1 列ずつ決める（research/labels/v22_decisions.jsonl）。
  python research/labels/v22_targets.py   → research/labels/v22_targets.jsonl
"""
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

ENERGY = re.compile(r"kwh|mwh|gwh|kbtu|\bgj\b|\bmj\b|energy|electricity|電力量|電力使用量|発電量|エネルギー|使用電力", re.I)
FILESIZE = re.compile(r"\b(mb|kb|gb|bytes?)\b|file ?size|ファイルサイズ|容量", re.I)
URI = re.compile(r"^https?://\S+/(id|def)/", re.I)
ORGAO = re.compile(r"órg[aã]o|orgao|entidade", re.I)
COSTC = re.compile(r"cost ?cent(re|er)|centro de custo", re.I)
DEPT = re.compile(r"department|dept\b", re.I)
NUM = re.compile(r"^[\d\s.,-]+$")


def rows():
    for p in sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl"))) + \
            sorted(glob.glob(os.path.join(ROOT, "materials", "real_labels*.jsonl"))):
        name = os.path.basename(p)
        for k, line in enumerate(open(p, encoding="utf-8")):
            r = json.loads(line)
            yield name, k, r


def rules(r):
    h, u, lab = str(r.get("header", "")), str(r.get("unit", "") or ""), r.get("label")
    vals = [str(v) for v in r.get("values", []) if str(v).strip()]
    hu = h + " " + u
    out = []
    if lab == "other" and ENERGY.search(hu):
        out.append(("B1_energy", "quantity"))
    if lab == "other" and FILESIZE.search(hu):
        out.append(("B1_filesize", "quantity"))
    if lab != "id" and vals and sum(bool(URI.match(v)) for v in vals) >= max(1, len(vals) // 2):
        out.append(("B6_uri", "id"))
    if lab != "org" and ORGAO.search(h) and not re.search(r"c[oó]digo|\bcod\b|\bid\b", h, re.I):
        out.append(("B2_orgao", "org"))
    if COSTC.search(h) and vals:
        want = "id" if all(NUM.match(v) for v in vals) else "account"
        if lab != want:
            out.append(("B2_costcentre", want))
    if DEPT.search(h) and lab in ("account", "org") and vals:
        out.append(("B2_department_check", None))   # 値が省庁なら org、中の部門なら account（1 列ずつ見る）
    if r.get("batch") == "b036" and re.fullmatch(r"zone_code", h, re.I) and lab != "category":
        out.append(("B3_zone_code", "category"))
    return out


def main():
    out = []
    for name, k, r in rows():
        for rule, want in rules(r):
            out.append({"file": name, "line": k, "rule": rule, "header": r.get("header"), "unit": r.get("unit", ""), "label": r.get("label"),
                        "want": want, "values": [str(v) for v in r.get("values", [])[:5]], "context": r.get("context", [])[:8], "table": r.get("table")})
    with open(os.path.join(HERE, "v22_targets.jsonl"), "w", encoding="utf-8") as f:
        for x in out:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    from collections import Counter
    print(Counter(x["rule"] for x in out))


if __name__ == "__main__":
    main()
