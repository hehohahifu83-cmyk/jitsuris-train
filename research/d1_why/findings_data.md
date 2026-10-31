# D1 が伸びなかった原因の数（決める陣、`research/d1_why/analyze.py`）

## 1. V・U が本体の入力を変えた列

| 形 | 入力が変わった列（set 1,620 列） | うち採点する列 | その列で A→形 の正しい（種子 1・2） |
|---|---:|---:|---|
| V | 31 | 16 | 12→13・12→13 |
| U | 21 | 16 | 11→12・12→12 |
- V：入力が同じ列 1194 のうち、A と正誤が入れ替わった列 種子 1 20・種子 2 27（学習のゆれ）
- U：入力が同じ列 1194 のうち、A と正誤が入れ替わった列 種子 1 33・種子 2 26（学習のゆれ）
- 参考：A の種子 1 と種子 2 で正誤が入れ替わった列 36（同じ設定の学習のゆれ）

## 2. A の誤りの段（種子 1・2）

| 段 | 種子 1 | 種子 2 |
|---|---:|---:|
| 本体の 1 位は正しい → 見張り・後ろの段で外れた（不明） | 46 | 48 |
| 本体の 1 位は違う・正解は 3 位以内 | 93 | 94 |
| 正解が本体の 3 位にもない | 15 | 16 |

### 本体の 1 位が正しいのに外れた列の理由（種子 1・2）

| 理由 | 種子 1 | 種子 2 |
|---|---:|---:|
| low_confidence_no_cue | 21 | 23 |
| None | 9 | 9 |
| amount_without_cue | 7 | 6 |
| rate_without_cue | 4 | 4 |
| verifier | 2 | 4 |
| cue_conflict | 2 | 1 |
| amount_precision | 1 | 1 |

### 正解が 3 位以内の列：本体の 1 位 → 正解（種子 1、多い順）

- id → category：23
- org → address：13
- quantity → category：9
- category → id：8
- quantity → amount：5
- other → quantity：4
- address → org：4
- quantity → id：3
- account → category：3
- rate → quantity：3
- date → id：2
- id → product：2
- text → category：2
- org → account：2
- rate → amount：1

## 3. A（種子 1）の誤りの正解の種類と、どう外れたか

| 正解 | 誤り（不明を含む） | 不明 | 別の種類（多い順） |
|---|---:|---:|---|
| category | 43 | 17 | id 17, account 3, text 2, quantity 2, org 1, address 1 |
| id | 33 | 22 | category 8, org 2, quantity 1 |
| quantity | 20 | 17 | category 2, id 1 |
| amount | 15 | 14 | quantity 1 |
| address | 15 | 3 | org 11, category 1 |
| date | 10 | 9 | category 1 |
| org | 7 | 1 | address 4, category 1, account 1 |
| rate | 4 | 4 |  |
| product | 3 | 1 | category 1, id 1 |
| account | 2 | 0 | org 2 |
| text | 2 | 1 | category 1 |

## 4. A の種子 1・2 の両方で誤った列（一部）

両方で誤り 138 列。

