# ラベル用シート 004 / 005

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_004.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0361（1 列）
- 見出し：Letzte Änderung
- 例1 値：2026-10-22T12:21:48+00:00 | 2026-10-21T07:50:50+00:00 | 2026-10-21T07:44:44+00:00 | 2026-10-21T07:50:43+00:00 | 2026-10-21T07:50:54+00:00
  - 同じ表の列：Titel, Datum, Verwaltungsebene, Typ, Status, Total der Gemeinden, Ausgezählte Gemeind…, Stimmbeteiligung

## g0362（1 列）
- 見出し：Stimmbeteiligung
- 例1 値：0.0 | 0.0 | 0.0 | 0.0 | 0.0
  - 同じ表の列：Titel, Datum, Verwaltungsebene, Typ, Status, Total der Gemeinden, Ausgezählte Gemeind…, Letzte Änderung

## g0363（2 列）
- 見出し：Link
- 例1 値：https://www.sg.ch/news/sgch_allgemein/2… | https://www.sg.ch/news/sgch_allgemein/2… | https://www.sg.ch/news/sgch_allgemein/2… | https://www.sg.ch/news/sgch_allgemein/2… | https://www.sg.ch/news/sgch_allgemein/2…
  - 同じ表の列：Titel, Veröffentlicht
- 例2 値：https://www.sg.ch/news/sgch_allgemein/2… | https://www.sg.ch/news/sgch_allgemein/2… | https://www.sg.ch/news/sgch_allgemein/2… | https://www.sg.ch/news/sgch_allgemein/2… | https://www.sg.ch/news/sgch_allgemein/2…
  - 同じ表の列：Veröffentlicht, bild

