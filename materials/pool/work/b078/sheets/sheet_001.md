# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：year
- 例1 値：2024 | 2024 | 2022 | 2025 | 2024
  - 同じ表の列：month, chargingPower_10kW_…, chargingPower_21kW_…, chargingPower_42kW_…, chargingPower_100kW…, chargingPower_100pl…, chargingPower_AG_co…, chargingPower_AG_sum

## g0002（1 列）
- 見出し：month
- 例1 値：01 | 01 | 10 | 09 | 06
  - 同じ表の列：year, chargingPower_10kW_…, chargingPower_21kW_…, chargingPower_42kW_…, chargingPower_100kW…, chargingPower_100pl…, chargingPower_AG_co…, chargingPower_AG_sum

## g0003（1 列）
- 見出し：chargingPower_10kW_count
- 例1 値：3262 | 2683 | 2429 | 3053 | 2685
  - 同じ表の列：year, month, chargingPower_21kW_…, chargingPower_42kW_…, chargingPower_100kW…, chargingPower_100pl…, chargingPower_AG_co…, chargingPower_AG_sum

## g0004（1 列）
- 見出し：chargingPower_21kW_count
- 例1 値：704 | 2427 | 2754 | 2766 | 2265
  - 同じ表の列：year, month, chargingPower_10kW_…, chargingPower_42kW_…, chargingPower_100kW…, chargingPower_100pl…, chargingPower_AG_co…, chargingPower_AG_sum

## g0005（1 列）
- 見出し：chargingPower_42kW_count
- 例1 値：8179 | 5975 | 3210 | 7830 | 3483
  - 同じ表の列：year, month, chargingPower_10kW_…, chargingPower_21kW_…, chargingPower_100kW…, chargingPower_100pl…, chargingPower_AG_co…, chargingPower_AG_sum

## g0006（1 列）
- 見出し：chargingPower_100kW_count
- 例1 値：1240 | 1025 | 941 | 1629 | 1748
  - 同じ表の列：year, month, chargingPower_10kW_…, chargingPower_21kW_…, chargingPower_42kW_…, chargingPower_100pl…, chargingPower_AG_co…, chargingPower_AG_sum

## g0007（1 列）
- 見出し：chargingPower_100pluskW_count
- 例1 値：596 | 1515 | 1289 | 900 | 822
  - 同じ表の列：year, month, chargingPower_10kW_…, chargingPower_21kW_…, chargingPower_42kW_…, chargingPower_100kW…, chargingPower_AG_co…, chargingPower_AG_sum

## g0008（1 列）
- 見出し：chargingPower_AG_count
- 例1 値：914 | 881 | 1271 | 808 | 487
  - 同じ表の列：year, month, chargingPower_10kW_…, chargingPower_21kW_…, chargingPower_42kW_…, chargingPower_100kW…, chargingPower_100pl…, chargingPower_AG_sum

## g0009（1 列）
- 見出し：chargingPower_AG_sum
- 例1 値：42053 | 17341 | 50084 | 55405 | 31448
  - 同じ表の列：year, month, chargingPower_10kW_…, chargingPower_21kW_…, chargingPower_42kW_…, chargingPower_100kW…, chargingPower_100pl…, chargingPower_AG_co…

## g0010（1 列）
- 見出し：chargingPower_AI_count
- 例1 値：29 | 24 | 16 | 28 | 13
  - 同じ表の列：year, month, chargingPower_10kW_…, chargingPower_21kW_…, chargingPower_42kW_…, chargingPower_100kW…, chargingPower_100pl…, chargingPower_AG_co…

## g0011（7 列）
- 見出し：Jahr
- 例1 値：2017 | 2017 | 2016 | 2020 | 2020
  - 同じ表の列：Art, Raum, Typ, Subtyp, Anzahl_stuecke_exkl…
- 例2 値：2022 | 2019 | 2018 | 2020 | 2020
  - 同じ表の列：Region, Massnahmenbereich, Auszahlungen_CHF

## g0012（1 列）
- 見出し：Art
- 例1 値：leuchten | leuchten | leuchten | leuchtmittel | leuchten
  - 同じ表の列：Jahr, Raum, Typ, Subtyp, Anzahl_stuecke_exkl…

## g0013（1 列）
- 見出し：Raum
- 例1 値：innen | innen | aussen | innen | undifferenziert
  - 同じ表の列：Jahr, Art, Typ, Subtyp, Anzahl_stuecke_exkl…

