# ラベル用シート 003 / 005

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：einheit
- 例1 値：Bq/l | μg/l | μg/l | μg/l | μg/l
  - 同じ表の列：gruppe, gruppe_id, analyt, analyt_id, kategorie, kategorie_sortierung, farbcode, start_datum

## g0242（1 列）
- 見出し：farbcode
- 例1 値：#00b4d8 | #ffe600 | #ff5100 | #64c800 | #ffb300
  - 同じ表の列：gruppe, gruppe_id, analyt, analyt_id, kategorie, kategorie_sortierung, einheit, start_datum

## g0243（1 列）
- 見出し：start_datum
- 例1 値：30.09.2024 | NA | 01.01.2020 | NA | NA
  - 同じ表の列：gruppe, gruppe_id, analyt, analyt_id, kategorie, kategorie_sortierung, einheit, farbcode

## g0244（1 列）
- 見出し：end_datum
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：gruppe, gruppe_id, analyt, analyt_id, kategorie, kategorie_sortierung, einheit, farbcode

## g0245（1 列）
- 見出し：indikator
- 例1 値：vollkosten_pro_stunde_abc | anz_stunden_a_aub | vollkosten_pro_stunde_b_uub | vollkosten_pro_stunde_a_aub | anz_stunden_b_uub
  - 同じ表の列：jahr, wert

## g0246（3 列）
- 見出し：wert
- 例1 値：95.7705711249091 | 213654 | 226 | 96.1067022480544 | 118.712120300752
  - 同じ表の列：jahr, indikator
- 例2 値：13.7 | 1996.2 | 952.9 | 264 | 766.3
  - 同じ表の列：jahr, funktionsbereich, funktion, einheit

## g0247（1 列）
- 見出し：bezirk_nr
- 例1 値：102 | 108 | 106 | 108 | 104
  - 同じ表の列：jahr, bezirk, id, plz, ort, typ, inhouse_spitex, pflegende_angehoeri…

## g0248（1 列）
- 見出し：bezirk
- 例1 値：Bezirk Dielsdorf | Bezirk Bülach | Bezirk Horgen | Bezirk Bülach | Bezirk Horgen
  - 同じ表の列：jahr, bezirk_nr, id, plz, ort, typ, inhouse_spitex, pflegende_angehoeri…

## g0249（1 列）
- 見出し：id
- 例1 値：7a12167e | f69bcdd0 | 788ff3f7 | bcba76e9 | 885c41a0
  - 同じ表の列：jahr, bezirk_nr, bezirk, plz, ort, typ, inhouse_spitex, pflegende_angehoeri…

## g0250（3 列）
- 見出し：plz
- 例1 値：8307 | 8627 | 8105 | 8193 | 8492
  - 同じ表の列：jahr, bezirk_nr, bezirk, id, ort, typ, inhouse_spitex, pflegende_angehoeri…
- 例2 値：8245 | 8180 | 8001 | 8180 | 8002
  - 同じ表の列：id, jahr, stadt, haus_nr, ladeleistung, connector_typ, stop_typ, aktiver_energieverb…

## g0251（1 列）
- 見出し：ort
- 例1 値：Thalwil | Wetzikon ZH | Wädenswil | Bauma | Wetzikon
  - 同じ表の列：jahr, bezirk_nr, bezirk, id, plz, typ, inhouse_spitex, pflegende_angehoeri…

## g0252（1 列）
- 見出し：typ
- 例1 値：Spitex-Institution ohne Leistungspflicht | Spitex-Institution mit Leistungspflicht | Spitex-Institution mit Leistungspflicht | Spitex-Institution mit Leistungspflicht | Spitex-Institution mit Leistungspflicht
  - 同じ表の列：jahr, bezirk_nr, bezirk, id, plz, ort, inhouse_spitex, pflegende_angehoeri…

## g0253（1 列）
- 見出し：inhouse_spitex
- 例1 値：nein | nein | nein | ja | nein
  - 同じ表の列：jahr, bezirk_nr, bezirk, id, plz, ort, typ, pflegende_angehoeri…

## g0254（1 列）
- 見出し：pflegende_angehoerige
- 例1 値：nicht erhoben | nicht erhoben | nicht erhoben | nicht erhoben | nicht erhoben
  - 同じ表の列：jahr, bezirk_nr, bezirk, id, plz, ort, typ, inhouse_spitex

## g0255（1 列）
- 見出し：indikator
- 例1 値：vollkosten_pro_stunde_b_uub | vollkosten_pro_stunde_a_aub | vollkosten_pro_stunde_c_gp | anz_vzae | anz_klienten
  - 同じ表の列：jahr, bezirk_nr, bezirk, id, plz, ort, typ, inhouse_spitex

## g0256（1 列）
- 見出し：quartal
- 例1 値：2 | 1 | 1 | 2 | 2
  - 同じ表の列：jahr, branchen, n, kumsum, vj_abs_n, vj_rel_n, vj_abs_kumsum, vj_rel_kumsum

## g0257（1 列）
- 見出し：branchen
- 例1 値：Total | Total | Diverse | Diverse | Total
  - 同じ表の列：jahr, quartal, n, kumsum, vj_abs_n, vj_rel_n, vj_abs_kumsum, vj_rel_kumsum

