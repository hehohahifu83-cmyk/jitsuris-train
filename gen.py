"""学習用データの合成（評価用の公開資料とは別に、一般的な業務の言葉から作る）。個人情報は含まない（値はすべて作り物）。
列名は「核になる言葉」に、前後の飾り（借方/貸方、税込/税抜、(円)、必須、番号の添字、英語の書き方の揺れ）を組み合わせて作る。
"""
import random
import string

CLASSES = ["date", "amount", "quantity", "rate", "id", "org", "person", "product", "account", "tax_class",
           "text", "category", "email", "phone", "address"]

CORE = {
    "date": ["日付", "年月日", "注文日", "受注日", "購入日", "売上日", "計上日", "入金日", "出金日", "支払日", "支払期限", "請求日",
             "納品日", "発送日", "出荷日", "到着日", "締め日", "締日", "伝票日付", "取引年月日", "利用日", "ご利用日", "精算日",
             "登録日", "更新日", "作成日", "削除日", "キャンセル日", "返品日", "決済日時", "注文日時", "受付日時", "登録日時",
             "更新日時", "処理日時", "日時", "時刻", "会計日時", "来店日", "予約日", "開始日", "終了日", "有効期限", "振込日",
             "引落日", "記帳日", "入荷日", "Date", "Order Date", "Created", "Updated", "Timestamp", "Time", "Paid Date",
             "Shipped At", "Ordered At", "Updated At", "Deleted At", "Due Date", "Invoice Date", "Transaction Date", "date", "created_at", "updated_at"],
    "amount": ["金額", "合計", "合計金額", "小計", "総額", "売上", "売上金額", "売上高", "請求金額", "支払金額", "入金額", "出金額",
               "振込金額", "利用金額", "ご利用金額", "税込金額", "税抜金額", "消費税", "消費税額", "内税", "外税", "送料", "手数料",
               "決済手数料", "値引", "値引額", "割引額", "ポイント利用額", "クーポン値引", "単価", "販売価格", "定価", "原価", "仕入価格",
               "残高", "差引残高", "預り金", "お預かり", "お釣り", "粗利", "利益", "返金額", "立替金", "Amount", "Price", "Unit Price",
               "Total Price", "Grand Total", "Sub Total", "Tax", "Tax Amount", "Fee", "Shipping Fee", "Discount", "Balance", "Cost",
               "Revenue", "Net Sales", "Gross Sales", "amount", "price", "total"],
    "quantity": ["数量", "個数", "点数", "件数", "口数", "本数", "枚数", "冊数", "人数", "回数", "在庫数", "入数", "注文数", "出荷数",
                 "発注数", "受注数", "返品数", "入荷数", "販売数", "数", "Qty", "Quantity", "Count", "Units", "Stock", "Pieces", "qty"],
    "rate": ["税率", "消費税率", "割引率", "値引率", "掛率", "利益率", "粗利率", "達成率", "構成比", "前月比", "前年比", "成長率",
             "手数料率", "ポイント率", "還元率", "%", "Tax Rate", "Rate", "Percent", "Ratio", "Margin %", "rate"],
    "id": ["番号", "ID", "No", "No.", "コード", "注文番号", "注文ID", "受注ID", "伝票番号", "伝票No", "請求書番号", "請求番号",
           "領収書番号", "取引ID", "取引番号", "会員番号", "会員ID", "顧客番号", "顧客ID", "顧客コード", "得意先コード", "仕入先コード",
           "商品コード", "商品ID", "品番", "型番", "JANコード", "JAN", "SKU", "バーコード", "管理コード", "社員番号", "店舗コード",
           "レシート番号", "問い合わせ番号", "追跡番号", "送り状番号", "予約番号", "口座番号", "登録番号", "インボイス番号", "整理番号",
           "Order ID", "Order Number", "Invoice No", "Customer ID", "Product ID", "Item Code", "Transaction ID", "Reference", "Tracking Number",
           "UUID", "id", "order_id", "sku"],
    "org": ["Payee", "Payer", "Sold-to Party", "Ship-to Party", "Bill-to Party", "Business Partner", "Counterparty", "Organization",
            "Sales Organization", "Customer Account", "Vendor Account Name", "Legal Entity", "Subsidiary", "取引先", "取引先名", "会社名", "法人名", "社名", "屋号", "店名", "店舗名", "店舗", "得意先", "得意先名", "仕入先", "仕入先名",
            "請求先", "支払先", "振込先", "納品先", "販売元", "メーカー", "ブランド", "運送会社", "配送業者", "銀行名", "金融機関",
            "支店", "支店名", "加盟店名", "利用店名", "ご利用店名", "Company", "Company Name", "Vendor", "Supplier", "Merchant", "Store",
            "Shop", "Bank", "Branch", "Carrier", "Brand", "company", "vendor"],
    "person": ["氏名", "名前", "お名前", "姓", "名", "フリガナ", "氏名（カナ）", "担当者", "担当者名", "担当", "購入者", "購入者名",
               "注文者", "注文者名", "受取人", "お届け先氏名", "送り主", "依頼人", "振込依頼人", "顧客名", "会員名", "作業者",
               "入力者", "承認者", "登録者", "更新者", "スタッフ", "Name", "Full Name", "First Name", "Last Name", "Customer Name",
               "Contact", "Staff", "Owner", "Created By", "Updated By", "Recipient", "customer_name"],
    "product": ["Material", "Material Description", "Article", "Goods", "Item Description", "商品名", "品名", "商品", "品目", "品目名", "アイテム", "アイテム名", "メニュー", "メニュー名", "サービス名", "プラン名",
                "銘柄", "銘柄名", "部品名", "製品名", "型式", "商品タイトル", "タイトル", "内容品", "Product", "Product Name", "Item",
                "Item Name", "Title", "Description of goods", "Service", "Menu", "product_name", "item"],
    "account": ["勘定科目", "科目", "補助科目", "科目名", "勘定科目名", "部門", "部門名", "部署", "費目", "経費科目", "セグメント",
                "プロジェクト", "コストセンター", "口座", "入金口座", "出金口座", "決済口座", "Account", "Account Title", "Subaccount",
                "Department", "Cost Center", "Ledger Account", "GL Account"],
    "tax_class": ["税区分", "消費税区分", "課税区分", "税コード", "税率区分", "インボイス", "適格請求書", "インボイス区分", "課税/非課税",
                  "内税/外税", "税計算", "税処理", "軽減税率", "Tax Class", "Tax Code", "Tax Category", "VAT Code", "Taxable"],
    "text": ["摘要", "備考", "メモ", "コメント", "内容", "明細", "説明", "詳細", "注記", "特記事項", "連絡事項", "お問い合わせ内容",
             "取引内容", "ご利用内容", "利用内容", "件名", "用途", "理由", "Note", "Notes", "Memo", "Comment", "Description", "Remarks",
             "Details", "Message", "note", "memo", "description"],
    "category": ["区分", "種別", "種類", "分類", "カテゴリ", "カテゴリー", "ステータス", "状態", "状況", "フラグ", "タイプ", "支払方法",
                 "決済方法", "支払い方法", "配送方法", "配送区分", "入出金区分", "取引区分", "売上区分", "会員ランク", "性別", "通貨",
                 "チャネル", "経路", "販売チャネル", "ラベル", "タグ", "有効", "無効", "公開", "対応状況", "発送状況", "入金状況",
                 "Status", "Type", "Category", "Kind", "Flag", "Payment Method", "Shipping Method", "Channel", "Currency", "Label",
                 "Tag", "Tags", "Gender", "Rank", "Enabled", "Active", "status", "type"],
    "email": ["メール", "メールアドレス", "Eメール", "E-mail", "mail", "連絡先メール", "Email", "Email Address", "e-mail", "email"],
    "phone": ["電話", "電話番号", "TEL", "Tel", "携帯", "携帯番号", "連絡先電話", "FAX", "Fax", "Phone", "Phone Number", "Mobile",
              "Telephone", "tel", "phone"],
    "address": ["住所", "所在地", "住所1", "住所2", "番地", "建物名", "都道府県", "市区町村", "郵便番号", "〒", "お届け先住所",
                "送付先住所", "請求先住所", "Address", "Address Line 1", "Address Line 2", "City", "State", "Prefecture", "Zip",
                "Zip Code", "Postal Code", "Country", "Region", "Street", "address", "zip"],
}

