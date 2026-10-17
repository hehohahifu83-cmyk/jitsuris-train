"""評価用の列名（学習には使わない）。出どころは各社の公開資料。正解の種類は Claude が手で付けた。
種類：date 日付・日時 / amount 金額 / quantity 数量 / rate 率 / id 番号・コード / org 会社・取引先・店・銀行 /
person 人の名前 / product 商品・品目 / account 勘定科目・補助科目・部門 / tax_class 税区分 / text 摘要・備考 /
category 区分・状態・方法・フラグ / email / phone / address 住所・郵便番号・国
出典（確認日 2026-10-15）：
- freee 取引インポート・MF 仕訳帳インポート：tool-kobo products/accounting-check/core.js（各社公式ヘルプに合わせた書式）
- 弥生会計 インポート形式：freee ヘルプ https://support.freee.co.jp/hc/ja/articles/204599604
- Shopify 注文エクスポート：https://help.shopify.com/manual/orders/export-orders
- ゆうちょ銀行 ビズダイレクト 入出金明細：https://www.jp-bank.japanpost.jp/hojin/smart/bizdirect/pdf/bizdirect_18.pdf
- SBI新生銀行 入出金明細照会：https://sbishinseibank.co.jp/institutional/products/pdf/scn_usermanual_appx.account_details_Inquiry.pdf
- 大和証券 取引履歴：https://www.daiwa.jp/olt_help/zan/h_10tori_0101-01.html
- 楽天・Amazon・Yahoo の一部の列：日本郵便 ゆうパックプリントR 説明書
"""

