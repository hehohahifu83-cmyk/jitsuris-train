# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Anlage_projekt-bezeichnung
- 例1 値：natürliche Person | natürliche Person | natürliche Person | natürliche Person | natürliche Person
  - 同じ表の列：Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, Jahr, Anmeldedatum, Anlage_inbetriebnah…

## g0002（1 列）
- 見出し：Empfaengerwechsel
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Anlage_projekt-beze…, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, Jahr, Anmeldedatum, Anlage_inbetriebnah…

## g0003（1 列）
- 見出し：Anlage_energietraeger
- 例1 値：Photovoltaik | Photovoltaik | Photovoltaik | Photovoltaik | Photovoltaik
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Leistung_kw, Produktion_kwh, Verguetung_chf, Jahr, Anmeldedatum, Anlage_inbetriebnah…

## g0004（1 列）
- 見出し：Leistung_kw
- 例1 値：3.6 | 3.1 | 3 | 2.9 | 3.4
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Produktion_kwh, Verguetung_chf, Jahr, Anmeldedatum, Anlage_inbetriebnah…

## g0005（1 列）
- 見出し：Produktion_kwh
- 例1 値：1755 | 3554 | 5323 | 2880 | 2153
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Verguetung_chf, Jahr, Anmeldedatum, Anlage_inbetriebnah…

## g0006（1 列）
- 見出し：Verguetung_chf
- 例1 値：2905 | 4035 | 639 | 1760 | 1563
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Jahr, Anmeldedatum, Anlage_inbetriebnah…

## g0007（1 列）
- 見出し：Jahr
- 例1 値：2011 | 2011 | 2011 | 2011 | 2011
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, Anmeldedatum, Anlage_inbetriebnah…

## g0008（1 列）
- 見出し：Anmeldedatum
- 例1 値：2008-05-02 | 2008-06-06 | 2008-05-01 | 2008-05-02 | 2008-05-02
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, Jahr, Anlage_inbetriebnah…

## g0009（1 列）
- 見出し：Anlage_inbetriebnahme
- 例1 値：2008-11-12 | 2010-02-05 | 2010-07-02 | 2011-09-09 | 2007-10-02
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, Jahr, Anmeldedatum

## g0010（1 列）
- 見出し：Anlage_vertragsende
- 例1 値：2032-12-31 | 2031-12-01 | 2033-12-01 | 2033-12-01 | 2033-12-31
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, Jahr, Anmeldedatum

## g0011（1 列）
- 見出し：Id
- 例1 値：5 | 16 | 3 | 4 | 12
  - 同じ表の列：Titel, Ausgabejahr, Auftraggeber, Kanton, Link

## g0012（1 列）
- 見出し：Titel
- 例1 値：Wärme- und Kältenutzung aus Sempacher- … | Perspectives chaleur du canton de Vaud | Potenzial des Walensees für Wärme- und … | Impacts of using lakes and rivers for e… | Factsheet Wärmenutzung aus Seen und Fli…
  - 同じ表の列：Id, Ausgabejahr, Auftraggeber, Kanton, Link

## g0013（1 列）
- 見出し：Ausgabejahr
- 例1 値：2019 | 2017 | 2014 | 2017 | 2019
  - 同じ表の列：Id, Titel, Auftraggeber, Kanton, Link

## g0014（1 列）
- 見出し：Auftraggeber
- 例1 値：Schmit M., Wüst. A, Bryner A,. Penicka … | Gaudard A., Weber C., Alexander T.J., H… | AWEL, Amt für Abfall Wasser, Energie un… | Amt für Wasser und Energie des Kantons … | Amt für Wasser und Energie des Kantons …
  - 同じ表の列：Id, Titel, Ausgabejahr, Kanton, Link

## g0018（1 列）
- 見出し：Thorium_Kg
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Date, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0019（1 列）
- 見出し：Uranium_depleted_Kg
- 例1 値：16 | 8 | 8 | 15 | 8
  - 同じ表の列：Date, Thorium_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0020（1 列）
- 見出し：Uranium_natural_Kg
- 例1 値：955833 | 1545182 | 1543682 | 1642580 | 662399
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0021（1 列）
- 見出し：Uranium_enriched_low_Kg
- 例1 値：107565 | 89831 | 81903 | 134011 | 131252
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0022（1 列）
- 見出し：Uranium_enriched_high_Kg
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_reprocessin…, Plutonium_Kg