## g0014（1 列）
- 見出し：Typ
- 例1 値：wandleuchten | strassenleuchten | aussenambiance | wandleuchten | notbeleuchtung
  - 同じ表の列：Jahr, Art, Raum, Subtyp, Anzahl_stuecke_exkl…

## g0015（1 列）
- 見出し：Subtyp
- 例1 値：led_eingebaut | led_eingebaut | schraub_oder_stecksockel | undifferenziert | led_eingebaut
  - 同じ表の列：Jahr, Art, Raum, Typ, Anzahl_stuecke_exkl…

## g0016（1 列）
- 見出し：Anzahl_stuecke_exkl_wiederverkauf
- 例1 値：10599088 | 1169506 | 141766 | 4391 | 467880
  - 同じ表の列：Jahr, Art, Raum, Typ, Subtyp

## g0017（1 列）
- 見出し：Region
- 例1 値：AR | TG | GE | BE | OW
  - 同じ表の列：Jahr, Massnahmenbereich, Auszahlungen_CHF

## g0018（1 列）
- 見出し：Massnahmenbereich
- 例1 値：Systemsanierung | Systemsanierung | Neubau | Haustechnik | Neubau
  - 同じ表の列：Jahr, Region, Auszahlungen_CHF

## g0019（1 列）
- 見出し：Auszahlungen_CHF
- 例1 値：4456720.00 | 10338535.00 | 7490236.40 | 814005.00 | 1362960.00
  - 同じ表の列：Jahr, Region, Massnahmenbereich

## g0020（3 列）
- 見出し：GEO_NR
- 例1 値：546 | 3215 | 2761 | 3443 | 1322
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：131 | 69 | 2 | 154 | 117
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0021（3 列）
- 見出し：CLASS_HAB
- 例1 値：2 | 1 | 2 | 1 | 2
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：3 | 4 | 2 | 2 | 2
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0022（3 列）
- 見出し：GEOM_PERIOD
- 例1 値：2021-07-01 | 2021-07-01 | 2021-07-01 | 2021-07-01 | 2021-07-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0023（1 列）
- 見出し：VARIABLE
- 例1 値：wcapt_sout | wcapt_t | deb_hj_moy | deb_hj_max | deb_hj_moy
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0024（1 列）
- 見出し：SOURCE
- 例1 値：SVGW | SVGW | SVGW | SVGW | SVGW
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0025（2 列）
- 見出し：VALUE_PERIOD
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS
- 例2 値：2020 | 2018 | 2018 | 2020 | 2020
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, STATUS

## g0026（3 列）
- 見出し：UNIT_VALUE
- 例1 値：Num | Num | Num | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, VALUE, STATUS
- 例2 値：Num | Num | Num | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, VALUE, STATUS

## g0027（2 列）
- 見出し：VALUE
- 例1 値：62775.0 | 2381.0 | 4013.0 | 351.0 | 3944.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS
- 例2 値：2048.0 | 798.9314211 | 6.0 | 4314.0 | 0.3
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, STATUS

## g0028（3 列）
- 見出し：STATUS
- 例1 値：A | O | A | O | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE
- 例2 値：O | A | A | A | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE

## g0029（1 列）
- 見出し：VARIABLE
- 例1 値：ept_bra_mas | acc_sich | etab_ecul_kun | etab_ecul_arc_bib | etab_ecul_pub
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0030（2 列）
- 見出し：SOURCE
- 例1 値：UDEMO | UDEMO | STATENT | KUWI, STATENT | KUWI, STATENT
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS
- 例2 値：MFZ, STATPOP | MFZ | MFZ | PEND, SE | MFZ
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, OBS_CONFIDENCE

## g0031（1 列）
- 見出し：VARIABLE
- 例1 値：pen_t | voit_tour | txmot | voit_tour | moto
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE, OBS_CONFIDENCE

## g0032（1 列）
- 見出し：VALUE_PERIOD
- 例1 値：2021 | 2021 | 2021 | 2021 | 2016/2020
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VALUE, VALUE, OBS_CONFIDENCE

## g0033（1 列）
- 見出し：VALUE
- 例1 値：2338 | 6306 | 102 | 86 | 50
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, OBS_CONFIDENCE

## g0034（1 列）
- 見出し：OBS_CONFIDENCE
- 例1 値：10.2 | 7.1 | 11.7 | 14.4 | 7.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE

## g0035（1 列）
- 見出し：kategorie
- 例1 値：Löschung | Auflösung infolge Konkurs | Löschung | Löschung | Neueintragung
  - 同じ表の列：publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_code, firmensitz, uid, rechtsform_code, rechtsform