PREFIX = {"": 8, "借方": 1, "貸方": 1, "お届け先": 1, "請求先": 1, "配送先": 1, "購入者": 1, "注文": 1, "商品": 1, "元": 0.5,
          "前回": 0.5, "今回": 0.5, "最終": 0.5, "Billing ": 0.6, "Shipping ": 0.6, "Customer ": 0.6, "Order ": 0.6, "Item ": 0.6}
SUFFIX = {"": 10, "(円)": 1, "（円）": 1, "（税込）": 0.7, "(税抜)": 0.7, "1": 0.6, "2": 0.6, "_1": 0.3, "（必須）": 0.4,
          "*": 0.3, "名": 0.3, " ": 0.2, "（任意）": 0.3}
PREFIX_FOR = {"amount": ["借方", "貸方"], "account": ["借方", "貸方"], "tax_class": ["借方", "貸方"], "org": ["借方", "貸方", "請求先", "配送先"],
              "person": ["お届け先", "請求先", "配送先", "購入者", "注文", "Billing ", "Shipping ", "Customer "],
              "address": ["お届け先", "請求先", "配送先", "購入者", "Billing ", "Shipping ", "Customer "],
              "phone": ["お届け先", "請求先", "配送先", "購入者", "Billing ", "Shipping ", "Customer "],
              "email": ["購入者", "注文", "Customer ", "Billing "], "date": ["注文", "最終", "前回", "今回", "Order ", "Item "],
              "id": ["注文", "商品", "元", "Order ", "Item ", "Customer "], "quantity": ["注文", "商品", "Item ", "Order "],
              "product": ["注文", "Item ", "Order "], "category": ["注文", "商品", "Order ", "Item "], "text": ["注文", "商品", "Order "],
              "rate": ["商品", "Item "]}


