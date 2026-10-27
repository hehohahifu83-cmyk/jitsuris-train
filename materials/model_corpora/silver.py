"""外の学習データ（SOTAB V2・WikiDBs）に、まとまり単位で 16 種のラベルを付け直す道具（銀ラベル。2026-10-28 Claude）。

オーナー許可（2026-10-27「進め方については許可する」）。費用のかかる API は使わない。
1. sheets：読み替えのまとまり（SOTAB は元の種類、WikiDBs は「型＋見出し」）ごとに、例の列を並べたシートを作る。
   ChatGPT は `answers/`、Grok は `answers_grok/` に、相手の答えを見ずに 16 種（決められなければ unknown、使えなければ S）で答える。
2. reps：読み替えのまとまりを値の形でさらに分け、各まとまりの代表の列を 1 つずつ選んで、C2 の予測に渡す set を作る（無料・CPU）。
3. 2 人の答えが一致したまとまり（割れたものは Claude が裁定）と、C2 の予測が一致した値の形のまとまりの列だけを銀ラベルにする（silver 命令。後で足す）。
銀ラベルは教材庫（batch_*.jsonl）には入れない。学習に使うかどうかは事前記録とオーナーの許可のあとで決める（research/c3-plan-2026-10-28.md）。

  python materials/model_corpora/silver.py sheets
  python materials/model_corpora/silver.py reps
  python materials/model_corpora/silver.py status [--teacher grok]
"""
import argparse
import gzip
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import label_sheets as LS  # noqa: E402

DATA = HERE / "data"
OUT = HERE / "silver"
CORPORA = ("sotab_v2", "wikidbs10k")
MIN_COLUMNS = 5        # WikiDBs の「型＋見出し」で、列がこれより少ないまとまりはシートに出さない（使わない）
SHEET_SIZE = 150
EXAMPLES = 3
REP_SET = HERE.parent / "pool" / "work" / "silver1" / "set.json"   # label-assist-predict.yml が読める場所


def read_rows():
    for corpus in CORPORA:
        for f in sorted((DATA / corpus).glob("part-*.jsonl.gz")):
            with gzip.open(f, "rt", encoding="utf-8") as fh:
                for line in fh:
                    yield json.loads(line)


def map_key(r):
    if r["corpus"] == "sotab_v2":
        return json.dumps(["sotab_v2", r["source_label"]], ensure_ascii=False)
    return json.dumps([r["corpus"], r["source_label"], LS.norm(r["header"]).casefold()], ensure_ascii=False)


def shape_key(r):
    return Counter(LS.shape(v) for v in r["values"]).most_common(1)[0][0] if r["values"] else "(空)"


def collect():
    """読み替えのまとまり → 列の数・例（別の表から）・値の形ごとの代表。"""
    groups = {}
    for r in read_rows():
        k = map_key(r)
        g = groups.setdefault(k, {"key": k, "corpus": r["corpus"], "n": 0, "examples": [], "tables": set(), "shapes": {}})
        g["n"] += 1
        if len(g["examples"]) < EXAMPLES and r["table"] not in g["tables"]:
            g["tables"].add(r["table"])
            g["examples"].append({k2: r.get(k2) for k2 in ("header", "values", "context", "table_title", "dbpedia_label", "table")})
        s = shape_key(r)
        if s not in g["shapes"]:
            g["shapes"][s] = {"n": 0, "rep": r}
        g["shapes"][s]["n"] += 1
    for g in groups.values():
        g.pop("tables")
    return groups


def kept(groups):
    out = [g for g in groups.values() if g["corpus"] == "sotab_v2" or g["n"] >= MIN_COLUMNS]
    return sorted(out, key=lambda g: (-g["n"], g["key"]))


def render(no, total, gs):
    lines = [f"# 銀ラベルのシート {no:03d} / {total:03d}（外の学習データの読み替え）", "",
             "- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列",
             "- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`",
             "- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前",
             f"- 使えるラベル：{' '.join(LS.ALL_LABELS)}",
             f"- 答え：末尾の雛形を、ChatGPT は `answers/sheet_{no:03d}.tsv`、Grok は `answers_grok/sheet_{no:03d}.tsv` に写して埋める。**相手の答えは見ない**", ""]
    for g in gs:
        key = json.loads(g["key"])
        title = f"元の種類 `{key[1]}`" if g["corpus"] == "sotab_v2" else f"見出し「{LS.cut(key[2], 60)}」（Wikidata の型 `{key[1]}`）"
        lines.append(f"## {g['group']} — {g['corpus']}：{title}（{g['n']:,} 列）")
        for n, ex in enumerate(g["examples"], 1):
            vals = " | ".join(LS.cut(v, 40) for v in (ex["values"] or [])[:5]) or "（空）"
            extra = []
            if ex.get("dbpedia_label"):
                extra.append(f"DBpedia：{ex['dbpedia_label'].rsplit('/', 1)[-1]}")
            if ex.get("table_title"):
                extra.append(f"表：{LS.cut(ex['table_title'], 40)}")
            if ex.get("context"):
                extra.append("同じ表の列：" + ", ".join(LS.cut(c, 20) for c in ex["context"][:6]))
            lines.append(f"- 例{n}：{vals}" + (f"（{'／'.join(extra)}）" if extra else ""))
        lines.append("")
    lines += ["## 答えの雛形", "", "```"] + [f"{g['group']}\t" for g in gs] + ["```", ""]
    return "\n".join(lines)


