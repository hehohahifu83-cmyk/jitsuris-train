# 直し H の 1 つずつの確かめ（`research/h_why/ablate.py`。使い済みの陣、探索用。採否には使わない）

## 古い 23 陣（1 本の合計）

| 形 | 採点 | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|---:|
| P | 4220 | 3740 | 324 | 2 | 154 |
| P＋H1 | 4220 | 3732 | 324 | 2 | 162 |
| P＋H2 | 4220 | 3742 | 322 | 2 | 154 |
| P＋H | 4220 | 3734 | 322 | 2 | 162 |

P＋H が変えた出力：10（当たりに 2、それ以外に 8）

- 悪く・外れのまま：本1 b062-0191 [Input Sector code] 正解 id：id → category
- 悪く・外れのまま：本1 b062-0258 [Economic Category Code] 正解 id：id → category
- 悪く・外れのまま：本1 b063-0296 [gruppe_id] 正解 id：id → category
- 悪く・外れのまま：本1 b064-0296 [Geschäftsart ID] 正解 id：id → category
- 悪く・外れのまま：本1 b065-0198 [Input Sector code] 正解 id：id → category
- 悪く・外れのまま：本1 b025-0015 [NACE Code] 正解 id：id → category
- 悪く・外れのまま：本1 b025-0021 [Nace Code] 正解 id：id → category
- 悪く・外れのまま：本1 b053-0022 [System ID // ID systeme] 正解 id：id → category
- 当たり：本1 b065-0157 [Procurement Start Date] unknown → date
- 当たり：本1 b065-0158 [Contract Commencement Date] unknown → date

## 決める陣（3 本の合計）

| 形 | 採点 | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|---:|
| P | 3621 | 3239 | 209 | 4 | 169 |
| P＋H1 | 3621 | 3241 | 209 | 4 | 167 |
| P＋H2 | 3621 | 3248 | 200 | 4 | 169 |
| P＋H | 3621 | 3250 | 200 | 4 | 167 |

P＋H が変えた出力：17（当たりに 14、それ以外に 3）

- 悪く・外れのまま：本1 b080-0021 [Class Code] 正解 id：id → category
- 悪く・外れのまま：本2 b080-0021 [Class Code] 正解 id：id → category
- 悪く・外れのまま：本3 b080-0021 [Class Code] 正解 id：id → category
- 当たり：本1 b067-0123 [PERIOD] unknown → date
- 当たり：本1 b071-0028 [集計日] unknown → date
- 当たり：本1 b071-0058 [区分番号] id → category
- 当たり：本1 b072-0272 [measured_at] unknown → date
- 当たり：本2 b067-0123 [PERIOD] unknown → date
- 当たり：本2 b071-0028 [集計日] unknown → date
- 当たり：本2 b071-0058 [区分番号] id → category
- 当たり：本2 b072-0272 [measured_at] unknown → date
- 当たり：本3 b067-0123 [PERIOD] unknown → date
- 当たり：本3 b071-0028 [集計日] unknown → date
- 当たり：本3 b071-0058 [区分番号] id → category
- 当たり：本3 b072-0272 [measured_at] unknown → date
- 当たり：本3 b074-0261 [eigentuemer_typ_nr] id → category
- 当たり：本3 b078-0169 [whg_bauj_group_nr] id → category

## 確かめる陣（3 本の合計）

| 形 | 採点 | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|---:|
| P | 3741 | 3228 | 278 | 18 | 217 |
| P＋H1 | 3741 | 3264 | 278 | 18 | 181 |
| P＋H2 | 3741 | 3240 | 266 | 18 | 217 |
| P＋H | 3741 | 3276 | 266 | 18 | 181 |

P＋H が変えた出力：54（当たりに 51、それ以外に 3）

- 悪く・外れのまま：本1 b071-0095 [選択死因分類コード] 正解 id：id → category
- 悪く・外れのまま：本2 b071-0095 [選択死因分類コード] 正解 id：id → category
- 悪く・外れのまま：本3 b071-0095 [選択死因分類コード] 正解 id：id → category
- 当たり：本1 b067-0428 [VORLAGENART_ID] id → category
- 当たり：本1 b067-0432 [ABSTIMMUNGSART_ID] id → category
- 当たり：本1 b069-0009 [NACE_Code] id → category
- 当たり：本1 b069-0016 [NACE Code] id → category
- 当たり：本1 b072-0200 [gebaeudekategorie_code] id → category
- 当たり：本1 b072-0343 [VORLAGENART_ID] id → category
- 当たり：本1 b072-0347 [ABSTIMMUNGSART_ID] id → category
- 当たり：本1 b073-0285 [指定有効期限] unknown → date
- 当たり：本1 b073-0295 [指定有効期限] unknown → date
- 当たり：本1 b073-0304 [当初指定年月日] unknown → date
- 当たり：本1 b073-0305 [指定有効期限] unknown → date
- 当たり：本1 b074-0116 [Strassenbezeichnung Sprache Code] id → category
- 当たり：本1 b074-0175 [gebaeudekategorie_code] id → category
- 当たり：本1 b074-0182 [heizsystem_code] id → category
- 当たり：本1 b078-0056 [rechtsform_code] id → category
- 当たり：本1 b078-0062 [koordinatenherkunft_code] id → category
- 当たり：本1 b078-0064 [gebaeudestatus_code] id → category
- 当たり：本2 b067-0428 [VORLAGENART_ID] id → category
- 当たり：本2 b067-0432 [ABSTIMMUNGSART_ID] id → category
- 当たり：本2 b069-0009 [NACE_Code] id → category
- 当たり：本2 b069-0016 [NACE Code] id → category
- 当たり：本2 b072-0200 [gebaeudekategorie_code] id → category
- 当たり：本2 b072-0343 [VORLAGENART_ID] id → category
- 当たり：本2 b072-0347 [ABSTIMMUNGSART_ID] id → category
- 当たり：本2 b073-0285 [指定有効期限] unknown → date
- 当たり：本2 b073-0295 [指定有効期限] unknown → date
- 当たり：本2 b073-0304 [当初指定年月日] unknown → date
- 当たり：本2 b073-0305 [指定有効期限] unknown → date
- 当たり：本2 b074-0116 [Strassenbezeichnung Sprache Code] id → category
- 当たり：本2 b074-0175 [gebaeudekategorie_code] id → category
- 当たり：本2 b074-0182 [heizsystem_code] id → category
- 当たり：本2 b078-0056 [rechtsform_code] id → category
- 当たり：本2 b078-0062 [koordinatenherkunft_code] id → category
- 当たり：本2 b078-0064 [gebaeudestatus_code] id → category
- 当たり：本3 b067-0428 [VORLAGENART_ID] id → category
- 当たり：本3 b067-0432 [ABSTIMMUNGSART_ID] id → category
- 当たり：本3 b069-0009 [NACE_Code] id → category
- 当たり：本3 b069-0016 [NACE Code] id → category
- 当たり：本3 b072-0200 [gebaeudekategorie_code] id → category
- 当たり：本3 b072-0343 [VORLAGENART_ID] id → category
- 当たり：本3 b072-0347 [ABSTIMMUNGSART_ID] id → category
- 当たり：本3 b073-0285 [指定有効期限] unknown → date
- 当たり：本3 b073-0295 [指定有効期限] unknown → date
- 当たり：本3 b073-0304 [当初指定年月日] unknown → date
- 当たり：本3 b073-0305 [指定有効期限] unknown → date
- 当たり：本3 b074-0116 [Strassenbezeichnung Sprache Code] id → category
- 当たり：本3 b074-0175 [gebaeudekategorie_code] id → category
- 当たり：本3 b074-0182 [heizsystem_code] id → category
- 当たり：本3 b078-0056 [rechtsform_code] id → category
- 当たり：本3 b078-0062 [koordinatenherkunft_code] id → category
- 当たり：本3 b078-0064 [gebaeudestatus_code] id → category

## E1（3 本の合計）

| 形 | 採点 | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|---:|
| P | 3645 | 3214 | 282 | 9 | 140 |
| P＋H1 | 3645 | 3223 | 282 | 9 | 131 |
| P＋H2 | 3645 | 3225 | 271 | 9 | 140 |
| P＋H | 3645 | 3234 | 271 | 9 | 131 |

P＋H が変えた出力：20（当たりに 20、それ以外に 0）

- 当たり：本1 b094-0095 [Time_UTC_HHMMSS_Heure_UTC_HHMMSS] unknown → date
- 当たり：本1 b094-0143 [Naics code
Code Scian] id → category
- 当たり：本1 b100-0048 [Zeitliche Abdeckung] unknown → date
- 当たり：本1 b102-0207 [施行期間(年度)] unknown → date
- 当たり：本1 b108-0176 [Naics_code
Code_SCIAN] id → category
- 当たり：本1 b108-0205 [Mois - Months] unknown → date
- 当たり：本1 b111-0066 [fahrzeugart_code] id → category
- 当たり：本2 b094-0095 [Time_UTC_HHMMSS_Heure_UTC_HHMMSS] unknown → date
- 当たり：本2 b094-0143 [Naics code
Code Scian] id → category
- 当たり：本2 b100-0048 [Zeitliche Abdeckung] unknown → date
- 当たり：本2 b102-0207 [施行期間(年度)] unknown → date
- 当たり：本2 b108-0176 [Naics_code
Code_SCIAN] id → category
- 当たり：本2 b108-0205 [Mois - Months] unknown → date
- 当たり：本2 b111-0066 [fahrzeugart_code] id → category
- 当たり：本3 b094-0095 [Time_UTC_HHMMSS_Heure_UTC_HHMMSS] unknown → date
- 当たり：本3 b094-0143 [Naics code
Code Scian] id → category
- 当たり：本3 b100-0048 [Zeitliche Abdeckung] unknown → date
- 当たり：本3 b108-0176 [Naics_code
Code_SCIAN] id → category
- 当たり：本3 b108-0205 [Mois - Months] unknown → date
- 当たり：本3 b111-0066 [fahrzeugart_code] id → category

## E2（3 本の合計）

| 形 | 採点 | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|---:|
| P | 3759 | 3399 | 203 | 1 | 156 |
| P＋H1 | 3759 | 3410 | 203 | 1 | 145 |
| P＋H2 | 3759 | 3418 | 184 | 1 | 156 |
| P＋H | 3759 | 3429 | 184 | 1 | 145 |

P＋H が変えた出力：30（当たりに 30、それ以外に 0）

- 当たり：本1 b094-0049 [FR_MOIS] unknown → date
- 当たり：本1 b094-0056 [EN_QUARTER] unknown → date
- 当たり：本1 b094-0059 [FR_TRIMESTRE] unknown → date
- 当たり：本1 b094-0060 [FR_MOIS] unknown → date
- 当たり：本1 b094-0069 [FR_TRIMESTRE] unknown → date
- 当たり：本1 b094-0070 [FR_MOIS] unknown → date
- 当たり：本1 b100-0140 [hh_typ_nr] id → category
- 当たり：本1 b104-0038 [中分類コード] id → category
- 当たり：本1 b104-0039 [小分類コード] id → category
- 当たり：本1 b104-0040 [細分類コード] id → category
- 当たり：本1 b109-0082 [Period] unknown → date
- 当たり：本1 b111-0121 [noga082_id] id → category
- 当たり：本2 b094-0049 [FR_MOIS] unknown → date
- 当たり：本2 b094-0059 [FR_TRIMESTRE] unknown → date
- 当たり：本2 b094-0060 [FR_MOIS] unknown → date
- 当たり：本2 b094-0069 [FR_TRIMESTRE] unknown → date
- 当たり：本2 b094-0070 [FR_MOIS] unknown → date
- 当たり：本2 b104-0038 [中分類コード] id → category
- 当たり：本2 b104-0039 [小分類コード] id → category
- 当たり：本2 b104-0040 [細分類コード] id → category
- 当たり：本2 b109-0082 [Period] unknown → date
- 当たり：本2 b111-0121 [noga082_id] id → category
- 当たり：本3 b094-0049 [FR_MOIS] unknown → date
- 当たり：本3 b094-0059 [FR_TRIMESTRE] unknown → date
- 当たり：本3 b094-0060 [FR_MOIS] unknown → date
- 当たり：本3 b094-0069 [FR_TRIMESTRE] unknown → date
- 当たり：本3 b094-0070 [FR_MOIS] unknown → date
- 当たり：本3 b100-0129 [global_group_nr] id → category
- 当たり：本3 b109-0082 [Period] unknown → date
- 当たり：本3 b111-0121 [noga082_id] id → category

