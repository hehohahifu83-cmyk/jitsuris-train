# ラベル用シート 001 / 004

- LABEL_GUIDE v2.1 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：valueCategory
- 例1 値：cases | max_value_5y | cases | cases | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type
- 例2 値：cases | cases | max_value_5y | min_value_5y | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0002（3 列）
- 見出し：temporal
- 例1 値：2023-M05 | 2024-M06 | 2020 | 2025-M12 | 2021-M10
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type
- 例2 値：2018-M07 | 2022 | 2015 | 2016-M03 | 2018-M07
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0003（3 列）
- 見出し：temporal_type
- 例1 値：year | year | month | month | month
  - 同じ表の列：valueCategory, temporal, georegion, georegion_type, agegroup, agegroup_type, sex, type
- 例2 値：month | year | year | month | month
  - 同じ表の列：valueCategory, temporal, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0004（3 列）
- 見出し：georegion
- 例1 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, type
- 例2 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, value

## g0005（3 列）
- 見出し：georegion_type
- 例1 値：grossregion | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, type
- 例2 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, value

## g0006（3 列）
- 見出し：agegroup
- 例1 値：all | all | all | 0 - 14 | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, type
- 例2 値：35 - 44 | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, value

## g0007（3 列）
- 見出し：agegroup_type
- 例1 値：agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, type
- 例2 値：agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, value

## g0008（3 列）
- 見出し：sex
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, type
- 例2 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, value

## g0009（1 列）
- 見出し：type
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0010（3 列）
- 見出し：value
- 例1 値：89 | 63 | 177 | 3 | 732
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex
- 例2 値：215 | 97 | 215 | 339 | 234
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0011（1 列）
- 見出し：valueCategory
- 例1 値：cases | cases | cases | cases | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0012（2 列）
- 見出し：pop
- 例1 値：NA | 913352 | 1188040 | NA | 1236387
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex
- 例2 値：NA | 1210345 | 8327126 | 39055 | 4140131
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0013（1 列）
- 見出し：site
- 例1 値：Reutlenweg | Kindergarten Geissberg | Schulhaus Feld | Stadtplatz Kloten | Friedhof Chloos
  - 同じ表の列：x_lv95, y_lv95, site_altitude_masl, sensor_id, sensor_height_magl, transect_code, wd_max_ufp, datetime_installed

## g0014（1 列）
- 見出し：x_lv95
- 例1 値：2686274.5 | 2687216 | 2688846.2 | 2686836.8 | 2686332.5
  - 同じ表の列：site, y_lv95, site_altitude_masl, sensor_id, sensor_height_magl, transect_code, wd_max_ufp, datetime_installed

## g0015（1 列）
- 見出し：y_lv95
- 例1 値：1256638.8 | 1256701.4 | 1257367.6 | 1257197.6 | 1256170.2
  - 同じ表の列：site, x_lv95, site_altitude_masl, sensor_id, sensor_height_magl, transect_code, wd_max_ufp, datetime_installed

## g0016（1 列）
- 見出し：site_altitude_masl
- 例1 値：439 | 456 | 458 | 508 | 444
  - 同じ表の列：site, x_lv95, y_lv95, sensor_id, sensor_height_magl, transect_code, wd_max_ufp, datetime_installed

## g0017（1 列）
- 見出し：sensor_id
- 例1 値：8505 | 8506 | 8511 | 8499 | 8514
  - 同じ表の列：site, x_lv95, y_lv95, site_altitude_masl, sensor_height_magl, transect_code, wd_max_ufp, datetime_installed

## g0018（1 列）
- 見出し：sensor_height_magl
- 例1 値：2.55 | 5.55 | 2.75 | 2.7 | 3.6
  - 同じ表の列：site, x_lv95, y_lv95, site_altitude_masl, sensor_id, transect_code, wd_max_ufp, datetime_installed

## g0019（1 列）
- 見出し：transect_code
- 例1 値：C0 | A3 | B1 | B3 | A4
  - 同じ表の列：site, x_lv95, y_lv95, site_altitude_masl, sensor_id, sensor_height_magl, wd_max_ufp, datetime_installed

## g0020（1 列）
- 見出し：wd_max_ufp
- 例1 値：258.75 | 270 | 247.5 | 303.75 | 292.5
  - 同じ表の列：site, x_lv95, y_lv95, site_altitude_masl, sensor_id, sensor_height_magl, transect_code, datetime_installed

