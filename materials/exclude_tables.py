"""個人別の記録を含む表を、表ごと教材から外す（2026-11-04 Claude、Codex の除外メモ sheets/answers_codex/notes.md による）。

  python materials/exclude_tables.py --batch b142
    → work/<陣>/exclude_tables.json（外す表の URL と理由。値は書かない）
    → 作業の置き場の値を消す：corpus.jsonl・set.json の values・row_values・context の値、sheets/*.md に出ていた値
      （行の番号は変えない。ラベル・予測との対応を崩さない）
  確定（pipeline.py finalize）は exclude_tables.json の表の行を教材に入れない。git の履歴には残るので、履歴から消すかはオーナーが決める。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
from pipeline import read_jsonl, work, write_jsonl  # noqa: E402

MARK = "［個人別の記録のため削除］"
URL = re.compile(r"(?:^|\s)[-*]\s*(.*?)\s+—\s+(https://\S+)")


def notes_tables(w):
    """notes.md の「- グループ: 題名 — URL」の行 → [(題名, URL)]。"""
    out = []
    for f in sorted((w / "sheets").glob("answers_*/notes.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = URL.search(line)
            if m:
                title = m.group(1).split(":", 1)[-1].strip()
                out.append((title, m.group(2).rstrip(").,")))
    return out


def excluded_rows(corpus, urls):
    return [i for i, c in enumerate(corpus) if c.get("resource_page") in urls or c.get("table") in urls]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    a = ap.parse_args(argv)
    w = work(a.batch)
    found = notes_tables(w)
    urls = {u for _, u in found}
    corpus = read_jsonl(w / "corpus.jsonl")
    rows = excluded_rows(corpus, urls)
    hit = {corpus[i].get("resource_page") for i in rows} | {corpus[i].get("table") for i in rows}
    missing = sorted(u for u in urls if u not in hit)
    secret = set()
    for i in rows:
        c = corpus[i]
        secret.update(str(v) for v in c.get("values", []) if len(str(v).strip()) >= 2)
        c["values"] = [MARK] * len(c.get("values", []))
        if "row_values" in c:
            c["row_values"] = MARK
    write_jsonl(w / "corpus.jsonl", corpus)
    sp = w / "set.json"
    if sp.exists():
        s = json.loads(sp.read_text(encoding="utf-8"))
        tables = {corpus[i]["table"] for i in rows}
        for col in s["columns"]:
            if col.get("table") in tables:
                col["values"] = [MARK] * len(col.get("values", []))
                if "row_values" in col:
                    col["row_values"] = MARK
        sp.write_text(json.dumps(s, ensure_ascii=False) + "\n", encoding="utf-8")
    for md in (w / "sheets").glob("sheet_*.md"):
        t = md.read_text(encoding="utf-8")
        for v in sorted(secret, key=len, reverse=True):
            t = t.replace(v, MARK)
        md.write_text(t, encoding="utf-8")
    doc = {"batch": a.batch, "source": "sheets/answers_codex/notes.md（Codex の除外メモ）",
           "tables": sorted({u for u in urls}), "rows": len(rows), "not_in_corpus": missing,
           "reason": "個人別の記録・個人事業主や代表者の実名・患者の属性などを含む表は、表ごと教材に入れない（先例で隠した列も）"}
    (w / "exclude_tables.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{a.batch}: 表 {len(urls)}・列 {len(rows)} を外し値を消した（corpus に無い URL {len(missing)}）")


if __name__ == "__main__":
    main()
