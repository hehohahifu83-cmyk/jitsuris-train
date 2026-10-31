# 確かめる陣の誤りの原因（L＋K、種子 1〜3。`research/confirm_why/analyze.py`）

- 採点 1247 列のうち、1 本でも正しくなかった固有の列 200（3 本とも 157）。
- 辞書が届きうる（3 本中 2 本以上で、迷い かつ 正解が上位 3）：152 列。本体が自信をもって誤り：34 列。正解が上位 3 に無い：14 列。

## 1 位 → 正解（届きうる列）

- id → id：23
- id → category：20
- amount → amount：18
- quantity → quantity：15
- org → address：13
- quantity → category：8
- category → category：7
- other → quantity：4
- date → date：4
- address → address：4
- text → text：4
- id → quantity：3
- text → category：2
- date → category：2
- id → address：2
- other → id：2
- category → text：2
- category → address：2
- org → org：2
- account → org：1
- other → rate：1
- rate → rate：1
- quantity → rate：1
- date → quantity：1
- quantity → id：1

## 止めた理由（届きうる列、種子 1）

- （なし）：84
- low_confidence_no_cue：34
- verifier：15
- amount_without_cue：10
- cue_conflict：6
- rate_without_cue：1
- recheck：1
- amount_precision：1

## 言語

- en：155
- ja：45

## 届きうる列

