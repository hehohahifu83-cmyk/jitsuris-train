"""不明になった列を先生（ChatGPT・Grok）に見せるシートを作る（2026-10-29 Claude）。正解・本体と検査役の答え・不明にした段は伏せる。
1 列ずつ「種類」と「決め手の手がかり」を答えてもらい、人なら決められるのに不明になった形を探す。
出力：research/unknown/sheets/sheet_NNN.md、research/unknown/sheet_index.json（u 番号 → 列の id。先生は答え終わるまで見ない）
使い方：python research/unknown/sheets.py
"""
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261029
SIZE = 110
CUES = ("見出しの語", "単位の列", "表の題名", "同じ表の列名", "値の形", "決められない")
LABELS = "account address amount category date email id org other person phone product quantity rate tax_class text unknown S"


def cut(s, n):
    s = str(s).replace("\n", " ")
    return s if len(s) <= n else s[:n] + "…"


def main():
    rows = [json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")]
    random.Random(SEED).shuffle(rows)
    os.makedirs(os.path.join(HERE, "sheets"), exist_ok=True)
    for who in ("answers_chatgpt", "answers_grok"):
        os.makedirs(os.path.join(HERE, who), exist_ok=True)
        open(os.path.join(HERE, who, ".keep"), "w").close()
    index = []
    sheets = [rows[i:i + SIZE] for i in range(0, len(rows), SIZE)]
    for no, part in enumerate(sheets, 1):
        L = [f"# 不明になった列の調査 {no:03d} / {len(sheets):03d}（1 列ずつ）", "",
             "公開データの表の列です。今の仕組みはこれらの列に種類を付けられず「不明」と答えました。人が見て決められるか、決められるなら何が決め手かを知りたい調査です。",
             "",
             "- **1 列ずつ**、LABEL_GUIDE.md（v2.1）のどの種類かを答える。決められなければ `unknown`。",
             "- **決め手**を次から 1 つ（いちばん効いたもの）：" + "・".join(CUES),
             "- メモは短く（なぜそう決めたか、何があれば決められたか）。日本語で。",
             f"- 使えるラベル：{LABELS}",
             "- 答え：末尾の雛形を写し、ChatGPT は `research/unknown/answers_chatgpt/sheet_NNN.tsv`、Grok は `research/unknown/answers_grok/sheet_NNN.tsv` に置く。1 行＝「u0001<TAB>ラベル<TAB>決め手<TAB>メモ」",
             "- **見ないもの**：`research/unknown/columns.jsonl`・`sheet_index.json`（正解と今の仕組みの答えが入っている）、もう一人の先生の答え、モデルの予測", ""]
        for r in part:
            uid = f"u{len(index) + 1:04d}"
            index.append({"u": uid, "id": r["id"]})
            L.append(f"## {uid} — 見出し「{cut(r['header'], 60)}」")
            L.append("- 値：" + " | ".join(cut(v, 30) for v in r["values"][:8]))
            extra = []
            if r.get("title"):
                extra.append(f"表の題名：{cut(r['title'], 60)}")
            if r.get("unit"):
                extra.append(f"同じ表の単位の列：{cut(r['unit'], 60)}")
            if r.get("siblings"):
                extra.append("同じ表の列名：" + ", ".join(cut(s, 24) for s in r["siblings"][:10]))
            L += [f"- {e}" for e in extra] + [""]
        L += ["## 答えの雛形", "", "```"] + [f"{x['u']}\t\t\t" for x in index[-len(part):]] + ["```", ""]
        open(os.path.join(HERE, "sheets", f"sheet_{no:03d}.md"), "w", encoding="utf-8").write("\n".join(L))
    json.dump({"note": "先生は答え終わるまで見ない", "items": index}, open(os.path.join(HERE, "sheet_index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"{len(index)} 列・{len(sheets)} 枚")


if __name__ == "__main__":
    main()
