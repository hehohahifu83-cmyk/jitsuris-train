"""D1 の新しい陣（b066〜）の採点できる列を、言語・公開元ごとに数える（2026-10-31 Claude）。

ChatGPT の答え（sheets/answers/。無い陣は Claude の answers_claude/）を label_sheets と同じ読み方で列に戻し、S・unknown を除いた列を数える。
Claude の裁定の前なので、最後の数ではない（裁定で S・unknown になる列が減らす）。

言語は表ごと（`bench/d1_eval_queue.md` の count_table の決まり）：
  表の列名・値に日本語の文字があれば ja、ドイツ語・フランス語の語（一覧の語・ウムラウトやアクセントのある語・-ung などで終わる長い語）が 3 種類以上なら defr、ほかは en。

  python bench/d1_counts.py [--from 66] [--to 81] [--out bench/d1_counts_<日付>.md]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "materials"))
import label_sheets  # noqa: E402
from pipeline import NOT_USED, read_jsonl, work  # noqa: E402

MIN = {"all": 2500, "en": 1000, "ja": 500, "defr": 500}
SHARE = 0.30
JA_RE = re.compile(r"[぀-ヿ一-鿿]")
WORD_RE = re.compile(r"[a-zäöüßàâçéèêëîïôûùœ]+")
DIACRITIC = re.compile(r"[äöüßàâçéèêëîïôûùœ]")
# 英語にない、ドイツ語・フランス語でよく出る語（機能語・表の列名の語）
DEFR = set("""
der die das und mit von für fur ist nicht im zum zur des dem den ein eine einer eines auf aus bei nach über uber unter
jahr jahre monat tag anzahl gemeinde kanton bezirk stadt gesamt wert einheit datum nummer strasse bevölkerung betrag
zeit temperatur druck feuchte stockwerk raum gebaude gebäude ort objekt zufahrt messort frage antwort altersgruppe
altersklasse sprachregion bezeichnung beschreibung kategorie typ art anteil kosten preis fläche flaeche menge stand
geschlecht alter staat land quartier wohnviertel name vorname
le la les et du une est pour avec sur dans par au aux nombre année annee commune région valeur
montant rue ville ou sans entre selon nom adresse lieu prix taux mois jour sexe âge age catégorie libellé libelle
""".split()) - {"name", "land", "art", "age", "typ"}
GERMAN_END = re.compile(r"(ung|ungen|keit|heit|schaft|zahl|zeit|jahr|nummer|stelle|gebiet|bereich|kreis)$")


def defr_words(words):
    return {w for w in words if w in DEFR or DIACRITIC.search(w) or (len(w) > 6 and GERMAN_END.search(w))}


def table_lang(rows):
    text = " ".join([r["header"] for r in rows] + [str(v) for r in rows for v in r.get("values", [])])
    text = re.sub(r"([a-zäöü])([A-ZÄÖÜ])", r"\1 \2", text)
    if JA_RE.search(text):
        return "ja"
    words = set(WORD_RE.findall(text.lower()))
    return "defr" if len(defr_words(words)) >= 3 else "en"


def batch_rows(batch):
    w = work(batch)
    corpus = read_jsonl(w / "corpus.jsonl")
    d = w / "sheets"
    meta = label_sheets.json.loads((d / "groups.json").read_text(encoding="utf-8"))
    # b084 から先はオーナー指示（2026-10-31「あと200列はお前がやってくれ」）で Claude が付ける（answers_claude/）
    teacher = "chatgpt" if any((d / "answers").glob("sheet_*.tsv")) else "claude"
    got, problems = label_sheets.read_answers(d, meta["groups"], teacher)
    if problems:
        raise SystemExit(f"{batch}: 答えに問題がある：{problems[:3]}")
    labels = label_sheets.merge(corpus, meta["groups"], got)
    return corpus, labels


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="lo", type=int, default=66)
    ap.add_argument("--to", dest="hi", type=int, default=81)
    ap.add_argument("--out")
    a = ap.parse_args(argv)

    per_batch, lang, pub, excl = [], Counter(), Counter(), Counter()
    for n in range(a.lo, a.hi + 1):
        b = f"b{n:03d}"
        if not (work(b) / "corpus.jsonl").exists():
            continue   # 採用 0 の陣（b082）
        corpus, labels = batch_rows(b)
        tables = defaultdict(list)
        for r, l in zip(corpus, labels):
            tables[r["table"]].append((r, l["label"]))
        bl = Counter()
        for t, items in tables.items():
            lg = table_lang([r for r, _ in items])
            for r, lab in items:
                if lab in NOT_USED:
                    excl[lab] += 1
                    continue
                bl[lg] += 1
                lang[lg] += 1
                pub[r.get("publisher") or r.get("source", "?")] += 1
        per_batch.append((b, len(corpus), sum(bl.values()), bl))

    total = sum(lang.values())
    out = [f"# D1 の新しい陣の採点できる列（b{a.lo:03d}〜b{a.hi:03d}、ChatGPT の初回ラベル、Claude の裁定前）", "",
           "`python bench/d1_counts.py` で作った。言語は表ごと（日本語の文字 → ja、独仏の語 3 種類以上 → defr、ほか en）。", "",
           "| 陣 | 列 | 採点できる | en | ja | defr |", "|---|---:|---:|---:|---:|---:|"]
    for b, raw, sc, bl in per_batch:
        out.append(f"| {b} | {raw} | {sc} | {bl['en']} | {bl['ja']} | {bl['defr']} |")
    raw_all = sum(x[1] for x in per_batch)
    out.append(f"| 計 | {raw_all} | {total} | {lang['en']} | {lang['ja']} | {lang['defr']} |")
    out += ["", f"除いた列：S {excl['S']}・unknown {excl['unknown']}", "", "| 最低 | 要る | 今 | 足りない |", "|---|---:|---:|---:|"]
    have = {"all": total, **lang}
    for k, need in MIN.items():
        out.append(f"| {k} | {need} | {have.get(k, 0)} | {max(0, need - have.get(k, 0))} |")
    top = pub.most_common(5)
    out += ["", f"公開元の数 {len(pub)}。多い順（上限は全体の {SHARE:.0%} = {int(total * SHARE)} 列）：", ""]
    out += [f"- {p}：{c}（{c / total:.1%}）" for p, c in top]
    text = "\n".join(out) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
