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
MON_EN = r"(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?"
MON_PT_ES_FR = (r"(?:janeiro|fevereiro|março|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro"
                r"|enero|febrero|marzo|mayo|junio|julio|septiembre|octubre|noviembre|diciembre"
                r"|janv?\.?|févr?\.?|fevr?\.?|mars|avr\.?|mai|juin|juil\.?|août|aout|sept?\.?|oct\.?|nov\.?|déc\.?|dec\.?)")
ERA = r"(?:明|大|昭|平|令|明治|大正|昭和|平成|令和)"
J_RES = [re.compile(p, re.I) for p in (
    ERA + r"\s*(?:元|\d{1,2})$",                                                   # 平23・令1・大5
    ERA + r"\s*(?:元|\d{1,2})\s*年\s*(?:\d{1,2}\s*月|平均|度|末)?$",                # 令和 7年11月・令和 5年平均
    r"(?:毎年)?\d{1,2}月(?:\d{1,2}日)?(?:午前|午後)?(?:\d{1,2}時)?(?:\d{1,2}分)?(?:ころ|頃|上旬|中旬|下旬|上旬頃|中旬頃|下旬頃)?$",  # 11月4日午前9時ころ・7月下旬・毎年1月1日
    r"(?:" + MON_PT_ES_FR + r"|" + MON_EN + r")\s*(?:de\s*)?(?:19|20)\d{2}$",      # junho 2025・jan. 2013
    MON_EN + r"\s*-\s*" + MON_EN + r"\s*(?:19|20)\d{2}$",                          # jan-mar 2020
    r"\d{1,2}/" + MON_EN + r"/(?:19|20)\d{2}(?:\s+\d{1,2}:\d{2}(?::\d{2})?)?$",     # 26/oct/2019 18:15
    r"\d{2}(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d{2}:\d{2}:\d{2}:\d{2}$",  # 09nov17:11:02:00（SAS）
    r"(?:[01]?\d|2[0-3]):[0-5]\d:[0-5]\d\.\d{1,3}$",                                # 16:35:00.00
    r"(?:[01]?\d|2[0-3])[:.][0-5]\d\s*[-~〜～]\s*(?:[01]?\d|2[0-3])[:.][0-5]\d$",   # 9:30-17:00・13.30-16.30
    r"(?:0?[1-9]|[12]\d|3[01])\.(?:0?[1-9]|1[0-2])\.\d{2}$",                       # 15.01.18
)]


def j_value(v):
    v = unicodedata.normalize("NFKC", str(v)).strip().lower().translate(DASHES)
    v = re.sub(r"\s+", " ", v)
    if not v:
        return None
    if guard.is_date_value(v, True):   # 空白を消して読むのはやめた（「4625 8433」の Fax・「63 917 461」の金額を 8 桁の日付に読んだ）
        return True
    if " / " in v:   # 「Jan. / jan. 2013」（英仏の 2 か国語）
        parts = [p.strip() for p in v.split(" / ") if p.strip()]
        mon = re.compile(r"(?:" + MON_PT_ES_FR + r"|" + MON_EN + r")$")
        return bool(parts) and bool(j_value(parts[-1])) and all(mon.match(p) or j_value(p) for p in parts[:-1])
    return any(r.match(v) for r in J_RES)


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