## g0258（1 列）
- 見出し：n
- 例1 値：2370 | 2392 | 2592 | 1939 | 1945
  - 同じ表の列：jahr, quartal, branchen, kumsum, vj_abs_n, vj_rel_n, vj_abs_kumsum, vj_rel_kumsum

## g0259（1 列）
- 見出し：kumsum
- 例1 値：5883 | 4856 | 4004 | 4071 | 2543
  - 同じ表の列：jahr, quartal, branchen, n, vj_abs_n, vj_rel_n, vj_abs_kumsum, vj_rel_kumsum

## g0260（1 列）
- 見出し：vj_abs_n
- 例1 値：194 | 56 | 5 | 317 | 185
  - 同じ表の列：jahr, quartal, branchen, n, kumsum, vj_rel_n, vj_abs_kumsum, vj_rel_kumsum

## g0261（1 列）
- 見出し：vj_rel_n
- 例1 値：0.031305114638448 | 0.031305114638448 | 0.016452442159383 | -0.0236286919831223 | -0.0381709741550695
  - 同じ表の列：jahr, quartal, branchen, n, kumsum, vj_abs_n, vj_abs_kumsum, vj_rel_kumsum

## g0262（1 列）
- 見出し：vj_abs_kumsum
- 例1 値：71 | 552 | 152 | 71 | 634
  - 同じ表の列：jahr, quartal, branchen, n, kumsum, vj_abs_n, vj_rel_n, vj_rel_kumsum

## g0263（1 列）
- 見出し：vj_rel_kumsum
- 例1 値：0.0921462534841777 | 0.158341658341658 | 0.0252650575231221 | 0.0200423429781227 | 0.0585305105853051
  - 同じ表の列：jahr, quartal, branchen, n, kumsum, vj_abs_n, vj_rel_n, vj_abs_kumsum

## g0264（7 列）
- 見出し：id
- 例1 値：2740038 | 2812258 | 2783338 | 2647506 | 2557854
  - 同じ表の列：jahr, stadt, plz, haus_nr, ladeleistung, connector_typ, stop_typ, aktiver_energieverb…
- 例2 値：6972024 | 18672024 | 17112024 | 3132024 | 13142024
  - 同じ表の列：jahr, kategorie, unterstutztes_proje…, begunstigte, beitrag_chf_pro_pro…

## g0265（1 列）
- 見出し：stadt
- 例1 値：Winterthur | Zürich | Bülach | Affoltern am Albis | Feuerthalen
  - 同じ表の列：id, jahr, plz, haus_nr, ladeleistung, connector_typ, stop_typ, aktiver_energieverb…

## g0266（1 列）
- 見出し：haus_nr
- 例1 値：9 | 9 | 17 | 12 | 9
  - 同じ表の列：id, jahr, stadt, plz, ladeleistung, connector_typ, stop_typ, aktiver_energieverb…

## g0267（1 列）
- 見出し：ladeleistung
- 例1 値：20.01 | 20.01 | 20.01 | 20.01 | 20.01
  - 同じ表の列：id, jahr, stadt, plz, haus_nr, connector_typ, stop_typ, aktiver_energieverb…

## g0268（1 列）
- 見出し：connector_typ
- 例1 値：Type 2 socket | Type 2 socket | Type 2 socket | Type 2 socket | Type 2 socket
  - 同じ表の列：id, jahr, stadt, plz, haus_nr, ladeleistung, stop_typ, aktiver_energieverb…

## g0269（1 列）
- 見出し：stop_typ
- 例1 値：NA | Lokaler Stop | EV getrennt | EV getrennt | EV getrennt
  - 同じ表の列：id, jahr, stadt, plz, haus_nr, ladeleistung, connector_typ, aktiver_energieverb…

## g0270（1 列）
- 見出し：aktiver_energieverbrauch
- 例1 値：2.156 | 4.37699999999998 | 5.31199999999999 | 1.18 | NA
  - 同じ表の列：id, jahr, stadt, plz, haus_nr, ladeleistung, connector_typ, stop_typ

## g0271（1 列）
- 見出し：aktive_ladeleistung
- 例1 値：3.26399993896484 | 3.26399993896484 | 3.32800006866455 | 3.39199995994567 | 3.39199995994567
  - 同じ表の列：id, jahr, stadt, plz, haus_nr, ladeleistung, connector_typ, stop_typ

## g0272（1 列）
- 見出し：geb_nr
- 例1 値：500 | 504 | 500 | 502 | 505
  - 同じ表の列：geb_bez, geb_eigentum, geb_verm_art, geb_policenr, geb_gemeinde, we_nr, we_bez

## g0273（1 列）
- 見出し：geb_bez
- 例1 値：WC-Gebäude mit Geräteraum Nr. 23 | HPS Kottenmatte 2, Sursee | Alpenquai 4, Luzern | Trakt 2 Verwaltungstrakt | Galtsauenstall
  - 同じ表の列：geb_nr, geb_eigentum, geb_verm_art, geb_policenr, geb_gemeinde, we_nr, we_bez

## g0274（1 列）
- 見出し：geb_eigentum
- 例1 値：K | K | Z | Z | Z
  - 同じ表の列：geb_nr, geb_bez, geb_verm_art, geb_policenr, geb_gemeinde, we_nr, we_bez

