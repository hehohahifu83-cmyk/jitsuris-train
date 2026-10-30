# ラベル用シート 002 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：untergruppe
- 例1 値：Landwirtschaftliche Maschinen | Landwirtschaftliche Maschinen | Landwirtschaftliche Maschinen | Landwirtschaftliche Maschinen | Landwirtschaftliche Maschinen
  - 同じ表の列：jahr, substanz, hauptgruppe, sektor, kanton, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer

## g0122（1 列）
- 見出し：sektor
- 例1 値：Landwirtschaft | Landwirtschaft | Landwirtschaft | Landwirtschaft | Landwirtschaft
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, kanton, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer

## g0123（2 列）
- 見出し：bfs_nr_gemeinde
- 例1 値：4616 | 4566 | 4864 | 4696 | 4506
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, sektor, kanton, gemeinde, bfs_bezirksnummer
- 例2 値：4451 | 4411 | 4401 | 4436 | 4401
  - 同じ表の列：jahr, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, eigentuemer_code, eigentuemer

## g0124（1 列）
- 見出し：gemeinde
- 例1 値：Neunforn | Bottighofen | Kradolf-Schönenberg | Gottlieben | Gachnang
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, sektor, kanton, bfs_nr_gemeinde, bfs_bezirksnummer

## g0125（1 列）
- 見出し：bfs_bezirksnummer
- 例1 値：2012 | 2011 | 2012 | 2011 | 2011
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, sektor, kanton, bfs_nr_gemeinde, gemeinde

## g0126（1 列）
- 見出し：bezirk
- 例1 値：Frauenfeld | Münchwilen | Weinfelden | Kreuzlingen | Frauenfeld
  - 同じ表の列：jahr, substanz, hauptgruppe, untergruppe, sektor, kanton, bfs_nr_gemeinde, gemeinde

## g0127（1 列）
- 見出し：gebaeudekategorie_code
- 例1 値：1025 | 1025 | 1025 | 1021 | 1040
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, eigentuemer_code, eigentuemer

## g0128（1 列）
- 見出し：gebaeudekategorie
- 例1 値：Einfamilienhäuser | Einfamilienhäuser | Einfamilienhäuser | Einfamilienhäuser | Wohngebäude mit Nebennutzung
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, bauperiode_code, bauperiode, geschosse_anzahl, eigentuemer_code, eigentuemer

## g0129（1 列）
- 見出し：bauperiode_code
- 例1 値：8019 | 8015 | 8021 | 8022 | 8016
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode, geschosse_anzahl, eigentuemer_code, eigentuemer

## g0130（1 列）
- 見出し：bauperiode
- 例1 値：Periode von 1961 bis 1970 | Periode von 1919 bis 1945 | Periode von 2001 bis 2005 | Periode von 2016 bis 2020 | Periode von 1919 bis 1945
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, geschosse_anzahl, eigentuemer_code, eigentuemer

## g0131（1 列）
- 見出し：geschosse_anzahl
- 例1 値：2 | 2 | 1 | 2 | 1
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, eigentuemer_code, eigentuemer

## g0132（1 列）
- 見出し：eigentuemer_code
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, eigentuemer

## g0133（1 列）
- 見出し：eigentuemer
- 例1 値：Juristische Person | Natürliche Person(en) | Natürliche Person(en) | Juristische Person | Juristische Person
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, eigentuemer_code

## g0134（1 列）
- 見出し：heizsystem_code
- 例1 値：7410 | 7430 | 7430 | 7410 | 7410
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, eigentuemer_code

## g0135（1 列）
- 見出し：rede_id
- 例1 値：001300008 | 001140081 | 000550025 | 002760006 | 000160061
  - 同じ表の列：datum, geschaeftsnummer, traktandum, sprecher, sprecher_typ, fraktion

## g0136（1 列）
- 見出し：datum
- 例1 値：2009-02-11 | 2010-01-13 | 2011-03-30 | 2014-03-26 | 2013-06-12
  - 同じ表の列：rede_id, geschaeftsnummer, traktandum, sprecher, sprecher_typ, fraktion

## g0137（1 列）
- 見出し：geschaeftsnummer
- 例1 値：12/BS 29/283 | 12/MO 17/113 | 08/EB 7/178 | 08/MO 55/413 | 08/IN 40/229
  - 同じ表の列：rede_id, datum, traktandum, sprecher, sprecher_typ, fraktion

