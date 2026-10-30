# ラベル用シート 003 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：direktion_code
- 例1 値：7 | 7 | 2 | 6 | 6
  - 同じ表の列：jahr, personalgruppe, kaderstufe, kennzahl, wert, einheit

## g0242（1 列）
- 見出し：personalgruppe
- 例1 値：Verwaltungs- und Betriebspersonal | Verwaltungs- und Betriebspersonal | Verwaltungs- und Betriebspersonal | Verwaltungs- und Betriebspersonal | Verwaltungs- und Betriebspersonal
  - 同じ表の列：jahr, direktion_code, kaderstufe, kennzahl, wert, einheit

## g0243（1 列）
- 見出し：kaderstufe
- 例1 値：Mittleres Kader | Mittleres Kader | Kein Kader | Mittleres Kader | Oberes Kader
  - 同じ表の列：jahr, direktion_code, personalgruppe, kennzahl, wert, einheit

## g0244（1 列）
- 見出し：kennzahl
- 例1 値：Anstellungen | Anstellungen | Anstellungen | Anstellungen | Anstellungen
  - 同じ表の列：jahr, direktion_code, personalgruppe, kaderstufe, wert, einheit

## g0245（1 列）
- 見出し：wert
- 例1 値：40 | 162 | 2607 | 70 | 10
  - 同じ表の列：jahr, direktion_code, personalgruppe, kaderstufe, kennzahl, einheit

## g0246（1 列）
- 見出し：einheit
- 例1 値：Anzahl | Anzahl | Anzahl | Anzahl | Anzahl
  - 同じ表の列：jahr, direktion_code, personalgruppe, kaderstufe, kennzahl, wert

## g0247（2 列）
- 見出し：ID
- 例1 値：1036760 | 1051139 | 1035521 | 1051176 | 1035320
  - 同じ表の列：Signatur, AutorIn, Titel, Titelvariante, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung
- 例2 値：1011496 | 1008957 | 1010706 | 1010800 | 1009009
  - 同じ表の列：Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Kollation

## g0248（1 列）
- 見出し：Signatur
- 例1 値：SLA-Glauser-B-1-SCN-08 | SLA-Glauser-B-1-MUR-01 | SLA-Glauser-E-03-B-1-MUEL-21 | SLA-Glauser-B-1-MES-02 | SLA-Glauser-A-1/74
  - 同じ表の列：ID, AutorIn, Titel, Titelvariante, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0249（1 列）
- 見出し：AutorIn
- 例1 値：Glauser, Friedrich | Glauser, Friedrich | Glauser, Friedrich | Glauser, Friedrich | Glauser, Friedrich
  - 同じ表の列：ID, Signatur, Titel, Titelvariante, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0250（1 列）
- 見出し：Titel
- 例1 値：Glauser, Friedrich an Witz, Friedrich; … | Glauser, Friedrich an Witz, Friedrich; … | Glauser, Friedrich an Bendel, Berthe; K… | Glauser, Friedrich an Goetz-von Rucktes… | Glauser, Friedrich: 'Juni in Nervi'
  - 同じ表の列：ID, Signatur, AutorIn, Titelvariante, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0251（1 列）
- 見出し：Titelvariante
- 例1 値：'Schlumpf Erwin Mord' | 'Schlumpf Erwin Mord' | 'Schlumpf Erwin Mord' | 'Schlumpf Erwin Mord'
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0252（1 列）
- 見出し：Ort
- 例1 値：La Bernerie | Bel-Aiz | Ostermundigen | Winterthur | Collioure
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Titelvariante, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0253（2 列）
- 見出し：Datierung_von
- 例1 値：19370817 | 19370209 | 19370208 | 191901 | 19310406
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Titelvariante, Ort, Datierung_bis, Datierung_Bemerkung
- 例2 値：19221230 | 19231231 | 19221026 | 19221210 | 19200227
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_bis, Datierung_Bemerkung, Kollation

## g0254（2 列）
- 見出し：Datierung_bis
- 例1 値：1923 | 1920 | 1923 | 1926 | 1919
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Titelvariante, Ort, Datierung_von, Datierung_Bemerkung
- 例2 値：1921 | 1915 | 1920
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_Bemerkung, Kollation

