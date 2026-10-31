<!-- b074：24/244 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b074.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0007（3 列）
- 見出し：agegroup_type
- 例1 値：agegroup_food | agegroup_food | agegroup_food | agegroup_food | agegroup_food
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, value
- 例2 値：agegroup_food | agegroup_food | agegroup_food | agegroup_food | agegroup_food
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, type

## g0037（1 列）
- 見出し：ID
- 例1 値：ep11 | ep8 | ep27 | ep19 | ep24
  - 同じ表の列：DE, FR, IT, EN

## g0077（1 列）
- 見出し：ESID
- 例1 値：10179490 | 10026581 | 10179490 | 10120297 | 10087620
  - 同じ表の列：EGID, EDID, EGAID, Eingangsnummer Gebä…, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…, Strassenbezeichnung…

## g0082（1 列）
- 見出し：Strassenbezeichnung Sprache Bezeichnung
- 例1 値：Deutsch | Deutsch | Deutsch | Deutsch | Deutsch
  - 同じ表の列：EGID, EDID, EGAID, Eingangsnummer Gebä…, ESID, Strassenbezeichnung, Strassenbezeichnung…, Strassenbezeichnung…

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

## g0108（1 列）
- 見出し：scen
- 例1 値：Szenario Hoch | Szenario Hoch | Szenario Hoch | Szenario Hoch | Szenario Hoch
  - 同じ表の列：gdenr, jahr, altersklasse, anzahl

## g0111（1 列）
- 見出し：ZST
- 例1 値：600 | 604 | 82 | 602 | 245
  - 同じ表の列：Strassennummer, Zählstellen-Bezeich…, Kanton, Richtung 1, Richtung 2, TAG, JJMMTT, Tag_Nr

## g0121（1 列）
- 見出し：untergruppe
- 例1 値：Landwirtschaftliche Maschinen | Landwirtschaftliche Maschinen | Landwirtschaftliche Maschinen | Landwirtschaftliche Maschinen | Landwirtschaftliche Maschinen
  - 同じ表の列：jahr, substanz, hauptgruppe, sektor, kanton, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer

## g0124（1 列）
- 見出し：gemeinde
- 例1 値：Neunforn | Bottighofen | Kradolf-Schönenberg | Gottlieben | Gachnang
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, sektor, kanton, bfs_nr_gemeinde, bfs_bezirksnummer

## g0134（1 列）
- 見出し：heizsystem_code
- 例1 値：7410 | 7430 | 7430 | 7410 | 7410
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, eigentuemer_code

## g0150（1 列）
- 見出し：operatingPoint
- 例1 値：true | true | true | true | true
  - 同じ表の列：numberShort, uicCountryCode, sloid, number, checkDigit, validFrom, validTo, designationOfficial

## g0158（1 列）
- 見出し：alternativeTransportCondition
- 例1 値：Alternativ kann der Bus ab Bushaltestel… | Hier reisen Sie mit alternativem ÖV Ric… | Shuttle erforderlich
  - 同じ表の列：sloid, number, meansOfTransport, zipCode, city, alternativeTransport, shuttleService, assistanceAvailabil…

## g0162（1 列）
- 見出し：parentNumberServicePoint
- 例1 値：8503138 | 8508295 | 8502025 | 8508262 | 8507373
  - 同じ表の列：sloid, parentSloidServiceP…, designation, additionalInformati…, wheelchairToilet, validFrom, validTo, creationDate

## g0170（1 列）
- 見出し：titel
- 例1 値：Einbürgerungsgesuch für Einzelpersonen,… | Antrag zur Erteilung einer Handwerkerbe… | Kopierauftrag | Antrag auf Befreiung von der Krankenver… | Anmeldeformular Aushub / Typ A
  - 同じ表の列：formular_id, formular, service_id, aufrufe_gesamt, sitzungen_positiv, sitzungen_negativ, erfolgsquote, timeout

## g0172（1 列）
- 見出し：aufrufe_gesamt
- 例1 値：11 | 3759 | 1076 | 1 | 37
  - 同じ表の列：formular_id, formular, titel, service_id, sitzungen_positiv, sitzungen_negativ, erfolgsquote, timeout

## g0180（1 列）
- 見出し：verantw_direktion
- 例1 値：DSSI | DPB | DTB | DSSI | DTB
  - 同じ表の列：jahr, strat_handlungsfeld, zug_legislaturziel, verantw_dienststelle, art, bewertung_per_jahre…

## g0186（1 列）
- 見出し：device_id
- 例1 値：8724dc06-ecbc-4bd3-bab4-1b581dcfafad | c290b9a6-cfb6-4ad4-b5f0-d08f87dec120 | c290b9a6-cfb6-4ad4-b5f0-d08f87dec120 | 66618728-f62b-4924-92bf-0aac4faddb93 | 66618728-f62b-4924-92bf-0aac4faddb93
  - 同じ表の列：measured_at, data, Gebaude, Stockwerk, Raum, data_co2, data_humidity, data_temperature

## g0196（1 列）
- 見出し：stadtkreis
- 例1 値：Wülflingen | Oberwinterthur | Seen | Seen | Seen
  - 同じ表の列：jahr, quartier_bfs_nr, quartier, stadtkreis_bfs_nr, whg_zim_group, wohnungen

## g0209（1 列）
- 見出し：geb_efhmfh_nr
- 例1 値：0 | 0 | 1 | 0 | 0
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, geb_efhmfh, grouping

## g0211（1 列）
- 見出し：grouping
- 例1 値：zimmer | flaeche | flaeche | flaeche | zimmer
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, geb_efhmfh_nr, geb_efhmfh

## g0218（3 列）
- 見出し：shortcode
- 例1 値：E3 | E3 | E3 | E3 | E3
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status
- 例2 値：K1 | K1 | K1 | K1 | K1
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status

## g0228（1 列）
- 見出し：title_fr_CH
- 例1 値：Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0234（1 列）
- 見出し：VORLAGE_LANGBEZ
- 例1 値：Mitgliederzahl des Regierungsrates und … | Mandatsverteilung zwischen Stadt und La… | Eidg. Volkszählung als Grundlage für di… | Mitgliederzahl des Regierungsrates und … | Vermehrung der Grossratswahlkreise
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, BFS, STAT_GEMEINDE_ID, GEMEINDE, BEZIRK, AZ_STIMMBERECHTIGTE

## 答えの雛形

```
g0007	
g0037	
g0077	
g0082	
g0087	
g0088	
g0108	
g0111	
g0121	
g0124	
g0134	
g0150	
g0158	
g0162	
g0170	
g0172	
g0180	
g0186	
g0196	
g0209	
g0211	
g0218	
g0228	
g0234	
```