## g0138（1 列）
- 見出し：traktandum
- 例1 値：5. Geschäftsbericht 2015, umfassend den… | 5. Interpellation von Erwin Imhof und S… | 5.3 Departement für Inneres und Volkswi… | 2.2 Teil II: A. Gesetz über die Zivil- … | 2. Motion von Paul Koch vom 12. Februar…
  - 同じ表の列：rede_id, datum, geschaeftsnummer, sprecher, sprecher_typ, fraktion

## g0139（1 列）
- 見出し：sprecher
- 例1 値：Kappeler | Tobler | Wiesli | Stuber | Senn
  - 同じ表の列：rede_id, datum, geschaeftsnummer, traktandum, sprecher_typ, fraktion

## g0140（1 列）
- 見出し：sprecher_typ
- 例1 値：Präsident | Mitglied GR | Mitglied GR | Mitglied GR | Mitglied GR
  - 同じ表の列：rede_id, datum, geschaeftsnummer, traktandum, sprecher, fraktion

## g0141（1 列）
- 見出し：fraktion
- 例1 値：EVP/EDU | CVP/GLP | SVP | SVP | SVP
  - 同じ表の列：rede_id, datum, geschaeftsnummer, traktandum, sprecher, sprecher_typ

## g0142（1 列）
- 見出し：numberShort
- 例1 値：22049 | 22044 | 22015 | 22018 | 22041
  - 同じ表の列：uicCountryCode, sloid, number, checkDigit, validFrom, validTo, designationOfficial, operatingPoint

## g0143（1 列）
- 見出し：uicCountryCode
- 例1 値：13 | 13 | 13 | 13 | 13
  - 同じ表の列：numberShort, sloid, number, checkDigit, validFrom, validTo, designationOfficial, operatingPoint

## g0144（2 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:1322057 | ch:1:sloid:1322045 | ch:1:sloid:1322076 | ch:1:sloid:1322070 | ch:1:sloid:1322052
  - 同じ表の列：numberShort, uicCountryCode, number, checkDigit, validFrom, validTo, designationOfficial, operatingPoint
- 例2 値：ch:1:sloid:85332 | ch:1:sloid:78674 | ch:1:sloid:72117 | ch:1:sloid:6621 | ch:1:sloid:6581
  - 同じ表の列：number, meansOfTransport, zipCode, city, alternativeTransport, shuttleService, assistanceAvailabil…, alternativeTranspor…

## g0145（2 列）
- 見出し：number
- 例1 値：1322007 | 1322030 | 1322084 | 1322106 | 1322097
  - 同じ表の列：numberShort, uicCountryCode, sloid, checkDigit, validFrom, validTo, designationOfficial, operatingPoint
- 例2 値：8506719 | 8506742 | 8579014 | 8591910 | 8579019
  - 同じ表の列：sloid, meansOfTransport, zipCode, city, alternativeTransport, shuttleService, assistanceAvailabil…, alternativeTranspor…

## g0146（1 列）
- 見出し：checkDigit
- 例1 値：4 | 9 | 2 | 3 | 8
  - 同じ表の列：numberShort, uicCountryCode, sloid, number, validFrom, validTo, designationOfficial, operatingPoint

## g0147（2 列）
- 見出し：validFrom
- 例1 値：2020-09-01T00:00:00 | 2020-09-01T00:00:00 | 2020-09-01T00:00:00 | 2020-09-01T00:00:00 | 2020-09-01T00:00:00
  - 同じ表の列：numberShort, uicCountryCode, sloid, number, checkDigit, validTo, designationOfficial, operatingPoint
- 例2 値：2021-11-03T00:00:00 | 2023-08-04T00:00:00 | 2021-01-21T00:00:00 | 2021-03-10T00:00:00 | 2023-08-23T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, wheelchairToilet, validTo, creationDate

## g0148（2 列）
- 見出し：validTo
- 例1 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：numberShort, uicCountryCode, sloid, number, checkDigit, validFrom, designationOfficial, operatingPoint
- 例2 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, wheelchairToilet, validFrom, creationDate

## g0149（1 列）
- 見出し：designationOfficial
- 例1 値：Gòglio | Vanzone | Castiglione | Migiandone Bivio | Intra, rimessa
  - 同じ表の列：numberShort, uicCountryCode, sloid, number, checkDigit, validFrom, validTo, operatingPoint

## g0150（1 列）
- 見出し：operatingPoint
- 例1 値：true | true | true | true | true
  - 同じ表の列：numberShort, uicCountryCode, sloid, number, checkDigit, validFrom, validTo, designationOfficial

