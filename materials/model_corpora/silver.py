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
  python materials/model_corpora/silver.py silver   # 銀 A：ChatGPT の答え（確かめの裁定を反映）× C2 の予測の一致／銀 B：Claude の裁定（silver_b_decisions.json）
  python materials/model_corpora/silver.py train --tier A   # 学習用の銀（C3b の 1 段目）：規則に合う列を、種類ごと・規則ごとの上限で抜き出す（2026-10-29）
  python materials/model_corpora/silver.py check2           # 学習用の銀（train_A）の検査シート：種類ごとに 60 列、銀のラベルを伏せて ChatGPT が 1 列ずつ答える（2026-10-29）
  python materials/model_corpora/silver.py check2-result    # ChatGPT の答えと銀のラベルの突き合わせ（Claude の裁定の下書き）
  python materials/model_corpora/silver.py clean            # 裁定（check2_decisions.json）で外す規則・種類を train_A から抜き、train_Aclean.jsonl.gz を作る
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


def b_keeps(dec, shape, pred):
    """Claude の裁定（silver_b_decisions.json の 1 まとまり）で、この値の形を使うか。"""
    if dec.get("mode") == "c2_agree" and pred != dec["label"]:
        return False
    if pred in dec.get("drop_c2", []):
        return False
    digits = dec.get("shape_digits")
    if digits == "none" and "9" in shape or digits == "some" and "9" not in shape:
        return False
    return True