| id | 列名 | 値 | 兄弟の列 | 正解 | 最終（3 本） | 上位 3（種子 1） | 理由 | 辞書 |
|---|---|---|---|---|---|---|---|---|
| b066-0091 | Annual Paybill  (delegated grades f | ｣104,332,000 ・ ｣139,451,519 ・ ｣42,321,409 ・ ｣7,942,113 ・ ｣153,857,343 | Main  department ・ Organisation ・ Headcount  (delega ・ In-year: Cost of i ・ In-year: Number of | amount | unknown,unknown,unknown | amount0.99, quantity0.00, rate0.00 | cue_conflict:date |  |
| b066-0096 | In-year: Median NCPRP for those rec | ｣500 ・ ｣75 ・ ｣0 ・ ｣350 ・ ｣0 | Main  department ・ Organisation ・ Annual Paybill  (d ・ Headcount  (delega ・ In-year: Cost of i | amount | unknown,unknown,unknown | amount0.99, quantity0.01, rate0.00 | cue_conflict:date |  |
| b066-0108 | Child - Access | 0 ・ 0 ・ 0 ・ 0 ・ 0 | Oct-10 ・ Abduction ・ Arrest/Detention - ・ Arrest/Detention - ・ Arrest/Detention - | quantity | unknown,unknown,unknown | quantity0.90, category0.08, other0.00 | low_confidence_no_cue |  |
| b066-0109 | Child Custody | 0 ・ 0 ・ 0 ・ <=5 ・ 0 | Oct-10 ・ Abduction ・ Arrest/Detention - ・ Arrest/Detention - ・ Arrest/Detention - | quantity | unknown,unknown,unknown | quantity0.88, category0.11, amount0.00 | low_confidence_no_cue |  |
| b066-0124 | Accommodation | ｣0.00 ・ ｣0.00 ・ ｣63.98 ・ ｣0.00 ・ ｣0.00 | Date ・ Country ・ Position Held ・ Transport (incl ai ・ Programme Printing | amount | unknown,unknown,unknown | amount0.99, quantity0.01, rate0.00 |  |  |
| b066-0126 | Programme Printing | ｣0.00 ・ ｣0.00 ・ ｣0.00 ・ ｣0.00 ・ ｣870.00 | Date ・ Country ・ Position Held ・ Accommodation ・ Transport (incl ai | amount | unknown,unknown,unknown | amount0.98, quantity0.01, rate0.00 |  |  |
| b066-0127 | Venue/production | ｣1,015.26 ・ ｣0.00 ・ ｣0.00 ・ ｣11,956.50 ・ ｣18,151.72 | Date ・ Country ・ Position Held ・ Accommodation ・ Transport (incl ai | amount | unknown,unknown,unknown | amount0.99, quantity0.00, rate0.00 |  |  |
| b066-0128 | Hospitality | ｣0.00 ・ ｣0.00 ・ ｣0.00 ・ ｣0.00 ・ ｣0.00 | Date ・ Country ・ Position Held ・ Accommodation ・ Transport (incl ai | amount | unknown,unknown,unknown | amount0.99, quantity0.00, rate0.00 |  |  |
| b066-0130 | Interpretation | ｣0.00 ・ ｣0.00 ・ ｣0.00 ・ ｣0.00 ・ ｣900.24 | Date ・ Country ・ Position Held ・ Accommodation ・ Transport (incl ai | amount | unknown,unknown,unknown | amount0.99, rate0.00, quantity0.00 |  |  |
| b066-0133 | Please enter information below rela | Annual Paybill   ・ ｣199,843,951 ・ ｣165,666,519 ・ ｣62,832,894 | Main  department ( ・ Organisation (Plea ・ SCS on standard co ・ Information for SC ・ Comments (Please e | amount | unknown,unknown,unknown | amount0.98, account0.00, tax_class0.00 | amount_without_cue |  |
| b066-0170 | Delegated grades only | Annual Paybill   ・ ｣1,880,195,630 ・ ｣38,635,567 ・ ｣165,827,234 ・ ｣105,550,079 | Main  department ・ Organisation ・ SCS on standard co ・ Information for SC ・ Comments | amount | unknown,unknown,unknown | amount0.99, quantity0.00, account0.00 | amount_without_cue |  |
| b067-0189 | geschaeft_vorberatende_kommission_d | Finanzkommission ・ Finanzkommission ・ Finanzkommission ・ Finanzkommission ・ Finanzkommission | geschaeft_nr ・ geschaeft_typ_deut ・ geschaeft_typ_fran ・ geschaeft_federfue ・ geschaeft_federfue | org | account,account,account | account0.89, org0.09, category0.01 |  |  |
| b067-0247 | sachbegriff_grgeko_1 | 74.1 Strassenver ・ 13.1 Gebiet, Org ・ 13.1 Gebiet, Org ・ 13.1 Gebiet, Org ・ 17.3 Richterlich | datum_geschaeft_ei ・ datum_geschaeft_ab ・ geschaeftsnummer ・ grg_nummer ・ geschaftstitel | category | text,text,text | text0.79, category0.20, account0.00 |  |  |
| b067-0258 | belegung | 40.73 ・ 85.68 ・ 13.29 ・ 45.39 ・ 5.45 | zeit_von ・ zeit_bis ・ inflow ・ outflow ・ median_standzeit | rate | unknown,unknown,unknown | other0.82, rate0.08, quantity0.07 |  |  |
| b067-0261 | median_standzeit | 1350.5 ・ 2640.0 ・ 38885.0 ・ 2221.0 ・ 1200.0 | zeit_von ・ zeit_bis ・ belegung ・ inflow ・ outflow | quantity | unknown,unknown,unknown | quantity0.84, other0.08, date0.06 | low_confidence_no_cue |  |
| b067-0282 | shortNumber | 36 ・ 90 ・ 85 ・ 20 ・ 71 | slnid ・ linienId ・ validFrom ・ validTo ・ status | id | unknown,unknown,unknown | id0.99, address0.01, category0.00 | verifier:quantity |  |
| b067-0313 | VZ-Sigel | Zo S ・ Bi S ・ Be 114 ・ Ba 108 ・ Ba 20 | ISIL ・ Status ・ Mutterinstitution ・ VZ-Code ・ Institutionstyp | id | unknown,unknown,unknown | id0.72, category0.26, address0.00 | low_confidence_no_cue |  |
| b067-0412 | buildingContractor_noUID | false ・ false ・ true ・ true ・ true | publicationDate ・ entryDeadline ・ expirationDate ・ bfs_nr ・ buildingContractor | category | unknown,unknown,unknown | id0.60, category0.38, address0.00 | low_confidence_no_cue |  |
| b067-0413 | buildingContractor_index | 1 ・ 2 ・ 1 ・ 2 ・ 3 | publicationDate ・ entryDeadline ・ expirationDate ・ bfs_nr ・ buildingContractor | id | unknown,category,unknown | id0.52, category0.45, other0.01 | low_confidence_no_cue |  |
| b067-0430 | THEMA_ID | 10 ・ 4,10 ・ 10 ・ 10 ・ 1 | ABSTIMMTAG ・ STAT_VORLAGE_ID ・ BFS_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ | category | unknown,unknown,unknown | id0.93, category0.06, address0.00 | verifier:quantity |  |
| b067-0432 | ABSTIMMUNGSART_ID | 2 ・ 2 ・ 2 ・ 2 ・ 2 | ABSTIMMTAG ・ STAT_VORLAGE_ID ・ BFS_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ | category | id,id,id | id0.71, category0.27, address0.00 |  |  |
| b068-0005 | Total, All Recipients, Number | 46940 ・ 16360 ・ 95830 ・ 81290 ・ 892600 | Province or Territ ・ Total, All Recipie ・ Less than $5,000,  ・ Less than $5,000,  ・ $5,000 to $9,999,  | quantity | unknown,unknown,unknown | quantity0.99, amount0.00, id0.00 | verifier:quantity |  |
| b068-0009 | $5,000 to $9,999, Number | 970 ・ 180 ・ 2310 ・ 1500 ・ 15880 | Province or Territ ・ Total, All Recipie ・ Total, All Recipie ・ Less than $5,000,  ・ Less than $5,000,  | quantity | unknown,unknown,unknown | quantity0.99, id0.00, category0.00 | cue_conflict:amount |  |
| b068-0011 | $10,000 to $14,999, Number | 2370 ・ 250 ・ 4110 ・ 4340 ・ 22610 | Province or Territ ・ Total, All Recipie ・ Total, All Recipie ・ Less than $5,000,  ・ Less than $5,000,  | quantity | unknown,unknown,unknown | quantity0.99, id0.01, category0.00 | cue_conflict:amount |  |
| b068-0013 | $15,000 to $19,999, Number | 2550 ・ 370 ・ 3130 ・ 2600 ・ 19350 | Province or Territ ・ Total, All Recipie ・ Total, All Recipie ・ Less than $5,000,  ・ Less than $5,000,  | quantity | unknown,unknown,unknown | quantity0.99, id0.00, category0.00 | cue_conflict:amount |  |
| b068-0019 | incidence_apr19 | 76.3 ・ 73 ・ 27.5 ・ 189 ・ 164.6 | Health_Region_ID ・ Health_Region_area ・ cases_apr19 ・ cases_may13 ・ Province | rate | unknown,quantity,unknown | rate0.92, other0.05, quantity0.01 | rate_without_cue |  |
| b068-0020 | incidence_may13 | 77.6 ・ 39.0 ・ 27.5 ・ 319.6 ・ 191.9 | Health_Region_ID ・ Health_Region_area ・ cases_apr19 ・ cases_may13 ・ Province | rate | unknown,quantity,unknown | quantity0.58, rate0.27, other0.13 | low_confidence_no_cue |  |
| b068-0027 | Collection Time/Duree d'echantillon | 258986 ・ 85925 ・ 86342 ・ 86689 ・ 86120 | Location/Emplaceme ・ Province/Province ・ Collection Start/D ・ AirVolume/Volume d ・ Cs-134 Activity/Cs | quantity | unknown,unknown,unknown | date0.96, quantity0.02, id0.00 |  |  |
| b068-0028 | AirVolume/Volume d'air (m3) | 70054.3 ・ 23139.7 ・ 23483.8 ・ 24680.7 ・ 25428.2 | Location/Emplaceme ・ Province/Province ・ Collection Start/D ・ Collection Time/Du ・ Cs-134 Activity/Cs | quantity | unknown,unknown,unknown | other0.57, quantity0.42, rate0.00 |  |  |
| b069-0001 | Obs | 60 ・ 147 ・ 166 ・ 184 ・ 207 | Data_Vintage ・ Publication_Month ・ Publication_Year ・ Controlling_Sub_Se ・ GOV_Dept_LA | id | unknown,unknown,unknown | quantity0.98, amount0.01, id0.00 | verifier:id |  |
| b069-0005 | Controlling_Sub_Sector | S11001 ・ S11001 ・ S11001 ・ S11001 ・ S11001 | Obs ・ Data_Vintage ・ Publication_Month ・ Publication_Year ・ GOV_Dept_LA | category | id,id,id | id0.66, category0.31, account0.01 | low_confidence_no_cue |  |
| b069-0043 | Number | 45 ・ 67 ・ 83 ・ 52 ・ 72 | Month ・ % | quantity | unknown,unknown,unknown | quantity0.98, id0.01, other0.00 | verifier:quantity |  |
| b072-0077 | parameter_decimals | 0 ・ 0 ・ 0 ・ 0 ・ 0 | parameter_group_de ・ parameter_group_fr ・ parameter_group_it ・ parameter_group_en ・ parameter_granular | quantity | unknown,unknown,unknown | quantity0.98, amount0.01, category0.01 | cue_conflict:rate |  |
| b072-0128 | geschaeft_laufnummer | 2026/7158 ・ 2026/6314 ・ 2026/6313 ・ 2026/5990 ・ 2026/5882 | dokument_titel ・ dokument_datum ・ geschaeft_titel | id | unknown,unknown,unknown | id0.99, address0.00, date0.00 | verifier:date |  |
| b072-0202 | bauperiode_code | 8019 ・ 8019 ・ 8015 ・ 8018 ・ 8022 | jahr ・ bfs_nr_gemeinde ・ gebaeudekategorie_ ・ gebaeudekategorie ・ bauperiode | category | unknown,unknown,unknown | id0.91, category0.05, date0.03 | low_confidence_no_cue |  |
| b072-0343 | VORLAGENART_ID | 1 ・ 1 ・ 3 ・ 2 ・ 1 | ABSTIMMTAG ・ STAT_VORLAGE_ID ・ BFS_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ | category | id,id,id | id0.88, category0.11, address0.00 |  |  |
| b072-0345 | THEMA_ID | 4 ・ 6 ・ 4,6 ・ 1,10 ・ 9 | ABSTIMMTAG ・ STAT_VORLAGE_ID ・ BFS_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ | category | unknown,unknown,unknown | id0.83, category0.16, text0.00 | verifier:quantity |  |
| b072-0347 | ABSTIMMUNGSART_ID | 2 ・ 2 ・ 2 ・ 2 ・ 2 | ABSTIMMTAG ・ STAT_VORLAGE_ID ・ BFS_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ | category | id,id,id | id0.50, category0.48, other0.00 |  |  |
| b072-0356 | br_abschnitt_code | NA ・ NA ・ NA ・ NA ・ NA | br_abschnitt_desc ・ wirtschaftssektor_ ・ wirtschaftssektor_ ・ location ・ date | category | unknown,unknown,unknown | id0.65, address0.24, category0.07 | low_confidence_no_cue |  |
| b073-0003 | 名称_カナ | モオカショウガッコウ ・ カメヤマショウガッコウ ・ モオカチュウガッコウ ・ モオカニシチュウガッコウ ・ モオカコウトウガッコウ | NO ・ 名称 ・ 市区町村コード ・ 災害種別_洪水 ・ 災害種別_崖崩れ、土石流及び地滑り | address | org,org,org | org0.84, address0.15, id0.00 |  |  |
| b073-0012 | 名称 | 真岡木綿会館 ・ 岡部記念館金鈴荘 ・ 真岡鐵道 ・ SLキューロク館 ・ 根本山自然観察センター | 全国地方公共団体コード ・ 地方公共団体名 ・ 名称_カナ ・ 説明 ・ 種別 | address | org,org,org | org0.68, address0.32, person0.00 |  |  |
| b073-0013 | 名称_カナ | モオカモメンカイカン ・ オカベキネンカンキンレイソウ ・ モオカテツドウ ・ エスエルキューロクカン ・ ネモトヤマシゼンカンサツセンター | 全国地方公共団体コード ・ 地方公共団体名 ・ 名称 ・ 説明 ・ 種別 | address | org,org,org | org0.67, address0.33, id0.00 |  |  |
| b073-0018 | 施設_名称（カナ） | ウラヤスエキダイサンジテンシャチ ・ ウラヤスエキダイヨンジテンシャチ ・ ウラヤスエキダイゴジテンシャチュ ・ ウラヤスエキダイロクジテンシャチ ・ ウラヤスエキダイナナジテンシャチ | 施設_全国地方公共団体コード ・ 施設_名称 ・ 施設_施設通称 ・ 施設_POIコード ・ 施設_概要 | address | org,org,org | org0.73, address0.26, id0.00 |  |  |
| b073-0038 | 合計戸数 | 26戸 ・ 21戸 ・ 20戸 ・ 20戸 ・ 25戸 | 施設名 ・ ｴﾚﾍﾞｰﾀｰ ・ 建設年度 ・ 構造 ・ 間取り | quantity | unknown,unknown,unknown | quantity0.99, other0.00, id0.00 |  |  |
| b073-0141 | 名称 | 岸和田城 ・ 岸和田城庭園（八陣の庭） ・ まちづくりの館 ・ 岸和田だんじり会館 ・ きしわだ自然資料館 | 全国地方公共団体コード ・ 地方公共団体名 ・ 名称_カナ ・ 名称_英語 ・ 説明 | address | org,org,org | org0.63, address0.36, text0.00 |  |  |
| b073-0142 | 名称_カナ | キシワダジョウ ・ キシワダジョウハチジンノニワ ・ マチヅクリノヤカタ ・ キシワダダンジリカイカン ・ キシワダシリョウカン | 全国地方公共団体コード ・ 地方公共団体名 ・ 名称 ・ 名称_英語 ・ 説明 | address | org,org,org | org0.59, address0.40, id0.00 |  |  |
| b073-0282 | ユニット | 2.0 ・ 1.0 ・ 1.0 ・ 1.0 ・ 1.0 | 事  業  所  名 ・ 所  在  地 ・ 実施ｻｰﾋﾞｽ ・ 利用定員 ・ 指定年月日 | quantity | unknown,unknown,id | id0.53, category0.43, quantity0.02 | low_confidence_no_cue |  |
| b073-0285 | 指定有効期限 | 44651 ・ 44742 ・ 44681 ・ 46112 ・ 46112 | 事  業  所  名 ・ 所  在  地 ・ 実施ｻｰﾋﾞｽ ・ ユニット ・ 利用定員 | date | unknown,unknown,unknown | date0.93, quantity0.04, org0.01 |  |  |
| b073-0292 | ユニット | 2.0 ・ 1.0 ・ 1.0 ・ 1.0 ・ 1.0 | 事  業  所  名 ・ 所  在  地 ・ 実施ｻｰﾋﾞｽ ・ 利用定員 ・ 指定年月日 | quantity | category,unknown,id | category0.73, id0.24, quantity0.01 |  |  |
| b073-0295 | 指定有効期限 | 46295.0 ・ 45382.0 ・ 45747.0 ・ 44895.0 ・ 45747.0 | 事  業  所  名 ・ 所  在  地 ・ 実施ｻｰﾋﾞｽ ・ ユニット ・ 利用定員 | date | unknown,unknown,unknown | date0.98, org0.01, quantity0.00 |  |  |
| b073-0304 | 当初指定年月日 | 36617 ・ 36617 ・ 36617 ・ 37135 ・ 36617 | 施  設  名 ・ 所  在  地 ・ 実施ｻｰﾋﾞｽ ・ 定員 ・ 短期入所定員 | date | unknown,unknown,unknown | date0.99, org0.00, address0.00 | verifier:id |  |
| b073-0305 | 指定有効期限 | 46112 ・ 46112 ・ 46112 ・ 46265 ・ 46112 | 施  設  名 ・ 所  在  地 ・ 実施ｻｰﾋﾞｽ ・ 定員 ・ 短期入所定員 | date | unknown,unknown,unknown | date0.96, quantity0.01, org0.01 |  |  |
| b074-0115 | Strassenbezeichnung Index | INZ ・ KIL ・ NEU ・ LÖR ・ KLY | EGID ・ EDID ・ EGAID ・ Eingangsnummer Geb ・ ESID | id | unknown,address,address | id0.58, address0.25, other0.09 | low_confidence_no_cue |  |
| b074-0171 | bfs_bezirksnummer | 2012 ・ 2015 ・ 2013 ・ 2015 ・ 2012 | jahr ・ substanz ・ hauptgruppe ・ untergruppe ・ sektor | id | unknown,unknown,unknown | id0.97, date0.01, address0.00 | verifier:date |  |
| b074-0175 | gebaeudekategorie_code | 1040 ・ 1021 ・ 1021 ・ 1030 ・ 1040 | jahr ・ bfs_nr_gemeinde ・ gebaeudekategorie ・ bauperiode_code ・ bauperiode | category | id,id,id | id0.60, category0.38, address0.01 | low_confidence_no_cue |  |
| b074-0177 | bauperiode_code | 8011 ・ 8020 ・ 8022 ・ 8016 ・ 8013 | jahr ・ bfs_nr_gemeinde ・ gebaeudekategorie_ ・ gebaeudekategorie ・ bauperiode | category | unknown,unknown,unknown | id0.94, category0.04, date0.01 | low_confidence_no_cue |  |
| b074-0178 | bauperiode | Periode vor 1919 ・ Periode von 2001 ・ Periode von 2011 ・ Periode von 1981 ・ Periode von 1946 | jahr ・ bfs_nr_gemeinde ・ gebaeudekategorie_ ・ gebaeudekategorie ・ bauperiode_code | category | unknown,unknown,unknown | date0.84, org0.05, text0.04 |  |  |
| b074-0191 | uicCountryCode | 13 ・ 13 ・ 13 ・ 13 ・ 13 | numberShort ・ sloid ・ number ・ checkDigit ・ validFrom | address | id,id,id | id0.89, address0.10, category0.01 | low_confidence_no_cue |  |
| b074-0194 | checkDigit | 9 ・ 5 ・ 3 ・ 1 ・ 3 | numberShort ・ uicCountryCode ・ sloid ・ number ・ validFrom | id | unknown,unknown,unknown | id0.58, category0.39, quantity0.01 | low_confidence_no_cue |  |
| b074-0311 | AZ_STIMMBERECHTIGTE | 97 ・ 260 ・ 340 ・ 22 ・ 136 | ABSTIMMUNGSTAG ・ STAT_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ ・ BFS | quantity | unknown,unknown,unknown | quantity0.86, other0.06, id0.04 | low_confidence_no_cue |  |
| b074-0312 | AZ_EINGELEGTE_STIMMZETTEL | 60 ・ 70 ・ 58 ・ 22 ・ 74 | ABSTIMMUNGSTAG ・ STAT_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ ・ BFS | quantity | unknown,unknown,unknown | id0.72, other0.10, quantity0.08 | low_confidence_no_cue |  |
| b075-0015 | Volume collected/ Volume collection | 593.79 ・ 1373.83 ・ 581.5 ・ 133.25 ・ 292 | Station ・ Location/Emplaceme ・ Sampler type/ Type ・ Start Date/  Date  ・ Stop Date/ Date de | quantity | unknown,unknown,unknown | quantity0.93, other0.06, amount0.00 | low_confidence_no_cue |  |
| b076-0052 | IDEDDP | 46:3600 ・ 31:4045 ・ 31:2492 ・ 26:1073 ・ 45:2114 | PK     (n^]ÃÌd ・ EGRID ・ COMMUNE ・ NO_COMM ・ NO_PARCELLE | id | unknown,unknown,unknown | id0.99, address0.00, category0.00 | verifier:date |  |
| b076-0058 | geschaeft_laufnummer | 2026/6465 ・ 2026/6005 ・ 2026/5953 ・ 2026/5777 ・ 2025/551 | geschaeft_titel ・ geachaeft_beginn | id | unknown,unknown,unknown | id0.99, address0.00, date0.00 | verifier:date |  |
| b076-0061 | numberShort | 17 ・ 679 ・ 679 ・ 679 ・ 679 | sloid ・ uicCountryCode ・ number ・ checkDigit ・ validFrom | id | unknown,unknown,unknown | other0.89, quantity0.09, id0.02 |  |  |
| b076-0062 | uicCountryCode | 14 ・ 14 ・ 14 ・ 14 ・ 14 | sloid ・ numberShort ・ number ・ checkDigit ・ validFrom | address | unknown,unknown,id | id0.87, address0.10, category0.02 | low_confidence_no_cue |  |
| b076-0064 | checkDigit | 4 ・ 1 ・ 1 ・ 1 ・ 1 | sloid ・ numberShort ・ uicCountryCode ・ number ・ validFrom | id | unknown,unknown,category | id0.74, category0.22, quantity0.01 | low_confidence_no_cue |  |
| b076-0068 | designationOperational | 01 ・ 02 ・ 01 ・ 00 ・ 06 | sloid ・ numberShort ・ uicCountryCode ・ number ・ checkDigit | category | unknown,unknown,unknown | id0.98, category0.02, address0.00 | verifier:date |  |
| b077-0008 | FAHRT_BEZEICHNER | 80:07____:3292:0 ・ 80:07____:3292:0 ・ 80:07____:3292:0 ・ 80:07____:3292:0 ・ 80:07____:3292:0 | BETRIEBSTAG ・ BETREIBER_ID ・ BETREIBER_ABK ・ PRODUKT_ID ・ LINIEN_ID | id | date,unknown,unknown | date0.76, id0.09, other0.06 |  |  |
| b077-0009 | BETREIBER_ID | 80:07____ ・ 80:07____ ・ 80:07____ ・ 80:07____ ・ 80:07____ | BETRIEBSTAG ・ FAHRT_BEZEICHNER ・ BETREIBER_ABK ・ PRODUKT_ID ・ LINIEN_ID | id | unknown,unknown,unknown | id0.99, date0.00, category0.00 | verifier:date |  |
| b077-0011 | PRODUKT_ID | Zug ・ Zug ・ Zug ・ Zug ・ Zug | BETRIEBSTAG ・ FAHRT_BEZEICHNER ・ BETREIBER_ID ・ BETREIBER_ABK ・ LINIEN_ID | category | id,id,id | id0.91, category0.04, product0.02 |  |  |
| b077-0025 | ug_Rampeneinsatz | -1 ・ -1 ・ 2 ・ 5 ・ 2 | Niederflurigkeit_F ・ Gebundenheit_Fahrz ・ sg_Autonomie ・ sg_Rampeneinsatz ・ sg_Voranmeldung | category | unknown,unknown,unknown | other0.57, category0.36, rate0.03 |  |  |
| b078-0061 | grundstücksnummer | 3438 ・ 1241 ・ 1241 ・ 2227 ・ 3727 | egid ・ gemeindenummer_bfs ・ egrid ・ koordinatenherkunf ・ koordinatenherkunf | id | unknown,unknown,address | id0.81, address0.18, org0.00 | low_confidence_no_cue |  |
| b078-0066 | gebaeudekategorie_code | 1020 ・ 1030 ・ 1020 ・ 1020 ・ 1020 | egid ・ gemeindenummer_bfs ・ egrid ・ grundstücksnummer ・ koordinatenherkunf | category | unknown,unknown,unknown | id0.57, category0.40, address0.01 | low_confidence_no_cue |  |
| b078-0070 | eidgenoessischer_eingangsidentifika | 0 ・ 0 ・ 0 ・ 0 ・ 0 | egid ・ gemeindenummer_bfs ・ eingangsnummer_geb ・ strassenbezeichnun ・ strassenbezeichnun | id | category,unknown,unknown | category0.78, id0.19, quantity0.02 |  |  |
| b078-0075 | strassenbezeichnung_offiziell_code | 1 ・ 1 ・ 1 ・ 1 ・ 1 | egid ・ gemeindenummer_bfs ・ eidgenoessischer_e ・ eingangsnummer_geb ・ strassenbezeichnun | category | unknown,id,unknown | id0.95, category0.04, address0.01 | low_confidence_no_cue |  |
| b078-0082 | Code | semf ・ semf ・ semf ・ semf ・ semf | Veranstaltungstag ・ Kategorie ・ Termin-ID ・ Veranstaltung-ID ・ Aktiv-Code | category | id,id,id | id0.95, category0.04, address0.00 |  |  |
| b078-0083 | Aktiv-Code | 1 ・ 1 ・ 1 ・ 1 ・ 1 | Veranstaltungstag ・ Kategorie ・ Termin-ID ・ Veranstaltung-ID ・ Code | category | id,id,id | id0.84, category0.14, address0.00 |  |  |
| b078-0084 | Wiederkehrend-Code | 1 ・ 1 ・ 1 ・ 1 ・ 1 | Veranstaltungstag ・ Kategorie ・ Termin-ID ・ Veranstaltung-ID ・ Code | category | id,id,id | id0.78, category0.21, quantity0.00 |  |  |
| b078-0099 | Wochentag | 0 ・ 0 ・ 1 ・ 1 ・ 1 | Monat ・ Start Zeitspanne ・ Ende Zeitspanne ・ Gemeinde ・ Wohnviertel-ID | category | unknown,unknown,unknown | quantity0.47, category0.34, date0.15 |  |  |
| b078-0105 | Bezirks-ID | 84 ・ 31 ・ 25 ・ 91 ・ 12 | Monat ・ Wochentag ・ Start Zeitspanne ・ Ende Zeitspanne ・ Gemeinde | id | unknown,unknown,unknown | id0.98, category0.01, address0.01 | verifier:quantity |  |
| b078-0109 | BEZIRK_NR | 2013 ・ 2012 ・ 2013 ・ 2013 ・ 2014 | BFS_NR_GEMEINDE ・ JAHR ・ KONFESSION_CODE ・ KONFESSION_BEZEICH ・ ANZAHL_PERSONEN | id | date,unknown,unknown | date0.82, id0.14, address0.01 |  |  |
| b078-0116 | BEZIRK_NR | 2014 ・ 2014 ・ 2015 ・ 2015 ・ 2013 | POLITISCHE_GEMEIND ・ BFS_NR_GEMEINDE ・ ORTSCHAFT ・ EINWOHNER_TOTAL ・ EINWOHNER_MAENNER | id | date,unknown,unknown | date0.93, id0.04, address0.01 | low_confidence_no_cue |  |
| b078-0118 | EINWOHNER_TOTAL | 5170 ・ 53 ・ x ・ 184 ・ 2219 | POLITISCHE_GEMEIND ・ BFS_NR_GEMEINDE ・ BEZIRK_NR ・ ORTSCHAFT ・ EINWOHNER_MAENNER | quantity | unknown,unknown,unknown | other0.81, quantity0.17, rate0.00 |  |  |
| b078-0120 | EINWOHNER_FRAUEN | 2587 ・ 30 ・ x ・ 89 ・ 1115 | POLITISCHE_GEMEIND ・ BFS_NR_GEMEINDE ・ BEZIRK_NR ・ ORTSCHAFT ・ EINWOHNER_TOTAL | quantity | unknown,unknown,unknown | other0.91, quantity0.05, address0.01 |  |  |
| b078-0127 | bfs_bezirksnummer | 2015 ・ 2012 ・ 2014 ・ 2012 ・ 2014 | datum ・ bfs_nr_gemeinde ・ gemeinde ・ bezirk ・ stimmberechtigte | id | unknown,unknown,unknown | id0.96, date0.02, address0.00 | verifier:date |  |
| b078-0130 | stiausweiseurne | 162 ・ 84 ・ 47 ・ 48 ・ 128 | datum ・ bfs_nr_gemeinde ・ gemeinde ・ bfs_bezirksnummer ・ bezirk | quantity | unknown,unknown,unknown | quantity0.82, id0.15, other0.01 | low_confidence_no_cue |  |
| b078-0133 | stiausweisebriefniuz | 0 ・ 0 ・ 0 ・ 4 ・ 0 | datum ・ bfs_nr_gemeinde ・ gemeinde ・ bfs_bezirksnummer ・ bezirk | quantity | unknown,unknown,category | amount0.38, quantity0.34, category0.20 |  |  |
| b079-0024 | MAP SCALE | Scale approximat ・ Scale approximat ・ Scale approximat ・ Scale approximat ・ Scale approximat | MAP TITLE, STATEME ・ OTHER MAP TITLE ・ OTHER MAP TITLE_2 ・ PLACE, PUBLISHER,  ・ PLACE, PRINTER | text | unknown,unknown,unknown | other0.92, text0.05, category0.01 |  |  |
| b079-0025 | PLACE, PUBLISHER, DATE OF PUBLICATI | Adelaide : Engin ・ Adelaide : Engin ・ Adelaide : Engin ・ Adelaide : Engin ・ Adelaide : Engin | MAP TITLE, STATEME ・ OTHER MAP TITLE ・ OTHER MAP TITLE_2 ・ MAP SCALE ・ PLACE, PRINTER | text | date,date,date | date0.45, text0.25, address0.14 | recheck:cue_date |  |
| b079-0026 | PLACE, PRINTER | Adelaide : A. Va ・ Adelaide : A. Va ・ Adelaide : A. Va ・ Adelaide : A. Va ・ Adelaide : A. Va | MAP TITLE, STATEME ・ OTHER MAP TITLE ・ OTHER MAP TITLE_2 ・ MAP SCALE ・ PLACE, PUBLISHER,  | text | address,address,address | address0.97, org0.03, id0.00 |  |  |
| b079-0027 | FORMAT, SIZE | 1 map on 4 sheet ・ 1 map on 5 sheet ・ 1 map on 3 sheet ・ 1 map on 3 sheet ・ 1 map on 3 sheet | MAP TITLE, STATEME ・ OTHER MAP TITLE ・ OTHER MAP TITLE_2 ・ MAP SCALE ・ PLACE, PUBLISHER,  | text | category,category,category | category0.76, text0.23, other0.00 |  |  |
| b080-0013 | Dept | 89 ・ 87 ・ 87 ・ 89 ・ 89 | Category ・ Fund ・ Organization Level ・ Org ・ AU | id | unknown,unknown,unknown | id0.94, quantity0.03, amount0.01 | low_confidence_no_cue |  |
| b080-0017 | Actual 2007-08 | 0.00 ・ 0.00 ・ 0.00 ・ 0.00 ・ 0.00 | Category ・ Fund ・ Organization Level ・ Dept ・ Org | amount | unknown,unknown,unknown | amount0.99, quantity0.00, rate0.00 | amount_without_cue |  |
| b080-0018 | Actual 2008-09 | 363.00 ・ 0.00 ・ 0.00 ・ 0.00 ・ 0.00 | Category ・ Fund ・ Organization Level ・ Dept ・ Org | amount | unknown,unknown,unknown | amount0.99, quantity0.00, rate0.00 | amount_without_cue |  |
| b080-0019 | Actual 2009-10 | 0.00 ・ 0.00 ・ 0.00 ・ 0.00 ・ 0.00 | Category ・ Fund ・ Organization Level ・ Dept ・ Org | amount | unknown,unknown,unknown | amount0.99, quantity0.00, rate0.00 | amount_without_cue |  |
| b085-0077 | Fare Paid | 187.8 ・ 32.5 ・ 42.74 ・ 37.74 ・ 141.99 | Flights ・ Departure Date ・ Origin City ・ Destination Airpor ・ Destination City | amount | unknown,unknown,unknown | amount0.98, quantity0.01, rate0.00 | amount_without_cue |  |
| b085-0088 | Delegated grades only | Annual Paybill   ・ ｣1,016,000,000 ・ ｣106,401,743 ・ ｣18,447,589 ・ ｣1,140,849,332 | Main  department ・ Organisation ・ SCS on standard co ・ Information for SC ・ Comments | amount | unknown,unknown,unknown | amount0.99, quantity0.00, account0.00 | amount_without_cue |  |
| b085-0122 | Delegated grades only | Annual Paybill   ・ ｣1,092,306,465 ・ ｣185,300,000 ・ ｣90,350,000 ・ ｣39,738,188 | Main  department ・ Organisation ・ SCS on standard co ・ Information for SC ・ Comments | amount | unknown,unknown,unknown | amount0.98, account0.00, tax_class0.00 | amount_without_cue |  |
| b087-0014 | Total Value Approved (｣) | ｣129,260 ・ ｣10,109,144 ・ ｣23,160,000 ・ ｣53,400 ・ ｣21,000 | Department ・ HNG Ref No ・ Basis for expendit ・ Date of approval | amount | unknown,unknown,unknown | amount0.99, quantity0.00, rate0.00 | amount_precision |  |
| b088-0003 | PARK_NO | 4 ・ 204 ・ 24 ・ 24 ・ 24 | OBJECTID ・ PARK ・ X_COORD ・ ARTIST ・ GISOBJID | id | unknown,unknown,unknown | id0.62, address0.36, org0.01 | low_confidence_no_cue |  |
| b088-0007 | OFFICIAL_N | Melville W. Full ・ Administration B ・ Chicago Stock Ex ・ Flying Dragon ・ Spirit of Music | OBJECTID ・ PARK ・ PARK_NO ・ X_COORD ・ ARTIST | text | unknown,category,category | category0.49, text0.47, address0.01 |  |  |
| b088-0015 | WARD | 49.0 ・ 4.0 ・ 29.0 ・ 48.0 ・ 48.0 | OBJECTID_1 ・ PARK ・ PARK_NO ・ BLDG_ID ・ BLDG_TYPE | id | unknown,unknown,unknown | other0.99, rate0.00, quantity0.00 |  |  |
| b090-0031 | 名称 | 美浜東第２街区公園 ・ 東野第７街区公園 ・ 高洲太陽の丘公園 ・ 日の出おひさま公園 ・ 舞浜公園 | 全国地方公共団体コード ・ ID ・ 地方公共団体名 ・ 名称_カナ ・ 名称_通称 | address | org,org,org | org0.77, address0.23, person0.00 |  |  |
| b090-0032 | 名称_カナ | ミハマヒガシダイ２ガイクコウエン ・ ヒガシノダイ７ガイクコウエン ・ タカスタイヨウノオカコウエン ・ ヒノデオヒサマコウエン ・ マイハマコウエン | 全国地方公共団体コード ・ ID ・ 地方公共団体名 ・ 名称 ・ 名称_通称 | address | org,org,org | org0.86, address0.13, id0.00 |  |  |
| b090-0033 | 名称_通称 | 美浜東第２街区公園 ・ 東野第７街区公園 ・ 高洲太陽の丘公園 ・ 日の出おひさま公園 ・ 舞浜公園 | 全国地方公共団体コード ・ ID ・ 地方公共団体名 ・ 名称 ・ 名称_カナ | address | org,org,org | org0.57, address0.42, person0.00 |  |  |
| b090-0174 | 歯科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 矯正歯科 ・ 小児歯科 | category | quantity,unknown,unknown | quantity0.97, category0.02, id0.00 |  |  |
| b090-0175 | 矯正歯科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 歯科 ・ 小児歯科 | category | quantity,unknown,unknown | quantity0.96, category0.03, id0.00 |  |  |
| b090-0176 | 小児歯科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 歯科 ・ 矯正歯科 | category | quantity,unknown,unknown | quantity0.97, category0.03, id0.00 |  |  |
| b090-0182 | 内科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 療養病床数 ・ 呼吸器科 | category | quantity,unknown,unknown | quantity0.98, category0.01, id0.00 |  |  |
| b090-0183 | 呼吸器科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 療養病床数 ・ 内科 | category | quantity,unknown,unknown | quantity0.97, category0.02, id0.00 |  |  |
| b090-0185 | 胃腸科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 療養病床数 ・ 内科 | category | quantity,unknown,unknown | quantity0.97, category0.02, id0.00 |  |  |
| b090-0247 | 合 計 | 96770268 ・ 92680320 ・ 117137187 ・ 124382551 ・ 122566100 | 区　　分 ・ 宿泊費 ・ 飲食費 ・ 土産品費 ・ 交通費 | amount | unknown,unknown,unknown | quantity0.47, amount0.46, id0.06 |  |  |
| b090-0250 | 土産品費 | 20725347 ・ 20750063 ・ 29477549 ・ 30719178 ・ 27209777 | 区　　分 ・ 合 計 ・ 宿泊費 ・ 飲食費 ・ 交通費 | amount | unknown,unknown,unknown | amount0.99, quantity0.00, id0.00 | amount_without_cue |  |
| b090-0252 | 入場料等 | 9374030 ・ 9366008 ・ 8115688 ・ 8303647 ・ 8315661 | 区　　分 ・ 合 計 ・ 宿泊費 ・ 飲食費 ・ 土産品費 | amount | unknown,unknown,unknown | amount0.95, id0.02, quantity0.02 | amount_without_cue |  |
| b067-0061 | staatsangehoerigkeit | Ausland ・ Schweiz ・ Ausland ・ Schweiz ・ Schweiz | stand ・ kanton ・ jahr ・ stufe ・ mittelschultyp | address | address,category,category | address0.51, category0.43, id0.02 |  |  |
| b067-0068 | staatsangehoerigkeit | Ausland ・ Schweiz ・ Ausland ・ Schweiz ・ Ausland | stand ・ kanton ・ jahr ・ stufe ・ schultyp | address | address,category,category | address0.69, category0.26, id0.02 |  |  |
| b067-0259 | inflow | 2 ・ 13 ・ 8 ・ 10 ・ 6 | zeit_von ・ zeit_bis ・ belegung ・ outflow ・ median_standzeit | quantity | unknown,unknown,quantity | quantity0.67, other0.30, category0.01 | low_confidence_no_cue |  |
| b067-0414 | buildingContractor_company_legalFor | 106 ・ 106 ・ 113 ・ 113 ・ 113 | publicationDate ・ entryDeadline ・ expirationDate ・ bfs_nr ・ buildingContractor | category | unknown,unknown,category | id0.88, category0.09, quantity0.02 | low_confidence_no_cue |  |
| b067-0415 | buildingContractor_company_legalFor | Aktiengesellscha ・ Aktiengesellscha ・ Besondere Rechts ・ Besondere Rechts ・ Besondere Rechts | publicationDate ・ entryDeadline ・ expirationDate ・ bfs_nr ・ buildingContractor | category | org,unknown,category | org0.91, category0.06, address0.01 |  |  |
| b068-0068 | question_value_e | All respondents ・ Yes ・ No ・ Yes ・ Yes | dept_f ・ dept_e ・ question ・ question_value_f ・ shr_w_resp | category | category,text,unknown | category0.86, text0.12, date0.00 |  |  |
| b070-0011 | ガソリン(TJ) | 6 ・ 16 ・ 4 ・ 0 ・ 7 | データID ・ 年度 ・ 部門 ・ カテゴリ ・ サブカテゴリ | quantity | unknown,unknown,quantity | other0.47, category0.40, quantity0.09 |  |  |
| b072-0203 | bauperiode | Periode von 1996 ・ Periode von 1996 ・ Periode von 1971 ・ Periode von 1991 ・ Periode von 2011 | jahr ・ bfs_nr_gemeinde ・ gebaeudekategorie_ ・ gebaeudekategorie ・ bauperiode_code | category | unknown,unknown,category | date0.89, org0.03, category0.03 |  |  |
| b073-0017 | 施設_名称 | 浦安駅第3自転車駐車場 ・ 浦安駅第4自転車駐車場 ・ 浦安駅第5自転車駐車場 ・ 浦安駅第6自転車駐車場 ・ 浦安駅第7自転車駐車場 | 施設_全国地方公共団体コード ・ 施設_名称（カナ） ・ 施設_施設通称 ・ 施設_POIコード ・ 施設_概要 | address | org,org,address | org0.61, address0.38, id0.00 |  |  |
| b073-0019 | 施設_施設通称 | 浦安駅第3自転車駐車場 ・ 浦安駅第4自転車駐車場 ・ 浦安駅第5自転車駐車場 ・ 浦安駅第6自転車駐車場 ・ 浦安駅第7自転車駐車場 | 施設_全国地方公共団体コード ・ 施設_名称 ・ 施設_名称（カナ） ・ 施設_POIコード ・ 施設_概要 | address | org,org,address | org0.66, address0.33, id0.00 |  |  |
| b074-0197 | designationOfficial | Castiglione ・ Domodossola, via ・ Bognanco, T. Vil ・ Boschetto ・ Campioli | numberShort ・ uicCountryCode ・ sloid ・ number ・ checkDigit | address | org,address,org | org0.55, address0.44, id0.00 |  |  |
| b074-0307 | BFS | 54 ・ 33 ・ 67 ・ 95 ・ 12 | ABSTIMMUNGSTAG ・ STAT_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ ・ STAT_GEMEINDE_ID | id | unknown,unknown,id | id0.65, quantity0.20, category0.13 | low_confidence_no_cue |  |
| b074-0318 | staatsan | CH ・ CH ・ CH ・ CH ・ CH | szenario ・ region ・ jahr ・ alter ・ anzahl | category | category,address,address | category0.64, address0.26, id0.07 |  |  |
| b077-0013 | LINIEN_TEXT | RERE7 ・ RERE7 ・ RERE7 ・ RERE7 ・ RERE7 | BETRIEBSTAG ・ FAHRT_BEZEICHNER ・ BETREIBER_ID ・ BETREIBER_ABK ・ PRODUKT_ID | category | category,id,id | category0.57, id0.41, text0.00 |  |  |
| b077-0019 | sg_Autonomie | 1 ・ 5 ・ -1 ・ -1 ・ -1 | Niederflurigkeit_F ・ Gebundenheit_Fahrz ・ sg_Rampeneinsatz ・ sg_Voranmeldung ・ sg_keinZugang | category | category,quantity,quantity | category0.66, quantity0.31, id0.01 |  |  |
| b077-0022 | sg_keinZugang | 5 ・ 5 ・ -1 ・ -1 ・ -1 | Niederflurigkeit_F ・ Gebundenheit_Fahrz ・ sg_Autonomie ・ sg_Rampeneinsatz ・ sg_Voranmeldung | category | quantity,unknown,category | quantity0.61, category0.31, other0.05 | low_confidence_no_cue |  |
| b077-0024 | ug_Autonomie | -1 ・ -1 ・ 1 ・ 5 ・ 2 | Niederflurigkeit_F ・ Gebundenheit_Fahrz ・ sg_Autonomie ・ sg_Rampeneinsatz ・ sg_Voranmeldung | category | category,quantity,unknown | category0.80, quantity0.17, other0.01 |  |  |
| b081-0146 | Purpose of Spend | Delivery of arts ・ Delivery of arts ・ Delivery of arts ・ Delivery of arts ・ Delivery of arts | Directorate/ Servi ・ Start Date ・ End Date ・ Award Amount (｣) ・ Registered Charity | text | text,account,account | text0.70, account0.24, category0.01 |  |  |
| b081-0152 | RBC Grant Reference | RBC 2014/1 ・ RBC 2014/14 ・ RBC 2014/17 ・ RBC 2014/18 ・ RBC 2014/19 | Purpose of Spend ・ Directorate/ Servi ・ Start Date ・ End Date ・ Award Amount (｣) | id | unknown,unknown,id | id0.92, category0.04, date0.02 | low_confidence_no_cue |  |
| b088-0010 | PARK_NO | 115.0 ・ 27.0 ・ 129.0 ・ 1255.0 ・ 1255.0 | OBJECTID_1 ・ PARK ・ BLDG_ID ・ BLDG_TYPE ・ CITY_BLDG_ | id | address,id,unknown | address0.58, id0.40, org0.01 |  |  |
| b090-0052 | 名称 | 彦根城 ・ 玄宮楽々園 ・ 彦根城博物館 ・ 夢京橋キャッスルロード ・ 四番町スクエア | 都道府県コード又は市区町村コード ・ 都道府県名 ・ 市区町村名 ・ 名称_カナ ・ 名称_英語 | address | address,org,org | address0.58, org0.41, text0.00 |  |  |
| b066-0027 | Estimated Start date of requirement | 0 to 6 Months ・ 0 to 6 Months ・ Start Date not y ・ Start Date not y ・ Start Date not y | BP ・ Title ・ Procurement Catego ・ Procurement Refere ・ Estimated value ra | category | category,category,date | category0.95, quantity0.03, text0.01 |  |  |
| b067-0318 | Adresszusatz | Anna-Seiler-Haus ・ ISE - Centre de  ・ Institut œcuméni ・ Karlihofplatz ・ Hôtel des Halles | ISIL ・ Status ・ Mutterinstitution ・ VZ-Sigel ・ VZ-Code | address | address,address,org | address0.96, org0.03, id0.00 |  |  |
| b070-0014 | A重油(TJ) | 266 ・ 306 ・ 34 ・ 0 ・ 479 | データID ・ 年度 ・ 部門 ・ カテゴリ ・ サブカテゴリ | quantity | unknown,quantity,quantity | other0.56, quantity0.40, category0.01 |  |  |
| b072-0141 | dokument_titel | M-095-2014-vorst ・ I-227-2014-vorst ・ M-232-2014-vorst ・ M-155-2014-vorst ・ 2015.RRGR.577-be | dokument_geschaeft ・ dokument_geschaeft ・ dokument_typ_deuts ・ dokument_typ_franz ・ dokument_ziel_publ | text | text,id,text | text0.50, other0.24, id0.15 |  |  |
| b072-0228 | designation | Quai 1 ・ Passage inférieu ・ Passage inférieu ・ Devant le début  ・ place de la gare | sloid ・ parentSloidService ・ parentNumberServic ・ mainReferencePoint ・ additionalInformat | address | address,address,category | address0.65, category0.29, text0.02 |  |  |
| b073-0025 | 施設_料金備考 | 一時利用のみ ・ 一時利用のみ ・ 一時利用のみ ・ 一時利用のみ | 施設_全国地方公共団体コード ・ 施設_名称 ・ 施設_名称（カナ） ・ 施設_施設通称 ・ 施設_POIコード | text | category,text,text | category0.83, text0.16, id0.00 |  |  |
| b073-0247 | 備考 | ※ ・ ※ | ランキング ・ ページタイトル ・ アクセス数 | text | text,text,category | text0.81, category0.17, date0.00 |  |  |
| b073-0350 | 主製品等 | 桧フローリング･集成床板･壁板等 ・ ペットフード製造 ・ 菌床しいたけの生産 ・ 学生服･スラックスの製造 ・ 野菜及び魚の仕分け、冷凍保存 | 市区町村コード ・ NO ・ 都道府県名 ・ 市区町村名 ・ 指定年（西暦） | text | text,unknown,text | text0.74, category0.20, product0.03 |  |  |
| b074-0165 | hauptgruppe | Land- und Forstw ・ Land- und Forstw ・ Land- und Forstw ・ Land- und Forstw ・ Land- und Forstw | jahr ・ substanz ・ untergruppe ・ sektor ・ kanton | category | category,address,category | category0.98, address0.01, id0.00 |  |  |
| b074-0190 | numberShort | 22012 ・ 22033 ・ 22005 ・ 22006 ・ 22010 | uicCountryCode ・ sloid ・ number ・ checkDigit ・ validFrom | id | id,id,unknown | id0.75, other0.12, quantity0.10 | low_confidence_no_cue |  |
| b077-0020 | sg_Rampeneinsatz | 2 ・ 5 ・ -1 ・ -1 ・ -1 | Niederflurigkeit_F ・ Gebundenheit_Fahrz ・ sg_Autonomie ・ sg_Voranmeldung ・ sg_keinZugang | category | category,category,quantity | category0.66, other0.11, rate0.10 |  |  |
| b078-0074 | strassenbezeichnung_index | Gem ・ Wei ・ Häs ・ Häs ・ Egg | egid ・ gemeindenummer_bfs ・ eidgenoessischer_e ・ eingangsnummer_geb ・ strassenbezeichnun | address | unknown,address,address | address0.49, id0.31, category0.10 |  |  |
| b080-0010 | Category | Bridges ・ Bridges ・ Bridges ・ Bridges ・ Bridges | Fund ・ Organization Level ・ Dept ・ Org ・ AU | category | account,category,category | account0.64, category0.34, org0.01 |  |  |
| b085-0086 | Main  department | Home Office ・ Home Office ・ Home Office | Organisation ・ Delegated grades o ・ SCS on standard co ・ Information for SC ・ Comments | org | org,org,account | org0.94, account0.04, address0.01 |  |  |
| b087-0011 | Department | MoD ・ MoD ・ MoD ・ MoD ・ MoD | HNG Ref No ・ Basis for expendit ・ Total Value Approv ・ Date of approval | org | org,org,account | org0.54, account0.44, category0.01 |  |  |
| b090-0054 | 名称_英語 | Hikone Castle ・ Genkyu-en Garden ・ Hikone Castle Mu ・ Yumekyobashi Cas ・ Yonban-cho Squar | 都道府県コード又は市区町村コード ・ 都道府県名 ・ 市区町村名 ・ 名称 ・ 名称_カナ | address | address,org,address | address0.58, org0.41, id0.00 |  |  |

## 本体が自信をもって誤り

| id | 列名 | 値 | 兄弟の列 | 正解 | 最終（3 本） | 上位 3（種子 1） | 理由 | 辞書 |
|---|---|---|---|---|---|---|---|---|
| b067-0249 | zustaendigkeit | Departement für  ・ Departement für  ・ Departement für  ・ Departement für  ・ Departement für  | datum_geschaeft_ei ・ datum_geschaeft_ab ・ geschaeftsnummer ・ grg_nummer ・ geschaftstitel | account | org,org,org | org0.97, account0.01, address0.01 |  |  |
| b067-0309 | Kollation | Ts./Dg. 8 Bl. ・ Ts./Dg. mit Korr ・ Ts./Dg. mit Korr ・ Ts./Dg. mit Korr ・ Ts./Dg. mit Korr | ID ・ Signatur ・ AutorIn ・ Titel ・ Titelvariante | text | category,category,category | category0.95, text0.04, date0.00 |  |  |
| b067-0328 | Kollation | 8°, 2 S., hs. ・ 8°, 2 S., hs. ・ 10 Bl. in Papier ・ auf 2 Briefumsch ・ 8°, 1 Bl., hs. | ID ・ Signatur ・ AutorIn ・ Titel ・ Ort | text | category,category,category | category0.99, text0.00, id0.00 |  |  |
| b067-0428 | VORLAGENART_ID | 3 ・ 2 ・ 1 ・ 2 ・ 1 | ABSTIMMTAG ・ STAT_VORLAGE_ID ・ BFS_VORLAGE_ID ・ VORLAGE_KURZBEZ ・ VORLAGE_LANGBEZ | category | id,id,id | id0.96, category0.03, address0.00 |  |  |
| b068-0007 | Less than $5,000, Number | 1470 ・ 360 ・ 4840 ・ 3070 ・ 23850 | Province or Territ ・ Total, All Recipie ・ Total, All Recipie ・ Less than $5,000,  ・ $5,000 to $9,999,  | quantity | amount,amount,amount | quantity0.99, id0.00, amount0.00 | verifier:quantity | K0043 |
| b068-0067 | question_value_f | Tous les réponda ・ Oui ・ Non ・ Oui ・ Oui | dept_f ・ dept_e ・ question ・ question_value_e ・ shr_w_resp | category | text,text,text | text0.96, category0.03, date0.00 |  |  |
| b069-0009 | NACE_Code | R9311 ・ J5812 ・ D3511 ・ D3511 ・ D3513 | Obs ・ Data_Vintage ・ Publication_Month ・ Publication_Year ・ Controlling_Sub_Se | category | id,id,id | id0.99, category0.00, address0.00 |  |  |
| b069-0014 | Sub Sector | S1311 ・ S1311 ・ S11001 ・ S11001 ・ S12001 | Obs ・ Data Vintage ・ Publication Month ・ Publication Year ・ Government Departm | category | unknown,id,id | id0.87, category0.12, address0.00 | low_confidence_no_cue |  |
| b069-0016 | NACE Code | M7219 ・ O8423 ・ D3511 ・ D3510 ・ K6492 | Obs ・ Data Vintage ・ Publication Month ・ Publication Year ・ Sub Sector | category | id,id,id | id0.99, address0.00, category0.00 |  |  |
| b072-0200 | gebaeudekategorie_code | 1021 ・ 1021 ・ 1025 ・ 1025 ・ 1025 | jahr ・ bfs_nr_gemeinde ・ gebaeudekategorie ・ bauperiode_code ・ bauperiode | category | id,id,id | id0.71, category0.27, address0.01 | low_confidence_no_cue |  |
| b073-0002 | 名称 | 真岡小学校 ・ 亀山小学校 ・ 真岡中学校 ・ 真岡西中学校 ・ 真岡高等学校 | NO ・ 名称_カナ ・ 市区町村コード ・ 災害種別_洪水 ・ 災害種別_崖崩れ、土石流及び地滑り | address | org,org,org | org0.97, address0.02, account0.00 |  |  |
| b073-0020 | 施設_POIコード | 3732 ・ 3732 ・ 3732 ・ 3732 ・ 3732 | 施設_全国地方公共団体コード ・ 施設_名称 ・ 施設_名称（カナ） ・ 施設_施設通称 ・ 施設_概要 | id | category,category,category | category0.96, id0.03, quantity0.00 |  |  |
| b074-0116 | Strassenbezeichnung Sprache Code | 9901 ・ 9901 ・ 9901 ・ 9901 ・ 9901 | EGID ・ EDID ・ EGAID ・ Eingangsnummer Geb ・ ESID | category | id,id,id | id0.71, category0.27, address0.01 |  |  |
| b074-0180 | eigentuemer_code | 2 ・ 1 ・ 1 ・ 2 ・ 3 | jahr ・ bfs_nr_gemeinde ・ gebaeudekategorie_ ・ gebaeudekategorie ・ bauperiode_code | category | id,id,unknown | id0.97, category0.02, address0.00 |  |  |
| b074-0182 | heizsystem_code | 7430 ・ 7410 ・ 7410 ・ 7410 ・ 7452 | jahr ・ bfs_nr_gemeinde ・ gebaeudekategorie_ ・ gebaeudekategorie ・ bauperiode_code | category | id,id,id | id0.98, category0.01, address0.00 |  |  |
| b074-0213 | designation | Schiffsteg Mosen ・ Berggasthaus Egg ・ Toilette ・ Toilette quai 3/ ・ Toilettes | sloid ・ parentSloidService ・ parentNumberServic ・ additionalInformat ・ wheelchairToilet | address | category,category,category | category0.97, address0.01, text0.01 |  |  |
| b076-0067 | designation | M ・ C ・ B ・ A ・ P | sloid ・ numberShort ・ uicCountryCode ・ number ・ checkDigit | id | category,category,category | category0.97, id0.02, text0.00 |  |  |
| b076-0075 | designation | C ・ A ・ C ・ D ・ D | sloid ・ type ・ trafficPointSloid ・ validFrom ・ validTo | id | category,category,category | category0.97, id0.02, text0.00 |  |  |
| b078-0056 | rechtsform_code | 0101 ・ 0101 ・ 0107 ・ 0101 ・ 0101 | kategorie ・ publikationsdatum_ ・ journaldatum_hande ・ id_shab ・ firmensitz_code | category | id,id,id | id0.99, category0.01, tax_class0.00 |  |  |
| b078-0062 | koordinatenherkunft_code | 901 ・ 901 ・ 901 ・ 901 ・ 901 | egid ・ gemeindenummer_bfs ・ egrid ・ grundstücksnummer ・ koordinatenherkunf | category | id,id,id | id0.98, category0.01, address0.01 |  |  |
| b078-0064 | gebaeudestatus_code | 1004 ・ 1004 ・ 1004 ・ 1004 ・ 1004 | egid ・ gemeindenummer_bfs ・ egrid ・ grundstücksnummer ・ koordinatenherkunf | category | id,id,id | id0.98, category0.01, address0.00 |  |  |
| b078-0071 | eingangsnummer_gebaeude | 14 ・ 8 ・ 96 ・ 116 ・ 86 | egid ・ gemeindenummer_bfs ・ eidgenoessischer_e ・ strassenbezeichnun ・ strassenbezeichnun | id | address,address,address | address0.98, id0.01, org0.00 |  | K0003 |
| b078-0111 | KONFESSION_CODE | 0 ・ 121 ・ 121 ・ 121 ・ 121 | BFS_NR_GEMEINDE ・ BEZIRK_NR ・ JAHR ・ KONFESSION_BEZEICH ・ ANZAHL_PERSONEN | category | unknown,id,id | id0.92, category0.07, tax_class0.00 | low_confidence_no_cue |  |
| b088-0017 | REGION | N ・ C ・ N ・ N ・ N | OBJECTID_1 ・ PARK ・ PARK_NO ・ BLDG_ID ・ BLDG_TYPE | id | category,category,category | category0.93, id0.03, address0.03 |  |  |
| b090-0177 | 歯科口腔外科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 歯科 ・ 矯正歯科 | category | quantity,unknown,quantity | quantity0.97, category0.02, id0.00 |  |  |
| b090-0184 | 消化器科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 療養病床数 ・ 内科 | category | quantity,unknown,quantity | quantity0.97, category0.02, id0.00 |  |  |
| b090-0186 | 循環器科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 療養病床数 ・ 内科 | category | quantity,unknown,quantity | quantity0.98, category0.01, id0.00 |  |  |
| b090-0187 | 小児科 | 1 ・ 1 ・ 1 ・ 1 ・ 1 | 施設正式名称 ・ 開設年月日 ・ 一般病床数 ・ 療養病床数 ・ 内科 | category | quantity,unknown,quantity | quantity0.98, category0.01, id0.00 |  |  |
| b090-0253 | その他 | 2280452 ・ 2327463 ・ 3295785 ・ 7367725 ・ 3603168 | 区　　分 ・ 合 計 ・ 宿泊費 ・ 飲食費 ・ 土産品費 | amount | quantity,quantity,quantity | quantity0.96, id0.02, amount0.01 |  |  |
| b066-0110 | Death - Accidental | 0 ・ 0 ・ 0 ・ 0 ・ 0 | Oct-10 ・ Abduction ・ Arrest/Detention - ・ Arrest/Detention - ・ Arrest/Detention - | quantity | quantity,unknown,quantity | quantity0.99, category0.01, amount0.00 |  |  |
| b068-0069 | shr_w_resp | 1 ・ 0.504 ・ 0.572 ・ 0.708 ・ 0.649 | dept_f ・ dept_e ・ question ・ question_value_f ・ question_value_e | rate | unknown,rate,rate | rate0.67, quantity0.23, other0.08 | low_confidence_no_cue |  |
| b078-0053 | firmensitz_code | 2844 ・ 2892 ・ 2770 ・ 2770 ・ 2765 | kategorie ・ publikationsdatum_ ・ journaldatum_hande ・ id_shab ・ firmensitz | id | id,id,unknown | id0.96, address0.03, category0.01 |  |  |
| b081-0030 | Percentage paid within 30 working d | DFTc ・ MCA Agency ・ HA Agency ・ DSA Agency ・ DVLA Agency | Jan-12 ・ Feb-12 ・ Mar-12 ・ Apr-12 ・ May-12 | org | org,org,rate | org0.97, account0.01, address0.01 |  | K0040 |
| b085-0076 | Flights | 2 ・ 1 ・ 1 ・ 1 ・ 2 | Fare Paid ・ Departure Date ・ Origin City ・ Destination Airpor ・ Destination City | quantity | quantity,quantity,unknown | quantity0.97, category0.02, other0.00 |  |  |

## 正解が上位 3 に無い

| id | 列名 | 値 | 兄弟の列 | 正解 | 最終（3 本） | 上位 3（種子 1） | 理由 | 辞書 |
|---|---|---|---|---|---|---|---|---|
| b067-0186 | geschaeft_federfuehrung_kuerzel_deu | DIJ ・ FIN ・ STA ・ BVD ・ FIN | geschaeft_nr ・ geschaeft_typ_deut ・ geschaeft_typ_fran ・ geschaeft_federfue ・ geschaeft_vorberat | account | unknown,org,org | category0.49, org0.39, address0.05 |  |  |
| b067-0187 | geschaeft_federfuehrung_kuerzel_fra | DIJ ・ FIN ・ CHA ・ DTT ・ FIN | geschaeft_nr ・ geschaeft_typ_deut ・ geschaeft_typ_fran ・ geschaeft_federfue ・ geschaeft_vorberat | account | org,org,org | org0.95, category0.02, address0.01 |  |  |
| b067-0286 | designation | Parking ・ Parking ・ Parking ・ Parking ・ Parking | sloid ・ parentSloidService ・ parentNumberServic ・ additionalInformat ・ placesAvailable | address | category,category,category | category0.98, text0.01, account0.00 |  |  |
| b069-0010 | Obs | 70.0 ・ 102.0 ・ 233.0 ・ 242.0 ・ 278.0 | Data Vintage ・ Publication Month ・ Publication Year ・ Sub Sector ・ Government Departm | id | unknown,unknown,unknown | quantity0.95, amount0.04, other0.00 | low_confidence_no_cue |  |
| b072-0191 | koordinaten | 47.5602763509581 ・ 47.5569415632088 ・ 47.5594057994964 ・ 47.5602763509581 ・ 47.5545873399660 | available_spots ・ deactivated_spots ・ occupied_spots ・ timestamp ・ total_spots | quantity | unknown,unknown,unknown | other0.98, rate0.01, address0.00 |  |  |
| b072-0247 | FotografIn | Berchem, Max van ・ Berchem, Max van ・ Berchem, Max van ・ Berchem, Max van ・ Berchem, Max van | ID ・ Signatur ・ Titel ・ Inhalt_Kurzbeschre ・ Datierung_von | id | person,person,person | person0.88, org0.03, other0.02 |  |  |
| b073-0223 | 開設 | 41000.0 ・ 41760.0 ・ 41487.0 ・ 45030.0 ・ 41334.0 | № ・ 施設名 ・ 定員 ・ 設置者 | date | quantity,quantity,quantity | quantity0.98, id0.01, amount0.00 |  |  |
| b073-0244 | ランキング | 5 ・ 9 ・ 14 ・ 23 ・ 26 | ページタイトル ・ アクセス数 ・ 備考 | category | unknown,unknown,unknown | quantity0.56, id0.32, other0.09 |  |  |
| b077-0010 | BETREIBER_ABK | DB ・ DB ・ DB ・ DB ・ DB | BETRIEBSTAG ・ FAHRT_BEZEICHNER ・ BETREIBER_ID ・ PRODUKT_ID ・ LINIEN_ID | org | category,category,category | category0.98, id0.01, text0.00 |  |  |
| b078-0119 | EINWOHNER_MAENNER | 2583 ・ 23 ・ x ・ 95 ・ 1104 | POLITISCHE_GEMEIND ・ BFS_NR_GEMEINDE ・ BEZIRK_NR ・ ORTSCHAFT ・ EINWOHNER_TOTAL | quantity | unknown,unknown,unknown | other0.85, address0.06, id0.03 |  |  |
| b081-0048 | RevisionNumber | 0 ・ 0 ・ 0 ・ 0 ・ 0 | NptgLocalityCode ・ AdministrativeArea ・ NptgDistrictCode ・ SourceLocalityType ・ Easting | quantity | id,id,id | id0.99, category0.00, address0.00 |  |  |
| b088-0016 | COMM_AREA | 1.0 ・ 0.0 ・ 25.0 ・ 77.0 ・ 77.0 | OBJECTID_1 ・ PARK ・ PARK_NO ・ BLDG_ID ・ BLDG_TYPE | id | unknown,unknown,unknown | other0.97, address0.01, rate0.01 |  |  |
| b090-0321 | 都市計画税 | ● ・ ● ・ ● ・ ● ・ ● | 都市計画区域名 ・ 市町村名 ・ 旧市町村名 ・ 土地利用 ・ 都市施設 | category | tax_class,unknown,unknown | tax_class0.66, amount0.26, id0.02 |  |  |
| b070-0015 | B重油(TJ) | 0 ・ 4 ・ 0 ・ 0 ・ 0 | データID ・ 年度 ・ 部門 ・ カテゴリ ・ サブカテゴリ | quantity | unknown,unknown,quantity | other0.85, category0.07, rate0.03 |  |  |
