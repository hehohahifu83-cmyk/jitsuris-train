"""直し J の候補（2026-11-09 Claude）：見張りの日付の値の読み取りが知らない、はっきり日付と言える書き方だけを足す。
値の形だけで数と区別できない形（4 桁の時刻 0300、0.375、月の数字だけ、1996.0、生没年 1876-1943）は足さない（Codex の日付 6 形の調べ）。

  python research/guard_dates/fix_j.py   → research/guard_dates/fix_j_eval.json（W2 の教材庫の検証で、戻る正解と新しい誤り）

使い方の決まり：見張りが date を date_value_evidence_low で止めたときだけ、値の 5 割以上が「今の決まり or 直し J」で日付に読めれば date を残す。
"""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import guard  # noqa: E402

DASHES = dict.fromkeys(map(ord, "‐‑‒–—―−"), "-")
# 2026-11-09 Codex の反例（fix_j_review_codex.md）で直した：月の名前は全部を書き出す（marketing・maybe を月に読まない）、
# 和暦・月日・時刻は数の範囲を確かめる、値だけで番号・経過時間・小数の範囲と区別できない形（15.01.18・16:35:00.00・13.30-16.30）は外す
MON_EN = (r"(?:january|february|march|april|may|june|july|august|september|october|november|december"
          r"|jan|feb|mar|apr|jun|jul|aug|sept|sep|oct|nov|dec)\.?")
MON_PT_ES_FR = (r"(?:janeiro|fevereiro|março|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro"
                r"|enero|febrero|marzo|mayo|junio|julio|septiembre|octubre|noviembre|diciembre"
                r"|janvier|janv\.|février|fevrier|févr\.|fevr\.|mars|avril|avr\.|mai|juin|juillet|juil\.|août|aout|septembre|sept\.|octobre|oct\.|novembre|nov\.|décembre|decembre|déc\.|dec\.)")
MON3 = {m: i for i, m in enumerate(("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"), 1)}
ERA_LIMIT = {"明": 45, "明治": 45, "大": 15, "大正": 15, "昭": 64, "昭和": 64, "平": 31, "平成": 31, "令": 30, "令和": 30}
ERA = r"(明治|大正|昭和|平成|令和|明|大|昭|平|令)"


def _ok_md(m, d=None):
    m = int(m)
    if not 1 <= m <= 12:
        return False
    if d is None:
        return True
    return 1 <= int(d) <= (29 if m == 2 else 30 if m in (4, 6, 9, 11) else 31)


def _ok_hm(h, mi="0", s="0"):
    return 0 <= int(h) <= 23 and 0 <= int(mi) <= 59 and 0 <= int(s) <= 59


def _era_year(era, y):
    return y == "元" or 1 <= int(y) <= ERA_LIMIT[era]


def _j_atom(v):
    m = re.fullmatch(ERA + r"\s*(元|\d{1,2})", v)                                     # 平23・令1
    if m:
        return _era_year(*m.groups())
    m = re.fullmatch(ERA + r"\s*(元|\d{1,2})\s*年\s*(?:(\d{1,2})\s*月|平均|度|末)?", v)  # 令和 7年11月・令和 5年平均
    if m:
        return _era_year(m.group(1), m.group(2)) and (m.group(3) is None or _ok_md(m.group(3)))
    m = re.fullmatch(r"(?:毎年)?(\d{1,2})月(?:(\d{1,2})日)?(?:(午前|午後)?(\d{1,2})時(?:(\d{1,2})分)?)?(?:ころ|頃|上旬|中旬|下旬|上旬頃|中旬頃|下旬頃)?", v)
    if m:                                                                              # 11月4日午前9時ころ・7月下旬・毎年1月1日
        mo, d, ampm, h, mi = m.groups()
        if not _ok_md(mo, d):
            return False
        return h is None or (int(h) <= (12 if ampm else 23) and _ok_hm(min(int(h), 23), mi or "0"))
    if re.fullmatch(r"(?:" + MON_PT_ES_FR + r"|" + MON_EN + r")\s*(?:de\s*)?(?:19|20)\d{2}", v):        # junho 2025・jan. 2013
        return True
    if re.fullmatch(MON_EN + r"\s*-\s*" + MON_EN + r"\s*(?:19|20)\d{2}", v):                        # jan-mar 2020
        return True
    m = re.fullmatch(r"(\d{1,2})/(" + MON_EN + r")/(?:19|20)\d{2}(?:\s+(\d{1,2}):(\d{2})(?::(\d{2}))?)?", v)  # 26/oct/2019 18:15
    if m:
        d, mon, h, mi, s = m.groups()
        return _ok_md(MON3[mon[:3]], d) and (h is None or _ok_hm(h, mi, s or "0"))
    m = re.fullmatch(r"(\d{2})(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d{2}:(\d{2}):(\d{2}):(\d{2})", v)  # 09nov17:11:02:00（SAS）
    if m:
        d, mon, h, mi, s = m.groups()
        return _ok_md(MON3[mon], d) and _ok_hm(h, mi, s)
    m = re.fullmatch(r"(\d{1,2}):(\d{2})\s*[-~〜～]\s*(\d{1,2}):(\d{2})", v)     # 9:30-17:00（コロンの時刻の範囲だけ）
    if m:
        h1, m1, h2, m2 = m.groups()
        return _ok_hm(h1, m1) and _ok_hm(h2, m2)
    return False


