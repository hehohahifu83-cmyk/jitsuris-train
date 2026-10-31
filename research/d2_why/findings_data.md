# D2 の原因の数字（`research/d2_why/analyze.py`）

- 採点 1210 列。安定して変わった列＝3 本中の正しい本数の差が 2 以上。

## 1. A→L で安定して変わった列：良くなった 14・悪くなった 4（差 +10）

### 種子のゆれの基準（6 本を 3 本ずつに分ける 10 通り。差＝後ろの 3 本 − 前の 3 本）

| 前の 3 本 | 安定した差（列） | 正しいの合計の差（本×列） |
|---|---:|---:|
| A1・A2・A3 | +10 | +26 |
| A1・L1・L2 | -9 | -22 |
| A1・L1・L3 | -6 | -10 |
| A1・A2・L1 | -5 | +2 |
| A1・A3・L3 | +5 | +14 |
| A1・A2・L3 | +4 | +10 |
| A1・A3・L1 | -3 | +6 |
| A1・A3・L2 | +3 | +2 |
| A1・L2・L3 | +2 | -14 |
| A1・A2・L2 | +1 | -2 |

### 良くなった列

- 正解：category 13、quantity 1
- 本体の 1 位（A の多数 → L の多数）：id→category 12、category→category 1、quantity→quantity 1
- 列名が KIND×CODE（v24 の形）：True 11、False 3
- 言語：en 11、ja 3
- 陣：b074 4、b078 4、b090 3、b067 1、b072 1、b076 1
- 正解の先生：Claude 裁定（answers_final） 13、ChatGPT（抜き取り裁定のみ） 1

| id | 列名 | 値（先頭 5） | 正解 | A の 1 位 | L の 1 位 | A 正 | L 正 |
|---|---|---|---|---|---|---:|---:|
| b067-0233 | Geschäftsart ID | 8 / 5 / 6 / 2 / 5 | category | id,id,id | category,category,category | 0 | 3 |
| b072-0297 | group_nr | 99 / 4 / 3 / 1 / 1 | category | id,id,id | category,category,category | 0 | 3 |
| b074-0015 | georegion_type | canton / CHFL / CHFL / CHFL / CHFL | category | category,category,address | category,category,category | 1 | 3 |
| b074-0054 | Antwort | a77 / a78 / a77 / a77 / a77 | category | id,id,id | category,id,category | 0 | 2 |
| b074-0261 | eigentuemer_typ_nr | 1 / 2 / 0 / 2 / 0 | category | id,id,id | category,category,id | 0 | 2 |
| b074-0272 | group_nr | 5 / 1 / 4 / 99 / 3 | category | id,id,id | category,category,category | 0 | 3 |
| b076-0020 | popExtrapolation | 165475.9 / NA / NA / 163499.3 / 193303.8 | quantity | quantity,quantity,quantity | quantity,quantity,quantity | 0 | 2 |
| b078-0157 | inserat_art_nr | 2 / 1 / 2 / 1 / 2 | category | id,id,id | category,category,category | 0 | 3 |
| b078-0169 | whg_bauj_group_nr | 2 / 1 / 1 / 2 / 1 | category | id,id,id | category,category,id | 0 | 2 |
| b078-0172 | group_nr | 2 / 6 / 5 / 5 / 5 | category | id,id,id | category,category,category | 0 | 3 |
| b078-0182 | group_nr | 3 / 2 / 6 / 3 / 2 | category | id,id,id | category,category,category | 0 | 3 |
| b090-0079 | POIコード | 1309 / 1305 / 1309 / 1404 / 1309 | category | id,id,id | category,category,category | 0 | 3 |
| b090-0141 | POIコード | 809 / 1003 / 1402 / 1599 / 1215 | category | id,id,id | category,category,category | 0 | 3 |
| b090-0338 | POIコード | 2004a / 0801a / 2004a / 1304a / 1017a | category | id,id,id | category,category,category | 0 | 3 |

### 悪くなった列

- 正解：id 4
- 本体の 1 位（A の多数 → L の多数）：id→category 2、id→id 1、id→address 1
- 列名が KIND×CODE（v24 の形）：False 2、True 2
- 言語：ja 3、en 1
- 陣：b073 3、b069 1
- 正解の先生：Claude 裁定（answers_final） 3、ChatGPT（抜き取り裁定のみ） 1

| id | 列名 | 値（先頭 5） | 正解 | A の 1 位 | L の 1 位 | A 正 | L 正 |
|---|---|---|---|---|---|---:|---:|
| b069-0051 | CoverageID | 3 / 1 / 2 / 3 / 3 | id | id,id,id | id,id,id | 3 | 0 |
| b073-0044 | 台帳番号2(敷地) | 381 / 541 / 853 / 665 / 652 | id | id,id,id | id,address,address | 3 | 1 |
| b073-0116 | POIコード | 1016 / 1110 / 1116 / 1116 / 1499 | id | id,id,id | category,category,category | 3 | 0 |
| b073-0195 | POIコード | 1509 / 1505 / 1509 / 1201 / 1505 | id | id,id,id | category,category,category | 3 | 0 |

## 2. 重大の列（数値どうしの言い切りの誤り）

| 名前 | id | 列名 | 正解 | 最終 |
|---|---|---|---|---|
| A1 | b072-0182 | Angebotsstufe Code | quantity | id（本体） |
| A1 | b074-0066 | GEO_COMM_WORK | id | quantity（本体） |
| A1 | b085-0042 | 2012/13 1 | amount | quantity（本体） |
| A2 | b071-0090 | 地域等 | id | quantity（本体） |
| A2 | b085-0042 | 2012/13 1 | amount | quantity（本体） |
| A3 | b072-0182 | Angebotsstufe Code | quantity | id（本体） |
| A3 | b074-0066 | GEO_COMM_WORK | id | quantity（本体） |
| A3 | b085-0042 | 2012/13 1 | amount | quantity（本体） |
| L1 | b074-0066 | GEO_COMM_WORK | id | quantity（本体） |
| L2 | b067-0115 | Settimana | date | quantity（本体） |
| L3 | b071-0090 | 地域等 | id | quantity（本体） |
| L3 | b074-0066 | GEO_COMM_WORK | id | quantity（本体） |

## 3. 列名が KIND×CODE の列（16 列）とそれ以外での正しい（3 本の平均）

| 範囲 | 列 | A | L | 差（列） |
|---|---:|---:|---:|---:|
| KIND×CODE | 16 | 3.0 | 11.3 | +8.3 |
| それ以外 | 1194 | 1049.7 | 1050.0 | +0.3 |
| 正解 id | 196 | 163.3 | 157.3 | -6.0 |
| 正解 category | 358 | 314.0 | 327.3 | +13.3 |