## g0151（1 列）
- 見出し：operatingPointWithTimetable
- 例1 値：true | true | true | true | true
  - 同じ表の列：numberShort, uicCountryCode, sloid, number, checkDigit, validFrom, validTo, designationOfficial

## g0152（1 列）
- 見出し：meansOfTransport
- 例1 値：BUS | BUS | BUS | BUS | TRAIN
  - 同じ表の列：sloid, number, zipCode, city, alternativeTransport, shuttleService, assistanceAvailabil…, alternativeTranspor…

## g0153（1 列）
- 見出し：zipCode
- 例1 値：4444 | 2345 | 2345 | 2735 | 4625
  - 同じ表の列：sloid, number, meansOfTransport, city, alternativeTransport, shuttleService, assistanceAvailabil…, alternativeTranspor…

## g0154（1 列）
- 見出し：city
- 例1 値：Glovelier | Courchavon | Solothurn | Les Reussilles | Court
  - 同じ表の列：sloid, number, meansOfTransport, zipCode, alternativeTransport, shuttleService, assistanceAvailabil…, alternativeTranspor…

## g0155（1 列）
- 見出し：alternativeTransport
- 例1 値：NO | NO | NO | NO | NO
  - 同じ表の列：sloid, number, meansOfTransport, zipCode, city, shuttleService, assistanceAvailabil…, alternativeTranspor…

## g0156（1 列）
- 見出し：shuttleService
- 例1 値：NO | NO | NO | NO | NO
  - 同じ表の列：sloid, number, meansOfTransport, zipCode, city, alternativeTransport, assistanceAvailabil…, alternativeTranspor…

## g0157（1 列）
- 見出し：assistanceAvailability
- 例1 値：YES | NOT_APPLICABLE | YES | NOT_APPLICABLE | NOT_APPLICABLE
  - 同じ表の列：sloid, number, meansOfTransport, zipCode, city, alternativeTransport, shuttleService, alternativeTranspor…

## g0158（1 列）
- 見出し：alternativeTransportCondition
- 例1 値：Alternativ kann der Bus ab Bushaltestel… | Hier reisen Sie mit alternativem ÖV Ric… | Shuttle erforderlich
  - 同じ表の列：sloid, number, meansOfTransport, zipCode, city, alternativeTransport, shuttleService, assistanceAvailabil…

## g0159（1 列）
- 見出し：assistanceService
- 例1 値：NOT_APPLICABLE | YES | NOT_APPLICABLE | YES | NO
  - 同じ表の列：sloid, number, meansOfTransport, zipCode, city, alternativeTransport, shuttleService, assistanceAvailabil…

## g0160（1 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:8055:282336 | ch:1:sloid:4400:990046 | ch:1:sloid:2292:671789 | ch:1:sloid:8309:537084 | ch:1:sloid:6292:307394
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, wheelchairToilet, validFrom, validTo, creationDate

## g0161（1 列）
- 見出し：parentSloidServicePoint
- 例1 値：ch:1:sloid:71566 | ch:1:sloid:262 | ch:1:sloid:2220 | ch:1:sloid:1200 | ch:1:sloid:1003
  - 同じ表の列：sloid, parentNumberService…, designation, additionalInformati…, wheelchairToilet, validFrom, validTo, creationDate

## g0162（1 列）
- 見出し：parentNumberServicePoint
- 例1 値：8503138 | 8508295 | 8502025 | 8508262 | 8507373
  - 同じ表の列：sloid, parentSloidServiceP…, designation, additionalInformati…, wheelchairToilet, validFrom, validTo, creationDate

## g0163（1 列）
- 見出し：designation
- 例1 値：Bissone (lago) | Toilette | Toilette | Toilette | Öffentliche Toiletten
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, additionalInformati…, wheelchairToilet, validFrom, validTo, creationDate

## g0164（1 列）
- 見出し：additionalInformation
- 例1 値：Rollstuhlgängige Toilette in Talstation | Unterhalt durch Gemeinde | Das öffentliche WC befindet sich im War… | WC Publics - Parc de la Gare | Toilette communale
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, wheelchairToilet, validFrom, validTo, creationDate

## g0165（1 列）
- 見出し：wheelchairToilet
- 例1 値：YES | NO | YES | NO | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, validFrom, validTo, creationDate

