"""教材庫のラベル付けを軽くする「ラベル用シート」（2026-10-24 Claude）。

ChatGPT が大きな corpus.jsonl を読まずに済むように、陣の列を
「見出しと値の形が同じもの」でまとめ、小さな Markdown のシートに分ける。
ChatGPT は 1 グループ 1 行「g0001<TAB>ラベル」だけを答えのファイルに書く。
番号がはっきりしているので行のずれは起きず、途中で止まってもシート単位で続きから再開できる。

使い方（Claude が実行する）：
  python materials/label_sheets.py make   --batch b006 [--size 120]   # work/b006/sheets/ に groups.json・sheet_001.md … を作る
  python materials/label_sheets.py status --batch b006                # どのシートの答えが済んだか
  python materials/label_sheets.py merge  --batch b006                # 答え → labels_chatgpt.jsonl（足りない・誤りがあれば止まる）

ChatGPT の答えのファイル：work/b006/sheets/answers/sheet_001.tsv（シートの末尾の「答えの雛形」を写して埋める）
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
from pipeline import LABELS, NOT_USED, read_jsonl, work, write_jsonl  # noqa: E402

ALL_LABELS = tuple(LABELS) + tuple(NOT_USED)
SHEET_SIZE = 120
ANSWER_RE = re.compile(r"^(g\d{4,})\t([A-Za-z_]+)\s*$")


def norm(s) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(s or ""))).strip()


def shape(v) -> str:
    """値の形：数字は 9、ラテン文字は a、そのほかはそのまま（先頭 12 文字）。"""
    t = norm(v)
    t = re.sub(r"[0-9]", "9", t)
    t = re.sub(r"[A-Za-z]", "a", t)
    return re.sub(r"9+", "9", re.sub(r"a+", "a", t))[:12]


def group_key(row) -> str:
    vals = [v for v in row.get("values", []) if norm(v)]
    shapes = sorted({shape(v) for v in vals}) if vals else ["(空)"]
    return json.dumps([norm(row.get("header")).casefold(), norm(row.get("unit")), shapes], ensure_ascii=False)


def make_groups(corpus):
    """見出し・単位・値の形が同じ列を 1 グループに。グループの番号は corpus で最初に出た順。"""
    order, members = [], {}
    for i, row in enumerate(corpus):
        k = group_key(row)
        if k not in members:
            members[k] = []
            order.append(k)
        members[k].append(i)
    return [{"group": f"g{n + 1:04d}", "rows": members[k]} for n, k in enumerate(order)]


def cut(s, n):
    s = norm(s)
    return s if len(s) <= n else s[: n - 1] + "…"


def render_sheet(no, groups, corpus, total_sheets, guide_version):
    out = [f"# ラベル用シート {no:03d} / {total_sheets:03d}", "",
           f"- LABEL_GUIDE {guide_version} だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S",
           f"- 使えるラベル：{' '.join(ALL_LABELS)}",
           "- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める",
           f"- 答え：末尾の「答えの雛形」を `answers/sheet_{no:03d}.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く", ""]
    for g in groups:
        rows = g["rows"]
        out.append(f"## {g['group']}（{len(rows)} 列）")
        first = corpus[rows[0]]
        out.append(f"- 見出し：{cut(first.get('header'), 80)}" + (f"（単位：{cut(first.get('unit'), 20)}）" if norm(first.get("unit")) else ""))
        for n, i in enumerate(rows[:2]):
            r = corpus[i]
            vals = " | ".join(cut(v, 40) for v in r.get("values", [])[:5]) or "（空）"
            ctx = ", ".join(cut(c, 20) for c in r.get("context", [])[:8])
            out.append(f"- 例{n + 1} 値：{vals}")
            out.append(f"  - 同じ表の列：{ctx or '（なし）'}")
        out.append("")
    out += ["## 答えの雛形", "", "```"] + [f"{g['group']}\t" for g in groups] + ["```", ""]
    return "\n".join(out)


def cmd_make(a):
    w = work(a.batch)
    corpus = read_jsonl(w / "corpus.jsonl")
    groups = make_groups(corpus)
    d = w / "sheets"
    if d.exists() and any(d.glob("answers/*.tsv")):
        raise SystemExit(f"{d}/answers に答えがもうある。作り直すと番号がずれるので止める")
    (d / "answers").mkdir(parents=True, exist_ok=True)
    for old in d.glob("sheet_*.md"):
        old.unlink()
    sheets = [groups[i:i + a.size] for i in range(0, len(groups), a.size)]
    guide = re.search(r"v\d+(?:\.\d+)?", (ROOT / "LABEL_GUIDE.md").read_text(encoding="utf-8").splitlines()[0])
    for n, gs in enumerate(sheets, 1):
        for g in gs:
            g["sheet"] = n
        (d / f"sheet_{n:03d}.md").write_text(render_sheet(n, gs, corpus, len(sheets), guide.group(0) if guide else ""), encoding="utf-8")
    (d / "groups.json").write_text(json.dumps({"batch": a.batch, "rows": len(corpus), "groups": groups}, ensure_ascii=False) + "\n", encoding="utf-8")
    (d / "answers" / ".keep").write_text("", encoding="utf-8")
    print(f"{a.batch}: {len(corpus)} 列 → {len(groups)} グループ、シート {len(sheets)} 枚（{d}）")


# 先生ごとの答えの置き場と、まとめたラベルのファイル（2026-10-28 Claude。Grok を 2 人目の先生に足した）。
# 2 人は相手の答えの置き場を見ない（独立に付ける）
TEACHERS = {"chatgpt": ("answers", "labels_chatgpt.jsonl", "ChatGPT"), "grok": ("answers_grok", "labels_grok.jsonl", "Grok"),
            "claude": ("answers_claude", "labels_claude.jsonl", "Claude")}


def read_answers(d, groups, teacher="chatgpt"):
    """答えのファイルを読む → (グループ→ラベル, 問題のリスト)。"""
    sheet_of = {g["group"]: g["sheet"] for g in groups}
    got, problems = {}, []
    for f in sorted((d / TEACHERS[teacher][0]).glob("sheet_*.tsv")):
        m = re.fullmatch(r"sheet_(\d{3})\.tsv", f.name)
        if not m:
            problems.append(f"{f.name}：ファイル名は sheet_NNN.tsv")
            continue
        no = int(m.group(1))
        for ln, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip("﻿").rstrip()
            if not line or line.startswith("#") or line.startswith("```"):
                continue
            am = ANSWER_RE.match(line)
            if not am:
                if re.match(r"^g\d{4,}\t?$", line):
                    continue   # まだ埋めていない行
                problems.append(f"{f.name} {ln} 行目：形が「g0001<TAB>ラベル」ではない：{line[:40]}")
                continue
            gid, lab = am.groups()
            if gid not in sheet_of:
                problems.append(f"{f.name} {ln} 行目：知らないグループ {gid}")
            elif sheet_of[gid] != no:
                problems.append(f"{f.name} {ln} 行目：{gid} はシート {sheet_of[gid]:03d} のグループ")
            elif lab not in ALL_LABELS:
                problems.append(f"{f.name} {ln} 行目：{gid} のラベル {lab} は決まりにない")
            elif gid in got and got[gid] != lab:
                problems.append(f"{f.name} {ln} 行目：{gid} に違うラベルが 2 つ（{got[gid]}・{lab}）")
            else:
                got[gid] = lab
    return got, problems


def load(a):
    w = work(a.batch)
    d = w / "sheets"
    meta = json.loads((d / "groups.json").read_text(encoding="utf-8"))
    return w, d, meta


def cmd_status(a):
    _, d, meta = load(a)
    got, problems = read_answers(d, meta["groups"], a.teacher)
    per = Counter(g["sheet"] for g in meta["groups"])
    done = Counter(g["sheet"] for g in meta["groups"] if g["group"] in got)
    full = [s for s in sorted(per) if done[s] == per[s]]
    part = [s for s in sorted(per) if 0 < done[s] < per[s]]
    rows_done = sum(len(g["rows"]) for g in meta["groups"] if g["group"] in got)
    print(f"{a.batch}（{TEACHERS[a.teacher][2]}）: グループ {len(got)}/{len(meta['groups'])}、列 {rows_done}/{meta['rows']}、"
          f"済んだシート {len(full)}/{len(per)}" + (f"、途中 {', '.join(f'{s:03d}' for s in part)}" if part else ""))
    for p in problems:
        print("問題：" + p)
    return 0 if not problems else 1


def merge(corpus, groups, got, teacher_name="ChatGPT"):
    missing = [g["group"] for g in groups if g["group"] not in got]
    if missing:
        raise ValueError(f"答えの無いグループ {len(missing)} 件（最初：{', '.join(missing[:5])}）")
    labels = [None] * len(corpus)
    for g in groups:
        for i in g["rows"]:
            if labels[i] is not None:
                raise ValueError(f"{i} 行目が 2 つのグループに入っている")
            labels[i] = {"table": corpus[i]["table"], "header": corpus[i]["header"], "label": got[g["group"]],
                         "teacher": teacher_name, "group": g["group"]}
    if any(x is None for x in labels):
        raise ValueError("どのグループにも入っていない行がある")
    return labels


def cmd_merge(a):
    w, d, meta = load(a)
    corpus = read_jsonl(w / "corpus.jsonl")
    if len(corpus) != meta["rows"]:
        raise SystemExit(f"corpus の行数 {len(corpus)} がシートを作ったとき（{meta['rows']}）と違う。シートを作り直す")
    got, problems = read_answers(d, meta["groups"], a.teacher)
    if problems:
        raise SystemExit("答えに問題がある：\n" + "\n".join(problems))
    try:
        labels = merge(corpus, meta["groups"], got, TEACHERS[a.teacher][2])
    except ValueError as exc:
        raise SystemExit(f"まだまとめられない：{exc}（`status` で確かめる）")
    out = w / TEACHERS[a.teacher][1]
    if out.exists() and not a.force:
        raise SystemExit(f"{out} がもうある（上書きするなら --force）")
    write_jsonl(out, labels)
    print(f"{a.batch}: {len(labels)} 列のラベルを {out} に書いた（グループ {len(got)}）。{dict(Counter(x['label'] for x in labels))}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("make"); p.add_argument("--batch", required=True); p.add_argument("--size", type=int, default=SHEET_SIZE)
    p = sub.add_parser("status"); p.add_argument("--batch", required=True); p.add_argument("--teacher", choices=sorted(TEACHERS), default="chatgpt")
    p = sub.add_parser("merge"); p.add_argument("--batch", required=True); p.add_argument("--force", action="store_true")
    p.add_argument("--teacher", choices=sorted(TEACHERS), default="chatgpt")
    a = ap.parse_args(argv)
    return {"make": cmd_make, "status": cmd_status, "merge": cmd_merge}[a.cmd](a) or 0


if __name__ == "__main__":
    raise SystemExit(main())
