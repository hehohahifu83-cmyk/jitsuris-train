# ラベル用シート 003 / 004

- LABEL_GUIDE v2.1 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：tarifstruktur
- 例1 値：SwissDRG-Basisfallpreis | Internistisch-onkologische Rehabilitati… | Jugendtarif | SwissDRG-Basisfallpreis | SwissDRG-Basisfallpreis
  - 同じ表の列：bereich, waehrung, referenztarif, gueltig_ab

## g0242（1 列）
- 見出し：waehrung
- 例1 値：CHF | CHF | CHF | CHF | CHF
  - 同じ表の列：bereich, tarifstruktur, referenztarif, gueltig_ab

## g0243（1 列）
- 見出し：referenztarif
- 例1 値：630 | 440 | 365 | 10150 | 9935
  - 同じ表の列：bereich, tarifstruktur, waehrung, gueltig_ab

## g0244（1 列）
- 見出し：gueltig_ab
- 例1 値：2022-01-01 | 2017-01-01 | 2017-01-01 | 2021-01-01 | 2019-02-01
  - 同じ表の列：bereich, tarifstruktur, waehrung, referenztarif

## g0245（1 列）
- 見出し：Abstimmungs ID
- 例1 値：3018 | 3725 | 3679 | 5339 | 6009
  - 同じ表の列：Abstimmungsgegensta…, Sitzungs ID, Sitzungstitel, Geschäfts ID, Geschäftsnummer, Geschäftsart ID, Geschäftsart, Abstimmungsdatum

## g0246（1 列）
- 見出し：Abstimmungsgegenstand
- 例1 値：Rückweisungsantrag SVP-Fraktion | Gesamtabstimmung | Eintreten | Rückweisungsantrag SP-GRÜ-Fraktion | Antrag der SP-GRÜ-Fraktion zu Art. 69 A…
  - 同じ表の列：Abstimmungs ID, Sitzungs ID, Sitzungstitel, Geschäfts ID, Geschäftsnummer, Geschäftsart ID, Geschäftsart, Abstimmungsdatum

## g0247（1 列）
- 見出し：Sitzungs ID
- 例1 値：18 | 64 | 90 | 19 | 8
  - 同じ表の列：Abstimmungs ID, Abstimmungsgegensta…, Sitzungstitel, Geschäfts ID, Geschäftsnummer, Geschäftsart ID, Geschäftsart, Abstimmungsdatum

## g0248（1 列）
- 見出し：Sitzungstitel
- 例1 値：Session des Kantonsrates vom 4. bis 7. … | Session des Kantonsrates vom 1. bis 3. … | Session des Kantonsrates vom 20. bis 22… | Session des Kantonsrates vom 16. bis 18… | Session des Kantonsrates vom 4. bis 7. …
  - 同じ表の列：Abstimmungs ID, Abstimmungsgegensta…, Sitzungs ID, Geschäfts ID, Geschäftsnummer, Geschäftsart ID, Geschäftsart, Abstimmungsdatum

## g0249（1 列）
- 見出し：Geschäfts ID
- 例1 値：6285 | 2162 | 4453 | 76 | 4518
  - 同じ表の列：Abstimmungs ID, Abstimmungsgegensta…, Sitzungs ID, Sitzungstitel, Geschäftsnummer, Geschäftsart ID, Geschäftsart, Abstimmungsdatum

## g0250（1 列）
- 見出し：Geschäftsnummer
- 例1 値：42.12.03 | 33.13.09 | 36.08.01 | 42.11.08 | 40.22.01
  - 同じ表の列：Abstimmungs ID, Abstimmungsgegensta…, Sitzungs ID, Sitzungstitel, Geschäfts ID, Geschäftsart ID, Geschäftsart, Abstimmungsdatum

## g0251（1 列）
- 見出し：Geschäftsart ID
- 例1 値：11 | 6 | 4 | 9 | 4
  - 同じ表の列：Abstimmungs ID, Abstimmungsgegensta…, Sitzungs ID, Sitzungstitel, Geschäfts ID, Geschäftsnummer, Geschäftsart, Abstimmungsdatum

## g0252（1 列）
- 見出し：Geschäftsart
- 例1 値：KR Gesetzgebungsgeschäft | KR Motion | KR Verwaltungsgeschäft | KR Verwaltungsgeschäft | KR Gesetzgebungsgeschäft
  - 同じ表の列：Abstimmungs ID, Abstimmungsgegensta…, Sitzungs ID, Sitzungstitel, Geschäfts ID, Geschäftsnummer, Geschäftsart ID, Abstimmungsdatum