## g0166（1 列）
- 見出し：creationDate
- 例1 値：2021-11-03T11:13:50 | 2021-12-01T10:19:07 | 2022-01-27T12:38:21 | 2022-02-14T12:07:29 | 2021-11-03T12:30:06
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, wheelchairToilet, validFrom, validTo

## g0167（1 列）
- 見出し：editionDate
- 例1 値：2024-04-08T10:45:07 | 2024-04-08T10:45:07 | 2024-04-08T10:45:07 | 2024-04-08T10:45:07 | 2024-04-08T10:45:07
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, wheelchairToilet, validFrom, validTo

## g0168（1 列）
- 見出し：formular_id
- 例1 値：BA_2 | FA_2 | EA_8_D | ESG_01_1 | BA_3
  - 同じ表の列：formular, titel, service_id, aufrufe_gesamt, sitzungen_positiv, sitzungen_negativ, erfolgsquote, timeout

## g0169（1 列）
- 見出し：formular
- 例1 値：ZA_1_2_Ehe_1 | STAPO_04_GesuchTombola | STAPO_09_MeldeformularEinsatzLaseranlag… | IDS_1_Test_1 | STAPO_11_Jahrmaerkte
  - 同じ表の列：formular_id, titel, service_id, aufrufe_gesamt, sitzungen_positiv, sitzungen_negativ, erfolgsquote, timeout

## g0170（1 列）
- 見出し：titel
- 例1 値：Einbürgerungsgesuch für Einzelpersonen,… | Antrag zur Erteilung einer Handwerkerbe… | Kopierauftrag | Antrag auf Befreiung von der Krankenver… | Anmeldeformular Aushub / Typ A
  - 同じ表の列：formular_id, formular, service_id, aufrufe_gesamt, sitzungen_positiv, sitzungen_negativ, erfolgsquote, timeout

## g0171（1 列）
- 見出し：service_id
- 例1 値：80238817-19c6-4dc6-a7b5-ec3a7bdefe65 | 97415254-3c0f-4bf9-9fee-fc9aa85249ac | ea1f9234-9cee-4eed-bf7f-10a3b0be9039
  - 同じ表の列：formular_id, formular, titel, aufrufe_gesamt, sitzungen_positiv, sitzungen_negativ, erfolgsquote, timeout

## g0172（1 列）
- 見出し：aufrufe_gesamt
- 例1 値：11 | 3759 | 1076 | 1 | 37
  - 同じ表の列：formular_id, formular, titel, service_id, sitzungen_positiv, sitzungen_negativ, erfolgsquote, timeout

## g0173（1 列）
- 見出し：sitzungen_positiv
- 例1 値：14 | 13 | 258 | 8 | 384
  - 同じ表の列：formular_id, formular, titel, service_id, aufrufe_gesamt, sitzungen_negativ, erfolgsquote, timeout

## g0174（1 列）
- 見出し：sitzungen_negativ
- 例1 値：154 | 1115 | 164 | 16 | 564
  - 同じ表の列：formular_id, formular, titel, service_id, aufrufe_gesamt, sitzungen_positiv, erfolgsquote, timeout

## g0175（1 列）
- 見出し：erfolgsquote
- 例1 値：0.7027027027027027 | 0.2692307692307692 | 0.4583333333333333 | 0.3854748603351955 | 0.3639896373056995
  - 同じ表の列：formular_id, formular, titel, service_id, aufrufe_gesamt, sitzungen_positiv, sitzungen_negativ, timeout

## g0176（1 列）
- 見出し：timeout
- 例1 値：1167 | 153 | 191 | 161 | 1
  - 同じ表の列：formular_id, formular, titel, service_id, aufrufe_gesamt, sitzungen_positiv, sitzungen_negativ, erfolgsquote

## g0177（1 列）
- 見出し：pdf
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：formular_id, formular, titel, service_id, aufrufe_gesamt, sitzungen_positiv, sitzungen_negativ, erfolgsquote

## g0178（1 列）
- 見出し：strat_handlungsfeld
- 例1 値：2 Smarte Stadt | NA | NA | 3 Gesellschaft | 1 Kooperation
  - 同じ表の列：jahr, zug_legislaturziel, verantw_direktion, verantw_dienststelle, art, bewertung_per_jahre…