def weighted(rng, d):
    keys = list(d)
    return rng.choices(keys, weights=[d[k] for k in keys])[0]


def vary_case(rng, s):
    if not any(c.isascii() and c.isalpha() for c in s):
        return s
    r = rng.random()
    if r < 0.25:
        return s.lower()
    if r < 0.35:
        return s.upper()
    if r < 0.5:
        return s.lower().replace(" ", "_")
    if r < 0.6:
        parts = s.split(" ")
        return parts[0].lower() + "".join(p[:1].upper() + p[1:] for p in parts[1:])
    return s


def to_fullwidth(rng, s):
    if rng.random() < 0.08:
        return "".join(chr(ord(c) + 0xFEE0) if "!" <= c <= "~" else c for c in s)
    return s


def header(rng, cls):
    core = rng.choice(CORE[cls])
    pre = rng.choice(PREFIX_FOR.get(cls, [""])) if rng.random() < 0.25 else ""
    # どの種類にも付きうる飾り（飾りだけで種類を覚えないように）
    if not pre and rng.random() < 0.2:
        pre = rng.choice(["Item ", "Line ", "Order ", "Customer ", "Product ", "注文", "明細", "商品", "顧客", "元", "新", "旧", "合計"]) if cls not in ("email", "phone") else ""
    suf = weighted(rng, SUFFIX)
    if cls not in ("amount",) and suf in ("(円)", "（円）", "（税込）", "(税抜)"):
        suf = ""
    h = pre + core + suf
    if rng.random() < 0.05:
        h = "[" + h + "]"
    return to_fullwidth(rng, vary_case(rng, h)).strip()


