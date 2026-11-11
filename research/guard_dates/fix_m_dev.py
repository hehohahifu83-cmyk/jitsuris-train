"""直し M の候補（再確認の手がかりの語を足す）の作るときの測り（2026-11-12 Claude。採否には使わない。fix_j.py と同じ教材庫の検証の行を使う）。
  python research/guard_dates/fix_m_dev.py [words]  → 標準出力（今の再確認 対 語を足した再確認：正しい・不明・重大）
"""
import ast, collections, glob, json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "research/w2_unknown"))
import guard, recheck as R  # noqa
import p0_input_diagnostic as P  # noqa

NUM = R.NUMERIC
def val_rows():
    pf = P.snapshot_module("pool_families")
    paths = [p for p in subprocess.check_output(["git", "ls-tree", "-r", "--name-only", P.BASE, "materials/pool"], text=True, cwd=ROOT).splitlines()
             if re.fullmatch(r"materials/pool/batch_[^/]+\.jsonl", p)]
    docs = [json.loads(line) for p in paths for line in P.blob(p).decode().splitlines()]
    junk = {"nan", "None", "", "NaN", "null", "NULL"}
    rows = [(d["header"].lstrip("﻿"), [v for v in d["values"] if v.strip() not in junk], d["label"], d["context"], d["table"], d.get("unit", "") or "") for d in docs]
    fm = {(q["table"], q["header"].strip()): q for q in map(json.loads, P.blob("materials/pool/labelfix_v24.jsonl").decode().splitlines()) if q.get("decision") == "change"}
    rows = [(r[:2] + (fm[(r[4], r[0].strip())]["label"],) + r[3:]) if (r[4], r[0].strip()) in fm and r[2] == fm[(r[4], r[0].strip())]["from"] else r for r in rows]
    _, val = pf.split_val_by_family([r[:5] for r in rows], salt="jitsuris-poolval-v2", mod=8)
    return val

def run(val, files, patch=None):
    orig = R.cue_types
    if patch:
        R.cue_types = lambda h, u="": orig(h, u) | patch(h, u)
    c = collections.Counter(); changed = []
    try:
        for f in files:
            for r in json.load(open(f))["rows"]:
                h, v, truth, ctx = val[int(r["index"])][:4]
                top3 = ast.literal_eval(r["top3"]) if isinstance(r["top3"], str) else r["top3"]
                g = r["guarded_prediction"]
                lab, _ = R.decide(g, top3, v[:20], h, "", 0.95, True, guard.header_date_ok, list(ctx))
                o = "unk" if lab == "unknown" else ("ok" if lab == truth else ("crit" if lab in NUM and truth in NUM else "wrong"))
                c[o] += 1
                changed.append((f, r["index"], lab, truth, h))
    finally:
        R.cue_types = orig
    return c, changed

if __name__ == "__main__":
    val = val_rows()
    files = sorted(glob.glob(str(ROOT / "eval_reports/latest/job*_probs_val_pool_ft.json")))
    from fix_m import extra_cues  # noqa
    a, ca = run(val, files)
    b, cb = run(val, files, extra_cues)
    print("今", dict(a)); print("直し M", dict(b))
    diff = collections.Counter()
    for x, y in zip(ca, cb):
        if x[2] != y[2]:
            diff[(x[2], y[2], x[3])] += 1
    for k, n in diff.most_common(30): print(n, "前", k[0], "→", k[1], "正解", k[2])
