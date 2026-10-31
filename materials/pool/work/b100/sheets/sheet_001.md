# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（11 列）
- 見出し：Jahr
- 例1 値：1977 | 2019 | 1993 | 1972 | 2004
  - 同じ表の列：Erzeugung_laufwerk_…, Erzeugung_speicherw…, Erzeugung_kernkraft…, Erzeugung_andere_to…, Erzeugung_andere_fo…, Erzeugung_andere_er…, Erzeugung_holz_GWh, Erzeugung_biogas_GWh
- 例2 値：1983 | 1980 | 1983 | 1983 | 1980
  - 同じ表の列：Rubrik, Energietraeger, TJ

## g0002（1 列）
- 見出し：Erzeugung_laufwerk_GWh
- 例1 値：15490 | 16590 | 15277 | 17648 | 14695
  - 同じ表の列：Jahr, Erzeugung_speicherw…, Erzeugung_kernkraft…, Erzeugung_andere_to…, Erzeugung_andere_fo…, Erzeugung_andere_er…, Erzeugung_holz_GWh, Erzeugung_biogas_GWh

## g0003（1 列）
- 見出し：Erzeugung_speicherwerk_GWh
- 例1 値：14832 | 18575 | 21013 | 16040 | 16029
  - 同じ表の列：Jahr, Erzeugung_laufwerk_…, Erzeugung_kernkraft…, Erzeugung_andere_to…, Erzeugung_andere_fo…, Erzeugung_andere_er…, Erzeugung_holz_GWh, Erzeugung_biogas_GWh

## g0004（1 列）
- 見出し：Erzeugung_kernkraftwerk_GWh
- 例1 値：24368 | 23334 | 7995 | 22020 | 1850
  - 同じ表の列：Jahr, Erzeugung_laufwerk_…, Erzeugung_speicherw…, Erzeugung_andere_to…, Erzeugung_andere_fo…, Erzeugung_andere_er…, Erzeugung_holz_GWh, Erzeugung_biogas_GWh

## g0005（1 列）
- 見出し：Erzeugung_andere_total_GWh
- 例1 値：1885 | 2866 | 2320 | 3103 | 2386
  - 同じ表の列：Jahr, Erzeugung_laufwerk_…, Erzeugung_speicherw…, Erzeugung_kernkraft…, Erzeugung_andere_fo…, Erzeugung_andere_er…, Erzeugung_holz_GWh, Erzeugung_biogas_GWh

## g0006（1 列）
- 見出し：Erzeugung_andere_fossil_GWh
- 例1 値：1082 | 1979 | 1728 | 1937 | 1877
  - 同じ表の列：Jahr, Erzeugung_laufwerk_…, Erzeugung_speicherw…, Erzeugung_kernkraft…, Erzeugung_andere_to…, Erzeugung_andere_er…, Erzeugung_holz_GWh, Erzeugung_biogas_GWh

## g0007（1 列）
- 見出し：Erzeugung_andere_erneuerbare_abfaelle_GWh
- 例1 値：705 | 1169 | 797 | 423 | 963
  - 同じ表の列：Jahr, Erzeugung_laufwerk_…, Erzeugung_speicherw…, Erzeugung_kernkraft…, Erzeugung_andere_to…, Erzeugung_andere_fo…, Erzeugung_holz_GWh, Erzeugung_biogas_GWh

## g0008（1 列）
- 見出し：Erzeugung_holz_GWh
- 例1 値：475 | 92 | 29 | 135 | 184
  - 同じ表の列：Jahr, Erzeugung_laufwerk_…, Erzeugung_speicherw…, Erzeugung_kernkraft…, Erzeugung_andere_to…, Erzeugung_andere_fo…, Erzeugung_andere_er…, Erzeugung_biogas_GWh

## g0009（1 列）
- 見出し：Erzeugung_biogas_GWh
- 例1 値：80 | 106 | 372 | 290 | 145
  - 同じ表の列：Jahr, Erzeugung_laufwerk_…, Erzeugung_speicherw…, Erzeugung_kernkraft…, Erzeugung_andere_to…, Erzeugung_andere_fo…, Erzeugung_andere_er…, Erzeugung_holz_GWh

## g0010（1 列）
- 見出し：Erzeugung_photovoltaik_GWh
- 例1 値：299 | 842 | 1119 | 3858 | 2599
  - 同じ表の列：Jahr, Erzeugung_laufwerk_…, Erzeugung_speicherw…, Erzeugung_kernkraft…, Erzeugung_andere_to…, Erzeugung_andere_fo…, Erzeugung_andere_er…, Erzeugung_holz_GWh

## g0011（1 列）
- 見出し：Rubrik
- 例1 値：Endverbrauch - Dienstleistungen | Energieumwandlung - Raffinerien | Lagerveränderung | Endverbrauch - Total | Eigenverbrauch des Energiesektors, Netz…
  - 同じ表の列：Jahr, Energietraeger, TJ

