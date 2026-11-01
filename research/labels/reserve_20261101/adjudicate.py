"""在庫 20 陣の 2 人のラベルの裁定（2026-11-01 Claude）。食い違い 372 グループのうち、Claude の答えと違う決定だけを OVERRIDE に書く（ほかは Claude の答えのまま）。
決め方は LABEL_GUIDE v2.3。決めにくいものは unknown。理由は reason の短い語。
  python research/labels/reserve_20261101/adjudicate.py → 各陣 sheets/answers_final/sheet_NNN.tsv・decisions.jsonl・summary
"""
import collections, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
G = "G"   # ChatGPT の答えを採る
OVERRIDE = {  # (陣, シート, グループ): (最終, 理由)
    ("b091", "001", "g0002"): (G, "暦年の列は date（Claude の付け間違い）"),
    **{("b091", "001", f"g{i:04d}"): ("S", "年度の見出しで値に単位の行（£millions）が混ざる表（v1.9）") for i in (10,)},
    ("b092", "001", "g0023"): ("S", "同じ表の他の列が崩れている（手順 D）"),
    ("b094", "001", "g0032"): (G, "品種は作物の種類の区分"), ("b094", "001", "g0036"): (G, "品種は作物の種類の区分"),
    ("b094", "001", "g0090"): (G, "表の名前は個々の表を指す"),
    ("b094", "002", "g0137"): (G, "大半が決まった文の繰り返し（B4）"),
    ("b094", "002", "g0144"): ("unknown", "役職名だけで人か組織か決められない"),
    **{("b094", "002", f"g{i:04d}"): (G, "年と年代が混ざるグラフの軸の値") for i in (147, 148, 149, 150)},
    ("b095", "001", "g0029"): (G, "燃料の品目は product"), ("b095", "001", "g0086"): (G, "表の名前は個々の表を指す"),
    ("b098", "001", "g0020"): (G, "割合か台数か決められない"),
    **{("b100", "001", f"g{i:04d}"): (G, "出典の機関の略号は org") for i in (18, 24, 27)},
    ("b100", "001", "g0034"): (G, "開始の時点"), ("b100", "001", "g0093"): (G, "最小が最大より大きい行があり意味が決まらない"),
    ("b100", "001", "g0094"): (G, "同上"),
    ("b102", "001", "g0080"): (G, "警察署・公園・保健所が混ざる"), ("b102", "001", "g0081"): (G, "同上"),
    **{("b103", "001", f"g{i:04d}"): (G, "崩れているのは区市町村名の列だけ（ほかの列は読める）") for i in range(71, 80)},
    ("b103", "002", "g0153"): (G, "同じ表の名称と同じく場所（手順 D）"), ("b103", "002", "g0154"): (G, "同上"),
    ("b103", "002", "g0226"): ("unknown", "回数かコードか決められない"),
    ("b104", "001", "g0012"): (G, "値が「*」だけの注の列"), ("b104", "001", "g0023"): (G, "注が混ざる"),
    ("b108", "001", "g0043"): (G, "燃料の品目は product（b095 と同じ）"),
    ("b108", "002", "g0158"): (G, "州の番号のコードは区域を指す id（国コードとは違う）"),
    ("b108", "002", "g0212"): (G, "値の範囲の書き方で意味が決まらない"),
    ("b109", "001", "g0021"): ("unknown", "パイプラインの名前は場所か設備か決められない"),
    ("b109", "002", "g0131"): (G, "指標のコード（B9）"),
    ("b110", "001", "g0027"): (G, "危険の組み合わせを書いた文"), ("b110", "001", "g0029"): ("unknown", "注の記号の意味が分からない"),
    ("b110", "001", "g0081"): (G, "表は読める（活動の名前）"), ("b110", "001", "g0082"): (G, "表は読める（件数）"),
}
DICT_META = {  # 生データの辞書の表（列の説明の表）の、表名・列の別名・値の参照の列は、どの種類とも言いにくい → unknown
    ("b108", "001", "g0001"), ("b108", "001", "g0007"), ("b108", "002", "g0144"), ("b108", "002", "g0146"), ("b108", "002", "g0147"),
    ("b108", "002", "g0149"), ("b108", "002", "g0151"), ("b109", "001", "g0059"), ("b109", "001", "g0065"), ("b109", "001", "g0066"),
    ("b109", "001", "g0069"), ("b109", "001", "g0070")}


def read(p):
    return dict(l.rstrip("\n").split("\t")[:2] for l in open(p, encoding="utf-8") if l.startswith("g"))


def main():
    doc = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude_answers_sha256.json"), encoding="utf-8"))
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
