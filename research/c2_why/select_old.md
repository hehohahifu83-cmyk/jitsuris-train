# C2 を選ぶ段：古い陣 23 個（C2 種子 1 の予測。決める陣・確かめる陣は使わない）

- 製品の形（F4・F8）。採点 4220 列：正しい 3603・不明 434・重大 3・ほか 180。

| 止めた理由 | 不明 | 1 位が正しい | 重大になる | ほかの誤り |
|---|---:|---:|---:|---:|
| other_class | 128 | 0 | 0 | 128 |
| low_confidence_no_cue | 60 | 45 | 5 | 10 |
| amount_without_cue | 57 | 30 | 26 | 1 |
| probability_below_threshold | 43 | 14 | 7 | 22 |
| rate_without_cue | 35 | 33 | 2 | 0 |
| verifier | 35 | 29 | 6 | 0 |
| cue_conflict | 25 | 20 | 4 | 1 |
| date_value_evidence_low | 23 | 22 | 0 | 1 |
| numeric_values_not_parseable | 16 | 13 | 0 | 3 |
| period_header_no_unit | 8 | 8 | 0 | 0 |
| numeric_top2_too_close | 2 | 0 | 2 | 0 |
| amount_precision | 2 | 2 | 0 | 0 |

| 理由 | 1 位 | < 0.70 | 0.70〜0.80 | 0.80〜0.90 | 0.90〜0.95 | 0.95 以上 |
|---|---|---|---|---|---|---|
| amount_without_cue | amount | 1／5／0 | 1／3／1 | 2／4／0 | 3／3／0 | 23／11／0 |
| date_value_evidence_low | date | 1／0／1 | — | 1／0／0 | 4／0／0 | 16／0／0 |
| low_confidence_no_cue | amount | — | 1／0／0 | — | — | — |
| low_confidence_no_cue | id | 3／0／6 | 0／0／1 | 8／1／1 | 3／0／1 | — |
| low_confidence_no_cue | quantity | 11／1／1 | 1／0／0 | 7／2／0 | 10／1／0 | — |
| low_confidence_no_cue | rate | — | — | — | 1／0／0 | — |
| probability_below_threshold | account | 1／0／5 | — | — | — | — |
| probability_below_threshold | address | 0／0／4 | — | — | — | — |
| probability_below_threshold | amount | 0／2／0 | — | — | — | — |
| probability_below_threshold | category | 6／0／2 | — | — | — | — |
| probability_below_threshold | date | 0／0／1 | — | — | — | — |
| probability_below_threshold | id | 0／1／1 | — | — | — | — |
| probability_below_threshold | org | 0／0／2 | — | — | — | — |
| probability_below_threshold | other | 0／0／4 | — | — | — | — |
| probability_below_threshold | quantity | 4／0／0 | — | — | — | — |
| probability_below_threshold | rate | 1／4／0 | — | — | — | — |
| probability_below_threshold | text | 2／0／3 | — | — | — | — |
| rate_without_cue | rate | 4／0／0 | 1／2／0 | 3／0／0 | 7／0／0 | 18／0／0 |
