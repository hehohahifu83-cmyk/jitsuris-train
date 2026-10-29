"""重大・不明になった列についての Claude の推論（2026-10-29。ChatGPT の説明を読む前に書いて commit する）。
Claude は正解と今の仕組みの段を見て書いている（ChatGPT は見ていない）。そのため「なぜ今の仕組みが止めた・誤ったか」と「規則にできるか」が中心。
出力：explain/claude_reasoning.jsonl（1 行＝シートの 1 列）・explain/claude_reasoning.md（規則ごとのまとめと、列ごとの推論）
使い方：python research/unknown/claude_reasoning.py
"""
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rules_draft import NUMERIC, RULES, decide, guard_name_numeric, present  # noqa: E402

OUT = os.path.join(HERE, "explain")

# 手で書いた推論（u 番号＝不明の列、陣の id＝今の仕組みが誤った列）。「正解を見直す」は LABEL_GUIDE と合わない疑いのある正解
NOTES = {
    # --- 今の仕組みが誤った列（misses.jsonl） ---
    "b064-0137": "【重大】「Semaine」（週）で値 2〜53 の整数。本体は quantity と言い切った。週・月の番号は日付の部分（LABEL_GUIDE の date）で、列名の語だけで決まる。G2 で date。同じ表に Nombre_Deces（件数）があるので、値の形（小さい整数）だけで読むと数量に寄る",
    "b015-0047": "「No.」だけで 1,2,3… と続く整数＝行の番号。本体は category。G6b で id",
    "b015-0052": "「No. laboratory confirmed」＝確認された件数。英語の「No. X」は number of X。recheck の \\bno\\.? of\\b は of が要るので当たらない。G6 で quantity",
    "b017-0263": "「batch」で 1,1,2,2。実験の回の番号。列名の語だけでは category と id の境目で、規則にしにくい（batch は区分とも読める）。決めないのが安全",
    "b060-0205": "「GOR CODE」で H・H。列名が CODE で終わるのに category。recheck の \\bcode$ は大文字小文字を問わないので当たるはず→見張りの段で category と言い切ったため recheck を通らない。言い切った答えにも列名の強い手がかり（code$）との食い違いを調べる段が要る（G10）",
    "b060-0706": "「Neither satisfied or dissatisfied」で 7,4,5,3 の整数＝回答の人数。同じ段階の列名でも、小数なら率（u0005 Satisfied 35.3）・整数なら人数。G3 は小数のときだけ rate にし、整数は決めない",
    "b060-0831": "「listed_building」で 1072858 など 7 桁の整数＝登録番号。本体は address。名前の種類なのに値が数字だけ→G8 で不明（列名に番号の語がないので id にはしない）",
    "b060-0900": "「Question」で Q1・Q10＝設問の番号。id か category かは境目（正解は id）。規則にしない",
    "b062-0186": "「Extending Agency」で 3,3,3＝機関のコード。本体は org。名前の種類なのに値が数字だけ→G8 で不明",
    "b065-0193": "b062-0186 と同じ表の形（別の年）。G8 で不明",
    "b063-0071": "「Gemeinde_Nr」で 5,7,12＝自治体の番号。本体は address。G8（_nr）で id。D5 の _nr$ でも id",
    "b063-0141": "「Id Of Animal Category」で animal_1。列名が Id で始まる。G5 で id",
    "b063-0147": "「Id Experiment Category」。G5 で id",
    "b063-0148": "「Id Of Disease Category」。G5 で id",
    "b063-0143": "「Degree of severity 0」で 0,12,200＝その重さの段階の動物の数。列名は区分の名前に見えるが、値は数。同じ表に Degree of severity 1〜3 が並ぶ（区分ごとの数の横持ちの表）。列名の語では決まらず、表をまるごと読む段が要る（G4：同じ形の兄弟列が並び、値が整数なら quantity）",
    "b063-0144": "b063-0143 と同じ（G4）",
    "b063-0145": "b063-0143 と同じ（G4）",
    "b063-0146": "b063-0143 と同じ（G4）。値が 0 だけ",
    "b065-0212": "「Arrest/Detention > Assault with Weapon」で 0 だけ。「区分 > 区分」の列名が並ぶ横持ちの表で、値は件数。G4",
    "b065-0214": "b065-0212 と同じ（G4）",
    "b063-0165": "「parameter_decimals」で 0＝小数の桁数。数（quantity）。G9",
    "b063-0173": "G9", "b063-0181": "G9", "b064-0109": "G9", "b064-0117": "G9",
    "b063-0300": "「kategorie_sortierung」で 1,1,2＝並べる順の番号。正解は id だが、順位（Rank）の列は category と付いている（u Rank）。並び順・順位の正解をそろえる必要がある（正解を見直す）",
    "b064-0197": "b063-0300 と同じ（正解を見直す）",
    "b063-0372": "「id2」で city・europe＝駐車場の短い名前のコード。列名の id2 は ^id\\b に当たらない（id の後に 2）。id\\d*$ にすれば当たる。G5 を広げるかは確かめる陣で",
    "b063-0392": "「traktandum_start_behandlung_uhrzeit」で 13.30-16.30＝時刻の幅。本体は text。G7 で date",
    "b063-0400": "「sessionssitzung_uhrzeit」。G7 で date",
    "b064-0046": "「nfr」で 5A＝排出の分類コード（NFR）。略語は辞書でしか決まらない。規則にしない",
    "b064-0147": "「GEO_CANT」で 1,1,2＝州の番号。GEO_ の列名で値が整数→id だが、GEO_ は地名の列にもなる。規則にしない",
    "b064-0168": "「abkuerzung」（略号）で UPI・ZEMIS＝システムの略号。id か category かは境目。規則にしない",
    "b064-0194": "「verteilzone」で 261_LZ＝区域のコード。列名からは区分（category）とも読める。規則にしない",
    "b064-0210": "「sitzung_titel」で「61. Sitzung」＝会の回の名前。正解は id だが、題名（titel）の列で文字の値なので text とも読める（正解を見直す）",
    "b064-0320": "「verantwortlichkeit_abkuerzung」で KTTGWH・BAFU＝担当の役所の略号。本体は org。略号は org とも id とも読める。正解は id（正解を見直す）",
    "b064-0384": "「Signatur」で GS-GUGE-BIEDERMANN-A-9＝所蔵の請求記号。本体は org（人名を含むため）。G5（^signatur$）で id",
    # --- 不明の列（u 番号）で ChatGPT が誤った・unknown にした列 ---
    "u0003": "「value」で 92,109。同じ表に valueCategory・agegroup・sex。value だけでは決めない（LABEL_GUIDE）。valueCategory の値（例：人数）が分かれば決まる→同じ表の単位・区分の列の値を決め方に渡す必要（G12）",
    "u0006": "「crime」で 0 だけ。同じ表に administration・agriculture…（分野の名前が並ぶ）＝その分野に当たるかの印（0/1）。正解は category。値が 0 だけでは数とも印とも読めない。決めないのが正しい",
    "u0008": "「Gcons2006」で 14300＝ガスの使用量（kWh）。略語で単位がない。決めない（同じ表に Gcons2005Valid）",
    "u0310": "u0008 と同じ",
    "u0012": "「reporting_period」で P01・P02＝会計の期間。正解 date、ChatGPT category。会計の期の番号は date か category か LABEL_GUIDE で決まっていない（正解を見直す）",
    "u0015": "「digital_platform」で e-manuscripta.ch。正解 category、ChatGPT other。サイトの名前の区分。境目",
    "u0016": "「Beschluss」（決定）で 11300。同じ表に Nachgefragt（申請）・Kategorie。決定した額。CHF の手がかりが同じ表のどこにもなければ決めない",
    "u0231": "「Nachgefragt」で 16100。u0016 と同じ表。申請額。通貨の手がかりがないので決めない",
    "u0017": "「VALUE」で値がすべて「.」（欠け）。正解は quantity だが、LABEL_GUIDE では値が空ばかりの列は S（正解を見直す）",
    "u0043": "「Versicherer」（保険者）で 57,62＝保険者の番号。名前の語なのに値が整数。G8 と同じ考えで、名前としては言い切らないが、id とも決めない",
    "u0046": "「funk」で 29,35。意味が分からない略語。決めない",
    "u0068": "「01:30」で 97,96。同じ表に DATE・00:00…＝30 分ごとの計測。量か率かは表の題名がないと分からない。決めない",
    "u0202": "u0068 と同じ", "u0225": "u0068 と同じ",
    "u0069": "「wert」で 12931,44。同じ表に metrik・einheit。einheit（単位）の値が渡れば決まる（G12）",
    "u0127": "「wert」。G12", "u0186": "「wert」。G12", "u0265": "「Wert」。同じ表に Einheit。G12", "u0223": "「Wert」で 4.4e10。同じ表に Kennzahl。G12",
    "u0070": "「Total」で 1,062.00（小数 2 桁）。同じ表に Transaction Date。金額らしいが通貨の手がかりがない。通貨の手がかりの規則（amount_cue_veto）で不明にしたのは決まりどおり",
    "u0081": "u0006 と同じ", "u0329": "u0006 と同じ",
    "u0101": "「designation」で停留所・窓口の名前。正解 category、ChatGPT address。地点の名前は address か category か境目",
    "u0103": "「EW_Compulsory_SA」で値がすべて [x]（伏せた値）。G1 で欠けとして外すと値が残らない。正解は quantity だが、値が空ばかりなら S（正解を見直す）。ChatGPT は [x] を印と読んで category にした→[x]・[z] は英国統計の欠けの記号だと規則に書く（G1）",
    "u0149": "u0103 と同じ（G1）", "u0157": "u0103 と同じ（G1）", "u0276": "u0103 と同じ（G1）", "u0305": "u0103 と同じ（G1）", "u0324": "u0103 と同じ（G1）",
    "u0117": "「referenztarif」で 683。同じ表に waehrung（通貨）。通貨の列があるので金額。同じ表の列名に通貨の語（waehrung・currency・devise）があれば通貨の手がかりにする（G11）",
    "u0129": "「Structure」で建物の名前。正解 category、ChatGPT address。境目",
    "u0141": "「service」でサービスの名前。正解 product、ChatGPT category。境目",
    "u0146": "「Titel」で Parkhaus Storchen。正解 org、ChatGPT address。境目",
    "u0147": "「monitoring_program」で BAQUA_TI。正解 category、ChatGPT id。値が 1 種類のコード。境目",
    "u0148": "「Type of Aid」で C01。正解 category、ChatGPT id。列名が Type of…（種類）なら値がコードでも category。規則にできる：列名が type・kind・art・typ・category で始まるなら id にしない",
    "u0192": "「STATISTIC」で STOCKNURSE。正解 category、ChatGPT id。統計の系列のコード（正解を見直す）",
    "u0171": "「@Caption」で @Creator…＝白書の表が崩れている。正解 date だが、LABEL_GUIDE では S（正解を見直す）",
    "u0228": "「NO_COMPLEMENTAIRE」で 1。同じ表の列名に ZIP のかけらが混ざる。ChatGPT は S。列名の NO_ は番号（id）。表が崩れていても列は読める",
    "u0239": "「originating_sector_fr」で役所の名前。正解 account、ChatGPT org。値は組織名なので org が自然（正解を見直す）",
    "u0256": "「Supplier」で TPS – Funding Account 1。正解 org、ChatGPT account。値は口座名なので境目",
    "u0294": "「Control Budget Code」で DEL・AME＝予算の区分。正解 category、ChatGPT id。列名が Code でも値が少ない種類の略号なら区分。境目",
    "u0306": "「Property」で Home Office - IPS。正解 org、ChatGPT account。組織名なので org",
    "u0309": "「Family_Famille」で植物の科。正解 category、ChatGPT other。分類群は区分",
}

