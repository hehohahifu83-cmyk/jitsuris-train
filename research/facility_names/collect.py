"""施設・場所の名前の列の一覧（2026-11-01 Claude。直し H を見送り、ほかの誤りに移る（オーナー「2番」）。最初は施設の名称の決まり）。
ChatGPT の案（ai-bridge messages/20261101-1823_…）「施設の一覧は『多いほう』ではなく、列が指す実体で決める」を確かめるための材料。
教材庫（materials/pool/batch_*.jsonl、学習に使う）と使い済みの評価の陣（b066〜b123 の裁定後の正解）から、
名前の列（名称・施設名・Name・Site など）で、今のラベルが org・address・unknown の列を集める。b018 は使わない。
  python research/facility_names/collect.py → research/facility_names/columns.tsv（ChatGPT が新しい決まりの答えを書き込む欄つき）
"""
import csv, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "bench"))
HEAD = re.compile(r"(名称|施設名|場所名|箇所|設置場所|投票所|避難所|^name$|name_|_name$|site$|^site|facility|location name|venue|property name|unit name)", re.I)
NOT = re.compile(r"(法人|会社|事業者|団体名|設置者|運営|管理者|担当|部署|課名|氏名|人名|商品|品名|データ|ファイル|項目|指標|名称_英語|名称_英字|名称_カナ|フリガナ|かな|ｶﾅ|よみ)", re.I)
KEEP = {"org", "address", "unknown"}


def rows():
    for p in sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl"))):
        for i, line in enumerate(open(p, encoding="utf-8")):
            r = json.loads(line)
            yield "train", f"{os.path.basename(p)[6:-6]}#{i}", r["table"], r["header"], r["values"], r.get("context", []), r.get("label", "")
    import d1_counts
    for n in range(66, 124):
        b = f"b{n:03d}"
        if not os.path.exists(os.path.join(ROOT, "materials", "pool", "work", b, "sheets", "groups.json")):
            continue
        try:
            corpus, labels = d1_counts.batch_rows(b)
        except SystemExit:
            continue
        side = "D1" if n <= 90 else ("E1/E2" if n <= 111 else "E3")
        for i, (c, l) in enumerate(zip(corpus, labels)):
            yield side, f"{b}#{i}", c["table"], c["header"], c["values"], c.get("context", []), l["label"]


def main():
    out, seen = [], set()
    for side, cid, table, header, values, ctx, label in rows():
        h = str(header).replace("\n", " ").strip()
        if label not in KEEP or not HEAD.search(h) or NOT.search(h):
            continue
        key = (table, h)
        if key in seen:
            continue
        seen.add(key)
        out.append([side, cid, h, " | ".join(str(v)[:30] for v in values[:5]), ", ".join(str(x)[:15] for x in ctx[:8]), label, "", ""])
    with open(os.path.join(HERE, "columns.tsv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["set", "id", "header", "values", "same_table_columns", "label_now", "label_new_rule", "reason"])
        w.writerows(out)
    from collections import Counter
    print(len(out), Counter((r[0], r[5]) for r in out))


if __name__ == "__main__":
    main()
