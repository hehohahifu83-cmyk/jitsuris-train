"""封印セット #2 のラベル用シートを作り、答えを読む（2026-10-25 Claude）。予測ファイルは読まない。

  make  <set.json> <出力の dir>   表ごとに列を並べたシート sheet_NNN.md と、答えの雛形を作る（1 列 1 行）
  read  <set.json> <答えの dir> <出力.json>   answers/sheet_NNN.tsv（列 ID TAB ラベル）→ {列 ID: ラベル}。全部の列がそろっているか確かめる
シートと答えは非公開の ai-bridge/labels/sealed2/ に置く（公開リポジトリに答えを置かない）。
"""
import json
import sys
from collections import OrderedDict
from pathlib import Path

LABELS = "account address amount category date email id org other person phone product quantity rate tax_class text unknown S".split()
PER_SHEET = 70


def cut(s, n=60):
    s = str(s).replace("\n", " ").replace("|", "｜")
    return s if len(s) <= n else s[:n] + "…"


def make(set_path, out):
    cols = json.load(open(set_path, encoding="utf-8"))["columns"]
    tables = OrderedDict()
    for c in cols:
        tables.setdefault(c["table"], []).append(c)
    sheets, cur = [], []
    for t, cs in tables.items():   # 表を途中で切らない
        if cur and sum(len(x) for x in cur) + len(cs) > PER_SHEET:
            sheets.append(cur); cur = []
        cur.append(cs)
    if cur:
        sheets.append(cur)
    out = Path(out); (out / "answers_template").mkdir(parents=True, exist_ok=True)
    for k, sh in enumerate(sheets, 1):
        lines = [f"# 封印セット #2 ラベル用シート {k:03d} / {len(sheets):03d}", "",
                 "- LABEL_GUIDE v1.9 だけで決める。**予測は見ない・相手のラベルは見ない**。決められない列は unknown、表が崩れている・値が空の列は S",
                 "- 使えるラベル：" + " ".join(LABELS),
                 f"- 答え：`answers_template/sheet_{k:03d}.tsv` を自分の答えの置き場に写し、各行の TAB の後ろにラベルを 1 つ書く", ""]
        tsv = []
        for cs in sh:
            c0 = cs[0]
            lines += [f"## 表 {c0['table']}（{c0['language']}・{len(cs)} 列）", f"- 同じ表の列：{cut(', '.join([c0['header']] + c0['siblings']), 400)}"]
            if c0.get("unit"):
                lines.append(f"- 単位列の値：{cut(c0['unit'], 120)}")
            for c in cs:
                lines.append(f"- **{c['id']}** 見出し：{cut(c['header'])} ／ 値：{' | '.join(cut(v, 40) for v in c['values'])}")
                tsv.append(f"{c['id']}\t")
            lines.append("")
        (out / f"sheet_{k:03d}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        (out / "answers_template" / f"sheet_{k:03d}.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    print(f"{len(cols)} columns, {len(tables)} tables, {len(sheets)} sheets")


def read(set_path, answers, out):
    ids = [c["id"] for c in json.load(open(set_path, encoding="utf-8"))["columns"]]
    got = {}
    for f in sorted(Path(answers).glob("sheet_*.tsv")):
        for n, line in enumerate(open(f, encoding="utf-8"), 1):
            if not line.strip():
                continue
            cid, _, lab = line.rstrip("\n").partition("\t")
            lab = lab.strip()
            if lab not in LABELS:
                raise SystemExit(f"{f.name}:{n} ラベルが知らない値：{lab!r}")
            if cid in got:
                raise SystemExit(f"{f.name}:{n} 列が重なっている：{cid}")
            got[cid] = lab
    missing = [i for i in ids if i not in got]
    extra = [i for i in got if i not in set(ids)]
    if missing or extra:
        raise SystemExit(f"足りない列 {len(missing)}（{missing[:5]}）・余分な列 {len(extra)}")
    Path(out).write_text(json.dumps({i: got[i] for i in ids}, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print(f"{len(ids)} labels → {out}")


if __name__ == "__main__":
    {"make": lambda: make(sys.argv[2], sys.argv[3]), "read": lambda: read(sys.argv[2], sys.argv[3], sys.argv[4])}[sys.argv[1]]()