def j_value(v):
    v = unicodedata.normalize("NFKC", str(v)).strip().lower().translate(DASHES)
    v = re.sub(r"\s+", " ", v)
    if not v:
        return None
    if guard.is_date_value(v, True):   # 空白を消して読むのはやめた（「4625 8433」の Fax・「63 917 461」の金額を 8 桁の日付に読んだ）
        return True
    if " / " in v:   # 「Jan. / jan. 2013」（英仏の 2 か国語）：最後が日付で、ほかは月の名前
        parts = [p.strip() for p in v.split(" / ") if p.strip()]
        mon = re.compile(r"(?:" + MON_PT_ES_FR + r"|" + MON_EN + r")")
        return bool(parts) and _j_atom(parts[-1]) and all(mon.fullmatch(p) or _j_atom(p) for p in parts[:-1])
    return _j_atom(v)


def j_keeps_date(values):
    vals = [str(x) for x in values if str(x).strip() and str(x).strip().lower() not in ("na", "nan", "-", "?")]
    return bool(vals) and sum(bool(j_value(x)) for x in vals) / len(vals) >= 0.5


def main():
    import json
    import glob
    import collections
    sys.path.insert(0, str(ROOT / "research/w2_unknown"))
    import p0_input_diagnostic as P
    import subprocess
    pf = P.snapshot_module("pool_families")
    paths = [p for p in subprocess.check_output(["git", "ls-tree", "-r", "--name-only", P.BASE, "materials/pool"], text=True, cwd=ROOT).splitlines()
             if re.fullmatch(r"materials/pool/batch_[^/]+\.jsonl", p)]
    docs = [json.loads(line) for p in paths for line in P.blob(p).decode().splitlines()]
    junk = {"nan", "None", "", "NaN", "null", "NULL"}
    rows = [(d["header"].lstrip("﻿"), [v for v in d["values"] if v.strip() not in junk], d["label"], d["context"], d["table"]) for d in docs]
    fm = {(q["table"], q["header"].strip()): q for q in map(json.loads, P.blob("materials/pool/labelfix_v24.jsonl").decode().splitlines()) if q.get("decision") == "change"}
    rows = [(r[:2] + (fm[(r[4], r[0].strip())]["label"],) + r[3:]) if (r[4], r[0].strip()) in fm and r[2] == fm[(r[4], r[0].strip())]["from"] else r for r in rows]
    _, val = pf.split_val_by_family(rows, salt="jitsuris-poolval-v2", mod=8)
    out = collections.Counter(); cols = {"recovered": collections.Counter(), "new_error": collections.Counter()}
    for f in sorted(glob.glob(str(ROOT / "eval_reports/latest/job*_probs_val_pool_ft.json"))):
        for r in json.load(open(f))["rows"]:
            if r["raw_prediction"] != "date" or r["decision_reason"] != "date_value_evidence_low":
                continue
            h, v = val[r["index"]][0], val[r["index"]][1]
            if guard.header_date_ok(h, v) or guard.header_date_ok_g(h, v):
                out["直しG で戻る（J の前）"] += 1
                continue
            if not j_keeps_date(v):
                continue
            kind = "recovered" if r["truth"] == "date" else "new_error"
            out[kind] += 1
            cols[kind][f"{h} | {r['truth']}"] += 1
    doc = {"outputs": dict(out), "columns": {k: dict(c) for k, c in cols.items()}}
    (ROOT / "research/guard_dates/fix_j_eval.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(doc, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
