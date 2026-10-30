# ラベル用シート 001 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：valueCategory
- 例1 値：cases | cases | cases | cases | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0002（3 列）
- 見出し：temporal
- 例1 値：2013 | 2015 | 2018 | 2025-M08 | 2022-M10
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value
- 例2 値：2015 | 2026-M09 | 2023 | 2018 | 2025
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type

## g0003（3 列）
- 見出し：temporal_type
- 例1 値：month | year | month | year | year
  - 同じ表の列：valueCategory, temporal, georegion, georegion_type, agegroup, agegroup_type, sex, value
- 例2 値：year | month | year | year | month
  - 同じ表の列：valueCategory, temporal, georegion, georegion_type, agegroup, agegroup_type, sex, type

## g0004（3 列）
- 見出し：georegion
- 例1 値：VS | VD | UR | SG | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, value
- 例2 値：CHFL | CHFL | CHFL | GE | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, type

## g0005（3 列）
- 見出し：georegion_type
- 例1 値：CHFL | CHFL | country | CHFL | canton
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, value
- 例2 値：canton | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, type

## g0006（1 列）
- 見出し：agegroup
- 例1 値：all | 45 - 64 | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, value

## g0007（3 列）
- 見出し：agegroup_type
- 例1 値：agegroup_food | agegroup_food | agegroup_food | agegroup_food | agegroup_food
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, value
- 例2 値：agegroup_food | agegroup_food | agegroup_food | agegroup_food | agegroup_food
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, type

## g0008（4 列）
- 見出し：sex
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, value
- 例2 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, type

## g0009（5 列）
- 見出し：value
- 例1 値：15 | 1 | 23 | 17 | 17
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex
- 例2 値：130 | 1267 | 470 | 77 | 44
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0010（2 列）
- 見出し：pop
- 例1 値：39055 | NA | 357282 | 79417 | 128794
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex
- 例2 値：35865 | 55585 | NA | 273801 | 297671
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0011（1 列）
- 見出し：valueCategory
- 例1 値：max_value_10y | cases | cases | cases_10y_mean | median_value_10y
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type

## g0012（2 列）
- 見出し：agegroup
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, type
- 例2 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, value

## g0013（1 列）
- 見出し：type
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0014（1 列）
- 見出し：valueCategory
- 例1 値：cases | cases | cases | cases_10y_mean | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0015（12 列）
- 見出し：Jahr
- 例1 値：2012 | 2016 | 2024 | 2012 | 2010
  - 同じ表の列：Energiesektor, Wert, Einheit
- 例2 値：2030 | 2030 | 2020 | 2015 | 2020
  - 同じ表の列：substanz, hauptgruppe, untergruppe, gemeinde, emission, bfsnr, kanton, einheit

## g0016（1 列）
- 見出し：Energiesektor
- 例1 値：Waerme | Waerme | Treibstoff | Strom | Waerme
  - 同じ表の列：Jahr, Wert, Einheit

## g0017（2 列）
- 見出し：Wert
- 例1 値：9161104 | 12246495 | 14779550 | 14813997 | 17405612
  - 同じ表の列：Jahr, Energiesektor, Einheit
- 例2 値：17 | 3791598 | 102 | 2635829 | 698
  - 同じ表の列：thema, indikator, einheit, region, jahr

## g0018（1 列）
- 見出し：Einheit
- 例1 値：MWh | MWh | MWh | MWh | MWh
  - 同じ表の列：Jahr, Energiesektor, Wert

## g0019（1 列）
- 見出し：substanz
- 例1 値：NOx | PM10 | NMVOC | BC | PM10
  - 同じ表の列：jahr, hauptgruppe, untergruppe, gemeinde, emission, bfsnr, kanton, einheit

## g0020（1 列）
- 見出し：hauptgruppe
- 例1 値：Industrie | Haushalte | Land- und Forstw. | Industrie | Verkehr
  - 同じ表の列：jahr, substanz, untergruppe, gemeinde, emission, bfsnr, kanton, einheit

## g0021（1 列）
- 見出し：untergruppe
- 例1 値：Zonenverkehr | Haushalte andere Brände etc | Kläranlagen | Deponien | Strassenverkehr
  - 同じ表の列：jahr, substanz, hauptgruppe, gemeinde, emission, bfsnr, kanton, einheit