## g0253（1 列）
- 見出し：Abstimmungsdatum
- 例1 値：2025-12-02T14:59:54+00:00 | 2026-03-04T09:42:51+00:00 | 2012-06-05T11:41:21+00:00 | 2026-09-15T12:04:32+00:00 | 2006-11-28T10:11:54+00:00
  - 同じ表の列：Abstimmungs ID, Abstimmungsgegensta…, Sitzungs ID, Sitzungstitel, Geschäfts ID, Geschäftsnummer, Geschäftsart ID, Geschäftsart

## g0254（1 列）
- 見出し：can_be_published_to_web
- 例1 値：FALSE | FALSE | FALSE | FALSE | FALSE
  - 同じ表の列：Abstimmungs ID, Abstimmungsgegensta…, Sitzungs ID, Sitzungstitel, Geschäfts ID, Geschäftsnummer, Geschäftsart ID, Geschäftsart

## g0255（1 列）
- 見出し：bfsnr
- 例1 値：3231 | 3443 | 3203 | 3293 | 3443
  - 同じ表の列：datum, gemeinde, altersklassen, teilgenommen, nicht_teilgenommen, stimmbeteiligung

## g0256（3 列）
- 見出し：gemeinde
- 例1 値：Schmerikon | Thal | Mels | Quarten | Uzwil
  - 同じ表の列：datum, bfsnr, altersklassen, teilgenommen, nicht_teilgenommen, stimmbeteiligung
- 例2 値：Langrickenbach | Frauenfeld | Arbon | Langrickenbach | Arbon
  - 同じ表の列：code, richtung, spur_code, reg_bus, datum, zeit_von, zeit_bis, jahr

## g0257（1 列）
- 見出し：altersklassen
- 例1 値：75+ | 55-64 | 45-54 | 65-74 | 55-64
  - 同じ表の列：datum, bfsnr, gemeinde, teilgenommen, nicht_teilgenommen, stimmbeteiligung

## g0258（1 列）
- 見出し：teilgenommen
- 例1 値：80 | 379 | 1361 | 27 | 181
  - 同じ表の列：datum, bfsnr, gemeinde, altersklassen, nicht_teilgenommen, stimmbeteiligung

## g0259（1 列）
- 見出し：nicht_teilgenommen
- 例1 値：57 | 195 | 77 | 365 | 264
  - 同じ表の列：datum, bfsnr, gemeinde, altersklassen, teilgenommen, stimmbeteiligung

## g0260（1 列）
- 見出し：stimmbeteiligung
- 例1 値：35.1 | 38.2 | 68.3 | 72.1 | 60.0
  - 同じ表の列：datum, bfsnr, gemeinde, altersklassen, teilgenommen, nicht_teilgenommen

## g0261（1 列）
- 見出し：verwaltungsebene
- 例1 値：municipal | district | municipal | federation | federation
  - 同じ表の列：datum, typ_code

## g0262（1 列）
- 見出し：typ_code
- 例1 値：1 | 1 | 2 | 1 | 1
  - 同じ表の列：datum, verwaltungsebene