## g0012（1 列）
- 見出し：Energietraeger
- 例1 値：Gas | Elektrizität | Holzenergie | Elektrizität | Rohöl
  - 同じ表の列：Jahr, Rubrik, TJ

## g0013（1 列）
- 見出し：TJ
- 例1 値：-1000 | -189770 | 36280 | NA | 23910
  - 同じ表の列：Jahr, Rubrik, Energietraeger

## g0014（3 列）
- 見出し：GEO_NR
- 例1 値：53 | 53 | 96 | 118 | 117
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：161 | 700 | 723 | 627 | 131
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0015（3 列）
- 見出し：CLASS_HAB
- 例1 値：2 | 4 | 4 | 2 | 2
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：2 | 4 | 4 | 6 | 2
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0016（3 列）
- 見出し：GEOM_PERIOD
- 例1 値：2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0017（1 列）
- 見出し：VARIABLE
- 例1 値：exe_ga_t | par_ga_f | par_s_occ | exe_cvp_f | exe_bdp_t
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0018（1 列）
- 見出し：SOURCE
- 例1 値：BFS, SSV | BFS, SSV | BFS, SSV | BFS, SSV | BFS, SSV
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0019（3 列）
- 見出し：VALUE_PERIOD
- 例1 値：2022 | 2022 | 2022 | 2022 | 2022
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS
- 例2 値：2018 | 2016 | 2020 | 2014 | 2020
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS

## g0020（3 列）
- 見出し：UNIT_VALUE
- 例1 値：Num | Num | Num | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, VALUE, STATUS
- 例2 値：Num | Per | Num | Num | Per
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, VALUE, STATUS

## g0021（1 列）
- 見出し：VALUE
- 例1 値：0 | 0 | 0 | 0 | 1
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS

## g0022（3 列）
- 見出し：STATUS
- 例1 値：A | A | A | A | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE
- 例2 値：A | A | A | A | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE

## g0023（1 列）
- 見出し：VARIABLE
- 例1 値：t_soc_2015 | tx_soc_2018 | tx_soc_2017 | tx_soc_2018 | tx_soc_2016
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0024（1 列）
- 見出し：SOURCE
- 例1 値：SHS | SHS | SHS | SHS | SHS
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0025（2 列）
- 見出し：VALUE
- 例1 値：497.0 | 1026.0 | 3.4 | 1873.0 | 556.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS
- 例2 値：11790.0 | 1258.0 | 712.0 | 2.4 | 3156.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS

## g0026（1 列）
- 見出し：VARIABLE
- 例1 値：chom_com_f | chom_com_t | chom_s3 | chom_f | etab_1_9
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0027（1 列）
- 見出し：SOURCE
- 例1 値：STATENT | STATENT | SECO, SE | SECO, SE | SECO, SE
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0028（1 列）
- 見出し：Zweck
- 例1 値：Zentrale Verwaltung der Daten der Stati… | Zentrale Bereitstellung von aktuellen B… | Zentrale Verwaltung der Daten der Stati… | Zentrale Verwaltung der Daten der Stati… | Zentrale Verwaltung der Daten der Bildu…
  - 同じ表の列：Inhalt, Merkmale, Verantwortlich, Zugriffsrechte, Referenz, Zeitliche Abdeckung, Frequenz, Konform zu

## g0029（1 列）
- 見出し：Inhalt
- 例1 値：Das Statistikregister des Schulpersonal… | Das Statistikregister der Bildungsinsti… | Daten aller natürlichen Personen, welch… | Das Statistikregister der Lernenden umf… | Das Statistikregister der Bodenpreise u…
  - 同じ表の列：Zweck, Merkmale, Verantwortlich, Zugriffsrechte, Referenz, Zeitliche Abdeckung, Frequenz, Konform zu