## g0022（1 列）
- 見出し：gemeinde
- 例1 値：Aeugst am Albis | Aeugst am Albis | Aeugst am Albis | Aeugst am Albis | Aeugst am Albis
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, emission, bfsnr, kanton, einheit

## g0023（1 列）
- 見出し：emission
- 例1 値：0 | 0 | 0 | 0 | 0.001210878
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, gemeinde, bfsnr, kanton, einheit

## g0024（2 列）
- 見出し：bfsnr
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, gemeinde, emission, kanton, einheit
- 例2 値：3272 | 3236 | 3218 | 3395 | 3233
  - 同じ表の列：date, commune, nationality_categor…, sex, age, anzahl_personen

## g0025（3 列）
- 見出し：kanton
- 例1 値：ZH | ZH | ZH | ZH | ZH
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, gemeinde, emission, bfsnr, einheit
- 例2 値：SG | SG | SG | SG | SG
  - 同じ表の列：ZST, Strassennummer, Zählstellen-Bezeich…, Richtung 1, Richtung 2, TAG, JJMMTT, Tag_Nr

## g0026（1 列）
- 見出し：einheit
- 例1 値：t/a | t/a | t/a | t/a | t/a
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, gemeinde, emission, bfsnr, kanton

## g0027（1 列）
- 見出し：einheit_lang
- 例1 値：Tonnen pro Jahr | Tonnen pro Jahr | Tonnen pro Jahr | Tonnen pro Jahr | Tonnen pro Jahr
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, gemeinde, emission, bfsnr, kanton

## g0028（1 列）
- 見出し：thema
- 例1 値：Bahnanteil | Bahnanteil | Regionen | Bahnanteil | Kiesabbau
  - 同じ表の列：indikator, einheit, region, jahr, wert

## g0029（1 列）
- 見出し：indikator
- 例1 値：Kiesabbau | Kiesabbau | Summe | Kiesabbau | Aushubeinbau
  - 同じ表の列：thema, einheit, region, jahr, wert

## g0030（1 列）
- 見出し：einheit
- 例1 値：m3 fest | ha | m3 fest | % | m3 fest
  - 同じ表の列：thema, indikator, region, jahr, wert

## g0031（1 列）
- 見出し：region
- 例1 値：Kanton Zürich | Kanton Zürich | Kanton Zürich | Kanton Zürich | Kanton Zürich
  - 同じ表の列：thema, indikator, einheit, jahr, wert

## g0032（1 列）
- 見出し：Sprachregion
- 例1 値：CH | fr | fr | CH | fr
  - 同じ表の列：Altersgruppe, Frage, Antwort, Anzahl

## g0033（1 列）
- 見出し：Altersgruppe
- 例1 値：6bis9 | 10bis13 | 14bis17 | 10bis13 | 10bis13
  - 同じ表の列：Sprachregion, Frage, Antwort, Anzahl

## g0034（1 列）
- 見出し：Frage
- 例1 値：c09B_10 | c09B_10 | c09B_02 | c09B_02 | c09B_09
  - 同じ表の列：Sprachregion, Altersgruppe, Antwort, Anzahl

## g0035（1 列）
- 見出し：Antwort
- 例1 値：a77 | a78 | a77 | a77 | a77
  - 同じ表の列：Sprachregion, Altersgruppe, Frage, Anzahl

## g0036（3 列）
- 見出し：Anzahl
- 例1 値：0 | 1 | 0 | 0 | 0
  - 同じ表の列：Sprachregion, Altersgruppe, Frage, Antwort
- 例2 値：109 | 11 | 161 | 345 | 66
  - 同じ表の列：scen, gdenr, jahr, altersklasse

## g0037（1 列）
- 見出し：ID
- 例1 値：ep11 | ep8 | ep27 | ep19 | ep24
  - 同じ表の列：DE, FR, IT, EN