## g0036（1 列）
- 見出し：publikationsdatum_shab
- 例1 値：2026-07-31 | 2026-09-08 | 2026-10-16 | 2026-10-15 | 2026-10-28
  - 同じ表の列：kategorie, journaldatum_handel…, id_shab, firmensitz_code, firmensitz, uid, rechtsform_code, rechtsform

## g0037（1 列）
- 見出し：journaldatum_handelsregister
- 例1 値：2026-09-24 | 2026-08-10 | 2026-08-25 | 2026-08-13 | 2026-08-18
  - 同じ表の列：kategorie, publikationsdatum_s…, id_shab, firmensitz_code, firmensitz, uid, rechtsform_code, rechtsform

## g0038（1 列）
- 見出し：id_shab
- 例1 値：1006721420 | 1006721416 | 1006731547 | 1006742410 | 1006790020
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, firmensitz_code, firmensitz, uid, rechtsform_code, rechtsform

## g0039（1 列）
- 見出し：firmensitz_code
- 例1 値：2775 | NaN | NaN | NaN | 2765
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz, uid, rechtsform_code, rechtsform

## g0040（1 列）
- 見出し：firmensitz
- 例1 値：Niederdorf | Binningen | Pratteln | Oberwil (BL) | Pratteln
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_code, uid, rechtsform_code, rechtsform

## g0041（1 列）
- 見出し：uid
- 例1 値：CHE303923836 | CHE216299320 | CHE210825977 | CHE198367743 | CHE411512105
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_code, firmensitz, rechtsform_code, rechtsform

## g0042（1 列）
- 見出し：rechtsform_code
- 例1 値：0107 | 0101 | 0107 | 0106 | 0107
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_code, firmensitz, uid, rechtsform

