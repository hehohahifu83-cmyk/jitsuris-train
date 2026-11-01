"""E3（b112〜b123）の 2 人のラベルの裁定（2026-11-01 Claude。直し H の事前記録 bench/hfix_prereg_20261101.md の正解）。
食い違い 146 グループのうち、Claude の答えと違う決定だけを OVERRIDE に書く（ほかは Claude の答えのまま）。決め方は LABEL_GUIDE v2.3。
Claude の答えは、先に固定した SHA-256（claude_answers_sha256.json）と一致することを確かめてから使う。
  python research/labels/e3_20261101/adjudicate.py → 各陣 sheets/answers_final/sheet_NNN.tsv・decisions.jsonl
"""
import collections, hashlib, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
G = "G"   # ChatGPT の答えを採る
READABLE = "崩れているのはこの表の 1 列だけ（ほかの列は読める。b103 と同じ）"
OVERRIDE = {  # (陣, シート, グループ): (最終, 理由)
    **{("b114", "001", f"g{i:04d}"): (G, READABLE) for i in (16, 17, 18, 19, 20, 21)},
    ("b114", "001", "g0025"): (G, "燃料の品目は product（b095・b108 と同じ）"),
    ("b114", "001", "g0031"): (G, "値が N/A ばかり（空の列）"),
    ("b114", "001", "g0060"): (G, "事件記録の数（見出しの題名で何の数か分かる）"), ("b114", "001", "g0061"): (G, "同上"),
    ("b114", "002", "g0154"): (G, "行ごとに違う説明の文（B4）"), ("b114", "002", "g0155"): (G, "同上"),
    ("b115", "001", "g0028"): ("quantity", "同じ表の排出量の列（Units の列つき、B1 の量）。g0032 と同じ"),
    **{("b115", "001", f"g{i:04d}"): (G, READABLE) for i in (51, 52, 53, 54, 55)},
    **{("b115", "001", f"g{i:04d}"): (G, "予算の表ではない事業の体系の一覧（B7 の科目ではない）") for i in (65, 66, 67)},
    ("b115", "002", "g0132"): (G, "列名がコードの州の略号は区域のコード（B3、GEO_CANT と同じ）"),
    **{("b118", "001", f"g{i:04d}"): (G, "語を並べた件名が行ごとに違う（キーワードの羅列は text）") for i in (2, 3, 4, 5)},
    **{("b119", "001", f"g{i:04d}"): (G, "施設の一覧の名称で、場所（キャンプ場・足湯・展望所）が多い（v1.7）") for i in (49, 50, 51)},
    **{("b119", "001", f"g{i:04d}"): (G, "施設の一覧の名称で、歴史館・資料館・センターが多い（v1.7）") for i in (103, 104, 105)},
    ("b119", "001", "g0120"): (G, "施設の一覧の名称で、学校・センターが多い（v1.7）"), ("b119", "002", "g0121"): (G, "同上（名称_カナ）"),
    ("b119", "002", "g0126"): (G, "センター・美術館・図書館が多い（v1.7）"),
    ("b119", "003", "g0251"): (G, "消防署・センター・公民館が多い（v1.7）"),
    ("b120", "001", "g0023"): (G, "行ごとに違う協定の内容の文（B4）"), ("b120", "001", "g0029"): (G, "同上"),
    ("b121", "001", "g0006"): (G, "庭園だけの一覧（場所。文化財の種類は混ざらない）"),
    ("b121", "001", "g0008"): (G, "作った時期の元号（暦の時点の粗い形）"),
    ("b121", "001", "g0012"): (G, "道路の一覧（起点・終点つき）の道路名は場所"), ("b121", "001", "g0013"): (G, "同上（よみがな）"),
}
DICT_META = set()

def read(p):
    return dict(l.rstrip("\n").split("\t")[:2] for l in open(p, encoding="utf-8") if l.startswith("g"))


def main():
    doc = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude_answers_sha256.json"), encoding="utf-8"))
    for k, sha in doc["files"].items():
        p = os.path.join(ROOT, "materials", "pool", "work", k[:4], "sheets", "answers_claude", "sheet_" + k.split("_")[-1])
        if hashlib.sha256(open(p, "rb").read()).hexdigest() != sha:
            raise SystemExit(f"{p} が固定した SHA と違う")
    dec, stat = [], collections.Counter()
    for k in doc["files"]:
        b, n = k[:4], k.split("_")[-1][:3]
        w = os.path.join(ROOT, "materials", "pool", "work", b, "sheets")
        c, g = read(f"{w}/answers_claude/sheet_{n}.tsv"), read(f"{w}/answers/sheet_{n}.tsv")
        final = {}
        for gid in c:
            cv, gv = c[gid].strip(), g[gid].strip()
            if cv == gv:
                final[gid] = cv; stat["一致"] += 1; continue
            key = (b, n, gid)
            if key in DICT_META:
                f, r = "unknown", "生データの辞書の表の列"
            elif key in OVERRIDE:
                f, r = OVERRIDE[key]; f = gv if f == G else f
            else:
                f, r = cv, "Claude の答え（LABEL_GUIDE に合う）"
            final[gid] = f
            stat["Claude" if f == cv else ("ChatGPT" if f == gv else "別の種類")] += 1
            dec.append({"batch": b, "sheet": n, "group": gid, "claude": cv, "chatgpt": gv, "final": f, "reason": r})
        os.makedirs(f"{w}/answers_final", exist_ok=True)
        with open(f"{w}/answers_final/sheet_{n}.tsv", "w", encoding="utf-8") as fh:
            fh.write("".join(f"{gid}\t{final[gid]}\n" for gid in c))
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "decisions.jsonl"), "w", encoding="utf-8") as fh:
        for d in dec:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    print(dict(stat), len(dec))


if __name__ == "__main__":
    main()