## g0023（1 列）
- 見出し：Uranium_reprocessing_Kg
- 例1 値：68416 | 0 | 127623 | 68416 | 183728
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Plutonium_Kg

## g0024（1 列）
- 見出し：Plutonium_Kg
- 例1 値：1430 | 1 | 1 | 1 | 2414
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…

## g0025（2 列）
- 見出し：GEO_NR
- 例1 値：118 | 1322 | 138 | 723 | 243
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：52 | 62 | 62 | 52 | 62
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0026（1 列）
- 見出し：CLASS_HAB
- 例1 値：2 | 2 | 3 | 4 | 1
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0027（3 列）
- 見出し：GEOM_PERIOD
- 例1 値：2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0028（1 列）
- 見出し：VARIABLE
- 例1 値：sec_t_20 | sec_t_20 | sec_tran_20 | schu_t_98 | sec_gen_20
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0029（2 列）
- 見出し：SOURCE
- 例1 値：SDL | SDL | SDL | SDL | SDL
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：ESTV | ESTV | EFV | ESTV | ESTV
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0030（1 列）
- 見出し：VALUE_PERIOD
- 例1 値：1998/99 | 2020/21 | 2008/09 | 2019/20 | 2020/21
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS

## g0031（3 列）
- 見出し：UNIT_VALUE
- 例1 値：Num | Num | Num | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, VALUE, STATUS
- 例2 値：Num | Num | Per | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, VALUE, STATUS

## g0032（1 列）
- 見出し：VALUE
- 例1 値：56 | 1233 | 3095 | 1120 | 0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS

## g0033（3 列）
- 見出し：STATUS
- 例1 値：A | A | A | A | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE
- 例2 値：A | A | A | A | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE

## g0034（1 列）
- 見出し：GEO_NR
- 例1 値：CH | 121 | 131 | 121 | CH
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0035（2 列）
- 見出し：CLASS_HAB
- 例1 値：4 | 2 | 2 | Total | 3
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：Total | 3 | 4 | Total | 4
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0036（1 列）
- 見出し：VARIABLE
- 例1 値：wh_en_gaz | umz_zu_t_p | bat_stor_2 | sur_5z | bat_tot
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0037（1 列）
- 見出し：SOURCE
- 例1 値：GWS | GWS | GWS, STATPOP | GWS | GWS
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0038（2 列）
- 見出し：VALUE_PERIOD
- 例1 値：2021 | 2020 | 2021 | 2021 | 2021
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS
- 例2 値：2023 | 2021 | 2023 | 2023 | 2021
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS

## g0039（2 列）
- 見出し：VALUE
- 例1 値：8428.0 | 886.0 | 208.0 | 275.0 | 44.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS
- 例2 値：26.05 | 0.0 | 223006.96 | 548.9 | 12.46
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS

## g0040（1 列）
- 見出し：VARIABLE
- 例1 値：rev_cel_20 | rev_mar_35 | rev_ren_70 | rev_cel_80 | dep_inv
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0041（2 列）
- 見出し：BFS_Gemeindenummer
- 例1 値：2764 | 2829 | 2861 | 2766 | 2828
  - 同じ表の列：Gemeinde, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Alter, Anzahl_Plätze_Tages…
- 例2 値：2769 | 2769 | 2769 | 2788 | 2829
  - 同じ表の列：Gemeinde, Kategorie, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate, n_eingangskoordinate

## g0042（1 列）
- 見出し：Gemeinde
- 例1 値：Birsfelden | Pratteln | Bubendorf | Münchenstein | Wahlen
  - 同じ表の列：BFS_Gemeindenummer, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Alter, Anzahl_Plätze_Tages…

## g0043（1 列）
- 見出し：Institution
- 例1 値：Tagesheim Kakadu | Kita Laufen | Kinderkrippe Häslischloss Gartenstadt 5 | Tagesstruktur Bottmingen Burggartenstra… | Kindertagesstätte Taavi
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, PLZ, Ort, Trägerschaft, Rechtsform, Alter, Anzahl_Plätze_Tages…

## g0046（1 列）
- 見出し：Trägerschaft
- 例1 値：Einwohnergemeinde Bottmingen | Chindernäst GmbH | familea – Für Frauen, Kinder und Famili… | familea – Für Frauen, Kinder und Famili… | Kinderkrippe Häslischloss GmbH
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Rechtsform, Alter, Anzahl_Plätze_Tages…