## g0021（1 列）
- 見出し：datetime_installed
- 例1 値：2025-03-07T15:00:00+0100 | 2025-02-25T11:00:00+0100 | 2025-03-07T11:00:00+0100 | 2025-03-04T11:00:00+0100 | 2025-02-14T16:00:00+0100
  - 同じ表の列：site, x_lv95, y_lv95, site_altitude_masl, sensor_id, sensor_height_magl, transect_code, wd_max_ufp

## g0022（1 列）
- 見出し：dp
- 例1 値：10.37 | 72.34 | 119.71 | 327.81 | 83.54
  - 同じ表の列：dp_lower, dp_upper

## g0023（1 列）
- 見出し：dp_lower
- 例1 値：23.71 | 153.99 | 74.99 | 33.98 | 25.48
  - 同じ表の列：dp, dp_upper

## g0024（1 列）
- 見出し：dp_upper
- 例1 値：107.46 | 56.23 | 29.43 | 80.58 | 339.82
  - 同じ表の列：dp, dp_lower

## g0025（12 列）
- 見出し：jahr
- 例1 値：1995 | 2001 | 2017 | 2009 | 1991
  - 同じ表の列：hauptgruppe, untergruppe, nfr, thg, thg_agg, quelle, einheit, einheit_lang
- 例2 値：2025 | 2025 | 2025 | 2025 | 2024
  - 同じ表の列：stand, kanton, schulgemeinde, anforderungstyp, anzahl, obs_status

## g0026（1 列）
- 見出し：hauptgruppe
- 例1 値：Abwasser und Abfall | Abwasser und Abfall | Abwasser und Abfall | Landwirtschaft | Abwasser und Abfall
  - 同じ表の列：jahr, untergruppe, nfr, thg, thg_agg, quelle, einheit, einheit_lang

## g0027（1 列）
- 見出し：untergruppe
- 例1 値：Abfalldeponie | Fermentation bei der Verdauung | Abwasserbehandlung | Fermentation bei der Verdauung | Abwasserbehandlung
  - 同じ表の列：jahr, hauptgruppe, nfr, thg, thg_agg, quelle, einheit, einheit_lang

## g0028（1 列）
- 見出し：nfr
- 例1 値：5C | 5D | 3B | 5A | 3A
  - 同じ表の列：jahr, hauptgruppe, untergruppe, thg, thg_agg, quelle, einheit, einheit_lang

## g0029（1 列）
- 見出し：thg
- 例1 値：CO2 | CH4 | HFC | HFC | HFC
  - 同じ表の列：jahr, hauptgruppe, untergruppe, nfr, thg_agg, quelle, einheit, einheit_lang

## g0030（1 列）
- 見出し：thg_agg
- 例1 値：CO2eq | CO2eq | CO2eq | CO2eq | CO2eq
  - 同じ表の列：jahr, hauptgruppe, untergruppe, nfr, thg, quelle, einheit, einheit_lang

## g0031（2 列）
- 見出し：quelle
- 例1 値：Region | Region | Region | Region | Region
  - 同じ表の列：jahr, hauptgruppe, untergruppe, nfr, thg, thg_agg, einheit, einheit_lang
- 例2 値：Wasserversorgung | Wasserversorgung | Wasserversorgung | Wasserversorgung | Wasserversorgung
  - 同じ表の列：jahr, datum, gemeinde_nummer, bezirk_nummer, verteilzone, analyt, kategorie, kategorie_sortierung

## g0032（1 列）
- 見出し：einheit
- 例1 値：t/a | t/a | t/a | t/a | t/a
  - 同じ表の列：jahr, hauptgruppe, untergruppe, nfr, thg, thg_agg, quelle, einheit_lang

## g0033（1 列）
- 見出し：einheit_lang
- 例1 値：Tonnen pro Jahr | Tonnen pro Jahr | Tonnen pro Jahr | Tonnen pro Jahr | Tonnen pro Jahr
  - 同じ表の列：jahr, hauptgruppe, untergruppe, nfr, thg, thg_agg, quelle, einheit

## g0034（1 列）
- 見出し：stand
- 例1 値：2026 | 2026 | 2026 | 2026 | 2026
  - 同じ表の列：jahr, hauptgruppe, untergruppe, nfr, thg, thg_agg, quelle, einheit