## g0364（1 列）
- 見出し：Titel
- 例1 値：X. Nachtrag zum Gesetz über die Verwalt… | Wirkungsbericht Behindertenpolitik | VIII. Nachtrag zum Sozialhilfegesetz (Z… | VI. Nachtrag zum Planungs- und Baugesetz | Gesetz über die Verfahren zur Verbesser…
  - 同じ表の列：Link, Veröffentlicht

## g0365（2 列）
- 見出し：Veröffentlicht
- 例1 値：2024-11-07T07:00:00+00:00 | 2024-01-05T06:00:00+00:00 | 2024-12-18T09:00:00+00:00 | 2024-04-05T06:00:00+00:00 | 2026-07-01T13:00:00+00:00
  - 同じ表の列：Link, Titel
- 例2 値：2026-05-13T06:30:00+00:00 | 2026-05-01T07:30:00+00:00 | 2026-06-17T09:00:00+00:00 | 2026-07-01T07:30:00+00:00 | 2025-11-14T09:42:00+00:00
  - 同じ表の列：Link, bild

## g0366（1 列）
- 見出し：bild
- 例1 値：https://daten.sg.ch/api/v2/catalog/data… | https://daten.sg.ch/api/v2/catalog/data… | https://daten.sg.ch/api/v2/catalog/data… | https://daten.sg.ch/api/v2/catalog/data… | https://daten.sg.ch/api/v2/catalog/data…
  - 同じ表の列：Link, Veröffentlicht

## g0367（1 列）
- 見出し：abschlusstyp
- 例1 値：Informatikerin/Informatiker EFZ mit BM1… | Passerelle | Berufsmaturität (BM1) | Passerelle | Berufsmaturität (BM2)
  - 同じ表の列：stand, kanton, jahr, anzahl

## g0368（1 列）
- 見出し：code
- 例1 値：2603 | 2903 | 2904 | 2904 | 2903
  - 同じ表の列：gemeinde, richtung, spur_code, reg_bus, datum, zeit_von, zeit_bis, jahr

## g0369（3 列）
- 見出し：gemeinde
- 例1 値：Amriswil | Amriswil | Amriswil | Amriswil | Amriswil
  - 同じ表の列：code, richtung, spur_code, reg_bus, datum, zeit_von, zeit_bis, jahr
- 例2 値：Arbon | Egnach | Romanshorn | Arbon | Arbon
  - 同じ表の列：firmen_uid, rechtsform, bfs_nr_gemeinde, ort, plz, egid, n_koord, e_koord

## g0370（1 列）
- 見出し：richtung
- 例1 値：zum Kreisel Spange Ost | zum Marktplatz | nach Weinfelden | zum Marktplatz | nach Weinfelden
  - 同じ表の列：code, gemeinde, spur_code, reg_bus, datum, zeit_von, zeit_bis, jahr

## g0371（1 列）
- 見出し：spur_code
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：code, gemeinde, richtung, reg_bus, datum, zeit_von, zeit_bis, jahr

## g0372（1 列）
- 見出し：reg_bus
- 例1 値：Nein | Nein | Nein | Nein | Nein
  - 同じ表の列：code, gemeinde, richtung, spur_code, datum, zeit_von, zeit_bis, jahr

## g0373（1 列）
- 見出し：zeit_von
- 例1 値：05:00 | 02:00 | 05:00 | 03:00 | 09:00
  - 同じ表の列：code, gemeinde, richtung, spur_code, reg_bus, datum, zeit_bis, jahr

## g0374（1 列）
- 見出し：zeit_bis
- 例1 値：19:00 | 19:00 | 00:00 | 07:00 | 00:00
  - 同じ表の列：code, gemeinde, richtung, spur_code, reg_bus, datum, zeit_von, jahr

## g0375（1 列）
- 見出し：monat
- 例1 値：10 | 10 | 10 | 10 | 10
  - 同じ表の列：code, gemeinde, richtung, spur_code, reg_bus, datum, zeit_von, zeit_bis

## g0376（1 列）
- 見出し：firmen_uid
- 例1 値：CHE107081336 | CHE165211040 | CHE115249023 | CHE309704600 | CHE111775956
  - 同じ表の列：rechtsform, bfs_nr_gemeinde, gemeinde, ort, plz, egid, n_koord, e_koord

## g0377（1 列）
- 見出し：rechtsform
- 例1 値：Aktiengesellschaft | Einzelunternehmen | Gesellschaft mit beschränkter Haftung G… | Aktiengesellschaft | Schweizerische Zweigniederlassung im Ha…
  - 同じ表の列：firmen_uid, bfs_nr_gemeinde, gemeinde, ort, plz, egid, n_koord, e_koord

## g0378（1 列）
- 見出し：bfs_nr_gemeinde
- 例1 値：4436 | 4436 | 4436 | 4421 | 4436
  - 同じ表の列：firmen_uid, rechtsform, gemeinde, ort, plz, egid, n_koord, e_koord

## g0379（1 列）
- 見出し：ort
- 例1 値：Romanshorn | Romanshorn | Arbon | Arbon | Kesswil
  - 同じ表の列：firmen_uid, rechtsform, bfs_nr_gemeinde, gemeinde, plz, egid, n_koord, e_koord

## g0380（1 列）
- 見出し：egid
- 例1 値：640500 | 2333608 | 645034 | 640227 | 190726169
  - 同じ表の列：firmen_uid, rechtsform, bfs_nr_gemeinde, gemeinde, ort, plz, n_koord, e_koord

## g0381（1 列）
- 見出し：n_koord
- 例1 値：47.5106754945046 | 47.5320156192408 | 47.526696783121 | 47.5179306558369 | 47.5231430987993
  - 同じ表の列：firmen_uid, rechtsform, bfs_nr_gemeinde, gemeinde, ort, plz, egid, e_koord

## g0382（1 列）
- 見出し：e_koord
- 例1 値：9.41462044204711 | 9.42549003689217 | 9.37465114478732 | 9.37110629568756 | 9.42072961977931
  - 同じ表の列：firmen_uid, rechtsform, bfs_nr_gemeinde, gemeinde, ort, plz, egid, n_koord

## g0383（1 列）
- 見出し：haushaltstyp
- 例1 値：Paare ohne Kinder | Einelternhaushalte | Einpersonenhaushalte | Einpersonenhaushalte | Übrige Haushalte
  - 同じ表の列：jahr, anzahl

## g0384（1 列）
- 見出し：gebiet
- 例1 値：Nidwalden | Nidwalden | Zug | Zentralschweiz | Zürich
  - 同じ表の列：jahr, sprache, anteil_prozent

## g0385（1 列）
- 見出し：sprache
- 例1 値：Tamilisch | Deutsch | Serbisch/Kroatisch | Rätoromanisch | Französisch
  - 同じ表の列：jahr, gebiet, anteil_prozent

## g0386（1 列）
- 見出し：anteil_prozent
- 例1 値：93.45 | 2.21 | 1.34 | 2.3 | 1.03
  - 同じ表の列：jahr, gebiet, sprache

## g0387（1 列）
- 見出し：szenario
- 例1 値：Referenzszenario | Referenzszenario | Hohes Szenario | Hohes Szenario | Hohes Szenario
  - 同じ表の列：jahr, anzahl

## g0388（1 列）
- 見出し：Anzahl_verzeigte_Jugendliche
- 例1 値：4844 | 4170 | 6648 | 4674 | 5961
  - 同じ表の列：Jahr, Anzahl_verzeigte_Ju…, Anzahl_einwohner_10…

## g0389（1 列）
- 見出し：Anzahl_verzeigte_Jugendliche_Gewaltdelikt
- 例1 値：996 | 514 | 857 | 914 | 1014
  - 同じ表の列：Jahr, Anzahl_verzeigte_Ju…, Anzahl_einwohner_10…

## g0390（1 列）
- 見出し：Anzahl_einwohner_10_17_jaehrig
- 例1 値：106282 | 127499 | 105118 | 113786 | 107042
  - 同じ表の列：Jahr, Anzahl_verzeigte_Ju…, Anzahl_verzeigte_Ju…

## g0391（1 列）
- 見出し：VM-Nummer
- 例1 値：62 | 714 | 144 | 577 | 504
  - 同じ表の列：TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0392（1 列）
- 見出し：TU-Code
- 例1 値：11 | 11 | 11 | 11 | 11
  - 同じ表の列：VM-Nummer, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0393（1 列）
- 見出し：Variante
- 例1 値：101 | 101 | 101 | 101 | 106
  - 同じ表の列：VM-Nummer, TU-Code, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0394（1 列）
- 見出し：SJYID
- 例1 値：ch:1:sjyid:100001:615-002 | ch:1:sjyid:100001:618-001 | ch:1:sjyid:100001:779-001 | ch:1:sjyid:100001:742-001 | ch:1:sjyid:100001:781-001
  - 同じ表の列：VM-Nummer, TU-Code, Variante, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0395（1 列）
- 見出し：Abfahrt-BP-Nummer
- 例1 値：8507492 | 8500010 | 8501609 | 8301003 | 8506302
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0396（1 列）
- 見出し：Abfahrtsort
- 例1 値：Bern | Domodossola (I) | St. Gallen | Basel SBB | Basel SBB
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0397（1 列）
- 見出し：Abfahrtszeit
- 例1 値：10:45 | 22:17 | 19:39 | 08:32 | 12:05
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Ankunft-BP-Nummer, Ankunftsort

## g0398（1 列）
- 見出し：Ankunft-BP-Nummer
- 例1 値：8505300 | 8301003 | 8506311 | 8503000 | 8500010
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunftsort

## g0399（1 列）
- 見出し：Ankunftsort
- 例1 値：Basel SBB | Basel SBB | Zürich HB | Genève-Aéroport | Domodossola (I)
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer

## g0400（1 列）
- 見出し：Ankunftszeit
- 例1 値：24:25 | 09:29 | 08:44 | 16:27 | 22:52
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer

## g0401（1 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:5113:346453 | ch:1:sloid:2224:380929 | ch:1:sloid:2195:53270 | ch:1:sloid:1601:859129 | ch:1:sloid:4287:968719
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validFrom, validTo

## g0402（1 列）
- 見出し：parentSloidServicePoint
- 例1 値：ch:1:sloid:4298 | ch:1:sloid:92050 | ch:1:sloid:6139 | ch:1:sloid:92052 | ch:1:sloid:2204
  - 同じ表の列：sloid, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validFrom, validTo

## g0403（1 列）
- 見出し：parentNumberServicePoint
- 例1 値：8501209 | 8507357 | 8505374 | 8505543 | 8505226
  - 同じ表の列：sloid, parentSloidServiceP…, type, designation, inductionLoop, wheelchairAccess, validFrom, validTo

## g0404（1 列）
- 見出し：type
- 例1 値：TICKET_COUNTER | TICKET_COUNTER | TICKET_COUNTER | INFORMATION_DESK | INFORMATION_DESK
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, inductionLoop, wheelchairAccess, validFrom, validTo

## g0405（1 列）
- 見出し：designation
- 例1 値：Stationsgebäude | Reisezentrum Ins | Billettschalter | Billettschalter | Billettschalter
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, inductionLoop, wheelchairAccess, validFrom, validTo

## g0406（1 列）
- 見出し：inductionLoop
- 例1 値：NOT_APPLICABLE | YES | YES | NO | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, wheelchairAccess, validFrom, validTo

## g0407（1 列）
- 見出し：wheelchairAccess
- 例1 値：YES | NOT_APPLICABLE | YES | NOT_APPLICABLE | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, validFrom, validTo

## g0408（2 列）
- 見出し：validFrom
- 例1 値：2023-03-01T00:00:00 | 2021-07-21T00:00:00 | 2021-11-03T00:00:00 | 2021-07-21T00:00:00 | 2022-11-03T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validTo
- 例2 値：2010-02-10T00:00:00 | 2025-12-14T00:00:00 | 2009-04-09T00:00:00 | 2014-07-01T00:00:00 | 2021-12-12T00:00:00
  - 同じ表の列：slnid, linienId, validTo, status, lineType, concessionType, swissLineNumber, number

## g0409（2 列）
- 見出し：validTo
- 例1 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validFrom
- 例2 値：9999-12-31T00:00:00 | 2029-12-08T00:00:00 | 2038-07-31T00:00:00 | 2029-12-08T00:00:00 | 2039-07-14T00:00:00
  - 同じ表の列：slnid, linienId, validFrom, status, lineType, concessionType, swissLineNumber, number

## g0410（1 列）
- 見出し：creationDate
- 例1 値：2022-11-03T14:20:46 | 2021-07-29T07:13:34 | 2023-10-31T14:52:33 | 2023-03-01T15:13:49 | 2023-03-09T15:01:45
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validFrom

## g0411（1 列）
- 見出し：slnid
- 例1 値：ch:1:slnid:1024452 | ch:1:slnid:1025305 | ch:1:slnid:1024957 | ch:1:slnid:1024534 | ch:1:slnid:1024787
  - 同じ表の列：linienId, validFrom, validTo, status, lineType, concessionType, swissLineNumber, number

## g0412（1 列）
- 見出し：linienId
- 例1 値：85:801:3273 | 85:23:127 | ch:1:Line:100122:31 | ch:1:Line:876:210 | ch:1:Line:100122:1
  - 同じ表の列：slnid, validFrom, validTo, status, lineType, concessionType, swissLineNumber, number

## g0413（1 列）
- 見出し：lineType
- 例1 値：ORDERLY | ORDERLY | ORDERLY | ORDERLY | ORDERLY
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, concessionType, swissLineNumber, number

## g0414（1 列）
- 見出し：concessionType
- 例1 値：FEDERALLY_LICENSED_OR_APPROVED_LINE | FEDERALLY_LICENSED_OR_APPROVED_LINE | FEDERALLY_LICENSED_OR_APPROVED_LINE | FEDERALLY_LICENSED_OR_APPROVED_LINE | FEDERALLY_LICENSED_OR_APPROVED_LINE
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, lineType, swissLineNumber, number

## g0415（1 列）
- 見出し：swissLineNumber
- 例1 値：f.24446 | n.3652 | f.2250 | f.22401 | f.2320
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, lineType, concessionType, number

## g0416（1 列）
- 見出し：number
- 例1 値：R7 | S12 | S17 | 25335 | 2130
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, lineType, concessionType, swissLineNumber

## g0417（1 列）
- 見出し：shortNumber
- 例1 値：9 | 44 | 27 | 1 | 66
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, lineType, concessionType, swissLineNumber

## g0418（1 列）
- 見出し：link
- 例1 値：http://www.dna-studios.ch/en/videogames… | https://gbanga.com/gameography/bumble-b… | http://www.bitforge.ch/portfolio/swiss-… | http://www.firststrike.mobi/ | http://www.perilsofman.com/
  - 同じ表の列：studio, released, platforms

## g0419（1 列）
- 見出し：studio
- 例1 値：Bro Destruct | Mario von Rickenbach + Michael Frei | Tchagata Games | 416Games | MobyDickGames
  - 同じ表の列：link, released, platforms

## g0420（1 列）
- 見出し：released
- 例1 値：2014 | 2011 | 2009 | 2015 | 2014
  - 同じ表の列：link, studio, platforms

## g0421（1 列）
- 見出し：platforms
- 例1 値：iOS / Android | iPhone | PC / Mac / Web | iOS, Java | Gear VR + Oculus RIFT
  - 同じ表の列：link, studio, released

## g0422（1 列）
- 見出し：ID
- 例1 値：ILU01-000806233 | ILU01-000732598 | ILU01-000325500 | ILU01-000207247 | ILU01-000312224
  - 同じ表の列：CALL_NUMBER, TYPE, BARCODE, AUTHOR, TITLE, PLACE, YEAR, NUM_LOAN

## g0423（1 列）
- 見出し：CALL_NUMBER
- 例1 値：B.e 6232 | A.b 5804:1 | B.a 4893 | B.a 5853 | A.b 3692:1 (2)
  - 同じ表の列：ID, TYPE, BARCODE, AUTHOR, TITLE, PLACE, YEAR, NUM_LOAN

## g0424（1 列）
- 見出し：TYPE
- 例1 値：BOOK | BOOK | BOOK | BOOK | BOOK
  - 同じ表の列：ID, CALL_NUMBER, BARCODE, AUTHOR, TITLE, PLACE, YEAR, NUM_LOAN

## g0425（1 列）
- 見出し：BARCODE
- 例1 値：ILUM03116898 | ILUM02203196 | ILUM02039336 | ILUM03118361 | ILUM02216255
  - 同じ表の列：ID, CALL_NUMBER, TYPE, AUTHOR, TITLE, PLACE, YEAR, NUM_LOAN

## g0426（1 列）
- 見出し：AUTHOR
- 例1 値：Meier, Martin | Porter, Sheena | Boston, Lucy Maria | Federer, Heinrich | Böll, Heinrich
  - 同じ表の列：ID, CALL_NUMBER, TYPE, BARCODE, TITLE, PLACE, YEAR, NUM_LOAN

## g0427（1 列）
- 見出し：TITLE
- 例1 値：Ein Löwe geht um in Arkada City | Österreich in Dichtung und Farbaufnahmen | Three weeks | Die Eiserne Harfe | Gesammelte Gedichte
  - 同じ表の列：ID, CALL_NUMBER, TYPE, BARCODE, AUTHOR, PLACE, YEAR, NUM_LOAN

## g0428（1 列）
- 見出し：PLACE
- 例1 値：Luzern | Luzern | Zürich | Luzern | Luzern
  - 同じ表の列：ID, CALL_NUMBER, TYPE, BARCODE, AUTHOR, TITLE, YEAR, NUM_LOAN

## g0429（1 列）
- 見出し：NUM_LOAN
- 例1 値：1 | 3 | 2 | 1 | 5
  - 同じ表の列：ID, CALL_NUMBER, TYPE, BARCODE, AUTHOR, TITLE, PLACE, YEAR

## g0430（1 列）
- 見出し：funktionsbereich
- 例1 値：Land-, forst- und hauswirtschaftliche F… | Weitere Funktionen | Funktionen der Justiz (ohne Rechtspfleg… | Medizinische, soziale, erzieherische un… | Weitere Funktionen
  - 同じ表の列：jahr, funktion, wert, einheit

## g0431（1 列）
- 見出し：funktion
- 例1 値：Flughafenpolizei (inkl. Stundenlöhner) | Handwerkliche und übrige Lernende | Ärzteschaft | Soziale, erzieherische, wissenschaftl. … | Handwerkliche und übrige Lernende
  - 同じ表の列：jahr, funktionsbereich, wert, einheit

## g0432（1 列）
- 見出し：einheit
- 例1 値：Beschäftigungsumfang | Beschäftigungsumfang | Beschäftigungsumfang | Beschäftigungsumfang | Beschäftigungsumfang
  - 同じ表の列：jahr, funktionsbereich, funktion, wert

## g0433（1 列）
- 見出し：Forschungsstelle
- 例1 値：BFE | INNOSUISSE | INNOSUISSE | INNOSUISSE | INNOSUISSE
  - 同じ表の列：Projekttitel deutsch, Projekttitel englis…, Projekttitel franzö…, Projekttitel italie…, Kurzbeschreibung, Projektstatus, Bereich, Projektkategorie

## g0434（1 列）
- 見出し：Projekttitel deutsch
- 例1 値：Feasibility study for PV Greenhouse Far… | NGG - Neue Generation Greiferantrieb | TexSpace | Steigerung der Datenteilbereitschaft in… | Entschädigung Teilnahme Workshop Wärmep…
  - 同じ表の列：Forschungsstelle, Projekttitel englis…, Projekttitel franzö…, Projekttitel italie…, Kurzbeschreibung, Projektstatus, Bereich, Projektkategorie

## g0435（1 列）
- 見出し：Projekttitel englisch
- 例1 値：Light-field near-eye display | Innovative structural concepts for moto… | Driving forces in leisure traffic | Data-driven Electrocardiogram Interpret… | Self-Lubricating Pretreatment for Autom…
  - 同じ表の列：Forschungsstelle, Projekttitel deutsch, Projekttitel franzö…, Projekttitel italie…, Kurzbeschreibung, Projektstatus, Bereich, Projektkategorie

## g0436（1 列）
- 見出し：Projekttitel französisch
- 例1 値：Maîtrise des légionelles dans les bâtim… | Prevention des néophytes le long des ro… | Programmes multiprofessionnels/multidis… | Dodeka Key | Analyse de l’approvisionnement en vacci…
  - 同じ表の列：Forschungsstelle, Projekttitel deutsch, Projekttitel englis…, Projekttitel italie…, Kurzbeschreibung, Projektstatus, Bereich, Projektkategorie

## g0437（1 列）
- 見出し：Projekttitel italienisch
- 例1 値：Building Intelligent Automation | Autogestione per le malattie croniche e… | Sistema di presentazione in realtà aume… | Sondaggio presso i partner dell'AFC 201… | Sondaggio "Acquisto compulsivo"
  - 同じ表の列：Forschungsstelle, Projekttitel deutsch, Projekttitel englis…, Projekttitel franzö…, Kurzbeschreibung, Projektstatus, Bereich, Projektkategorie

## g0438（1 列）
- 見出し：Kurzbeschreibung
- 例1 値：Deep Learning & Neural Networks: selbst… | Das Ziel dieses Projektes ist es, Verha… | Secure Biometric IdentIfication with Pr… | PresMonA - Pressure monitoring for air … | Kaffeebohnensortierung
  - 同じ表の列：Forschungsstelle, Projekttitel deutsch, Projekttitel englis…, Projekttitel franzö…, Projekttitel italie…, Projektstatus, Bereich, Projektkategorie

## g0439（1 列）
- 見出し：Projektstatus
- 例1 値：Abgeschlossen | Abgeschlossen | Abgeschlossen | Abgeschlossen | Abgeschlossen
  - 同じ表の列：Forschungsstelle, Projekttitel deutsch, Projekttitel englis…, Projekttitel franzö…, Projekttitel italie…, Kurzbeschreibung, Bereich, Projektkategorie

## g0440（1 列）
- 見出し：Bereich
- 例1 値：Prävention nichtübertragbarer Krankheit… | Kommunikation und Kampagnen | 80 Energy & Environment | Wirksamkeitsüberprüfungen | 70 Engineering
  - 同じ表の列：Forschungsstelle, Projekttitel deutsch, Projekttitel englis…, Projekttitel franzö…, Projekttitel italie…, Kurzbeschreibung, Projektstatus, Projektkategorie

## g0441（1 列）
- 見出し：Projektkategorie
- 例1 値：Advanced combustion engines, Verbrennun… | Anwendungsorientierte Forschung, Wasser… | Biomasse & Holz (inkl. Abfälle, Klärsch… | Ressortforschung gemäss Definition BAG … | Ressortforschung gemäss Definition BAG …
  - 同じ表の列：Forschungsstelle, Projekttitel deutsch, Projekttitel englis…, Projekttitel franzö…, Projekttitel italie…, Kurzbeschreibung, Projektstatus, Bereich

## g0442（1 列）
- 見出し：NABS-Kategorie
- 例1 値：Industrielle Produktivität und Technolo… | Industrielle Produktivität und Technolo… | Industrielle Produktivität und Technolo… | Industrielle Produktivität und Technolo… | Industrielle Produktivität und Technolo…
  - 同じ表の列：Forschungsstelle, Projekttitel deutsch, Projekttitel englis…, Projekttitel franzö…, Projekttitel italie…, Kurzbeschreibung, Projektstatus, Bereich

## g0443（1 列）
- 見出し：Signatur
- 例1 値：GS-POCHON-598 | GS-POCHON-99 | GS-POCHON-175 | GS-POCHON-413 | GS-POCHON-543
  - 同じ表の列：ID, KünstlerIn, Titel, DIN-Format, Ansichtsbild, Andere_Id

## g0444（1 列）
- 見出し：KünstlerIn
- 例1 値：Pochon, Adolf | Pochon, Adolf | Pochon, Adolf | Pochon, Adolf | Pochon, Adolf
  - 同じ表の列：ID, Signatur, Titel, DIN-Format, Ansichtsbild, Andere_Id

## g0445（1 列）
- 見出し：Titel
- 例1 値：Service de France 1816. 3ème Régiment. … | Service de Hollande 1725-1740. Régiment… | Bern (Kanton). Dragoner 1713-1798 | Basel. Varia | Service de Naples 1825-1836. Régiment d…
  - 同じ表の列：ID, Signatur, KünstlerIn, DIN-Format, Ansichtsbild, Andere_Id

## g0446（1 列）
- 見出し：DIN-Format
- 例1 値：A4 | A4 | A4 | A4 | A2
  - 同じ表の列：ID, Signatur, KünstlerIn, Titel, Ansichtsbild, Andere_Id

## g0447（1 列）
- 見出し：Ansichtsbild
- 例1 値：https://www.helveticarchives.ch/getimag… | https://www.helveticarchives.ch/getimag… | https://www.helveticarchives.ch/getimag… | https://www.helveticarchives.ch/getimag… | https://www.helveticarchives.ch/getimag…
  - 同じ表の列：ID, Signatur, KünstlerIn, Titel, DIN-Format, Andere_Id

## g0448（1 列）
- 見出し：Andere_Id
- 例1 値：264-5; 757 | 24-1 | 71-1; 744 | 266-2; 762 | 67-1; 743
  - 同じ表の列：ID, Signatur, KünstlerIn, Titel, DIN-Format, Ansichtsbild

## g0449（1 列）
- 見出し：Signatur
- 例1 値：EAD-WEHR-32040-B | EAD-WEHR-32110-B | EAD-WEHR-32022-A | EAD-WEHR-32020-A | EAD-WEHR-32092-B
  - 同じ表の列：ID, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe

## g0450（2 列）
- 見出し：FotografIn
- 例1 値：Spelterini, Eduard | Spelterini, Eduard | Spelterini, Eduard | Spelterini, Eduard | Spelterini, Eduard
  - 同じ表の列：ID, Signatur, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe
- 例2 値：Schwarzenbach, Annemarie | Schwarzenbach, Annemarie | Schwarzenbach, Annemarie | Schwarzenbach, Annemarie | Schwarzenbach, Annemarie
  - 同じ表の列：ID, Signatur, Titel, Titelvariante, Datierung_von, Datierung_bis, Land_all, Ort_all

## g0451（1 列）
- 見出し：Titel
- 例1 値：Tödi, Teilansicht | Transvaal, Landschaft | Eiger, Mönch, Finsteraarhorn und Jungfr… | Jungfrau, Landschaft | Berg, Landschaft [Lokalisierung unsiche…
  - 同じ表の列：ID, Signatur, FotografIn, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe

## g0452（1 列）
- 見出し：Inhalt_Kurzbeschreibung
- 例1 値：Mont-Blanc-Gruppe mit Pointe d'Orny, ga… | Lagginhorn, 4010 m, Südseite, Ballonauf… | Johannesburg, Ballonaufnahme | Monte Rosa-Gebiet aus 4000 m Höhe, Ball… | Kopenhagen, Blick auf die Innenstadt mi…
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Datierung_von, Datierung_bis, Datierung_Bemerkung, Farbe

## g0453（2 列）
- 見出し：Datierung_von
- 例1 値：1893 | 1893 | 1893 | 1893 | 1893
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_bis, Datierung_Bemerkung, Farbe
- 例2 値：1935 | 1933 | 1933 | 1935 | 1933
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Titelvariante, Datierung_bis, Land_all, Ort_all

## g0454（2 列）
- 見出し：Datierung_bis
- 例1 値：1924 | 1924 | 1924 | 1924 | 1924
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_Bemerkung, Farbe
- 例2 値：1934 | 1935 | 1934 | 1935 | 1934
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Titelvariante, Datierung_von, Land_all, Ort_all

## g0455（1 列）
- 見出し：Datierung_Bemerkung
- 例1 値：Bild muss vor 1903 entstanden sein, wei…
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Farbe

## g0456（1 列）
- 見出し：Farbe
- 例1 値：S/W | S/W | S/W | S/W | S/W
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0457（1 列）
- 見出し：Orientierung_Form
- 例1 値：Horizontal | Horizontal | Horizontal | Horizontal | Horizontal
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0458（1 列）
- 見出し：Signatur
- 例1 値：SLA-Schwarzenbach-A-5-05/029 | SLA-Schwarzenbach-A-5-04/069 | SLA-Schwarzenbach-A-5-04/187 | SLA-Schwarzenbach-A-5-02/083 | SLA-Schwarzenbach-A-5-04/258
  - 同じ表の列：ID, FotografIn, Titel, Titelvariante, Datierung_von, Datierung_bis, Land_all, Ort_all

## g0459（1 列）
- 見出し：Titel
- 例1 値：Türkei, Kaiserie (Kayseri): Stadtansicht | Georgien, Grusinische Heerstrasse (Geor… | Irak, Babylon: Alltagsszene u. Landscha… | Persien, Isfahan: Meidan-i-Schah | Irak, Kadimein (Kazimiyya): Moschee
  - 同じ表の列：ID, Signatur, FotografIn, Titelvariante, Datierung_von, Datierung_bis, Land_all, Ort_all

## g0460（1 列）
- 見出し：Titelvariante
- 例1 値：Lokalisierung unsicher
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Datierung_von, Datierung_bis, Land_all, Ort_all

## g0461（1 列）
- 見出し：Land_all
- 例1 値：Persien | Syrien | Russland | Persien | Türkei
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Titelvariante, Datierung_von, Datierung_bis, Ort_all

## g0462（1 列）
- 見出し：Ort_all
- 例1 値：Babol | Persepolis | Mazanderan | Teheran | Mazanderan
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Titelvariante, Datierung_von, Datierung_bis, Land_all

## g0463（1 列）
- 見出し：Ort_Wikidata
- 例1 値：Alborz mountain range | Sultan Han | Mazandaran Province | Al-Ukhaidir Fortress | Baghdad
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Titelvariante, Datierung_von, Datierung_bis, Land_all

## g0464（1 列）
- 見出し：GrantNumber
- 例1 値：10007274 | 38244 | 225199 | 207145 | 189762
  - 同じ表の列：Title, TitleEnglish, FundingInstrumentPu…, FundingInstrumentRe…, FundingInstrumentLe…, Institute, InstituteCountry, ResearchInstitution

## g0465（1 列）
- 見出し：Title
- 例1 値：Dérives urbaines des campganes chinoises | Umstrittene Sichtbarkeit. Moscheebaukon… | Reverse iontophoresis: Noninvasive drug… | Spiel des Lebens / Le jeu de la vie | La folie du suicide. Une histoire médic…
  - 同じ表の列：GrantNumber, TitleEnglish, FundingInstrumentPu…, FundingInstrumentRe…, FundingInstrumentLe…, Institute, InstituteCountry, ResearchInstitution

## g0466（1 列）
- 見出し：TitleEnglish
- 例1 値：Johann Caspar Lavater - Historico-Criti… | Assessing metal bioavailability through… | Contentious visiblity. Conflicts trigge… | Contact mechanics of rough surfaces | Photopolymerizable, stable hydrogels fo…
  - 同じ表の列：GrantNumber, Title, FundingInstrumentPu…, FundingInstrumentRe…, FundingInstrumentLe…, Institute, InstituteCountry, ResearchInstitution

## g0467（1 列）
- 見出し：FundingInstrumentPublished
- 例1 値：Fellowships for prospective researchers | Project funding | Project funding | Project funding | Bridge - Proof of Concept
  - 同じ表の列：GrantNumber, Title, TitleEnglish, FundingInstrumentRe…, FundingInstrumentLe…, Institute, InstituteCountry, ResearchInstitution

## g0468（1 列）
- 見出し：FundingInstrumentReporting
- 例1 値：Project funding | Project funding | Project funding | National Research Programmes (NRPs) | Scientific Exchanges
  - 同じ表の列：GrantNumber, Title, TitleEnglish, FundingInstrumentPu…, FundingInstrumentLe…, Institute, InstituteCountry, ResearchInstitution

## g0469（1 列）
- 見出し：FundingInstrumentLevel1
- 例1 値：Careers | Programmes | Projects | Projects | Projects
  - 同じ表の列：GrantNumber, Title, TitleEnglish, FundingInstrumentPu…, FundingInstrumentRe…, Institute, InstituteCountry, ResearchInstitution

## g0470（1 列）
- 見出し：Institute
- 例1 値：UNI: Harvard University Cambridge, MA 0… | Society, Gender and Health Department o… | Max Planck Institute for Chemical Ecolo… | Département de Génétique et Evolution F… | University of East Anglia
  - 同じ表の列：GrantNumber, Title, TitleEnglish, FundingInstrumentPu…, FundingInstrumentRe…, FundingInstrumentLe…, InstituteCountry, ResearchInstitution

## g0471（1 列）
- 見出し：InstituteCountry
- 例1 値：Switzerland | Switzerland | Switzerland | Switzerland | Switzerland
  - 同じ表の列：GrantNumber, Title, TitleEnglish, FundingInstrumentPu…, FundingInstrumentRe…, FundingInstrumentLe…, Institute, ResearchInstitution

## g0472（1 列）
- 見出し：ResearchInstitution
- 例1 値：Berne University of Applied Sciences – … | Institution abroad – IACH | Non-profit organisations (libraries, mu… | Institution abroad – IACH | University of Geneva – GE
  - 同じ表の列：GrantNumber, Title, TitleEnglish, FundingInstrumentPu…, FundingInstrumentRe…, FundingInstrumentLe…, Institute, InstituteCountry

## g0473（1 列）
- 見出し：ResearchInstitutionType
- 例1 値：Other | Cantonal university | University of applied sciences | Other | Cantonal university
  - 同じ表の列：GrantNumber, Title, TitleEnglish, FundingInstrumentPu…, FundingInstrumentRe…, FundingInstrumentLe…, Institute, InstituteCountry

## g0474（1 列）
- 見出し：Titel (de)
- 例1 値：Kennzahlen der Schweizer Spitäler 2010 | Öffentliche Unterhaltsarbeiten (Ausgabe… | Investitionen in den Forstbetrieben in … | Gesamte Prämieneinnahmen der beaufsicht… | Strassenverkehrsunfälle: Verunfallte
  - 同じ表の列：ID, Departement (de), Aufgabengebiet (de)

## g0475（1 列）
- 見出し：Departement (de)
- 例1 値：UVEK | WBF | EDI | UVEK | UVEK
  - 同じ表の列：ID, Titel (de), Aufgabengebiet (de)

## g0476（1 列）
- 見出し：Aufgabengebiet (de)
- 例1 値：Soziale Wohlfahrt | Institutionelle und finanzielle Vorauss… | Institutionelle und finanzielle Vorauss… | Institutionelle und finanzielle Vorauss… | Institutionelle und finanzielle Vorauss…
  - 同じ表の列：ID, Titel (de), Departement (de)

## g0477（1 列）
- 見出し：NUTZUNGSLIZENZ
- 例1 値：Nutzungslizenz: CC0 | Nutzungslizenz: CC0 | Nutzungslizenz: CC0 | Nutzungslizenz: CC0 | Nutzungslizenz: CC0
  - 同じ表の列：ID, PERMALINK, PERSONENART, STARTDATUM_TYP, STARTDATUM, ENDDATUM_TYP, ENDDATUM, STARTORT_TYP

## g0478（1 列）
- 見出し：PERMALINK
- 例1 値：https://recherche.sik-isea.ch/sik:perso… | https://recherche.sik-isea.ch/sik:perso… | https://recherche.sik-isea.ch/sik:perso… | https://recherche.sik-isea.ch/sik:perso… | https://recherche.sik-isea.ch/sik:perso…
  - 同じ表の列：NUTZUNGSLIZENZ, ID, PERSONENART, STARTDATUM_TYP, STARTDATUM, ENDDATUM_TYP, ENDDATUM, STARTORT_TYP

## g0479（1 列）
- 見出し：PERSONENART
- 例1 値：Person | Person | Person | Person | Person
  - 同じ表の列：NUTZUNGSLIZENZ, ID, PERMALINK, STARTDATUM_TYP, STARTDATUM, ENDDATUM_TYP, ENDDATUM, STARTORT_TYP

## g0480（1 列）
- 見出し：STARTDATUM_TYP
- 例1 値：Geburtsdatum | Geburtsdatum | Geburtsdatum | Geburtsdatum | Geburtsdatum
  - 同じ表の列：NUTZUNGSLIZENZ, ID, PERMALINK, PERSONENART, STARTDATUM, ENDDATUM_TYP, ENDDATUM, STARTORT_TYP

## 答えの雛形

```
g0361	
g0362	
g0363	
g0364	
g0365	
g0366	
g0367	
g0368	
g0369	
g0370	
g0371	
g0372	
g0373	
g0374	
g0375	
g0376	
g0377	
g0378	
g0379	
g0380	
g0381	
g0382	
g0383	
g0384	
g0385	
g0386	
g0387	
g0388	
g0389	
g0390	
g0391	
g0392	
g0393	
g0394	
g0395	
g0396	
g0397	
g0398	
g0399	
g0400	
g0401	
g0402	
g0403	
g0404	
g0405	
g0406	
g0407	
g0408	
g0409	
g0410	
g0411	
g0412	
g0413	
g0414	
g0415	
g0416	
g0417	
g0418	
g0419	
g0420	
g0421	
g0422	
g0423	
g0424	
g0425	
g0426	
g0427	
g0428	
g0429	
g0430	
g0431	
g0432	
g0433	
g0434	
g0435	
g0436	
g0437	
g0438	
g0439	
g0440	
g0441	
g0442	
g0443	
g0444	
g0445	
g0446	
g0447	
g0448	
g0449	
g0450	
g0451	
g0452	
g0453	
g0454	
g0455	
g0456	
g0457	
g0458	
g0459	
g0460	
g0461	
g0462	
g0463	
g0464	
g0465	
g0466	
g0467	
g0468	
g0469	
g0470	
g0471	
g0472	
g0473	
g0474	
g0475	
g0476	
g0477	
g0478	
g0479	
g0480	
```
