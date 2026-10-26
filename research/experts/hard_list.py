"""苦手克服モデル（H）の教材の一覧を作る（2026-10-26 Claude。オーナー指示「ミスや不明となった項目と似た教材のみを重点的に学習させたモデル」）。

教材庫 b001〜b014 の採点できる列から：
1. 苦手の列：本体が間違えた・不明になった列。本体（C2）は教材庫を学んだので自分の苦手が見えない → 教材庫を学んでいない版 31 の見張り後の答え（pred_e5base_seed1）で見つける
2. 似た教材（迷い）：苦手の列と同じ取り違えの組（正解, 間違えた答え）を、2 位として確率 0.1 以上で迷った列
3. 似た教材（列名）：苦手の列と同じ列名の列（1 つの列名につき 10 列まで。「名称」などで偏らないように）
出力：materials/pool/hard_list.jsonl（table・header・reason）。学習は encoder_exp の FT_POOL_HARD_LIST（この一覧の列を FT_POOL_HARD_LIST_COPIES 回ぶん重ねる）
b015 以降（線を決める陣・確かめる陣）は使わない
使い方：python research/experts/hard_list.py
"""
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import pool_bench as B  # noqa: E402
import verifier_eval as E  # noqa: E402

BATCHES = tuple(f"b{n:03d}" for n in range(1, 15))
P2, PER_HEADER = 0.1, 10


def nh(h):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(h))).strip().casefold()


def main():
    cols = [c for b in BATCHES for c in E.load_batch(b)]
    sc = [c for c in cols if c["truth"] and c["truth"] not in B.NOT_USED and c["truth"] != "person"]
    hard = [c for c in sc if c["pred"] != c["truth"] and not (c["truth"] == "other" and c["pred"] == "unknown")]
    ids = {c["id"] for c in hard}
    pairs = {(c["truth"], c["pred"]) for c in hard if c["pred"] != "unknown"} | \
            {(c["truth"], t["label"]) for c in hard if c["pred"] == "unknown" for t in (c["top3"] or [])[:2] if t["label"] != c["truth"]}
    out = [(c, "hard_wrong" if c["pred"] != "unknown" else "hard_unknown") for c in hard]
    near = [c for c in sc if c["id"] not in ids and len(c["top3"] or []) > 1 and (c["truth"], c["top3"][1]["label"]) in pairs
            and c["top3"][1]["probability"] >= P2]
    out += [(c, "similar_confusion") for c in near]
    ids |= {c["id"] for c in near}
    hh = {nh(c["header"]) for c in hard}
    per = defaultdict(int)
    for c in sc:
        h = nh(c["header"])
        if c["id"] in ids or h not in hh or per[h] >= PER_HEADER:
            continue
        per[h] += 1
        out.append((c, "similar_header"))
    with open(os.path.join(ROOT, "materials", "pool", "hard_list.jsonl"), "w", encoding="utf-8") as f:
        for c, why in out:
            f.write(json.dumps({"table": c["table"], "header": c["header"], "batch": c["batch"], "truth": c["truth"], "reason": why}, ensure_ascii=False) + "\n")
    print(len(out), Counter(w for _, w in out))


if __name__ == "__main__":
    main()