## g0035（3 列）
- 見出し：stand
- 例1 値：2026-10-28 | 2026-10-28 | 2026-10-28 | 2026-10-28 | 2026-10-28
  - 同じ表の列：kanton, jahr, schulgemeinde, anforderungstyp, anzahl, obs_status
- 例2 値：2026-10-28 | 2026-10-28 | 2026-10-28 | 2026-10-28 | 2026-10-28
  - 同じ表の列：kanton, jahr, staatsangehoerigkeit, staatsangehoerigkei…, anzahl

## g0036（4 列）
- 見出し：kanton
- 例1 値：zh | zh | zh | zh | zh
  - 同じ表の列：stand, jahr, schulgemeinde, anforderungstyp, anzahl, obs_status
- 例2 値：zh | zh | zh | zh | zh
  - 同じ表の列：stand, jahr, staatsangehoerigkeit, staatsangehoerigkei…, anzahl

## g0037（1 列）
- 見出し：schulgemeinde
- 例1 値：Volketswil | Hinwil | Wangen-Brüttisellen | Rüschlikon | Embrach
  - 同じ表の列：stand, kanton, jahr, anforderungstyp, anzahl, obs_status

## g0038（1 列）
- 見出し：anforderungstyp
- 例1 値：Sek B | Sek A | Sek B | Sek B | Heim-/Sonderschulung
  - 同じ表の列：stand, kanton, jahr, schulgemeinde, anzahl, obs_status

## g0039（3 列）
- 見出し：anzahl
- 例1 値：60 | 129 | 346 | 100 | 27
  - 同じ表の列：stand, kanton, jahr, schulgemeinde, anforderungstyp, obs_status
- 例2 値：338 | 247 | 194 | 13 | 578
  - 同じ表の列：stand, kanton, jahr, staatsangehoerigkeit, staatsangehoerigkei…

## g0040（3 列）
- 見出し：obs_status
- 例1 値：A | A | A | A | A
  - 同じ表の列：stand, kanton, jahr, schulgemeinde, anforderungstyp, anzahl
- 例2 値：A | A | A | A | A
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger, schultraegertyp, erstsprache, anzahl

## g0041（1 列）
- 見出し：staatsangehoerigkeit
- 例1 値：Syrien | Philippinen | Schweiz | Korea (Süd-) | Armenien
  - 同じ表の列：stand, kanton, jahr, staatsangehoerigkei…, anzahl

## g0042（1 列）
- 見出し：staatsangehoerigkeit_iso2_code
- 例1 値：EG | TH | TW | PH | SL
  - 同じ表の列：stand, kanton, jahr, staatsangehoerigkeit, anzahl

## g0043（1 列）
- 見出し：schultraeger_code
- 例1 値：B052 | X710 | G122 | C070 | M161
  - 同じ表の列：stand, kanton, jahr, schultraeger, schultraegertyp, erstsprache, anzahl, obs_status

## g0044（1 列）
- 見出し：schultraeger
- 例1 値：Benken | Elgg | Dättlikon | Rheinau | Seuzach
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraegertyp, erstsprache, anzahl, obs_status