SYSTEM_WHY = {
    "other_class": "見張り：本体の 1 位が other（種類を付けない）",
    "probability_below_threshold": "見張り：本体の 1 位の確率がしきい値より低い",
    "date_value_evidence_low": "見張り：date なのに値に日付の形が少ない",
    "numeric_values_not_parseable": "見張り：数字の種類なのに値が数として読めない",
    "numeric_top2_too_close": "見張り：数字の種類の 1 位と 2 位が近い",
    "amount_without_cue": "recheck：amount なのに列名・単位に金額の手がかりがない",
    "low_confidence_no_cue": "recheck：確信が低く、手がかりもない",
    "rate_without_cue": "recheck：rate なのに率の手がかりがない",
    "no_value_evidence": "recheck：値に根拠がない（0 だけなど）",
}


def main():
    idx = json.load(open(os.path.join(OUT, "index.json"), encoding="utf-8"))["items"]
    misses = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "misses.jsonl"), encoding="utf-8")}
    cols = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "columns.jsonl"), encoding="utf-8")}
    cmp_rows = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "compare.jsonl"), encoding="utf-8")}
    out = []
    for it in idx:
        if it["group"] == "misses":
            m = misses[it["id"]]
            lab, rid = decide(m["header"], m.get("unit"), m["values"], m["siblings"])
            g, gid = guard_name_numeric(m["final"], m["header"], m["values"])
            mine = lab or (g if gid else m["final"])
            why = f"今の仕組みは {m['final']} と言い切った（本体 {m['pred']}）"
            out.append({"key": it["key"], "id": it["id"], "group": "misses", "header": m["header"], "truth": m["truth"], "system": m["final"], "system_why": why,
                        "claude": mine, "rule": rid if lab else gid, "note": NOTES.get(it["id"], "")})
        else:
            c, r = cols[it["id"]], cmp_rows[it["id"]]
            lab, rid = decide(c["header"], c.get("unit"), c["values"], c["siblings"])
            reason = c["guard_reason"] or c["base_reason"] or c["veto_reason"]
            out.append({"key": it["key"], "id": it["id"], "u": it["u"], "group": "unknown", "header": c["header"], "truth": c["truth"], "system": "unknown",
                        "system_why": SYSTEM_WHY.get(reason, reason) + f"（本体 1 位 {c['model_top3'][0][0]} {c['model_top3'][0][1]}）",
                        "claude": lab or "unknown", "rule": rid, "chatgpt_before": r["chatgpt"], "note": NOTES.get(it["u"], "")})
    with open(os.path.join(OUT, "claude_reasoning.jsonl"), "w", encoding="utf-8") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")

    def tally(rows):
        ok = sum(o["claude"] == o["truth"] for o in rows)
        crit = sum(o["claude"] != o["truth"] and o["claude"] in NUMERIC and o["truth"] in NUMERIC for o in rows)
        unk = sum(o["claude"] == "unknown" for o in rows)
        return ok, crit, unk, len(rows) - ok - crit - unk

    mi = [o for o in out if o["group"] == "misses"]
    un = [o for o in out if o["group"] == "unknown"]
    L = ["# 重大・不明になった列：Claude の推論（`research/unknown/claude_reasoning.py`）", "",
         "ChatGPT の説明（`explain/answers_chatgpt/`）を読む前に書いた。Claude は正解・今の仕組みの段を見ている。規則は `rules_draft.py`（まだ製品に入れていない）。", "",
         "## 規則の下書きを当てた結果（決める陣＝新しい陣 8 つ。参考値）", "",
         "| 列の組 | 列 | 正しい | 重大 | 不明のまま | ほかの誤り |", "|---|---:|---:|---:|---:|---:|"]
    for name, rows in (("今の仕組みが誤った列（重大 1・数字の列を数字以外と言い切った 36）", mi), ("不明の列のうち A〜F で拾えない 199 列", un)):
        L.append(f"| {name} | {len(rows)} | " + " | ".join(str(x) for x in tally(rows)) + " |")
    L += ["", f"- 今の仕組みが誤った 37 列：今は正しい 0。規則の下書きで正しくなる {tally(mi)[0]}、不明に下がる {tally(mi)[2]}（言い切りの誤りが不明になるのは安全側）",
          "", "## 規則ごと", "", "| 規則 | 種類 | 中身 | 当たった列 | 正しい | 重大 |", "|---|---|---|---:|---:|---:|"]
    by = defaultdict(list)
    for o in out:
        if o["rule"]:
            by[o["rule"]].append(o)
    desc = {r[0]: (r[1], r[2]) for r in RULES}
    desc["G8"] = ("id／不明", "名前の種類なのに値が数字だけ → 列名に番号の語があれば id、なければ不明（言い切った答えに当てる）")
    for rid in sorted(by):
        rows = by[rid]
        L.append(f"| {rid} | {desc.get(rid, ('', ''))[0]} | {desc.get(rid, ('', ''))[1]} | {len(rows)} | {sum(o['claude'] == o['truth'] for o in rows)} | "
                 f"{sum(o['claude'] != o['truth'] and o['claude'] in NUMERIC and o['truth'] in NUMERIC for o in rows)} |")
    L += ["", "## 規則にしない・別の段が要るもの（推論から）", "",
          "- **G1 欠けの記号**：[x]・[z]・[c]（英国統計）・「.」（CSO）・NA・nil は値の形を読む前に外す。外して値が残らない列は S（今の正解は quantity が付いているので正解を見直す）。ChatGPT は [x] を印と読んで category にした",
          "- **G4 横持ちの表**：「Degree of severity 0〜3」「Arrest/Detention > …」「EW_…_SA」のように、同じ形の列名が並んで値が整数なら、それぞれ区分ごとの数（quantity）。列名の語だけでは決まらず、表をまるごと見る段が要る（C3 計画の「表をまるごと読む本体」・C3c）",
          "- **G10 言い切った答えと列名の強い手がかりの食い違い**：「GOR CODE」を category と言い切った。今は見張りで言い切った列は recheck を通らない。言い切った答えにも code$・_nr・No. の手がかりとの食い違いを調べる段を足す",
          "- **G11 同じ表の通貨の列**：同じ表の列名に waehrung・currency・devise があれば、その表の金額らしい列の通貨の手がかりにする",
          "- **G12 汎用の値の列**：value・wert・VALUE・OBS_VALUE は、同じ表の einheit・unit・metrik・valueCategory の**値**が渡れば決まる。今はシートにも決め方にも単位の列の名前しか渡っていない。データの経路を直す（決め方の規則ではない）",
          "- **正解を見直す**：u0017・u0103 など値がすべて欠けの列（LABEL_GUIDE では S）、u0171（崩れた白書の表）、並び順（kategorie_sortierung＝id）と順位（Rank＝category）の食い違い、u0239・u0306（組織名に account／org）。正解の側を直すと不明・誤りの数が変わる",
          "", "## 列ごと", "", "| 番号 | 見出し | 正解 | 今の仕組み（理由） | ChatGPT 前回 | Claude | 規則 | 推論 |", "|---|---|---|---|---|---|---|---|"]
    for o in out:
        L.append(f"| {o['key']} | {o['header'][:40].replace('|', '/')} | {o['truth']} | {o['system_why'][:60]} | {o.get('chatgpt_before', '—')} | {o['claude']} | {o['rule'] or ''} | {o['note'].replace('|', '/')} |")
    open(os.path.join(OUT, "claude_reasoning.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:30]))


if __name__ == "__main__":
    main()
