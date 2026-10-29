"""重大・不明になった列を ChatGPT に聞き返すシートを作る（2026-10-29 Claude。オーナー「重大、不明になった列をチャットGPTに聞き返して
なぜその判断になったのかを事細かに説明させてお前の推論と付き合わせてC3の判断のルールに反映できるようにしろ」）。

- シート 001（x 番号）：今の製品の形が誤った列（misses.jsonl：重大 1・数字の列を数字以外と言い切った 36）。何も見せずに新しく判断して説明してもらう
- シート 002〜（e 番号）：不明 329 列のうち、手がかりの候補（candidates.py）で拾えない列。前回の ChatGPT の答えを見せ、なぜそう判断したかを説明してもらう。
  前回正しかった列も混ぜる（誤った列だけを選んだと分からないように）
正解・今の仕組みの答え・段は伏せる。出力：explain/sheets/explain_NNN.md、explain/index.json（先生は見ない）
使い方：python research/unknown/explain.py（001〜006）／python research/unknown/explain.py --m11（007・008）
"""
import json
import os
import random
import sys

sys.path.insert(0, ROOT_DIR := os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import verifier_eval as E  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from candidates import CANDS, hit  # noqa: E402
from rules_draft import present  # noqa: E402

OUT = os.path.join(HERE, "explain")
SEED = 20261030
SIZE = 40
CUES = ("見出しの語", "単位の列", "表の題名", "同じ表の列名", "値の形", "決められない")
LABELS = "account address amount category date email id org other person phone product quantity rate tax_class text unknown S"

FORM_NEW = ["- 種類：", "- 決め手：", "- ①列名・単位の語から読めること：", "- ②表の題名から読めること：", "- ③同じ表の列名から読めること：",
            "- ④値の形から読めること：", "- 迷った種類と、それを退けた理由：", "- 自信が低い・決められないなら、その理由と、何があれば決められたか：",
            "- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：", "- 確信：高・中・低"]
FORM_AGAIN = ["- 前回の答えを変えるか：変えない／変える（新しい種類）"] + FORM_NEW


def cut(s, n):
    s = str(s).replace("\n", " ")
    return s if len(s) <= n else s[:n] + "…"


def block(uid, header, values, title, unit, siblings, prev=None, later=None, later_label="欠けでない値（表の後ろの行から。先頭 8 個は欠けの記号だけ）"):
    L = [f"## {uid} — 見出し「{cut(header, 60)}」", "- 値：" + " | ".join(cut(v, 30) for v in values[:8])]
    if later:
        L.append(f"- {later_label}：" + " | ".join(cut(v, 30) for v in later[:8]))
    if title:
        L.append(f"- 表の題名：{cut(title, 70)}")
    if unit:
        L.append(f"- 同じ表の単位の列：{cut(unit, 60)}")
    if siblings:
        L.append("- 同じ表の列名：" + ", ".join(cut(s, 30) for s in siblings[:12]))
    if prev:
        L.append(f"- **前回のあなたの答え**：{prev['label']}（決め手：{prev['cue']}）メモ「{prev['memo']}」")
    return L + [""]


def head(no, total, again):
    L = [f"# 判断の説明 {no:03d} / {total:03d}（1 列ずつ、くわしく）", "",
         "今の仕組みが「不明」と答えたか、種類を取り違えた列です。人がどう考えて種類を決めるかを、決め方の規則（C3 の判断のルール）に移したいので、**考えた順にくわしく**書いてください。",
         "",
         "- LABEL_GUIDE.md（v2.1）の判定の順番（①列名・単位 → ②表の題名 → ③同じ表の列 → ④値の形）で、それぞれから**何が読めたか・読めなかったか**を書く。読めなければ「なし」",
         "- 「迷った種類」には、候補に上がった別の種類と、それを退けた理由を書く（例：「amount も考えたが、通貨の記号も単位の列もなく、値が整数の小さい数なので quantity」）",
         "- 「規則にするなら」は、ほかの表にも当てはまる言い方で 1〜2 文。当てはまらない例（その規則で誤りそうな列）も書く。規則にできないなら「できない（理由）」",
         f"- 決め手は次から 1 つ：{'・'.join(CUES)}。使えるラベル：{LABELS}",
         "- **見ないもの**：`research/unknown/columns.jsonl`・`misses.jsonl`・`sheet_index.json`・`explain/index.json`・`compare*`・`candidates*`・`findings.md`（正解と今の仕組みの答えが入っている）、Grok の答え、モデルの予測",
         f"- 答え：末尾の雛形を写して埋め、`research/unknown/explain/answers_chatgpt/explain_{no:03d}.md` に置く。見出し（`## x0001` など）と各行の頭（`- 種類：` など）は変えない", ""]
    if again:
        L.insert(4, "- この枚の列には、**前回の調査でのあなたの答え**を付けてあります（正しいとも誤りとも限りません）。前回なぜそう判断したかを、今の目で説明してください。考え直して変えるなら「前回の答えを変えるか」に書く")
    return L


def main():
    titles = json.load(open(os.path.join(ROOT, "materials", "pool", "titles.json"), encoding="utf-8"))
    misses = [json.loads(l) for l in open(os.path.join(HERE, "misses.jsonl"), encoding="utf-8")]
    cmp_rows = [json.loads(l) for l in open(os.path.join(HERE, "compare.jsonl"), encoding="utf-8")]
    cols = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}
    # 先頭 8 個が欠けの記号だけの列は、後ろの行の値も見せる（2026-10-29 追加：本体の入力も先頭 5 個だけで、EW_…_SA の 6 列は後ろに件数がある）
    full = {}
    for b in sorted({json.loads(l)["batch"] for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}):
        for c in E.load_batch(b):
            full[c["id"]] = [str(v) for v in c["values"]]
    rng = random.Random(SEED)
    rng.shuffle(misses)
    rest = [r for r in cmp_rows if not any(hit(c, r) for c in CANDS)]
    rng.shuffle(rest)
    groups = [("x", misses, False)] + [("e", rest[i:i + SIZE], True) for i in range(0, len(rest), SIZE)]
    os.makedirs(os.path.join(OUT, "sheets"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "answers_chatgpt"), exist_ok=True)
    open(os.path.join(OUT, "answers_chatgpt", ".keep"), "w").close()
    index, n_e, n_x = [], 0, 0
    for no, (kind, part, again) in enumerate(groups, 1):
        L = head(no, len(groups), again)
        tpl = []
        for r in part:
            if kind == "x":
                n_x += 1
                uid = f"x{n_x:04d}"
                L += block(uid, r["header"], r["values"], titles.get(r["table"], ""), r.get("unit") or "", r["siblings"])
                index.append({"key": uid, "id": r["id"], "group": "misses"})
            else:
                n_e += 1
                uid = f"e{n_e:04d}"
                c = cols[r["id"]]
                prev = {"label": r["chatgpt"], "cue": r["chatgpt_cue"], "memo": r["chatgpt_memo"]}
                later = present(full.get(r["id"], [])) if not present(c["values"]) else None
                L += block(uid, c["header"], c["values"], c["title"], c.get("unit") or "", c["siblings"], prev, later)
                index.append({"key": uid, "id": r["id"], "u": r["u"], "group": "unknown"})
            tpl += [f"## {uid}"] + (FORM_AGAIN if again else FORM_NEW) + [""]
        L += ["## 答えの雛形", "", "```markdown"] + tpl + ["```", ""]
        open(os.path.join(OUT, "sheets", f"explain_{no:03d}.md"), "w", encoding="utf-8").write("\n".join(L))
    json.dump({"note": "先生は答え終わるまで見ない", "items": index}, open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"{len(groups)} 枚：誤った列 {n_x}・不明の列 {n_e}")


