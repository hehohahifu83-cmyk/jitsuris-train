# ラベル用シート 001 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：valueCategory
- 例1 値：cases | cases | cases | cases | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0002（1 列）
- 見出し：temporal
- 例1 値：2020 | 2022 | 2025 | 2014 | 2016
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0003（3 列）
- 見出し：temporal_type
- 例1 値：year | year | year | year | year
  - 同じ表の列：valueCategory, temporal, georegion, georegion_type, agegroup, agegroup_type, sex, value
- 例2 値：month | year | month | month | year
  - 同じ表の列：valueCategory, temporal, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0004（2 列）
- 見出し：georegion
- 例1 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, value
- 例2 値：CHFL | SG | BS | UR | BL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, value

## g0005（3 列）
- 見出し：georegion_type
- 例1 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, value
- 例2 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, value

## g0006（1 列）
- 見出し：agegroup
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, value

## g0007（3 列）
- 見出し：agegroup_type
- 例1 値：agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, value
- 例2 値：agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, value

## g0008（3 列）
- 見出し：sex
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, value
- 例2 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, value

## g0009（3 列）
- 見出し：value
- 例1 値：65 | 40 | 64 | 45 | 40
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex
- 例2 値：40 | 26 | 21 | 19 | 32
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0010（1 列）
- 見出し：pop
- 例1 値：8275032 | 9091915 | 8176760 | 8457360 | 8364748
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0011（2 列）
- 見出し：valueCategory
- 例1 値：cases | max_value_5y | cases | cases | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value
- 例2 値：cases | median_value_5y | median_value_5y | min_value_5y | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0012（2 列）
- 見出し：temporal
- 例1 値：2020-M10 | 2017 | 2023-M05 | 2016 | 2018
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value
- 例2 値：2018 | 2026-M07 | 2020-M03 | 2025-M11 | 2025-M04
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0013（1 列）
- 見出し：georegion
- 例1 値：CHFL | CHFL | CHFL | région_lémanique | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, value

## g0014（2 列）
- 見出し：agegroup
- 例1 値：all | all | all | 45 - 54 | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, value
- 例2 値：all | 17 - 24 | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, value

## g0015（2 列）
- 見出し：pop
- 例1 値：9091915 | NA | 8176760 | NA | 9091915
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex
- 例2 値：NA | 711232 | 36819 | 8855062 | 8855062
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0016（1 列）
- 見出し：Messort_Code
- 例1 値：207 | 188 | 33 | 77 | 71
  - 同じ表の列：Messort_Typ, X_LV95, Y_LV95, Messintervall, Gemeinde

## g0017（1 列）
- 見出し：Messort_Typ
- 例1 値：Schulhaus | Schulhaus | Schulhaus | Schulhaus | Schulhaus
  - 同じ表の列：Messort_Code, X_LV95, Y_LV95, Messintervall, Gemeinde

## g0018（1 列）
- 見出し：X_LV95
- 例1 値：2682361 | 2674415 | 2674747 | 2700638 | 2700104
  - 同じ表の列：Messort_Code, Messort_Typ, Y_LV95, Messintervall, Gemeinde

## g0019（1 列）
- 見出し：Y_LV95
- 例1 値：1264523 | 1255711 | 1248196 | 1245889 | 1236642
  - 同じ表の列：Messort_Code, Messort_Typ, X_LV95, Messintervall, Gemeinde

## g0020（1 列）
- 見出し：Messintervall
- 例1 値：Einmalige Messung | Einmalige Messung | Einmalige Messung | Einmalige Messung | Einmalige Messung
  - 同じ表の列：Messort_Code, Messort_Typ, X_LV95, Y_LV95, Gemeinde

## g0021（1 列）
- 見出し：Gemeinde
- 例1 値：Bonstetten | Esslingen | Stadt Zürich | Höri | Bachs
  - 同じ表の列：Messort_Code, Messort_Typ, X_LV95, Y_LV95, Messintervall

## g0022（1 列）
- 見出し：site
- 例1 値：7a | 4 | 4 | 1 | 4
  - 同じ表の列：parameter, value, unit

## g0023（1 列）
- 見出し：parameter
- 例1 値：latitude | latitude | magl | latitude | magl
  - 同じ表の列：site, value, unit

## g0024（1 列）
- 見出し：value
- 例1 値：2702797 | 2701041 | 2702426 | 4 | 8.788527321
  - 同じ表の列：site, parameter, unit

## g0025（1 列）
- 見出し：unit
- 例1 値：m | m | ° | m | m
  - 同じ表の列：site, parameter, value

