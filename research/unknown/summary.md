# 不明になった列の調査：集計（`research/unknown/audit.py`）

- 新しい陣 8 つ・本体 C2・今の製品の形。採点の範囲（正解が other・person の列は除く）で不明 329 列（採点 2,852 列の 11.5%）
- 本体の 1 位が正解だった不明：170（52%）＝本体は分かっていたのに、決め方の段で不明になった列

| 不明にした段 | 列 | 正解の種類（多い順） |
|---|---:|---|
| 見張り（本体の段） | 162 | id 54, quantity 36, date 23, category 20, rate 12, amount 7 |
| recheck | 137 | quantity 44, amount 37, rate 23, id 21, category 7, date 4 |
| 検査役 | 26 | amount 13, quantity 6, id 5, rate 2 |
| 通貨の手がかり | 4 | quantity 2, amount 2 |

## 見張りの理由（本体の段で不明）

| 理由 | 列 |
|---|---:|
| other_class | 94 |
| probability_below_threshold | 32 |
| date_value_evidence_low | 24 |
| numeric_values_not_parseable | 10 |
| numeric_top2_too_close | 2 |

## recheck の理由

| 理由 | 列 |
|---|---:|
| amount_without_cue | 45 |
| low_confidence_no_cue | 29 |
| rate_without_cue | 24 |
| no_value_evidence | 18 |
| cue_conflict:amount | 10 |
| cue_conflict:date | 6 |
| cue_conflict:rate | 4 |
| cue_conflict:quantity | 1 |
