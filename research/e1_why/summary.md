# E1 の誤りと不明の原因（`research/e1_why/analyze.py`、使い済みの陣。採否には使わない）

## L＋K2（3 本の合計 3645）

- 正しい：3147（86.3%）
- 不明・本体の 1 位は当たり（止めすぎ）：196（5.4%）
- 誤り・本体の 1 位のまま：156（4.3%）
- 不明・本体は外れ、正解は上位 3：121（3.3%）
- 不明・本体は外れ、正解は上位 3 の外：25（0.7%）

- 参考：本体の 1 位だけで答えたときの正しい 3341（91.7%）、最終 3147（86.3%）

### 止めすぎ：止めた理由（先頭の語）

- low_confidence_no_cue：45
- date_value_evidence_low：35
- verifier：30
- rate_without_cue：30
- cue_conflict：21
- period_header_no_unit：12
- amount_without_cue：10
- probability_below_threshold：7
- numeric_top2_too_close：3
- ：3

### 止めすぎ：正解の種類

- id：48
- date：46
- rate：42
- quantity：32
- amount：23
- address：2
- text：1
- org：1
- category：1

### 止めすぎ：本体の確率

- 0.5–0.8：21
- 0.8–0.95：45
- <0.5：7
- ≥0.95：123

### 誤り：最終 → 正解（上位）

- org → address：42
- category → id：19
- id → category：18
- address → category：12
- category → account：9
- category → org：9
- quantity → rate：7
- category → quantity：7
- category → date：5
- account → org：5
- category → text：5
- quantity → id：5
- quantity → amount：3
- category → product：3
- text → category：2

### 不明と誤りの言語

- en：405
- ja：93

### 不明と誤りが集まる表（上位 10）

- b109 ordpaye-paydashboard/tableaudebordpaye-paydashboard.csv：21
- b094 2003%2FSYWR_Point_count_data_Donnees_points_dEcoute.csv：16
- b107 3/State_and_Guest_of_Government_April_2014-Jan_2015.csv：15
- b100 catalog/datasets/sk-stat-70/exports/csv?use_labels=true：12
- b108 obase.canada.ca/src/data/covidLive/covid19-download.csv：12
- b108 data.tpsgc-pwgsc.gc.ca/ba1/auto-auth/auto-auth-2627.csv：12
- b111 /catalog/datasets/djs-stv-9/exports/csv?use_labels=true：12
- b094 c/data/covidLive/vaccination-coverage-byVaccineType.csv：11
- b100 /v2/catalog/datasets/100062/exports/csv?use_labels=true：10
- b108 wnload/nrc-peer-reviewed-publications-2018_fulltext.csv：10

## LV＋K2（3 本の合計 3645）

- 正しい：3164（86.8%）
- 不明・本体の 1 位は当たり（止めすぎ）：193（5.3%）
- 誤り・本体の 1 位のまま：158（4.3%）
- 不明・本体は外れ、正解は上位 3：107（2.9%）
- 不明・本体は外れ、正解は上位 3 の外：23（0.6%）

- 参考：本体の 1 位だけで答えたときの正しい 3351（91.9%）、最終 3164（86.8%）

### 止めすぎ：止めた理由（先頭の語）

- low_confidence_no_cue：39
- date_value_evidence_low：36
- verifier：33
- rate_without_cue：30
- cue_conflict：20
- period_header_no_unit：12
- amount_without_cue：9
- probability_below_threshold：8
- numeric_top2_too_close：3
- ：3

### 止めすぎ：正解の種類

- date：48
- id：46
- rate：43
- quantity：28
- amount：22
- category：6

### 止めすぎ：本体の確率

- 0.5–0.8：19
- 0.8–0.95：42
- <0.5：8
- ≥0.95：124

### 誤り：最終 → 正解（上位）

- org → address：44
- id → category：19
- category → id：19
- address → category：12
- category → account：10
- category → org：9
- quantity → rate：9
- quantity → id：6
- quantity → amount：5
- category → date：5
- account → org：4
- category → text：4
- category → product：4
- category → quantity：3
- org → product：1

### 不明と誤りの言語

- en：389
- ja：92

### 不明と誤りが集まる表（上位 10）

- b109 ordpaye-paydashboard/tableaudebordpaye-paydashboard.csv：22
- b094 2003%2FSYWR_Point_count_data_Donnees_points_dEcoute.csv：15
- b107 3/State_and_Guest_of_Government_April_2014-Jan_2015.csv：15
- b094 c/data/covidLive/vaccination-coverage-byVaccineType.csv：12
- b100 catalog/datasets/sk-stat-70/exports/csv?use_labels=true：12
- b108 obase.canada.ca/src/data/covidLive/covid19-download.csv：12
- b108 data.tpsgc-pwgsc.gc.ca/ba1/auto-auth/auto-auth-2627.csv：12
- b100 /v2/catalog/datasets/100062/exports/csv?use_labels=true：11
- b108 c/data/covidLive/vaccination-coverage-byVaccineType.csv：10
- b092 tachment_data/file/61946/workforce-scoping-exercise.csv：9

