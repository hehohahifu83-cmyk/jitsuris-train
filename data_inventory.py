"""本物のラベル付き列（materials/real_labels*.jsonl）の棚卸し。2026-10-21、Claude。

何を出すか（集計だけ。値・見出しの中身は出さない）：
  1. 種類ごとの 列数・表数・データセット数・系統数・最大の系統の割合・日本語の列数と表数
  2. 目標（specs/data_targets.json）との差：足りない所に「足りない」と印をつける
  3. 系統ごとの列数（偏りを見る）
  4. 評価セット（任意）の見出しのうち、学習に同じ見出しがある割合（独立性の確認。ラベルは読まない）

使い方：
  python data_inventory.py --out bench/data_inventory_YYYYMMDD.md
  python data_inventory.py --eval-set independent_eval/results/main/independent_main.json --out ...

用語（この表だけの決まり）：
  列        = jsonl の 1 行（出典 source と表 table と見出し header と値 values と label を持つ）
  表        = (source, table) の組
  データセット = source の文字列（例 egov_biz:cc4ea0f9-…、gittables:neonatal_mortality_tables_licensed.zip）
  系統      = source の「:」より前（egov_biz、gittables、canada、datagov_uk …）。新しい教材は spec:<ベンダー>、<公開元>:<ID> の形にして系統を分ける
  日本語の列 = 見出しか値にひらがな・カタカナ・漢字がある列
ラベルが S／unknown の行は、学習に使われないので数えない。
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

CLASSES = ["date", "amount", "quantity", "rate", "id", "org", "person", "product", "account", "tax_class", "text", "category", "email", "phone", "address", "other"]
SKIP_LABELS = (None, "", "S", "unknown")
_JA = re.compile(r"[ぁ-んァ-ン一-龥]")


def has_japanese(row):
    return bool(_JA.search(str(row.get("header", "")))) or any(_JA.search(str(v)) for v in (row.get("values") or []))


def family_of(source):
    return str(source or "").split(":", 1)[0] or "(なし)"


def load_rows(pattern="materials/real_labels*.jsonl"):
    rows = []
    for path in sorted(glob.glob(pattern)):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    return rows


def inventory(rows):
    """種類ごとの集計を返す。"""
    cols = Counter(); tabs = defaultdict(set); sets = defaultdict(set); fams = defaultdict(Counter)
    ja_cols = Counter(); ja_tabs = defaultdict(set); skipped = 0
    for r in rows:
        lab = r.get("label")
        if lab in SKIP_LABELS:
            skipped += 1
            continue
        cols[lab] += 1
        key = (r.get("source"), r.get("table"))
        tabs[lab].add(key); sets[lab].add(r.get("source")); fams[lab][family_of(r.get("source"))] += 1
        if has_japanese(r):
            ja_cols[lab] += 1; ja_tabs[lab].add(key)
    out = {}
    for c in CLASSES:
        n = cols[c]
        top_fam, top_n = (fams[c].most_common(1)[0] if fams[c] else ("-", 0))
        out[c] = {"columns": n, "tables": len(tabs[c]), "datasets": len(sets[c]), "families": len(fams[c]),
                  "top_family": top_fam, "top_family_share": (top_n / n) if n else 0.0,
                  "ja_columns": ja_cols[c], "ja_tables": len(ja_tabs[c])}
    total_fam = Counter()
    for c in CLASSES:
        total_fam.update(fams[c])
    return {"classes": out, "skipped": skipped, "families": total_fam, "total": sum(cols.values()), "total_ja": sum(ja_cols.values())}


def gaps(inv, targets):
    """目標との差。{種類: [足りない項目の文字列]}。目標は specs/data_targets.json（per_class と、種類ごとの上書き overrides）。"""
    base = dict(targets.get("per_class", {}))
    result = {}
    for c, v in inv["classes"].items():
        t = {**base, **(targets.get("overrides", {}).get(c, {}))}
        miss = []
        if v["tables"] < t.get("min_tables", 0):
            miss.append(f"表 {v['tables']}/{t['min_tables']}")
        if v["ja_tables"] < t.get("min_ja_tables", 0):
            miss.append(f"日本語の表 {v['ja_tables']}/{t['min_ja_tables']}")
        if v["datasets"] < t.get("min_datasets", 0):
            miss.append(f"データセット {v['datasets']}/{t['min_datasets']}")
        if v["columns"] and v["top_family_share"] > t.get("max_family_share", 1.0):
            miss.append(f"系統 {v['top_family']} が {v['top_family_share']:.0%}（上限 {t['max_family_share']:.0%}）")
        result[c] = miss
    return result


def header_overlap(eval_set_path, train_headers):
    """評価セットの見出し（正規化）のうち、学習にもあるものの割合。ラベルは読まない。"""
    from slice_eval import normalized_header as nh
    with open(eval_set_path, encoding="utf-8") as fh:
        doc = json.load(fh)
    cols = doc["columns"]
    hit = sum(1 for c in cols if nh(c["header"]) in train_headers)
    return len(cols), hit


def render(inv, gap=None, overlap=None):
    L = ["# 本物のラベル付き列の棚卸し（data_inventory.py）", "",
         f"対象：materials/real_labels*.jsonl のうちラベルが学習に使われる列（S／unknown を除く）{inv['total']} 列（S／unknown の行 {inv['skipped']} 行は除外）。日本語を含む列 {inv['total_ja']} 列（{inv['total_ja'] / max(1, inv['total']):.1%}）。",
         "表＝(source, table) の組、データセット＝source、系統＝source の「:」より前。水増し前の元の列の数（学習の行数ではない）。",
         "固定試験の側の表（表単位で分けた試験側）も含む。学習に入る行だけの数ではなく、『ラベル付きの本物の列の全体』の棚卸し。合成データ（gen.py）は含まない。", "",
         "## 種類別", "", "| 種類 | 列 | 表 | データセット | 系統 | 最大の系統（割合） | 日本語の列 | 日本語の表 | 目標との差 |", "|---|---:|---:|---:|---:|---|---:|---:|---|"]
    for c in CLASSES:
        v = inv["classes"][c]
        miss = "；".join(gap[c]) if gap and gap.get(c) else ("OK" if gap else "—")
        L.append(f"| {c} | {v['columns']} | {v['tables']} | {v['datasets']} | {v['families']} | {v['top_family']}（{v['top_family_share']:.0%}） | {v['ja_columns']} | {v['ja_tables']} | {miss} |")
    L += ["", "## 系統別の列数（全種類の合計）", "", "| 系統 | 列 |", "|---|---:|"]
    for fam, n in inv["families"].most_common():
        L.append(f"| {fam} | {n} |")
    if overlap:
        n, hit = overlap
        L += ["", "## 評価セットの見出しの独立性", "",
              f"評価セットの {n} 列のうち、正規化した見出しが real_labels*.jsonl のどこかにもある列は {hit} 列（{hit / max(1, n):.1%}）。残り {n - hit} 列が、この範囲では未知の見出し。",
              "合成データ（gen.py・自治体・カリキュラム）の見出しは含まない。学習に使う全行を含む正確な値は slice_eval.py の『見出しの区分』（2026-10-21 の主セットでは、学習の全行に対して 27 列＝8.6% が既知）。"]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--pattern", default="materials/real_labels*.jsonl")
    ap.add_argument("--targets", default="specs/data_targets.json")
    ap.add_argument("--eval-set", help="評価セットの JSON（見出しの重なりだけを見る）")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    rows = load_rows(a.pattern)
    if not rows:
        raise SystemExit(f"行がありません：{a.pattern}")
    inv = inventory(rows)
    gap = None
    if os.path.exists(a.targets):
        with open(a.targets, encoding="utf-8") as fh:
            gap = gaps(inv, json.load(fh))
    overlap = None
    if a.eval_set:
        from slice_eval import normalized_header as nh
        overlap = header_overlap(a.eval_set, {nh(r.get("header", "")) for r in rows})
    text = render(inv, gap, overlap)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