## g0275（1 列）
- 見出し：geb_verm_art
- 例1 値：Finanzvermögen | Verwaltungsvermögen | Verwaltungsvermögen | Verwaltungsvermögen | Verwaltungsvermögen
  - 同じ表の列：geb_nr, geb_bez, geb_eigentum, geb_policenr, geb_gemeinde, we_nr, we_bez

## g0276（1 列）
- 見出し：geb_policenr
- 例1 値：307.0055.L | 204.1328.B | 401.0429.B | 515.0191.D | 210.0261.B
  - 同じ表の列：geb_nr, geb_bez, geb_eigentum, geb_verm_art, geb_gemeinde, we_nr, we_bez

## g0277（1 列）
- 見出し：geb_gemeinde
- 例1 値：Kriens | Hitzkirch | Pfaffnau | Luzern | Schüpfheim
  - 同じ表の列：geb_nr, geb_bez, geb_eigentum, geb_verm_art, geb_policenr, we_nr, we_bez

## g0278（1 列）
- 見出し：we_nr
- 例1 値：12 | 202 | 34 | 607 | 48
  - 同じ表の列：geb_nr, geb_bez, geb_eigentum, geb_verm_art, geb_policenr, geb_gemeinde, we_bez

## g0279（1 列）
- 見出し：we_bez
- 例1 値：Schwändiwald | Sonnhaldenhof | Centralstrasse 31a (Parkplätze) | HFD Sedelstrasse 34, Emmen | Strafanstalt Wauwilermoos
  - 同じ表の列：geb_nr, geb_bez, geb_eigentum, geb_verm_art, geb_policenr, geb_gemeinde, we_nr

## g0280（1 列）
- 見出し：Anfangszeit
- 例1 値：2026-10-19T05:30:00+00:00 | 2026-10-28T05:30:00+00:00 | 2026-10-24T10:00:00+00:00 | 2026-10-11T02:00:00+00:00 | 2026-10-11T07:30:00+00:00
  - 同じ表の列：PM10, PM2.5, NO2, O3

## g0281（1 列）
- 見出し：PM10
- 例1 値：9.3877 | 10.256 | 6.726 | 7.0309 | 8.0079
  - 同じ表の列：Anfangszeit, PM2.5, NO2, O3

## g0282（1 列）
- 見出し：PM2.5
- 例1 値：1.9319 | 4.6913 | 5.4599 | 4.4024 | 3.2808
  - 同じ表の列：Anfangszeit, PM10, NO2, O3

## g0283（1 列）
- 見出し：NO2
- 例1 値：3.068079 | 9.264856 | 6.636986 | 7.185623 | 1.066523
  - 同じ表の列：Anfangszeit, PM10, PM2.5, O3

## g0284（1 列）
- 見出し：O3
- 例1 値：25.272659 | 44.687998 | 47.552817 | 70.102301 | 59.810097
  - 同じ表の列：Anfangszeit, PM10, PM2.5, NO2

## g0285（1 列）
- 見出し：firmensitz_code
- 例1 値：2761 | 2761 | 2761 | 2762 | 2761
  - 同じ表の列：firmensitz, uid, zusatz, strassenbezeichnung, eingangsnummer_geba…, postleitzahl, ort, firmensitz_bezirk_nr

## g0286（1 列）
- 見出し：firmensitz
- 例1 値：Aesch (BL) | Allschwil | Aesch (BL) | Aesch (BL) | Aesch (BL)
  - 同じ表の列：firmensitz_code, uid, zusatz, strassenbezeichnung, eingangsnummer_geba…, postleitzahl, ort, firmensitz_bezirk_nr

## g0287（1 列）
- 見出し：uid
- 例1 値：CHE257977181 | CHE414260414 | CHE269433367 | CHE106283297 | CHE112626968
  - 同じ表の列：firmensitz_code, firmensitz, zusatz, strassenbezeichnung, eingangsnummer_geba…, postleitzahl, ort, firmensitz_bezirk_nr

## g0288（1 列）
- 見出し：zusatz
- 例1 値：c/o Domaine Nussbaumer AG | c/o Daniel Gull | c/o Pentapharm AG | c/o Jos. Schneider AG | c/o Jesse Ng
  - 同じ表の列：firmensitz_code, firmensitz, uid, strassenbezeichnung, eingangsnummer_geba…, postleitzahl, ort, firmensitz_bezirk_nr

## g0289（1 列）
- 見出し：strassenbezeichnung
- 例1 値：Rosenbergweg | Burgfeldermattweg | Gewerbestrasse | Obertorweg | Hauelweg
  - 同じ表の列：firmensitz_code, firmensitz, uid, zusatz, eingangsnummer_geba…, postleitzahl, ort, firmensitz_bezirk_nr

## g0290（1 列）
- 見出し：eingangsnummer_gebaeude
- 例1 値：31 | 191 | 9 | 12 | 4
  - 同じ表の列：firmensitz_code, firmensitz, uid, zusatz, strassenbezeichnung, postleitzahl, ort, firmensitz_bezirk_nr