## g0043（1 列）
- 見出し：rechtsform
- 例1 値：Kollektivgesellschaft (KlG) | Einzelunternehmen | Gesellschaft mit beschränkter Haftung (… | Aktiengesellschaft (AG) | Einzelunternehmen
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_code, firmensitz, uid, rechtsform_code

## g0044（2 列）
- 見出し：egid
- 例1 値：390552 | 390791 | 390197 | 390583 | 390165
  - 同じ表の列：gemeindenummer_bfs, egrid, grundstücksnummer, koordinatenherkunft…, koordinatenherkunft…, gebaeudestatus_code, gebaeudestatus_beze…, gebaeudekategorie_c…
- 例2 値：390059 | 391031 | 391052 | 390977 | 390327
  - 同じ表の列：gemeindenummer_bfs, eidgenoessischer_ei…, eingangsnummer_geba…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0045（2 列）
- 見出し：gemeindenummer_bfs
- 例1 値：2761 | 2761 | 2761 | 2761 | 2761
  - 同じ表の列：egid, egrid, grundstücksnummer, koordinatenherkunft…, koordinatenherkunft…, gebaeudestatus_code, gebaeudestatus_beze…, gebaeudekategorie_c…
- 例2 値：2761 | 2761 | 2761 | 2761 | 2761
  - 同じ表の列：egid, eidgenoessischer_ei…, eingangsnummer_geba…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0046（1 列）
- 見出し：egrid
- 例1 値：CH927718824903 | CH543603777742 | CH707749208210 | CH244982777059 | CH367782498945
  - 同じ表の列：egid, gemeindenummer_bfs, grundstücksnummer, koordinatenherkunft…, koordinatenherkunft…, gebaeudestatus_code, gebaeudestatus_beze…, gebaeudekategorie_c…

## g0047（1 列）
- 見出し：grundstücksnummer
- 例1 値：3779 | 2448 | 1051 | 930 | 948
  - 同じ表の列：egid, gemeindenummer_bfs, egrid, koordinatenherkunft…, koordinatenherkunft…, gebaeudestatus_code, gebaeudestatus_beze…, gebaeudekategorie_c…

## g0048（1 列）
- 見出し：koordinatenherkunft_code
- 例1 値：901 | 901 | 901 | 901 | 901
  - 同じ表の列：egid, gemeindenummer_bfs, egrid, grundstücksnummer, koordinatenherkunft…, gebaeudestatus_code, gebaeudestatus_beze…, gebaeudekategorie_c…

## g0049（1 列）
- 見出し：koordinatenherkunft_bezeichnung
- 例1 値：Amtliche Vermessung, DM.01 | Amtliche Vermessung, DM.01 | Amtliche Vermessung, DM.01 | Amtliche Vermessung, DM.01 | Amtliche Vermessung, DM.01
  - 同じ表の列：egid, gemeindenummer_bfs, egrid, grundstücksnummer, koordinatenherkunft…, gebaeudestatus_code, gebaeudestatus_beze…, gebaeudekategorie_c…

## g0050（1 列）
- 見出し：gebaeudestatus_code
- 例1 値：1004 | 1004 | 1004 | 1004 | 1004
  - 同じ表の列：egid, gemeindenummer_bfs, egrid, grundstücksnummer, koordinatenherkunft…, koordinatenherkunft…, gebaeudestatus_beze…, gebaeudekategorie_c…

## g0051（1 列）
- 見出し：gebaeudestatus_bezeichnung
- 例1 値：Bestehend | Bestehend | Abgebrochen | Bestehend | Bestehend
  - 同じ表の列：egid, gemeindenummer_bfs, egrid, grundstücksnummer, koordinatenherkunft…, koordinatenherkunft…, gebaeudestatus_code, gebaeudekategorie_c…

## g0052（1 列）
- 見出し：gebaeudekategorie_code
- 例1 値：1020 | 1020 | 1020 | 1040 | 1020
  - 同じ表の列：egid, gemeindenummer_bfs, egrid, grundstücksnummer, koordinatenherkunft…, koordinatenherkunft…, gebaeudestatus_code, gebaeudestatus_beze…

## g0053（1 列）
- 見出し：gebaeudekategorie_bezeichnung
- 例1 値：Gebäude mit ausschliesslicher Wohnnutzu… | Gebäude mit ausschliesslicher Wohnnutzu… | Gebäude mit ausschliesslicher Wohnnutzu… | Gebäude mit ausschliesslicher Wohnnutzu… | Gebäude mit ausschliesslicher Wohnnutzu…
  - 同じ表の列：egid, gemeindenummer_bfs, egrid, grundstücksnummer, koordinatenherkunft…, koordinatenherkunft…, gebaeudestatus_code, gebaeudestatus_beze…

## g0054（1 列）
- 見出し：eidgenoessischer_eingangsidentifikator
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：egid, gemeindenummer_bfs, eingangsnummer_geba…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0055（1 列）
- 見出し：eingangsnummer_gebaeude
- 例1 値：167 | 62 | 8 | 20 | 46
  - 同じ表の列：egid, gemeindenummer_bfs, eidgenoessischer_ei…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0056（1 列）
- 見出し：strassenbezeichnung
- 例1 値：Bahnhofstrasse | Schartenfluhweg | Bahnhofstrasse | Im Häslirain | Spitzenrainweg
  - 同じ表の列：egid, gemeindenummer_bfs, eidgenoessischer_ei…, eingangsnummer_geba…, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0057（1 列）
- 見出し：strassenbezeichnung_kurz
- 例1 値：Dornacherstr. | Im Egg | Dornacherstr. | Steinackerstr. | Ahornweg
  - 同じ表の列：egid, gemeindenummer_bfs, eidgenoessischer_ei…, eingangsnummer_geba…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0058（1 列）
- 見出し：strassenbezeichnung_index
- 例1 値：And | Mey | Fie | Sem | Zie
  - 同じ表の列：egid, gemeindenummer_bfs, eidgenoessischer_ei…, eingangsnummer_geba…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0059（1 列）
- 見出し：strassenbezeichnung_offiziell_code
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：egid, gemeindenummer_bfs, eidgenoessischer_ei…, eingangsnummer_geba…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0060（1 列）
- 見出し：strassenbezeichnung_offiziell_bezeichnung
- 例1 値：ja | ja | ja | ja | ja
  - 同じ表の列：egid, gemeindenummer_bfs, eidgenoessischer_ei…, eingangsnummer_geba…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0061（1 列）
- 見出し：postleitzahl
- 例1 値：4147 | 4147 | 4147 | 4147 | 4147
  - 同じ表の列：egid, gemeindenummer_bfs, eidgenoessischer_ei…, eingangsnummer_geba…, strassenbezeichnung, strassenbezeichnung…, strassenbezeichnung…, strassenbezeichnung…

## g0062（1 列）
- 見出し：Veranstaltungstag
- 例1 値：2026-02-04 | 2027-04-27 | 2027-11-17 | 2026-04-25 | 2026-06-21
  - 同じ表の列：Kategorie, Termin-ID, Veranstaltung-ID, Code, Aktiv-Code, Wiederkehrend-Code, Start der Erfassung, Jahr

## g0063（1 列）
- 見出し：Kategorie
- 例1 値：Kultur und Unterhaltung | Sport | Ferien | Ferien | Ferien
  - 同じ表の列：Veranstaltungstag, Termin-ID, Veranstaltung-ID, Code, Aktiv-Code, Wiederkehrend-Code, Start der Erfassung, Jahr

## g0064（1 列）
- 見出し：Termin-ID
- 例1 値：3870 | 3846 | 3846 | 3870 | 3869
  - 同じ表の列：Veranstaltungstag, Kategorie, Veranstaltung-ID, Code, Aktiv-Code, Wiederkehrend-Code, Start der Erfassung, Jahr

## g0065（1 列）
- 見出し：Veranstaltung-ID
- 例1 値：184 | 63 | 184 | 184 | 77
  - 同じ表の列：Veranstaltungstag, Kategorie, Termin-ID, Code, Aktiv-Code, Wiederkehrend-Code, Start der Erfassung, Jahr

## g0066（1 列）
- 見出し：Code
- 例1 値：hilsa | semf | stimfe | semf | stimfe
  - 同じ表の列：Veranstaltungstag, Kategorie, Termin-ID, Veranstaltung-ID, Aktiv-Code, Wiederkehrend-Code, Start der Erfassung, Jahr

## g0067（1 列）
- 見出し：Aktiv-Code
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Veranstaltungstag, Kategorie, Termin-ID, Veranstaltung-ID, Code, Wiederkehrend-Code, Start der Erfassung, Jahr

## g0068（1 列）
- 見出し：Wiederkehrend-Code
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Veranstaltungstag, Kategorie, Termin-ID, Veranstaltung-ID, Code, Aktiv-Code, Start der Erfassung, Jahr

## g0069（1 列）
- 見出し：Start der Erfassung
- 例1 値：2007-01-01 | 2006-01-01 | 2007-01-01 | 2007-01-01 | 2007-01-01
  - 同じ表の列：Veranstaltungstag, Kategorie, Termin-ID, Veranstaltung-ID, Code, Aktiv-Code, Wiederkehrend-Code, Jahr

## g0070（1 列）
- 見出し：Dauer in Tagen
- 例1 値：65 | 389 | 22 | 389 | 6
  - 同じ表の列：Veranstaltungstag, Kategorie, Termin-ID, Veranstaltung-ID, Code, Aktiv-Code, Wiederkehrend-Code, Start der Erfassung

## g0071（1 列）
- 見出し：Basel;10;47.55775627101952
- 例1 値：Bettingen;30;47.570375216112126 | Basel;10;47.55775627101952 | Riehen;20;47.579448855581205 | Bettingen;30;47.570375216112126 | Riehen;20;47.579448855581205
  - 同じ表の列：7.593600950306357;"…, 47.564366], [7.5573, 47.565031], [7.558265, 47.567247], [7.559335, 47.569389]

## g0072（1 列）
- 見出し：7.593600950306357;"{""coordinates"": [[[7.55466
- 例1 値：7.672205414795705;"{""coordinates"": [[… | 7.672205414795705;"{""coordinates"": [[… | 7.672205414795705;"{""coordinates"": [[… | 7.672205414795705;"{""coordinates"": [[… | 7.672205414795705;"{""coordinates"": [[…
  - 同じ表の列：Basel;10;47.5577562…, 47.564366], [7.5573, 47.565031], [7.558265, 47.567247], [7.559335, 47.569389]

## g0073（1 列）
- 見出し：47.564366]
- 例1 値：47.562116] | 47.562116] | 47.573414] | 47.564366] | 47.564366]
  - 同じ表の列：Basel;10;47.5577562…, 7.593600950306357;"…, [7.5573, 47.565031], [7.558265, 47.567247], [7.559335, 47.569389]