## g0047（1 列）
- 見出し：Rechtsform
- 例1 値：privat | privat | öffentlich-rechtlich | privat | privat
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Trägerschaft, Alter, Anzahl_Plätze_Tages…

## g0048（1 列）
- 見出し：Alter
- 例1 値：4 bis 13 Jahre | 4 bis 12 Jahre | 4 Monate bis Kindergarteneeintritt | 3 Monate bis 13 Jahre | 6 bis 13 Jahre
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Anzahl_Plätze_Tages…

## g0049（1 列）
- 見出し：Anzahl_Plätze_Tagesbetreuung
- 例1 値：22 | 17 | 33 | 30 | 20
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Alter

## g0050（1 列）
- 見出し：Anzahl_Plätze_Mittagstisch
- 例1 値：140 | 12 | 60 | 47 | 30
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Alter

## g0052（1 列）
- 見出し：Kategorie
- 例1 値：Spielgruppe | Spielgruppe | Spielgruppe | Spielgruppe | Spielgruppe
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate, n_eingangskoordinate

## g0055（1 列）
- 見出し：Datenquelle
- 例1 値：Sicherheitsdirektion BL - Fachbereich F… | Sicherheitsdirektion BL - Fachbereich F… | Sicherheitsdirektion BL - Fachbereich F… | Sicherheitsdirektion BL - Fachbereich F… | Sicherheitsdirektion BL - Fachbereich F…
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Website, e_eingangskoordinate, n_eingangskoordinate

## g0056（1 列）
- 見出し：e_eingangskoordinate
- 例1 値：2612552.315 | 2633387.897 | 2604342.986 | 2613082.039 | 2622673.998
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Website, Datenquelle, n_eingangskoordinate

## g0057（1 列）
- 見出し：n_eingangskoordinate
- 例1 値：1260423.022 | 1257689.259 | 1265441.86 | 1257419.895 | 1263654.607
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate

## g0058（2 列）
- 見出し：koordinaten
- 例1 値：47.532371526089605, 7.6319822337704455 | 47.50954343697323, 7.599860505798547 | 47.54016386996969, 7.574738266367988 | 47.5095434279977, 7.599860492497234 | 47.51301154383288, 7.598501364512049
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate
- 例2 値：47.49374270802317, 7.591097830566832 | 47.46316461919887, 7.836230540920188 | 47.461132638449556, 7.914650025186573 | 47.41206395741037, 7.844308260868218 | 47.49913102298276, 7.558253240913667
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODE

## g0059（1 列）
- 見出し：BFS_Nummer
- 例1 値：2882 | 2854 | 2862 | 2890 | 2768
  - 同じ表の列：Zusatz, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODE, GKODN

## g0060（1 列）
- 見出し：Zusatz
- 例1 値：Gemeindeverwaltung Ettingen | c/o Gemeindeverwaltung Zeglingen | Gemeindeverwaltung Maisprach | Gemeindeverwaltung Buus | Gemeindeverwaltung Giebenach
  - 同じ表の列：BFS_Nummer, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODE, GKODN

## g0063（1 列）
- 見出し：UID_Nummer
- 例1 値：CHE115091561 | CHE115091070 | CHE115093063 | CHE115090946 | CHE115091897
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Link, GKODE, GKODN

## g0064（1 列）
- 見出し：UID_Link
- 例1 値：https://www.uid.admin.ch/Detail.aspx?ui… | https://www.uid.admin.ch/Detail.aspx?ui… | https://www.uid.admin.ch/Detail.aspx?ui… | https://www.uid.admin.ch/Detail.aspx?ui… | https://www.uid.admin.ch/Detail.aspx?ui…
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Nummer, GKODE, GKODN

## g0065（1 列）
- 見出し：GKODE
- 例1 値：2630957.514 | 2627789.583 | 2628702.59 | 2624169.498 | 2635893.487
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODN

## g0066（1 列）
- 見出し：GKODN
- 例1 値：1252905.321 | 1265693.976 | 1249827.567 | 1262063.929 | 1255642.584
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODE

## g0068（2 列）
- 見出し：Vorlage-ID
- 例1 値：2 | 3 | 6 | 2 | 2
  - 同じ表の列：Datum, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal
- 例2 値：5 | 2 | 2 | 2 | 3
  - 同じ表の列：Datum, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0069（1 列）