## g0026（1 列）
- 見出し：starttime
- 例1 値：2020-03-01T10:30:00+01:00 | 2020-03-03T17:40:00+01:00 | 2020-03-05T23:30:00+01:00 | 2020-03-02T21:40:00+01:00 | 2020-03-01T17:20:00+01:00
  - 同じ表の列：parameter, unit

## g0027（1 列）
- 見出し：parameter
- 例1 値：PN[5-100nm] | PN[5-100nm] | PN[5-100nm] | PN[5-100nm] | PN[5-100nm]
  - 同じ表の列：starttime, unit

## g0028（1 列）
- 見出し：unit
- 例1 値：#/cm3 | #/cm3 | #/cm3 | #/cm3 | #/cm3
  - 同じ表の列：starttime, parameter

## g0029（3 列）
- 見出し：stand
- 例1 値：2026-10-30 | 2026-10-30 | 2026-10-30 | 2026-10-30 | 2026-10-30
  - 同じ表の列：kanton, jahr, schultraeger_code, schultraeger, schultraeger_typ, staatsangehoerigkeit, staatsangehoerigkei…, anzahl
- 例2 値：2026-10-30 | 2026-10-30 | 2026-10-30 | 2026-10-30 | 2026-10-30
  - 同じ表の列：kanton, jahr, stufe, mittelschultyp, bildungsart, finanzierung, staatsangehoerigkeit, anzahl

## g0030（3 列）
- 見出し：kanton
- 例1 値：zh | zh | zh | zh | zh
  - 同じ表の列：stand, jahr, schultraeger_code, schultraeger, schultraeger_typ, staatsangehoerigkeit, staatsangehoerigkei…, anzahl
- 例2 値：zh | zh | zh | zh | zh
  - 同じ表の列：stand, jahr, stufe, mittelschultyp, bildungsart, finanzierung, staatsangehoerigkeit, anzahl

## g0031（8 列）
- 見出し：jahr
- 例1 値：2025 | 2025 | 2025 | 2025 | 2025
  - 同じ表の列：stand, kanton, schultraeger_code, schultraeger, schultraeger_typ, staatsangehoerigkeit, staatsangehoerigkei…, anzahl
- 例2 値：2023 | 2024 | 2025 | 2023 | 2023
  - 同じ表の列：stand, kanton, stufe, mittelschultyp, bildungsart, finanzierung, staatsangehoerigkeit, anzahl

## g0032（1 列）
- 見出し：schultraeger_code
- 例1 値：C050 | L062 | L022 | C020 | M040
  - 同じ表の列：stand, kanton, jahr, schultraeger, schultraeger_typ, staatsangehoerigkeit, staatsangehoerigkei…, anzahl

## g0033（1 列）
- 見出し：schultraeger
- 例1 値：Grüningen | Affoltern a.A.-Aeugst | Hombrechtikon | Aeugst a.A. | Adliswil
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger_typ, staatsangehoerigkeit, staatsangehoerigkei…, anzahl