## g0074（1 列）
- 見出し：[7.5573
- 例1 値：[7.623389 | [7.65251 | [7.5573 | [7.5573 | [7.623389
  - 同じ表の列：Basel;10;47.5577562…, 7.593600950306357;"…, 47.564366], 47.565031], [7.558265, 47.567247], [7.559335, 47.569389]

## g0075（1 列）
- 見出し：47.565031]
- 例1 値：47.575366] | 47.565031] | 47.56221] | 47.56221] | 47.565031]
  - 同じ表の列：Basel;10;47.5577562…, 7.593600950306357;"…, 47.564366], [7.5573, [7.558265, 47.567247], [7.559335, 47.569389]

## g0076（1 列）
- 見出し：[7.558265
- 例1 値：[7.627023 | [7.558265 | [7.652572 | [7.558265 | [7.652572
  - 同じ表の列：Basel;10;47.5577562…, 7.593600950306357;"…, 47.564366], [7.5573, 47.565031], 47.567247], [7.559335, 47.569389]

## g0077（1 列）
- 見出し：47.567247]
- 例1 値：47.577351] | 47.562251] | 47.562251] | 47.577351] | 47.577351]
  - 同じ表の列：Basel;10;47.5577562…, 7.593600950306357;"…, 47.564366], [7.5573, 47.565031], [7.558265, [7.559335, 47.569389]

