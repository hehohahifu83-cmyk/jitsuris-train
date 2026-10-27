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
  python materials/model_corpora/silver.py check    # 大きいまとまりの中が 1 種類かを、抜き取った列ごとに確かめるシート（c3 計画の段 1 の 3）
  python materials/model_corpora/silver.py silver   # ChatGPT の答え（確かめの裁定を反映）と C2 の予測が一致した「まとまり×値の形」を銀にする
"""
import argparse
import gzip
import json
import random
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
NO_HEADER = "（見出しなし）"   # SOTAB の列には見出しがない。予測の道具は空の見出しを受け付けないので、決まった語を入れる
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
             "- **Wikidata の型の読み方**：`wikibase-entityid` は「ほかの項目へのつながり」で、**値は名前**（首都なら都市の名前、議会なら組織の名前）。**番号（id）という意味ではない**ので、値で決める。`string` は文字列（コード・ファイル名・URL も入る）、`quantity` は数、`time` は日付、`globecoordinate` は座標、`monolingualtext` はある言語の文字",
             "- SOTAB の元の種類は Schema.org の名前（`postalCode`＝郵便番号、`price`＝価格、`Date`＝日付、`addressLocality`＝市町村 など）。値と元の種類で LABEL_GUIDE の種類に読み替える",
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
            cols.append({"id": cid, "table": r["table"], "source": r["corpus"], "language": "en", "header": r["header"] or NO_HEADER,
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


CHECK_GROUPS = 60       # 列の多い順に、ChatGPT の答えが unknown・S でないまとまりをこの数だけ
CHECK_PER_GROUP = 5     # まとまりごとに抜き取る列（なるべく別の表から）
CHECK_SEED = 20261028


def cmd_check(_a):
    """大きいまとまりから列を抜き取り、まとまりの名前・答えを伏せて並べたシートを作る。誤りが 5% を超えるまとまりは銀にしない。"""
    meta = json.loads((OUT / "groups.json").read_text(encoding="utf-8"))
    got, problems = LS.read_answers(OUT, meta["groups"], "chatgpt")
    if problems or len(got) != len(meta["groups"]):
        raise SystemExit("ChatGPT の答えがそろっていない")
    pick = [g for g in sorted(meta["groups"], key=lambda g: -g["columns"]) if got[g["group"]] not in ("unknown", "S")][:CHECK_GROUPS]
    want = {g["key"]: g["group"] for g in pick}
    rng = random.Random(CHECK_SEED)
    seen, res = defaultdict(int), defaultdict(list)
    for r in read_rows():          # 表ごとに 1 列までの貯め置き抜き取り（同じ表の列が並ばないように）
        gid = want.get(map_key(r))
        if not gid or not r["values"]:
            continue
        seen[gid] += 1
        bucket = res[gid]
        if len(bucket) < CHECK_PER_GROUP * 4:
            bucket.append(r)
        else:
            j = rng.randrange(seen[gid])
            if j < len(bucket):
                bucket[j] = r
    items = []
    for gid in want.values():
        tables, chosen = set(), []
        for r in sorted(res[gid], key=lambda r: rng.random()):
            if r["table"] not in tables:
                tables.add(r["table"])
                chosen.append(r)
            if len(chosen) == CHECK_PER_GROUP:
                break
        items += [(gid, r) for r in chosen]
    rng.shuffle(items)
    d = OUT / "check"
    d.mkdir(exist_ok=True)
    (OUT / "answers_check").mkdir(exist_ok=True)
    (OUT / "answers_check" / ".keep").write_text("", encoding="utf-8")
    index, sheets = [], defaultdict(list)
    for i, (gid, r) in enumerate(items, 1):
        cid = f"c{i:04d}"
        index.append({"id": cid, "group": gid, "table": r["table"]})
        sheets[(i - 1) // SHEET_SIZE + 1].append((cid, r))
    total = len(sheets)
    for no, rows in sheets.items():
        lines = [f"# 銀ラベルの確かめ {no:03d} / {total:03d}（1 列ずつ）", "",
                 "- **1 列ずつ**、LABEL_GUIDE.md v2.0 のどの種類かを答える。まとまりの名前・前の答えは伏せてある。前のシートの自分の答えは見ないで、その列だけで決める",
                 "- 読み方は銀ラベルのシート（`sheets/sheet_001.md` の冒頭）と同じ。決められない → `unknown`、人の名前・連絡先・崩れた値 → `S`",
                 f"- 使えるラベル：{' '.join(LS.ALL_LABELS)}",
                 f"- 答え：末尾の雛形を `answers_check/check_{no:03d}.tsv` に写して埋める", ""]
        for cid, r in rows:
            if r["corpus"] == "sotab_v2":
                head = f"見出しなし（SOTAB、元の種類 `{r['source_label']}`）"
            else:
                head = f"見出し「{LS.cut(r['header'], 60)}」（WikiDBs、Wikidata の型 `{r['source_label']}`）"
            vals = " | ".join(LS.cut(v, 40) for v in r["values"][:8])
            extra = []
            if r.get("table_title"):
                extra.append(f"表：{LS.cut(r['table_title'], 40)}")
            if r.get("context"):
                extra.append("同じ表の列：" + ", ".join(LS.cut(c, 20) for c in r["context"][:6]))
            lines += [f"## {cid} — {head}", f"- 値：{vals}"] + ([f"- {'／'.join(extra)}"] if extra else []) + [""]
        lines += ["## 答えの雛形", "", "```"] + [f"{cid}\t" for cid, _ in rows] + ["```", ""]
        (d / f"check_{no:03d}.md").write_text("\n".join(lines), encoding="utf-8")
    (OUT / "check_index.json").write_text(json.dumps({"created_by": "materials/model_corpora/silver.py check", "seed": CHECK_SEED,
                                                     "groups": [g["group"] for g in pick], "columns": index},
                                                    ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    cov = sum(g["columns"] for g in pick)
    print(f"まとまり {len(pick)}（{cov:,} 列を覆う）・抜き取り {len(items)} 列・シート {total} 枚")


PRED = REP_SET.parent / "pred_c2_seed1.json"


def cmd_silver(_a):
    """2026-10-28 オーナー判断で Grok 抜き：ChatGPT の答え × C2 の予測（guard 後）の一致だけを銀にする。列そのものは書かず、規則（まとまり×値の形）を書く。"""
    meta = json.loads((OUT / "groups.json").read_text(encoding="utf-8"))
    got, problems = LS.read_answers(OUT, meta["groups"], "chatgpt")
    if problems or len(got) != len(meta["groups"]):
        raise SystemExit("ChatGPT の答えがそろっていない")
    dec = json.loads((OUT / "check_decisions.json").read_text(encoding="utf-8"))
    for gid, v in dec["relabel"].items():
        if got[gid] != v["from"]:
            raise SystemExit(f"{gid}：裁定の from と答えが違う")
        got[gid] = v["to"]
    pred = json.loads(PRED.read_text(encoding="utf-8"))
    want_sha = __import__("hashlib").sha256(REP_SET.read_bytes()).hexdigest()
    if pred["set_sha256"] != want_sha:
        raise SystemExit("予測の set と今の set が違う")
    by_id = {r["id"]: r for r in pred["rows"]}
    key_of = {g["group"]: g["key"] for g in meta["groups"]}
    rules, why = [], Counter()
    for rep in json.loads((OUT / "reps.json").read_text(encoding="utf-8")):
        gid, n, lab = rep["group"], rep["columns"], got[rep["group"]]
        p = by_id[rep["id"]]["guarded_prediction"]
        if gid in dec["exclude"]:
            why["確かめで外した"] += n
        elif lab in ("unknown", "S"):
            why["ChatGPT が unknown・S"] += n
        elif p == lab:
            rules.append({"group": gid, "key": key_of[gid], "shape": rep["shape"], "label": lab, "columns": n})
            why["銀"] += n
        else:
            why["C2 が不明" if p == "unknown" else "C2 と割れた"] += n
    by_label = Counter()
    for r in rules:
        by_label[r["label"]] += r["columns"]
    doc = {"created_by": "materials/model_corpora/silver.py silver", "teachers": "ChatGPT（answers/）× C2 種子 1（guard 後）",
           "pred_sha256": __import__("hashlib").sha256(PRED.read_bytes()).hexdigest(), "set_sha256": want_sha,
           "check_decisions": "check_decisions.json", "columns": dict(why), "by_label": dict(by_label.most_common()), "rules": rules}
    (OUT / "silver_rules.json").write_text(json.dumps(doc, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    total = sum(why.values())
    print(f"銀 {why['銀']:,} / {total:,} 列（{why['銀'] / total:.1%}）・規則 {len(rules):,}：{dict(why)}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sheets")
    sub.add_parser("reps")
    sub.add_parser("check")
    sub.add_parser("silver")
    p = sub.add_parser("status")
    p.add_argument("--teacher", choices=sorted(LS.TEACHERS), default="chatgpt")
    a = ap.parse_args(argv)
    return {"sheets": cmd_sheets, "reps": cmd_reps, "status": cmd_status, "check": cmd_check, "silver": cmd_silver}[a.cmd](a) or 0


if __name__ == "__main__":
    raise SystemExit(main())