## g0034（1 列）
- 見出し：schultraeger_typ
- 例1 値：Gemeindezusammenschluss Primarschul- un… | Einheitsgemeinde (politisch, Primar- un… | Einheitsgemeinde (politisch, Primar- un… | Einheitsgemeinde (politisch, Primar- un… | Einheitsgemeinde (politisch, Primar- un…
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger, staatsangehoerigkeit, staatsangehoerigkei…, anzahl

## g0035（1 列）
- 見出し：staatsangehoerigkeit
- 例1 値：Italien | Restliches Europa | Irak | Türkiye | Italien
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger, schultraeger_typ, staatsangehoerigkei…, anzahl

## g0036（1 列）
- 見出し：staatsangehoerigkeit_iso2_code
- 例1 値：UA | RO | SI | RO | SK
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger, schultraeger_typ, staatsangehoerigkeit, anzahl

## g0037（5 列）
- 見出し：anzahl
- 例1 値：15 | 8 | 16 | 8 | 6
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger, schultraeger_typ, staatsangehoerigkeit, staatsangehoerigkei…
- 例2 値：8 | 661 | 2 | 5 | 5
  - 同じ表の列：stand, kanton, jahr, stufe, mittelschultyp, bildungsart, finanzierung, staatsangehoerigkeit

## g0038（2 列）
- 見出し：obs_status
- 例1 値：A | Q | A | A | A
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger, schultraeger_typ, staatsangehoerigkeit, staatsangehoerigkei…
- 例2 値：A | A | A | A | A
  - 同じ表の列：PERIOD, INDICATOR, DIMENSION, UNIT_MEA, VALUE, OBS_STATUS_2

## g0039（2 列）
- 見出し：stufe
- 例1 値：Sekundarstufe II | Sekundarstufe I | Sekundarstufe I | Sekundarstufe II | Sekundarstufe II
  - 同じ表の列：stand, kanton, jahr, mittelschultyp, bildungsart, finanzierung, staatsangehoerigkeit, anzahl
- 例2 値：Sekundarstufe II | Sekundarstufe I | Sekundarstufe II | Sekundarstufe I | Sekundarstufe II
  - 同じ表の列：stand, kanton, jahr, schultyp, staatsangehoerigkeit, traegerschaft, finanzierung, anzahl

## g0040（1 列）
- 見出し：mittelschultyp
- 例1 値：Gymnasium | Gymnasium | Gymnasium | Handelsmittelschule | Gymnasium
  - 同じ表の列：stand, kanton, jahr, stufe, bildungsart, finanzierung, staatsangehoerigkeit, anzahl

## g0041（1 列）
- 見出し：bildungsart
- 例1 値：SPF Alte Sprachen | SPF Alte Sprachen | Fachmaturität Gesundheit/Naturwissensch… | SPF Bildnerisches Gestalten | SPF Eine moderne Sprache
  - 同じ表の列：stand, kanton, jahr, stufe, mittelschultyp, finanzierung, staatsangehoerigkeit, anzahl

## g0042（2 列）
- 見出し：finanzierung
- 例1 値：priv | priv | priv | priv | oef
  - 同じ表の列：stand, kanton, jahr, stufe, mittelschultyp, bildungsart, staatsangehoerigkeit, anzahl
- 例2 値：priv | oef | oef | oef | oef
  - 同じ表の列：stand, kanton, jahr, stufe, schultyp, staatsangehoerigkeit, traegerschaft, anzahl

## g0043（2 列）
- 見出し：staatsangehoerigkeit
- 例1 値：Ausland | Schweiz | Ausland | Schweiz | Ausland
  - 同じ表の列：stand, kanton, jahr, stufe, mittelschultyp, bildungsart, finanzierung, anzahl
- 例2 値：Ausland | Ausland | Schweiz | Schweiz | Ausland
  - 同じ表の列：stand, kanton, jahr, stufe, schultyp, traegerschaft, finanzierung, anzahl

## g0044（1 列）
- 見出し：schultyp
- 例1 値：Berufsfachschule | Berufsfachschule | Mittelschule | Heim- und Sonderschule | Heim- und Sonderschule
  - 同じ表の列：stand, kanton, jahr, stufe, staatsangehoerigkeit, traegerschaft, finanzierung, anzahl

## g0045（1 列）
- 見出し：traegerschaft
- 例1 値：priv | priv | priv | oef | priv
  - 同じ表の列：stand, kanton, jahr, stufe, schultyp, staatsangehoerigkeit, finanzierung, anzahl

## g0046（1 列）
- 見出し：reportDate
- 例1 値：2026-01-27T00:00:00 | 2026-01-14T00:00:00 | 2026-01-12T00:00:00 | 2026-01-08T00:00:00 | 2026-01-16T00:00:00
  - 同じ表の列：canton, municipality, diseasesGroup_de, diseasesGroup_fr, diseasesGroup_it, diseasesGroup_en, diseases_de, diseases_fr

## g0047（2 列）
- 見出し：canton
- 例1 値：FR | GR | NE | JU | LU
  - 同じ表の列：reportDate, municipality, diseasesGroup_de, diseasesGroup_fr, diseasesGroup_it, diseasesGroup_en, diseases_de, diseases_fr
- 例2 値：AG | SG | BL | BE | VD
  - 同じ表の列：year, diseasesGroup, diseases, species, count

## g0048（1 列）
- 見出し：municipality
- 例1 値：Rossemaison | Buchholterberg | Erlen | Avry | Teufen (AR)
  - 同じ表の列：reportDate, canton, diseasesGroup_de, diseasesGroup_fr, diseasesGroup_it, diseasesGroup_en, diseases_de, diseases_fr

## g0049（1 列）
- 見出し：diseasesGroup_de
- 例1 値：Zu bekämpfende Seuchen | Zu überwachende Seuchen | Zu bekämpfende Seuchen | Zu bekämpfende Seuchen | Zu bekämpfende Seuchen
  - 同じ表の列：reportDate, canton, municipality, diseasesGroup_fr, diseasesGroup_it, diseasesGroup_en, diseases_de, diseases_fr

## g0050（1 列）
- 見出し：diseasesGroup_fr
- 例1 値：Epizooties à surveiller | Epizooties à combattre | Epizooties à surveiller | Epizooties à combattre | Epizooties à combattre
  - 同じ表の列：reportDate, canton, municipality, diseasesGroup_de, diseasesGroup_it, diseasesGroup_en, diseases_de, diseases_fr

## g0051（1 列）
- 見出し：diseasesGroup_it
- 例1 値：Epizoozie da combattere | Epizoozie da combattere | Epizoozie da combattere | Epizoozie da combattere | Epizoozie da combattere
  - 同じ表の列：reportDate, canton, municipality, diseasesGroup_de, diseasesGroup_fr, diseasesGroup_en, diseases_de, diseases_fr

## g0052（1 列）
- 見出し：diseasesGroup_en
- 例1 値：Epidemics to be supervised | Epidemics to be fought | Epidemics to be fought | Epidemics to be fought | Epidemics to be fought
  - 同じ表の列：reportDate, canton, municipality, diseasesGroup_de, diseasesGroup_fr, diseasesGroup_it, diseases_de, diseases_fr

## g0053（1 列）
- 見出し：diseases_de
- 例1 値：Blauzungenkrankheit (Bluetongue) | Blauzungenkrankheit (Bluetongue) | Moderhinke | Blauzungenkrankheit (Bluetongue) | Blauzungenkrankheit (Bluetongue)
  - 同じ表の列：reportDate, canton, municipality, diseasesGroup_de, diseasesGroup_fr, diseasesGroup_it, diseasesGroup_en, diseases_fr

## g0054（1 列）
- 見出し：diseases_fr
- 例1 値：Toxoplasmose | Fièvre catarrhale du mouton (blue tongu… | Fièvre catarrhale du mouton (blue tongu… | Fièvre catarrhale du mouton (blue tongu… | Fièvre catarrhale du mouton (blue tongu…
  - 同じ表の列：reportDate, canton, municipality, diseasesGroup_de, diseasesGroup_fr, diseasesGroup_it, diseasesGroup_en, diseases_de

## g0055（1 列）
- 見出し：diseases_it
- 例1 値：Febbre catarrale ovina (Blue tongue o «… | Febbre catarrale ovina (Blue tongue o «… | Zoppina | Febbre catarrale ovina (Blue tongue o «… | Zoppina
  - 同じ表の列：reportDate, canton, municipality, diseasesGroup_de, diseasesGroup_fr, diseasesGroup_it, diseasesGroup_en, diseases_de

## g0056（1 列）
- 見出し：Nr (abs)
- 例1 値：20827 | 20816 | 20908 | 20787 | 20791
  - 同じ表の列：Milchproduktkategor…, Beschreibung, Proben-Nr. extern, Datum Probenahme, Bemerkung generell, Produktionsland, PFBA [ug/kg], PFPeA [ug/kg]

## g0057（1 列）
- 見出し：Milchproduktkategorie
- 例1 値：Halbhartkäse | Rahm | Halbhartkäse | Halbhartkäse | Rahm
  - 同じ表の列：Nr (abs), Beschreibung, Proben-Nr. extern, Datum Probenahme, Bemerkung generell, Produktionsland, PFBA [ug/kg], PFPeA [ug/kg]

## g0058（1 列）
- 見出し：Beschreibung
- 例1 値：Butter | Mozzarella | Mozzarella | Bio Halbrahm, 28% Milchfett | Butter, bio
  - 同じ表の列：Nr (abs), Milchproduktkategor…, Proben-Nr. extern, Datum Probenahme, Bemerkung generell, Produktionsland, PFBA [ug/kg], PFPeA [ug/kg]

## g0059（1 列）
- 見出し：Proben-Nr. extern
- 例1 値：39 | 171 | 30 | 164 | 89
  - 同じ表の列：Nr (abs), Milchproduktkategor…, Beschreibung, Datum Probenahme, Bemerkung generell, Produktionsland, PFBA [ug/kg], PFPeA [ug/kg]

## g0060（1 列）
- 見出し：Datum Probenahme
- 例1 値：2025-03-26T00:00:00 | 2025-03-29T00:00:00 | 2025-03-15T00:00:00 | 2025-03-26T00:00:00 | 2025-03-26T00:00:00
  - 同じ表の列：Nr (abs), Milchproduktkategor…, Beschreibung, Proben-Nr. extern, Bemerkung generell, Produktionsland, PFBA [ug/kg], PFPeA [ug/kg]

## g0061（1 列）
- 見出し：Bemerkung generell
- 例1 値：IT | CH | IT | CH | CH
  - 同じ表の列：Nr (abs), Milchproduktkategor…, Beschreibung, Proben-Nr. extern, Datum Probenahme, Produktionsland, PFBA [ug/kg], PFPeA [ug/kg]

## g0062（1 列）
- 見出し：Produktionsland
- 例1 値：Schweiz | Schweiz | Schweiz | Italien | Schweiz
  - 同じ表の列：Nr (abs), Milchproduktkategor…, Beschreibung, Proben-Nr. extern, Datum Probenahme, Bemerkung generell, PFBA [ug/kg], PFPeA [ug/kg]

## g0063（1 列）
- 見出し：PFBA [ug/kg]
- 例1 値：<0.05 | <0.05 | <0.05 | <0.05 | <0.05
  - 同じ表の列：Nr (abs), Milchproduktkategor…, Beschreibung, Proben-Nr. extern, Datum Probenahme, Bemerkung generell, Produktionsland, PFPeA [ug/kg]

## g0064（1 列）
- 見出し：PFPeA [ug/kg]
- 例1 値：<0.05 | <0.05 | <0.05 | <0.05 | <0.05
  - 同じ表の列：Nr (abs), Milchproduktkategor…, Beschreibung, Proben-Nr. extern, Datum Probenahme, Bemerkung generell, Produktionsland, PFBA [ug/kg]

## g0065（1 列）
- 見出し：PFHxA [ug/kg]
- 例1 値：<0.05 | <0.05 | <0.05 | <0.05 | <0.05
  - 同じ表の列：Nr (abs), Milchproduktkategor…, Beschreibung, Proben-Nr. extern, Datum Probenahme, Bemerkung generell, Produktionsland, PFBA [ug/kg]

## g0066（1 列）
- 見出し：year
- 例1 値：1997 | 1996 | 1991 | 1992 | 1991
  - 同じ表の列：canton, diseasesGroup, diseases, species, count

## g0067（1 列）
- 見出し：diseasesGroup
- 例1 値：Epidemics to be supervised | Epidemics to be eradicated | Epidemics to be fought | Epidemics to be fought | Epidemics to be supervised
  - 同じ表の列：year, canton, diseases, species, count

## g0068（1 列）
- 見出し：diseases
- 例1 値：Blackleg | European foulbrood of honey bees | Rabies | Rabies | American foulbrood of honey bees
  - 同じ表の列：year, canton, diseasesGroup, species, count

## g0069（1 列）
- 見出し：species
- 例1 値：Cattle | Pigeon | Cattle | Dog | Cattle
  - 同じ表の列：year, canton, diseasesGroup, diseases, count

## g0070（1 列）
- 見出し：count
- 例1 値：1 | 1 | 1 | 5 | 1
  - 同じ表の列：year, canton, diseasesGroup, diseases, species

## g0071（2 列）
- 見出し：parameter_group_de
- 例1 値：Niederschlag | Niederschlag | Niederschlag | Niederschlag | Niederschlag
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Strahlung | Temperatur | Feuchte | Wind | Wind
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0072（1 列）
- 見出し：parameter_group_fr
- 例1 値：Pr馗ipitations | Pr馗ipitations | Pr馗ipitations | Pr馗ipitations | Pr馗ipitations
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0073（1 列）
- 見出し：parameter_group_it
- 例1 値：Precipitazioni | Precipitazioni | Precipitazioni | Precipitazioni | Precipitazioni
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0074（2 列）
- 見出し：parameter_group_en
- 例1 値：Precipitation | Precipitation | Precipitation | Precipitation | Precipitation
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Wind | Sunshine | Temperature | Temperature | Radiation
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0075（2 列）
- 見出し：parameter_granularity
- 例1 値：M | Y | D | D | T
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Y | T | H | Y | M
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_decimals, parameter_datatype, parameter_unit

## g0076（2 列）
- 見出し：parameter_decimals
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit
- 例2 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit

## g0077（2 列）
- 見出し：parameter_datatype
- 例1 値：Float | Float | Float | Float | Float
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_unit
- 例2 値：Float | Float | Integer | Float | Float
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_unit

## g0078（1 列）
- 見出し：parameter_unit
- 例1 値：mm | mm | mm | mm | mm
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0079（1 列）
- 見出し：parameter_group_fr
- 例1 値：Température | Température | Température | Température | Ensoleillement
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0080（1 列）
- 見出し：parameter_group_it
- 例1 値：Temperatura | Soleggiamento | Vento | Temperatura | Umidità
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0081（1 列）
- 見出し：parameter_unit
- 例1 値：°C | W/m2 | km/h | km/h | min
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0082（1 列）
- 見出し：AC
- 例1 値：2013 | 2010 | 2010 | 2012 | 2010
  - 同じ表の列：Settimana, Fine, Eta, Num_Decessi, Atteso, Lim_inf, Lim_sup, Eccessi

## g0083（1 列）
- 見出し：Settimana
- 例1 値：19 | 11 | 20 | 16 | 1
  - 同じ表の列：AC, Fine, Eta, Num_Decessi, Atteso, Lim_inf, Lim_sup, Eccessi

## g0084（1 列）
- 見出し：Fine
- 例1 値：08.05.2016 | 24.08.2014 | 13.04.2014 | 15.09.2019 | 01.09.2019
  - 同じ表の列：AC, Settimana, Eta, Num_Decessi, Atteso, Lim_inf, Lim_sup, Eccessi

## g0085（1 列）
- 見出し：Eta
- 例1 値：0-64 | 0-64 | 0-64 | 65+ | 0-64
  - 同じ表の列：AC, Settimana, Fine, Num_Decessi, Atteso, Lim_inf, Lim_sup, Eccessi

## g0086（1 列）
- 見出し：Num_Decessi
- 例1 値：161 | 945 | 159 | 169 | 147
  - 同じ表の列：AC, Settimana, Fine, Eta, Atteso, Lim_inf, Lim_sup, Eccessi

## g0087（1 列）
- 見出し：Atteso
- 例1 値：165 | 182 | 167 | 950 | 958
  - 同じ表の列：AC, Settimana, Fine, Eta, Num_Decessi, Lim_inf, Lim_sup, Eccessi

## g0088（1 列）
- 見出し：Lim_inf
- 例1 値：136 | 1097 | 139 | 133 | 893
  - 同じ表の列：AC, Settimana, Fine, Eta, Num_Decessi, Atteso, Lim_sup, Eccessi

## g0089（1 列）
- 見出し：Lim_sup
- 例1 値：1246 | 206 | 1193 | 1359 | 985
  - 同じ表の列：AC, Settimana, Fine, Eta, Num_Decessi, Atteso, Lim_inf, Eccessi

## g0090（1 列）
- 見出し：Eccessi
- 例1 値：1572 | 1237 | 1227 | 1377 | 232
  - 同じ表の列：AC, Settimana, Fine, Eta, Num_Decessi, Atteso, Lim_inf, Lim_sup

## g0091（1 列）
- 見出し：PERIOD
- 例1 値：2018-04-01/2018-10-01 | 2005-10-01/2006-04-01 | 2018-04-01/2018-10-01 | 2012-04-01/2012-10-01 | 2014-04-01/2014-10-01
  - 同じ表の列：INDICATOR, DIMENSION, UNIT_MEA, VALUE, OBS_STATUS, OBS_STATUS_2

## g0092（1 列）
- 見出し：INDICATOR
- 例1 値：30106_ind01 | 30106_ind01 | 30106_ind01 | 30106_ind01 | 30106_ind01
  - 同じ表の列：PERIOD, DIMENSION, UNIT_MEA, VALUE, OBS_STATUS, OBS_STATUS_2

## g0093（1 列）
- 見出し：DIMENSION
- 例1 値：30106_dim02 | 30106_dim06 | 30106_T | 30106_dim16 | 30106_dim14
  - 同じ表の列：PERIOD, INDICATOR, UNIT_MEA, VALUE, OBS_STATUS, OBS_STATUS_2

## g0094（1 列）
- 見出し：UNIT_MEA
- 例1 値：Percent | Percent | Percent | Percent | Percent
  - 同じ表の列：PERIOD, INDICATOR, DIMENSION, VALUE, OBS_STATUS, OBS_STATUS_2

## g0095（2 列）
- 見出し：VALUE
- 例1 値：53.1 | 9.74117647058823 | 98.7 | 55.7 | 73.1
  - 同じ表の列：PERIOD, INDICATOR, DIMENSION, UNIT_MEA, OBS_STATUS, OBS_STATUS_2
- 例2 値：93.42545789 | 2.414964173 | 5.031838771 | 136.9 | 4.988716
  - 同じ表の列：PERIOD_REF, PERIOD_COMP, REGION, INDICATORS, UNIT_MES, STATUS, STATUS_1

## g0096（1 列）
- 見出し：OBS_STATUS_2
- 例1 値：B | B | B | B | B
  - 同じ表の列：PERIOD, INDICATOR, DIMENSION, UNIT_MEA, VALUE, OBS_STATUS

## g0097（1 列）
- 見出し：PERIOD_REF
- 例1 値：1979/1985 | 2019 | 2018 | 2019 | 2019
  - 同じ表の列：PERIOD_COMP, REGION, INDICATORS, UNIT_MES, VALUE, STATUS, STATUS_1

## g0098（1 列）
- 見出し：PERIOD_COMP
- 例1 値：2004/2009 | 2004/2009 | 2004/2009 | 2004/2009 | 2004/2009
  - 同じ表の列：PERIOD_REF, REGION, INDICATORS, UNIT_MES, VALUE, STATUS, STATUS_1

## g0099（1 列）
- 見出し：REGION
- 例1 値：GL | GL | SZ | OW | SZ
  - 同じ表の列：PERIOD_REF, PERIOD_COMP, INDICATORS, UNIT_MES, VALUE, STATUS, STATUS_1

## g0100（1 列）
- 見出し：INDICATORS
- 例1 値：Ind_04_01 | Ind_01_08 | Ind_13_02 | Ind_01_03 | Ind_13_04
  - 同じ表の列：PERIOD_REF, PERIOD_COMP, REGION, UNIT_MES, VALUE, STATUS, STATUS_1

## g0101（1 列）
- 見出し：UNIT_MES
- 例1 値：UM_5 | UM_2 | UM_2 | UM_2 | UM_2
  - 同じ表の列：PERIOD_REF, PERIOD_COMP, REGION, INDICATORS, VALUE, STATUS, STATUS_1

## g0102（7 列）
- 見出し：STATUS
- 例1 値：A | A | A | A | A
  - 同じ表の列：PERIOD_REF, PERIOD_COMP, REGION, INDICATORS, UNIT_MES, VALUE, STATUS_1
- 例2 値：abgeschlossen | Abgeschlossen | abgeschlossen | abgeschlossen | Abgeschlossen
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, geschaeftsnummer, grg_nummer, geschaftstitel, geschaftsart, kennung, sachbegriff_grgeko_1

## g0103（1 列）
- 見出し：STATUS_1
- 例1 値：P | P | P | P | P
  - 同じ表の列：PERIOD_REF, PERIOD_COMP, REGION, INDICATORS, UNIT_MES, VALUE, STATUS

## g0104（1 列）
- 見出し：gremium_kategorie
- 例1 値：Kommissionen | Kommissionen | Kommissionen | Spezialkommissionen | Kommissionen
  - 同じ表の列：gremium_id

## g0105（1 列）
- 見出し：gremium_id
- 例1 値：3f3f84e9f1264556899c9b11ab06f9cb | 3f3f84e9f1264556899c9b11ab06f9cb | 7e8394ffeb8d4ef4b2a49ee221efc51c | 9bedd4394ace48eca08752a9e355d1cc | 3d8015ae09124a7781c1e6588833d0d5
  - 同じ表の列：gremium_kategorie

## g0106（3 列）
- 見出し：Datum
- 例1 値：2026-10-25 | 2026-10-29 | 2026-10-26 | 2026-10-29 | 2026-10-29
  - 同じ表の列：Datensatztitel, Datensatz ID, Visitors, Interactions
- 例2 値：2025-11-30 | 2026-09-27 | 2025-11-30 | 2026-03-08 | 2026-09-27
  - 同じ表の列：bfsnr, gemeinde, politischerkreis, quartiergruppen, altersklassen, teilgenommen, nicht_teilgenommen, stimmbeteiligung

## g0107（1 列）
- 見出し：Datensatztitel
- 例1 値：Eidgenössische und kantonale Wahlen: Ka… | Landratswahlen: Wahlkreise | OGD-Portal: Tägliche Nutzung nach Daten… | Bewohnte Wohnungen nach Bewohnertyp, Ge… | Apotheken mit Betriebsbewilligung oder …
  - 同じ表の列：Datum, Datensatz ID, Visitors, Interactions

## g0108（1 列）
- 見出し：Datensatz ID
- 例1 値：12200 | 12990 | 10350 | 12610 | 12070
  - 同じ表の列：Datum, Datensatztitel, Visitors, Interactions

## g0109（1 列）
- 見出し：Visitors
- 例1 値：3 | 3 | 11 | 17 | 9
  - 同じ表の列：Datum, Datensatztitel, Datensatz ID, Interactions

## g0110（1 列）
- 見出し：Interactions
- 例1 値：2 | 12 | 10 | 83 | 12
  - 同じ表の列：Datum, Datensatztitel, Datensatz ID, Visitors

## g0111（1 列）
- 見出し：Anfangszeit
- 例1 値：2026-10-11T04:00:00+00:00 | 2026-10-24T15:00:00+00:00 | 2026-10-23T09:00:00+00:00 | 2026-10-10T00:30:00+00:00 | 2026-10-27T15:30:00+00:00
  - 同じ表の列：Temperatur, Druck, Feuchte

## g0112（1 列）
- 見出し：Temperatur
- 例1 値：12.852 | 7.9051 | 21.53 | 8.5547 | 6.0567
  - 同じ表の列：Anfangszeit, Druck, Feuchte

## g0113（1 列）
- 見出し：Druck
- 例1 値：989.48 | 988.69 | 987.83 | 982.81 | 989.69
  - 同じ表の列：Anfangszeit, Temperatur, Feuchte

## g0114（1 列）
- 見出し：Feuchte
- 例1 値：100.0 | 96.206 | 91.147 | 100.0 | 84.466
  - 同じ表の列：Anfangszeit, Temperatur, Druck

## g0115（1 列）
- 見出し：Temperatur
- 例1 値：11 | 27 | 21 | 11 | 20
  - 同じ表の列：Zeit, Koordinaten

## g0116（1 列）
- 見出し：Zeit
- 例1 値：2024-11-26T03:45:03+00:00 | 2024-12-04T11:00:08+00:00 | 2024-11-30T20:30:06+00:00 | 2024-11-24T21:45:03+00:00 | 2024-11-27T20:00:15+00:00
  - 同じ表の列：Temperatur, Koordinaten

## g0117（2 列）
- 見出し：Koordinaten
- 例1 値：47.570688, 7.613675 | 47.570491, 7.61478 | 47.570848, 7.61543 | 47.570491, 7.61478 | 47.562072, 7.557569
  - 同じ表の列：Temperatur, Zeit
- 例2 値：47.556941563208895, 8.898625498429137 | 47.559405799496446, 8.899641893040318 | 47.55458733996604, 8.899255682034969 | 47.559405799496446, 8.899641893040318 | 47.559405799496446, 8.899641893040318
  - 同じ表の列：zeit_von, zeit_bis, belegung, inflow, outflow, median_standzeit

## g0118（2 列）
- 見出し：Geo Point
- 例1 値：47.55581919145133, 7.590342914327154 | 47.55729455281475, 7.586954243042777 | 47.55553082442547, 7.590140457807997 | 47.555686736520336, 7.588739701227188 | 47.55512732277671, 7.588347018843152
  - 同じ表の列：Geo Shape, Fussgängerzonen-ID, Regime, Zum Objekt navigier…
- 例2 値：47.552567118976285, 7.59335833293789 | 47.562969582301, 7.597649630679965 | 47.562324144105176, 7.59570792697212 | 47.55779146806161, 7.589674418935021 | 47.552905554813066, 7.588370883848422
  - 同じ表の列：Geo Shape, Objekt-ID, Infos, Zufahrt, Zum Objekt navigier…

## g0119（2 列）
- 見出し：Geo Shape
- 例1 値：{"coordinates": [[[7.590740106990192, 4… | {"coordinates": [[[7.586705685763728, 4… | {"coordinates": [[[7.587760666756755, 4… | {"coordinates": [[[7.589198970151025, 4… | {"coordinates": [[[7.589478035488302, 4…
  - 同じ表の列：Geo Point, Fussgängerzonen-ID, Regime, Zum Objekt navigier…
- 例2 値：{"coordinates": [[[7.592234657243623, 4… | {"coordinates": [[[7.596971742897135, 4… | {"coordinates": [[[7.594647883042579, 4… | {"coordinates": [[[7.588712113188724, 4… | {"coordinates": [[[7.588330345162404, 4…
  - 同じ表の列：Geo Point, Objekt-ID, Infos, Zufahrt, Zum Objekt navigier…

## g0120（1 列）
- 見出し：Fussgängerzonen-ID
- 例1 値：34 | 31 | 23 | 8 | 22
  - 同じ表の列：Geo Point, Geo Shape, Regime, Zum Objekt navigier…

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
