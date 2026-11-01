"""教材庫の全部の施設・場所の名前の列を LABEL_GUIDE v2.4 B10 で付け直すための材料（2026-11-01 Claude、オーナー「やれ」）。

  python research/facility_names/pool_v24.py sheet     → pool_sheet.tsv（ラベルなし。先生 2 人が独立に答える）
  python research/facility_names/pool_v24.py claude OUT → Claude の答えの下書き（B10 を規則にしたもの）を OUT に書く
                                                         （Claude が全部の行を見直してから SHA を固定する。ChatGPT の答えのあとでリポジトリに置く）

対象：materials/pool/batch_*.jsonl のうち、名前の列（collect.py の HEAD・NOT）と、その読み・英字・通称の列で、今のラベルが org・address・unknown のもの。
386 行のシート（sheet.tsv、裁定済み final.tsv）に入っている表・列名は外す。同じ表・同じ列名の行は 1 行にまとめる（付け直しは全部の行に当てる）。
"""
import csv, glob, json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from collect import HEAD, NOT, KEEP  # noqa: E402

READING = re.compile(r"(カナ|かな|ｶﾅ|フリガナ|ふりがな|よみ|読み|英字|英語|ローマ字|_en$|通称)", re.I)
# B10-2 営業許可・登録の台帳
LIC = re.compile(r"(許可|業種|営業の種類|業務種別|登録番号|営業種別|届出|確認年月日|確認番号|確認通知書)")
# B10-1 同じ種類の機関（値の語）と、機関としての属性（同じ表の列）
INST_V = re.compile(r"(保育|こども園|幼稚園|医院|クリニック|病院|歯科|診療所|学童|児童クラブ|小学校|中学校|高等学校|高校|大学|学院|特別支援学校|整骨院|接骨院|鍼灸|治療院|薬局|介護|デイサービス|ケアプラン|訪問看護|老人ホーム|グループホーム)")
INST_C = re.compile(r"(医療機関の種類|診療科|診療科目|病床|定員|受入年齢|対象年齢|収容定員|サービス種類|サービス種別|実施サービス|事業所番号|学校種別|学校ID|設置主体|開設者|開設年月日|認可|保育施設種別|延長保育|一時預かり|内科|歯科|小児科)")
# B10-3 場所の属性（同じ表の列）
LOC_C = re.compile(r"(POI|設置位置|緯度|経度|^X$|^Y$|座標|災害種別|投票区|SSID|町字ID|バリアフリー|利用可能曜日|利用可能時間|標高|収容人数|想定収容|避難|高度の種別|駐車場|トイレ|AED|Wi-?Fi|開館|開庁|休館|設備|所在地|住所)", re.I)
# 場所として使う一覧（避難所・投票所・AED や Wi-Fi の設置・おむつ替え）の印。機関の名簿の印より先に見る
USE_LOC = re.compile(r"(洪水|津波|高潮|崖崩れ|土砂|設置位置|設置箇所|SSID|提供エリア|災害種別|避難|投票|AED|小児対応|おむつ|授乳|赤ちゃんの駅|収容人数|想定収容)", re.I)
# 組織の名前らしい値
ORG_V = re.compile(r"(株式会社|有限会社|合同会社|（株）|\(株\)|㈱|（有）|\(有\)|㈲|法人|町会|町内会|自治会|協議会|組合|連合会|青年会|クラブ|サークル|の会$|協会|財団|商店|商会)")
# 場所そのものの名前（公園・広場など。v1.7・v1.9 の例）
PLACE_V = re.compile(r"(体育館|グランド|グラウンド|校庭|屋外運動場|倉庫|足湯|公園|広場|緑地|グラウンド|運動場|海水浴場|史跡|橋$|神社|寺|団地|住宅|ダム|トイレ|待合所|展望|駐輪場|駐車場|停留所|バス停|ポート|会議室|和室|ホール|体育室|集会所|避難|高台|空き地)")
# いろいろな種類の施設（語尾の種類の数で見る。公共施設の一覧は場所の一覧＝B10-3）
KINDS = [("役所", r"(役所|役場|庁舎|支所|出張所)"), ("学校", r"(小学校|中学校|高等学校|学校)$"), ("公民館", r"(公民館|集会所|会館|コミュニティ|センター)"),
         ("体育", r"(体育館|グラウンド|運動場|テニスコート|プール|競技場|武道館)"), ("公園", r"(公園|広場|緑地)"), ("図書館", r"(図書館|資料館|博物館|美術館|文化)"),
         ("保育", r"(保育|こども園|幼稚園|児童館|児童センター|学童)"), ("福祉", r"(福祉|老人|デイ|介護)"), ("医療", r"(病院|診療所|医院|クリニック|保健)"),
         ("駅", r"(駅|ターミナル|港)"), ("消防", r"(消防|警察|交番)"), ("史跡", r"(史跡|跡$|神社|寺$)"), ("住宅", r"(住宅|団地)"), ("浄水", r"(浄水場|処理場|ポンプ場|清掃)")]