# ---------- 値の合成（作り物。実在の人・会社・住所ではない） ----------
KANJI_FAMILY = ["佐藤", "鈴木", "高橋", "田中", "伊藤", "渡辺", "山本", "中村", "小林", "加藤", "吉田", "山田", "松本", "井上", "木村"]
KANJI_GIVEN = ["太郎", "花子", "一郎", "陽子", "健", "美咲", "翔", "結衣", "大輔", "さくら"]
KANA_FAMILY = ["サトウ", "スズキ", "タカハシ", "タナカ", "ヤマダ"]
ORG_STEM = ["さくら", "あおば", "ひかり", "みらい", "東西", "南北", "中央", "第一", "丸山", "大和", "青空", "北斗", "日の出", "ミナト", "サンライズ"]
ORG_KIND = ["株式会社", "有限会社", "合同会社", "(株)", "㈱", "商店", "工業", "物産", "食品", "銀行", "信用金庫", "運輸", "ストア", "Inc.", "LLC"]
PRODUCTS = ["Tシャツ", "コーヒー豆 200g", "ノート A5", "ボールペン 黒", "ハンドクリーム", "トートバッグ", "マグカップ", "お米 5kg",
            "ワイヤレスイヤホン", "USBケーブル 1m", "ランチセット", "カット", "月額プラン", "Sticker Pack", "Hoodie - L", "Gift Card"]
ACCOUNTS = ["売上高", "仕入高", "消耗品費", "旅費交通費", "通信費", "支払手数料", "広告宣伝費", "普通預金", "現金", "売掛金", "買掛金",
            "未払金", "地代家賃", "水道光熱費", "外注費", "雑費", "会議費", "接待交際費", "営業部", "本社", "Sales", "Cash"]
TAX = ["課税売上10%", "課税売上8%（軽減）", "対象外", "非課税", "課対仕入10%", "課税仕入 8%（軽）", "免税", "不課税", "適格", "非適格",
       "区分記載", "内税", "外税", "10%", "8%(軽)"]
TEXTS = ["事務用品の購入", "3月分 利用料", "振込手数料", "ネット注文 #1023", "交通費（打合せ）", "返品対応", "サンプル送付", "備考なし",
         "ﾌﾘｺﾐ ｻｸﾗｼﾖｳｼﾞ", "カード ご利用分", "Thanks for your order", "gift wrapping please", "午前中指定", "要確認", ""]
CATS = {"支払": ["クレジットカード", "銀行振込", "代金引換", "コンビニ払い", "PayPay", "現金"], "状態": ["未発送", "発送済み", "キャンセル", "入金待ち", "完了"],
        "区分": ["入金", "出金", "売上", "返品", "通常", "予約"], "en": ["paid", "pending", "refunded", "fulfilled", "unfulfilled", "yes", "no", "TRUE", "FALSE"],
        "通貨": ["JPY", "USD"], "記号": ["A", "B", "C", "1", "0", "○", "×"],
        "コード": ["0", "1", "2"], "コード2": ["1", "2", "3", "9"], "コード3": ["10", "20", "30"], "真偽": ["true", "false"]}
PREFS = ["東京都", "大阪府", "北海道", "福岡県", "愛知県", "神奈川県", "京都府", "沖縄県"]
CITIES = ["中央区", "北区", "港区", "西区", "みどり市", "さくら町", "青葉区"]


def fmt_amount(rng, v):
    style = rng.random()
    neg = rng.random() < 0.08
    if style < 0.35:
        s = str(v)
    elif style < 0.65:
        s = f"{v:,}"
    elif style < 0.75:
        s = f"¥{v:,}"
    elif style < 0.82:
        s = f"{v:,}円"
    elif style < 0.9:
        s = f"{v}.00"
    else:
        s = f"\\{v:,}"
    if neg:
        s = rng.choice(["-", "▲", "△"]) + s
    return s


