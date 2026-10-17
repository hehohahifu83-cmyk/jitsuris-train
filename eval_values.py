"""評価用の値（学習用の gen.py とは別の言葉・別の書式で作る。学習の値をそのまま覚えただけで当たらないようにする）。
作り物で、実在の人・会社・住所ではない。"""
import random

PRODUCTS = ["オーガニック緑茶 100g", "レザー名刺入れ", "保冷バッグ M", "抗菌まな板", "子ども用長靴 18cm", "定期便（毎月）",
            "Ceramic Bowl", "Linen Shirt - Navy", "シャンプー詰め替え", "体験レッスン 60分", "クラフトビール 6本", "A4 コピー用紙 500枚"]
ORGS = ["こもれび商事株式会社", "(有)たけのこ製作所", "合同会社ハルカゼ", "くすのき信用金庫", "ふたば物流", "Blue Harbor Co.",
        "ﾆｼｷ(ｶ", "やまびこ工務店", "つばめ銀行 本店", "ミドリ薬局 駅前店"]
PEOPLE = ["森 さやか", "石川 拓海", "小野寺 恵", "Kenji Mori", "ﾔﾏｸﾞﾁ ｹﾝ", "斎藤 / 経理", "Emily Chen", "長谷川 葵"]
ACCOUNTS = ["新聞図書費", "福利厚生費", "荷造運賃", "租税公課", "前払費用", "仮払金", "事業主貸", "車両費", "研修費", "販売促進費", "総務部", "第二営業課"]
TAX = ["課対仕入（控80）10%", "課税売上 10%", "非課税仕入", "対象外仕入", "課税仕入 8%（軽）", "不課税", "適格請求書", "控除対象外", "8%軽減"]
TEXTS = ["ﾃｽｳﾘﾖｳ", "11月 サーバー代", "立替精算（交通費）", "ご注文ありがとうございます", "再発送分", "ATM 引出", "口座振替 電気代",
         "please leave at door", "領収書あり", "返金処理済み", "振替 ｱｵｿﾞﾗ", "【至急】納期確認"]
CATS = [["入金", "出金"], ["済", "未"], ["通常", "決算"], ["voided", "authorized", "partially_paid", "paid"], ["0", "1", "3"],
        ["宅配便", "メール便", "店頭受取"], ["振替伝票", "入金伝票"], ["low", "medium", "high"], ["web", "pos", "shopify_draft_order"]]


def eval_value(rng, cls, ctx):
    if cls == "date":
        y, m, d = rng.randint(2020, 2026), rng.randint(1, 12), rng.randint(1, 28)
        f = ctx.setdefault("f", rng.randrange(6))
        return [f"{y}.{m:02d}.{d:02d}", f"{y}/{m}/{d} {rng.randint(0,23)}:{rng.randint(0,59):02d}", f"{y}-{m:02d}-{d:02d} {rng.randint(0,23):02d}:{rng.randint(0,59):02d}:00 +0900",
                f"{y}/{m:02d}/{d:02d}", f"{m:02d}/{d:02d}/{y}", f"{y}{m:02d}{d:02d}"][f]
    if cls == "amount":
        v = rng.choice([980, 1210, 3300, 15400, 220000, 54, 8, 1234567, 0, 45000])
        f = ctx.setdefault("f", rng.randrange(5))
        return [str(v), f"{v:,}", f"{v}.00", f"-{v}" if rng.random() < 0.3 else str(v), f"{v:,}円"][f]
    if cls == "quantity":
        return str(rng.choice([1, 1, 2, 3, 1, 5, 12, 1]))
    if cls == "rate":
        return rng.choice(["10%", "8%", "0.1", "0.08", "15.0%"]) if ctx.setdefault("f", rng.randrange(2)) == 0 else rng.choice(["10", "8", "0"])
    if cls == "id":
        f = ctx.setdefault("f", rng.randrange(6))
        n = rng.randint(1, 9999999)
        return [f"#{n % 100000}", f"{n:010d}", f"SKU-{n % 999:03d}-BLK", f"gid://shopify/Order/{n}", str(n % 5000 + 1), f"R{n % 10**6:06d}"][f]
    if cls == "org":
        return rng.choice(ORGS)
    if cls == "person":
        return rng.choice(PEOPLE)
    if cls == "product":
        return rng.choice(PRODUCTS)
    if cls == "account":
        return rng.choice(ACCOUNTS)
    if cls == "tax_class":
        return rng.choice(TAX)
    if cls == "text":
        return rng.choice(TEXTS)
    if cls == "category":
        return rng.choice(ctx.setdefault("pool", rng.choice(CATS)))
    if cls == "email":
        return rng.choice(["k.mori", "orders", "hello", "a.chen"]) + "@" + rng.choice(["example.org", "example.net", "mail.example.jp"])
    if cls == "phone":
        return rng.choice(["'09012345678", "03 1234 5678", "+819011112222", "0120-000-000", "080-1111-2222"])
    if cls == "address":
        f = ctx.setdefault("f", rng.randrange(5))
        return [rng.choice(["神奈川県横浜市西区みなと1-2-3", "宮城県仙台市青葉区一番町4-5"]), rng.choice(["220-0012", "9800811"]),
                rng.choice(["Kanagawa", "JP-14", "Miyagi"]), rng.choice(["ハイツ青葉 201", "Apt 3B", ""]), rng.choice(["JP", "Japan", "US"])][f]
    raise ValueError(cls)


def eval_column(rng, cls, n=10):
    ctx = {}
    return [eval_value(rng, cls, ctx) for _ in range(n)]