## g0291（1 列）
- 見出し：postleitzahl
- 例1 値：4123 | 4147 | 4123 | 4123 | 4123
  - 同じ表の列：firmensitz_code, firmensitz, uid, zusatz, strassenbezeichnung, eingangsnummer_geba…, ort, firmensitz_bezirk_nr

## g0292（1 列）
- 見出し：ort
- 例1 値：Aesch BL | Aesch BL | Aesch BL | Aesch BL | Aesch BL
  - 同じ表の列：firmensitz_code, firmensitz, uid, zusatz, strassenbezeichnung, eingangsnummer_geba…, postleitzahl, firmensitz_bezirk_nr

## g0293（1 列）
- 見出し：firmensitz_bezirk_nr
- 例1 値：1301 | 1301 | 1301 | 1301 | 1301
  - 同じ表の列：firmensitz_code, firmensitz, uid, zusatz, strassenbezeichnung, eingangsnummer_geba…, postleitzahl, ort

## g0294（1 列）
- 見出し：firmensitz_bezirk
- 例1 値：Arlesheim | Arlesheim | Arlesheim | Arlesheim | Arlesheim
  - 同じ表の列：firmensitz_code, firmensitz, uid, zusatz, strassenbezeichnung, eingangsnummer_geba…, postleitzahl, ort

## g0295（4 列）
- 見出し：Datum
- 例1 値：2025-03-04 | 2026-08-23 | 2024-08-21 | 2024-02-20 | 2024-10-16
  - 同じ表の列：Visitors, Interactions
- 例2 値：2026-11-29 | 2026-11-29 | 2026-11-29 | 2026-11-29 | 2026-11-29
  - 同じ表の列：Titel, Verwaltungsebene, Typ, Status, Total der Gemeinden, Ausgezählte Gemeind…, Letzte Änderung, Stimmbeteiligung

## g0296（1 列）
- 見出し：Visitors
- 例1 値：191 | 87 | 89 | 158 | 77
  - 同じ表の列：Datum, Interactions

## g0297（1 列）
- 見出し：Interactions
- 例1 値：3544 | 4040 | 1075 | 3675 | 4327
  - 同じ表の列：Datum, Visitors

## g0298（1 列）
- 見出し：Titel
- 例1 値：Parkhaus Post Basel | Parkhaus Messe | Parkhaus Storchen | Parkhaus Bahnhof Süd | Parkhaus City
  - 同じ表の列：Publikationszeit, Anzahl frei, Total, Anteil frei, Auslastung, Auslastung in Proze…, Link, geo_point_2d

## g0299（1 列）
- 見出し：Publikationszeit
- 例1 値：2026-10-28T12:39:00+00:00 | 2026-10-28T12:39:00+00:00 | 2026-10-28T12:39:00+00:00 | 2026-10-28T12:39:00+00:00 | 2026-10-28T12:39:00+00:00
  - 同じ表の列：Titel, Anzahl frei, Total, Anteil frei, Auslastung, Auslastung in Proze…, Link, geo_point_2d

## g0300（1 列）
- 見出し：Anzahl frei
- 例1 値：124 | 32 | 0 | 182 | 59
  - 同じ表の列：Titel, Publikationszeit, Total, Anteil frei, Auslastung, Auslastung in Proze…, Link, geo_point_2d

## g0301（1 列）
- 見出し：Total
- 例1 値：120 | 120 | 165 | 350 | 100
  - 同じ表の列：Titel, Publikationszeit, Anzahl frei, Anteil frei, Auslastung, Auslastung in Proze…, Link, geo_point_2d

## g0302（1 列）
- 見出し：Anteil frei
- 例1 値：0.4357142857142857 | 0.09125475285171103 | 0.3368421052631579 | 0.0 | 0.20557491289198607
  - 同じ表の列：Titel, Publikationszeit, Anzahl frei, Total, Auslastung, Auslastung in Proze…, Link, geo_point_2d

## g0303（1 列）
- 見出し：Auslastung
- 例1 値：0.6631578947368422 | 0.9285714285714286 | 1.0 | 0.908745247148289 | 0.5916666666666667
  - 同じ表の列：Titel, Publikationszeit, Anzahl frei, Total, Anteil frei, Auslastung in Proze…, Link, geo_point_2d

## g0304（1 列）
- 見出し：Auslastung in Prozent
- 例1 値：66 | 79 | 59 | 81 | 100
  - 同じ表の列：Titel, Publikationszeit, Anzahl frei, Total, Anteil frei, Auslastung, Link, geo_point_2d

## g0305（1 列）
- 見出し：Link
- 例1 値：https://www.parkleitsystem-basel.ch/par… | https://www.parkleitsystem-basel.ch/par… | https://www.parkleitsystem-basel.ch/par… | https://www.parkleitsystem-basel.ch/par… | https://www.parkleitsystem-basel.ch/par…
  - 同じ表の列：Titel, Publikationszeit, Anzahl frei, Total, Anteil frei, Auslastung, Auslastung in Proze…, geo_point_2d

## g0306（2 列）
- 見出し：geo_point_2d
- 例1 値：47.547299, 7.5922975 | 47.5515968, 7.593512 | 47.5622725, 7.5917937 | 47.5458851, 7.5884556 | 47.563241, 7.602175
  - 同じ表の列：Titel, Publikationszeit, Anzahl frei, Total, Anteil frei, Auslastung, Auslastung in Proze…, Link