def value(rng, cls, ctx):
    r = rng.random
    if cls == "date":
        y, m, d = rng.randint(2019, 2026), rng.randint(1, 12), rng.randint(1, 28)
        hh, mm, ss = rng.randint(0, 23), rng.randint(0, 59), rng.randint(0, 59)
        f = ctx.setdefault("date_fmt", rng.randrange(10))
        return [f"{y}/{m:02d}/{d:02d}", f"{y}-{m:02d}-{d:02d}", f"{y}年{m}月{d}日", f"{y}/{m}/{d}", f"{y}{m:02d}{d:02d}",
                f"{y}-{m:02d}-{d:02d} {hh:02d}:{mm:02d}:{ss:02d}", f"{y}/{m:02d}/{d:02d} {hh:02d}:{mm:02d}",
                f"{y}-{m:02d}-{d:02d}T{hh:02d}:{mm:02d}:{ss:02d}+09:00", f"R{y-2018}.{m}.{d}", f"{m}/{d}/{y}"][f]
    if cls == "amount":
        scale = ctx.setdefault("amount_scale", rng.choice([10, 100, 1000, 10000, 100000, 1000000]))
        return fmt_amount(rng, int(abs(rng.lognormvariate(0, 1)) * scale) // 10 * 10)
    if cls == "quantity":
        return str(rng.choice([1, 1, 1, 2, 2, 3, 4, 5, 6, 10, 12, 20, 24, 100])) + (rng.choice(["", "", "個", "点"]) if r() < 0.1 else "")
    if cls == "rate":
        f = ctx.setdefault("rate_fmt", rng.randrange(4))
        v = rng.choice([8, 10, 5, 3, 0, 12.5, 30, 45.2])
        return [f"{v}%", f"{v / 100:.2f}", f"{v}", f"{v}％"][f]
    if cls == "id":
        f = ctx.setdefault("id_fmt", rng.randrange(8))
        n = rng.randint(1, 99999999)
        return [f"{n:08d}", f"#{1000 + n % 9000}", f"A{n % 100000:05d}", f"ORD-{n % 1000000:06d}", f"49{n:011d}"[:13],
                "".join(rng.choices(string.ascii_uppercase + string.digits, k=10)), str(n % 100000), f"{n % 10000:04d}-{n % 1000:03d}"][f]
    if cls == "org":
        return rng.choice([rng.choice(ORG_KIND) + rng.choice(ORG_STEM), rng.choice(ORG_STEM) + rng.choice(ORG_KIND),
                           rng.choice(ORG_STEM) + rng.choice(["店", "支店", "本店", "銀行"]), "ｶ)" + rng.choice(["ｻｸﾗ", "ﾋｶﾘ", "ﾐﾗｲ"])])
    if cls == "person":
        return rng.choice([rng.choice(KANJI_FAMILY) + " " + rng.choice(KANJI_GIVEN), rng.choice(KANJI_FAMILY) + rng.choice(KANJI_GIVEN),
                           rng.choice(KANA_FAMILY) + " " + rng.choice(["タロウ", "ハナコ"]), rng.choice(["Taro Yamada", "Hanako Sato", "Ken Ito"])])
    if cls == "product":
        return rng.choice(PRODUCTS)
    if cls == "account":
        return rng.choice(ACCOUNTS)
    if cls == "tax_class":
        return rng.choice(TAX)
    if cls == "text":
        return rng.choice(TEXTS)
    if cls == "category":
        pool = ctx.setdefault("cat_pool", rng.choice(list(CATS.values())))
        return rng.choice(pool)
    if cls == "email":
        return rng.choice(["info", "sales", "taro.y", "hanako", "shop"]) + str(rng.randint(1, 99)) + "@example." + rng.choice(["com", "jp", "co.jp"])
    if cls == "phone":
        a, b, c = rng.randint(10, 99), rng.randint(1000, 9999), rng.randint(1000, 9999)
        return rng.choice([f"0{a}-{b}-{c}", f"0{a}{b}{c}", f"090-{b}-{c}", f"+81 {a} {b} {c}"])
    if cls == "address":
        f = ctx.setdefault("addr_fmt2", rng.randrange(6))
        return [rng.choice(PREFS) + rng.choice(CITIES) + f"{rng.randint(1, 9)}-{rng.randint(1, 20)}-{rng.randint(1, 30)}",
                f"{rng.randint(100, 999)}-{rng.randint(1000, 9999)}", rng.choice(PREFS), rng.choice(["Japan", "JP", "日本", "Tokyo", "Osaka"]),
                f"{rng.randint(100, 999)}{rng.randint(1000, 9999)}", f"〒{rng.randint(100, 999)}-{rng.randint(1000, 9999)}"][f]
    raise ValueError(cls)


HARD_NUMERIC = 0.0  # 数字の種類どうしで値が似る例の割合（train3 で設定）
SHARED_NUMERIC = 0.0  # 数字の種類で、種類によらない同じ作り方の値を使う割合


def hard_value(rng, cls):
    """金額・数量・率・番号の値を、わざと見分けにくくする（実際の CSV では値だけでは決まらないことが多い）"""
    if cls == "amount":
        return str(rng.choice([0, 1, 3, 5, 8, 12, 50, 100, 120, 300]))
    if cls == "quantity":
        return str(rng.choice([100, 250, 1200, 3000, 15000, 48, 2]))
    if cls == "rate":
        return str(rng.choice([8, 10, 0, 5, 15, 30, 100]))
    if cls == "id":
        return str(rng.choice([1, 2, 3, 15, 120, 1001, 2350]))
    return None


def column(rng, cls, n=None, empty_rate=None):
    n = n or rng.choice([5, 8, 10, 20])
    if cls in ("amount", "quantity", "rate", "id") and rng.random() < HARD_NUMERIC:
        return [hard_value(rng, cls) for _ in range(n)]
    # 数字の種類どうしで「同じ作り方」の値（値だけでは決まらない例。列名で決める力をつける。OpenAI の指摘 2026-10-16）
    if cls in ("amount", "quantity", "rate", "id") and rng.random() < SHARED_NUMERIC:
        pool = rng.choice([[1, 2, 3, 5, 8, 10, 12], [0, 100, 250, 1200, 3000], [1001, 1002, 1003, 1010], [5, 8, 10, 15, 30]])
        return [str(rng.choice(pool)) for _ in range(n)]
    ctx = {}
    er = rng.choice([0, 0, 0, 0.1, 0.3]) if empty_rate is None else empty_rate
    return [("" if rng.random() < er else value(rng, cls, ctx)) for _ in range(n)]


def make_train(n_per_class=600, seed=1):
    rng = random.Random(seed)
    rows = []
    for cls in CLASSES:
        for _ in range(n_per_class):
            rows.append((header(rng, cls), column(rng, cls), cls))
    rng.shuffle(rows)
    return rows


# ---------- 組み立て式の列名（2026-10-16 追加）：「何の」＋「どの属性」 ----------
# 英語の snake_case・camelCase・Title Case と、日本語の「対象＋属性」を一般的な語で組み立てる。
# 未見セット（blind_set.py）の中身は見ていない。英語の組み立てに弱いという一般的な弱点への対策。
EN_ENTITY = ["customer", "billing", "shipping", "order", "item", "line_item", "product", "payment", "charge", "invoice", "account",
             "merchant", "seller", "buyer", "store", "vendor", "supplier", "refund", "payout", "transfer", "transaction", "user",
             "member", "employee", "booking", "reservation", "shipment", "package", "listing", "variant", "subscription", "plan"]
EN_PARTY = ["payee", "payer", "party", "partner", "counterparty", "organization", "entity"]
EN_ATTR = {
    "id": ["id", "number", "no", "code", "sku", "ref", "reference", "key", "uuid", "barcode", "upc", "ean", "tracking_number"],
    "amount": ["amount", "total", "price", "fee", "cost", "subtotal", "gross", "net", "balance", "tax_amount", "discount", "value", "paid", "due"],
    "quantity": ["qty", "quantity", "count", "units", "stock", "available", "sold", "ordered"],
    "date": ["date", "time", "created", "updated", "created_at", "updated_at", "paid_at", "shipped_at", "utc", "timestamp", "datetime", "day", "deadline", "expires_at"],
    "rate": ["rate", "percent", "percentage", "ratio", "pct"],
    "category": ["status", "type", "method", "brand", "currency", "reason", "category", "kind", "level", "mode", "channel", "source", "flag", "is_active", "is_test", "condition"],
    "text": ["description", "note", "notes", "memo", "comment", "message", "remarks", "instructions"],
    "product": ["title", "product_name", "item_name", "name"],
    "email": ["email", "email_address", "mail"],
    "phone": ["phone", "phone_number", "tel", "mobile"],
    "address": ["address", "address_line1", "address_line2", "line1", "line2", "city", "state", "province", "zip", "postal_code", "country", "country_code", "street"],
    "person": ["name", "full_name", "first_name", "last_name", "contact_name"],
    "org": ["company", "company_name", "business_name", "store_name", "bank_name", "merchant_name"],
}
PERSONISH = {"customer", "billing", "shipping", "buyer", "user", "member", "employee", "seller"}
ORGISH = {"merchant", "store", "vendor", "supplier", "account"}
JA_ENTITY = ["注文", "受注", "顧客", "会員", "請求", "支払", "入金", "出金", "振込", "商品", "取引", "予約", "配送", "発送", "返品", "仕入", "売上", "明細", "口座", "契約"]
JA_ATTR = {"id": ["番号", "ID", "No", "コード"], "date": ["日", "日時", "日付", "年月日", "予定日"], "amount": ["金額", "額", "合計", "単価", "手数料"],
           "quantity": ["数", "数量", "件数"], "category": ["区分", "状態", "方法", "種別", "ステータス"], "text": ["メモ", "備考", "内容"],
           "address": ["住所", "郵便番号", "都道府県"], "phone": ["電話番号", "TEL"], "email": ["メール", "メールアドレス"]}


def en_join(rng, parts):
    style = rng.random()
    words = [w for p in parts for w in p.split("_")]
    if style < 0.45:
        return "_".join(words)
    if style < 0.6:
        return words[0] + "".join(w[:1].upper() + w[1:] for w in words[1:])
    if style < 0.8:
        return " ".join(w[:1].upper() + w[1:] for w in words)
    if style < 0.9:
        return " ".join(words)
    return "-".join(words)


def composed_header(rng, cls):
    if rng.random() < 0.6 and cls in EN_ATTR:
        attr = rng.choice(EN_ATTR[cls])
        ent = rng.choice(EN_ENTITY)
        if cls == "person":
            ent = rng.choice(sorted(PERSONISH))
        if cls == "org":
            ent = rng.choice(sorted(ORGISH)) if rng.random() < 0.5 else ""
        if cls == "product" and attr == "name":
            ent = rng.choice(["product", "item", "line_item", "variant", "listing"])
        parts = [p for p in ([ent] if ent and rng.random() < 0.85 else []) + ([rng.choice(["original", "total", "local", "settlement", "customer_facing", "net"])] if cls in ("amount", "category") and rng.random() < 0.15 else []) + [attr]]
        return en_join(rng, parts)
    if cls in JA_ATTR:
        return rng.choice(JA_ENTITY) + rng.choice(JA_ATTR[cls])
    return header(rng, cls)


def make_train2(n_per_class=1500, composed_share=0.4, seed=1):
    rng = random.Random(seed)
    rows = []
    for cls in CLASSES:
        for _ in range(n_per_class):
            h = composed_header(rng, cls) if rng.random() < composed_share else header(rng, cls)
            rows.append((h, column(rng, cls), cls))
    rng.shuffle(rows)
    return rows