## g0078（1 列）
- 見出し：[7.559335
- 例1 値：[7.652635 | [7.652635 | [7.626118 | [7.626118 | [7.626118
  - 同じ表の列：Basel;10;47.5577562…, 7.593600950306357;"…, 47.564366], [7.5573, 47.565031], [7.558265, 47.567247], 47.569389]

## g0079（1 列）
- 見出し：47.569389]
- 例1 値：47.57811] | 47.562291] | 47.57811] | 47.569389] | 47.57811]
  - 同じ表の列：Basel;10;47.5577562…, 7.593600950306357;"…, 47.564366], [7.5573, 47.565031], [7.558265, 47.567247], [7.559335

## g0080（1 列）
- 見出し：[7.556464
- 例1 値：[7.625212 | [7.625212 | [7.625212 | [7.652698 | [7.625212
  - 同じ表の列：Basel;10;47.5577562…, 7.593600950306357;"…, 47.564366], [7.5573, 47.565031], [7.558265, 47.567247], [7.559335

## g0081（1 列）
- 見出し：Monat
- 例1 値：2026-09 | 2026-09 | 2026-09 | 2026-09 | 2026-09
  - 同じ表の列：Wochentag, Start Zeitspanne, Ende Zeitspanne, Gemeinde, Wohnviertel-ID, Wohnviertel, Bezirks-ID, Bezirk

## g0082（1 列）
- 見出し：Wochentag
- 例1 値：2 | 0 | 5 | 1 | 0
  - 同じ表の列：Monat, Start Zeitspanne, Ende Zeitspanne, Gemeinde, Wohnviertel-ID, Wohnviertel, Bezirks-ID, Bezirk

## g0083（1 列）
- 見出し：Start Zeitspanne
- 例1 値：00:00 | 00:00 | 00:00 | 00:00 | 00:00
  - 同じ表の列：Monat, Wochentag, Ende Zeitspanne, Gemeinde, Wohnviertel-ID, Wohnviertel, Bezirks-ID, Bezirk

## g0084（1 列）
- 見出し：Ende Zeitspanne
- 例1 値：03:00 | 03:00 | 03:00 | 03:00 | 03:00
  - 同じ表の列：Monat, Wochentag, Start Zeitspanne, Gemeinde, Wohnviertel-ID, Wohnviertel, Bezirks-ID, Bezirk

## g0085（1 列）
- 見出し：Gemeinde
- 例1 値：Basel | Basel | Basel | Basel | Basel
  - 同じ表の列：Monat, Wochentag, Start Zeitspanne, Ende Zeitspanne, Wohnviertel-ID, Wohnviertel, Bezirks-ID, Bezirk

## g0086（1 列）
- 見出し：Wohnviertel-ID
- 例1 値：4 | 3 | 5 | 1 | 4
  - 同じ表の列：Monat, Wochentag, Start Zeitspanne, Ende Zeitspanne, Gemeinde, Wohnviertel, Bezirks-ID, Bezirk

## g0087（1 列）
- 見出し：Wohnviertel
- 例1 値：Hirzbrunnen | Bruderholz | Gundeldingen | Vorstädte | Am Ring
  - 同じ表の列：Monat, Wochentag, Start Zeitspanne, Ende Zeitspanne, Gemeinde, Wohnviertel-ID, Bezirks-ID, Bezirk

## g0088（1 列）
- 見出し：Bezirks-ID
- 例1 値：14 | 42 | 115 | 114 | 24
  - 同じ表の列：Monat, Wochentag, Start Zeitspanne, Ende Zeitspanne, Gemeinde, Wohnviertel-ID, Wohnviertel, Bezirk

## g0089（1 列）
- 見出し：Bezirk
- 例1 値：Kannenfeld | Alban | St.Johann | Spalen | Spalen
  - 同じ表の列：Monat, Wochentag, Start Zeitspanne, Ende Zeitspanne, Gemeinde, Wohnviertel-ID, Wohnviertel, Bezirks-ID

## g0090（1 列）
- 見出し：Fahrzeugtyp
- 例1 値：bicycle | SCOOTER | SCOOTER | bicycle | E-Bike
  - 同じ表の列：Monat, Wochentag, Start Zeitspanne, Ende Zeitspanne, Gemeinde, Wohnviertel-ID, Wohnviertel, Bezirks-ID

## g0091（3 列）
- 見出し：BFS_NR_GEMEINDE
- 例1 値：4721 | 4791 | 4741 | 4441 | 4621
  - 同じ表の列：BEZIRK_NR, JAHR, KONFESSION_CODE, KONFESSION_BEZEICHN…, ANZAHL_PERSONEN
- 例2 値：4901 | 4411 | 4476 | 4891 | 4826
  - 同じ表の列：POLITISCHE_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_0_19, EINWOHNER_20_39

## g0092（2 列）
- 見出し：BEZIRK_NR
- 例1 値：2011 | 2015 | 2015 | 2014 | 2012
  - 同じ表の列：BFS_NR_GEMEINDE, JAHR, KONFESSION_CODE, KONFESSION_BEZEICHN…, ANZAHL_PERSONEN
- 例2 値：2014 | 2014 | 2014 | 2012 | 2015
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_0_19, EINWOHNER_20_39

## g0093（1 列）
- 見出し：KONFESSION_CODE
- 例1 値：0 | 0 | 111 | 0 | 0
  - 同じ表の列：BFS_NR_GEMEINDE, BEZIRK_NR, JAHR, KONFESSION_BEZEICHN…, ANZAHL_PERSONEN

## g0094（1 列）
- 見出し：KONFESSION_BEZEICHNUNG
- 例1 値：Römisch-katholisch | Evangelisch-reformiert | Römisch-katholisch | Evangelisch-reformiert | Römisch-katholisch
  - 同じ表の列：BFS_NR_GEMEINDE, BEZIRK_NR, JAHR, KONFESSION_CODE, ANZAHL_PERSONEN

## g0095（1 列）
- 見出し：ANZAHL_PERSONEN
- 例1 値：991 | 178 | 636 | 243 | 253
  - 同じ表の列：BFS_NR_GEMEINDE, BEZIRK_NR, JAHR, KONFESSION_CODE, KONFESSION_BEZEICHN…

## g0096（1 列）
- 見出し：POLITISCHE_GEMEINDE
- 例1 値：Zihlschlacht-Sitterdorf | Kradolf-Schönenberg | Bussnang | Affeltrangen | Fischingen
  - 同じ表の列：BFS_NR_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_0_19, EINWOHNER_20_39

## g0097（1 列）
- 見出し：ORTSCHAFT
- 例1 値：Raperswilen | Eschenz | Matzingen | Illighausen | Nussbaumen
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, BEZIRK_NR, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_0_19, EINWOHNER_20_39

## g0098（1 列）
- 見出し：EINWOHNER_TOTAL
- 例1 値：314 | 3849 | 414 | 4480 | x
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_0_19, EINWOHNER_20_39

## g0099（1 列）
- 見出し：EINWOHNER_MAENNER
- 例1 値：457 | x | x | 479 | x
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_FRAUEN, EINWOHNER_0_19, EINWOHNER_20_39

## g0100（1 列）
- 見出し：EINWOHNER_FRAUEN
- 例1 値：5663 | x | 12751 | 35 | x
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_0_19, EINWOHNER_20_39

## g0101（1 列）
- 見出し：EINWOHNER_0_19
- 例1 値：171 | 195 | 351 | 277 | 84
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_20_39

## g0102（1 列）
- 見出し：EINWOHNER_20_39
- 例1 値：65 | 496 | 630 | 360 | 36
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_0_19

## g0103（1 列）
- 見出し：EINWOHNER_40_64
- 例1 値：251 | 74 | 7 | 15 | 79
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_0_19

## g0104（1 列）
- 見出し：datum
- 例1 値：2004-02-08 | 2012-09-23 | 2022-11-27 | 2011-10-23 | 2016-06-05
  - 同じ表の列：bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer, bezirk, stimmberechtigte, stiausweiseurne, stiausweisevorzeitig, stiausweisebriefgue…

## g0105（1 列）
- 見出し：gemeinde
- 例1 値：Märstetten | Kreuzlingen | Ermatingen | Münchwilen | Erlen
  - 同じ表の列：datum, bfs_nr_gemeinde, bfs_bezirksnummer, bezirk, stimmberechtigte, stiausweiseurne, stiausweisevorzeitig, stiausweisebriefgue…

## g0106（1 列）
- 見出し：bfs_bezirksnummer
- 例1 値：2012 | 2014 | 2014 | 2011 | 2015
  - 同じ表の列：datum, bfs_nr_gemeinde, gemeinde, bezirk, stimmberechtigte, stiausweiseurne, stiausweisevorzeitig, stiausweisebriefgue…

## g0107（1 列）
- 見出し：bezirk
- 例1 値：Frauenfeld | Arbon | Arbon | Frauenfeld | Weinfelden
  - 同じ表の列：datum, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer, stimmberechtigte, stiausweiseurne, stiausweisevorzeitig, stiausweisebriefgue…

## g0108（1 列）
- 見出し：stimmberechtigte
- 例1 値：971 | 1790 | 2429 | 648 | 828
  - 同じ表の列：datum, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer, bezirk, stiausweiseurne, stiausweisevorzeitig, stiausweisebriefgue…

## g0109（1 列）
- 見出し：stiausweiseurne
- 例1 値：453 | 123 | 328 | 164 | 85
  - 同じ表の列：datum, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer, bezirk, stimmberechtigte, stiausweisevorzeitig, stiausweisebriefgue…

## g0110（1 列）
- 見出し：stiausweisevorzeitig
- 例1 値：0 | 0 | 0 | 29 | 9
  - 同じ表の列：datum, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer, bezirk, stimmberechtigte, stiausweiseurne, stiausweisebriefgue…

## g0111（1 列）
- 見出し：stiausweisebriefgueltig
- 例1 値：324 | 222 | 1508 | 2316 | 120
  - 同じ表の列：datum, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer, bezirk, stimmberechtigte, stiausweiseurne, stiausweisevorzeitig

## g0112（1 列）
- 見出し：stiausweisebriefniuz
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：datum, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer, bezirk, stimmberechtigte, stiausweiseurne, stiausweisevorzeitig

## g0113（1 列）
- 見出し：Monat_Jahr
- 例1 値：2026-09 | 2025-08 | 2025-10 | 2025-09 | 2026-04
  - 同じ表の列：Abfallfraktion, Unterkategorie, Entsorgungsart, Abfuhrgebiet, Annahmestelle, Deponie Anlieferung, Gewicht in kg, Gewicht in t

## g0114（1 列）
- 見出し：Abfallfraktion
- 例1 値：Karton | Papier | Papier | Karton | Altmetall
  - 同じ表の列：Monat_Jahr, Unterkategorie, Entsorgungsart, Abfuhrgebiet, Annahmestelle, Deponie Anlieferung, Gewicht in kg, Gewicht in t

## g0115（1 列）
- 見出し：Unterkategorie
- 例1 値：Infektiöse Abfälle | Braunglas | Grünglas | Infektiöse Abfälle | Altmedikamente
  - 同じ表の列：Monat_Jahr, Abfallfraktion, Entsorgungsart, Abfuhrgebiet, Annahmestelle, Deponie Anlieferung, Gewicht in kg, Gewicht in t

## g0116（1 列）
- 見出し：Entsorgungsart
- 例1 値：Strassensammlung | Strassensammlung | Strassensammlung | Strassensammlung | Strassensammlung
  - 同じ表の列：Monat_Jahr, Abfallfraktion, Unterkategorie, Abfuhrgebiet, Annahmestelle, Deponie Anlieferung, Gewicht in kg, Gewicht in t

## g0117（1 列）
- 見出し：Abfuhrgebiet
- 例1 値：I | I | I | A | B
  - 同じ表の列：Monat_Jahr, Abfallfraktion, Unterkategorie, Entsorgungsart, Annahmestelle, Deponie Anlieferung, Gewicht in kg, Gewicht in t

## g0118（1 列）
- 見出し：Annahmestelle
- 例1 値：Apotheken / Drogerien | RE West | RE West | Apotheken / Drogerien | Sammelstellen
  - 同じ表の列：Monat_Jahr, Abfallfraktion, Unterkategorie, Entsorgungsart, Abfuhrgebiet, Deponie Anlieferung, Gewicht in kg, Gewicht in t

## g0119（1 列）
- 見出し：Deponie Anlieferung
- 例1 値：Privatanlieferer | Privatanlieferer | Privatanlieferer | Privatanlieferer | Privatanlieferer
  - 同じ表の列：Monat_Jahr, Abfallfraktion, Unterkategorie, Entsorgungsart, Abfuhrgebiet, Annahmestelle, Gewicht in kg, Gewicht in t

## g0120（1 列）
- 見出し：Gewicht in kg
- 例1 値：4500.0 | 2920.0 | 4050.0 | 5740.0 | 4190.0
  - 同じ表の列：Monat_Jahr, Abfallfraktion, Unterkategorie, Entsorgungsart, Abfuhrgebiet, Annahmestelle, Deponie Anlieferung, Gewicht in t

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
