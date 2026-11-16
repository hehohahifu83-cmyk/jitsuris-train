"""教材庫の表で、同じ表の列が同じ行（row_index）の値（row_values）を持つかを数える（2026-11-16 Claude。読むだけ。方法 T の前提の確かめ）。
  python research/table_reading/row_alignment.py → research/table_reading/row_alignment.json
数えるもの：表の数、全列の row_index が同じ表、row_values の長さが row_index と合う表、同じ行番号の重複、揃わない表の id と理由。
入力のファイルの SHA-256 も残す（同じ教材庫で再現するため）。
"""
import glob
import hashlib
import json
import os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl")))
    T = defaultdict(list)
    sha = {}
    for f in files:
        b = open(f, "rb").read()
        sha[os.path.relpath(f, ROOT)] = hashlib.sha256(b).hexdigest()
        for line in b.decode("utf-8").splitlines():
            if line.strip():
                d = json.loads(line)
                T[d["table"]].append(d)
    c, bad, ncols = Counter(), [], Counter()
    for t, cs in sorted(T.items()):
        ncols[len(cs)] += 1
        ri = [tuple(x.get("row_index") or ()) for x in cs]
        why = []
        if any(not r for r in ri):
            why.append("row_index が空の列がある")
        if len(set(ri)) != 1:
            why.append("列ごとに row_index が違う")
        if any(len(x.get("row_values") or []) != len(x.get("row_index") or []) for x in cs):
            why.append("row_values と row_index の長さが違う")
        if ri and len(set(ri[0])) != len(ri[0]):
            why.append("同じ行番号の重複")
        if len({x["header"] for x in cs}) != len(cs):
            why.append("同じ列名が 2 つ以上")
        c["揃う" if not why else "揃わない"] += 1
        if why:
            bad.append({"table": t, "columns": len(cs), "why": why})
    out = {"tables": len(T), "columns": sum(len(v) for v in T.values()), "count": dict(c),
           "columns_per_table": {str(k): v for k, v in sorted(ncols.items())}, "not_aligned": bad, "inputs_sha256": sha}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "row_alignment.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "inputs_sha256"}, ensure_ascii=False)[:1500])


if __name__ == "__main__":
    main()
