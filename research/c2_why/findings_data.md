# C2：不明になった列の理由と、本体の 1 位を言い切った場合（L 種子 1〜3 の合計、決める陣）

| 止めた理由 | 不明の列（3 本の合計） | 1 位が正しい | 1 位が重大になる | 1 位がほかの誤り | 言い切ったときの差し引き（正しい − 重大×3 − ほか） |
|---|---:|---:|---:|---:|---:|
| low_confidence_no_cue | 97 | 67 | 10 | 20 | +17 |
| other_class | 36 | 0 | 0 | 36 | -36 |
| date_value_evidence_low | 28 | 20 | 3 | 5 | +6 |
| amount_without_cue | 26 | 21 | 5 | 0 | +6 |
| probability_below_threshold | 24 | 9 | 3 | 12 | -12 |
| verifier | 18 | 9 | 5 | 4 | -10 |
| rate_without_cue | 14 | 12 | 2 | 0 | +6 |
| period_header_no_unit | 12 | 0 | 12 | 0 | -36 |
| numeric_values_not_parseable | 10 | 4 | 0 | 6 | -2 |
| amount_precision | 3 | 3 | 0 | 0 | +3 |
| cue_conflict | 3 | 3 | 0 | 0 | +3 |
| numeric_top2_too_close | 2 | 0 | 2 | 0 | -6 |

## 自信が足りないだけで止めた理由：本体の 1 位の種類 × 1 位の確率ごと（3 本の合計。正しい／重大／ほか）

| 理由 | 1 位 | < 0.70 | 0.70〜0.80 | 0.80〜0.90 | 0.90〜0.95 | 0.95 以上 |
|---|---|---|---|---|---|---|
| low_confidence_no_cue | id | 6／0／7 | 7／0／1 | 12／0／5 | 18／0／1 | — |
| low_confidence_no_cue | quantity | 4／1／3 | 4／0／0 | 4／4／1 | 11／5／2 | — |
| low_confidence_no_cue | rate | — | — | — | 1／0／0 | — |
| amount_without_cue | amount | 0／2／0 | 0／2／0 | 1／1／0 | 2／0／0 | 18／0／0 |
| rate_without_cue | rate | 0／1／0 | 0／1／0 | 1／0／0 | 3／0／0 | 8／0／0 |
| date_value_evidence_low | date | 0／1／2 | — | 2／0／0 | 0／2／0 | 18／0／3 |

## low_confidence_no_cue