## g0179（1 列）
- 見出し：zug_legislaturziel
- 例1 値：8.11 Anzahl zurückgelegter Wege | NA | 9.21 Erneuerbare Energien 2024 | 2.32 eGovernment Strategie | 3.301 Vision 2030: Lebensqualität
  - 同じ表の列：jahr, strat_handlungsfeld, verantw_direktion, verantw_dienststelle, art, bewertung_per_jahre…

## g0180（1 列）
- 見出し：verantw_direktion
- 例1 値：DSSI | DPB | DTB | DSSI | DTB
  - 同じ表の列：jahr, strat_handlungsfeld, zug_legislaturziel, verantw_dienststelle, art, bewertung_per_jahre…

## g0181（1 列）
- 見出し：verantw_dienststelle
- 例1 値：TBA | SF | BA | KESB | LIE
  - 同じ表の列：jahr, strat_handlungsfeld, zug_legislaturziel, verantw_direktion, art, bewertung_per_jahre…

## g0182（1 列）
- 見出し：art
- 例1 値：strategisch | operativ | strategisch | operativ | strategisch
  - 同じ表の列：jahr, strat_handlungsfeld, zug_legislaturziel, verantw_direktion, verantw_dienststelle, bewertung_per_jahre…

## g0183（1 列）
- 見出し：bewertung_per_jahresende
- 例1 値：+ erreicht | + erreicht | + erreicht | + erreicht | + erreicht
  - 同じ表の列：jahr, strat_handlungsfeld, zug_legislaturziel, verantw_direktion, verantw_dienststelle, art

## g0184（1 列）
- 見出し：measured_at
- 例1 値：2026-01-30T12:00:00 | 2026-06-10T09:00:02 | 2025-12-07T23:00:00 | 2026-01-30T18:00:00 | 2026-01-30T21:00:00
  - 同じ表の列：data, device_id, Gebaude, Stockwerk, Raum, data_co2, data_humidity, data_temperature

