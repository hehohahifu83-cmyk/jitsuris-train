"""教材（先生役：Claude、2026-10-16）。業務の表を分野ごとに書いたもの。
注意：各社の正式な列名そのものではなく、Claude の知識から「その分野の CSV にありそうな列名」を書いたもの。
表ごとに書くので、同じ表のほかの列（文脈）も学べる。未見セット1・2の出典（Airレジ・HubSpot・Stripe 等）は使っていない。
種類：date amount quantity rate id org person product account tax_class text category email phone address"""

T = {}


def table(name, spec):
    """spec：'列名:種類' を | で区切った文字列"""
    cols = []
    for part in spec.split("|"):
        part = part.strip()
        if not part:
            continue
        h, lab = part.rsplit(":", 1)
        cols.append((h.strip(), lab.strip()))
    T[name] = cols


# ---------- POS・店舗 ----------
table("pos_sales_ja", "取引日時:date|取引番号:id|レシート番号:id|店舗コード:id|店舗名:org|レジ番号:id|担当者:person|商品コード:id|商品名:product|部門:category|単価:amount|数量:quantity|小計:amount|値引額:amount|割引率:rate|税率:rate|消費税:amount|合計金額:amount|支払方法:category|預り金:amount|釣銭:amount|客層:category|会員番号:id|取消区分:category|備考:text")
table("pos_daily_ja", "営業日:date|店舗:org|売上合計:amount|純売上:amount|客数:quantity|客単価:amount|点数:quantity|返品金額:amount|返品件数:quantity|現金売上:amount|カード売上:amount|電子マネー売上:amount|QR決済売上:amount|前年同日比:rate|天気:category|メモ:text")
table("pos_items_en", "Date:date|Time:date|Receipt No:id|Store ID:id|Location:org|Register:id|Cashier:person|SKU:id|Item:product|Variant:category|Category:category|Qty:quantity|Unit Price:amount|Gross Sales:amount|Discounts:amount|Net Sales:amount|Tax:amount|Tip:amount|Total Collected:amount|Payment Type:category|Card Brand:category|Customer Name:person|Customer ID:id|Notes:text")
table("pos_staff_ja", "勤務日:date|スタッフID:id|スタッフ名:person|出勤時刻:date|退勤時刻:date|売上担当件数:quantity|担当売上:amount|店舗名:org")
# ---------- EC ----------
table("ec_orders_ja", "注文番号:id|注文日時:date|入金日:date|発送日:date|注文ステータス:category|支払方法:category|購入者名:person|購入者フリガナ:person|購入者メールアドレス:email|購入者電話番号:phone|購入者郵便番号:address|購入者都道府県:address|購入者住所:address|お届け先名:person|お届け先郵便番号:address|お届け先住所1:address|お届け先住所2:address|お届け先電話番号:phone|商品ID:id|商品名:product|バリエーション:category|販売価格:amount|個数:quantity|商品小計:amount|送料:amount|代引手数料:amount|クーポン割引:amount|ポイント利用:amount|請求金額:amount|配送方法:category|お届け希望日:date|お届け時間帯:category|追跡番号:id|備考:text")
table("ec_items_ja", "商品管理番号:id|商品番号:id|商品名:product|キャッチコピー:text|販売価格:amount|表示価格:amount|原価:amount|在庫数:quantity|在庫タイプ:category|カテゴリ:category|ブランド:org|JANコード:id|重量:quantity|公開状態:category|販売開始日時:date|販売終了日時:date|商品説明:text|送料区分:category|税率区分:tax_class")
table("ec_orders_en", "order-id:id|order-item-id:id|purchase-date:date|payments-date:date|buyer-email:email|buyer-name:person|buyer-phone-number:phone|sku:id|product-name:product|quantity-purchased:quantity|currency:category|item-price:amount|item-tax:amount|shipping-price:amount|shipping-tax:amount|ship-service-level:category|recipient-name:person|ship-address-1:address|ship-address-2:address|ship-city:address|ship-state:address|ship-postal-code:address|ship-country:address|ship-phone-number:phone|delivery-start-date:date|fulfillment-channel:category|sales-channel:category|order-status:category")
table("ec_settlement_en", "settlement-id:id|settlement-start-date:date|settlement-end-date:date|deposit-date:date|total-amount:amount|transaction-type:category|order-id:id|merchant-order-id:id|adjustment-id:id|amount-type:category|amount-description:text|amount:amount|fulfillment-id:category|posted-date:date|sku:id|quantity-purchased:quantity|promotion-id:id")
table("ec_reviews_ja", "レビューID:id|投稿日時:date|商品番号:id|商品名:product|評価:quantity|タイトル:text|本文:text|投稿者:person|購入日:date|公開状態:category")
table("ec_woo_en", "Order Number:id|Order Status:category|Order Date:date|Customer Note:text|First Name (Billing):person|Last Name (Billing):person|Company (Billing):org|Address 1&2 (Billing):address|City (Billing):address|State Code (Billing):address|Postcode (Billing):address|Country Code (Billing):address|Email (Billing):email|Phone (Billing):phone|Payment Method Title:category|Cart Discount Amount:amount|Order Subtotal Amount:amount|Shipping Method Title:category|Order Shipping Amount:amount|Order Total Amount:amount|Order Total Tax Amount:amount|SKU:id|Item #:id|Item Name:product|Quantity (- Refund):quantity|Item Cost:amount|Coupon Code:id")
# ---------- 決済 ----------
table("pay_ja", "決済日時:date|決済ID:id|加盟店ID:id|加盟店名:org|取引種別:category|決済手段:category|ブランド:category|決済金額:amount|手数料率:rate|決済手数料:amount|入金予定額:amount|入金予定日:date|入金日:date|ステータス:category|オーダーID:id|返金額:amount|返金日時:date|カード番号下4桁:id|承認番号:id|メモ:text")
table("pay_en", "Transaction ID:id|Date:date|Time Zone:category|Name:person|Type:category|Status:category|Currency:category|Gross:amount|Fee:amount|Net:amount|From Email Address:email|To Email Address:email|Item Title:product|Item ID:id|Shipping and Handling Amount:amount|Sales Tax:amount|Invoice Number:id|Reference Txn ID:id|Balance:amount|Country Code:address|Contact Phone Number:phone|Subject:text|Note:text")
# ---------- 銀行・カード ----------
table("bank_ja", "日付:date|取引日:date|起算日:date|摘要:text|お取引内容:text|お預入金額:amount|お引出金額:amount|入金:amount|出金:amount|差引残高:amount|残高:amount|取引区分:category|振込依頼人名:person|メモ:text|口座番号:id|支店名:org")
table("bank_net_ja", "照会日:date|取引年月日:date|入出金区分:category|取引金額:amount|手数料:amount|現在残高:amount|内容:text|振込先金融機関:org|振込先支店:org|振込先口座番号:id|受取人名:person|EDI情報:text|取引番号:id")
table("bank_en", "Posting Date:date|Transaction Date:date|Description:text|Details:text|Debit:amount|Credit:amount|Amount:amount|Running Balance:amount|Check or Slip #:id|Type:category|Account Number:id|Bank Name:org|Memo:text")
table("card_ja", "利用日:date|ご利用日:date|ご利用店名:org|利用者:person|支払区分:category|今回回数:quantity|支払回数:quantity|利用金額:amount|ご利用金額:amount|手数料:amount|今回お支払金額:amount|支払月:date|お支払日:date|カード番号:id|備考:text|現地通貨額:amount|通貨略称:category|換算レート:rate")
table("card_en", "Transaction Date:date|Post Date:date|Description:text|Merchant:org|Category:category|Type:category|Amount:amount|Card Member:person|Account #:id|Reference:id|Extended Details:text|Foreign Spend Amount:amount|Exchange Rate:rate")
# ---------- 給与・勤怠・人事 ----------
table("payroll_ja", "社員番号:id|氏名:person|フリガナ:person|所属:account|役職:category|雇用形態:category|支給日:date|対象期間:date|基本給:amount|役職手当:amount|通勤手当:amount|残業手当:amount|総支給額:amount|健康保険料:amount|厚生年金保険料:amount|雇用保険料:amount|所得税:amount|住民税:amount|控除合計:amount|差引支給額:amount|振込額:amount|出勤日数:quantity|欠勤日数:quantity|残業時間:quantity|有給取得日数:quantity|扶養人数:quantity")
table("attendance_ja", "日付:date|曜日:category|従業員コード:id|従業員名:person|所属:account|勤務区分:category|出勤:date|退勤:date|休憩開始:date|休憩終了:date|休憩時間:quantity|労働時間:quantity|残業時間:quantity|深夜時間:quantity|遅刻:category|早退:category|打刻場所:address|申請状況:category|承認者:person|備考:text")
table("hr_ja", "従業員番号:id|姓:person|名:person|セイ:person|メイ:person|生年月日:date|性別:category|入社日:date|退職日:date|部署:account|役職:category|雇用形態:category|メールアドレス:email|電話番号:phone|携帯電話番号:phone|郵便番号:address|住所:address|緊急連絡先氏名:person|緊急連絡先電話番号:phone|基本給:amount|銀行名:org|支店名:org|口座番号:id|口座名義:person|マイナンバー提出状況:category")
table("hr_en", "Employee ID:id|First Name:person|Last Name:person|Preferred Name:person|Work Email:email|Personal Email:email|Mobile Phone:phone|Hire Date:date|Termination Date:date|Department:account|Job Title:category|Employment Type:category|Manager:person|Annual Salary:amount|Pay Frequency:category|Work Location:address|Birth Date:date|Gender:category|Status:category")
table("timesheet_en", "Date:date|Employee:person|Employee Number:id|Project:account|Task:text|Clock In:date|Clock Out:date|Break (min):quantity|Regular Hours:quantity|Overtime Hours:quantity|Hourly Rate:amount|Total Pay:amount|Approved By:person|Approval Status:category|Notes:text")
# ---------- 経費・請求書・見積 ----------
table("expense_ja", "申請番号:id|申請日:date|利用日:date|申請者:person|部署:account|経費科目:account|勘定科目:account|支払先:org|内容:text|金額:amount|税込金額:amount|税抜金額:amount|消費税額:amount|税区分:tax_class|インボイス登録番号:id|適格請求書:tax_class|支払方法:category|精算日:date|承認者:person|承認状況:category|プロジェクト:account|領収書添付:category|備考:text")
table("expense_en", "Report ID:id|Report Name:text|Submitted Date:date|Transaction Date:date|Employee:person|Employee Email:email|Expense Type:account|Vendor:org|Business Purpose:text|City:address|Country:address|Amount:amount|Currency:category|Exchange Rate:rate|Amount (USD):amount|Tax Amount:amount|Payment Type:category|Approval Status:category|Approved Date:date|Cost Center:account|Project Code:id|Receipt Attached:category")
table("invoice_ja", "請求書番号:id|請求日:date|お支払期限:date|取引先名:org|取引先コード:id|担当者名:person|件名:text|品目:product|数量:quantity|単位:category|単価:amount|金額:amount|小計:amount|消費税率:rate|消費税:amount|請求金額合計:amount|入金状況:category|入金日:date|入金額:amount|振込先:org|登録番号:id|備考:text|発行者:person")
table("quote_ja", "見積番号:id|見積日:date|有効期限:date|顧客名:org|顧客担当者:person|件名:text|商品名:product|数量:quantity|単価:amount|値引:amount|見積金額:amount|税額:amount|合計:amount|受注確度:rate|ステータス:category|営業担当:person|メモ:text")
table("invoice_en", "Invoice Number:id|Invoice Date:date|Due Date:date|Customer:org|Customer Contact:person|Billing Email:email|PO Number:id|Description:text|Product/Service:product|Qty:quantity|Rate:amount|Amount:amount|Subtotal:amount|Tax Rate:rate|Tax:amount|Discount:amount|Total:amount|Amount Paid:amount|Balance Due:amount|Status:category|Paid Date:date|Terms:category|Memo:text")
# ---------- 在庫・仕入・物流 ----------
table("inventory_ja", "品番:id|商品コード:id|JANコード:id|商品名:product|規格:category|カテゴリ:category|保管場所:address|ロット番号:id|賞味期限:date|入荷日:date|入荷数:quantity|出荷数:quantity|在庫数:quantity|引当数:quantity|発注点:quantity|発注数:quantity|仕入単価:amount|在庫金額:amount|仕入先:org|最終棚卸日:date|備考:text")
table("purchase_ja", "発注番号:id|発注日:date|納期:date|仕入先コード:id|仕入先名:org|担当者:person|商品コード:id|品名:product|発注数量:quantity|入荷済数量:quantity|単価:amount|発注金額:amount|消費税:amount|支払条件:category|状態:category|備考:text")
table("shipping_ja", "お客様管理番号:id|送り状種類:category|クール区分:category|伝票番号:id|出荷予定日:date|お届け予定日:date|配達時間帯:category|お届け先コード:id|お届け先電話番号:phone|お届け先郵便番号:address|お届け先住所:address|お届け先アパートマンション名:address|お届け先会社・部門:org|お届け先名:person|ご依頼主電話番号:phone|ご依頼主郵便番号:address|ご依頼主住所:address|ご依頼主名:person|品名:product|荷扱い:category|記事:text|個数:quantity|重量:quantity|サイズ:category|代金引換額:amount|運賃:amount")
table("inventory_en", "Item Code:id|Barcode:id|Item Name:product|Description:text|Category:category|Warehouse:address|Bin Location:address|Lot Number:id|Expiry Date:date|On Hand:quantity|Allocated:quantity|Available:quantity|Reorder Point:quantity|Unit Cost:amount|Total Value:amount|Supplier:org|Last Counted:date|Unit of Measure:category")
# ---------- CRM・予約・会員 ----------
table("crm_ja", "顧客ID:id|会社名:org|部署名:account|担当者名:person|役職:category|メールアドレス:email|電話番号:phone|FAX番号:phone|郵便番号:address|都道府県:address|市区町村:address|番地:address|業種:category|従業員数:quantity|年商:amount|リードソース:category|ステータス:category|営業担当:person|最終接触日:date|次回アクション日:date|商談金額:amount|受注予定日:date|確度:rate|メモ:text")
table("crm_en", "Account ID:id|Account Name:org|Industry:category|Annual Revenue:amount|Employees:quantity|Billing Street:address|Billing City:address|Billing State/Province:address|Billing Zip/Postal Code:address|Billing Country:address|Phone:phone|Website:text|Account Owner:person|Opportunity Name:text|Stage:category|Amount:amount|Probability (%):rate|Close Date:date|Lead Source:category|Contact Name:person|Email:email|Created Date:date|Last Modified Date:date")
table("reserve_ja", "予約番号:id|予約受付日時:date|予約日:date|開始時刻:date|終了時刻:date|メニュー:product|コース:product|担当スタッフ:person|お客様名:person|お客様名カナ:person|電話番号:phone|メールアドレス:email|人数:quantity|料金:amount|前払い:amount|キャンセル料:amount|予約経路:category|予約ステータス:category|来店回数:quantity|要望:text|備考:text")
table("member_ja", "会員番号:id|会員ランク:category|氏名:person|カナ:person|性別:category|生年月日:date|年齢:quantity|郵便番号:address|住所:address|電話番号:phone|メールアドレス:email|入会日:date|最終購入日:date|購入回数:quantity|累計購入金額:amount|保有ポイント:quantity|ポイント付与率:rate|メルマガ配信:category|退会日:date|備考:text")
# ---------- 広告・分析 ----------
table("ads_ja", "日付:date|キャンペーン:text|キャンペーンID:id|広告グループ:text|広告ID:id|ステータス:category|表示回数:quantity|クリック数:quantity|クリック率:rate|平均クリック単価:amount|費用:amount|コンバージョン:quantity|コンバージョン率:rate|コンバージョン単価:amount|コンバージョン値:amount|広告費用対効果:rate|インプレッションシェア:rate")
table("ads_en", "Day:date|Campaign name:text|Campaign ID:id|Ad set name:text|Ad name:text|Delivery status:category|Reach:quantity|Impressions:quantity|Frequency:rate|Link clicks:quantity|CTR (link click-through rate):rate|CPC (cost per link click):amount|Amount spent (JPY):amount|Purchases:quantity|Purchase conversion value:amount|Purchase ROAS:rate|Cost per purchase:amount|Reporting starts:date|Reporting ends:date")
table("analytics_en", "Date:date|Session source / medium:category|Landing page:text|Country:address|City:address|Device category:category|Users:quantity|New users:quantity|Sessions:quantity|Engaged sessions:quantity|Engagement rate:rate|Average engagement time:quantity|Bounce rate:rate|Conversions:quantity|Total revenue:amount|Transactions:quantity|Item name:product|Items purchased:quantity")
# ---------- 会計ソフト（クラウド以外）・固定資産 ----------
table("ledger_ja", "伝票日付:date|伝票番号:id|行番号:id|借方科目コード:id|借方科目名:account|借方補助:account|借方部門:account|借方税区分:tax_class|借方金額:amount|借方消費税額:amount|貸方科目コード:id|貸方科目名:account|貸方補助:account|貸方部門:account|貸方税区分:tax_class|貸方金額:amount|貸方消費税額:amount|摘要:text|取引先:org|入力者:person|入力日時:date")
table("assets_ja", "資産番号:id|資産名称:product|勘定科目:account|取得日:date|事業供用日:date|取得価額:amount|償却方法:category|耐用年数:quantity|償却率:rate|当期償却額:amount|期末帳簿価額:amount|設置場所:address|管理部門:account|数量:quantity|備考:text")
table("budget_ja", "年月:date|部門:account|勘定科目:account|予算額:amount|実績額:amount|差異:amount|達成率:rate|前年実績:amount|前年比:rate|コメント:text")
table("sales_mgmt_ja", "売上日:date|伝票No:id|得意先コード:id|得意先名:org|担当者:person|商品コード:id|商品名:product|数量:quantity|単位:category|単価:amount|売上金額:amount|原価:amount|粗利:amount|粗利率:rate|税区分:tax_class|消費税:amount|納品先:org|締日:date|回収予定日:date")

CURRICULUM = T