## g0263（1 列）
- 見出し：doc_title
- 例1 値：Beantwortung vom 19.08.2025 (24/IN 6/51) | Wortlaut/Begründung vom 13.02.2013 (12/… | 1. Lesung vom 12.02.2014 | Wortlaut vom 01.07.2026 (24/PI 7/363) | Beantwortung vom 11.03.2025 (20/MO 59/6…
  - 同じ表の列：geschaeftstitel, geschaeftsnummer

## g0264（1 列）
- 見出し：geschaeftstitel
- 例1 値：Gesetz betreffend die Änderung des Gese… | Gesetz betreffend die Änderung des Gese… | Verordnung betreffend die Änderung der … | Interpellation von Martina Pfiffner Mül… | Beschluss betreffend Verzicht auf die A…
  - 同じ表の列：doc_title, geschaeftsnummer

## g0265（1 列）
- 見出し：geschaeftsnummer
- 例1 値：12/BS 29/283 | 12/BS 37/361 | 24/MO 26/181 | 20/EA 239/592 | 16/MO 28/282
  - 同じ表の列：doc_title, geschaeftstitel

## g0266（1 列）
- 見出し：obj_id
- 例1 値：27592042 | 17487042 | 17542042 | 8283042 | 8281042
  - 同じ表の列：parameter, einheit, gueltig_von, gueltig_bis, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…, verantwortlichkeit_…

## g0267（1 列）
- 見出し：parameter
- 例1 値：EL | Pegel | Wasserstand | Abfluss | Pegel kombiniert
  - 同じ表の列：obj_id, einheit, gueltig_von, gueltig_bis, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…, verantwortlichkeit_…

## g0268（1 列）
- 見出し：einheit
- 例1 値：mS/cm | m ü. M. | m | m | mS/cm
  - 同じ表の列：obj_id, parameter, gueltig_von, gueltig_bis, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…, verantwortlichkeit_…

## g0269（1 列）
- 見出し：gueltig_von
- 例1 値：1996-12-04 | 2017-02-02 | 2012-09-25 | 1000-01-01 | 1993-09-22
  - 同じ表の列：obj_id, parameter, einheit, gueltig_bis, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…, verantwortlichkeit_…

## g0270（1 列）
- 見出し：gueltig_bis
- 例1 値：2999-12-31 | 2015-09-29 | 2999-12-31 | 2999-12-31 | 2999-12-31
  - 同じ表の列：obj_id, parameter, einheit, gueltig_von, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…, verantwortlichkeit_…

## g0271（1 列）
- 見出し：qualitaet
- 例1 値：Messgenauigkeit: +/- 0.1 °C | Ablesegenauigkeit: +/- 1 cm | Messgenauigkeit: +/- 0.1 °C | Ablesegenauigkeit: +/- 1 cm | Messgenauigkeit: +/- 0.1 °C
  - 同じ表の列：obj_id, parameter, einheit, gueltig_von, gueltig_bis, verantwortlichkeit_…, verantwortlichkeit_…, verantwortlichkeit_…

## g0272（1 列）
- 見出し：verantwortlichkeit_organisation
- 例1 値：Kanton Thurgau Amt für Umwelt | Kanton Thurgau Amt für Umwelt | Trinkwasserversorger | Kanton Thurgau Amt für Umwelt | Kanton Thurgau Amt für Umwelt
  - 同じ表の列：obj_id, parameter, einheit, gueltig_von, gueltig_bis, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…

## g0273（1 列）
- 見出し：verantwortlichkeit_abkuerzung
- 例1 値：KTTGWH | KTTGWH | KTTGWH | BAFU | KTTGWH
  - 同じ表の列：obj_id, parameter, einheit, gueltig_von, gueltig_bis, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…

## g0274（1 列）
- 見出し：verantwortlichkeit_abteilung
- 例1 値：Amt für Umwelt Fachstelle Hydrometrie | Amt für Umwelt Fachstelle Hydrometrie | Amt für Umwelt Fachstelle Hydrometrie | Amt für Umwelt Fachstelle Hydrometrie | Amt für Umwelt Fachstelle Hydrometrie
  - 同じ表の列：obj_id, parameter, einheit, gueltig_von, gueltig_bis, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…

## g0275（1 列）
- 見出し：messgruppierung_ortsbezeichnung
- 例1 値：Feldhof Weinfelden | Frauenfeld Tuchschmid | Salmsacher Aach Hefenhofen NAWA GQ | Glatt Herisau | Allmend A2
  - 同じ表の列：obj_id, parameter, einheit, gueltig_von, gueltig_bis, qualitaet, verantwortlichkeit_…, verantwortlichkeit_…

## g0276（1 列）
- 見出し：code
- 例1 値：428 | 414 | 523 | 529 | 426
  - 同じ表の列：gemeinde, richtung, spur_code, reg_bus, datum, zeit_von, zeit_bis, jahr

## g0277（1 列）
- 見出し：richtung
- 例1 値：nach Kreuzlingen | nach Schaffhausen | nach Lengwil | nach Amlikon | nach Steinach
  - 同じ表の列：code, gemeinde, spur_code, reg_bus, datum, zeit_von, zeit_bis, jahr

## g0278（1 列）
- 見出し：spur_code
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：code, gemeinde, richtung, reg_bus, datum, zeit_von, zeit_bis, jahr

## g0279（1 列）
- 見出し：reg_bus
- 例1 値：Nein | Nein | Nein | Nein | Nein
  - 同じ表の列：code, gemeinde, richtung, spur_code, datum, zeit_von, zeit_bis, jahr

## g0280（1 列）
- 見出し：zeit_von
- 例1 値：19:00 | 18:00 | 01:00 | 03:00 | 06:00
  - 同じ表の列：code, gemeinde, richtung, spur_code, reg_bus, datum, zeit_bis, jahr

## g0281（1 列）
- 見出し：zeit_bis
- 例1 値：11:00 | 02:00 | 20:00 | 20:00 | 20:00
  - 同じ表の列：code, gemeinde, richtung, spur_code, reg_bus, datum, zeit_von, jahr

## g0282（1 列）
- 見出し：monat
- 例1 値：10 | 10 | 10 | 10 | 10
  - 同じ表の列：code, gemeinde, richtung, spur_code, reg_bus, datum, zeit_von, zeit_bis

## g0283（1 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:8255:522578 | ch:1:sloid:4216:628163 | ch:1:sloid:3109:771298 | ch:1:sloid:15997:624671 | ch:1:sloid:3222:903755
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0284（3 列）
- 見出し：parentSloidServicePoint
- 例1 値：ch:1:sloid:8204 | ch:1:sloid:7087 | ch:1:sloid:7384 | ch:1:sloid:5064 | ch:1:sloid:30790
  - 同じ表の列：sloid, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo
- 例2 値：ch:1:sloid:1765 | ch:1:sloid:87135 | ch:1:sloid:88885 | ch:1:sloid:70450 | ch:1:sloid:82897
  - 同じ表の列：sloid, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0285（3 列）
- 見出し：parentNumberServicePoint
- 例1 値：8500267 | 8504298 | 8587727 | 8503461 | 8504412
  - 同じ表の列：sloid, parentSloidServiceP…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo
- 例2 値：8591269 | 8593272 | 8576021 | 8594361 | 8579615
  - 同じ表の列：sloid, parentSloidServiceP…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0286（1 列）
- 見出し：designation
- 例1 値：Places P+R | Parking | Parking | Parkplatz | Parkplätze
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0287（1 列）
- 見出し：additionalInformation
- 例1 値：55 / 2 Parkplätze (BehiG Parkplatz Seit… | 8 Parkplätze | 24 Parkplätze | 5 Parkplätze (Es sind mehr als 5 Parkpl… | Parkplätze vom Zeltpaltz benutzen ( Geb…
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0288（1 列）
- 見出し：placesAvailable
- 例1 値：YES | YES | YES | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, prmPlacesAvailable, validFrom, validTo

## g0289（1 列）
- 見出し：prmPlacesAvailable
- 例1 値：NO | YES | YES | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, validFrom, validTo

## g0290（2 列）
- 見出し：validFrom
- 例1 値：2023-08-22T00:00:00 | 2021-12-10T00:00:00 | 2023-09-07T00:00:00 | 2021-11-03T00:00:00 | 2022-04-14T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validTo
- 例2 値：2021-07-21T00:00:00 | 2021-10-04T00:00:00 | 2021-07-21T00:00:00 | 2023-09-12T00:00:00 | 2022-11-09T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validTo

## g0291（2 列）
- 見出し：validTo
- 例1 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom
- 例2 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom

## g0292（2 列）
- 見出し：creationDate
- 例1 値：2023-10-31T15:08:05 | 2024-02-05T12:00:59 | 2022-01-31T13:58:07 | 2023-11-06T08:39:30 | 2022-04-19T06:50:30
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom
- 例2 値：2022-04-13T18:57:40 | 2020-09-14T13:15:14 | 2022-07-11T04:35:53 | 2022-08-09T12:56:21 | 2022-07-11T08:58:33
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom

## g0293（1 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:91269::10 | ch:1:sloid:76021::50 | ch:1:sloid:5151:0:01 | ch:1:sloid:83599:0:375590 | ch:1:sloid:73985:0:158640
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0294（1 列）
- 見出し：boardingDevice
- 例1 値：NOT_APPLICABLE | LIFTS | NO | LIFTS | LIFTS
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0295（1 列）
- 見出し：shuttle
- 例1 値：YES | NO | YES | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0296（1 列）
- 見出し：contrastingAreas
- 例1 値：YES | YES | NO | YES | NO
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, dynamicAudio, dynamicVisual, height

## g0297（1 列）
- 見出し：dynamicAudio
- 例1 値：YES | YES | YES | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicVisual, height

## g0298（1 列）
- 見出し：dynamicVisual
- 例1 値：YES | YES | NO | YES | NO
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, height

## g0299（1 列）
- 見出し：height
- 例1 値：22.0 | 22.0 | 16.0 | 12.0 | 22.0
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual

## g0300（1 列）
- 見出し：inclination
- 例1 値：1.0 | 2.0 | 2.0 | 1.0 | 2.0
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual

## g0301（1 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:283:Haupteingang | ch:1:sloid:6280:2 | ch:1:sloid:2105:551361 | ch:1:sloid:6131:260356 | ch:1:sloid:8001:833771
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom, validTo

## g0302（1 列）
- 見出し：designation
- 例1 値：Halte d'Albeuve | Hauptzugang | Haupteingang | Point de référence principal | Hauptzugang
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, mainReferencePoint, additionalInformati…, referencePointType, validFrom, validTo

## g0303（1 列）
- 見出し：mainReferencePoint
- 例1 値：true | true | true | false | true
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, referencePointType, validFrom, validTo

## g0304（1 列）
- 見出し：additionalInformation
- 例1 値：Le point de référence se situe côté Nor… | Gedeckter Wartebereich | Überdachung Hauptzugang | Le point de référence se situe devant l… | Hausperron
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, referencePointType, validFrom, validTo

## g0305（1 列）
- 見出し：referencePointType
- 例1 値：MAIN_STATION_ENTRANCE | MAIN_STATION_ENTRANCE | MAIN_STATION_ENTRANCE | MAIN_STATION_ENTRANCE | MAIN_STATION_ENTRANCE
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, validFrom, validTo

## g0306（3 列）
- 見出し：ID
- 例1 値：1103127 | 1103306 | 1097848 | 1099841 | 1063549
  - 同じ表の列：Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Illustration
- 例2 値：1514943 | 1392785 | 1392226 | 1207822 | 1731187
  - 同じ表の列：Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe

## g0307（1 列）
- 見出し：Signatur
- 例1 値：SLA-Rhyn-03-x/01 | SLA-Rhyn-06-h/02 | SLA-Rhyn-09-b/01 | SLA-Rhyn-01-i/01 | SLA-Rhyn-04-e/01
  - 同じ表の列：ID, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Illustration

## g0308（1 列）
- 見出し：AutorIn
- 例1 値：Whittier, John Greenleaf | Joseph II. | Lannoy, Eugenio von | Volta, Alessandro | Mörike, Eduard
  - 同じ表の列：ID, Signatur, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Illustration

## g0309（1 列）
- 見出し：Titel
- 例1 値：Reinhart, Josef an Rhyn, Hans; Korrespo… | Wöhler, Friedrich an N.N. | Lumière, Louis an Strasser, Josef; Korr… | Schomburgk, Richard an Kaup, Johann Jak… | Kirchhoff, Gustav Robert an Quételet, A…
  - 同じ表の列：ID, Signatur, AutorIn, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Illustration

## g0310（1 列）
- 見出し：Ort
- 例1 値：Giessen | Wien | Stockholm / Riksmusei | s.l. | Potsdam
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Datierung_von, Datierung_bis, Datierung_Bemerkung, Illustration

## g0311（3 列）
- 見出し：Datierung_von
- 例1 値：18581020 | 19041028 | 19040104 | 18341004 | 18780902
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_bis, Datierung_Bemerkung, Illustration
- 例2 値：1906 | 1906 | 1905 | 1906 | 1905
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_bis, Datierung_Bemerkung, Farbe

## g0312（3 列）
- 見出し：Datierung_bis
- 例1 値：1841
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_Bemerkung, Illustration
- 例2 値：1934 | 1934 | 1934
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_Bemerkung, Farbe

## g0313（1 列）
- 見出し：Datierung_Bemerkung
- 例1 値：Poststempel | Entzifferung Jahr unsicher | Entzifferung unsicher | 2. Februar 18(?)3 | 9. Juni (?)
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Illustration

## g0314（1 列）
- 見出し：Illustration
- 例1 値：Text v. J.G. v. Herder; bezeugt v. sein… | recto: Windischleuba (s/w-Foto)
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0315（1 列）
- 見出し：Widmung
- 例1 値：'In segno di alta stima, e Considerazio…
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0316（1 列）
- 見出し：Signatur
- 例1 値：EAD-WEHR-2667-B | EAD-WEHR-1852-B | EAD-WEHR-2186-B | EAD-WEHR-2338-B | EAD-WEHR-1653b-B
  - 同じ表の列：ID, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe

## g0317（1 列）
- 見出し：FotografIn
- 例1 値：Wehrli, Harry | Wehrli, Bruno | Wehrli, Bruno | Wehrli, Artur | Brun, Hans
  - 同じ表の列：ID, Signatur, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe

## g0318（1 列）
- 見出し：Titel
- 例1 値：St. Annahorn, Panorama | Brunnen, Ortsgesamtansicht | Rigi Kulm, Landschaft | Maderanertal, Landschaft | Andermatt, Urnerloch, Ortsteilansicht
  - 同じ表の列：ID, Signatur, FotografIn, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe

## g0319（1 列）
- 見出し：Inhalt_Kurzbeschreibung
- 例1 値：Links ist die Fassade des Klosters , ze… | Blick auf das Löwendenkmal und die umli… | Blick auf die Gemeinde Hospental | Blick von Ufer des Wildenmattensees auf… | Zürich, Blick entlang des Utoquais in R…
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe

## g0320（1 列）
- 見出し：Datierung_Bemerkung
- 例1 値：geschätzt
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Farbe

## g0321（1 列）
- 見出し：Farbe
- 例1 値：S/W | S/W | S/W | S/W | S/W
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0322（1 列）
- 見出し：Orientierung_Form
- 例1 値：Vertikal | Horizontal | Horizontal | Vertikal | Horizontal
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0323（1 列）
- 見出し：Signatur
- 例1 値：GS-GUGE-STADTTORE-B-1 | GS-GUGE-JOYEUX-WEXELBERG-A-1b | GS-GUGE-FEYERABEND-E-15 | GS-GUGE-DIKENMANN-JK-E-1 | GS-GUGE-JOYEUX-WEXELBERG-A-4
  - 同じ表の列：ID, KünstlerIn, Titel, Inhalt_Kurzbeschrei…, Titelvariante, Datierung_von, Datierung_bis, Serientitel

## g0324（1 列）
- 見出し：KünstlerIn
- 例1 値：Linck, Jean-Antoine | Aberli, Johann Ludwig | Füssli, Johann Melchior | König, Franz Niklaus | Carrard, Jules-Samuel-Henri-Louis [pein…
  - 同じ表の列：ID, Signatur, Titel, Inhalt_Kurzbeschrei…, Titelvariante, Datierung_von, Datierung_bis, Serientitel

## g0325（1 列）
- 見出し：Titel
- 例1 値：Cuirassier vom Kaiserl. Regiment Hohen-… | Vue de Lausanne et de Ses environs pris… | [Après le goûter] | [Ansicht von Heiden und dem Bodensee] | Im Giessen bey Wädischweil am Zürcher-S…
  - 同じ表の列：ID, Signatur, KünstlerIn, Inhalt_Kurzbeschrei…, Titelvariante, Datierung_von, Datierung_bis, Serientitel

## g0326（1 列）
- 見出し：Inhalt_Kurzbeschreibung
- 例1 値：Genreszene mit Gemüsehandel in Bern. Fr… | Genreszene mit Kirchgang zur Taufe. Bau… | Genreszene mit drei Kindern beim Essen | Genreszene mit Weindegustation. Gasthof… | Königsfelden, Teilansicht. Anbau; Befes…
  - 同じ表の列：ID, Signatur, KünstlerIn, Titel, Titelvariante, Datierung_von, Datierung_bis, Serientitel

## g0327（1 列）
- 見出し：Titelvariante
- 例1 値：[Bad Blumenstein Bern] | [Vue de l'Isle St. Pierre sur le Lac de… | [Rigi Klösterli] | [Bauernhaus bei Interlaken] | [Strafvollzug]
  - 同じ表の列：ID, Signatur, KünstlerIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Serientitel

## g0328（1 列）
- 見出し：Serientitel
- 例1 値：Ansichten der Hauptorte der alten 13ört… | Sammlung malerischer Ansichten aufgenom… | Ähnlich wie das Blatt 'L'Embarquement d… | XXIV. Radierte Blätter von Franz Niklau… | Sammlung malerischer Ansichten aufgenom…
  - 同じ表の列：ID, Signatur, KünstlerIn, Titel, Inhalt_Kurzbeschrei…, Titelvariante, Datierung_von, Datierung_bis

## g0329（1 列）
- 見出し：Farbe
- 例1 値：Farbig | S/W | Farbig | Farbig | S/W
  - 同じ表の列：ID, Signatur, KünstlerIn, Titel, Inhalt_Kurzbeschrei…, Titelvariante, Datierung_von, Datierung_bis

## g0330（1 列）
- 見出し：Weiher
- 例1 値：Mannenweiher | Mannenweiher | Mannenweiher | Mannenweiher | Mannenweiher
  - 同じ表の列：Datum, Messtiefe (m), Temperatur [°C], Sauerstoffgehalt [m…

## g0331（1 列）
- 見出し：Messtiefe (m)
- 例1 値：4.0 | 2.5 | 3.5 | 4.5 | 5.0
  - 同じ表の列：Datum, Weiher, Temperatur [°C], Sauerstoffgehalt [m…

## g0332（1 列）
- 見出し：Temperatur [°C]
- 例1 値：10.7 | 25.2 | 17.7 | 15.1 | 21.0
  - 同じ表の列：Datum, Weiher, Messtiefe (m), Sauerstoffgehalt [m…

## g0333（1 列）
- 見出し：Sauerstoffgehalt [mg O2/l]
- 例1 値：7.2 | 8.9 | 9.6 | 7.3 | 9.0
  - 同じ表の列：Datum, Weiher, Messtiefe (m), Temperatur [°C]

## g0334（1 列）
- 見出し：Legislatur
- 例1 値：01.01.2021 - 31.12.2024 | 01.01.2009 - 31.12.2012 | 01.01.2017 - 31.12.2020 | 01.01.2021 - 31.12.2024 | 01.01.2025 - 31.12.2028
  - 同じ表の列：Jahr, Bezeichnung, Sitzungsdatum, Traktandenstatus, Freigabe, Ort, Zeit, Bemerkungen

## g0335（1 列）
- 見出し：Bezeichnung
- 例1 値：45. Sitzung Stadtparlament open end | 37. Sitzung Stadtparlament | 38. Sitzung Stadtparlament | 17. Sitzung Stadtparlament | 45. Sitzung Stadtparlament
  - 同じ表の列：Legislatur, Jahr, Sitzungsdatum, Traktandenstatus, Freigabe, Ort, Zeit, Bemerkungen

## g0336（1 列）
- 見出し：Sitzungsdatum
- 例1 値：2010-11-23 | 2003-08-26 | 2007-10-30 | 2003-09-16 | 2011-05-03
  - 同じ表の列：Legislatur, Jahr, Bezeichnung, Traktandenstatus, Freigabe, Ort, Zeit, Bemerkungen

## g0337（1 列）
- 見出し：Traktandenstatus
- 例1 値：behandelt | behandelt | verschoben | behandelt | verschoben
  - 同じ表の列：Legislatur, Jahr, Bezeichnung, Sitzungsdatum, Freigabe, Ort, Zeit, Bemerkungen

## g0338（1 列）
- 見出し：Freigabe
- 例1 値：Öffentlich | Öffentlich | Öffentlich | Öffentlich | Öffentlich
  - 同じ表の列：Legislatur, Jahr, Bezeichnung, Sitzungsdatum, Traktandenstatus, Ort, Zeit, Bemerkungen

## g0339（1 列）
- 見出し：Zeit
- 例1 値：16:00 | 16:00 | 16:00 | 16:00 | 16:00
  - 同じ表の列：Legislatur, Jahr, Bezeichnung, Sitzungsdatum, Traktandenstatus, Freigabe, Ort, Bemerkungen

## g0340（1 列）
- 見出し：Bemerkungen
- 例1 値：bis maximal 22.00 Uhr | bis 20.00 Uhr | bis maximal 22.00 Uhr | Aufräumsitzung - | bis 20.00 Uhr
  - 同じ表の列：Legislatur, Jahr, Bezeichnung, Sitzungsdatum, Traktandenstatus, Freigabe, Ort, Zeit

## g0341（1 列）
- 見出し：Geschaeftstyp
- 例1 値：Sachgeschäft | Parlamentarische Vorstösse/Interpellati… | Sachgeschäft | Sachgeschäft | Parlamentarische Vorstösse/Interpellati…
  - 同じ表の列：Legislatur, Jahr, Bezeichnung, Sitzungsdatum, Traktandenstatus, Freigabe, Ort, Zeit

## g0342（1 列）
- 見出し：Link
- 例1 値：https://www.stadt.sg.ch/news/stsg_medie… | https://www.stadt.sg.ch/news/stsg_medie… | https://www.stadt.sg.ch/news/stsg_medie… | https://www.stadt.sg.ch/news/stsg_home/… | https://www.stadt.sg.ch/news/stsg_medie…
  - 同じ表の列：Veröffentlicht

## g0343（1 列）
- 見出し：Veröffentlicht
- 例1 値：2024-03-27T08:00:00+00:00 | 2024-11-22T15:17:00+00:00 | 2026-08-14T09:30:00+00:00 | 2026-08-20T08:00:00+00:00 | 2025-06-11T07:00:00+00:00
  - 同じ表の列：Link

## g0344（1 列）
- 見出し：gemeinde_bfs_nr
- 例1 値：230 | 230 | 230 | 230 | 230
  - 同じ表の列：gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, richtung, spur_nr, lat

## g0345（1 列）
- 見出し：anlage_nr
- 例1 値：1f1fc3fe467d6edf4beb8a16ac498c4d | 1f1fc3fe467d6edf4beb8a16ac498c4d | a2f9487a8f950b5c2d4167a3fe21b1ea | a2f9487a8f950b5c2d4167a3fe21b1ea | 82af9ec3ea3d1189a4102c7fca7d10cb
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_typ, zeit_von, zeit_bis, richtung, spur_nr, lat

## g0346（1 列）
- 見出し：anlage_typ
- 例1 値：MIV | MIV | MIV | MIV | MIV
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, zeit_von, zeit_bis, richtung, spur_nr, lat

## g0347（1 列）
- 見出し：zeit_von
- 例1 値：2026-10-22T18:00:00+01 | 2026-10-23T17:00:00+01 | 2026-10-25T05:00:00+01 | 2026-10-26T11:00:00+01 | 2026-10-23T21:00:00+01
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_bis, richtung, spur_nr, lat

## g0348（1 列）
- 見出し：zeit_bis
- 例1 値：2026-10-26T08:59:59+01 | 2026-10-24T15:59:59+01 | 2026-10-22T18:59:59+01 | 2026-10-22T07:59:59+01 | 2026-10-23T17:59:59+01
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, richtung, spur_nr, lat

## g0349（1 列）
- 見出し：richtung
- 例1 値：N | SW | N | W | O
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, spur_nr, lat

## g0350（1 列）
- 見出し：spur_nr
- 例1 値：1.0 | 2.0 | 1.0 | 2.0 | 3.0
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, richtung, lat

## g0351（1 列）
- 見出し：lat
- 例1 値：47.47620118095351 | 47.49026195657432 | 47.49026195657432 | 47.47620118095351 | 47.49338159108304
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, richtung, spur_nr

## g0352（1 列）
- 見出し：lon
- 例1 値：8.760473555351716 | 8.760473555351716 | 8.70246489541625 | 8.760473555351716 | 8.70246489541625
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, richtung, spur_nr

## g0353（1 列）
- 見出し：station_id
- 例1 値：2206LH003 | 2206LH025 | 2206LH014 | 2206LH005 | 2206LH027
  - 同じ表の列：laengengrad, breitengrad, hoehe_in_meter_uebe…, daten_von, daten_bis

## g0354（1 列）
- 見出し：laengengrad
- 例1 値：8.763450175382351 | 8.720378186888198 | 8.730928329855894 | 8.716186053985846 | 8.714779886586909
  - 同じ表の列：station_id, breitengrad, hoehe_in_meter_uebe…, daten_von, daten_bis

## g0355（1 列）
- 見出し：breitengrad
- 例1 値：47.510075950117184 | 47.50440581492762 | 47.48818074324235 | 47.49551797250066 | 47.51241634805927
  - 同じ表の列：station_id, laengengrad, hoehe_in_meter_uebe…, daten_von, daten_bis

## g0356（1 列）
- 見出し：hoehe_in_meter_ueber_meeresspiegel
- 例1 値：458.0 | 438.0 | 436.0 | 461.0 | 462.0
  - 同じ表の列：station_id, laengengrad, breitengrad, daten_von, daten_bis

## g0357（1 列）
- 見出し：daten_von
- 例1 値：2022-11-01T00:00:00 | 2022-11-01T00:00:00 | 2022-11-01T00:00:00 | 2022-11-01T00:00:00 | 2022-11-01T00:00:00
  - 同じ表の列：station_id, laengengrad, breitengrad, hoehe_in_meter_uebe…, daten_bis

## g0358（1 列）
- 見出し：daten_bis
- 例1 値：2026-10-28T00:00:00 | 2026-10-28T00:00:00 | 2026-10-28T00:00:00 | 2026-10-28T00:00:00 | 2026-10-28T00:00:00
  - 同じ表の列：station_id, laengengrad, breitengrad, hoehe_in_meter_uebe…, daten_von

## g0359（1 列）
- 見出し：zeitpunkt
- 例1 値：2022-01-06T22:45:00+01:00 | 2022-01-02T21:45:00+01:00 | 2022-01-04T21:15:00+01:00 | 2022-01-10T11:45:00+01:00 | 2022-01-08T00:45:00+01:00
  - 同じ表の列：bruttolastgang_kwh

## g0360（1 列）
- 見出し：bruttolastgang_kwh
- 例1 値：17356.152 | 17693.366 | 13460.612 | 12561.281 | 15519.994
  - 同じ表の列：zeitpunkt

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
g0249	
g0250	
g0251	
g0252	
g0253	
g0254	
g0255	
g0256	
g0257	
g0258	
g0259	
g0260	
g0261	
g0262	
g0263	
g0264	
g0265	
g0266	
g0267	
g0268	
g0269	
g0270	
g0271	
g0272	
g0273	
g0274	
g0275	
g0276	
g0277	
g0278	
g0279	
g0280	
g0281	
g0282	
g0283	
g0284	
g0285	
g0286	
g0287	
g0288	
g0289	
g0290	
g0291	
g0292	
g0293	
g0294	
g0295	
g0296	
g0297	
g0298	
g0299	
g0300	
g0301	
g0302	
g0303	
g0304	
g0305	
g0306	
g0307	
g0308	
g0309	
g0310	
g0311	
g0312	
g0313	
g0314	
g0315	
g0316	
g0317	
g0318	
g0319	
g0320	
g0321	
g0322	
g0323	
g0324	
g0325	
g0326	
g0327	
g0328	
g0329	
g0330	
g0331	
g0332	
g0333	
g0334	
g0335	
g0336	
g0337	
g0338	
g0339	
g0340	
g0341	
g0342	
g0343	
g0344	
g0345	
g0346	
g0347	
g0348	
g0349	
g0350	
g0351	
g0352	
g0353	
g0354	
g0355	
g0356	
g0357	
g0358	
g0359	
g0360	
```