## g0185（1 列）
- 見出し：data
- 例1 値：{"co2": 685.3333333333334, "temperature… | {"co2": 574.625, "temperature": 22.0625… | {"co2": 831.2, "temperature": 24.030000… | {"co2": 215.86666666666667, "temperatur… | {"co2": 555.2142857142857, "temperature…
  - 同じ表の列：measured_at, device_id, Gebaude, Stockwerk, Raum, data_co2, data_humidity, data_temperature

## g0186（1 列）
- 見出し：device_id
- 例1 値：8724dc06-ecbc-4bd3-bab4-1b581dcfafad | c290b9a6-cfb6-4ad4-b5f0-d08f87dec120 | c290b9a6-cfb6-4ad4-b5f0-d08f87dec120 | 66618728-f62b-4924-92bf-0aac4faddb93 | 66618728-f62b-4924-92bf-0aac4faddb93
  - 同じ表の列：measured_at, data, Gebaude, Stockwerk, Raum, data_co2, data_humidity, data_temperature

## g0187（1 列）
- 見出し：Gebaude
- 例1 値：Neugasse 25 | VM | Neugasse 25 | VM | VM
  - 同じ表の列：measured_at, data, device_id, Stockwerk, Raum, data_co2, data_humidity, data_temperature

## g0188（1 列）
- 見出し：Stockwerk
- 例1 値：2.OG | 2.OG | 2.OG | 2.OG | 2.OG
  - 同じ表の列：measured_at, data, device_id, Gebaude, Raum, data_co2, data_humidity, data_temperature

## g0189（1 列）
- 見出し：Raum
- 例1 値：Büro DIT-OTS-Netzwerk | Büro DIT-OTS-Netzwerk | Büro DIT-OTS-Netzwerk | Büro DIT-OTS-Netzwerk | Büro DIT-OTS-Netzwerk
  - 同じ表の列：measured_at, data, device_id, Gebaude, Stockwerk, data_co2, data_humidity, data_temperature

## g0190（1 列）
- 見出し：data_co2
- 例1 値：829 | 875 | 305 | 323 | 804
  - 同じ表の列：measured_at, data, device_id, Gebaude, Stockwerk, Raum, data_humidity, data_temperature

## g0191（1 列）
- 見出し：data_humidity
- 例1 値：30.100000381469727 | 31.3545448996804 | 48.460000610351564 | 47.357142857142854 | 30.100000381469727
  - 同じ表の列：measured_at, data, device_id, Gebaude, Stockwerk, Raum, data_co2, data_temperature

## g0192（1 列）
- 見出し：data_temperature
- 例1 値：27.47777769300673 | 23.8166659673055 | 18.949999809265137 | 24.5 | 24.399999618530273
  - 同じ表の列：measured_at, data, device_id, Gebaude, Stockwerk, Raum, data_co2, data_humidity

## g0193（2 列）
- 見出し：quartier_bfs_nr
- 例1 値：620 | 340 | 160 | 640 | 510
  - 同じ表の列：jahr, quartier, stadtkreis_bfs_nr, stadtkreis, whg_zim_group, wohnungen
- 例2 値：120 | 140 | 240 | 160 | 240
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier, geb_efhmfh_nr, geb_efhmfh, grouping

## g0194（2 列）
- 見出し：quartier
- 例1 値：Grüze | Zinzikon | Talacker | Endliker | Ricketwil
  - 同じ表の列：jahr, quartier_bfs_nr, stadtkreis_bfs_nr, stadtkreis, whg_zim_group, wohnungen
- 例2 値：Brühlberg | Guggenbühl | Hegmatten | Brühlberg | Hegi
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, geb_efhmfh_nr, geb_efhmfh, grouping

## g0195（3 列）
- 見出し：stadtkreis_bfs_nr
- 例1 値：2 | 2 | 2 | 6 | 3
  - 同じ表の列：jahr, quartier_bfs_nr, quartier, stadtkreis, whg_zim_group, wohnungen
- 例2 値：4 | 5 | 3 | 2 | 4
  - 同じ表の列：typ, erhebung_art, erhebung_quelle, jahr_von, jahr_bis, geom_code, stadtkreis, eigentuemer_typ_nr

## g0196（1 列）
- 見出し：stadtkreis
- 例1 値：Wülflingen | Oberwinterthur | Seen | Seen | Seen
  - 同じ表の列：jahr, quartier_bfs_nr, quartier, stadtkreis_bfs_nr, whg_zim_group, wohnungen

## g0197（1 列）
- 見出し：whg_zim_group
- 例1 値：4 | 5 | 6+ | 2 | 2
  - 同じ表の列：jahr, quartier_bfs_nr, quartier, stadtkreis_bfs_nr, stadtkreis, wohnungen

## g0198（1 列）
- 見出し：wohnungen
- 例1 値：7 | 10 | 555 | 225 | 520
  - 同じ表の列：jahr, quartier_bfs_nr, quartier, stadtkreis_bfs_nr, stadtkreis, whg_zim_group

## g0199（1 列）
- 見出し：typ
- 例1 値：Bestandsmieten | Bestandsmieten | Bestandsmieten | Bestandsmieten | Bestandsmieten
  - 同じ表の列：erhebung_art, erhebung_quelle, jahr_von, jahr_bis, geom_code, stadtkreis_bfs_nr, stadtkreis, eigentuemer_typ_nr

## g0200（1 列）
- 見出し：erhebung_art
- 例1 値：Stichprobe | Stichprobe | Stichprobe | Insersationsdaten | Stichprobe
  - 同じ表の列：typ, erhebung_quelle, jahr_von, jahr_bis, geom_code, stadtkreis_bfs_nr, stadtkreis, eigentuemer_typ_nr

## g0201（1 列）
- 見出し：erhebung_quelle
- 例1 値：Strukturerhebung (SE) | Strukturerhebung (SE) | Strukturerhebung (SE) | Strukturerhebung (SE) | Strukturerhebung (SE)
  - 同じ表の列：typ, erhebung_art, jahr_von, jahr_bis, geom_code, stadtkreis_bfs_nr, stadtkreis, eigentuemer_typ_nr

## g0202（1 列）
- 見出し：jahr_von
- 例1 値：2019 | 2019 | 2019 | 2021 | 2019
  - 同じ表の列：typ, erhebung_art, erhebung_quelle, jahr_bis, geom_code, stadtkreis_bfs_nr, stadtkreis, eigentuemer_typ_nr

## g0203（1 列）
- 見出し：jahr_bis
- 例1 値：2021 | 2023 | 2023 | 2023 | 2021
  - 同じ表の列：typ, erhebung_art, erhebung_quelle, jahr_von, geom_code, stadtkreis_bfs_nr, stadtkreis, eigentuemer_typ_nr

## g0204（2 列）
- 見出し：geom_code
- 例1 値：stadtkreis | gemeinde | stadtkreis | stadtkreis | stadtkreis
  - 同じ表の列：typ, erhebung_art, erhebung_quelle, jahr_von, jahr_bis, stadtkreis_bfs_nr, stadtkreis, eigentuemer_typ_nr
- 例2 値：gemeinde | stadtkreis | gemeinde | quartier | stadtkreis
  - 同じ表の列：jahr, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, geb_efhmfh_nr, geb_efhmfh, grouping

## g0205（1 列）
- 見出し：stadtkreis
- 例1 値：Töss | Oberwinterthur | Töss | Stadt | Töss
  - 同じ表の列：typ, erhebung_art, erhebung_quelle, jahr_von, jahr_bis, geom_code, stadtkreis_bfs_nr, eigentuemer_typ_nr

## g0206（1 列）
- 見出し：eigentuemer_typ_nr
- 例1 値：1 | 2 | 0 | 2 | 0
  - 同じ表の列：typ, erhebung_art, erhebung_quelle, jahr_von, jahr_bis, geom_code, stadtkreis_bfs_nr, stadtkreis

## g0207（1 列）
- 見出し：eigentuemer_typ
- 例1 値：Genossenschaften | übrige Mietende | Gesamt | Gesamt | Gesamt
  - 同じ表の列：typ, erhebung_art, erhebung_quelle, jahr_von, jahr_bis, geom_code, stadtkreis_bfs_nr, stadtkreis

## g0208（1 列）
- 見出し：stadtkreis
- 例1 値：Seen | Oberwinterthur | Stadt | Oberwinterthur | Stadt
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, quartier_bfs_nr, quartier, geb_efhmfh_nr, geb_efhmfh, grouping

## g0209（1 列）
- 見出し：geb_efhmfh_nr
- 例1 値：0 | 0 | 1 | 0 | 0
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, geb_efhmfh, grouping

## g0210（1 列）
- 見出し：geb_efhmfh
- 例1 値：Wohnungen in MFH | Wohnungen in MFH | Wohnungen Gesamt | Wohnungen Gesamt | Wohnungen in MFH
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, geb_efhmfh_nr, grouping

## g0211（1 列）
- 見出し：grouping
- 例1 値：zimmer | flaeche | flaeche | flaeche | zimmer
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, geb_efhmfh_nr, geb_efhmfh

## g0212（1 列）
- 見出し：group_nr
- 例1 値：5 | 1 | 4 | 99 | 3
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, geb_efhmfh_nr, geb_efhmfh

## g0213（2 列）
- 見出し：id
- 例1 値：anderung-des-bundesgesetzes-uber-die-ab… | anderung-des-bundesgesetzes-uber-die-ab… | anderung-des-bundesgesetzes-uber-die-ab… | anderung-des-bundesgesetzes-uber-die-ab… | anderung-des-bundesgesetzes-uber-die-ab…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status
- 例2 値：volksinitiative-weniger-steuern-fur-das… | volksinitiative-weniger-steuern-fur-das… | volksinitiative-weniger-steuern-fur-das… | volksinitiative-weniger-steuern-fur-das… | volksinitiative-weniger-steuern-fur-das…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0214（1 列）
- 見出し：title_de_CH
- 例1 値：Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0215（1 列）
- 見出し：title_fr_CH
- 例1 値：Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0216（1 列）
- 見出し：title_it_CH
- 例1 値：Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0217（1 列）
- 見出し：title_rm_CH
- 例1 値：Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab… | Änderung des Bundesgesetzes über die Ab…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0218（3 列）
- 見出し：shortcode
- 例1 値：E3 | E3 | E3 | E3 | E3
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status
- 例2 値：K1 | K1 | K1 | K1 | K1
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status

## g0219（3 列）
- 見出し：domain
- 例1 値：federation | federation | federation | federation | federation
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status
- 例2 値：canton | canton | canton | canton | canton
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status

## g0220（3 列）
- 見出し：status
- 例1 値：unknown | unknown | unknown | unknown | unknown
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain
- 例2 値：unknown | unknown | unknown | unknown | unknown
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain

## g0221（3 列）
- 見出し：answer
- 例1 値：rejected | rejected | rejected | rejected | rejected
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain
- 例2 値：rejected | rejected | rejected | rejected | rejected
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain

## g0222（1 列）
- 見出し：title_de_CH
- 例1 値：Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0223（1 列）
- 見出し：title_fr_CH
- 例1 値：Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0224（1 列）
- 見出し：title_it_CH
- 例1 値：Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0225（1 列）
- 見出し：title_rm_CH
- 例1 値：Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da… | Volksinitiative "Weniger Steuern für da…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0226（1 列）
- 見出し：id
- 例1 値：volksinitiative-gegen-masseneinwanderung | volksinitiative-gegen-masseneinwanderung | volksinitiative-gegen-masseneinwanderung | volksinitiative-gegen-masseneinwanderung | volksinitiative-gegen-masseneinwanderung
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0227（1 列）
- 見出し：title_de_CH
- 例1 値：Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0228（1 列）
- 見出し：title_fr_CH
- 例1 値：Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0229（1 列）
- 見出し：title_it_CH
- 例1 値：Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0230（1 列）
- 見出し：title_rm_CH
- 例1 値：Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu… | Volksinitiative "Gegen Masseneinwanderu…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0231（1 列）
- 見出し：ABSTIMMUNGSTAG
- 例1 値：16.08.1840 | 16.08.1840 | 16.08.1840 | 16.08.1840 | 16.08.1840
  - 同じ表の列：STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, BFS, STAT_GEMEINDE_ID, GEMEINDE, BEZIRK, AZ_STIMMBERECHTIGTE

## g0232（1 列）
- 見出し：STAT_VORLAGE_ID
- 例1 値：805 | 805 | 807 | 804 | 806
  - 同じ表の列：ABSTIMMUNGSTAG, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, BFS, STAT_GEMEINDE_ID, GEMEINDE, BEZIRK, AZ_STIMMBERECHTIGTE

## g0233（1 列）
- 見出し：VORLAGE_KURZBEZ
- 例1 値：Wahl der Pfarrer und Lehrer durch die G… | Einführung von Ordnungs- u. Polizeistra… | Wahl der Pfarrer und Lehrer durch die G… | Organisation von Regierungs-: Kirchen- … | Einführung von Ordnungs- u. Polizeistra…
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_LANGBEZ, BFS, STAT_GEMEINDE_ID, GEMEINDE, BEZIRK, AZ_STIMMBERECHTIGTE

## g0234（1 列）
- 見出し：VORLAGE_LANGBEZ
- 例1 値：Mitgliederzahl des Regierungsrates und … | Mandatsverteilung zwischen Stadt und La… | Eidg. Volkszählung als Grundlage für di… | Mitgliederzahl des Regierungsrates und … | Vermehrung der Grossratswahlkreise
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, BFS, STAT_GEMEINDE_ID, GEMEINDE, BEZIRK, AZ_STIMMBERECHTIGTE

## g0235（1 列）
- 見出し：BFS
- 例1 値：4 | 3 | 70 | 33 | 62
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, STAT_GEMEINDE_ID, GEMEINDE, BEZIRK, AZ_STIMMBERECHTIGTE

## g0236（1 列）
- 見出し：STAT_GEMEINDE_ID
- 例1 値：11 | 25 | 122 | 72 | 67
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, BFS, GEMEINDE, BEZIRK, AZ_STIMMBERECHTIGTE

## g0237（1 列）
- 見出し：BEZIRK
- 例1 値：Pfäffikon | Dielsdorf | Pfäffikon | Uster | Hinwil
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, BFS, STAT_GEMEINDE_ID, GEMEINDE, AZ_STIMMBERECHTIGTE

## g0238（1 列）
- 見出し：AZ_STIMMBERECHTIGTE
- 例1 値：650 | 143 | 160 | 395 | 69
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, BFS, STAT_GEMEINDE_ID, GEMEINDE, BEZIRK

## g0239（1 列）
- 見出し：AZ_EINGELEGTE_STIMMZETTEL
- 例1 値：99 | 26 | 56 | 42 | 33
  - 同じ表の列：ABSTIMMUNGSTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, BFS, STAT_GEMEINDE_ID, GEMEINDE, BEZIRK

## g0240（1 列）
- 見出し：gebietstyp_code
- 例1 値：3 | 3 | 3 | 3 | 3
  - 同じ表の列：gemeinde_code

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
g0195	
g0196	
g0197	
g0198	
g0199	
g0200	
g0201	
g0202	
g0203	
g0204	
g0205	
g0206	
g0207	
g0208	
g0209	
g0210	
g0211	
g0212	
g0213	
g0214	
g0215	
g0216	
g0217	
g0218	
g0219	
g0220	
g0221	
g0222	
g0223	
g0224	
g0225	
g0226	
g0227	
g0228	
g0229	
g0230	
g0231	
g0232	
g0233	
g0234	
g0235	
g0236	
g0237	
g0238	
g0239	
g0240	
```
