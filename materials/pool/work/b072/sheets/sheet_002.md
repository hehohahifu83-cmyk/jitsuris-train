# ラベル用シート 002 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：einheit
- 例1 値：Veränderung ggü. Vorjahr in %, zu Preis… | In CHF, zu laufenden Preisen | In CHF, zu laufenden Preisen | In CHF, zu laufenden Preisen | In CHF, zu laufenden Preisen
  - 同じ表の列：modell_lauf, indikator, region, branche, jahr, wert

## g0122（1 列）
- 見出し：region
- 例1 値：Kanton Graubünden | Kanton Graubünden | Kanton Graubünden | Kanton Graubünden | Kanton Graubünden
  - 同じ表の列：modell_lauf, indikator, einheit, branche, jahr, wert

## g0123（1 列）
- 見出し：branche
- 例1 値：Energie- und Wasserversorgung [NOGA 35-… | Baugewerbe [NOGA 41-43] | Primärer Sektor [NOGA 01-03] | Sekundärer Sektor [NOGA 05-43] | Primärer Sektor [NOGA 01-03]
  - 同じ表の列：modell_lauf, indikator, einheit, region, jahr, wert

## g0124（1 列）
- 見出し：wert
- 例1 値：729578213.17411 | 0.70744559 | -18.80813287 | 1816973780.9259 | -0.25938989
  - 同じ表の列：modell_lauf, indikator, einheit, region, branche, jahr

## g0125（1 列）
- 見出し：gewicht_grp
- 例1 値：7 | 7 | 6 | 6 | 7
  - 同じ表の列：id, year, gewicht_label, alter_mutter_cd, alter_mutter_label, gestations_alter_grp, gestations_alter_la…, geburts_art

## g0126（1 列）
- 見出し：gewicht_label
- 例1 値：3000 bis 2499 Gramm | 3000 bis 2499 Gramm | 3500 bis 3999 Gramm | 2500 bis 2999 Gramm | 3500 bis 3999 Gramm
  - 同じ表の列：id, year, gewicht_grp, alter_mutter_cd, alter_mutter_label, gestations_alter_grp, gestations_alter_la…, geburts_art

## g0127（1 列）
- 見出し：alter_mutter_cd
- 例1 値：1 | 2 | 2 | 2 | 2
  - 同じ表の列：id, year, gewicht_grp, gewicht_label, alter_mutter_label, gestations_alter_grp, gestations_alter_la…, geburts_art

## g0128（1 列）
- 見出し：alter_mutter_label
- 例1 値：20- bis 29-jährig | 20- bis 29-jährig | 30- bis 39-jährig | 30- bis 39-jährig | 30- bis 39-jährig
  - 同じ表の列：id, year, gewicht_grp, gewicht_label, alter_mutter_cd, gestations_alter_grp, gestations_alter_la…, geburts_art

## g0129（1 列）
- 見出し：gestations_alter_grp
- 例1 値：9 | 9 | 9 | 9 | 9
  - 同じ表の列：id, year, gewicht_grp, gewicht_label, alter_mutter_cd, alter_mutter_label, gestations_alter_la…, geburts_art

## g0130（1 列）
- 見出し：gestations_alter_label
- 例1 値：unbekannt | unbekannt | unbekannt | unbekannt | unbekannt
  - 同じ表の列：id, year, gewicht_grp, gewicht_label, alter_mutter_cd, alter_mutter_label, gestations_alter_grp, geburts_art

## g0131（1 列）
- 見出し：geburts_art
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：id, year, gewicht_grp, gewicht_label, alter_mutter_cd, alter_mutter_label, gestations_alter_grp, gestations_alter_la…

## g0132（1 列）
- 見出し：geburts_art_label
- 例1 値：Einzelgeburt | Einzelgeburt | Einzelgeburt | Einzelgeburt | Einzelgeburt
  - 同じ表の列：id, year, gewicht_grp, gewicht_label, alter_mutter_cd, alter_mutter_label, gestations_alter_grp, gestations_alter_la…

## g0133（1 列）
- 見出し：provider
- 例1 値：2 | 2 | 1 | 1 | 3
  - 同じ表の列：year, service, service_type, age_class, hours

## g0134（1 列）
- 見出し：service
- 例1 値：aup | klv | hwt | klv | klv
  - 同じ表の列：year, provider, service_type, age_class, hours

## g0135（1 列）
- 見出し：service_type
- 例1 値：b | c | a | a | b
  - 同じ表の列：year, provider, service, age_class, hours

## g0136（1 列）
- 見出し：age_class
- 例1 値：65-79 | 0-4 | 0-4 | 20-64 | 20-64
  - 同じ表の列：year, provider, service, service_type, hours

## g0137（1 列）
- 見出し：hours
- 例1 値：0 | 0 | 42294 | 303 | 3144
  - 同じ表の列：year, provider, service, service_type, age_class

## g0138（1 列）
- 見出し：Verkehrsmittel
- 例1 値：Bus | Bahn | Bahn | Bahn | Bus
  - 同じ表の列：Jahr, Fahrplanfeld, Kürzel Transportunt…, Kurspaare Mo-Fr, Kurspaare Sa, Kurspaare So, Angebotsstufe Code, Angebotsstufe Label

## g0139（1 列）
- 見出し：Fahrplanfeld
- 例1 値：80.701 | 80.331 | 80.792 (m.Bund) | 735 | 855
  - 同じ表の列：Jahr, Verkehrsmittel, Kürzel Transportunt…, Kurspaare Mo-Fr, Kurspaare Sa, Kurspaare So, Angebotsstufe Code, Angebotsstufe Label

## g0140（1 列）
- 見出し：Kürzel Transportunternehmen
- 例1 値：Thurbo | PAG OS | PAG OS | VBSG | BOS
  - 同じ表の列：Jahr, Verkehrsmittel, Fahrplanfeld, Kurspaare Mo-Fr, Kurspaare Sa, Kurspaare So, Angebotsstufe Code, Angebotsstufe Label

## g0141（1 列）
- 見出し：Kurspaare Mo-Fr
- 例1 値：3.0 | 37.0 | 49.5 | 2.5 | 6.0
  - 同じ表の列：Jahr, Verkehrsmittel, Fahrplanfeld, Kürzel Transportunt…, Kurspaare Sa, Kurspaare So, Angebotsstufe Code, Angebotsstufe Label

## g0142（1 列）
- 見出し：Kurspaare Sa
- 例1 値：8.0 | 30.0 | 0.0 | 2.0 | 8.0
  - 同じ表の列：Jahr, Verkehrsmittel, Fahrplanfeld, Kürzel Transportunt…, Kurspaare Mo-Fr, Kurspaare So, Angebotsstufe Code, Angebotsstufe Label

## g0143（1 列）
- 見出し：Kurspaare So
- 例1 値：19.0 | 17.0 | 9.0 | 31.0 | 38.0
  - 同じ表の列：Jahr, Verkehrsmittel, Fahrplanfeld, Kürzel Transportunt…, Kurspaare Mo-Fr, Kurspaare Sa, Angebotsstufe Code, Angebotsstufe Label

## g0144（1 列）
- 見出し：Angebotsstufe Code
- 例1 値：2 | 3 | 1 | 1 | 3
  - 同じ表の列：Jahr, Verkehrsmittel, Fahrplanfeld, Kürzel Transportunt…, Kurspaare Mo-Fr, Kurspaare Sa, Kurspaare So, Angebotsstufe Label

## g0145（1 列）
- 見出し：Angebotsstufe Label
- 例1 値：15 bis 29 Kurspaare pro Tag (Stundentak… | Grundversorgung bis 14 Kurspaare pro Ta… | Grundversorgung bis 14 Kurspaare pro Ta… | 30 bis 59 Kurspaare pro Tag (Halbstunde… | 15 bis 29 Kurspaare pro Tag (Stundentak…
  - 同じ表の列：Jahr, Verkehrsmittel, Fahrplanfeld, Kürzel Transportunt…, Kurspaare Mo-Fr, Kurspaare Sa, Kurspaare So, Angebotsstufe Code

## g0146（1 列）
- 見出し：Kurskilometer
- 例1 値：180164 | 179477 | 1869 | 917011 | 224098
  - 同じ表の列：Jahr, Verkehrsmittel, Fahrplanfeld, Kürzel Transportunt…, Kurspaare Mo-Fr, Kurspaare Sa, Kurspaare So, Angebotsstufe Code

## g0147（1 列）
- 見出し：available_spots
- 例1 値：18 | 102 | 91 | 42 | 102
  - 同じ表の列：deactivated_spots, occupied_spots, timestamp, total_spots, visualplan_id, koordinaten

## g0148（1 列）
- 見出し：deactivated_spots
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：available_spots, occupied_spots, timestamp, total_spots, visualplan_id, koordinaten

## g0149（1 列）
- 見出し：occupied_spots
- 例1 値：40 | 100 | 9 | 152 | 21
  - 同じ表の列：available_spots, deactivated_spots, timestamp, total_spots, visualplan_id, koordinaten

## g0150（1 列）
- 見出し：timestamp
- 例1 値：2026-10-30T13:13:50+00:00 | 2026-10-30T11:08:49+00:00 | 2026-10-30T08:33:47+00:00 | 2026-10-30T09:18:48+00:00 | 2026-10-30T06:48:46+00:00
  - 同じ表の列：available_spots, deactivated_spots, occupied_spots, total_spots, visualplan_id, koordinaten

## g0151（1 列）
- 見出し：total_spots
- 例1 値：114 | 30 | 62 | 9 | 114
  - 同じ表の列：available_spots, deactivated_spots, occupied_spots, timestamp, visualplan_id, koordinaten

## g0152（1 列）
- 見出し：visualplan_id
- 例1 値：5 | 4 | 2 | 7 | 5
  - 同じ表の列：available_spots, deactivated_spots, occupied_spots, timestamp, total_spots, koordinaten

## g0153（1 列）
- 見出し：koordinaten
- 例1 値：47.556630166103474, 8.898067598769348 | 47.559405799496446, 8.899641893040318 | 47.556630166103474, 8.898067598769348 | 47.559405799496446, 8.899641893040318 | 47.553895843115285, 8.899802852674002
  - 同じ表の列：available_spots, deactivated_spots, occupied_spots, timestamp, total_spots, visualplan_id

## g0154（1 列）
- 見出し：nr
- 例1 値：117 | 200 | 324 | 244 | 65
  - 同じ表の列：ort, partei, geschaeftstitel, geschaeftsnummer, erstunterzeichner

## g0155（1 列）
- 見出し：ort
- 例1 値：Frauenfeld | Mammern | Eschlikon | Weinfelden | Frauenfeld
  - 同じ表の列：nr, partei, geschaeftstitel, geschaeftsnummer, erstunterzeichner

## g0156（1 列）
- 見出し：partei
- 例1 値：CVP | SVP | FDP | SP | SP
  - 同じ表の列：nr, ort, geschaeftstitel, geschaeftsnummer, erstunterzeichner

## g0157（1 列）
- 見出し：geschaeftstitel
- 例1 値：Motion von Christian Caviezel, Beat Stu… | Motion von Bruno Lüscher, Gallus Müller… | Einfache Anfrage von Oliver Martin, Pau… | Einfache Anfrage von Edith Wohlfender-O… | Interpellation von Turi Schallenberg, K…
  - 同じ表の列：nr, ort, partei, geschaeftsnummer, erstunterzeichner

## g0158（1 列）
- 見出し：geschaeftsnummer
- 例1 値：08/MO 56/422 | 16/EA 7/42 | 24/EA 20/67 | 08/AN 7/166 | 08/MO 34/254
  - 同じ表の列：nr, ort, partei, geschaeftstitel, erstunterzeichner

## g0159（1 列）
- 見出し：erstunterzeichner
- 例1 値：ja | ja | ja | ja | nein
  - 同じ表の列：nr, ort, partei, geschaeftstitel, geschaeftsnummer

## g0160（1 列）
- 見出し：bfs_nr_gemeinde
- 例1 値：4546 | 4821 | 4551 | 4821 | 4551
  - 同じ表の列：jahr, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, zimmer_anzahl, flaechenkategorie

## g0161（1 列）
- 見出し：gebaeudekategorie_code
- 例1 値：1030 | 1021 | 1030 | 1025 | 1021
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, zimmer_anzahl, flaechenkategorie

## g0162（1 列）
- 見出し：gebaeudekategorie
- 例1 値：Mehrfamilienhäuser | Wohngebäude mit Nebennutzung | Einfamilienhäuser | Gebäude mit teilweiser Wohnnutzung | Einfamilienhäuser
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, bauperiode_code, bauperiode, geschosse_anzahl, zimmer_anzahl, flaechenkategorie

## g0163（1 列）
- 見出し：bauperiode_code
- 例1 値：8022 | 8018 | 8017 | 8013 | 8018
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode, geschosse_anzahl, zimmer_anzahl, flaechenkategorie

## g0164（1 列）
- 見出し：bauperiode
- 例1 値：Periode vor 1919 | Periode von 1971 bis 1980 | Periode vor 1919 | Periode von 1919 bis 1945 | Periode vor 1919
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, geschosse_anzahl, zimmer_anzahl, flaechenkategorie

## g0165（1 列）
- 見出し：geschosse_anzahl
- 例1 値：3 | 2 | 2 | 2 | 4
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, zimmer_anzahl, flaechenkategorie

## g0166（1 列）
- 見出し：zimmer_anzahl
- 例1 値：8 | 6 | 4 | 6 | 5
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, flaechenkategorie

## g0167（1 列）
- 見出し：flaechenkategorie
- 例1 値：100-149 m2 | 100-149 m2 | 100-149 m2 | 150+ m2 | 70-99 m2
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, zimmer_anzahl

## g0168（1 列）
- 見出し：anzahl
- 例1 値：3 | 1 | 2 | 1 | 1
  - 同じ表の列：jahr, bfs_nr_gemeinde, gebaeudekategorie_c…, gebaeudekategorie, bauperiode_code, bauperiode, geschosse_anzahl, zimmer_anzahl

## g0169（1 列）
- 見出し：periode
- 例1 値：1992/97 | 2004/09 | 1979/85 | 2013/18 | 2004/09
  - 同じ表の列：flugjahr, gemeinde, bfscode, flaechentyp, flaechentyp_detaill…, flaeche_hektar

## g0170（1 列）
- 見出し：flugjahr
- 例1 値：1982/83 | 1994/96 | 2007 | 1982/83 | 2016
  - 同じ表の列：periode, gemeinde, bfscode, flaechentyp, flaechentyp_detaill…, flaeche_hektar

## g0171（1 列）
- 見出し：gemeinde
- 例1 値：Oberägeri | Risch | Steinhausen | Hünenberg | Risch
  - 同じ表の列：periode, flugjahr, bfscode, flaechentyp, flaechentyp_detaill…, flaeche_hektar

## g0172（1 列）
- 見出し：bfscode
- 例1 値：1704 | 1706 | 1701 | 1704 | 1705
  - 同じ表の列：periode, flugjahr, gemeinde, flaechentyp, flaechentyp_detaill…, flaeche_hektar

## g0173（1 列）
- 見出し：flaechentyp
- 例1 値：Bestockte Flächen | Siedlungsflächen | Landwirtschaftsflächen | Landwirtschaftsflächen | Unproduktive Flächen
  - 同じ表の列：periode, flugjahr, gemeinde, bfscode, flaechentyp_detaill…, flaeche_hektar

## g0174（1 列）
- 見出し：flaechentyp_detailliert
- 例1 値：Alpwirtschaftsflächen | Unproduktive Vegetation | Ackerland | Ackerland | Wald (ohne Gebüschwald)
  - 同じ表の列：periode, flugjahr, gemeinde, bfscode, flaechentyp, flaeche_hektar

## g0175（1 列）
- 見出し：flaeche_hektar
- 例1 値：31 | 26 | 81 | 45 | 143
  - 同じ表の列：periode, flugjahr, gemeinde, bfscode, flaechentyp, flaechentyp_detaill…

## g0176（1 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:75257:0:159986 | ch:1:sloid:78780:0:166771 | ch:1:sloid:7785:0:233351 | ch:1:sloid:75119:0:397731 | ch:1:sloid:78259:1:50
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0177（3 列）
- 見出し：parentSloidServicePoint
- 例1 値：ch:1:sloid:83860 | ch:1:sloid:82467 | ch:1:sloid:73523 | ch:1:sloid:91805 | ch:1:sloid:87848
  - 同じ表の列：sloid, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height
- 例2 値：ch:1:sloid:8058 | ch:1:sloid:6290 | ch:1:sloid:4225 | ch:1:sloid:3078 | ch:1:sloid:4134
  - 同じ表の列：sloid, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom, validTo

## g0178（3 列）
- 見出し：parentNumberServicePoint
- 例1 値：8578259 | 8504305 | 8507781 | 8503560 | 8588885
  - 同じ表の列：sloid, parentSloidServiceP…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height
- 例2 値：8504321 | 8506209 | 8502270 | 8506377 | 8503282
  - 同じ表の列：sloid, parentSloidServiceP…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom, validTo

## g0179（1 列）
- 見出し：boardingDevice
- 例1 値：NO | NOT_APPLICABLE | LIFTS | NO | NO
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0180（1 列）
- 見出し：shuttle
- 例1 値：NO | NO | NO | TO_BE_COMPLETED | NO
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0181（1 列）
- 見出し：contrastingAreas
- 例1 値：YES | NO | NO | NO | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, dynamicAudio, dynamicVisual, height

## g0182（1 列）
- 見出し：dynamicAudio
- 例1 値：YES | NO | YES | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicVisual, height

## g0183（1 列）
- 見出し：dynamicVisual
- 例1 値：YES | YES | YES | NO | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, height

## g0184（1 列）
- 見出し：height
- 例1 値：22.0 | 8.0 | 16.0 | 22.0 | 12.0
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual

## g0185（1 列）
- 見出し：inclination
- 例1 値：2.0 | 2.0 | 2.0 | 2.0 | -2.0
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual

## g0186（1 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:3061:238986 | ch:1:sloid:1362:201051 | ch:1:sloid:7552:56468 | ch:1:sloid:8317:946324 | ch:1:sloid:8301:638695
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom, validTo

## g0187（1 列）
- 見出し：designation
- 例1 値：Hauptzugang | Haupteingang | Hauptzugang | Bahnzugang | Hauptzugang
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, mainReferencePoint, additionalInformati…, referencePointType, validFrom, validTo

## g0188（1 列）
- 見出し：mainReferencePoint
- 例1 値：true | true | true | true | true
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, referencePointType, validFrom, validTo

## g0189（1 列）
- 見出し：additionalInformation
- 例1 値：Der Referenzpunkt befindet sich beim Ha… | Gedeckter Kundencenterbereich Bahnhofpl… | Zugang auf das Perron auf der linken Se… | Der Hauptzugang befindet sich auf dem H… | accès par les escaliers qui sont devant…
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, referencePointType, validFrom, validTo

## g0190（1 列）
- 見出し：referencePointType
- 例1 値：PLATFORM | PLATFORM | MAIN_STATION_ENTRANCE | MAIN_STATION_ENTRANCE | MAIN_STATION_ENTRANCE
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, validFrom, validTo

## g0191（2 列）
- 見出し：validFrom
- 例1 値：2023-09-12T00:00:00 | 2021-07-21T00:00:00 | 2021-12-22T00:00:00 | 2021-07-21T00:00:00 | 2021-07-21T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validTo
- 例2 値：2021-07-21T00:00:00 | 2021-07-21T00:00:00 | 2023-11-28T00:00:00 | 2023-09-12T00:00:00 | 2023-09-12T00:00:00
  - 同じ表の列：elementSloid, parentSloidServiceP…, parentNumberService…, referencePointSloid, tactileVisualMarks, contrastingAreas, stepFreeAccess, referencePointEleme…

## g0192（2 列）
- 見出し：validTo
- 例1 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom
- 例2 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：elementSloid, parentSloidServiceP…, parentNumberService…, referencePointSloid, tactileVisualMarks, contrastingAreas, stepFreeAccess, referencePointEleme…

## g0193（1 列）
- 見出し：creationDate
- 例1 値：2022-07-13T05:39:34 | 2022-07-28T13:55:34 | 2020-08-25T08:53:29 | 2023-12-19T21:10:10 | 2023-04-20T14:05:55
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom

## g0194（1 列）
- 見出し：elementSloid
- 例1 値：ch:1:sloid:6128:758331 | ch:1:sloid:7270:0:859564 | ch:1:sloid:5373::02 | ch:1:sloid:7069:53857 | ch:1:sloid:8321:0:886771
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, referencePointSloid, tactileVisualMarks, contrastingAreas, stepFreeAccess, referencePointEleme…, validFrom

## g0195（1 列）
- 見出し：referencePointSloid
- 例1 値：ch:1:sloid:8217:726728 | ch:1:sloid:1172:452798 | ch:1:sloid:186:719552 | ch:1:sloid:9060:86031 | ch:1:sloid:4070:206844
  - 同じ表の列：elementSloid, parentSloidServiceP…, parentNumberService…, tactileVisualMarks, contrastingAreas, stepFreeAccess, referencePointEleme…, validFrom

## g0196（1 列）
- 見出し：tactileVisualMarks
- 例1 値：NOT_APPLICABLE | YES | YES | NO | YES
  - 同じ表の列：elementSloid, parentSloidServiceP…, parentNumberService…, referencePointSloid, contrastingAreas, stepFreeAccess, referencePointEleme…, validFrom

## g0197（1 列）
- 見出し：contrastingAreas
- 例1 値：NO | NOT_APPLICABLE | NOT_APPLICABLE | NO | NOT_APPLICABLE
  - 同じ表の列：elementSloid, parentSloidServiceP…, parentNumberService…, referencePointSloid, tactileVisualMarks, stepFreeAccess, referencePointEleme…, validFrom

## g0198（1 列）
- 見出し：stepFreeAccess
- 例1 値：TO_BE_COMPLETED | YES | YES_WITH_LIFT | YES_WITH_RAMP | YES_WITH_RAMP
  - 同じ表の列：elementSloid, parentSloidServiceP…, parentNumberService…, referencePointSloid, tactileVisualMarks, contrastingAreas, referencePointEleme…, validFrom

## g0199（1 列）
- 見出し：referencePointElementType
- 例1 値：PLATFORM | PARKING_LOT | TOILET | PLATFORM | PLATFORM
  - 同じ表の列：elementSloid, parentSloidServiceP…, parentNumberService…, referencePointSloid, tactileVisualMarks, contrastingAreas, stepFreeAccess, validFrom

## g0200（1 列）
- 見出し：Signatur
- 例1 値：EAD-6833 | EAD-7399 | EAD-6902 | EAD-6807 | EAD-7200
  - 同じ表の列：ID, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Farbe, Orientierung_Form

## g0201（1 列）
- 見出し：FotografIn
- 例1 値：Berchem, Max van | Berchem, Max van | Berchem, Max van | Berchem, Max van | Berchem, Max van
  - 同じ表の列：ID, Signatur, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Farbe, Orientierung_Form

## g0202（1 列）
- 見出し：Titel
- 例1 値：Bern, Haus, vue partielle extérieure | Fribourg, Maison, vue partielle extérie… | Payerne, Temple, vue partielle | Fribourg, Chapelle, vue d'ensemble exté… | Rheinfelden, Brücke, vue partielle
  - 同じ表の列：ID, Signatur, FotografIn, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Farbe, Orientierung_Form

## g0203（1 列）
- 見出し：Inhalt_Kurzbeschreibung
- 例1 値：Vue partielle d'une maison et du jardin… | Vue d'ensemble de la fontaine de Moïse … | Vue d'une maison à Lucens | Vue partielle de l'imposant porche d'en… | Vue d'ensemble extérieure d'un portail …
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Datierung_von, Datierung_bis, Farbe, Orientierung_Form

## g0204（1 列）
- 見出し：Datierung_von
- 例1 値：1898 | 190204 | 1899 | 1900 | 1901
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_bis, Farbe, Orientierung_Form

## g0205（1 列）
- 見出し：Datierung_bis
- 例1 値：1907 | 1907 | 1907 | 1907 | 1907
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Farbe, Orientierung_Form

## g0206（1 列）
- 見出し：Farbe
- 例1 値：S/W | S/W | S/W | S/W | S/W
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Orientierung_Form

## g0207（1 列）
- 見出し：Orientierung_Form
- 例1 値：Vertikal | Vertikal | Horizontal | Vertikal | Vertikal
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Farbe

## g0208（1 列）
- 見出し：Archivatlenart
- 例1 値：Fotografie | Fotografie | Fotografie | Fotografie | Fotografie
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Farbe

## g0209（1 列）
- 見出し：objectid
- 例1 値：2 | 33 | 10 | 20 | 16
  - 同じ表の列：leistung_in_kwp, modultyp, leistung_modul_in_wp, anzahl_module, wechselrichterleist…, flache, link, geo_point_2d

## g0210（1 列）
- 見出し：leistung_in_kwp
- 例1 値：54.76 | 36.18 | 141.9 | 169.6 | 6.48
  - 同じ表の列：objectid, modultyp, leistung_modul_in_wp, anzahl_module, wechselrichterleist…, flache, link, geo_point_2d

## g0211（1 列）
- 見出し：modultyp
- 例1 値：HareonHR-260-18/Bb poly | SunTech HyPro STP 325S | Axitec Axipremium X HC BLK | Trina Solar-400DE | SunTech HyPro STP 300S,SunTech HyPro ST…
  - 同じ表の列：objectid, leistung_in_kwp, leistung_modul_in_wp, anzahl_module, wechselrichterleist…, flache, link, geo_point_2d

## g0212（1 列）
- 見出し：leistung_modul_in_wp
- 例1 値：300 | 300 | 255 | 230,260 | 205
  - 同じ表の列：objectid, leistung_in_kwp, modultyp, anzahl_module, wechselrichterleist…, flache, link, geo_point_2d

## g0213（1 列）
- 見出し：anzahl_module
- 例1 値：3096 | 134 | 324 | 132 | 2436
  - 同じ表の列：objectid, leistung_in_kwp, modultyp, leistung_modul_in_wp, wechselrichterleist…, flache, link, geo_point_2d

## g0214（1 列）
- 見出し：wechselrichterleistung_kva
- 例1 値：127.0 | 55.2 | 838.0 | 26.8 | 10.0
  - 同じ表の列：objectid, leistung_in_kwp, modultyp, leistung_modul_in_wp, anzahl_module, flache, link, geo_point_2d

## g0215（1 列）
- 見出し：flache
- 例1 値：904 | 250 | 848 | 66 | 970
  - 同じ表の列：objectid, leistung_in_kwp, modultyp, leistung_modul_in_wp, anzahl_module, wechselrichterleist…, link, geo_point_2d

## g0216（1 列）
- 見出し：link
- 例1 値：https://sgsw.solarlog-web.ch/61003.html | noch nicht vorhanden | https://sgsw.solarlog-web.ch/62694.html | https://sgsw.solarlog-web.ch/40750.html | https://sgsw.solarlog-web.ch/40555.html
  - 同じ表の列：objectid, leistung_in_kwp, modultyp, leistung_modul_in_wp, anzahl_module, wechselrichterleist…, flache, geo_point_2d

## g0217（2 列）
- 見出し：geo_point_2d
- 例1 値：47.4049134337, 9.29446568632 | 47.406975942, 9.31446183282 | 47.4062257789, 9.30458367365 | 47.4299300326, 9.39611228046 | 47.44135, 9.4102
  - 同じ表の列：objectid, leistung_in_kwp, modultyp, leistung_modul_in_wp, anzahl_module, wechselrichterleist…, flache, link
- 例2 値：47.41209608066285, 9.33591068841119 | 47.41209608066285, 9.33591068841119 | 47.41209608066285, 9.33591068841119 | 47.439195139754474, 9.406626586373676 | 47.43919901794274, 9.406667805210304
  - 同じ表の列：measured_at_new, measured_at, data, device_id, location, data_distance

## g0218（1 列）
- 見出し：geo_shape
- 例1 値：{"coordinates":[[[9.3649,47.4183],[9.36… | NA | {"coordinates":[[[9.3495,47.4169],[9.34… | NA | NA
  - 同じ表の列：objectid, leistung_in_kwp, modultyp, leistung_modul_in_wp, anzahl_module, wechselrichterleist…, flache, link

## g0219（1 列）
- 見出し：Gemeinde
- 例1 値：Rehetobel | Wolfhalden | Schönengrund | Andwil (SG) | Waldstatt
  - 同じ表の列：Gemeinde Code, Kanton, Kanton Code, Geo Point, Geo Shape

## g0220（1 列）
- 見出し：Gemeinde Code
- 例1 値：3022 | 3214 | 4421 | 3006 | 3102
  - 同じ表の列：Gemeinde, Kanton, Kanton Code, Geo Point, Geo Shape

## g0221（1 列）
- 見出し：Kanton
- 例1 値：St. Gallen | Appenzell Ausserrhoden | Appenzell Ausserrhoden | St. Gallen | Appenzell Ausserrhoden
  - 同じ表の列：Gemeinde, Gemeinde Code, Kanton Code, Geo Point, Geo Shape

## g0222（1 列）
- 見出し：Kanton Code
- 例1 値：15 | 15 | 17 | 15 | 15
  - 同じ表の列：Gemeinde, Gemeinde Code, Kanton, Geo Point, Geo Shape

## g0223（1 列）
- 見出し：Geo Shape
- 例1 値：{"coordinates": [[[[9.3538638087, 47.51… | {"coordinates": [[[9.5112303051, 47.479… | {"coordinates": [[[9.3620027467, 47.445… | {"coordinates": [[[9.5107224871, 47.402… | {"coordinates": [[[9.3253480149, 47.400…
  - 同じ表の列：Gemeinde, Gemeinde Code, Kanton, Kanton Code, Geo Point

## g0224（1 列）
- 見出し：measured_at_new
- 例1 値：2024-08-09T18:00:00.057000+00:00 | 2024-08-21T03:00:00.060000+00:00 | 2024-07-14T16:00:01.855000+00:00 | 2024-07-17T10:00:00.184000+00:00 | 2024-07-25T09:00:08.061000+00:00
  - 同じ表の列：measured_at, data, device_id, location, data_distance, geo_point_2d

## g0225（1 列）
- 見出し：measured_at
- 例1 値：1723010401.69 | 1724457600.055 | 1725537600.068 | 1720990800.522 | 1723046400.043
  - 同じ表の列：measured_at_new, data, device_id, location, data_distance, geo_point_2d

## g0226（1 列）
- 見出し：data
- 例1 値：{"distance": 1354} | {"distance": 602} | {"distance": 1354} | {"distance": 1075} | {"distance": 1010}
  - 同じ表の列：measured_at_new, measured_at, device_id, location, data_distance, geo_point_2d

## g0227（1 列）
- 見出し：device_id
- 例1 値：6d43f154-1009-470a-95a2-f40fe4b8a204 | a1f343aa-dbbd-4b7e-ac42-58ee4bfffd06 | 827fd8d9-b94a-414c-aa38-0bb6d7880527 | 6d43f154-1009-470a-95a2-f40fe4b8a204 | 6d43f154-1009-470a-95a2-f40fe4b8a204
  - 同じ表の列：measured_at_new, measured_at, data, location, data_distance, geo_point_2d

## g0228（1 列）
- 見出し：location
- 例1 値：{"coordinates": [9.406626586373676, 47.… | {"coordinates": [9.406626586373676, 47.… | {"coordinates": [9.33591068841119, 47.4… | {"coordinates": [9.33352525794038, 47.4… | {"coordinates": [9.406626586373676, 47.…
  - 同じ表の列：measured_at_new, measured_at, data, device_id, data_distance, geo_point_2d

## g0229（1 列）
- 見出し：data_distance
- 例1 値：1204.0 | 1354.0 | 1397.0 | 752.0 | 1333.0
  - 同じ表の列：measured_at_new, measured_at, data, device_id, location, geo_point_2d

## g0230（2 列）
- 見出し：stichtag
- 例1 値：2021-12-31 | 2025-12-31 | 2026-09-30 | 2023-12-31 | 2025-12-31
  - 同じ表の列：jahr, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier
- 例2 値：2022-12-31 | 2018-12-31 | 2022-12-31 | 2020-12-31 | 2020-12-31
  - 同じ表の列：jahr, monat, wissensstand_am, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis

## g0231（3 列）
- 見出し：geom_code
- 例1 値：stadtkreis | quartier | stadtkreis | quartier | quartier
  - 同じ表の列：jahr, stichtag, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier
- 例2 値：quartier | stadtkreis | quartier | quartier | stadtkreis
  - 同じ表の列：jahr, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view_nr, bilanz_view, grouping

## g0232（2 列）
- 見出し：gemeinde_bfs_nr
- 例1 値：230 | 230 | 230 | 230 | 230
  - 同じ表の列：jahr, stichtag, geom_code, gemeinde, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier
- 例2 値：230 | 230 | 230 | 230 | 230
  - 同じ表の列：jahr, monat, stichtag, wissensstand_am, geom_code, gemeinde, stadtkreis_bfs_nr, stadtkreis

## g0233（2 列）
- 見出し：gemeinde
- 例1 値：Winterthur | Winterthur | Winterthur | Winterthur | Winterthur
  - 同じ表の列：jahr, stichtag, geom_code, gemeinde_bfs_nr, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier
- 例2 値：Winterthur | Winterthur | Winterthur | Winterthur | Winterthur
  - 同じ表の列：jahr, monat, stichtag, wissensstand_am, geom_code, gemeinde_bfs_nr, stadtkreis_bfs_nr, stadtkreis

## g0234（3 列）
- 見出し：stadtkreis_bfs_nr
- 例1 値：2 | 5 | 7 | 1 | 1
  - 同じ表の列：jahr, stichtag, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis, quartier_bfs_nr, quartier
- 例2 値：4 | 2 | 3 | 5 | 1
  - 同じ表の列：jahr, geom_code, stadtkreis, quartier_bfs_nr, quartier, bilanz_view_nr, bilanz_view, grouping

## g0235（1 列）
- 見出し：stadtkreis
- 例1 値：Töss | Seen | Töss | Stadt | Töss
  - 同じ表の列：jahr, stichtag, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, quartier_bfs_nr, quartier

## g0236（3 列）
- 見出し：quartier_bfs_nr
- 例1 値：290 | 290 | 430 | 730 | 220
  - 同じ表の列：jahr, stichtag, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis, quartier
- 例2 値：315 | 140 | 390 | 315 | 710
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier, bilanz_view_nr, bilanz_view, grouping

## g0237（1 列）
- 見出し：quartier
- 例1 値：Deutweg | Niederfeld | Heiligberg | Iberg | Gutschick
  - 同じ表の列：jahr, stichtag, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr

## g0238（1 列）
- 見出し：bestand
- 例1 値：140 | 1694 | 226 | 52 | 89
  - 同じ表の列：jahr, stichtag, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr

## g0239（1 列）
- 見出し：stadtkreis
- 例1 値：Stadt | Seen | Seen | Wülflingen | Stadt
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, quartier_bfs_nr, quartier, bilanz_view_nr, bilanz_view, grouping

## g0240（1 列）
- 見出し：quartier
- 例1 値：Brühlberg | Schlosstal | Rosenberg | Endliker | Dättnau
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, bilanz_view_nr, bilanz_view, grouping

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