## g0045（1 列）
- 見出し：schultraegertyp
- 例1 値：Gemeindezusammenschluss Primarschul- un… | Gemeindezusammenschluss Primarschul- un… | Primarschulgemeinde | Einheitsgemeinde (politisch, Primar- un… | Gemeindezusammenschluss Primarschul- un…
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger, erstsprache, anzahl, obs_status

## g0046（1 列）
- 見出し：erstsprache
- 例1 値：Deutsch | Übrige Sprachen | Deutsch | Übrige Sprachen | Deutsch
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger, schultraegertyp, anzahl, obs_status

## g0047（1 列）
- 見出し：Typologie
- 例1 値：K211 | K231 | K121 | K231 | K212
  - 同じ表の列：Kanton, Status, Institution, Ort, Notfalldienst, Infrastruktur1, Infrastruktur2, Infrastruktur3

## g0048（1 列）
- 見出し：Status
- 例1 値：öffentlich oder subventioniert | öffentlich oder subventioniert | öffentlich oder subventioniert | privat | öffentlich oder subventioniert
  - 同じ表の列：Kanton, Typologie, Institution, Ort, Notfalldienst, Infrastruktur1, Infrastruktur2, Infrastruktur3

## g0049（1 列）
- 見出し：Institution
- 例1 値：Beth Shalom Drogenentzug und Therapievo… | Klinik SGM Langenthal | Hôpital Intercantonal de la Broye (HIB)… | Klinik Pyramide am See AG | Hôpital de la Riviera ­ A, soins aigus
  - 同じ表の列：Kanton, Typologie, Status, Ort, Notfalldienst, Infrastruktur1, Infrastruktur2, Infrastruktur3

## g0050（1 列）
- 見出し：Ort
- 例1 値：1211 Genève 14 | 4054 Basel | 6083 Hasliberg Hohfluh | 9016 St. Gallen | 1110 Morges
  - 同じ表の列：Kanton, Typologie, Status, Institution, Notfalldienst, Infrastruktur1, Infrastruktur2, Infrastruktur3

## g0051（1 列）
- 見出し：Notfalldienst
- 例1 値：Nein | Ja | Nein | Nein | Ja
  - 同じ表の列：Kanton, Typologie, Status, Institution, Ort, Infrastruktur1, Infrastruktur2, Infrastruktur3

## g0052（1 列）
- 見出し：Infrastruktur1
- 例1 値：CT | CT | CT | CT | CT
  - 同じ表の列：Kanton, Typologie, Status, Institution, Ort, Notfalldienst, Infrastruktur2, Infrastruktur3

## g0053（1 列）
- 見出し：Infrastruktur2
- 例1 値：LITO | LITO | LITO | LITO | LITO
  - 同じ表の列：Kanton, Typologie, Status, Institution, Ort, Notfalldienst, Infrastruktur1, Infrastruktur3

## g0054（1 列）
- 見出し：Infrastruktur3
- 例1 値：MRI | MRI | MRI | MRI | MRI
  - 同じ表の列：Kanton, Typologie, Status, Institution, Ort, Notfalldienst, Infrastruktur1, Infrastruktur2

## g0055（1 列）
- 見出し：Infrastruktur4
- 例1 値：PET | PET | PET | PET | PET
  - 同じ表の列：Kanton, Typologie, Status, Institution, Ort, Notfalldienst, Infrastruktur1, Infrastruktur2

## g0056（1 列）
- 見出し：Category
- 例1 値：Farm animals | Farm animals | Pets | Farm animals | Pets
  - 同じ表の列：Species, Prescription type, Category of use, Year, Animal treatments, Animal treatments w…, Animal treatments p…, Animal treatments w…

## g0057（1 列）
- 見出し：Species
- 例1 値：Pigs | Poultry | Rabbits | Poultry | Poultry
  - 同じ表の列：Category, Prescription type, Category of use, Year, Animal treatments, Animal treatments w…, Animal treatments p…, Animal treatments w…

## g0058（1 列）
- 見出し：Prescription type
- 例1 値：All prescription types | All prescription types | All prescription types | All prescription types | All prescription types
  - 同じ表の列：Category, Species, Category of use, Year, Animal treatments, Animal treatments w…, Animal treatments p…, Animal treatments w…

## g0059（1 列）
- 見出し：Category of use
- 例1 値：Game animals | Cattle rearing and fattening | Game animals | Fattening pigs and giltsm | Laying hens
  - 同じ表の列：Category, Species, Prescription type, Year, Animal treatments, Animal treatments w…, Animal treatments p…, Animal treatments w…

## g0060（1 列）
- 見出し：Year
- 例1 値：2023 | 2023 | 2023 | 2021 | 2021
  - 同じ表の列：Category, Species, Prescription type, Category of use, Animal treatments, Animal treatments w…, Animal treatments p…, Animal treatments w…

## g0061（1 列）
- 見出し：Animal treatments
- 例1 値：11018670 | 22602 | 235775 | 21100 | 14283
  - 同じ表の列：Category, Species, Prescription type, Category of use, Year, Animal treatments w…, Animal treatments p…, Animal treatments w…

## g0062（1 列）
- 見出し：Animal treatments with critical antibiotics
- 例1 値：13430 | 2094 | 11783 | 100639 | 5
  - 同じ表の列：Category, Species, Prescription type, Category of use, Year, Animal treatments, Animal treatments p…, Animal treatments w…

## g0063（1 列）
- 見出し：Animal treatments per 1000
- 例1 値：35.93 | 48.17 | 39.83 | 22.35 | 26.99
  - 同じ表の列：Category, Species, Prescription type, Category of use, Year, Animal treatments, Animal treatments w…, Animal treatments w…

## g0064（1 列）
- 見出し：Animal treatments with critical antibiotics per 1000
- 例1 値：81.78 | 68.9 | 11.2 | 3.13 | 3.72
  - 同じ表の列：Category, Species, Prescription type, Category of use, Year, Animal treatments, Animal treatments w…, Animal treatments p…

## g0065（1 列）
- 見出し：Total animal numbers across production cycles
- 例1 値：26588 | 265975 | 4958978 | 552085 | 4462704
  - 同じ表の列：Category, Species, Prescription type, Category of use, Year, Animal treatments, Animal treatments w…, Animal treatments p…

## g0066（1 列）
- 見出し：ID
- 例1 値：group8 | group3 | group2 | group7 | group4
  - 同じ表の列：DE, FR, IT, EN

## g0067（1 列）
- 見出し：DE
- 例1 値：Kindernahrung | Alle | Getreide | Getränke | Gemüse
  - 同じ表の列：ID, FR, IT, EN

## g0068（1 列）
- 見出し：FR
- 例1 値：Autres | Légumes | Huiles végétales | Fruits | Tous
  - 同じ表の列：ID, DE, IT, EN

## g0069（1 列）
- 見出し：IT
- 例1 値：Bevande | Tutti | Frutta | Alimenti per l'infanzia | Oli vegetali
  - 同じ表の列：ID, DE, FR, EN

## g0070（1 列）
- 見出し：EN
- 例1 値：Fruits | Animal fats | Cereals | Other | Vegetable oils
  - 同じ表の列：ID, DE, FR, IT

## g0071（1 列）
- 見出し：YearWeekIso
- 例1 値：202443 | 202451 | 202443 | 202451 | 202449
  - 同じ表の列：LastDayOfWeek, Variable, Number

## g0072（1 列）
- 見出し：LastDayOfWeek
- 例1 値：2025-01-12 | 2025-02-02 | 2025-01-26 | 2024-12-15 | 2025-01-05
  - 同じ表の列：YearWeekIso, Variable, Number

## g0073（1 列）
- 見出し：Variable
- 例1 値：farms_examined_negative_count | farms_total_count | farms_examined_negative_count | farms_examined_count | farms_total_count
  - 同じ表の列：YearWeekIso, LastDayOfWeek, Number

## g0074（1 列）
- 見出し：Number
- 例1 値：12159 | 3114 | 6394 | 3915 | 202
  - 同じ表の列：YearWeekIso, LastDayOfWeek, Variable

## g0075（1 列）
- 見出し：parameter_group_de
- 例1 値：Phänologie | Phänologie | Phänologie | Phänologie | Phänologie
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0076（1 列）
- 見出し：parameter_group_fr
- 例1 値：Phénologie | Phénologie | Phénologie | Phénologie | Phénologie
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0077（2 列）
- 見出し：parameter_group_it
- 例1 値：Fenologia | Fenologia | Fenologia | Fenologia | Fenologia
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Precipitazioni | Radiazione | Pressione | Vento | Vento
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0078（2 列）
- 見出し：parameter_group_en
- 例1 値：Phenology | Phenology | Phenology | Phenology | Phenology
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Temperature | Temperature | Radiation | Temperature | Temperature
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0079（2 列）
- 見出し：parameter_granularity
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：D | Y | D | Y | D
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_decimals, parameter_datatype, parameter_unit

## g0080（2 列）
- 見出し：parameter_decimals
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit
- 例2 値：0 | 1 | 0 | 0 | 1
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit

## g0081（2 列）
- 見出し：parameter_datatype
- 例1 値：Integer | Integer | Integer | Integer | Integer
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_unit
- 例2 値：Float | Integer | Float | Float | Integer
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_unit

## g0082（1 列）
- 見出し：parameter_unit
- 例1 値：Datum/DOY | Datum/DOY | Datum/DOY | Datum/DOY | Datum/DOY
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0083（1 列）
- 見出し：parameter_group_de
- 例1 値：Feuchte | Verdunstung | Temperatur | Druck | Temperatur
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0084（1 列）
- 見出し：parameter_group_fr
- 例1 値：Température | Pression | Précipitations | Neige | Vent
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0085（1 列）
- 見出し：parameter_unit
- 例1 値：°C | hPa | km/h | mm | No
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0086（1 列）
- 見出し：Measure
- 例1 値：blev | blev | blev | blev | blev
  - 同じ表の列：Time, Variable, Region, Sector, Value

## g0087（1 列）
- 見出し：Time
- 例1 値：2022 | 2022 | 2022 | 2022 | 2022
  - 同じ表の列：Measure, Variable, Region, Sector, Value

## g0088（1 列）
- 見出し：Variable
- 例1 値：ExpVol | ExpVol | ExpVol | ExpVol | ExpVol
  - 同じ表の列：Measure, Time, Region, Sector, Value

## g0089（1 列）
- 見出し：Region
- 例1 値：ZH | ZH | ZH | BE | ZH
  - 同じ表の列：Measure, Time, Variable, Sector, Value

## g0090（1 列）
- 見出し：Sector
- 例1 値：B1_Mining | P1_Education | H6_Telecom | L2_Consult | L1_RealEst
  - 同じ表の列：Measure, Time, Variable, Region, Value

## g0091（3 列）
- 見出し：Value
- 例1 値：64.6440200805664 | 19.2769241333008 | 3.10305404663086 | 8.83381271362305 | 631.85595703125
  - 同じ表の列：Measure, Time, Variable, Region, Sector
- 例2 値：0.0392 | 0.0227 | 0.4299 | 3.9067 | 0.0001
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, OBS_CONFIDENCE

## g0092（1 列）
- 見出し：TRANSPORT_TYPE
- 例1 値：SOFT_MOB | OTHER | OTHER | PRIV_MOT_TRANSP | OTHER
  - 同じ表の列：TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0093（1 列）
- 見出し：TRANSPORT_MEAN
- 例1 値：CABLE | CAR_PASS | BOAT | TRAN_LIKE_EQU | TOT
  - 同じ表の列：TRANSPORT_TYPE, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0094（1 列）
- 見出し：TRAVEL_REASON
- 例1 値：WORK | OTH_REAS | LEISU | OTH_REAS | SERV_ACC
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0095（1 列）
- 見出し：SOCIO_DEMO_VARIABLE_TYPE
- 例1 値：GEO | GEO | GEO | GEO | GEO
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0096（1 列）
- 見出し：SOCIO_DEMO_VARIABLE
- 例1 値：CH02 | CH02 | CH01 | CH03 | CH
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0097（1 列）
- 見出し：PERIOD_REF
- 例1 値：2015 | 2015 | 2015 | 2015 | 2015
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0098（1 列）
- 見出し：UNIT_MEAS
- 例1 値：KM | KM | KM | KM | KM
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, VALUE, OBS_CONFIDENCE

## g0099（1 列）
- 見出し：OBS_CONFIDENCE
- 例1 値：0.0003 | 0.0057 | 0.0324 | 0.0276 | 0.2116
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE

## g0100（1 列）
- 見出し：AC
- 例1 値：2015 | 2015 | 2017 | 2019 | 2015
  - 同じ表の列：Semaine, Fin, Age, Nombre_Deces, Attendu, Lim_min, Lim_sup, Exces

## g0101（1 列）
- 見出し：Semaine
- 例1 値：18 | 41 | 42 | 35 | 23
  - 同じ表の列：AC, Fin, Age, Nombre_Deces, Attendu, Lim_min, Lim_sup, Exces

## g0102（1 列）
- 見出し：Fin
- 例1 値：25.03.2018 | 06.05.2012 | 10.07.2011 | 20.09.2015 | 12.03.2017
  - 同じ表の列：AC, Semaine, Age, Nombre_Deces, Attendu, Lim_min, Lim_sup, Exces

## g0103（1 列）
- 見出し：Age
- 例1 値：0-64 | 0-64 | 65+ | 0-64 | 65+
  - 同じ表の列：AC, Semaine, Fin, Nombre_Deces, Attendu, Lim_min, Lim_sup, Exces

## g0104（1 列）
- 見出し：Nombre_Deces
- 例1 値：170 | 1093 | 1020 | 171 | 999
  - 同じ表の列：AC, Semaine, Fin, Age, Attendu, Lim_min, Lim_sup, Exces

## g0105（1 列）
- 見出し：Attendu
- 例1 値：183 | 1150 | 1063 | 1060 | 173
  - 同じ表の列：AC, Semaine, Fin, Age, Nombre_Deces, Lim_min, Lim_sup, Exces

## g0106（1 列）
- 見出し：Lim_min
- 例1 値：1016 | 906 | 839 | 137 | 945
  - 同じ表の列：AC, Semaine, Fin, Age, Nombre_Deces, Attendu, Lim_sup, Exces

## g0107（1 列）
- 見出し：Lim_sup
- 例1 値：1055 | 1128 | 214 | 1234 | 215
  - 同じ表の列：AC, Semaine, Fin, Age, Nombre_Deces, Attendu, Lim_min, Exces

## g0108（1 列）
- 見出し：Exces
- 例1 値：1412 | 1077 | 1203 | 1549 | 1237
  - 同じ表の列：AC, Semaine, Fin, Age, Nombre_Deces, Attendu, Lim_min, Lim_sup

## g0109（1 列）
- 見出し：REF_YEAR
- 例1 値：2020 | 2020 | 2020 | 2020 | 2020
  - 同じ表の列：GEO_COMM, GEO_CANT, VALUE

## g0110（1 列）
- 見出し：GEO_COMM
- 例1 値：2866 | 592 | 160 | 1707 | 2260
  - 同じ表の列：REF_YEAR, GEO_CANT, VALUE

## g0111（1 列）
- 見出し：GEO_CANT
- 例1 値：11 | 10 | 1 | 2 | 2
  - 同じ表の列：REF_YEAR, GEO_COMM, VALUE

## g0112（1 列）
- 見出し：PK     L"]]­„32MóMó   SIT_AUTOR_DOSSIER.csvï»¿OBJECT
- 例1 値：52 | 270 | 864 | 437 | 471
  - 同じ表の列：ID_DOSSIER, TYPE_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_DOSSIER, NO_COMPLEMENTAIRE, STATUT, OPERATION

## g0113（1 列）
- 見出し：ID_DOSSIER
- 例1 値：DD 82066/1 | DD 76086/1 | DD 90794/1 | DD 15194/1 | DD 32470/1
  - 同じ表の列：PK     L"]]­„32M…, TYPE_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_DOSSIER, NO_COMPLEMENTAIRE, STATUT, OPERATION

## g0114（1 列）
- 見出し：TYPE_DOSSIER
- 例1 値：DD | DD | DD | DD | DD
  - 同じ表の列：PK     L"]]­„32M…, ID_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_DOSSIER, NO_COMPLEMENTAIRE, STATUT, OPERATION

## g0115（1 列）
- 見出し：TYPE_OPERATION
- 例1 値：-- | -- | -- | -- | --
  - 同じ表の列：PK     L"]]­„32M…, ID_DOSSIER, TYPE_DOSSIER, NOM_DOSSIER, NO_DOSSIER, NO_COMPLEMENTAIRE, STATUT, OPERATION

## g0116（1 列）
- 見出し：NOM_DOSSIER
- 例1 値：Demande dÃ©finitive | Demande dÃ©finitive | Demande dÃ©finitive | Demande dÃ©finitive | Demande dÃ©finitive
  - 同じ表の列：PK     L"]]­„32M…, ID_DOSSIER, TYPE_DOSSIER, TYPE_OPERATION, NO_DOSSIER, NO_COMPLEMENTAIRE, STATUT, OPERATION

## g0117（1 列）
- 見出し：NO_DOSSIER
- 例1 値：36752 | 80321 | 61845 | 93616 | 87324
  - 同じ表の列：PK     L"]]­„32M…, ID_DOSSIER, TYPE_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_COMPLEMENTAIRE, STATUT, OPERATION

## g0118（1 列）
- 見出し：NO_COMPLEMENTAIRE
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：PK     L"]]­„32M…, ID_DOSSIER, TYPE_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_DOSSIER, STATUT, OPERATION

## g0119（1 列）
- 見出し：STATUT
- 例1 値：- | - | - | - | -
  - 同じ表の列：PK     L"]]­„32M…, ID_DOSSIER, TYPE_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_DOSSIER, NO_COMPLEMENTAIRE, OPERATION

## g0120（1 列）
- 見出し：OPERATION
- 例1 値：Non renseignÃ© (valeur par dÃ©faut Ã l'… | Non renseignÃ© (valeur par dÃ©faut Ã l'… | Non renseignÃ© (valeur par dÃ©faut Ã l'… | Non renseignÃ© (valeur par dÃ©faut Ã l'… | Non renseignÃ© (valeur par dÃ©faut Ã l'…
  - 同じ表の列：PK     L"]]­„32M…, ID_DOSSIER, TYPE_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_DOSSIER, NO_COMPLEMENTAIRE, STATUT

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