| 本 | id | 列名 | 正解 | 1 位 | 1 位の確率 | 値 |
|---|---|---|---|---|---:|---|
| L1 | b066-0015 | OrganisationLabel | id | id | 0.638 | 23UB / 23UB / 23UB / 23UB |
| L1 | b067-0211 | nasak_anlage_nationale_bedeutu | category | quantity | 0.651 | 0 / 0 / 0 / 1 |
| L1 | b067-0358 | bruttolastgang_kwh | quantity | quantity | 0.949 | 127023.313 / 119504.252 / 46798.272 / 65897.216 |
| L1 | b069-0051 | CoverageID | id | id | 0.875 | 3 / 1 / 2 / 3 |
| L1 | b072-0091 | INDICATORS | id | id | 0.919 | Ind_01_01 / Ind_01_01 / Ind_01_01 / Ind_01_01 |
| L1 | b072-0093 | VALUE | quantity | quantity | 0.885 | 4661 / 1178 / 43632 / 1505 |
| L1 | b072-0098 | UNIT_MES | category | id | 0.74 | UM_26 / UM_2 / UM_2 / UM_18 |
| L1 | b072-0161 | gewicht_grp | category | quantity | 0.501 | 7 / 7 / 6 / 6 |
| L1 | b072-0163 | alter_mutter_cd | category | id | 0.818 | 1 / 2 / 2 / 2 |
| L1 | b072-0165 | gestations_alter_grp | category | quantity | 0.906 | 9 / 9 / 9 / 9 |
| L1 | b072-0285 | quartier_bfs_nr | id | id | 0.914 | 290 / 290 / 430 / 730 |
| L1 | b072-0294 | bilanz_view_nr | category | id | 0.933 | 3 / 2 / 3 / 1 |
| L1 | b072-0307 | quartier_bfs_nr | id | id | 0.906 | 160 / 640 / 330 / 220 |
| L1 | b073-0047 | 階数 地上(棟) | quantity | quantity | 0.887 | 7 / 4 / 6 / 3 |
| L1 | b073-0048 | 階数 地下(棟) | quantity | quantity | 0.937 | 1 / 1 / 2 / 1 |
| L1 | b074-0033 | Wert | quantity | quantity | 0.704 | 9161104 / 12246495 / 14779550 / 14813997 |
| L1 | b074-0063 | GEO_CANT_RESID | id | id | 0.844 | 1 / 1 / 1 / 1 |
| L1 | b074-0080 | GEO_CANT_RESID | id | id | 0.83 | 1 / 1 / 1 / 1 |
| L1 | b074-0154 | Strassennummer | id | id | 0.92 | A 13 / A 3 / A 1 / A 3 |
| L1 | b074-0247 | quartier_bfs_nr | id | id | 0.91 | 620 / 340 / 160 / 640 |
| L1 | b074-0267 | quartier_bfs_nr | id | id | 0.913 | 120 / 140 / 240 / 160 |
| L1 | b076-0019 | value | quantity | quantity | 0.627 | 0 / 2137.2 / 2191.6 / 1408.3 |
| L1 | b078-0024 | VARIABLE | id | id | 0.855 | wcapt_sout / wcapt_t / deb_hj_moy / deb_hj_max |
| L1 | b078-0142 | Gewicht in t | quantity | quantity | 0.77 | 3.71 / 4.7 / 4.33 / 238.35 |
| L1 | b078-0165 | stadtkreis_bfs_nr | id | id | 0.94 | 3 / 2 / 2 / 5 |
| L1 | b078-0167 | quartier_bfs_nr | id | id | 0.891 | 310 / 230 / 220 / 110 |
| L1 | b078-0177 | quartier_bfs_nr | id | id | 0.897 | 320 / 270 / 315 / 320 |
| L1 | b085-0042 | 2012/13 1 | amount | quantity | 0.922 | 1 025 431 / 4 169 389 / 220 220 / 424 145 |
| L1 | b088-0024 | Memory | quantity | quantity | 0.925 | 4096 / 8192 / 8192 / 8192 |
| L1 | b088-0025 | HDD/SSD | quantity | quantity | 0.667 | 238472 / 244191 / 238472 / 476937 |
| L1 | b089-0003 | Fleet | quantity | quantity | 0.94 | 2433 / 3491 / 3803 / 4861 |
| L1 | b090-0073 | # | id | quantity | 0.658 | 57 / 56 / 51 / 23 |
| L2 | b067-0042 | parameter | category | id | 0.63 | PN[5-100nm] / PN[5-100nm] / PN[5-100nm] / PN[5-100nm] |
| L2 | b067-0133 | INDICATORS | id | id | 0.945 | Ind_04_01 / Ind_01_08 / Ind_13_02 / Ind_01_03 |
| L2 | b067-0225 | quartiergruppen | id | id | 0.718 | 25 / 13 / 31 / 23 |
| L2 | b069-0049 | AreaCode | id | id | 0.759 | CKST / NAT / SLWC / DML |
| L2 | b069-0051 | CoverageID | id | id | 0.917 | 3 / 1 / 2 / 3 |
| L2 | b071-0090 | 地域等 | id | quantity | 0.906 | 226 / 229 / 647 / 341 |
| L2 | b072-0070 | total_per_day | quantity | quantity | 0.937 | 34451.0 / 34504.0 / 34465.0 / 34465.0 |
| L2 | b072-0093 | VALUE | quantity | quantity | 0.932 | 4661 / 1178 / 43632 / 1505 |
| L2 | b072-0097 | INDICATORS | id | id | 0.912 | Ind_17_03 / Ind_04_08 / Ind_19_02 / Ind_01_14 |
| L2 | b072-0098 | UNIT_MES | category | id | 0.575 | UM_26 / UM_2 / UM_2 / UM_18 |
| L2 | b072-0103 | GEO_CANT | id | id | 0.783 | 1 / 2 / 1 / 2 |
| L2 | b072-0165 | gestations_alter_grp | category | quantity | 0.935 | 9 / 9 / 9 / 9 |
| L2 | b072-0294 | bilanz_view_nr | category | id | 0.852 | 3 / 2 / 3 / 1 |
| L2 | b073-0052 | 項別(棟) | id | id | 0.945 | 503 / 161 / 501 / 161 |
| L2 | b073-0053 | 項別(棟)名 | category | id | 0.869 | １６項イ / １６項イ / １６項イ / １６項ロ |
| L2 | b074-0063 | GEO_CANT_RESID | id | id | 0.861 | 1 / 1 / 1 / 1 |
| L2 | b074-0065 | GEO_CANT_WORK | id | id | 0.573 | 1 / 1 / 1 / 1 |
| L2 | b074-0066 | GEO_COMM_WORK | id | id | 0.792 | 35 / 2 / 14 / 53 |
| L2 | b074-0080 | GEO_CANT_RESID | id | id | 0.851 | 1 / 1 / 1 / 1 |
| L2 | b074-0082 | GEO_CANT_WORK | id | id | 0.765 | 1 / 1 / 19 / 1 |
| L2 | b074-0154 | Strassennummer | id | id | 0.656 | A 13 / A 3 / A 1 / A 3 |
| L2 | b074-0159 | TAG | date | quantity | 0.844 | 366 / 31 / 164 / 95 |
| L2 | b074-0229 | pdf | category | quantity | 0.633 | 0 / 0 / 0 / 0 |
| L2 | b076-0019 | value | quantity | quantity | 0.653 | 0 / 2137.2 / 2191.6 / 1408.3 |
| L2 | b076-0033 | SPDEPS | id | id | 0.694 | SPBENEFNORER / SPBENEFNORER / SPBENEFNORER / SPBENEFNORER |
| L2 | b076-0034 | UNIT | category | id | 0.564 | MIO_NAC / MIO_NAC / MIO_NAC / MIO_NAC |
| L2 | b076-0091 | Tag_Nr | id | id | 0.507 | 5 / 1 / 3 / 4 |
| L2 | b076-0100 | Tag_NR | id | id | 0.811 | 4 / 3 / 4 / 5 |
| L2 | b077-0003 | RANG_GDE | category | id | 0.687 | 432 / 163 / 250 / 328 |
| L2 | b077-0005 | PCT_GDE | rate | rate | 0.921 | 0.20 / 0.04 / 0.15 / 0.03 |
| L2 | b078-0024 | VARIABLE | id | id | 0.847 | wcapt_sout / wcapt_t / deb_hj_moy / deb_hj_max |
| L2 | b078-0042 | VARIABLE | id | id | 0.781 | pen_t / voit_tour / txmot / voit_tour |
| L2 | b078-0159 | whg_neualt_nr | category | id | 0.625 | 2 / 1 / 2 / 0 |
| L2 | b085-0042 | 2012/13 1 | amount | quantity | 0.939 | 1 025 431 / 4 169 389 / 220 220 / 424 145 |
| L2 | b088-0024 | Memory | quantity | quantity | 0.681 | 4096 / 8192 / 8192 / 8192 |
| L2 | b088-0025 | HDD/SSD | quantity | quantity | 0.768 | 238472 / 244191 / 238472 / 476937 |
| L3 | b066-0015 | OrganisationLabel | id | id | 0.873 | 23UB / 23UB / 23UB / 23UB |
| L3 | b066-0017 | OrganisationLabel_2 | id | id | 0.777 | 23UB / 23UB / 23UB / 23UB |
| L3 | b067-0115 | Settimana | date | quantity | 0.948 | 19 / 11 / 20 / 16 |
| L3 | b069-0049 | AreaCode | id | id | 0.545 | CKST / NAT / SLWC / DML |
| L3 | b069-0051 | CoverageID | id | id | 0.919 | 3 / 1 / 2 / 3 |
| L3 | b072-0070 | total_per_day | quantity | quantity | 0.934 | 34451.0 / 34504.0 / 34465.0 / 34465.0 |
| L3 | b072-0092 | UNIT_MES | category | id | 0.895 | UM_6 / UM_6 / UM_6 / UM_6 |
| L3 | b072-0093 | VALUE | quantity | quantity | 0.702 | 4661 / 1178 / 43632 / 1505 |
| L3 | b072-0103 | GEO_CANT | id | id | 0.929 | 1 / 2 / 1 / 2 |
| L3 | b073-0048 | 階数 地下(棟) | quantity | quantity | 0.935 | 1 / 1 / 2 / 1 |
| L3 | b073-0052 | 項別(棟) | id | id | 0.915 | 503 / 161 / 501 / 161 |
| L3 | b073-0053 | 項別(棟)名 | category | id | 0.83 | １６項イ / １６項イ / １６項イ / １６項ロ |
| L3 | b074-0033 | Wert | quantity | quantity | 0.939 | 9161104 / 12246495 / 14779550 / 14813997 |
| L3 | b074-0063 | GEO_CANT_RESID | id | id | 0.933 | 1 / 1 / 1 / 1 |
| L3 | b074-0065 | GEO_CANT_WORK | id | quantity | 0.882 | 1 / 1 / 1 / 1 |
| L3 | b074-0080 | GEO_CANT_RESID | id | id | 0.914 | 1 / 1 / 1 / 1 |
| L3 | b074-0146 | age | quantity | quantity | 0.938 | 57 / 70 / 41 / 6 |
| L3 | b074-0149 | gdenr | id | id | 0.938 | 3217 / 3216 / 3216 / 3215 |
| L3 | b074-0153 | ZST | id | quantity | 0.813 | 600 / 604 / 82 / 602 |
| L3 | b074-0159 | TAG | date | quantity | 0.808 | 366 / 31 / 164 / 95 |
| L3 | b074-0261 | eigentuemer_typ_nr | category | id | 0.668 | 1 / 2 / 0 / 2 |
| L3 | b076-0019 | value | quantity | quantity | 0.853 | 0 / 2137.2 / 2191.6 / 1408.3 |
| L3 | b076-0020 | popExtrapolation | quantity | quantity | 0.929 | 165475.9 / NA / NA / 163499.3 |
| L3 | b076-0091 | Tag_Nr | id | id | 0.927 | 5 / 1 / 3 / 4 |
| L3 | b078-0033 | VARIABLE | id | id | 0.864 | ept_bra_mas / acc_sich / etab_ecul_ku / etab_ecul_ar |
| L3 | b078-0169 | whg_bauj_group_nr | category | id | 0.542 | 2 / 1 / 1 / 2 |
| L3 | b078-0179 | haushalt_wohndauer_nr | category | quantity | 0.897 | 2 / 0 / 2 / 0 |
| L3 | b085-0042 | 2012/13 1 | amount | quantity | 0.919 | 1 025 431 / 4 169 389 / 220 220 / 424 145 |
| L3 | b088-0024 | Memory | quantity | quantity | 0.865 | 4096 / 8192 / 8192 / 8192 |

