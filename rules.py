"""比べる相手：キーワードのルール（AIなし）。公平に強くするため、列名の言葉と値の形の両方を見る。
順番が大事（例：「税区分」は「税」より先、「金額」は「額」より先）。"""
import re
from features import norm_header, value_stats, STAT_NAMES

HEADER_RULES = [
    ("email", r"mail|メール"),
    ("phone", r"電話|tel|phone|fax|携帯|mobile"),
    ("tax_class", r"税区分|課税|税コード|tax ?(class|code|category)|インボイス|適格|vat|taxable|内税/外税|軽減"),
    ("rate", r"率|%|％|rate|percent|ratio|比$"),
    ("date", r"日付|年月日|日時|時刻|期日|期限|日$|^日|date|time|created|updated|_at$| at$|timestamp"),
    ("account", r"勘定|科目|部門|部署|セグメント|account|department|cost ?center|口座$"),
    ("quantity", r"数量|個数|点数|件数|口数|本数|枚数|人数|回数|数$|qty|quantity|count|units"),
    ("amount", r"金額|合計|小計|総額|売上|価格|単価|税額|消費税|送料|手数料|値引|割引|残高|原価|利益|円|amount|price|total|tax|fee|discount|balance|cost|revenue|sales|shipping$|額"),
    ("id", r"番号|コード|no\.?$|^no|id$|^id|sku|jan|品番|型番|uuid|reference|number|ナンバー"),
    ("address", r"住所|所在地|番地|建物|都道府県|市区町村|郵便|〒|address|city|state|province|zip|postal|country|street|region"),
    ("org", r"取引先|会社|法人|屋号|店|得意先|仕入先|請求先|支払先|振込先|メーカー|ブランド|銀行|金融機関|支店|company|vendor|supplier|merchant|store|shop|bank|branch|carrier|brand|location"),
    ("person", r"氏名|名前|お名前|担当|購入者|注文者|受取人|依頼人|顧客名|会員名|者$|スタッフ|name|staff|owner|employee|by$|recipient"),
    ("product", r"商品|品名|品目|アイテム|メニュー|サービス|銘柄|製品|タイトル|product|item|title|menu|service"),
    ("text", r"摘要|備考|メモ|コメント|内容|明細|説明|詳細|注記|件名|用途|note|memo|comment|description|remark|detail|message"),
    ("category", r"区分|種別|種類|分類|カテゴリ|ステータス|状態|状況|フラグ|タイプ|方法|通貨|チャネル|ラベル|タグ|status|type|category|kind|flag|method|channel|currency|label|tag|gender|rank|source|level"),
]
HEADER_RULES = [(c, re.compile(p)) for c, p in HEADER_RULES]


def rule_by_header(header):
    h = norm_header(header)
    for c, r in HEADER_RULES:
        if r.search(h):
            return c
    return None


def rule_by_values(values):
    s = dict(zip(STAT_NAMES, value_stats(values)))
    if s["empty"] >= 0.999:
        return None
    if s["email"] > 0.6:
        return "email"
    if s["date"] + s["datetime"] > 0.6:
        return "date"
    if s["postal"] > 0.6 or s["pref"] > 0.6:
        return "address"
    if s["phone"] > 0.6:
        return "phone"
    if s["pct"] > 0.6:
        return "rate"
    if s["num"] > 0.8:
        if s["yen"] > 0.3 or s["comma"] > 0.3:
            return "amount"
        if s["lead0"] > 0.3 or s["len_fixed"] > 0:
            return "id"
        if s["small_int"] > 0.9 and s["log_mean"] < 0.2:
            return "quantity"
        return "amount"
    if s["org"] > 0.5:
        return "org"
    return None


def rule(header, values):
    return rule_by_header(header) or rule_by_values(values) or "unknown"
