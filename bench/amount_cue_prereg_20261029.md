# 通貨の手がかりの無い「金額」を不明にする：事前記録（2026-10-29 Claude）

- オーナー：「続けて」（2026-10-29）。
- きっかけ：新しい公開元の陣の件数↔金額の取り違え 28 列のうち、化石燃料のトン数・就業者数・kWh・汎用の wert などは、見出し・単位・値のどこにも通貨の手がかりが無いのに本体が amount（金額）と言っていた（`bench/unit_header_prereg_20261029.md` のきっかけ）。
- **この記録は、試しの結果を見る前に固定する**。封印セット・blind_set*・セット 3・5・7・b018 は使わない。

## 決まり（1 つだけ。動かすつまみは無い）
製品の形（recheck v1 → 検査役 v2 → ρ=0.8）の最後の判定が amount の列で、**見出し・同じ表の単位の例・値の先頭 5 件のどれにも通貨の手がかりが無ければ、不明にする**。同じ表のほかの列名は見ない（隣に「Amount」の列があるだけで手がかりにしないため）。

通貨の手がかり（大文字小文字を区別しない。語は単語の一部でもよい）：
- 記号・略号：£ $ € ¥ ￥ ₹ ₩ R$ CHF Fr. EUR USD GBP AUD CAD NZD JPY BRL
- 英語：amount・amt・cost・price・pay・paid・payment・spend・expend・expense・income・revenue・budget・salary・wage・fee・charge・tax・vat・grant・fund・value of・invoice・net・gross・total cost・euro・dollar・pound・sterling・cent
- ドイツ語・フランス語・スペイン語・ポルトガル語：betrag・kosten・preis・ausgaben・einnahmen・lohn・gehalt・franken・steuer・montant・coût・cout・prix・dépense・recette・salaire・valor・custo・preço・preco・receita・despesa・importe・gasto・ingreso
- 日本語：金額・円・費・価格・料・額・予算・支出・収入・税・単価・給与・報酬・売上

## 試し（学習なし・CPU）
- 新しい陣 8 つ（b015・b016・b017・b060・b062・b063・b064・b065）すべて、本体 C2 種子 1。決まりの前と後を同じ列で比べる。

## 採否（変えない）
- 8 陣の合計で、**重大が増えない**、**誤りの数が減る**、**正解率の下がりが 0.5 ポイント以内**の 3 つをすべて満たせば採る。
- 採ったら：製品の決め方に入れる（次に凍結する構成に入れる。凍結済みの C1 の記録は書き換えない）。
- 記録だけ：不明になった列のうち、本当は amount だった列（取りこぼし）と、本当は amount でなかった列（救った誤り）の数と見出し。

## 結果
（ここに書く。上の規則は変えない）