def cmd_silver(_a):
    """2026-10-28 オーナー判断で Grok 抜き。銀 A：ChatGPT の答え（確かめの裁定を反映）× C2 の予測（guard 後）の一致。
    銀 B：外れた列の多いまとまりを Claude が裁定したもの（silver_b_decisions.json。独立の 2 票ではないので A と分ける）。
    列そのものは書かず、規則（まとまり×値の形）を書く。"""
    meta = json.loads((OUT / "groups.json").read_text(encoding="utf-8"))
    got, problems = LS.read_answers(OUT, meta["groups"], "chatgpt")
    if problems or len(got) != len(meta["groups"]):
        raise SystemExit("ChatGPT の答えがそろっていない")
    dec = json.loads((OUT / "check_decisions.json").read_text(encoding="utf-8"))
    for gid, v in dec["relabel"].items():
        if got[gid] != v["from"]:
            raise SystemExit(f"{gid}：裁定の from と答えが違う")
        got[gid] = v["to"]
    bdec = json.loads((OUT / "silver_b_decisions.json").read_text(encoding="utf-8"))
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
        b = bdec["labels"].get(gid)
        rule = {"group": gid, "key": key_of[gid], "shape": rep["shape"], "columns": n}
        if b:
            if not b_keeps(b, rep["shape"], p):
                why["Claude の裁定で外した値の形"] += n
            elif p == b["label"] == lab and gid not in dec["exclude"]:
                rules.append({**rule, "label": lab, "tier": "A"})
                why["銀 A"] += n
            else:
                rules.append({**rule, "label": b["label"], "tier": "B"})
                why["銀 B"] += n
        elif gid in dec["exclude"]:
            why["確かめで外した"] += n
        elif lab in ("unknown", "S"):
            why["ChatGPT が unknown・S"] += n
        elif p == lab:
            rules.append({**rule, "label": lab, "tier": "A"})
            why["銀 A"] += n
        else:
            why["C2 が不明" if p == "unknown" else "C2 と割れた"] += n
    by_label = {t: Counter() for t in ("A", "B")}
    for r in rules:
        by_label[r["tier"]][r["label"]] += r["columns"]
    doc = {"created_by": "materials/model_corpora/silver.py silver", "teachers": "A：ChatGPT（answers/）× C2 種子 1（guard 後）／B：Claude の裁定（silver_b_decisions.json）",
           "pred_sha256": __import__("hashlib").sha256(PRED.read_bytes()).hexdigest(), "set_sha256": want_sha,
           "check_decisions": "check_decisions.json", "b_decisions": "silver_b_decisions.json", "columns": dict(why),
           "by_label": {t: dict(c.most_common()) for t, c in by_label.items()}, "rules": rules}
    (OUT / "silver_rules.json").write_text(json.dumps(doc, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    total = sum(why.values())
    ab = why["銀 A"] + why["銀 B"]
    print(f"銀 {ab:,} / {total:,} 列（{ab / total:.1%}。A {why['銀 A']:,}・B {why['銀 B']:,}）・規則 {len(rules):,}：{dict(why)}")


TRAIN_SALT = "jitsuris-silver-train-v1"


def cmd_train(a):
    """C3b の 1 段目（銀で学ぶ）の教材（2026-10-29 Claude。オーナー許可 2026-10-28「許可する」、事前記録 bench/c3_prereg_20261029.md の次の回）。
    silver_rules.json の規則（まとまり×値の形）に合う列を、規則ごとに per_rule 列・種類ごとに per_label 列までに抜き出す。
    銀 A は id が 41% と偏るので、種類ごとの上限で均す。person は教材庫と同じく使わない。どの列を取るかは列の中身と salt の SHA-256 だけで決める。
    出力：silver/train_<tier>.jsonl.gz（1 行＝1 列。header・values・label・context・table・title・rule）"""
    import hashlib
    doc = json.loads((OUT / "silver_rules.json").read_text(encoding="utf-8"))
    tiers = set(a.tier.split("+"))
    rules = {(r["key"], r["shape"]): r for r in doc["rules"] if r["tier"] in tiers and r["label"] != "person"}
    # 1 回目：規則ごとの列の数 → 取る数（規則ごとの上限 → 種類ごとの上限で縮める）
    n = Counter()
    for r in read_rows():
        k = (map_key(r), shape_key(r))
        if k in rules:
            n[k] += 1
    want = {k: min(c, a.per_rule) for k, c in n.items()}
    by_label = Counter()
    for k, w in want.items():
        by_label[rules[k]["label"]] += w
    for k in want:
        tot = by_label[rules[k]["label"]]
        if tot > a.per_label:
            want[k] = want[k] * a.per_label / tot
    # 2 回目：規則の中で、ハッシュの小さい順に近い形で取る（取る割合＝want/n）
    out, got = [], Counter()
    for r in read_rows():
        k = (map_key(r), shape_key(r))
        if k not in rules:
            continue
        h = int(hashlib.sha256(f"{TRAIN_SALT}|{r['corpus']}|{r['table']}|{r['col']}".encode()).hexdigest()[:12], 16) / 16 ** 12
        if h >= want[k] / n[k]:
            continue
        lab = rules[k]["label"]
        got[lab] += 1
        out.append({"header": r["header"] or NO_HEADER, "values": r["values"], "label": lab, "context": r.get("context") or [],
                    "table": f"{r['corpus']}:{r['table']}", "title": r.get("table_title") or "", "rule": rules[k]["group"]})
    path = OUT / f"train_{a.tier.replace('+', '')}.jsonl.gz"
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for d in out:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print(f"{path.name}: {len(out):,} 列・規則 {len(n):,}（per_rule {a.per_rule}・per_label {a.per_label}）：{dict(got.most_common())}")


CHECK2_PER_LABEL = 60
CHECK2_SEED = 20261029


def cmd_check2(_a):
    """学習に使う銀（train_A.jsonl.gz）を検査する（2026-10-29 Claude。オーナー「後で行う銀の学習についてはチャットGPTと協力して邪魔になる要素を検査排除してくれ」）。
    種類ごとに 60 列（規則ごと 1 列・表ごと 1 列まで）を抜き出し、銀のラベル・規則・表の名前を伏せてシートに並べる。対応表は check2_index.json（ChatGPT は答え終わるまで見ない）。"""
    with gzip.open(OUT / "train_A.jsonl.gz", "rt", encoding="utf-8") as f:
        rows = [json.loads(l) for l in f if l.strip()]
    rng = random.Random(CHECK2_SEED)
    rng.shuffle(rows)
    by_label = defaultdict(list)
    used_rules, used_tables = set(), set()
    for r in rows:
        if len(by_label[r["label"]]) >= CHECK2_PER_LABEL or r["rule"] in used_rules or r["table"] in used_tables or not r["values"]:
            continue
        by_label[r["label"]].append(r)
        used_rules.add(r["rule"]); used_tables.add(r["table"])
    # 規則の少ない種類（date・amount など）は 60 列に届かないので、同じ規則の別の表の列で埋める（規則ごと 5 列まで）
    per_rule = Counter(r["rule"] for rs in by_label.values() for r in rs)
    for r in rows:
        if len(by_label[r["label"]]) >= CHECK2_PER_LABEL or per_rule[r["rule"]] >= 5 or r["table"] in used_tables or not r["values"]:
            continue
        by_label[r["label"]].append(r)
        per_rule[r["rule"]] += 1; used_tables.add(r["table"])
    items = [r for rs in by_label.values() for r in rs]
    rng.shuffle(items)
    d = OUT / "check2"
    d.mkdir(exist_ok=True)
    (OUT / "answers_check2").mkdir(exist_ok=True)
    (OUT / "answers_check2" / ".keep").write_text("", encoding="utf-8")
    index, sheets = [], defaultdict(list)
    for i, r in enumerate(items, 1):
        cid = f"k{i:04d}"
        index.append({"id": cid, "label": r["label"], "rule": r["rule"], "table": r["table"], "header": r["header"]})
        sheets[(i - 1) // SHEET_SIZE + 1].append((cid, r))
    total = len(sheets)
    for no, rs in sheets.items():
        lines = [f"# 学習用の銀の検査 {no:03d} / {total:03d}（1 列ずつ）", "",
                 "- **1 列ずつ**、LABEL_GUIDE.md（v2.1）のどの種類かを答える。銀のラベル・まとまりの名前・前のシートの答えは見ないで、その列だけで決める",
                 "- 外の学習データ（SOTAB V2 の Web の表・WikiDBs の Wikidata の表）の列。見出しの無い列は「（見出しなし）」",
                 "- 決められない → `unknown`、人の名前・連絡先・崩れた値 → `S`。迷ったら理由を notes.md に 1 行（列の番号つき）",
                 f"- 使えるラベル：{' '.join(LS.ALL_LABELS)}",
                 f"- 答え：末尾の雛形を `answers_check2/check_{no:03d}.tsv` に写して埋める（1 行＝「k0001<TAB>ラベル」）", ""]
        for cid, r in rs:
            vals = " | ".join(LS.cut(v, 40) for v in r["values"][:8])
            extra = []
            if r.get("title"):
                extra.append(f"表：{LS.cut(r['title'], 40)}")
            if r.get("context"):
                extra.append("同じ表の列：" + ", ".join(LS.cut(c, 20) for c in r["context"][:6]))
            lines += [f"## {cid} — 見出し「{LS.cut(r['header'], 60)}」", f"- 値：{vals}"] + ([f"- {'／'.join(extra)}"] if extra else []) + [""]
        lines += ["## 答えの雛形", "", "```"] + [f"{cid}\t" for cid, _ in rs] + ["```", ""]
        (d / f"check_{no:03d}.md").write_text("\n".join(lines), encoding="utf-8")
    (OUT / "check2_index.json").write_text(json.dumps({"note": "ChatGPT は答え終わるまで見ない", "items": index}, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print(f"check2：{len(items)} 列・{total} 枚：{dict(Counter(r['label'] for r in items))}")


def cmd_check2_result(_a):
    """ChatGPT の 1 列ずつの答え（answers_check2/）と銀のラベルを突き合わせる。種類ごとの一致率と、食い違った列の一覧（Claude が裁定する）を出す。"""
    index = json.loads((OUT / "check2_index.json").read_text(encoding="utf-8"))["items"]
    got = {}
    for f in sorted((OUT / "answers_check2").glob("check_*.tsv")):
        for line in f.read_text(encoding="utf-8").splitlines():
            parts = line.strip().split("\t")
            if len(parts) >= 2 and parts[0].startswith("k"):
                got[parts[0]] = parts[1].strip()
    missing = [x["id"] for x in index if x["id"] not in got]
    if missing:
        raise SystemExit(f"答えが無い列：{missing[:10]}（{len(missing)}）")
    bad = [x for x in index if got[x["id"]] not in LS.ALL_LABELS]
    if bad:
        raise SystemExit(f"決まりにないラベル：{[(x['id'], got[x['id']]) for x in bad[:10]]}")
    per, diff = defaultdict(Counter), []
    for x in index:
        a = got[x["id"]]
        per[x["label"]]["n"] += 1
        per[x["label"]]["agree" if a == x["label"] else "diff"] += 1
        if a != x["label"]:
            diff.append({**x, "chatgpt": a})
    out = {"per_label": {k: dict(v) for k, v in sorted(per.items())}, "diff": diff}
    (OUT / "check2_result.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in sorted(per.items()):
        print(f"{k}: 一致 {v['agree']}/{v['n']}")
    print(f"食い違い {len(diff)} 列 → check2_result.json（Claude が裁定）")


def cmd_clean(_a):
    """check2 の裁定（check2_decisions.json）で、誤りの規則（まとまり）と誤りの多い種類・金額・件数を学習用の銀から外す（2026-10-29 Claude）。"""
    dec = json.loads((OUT / "check2_decisions.json").read_text(encoding="utf-8"))
    groups, labels = set(dec["exclude_groups"]), set(dec["drop_labels"])
    kept, why = [], Counter()
    with gzip.open(OUT / "train_A.jsonl.gz", "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            if d["label"] in labels:
                why["外す種類"] += 1
            elif d["rule"] in groups:
                why["誤りの規則"] += 1
            else:
                kept.append(d)
    path = OUT / "train_Aclean.jsonl.gz"
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for d in kept:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print(f"{path.name}: {len(kept):,} 列（外した {dict(why)}）：{dict(Counter(d['label'] for d in kept).most_common())}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sheets")
    sub.add_parser("reps")
    sub.add_parser("check")
    sub.add_parser("silver")
    sub.add_parser("check2")
    sub.add_parser("check2-result")
    sub.add_parser("clean")
    p = sub.add_parser("train")
    p.add_argument("--tier", default="A", choices=["A", "B", "A+B"])
    p.add_argument("--per-rule", type=int, default=60)
    p.add_argument("--per-label", type=int, default=4000)
    p = sub.add_parser("status")
    p.add_argument("--teacher", choices=sorted(LS.TEACHERS), default="chatgpt")
    a = ap.parse_args(argv)
    return {"sheets": cmd_sheets, "reps": cmd_reps, "status": cmd_status, "check": cmd_check, "silver": cmd_silver, "train": cmd_train, "check2": cmd_check2,
            "check2-result": cmd_check2_result, "clean": cmd_clean}[a.cmd](a) or 0


if __name__ == "__main__":
    raise SystemExit(main())