- 見出し：Titel
- 例1 値：«Stempelabgaben» | «Wirtschaftsabkommen Indonesien» | «Stimm- und Wahlrecht» | «Filmgesetz» | Änderung Zivildienstgesetz
  - 同じ表の列：Datum, Vorlage-ID, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal

## g0070（1 列）
- 見出し：ID und Titel der Vorlage
- 例1 値：2: «Berufliche Vorsorge» | 1: «Liegenschaftssteuern» | 1: «Prämien-Entlastungs-Initiative» | 2: «Kriegsmaterial-Exporte» | 2: «Justiz-Initiative»
  - 同じ表の列：Datum, Vorlage-ID, Titel, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal

## g0071（2 列）
- 見出し：Art der Vorlage
- 例1 値：national | kantonal | national | national | national
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal
- 例2 値：national | national | kantonal | national | national
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0072（2 列）
- 見出し：Gemeinde-ID
- 例1 値：1 | 3 | 1 | 3 | 2
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde, Wahllokal-ID, Wahllokal
- 例2 値：9 | 9 | 1 | 2 | 3
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde, ID, Resultattyp

## g0073（1 列）
- 見出し：Gemeinde
- 例1 値：Bettingen | Basel | Auslandschweizer | Basel | Basel
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Wahllokal-ID, Wahllokal

## g0074（1 列）
- 見出し：Wahllokal-ID
- 例1 値：15 | 15 | 21 | 20 | 30
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal

