# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：Jahr
- 例1 値：1998 | 2014 | 2011 | 1997 | 2023
  - 同じ表の列：Monat, Heizgradtage
- 例2 値：2020 | 2020 | 2021 | 2020 | 2021
  - 同じ表の列：Kantonskuerzel, fr_0101, fr_0102, fr_0103, fr_0201, fr_0202, fr_0203, fr_0204

## g0002（1 列）
- 見出し：Monat
- 例1 値：1 | 10 | 1 | 8 | 11
  - 同じ表の列：Jahr, Heizgradtage

## g0003（1 列）
- 見出し：Heizgradtage
- 例1 値：208.0 | 468.9 | 387.4 | 526.3 | 515.5
  - 同じ表の列：Jahr, Monat

## g0004（1 列）
- 見出し：Kantonskuerzel
- 例1 値：AI | LU | SO | UR | TG
  - 同じ表の列：jahr, fr_0101, fr_0102, fr_0103, fr_0201, fr_0202, fr_0203, fr_0204

## g0005（1 列）
- 見出し：fr_0101
- 例1 値：Energiegesetz (EnG) vom 01.07.04 (Stand… | Energiegesetz 2000 EnG, in Kraft seit 0… | Energiegesetz 2016, EnG, Inkraftsetzung… | Energienutzungsgesetz 731.1 vom 10.03.0… | 741.1 Kantonales Energiegesetz (KEnG) v…
  - 同じ表の列：Kantonskuerzel, jahr, fr_0102, fr_0103, fr_0201, fr_0202, fr_0203, fr_0204

## g0006（1 列）
- 見出し：fr_0102
- 例1 値：Verordnung über Förderbeiträge per 01.0… | Keine | Ordonnance relative à une augmentation … | Keine | DE incentivi del 06.04.16; modifiche de…
  - 同じ表の列：Kantonskuerzel, jahr, fr_0101, fr_0103, fr_0201, fr_0202, fr_0203, fr_0204

## g0007（1 列）
- 見出し：fr_0103
- 例1 値：Umsetzung MuKEn 2014 im BauG: parlament… | Keine | Revision der Energienutzungsverordnung … | Ab 01.01.18 Vorgabe für alle EVU: Stand… | Teilrevision des Energiegesetzes am 26.…
  - 同じ表の列：Kantonskuerzel, jahr, fr_0101, fr_0102, fr_0201, fr_0202, fr_0203, fr_0204

## g0008（1 列）
- 見出し：fr_0201
- 例1 値：PDE 2020-2030 (plan directeur cantonal … | Energiestrategie 2013-2020 | Conception directrice de l'énergie 2015… | 1) Konzept zur verstärkten Förderung er… | Conception directrice de l'énergie 2015…
  - 同じ表の列：Kantonskuerzel, jahr, fr_0101, fr_0102, fr_0103, fr_0202, fr_0203, fr_0204

## g0009（1 列）
- 見出し：fr_0202
- 例1 値：Bis 2030: Reduktion Energiebedarf um 20… | §2 EnG, Abs. 1) Reduktion CO2-Ausstoss … | 2000-Watt-Gesellschaft mit klimaneutral… | Tendre vers la Société à 2000 W à l'hor… | Objectif de la politique énergétique du…
  - 同じ表の列：Kantonskuerzel, jahr, fr_0101, fr_0102, fr_0103, fr_0201, fr_0203, fr_0204

## g0010（1 列）
- 見出し：fr_0203
- 例1 値：Energiekonzept 2019-2021 mit Beschluss … | RR Beschluss vom 9. April 2019 / Nr. 228 | Verabschiedet durch Regierungsrat am 08… | Leitbild vom Regierungsrat beschlossen … | Rapport n°160 du Conseil d'Etat présent…
  - 同じ表の列：Kantonskuerzel, jahr, fr_0101, fr_0102, fr_0103, fr_0201, fr_0202, fr_0204

## g0011（1 列）
- 見出し：fr_0204
- 例1 値：Neue Energie- und Klimaplanung 2022+ in… | Aus dem Planungsbericht folgt ein Massn… | Gegenvorschlag Klimagerechtigkeitsiniti… | Vision: 2000-Watt-Gesellschaft im Jahr … | St. Galler Energiekonzept 2021-2030 von…
  - 同じ表の列：Kantonskuerzel, jahr, fr_0101, fr_0102, fr_0103, fr_0201, fr_0202, fr_0203

## g0012（1 列）
- 見出し：fr_0301
- 例1 値：Nein | Nein | Non | Oui, sans divergence dans le contenu | Oui, mais avec divergence dans le conte…
  - 同じ表の列：Kantonskuerzel, jahr, fr_0101, fr_0102, fr_0103, fr_0201, fr_0202, fr_0203

## g0013（1 列）
- 見出し：GEO_NR
- 例1 値：CH | CH | 2 | 52 | 66
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0014（2 列）
- 見出し：CLASS_HAB
- 例1 値：2 | 4 | 3 | 4 | 4
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：2 | 2 | 3 | 4 | 2
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0015（2 列）
- 見出し：GEOM_PERIOD
- 例1 値：2020-10-18 | 2022-01-01 | 2022-01-01 | 2020-10-18 | 2022-01-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：2021-07-01 | 2021-07-01 | 2021-07-01 | 2021-07-01 | 2021-07-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0016（1 列）
- 見出し：VARIABLE
- 例1 値：rev_mars_1000 | eng_prov_cou | rec_fsc | act_t | rev_mar_200
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0017（2 列）
- 見出し：SOURCE
- 例1 値：EFV | EFV | EFV | ESTV | ESTV
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：HESTA | HESTA | HESTA | HESTA | HESTA
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0018（2 列）
- 見出し：VALUE_PERIOD
- 例1 値：2022 | 2022 | 2022 | 2020 | 2020
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS
- 例2 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS

## g0019（2 列）
- 見出し：UNIT_VALUE
- 例1 値：Num | Per | Num | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, VALUE, STATUS
- 例2 値：Per | Num | Num | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, VALUE, STATUS

## g0020（2 列）
- 見出し：VALUE
- 例1 値：34.16 | 4791.0 | 68505.0 | 0.05 | 21712.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS
- 例2 値：144.0 | 25.0 | 3912.0 | 42900.0 | 90.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS

## g0021（2 列）
- 見出し：STATUS
- 例1 値：M | A | A | A | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE
- 例2 値：Q | A | A | Q | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE

## g0022（1 列）
- 見出し：GEO_NR
- 例1 値：581 | 1630 | 161 | 404 | 363
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0023（1 列）
- 見出し：VARIABLE
- 例1 値：nui_1000 | nui_1000 | nuit_etr_p | nuit_t | nui_1000
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0024（3 列）
- 見出し：DATE
- 例1 値：1875-05-23 | 1876-04-23 | 1877-10-21 | 1876-04-23 | 1882-07-30
  - 同じ表の列：anr, TITEL, GMDnr, GMD, BEZnr, BEZ, BERE, STIM
- 例2 値：1876-05-28 | 1874-06-21 | 1876-05-28 | 1876-05-28 | 1876-05-28
  - 同じ表の列：BLNr, TITEL, GMDnr, GMD, BEZnr, BEZ, BERE, STIM

## g0025（1 列）
- 見出し：anr
- 例1 値：19.0 | 22.0 | 14.0 | 17.0 | 22.0
  - 同じ表の列：DATE, TITEL, GMDnr, GMD, BEZnr, BEZ, BERE, STIM

## g0026（1 列）
- 見出し：TITEL
- 例1 値：Bundesgesez betreffend die politischen … | Totalrevision | Bundesgesez betreffend Gewährung von Su… | Bundesgesez über die politische Stimmbe… | Totalrevision
  - 同じ表の列：DATE, anr, GMDnr, GMD, BEZnr, BEZ, BERE, STIM

## g0027（2 列）
- 見出し：GMDnr
- 例1 値：6 | 71 | 57 | 47 | 7
  - 同じ表の列：DATE, anr, TITEL, GMD, BEZnr, BEZ, BERE, STIM
- 例2 値：7 | 15 | 32 | 6 | 17
  - 同じ表の列：DATE, BLNr, TITEL, GMD, BEZnr, BEZ, BERE, STIM

## g0028（1 列）
- 見出し：GMD
- 例1 値：Rümlingen | Liedertswil | Schönenbuch | Biel-Benken | Reinach (BL)
  - 同じ表の列：DATE, anr, TITEL, GMDnr, BEZnr, BEZ, BERE, STIM

## g0029（2 列）
- 見出し：BEZnr
- 例1 値：1305 | 1305 | 1303 | 1304 | 1304
  - 同じ表の列：DATE, anr, TITEL, GMDnr, GMD, BEZ, BERE, STIM
- 例2 値：1301 | 1303 | 1301 | 1303 | 1303
  - 同じ表の列：DATE, BLNr, TITEL, GMDnr, GMD, BEZ, BERE, STIM

## g0030（2 列）
- 見出し：BEZ
- 例1 値：Arlesheim | Sissach | Sissach | Arlesheim | Arlesheim
  - 同じ表の列：DATE, anr, TITEL, GMDnr, GMD, BEZnr, BERE, STIM
- 例2 値：Sissach | Liestal | Sissach | Sissach | Sissach
  - 同じ表の列：DATE, BLNr, TITEL, GMDnr, GMD, BEZnr, BERE, STIM

## g0031（2 列）
- 見出し：BERE
- 例1 値：70 | 50 | 46 | 154 | 69
  - 同じ表の列：DATE, anr, TITEL, GMDnr, GMD, BEZnr, BEZ, STIM
- 例2 値：26 | 99 | 104 | 182 | 168
  - 同じ表の列：DATE, BLNr, TITEL, GMDnr, GMD, BEZnr, BEZ, STIM

## g0032（2 列）
- 見出し：STIM
- 例1 値：78 | 150 | 43 | 82 | 139
  - 同じ表の列：DATE, anr, TITEL, GMDnr, GMD, BEZnr, BEZ, BERE
- 例2 値：31 | 56 | 78 | 36 | 28
  - 同じ表の列：DATE, BLNr, TITEL, GMDnr, GMD, BEZnr, BEZ, BERE

## g0033（2 列）
- 見出し：LEUG
- 例1 値：2 | 2 | 2 | 1 | 1
  - 同じ表の列：DATE, anr, TITEL, GMDnr, GMD, BEZnr, BEZ, BERE
- 例2 値：4 | 8 | 1 | 1 | 6
  - 同じ表の列：DATE, BLNr, TITEL, GMDnr, GMD, BEZnr, BEZ, BERE

## g0034（1 列）
- 見出し：BLNr
- 例1 値：76.0 | 80.0 | 71.0 | 73.0 | 77.0
  - 同じ表の列：DATE, TITEL, GMDnr, GMD, BEZnr, BEZ, BERE, STIM

## g0035（1 列）
- 見出し：TITEL
- 例1 値：Frage, ob die kantonale Verfassung soll… | Gesetz betreffend das Bergbauregal | Gesetz betreffend das Gemeindeschulwesen | Frage, ob die kantonale Verfassung soll… | Landratsbeschluss betreffend den Einzug…
  - 同じ表の列：DATE, BLNr, GMDnr, GMD, BEZnr, BEZ, BERE, STIM

## g0036（1 列）
- 見出し：GMD
- 例1 値：Arisdorf | Tecknau | Liestal | Arboldswil | Lausen
  - 同じ表の列：DATE, BLNr, TITEL, GMDnr, BEZnr, BEZ, BERE, STIM

## g0037（1 列）
- 見出し：entity_id
- 例1 値：2866 | 2894 | 2895 | 2771 | 2789
  - 同じ表の列：date, district, vote_id, domain, type, title_de_CH, counted, answer

## g0038（1 列）
- 見出し：district
- 例1 値：Arlesheim | Sissach | Laufen | Waldenburg | Arlesheim
  - 同じ表の列：date, entity_id, vote_id, domain, type, title_de_CH, counted, answer

## g0039（1 列）
- 見出し：vote_id
- 例1 値：20261129_K5 | 20260614_E2 | 20261129_E4 | 20260927_E1 | 20261129_K5
  - 同じ表の列：date, entity_id, district, domain, type, title_de_CH, counted, answer

## g0040（1 列）
- 見出し：domain
- 例1 値：canton | federation | federation | canton | federation
  - 同じ表の列：date, entity_id, district, vote_id, type, title_de_CH, counted, answer

## g0041（1 列）
- 見出し：type
- 例1 値：tie-breaker | proposal | proposal | proposal | proposal
  - 同じ表の列：date, entity_id, district, vote_id, domain, title_de_CH, counted, answer

## g0042（1 列）
- 見出し：title_de_CH
- 例1 値：Formulierte Verfassungsinitiative «Fair… | Volksinitiative «Für eine Einschränkung… | Volksinitiative «Wahrung der schweizeri… | Änderung vom 26. September 2025 des Bun… | Bundesbeschluss vom 19. Juni 2026 über …
  - 同じ表の列：date, entity_id, district, vote_id, domain, type, counted, answer

## g0043（1 列）
- 見出し：counted
- 例1 値：False | True | False | True | True
  - 同じ表の列：date, entity_id, district, vote_id, domain, type, title_de_CH, answer

## g0044（1 列）
- 見出し：answer
- 例1 値：rejected | rejected | rejected | rejected | rejected
  - 同じ表の列：date, entity_id, district, vote_id, domain, type, title_de_CH, counted

## g0045（1 列）
- 見出し：percent_yeas
- 例1 値：43.58293209364104 | 40.56382145653876 | 33.66935483870967 | 37.75322283609576 | 35.91549295774648
  - 同じ表の列：date, entity_id, district, vote_id, domain, type, title_de_CH, counted

## g0046（1 列）
- 見出し：Probentyp
- 例1 値：WASSER | WASSER | WASSER | WASSER | WASSER
  - 同じ表の列：Probenahmestelle, Geo Point, X-Koordinate, Y-Koordinate, Probenahmedatum, Entnahmezeit, Probenahmedauer, Reihenfolge

## g0047（1 列）
- 見出し：Probenahmestelle
- 例1 値：GEW_RHEIN_RUES | GEW_RHEIN_RUES | GEW_RHEIN_RUES | GEW_RHEIN_RUES | GEW_RHEIN_RUES
  - 同じ表の列：Probentyp, Geo Point, X-Koordinate, Y-Koordinate, Probenahmedatum, Entnahmezeit, Probenahmedauer, Reihenfolge

## g0048（1 列）
- 見出し：Geo Point
- 例1 値：47.601425244728325, 7.592921637557185 | 47.601425244728325, 7.592921637557185 | 47.601425244728325, 7.592921637557185 | 47.601425244728325, 7.592921637557185 | 47.601425244728325, 7.592921637557185
  - 同じ表の列：Probentyp, Probenahmestelle, X-Koordinate, Y-Koordinate, Probenahmedatum, Entnahmezeit, Probenahmedauer, Reihenfolge

## g0049（1 列）
- 見出し：X-Koordinate
- 例1 値：2611604 | 2611604 | 2611604 | 2611604 | 2611604
  - 同じ表の列：Probentyp, Probenahmestelle, Geo Point, Y-Koordinate, Probenahmedatum, Entnahmezeit, Probenahmedauer, Reihenfolge

## g0050（1 列）
- 見出し：Y-Koordinate
- 例1 値：1272316 | 1272316 | 1272316 | 1272316 | 1272316
  - 同じ表の列：Probentyp, Probenahmestelle, Geo Point, X-Koordinate, Probenahmedatum, Entnahmezeit, Probenahmedauer, Reihenfolge

## g0051（1 列）
- 見出し：Probenahmedatum
- 例1 値：06.10.2026 | 22.09.2026 | 08.09.2026 | 06.10.2026 | 22.09.2026
  - 同じ表の列：Probentyp, Probenahmestelle, Geo Point, X-Koordinate, Y-Koordinate, Entnahmezeit, Probenahmedauer, Reihenfolge

## g0052（1 列）
- 見出し：Entnahmezeit
- 例1 値：08:00 | 08:00 | 08:00 | 08:00 | 08:00
  - 同じ表の列：Probentyp, Probenahmestelle, Geo Point, X-Koordinate, Y-Koordinate, Probenahmedatum, Probenahmedauer, Reihenfolge

## g0053（1 列）
- 見出し：Probenahmedauer
- 例1 値：14M_MS | 14M_MS | 1M14_MS | 14M_MS | 1M28_MS
  - 同じ表の列：Probentyp, Probenahmestelle, Geo Point, X-Koordinate, Y-Koordinate, Probenahmedatum, Entnahmezeit, Reihenfolge

## g0054（1 列）
- 見出し：Reihenfolge
- 例1 値：113900 | 413500 | 402800 | 113905 | 127500
  - 同じ表の列：Probentyp, Probenahmestelle, Geo Point, X-Koordinate, Y-Koordinate, Probenahmedatum, Entnahmezeit, Probenahmedauer

## g0055（1 列）
- 見出し：Gruppe
- 例1 値：Pestizide | Arzneimittel | Kationen | Summenparameter | Pestizide
  - 同じ表の列：Probentyp, Probenahmestelle, Geo Point, X-Koordinate, Y-Koordinate, Probenahmedatum, Entnahmezeit, Probenahmedauer

## g0056（2 列）
- 見出し：Zeitstempel
- 例1 値：2026-10-30T00:55:00+00:00 | 2026-10-30T23:50:00+00:00 | 2026-10-31T22:05:00+00:00 | 2026-10-30T06:40:00+00:00 | 2026-10-29T16:35:00+00:00
  - 同じ表の列：Abflussmenge, Pegel, Wasserstand
- 例2 値：2026-10-31T22:23:00+00:00 | 2026-10-28T17:57:00+00:00 | 2026-10-31T22:34:00+00:00 | 2026-10-30T19:39:00+00:00 | 2026-10-30T16:36:00+00:00
  - 同じ表の列：Station, Wert, Geopunkt, Geographische Breite, Geographische Länge, EUI

## g0057（1 列）
- 見出し：Abflussmenge
- 例1 値：352.363 | 365.218 | 331.814 | 394.483 | 373.505
  - 同じ表の列：Zeitstempel, Pegel, Wasserstand

## g0058（1 列）
- 見出し：Pegel
- 例1 値：487.6000000000005 | 492.1999999999997 | 487.3999999999995 | 485.499999999999 | 488.2000000000005
  - 同じ表の列：Zeitstempel, Abflussmenge, Wasserstand

## g0059（1 列）
- 見出し：Wasserstand
- 例1 値：244.819 | 244.883 | 244.893 | 244.927 | 244.882
  - 同じ表の列：Zeitstempel, Abflussmenge, Pegel

## g0060（1 列）
- 見出し：Station
- 例1 値：Feldbergstrasse | Feldbergstrasse | Feldbergstrasse | Feldbergstrasse | Feldbergstrasse
  - 同じ表の列：Zeitstempel, Wert, Geopunkt, Geographische Breite, Geographische Länge, EUI

## g0061（1 列）
- 見出し：Wert
- 例1 値：68.0 | 66.8 | 68.3 | 67.0 | 66.4
  - 同じ表の列：Station, Zeitstempel, Geopunkt, Geographische Breite, Geographische Länge, EUI

## g0062（1 列）
- 見出し：Geopunkt
- 例1 値：47.567005, 7.594749 | 47.567005, 7.594749 | 47.567005, 7.594749 | 47.567005, 7.594749 | 47.567005, 7.594749
  - 同じ表の列：Station, Zeitstempel, Wert, Geographische Breite, Geographische Länge, EUI

## g0063（1 列）
- 見出し：Geographische Breite
- 例1 値：47.567005 | 47.567005 | 47.567005 | 47.567005 | 47.567005
  - 同じ表の列：Station, Zeitstempel, Wert, Geopunkt, Geographische Länge, EUI

## g0064（1 列）
- 見出し：Geographische Länge
- 例1 値：7.594749 | 7.594749 | 7.594749 | 7.594749 | 7.594749
  - 同じ表の列：Station, Zeitstempel, Wert, Geopunkt, Geographische Breite, EUI

## g0065（1 列）
- 見出し：EUI
- 例1 値：0004A30B00F156E2 | 0004A30B00F156E2 | 0004A30B00F156E2 | 0004A30B00F156E2 | 0004A30B00F156E2
  - 同じ表の列：Station, Zeitstempel, Wert, Geopunkt, Geographische Breite, Geographische Länge

## g0066（1 列）
- 見出し：traktandum_uid
- 例1 値：a3d0be7d3ca2411db7df770f687536a7 | 7974df5e483a4a4e82dbb469cb04d048 | e952ea61d25446e5bab58baf00463d83 | 13bc6d4ba4234e21baa2d866e041ca09 | 3864592eee3f49689c06a5da319e84b0
  - 同じ表の列：element_id, antrag_titel, Übersicht vom

## g0067（1 列）
- 見出し：element_id
- 例1 値：7c293ea6-0871-4c03-a032-21d4bb7851a2 | 67c5f15ae74e1aca7cbf1f1f | 68b97aca0b48f589b235fff2 | a994b931-48c7-4b5f-92ce-11beeee90291 | 6406319340392e7dfdbdcbe6
  - 同じ表の列：traktandum_uid, antrag_titel, Übersicht vom

## g0068（1 列）
- 見出し：antrag_titel
- 例1 値：Antrag / Proposition | Antrag / Proposition | Eventualantrag / Proposition subsidiaire | Antrag / Proposition | Antrag / Proposition
  - 同じ表の列：traktandum_uid, element_id, Übersicht vom

## g0069（1 列）
- 見出し：Übersicht vom
- 例1 値：2026-11-01 00:00 | 2026-11-01 00:00 | 2026-11-01 00:00 | 2026-11-01 00:00 | 2026-11-01 00:00
  - 同じ表の列：traktandum_uid, element_id, antrag_titel

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
```
