"""教材庫の施設の名称 2,223 行の裁定（2026-11-04 Claude）。

  python research/facility_names/adjudicate_pool.py CLAUDE.tsv
    CLAUDE.tsv＝`pool_v24.py claude` の出力（SHA は research/labels/facility_v24/claude_answers_sha256.json と照合する）
    ChatGPT の答え＝research/labels/facility_v24/answers_chatgpt.tsv（ブラインド入力 pool_blind_sheet.tsv への独立の答え）
  → research/labels/facility_v24/pool_final.tsv（id・header・label_claude・label_chatgpt・label_final・basis）

決め方：2 人が一致した行はそのまま（basis=agree）。割れた行は、LABEL_GUIDE v2.4 B10 と 386 行のシートの裁定（final.tsv）の先例で決める。
  R1 同じ種類の機関の名簿：機関としての属性（種別・団体名・法人番号・定員・受入年齢・診療科・開設…）が同じ表にあれば org（B10-1）、無ければ address（座標・場所の属性だけの同種の一覧、B10-3）
  R2 団体・会社の名前（町会・自治会・葬儀社など）：org（先例：町会 7/8 が org、葬儀社 org）
  R3 台帳：許可番号・業種・営業の種類・登録番号があれば org（B10-2）。確認番号・確認年月日・営業形態だけ（クリーニング・理容・美容所の届出の確認）は address（先例 b011#1129・b010#1326・b008#1451・b007#2097）
  R4 読み・英字・通称の列：同じ表の名前の列の裁定に合わせる
  MANUAL 規則で決めない行は Claude が 1 行ずつ見て決めた（理由つき）
"""
import csv, json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import pool_v24 as P  # noqa: E402

INST_MORE = re.compile(r"(種別|団体名|法人番号|収容定員|受入年齢)")  # 先例：種別の付く保育所の名簿は org（final.tsv の保育 21 件中 18 件）
LIC_STRONG = re.compile(r"(許可|業種|営業の種類|登録番号|営業種別)")
_LIB = "図書館の一覧は場所（先例：図書館 9/9 が address）"
_SHOP = "店・宿の一覧で許可の台帳ではない（先例 b003#2238・b009#1397 は address）"
_KID = "子ども食堂の一覧（開催頻度・運営団体などの活動の属性。先例：食堂 6/8 が org）"
_MIX = "いろいろな種類の公共施設の一覧（B10-3）"
MANUAL = {
    "b003#448": ("org", "保育所の名簿で受入年齢が付く（B10-1）"),
    "b003#1721": ("address", "列名「場所名称」で値は所在地・保管場所（B10-3）"),
    "b003#3465": ("org", "活動の場・教室の一覧で活動内容・対象者が付く（団体）"),
    "b003#3897": ("address", "施設カテゴリ・施設種別・方書の付くいろいろな種類の施設の案内（B10-3）"),
    "b003#3907": ("address", "施設カテゴリ・施設種別・方書の付くいろいろな種類の施設の案内（B10-3）"),
    "b004#2901": ("address", "施設カテゴリ・施設種別・方書の付くいろいろな種類の施設の案内（B10-3）"),
    "b003#4436": ("org", "排水の届出の責任者（市・郡の部局）＝運営者（B10-4）"),
    "b004#187": ("address", "列名「場所名称」で値は文化財の保管場所（B10-3）"),
    "b004#2221": ("address", "値が空。列名「場所名称」（v1.7・v1.9）"),
    "b012#857": ("address", "値が空。同じ表の名前の列（POI の表）に合わせる"),
    "b004#1546": ("address", _SHOP), "b005#1137": ("address", _SHOP), "b007#453": ("address", _SHOP), "b011#1135": ("address", _SHOP),
    "b007#2282": ("address", _SHOP), "b007#2339": ("address", _SHOP), "b007#2342": ("address", _SHOP), "b007#2345": ("address", _SHOP),
    "b010#1331": ("address", _SHOP), "b011#105": ("address", _SHOP),
    "b004#2362": ("address", _MIX), "b004#2875": ("address", "庁舎（建物）の一覧（B10-3）"), "b005#1855": ("address", _MIX + "、X・Y が付く"),
    "b006#1473": ("address", "市役所・支所の一覧で X・Y だけが付く（B10-3 の座標だけの同種の一覧）"),
    "b007#1768": ("address", _MIX + "（市役所・郵便局。設置者は別の列）"), "b010#64": ("address", _MIX), "b012#964": ("address", _MIX + "、施設区分が付く"),
    "b005#2031": ("org", "地域包括支援センターの名簿で団体名・説明が付く（B10-1）"),
    "b005#2075": ("org", "こども園の名簿で種別・認可年月日が付く（B10-1）"),
    "b007#311": ("org", "こども園の名簿で種別が付く（B10-1）"),
    "b007#510": ("org", "駅の一覧（v1.7・v1.9 の例：駅は org）"),
    "b008#176": ("address", "動物園・水族館は訪れる場所（v1.7 の観光地）"),
    "b008#481": ("address", _LIB), "b009#1394": ("address", _LIB), "b011#1115": ("address", _LIB), "b011#1172": ("address", _LIB),
    "b008#801": ("org", "教育の提供者（Provider）の名前（同じ表に Site Code・所在地が別にある）"),
    "b009#1313": ("org", "審議会・委員会の一覧（組織）"),
    "b012#1815": ("org", "サークル・同好会の一覧で活動内容が付く（団体）"),
    "b012#1823": ("org", "葬儀社の一覧（会社）"),
    "b016#6": ("org", "警察本部の一覧（v1.7 の例：消防署は org）"),
    "b055#54": ("address", "貸しスペース・ワークスペースの一覧で営業時間・アクセスが付く（v1.9 スペース名称）"),
    "b007#2263": ("org", _KID), "b010#432": ("org", _KID), "b010#1507": ("org", _KID), "b010#1517": ("org", _KID),
    "b011#278": ("org", _KID), "b011#307": ("org", _KID), "b011#322": ("org", _KID), "b011#332": ("org", _KID),
    "b011#352": ("org", _KID), "b011#1376": ("org", _KID), "b012#1741": ("org", _KID), "b012#1785": ("org", _KID),
}