def cmd_sheets(_a):
    if any(OUT.glob("answers*/*.tsv")):
        raise SystemExit(f"{OUT} に答えがもうある。作り直すと番号がずれるので止める")
    allg = collect()
    gs = kept(allg)
    for i, g in enumerate(gs, 1):
        g["group"] = f"g{i:04d}"
        g["sheet"] = (i - 1) // SHEET_SIZE + 1
    total = (len(gs) + SHEET_SIZE - 1) // SHEET_SIZE
    (OUT / "sheets").mkdir(parents=True, exist_ok=True)
    for d in ("answers", "answers_grok"):
        (OUT / d).mkdir(exist_ok=True)
        (OUT / d / ".keep").write_text("", encoding="utf-8")
    by_sheet = defaultdict(list)
    for g in gs:
        by_sheet[g["sheet"]].append(g)
    for no, items in by_sheet.items():
        (OUT / "sheets" / f"sheet_{no:03d}.md").write_text(render(no, total, items), encoding="utf-8")
    meta = {"created_by": "materials/model_corpora/silver.py sheets", "label_guide": "v2.0", "min_columns": MIN_COLUMNS,
            "groups": [{"group": g["group"], "sheet": g["sheet"], "key": g["key"], "corpus": g["corpus"], "columns": g["n"],
                        "shapes": {s: v["n"] for s, v in g["shapes"].items()}} for g in gs]}
    (OUT / "groups.json").write_text(json.dumps(meta, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    covered = sum(g["n"] for g in gs)
    allc = sum(g["n"] for g in allg.values())
    print(f"まとまり {len(gs)}・シート {total} 枚・列 {covered:,} / {allc:,}")


def cmd_reps(_a):
    meta = json.loads((OUT / "groups.json").read_text(encoding="utf-8"))
    wanted = {g["key"]: g["group"] for g in meta["groups"]}
    groups = collect()
    cols, index = [], []
    for key, gid in wanted.items():
        for s, v in sorted(groups[key]["shapes"].items(), key=lambda x: -x[1]["n"]):
            r = v["rep"]
            cid = f"s1-{len(cols) + 1:06d}"
            cols.append({"id": cid, "table": r["table"], "source": r["corpus"], "language": "en", "header": r["header"],
                         "values": r["values"][:5] or [""], "siblings": r.get("context") or [], "unit": ""})
            index.append({"id": cid, "group": gid, "shape": s, "columns": v["n"]})
    REP_SET.parent.mkdir(parents=True, exist_ok=True)
    REP_SET.write_text(json.dumps({"schema_version": 1, "set_id": "label-assist-silver1", "columns": cols}, ensure_ascii=False, indent=0) + "\n",
                       encoding="utf-8")
    (OUT / "reps.json").write_text(json.dumps(index, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print(f"代表 {len(cols):,} 列 → {REP_SET}")


def cmd_status(a):
    meta = json.loads((OUT / "groups.json").read_text(encoding="utf-8"))
    got, problems = LS.read_answers(OUT, meta["groups"], a.teacher)
    per = Counter(g["sheet"] for g in meta["groups"])
    done = Counter(g["sheet"] for g in meta["groups"] if g["group"] in got)
    print(f"銀（{LS.TEACHERS[a.teacher][2]}）：まとまり {len(got)}/{len(meta['groups'])}、済んだシート {sum(done[s] == per[s] for s in per)}/{len(per)}")
    for p in problems:
        print("問題：" + p)
    return 1 if problems else 0


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sheets")
    sub.add_parser("reps")
    p = sub.add_parser("status")
    p.add_argument("--teacher", choices=sorted(LS.TEACHERS), default="chatgpt")
    a = ap.parse_args(argv)
    return {"sheets": cmd_sheets, "reps": cmd_reps, "status": cmd_status}[a.cmd](a) or 0


if __name__ == "__main__":
    raise SystemExit(main())