def again_m11():
    """シート 007〜（r 番号）：原因がまだ分からない「本体が誤り」の列（root_cause.jsonl の M11）を、列ごとの説明でもう一度聞く（2026-10-30）。
    002〜006 の説明は項目ごとに 3〜12 通りの決まり文句だった（explain/compare.md「説明の点検」）ので、001 と同じく列ごとに書いてもらう。"""
    rc = [json.loads(l) for l in open(os.path.join(HERE, "root_cause.jsonl"), encoding="utf-8")]
    ids = [r["id"] for r in rc if r["mechanism"].startswith("M11")]
    cols = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}
    cmp_rows = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "compare.jsonl"), encoding="utf-8")}
    full = {}
    for b in sorted({cols[i]["batch"] for i in ids}):
        for c in E.load_batch(b):
            full[c["id"]] = [str(v) for v in c["values"]]
    random.Random(SEED + 7).shuffle(ids)
    half = (len(ids) + 1) // 2
    index = json.load(open(os.path.join(OUT, "index.json"), encoding="utf-8"))
    index["items"] = [x for x in index["items"] if not x["key"].startswith("r")]
    n = 0
    for no, part in ((7, ids[:half]), (8, ids[half:])):
        L = head(no, 8, True)
        L.insert(4, "- **この枚は 001 と同じく、列ごとに考えて書いてください**。各項目に、その列の見出しの語・値・同じ表の列名を具体的に入れる。ほかの列と同じ理由なら、文を写さず「r0003 と同じ（違い：…）」と書く。決まり文句（「兄弟列の構造から…を見分ける」「数字だけでIDや量と決めない」など）は使わない")
        L.insert(5, "- 値は先頭 8 個と、表の後ろの行から欠けでない値 8 個を並べた。分からない語（略語・ドイツ語・フランス語）は、どう読んだかを書く")
        tpl = []
        for i in part:
            n += 1
            uid = f"r{n:04d}"
            c, r = cols[i], cmp_rows[i]
            later = [v for v in present(full.get(i, [])) if v not in c["values"][:8]][:8]
            L += block(uid, c["header"], c["values"], c["title"], c.get("unit") or "", c["siblings"],
                       {"label": r["chatgpt"], "cue": r["chatgpt_cue"], "memo": r["chatgpt_memo"]}, later or None, "表の後ろの行の値（欠けを除く、先頭 8 個と重ならないもの）")
            index["items"].append({"key": uid, "id": i, "u": r["u"], "group": "unknown_m11"})
            tpl += [f"## {uid}"] + FORM_AGAIN + [""]
        L += ["## 答えの雛形", "", "```markdown"] + tpl + ["```", ""]
        open(os.path.join(OUT, "sheets", f"explain_{no:03d}.md"), "w", encoding="utf-8").write("\n".join(L))
    json.dump(index, open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"007・008：M11 の {n} 列")


if __name__ == "__main__":
    again_m11() if "--m11" in sys.argv else main()
