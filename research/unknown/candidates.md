# 不明になった列の調査：手がかりの候補（`research/unknown/candidates.py`）

- **決める陣（不明 329 列そのもの）での参考値**。ここで作った候補なので当てはまりは良く見える。採るかどうかは事前記録を書いてから別の陣で確かめる
- 重大＝正解が数字の種類なのに別の種類にしたもの。「ChatGPT と同じ」は ChatGPT の答えと一致した数
- 合格線（不明 10% 以下）まで 44 列

| 候補 | 種類 | 当たった列 | 表 | 陣 | 正しい | 重大 | ほかの誤り | ChatGPT と同じ |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A 文字化けの £（｣→」）を通貨に | amount | 7 | 5 | 3 | 7 | 0 | 0 | 7 |
| A' 値の先頭が文字化けの £ | amount | 20 | 13 | 3 | 20 | 0 | 0 | 20 |
| B 列名の URI・URL と値が http の識別子 | id | 45 | 38 | 3 | 45 | 0 | 0 | 45 |
| C 列名の kWh・MWh・GWh・filesize | quantity | 12 | 5 | 3 | 12 | 0 | 0 | 12 |
| D1 ドイツ語の数量（anzahl・bestand・summe von・gemeinden・electorat） | quantity | 11 | 9 | 1 | 11 | 0 | 0 | 11 |
| D2 ドイツ語の率（prozent・quote・grad・beteiligung） | rate | 9 | 5 | 2 | 9 | 0 | 0 | 9 |
| D3 ドイツ語・スイスの金額（chf・betrag・ausgaben・kosten） | amount | 3 | 3 | 1 | 3 | 0 | 0 | 3 |
| D4 ドイツ語の日付（jahr・monat・datum・datierung）・pubdate | date | 7 | 5 | 2 | 7 | 0 | 0 | 7 |
| D5 ドイツ語の番号（_code・_nr・laufnummer） | id | 7 | 6 | 2 | 7 | 0 | 0 | 7 |
| E 英語の金額の語（value of・contract value・paybill・surplus amount・income amount） | amount | 9 | 9 | 3 | 9 | 0 | 0 | 9 |
| F 英語の率（percent が語の中・per 1000） | rate | 4 | 2 | 2 | 4 | 0 | 0 | 4 |

- すべての候補を合わせると：答えになる列 **130**（91 表から。正しい 130・重大 0・ほかの誤り 0）。2 つの種類が当たって決めない列 0
- 不明 329 → 199（採点 2852 列の 7.0%）。正解率は 130 列ぶん上がる


## 候補で拾えず、ChatGPT は正しく決めた列（理由・正解の種類、多い順）

| 理由 | 正解 | 列 |
|---|---|---:|
| rate_without_cue | rate | 15 |
| date_value_evidence_low | date | 15 |
| amount_without_cue | quantity | 12 |
| other_class | quantity | 10 |
| amount_without_cue | amount | 10 |
| no_value_evidence | quantity | 9 |
| probability_below_threshold | category | 9 |
| other_class | id | 8 |
| cue_conflict:amount | id | 7 |
| other_class | rate | 6 |
| low_confidence_no_cue | quantity | 5 |
| verifier:quantity | amount | 5 |
| verifier:quantity | quantity | 5 |
| low_confidence_no_cue | id | 4 |
| probability_below_threshold | text | 3 |
| numeric_values_not_parseable | category | 3 |
| probability_below_threshold | quantity | 3 |
| other_class | category | 3 |
| verifier:quantity | rate | 2 |
| cue_conflict:rate | id | 2 |