## g0255（1 列）
- 見出し：Datierung_Bemerkung
- 例1 値：Werktyposkript | Jahr erschlossen | Ort des Poststempels | Datum des Poststempels | Poststempel
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Titelvariante, Ort, Datierung_von, Datierung_bis

## g0256（1 列）
- 見出し：Kollation
- 例1 値：1 Br. (Dg.) | 1 Br. | 1 Br. | 1 Br. | Ts./Dg.mit Korr. hs. 17 Bl.
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Titelvariante, Ort, Datierung_von, Datierung_bis

## g0257（1 列）
- 見出し：ISIL
- 例1 値：CH-001323-3 | CH-000298-4 | CH-000542-5 | CH-000201-6 | CH-000844-6
  - 同じ表の列：Status, Mutterinstitution, VZ-Sigel, VZ-Code, Institutionstyp, Institutionskategor…, Grossregion, Adresszusatz

## g0258（1 列）
- 見出し：Mutterinstitution
- 例1 値：CH-002183-5 | CH-002412-X | CH-000017-5 | CH-000017-5 | CH-000001-5
  - 同じ表の列：ISIL, Status, VZ-Sigel, VZ-Code, Institutionstyp, Institutionskategor…, Grossregion, Adresszusatz

## g0259（1 列）
- 見出し：VZ-Sigel
- 例1 値：Be 138 | Be 88 | Be 75 | Ge 122 | Ba 98
  - 同じ表の列：ISIL, Status, Mutterinstitution, VZ-Code, Institutionstyp, Institutionskategor…, Grossregion, Adresszusatz

## g0260（1 列）
- 見出し：VZ-Code
- 例1 値：BL001 | GE124 | GE140 | BE074 | GE073
  - 同じ表の列：ISIL, Status, Mutterinstitution, VZ-Sigel, Institutionstyp, Institutionskategor…, Grossregion, Adresszusatz

## g0261（1 列）
- 見出し：Institutionstyp
- 例1 値：Bibliothek | Bibliothek | Bibliothek | Bibliothek | Bibliothek
  - 同じ表の列：ISIL, Status, Mutterinstitution, VZ-Sigel, VZ-Code, Institutionskategor…, Grossregion, Adresszusatz

## g0262（1 列）
- 見出し：Institutionskategorie
- 例1 値：Öffentliche und gemischte Bibliothek | Kantonsbibliothek | Hochschul- und Forschungsbibliothek | Öffentliche und gemischte Bibliothek | Hochschul- und Forschungsbibliothek
  - 同じ表の列：ISIL, Status, Mutterinstitution, VZ-Sigel, VZ-Code, Institutionstyp, Grossregion, Adresszusatz

## g0263（1 列）
- 見出し：Grossregion
- 例1 値：Espace Mittelland | Ostschweiz | Ostschweiz | Nordwestschweiz | Espace Mittelland
  - 同じ表の列：ISIL, Status, Mutterinstitution, VZ-Sigel, VZ-Code, Institutionstyp, Institutionskategor…, Adresszusatz

## g0264（1 列）
- 見出し：Adresszusatz
- 例1 値：Pavillon Sicli | Engelhof | Pfarreisekretariat | Hôtel de Gléresse | Faculty of Medicine, University of Gene…
  - 同じ表の列：ISIL, Status, Mutterinstitution, VZ-Sigel, VZ-Code, Institutionstyp, Institutionskategor…, Grossregion

## g0265（1 列）
- 見出し：Postfach
- 例1 値：Postfach | Postfach | Case postale 126 | Case Postale 191 | Postfach 16
  - 同じ表の列：ISIL, Status, Mutterinstitution, VZ-Sigel, VZ-Code, Institutionstyp, Institutionskategor…, Grossregion

## g0266（1 列）
- 見出し：Signatur
- 例1 値：SLA-RMR-Ms_B_10/03 | SLA-RMR-Ms_B_7/82 | SLA-RMR-Ms_B_7/20 | SLA-RMR-Ms_B_1/107 | SLA-RMR-Ms_B_49/a
  - 同じ表の列：ID, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Kollation