- 例2 値：47.41756, 9.38057 | 47.44166666666667, 9.4125 | 47.4, 9.300833333333333 | 47.44694444444445, 9.405277777777778 | 47.42486, 9.37406
  - 同じ表の列：measured_at, device_id, location, data_temperature

## g0307（1 列）
- 見出し：id2
- 例1 値：storchen | claramatte | steinen | rebgasse | centralbahn
  - 同じ表の列：Titel, Publikationszeit, Anzahl frei, Total, Anteil frei, Auslastung, Auslastung in Proze…, Link

## g0308（1 列）
- 見出し：Temperatur
- 例1 値：16 | 26 | 20 | 13 | 15
  - 同じ表の列：Zeit, Koordinaten

## g0309（1 列）
- 見出し：Zeit
- 例1 値：2026-10-28T12:30:10+00:00 | 2026-10-28T12:30:10+00:00 | 2026-10-28T12:30:10+00:00 | 2026-10-28T12:30:10+00:00 | 2026-10-28T12:30:10+00:00
  - 同じ表の列：Temperatur, Koordinaten

## g0310（2 列）
- 見出し：Koordinaten
- 例1 値：47.570688, 7.613675 | 47.562072, 7.557569 | 47.570848, 7.61543 | 47.56169, 7.556763 | 47.538282, 7.620919
  - 同じ表の列：Temperatur, Zeit
- 例2 値：47.5106754945046, 9.42897632282134 | 47.5645052079446, 9.3821658411487 | 47.5636635895563, 9.37780847221199 | 47.5561719692823, 9.32875092014158 | 47.5620210371962, 9.36579308572479
  - 同じ表の列：firmen_uid, rechtsform, bfs_nr_gemeinde, gemeinde, ort, plz, egid, n_koord

## g0311（1 列）
- 見出し：Geo Point
- 例1 値：47.56858401046934, 7.644650007443797 | 47.49715001045031, 7.622140007435679 | 47.54728001047522, 7.605240307398976 | 47.53642701047293, 7.604179007401177 | 47.56093201047601, 7.598360507388766
  - 同じ表の列：Geo Shape, Anbieter, Fahrzeugtyp, Formfaktor, Antriebstyp, Maximale Reichweite, Derzeitige Reichwei…, URI zur Vermietung