| id | 正解 | 答え（1・2） | 本体の 1 位 | 理由 | 列名 | 値 |
|---|---|---|---|---|---|---|
| b066-0015 | id | unknown・org | id | low_confidence_no_cue | OrganisationLabel | 23UB / 23UB / 23UB |
| b066-0017 | id | org・org | org | None | OrganisationLabel_2 | 23UB / 23UB / 23UB |
| b066-0064 | amount | unknown・unknown | amount | amount_precision | Value of New Contract (Excludi | 3,205,468 / 2,170,000 / £2,000,000 |
| b066-0075 | amount | unknown・unknown | amount | None | Outturn | - / 1,060,382 / - |
| b066-0076 | amount | unknown・unknown | amount | amount_without_cue | Outturn_2 | - / 1,758,696 / 7,870,142 |
| b066-0201 | rate | unknown・unknown | rate | rate_without_cue | Pay Multiple | 3.6 / 3.8 / 3.5 |
| b066-0221 | category | account・account | account | None | ServiceCategory | Support Services / Highways and transport services |
| b066-0224 | category | account・account | account | None | ProcurementClassification:Proc | Works-Construction Repair and Maintenance|Building |
| b066-0232 | date | unknown・unknown | date | cue_conflict:amount | PaymentDate | 23/02/2015 / 09/06/2014 / 29/10/2014|26/11/2014 |
| b066-0233 | category | unknown・unknown | quantity | None | GrantDuration | One off / 1 year / 3 years |
| b067-0115 | date | unknown・unknown | date | None | Settimana | 19 / 11 / 20 |
| b067-0123 | date | unknown・unknown | date | None | PERIOD | 2018-04-01/2018-10-01 / 2005-10-01/2006-04-01 / 20 |
| b067-0127 | rate | unknown・unknown | rate | rate_without_cue | VALUE | 53.1 / 9.74117647058823 / 98.7 |
| b067-0135 | rate | unknown・unknown | rate | rate_without_cue | VALUE | 93.42545789 / 2.414964173 / 5.031838771 |
| b067-0200 | org | address・address | address | None | infrastruktur | Heididorf Maienfeld / Baumwipfelpfad Laax / Biathl |
| b067-0203 | org | address・address | address | None | anlagenbezeichnung | Roland Arena Lenzerheide / Leichtathletikanlage St |
| b067-0215 | date | unknown・unknown | date | None | monat | 7 / 9 / 9 |
| b067-0225 | id | unknown・unknown | id | low_confidence_no_cue | quartiergruppen | 25 / 13 / 31 |
| b067-0229 | rate | unknown・unknown | rate | rate_without_cue | stimmbeteiligung | 34.8 / 71.7 / 68.8 |
| b067-0233 | category | id・id | id | None | Geschäftsart ID | 8 / 5 / 6 |
| b067-0235 | category | id・id | id | None | process_state_id | 46 / 46 / 46 |
| b067-0343 | category | id・id | id | None | tag_nr | 6 / 2 / 2 |
| b067-0346 | quantity | unknown・unknown | rate | rate_without_cue | Passanten in Richtung Neumarkt | 19.0 / 41.0 / 1.0 |
| b067-0347 | quantity | unknown・unknown | other | None | Passanten in Richtung Multerga | 62.0 / 8.0 / 26.0 |
| b069-0049 | id | unknown・unknown | id | low_confidence_no_cue | AreaCode | CKST / NAT / SLWC |
| b070-0031 | category | quantity・quantity | quantity | low_confidence_no_cue | 年  齢 | 90 / 8 / 77 |
| b071-0028 | date | unknown・unknown | date | None | 集計日 | 42735 / 42735 / 42735 |
| b071-0051 | category | unknown・unknown | quantity | verifier:id | 年齢 | 83 / 82 / 13 |
| b071-0057 | category | address・address | address | None | 管轄 | 新千里 / 新千里 / 本庁 |
| b071-0058 | category | id・id | id | None | 区分番号 | 9 / 3 / 10 |
| b071-0195 | amount | unknown・unknown | amount | amount_without_cue | 入園料 | 112920 / 110208 / 109367 |
| b072-0033 | id | category・category | category | None | site | C / C / C |
| b072-0036 | product | id・id | id | low_confidence_no_cue | rsd_model | Opus-RSD3000/RSD518 / Opus-RSD3000/RSD518 / Opus-R |
| b072-0061 | category | unknown・unknown | other | None | Vogelart | Stockente / Lachmöwe / Blässhuhn |
| b072-0093 | quantity | unknown・unknown | quantity | low_confidence_no_cue | VALUE | 4661 / 1178 / 43632 |
| b072-0103 | id | unknown・unknown | id | verifier:quantity | GEO_CANT | 1 / 2 / 1 |
| b072-0153 | date | category・category | category | None | indikator | Wertschöpfung nominal / Wertschöpfung nominal / Wa |
| b072-0161 | category | unknown・unknown | quantity | low_confidence_no_cue | gewicht_grp | 7 / 7 / 6 |
| b072-0163 | category | unknown・unknown | id | low_confidence_no_cue | alter_mutter_cd | 1 / 2 / 2 |
| b072-0165 | category | unknown・unknown | quantity | low_confidence_no_cue | gestations_alter_grp | 9 / 9 / 9 |
| b072-0177 | id | unknown・unknown | other | None | Fahrplanfeld | 80.701 / 80.331 / 80.792 (m.Bund) |
| b072-0179 | id | unknown・unknown | amount | amount_without_cue | Kurspaare Mo-Fr | 3.0 / 37.0 / 49.5 |
| b072-0180 | org | unknown・unknown | other | None | Kurspaare Sa | 8.0 / 30.0 / 0.0 |
| b072-0181 | quantity | unknown・unknown | other | None | Kurspaare So | 19.0 / 17.0 / 9.0 |
| b072-0182 | quantity | id・category | id | None | Angebotsstufe Code | 2 / 3 / 1 |
| b072-0183 | quantity | category・category | category | None | Angebotsstufe Label | 15 bis 29 Kurspaare pro Tag (Stundentakt) sowie se |
| b072-0257 | product | category・unknown | category | None | modultyp | HareonHR-260-18/Bb poly / SunTech HyPro STP 325S / |
| b072-0272 | date | unknown・unknown | date | None | measured_at | 1723010401.69 / 1724457600.055 / 1725537600.068 |
| b072-0275 | address | unknown・unknown | other | None | location | {"coordinates": [9.406626586373676, 47.43919513975 |
| b072-0294 | category | id・unknown | id | None | bilanz_view_nr | 3 / 2 / 3 |
| b072-0297 | category | id・id | id | None | group_nr | 99 / 4 / 3 |
| b072-0299 | date | unknown・unknown | date | None | monat | 12 / 12 / 12 |
| b073-0046 | address | org・org | org | None | 棟 名称 | 日比野ビル / 常磐公園噴水機械棟 / ㈱サカツコーポレーション アルコ静岡店 |
| b073-0050 | id | category・unknown | category | None | 査察区分(棟) | 2 / 4 / 3 |
| b073-0123 | address | org・org | org | None | 名称_カナ | カイエジ / オオトリタイシャ / コヤマケジュウタク |
| b073-0189 | address | org・org | org | None | 場所名称 | 砥部焼伝統産業会館 / 砥部むかしのくらし館 / 佐々木酒造 |
| b073-0206 | id | unknown・unknown | date | None | 年No. | 466 / 667 / 16 |
| b073-0212 | category | org・org | org | None | 集計用 | 八幡西警察署わいせつ / 西警察署屋外盗 / 折尾警察署 |
| b073-0262 | org | account・account | account | None | 組織名称 | のぞみが丘小学校区協働のまちづくり協議会 / 立石校区協働のまちづくり協議会 / 大原校区協働のまち |
| b073-0319 | address | org・org | org | None | 名称 | 駅南住宅みやびのもり / 城東中学校 / オーシャンＣｉｔｙ |
| b073-0327 | address | org・org | org | None | 名称 | 野津原公民館 / 城南小学校 / 明治小学校 |
| b073-0388 | address | org・org | org | None | 施設名 | 南栄リース桜島広場（桜島多目的広場） / あいハウジンググラウンド松元（松元平野岡運動場） / 鴨池 |
| b073-0408 | org | address・address | address | None | 名称_カナ | DFSギャラリア　2F / ヤキニクコクサイインナハ（テンプスガワ） / シュリジョウコウエン（ホウ |
| b074-0033 | quantity | unknown・unknown | quantity | low_confidence_no_cue | Wert | 9161104 / 12246495 / 14779550 |
| b074-0040 | quantity | unknown・unknown | other | None | emission | 0 / 0 / 0 |
| b074-0050 | quantity | unknown・unknown | quantity | cue_conflict:rate | wert | 17 / 3791598 / 102 |
| b074-0054 | category | id・id | id | low_confidence_no_cue | Antwort | a77 / a78 / a77 |
| b074-0063 | id | unknown・unknown | id | low_confidence_no_cue | GEO_CANT_RESID | 1 / 1 / 1 |
| b074-0065 | id | unknown・unknown | quantity | low_confidence_no_cue | GEO_CANT_WORK | 1 / 1 / 1 |
| b074-0066 | id | quantity・unknown | quantity | None | GEO_COMM_WORK | 35 / 2 / 14 |
| b074-0080 | id | unknown・unknown | id | low_confidence_no_cue | GEO_CANT_RESID | 1 / 1 / 1 |
| b074-0082 | id | unknown・unknown | id | low_confidence_no_cue | GEO_CANT_WORK | 1 / 1 / 19 |
| b074-0083 | id | unknown・unknown | id | low_confidence_no_cue | GEO_COMM_WORK | 4001 / 10 / 230 |
| b074-0153 | id | unknown・unknown | quantity | low_confidence_no_cue | ZST | 600 / 604 / 82 |
| b074-0154 | id | unknown・address | id | low_confidence_no_cue | Strassennummer | A 13 / A 3 / A 1 |
| b074-0159 | date | unknown・unknown | date | None | TAG | 366 / 31 / 164 |
| b074-0161 | category | unknown・unknown | id | None | Tag_Nr | 6 / 2 / 4 |
| b074-0229 | category | unknown・unknown | quantity | low_confidence_no_cue | pdf | 0 / 0 / 0 |
| b074-0232 | category | text・text | text | None | zug_legislaturziel | 8.11 Anzahl zurückgelegter Wege / NA / 9.21 Erneue |
| b074-0233 | account | org・unknown | org | None | verantw_direktion | DSSI / DPB / DTB |
