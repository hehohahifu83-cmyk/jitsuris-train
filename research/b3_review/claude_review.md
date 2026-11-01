# 古い陣の種類のコードの見直し：Claude の確かめ（2026-11-01）

対象：ChatGPT の `sheet.tsv` 42 行（`label_b3`）。LABEL_GUIDE v2.3 の B3・B7・B9 で全行を読んだ。

## 結論
- **42 行のうち 41 行に賛成**（category 36・id 4・account 1）。NAICS・NACE・ANZSIC・種類／状態／区分のコード → category、Class ID・System ID・Form ID のように個々の物を指す番号 → id、予算の経済区分（b062#170 Economic Category Code）→ account（B7 の「予算の経済分類」）。
- **違う 1 行：b063#284 `gruppe_id`**。ChatGPT は unknown。同じ表に名前の列 `gruppe` と、個々の分析項目の `analyt_id`・`analyt` がある。gruppe は分析項目をまとめる区分（項目の種類）で、個々の物ではないので、Claude は **category**。ただし別表のグループを指す鍵と読む余地はあり、unknown も誤りとは言わない。
- 変わる行：ChatGPT の案で 32 行（id→category 30・id→account 1・id→unknown 1）。Claude の案だと id→category 31・id→account 1。

## 次
- オーナーに：教材庫の古いラベルを B3 で付け直すか（学び直しを伴う）。付け直すなら、同じ意味の列（列名の語：NACE・NAICS・ANZSIC・〜_type_code・〜status_code・〜区分コード・〜Category Code）を教材庫全体から決まった方法で拾い、同じ 2 人の確かめをする。