def read(p, key="id"):
    return {r[key]: r for r in csv.DictReader(open(p, encoding="utf-8"), delimiter="\t")}


def main():
    cl = read(sys.argv[1])
    gp = read(os.path.join(ROOT, "research", "labels", "facility_v24", "answers_chatgpt.tsv"))
    tg = P.targets()
    keys = sorted(tg, key=lambda k: (tg[k][0][0], tg[k][0][1]))
    idk = {f"{tg[k][0][0][6:-6]}#{tg[k][0][1]}": k for k in keys}
    assert set(idk) == set(cl) == set(gp), "id の集合が合わない"
    # 386 行のシートで決めた名前の列（読みの列の元）
    fin = read(os.path.join(HERE, "final.tsv"))
    per_table = {}
    for f, i, r in P.pool_rows():
        lab = fin.get(f"{f[6:-6]}#{i}")
        if lab:
            per_table[(r["table"], P.norm(r["header"]))] = lab["label_final"]
    out = {}
    order = sorted(idk, key=lambda i: bool(P.READING.search(idk[i][1])))  # 名前の列を先に
    for i in order:
        k = idk[i]; c = cl[i]["label_v24"]; g = gp[i]["label"]
        _, _, r = tg[k][0]
        ctx = " ".join(str(x) for x in r.get("context", []))
        if c == g:
            out[i] = (c, "agree")
            continue
        if i in MANUAL:
            out[i] = MANUAL[i]
            continue
        why = cl[i]["reason"]
        if P.READING.search(k[1]):
            base = (k[0], P.base_header(k[1]))
            ids = [j for j, kk in idk.items() if kk == base]
            if ids and ids[0] in out:
                out[i] = (out[ids[0]][0], f"R4 同じ表の名前の列（{ids[0]}）に合わせる")
                continue
            if base in per_table:
                out[i] = (per_table[base], "R4 同じ表の名前の列（386 行のシートの裁定）に合わせる")
                continue
            out[i] = (None, "未裁定：読みの列で元の列が見つからない")
            continue
        if "B10-1" in why:
            out[i] = ("org", "R1 機関の属性が付く同種の名簿（B10-1）") if (P.INST_C.search(ctx) or INST_MORE.search(ctx)) else ("address", "R1 機関の属性が無い同種の一覧（B10-3）")
        elif "B10-4" in why:
            out[i] = ("org", "R2 団体・会社の名前（先例）")
        elif "B10-2" in why:
            out[i] = ("org", "R3 許可・登録の台帳（B10-2）") if LIC_STRONG.search(ctx) else ("address", "R3 届出の確認だけの台帳（先例）")
        else:
            out[i] = (None, "未裁定")
    left = [i for i in out if out[i][0] is None]
    if left:
        for i in left:
            print("未裁定", i, idk[i][1], cl[i]["label_v24"], gp[i]["label"], cl[i]["reason"])
        sys.exit(1)
    path = os.path.join(ROOT, "research", "labels", "facility_v24", "pool_final.tsv")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["id", "header", "label_now", "label_claude", "label_chatgpt", "label_final", "basis"])
        for k in keys:
            f, n, r = tg[k][0]
            i = f"{f[6:-6]}#{n}"
            w.writerow([i, k[1], r["label"], cl[i]["label_v24"], gp[i]["label"], out[i][0], out[i][1]])
    dis = [i for i in out if out[i][1] != "agree"]
    print("rows", len(out), "agree", len(out) - len(dis), "adjudicated", len(dis))
    print("final", Counter(v[0] for v in out.values()))
    print("winner", Counter("claude" if out[i][0] == cl[i]["label_v24"] else "chatgpt" if out[i][0] == gp[i]["label"] else "neither" for i in dis))
    print("basis", Counter(out[i][1].split(" ")[0] if out[i][1].startswith("R") else "MANUAL" for i in dis))


if __name__ == "__main__":
    main()
