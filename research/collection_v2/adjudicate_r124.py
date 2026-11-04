"""教材 b124〜b151 の裁定（2026-11-04 Claude）。先生＝Codex（LABEL_GUIDE v2.4）、2 人目の票＝今の土台 L 種子 1（v2.4 の付け直しより前の教材で学んだ）。

  python research/collection_v2/adjudicate_r124.py   → 各陣の work/<陣>/decisions.jsonl

決め方（食い違い to_review）：
  K1 先生が S（崩れた表・個人名・個人別の記録）→ S（教材に入れない）
  K2 先生が unknown → unknown（教材に入れない。人が見ても決められない列）
  K3 モデルが unknown（見張りが言い切りを止めた）→ 先生のラベル（モデルは別のラベルを言っていない）
  K4 先生 address・モデル org で、見出しが施設の名前の列（名称・名称_カナ・名称_通称・施設名…）
     → address：いろいろな種類の公共施設・AED・避難所の一覧（B10-3）。同じ表の「法人番号・団体名」は管理団体の列で施設の属性ではない
  K5 見出しごとの決まり（教材庫の確定ラベルと LABEL_GUIDE に合わせる）：設置位置＝address（教材庫 80/80）、利用可能曜日＝category（曜日、
     教材庫 180/182）、開始時間・終了時間＝値が時刻なら date（B8）・「施設の…に従う」なら text、利用可能時間（終日など）・特記事項・休館日＝text（営業時間・休みの日の説明）、
     診療科目＝category（B7）
  MANUAL 1 行ずつ見て決めた（理由つき）
抜き取り（audit、先生とモデルが一致）は全部見て、誤りを label に書く。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCHES = ["b124", "b127", "b128", "b131", "b132", "b133", "b134", "b135", "b136", "b137", "b139", "b140",
           "b142", "b143", "b144", "b145", "b147", "b149", "b150", "b151"]
FAC = re.compile(r"^(\d+\.)?(名称(_カナ|_通称)?|カナ|施設名|公民館名|場所名称|投票所施設名|方書|.*施.*設.*名.*|投.*票.*場.*所)$")
TIME = re.compile(r"^\d{1,2}[:：]\d{2}")
MANUAL = {
    "b124#6": ("text", "その他の情報の自由な文"),
    "b124#7": ("text", "登録の区分の番号と名前の羅列（キーワードの羅列）"),
    "b131#3": ("quantity", "天然ガス液の量（単位は別の列）"),
    "b131#23": ("other", "参照表・ファイル名の値"),
    "b131#41": ("category", "対象のコード（TRD 等の決まった区分）"),
    "b131#42": ("category", "0/1 の印"), "b131#43": ("category", "0/1 の印"),
    "b131#53": ("category", "採取の状態のコード"), "b131#60": ("category", "鉱物の種類のコード"),
    "b131#9": ("other", "項目名（フィールド名）の一覧"), "b131#5": ("other", "項目名（フィールド名）の一覧"),
    "b131#14": ("org", "部隊・基地の名前（組織）"),
    "b131#8": ("other", "データセット名"), "b131#12": ("other", "データセット名"),
    "b131#16": ("other", "表・ファイル名"), "b131#17": ("other", "項目の別名"),
    "b131#33": ("category", "対象の種の区分（waterfowl の繰り返し）"),
    "b132#5": ("category", "座標系の区分"), "b132#8": ("org", "出典の機関"),
    "b132#21": ("account", "法定の歳出の項目（B7）"), "b132#22": ("account", "法定の歳出の項目（B7）"),
    "b132#33": ("category", "支払の種類（補助金・拠出金）"), "b132#34": ("category", "支払の種類（補助金・拠出金）"),
    "b132#11": ("other", "項目名の一覧"), "b132#12": ("other", "レイヤー名"), "b132#13": ("other", "項目名の一覧"),
    "b133#0": ("other", "項目名の一覧"), "b133#3": ("other", "データセット名"), "b133#7": ("other", "データセット名"),
    "b134#2": ("date", "暦年（2016 など、date の決まり）"), "b134#12": ("date", "暦年"), "b134#19": ("date", "暦年"),
    "b134#4": ("category", "統計の区分のコード"), "b134#6": ("category", "統計の区分のコード"),
    "b134#33": ("category", "有無（no）"), "b134#41": ("category", "敬称の決まった語"),
    "b135#14": ("category", "開始の方法のコード"), "b135#57": ("id", "政策目標の番号"),
    "b136#11": ("org", "局（Direktion）の名前・略号（v1.7：役所の略号は org）"),
    "b137#102": ("text", "議案の番号と題名"), "b137#154": ("id", "公開元の識別子（slug）"),
    "b137#96": ("other", "座標（スイスの平面直角座標）"), "b137#97": ("other", "座標（スイスの平面直角座標）"),
    "b137#140": ("category", "系統の区分"), "b137#37": ("category", "出典のコード（GWS・STATPOP）"),
    "b137#53": ("org", "運営の団体・会社"),
    "b137#57": ("text", "設備の羅列"), "b137#58": ("text", "サービスの羅列"), "b137#59": ("text", "空間の種類の羅列"),
    "b137#85": ("org", "データの出典の役所（局・部）"),
    "b137#135": ("category", "件名の分類"), "b137#136": ("category", "件名の分類"), "b137#137": ("category", "件名の分類"),
    "b137#143": ("org", "駅（v1.7・v1.9：駅は org）"), "b137#146": ("org", "駅（v1.7・v1.9：駅は org）"),
    "b137#150": ("org", "局の略号（v1.7）"), "b137#151": ("account", "部署（Dienststelle）の略号"),
    "b137#107": ("category", "投票の方法の区分"),
    "b139#1": ("text", "行動計画の文（どれも違う）"),
    "b142#150": ("amount", "貸付残高の合計（金額）"),
    "b142#170": ("unknown", "単位も文脈も無い 1 行の数"), "b142#173": ("unknown", "単位も文脈も無い 1 行の数"),
    "b142#176": ("unknown", "単位も文脈も無い 1 行の数"), "b142#177": ("unknown", "単位も文脈も無い 1 行の数"),
    "b142#88": ("text", "見どころの説明"), "b142#268": ("text", "運用時間の説明（24h）"),
    "b142#1121": ("address", "管理団体が自治体名だけ（v1.1：自治体名だけの団体名は address）"),
    "b143#547": ("other", "1 世帯あたりの人員（平均＝統計値、v1.4）"),
    "b143#2": ("address", "対象の物件（建物）の名前"),
    "b143#125": ("product", "物品・役務の名前（クリーニング）"),
    "b143#331": ("category", "許可の品目の区分"),
    "b143#442": ("category", "方角（南・北）の区分"),
    "b144#1": ("category", "座標系の区分"), "b144#7": ("category", "座標系の区分"),
    "b145#1": ("category", "座標系の区分"), "b145#7": ("category", "座標系の区分"),
    "b144#83": ("quantity", "人数（調査の回答の数）"),
    "b144#151": ("quantity", "前年との差（人数の増減）"),
    "b144#207": ("category", "重複の有無（0/1）"), "b145#908": ("category", "福祉避難所の有無（1）"),
    "b144#453": ("account", "問い合わせの部署（〇〇室）"), "b145#30": ("account", "問い合わせの部署（〇〇室）"),
    "b144#265": ("address", "営業所の所在地"),
    "b144#8": ("address", "庁舎の名前（見出しがずれた表）"), "b145#2": ("address", "庁舎・センターの名前（見出しがずれた表）"),
    "b145#8": ("address", "庁舎の名前（見出しがずれた表）"),
    "b145#335": ("text", "設備の羅列"), "b145#461": ("text", "設備の羅列"),
    "b145#593": ("address", "方書（番地）"),
    "b143#567": ("text", "備考（指定の状態の記述）"), "b143#1137": ("text", "備考"), "b144#940": ("text", "備考"),
    "b144#1134": ("text", "備考"), "b145#874": ("text", "備考"), "b145#929": ("text", "備考"), "b145#1077": ("text", "備考"),
    "b142#801": ("text", "時間外の対応の説明"),
}


def rule(r):
    t, m, h = r["teacher"], r["model"], r["header"].strip()
    v = [str(x) for x in r["values"]]
    if t == "S":
        return "S", "K1 先生が S（崩れた表・個人名・個人別の記録）"
    if t == "unknown":
        return "unknown", "K2 先生が unknown"
    if m == "unknown":
        return t, "K3 モデルは言い切っていない"
    if (t, m) == ("address", "org") and FAC.match(h):
        return "address", "K4 いろいろな種類の施設の一覧の名前（B10-3）"
    hh = h.replace("\n", "")
    if re.search(r"設置位置", hh):
        return "address", "K5 設置位置（教材庫 80/80）"
    if re.search(r"利用可能曜日", hh):
        return "category", "K5 曜日（LABEL_GUIDE date の欄・教材庫）"
    if hh in ("開始時間", "終了時間"):
        return ("date", "K5 時刻（B8）") if sum(bool(TIME.match(x)) for x in v) * 2 >= len(v) else ("text", "K5 時刻でない説明")
    if hh in ("利用可能時間", "利用可能日時特記事項", "休館日(熱中症特別警戒情報運用期間中)"):
        return "text", "K5 利用時間・休みの日の説明（営業時間の説明は text）"
    if hh == "診療科目":
        return "category", "K5 診療科目（B7）"
    return None


def main():
    tot = {}
    for b in BATCHES:
        w = ROOT / "materials" / "pool" / "work" / b
        out = []
        for line in open(w / "review.jsonl", encoding="utf-8"):
            r = json.loads(line)
            key = f"{b}#{r['i']}"
            if r["kind"] == "audit":
                lab, why = AUDIT_FIX.get(key, (r["teacher"], "抜き取り：先生とモデルの一致を確かめた"))
            elif key in MANUAL:
                lab, why = MANUAL[key]
            else:
                got = rule(r)
                if not got:
                    raise SystemExit(f"未裁定 {key} {r['teacher']} {r['model']} {r['header']!r}")
                lab, why = got
            out.append({"i": r["i"], "label": lab, "reason": why, "by": "claude-20261104"})
        with open(w / "decisions.jsonl", "w", encoding="utf-8") as fh:
            for d in out:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        tot[b] = len(out)
    print(tot)


AUDIT_FIX = {}

if __name__ == "__main__":
    main()