FIXED = [  # 列名だけで決まるもの
    (re.compile(r"(スペース名称|停留所|投票所|投票区|設置場所|場所名称|駐輪場|防災行政無線|赤ちゃんの駅|公園名称|公衆トイレ)"), "address", "列名が場所を指す（v1.7・v1.9、B10-3）"),
    (re.compile(r"(姉妹都市|友好都市|国の名称)"), "address", "都市・国の名前（種類の表：区域の名前は address）"),
    (re.compile(r"(介護サービス事業所名称|事業所名称|学校名称|施術所名称|美容所の名称|理容所の名称)"), "org", "列名が機関・事業所を指す（B10-1・B10-2）"),
]


# 規則で決めきれなかった行を Claude が手で見て決めたもの（それ以外の保留は今のラベルのまま）
_A = "公民館・コミュニティセンター・ホールの一覧は会場・建物（B10-3、案の例「公民館」）"
MANUAL = {
    "b006#1434": ("address", "配水池・ポンプ所・水源地は設備の場所（B10-3）"),
    "b004#2697": ("address", "クリーンセンター・環境センターは処理施設の場所（B10-3）"),
    "b004#2925": ("address", _A), "b007#1752": ("address", _A), "b007#2348": ("address", _A), "b006#1467": ("address", _A),
    "b005#1012": ("address", _A), "b007#2656": ("address", _A),
    "b006#925": ("address", "海水浴場・園・温泉など訪れる場所（v1.7、B10-3）"),
    "b012#1726": ("address", _A), "b012#35": ("address", _A), "b012#55": ("address", _A), "b010#1719": ("address", _A),
    "b008#906": ("address", "ごみの処分場・中継所は場所（B10-3）"), "b012#395": ("address", "プールは訪れる場所（B10-3）"),
    "b008#176": ("address", "動物園・水族館は訪れる場所（v1.7 の観光地、B10-3）"),
}


def pool_rows():
    for p in sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl"))):
        f = os.path.basename(p)
        for i, line in enumerate(open(p, encoding="utf-8")):
            r = json.loads(line)
            yield f, i, r


def norm(h):
    return str(h).replace("\n", " ").strip()


def base_header(h):
    """読み・英字・通称の列 → 元の名前の列名の候補（名称_カナ → 名称）。"""
    b = re.sub(r"[_＿（(]?(カナ|かな|ｶﾅ|フリガナ|ふりがな|よみ|読み|英字|英語|ローマ字|通称)[）)]?.*$", "", h)
    b = re.sub(r"[\s_＿]+$", "", b)
    return b or h


def targets():
    done = {(r["table"], norm(r["header"])) for r in _sheet_keys()}
    tables = {}
    for f, i, r in pool_rows():
        tables.setdefault(r["table"], []).append((f, i, r))
    out = {}
    for table, rows in tables.items():
        heads = {norm(r["header"]) for _, _, r in rows}
        for f, i, r in rows:
            h = norm(r["header"])
            if r.get("label") not in KEEP:
                continue
            is_name = HEAD.search(h) and not NOT.search(h)
            is_read = READING.search(h) and HEAD.search(base_header(h)) and base_header(h) in heads
            if not (is_name or is_read):
                continue
            key = (table, h)
            if key in done:
                continue
            out.setdefault(key, []).append((f, i, r))
    return out


def _sheet_keys():
    """386 行のシートの教材の行（表・列名）。"""
    ids = {x["id"] for x in csv.DictReader(open(os.path.join(HERE, "sheet.tsv"), encoding="utf-8"), delimiter="\t") if x["set"] == "train"}
    for f, i, r in pool_rows():
        if f"{f[6:-6]}#{i}" in ids:
            yield r


def sheet_line(key, group):
    f, i, r = group[0]
    vals = [str(v) for v in (r.get("row_values") or r["values"])][:12]
    ctx = [str(x) for x in r.get("context", [])]
    return [f"{f[6:-6]}#{i}", key[1], " | ".join(v[:30] for v in vals), ", ".join(c[:20] for c in ctx[:16]), r.get("label", ""), str(len(group))]