## g0075（1 列）
- 見出し：Wahllokal
- 例1 値：Basel brieflich Stimmende | Elektronisch Stimmende AS | Riehen briefl. & elektr. Stimmende (Tot… | Basel brieflich Stimmende | Basel brieflich Stimmende
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID

## g0076（2 列）
- 見出し：ID
- 例1 値：2021-09-26_01_11 | 2022-11-27_01_30 | 2025-09-28_02_23 | 2021-09-26_04_10 | 2021-09-26_03_21
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID
- 例2 値：2021-11-28_02_09 | 2022-02-13_01_09 | 2026-06-14_04_03 | 2022-09-25_03_01 | 2021-03-07_01_01
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Resultattyp

## g0077（1 列）
- 見出し：Titel
- 例1 値：Klimafonds-Initiative | «Prämien-Entlastungs-Initiative» | «Transplantationsgesetz» | «Berufliche Vorsorge» | «13. AHV-Rente»
  - 同じ表の列：Datum, Vorlage-ID, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0078（1 列）
- 見出し：ID und Titel der Vorlage
- 例1 値：3: «Zämme in Europa» | 1: «Klimagerechtigkeitsinitiative» und … | 1: «Gute-Luft-Initiative» | 2: Ernährungsinitiative | 4: «Parkgebühren»
  - 同じ表の列：Datum, Vorlage-ID, Titel, Art der Vorlage, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0079（1 列）
- 見出し：Gemeinde
- 例1 値：Auslandschweizer/-innen | Bettingen | Bettingen | Basel-Stadt | Basel
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, ID, Resultattyp

## g0080（1 列）
- 見出し：Resultattyp
- 例1 値：Schlussresultat | Schlussresultat | Schlussresultat | Schlussresultat | Schlussresultat
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID

## g0081（1 列）
- 見出し：Stimmberechtigte
- 例1 値：709 | 9066 | 786 | 755 | 90221
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID

## g0082（1 列）
- 見出し：Verkehrsmittel
- 例1 値：Barrierefrei | Auto | Auto | Bus | Velo
  - 同じ表の列：Sperrung, ZusatzPP, Alt-Texte, Bildquellen

## g0083（1 列）
- 見出し：Sperrung
- 例1 値：False | False | False | True | True
  - 同じ表の列：Verkehrsmittel, ZusatzPP, Alt-Texte, Bildquellen

## g0084（1 列）
- 見出し：ZusatzPP
- 例1 値：False | True | False | False | False
  - 同じ表の列：Verkehrsmittel, Sperrung, Alt-Texte, Bildquellen

## g0085（1 列）
- 見出し：Alt-Texte
- 例1 値：Anreiseempfehlung für Autofahrer ohne S… | Anreiseempfehlung für Busreisende ohne … | Anreiseempfehlung für Autofahrer mit Sp… | Anreiseempfehlung für Autofahrer mit Sp… | Anreiseempfehlung für Tramreisende
  - 同じ表の列：Verkehrsmittel, Sperrung, ZusatzPP, Bildquellen

## g0086（1 列）
- 見出し：Bildquellen
- 例1 値：https://data-bs.ch/stata/kapo/eventverk… | https://data-bs.ch/stata/kapo/eventverk… | https://data-bs.ch/stata/kapo/eventverk… | https://data-bs.ch/stata/kapo/eventverk… | https://data-bs.ch/stata/kapo/eventverk…
  - 同じ表の列：Verkehrsmittel, Sperrung, ZusatzPP, Alt-Texte

## g0087（1 列）
- 見出し：abstimmung_uid
- 例1 値：46a74f36-c808-43df-885d-a5668e2c5ccc | 7f120b28-5071-4c40-a59a-cd8ca765ac83 | a6ced6ac-c395-4a0d-b7e7-8ea72b181218 | 7f120b28-5071-4c40-a59a-cd8ca765ac83 | 0fac2ba7-179d-4b35-b041-3ca837274ecd
  - 同じ表の列：traktandum_uid, abstimmungsliste_st…, Übersicht vom

## g0088（1 列）
- 見出し：traktandum_uid
- 例1 値：8ffaea47e49c4149bf701644fa52ed47 | 4e6eedc28dd54a54a7174db854405046 | 3703926f3fdf43f0b508508a235cc1bf | c863e8c364d2410983c454fe13b28d0c | c863e8c364d2410983c454fe13b28d0c
  - 同じ表の列：abstimmung_uid, abstimmungsliste_st…, Übersicht vom

## g0089（1 列）
- 見出し：abstimmungsliste_stimme
- 例1 値：Ja | Ja | Ja | Ja | Ja
  - 同じ表の列：abstimmung_uid, traktandum_uid, Übersicht vom

## g0090（1 列）
- 見出し：Übersicht vom
- 例1 値：2026-11-04 00:00 | 2026-11-04 00:00 | 2026-11-04 00:00 | 2026-11-04 00:00 | 2026-11-04 00:00
  - 同じ表の列：abstimmung_uid, traktandum_uid, abstimmungsliste_st…

## g0091（1 列）
- 見出し：datum_vorstoss_eingang
- 例1 値：2019-01-23 | 2022-03-30 | 2017-08-30 | 2019-05-08 | 2023-03-01
  - 同じ表の列：registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0092（1 列）
- 見出し：registraturnummer
- 例1 値：2020/EA 43/108 | 2020/EA 15/49 | 2012/EA 62/182 | 2020/EA 72/197 | 2012/EA 69/193
  - 同じ表の列：datum_vorstoss_eing…, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0093（1 列）
- 見出し：nr_legislatur
- 例1 値：0421/2016-2020/GR | 0291/2012-2016/GR | 0045/2020-2024/GR | 0331/2012-2016/GR | 0470/2016-2020/GR
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0094（1 列）
- 見出し：grg_nr
- 例1 値：58 | 492 | 55 | 114 | 217
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0095（1 列）
- 見出し：vorstoss_bezeichnung
- 例1 値：Pandemieplan Thurgau - Erwachen aus dem… | Kosten-Nutzen einer ISO27001-Zertifizie… | Stimmrechtsalter 16 im Kanton Thurgau | Bäuerliches Bodenrecht | Ausstellung von Leumundszeugnissen
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0096（1 列）
- 見出し：vorstossart_bezeichnung
- 例1 値：Einfache Anfrage | Interpellation | Antrag nach § 52 bzw. § 46 der Geschäft… | Interpellation | Interpellation
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0097（1 列）
- 見出し：vorstossart_code
- 例1 値：5 | 5 | 5 | 5 | 5
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0098（1 列）
- 見出し：sachbegriffe_grgeko_1
- 例1 値：74.1 Strassenverkehr, öffentlicher Verk… | 85.0 Fürsorge, Massnahmen, Kinderheime,… | 14.2 Niederlassung, Aufenthalt, Asyl | 64.1 Staats- und Gemeindesteuern, allge… | 55.1 Polizeikorps / interkantonale Zusa…
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…

## g0099（1 列）
- 見出し：sachbegriffe_grgeko_2
- 例1 値：90.0 Wirtschaftliche Entwicklung | 73.2 Elektrizität inkl. Versorgung, Was… | 16.2 Abstimmungen | 70.2 Baugesetz; Planungen Hoch- und Tie… | 74.1 Strassenverkehr, öffentlicher Verk…
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…

## g0100（1 列）
- 見出し：sachbegriffe_grgeko_3
- 例1 値：73.1 Allgemeines, Energiegesetz, Kernen… | 90.0 Wirtschaftliche Entwicklung | 70.1 Raumplanung, Richtpläne | 13.1 Gebiet, Organisation, Reglemente, …
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…

## g0101（1 列）
- 見出し：VM-Nummer
- 例1 値：27 | 612 | 769 | 704 | 146
  - 同じ表の列：TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0102（1 列）
- 見出し：TU-Code
- 例1 値：11 | 11 | 11 | 11 | 11
  - 同じ表の列：VM-Nummer, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0103（1 列）
- 見出し：Variante
- 例1 値：101 | 102 | 111 | 109 | 101
  - 同じ表の列：VM-Nummer, TU-Code, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0104（1 列）
- 見出し：SJYID
- 例1 値：ch:1:sjyid:100001:66-005 | ch:1:sjyid:100001:13-002 | ch:1:sjyid:100001:717-001 | ch:1:sjyid:100001:74-002 | ch:1:sjyid:100001:40-001
  - 同じ表の列：VM-Nummer, TU-Code, Variante, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0105（1 列）
- 見出し：Abfahrt-BP-Nummer
- 例1 値：8507000 | 8507492 | 8500010 | 8507000 | 8509000
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0106（1 列）
- 見出し：Abfahrtsort
- 例1 値：Basel SBB | St. Gallen | Domodossola (I) | Basel SBB | Bregenz
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0107（1 列）
- 見出し：Abfahrtszeit
- 例1 値：07:18 | 31:14 | 14:30 | 20:38 | 19:41
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Ankunft-BP-Nummer, Ankunftsort

## g0108（1 列）
- 見出し：Ankunft-BP-Nummer
- 例1 値：8503000 | 8301003 | 8501609 | 8500010 | 8500090
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunftsort

## g0109（1 列）
- 見出し：Ankunftsort
- 例1 値：Basel Bad Bf | Basel SBB | Zürich HB | Feldkirch | Domodossola (I)
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer

## g0110（1 列）
- 見出し：Ankunftszeit
- 例1 値：18:13 | 09:53 | 20:23 | 11:52 | 11:29
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer

## g0111（1 列）
- 見出し：ID
- 例1 値：FK | SPB | KOM | SBF | OMB
  - 同じ表の列：Organisation_Kurzbe…, Direktion_Kurzbezei…, Dienststelle_Kurzbe…

## g0112（1 列）
- 見出し：Organisation_Kurzbezeichnung
- 例1 値：Stadt | Stadt | Stadt | Stadt | Stadt
  - 同じ表の列：ID, Direktion_Kurzbezei…, Dienststelle_Kurzbe…

## g0113（1 列）
- 見出し：Direktion_Kurzbezeichnung
- 例1 値：DPB | DIF | DSSI | DPB | BB
  - 同じ表の列：ID, Organisation_Kurzbe…, Dienststelle_Kurzbe…

## g0114（1 列）
- 見出し：Dienststelle_Kurzbezeichnung
- 例1 値：SF | SGR | SGSW | PD | ABB
  - 同じ表の列：ID, Organisation_Kurzbe…, Direktion_Kurzbezei…

## g0115（1 列）
- 見出し：PUBLISHER
- 例1 値：Oberjugendanwaltschaft des Kantons Züri… | Statistisches Amt des Kantons Zürich | Volksschulamt des Kantons Zürich | Stadt Uster | Gesundheitsdirektion des Kantons Zürich
  - 同じ表の列：ABTEILUNG, PUBLISHER_SUFFIX

## g0116（1 列）
- 見出し：ABTEILUNG
- 例1 値：Kantonale Denkmalpflege | Analysen & Studien | Kantonales Rechnungswesen | Geschäftsfeld Medizin, Abteilung Gesund… | Kantonales Labor
  - 同じ表の列：PUBLISHER, PUBLISHER_SUFFIX

## g0117（1 列）
- 見出し：PUBLISHER_SUFFIX
- 例1 値：stadt-uster | statistisches-amt-kanton-zuerich | stadt-winterthur | direktion-der-justiz-und-des-innern-kan… | aln-kanton-zuerich
  - 同じ表の列：PUBLISHER, ABTEILUNG

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
g0046	
g0047	
g0048	
g0049	
g0050	
g0052	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0063	
g0064	
g0065	
g0066	
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
```