## g0312（1 列）
- 見出し：Geo Shape
- 例1 値：{"coordinates": [7.569254007374221, 47.… | {"coordinates": [7.606054007406482, 47.… | {"coordinates": [7.613598007408942, 47.… | {"coordinates": [7.548401007339185, 47.… | {"coordinates": [7.619745007416077, 47.…
  - 同じ表の列：Geo Point, Anbieter, Fahrzeugtyp, Formfaktor, Antriebstyp, Maximale Reichweite, Derzeitige Reichwei…, URI zur Vermietung

## g0313（1 列）
- 見出し：Anbieter
- 例1 値：Pick-e-Bike | Velospot | Pick-e-Bike | Voi | Velospot
  - 同じ表の列：Geo Point, Geo Shape, Fahrzeugtyp, Formfaktor, Antriebstyp, Maximale Reichweite, Derzeitige Reichwei…, URI zur Vermietung

## g0314（1 列）
- 見出し：Fahrzeugtyp
- 例1 値：scooter | E-Bike | scooter | E-Bike | scooter
  - 同じ表の列：Geo Point, Geo Shape, Anbieter, Formfaktor, Antriebstyp, Maximale Reichweite, Derzeitige Reichwei…, URI zur Vermietung

## g0315（1 列）
- 見出し：Formfaktor
- 例1 値：scooter | bicycle | moped | bicycle | scooter
  - 同じ表の列：Geo Point, Geo Shape, Anbieter, Fahrzeugtyp, Antriebstyp, Maximale Reichweite, Derzeitige Reichwei…, URI zur Vermietung

## g0316（1 列）
- 見出し：Antriebstyp
- 例1 値：electric | electric_assist | electric | electric_assist | electric
  - 同じ表の列：Geo Point, Geo Shape, Anbieter, Fahrzeugtyp, Formfaktor, Maximale Reichweite, Derzeitige Reichwei…, URI zur Vermietung

## g0317（1 列）
- 見出し：Maximale Reichweite
- 例1 値：80000 | 80000 | 30000 | 70000 | 30000
  - 同じ表の列：Geo Point, Geo Shape, Anbieter, Fahrzeugtyp, Formfaktor, Antriebstyp, Derzeitige Reichwei…, URI zur Vermietung

## g0318（1 列）
- 見出し：Derzeitige Reichweite
- 例1 値：96000 | 59200 | 58800 | 57600 | 79200
  - 同じ表の列：Geo Point, Geo Shape, Anbieter, Fahrzeugtyp, Formfaktor, Antriebstyp, Maximale Reichweite, URI zur Vermietung

## g0319（1 列）
- 見出し：URI zur Vermietung
- 例1 値：https://www.voiscooters.com/de/ | http://www.pick-e-bike.ch/ | http://www.pick-e-bike.ch/ | https://www.voiscooters.com/de/ | http://www.pick-e-bike.ch/
  - 同じ表の列：Geo Point, Geo Shape, Anbieter, Fahrzeugtyp, Formfaktor, Antriebstyp, Maximale Reichweite, Derzeitige Reichwei…

## g0320（1 列）
- 見出し：Navigieren zu
- 例1 値：https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/…
  - 同じ表の列：Geo Point, Geo Shape, Anbieter, Fahrzeugtyp, Formfaktor, Antriebstyp, Maximale Reichweite, Derzeitige Reichwei…

## g0321（1 列）
- 見出し：ratsorgan_uid
- 例1 値：f2cb74be68324391a0ab07a565d1ce98 | 3391039997a441b3a142ea8e5db68c81 | da02607aa637486b91e4e64a34b77f06 | 1ea6c3cf0fde4b5283eb9dab423b160b | 3391039997a441b3a142ea8e5db68c81
  - 同じ表の列：Übersicht vom

## g0322（2 列）
- 見出し：Übersicht vom
- 例1 値：2026-10-28 00:00 | 2026-10-28 00:00 | 2026-10-28 00:00 | 2026-10-28 00:00 | 2026-10-28 00:00
  - 同じ表の列：ratsorgan_uid
- 例2 値：2026-10-28 00:00 | 2026-10-28 00:00 | 2026-10-28 00:00 | 2026-10-28 00:00 | 2026-10-28 00:00
  - 同じ表の列：session_uid, sessionssitzung_dat…, sessionssitzung_uhr…, sessionssitzung_bez…

## g0323（2 列）
- 見出し：session_uid
- 例1 値：ec453e3b54be4532a51c2820ca83b706 | 1e51bdd8d74a49edb264ae34177520f3 | ad2f83bd1c2c40848b79aba61e3bdd4e | 3a297152a0ef477ea6ddf7e248626d2f | 31b9cd4b158644b3afe5ab5fcb3077f8
  - 同じ表の列：traktandum_nummer, traktandum_geschaef…, traktandum_start_be…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…
- 例2 値：ec453e3b54be4532a51c2820ca83b706 | 4c7e380da1ef47c09c6612296c450927 | 66ccf0a9f4d24d318ff3b99e646644e8 | aecf375037ef4ddbade50879c538b5b4 | 383c1b11d0c145c5aed4de8403757176
  - 同じ表の列：sessionssitzung_dat…, sessionssitzung_uhr…, sessionssitzung_bez…, Übersicht vom

## g0324（1 列）
- 見出し：traktandum_nummer
- 例1 値：26 | 49 | 65 | 61 | 34
  - 同じ表の列：session_uid, traktandum_geschaef…, traktandum_start_be…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0325（1 列）
- 見出し：traktandum_geschaeft_nr
- 例1 値：2024.BVD.2180 | 2024.GRPARL.86 | 2018.GEF.1276 | 2025.GRPARL.1521 | 2022.BVD.7694
  - 同じ表の列：session_uid, traktandum_nummer, traktandum_start_be…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0326（1 列）
- 見出し：traktandum_start_behandlung_datum
- 例1 値：2022-11-28 | 2024-03-07 | 2024-03-05 | 2023-03-08 | 2024-03-07
  - 同じ表の列：session_uid, traktandum_nummer, traktandum_geschaef…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0327（1 列）
- 見出し：traktandum_start_behandlung_uhrzeit
- 例1 値：13.30–16.00 | 13.30–16.30 | 13.30-16.30 | 13.30-16.30 | 09.00–11.45
  - 同じ表の列：session_uid, traktandum_nummer, traktandum_geschaef…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0328（1 列）
- 見出し：traktandum_beschluss_uhrzeit
- 例1 値：2023-11-29 14:28:26.018 | 2025-09-02 13:57:22.013 | 2023-09-05 15:28:42.044 | 2025-06-12 14:15:06.031 | 2024-06-12 13:50:43.013
  - 同じ表の列：session_uid, traktandum_nummer, traktandum_geschaef…, traktandum_start_be…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0329（1 列）
- 見出し：traktandum_beschluss_deutsch
- 例1 値：Annahme | Punktweise beschlossen | Punktweise beschlossen | Kenntnisnahme | Rückweisung mit Auflagen
  - 同じ表の列：session_uid, traktandum_nummer, traktandum_geschaef…, traktandum_start_be…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0330（1 列）
- 見出し：traktandum_beschluss_franz
- 例1 値：Prise de connaissance et déclaration de… | Adoption | Prise de connaissance et déclaration de… | Adoption | Adoption
  - 同じ表の列：session_uid, traktandum_nummer, traktandum_geschaef…, traktandum_start_be…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0331（1 列）
- 見出し：traktandum_beschlussdetail_deutsch
- 例1 値：Ziffer 1: Ablehnung (49 Ja, 99 Nein, 1 … | Ziffer 1: Annahme (89 Ja, 55 Nein, 1 En… | Annahme: 144 Ja, 0 Nein, 0 Enthaltungen… | Annahme: 85 Ja, 60 Nein, 1 EnthaltungAn… | Ziffer 1: Annahme als Postulat (83 Ja, …
  - 同じ表の列：session_uid, traktandum_nummer, traktandum_geschaef…, traktandum_start_be…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0332（1 列）
- 見出し：traktandum_beschlussdetail_franz
- 例1 値：Chiffre 1 : adoption (130 oui, 17 non, … | Chiffre 1 : adoption (153 oui, 0 non, 0… | Chiffre 1 : rejet sous forme de postula… | Adoption : 133 oui, 0 non, 1 abstention… | avec charges
  - 同じ表の列：session_uid, traktandum_nummer, traktandum_geschaef…, traktandum_start_be…, traktandum_start_be…, traktandum_beschlus…, traktandum_beschlus…, traktandum_beschlus…

## g0333（1 列）
- 見出し：sessionssitzung_datum
- 例1 値：2023-03-07 | 2019-09-04 | 2016-09-13 | 2026-06-10 | 2018-01-24
  - 同じ表の列：session_uid, sessionssitzung_uhr…, sessionssitzung_bez…, Übersicht vom

## g0334（1 列）
- 見出し：sessionssitzung_uhrzeit
- 例1 値：13.30–16.30 | 13.30-16.30 | 13.00-16.35 | 09.00-11.45 | 17.00-19.00
  - 同じ表の列：session_uid, sessionssitzung_dat…, sessionssitzung_bez…, Übersicht vom

## g0335（1 列）
- 見出し：sessionssitzung_bezeichnung
- 例1 値：Donnerstag (Nachmittag) | Dienstag (Vormittag) | Montag (Nachmittag) | Mittwoch (Vormittag) | Mittwoch (Nachmittag)
  - 同じ表の列：session_uid, sessionssitzung_dat…, sessionssitzung_uhr…, Übersicht vom

## g0336（1 列）
- 見出し：biomasse_kwh
- 例1 値：75843725.0 | 75289240.0 | 95461056.0 | 84887134.0 | 86258045.0
  - 同じ表の列：jahr, wind_kwh, abfall_kwh, trinkwasserkraftwer…, klein_wasserkraftwe…, photovoltaik_kwh, wasserkraft_kwh

## g0337（1 列）
- 見出し：wind_kwh
- 例1 値：4639000.0 | 4773000.0 | 4379000.0 | 4372000.0 | 4400000.0
  - 同じ表の列：jahr, biomasse_kwh, abfall_kwh, trinkwasserkraftwer…, klein_wasserkraftwe…, photovoltaik_kwh, wasserkraft_kwh

## g0338（1 列）
- 見出し：abfall_kwh
- 例1 値：16000000.0 | 43000000.0 | 44000000.0 | 15000000.0 | 63000000.0
  - 同じ表の列：jahr, biomasse_kwh, wind_kwh, trinkwasserkraftwer…, klein_wasserkraftwe…, photovoltaik_kwh, wasserkraft_kwh

## g0339（1 列）
- 見出し：trinkwasserkraftwerk_kwh
- 例1 値：15687751.0 | 23303726.0 | 17049022.0 | 30345196.0 | 31614931.0
  - 同じ表の列：jahr, biomasse_kwh, wind_kwh, abfall_kwh, klein_wasserkraftwe…, photovoltaik_kwh, wasserkraft_kwh

## g0340（1 列）
- 見出し：klein_wasserkraftwerk_kwh
- 例1 値：309904580.0 | 309656003.0 | 382054764.0 | 425493400.0 | 381709879.0
  - 同じ表の列：jahr, biomasse_kwh, wind_kwh, abfall_kwh, trinkwasserkraftwer…, photovoltaik_kwh, wasserkraft_kwh

## g0341（1 列）
- 見出し：photovoltaik_kwh
- 例1 値：66784116.1 | 111406369.1 | 595338.0 | 693638.0 | 1216112.0
  - 同じ表の列：jahr, biomasse_kwh, wind_kwh, abfall_kwh, trinkwasserkraftwer…, klein_wasserkraftwe…, wasserkraft_kwh

## g0342（1 列）
- 見出し：wasserkraft_kwh
- 例1 値：7402000000.0 | 6657000000.0 | 7273783000.0 | 7282000000.0 | 6246000000.0
  - 同じ表の列：jahr, biomasse_kwh, wind_kwh, abfall_kwh, trinkwasserkraftwer…, klein_wasserkraftwe…, photovoltaik_kwh

## g0343（1 列）
- 見出し：bfsnr
- 例1 値：3821 | 3734 | 3961 | 3972 | 3981
  - 同じ表の列：gemeinde, region, raumtyp, handlungsraum, gemeindetyp, ch_hauptnutzung_code, standueberbauung, standueberbauung_ag…

## g0344（1 列）
- 見出し：gemeinde
- 例1 値：Felsberg | Breil/Brigels | Churwalden | Trin | Celerina/Schlarigna
  - 同じ表の列：bfsnr, region, raumtyp, handlungsraum, gemeindetyp, ch_hauptnutzung_code, standueberbauung, standueberbauung_ag…

## g0345（1 列）
- 見出し：region
- 例1 値：Imboden | Maloja | Engiadina Bassa/Val Müstair | Prättigau/Davos | Maloja
  - 同じ表の列：bfsnr, gemeinde, raumtyp, handlungsraum, gemeindetyp, ch_hauptnutzung_code, standueberbauung, standueberbauung_ag…

## g0346（1 列）
- 見出し：raumtyp
- 例1 値：Touristischer Intensiverholungsraum | Ländlicher Raum | Suburbaner Raum | Suburban-touristischer Intensiverholung… | Ländlicher Raum
  - 同じ表の列：bfsnr, gemeinde, region, handlungsraum, gemeindetyp, ch_hauptnutzung_code, standueberbauung, standueberbauung_ag…

## g0347（1 列）
- 見出し：handlungsraum
- 例1 値：Prättigau/Davos | Moesano | Viamala | Surselva | Engiadina Bassa/Val Müstair
  - 同じ表の列：bfsnr, gemeinde, region, raumtyp, gemeindetyp, ch_hauptnutzung_code, standueberbauung, standueberbauung_ag…

## g0348（1 列）
- 見出し：gemeindetyp
- 例1 値：Gemeinden mit starkem Bevölkerungsrückg… | Industriell-tertiäre Gemeinden (SIT) | Gemeinden mit starkem Bevölkerungsrückg… | Semitouristische Gemeinden (TST) | Semitouristische Gemeinden (TST)
  - 同じ表の列：bfsnr, gemeinde, region, raumtyp, handlungsraum, ch_hauptnutzung_code, standueberbauung, standueberbauung_ag…

## g0349（1 列）
- 見出し：ch_hauptnutzung_code
- 例1 値：12.0 | 14.0 | 14.0 | 13.0 | 11.0
  - 同じ表の列：bfsnr, gemeinde, region, raumtyp, handlungsraum, gemeindetyp, standueberbauung, standueberbauung_ag…

## g0350（1 列）
- 見出し：standueberbauung
- 例1 値：ueberbaut | ueberbaut | ueberbaut | nicht_ueberbaut | nicht_ueberbaut
  - 同じ表の列：bfsnr, gemeinde, region, raumtyp, handlungsraum, gemeindetyp, ch_hauptnutzung_code, standueberbauung_ag…

## g0351（1 列）
- 見出し：standueberbauung_aggregiert2
- 例1 値：überbaut | überbaut | nicht überbaut | überbaut | nicht überbaut
  - 同じ表の列：bfsnr, gemeinde, region, raumtyp, handlungsraum, gemeindetyp, ch_hauptnutzung_code, standueberbauung

## g0352（1 列）
- 見出し：auswertung_datum
- 例1 値：2026-10-01 | 2026-10-01 | 2026-10-01 | 2026-10-01 | 2026-10-01
  - 同じ表の列：bfsnr, gemeinde, region, raumtyp, handlungsraum, gemeindetyp, ch_hauptnutzung_code, standueberbauung

## g0353（1 列）
- 見出し：unterstutztes_projekt
- 例1 値：Besuch Musical "Mamma Mia" | Wettbewerb für professioneelles Kulturs… | Sportmaterialien und Sportgeräte | Sportveranstaltungen | Sportveranstaltungen
  - 同じ表の列：id, jahr, kategorie, begunstigte, beitrag_chf_pro_pro…

## g0354（1 列）
- 見出し：begunstigte
- 例1 値：Tandem-Spicchi di vacanza, Mendrisio | Pistolenclub Igis-Landquart, Schiers | Schwingerverband der Landschaft Davos, … | IG Team Surselva, Tavanasa | Ski-Langlauf, Förderbeitrag, Chur
  - 同じ表の列：id, jahr, kategorie, unterstutztes_proje…, beitrag_chf_pro_pro…

## g0355（1 列）
- 見出し：beitrag_chf_pro_projekt
- 例1 値：800.0 | 4000.0 | 4000.0 | 800.0 | 3000.0
  - 同じ表の列：id, jahr, kategorie, unterstutztes_proje…, begunstigte

## g0356（1 列）
- 見出し：Titel
- 例1 値：Erneuerungswahl Kreisgericht St.Gallen:… | Änderung vom 19. Dezember 2025 des Bund… | Erneuerungswahl Kreisgericht Toggenburg… | Volksinitiative «Ja zu fairen Bundesste… | Nachtrag zum Gesetz über die soziale Si…
  - 同じ表の列：Datum, Verwaltungsebene, Typ, Status, Total der Gemeinden, Ausgezählte Gemeind…, Letzte Änderung, Stimmbeteiligung

## g0357（1 列）
- 見出し：Verwaltungsebene
- 例1 値：none | federation | federation | none | federation
  - 同じ表の列：Titel, Datum, Typ, Status, Total der Gemeinden, Ausgezählte Gemeind…, Letzte Änderung, Stimmbeteiligung

## g0358（1 列）
- 見出し：Typ
- 例1 値：vote | election | election | vote | vote
  - 同じ表の列：Titel, Datum, Verwaltungsebene, Status, Total der Gemeinden, Ausgezählte Gemeind…, Letzte Änderung, Stimmbeteiligung

## g0359（1 列）
- 見出し：Total der Gemeinden
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Titel, Datum, Verwaltungsebene, Typ, Status, Ausgezählte Gemeind…, Letzte Änderung, Stimmbeteiligung

## g0360（1 列）
- 見出し：Ausgezählte Gemeinden
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Titel, Datum, Verwaltungsebene, Typ, Status, Total der Gemeinden, Letzte Änderung, Stimmbeteiligung

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