EVAL = [
    # freee 取引インポート
    ("freee", "収支区分", "category"), ("freee", "管理番号", "id"), ("freee", "発生日", "date"), ("freee", "決済期日", "date"),
    ("freee", "取引先コード", "id"), ("freee", "取引先", "org"), ("freee", "勘定科目", "account"), ("freee", "税区分", "tax_class"),
    ("freee", "金額", "amount"), ("freee", "税計算区分", "tax_class"), ("freee", "税額", "amount"), ("freee", "備考", "text"),
    ("freee", "品目", "product"), ("freee", "部門", "account"), ("freee", "メモタグ", "category"), ("freee", "決済日", "date"),
    ("freee", "決済口座", "account"), ("freee", "決済金額", "amount"),
    # マネーフォワード 仕訳帳インポート
    ("mf", "取引No", "id"), ("mf", "取引日", "date"), ("mf", "借方勘定科目", "account"), ("mf", "借方補助科目", "account"),
    ("mf", "借方部門", "account"), ("mf", "借方取引先", "org"), ("mf", "借方税区分", "tax_class"), ("mf", "借方インボイス", "tax_class"),
    ("mf", "借方金額(円)", "amount"), ("mf", "借方税額", "amount"), ("mf", "貸方勘定科目", "account"), ("mf", "貸方補助科目", "account"),
    ("mf", "貸方部門", "account"), ("mf", "貸方取引先", "org"), ("mf", "貸方税区分", "tax_class"), ("mf", "貸方インボイス", "tax_class"),
    ("mf", "貸方金額(円)", "amount"), ("mf", "貸方税額", "amount"), ("mf", "摘要", "text"), ("mf", "仕訳メモ", "text"),
    ("mf", "タグ", "category"), ("mf", "MF仕訳タイプ", "category"), ("mf", "決算整理仕訳", "category"), ("mf", "作成日時", "date"),
    ("mf", "作成者", "person"), ("mf", "最終更新日時", "date"), ("mf", "最終更新者", "person"),
    # 弥生会計 インポート形式
    ("yayoi", "識別フラグ", "category"), ("yayoi", "伝票No", "id"), ("yayoi", "決算", "category"), ("yayoi", "取引日付", "date"),
    ("yayoi", "借方勘定科目", "account"), ("yayoi", "借方補助科目", "account"), ("yayoi", "借方部門", "account"), ("yayoi", "借方税区分", "tax_class"),
    ("yayoi", "借方金額", "amount"), ("yayoi", "借方税金額", "amount"), ("yayoi", "貸方勘定科目", "account"), ("yayoi", "貸方補助科目", "account"),
    ("yayoi", "貸方部門", "account"), ("yayoi", "貸方税区分", "tax_class"), ("yayoi", "貸方金額", "amount"), ("yayoi", "貸方税金額", "amount"),
    ("yayoi", "摘要", "text"), ("yayoi", "番号", "id"), ("yayoi", "期日", "date"), ("yayoi", "タイプ", "category"),
    ("yayoi", "生成元", "category"), ("yayoi", "仕訳メモ", "text"), ("yayoi", "付箋1", "category"), ("yayoi", "付箋2", "category"),
    ("yayoi", "調整", "category"),
    # Shopify 注文エクスポート（英語）
    ("shopify", "Name", "id"), ("shopify", "Phone", "phone"), ("shopify", "Email", "email"), ("shopify", "Financial Status", "category"),
    ("shopify", "Paid at", "date"), ("shopify", "Fulfillment Status", "category"), ("shopify", "Fulfilled at", "date"),
    ("shopify", "Accepts Marketing", "category"), ("shopify", "Currency", "category"), ("shopify", "Subtotal", "amount"),
    ("shopify", "Shipping", "amount"), ("shopify", "Taxes", "amount"), ("shopify", "Total", "amount"), ("shopify", "Discount Code", "id"),
    ("shopify", "Discount Amount", "amount"), ("shopify", "Shipping Method", "category"), ("shopify", "Created at", "date"),
    ("shopify", "Lineitem quantity", "quantity"), ("shopify", "Lineitem name", "product"), ("shopify", "Lineitem price", "amount"),
    ("shopify", "Lineitem compare-at price", "amount"), ("shopify", "Lineitem SKU", "id"), ("shopify", "Lineitem requires shipping", "category"),
    ("shopify", "Lineitem taxable", "category"), ("shopify", "Lineitem fulfillment status", "category"), ("shopify", "Billing Name", "person"),
    ("shopify", "Billing Street", "address"), ("shopify", "Billing Address1", "address"), ("shopify", "Billing Address2", "address"),
    ("shopify", "Billing Company", "org"), ("shopify", "Billing City", "address"), ("shopify", "Billing Zip", "address"),
    ("shopify", "Billing Province", "address"), ("shopify", "Billing Province Name", "address"), ("shopify", "Billing Country", "address"),
    ("shopify", "Billing Phone", "phone"), ("shopify", "Shipping Name", "person"), ("shopify", "Shipping Street", "address"),
    ("shopify", "Shipping Address1", "address"), ("shopify", "Shipping Address2", "address"), ("shopify", "Shipping Company", "org"),
    ("shopify", "Shipping City", "address"), ("shopify", "Shipping Zip", "address"), ("shopify", "Shipping Province", "address"),
    ("shopify", "Shipping Province Name", "address"), ("shopify", "Shipping Country", "address"), ("shopify", "Shipping Phone", "phone"),
    ("shopify", "Notes", "text"), ("shopify", "Note Attributes", "text"), ("shopify", "Canceled at", "date"),
    ("shopify", "Payment Method", "category"), ("shopify", "Payment References", "id"), ("shopify", "Refunded Amount", "amount"),
    ("shopify", "Vendor", "org"), ("shopify", "Outstanding Balance", "amount"), ("shopify", "Employee", "person"),
    ("shopify", "Location", "org"), ("shopify", "Device ID", "id"), ("shopify", "Id", "id"), ("shopify", "Tags", "category"),
    ("shopify", "Risk Level", "category"), ("shopify", "Source", "category"), ("shopify", "Lineitem discount", "amount"),
    ("shopify", "Payment ID", "id"), ("shopify", "Payment terms", "category"), ("shopify", "Next payment due at", "date"),
    # 銀行・証券
    ("yucho", "取引日", "date"), ("yucho", "入出金区分", "category"), ("yucho", "取引内容", "text"), ("yucho", "送金人名等", "person"),
    ("yucho", "受入明細番号", "id"), ("yucho", "取扱口数", "quantity"), ("yucho", "取引金額", "amount"), ("yucho", "現在（貸付）高", "amount"),
    ("yucho", "EDI情報等", "text"),
    ("sbi", "照会口座", "id"), ("sbi", "番号", "id"), ("sbi", "勘定日", "date"), ("sbi", "(起算日)", "date"),
    ("sbi", "出金金額(円)", "amount"), ("sbi", "入金金額(円)", "amount"), ("sbi", "小切手区分", "category"), ("sbi", "残高(円)", "amount"),
    ("sbi", "取引区分", "category"), ("sbi", "明細区分", "category"), ("sbi", "金融機関名", "org"), ("sbi", "支店名", "org"), ("sbi", "摘要", "text"),
    ("daiwa", "約定日", "date"), ("daiwa", "受渡日", "date"), ("daiwa", "銘柄名", "product"), ("daiwa", "取引", "category"),
    ("daiwa", "数量", "quantity"), ("daiwa", "単価", "amount"), ("daiwa", "精算金額", "amount"),
    # 楽天・Amazon・Yahoo（一部の列）
    ("mall", "受注番号", "id"), ("mall", "レコードナンバー", "id"), ("mall", "入札番号", "id"), ("mall", "注文番号", "id"),
    ("mall", "送付先ID", "id"), ("mall", "決済方法", "category"), ("mall", "支払方法名", "category"), ("mall", "配送区分", "category"),
    ("mall", "商品番号", "id"), ("mall", "品名", "product"), ("mall", "個数", "quantity"), ("mall", "payment-method", "category"),
    ("mall", "お支払い方法種別", "category"), ("mall", "配達時間帯", "category"),
]