## g0267（1 列）
- 見出し：AutorIn
- 例1 値：Rilke, Rainer Maria | Michelangelo | Rilke, Rainer Maria | Mallarmé, Stéphane | Rilke, Rainer Maria
  - 同じ表の列：ID, Signatur, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Kollation

## g0268（1 列）
- 見出し：Titel
- 例1 値：Rilke, Rainer Maria an Wunderly-Volkart… | Rilke, Rainer Maria an Reinhart, Georg;… | Rilke, Rainer Maria an Forrer, Anita (S… | Rilke, Rainer Maria an Clavel, Fanny; K… | Rilke, Rainer Maria an Schoenauer, H. (…
  - 同じ表の列：ID, Signatur, AutorIn, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Kollation

## g0269（1 列）
- 見出し：Ort
- 例1 値：Muzot | Gut Schönauburg bei Pratteln | Genf | Locarno | München
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Datierung_von, Datierung_bis, Datierung_Bemerkung, Kollation

## g0270（1 列）
- 見出し：Datierung_Bemerkung
- 例1 値：Datum des Poststempels | Datierung: Montag, ohne Jahresangabe | '(Allerheiligen)' | Datum des Poststempels; datiert: Montag | Briefkopf:'(Mittwoch nach Pfingsten.)'
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Kollation

## g0271（1 列）
- 見出し：Kollation
- 例1 値：1 Br. hs. | 1 Br. hs. | 1 Br. hs. | 1 Br. hs. m. Kuv. | 1 Br. hs.
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0272（1 列）
- 見出し：Widmung
- 例1 値：hs. Widmung an Baumgartner, Frieda | Niederschrift für Alfred Wolfenstein, m… | jeder Bd. m. Widmung an Voorhoeve, Coby
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0273（1 列）
- 見出し：Sensor ID
- 例1 値：5896ea43-5618-4717-ae19-81eb3fc0eebd | 5896ea43-5618-4717-ae19-81eb3fc0eebd | 5896ea43-5618-4717-ae19-81eb3fc0eebd | 5896ea43-5618-4717-ae19-81eb3fc0eebd | 5896ea43-5618-4717-ae19-81eb3fc0eebd
  - 同じ表の列：Gemessen am, Standort, Y Orientation Angle, X Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…, Windgeschwindigkeit…

## g0274（2 列）
- 見出し：Gemessen am
- 例1 値：2025-08-03T10:00:00.169000+00:00 | 2024-08-01T23:00:00.262000+00:00 | 2026-01-11T17:00:00.076000+00:00 | 2024-09-25T21:00:08.459000+00:00 | 2026-01-22T16:00:00.061000+00:00
  - 同じ表の列：Sensor ID, Standort, Y Orientation Angle, X Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…, Windgeschwindigkeit…
- 例2 値：2025-08-09T20:00:00.061000+00:00 | 2025-03-08T00:00:00.068000+00:00 | 2025-03-31T11:00:00.054000+00:00 | 2025-05-16T12:00:00.053000+00:00 | 2025-11-07T00:00:00.104000+00:00
  - 同じ表の列：Sensor ID, datum_tag, tag_nr, Wochentag, Arbeitstag, Passanten in Richtu…, Passanten in Richtu…, Passanten in beide …

## g0275（2 列）
- 見出し：Standort
- 例1 値：{"coordinates": [9.370882882317716, 47.… | {"coordinates": [9.370882882317716, 47.… | {"coordinates": [9.370882882317716, 47.… | {"coordinates": [9.370882882317716, 47.… | {"coordinates": [9.370882882317716, 47.…
  - 同じ表の列：Sensor ID, Gemessen am, Y Orientation Angle, X Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…, Windgeschwindigkeit…
- 例2 値：{"coordinates": [9.373069722530204, 47.… | {"coordinates": [9.373069722530204, 47.… | {"coordinates": [9.373069722530204, 47.… | {"coordinates": [9.373069722530204, 47.… | {"coordinates": [9.373069722530204, 47.…
  - 同じ表の列：Sensor ID, Gemessen am, datum_tag, tag_nr, Wochentag, Arbeitstag, Passanten in Richtu…, Passanten in Richtu…

## g0276（1 列）
- 見出し：Y Orientation Angle
- 例1 値：-2.4166666666666665 | -2.4166666666666665 | -2.1 | -2.033333333333333 | -2.4166666666666665
  - 同じ表の列：Sensor ID, Gemessen am, Standort, X Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…, Windgeschwindigkeit…

## g0277（1 列）
- 見出し：X Orientation Angle
- 例1 値：-2.1333333333333333 | -2.0333333333333337 | -2.016666666666667 | -2.1166666666666667 | -2.0
  - 同じ表の列：Sensor ID, Gemessen am, Standort, Y Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…, Windgeschwindigkeit…

## g0278（1 列）
- 見出し：Windgeschwindigkeit
- 例1 値：0.5766666666666667 | 0.8316666666666666 | 0.6050000000000001 | 0.8416666666666667 | 0.8033333333333333
  - 同じ表の列：Sensor ID, Gemessen am, Standort, Y Orientation Angle, X Orientation Angle, Windrichtung, Windgeschwindigkeit…, Windgeschwindigkeit…

## g0279（1 列）
- 見出し：Windrichtung
- 例1 値：240.4333333333333 | 117.43333333333334 | 186.0333333333333 | 245.93333333333337 | 74.86666666666666
  - 同じ表の列：Sensor ID, Gemessen am, Standort, Y Orientation Angle, X Orientation Angle, Windgeschwindigkeit, Windgeschwindigkeit…, Windgeschwindigkeit…

## g0280（1 列）
- 見出し：Windgeschwindigkeit Norden
- 例1 値：0.5816666666666667 | 0.021666666666666706 | -0.07833333333333332 | -0.16833333333333333 | 0.10333333333333332
  - 同じ表の列：Sensor ID, Gemessen am, Standort, Y Orientation Angle, X Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…

## g0281（1 列）
- 見出し：Windgeschwindigkeit Osten
- 例1 値：0.5516666666666666 | 0.14 | -0.7866666666666666 | 0.17 | -0.5299999999999999
  - 同じ表の列：Sensor ID, Gemessen am, Standort, Y Orientation Angle, X Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…

## g0282（1 列）
- 見出し：Maximum Windgeschwindigkeit
- 例1 値：4.095 | 1.6866666666666668 | 1.7983333333333331 | 1.0766666666666667 | 1.9016666666666666
  - 同じ表の列：Sensor ID, Gemessen am, Standort, Y Orientation Angle, X Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…

## g0283（1 列）
- 見出し：Sensor ID
- 例1 値：8a360f09-d606-4d26-b79f-3b6138002b8c | 8a360f09-d606-4d26-b79f-3b6138002b8c | 8a360f09-d606-4d26-b79f-3b6138002b8c | 8a360f09-d606-4d26-b79f-3b6138002b8c | 8a360f09-d606-4d26-b79f-3b6138002b8c
  - 同じ表の列：Gemessen am, datum_tag, tag_nr, Wochentag, Arbeitstag, Passanten in Richtu…, Passanten in Richtu…, Passanten in beide …

## g0284（1 列）
- 見出し：datum_tag
- 例1 値：2025-05-09 | 2025-04-06 | 2025-01-27 | 2025-03-21 | 2025-04-14
  - 同じ表の列：Sensor ID, Gemessen am, tag_nr, Wochentag, Arbeitstag, Passanten in Richtu…, Passanten in Richtu…, Passanten in beide …

## g0285（1 列）
- 見出し：tag_nr
- 例1 値：6 | 2 | 2 | 5 | 5
  - 同じ表の列：Sensor ID, Gemessen am, datum_tag, Wochentag, Arbeitstag, Passanten in Richtu…, Passanten in Richtu…, Passanten in beide …

## g0286（1 列）
- 見出し：Wochentag
- 例1 値：Sonntag | Samstag | Montag | Freitag | Sonntag
  - 同じ表の列：Sensor ID, Gemessen am, datum_tag, tag_nr, Arbeitstag, Passanten in Richtu…, Passanten in Richtu…, Passanten in beide …

## g0287（1 列）
- 見出し：Arbeitstag
- 例1 値：Werktage | Wochenende | Werktage | Wochenende | Werktage
  - 同じ表の列：Sensor ID, Gemessen am, datum_tag, tag_nr, Wochentag, Passanten in Richtu…, Passanten in Richtu…, Passanten in beide …

## g0288（1 列）
- 見出し：Passanten in Richtung Neumarkt
- 例1 値：19.0 | 41.0 | 1.0 | 34.0 | 51.0
  - 同じ表の列：Sensor ID, Gemessen am, datum_tag, tag_nr, Wochentag, Arbeitstag, Passanten in Richtu…, Passanten in beide …

## g0289（1 列）
- 見出し：Passanten in Richtung Multergasse
- 例1 値：62.0 | 8.0 | 26.0 | 49.0 | 5.0
  - 同じ表の列：Sensor ID, Gemessen am, datum_tag, tag_nr, Wochentag, Arbeitstag, Passanten in Richtu…, Passanten in beide …

## g0290（1 列）
- 見出し：Passanten in beide Richtungen (Summe)
- 例1 値：63.0 | 4.0 | 83.0 | 111.0 | 122.0
  - 同じ表の列：Sensor ID, Gemessen am, datum_tag, tag_nr, Wochentag, Arbeitstag, Passanten in Richtu…, Passanten in Richtu…

## g0291（1 列）
- 見出し：Nr
- 例1 値：1 | 9 | 4 | 3 | 10
  - 同じ表の列：Ort, Beschreibung, LV95 E, LV95 N, Standort, Bild

## g0292（1 列）
- 見出し：Ort
- 例1 値：Rehetobelstrasse/vis-à-vis Nr. 60 | Rosenbergstrasse/Dufourstrasse | Burgstrasse, westlich Haus Nr. 63 | Zürcher Strasse/westlich Fürstenlandbrü… | St.Georgen-Strasse/westlich Bitzistrasse
  - 同じ表の列：Nr, Beschreibung, LV95 E, LV95 N, Standort, Bild

## g0293（1 列）
- 見出し：Beschreibung
- 例1 値：Metallzaun gegenüber Gartenbauamt | Metallgeländer beim Trottoir | Metallgeländer beim Trottoir | Metallgeländer beim Trottoir | Metallzaun beim Trottoir
  - 同じ表の列：Nr, Ort, LV95 E, LV95 N, Standort, Bild

## g0294（1 列）
- 見出し：LV95 E
- 例1 値：2745893.7 | 2744897.1 | 2744836.2 | 2745653.8 | 2747916.7
  - 同じ表の列：Nr, Ort, Beschreibung, LV95 N, Standort, Bild

## g0295（1 列）
- 見出し：LV95 N
- 例1 値：1254542.2 | 1253834.4 | 1254050.2 | 1253600.1 | 1256093.4
  - 同じ表の列：Nr, Ort, Beschreibung, LV95 E, Standort, Bild

## g0296（1 列）
- 見出し：Standort
- 例1 値：2047-09-30T00:00:00 | 2047-09-30T00:00:00 | 2047-09-30T00:00:00 | 2047-09-30T00:00:00 | 2047-09-30T00:00:00
  - 同じ表の列：Nr, Ort, Beschreibung, LV95 E, LV95 N, Bild

## g0297（1 列）
- 見出し：Bild
- 例1 値：https://daten.stadt.sg.ch/api/v2/catalo… | https://daten.stadt.sg.ch/api/v2/catalo… | https://daten.stadt.sg.ch/api/v2/catalo… | https://daten.stadt.sg.ch/api/v2/catalo… | https://daten.stadt.sg.ch/api/v2/catalo…
  - 同じ表の列：Nr, Ort, Beschreibung, LV95 E, LV95 N, Standort

## g0298（1 列）
- 見出し：zeitpunkt
- 例1 値：2024-02-07T05:00:00+01:00 | 2024-01-28T06:00:00+01:00 | 2024-02-05T03:00:00+01:00 | 2024-01-18T12:00:00+01:00 | 2024-01-13T18:00:00+01:00
  - 同じ表の列：bruttolastgang_kwh

## g0299（1 列）
- 見出し：bruttolastgang_kwh
- 例1 値：127023.313 | 119504.252 | 46798.272 | 65897.216 | 54330.54
  - 同じ表の列：zeitpunkt

## g0300（1 列）
- 見出し：stichtag
- 例1 値：2017-12-31 | 2019-12-31 | 2019-12-31 | 2017-12-31 | 2017-12-31
  - 同じ表の列：jahr, gemeinde_bfs_nr, gemeinde, altersklasse, heimat, anzahl, anzahl_ist_kleingru…

## g0301（2 列）
- 見出し：gemeinde_bfs_nr
- 例1 値：230 | 230 | 230 | 230 | 230
  - 同じ表の列：jahr, stichtag, gemeinde, altersklasse, heimat, anzahl, anzahl_ist_kleingru…
- 例2 値：230 | 230 | 230 | 230 | 230
  - 同じ表の列：jahr, gemeinde, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, altersklasse

## g0302（1 列）
- 見出し：heimat
- 例1 値：Schweiz | Ausland | Schweiz | Ausland | Schweiz
  - 同じ表の列：jahr, stichtag, gemeinde_bfs_nr, gemeinde, altersklasse, anzahl, anzahl_ist_kleingru…

## g0303（1 列）
- 見出し：anzahl_ist_kleingruppe
- 例1 値：False | False | False | False | False
  - 同じ表の列：jahr, stichtag, gemeinde_bfs_nr, gemeinde, altersklasse, heimat, anzahl

## g0304（1 列）
- 見出し：geom_code
- 例1 値：quartier | quartier | quartier | stadtkreis | quartier
  - 同じ表の列：jahr, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, altersklasse

## g0305（1 列）
- 見出し：stadtkreis_bfs_nr
- 例1 値：6 | 2 | 5 | 2 | 7
  - 同じ表の列：jahr, gemeinde_bfs_nr, gemeinde, geom_code, stadtkreis, quartier_bfs_nr, quartier, altersklasse

## g0306（1 列）
- 見出し：stadtkreis
- 例1 値：Veltheim | Seen | Oberwinterthur | Oberwinterthur | Töss
  - 同じ表の列：jahr, gemeinde_bfs_nr, gemeinde, geom_code, stadtkreis_bfs_nr, quartier_bfs_nr, quartier, altersklasse

## g0307（1 列）
- 見出し：quartier_bfs_nr
- 例1 値：315 | 270 | 320 | 510 | 710
  - 同じ表の列：jahr, gemeinde_bfs_nr, gemeinde, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier, altersklasse

## g0308（1 列）
- 見出し：quartier
- 例1 値：Gotzenwil | Neuwiesen | Deutweg | Ricketwil | Guggenbühl
  - 同じ表の列：jahr, gemeinde_bfs_nr, gemeinde, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, altersklasse

## g0309（1 列）
- 見出し：einwohnende
- 例1 値：17 | 194 | 598 | 203 | 31
  - 同じ表の列：jahr, gemeinde_bfs_nr, gemeinde, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier

## g0310（1 列）
- 見出し：id
- 例1 値：anderung-vom-28.-september-2012-des-asy… | anderung-vom-28.-september-2012-des-asy… | anderung-vom-28.-september-2012-des-asy… | anderung-vom-28.-september-2012-des-asy… | anderung-vom-28.-september-2012-des-asy…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0311（1 列）
- 見出し：title_de_CH
- 例1 値：Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0312（1 列）
- 見出し：title_fr_CH
- 例1 値：Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0313（1 列）
- 見出し：title_it_CH
- 例1 値：Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0314（1 列）
- 見出し：title_rm_CH
- 例1 値：Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy… | Änderung vom 28. September 2012 des Asy…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0315（3 列）
- 見出し：date
- 例1 値：2013-06-09 | 2013-06-09 | 2013-06-09 | 2013-06-09 | 2013-06-09
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status
- 例2 値：2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status

## g0316（3 列）
- 見出し：shortcode
- 例1 値：E2 | E2 | E2 | E2 | E2
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status
- 例2 値：E1 | E1 | E1 | E1 | E1
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status

## g0317（3 列）
- 見出し：domain
- 例1 値：federation | federation | federation | federation | federation
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status
- 例2 値：federation | federation | federation | federation | federation
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status

## g0318（3 列）
- 見出し：answer
- 例1 値：accepted | accepted | accepted | accepted | accepted
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain
- 例2 値：rejected | rejected | rejected | rejected | rejected
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain

## g0319（1 列）
- 見出し：id
- 例1 値：volksinitiative-ja-zur-aufhebung-der-we… | volksinitiative-ja-zur-aufhebung-der-we… | volksinitiative-ja-zur-aufhebung-der-we… | volksinitiative-ja-zur-aufhebung-der-we… | volksinitiative-ja-zur-aufhebung-der-we…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0320（1 列）
- 見出し：title_de_CH
- 例1 値：Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0321（1 列）
- 見出し：title_fr_CH
- 例1 値：Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0322（1 列）
- 見出し：title_it_CH
- 例1 値：Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0323（1 列）
- 見出し：title_rm_CH
- 例1 値：Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0324（1 列）
- 見出し：id
- 例1 値：bundesgesetz-uber-die-bekampfung-ubertr… | bundesgesetz-uber-die-bekampfung-ubertr… | bundesgesetz-uber-die-bekampfung-ubertr… | bundesgesetz-uber-die-bekampfung-ubertr… | bundesgesetz-uber-die-bekampfung-ubertr…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0325（1 列）
- 見出し：title_de_CH
- 例1 値：Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0326（1 列）
- 見出し：title_fr_CH
- 例1 値：Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0327（1 列）
- 見出し：title_it_CH
- 例1 値：Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0328（1 列）
- 見出し：title_rm_CH
- 例1 値：Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr… | Bundesgesetz über die Bekämpfung übertr…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0329（1 列）
- 見出し：publicationDate
- 例1 値：2026-10-09 | 2026-10-23 | 2026-10-30 | 2026-10-09 | 2026-10-23
  - 同じ表の列：entryDeadline, expirationDate, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0330（1 列）
- 見出し：entryDeadline
- 例1 値：2026-11-12 | 2026-10-20 | 2026-10-15 | 2026-10-26 | 2026-10-26
  - 同じ表の列：publicationDate, expirationDate, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0331（1 列）
- 見出し：expirationDate
- 例1 値：2027-09-30 | 2027-10-16 | 2027-10-09 | 2027-09-25 | 2027-10-15
  - 同じ表の列：publicationDate, entryDeadline, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0332（1 列）
- 見出し：bfs_nr
- 例1 値：261 | 68 | 261 | 293 | 261
  - 同じ表の列：publicationDate, entryDeadline, expirationDate, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0333（1 列）
- 見出し：buildingContractor_legalEntity_selectType
- 例1 値：person | person | person | person | company
  - 同じ表の列：publicationDate, entryDeadline, expirationDate, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0334（1 列）
- 見出し：buildingContractor_noUID
- 例1 値：false | false | false | false | false
  - 同じ表の列：publicationDate, entryDeadline, expirationDate, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0335（1 列）
- 見出し：buildingContractor_index
- 例1 値：1 | 2 | 1 | 2 | 1
  - 同じ表の列：publicationDate, entryDeadline, expirationDate, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0336（1 列）
- 見出し：buildingContractor_company_legalForm
- 例1 値：106 | 106 | 106 | 110 | 223
  - 同じ表の列：publicationDate, entryDeadline, expirationDate, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0337（1 列）
- 見出し：buildingContractor_company_legalForm_de
- 例1 値：Aktiengesellschaft (AG) | Verwaltungseinheit der Gemeinde | Einfache Gesellschaft | Besondere Rechtsform | Aktiengesellschaft (AG)
  - 同じ表の列：publicationDate, entryDeadline, expirationDate, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0338（1 列）
- 見出し：projectFramer_selectType
- 例1 値：none | none | delegationBuildingContractor | other | other
  - 同じ表の列：publicationDate, entryDeadline, expirationDate, bfs_nr, buildingContractor_…, buildingContractor_…, buildingContractor_…, buildingContractor_…

## g0339（1 列）
- 見出し：datensatz_id
- 例1 値：705 | 1723 | 723 | 3148 | 1381
  - 同じ表の列：datum, publisher, datensatz_titel, anzahl_klicks, anzahl_besuchende

## g0340（1 列）
- 見出し：publisher
- 例1 値：statistisches-amt-kanton-zuerich | afm-kanton-zuerich | statistisches-amt-kanton-zuerich | stadt-winterthur | gesundheitsdirektion-kanton-zuerich
  - 同じ表の列：datum, datensatz_id, datensatz_titel, anzahl_klicks, anzahl_besuchende

## g0341（1 列）
- 見出し：datensatz_titel
- 例1 値：Echtzeitdaten am Wahl- und Abstimmungst… | Wirtschaft in Winterthur nach Quartiere… | Immobilienpreise im Kanton Zürich | Aerzte [Anz.] | Wasserverbrauch pro Tag und Kopf [Liter]
  - 同じ表の列：datum, datensatz_id, publisher, anzahl_klicks, anzahl_besuchende

## g0342（1 列）
- 見出し：anzahl_klicks
- 例1 値：1 | 3 | 2 | 1 | 1
  - 同じ表の列：datum, datensatz_id, publisher, datensatz_titel, anzahl_besuchende

## g0343（1 列）
- 見出し：anzahl_besuchende
- 例1 値：2 | 1 | 2 | 1 | 1
  - 同じ表の列：datum, datensatz_id, publisher, datensatz_titel, anzahl_klicks

## g0344（1 列）
- 見出し：ABSTIMMTAG
- 例1 値：2007-06-17T00:00:00Z | 2006-05-21T00:00:00Z | 2003-05-18T00:00:00Z | 2005-11-27T00:00:00Z | 2004-05-16T00:00:00Z
  - 同じ表の列：STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0345（1 列）
- 見出し：STAT_VORLAGE_ID
- 例1 値：223 | 181 | 254 | 154 | 236
  - 同じ表の列：ABSTIMMTAG, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0346（1 列）
- 見出し：BFS_VORLAGE_ID
- 例1 値：477 | 479 | 500 | 498 | 510
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0347（1 列）
- 見出し：VORLAGE_KURZBEZ
- 例1 値：Kirchengesetz | Kantonale Steuerinitiative | Volksinitiative «für die Halbierung des… | Bundesbeschluss über die Justizreform | Gold für die AHV (Kosa)
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0348（1 列）
- 見出し：VORLAGE_LANGBEZ
- 例1 値：Bundesgesetz vom 18. Juni 2004 über die… | Bundesbeschluss über die Änderung der V… | Bundesbeschluss vom 16. Dezember 2005 ü… | «Kredit Fernwärmeerschliessung» | Bundesbeschluss über Bau und Finanzieru…
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0349（1 列）
- 見出し：VORLAGENART_ID
- 例1 値：1 | 1 | 3 | 3 | 11
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0350（1 列）
- 見出し：VORLAGENART_BEZ
- 例1 値：Konstruktives Referendum: Gegenvorschla… | Fakultatives Referendum | Volksinitiative | Fakultatives Referendum | Obligatorisches Referendum
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, THEMA_ID, THEMA

## g0351（1 列）
- 見出し：THEMA_ID
- 例1 値：6 | 3 | 2 | 10 | 3
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA

## g0352（1 列）
- 見出し：THEMA
- 例1 値：Staatsordnung,Soziale Fragen – Sozialpo… | Sicherheitspolitik | Staatsordnung,Soziale Fragen – Sozialpo… | Staatsordnung,Umwelt und Lebensraum | Sicherheitspolitik
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID

## g0353（1 列）
- 見出し：ABSTIMMUNGSART_ID
- 例1 値：2 | 2 | 2 | 1 | 2
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID

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
```
