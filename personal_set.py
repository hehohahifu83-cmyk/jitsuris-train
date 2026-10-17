"""「AIの卵」の評価用：店ごとのくせのある列名（Claude が作った架空のもの。公開資料ではない）。
種類は手で付けた。学習用の gen.py にも評価用の eval_set.py にも入れていない。"""
PERSONAL = [
    ("ｳﾘｱｹﾞ", "amount"), ("うりあげ", "amount"), ("品代", "amount"), ("入金予定", "amount"), ("見込", "amount"), ("立替", "amount"),
    ("先方", "org"), ("相手先", "org"), ("卸元", "org"), ("ご依頼主", "person"), ("送り人", "person"), ("ｶﾅ", "person"),
    ("K-CODE", "id"), ("管理No2", "id"), ("ｼﾘｱﾙ", "id"), ("票番", "id"), ("ﾁｹｯﾄ", "id"), ("入数2", "quantity"), ("ケース", "quantity"),
    ("発注残", "quantity"), ("戻り", "quantity"), ("処理", "category"), ("ランク2", "category"), ("曜", "category"), ("Ｔ番号", "id"),
    ("年月", "date"), ("出", "date"), ("計上", "date"), ("ネタ", "product"), ("中身", "product"), ("経費の種類", "account"),
    ("課非", "tax_class"), ("ひとこと", "text"), ("ﾒｰﾙｱﾄﾞ", "email"), ("れんらくさき", "phone"), ("送り先", "address"),
]