def decide(h, vals, ctx, now, table_answers):
    """B10 を規則にした Claude の下書き。戻り値 (ラベル, 理由)。決めきれないときは今のラベルのまま（理由に「保留」）。"""
    if READING.search(h) and base_header(h) in table_answers:
        return table_answers[base_header(h)][0], "読み・英字・通称の列は同じ表の名前の列に合わせる"
    for pat, lab, why in FIXED:
        if pat.search(h):
            return lab, why
    vals = [v for v in vals if str(v).strip() and str(v).strip() not in ("nan", "None", "-")]
    c = " ".join(ctx)
    kinds = {k for v in vals for k, pat in KINDS if re.search(pat, v)}
    lic = bool(LIC.search(c))
    inst_v = sum(bool(INST_V.search(v)) and not PLACE_V.search(v) for v in vals)
    org_v = sum(bool(ORG_V.search(v)) for v in vals)
    place_v = sum(bool(PLACE_V.search(v)) for v in vals)
    n = max(len(vals), 1)
    inst_c = bool(INST_C.search(c))
    loc_c = bool(LOC_C.search(c))
    if lic:
        return "org", "営業許可・登録の台帳の店名（B10-2）"
    if org_v >= 0.6 * n:
        return "org", "値の多くが団体・会社の名前（B10-4）"
    if USE_LOC.search(c):
        return "address", "避難所・投票所・設置場所など場所として使う一覧（B10-3）"
    if len(kinds) >= 3 and not inst_c:
        return "address", f"いろいろな種類の施設が並ぶ一覧（{len(kinds)} 種類、B10-3）"
    if place_v >= 0.5 * n:
        return "address", "値の多くが場所そのものの名前（体育館・校庭・公園など、v1.7、B10-3）"
    if inst_v >= 0.6 * n:
        return "org", "同じ種類の機関の名簿（B10-1）"
    if loc_c and not inst_c:
        return "address", "いろいろな施設の一覧で場所の属性が付く（B10-3）"
    if len(kinds) >= 3 and not inst_c:
        return "address", f"いろいろな種類の施設が並ぶ一覧（{len(kinds)} 種類、B10-3）"
    if place_v >= 0.6 * n:
        return "address", "値の多くが場所そのものの名前（v1.7、B10-3）"
    if inst_v >= 0.6 * n and inst_c:
        return "org", "同じ種類の機関の名簿（B10-1）"
    return now, "保留：規則で決めきれない（今のラベルのまま、手で見る）"


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "sheet"
    tg = targets()
    keys = sorted(tg, key=lambda k: (tg[k][0][0], tg[k][0][1]))
    if cmd == "sheet":
        with open(os.path.join(HERE, "pool_sheet.tsv"), "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(["id", "header", "values", "same_table_columns", "label_now", "rows", "label_v24", "reason"])
            for k in keys:
                line = sheet_line(k, tg[k])
                w.writerow(line[:6] + ["", ""])
        print(len(keys), "keys", sum(len(v) for v in tg.values()), "rows", Counter(tg[k][0][2]["label"] for k in keys))
    elif cmd == "claude":
        out = sys.argv[2]
        per_table = {}
        # 386 行のシートで決めた名前の列（final.tsv）を、同じ表の読みの列の元にする
        fin = {x["id"]: x["label_final"] for x in csv.DictReader(open(os.path.join(HERE, "final.tsv"), encoding="utf-8"), delimiter="\t")}
        for f, i, r in pool_rows():
            lab = fin.get(f"{f[6:-6]}#{i}")
            if lab:
                per_table.setdefault(r["table"], {})[norm(r["header"])] = (lab, "386 行のシートの裁定")
        # 名前の列を先に、読みの列を後に決める
        order = sorted(keys, key=lambda k: bool(READING.search(k[1])))
        ans = {}
        for k in order:
            f, i, r = tg[k][0]
            vals = [str(v) for v in (r.get("row_values") or r["values"])]
            ctx = [str(x) for x in r.get("context", [])]
            ta = per_table.setdefault(k[0], {})
            lab, why = decide(k[1], vals, ctx, r["label"], ta)
            cid = f"{f[6:-6]}#{i}"
            if cid in MANUAL:
                lab, why = MANUAL[cid]
            ta[k[1]] = (lab, why)
            ans[k] = (lab, why)
        with open(out, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(["id", "header", "label_now", "label_v24", "reason"])
            for k in keys:
                f, i, r = tg[k][0]
                w.writerow([f"{f[6:-6]}#{i}", k[1], r["label"], ans[k][0], ans[k][1]])
        c = Counter((tg[k][0][2]["label"], ans[k][0]) for k in keys)
        print(sorted(c.items()), "hold", sum("保留" in ans[k][1] for k in keys))


if __name__ == "__main__":
    main()