## other_class

| 本 | id | 列名 | 正解 | 1 位 | 1 位の確率 | 値 |
|---|---|---|---|---|---:|---|
| L1 | b067-0125 | DIMENSION | id | other | 0.831 | 30106_dim02 / 30106_dim06 / 30106_T / 30106_dim16 |
| L1 | b067-0346 | Passanten in Richtung Neumarkt | quantity | other | 0.57 | 19.0 / 41.0 / 1.0 / 34.0 |
| L1 | b067-0347 | Passanten in Richtung Multerga | quantity | other | 0.533 | 62.0 / 8.0 / 26.0 / 49.0 |
| L1 | b072-0061 | Vogelart | category | other | 0.961 | Stockente / Lachmöwe / Blässhuhn / Lachmöwe |
| L1 | b072-0177 | Fahrplanfeld | id | other | 0.985 | 80.701 / 80.331 / 80.792 (m.Bu / 735 |
| L1 | b072-0180 | Kurspaare Sa | org | other | 0.764 | 8.0 / 30.0 / 0.0 / 2.0 |
| L1 | b072-0275 | location | address | other | 0.985 | {"coordinate / {"coordinate / {"coordinate / {"coordinate |
| L1 | b074-0040 | emission | quantity | other | 0.933 | 0 / 0 / 0 / 0 |
| L1 | b076-0097 | Gewicht in kg (ca.) | quantity | other | 0.602 | 5.0 / 5.0 / 60.0 / 20.0 |
| L2 | b072-0061 | Vogelart | category | other | 0.96 | Stockente / Lachmöwe / Blässhuhn / Lachmöwe |
| L2 | b072-0161 | gewicht_grp | category | other | 0.674 | 7 / 7 / 6 / 6 |
| L2 | b072-0177 | Fahrplanfeld | id | other | 0.987 | 80.701 / 80.331 / 80.792 (m.Bu / 735 |
| L2 | b072-0179 | Kurspaare Mo-Fr | id | other | 0.578 | 3.0 / 37.0 / 49.5 / 2.5 |
| L2 | b072-0180 | Kurspaare Sa | org | other | 0.536 | 8.0 / 30.0 / 0.0 / 2.0 |
| L2 | b072-0181 | Kurspaare So | quantity | other | 0.566 | 19.0 / 17.0 / 9.0 / 31.0 |
| L2 | b072-0275 | location | address | other | 0.988 | {"coordinate / {"coordinate / {"coordinate / {"coordinate |
| L2 | b074-0040 | emission | quantity | other | 0.886 | 0 / 0 / 0 / 0 |
| L2 | b076-0097 | Gewicht in kg (ca.) | quantity | other | 0.871 | 5.0 / 5.0 / 60.0 / 20.0 |
| L2 | b078-0142 | Gewicht in t | quantity | other | 0.532 | 3.71 / 4.7 / 4.33 / 238.35 |
| L3 | b067-0120 | Lim_inf | quantity | other | 0.655 | 136 / 1097 / 139 / 133 |
| L3 | b067-0125 | DIMENSION | id | other | 0.966 | 30106_dim02 / 30106_dim06 / 30106_T / 30106_dim16 |
| L3 | b072-0061 | Vogelart | category | other | 0.969 | Stockente / Lachmöwe / Blässhuhn / Lachmöwe |
| L3 | b072-0069 | diff | quantity | other | 0.553 | -585 / -13 / -3 / 387 |
| L3 | b072-0161 | gewicht_grp | category | other | 0.747 | 7 / 7 / 6 / 6 |
| L3 | b072-0177 | Fahrplanfeld | id | other | 0.954 | 80.701 / 80.331 / 80.792 (m.Bu / 735 |
| L3 | b072-0179 | Kurspaare Mo-Fr | id | other | 0.852 | 3.0 / 37.0 / 49.5 / 2.5 |
| L3 | b072-0180 | Kurspaare Sa | org | other | 0.942 | 8.0 / 30.0 / 0.0 / 2.0 |
| L3 | b072-0181 | Kurspaare So | quantity | other | 0.97 | 19.0 / 17.0 / 9.0 / 31.0 |
| L3 | b072-0275 | location | address | other | 0.983 | {"coordinate / {"coordinate / {"coordinate / {"coordinate |
| L3 | b074-0040 | emission | quantity | other | 0.759 | 0 / 0 / 0 / 0 |
| L3 | b076-0029 | value | quantity | other | 0.571 | 8 / 0 / NA / 68 |
| L3 | b076-0097 | Gewicht in kg (ca.) | quantity | other | 0.911 | 5.0 / 5.0 / 60.0 / 20.0 |
| L3 | b077-0005 | PCT_GDE | rate | other | 0.691 | 0.20 / 0.04 / 0.15 / 0.03 |
| L3 | b078-0024 | VARIABLE | id | other | 0.627 | wcapt_sout / wcapt_t / deb_hj_moy / deb_hj_max |
| L3 | b078-0142 | Gewicht in t | quantity | other | 0.537 | 3.71 / 4.7 / 4.33 / 238.35 |
| L3 | b088-0025 | HDD/SSD | quantity | other | 0.512 | 238472 / 244191 / 238472 / 476937 |

## date_value_evidence_low

| 本 | id | 列名 | 正解 | 1 位 | 1 位の確率 | 値 |
|---|---|---|---|---|---:|---|
| L1 | b067-0115 | Settimana | date | date | 0.96 | 19 / 11 / 20 / 16 |
| L1 | b067-0123 | PERIOD | date | date | 0.979 | 2018-04-01/2 / 2005-10-01/2 / 2018-04-01/2 / 2012-04-01/2 |
| L1 | b067-0215 | monat | date | date | 0.987 | 7 / 9 / 9 / 9 |
| L1 | b071-0028 | 集計日 | date | date | 0.979 | 42735 / 42735 / 42735 / 42735 |
| L1 | b072-0272 | measured_at | date | date | 0.988 | 1723010401.6 / 1724457600.0 / 1725537600.0 / 1720990800.5 |
| L1 | b072-0299 | monat | date | date | 0.986 | 12 / 12 / 12 / 12 |
| L1 | b073-0206 | 年No. | id | date | 0.907 | 466 / 667 / 16 / 278 |
| L1 | b074-0159 | TAG | date | date | 0.87 | 366 / 31 / 164 / 95 |
| L1 | b074-0161 | Tag_Nr | category | date | 0.582 | 6 / 2 / 4 / 2 |
| L1 | b076-0012 | temporal | date | date | 0.975 | 2023-M07 / 2018-M06 / 2024-M05 / 2023-M01 |
| L1 | b076-0088 | Projektjahr | category | date | 0.965 | Durchführung / Durchführung / Durchführung / Durchführung |
| L1 | b076-0091 | Tag_Nr | id | date | 0.555 | 5 / 1 / 3 / 4 |
| L1 | b090-0081 | 開始時間 | text | date | 0.692 | （月?金）児童の下校時（ / （月?金）児童の下校時（ / （月?金）児童の下校時（ / （月?金）児童の下校時（ |
| L2 | b067-0123 | PERIOD | date | date | 0.987 | 2018-04-01/2 / 2005-10-01/2 / 2018-04-01/2 / 2012-04-01/2 |
| L2 | b067-0215 | monat | date | date | 0.989 | 7 / 9 / 9 / 9 |
| L2 | b071-0028 | 集計日 | date | date | 0.98 | 42735 / 42735 / 42735 / 42735 |
| L2 | b072-0272 | measured_at | date | date | 0.971 | 1723010401.6 / 1724457600.0 / 1725537600.0 / 1720990800.5 |
| L2 | b072-0299 | monat | date | date | 0.989 | 12 / 12 / 12 / 12 |
| L2 | b076-0012 | temporal | date | date | 0.983 | 2023-M07 / 2018-M06 / 2024-M05 / 2023-M01 |
| L2 | b076-0088 | Projektjahr | category | date | 0.956 | Durchführung / Durchführung / Durchführung / Durchführung |
| L3 | b067-0123 | PERIOD | date | date | 0.989 | 2018-04-01/2 / 2005-10-01/2 / 2018-04-01/2 / 2012-04-01/2 |
| L3 | b067-0215 | monat | date | date | 0.988 | 7 / 9 / 9 / 9 |
| L3 | b071-0028 | 集計日 | date | date | 0.864 | 42735 / 42735 / 42735 / 42735 |
| L3 | b072-0272 | measured_at | date | date | 0.98 | 1723010401.6 / 1724457600.0 / 1725537600.0 / 1720990800.5 |
| L3 | b072-0299 | monat | date | date | 0.989 | 12 / 12 / 12 / 12 |
| L3 | b073-0206 | 年No. | id | date | 0.949 | 466 / 667 / 16 / 278 |
| L3 | b076-0012 | temporal | date | date | 0.978 | 2023-M07 / 2018-M06 / 2024-M05 / 2023-M01 |
| L3 | b076-0088 | Projektjahr | category | date | 0.981 | Durchführung / Durchführung / Durchführung / Durchführung |

## amount_without_cue

| 本 | id | 列名 | 正解 | 1 位 | 1 位の確率 | 値 |
|---|---|---|---|---|---:|---|
| L1 | b066-0076 | Outturn_2 | amount | amount | 0.974 | - / 1,758,696 / 7,870,142 / - |
| L1 | b071-0195 | 入園料 | amount | amount | 0.955 | 112920 / 110208 / 109367 / 149085 |
| L1 | b072-0179 | Kurspaare Mo-Fr | id | amount | 0.746 | 3.0 / 37.0 / 49.5 / 2.5 |
| L1 | b072-0181 | Kurspaare So | quantity | amount | 0.547 | 19.0 / 17.0 / 9.0 / 31.0 |
| L1 | b076-0036 | OBS_VALUE | amount | amount | 0.875 | 197.893 / 877.968 / 21.156 / 121.75 |
| L1 | b076-0040 | VALUE | quantity | amount | 0.762 | 10496 / 2883638 / 5737 / 1134232 |
| L1 | b078-0020 | Auszahlungen_CHF | amount | amount | 0.989 | 4456720.00 / 10338535.00 / 7490236.40 / 814005.00 |
| L1 | b085-0025 | TOTAL | amount | amount | 0.984 | 515.35 / 2681.19 / -1646.19 / -1929.09 |
| L1 | b090-0147 | 製造品出荷額等 | amount | amount | 0.988 | 7367879.88 / 5958822.0 / 5789243.0 / 10237865.0 |
| L1 | b090-0148 | 付加価値額 | amount | amount | 0.989 | 2654615.0 / 1147821.0 / 2651256.0 / 2463759.0 |
| L2 | b066-0076 | Outturn_2 | amount | amount | 0.988 | - / 1,758,696 / 7,870,142 / - |
| L2 | b071-0195 | 入園料 | amount | amount | 0.925 | 112920 / 110208 / 109367 / 149085 |
| L2 | b076-0036 | OBS_VALUE | amount | amount | 0.912 | 197.893 / 877.968 / 21.156 / 121.75 |
| L2 | b076-0040 | VALUE | quantity | amount | 0.67 | 10496 / 2883638 / 5737 / 1134232 |
| L2 | b078-0020 | Auszahlungen_CHF | amount | amount | 0.99 | 4456720.00 / 10338535.00 / 7490236.40 / 814005.00 |
| L2 | b085-0025 | TOTAL | amount | amount | 0.99 | 515.35 / 2681.19 / -1646.19 / -1929.09 |
| L2 | b090-0147 | 製造品出荷額等 | amount | amount | 0.989 | 7367879.88 / 5958822.0 / 5789243.0 / 10237865.0 |
| L2 | b090-0148 | 付加価値額 | amount | amount | 0.99 | 2654615.0 / 1147821.0 / 2651256.0 / 2463759.0 |
| L3 | b066-0076 | Outturn_2 | amount | amount | 0.982 | - / 1,758,696 / 7,870,142 / - |
| L3 | b071-0195 | 入園料 | amount | amount | 0.971 | 112920 / 110208 / 109367 / 149085 |
| L3 | b076-0036 | OBS_VALUE | amount | amount | 0.98 | 197.893 / 877.968 / 21.156 / 121.75 |
| L3 | b076-0040 | VALUE | quantity | amount | 0.867 | 10496 / 2883638 / 5737 / 1134232 |
| L3 | b078-0020 | Auszahlungen_CHF | amount | amount | 0.989 | 4456720.00 / 10338535.00 / 7490236.40 / 814005.00 |
| L3 | b085-0025 | TOTAL | amount | amount | 0.989 | 515.35 / 2681.19 / -1646.19 / -1929.09 |
| L3 | b090-0147 | 製造品出荷額等 | amount | amount | 0.987 | 7367879.88 / 5958822.0 / 5789243.0 / 10237865.0 |
| L3 | b090-0148 | 付加価値額 | amount | amount | 0.99 | 2654615.0 / 1147821.0 / 2651256.0 / 2463759.0 |

## probability_below_threshold

| 本 | id | 列名 | 正解 | 1 位 | 1 位の確率 | 値 |
|---|---|---|---|---|---:|---|
| L1 | b073-0123 | 名称_カナ | address | org | 0.499 | カイエジ / オオトリタイシャ / コヤマケジュウタク / サカイ・ミドリノミュージ |
| L1 | b074-0065 | GEO_CANT_WORK | id | quantity | 0.484 | 1 / 1 / 1 / 1 |
| L1 | b074-0153 | ZST | id | other | 0.322 | 600 / 604 / 82 / 602 |
| L1 | b074-0229 | pdf | category | category | 0.485 | 0 / 0 / 0 / 0 |
| L1 | b077-0003 | RANG_GDE | category | other | 0.36 | 432 / 163 / 250 / 328 |
| L1 | b078-0034 | SOURCE | category | category | 0.486 | UDEMO / UDEMO / STATENT / KUWI, STATEN |
| L1 | b078-0042 | VARIABLE | id | id | 0.472 | pen_t / voit_tour / txmot / voit_tour |
| L1 | b078-0139 | Annahmestelle | address | org | 0.491 | Apotheken /  / RE West / RE West / Apotheken /  |
| L2 | b067-0346 | Passanten in Richtung Neumarkt | quantity | other | 0.494 | 19.0 / 41.0 / 1.0 / 34.0 |
| L2 | b072-0257 | modultyp | product | other | 0.425 | HareonHR-260 / SunTech HyPr / Axitec Axipr / Trina Solar- |
| L2 | b074-0161 | Tag_Nr | category | category | 0.384 | 6 / 2 / 4 / 2 |
| L2 | b074-0234 | verantw_dienststelle | account | org | 0.481 | TBA / SF / BA / KESB |
| L2 | b077-0002 | GDENR | id | id | 0.348 | 2 / 2 / 2 / 2 |
| L2 | b088-0020 | Model# | product | product | 0.475 | M83 / X1 YOGA / M710S / M710S |
| L3 | b067-0009 | value | quantity | rate | 0.491 | 65 / 40 / 64 / 45 |
| L3 | b067-0084 | Beschreibung | product | text | 0.487 | Butter / Mozzarella / Mozzarella / Bio Halbrahm |
| L3 | b067-0346 | Passanten in Richtung Neumarkt | quantity | rate | 0.454 | 19.0 / 41.0 / 1.0 / 34.0 |
| L3 | b067-0347 | Passanten in Richtung Multerga | quantity | other | 0.478 | 62.0 / 8.0 / 26.0 / 49.0 |
| L3 | b074-0082 | GEO_CANT_WORK | id | category | 0.402 | 1 / 1 / 19 / 1 |
| L3 | b076-0083 | sammlung | category | org | 0.488 | Kehricht / Papier / Grüngut / Kehricht |
| L3 | b077-0003 | RANG_GDE | category | category | 0.449 | 432 / 163 / 250 / 328 |
| L3 | b078-0034 | SOURCE | category | category | 0.399 | UDEMO / UDEMO / STATENT / KUWI, STATEN |
| L3 | b078-0042 | VARIABLE | id | category | 0.498 | pen_t / voit_tour / txmot / voit_tour |
| L3 | b081-0156 | TitileOfOpportunity | text | text | 0.499 | Roof Anchors / Service Rise / Flood Impact / Treasury Man |

## verifier

| 本 | id | 列名 | 正解 | 1 位 | 1 位の確率 | 値 |
|---|---|---|---|---|---:|---|
| L1 | b071-0051 | 年齢 | category | quantity | 0.986 | 83 / 82 / 13 / 87 |
| L1 | b072-0103 | GEO_CANT | id | id | 0.959 | 1 / 2 / 1 / 2 |
| L1 | b074-0050 | wert | quantity | quantity | 0.825 | 17 / 3791598 / 102 / 2635829 |
| L1 | b074-0083 | GEO_COMM_WORK | id | id | 0.958 | 4001 / 10 / 230 / 1322 |
| L1 | b081-0130 | Project Code | id | id | 0.98 | 0 / 0 / 0 / 0 |
| L1 | b085-0054 | RATE | amount | rate | 0.828 | £65.62 / £136.78 or 9 / £112.55 / £108.30 |
| L2 | b071-0051 | 年齢 | category | quantity | 0.987 | 83 / 82 / 13 / 87 |
| L2 | b074-0050 | wert | quantity | quantity | 0.4 | 17 / 3791598 / 102 / 2635829 |
| L2 | b074-0083 | GEO_COMM_WORK | id | id | 0.98 | 4001 / 10 / 230 / 1322 |
| L2 | b074-0153 | ZST | id | quantity | 0.972 | 600 / 604 / 82 / 602 |
| L2 | b081-0130 | Project Code | id | id | 0.942 | 0 / 0 / 0 / 0 |
| L2 | b085-0054 | RATE | amount | rate | 0.558 | £65.62 / £136.78 or 9 / £112.55 / £108.30 |
| L3 | b071-0051 | 年齢 | category | quantity | 0.989 | 83 / 82 / 13 / 87 |
| L3 | b072-0165 | gestations_alter_grp | category | quantity | 0.975 | 9 / 9 / 9 / 9 |
| L3 | b074-0050 | wert | quantity | rate | 0.537 | 17 / 3791598 / 102 / 2635829 |
| L3 | b074-0083 | GEO_COMM_WORK | id | id | 0.951 | 4001 / 10 / 230 / 1322 |
| L3 | b081-0130 | Project Code | id | id | 0.871 | 0 / 0 / 0 / 0 |
| L3 | b085-0054 | RATE | amount | rate | 0.56 | £65.62 / £136.78 or 9 / £112.55 / £108.30 |