## g0030（1 列）
- 見出し：Merkmale
- 例1 値：Bundesrechtliche Merkmale gemäss GWR Me… | Beschäftigungsgrad, Geburtsdatum, Arbei… | Name, Adressangaben, Kontaktangaben (E-… | Erhebungsjahr, Belegs- und Fallnummer, … | Bildungsinstitution, Schulhaus, Klasse,…
  - 同じ表の列：Zweck, Inhalt, Verantwortlich, Zugriffsrechte, Referenz, Zeitliche Abdeckung, Frequenz, Konform zu

## g0031（1 列）
- 見出し：Verantwortlich
- 例1 値：Amt für Daten und Statistik BL | Amt für Daten und Statistik BL | Amt für Daten und Statistik BL | Amt für Daten und Statistik BL | Amt für Daten und Statistik BL
  - 同じ表の列：Zweck, Inhalt, Merkmale, Zugriffsrechte, Referenz, Zeitliche Abdeckung, Frequenz, Konform zu

## g0032（1 列）
- 見出し：Zugriffsrechte
- 例1 値：nicht-öffentlich | eingeschränkt | nicht-öffentlich | nicht-öffentlich | nicht-öffentlich
  - 同じ表の列：Zweck, Inhalt, Merkmale, Verantwortlich, Referenz, Zeitliche Abdeckung, Frequenz, Konform zu

## g0033（1 列）
- 見出し：Referenz
- 例1 値：https://bl.clex.ch/api/annex_document_d… | https://www.baselland.ch/politik-und-be… | https://bl.clex.ch/api/annex_document_d… | https://bl.clex.ch/api/annex_document_d… | https://bl.clex.ch/api/annex_document_d…
  - 同じ表の列：Zweck, Inhalt, Merkmale, Verantwortlich, Zugriffsrechte, Zeitliche Abdeckung, Frequenz, Konform zu

## g0034（1 列）
- 見出し：Zeitliche Abdeckung
- 例1 値：seit 2010 | seit 2008 | seit 1979 | seit 1986 | seit 2012
  - 同じ表の列：Zweck, Inhalt, Merkmale, Verantwortlich, Zugriffsrechte, Referenz, Frequenz, Konform zu

## g0035（1 列）
- 見出し：Frequenz
- 例1 値：bei Bedarf | jährlich | stündlich | jährlich | jährlich
  - 同じ表の列：Zweck, Inhalt, Merkmale, Verantwortlich, Zugriffsrechte, Referenz, Zeitliche Abdeckung, Konform zu

## g0036（1 列）
- 見出し：Konform zu
- 例1 値：https://www.ech.ch/de/ech/ech-0020/3.0 | https://www.ech.ch/de/ech/ech-0206/2.0.0
  - 同じ表の列：Zweck, Inhalt, Merkmale, Verantwortlich, Zugriffsrechte, Referenz, Zeitliche Abdeckung, Frequenz

## g0037（1 列）
- 見出し：Mitwirkende Stelle
- 例1 値：Generalsekretariat der Bildungs-, Kultu… | Bildungs-, Kultur- und Sportdirektion | Einwohnergemeinden, kantonale Dienstste… | Meldepflichtige Institutionen gemäss Ar…
  - 同じ表の列：Zweck, Inhalt, Merkmale, Verantwortlich, Zugriffsrechte, Referenz, Zeitliche Abdeckung, Frequenz

## g0038（1 列）
- 見出し：Klasse_Steuerbares_Vermoegen_Code
- 例1 値：10 | 6 | 10 | 14 | 14
  - 同じ表の列：Jahr, Klasse_Steuerbares_…, Indikator, Wert

## g0039（1 列）
- 見出し：Klasse_Steuerbares_Vermoegen_CHF
- 例1 値：200'000 - 249'999 | 500'000 - 599'999 | 10'000'000 + | 200'000 - 249'999 | 5'000'000 - 9'999'999
  - 同じ表の列：Jahr, Klasse_Steuerbares_…, Indikator, Wert

## g0040（1 列）
- 見出し：Indikator
- 例1 値：Vermoegenssteuerertrag_CHF | Steuerbares_Vermoegen_CHF | Anzahl_Steuerpflichtige | Vermoegenssteuerertrag_CHF | Anzahl_Steuerpflichtige
  - 同じ表の列：Jahr, Klasse_Steuerbares_…, Klasse_Steuerbares_…, Wert

## g0041（1 列）
- 見出し：Wert
- 例1 値：2228.0 | 2261.0 | 669351416.0 | 14872898.35 | 1461420.85
  - 同じ表の列：Jahr, Klasse_Steuerbares_…, Klasse_Steuerbares_…, Indikator

## g0042（1 列）
- 見出し：Bezirk_Nummer
- 例1 値：1304 | 1305 | 1304 | 1305 | 1305
  - 同じ表の列：Jahr, Bezirk, Zimmerzahl, Verkaufspreis_CHF

## g0043（1 列）
- 見出し：Bezirk
- 例1 値：Bezirk Laufen | Bezirk Sissach | Bezirk Arlesheim | Bezirk Sissach | Bezirk Sissach
  - 同じ表の列：Jahr, Bezirk_Nummer, Zimmerzahl, Verkaufspreis_CHF

## g0044（1 列）
- 見出し：Zimmerzahl
- 例1 値：5+ | 5+ | 5+ | 5+ | 3
  - 同じ表の列：Jahr, Bezirk_Nummer, Bezirk, Verkaufspreis_CHF

## g0045（1 列）
- 見出し：Verkaufspreis_CHF
- 例1 値：490667 | 572545 | ( ) | 581285 | 806493
  - 同じ表の列：Jahr, Bezirk_Nummer, Bezirk, Zimmerzahl

## g0046（1 列）
- 見出し：Messung-ID
- 例1 値：124 | 573 | 527 | 500 | 531
  - 同じ表の列：Messbeginn, Messende, Ort, Zone, Richtung 1, Fahrzeuge Richtung 1, V50 Richtung 1, V85 Richtung 1

## g0047（1 列）
- 見出し：Messbeginn
- 例1 値：2021-07-19 | 2022-03-21 | 2021-03-08 | 2025-03-31 | 2020-05-18
  - 同じ表の列：Messung-ID, Messende, Ort, Zone, Richtung 1, Fahrzeuge Richtung 1, V50 Richtung 1, V85 Richtung 1

## g0048（1 列）
- 見出し：Messende
- 例1 値：2025-02-16 | 2026-02-17 | 2024-04-02 | 2021-08-30 | 2020-07-20
  - 同じ表の列：Messung-ID, Messbeginn, Ort, Zone, Richtung 1, Fahrzeuge Richtung 1, V50 Richtung 1, V85 Richtung 1

## g0049（1 列）
- 見出し：Ort
- 例1 値：Basel | Basel | Basel | Basel | Basel
  - 同じ表の列：Messung-ID, Messbeginn, Messende, Zone, Richtung 1, Fahrzeuge Richtung 1, V50 Richtung 1, V85 Richtung 1

## g0050（1 列）
- 見出し：Zone
- 例1 値：30 | 50 | 30 | 50 | 50
  - 同じ表の列：Messung-ID, Messbeginn, Messende, Ort, Richtung 1, Fahrzeuge Richtung 1, V50 Richtung 1, V85 Richtung 1

## g0051（1 列）
- 見出し：Richtung 1
- 例1 値：Giornicostrasse | Helvetierstrasse | Barfüsserplatz | Oberwilerstrasse | Banngrenze Bettingen
  - 同じ表の列：Messung-ID, Messbeginn, Messende, Ort, Zone, Fahrzeuge Richtung 1, V50 Richtung 1, V85 Richtung 1

## g0052（1 列）
- 見出し：Fahrzeuge Richtung 1
- 例1 値：5655.0 | 201276.0 | 8472.0 | 27890.0 | 44348.0
  - 同じ表の列：Messung-ID, Messbeginn, Messende, Ort, Zone, Richtung 1, V50 Richtung 1, V85 Richtung 1

## g0053（1 列）
- 見出し：V50 Richtung 1
- 例1 値：29.0 | 17.0 | 29.0 | 31.0 | 50.0
  - 同じ表の列：Messung-ID, Messbeginn, Messende, Ort, Zone, Richtung 1, Fahrzeuge Richtung 1, V85 Richtung 1

## g0054（1 列）
- 見出し：V85 Richtung 1
- 例1 値：26.0 | 47.0 | 21.0 | 21.0 | 36.0
  - 同じ表の列：Messung-ID, Messbeginn, Messende, Ort, Zone, Richtung 1, Fahrzeuge Richtung 1, V50 Richtung 1

## g0055（1 列）
- 見出し：Übertretungsquote Richtung 1
- 例1 値：1.1 | 6.23 | 3.53 | 6.4 | 4.49
  - 同じ表の列：Messung-ID, Messbeginn, Messende, Ort, Zone, Richtung 1, Fahrzeuge Richtung 1, V50 Richtung 1

## g0056（1 列）
- 見出し：StationId
- 例1 値：1655 | 1443 | 4541 | 720 | 1205
  - 同じ表の列：SensorNr, lat, lon, geo_point_2d, XCoord, YCoord, topTerrain, refPoint

## g0057（1 列）
- 見出し：SensorNr
- 例1 値：10 | 10 | 10 | 10 | 10
  - 同じ表の列：StationId, lat, lon, geo_point_2d, XCoord, YCoord, topTerrain, refPoint

## g0058（1 列）
- 見出し：lat
- 例1 値：47.56404716876332 | 47.559077466314534 | 47.57109702010099 | 47.560932815623566 | 47.55084084591139
  - 同じ表の列：StationId, SensorNr, lon, geo_point_2d, XCoord, YCoord, topTerrain, refPoint

## g0059（1 列）
- 見出し：lon
- 例1 値：7.574904561270931 | 7.594774243128972 | 7.596807260222682 | 7.6000706007077286 | 7.567225700153881
  - 同じ表の列：StationId, SensorNr, lat, geo_point_2d, XCoord, YCoord, topTerrain, refPoint

## g0060（1 列）
- 見出し：geo_point_2d
- 例1 値：47.57172410382941, 7.558136165736032 | 47.57342737252096, 7.6000706007077286 | 47.570212150660964, 7.590000788775492 | 47.56563540672905, 7.574546852203753 | 47.55104942594387, 7.587754523570976
  - 同じ表の列：StationId, SensorNr, lat, lon, XCoord, YCoord, topTerrain, refPoint

## g0061（1 列）
- 見出し：XCoord
- 例1 値：2611783 | 2611540 | 2611850 | 2610853 | 2615175
  - 同じ表の列：StationId, SensorNr, lat, lon, geo_point_2d, YCoord, topTerrain, refPoint

## g0062（1 列）
- 見出し：YCoord
- 例1 値：1271314 | 1268763 | 1266561 | 1269263 | 1268763
  - 同じ表の列：StationId, SensorNr, lat, lon, geo_point_2d, XCoord, topTerrain, refPoint

## g0063（1 列）
- 見出し：topTerrain
- 例1 値：269.91 | 255.82 | 253.86 | 256.6 | 281.04
  - 同じ表の列：StationId, SensorNr, lat, lon, geo_point_2d, XCoord, YCoord, refPoint

## g0064（1 列）
- 見出し：refPoint
- 例1 値：276.05 | 261.66 | 275.33 | 267.82 | 256.12
  - 同じ表の列：StationId, SensorNr, lat, lon, geo_point_2d, XCoord, YCoord, topTerrain

## g0065（1 列）
- 見出し：10YMin
- 例1 値：260.39 | 247.53 | 250.27 | 245.66 | 250.27
  - 同じ表の列：StationId, SensorNr, lat, lon, geo_point_2d, XCoord, YCoord, topTerrain

## g0066（1 列）
- 見出し：Beschriftung
- 例1 値：1.1.001 | 1.1.013 | 1.1.004 | 1.2.009 | 1.2.022
  - 同じ表の列：ID Statistische Rau…, ID Statistische Rau…, Geometrie, Geo Point, Jahr, Anteil Ausländer, Anteil Kantonsbürger, Anteil Kantonsbürge…

## g0067（1 列）
- 見出し：ID Statistische Raumeinheit
- 例1 値：012 | 012 | 012 | 011 | 011
  - 同じ表の列：Beschriftung, ID Statistische Rau…, Geometrie, Geo Point, Jahr, Anteil Ausländer, Anteil Kantonsbürger, Anteil Kantonsbürge…

## g0068（1 列）
- 見出し：ID Statistische Raumeinheit_2
- 例1 値：01 | 01 | 01 | 01 | 01
  - 同じ表の列：Beschriftung, ID Statistische Rau…, Geometrie, Geo Point, Jahr, Anteil Ausländer, Anteil Kantonsbürger, Anteil Kantonsbürge…

## g0069（1 列）
- 見出し：Geometrie
- 例1 値：{"coordinates": [[[7.588946, 47.559206]… | {"coordinates": [[[7.587959, 47.559151]… | {"coordinates": [[[7.59431, 47.555914],… | {"coordinates": [[[7.589435, 47.555193]… | {"coordinates": [[[7.589352, 47.557014]…
  - 同じ表の列：Beschriftung, ID Statistische Rau…, ID Statistische Rau…, Geo Point, Jahr, Anteil Ausländer, Anteil Kantonsbürger, Anteil Kantonsbürge…

## g0070（1 列）
- 見出し：Geo Point
- 例1 値：47.559019039612224, 7.587435364056381 | 47.55985278510657, 7.587280473689219 | 47.554728037794746, 7.593386302929415 | 47.55474486570151, 7.590993715777986 | 47.55543434740238, 7.592125406210662
  - 同じ表の列：Beschriftung, ID Statistische Rau…, ID Statistische Rau…, Geometrie, Jahr, Anteil Ausländer, Anteil Kantonsbürger, Anteil Kantonsbürge…

## g0071（1 列）
- 見出し：Anteil Ausländer
- 例1 値：32.5 | 52.9 | 10.0 | 12.9 | 20.0
  - 同じ表の列：Beschriftung, ID Statistische Rau…, ID Statistische Rau…, Geometrie, Geo Point, Jahr, Anteil Kantonsbürger, Anteil Kantonsbürge…

## g0072（1 列）
- 見出し：Anteil Kantonsbürger
- 例1 値：18.8 | 10.0 | 45.7 | 56.0 | 62.5
  - 同じ表の列：Beschriftung, ID Statistische Rau…, ID Statistische Rau…, Geometrie, Geo Point, Jahr, Anteil Ausländer, Anteil Kantonsbürge…

## g0073（1 列）
- 見出し：Anteil Kantonsbürger an der Schweizer Bevölkerung
- 例1 値：50.0 | 100.0 | 12.5 | 30.0 | 66.7
  - 同じ表の列：Beschriftung, ID Statistische Rau…, ID Statistische Rau…, Geometrie, Geo Point, Jahr, Anteil Ausländer, Anteil Kantonsbürger

## g0074（1 列）
- 見出し：Anteil Schweizer
- 例1 値：70.0 | 75.0 | 95.0 | 20.0 | 70.0
  - 同じ表の列：Beschriftung, ID Statistische Rau…, ID Statistische Rau…, Geometrie, Geo Point, Jahr, Anteil Ausländer, Anteil Kantonsbürger

## g0075（1 列）
- 見出し：berufsnr
- 例1 値：21107 | 71429 | 21604 | 46505 | 53304
  - 同じ表の列：isced, berufsbezeichnung, efz_eba, jahr, bildungsverh_m, bildungsverh_w, ausbildungsverh_ver…, ausbildungsverh_ver…

## g0076（1 列）
- 見出し：isced
- 例1 値：Baugewerbe, Hoch- und Tiefbau | Elektronik und Automation | Kraftfahrzeuge, Schiffe und Flugzeuge | Gross- und Einzelhandel | Software- und Applikationsentwicklung u…
  - 同じ表の列：berufsnr, berufsbezeichnung, efz_eba, jahr, bildungsverh_m, bildungsverh_w, ausbildungsverh_ver…, ausbildungsverh_ver…

## g0077（1 列）
- 見出し：berufsbezeichnung
- 例1 値：Detailhandelsfachmann EFZ Beratung/Uhre… | Gebäudeinformatiker EFZ Gebäudeautomati… | Kaufmann EFZ Basis-Grundbildung Maschin… | Detailhandelsfachmann EFZ Beratung/Öffe… | Fachmann Information und Dokumentation …
  - 同じ表の列：berufsnr, isced, efz_eba, jahr, bildungsverh_m, bildungsverh_w, ausbildungsverh_ver…, ausbildungsverh_ver…

## g0078（1 列）
- 見出し：efz_eba
- 例1 値：EFZ | EFZ | EFZ | EFZ | EFZ
  - 同じ表の列：berufsnr, isced, berufsbezeichnung, jahr, bildungsverh_m, bildungsverh_w, ausbildungsverh_ver…, ausbildungsverh_ver…

## g0079（1 列）
- 見出し：bildungsverh_m
- 例1 値：29 | 1 | 0 | 0 | 22
  - 同じ表の列：berufsnr, isced, berufsbezeichnung, efz_eba, jahr, bildungsverh_w, ausbildungsverh_ver…, ausbildungsverh_ver…

## g0080（1 列）
- 見出し：bildungsverh_w
- 例1 値：0 | 1 | 0 | 0 | 7
  - 同じ表の列：berufsnr, isced, berufsbezeichnung, efz_eba, jahr, bildungsverh_m, ausbildungsverh_ver…, ausbildungsverh_ver…

## g0081（1 列）
- 見出し：ausbildungsverh_vertrag_m
- 例1 値：0 | 1 | 11 | 1 | 1
  - 同じ表の列：berufsnr, isced, berufsbezeichnung, efz_eba, jahr, bildungsverh_m, bildungsverh_w, ausbildungsverh_ver…

## g0082（1 列）
- 見出し：ausbildungsverh_vertrag_w
- 例1 値：0 | 0 | 0 | 0 | 1
  - 同じ表の列：berufsnr, isced, berufsbezeichnung, efz_eba, jahr, bildungsverh_m, bildungsverh_w, ausbildungsverh_ver…

## g0083（1 列）
- 見出し：repetent_m
- 例1 値：5 | 0 | 0 | 0 | 0
  - 同じ表の列：berufsnr, isced, berufsbezeichnung, efz_eba, jahr, bildungsverh_m, bildungsverh_w, ausbildungsverh_ver…

## g0084（2 列）
- 見出し：bfs_nr_gemeinde
- 例1 値：4591 | 4421 | 4611 | 4476 | 4666
  - 同じ表の列：jahr, gesamtsteuerfuss_ev…, gesamtsteuerfuss_ka…, gesamtsteuerfuss_ko…, gesamtsteuerfuss_jp
- 例2 値：4816 | 4571 | 4941 | 4806 | 4561
  - 同じ表の列：gemeinde, bezirk, bfs_nr_bezirk, jahr, bauzone, minimum, maximum, markt_ja_nein

## g0085（1 列）
- 見出し：gesamtsteuerfuss_evang
- 例1 値：283 | 278 | 294 | 288 | 244
  - 同じ表の列：bfs_nr_gemeinde, jahr, gesamtsteuerfuss_ka…, gesamtsteuerfuss_ko…, gesamtsteuerfuss_jp

## g0086（1 列）
- 見出し：gesamtsteuerfuss_kath
- 例1 値：239 | 287 | 279 | 271 | 226
  - 同じ表の列：bfs_nr_gemeinde, jahr, gesamtsteuerfuss_ev…, gesamtsteuerfuss_ko…, gesamtsteuerfuss_jp

## g0087（1 列）
- 見出し：gesamtsteuerfuss_konfessionslos
- 例1 値：252 | 244 | 201 | 273 | 249
  - 同じ表の列：bfs_nr_gemeinde, jahr, gesamtsteuerfuss_ev…, gesamtsteuerfuss_ka…, gesamtsteuerfuss_jp

## g0088（1 列）
- 見出し：gesamtsteuerfuss_jp
- 例1 値：280.0 | 285.2 | 283.8 | 293.3 | 268.8
  - 同じ表の列：bfs_nr_gemeinde, jahr, gesamtsteuerfuss_ev…, gesamtsteuerfuss_ka…, gesamtsteuerfuss_ko…

## g0089（1 列）
- 見出し：gemeinde
- 例1 値：Raperswilen | Rickenbach bei Wil | Hauptwil-Gottshaus | Bottighofen | Münchwilen
  - 同じ表の列：bfs_nr_gemeinde, bezirk, bfs_nr_bezirk, jahr, bauzone, minimum, maximum, markt_ja_nein

## g0090（1 列）
- 見出し：bezirk
- 例1 値：Weinfelden | Frauenfeld | Münchwilen | Weinfelden | Kreuzlingen
  - 同じ表の列：gemeinde, bfs_nr_gemeinde, bfs_nr_bezirk, jahr, bauzone, minimum, maximum, markt_ja_nein

## g0091（1 列）
- 見出し：bfs_nr_bezirk
- 例1 値：2013 | 2013 | 2013 | 2011 | 2011
  - 同じ表の列：gemeinde, bfs_nr_gemeinde, bezirk, jahr, bauzone, minimum, maximum, markt_ja_nein

## g0092（1 列）
- 見出し：bauzone
- 例1 値：3 MFH | 3 MFH | 4 EFH | 4 EFH | 4 EFH
  - 同じ表の列：gemeinde, bfs_nr_gemeinde, bezirk, bfs_nr_bezirk, jahr, minimum, maximum, markt_ja_nein

## g0093（1 列）
- 見出し：minimum
- 例1 値：425 | 80 | 65 | 80 | 160
  - 同じ表の列：gemeinde, bfs_nr_gemeinde, bezirk, bfs_nr_bezirk, jahr, bauzone, maximum, markt_ja_nein

## g0094（1 列）
- 見出し：maximum
- 例1 値：280 | 150 | 410 | 0 | 0
  - 同じ表の列：gemeinde, bfs_nr_gemeinde, bezirk, bfs_nr_bezirk, jahr, bauzone, minimum, markt_ja_nein

## g0095（1 列）
- 見出し：markt_ja_nein
- 例1 値：n | j | j | j | n
  - 同じ表の列：gemeinde, bfs_nr_gemeinde, bezirk, bfs_nr_bezirk, jahr, bauzone, minimum, maximum

## g0096（1 列）
- 見出し：periode
- 例1 値：1992/97 | 2013/18 | 1979/85 | 2013/18 | 2004/09
  - 同じ表の列：flugjahr, gemeinde, bfscode, flaechentyp, flaechentyp_detaill…, flaeche_hektar

## g0097（1 列）
- 見出し：flugjahr
- 例1 値：2007 | 2007 | 2016 | 2007 | 1994/96
  - 同じ表の列：periode, gemeinde, bfscode, flaechentyp, flaechentyp_detaill…, flaeche_hektar

## g0098（1 列）
- 見出し：gemeinde
- 例1 値：Menzingen | Neuheim | Menzingen | Zug | Oberägeri
  - 同じ表の列：periode, flugjahr, bfscode, flaechentyp, flaechentyp_detaill…, flaeche_hektar

## g0099（1 列）
- 見出し：bfscode
- 例1 値：1709 | 1711 | 1702 | 1706 | 1705
  - 同じ表の列：periode, flugjahr, gemeinde, flaechentyp, flaechentyp_detaill…, flaeche_hektar

## g0100（1 列）
- 見出し：flaechentyp
- 例1 値：Unproduktive Flächen | Bestockte Flächen | Unproduktive Flächen | Unproduktive Flächen | Unproduktive Flächen
  - 同じ表の列：periode, flugjahr, gemeinde, bfscode, flaechentyp_detaill…, flaeche_hektar

## g0101（1 列）
- 見出し：flaechentyp_detailliert
- 例1 値：Wald (ohne Gebüschwald) | Naturwiesen, Heimweiden | Vegetationslose Flächen | Gletscher, Firn | Gebäudeareal
  - 同じ表の列：periode, flugjahr, gemeinde, bfscode, flaechentyp, flaeche_hektar

## g0102（1 列）
- 見出し：flaeche_hektar
- 例1 値：22 | 69 | 333 | 3 | 3
  - 同じ表の列：periode, flugjahr, gemeinde, bfscode, flaechentyp, flaechentyp_detaill…

## g0103（3 列）
- 見出し：geom_code
- 例1 値：stadtkreis | stadtkreis | gemeinde | stadtkreis | stadtkreis
  - 同じ表の列：jahr, stadtkreis_bfs_nr, stadtkreis, global_grouping, global_group_nr, global_group_value, grouping, group_nr
- 例2 値：quartier | quartier | quartier | stadtkreis | quartier
  - 同じ表の列：jahr, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, hh_typ_nr, hh_typ, einheit_nr

## g0104（3 列）
- 見出し：stadtkreis_bfs_nr
- 例1 値：1 | 2 | 2 | 4 | 4
  - 同じ表の列：jahr, geom_code, stadtkreis, global_grouping, global_group_nr, global_group_value, grouping, group_nr
- 例2 値：3 | 7 | 6 | 3 | 2
  - 同じ表の列：jahr, geom_code, stadtkreis, quartier_bfs_nr, quartier, hh_typ_nr, hh_typ, einheit_nr

## g0105（1 列）
- 見出し：stadtkreis
- 例1 値：Oberwinterthur | Wülflingen | Oberwinterthur | Stadt | Seen
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, global_grouping, global_group_nr, global_group_value, grouping, group_nr

## g0106（1 列）
- 見出し：global_grouping
- 例1 値：haushalt_lebensphase | haushalt_lebensphase | haushalt_lebensphase | haushalt_lebensphase | haushalt_typ
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, global_group_nr, global_group_value, grouping, group_nr

## g0107（1 列）
- 見出し：global_group_nr
- 例1 値：3 | 4 | 3 | 2 | 2
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, global_grouping, global_group_value, grouping, group_nr

## g0108（1 列）
- 見出し：global_group_value
- 例1 値：Älterer Haushalt | Einpersonenhaushalt | Zweipersonenhaushalt | Junger Haushalt | Paarhaushalt mit Kind(ern)
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, global_grouping, global_group_nr, grouping, group_nr

## g0109（2 列）
- 見出し：grouping
- 例1 値：bauperiode | gebaeudetyp | bauperiode | gebaeudetyp | belegung
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, global_grouping, global_group_nr, global_group_value, group_nr
- 例2 値：altersklasse | altersklasse | altersklasse | altersklasse | distanz
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view_nr, bilanz_view

## g0110（2 列）
- 見出し：group_nr
- 例1 値：3 | 1 | 5 | 99 | 4
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, global_grouping, global_group_nr, global_group_value, grouping
- 例2 値：2 | 6 | 3 | 2 | 4
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view_nr, bilanz_view

## g0111（1 列）
- 見出し：group_value
- 例1 値：Weniger Zi. als Pers. | Einfamilienhaus | vor 1946 | 3+ Zi. mehr als Pers. | vor 1946
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, global_grouping, global_group_nr, global_group_value, grouping

## g0112（1 列）
- 見出し：stadtkreis
- 例1 値：Wülflingen | Töss | Wülflingen | Seen | Oberwinterthur
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, quartier_bfs_nr, quartier, hh_typ_nr, hh_typ, einheit_nr

## g0113（2 列）
- 見出し：quartier_bfs_nr
- 例1 値：420 | 330 | 110 | 680 | 240
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier, hh_typ_nr, hh_typ, einheit_nr
- 例2 値：260 | 210 | 250 | 140 | 230
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier, bilanz_view_nr, bilanz_view, grouping

## g0114（1 列）
- 見出し：quartier
- 例1 値：Oberseen | Lind | Blumenau | Neuburg | Büelwiesen
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, hh_typ_nr, hh_typ, einheit_nr

## g0115（1 列）
- 見出し：hh_typ_nr
- 例1 値：5 | 6 | 6 | 3 | 4
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, hh_typ, einheit_nr

## g0116（1 列）
- 見出し：hh_typ
- 例1 値：Einelternhaushalt | Zweipersonenhaushalt | Zweipersonenhaushalt | Sonstiger Mehrpersonenhaushalt | Zweipersonenhaushalt
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, hh_typ_nr, einheit_nr

## g0117（1 列）
- 見出し：einheit_nr
- 例1 値：1 | 2 | 1 | 2 | 1
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, hh_typ_nr, hh_typ

## g0118（1 列）
- 見出し：einheit
- 例1 値：pro Äquivalenzperson | pro Äquivalenzperson | pro Haushalt | pro Haushalt | pro Äquivalenzperson
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, hh_typ_nr, hh_typ

## g0119（1 列）
- 見出し：stadtkreis
- 例1 値：Stadt | Stadt | Seen | Stadt | Seen
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, quartier_bfs_nr, quartier, bilanz_view_nr, bilanz_view, grouping

## g0120（1 列）
- 見出し：quartier
- 例1 値：Altstadt | Waldegg | Heiligberg | Neuwiesen | Lind
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, bilanz_view_nr, bilanz_view, grouping

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