## g0038（1 列）
- 見出し：DE
- 例1 値：Mykotoxine, Mikrobiologie, Farbstoffe, … | verbotene Arzneistoffe und Kennzeichnung | Mikrobiologischen und chemischen Kriter… | Ethylenoxid-Rückstände | Mikrobiologie (Salmonellen und Listerie…
  - 同じ表の列：ID, FR, IT, EN

## g0039（1 列）
- 見出し：FR
- 例1 値：Norovirus | Résidus de pesticides | Aflatoxines | Conservateurs et substances parfumantes… | Mycotoxines et salmonelles
  - 同じ表の列：ID, DE, IT, EN

## g0040（1 列）
- 見出し：IT
- 例1 値：Micotossine, aspetti microbiologici, co… | Micotossine e microbiologia | Salmonella, trattamento mediante irradi… | Aflatossine | Norovirus
  - 同じ表の列：ID, DE, FR, EN

## g0041（1 列）
- 見出し：EN
- 例1 値：Cadmium | Pesticide residues | Allergenic fragrances | Contamination with polycyclic aromatic … | Mycotoxins and salmonella
  - 同じ表の列：ID, DE, FR, IT

## g0042（2 列）
- 見出し：PERSPECTIVE
- 例1 値：R | R | R | R | R
  - 同じ表の列：REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE
- 例2 値：R | R | R | R | R
  - 同じ表の列：REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE

## g0043（2 列）
- 見出し：REF_YEAR
- 例1 値：2014 | 2014 | 2014 | 2014 | 2014
  - 同じ表の列：PERSPECTIVE, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE
- 例2 値：2018 | 2018 | 2018 | 2018 | 2018
  - 同じ表の列：PERSPECTIVE, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE

## g0044（2 列）
- 見出し：GEO_CANT_RESID
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE
- 例2 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE

## g0045（2 列）
- 見出し：GEO_COMM_RESID
- 例1 値：29 | 4 | 4 | 3 | 1
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE
- 例2 値：3 | 10 | 25 | 26 | 26
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE

## g0046（2 列）
- 見出し：GEO_CANT_WORK
- 例1 値：1 | 1 | 1 | 1 | 19
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_COMM_WORK, VALUE
- 例2 値：1 | 1 | 19 | 1 | 1
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_COMM_WORK, VALUE

## g0047（2 列）
- 見出し：GEO_COMM_WORK
- 例1 値：35 | 2 | 14 | 53 | 138
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, VALUE
- 例2 値：4001 | 10 | 230 | 1322 | 7777
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, VALUE

## g0048（1 列）
- 見出し：RELI
- 例1 値：57731944 | 59562264 | 60062072 | 50611195 | 54161649
  - 同じ表の列：E_COORD, N_COORD, YEAR, POP_TOTAL, D_BAKERY, D_BOOK, D_GARAGE, D_GROCERY

## g0049（1 列）
- 見出し：E_COORD
- 例1 値：2757200 | 2683400 | 2557000 | 2607000 | 2596100
  - 同じ表の列：RELI, N_COORD, YEAR, POP_TOTAL, D_BAKERY, D_BOOK, D_GARAGE, D_GROCERY

## g0050（1 列）
- 見出し：N_COORD
- 例1 値：1198700 | 1200300 | 1233500 | 1118200 | 1265000
  - 同じ表の列：RELI, E_COORD, YEAR, POP_TOTAL, D_BAKERY, D_BOOK, D_GARAGE, D_GROCERY

## g0051（1 列）
- 見出し：YEAR
- 例1 値：2018 | 2018 | 2018 | 2018 | 2018
  - 同じ表の列：RELI, E_COORD, N_COORD, POP_TOTAL, D_BAKERY, D_BOOK, D_GARAGE, D_GROCERY

## g0052（1 列）
- 見出し：POP_TOTAL
- 例1 値：13 | 21 | 37 | 48 | 7
  - 同じ表の列：RELI, E_COORD, N_COORD, YEAR, D_BAKERY, D_BOOK, D_GARAGE, D_GROCERY

## g0053（1 列）
- 見出し：D_BAKERY
- 例1 値：1874 | 574 | 2495 | 653 | 3056
  - 同じ表の列：RELI, E_COORD, N_COORD, YEAR, POP_TOTAL, D_BOOK, D_GARAGE, D_GROCERY

## g0054（1 列）
- 見出し：D_BOOK
- 例1 値：2494 | 1592 | 987 | 2454 | 3952
  - 同じ表の列：RELI, E_COORD, N_COORD, YEAR, POP_TOTAL, D_BAKERY, D_GARAGE, D_GROCERY

## g0055（1 列）
- 見出し：D_GARAGE
- 例1 値：3641 | 1119 | 1796 | 234 | 657
  - 同じ表の列：RELI, E_COORD, N_COORD, YEAR, POP_TOTAL, D_BAKERY, D_BOOK, D_GROCERY

## g0056（1 列）
- 見出し：D_GROCERY
- 例1 値：430 | 2242 | 737 | 3476 | 71
  - 同じ表の列：RELI, E_COORD, N_COORD, YEAR, POP_TOTAL, D_BAKERY, D_BOOK, D_GARAGE

## g0057（1 列）
- 見出し：D_HMARKET
- 例1 値：26053 | 8585 | 21587 | 8287 | 2233
  - 同じ表の列：RELI, E_COORD, N_COORD, YEAR, POP_TOTAL, D_BAKERY, D_BOOK, D_GARAGE

## g0058（3 列）
- 見出し：Anfangszeit
- 例1 値：2026-10-12T14:30:00+00:00 | 2026-10-23T21:00:00+00:00 | 2026-10-15T03:00:00+00:00 | 2026-10-20T08:00:00+00:00 | 2026-10-18T22:00:00+00:00
  - 同じ表の列：Temperatur, Druck, Feuchte, Windgeschwindigkeit, Windrichtung
- 例2 値：2026-10-24T12:30:00+00:00 | 2026-10-13T16:30:00+00:00 | 2026-10-15T11:00:00+00:00 | 2026-10-22T10:30:00+00:00 | 2026-10-25T03:00:00+00:00
  - 同じ表の列：Temperatur, Druck, Feuchte, Windgeschwindigkeit, Windrichtung

## g0059（2 列）
- 見出し：Temperatur
- 例1 値：11.276 | 7.303704 | 9.943333 | 9.937931 | 14.27
  - 同じ表の列：Anfangszeit, Druck, Feuchte, Windgeschwindigkeit, Windrichtung
- 例2 値：8.8875 | 14.193 | 9.1 | 10.931 | 13.458
  - 同じ表の列：Anfangszeit, Druck, Feuchte, Windgeschwindigkeit, Windrichtung

## g0060（2 列）
- 見出し：Druck
- 例1 値：988.623333 | 988.833333 | 981.728571 | 978.333333 | 985.983333
  - 同じ表の列：Anfangszeit, Temperatur, Feuchte, Windgeschwindigkeit, Windrichtung
- 例2 値：979.04 | 976.08 | 984.12 | 962.21 | 983.14
  - 同じ表の列：Anfangszeit, Temperatur, Feuchte, Windgeschwindigkeit, Windrichtung

## g0061（2 列）
- 見出し：Feuchte
- 例1 値：74.884615 | 45.226923 | 84.793333 | 64.906667 | 81.013333
  - 同じ表の列：Anfangszeit, Temperatur, Druck, Windgeschwindigkeit, Windrichtung
- 例2 値：85.051 | 85.183 | 88.022 | 81.758 | 87.728
  - 同じ表の列：Anfangszeit, Temperatur, Druck, Windgeschwindigkeit, Windrichtung

## g0062（2 列）
- 見出し：Windgeschwindigkeit
- 例1 値：0.754167 | 4.0 | 1.173333 | 1.6 | 0.45
  - 同じ表の列：Anfangszeit, Temperatur, Druck, Feuchte, Windrichtung
- 例2 値：2.3754 | 1.1511 | 1.3148 | 1.486 | 1.6628
  - 同じ表の列：Anfangszeit, Temperatur, Druck, Feuchte, Windrichtung

## g0063（2 列）
- 見出し：Windrichtung
- 例1 値：122.918266 | 274.051234 | 244.279333 | 98.432961 | 59.328997
  - 同じ表の列：Anfangszeit, Temperatur, Druck, Feuchte, Windgeschwindigkeit
- 例2 値：265.66 | 239.26 | 178.73 | 96.114 | 32.291
  - 同じ表の列：Anfangszeit, Temperatur, Druck, Feuchte, Windgeschwindigkeit

## g0064（1 列）
- 見出し：PM10
- 例1 値：12.438 | 10.513 | 7.8075 | 14.72 | 8.7427
  - 同じ表の列：Anfangszeit, PM2.5, NO2

## g0065（1 列）
- 見出し：PM2.5
- 例1 値：6.1715 | 6.7136 | 2.6051 | 8.5788 | 4.0819
  - 同じ表の列：Anfangszeit, PM10, NO2

## g0066（1 列）
- 見出し：NO2
- 例1 値：21.475022 | 18.091415 | 7.003381 | 16.139731 | 21.773339
  - 同じ表の列：Anfangszeit, PM10, PM2.5

## g0067（1 列）
- 見出し：id
- 例1 値：122814 | 120477 | 122151 | 121937 | 122347
  - 同じ表の列：Jahr, Postleitzahl, Gemeinde, Alter, Rasse, Farbe

## g0068（1 列）
- 見出し：Postleitzahl
- 例1 値：4052 | 4056 | 4055 | 4058 | 4058
  - 同じ表の列：id, Jahr, Gemeinde, Alter, Rasse, Farbe

## g0069（2 列）
- 見出し：Gemeinde
- 例1 値：Basel | Basel | Basel | Basel | Basel
  - 同じ表の列：id, Jahr, Postleitzahl, Alter, Rasse, Farbe
- 例2 値：Altikon | Dinhard | Egg | Regensberg | Weiach
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, BFS, STAT_GEMEINDE_ID, BEZIRK, AZ_STIMMBERECHTIGTE

## g0070（2 列）
- 見出し：Alter
- 例1 値：10 | 6 | 5 | 7 | 9
  - 同じ表の列：id, Jahr, Postleitzahl, Gemeinde, Rasse, Farbe
- 例2 値：17 | 62 | 5 | 7 | 81
  - 同じ表の列：szenario, region, jahr, staatsan, anzahl

## g0071（1 列）
- 見出し：Rasse
- 例1 値：Cavalier King Charles Spaniel | Diverser Mischling | Labrador-Mix | Diverser Mischling | Pudel, klein und mittel
  - 同じ表の列：id, Jahr, Postleitzahl, Gemeinde, Alter, Farbe

## g0072（1 列）
- 見出し：Farbe
- 例1 値：Saufarben | Braun Schwarz | Tricolor | Schwarz | Tricolor
  - 同じ表の列：id, Jahr, Postleitzahl, Gemeinde, Alter, Rasse

## g0073（1 列）
- 見出し：EGID
- 例1 値：243055628 | 243058235 | 243057003 | 243057503 | 243058541
  - 同じ表の列：EDID, EGAID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…, Strassenbezeichnung…

## g0074（1 列）
- 見出し：EDID
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：EGID, EGAID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…, Strassenbezeichnung…

## g0075（1 列）
- 見出し：EGAID
- 例1 値：102410816 | 102437505 | 103373133 | 102436963 | 102436301
  - 同じ表の列：EGID, EDID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…, Strassenbezeichnung…

## g0076（1 列）
- 見出し：Eingangsnummer Gebäude
- 例1 値：21.2 | 22b | 14.1 | 24 | 2a
  - 同じ表の列：EGID, EDID, EGAID, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…, Strassenbezeichnung…

## g0077（1 列）
- 見出し：ESID
- 例1 値：10179490 | 10026581 | 10179490 | 10120297 | 10087620
  - 同じ表の列：EGID, EDID, EGAID, Eingangsnummer Gebä…, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…, Strassenbezeichnung…

## g0078（1 列）
- 見出し：Strassenbezeichnung
- 例1 値：Gotthardstrasse | Scherkesselweg | Niklaus von Flüe-Strasse | Bruderholzallee | Maienbühlsträsschen
  - 同じ表の列：EGID, EDID, EGAID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung…, Strassenbezeichnung…, Strassenbezeichnung…

## g0079（1 列）
- 見出し：Strassenbezeichnung kurz
- 例1 値：Leonhardsstr. | Dorfstr. | Giornicostr. | Prag-Str. | Unterer Batterieweg
  - 同じ表の列：EGID, EDID, EGAID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…

## g0080（1 列）
- 見出し：Strassenbezeichnung Index
- 例1 値：WEI | BRU | CHR | THI | KRA
  - 同じ表の列：EGID, EDID, EGAID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…

## g0081（1 列）
- 見出し：Strassenbezeichnung Sprache Code
- 例1 値：9901 | 9901 | 9901 | 9901 | 9901
  - 同じ表の列：EGID, EDID, EGAID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…

## g0082（1 列）
- 見出し：Strassenbezeichnung Sprache Bezeichnung
- 例1 値：Deutsch | Deutsch | Deutsch | Deutsch | Deutsch
  - 同じ表の列：EGID, EDID, EGAID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…

## g0083（1 列）
- 見出し：Scheidungsdatum
- 例1 値：2024-05-27 | 2024-05-28 | 2025-07-08 | 2024-08-26 | 2024-04-18
  - 同じ表の列：Jahr, Monat, Kalenderwoche, Datum Wochenstart, Tag in Jahr, Wochentag, Alter Partner 1, Alter Partner 2

## g0084（1 列）
- 見出し：Monat
- 例1 値：6 | 9 | 6 | 11 | 6
  - 同じ表の列：Scheidungsdatum, Jahr, Kalenderwoche, Datum Wochenstart, Tag in Jahr, Wochentag, Alter Partner 1, Alter Partner 2

## g0085（1 列）
- 見出し：Kalenderwoche
- 例1 値：37 | 50 | 26 | 7 | 27
  - 同じ表の列：Scheidungsdatum, Jahr, Monat, Datum Wochenstart, Tag in Jahr, Wochentag, Alter Partner 1, Alter Partner 2

## g0086（1 列）
- 見出し：Datum Wochenstart
- 例1 値：2023-08-21 | 2024-04-08 | 2024-05-27 | 2025-06-23 | 2025-07-07
  - 同じ表の列：Scheidungsdatum, Jahr, Monat, Kalenderwoche, Tag in Jahr, Wochentag, Alter Partner 1, Alter Partner 2

## g0087（1 列）
- 見出し：Tag in Jahr
- 例1 値：122 | 146 | 59 | 172 | 30
  - 同じ表の列：Scheidungsdatum, Jahr, Monat, Kalenderwoche, Datum Wochenstart, Wochentag, Alter Partner 1, Alter Partner 2

## g0088（2 列）
- 見出し：Wochentag
- 例1 値：Mo | Di | Mo | Di | Mo
  - 同じ表の列：Scheidungsdatum, Jahr, Monat, Kalenderwoche, Datum Wochenstart, Tag in Jahr, Alter Partner 1, Alter Partner 2
- 例2 値：Dienstag | Donnerstag | Freitag | Mittwoch | Mittwoch
  - 同じ表の列：ZST, Strassennummer, Zählstellen-Bezeich…, Kanton, Richtung 1, Richtung 2, TAG, JJMMTT

## g0089（1 列）
- 見出し：Alter Partner 1
- 例1 値：58 | 56 | 45 | 38 | 53
  - 同じ表の列：Scheidungsdatum, Jahr, Monat, Kalenderwoche, Datum Wochenstart, Tag in Jahr, Wochentag, Alter Partner 2

## g0090（1 列）
- 見出し：Alter Partner 2
- 例1 値：42 | 46 | 33 | 32 | 51
  - 同じ表の列：Scheidungsdatum, Jahr, Monat, Kalenderwoche, Datum Wochenstart, Tag in Jahr, Wochentag, Alter Partner 1

## g0091（1 列）
- 見出し：Staatsangehörigkeit Partner 1
- 例1 値：Ausl | Ausl | CH | CH | CH
  - 同じ表の列：Scheidungsdatum, Jahr, Monat, Kalenderwoche, Datum Wochenstart, Tag in Jahr, Wochentag, Alter Partner 1

## g0092（2 列）
- 見出し：traktandum_uid
- 例1 値：c5e182780e594018aac8afb21e9e9815 | b4bb383a86c044459129ed4d6b9dfd7a | 77af176683644ba3ba72ba0ad41e0689 | 277003b2a1454a3dace02f7e39f8284d | 10a85e2f18c84862bfeff0b9726384b7
  - 同じ表の列：element_nummer, votum_mitglied, votum_startzeit, Übersicht vom
- 例2 値：c863e8c364d2410983c454fe13b28d0c | 23640f8747b74b1183eae7af02ec7465 | cdf3d6b73c6042388ad51b3794747418 | df5507c77d4f41cfa61390412cdb8628 | 596a38e093394229a12e4979dfe3aa31
  - 同じ表の列：tagblatt_element_nu…, tagblatt_element_typ, tagblatt_element_ti…, tagblatt_element_st…, tagblatt_element_da…, tagblatt_element_be…, Übersicht vom

## g0093（1 列）
- 見出し：element_nummer
- 例1 値：33 | 2 | 23 | 4 | 11
  - 同じ表の列：traktandum_uid, votum_mitglied, votum_startzeit, Übersicht vom

## g0094（1 列）
- 見出し：votum_mitglied
- 例1 値：Edith Siegenthaler | Edith Siegenthaler | Jan Remund | Edith Siegenthaler | Edith Siegenthaler
  - 同じ表の列：traktandum_uid, element_nummer, votum_startzeit, Übersicht vom

## g0095（1 列）
- 見出し：votum_startzeit
- 例1 値：2026-03-03 14:43:05 | 2026-03-02 15:22:11.284 | 2026-03-04 14:10:57.686 | 2026-03-03 13:16:41.224 | 2026-03-03 10:43:20.233
  - 同じ表の列：traktandum_uid, element_nummer, votum_mitglied, Übersicht vom

## g0096（2 列）
- 見出し：Übersicht vom
- 例1 値：2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00
  - 同じ表の列：traktandum_uid, element_nummer, votum_mitglied, votum_startzeit
- 例2 値：2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00
  - 同じ表の列：traktandum_uid, tagblatt_element_nu…, tagblatt_element_typ, tagblatt_element_ti…, tagblatt_element_st…, tagblatt_element_da…, tagblatt_element_be…

## g0097（1 列）
- 見出し：tagblatt_element_nummer
- 例1 値：15 | 2 | 3 | 5 | 1
  - 同じ表の列：traktandum_uid, tagblatt_element_typ, tagblatt_element_ti…, tagblatt_element_st…, tagblatt_element_da…, tagblatt_element_be…, Übersicht vom

## g0098（1 列）
- 見出し：tagblatt_element_typ
- 例1 値：speaker | speaker | speaker | speaker | speaker
  - 同じ表の列：traktandum_uid, tagblatt_element_nu…, tagblatt_element_ti…, tagblatt_element_st…, tagblatt_element_da…, tagblatt_element_be…, Übersicht vom

## g0099（1 列）
- 見出し：tagblatt_element_titel
- 例1 値：Maya Weber Hadorn | Simone Leuenberger | Abstimmung / Vote | Mathias Müller | Edith Siegenthaler
  - 同じ表の列：traktandum_uid, tagblatt_element_nu…, tagblatt_element_typ, tagblatt_element_st…, tagblatt_element_da…, tagblatt_element_be…, Übersicht vom

## g0100（1 列）
- 見出し：tagblatt_element_startzeit
- 例1 値：2026-03-03 17:50:07.66 | 2026-03-02 14:05:08.244 | 2026-03-04 16:27:48.361 | 2026-03-04 17:01:49.62 | 2026-06-03 15:44:39.154
  - 同じ表の列：traktandum_uid, tagblatt_element_nu…, tagblatt_element_typ, tagblatt_element_ti…, tagblatt_element_da…, tagblatt_element_be…, Übersicht vom

## g0101（1 列）
- 見出し：tagblatt_element_dauer
- 例1 値：100.695 | 14.891 | 80.287 | 9.731 | 245.402
  - 同じ表の列：traktandum_uid, tagblatt_element_nu…, tagblatt_element_typ, tagblatt_element_ti…, tagblatt_element_st…, tagblatt_element_be…, Übersicht vom

## g0102（1 列）
- 見出し：tagblatt_element_bearbeitungsstatus
- 例1 値：None | None | None | None | None
  - 同じ表の列：traktandum_uid, tagblatt_element_nu…, tagblatt_element_typ, tagblatt_element_ti…, tagblatt_element_st…, tagblatt_element_da…, Übersicht vom

## g0103（4 列）
- 見出し：date
- 例1 値：2024-12-31 | 2024-12-31 | 2024-12-31 | 2024-12-31 | 2024-12-31
  - 同じ表の列：bfsnr, commune, nationality_categor…, sex, age, anzahl_personen
- 例2 値：2013-11-24 | 2013-11-24 | 2013-11-24 | 2013-11-24 | 2013-11-24
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status

## g0104（1 列）
- 見出し：commune
- 例1 値：Neckertal | St. Margrethen | Uzwil | Grabs | Grabs
  - 同じ表の列：date, bfsnr, nationality_categor…, sex, age, anzahl_personen

## g0105（1 列）
- 見出し：nationality_categorie
- 例1 値：Schweiz | Schweiz | Schweiz | Schweiz | Ausland
  - 同じ表の列：date, bfsnr, commune, sex, age, anzahl_personen

## g0106（1 列）
- 見出し：age
- 例1 値：57 | 70 | 41 | 6 | 68
  - 同じ表の列：date, bfsnr, commune, nationality_categor…, sex, anzahl_personen

## g0107（1 列）
- 見出し：anzahl_personen
- 例1 値：3 | 6 | 15 | 4 | 3
  - 同じ表の列：date, bfsnr, commune, nationality_categor…, sex, age

## g0108（1 列）
- 見出し：scen
- 例1 値：Szenario Hoch | Szenario Hoch | Szenario Hoch | Szenario Hoch | Szenario Hoch
  - 同じ表の列：gdenr, jahr, altersklasse, anzahl

## g0109（1 列）
- 見出し：gdenr
- 例1 値：3217 | 3216 | 3216 | 3215 | 3218
  - 同じ表の列：scen, jahr, altersklasse, anzahl

## g0110（1 列）
- 見出し：altersklasse
- 例1 値：50-54 | 65-69 | 65-69 | 80-84 | 80-84
  - 同じ表の列：scen, gdenr, jahr, anzahl

## g0111（1 列）
- 見出し：ZST
- 例1 値：600 | 604 | 82 | 602 | 245
  - 同じ表の列：Strassennummer, Zählstellen-Bezeich…, Kanton, Richtung 1, Richtung 2, TAG, JJMMTT, Tag_Nr

## g0112（1 列）
- 見出し：Strassennummer
- 例1 値：A 13 | A 3 | A 1 | A 3 | A 1
  - 同じ表の列：ZST, Zählstellen-Bezeich…, Kanton, Richtung 1, Richtung 2, TAG, JJMMTT, Tag_Nr

## g0113（1 列）
- 見出し：Zählstellen-Bezeichnung
- 例1 値：ST. GALLEN E, BERGBACHVIADUKT (AB) | GOSSAU (AB) | GOSSAU, OBERBERG (AB) | MEGGENHUS, VERZWEIGUNG (AB) | ARBON, A1/ZUBRINGER SG
  - 同じ表の列：ZST, Strassennummer, Kanton, Richtung 1, Richtung 2, TAG, JJMMTT, Tag_Nr

## g0114（1 列）
- 見出し：Richtung 1
- 例1 値：ST.GALLEN | SARGANS | SARGANS | A1 ST.MARGRETHEN / WINTERTHUR | SARGANS
  - 同じ表の列：ZST, Strassennummer, Zählstellen-Bezeich…, Kanton, Richtung 2, TAG, JJMMTT, Tag_Nr

## g0115（1 列）
- 見出し：Richtung 2
- 例1 値：ST. GALLEN WEST | WINTERTHUR | ZUERICH | WINTERTHUR | GOSSAU
  - 同じ表の列：ZST, Strassennummer, Zählstellen-Bezeich…, Kanton, Richtung 1, TAG, JJMMTT, Tag_Nr

## g0116（1 列）
- 見出し：TAG
- 例1 値：366 | 31 | 164 | 95 | 233
  - 同じ表の列：ZST, Strassennummer, Zählstellen-Bezeich…, Kanton, Richtung 1, Richtung 2, JJMMTT, Tag_Nr

## g0117（1 列）
- 見出し：JJMMTT
- 例1 値：2019-09-08 | 2020-01-05 | 2020-12-09 | 2020-12-22 | 2020-01-31
  - 同じ表の列：ZST, Strassennummer, Zählstellen-Bezeich…, Kanton, Richtung 1, Richtung 2, TAG, Tag_Nr

## g0118（1 列）
- 見出し：Tag_Nr
- 例1 値：6 | 2 | 4 | 2 | 1
  - 同じ表の列：ZST, Strassennummer, Zählstellen-Bezeich…, Kanton, Richtung 1, Richtung 2, TAG, JJMMTT

## g0119（1 列）
- 見出し：substanz
- 例1 値：CO2 | CO2 | N2O | N2O | F-Gase
  - 同じ表の列：jahr, hauptgruppe, untergruppe, sektor, kanton, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer

## g0120（1 列）
- 見出し：hauptgruppe
- 例1 値：Land- und Forstw. | Land- und Forstw. | Land- und Forstw. | Land- und Forstw. | Land- und Forstw.
  - 同じ表の列：jahr, substanz, untergruppe, sektor, kanton, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
g0053	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
