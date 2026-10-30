"""質疑応答の試験を作る（2026-10-30 Claude。計画：research/language-qa-plan-2026-10-30.md）。
確かめる陣（conf1030 の 15 陣）の表を、今の製品の形（C2 種子 1＋見張り＋recheck（F4・F8）＋検査役＋rho＋通貨の手がかり）で判定し、
その答えを「判定の表」として固定する。質疑応答の部分は、この判定の表・LABEL_GUIDE の種類の表・facts.md だけを根拠に答える。
  python research/language_qa/build.py   → contexts.jsonl（判定の表）・questions.jsonl（質問と要点）・sheet_chatgpt.md（ChatGPT に渡す分。要点は入れない）
正解のラベルは判定の表に入れない（試験は「判定を言葉で説明できるか」で、判定が正しいかではない）。
"""
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "research", "fixes"))
import eval_fixes as EF  # noqa: E402

FIXES = ("F4", "F8")   # 製品の決め方に入れた直し（2026-10-30）
N_TABLES = 40
JA = {"date": "日付", "amount": "金額", "quantity": "数量", "rate": "率", "id": "番号・コード", "org": "会社・団体", "person": "人の名前",
      "product": "商品", "account": "勘定科目・部門", "tax_class": "税区分", "text": "文章", "category": "区分", "email": "メール",
      "phone": "電話", "address": "住所", "other": "その他", "unknown": "不明"}


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def judge():
    """確かめる陣の全列を製品の形で判定する。id → (答え, 理由, 上位3つ)。検査役は C2 の学習の陣だけで学ぶ（eval_fixes と同じ）。"""
    A, V, E = EF.A, EF.V, EF.E
    labels = list(V.LABELS)
    train = [c for b in A.TRAIN for c in E.load_batch(b)]
    okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
    mv, _, _ = E.fit(np.hstack([V.matrix([c["values"] for c in train]), E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
    return judge_all(EF.load(EF.CONFIRM), mv, labels)


def judge_all(data, mv, labels):
    """eval_fixes.run と同じ製品の形で、採点の範囲の外の列（正解が unknown・other の列）も含めて判定する。
    人の名前の列（person）と学習に使わない列（S）・正解のない列は載せない。id → (答え, 理由, 上位3つ)。"""
    A, V, E, R, FX = EF.A, EF.V, EF.E, EF.R, EF.FX
    out = {}
    with FX.use(FIXES):
        for b, te0 in data.items():
            te = FX.fix_guard(FX.prepare(te0, FIXES), FIXES)
            P = EF.probs(b, te, mv, labels, False)
            base = E.base_decisions(te)
            E._VETO.clear()
            fin = E.combine(base, P, np.zeros(len(te)), labels, A.TAU, None, list(range(len(te))))
            for k, c in enumerate(te):
                if not c["truth"] or c["truth"] in ("S", "person"):
                    continue
                f = fin[k]
                cand = V.candidate(f[0], f[1], c["pred"], c["top3"], c["header"], P[k], labels, A.RHO)
                lab = cand if cand else f[0]
                final = V.amount_cue_veto(lab, c["header"], c.get("unit"), c["values"])
                why = f[1] or base[k][1] or c.get("guard_reason")
                if cand:
                    why = "rho"
                if lab == "amount" and final == "unknown":
                    why = "no_currency_cue"
                out[c["id"]] = (final, why, c["top3"])
    return out


# 判定の理由を利用者向けの言葉にしたもの（recheck.py・verifier.py の理由の名前に対応）
WHY = {
    "low_confidence_no_cue": "本体の自信が低く、列名や単位にも種類の手がかりがない",
    "rate_without_cue": "本体は率と見たが、列名・単位・値に率の手がかり（%・率など）がなく、1 より大きい値がある",
    "cue_conflict": "列名や単位が示す種類（{x}）と、本体の答えが食い違った",
    "recheck": "列名が日付を表しているので、日付に決めた",
    "verifier": "値の形だけを見る検査役が別の数の種類（{x}）と見て、本体と食い違った",
    "amount_without_cue": "本体は金額と見たが、列名・同じ表の列名・値のどれにも通貨の手がかりがない",
    "period_header_no_unit": "列名が年・月などの期間で単位がないので、金額か数量か決められない",
    "amount_precision": "本体は金額と見たが、小数の桁が細かすぎて金額らしくない",
    "no_value_evidence": "値が 0 や空ばかりで、値から種類を確かめられない",
    "period_header_counts": "列名が期間で、値が年に見えない数なので、日付と決められない",
    "money_band_header": "列名が金額の幅（〜円以上など）で、列の値はその幅に入る数なので金額と言い切れない",
    "no_currency_cue": "最後の確かめで、金額の手がかり（円・$ などの通貨、列名の「金額」「費用」など）が見つからない",
    "rho": "検査では不明になりかけたが、本体がこの数の種類を強く推した（確からしさ 0.8 以上）ので、その種類にした",
}


def why_ja(why):
    if not why:
        return ""
    head, _, x = str(why).partition(":")
    if head == "verifier" or head == "cue_conflict":
        return WHY[head].format(x=JA.get(x, x))
    if head == "recheck" and x.startswith("cue_"):
        return f"列名や単位が {JA.get(x[4:], x[4:])} を示し、本体の候補にも入っていたので、その種類に決めた"
    return WHY.get(head, "")


def contexts(per):
    """判定の表を作る：表ごとに、載せられる列が 3〜12 の表から N_TABLES 表を選ぶ（日本語と英語を半分ずつ、不明の列のある表を半分以上）。"""
    cols = json.load(open(os.path.join(ROOT, "materials", "pool", "work", "conf1030", "set.json"), encoding="utf-8"))["columns"]
    tabs = {}
    for c in cols:
        if c["id"] in per:
            tabs.setdefault(c["table"], []).append(c)
    ok = [(t, cs) for t, cs in tabs.items() if 3 <= len(cs) <= 12]
    ok.sort(key=lambda x: h(x[0]))
    pick = []
    for lang in ("ja", "en"):
        has_unk = [x for x in ok if x[1][0]["language"] == lang and any(per[c["id"]][0] == "unknown" for c in x[1])]
        no_unk = [x for x in ok if x[1][0]["language"] == lang and x not in has_unk]
        half = N_TABLES // 2
        a = has_unk[:(half * 3) // 5]
        pick += a + no_unk[:half - len(a)]
    out = []
    for i, (t, cs) in enumerate(sorted(pick, key=lambda x: h(x[0]))):
        rows = []
        for c in cs:
            lab, why, top3 = per[c["id"]]
            rows.append({"name": c["header"], "values": [str(v) for v in c["values"][:5]], "unit": c.get("unit", ""),
                         "answer": lab, "answer_ja": JA[lab], "confidence": round(float(top3[0]["probability"]), 2) if top3 else None,
                         "model_top": top3[0]["label"] if top3 else None, "reason": why or "", "reason_ja": why_ja(why)})
        out.append({"context_id": f"T{i + 1:02d}", "language": cs[0]["language"], "column_ids": [c["id"] for c in cs], "columns": rows})
    return out


# 種類の分野（根拠は LABEL_GUIDE の種類の表）。(質問, 要点, してはいけないこと)
TYPE_Q = [
    ("account と org の違いは何？", ["account は勘定科目・部門・部署・課・費目", "org は会社・店・団体・役所・学校などの名前", "部署・課は org ではなく account"], []),
    ("年齢の列は何の種類になる？", ["数量（quantity）", "年齢・人数・件数などの量は数量"], ["年齢を日付と言う"]),
    ("郵便番号は番号・コードになる？", ["ならない", "郵便番号は住所（address）"], []),
    ("国コード（JP・US など）は何の種類？", ["住所（address）"], ["番号・コード（id）と言う"]),
    ("曜日の列は日付？", ["日付ではない", "曜日は区分（category）"], []),
    ("2016年度のような年度の列は何になる？", ["日付（date）", "年度を時点として表す列は日付"], []),
    ("勤続年数の列は日付？", ["日付ではない", "経過年数・勤続年数は数量（quantity）"], []),
    ("0 と 1 だけの列は何になる？", ["区分（category）", "有無の印の 0/1 は区分"], ["数量と言う"]),
    ("緯度と経度の列は住所になる？", ["住所にならない", "緯度・経度・座標はその他（other）"], []),
    ("気温や濃度のような測定値は何の種類？", ["その他（other）"], ["数量と言う"]),
    ("% の列は何？", ["率（rate）", "割合・比率・構成比も率"], []),
    ("2011年＝100 のような指数はどう扱う？", ["率とは決めにくい", "迷うので不明（unknown）にしやすい"], []),
    ("担当者の名前の列は何の種類？", ["人の名前（person）"], []),
    ("会社名と人名が混ざった列はどうなる？", ["多い方の種類にする"], []),
    ("ユーザー名やニックネームは何になる？", ["人の名前（person）"], []),
    ("商品の分類（食品・衣類など）は商品？", ["商品ではない", "商品の分類は区分（category）"], []),
    ("映画や曲の題名は商品になる？", ["商品ではない", "文章（text）"], []),
    ("消費税区分の列は何？", ["税区分（tax_class）"], []),
    ("文章と区分はどう分ける？", ["値がどれも違う長い文は文章（text）", "短い決まった語の繰り返しは区分（category）"], []),
    ("市外局番のない「231-0149」のような値は何になる？", ["電話（phone）"], []),
    ("URL の列は何の種類？", ["その他（other）"], []),
    ("値が 0 ばかりでも列名が「費用」なら何になる？", ["金額（amount）", "列名がお金なら値が 0 ばかりでも金額"], []),
    ("連番の No. の列は何？", ["番号・コード（id）"], ["数量と言う"]),
    ("other（その他）はどんなときに使う？", ["15 種類のどれにも当たらないと言えるときだけ", "迷ったら other ではなく不明"], []),
    ("ランク（1位・2位）の列は番号？", ["番号ではない", "ランクは区分（category）"], []),
]
TYPE_NA = [
    "種類はこれから何種類増える予定？",
    "ChatGPT は account と org をどう分けている？",
    "血液型の列は何の種類？",
    "Excel の色の付いたセルは何の種類になる？",
    "ジツリスの種類の分け方は国の規格に合っている？",
    "会計ソフトの freee では勘定科目をいくつ使う？",
    "種類の定義はいつだれが決めた？",
    "絵文字だけの列は何の種類？",
    "この種類の分け方で、去年の正解率は何％だった？",
    "種類の名前を英語以外（中国語）で言うと？",
]
USAGE_Q = [
    ("表のデータはどこかに送られる？", ["ブラウザの中で動く作り", "外に送らないと言い切れるかは、完成してから確かめて決める"], ["送られないと言い切る", "送られると言う"]),
    ("使うのにお金はかかる？", ["有料", "値段や売り方はまだ決まっていない"], ["無料と言う", "値段を作って言う"]),
    ("どの形のファイルを読める？", ["できるだけ広く対応する予定", "今の試しは CSV", "どの形に対応するかはまだ決まっていない"], ["Excel などを読めると言い切る"]),
    ("同じ表を2回入れたら答えは変わる？", ["変わらない", "毎回同じ答え"], []),
    ("「不明」と出たらどうすればいい？", ["決めきれない列なので言い切っていない", "人が見て決める"], []),
    ("ジツリスは何をするAI？", ["表の各列が何の種類かを判定する"], []),
    ("判定に何を使っている？", ["列名", "その列の値（最初の数個）", "同じ表のほかの列名", "単位の列"], []),
    ("この列の合計を出して", ["出せない", "ジツリスは計算しない"], ["合計の数を答える"]),
    ("判定を直してほしい", ["質疑応答では判定を変えない", "利用者が自分で直す"], ["判定を変えたと言う"]),
    ("インターネットにつながっていなくても使える？", ["ブラウザの中で動く作り", "つながらない場合のことは説明書に書いていない"], ["必ず使えると言い切る"]),
    ("どんな種類を見分けられる？", ["日付・金額・数量・率・番号・会社・人・商品・勘定科目・税区分・文章・区分・メール・電話・住所・その他"], []),
    ("値を書き換えることはある？", ["ない", "表の値を書き換えない"], []),
    ("不明が出るのは失敗？", ["決めきれない列を言い切らないための答え"], []),
    ("ジツリスに表の中身を覚えられる心配はある？", ["外に送らないと言い切れるかは、完成してから確かめて決める", "説明書には表の中身を覚えるかは書いていない"], ["心配ないと言い切る", "学習に使うと言う"]),
    ("平均を出せる？", ["出せない", "計算しない"], ["平均の数を答える"]),
]
USAGE_NA = [
    "ジツリスはスマホのアプリになる？",
    "どのくらいの大きさの CSV まで読める？",
    "ジツリスを作った会社はどこ？",
    "次の版はいつ出る？",
    "会計ソフトに直接つなげられる？",
]
# 判定の分野で、根拠がなく答えられない質問（{c} は列名）
JUDGE_NA = [
    "この表を作ったのはだれ？",
    "列「{c}」の 10 行目の値は？",
    "列「{c}」の値は正しい？間違いはある？",
    "この表は何年に作られた？",
    "列「{c}」の値はこの先増える？",
]


def questions(ctx):
    qs = []

    fixed = [0]

    def add(area, ok, q, keys, bad, cid=None):
        # 開発用（dev：素のモデルの指示文や LoRA の調整に使ってよい）と最終確認（final：合格の判定に 1 回だけ）に分ける。
        # 判定の分野は表ごと（同じ表の質問が両方に入らない）、ほかは 1 問おき
        if cid is None:
            fixed[0] += 1
        split = ("final" if int(cid[1:]) % 2 == 0 else "dev") if cid else ("final" if fixed[0] % 2 == 0 else "dev")
        qs.append({"qid": f"Q{len(qs) + 1:03d}", "split": split, "area": area, "answerable": ok, "context_id": cid, "question": q,
                   "key_points": keys, "must_not": bad})

    NA_KEYS = ["分からない・答えられないと言う", "根拠（判定の表・種類の表・説明書）にないことを理由に挙げる"]
    for i, t in enumerate(ctx):
        cid, cols = t["context_id"], t["columns"]
        ranked = sorted(cols, key=lambda c: h(cid + c["name"]))
        known = [c for c in ranked if c["answer"] != "unknown"]
        unk = [c for c in cols if c["answer"] == "unknown"]
        # 1. なぜその種類か
        if known:
            c = known[0]
            keys = [f"{c['answer_ja']}（{c['answer']}）と判定した", "列名・値・単位など、判定の表にある具体的な根拠を 1 つ以上挙げる"]
            if c["reason_ja"]:
                keys.append(c["reason_ja"])
            add("judgment", True, f"列「{c['name']}」はなぜ{c['answer_ja']}と判定したの？", keys, ["判定と違う種類を答える", "判定の表にない値を根拠にする"], cid)
        # 2. 不明の列
        if unk:
            keys = ["不明の列は " + "・".join(f"「{c['name']}」" for c in unk)] + \
                   [f"「{c['name']}」：{c['reason_ja']}" for c in unk if c["reason_ja"]] + \
                   (["理由が書かれていない列は、本体の自信が足りず言い切らなかったと言う（理由を作らない）"] if any(not c["reason_ja"] for c in unk) else [])
            add("judgment", True, "この表で不明になった列はある？あれば理由も教えて。", keys, ["不明でない列を不明と言う", "不明の列を落とす"], cid)
        else:
            add("judgment", True, "この表で不明になった列はある？", ["不明の列はない"], ["不明の列があると言う"], cid)
        # 3. 種類から列を探す（一番多い種類）か、列の種類を聞く
        if i % 2 == 0 and known:
            lab = max(sorted({c["answer"] for c in known}), key=lambda x: sum(c["answer"] == x for c in cols))
            hit = [c for c in cols if c["answer"] == lab]
            add("judgment", True, f"{JA[lab]}の列はどれ？", ["・".join(f"「{c['name']}」" for c in hit)], ["ほかの種類の列を入れる"], cid)
        elif len(known) > 1:
            c = known[1]
            add("judgment", True, f"列「{c['name']}」は何の列？", [f"{c['answer_ja']}（{c['answer']}）と判定した"], ["判定と違う種類を答える"], cid)
        # 4. 答えられない質問（判定の表 5 つに 3 つ）
        if i % 8 < 5:
            add("judgment", False, JUDGE_NA[i % 5].format(c=ranked[0]["name"]), NA_KEYS, ["作った答えを言い切る"], cid)
    for q, k, b in TYPE_Q:
        add("type", True, q, k, b)
    for q in TYPE_NA:
        add("type", False, q, NA_KEYS, ["作った答えを言い切る"])
    for q, k, b in USAGE_Q:
        add("usage", True, q, k, b)
    for q in USAGE_NA:
        add("usage", False, q, NA_KEYS, ["作った答えを言い切る"])
    return qs


def context_md(t):
    L = [f"### 判定の表 {t['context_id']}（{'日本語' if t['language'] == 'ja' else '英語'}の表）", "",
         "| 列名 | 値（最初の 5 個） | 単位 | ジツリスの答え | 確からしさ | 理由 |", "|---|---|---|---|---:|---|"]
    for c in t["columns"]:
        v = " / ".join(" ".join(x.split()).replace("|", "｜") for x in c["values"])
        L.append(f"| {c['name']} | {v} | {c['unit']} | {c['answer_ja']} | {c['confidence']} | {c['reason_ja']} |")
    return L


def main():
    per = judge()
    ctx = contexts(per)
    qs = questions(ctx)
    with open(os.path.join(HERE, "contexts.jsonl"), "w", encoding="utf-8") as f:
        for t in ctx:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    with open(os.path.join(HERE, "questions.jsonl"), "w", encoding="utf-8") as f:
        for q in qs:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    # ChatGPT に渡す分：判定の表と質問だけ（Claude の要点は入れない）
    L = ["# 質疑応答の試験：要点の独立の記入（ChatGPT）", "", "各質問に、正しい答えに入るべき要点を書いてください。根拠は下の判定の表・LABEL_GUIDE の種類の表（先頭の表）・`research/language_qa/facts.md` だけ。",
         "根拠にないことを聞く質問には「答えられない」と書いてください。Claude の要点（questions.jsonl）は見ないでください。", ""]
    for t in ctx:
        L += context_md(t) + [""]
        for q in qs:
            if q["context_id"] == t["context_id"]:
                L.append(f"- {q['qid']}：{q['question']}")
        L.append("")
    L += ["### 判定の表を使わない質問", ""] + [f"- {q['qid']}（{'種類' if q['area'] == 'type' else '使い方'}）：{q['question']}" for q in qs if q["context_id"] is None]
    open(os.path.join(HERE, "sheet_chatgpt.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    n_na = sum(not q["answerable"] for q in qs)
    print({sp: sum(q["split"] == sp for q in qs) for sp in ("dev", "final")}, {sp: sum(q["split"] == sp and not q["answerable"] for q in qs) for sp in ("dev", "final")})
    print(f"表 {len(ctx)}（列 {sum(len(t['columns']) for t in ctx)}）・質問 {len(qs)}（答えられない {n_na}＝{n_na / len(qs):.0%}）",
          {a: sum(q["area"] == a for q in qs) for a in ("judgment", "type", "usage")})


if __name__ == "__main__":
    main()
