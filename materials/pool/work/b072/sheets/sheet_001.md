# ラベル用シート 001 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：valueCategory
- 例1 値：cases | cases | cases | cases | max_value_5y
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type
- 例2 値：min_value_10y | cases | cases | cases | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, value

## g0002（3 列）
- 見出し：temporal
- 例1 値：2023-M02 | 2015 | 2018-M08 | 2019 | 2017
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type
- 例2 値：2017 | 2017-M08 | 2018-M11 | 2022 | 2023
  - 同じ表の列：valueCategory, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type

## g0003（3 列）
- 見出し：temporal_type
- 例1 値：month | month | year | month | year
  - 同じ表の列：valueCategory, temporal, georegion, georegion_type, agegroup, agegroup_type, sex, type
- 例2 値：month | month | month | month | year
  - 同じ表の列：valueCategory, temporal, georegion, georegion_type, agegroup, agegroup_type, sex, type

## g0004（3 列）
- 見出し：georegion
- 例1 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, type
- 例2 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion_type, agegroup, agegroup_type, sex, type

## g0005（3 列）
- 見出し：georegion_type
- 例1 値：CHFL | CHFL | grossregion | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, type
- 例2 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, type

## g0006（1 列）
- 見出し：agegroup
- 例1 値：all | all | 65+ | 35 - 44 | unknown
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, type

## g0007（3 列）
- 見出し：agegroup_type
- 例1 値：agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, type
- 例2 値：agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti | agegroup_sti
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, sex, type

## g0008（3 列）
- 見出し：sex
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, type
- 例2 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, type

## g0009（2 列）
- 見出し：type
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex
- 例2 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0010（5 列）
- 見出し：value
- 例1 値：101 | 200 | 89 | 85 | 146
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex
- 例2 値：112 | 147 | 86 | 82 | 1112
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0011（1 列）
- 見出し：valueCategory
- 例1 値：cases | cases | cases | cases | cases
  - 同じ表の列：temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex, type

## g0012（1 列）
- 見出し：agegroup
- 例1 値：all | all | all | all | all
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, type

## g0013（1 列）
- 見出し：agegroup
- 例1 値：all | all | all | all | 25 - 44
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup_type, sex, value

## g0014（1 列）
- 見出し：pop
- 例1 値：NA | 9002273 | 9127125 | 420326 | 331763
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, georegion_type, agegroup, agegroup_type, sex

## g0015（3 列）
- 見出し：id
- 例1 値：1328 | 987 | 982 | 610 | 777
  - 同じ表の列：date_measured, site, site_roadgrade, site_air_temperature, rsd_model, vehicle_type, vehicle_fuel_type, vehicle_euronorm
- 例2 値：706 | 187 | 649 | 177 | 897
  - 同じ表の列：year, gewicht_grp, gewicht_label, alter_mutter_cd, alter_mutter_label, gestations_alter_grp, gestations_alter_la…, geburts_art

## g0016（1 列）
- 見出し：date_measured
- 例1 値：2002-05-16 | 2002-05-16 | 2002-05-16 | 2002-05-16 | 2002-05-16
  - 同じ表の列：id, site, site_roadgrade, site_air_temperature, rsd_model, vehicle_type, vehicle_fuel_type, vehicle_euronorm

## g0017（1 列）
- 見出し：site
- 例1 値：C | C | C | C | C
  - 同じ表の列：id, date_measured, site_roadgrade, site_air_temperature, rsd_model, vehicle_type, vehicle_fuel_type, vehicle_euronorm

## g0018（1 列）
- 見出し：site_roadgrade
- 例1 値：0.094 | 0.094 | 0.094 | 0.094 | 0.094
  - 同じ表の列：id, date_measured, site, site_air_temperature, rsd_model, vehicle_type, vehicle_fuel_type, vehicle_euronorm

## g0019（1 列）
- 見出し：site_air_temperature
- 例1 値：25.5 | 24.9 | 25.6 | 24.9 | 25.2
  - 同じ表の列：id, date_measured, site, site_roadgrade, rsd_model, vehicle_type, vehicle_fuel_type, vehicle_euronorm

## g0020（1 列）
- 見出し：rsd_model
- 例1 値：Opus-RSD3000/RSD518 | Opus-RSD3000/RSD518 | Opus-RSD3000/RSD518 | Opus-RSD3000/RSD518 | Opus-RSD3000/RSD518
  - 同じ表の列：id, date_measured, site, site_roadgrade, site_air_temperature, vehicle_type, vehicle_fuel_type, vehicle_euronorm

## g0021（1 列）
- 見出し：vehicle_type
- 例1 値：passenger car | passenger car | passenger car | passenger car | light duty vehicle
  - 同じ表の列：id, date_measured, site, site_roadgrade, site_air_temperature, rsd_model, vehicle_fuel_type, vehicle_euronorm

## g0022（1 列）
- 見出し：vehicle_fuel_type
- 例1 値：gasoline | gasoline | gasoline | gasoline | gasoline
  - 同じ表の列：id, date_measured, site, site_roadgrade, site_air_temperature, rsd_model, vehicle_type, vehicle_euronorm

## g0023（1 列）
- 見出し：vehicle_euronorm
- 例1 値：Euro3 | Euro2 | Euro1 | Euro1 | Euro3
  - 同じ表の列：id, date_measured, site, site_roadgrade, site_air_temperature, rsd_model, vehicle_type, vehicle_fuel_type

## g0024（1 列）
- 見出し：vehicle_make
- 例1 値：Hyundai | Ford | Opel | Subaru | VW
  - 同じ表の列：id, date_measured, site, site_roadgrade, site_air_temperature, rsd_model, vehicle_type, vehicle_fuel_type

## g0025（1 列）
- 見出し：Fahrzeugtyp
- 例1 値：Personenwagen (M1) | Personenwagen (M1) | Lieferwagen (N1) | Lieferwagen (N1) | Personenwagen (M1)
  - 同じ表の列：Jahr, Indikator, Wert, Einheit

## g0026（10 列）
- 見出し：Jahr
- 例1 値：2024 | 2021 | 2022 | 2015 | 2021
  - 同じ表の列：Fahrzeugtyp, Indikator, Wert, Einheit
- 例2 値：2024 | 2012 | 2013 | 2011 | 2021
  - 同じ表の列：Energiesektor, Energieträger, Wert, Einheit

## g0027（1 列）
- 見出し：Indikator
- 例1 値：Treibhausgasemissionen | Fahrleistung | Emissionsfaktor | Fahrzeugbestand | Fahrleistung
  - 同じ表の列：Fahrzeugtyp, Jahr, Wert, Einheit

## g0028（2 列）
- 見出し：Wert
- 例1 値：206 | 875 | 13781977 | 2034073 | 13658213
  - 同じ表の列：Fahrzeugtyp, Jahr, Indikator, Einheit
- 例2 値：113270 | 70173 | 121700 | 126062 | 566075
  - 同じ表の列：Jahr, Energiesektor, Energieträger, Einheit

## g0029（1 列）
- 見出し：Einheit
- 例1 値：g CO2/fzkm | Anzahl | Tonnen | Tonnen | Anzahl
  - 同じ表の列：Fahrzeugtyp, Jahr, Indikator, Wert

## g0030（1 列）
- 見出し：Energiesektor
- 例1 値：Wärme | Strom | Strom | Wärme | Strom
  - 同じ表の列：Jahr, Energieträger, Wert, Einheit

## g0031（1 列）
- 見出し：Energieträger
- 例1 値：Wasser | Wasser | Biomasse (einschliesslich Holz) | Biomasse (einschliesslich Holz) | Geothermie (untief)
  - 同じ表の列：Jahr, Energiesektor, Wert, Einheit

## g0032（1 列）
- 見出し：Einheit
- 例1 値：MWh | MWh | MWh | MWh | MWh
  - 同じ表の列：Jahr, Energiesektor, Energieträger, Wert

## g0033（3 列）
- 見出し：Year
- 例1 値：2014 | 2014 | 2014 | 2014 | 2014
  - 同じ表の列：Canton, Species, Type of Slaughter, Origin of animal, Fitness for consump…, Count
- 例2 値：1994 | 1994 | 1994 | 1994 | 1994
  - 同じ表の列：id, gewicht_grp, gewicht_label, alter_mutter_cd, alter_mutter_label, gestations_alter_grp, gestations_alter_la…, geburts_art

## g0034（1 列）
- 見出し：Canton
- 例1 値：BL | FR | SH | FL | LU
  - 同じ表の列：Year, Species, Type of Slaughter, Origin of animal, Fitness for consump…, Count

## g0035（1 列）
- 見出し：Species
- 例1 値：Swine | Cattle < 6We | Goats | Cattle > 6We | Cattle < 6We
  - 同じ表の列：Year, Canton, Type of Slaughter, Origin of animal, Fitness for consump…, Count

## g0036（1 列）
- 見出し：Type of Slaughter
- 例1 値：Sanitary | Normal | Sanitary | Normal | Normal
  - 同じ表の列：Year, Canton, Species, Origin of animal, Fitness for consump…, Count

## g0037（1 列）
- 見出し：Origin of animal
- 例1 値：Abroad | Inland | Inland | Inland | Abroad
  - 同じ表の列：Year, Canton, Species, Type of Slaughter, Fitness for consump…, Count

## g0038（1 列）
- 見出し：Fitness for consumption
- 例1 値：No | Yes | Yes | Yes | No
  - 同じ表の列：Year, Canton, Species, Type of Slaughter, Origin of animal, Count

## g0039（1 列）
- 見出し：Count
- 例1 値：0 | 6 | 0 | 0 | 1
  - 同じ表の列：Year, Canton, Species, Type of Slaughter, Origin of animal, Fitness for consump…

## g0040（1 列）
- 見出し：Kanton
- 例1 値：ZH | VD | ZH | ZH | SH
  - 同じ表の列：Fundort, Probenahme-Datum, Vogelart, Status Wildvogel, Ergebnis, Pathogenitaet, Subtyp

## g0041（1 列）
- 見出し：Fundort
- 例1 値：4054 Zoo Basel Binningerstrasse 40 Bade… | Flughafen Zürich | Zürich | St Auban | La Sauge, Canal de la Broye
  - 同じ表の列：Kanton, Probenahme-Datum, Vogelart, Status Wildvogel, Ergebnis, Pathogenitaet, Subtyp

## g0042（1 列）
- 見出し：Probenahme-Datum
- 例1 値：2023-03-02 | 2023-02-26 | 2023-01-23 | 2023-09-14 | 2021-01-05
  - 同じ表の列：Kanton, Fundort, Vogelart, Status Wildvogel, Ergebnis, Pathogenitaet, Subtyp

## g0043（1 列）
- 見出し：Vogelart
- 例1 値：Stockente | Lachmöwe | Blässhuhn | Lachmöwe | Lachmöwe
  - 同じ表の列：Kanton, Fundort, Probenahme-Datum, Status Wildvogel, Ergebnis, Pathogenitaet, Subtyp

## g0044（1 列）
- 見出し：Status Wildvogel
- 例1 値：Totfund mehrere Tiere an einem Ort | Totfund mehrere Tiere an einem Ort | Totfund mehrere Tiere an einem Ort | Totfund mehrere Tiere an einem Ort | Totfund Einzeltier
  - 同じ表の列：Kanton, Fundort, Probenahme-Datum, Vogelart, Ergebnis, Pathogenitaet, Subtyp

## g0045（1 列）
- 見出し：Ergebnis
- 例1 値：negativ | negativ | negativ | negativ | positiv
  - 同じ表の列：Kanton, Fundort, Probenahme-Datum, Vogelart, Status Wildvogel, Pathogenitaet, Subtyp

## g0046（1 列）
- 見出し：Pathogenitaet
- 例1 値：highly pathogenic avian influenza (HPAI) | highly pathogenic avian influenza (HPAI) | highly pathogenic avian influenza (HPAI) | highly pathogenic avian influenza (HPAI) | highly pathogenic avian influenza (HPAI)
  - 同じ表の列：Kanton, Fundort, Probenahme-Datum, Vogelart, Status Wildvogel, Ergebnis, Subtyp

## g0047（1 列）
- 見出し：Subtyp
- 例1 値：H5N1 | H5N1 | H5N1 | H5N1 | H5N1
  - 同じ表の列：Kanton, Fundort, Probenahme-Datum, Vogelart, Status Wildvogel, Ergebnis, Pathogenitaet

## g0048（1 列）
- 見出し：BVD_AMPEL
- 例1 値：orange | red | green | green | green
  - 同じ表の列：TIMESTEP, N_FARMS, diff, total_per_day, percentage

## g0049（1 列）
- 見出し：TIMESTEP
- 例1 値：2024-12 | 2024-11 | 2024-12 | 2025-02 | 2025-02
  - 同じ表の列：BVD_AMPEL, N_FARMS, diff, total_per_day, percentage

## g0050（1 列）
- 見出し：N_FARMS
- 例1 値：48.0 | 4225.0 | 30172.0 | 4354.0 | 30643.0
  - 同じ表の列：BVD_AMPEL, TIMESTEP, diff, total_per_day, percentage

## g0051（1 列）
- 見出し：diff
- 例1 値：-585 | -13 | -3 | 387 | -129
  - 同じ表の列：BVD_AMPEL, TIMESTEP, N_FARMS, total_per_day, percentage

## g0052（1 列）
- 見出し：total_per_day
- 例1 値：34451.0 | 34504.0 | 34465.0 | 34465.0 | 34451.0
  - 同じ表の列：BVD_AMPEL, TIMESTEP, N_FARMS, diff, percentage

## g0053（1 列）
- 見出し：percentage
- 例1 値：0.1 | 87.6 | 88.1 | 87.2 | 0.1
  - 同じ表の列：BVD_AMPEL, TIMESTEP, N_FARMS, diff, total_per_day

## g0054（2 列）
- 見出し：parameter_group_de
- 例1 値：Niederschlag | Niederschlag | Niederschlag | Niederschlag | Niederschlag
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Temperatur | Niederschlag | Temperatur | Temperatur | Temperatur
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0055（1 列）
- 見出し：parameter_group_fr
- 例1 値：Précipitations | Précipitations | Précipitations | Précipitations | Précipitations
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0056（2 列）
- 見出し：parameter_group_it
- 例1 値：Precipitazioni | Precipitazioni | Precipitazioni | Precipitazioni | Precipitazioni
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Temperatura | Pressione | Temperatura | Temperatura | Vento
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0057（2 列）
- 見出し：parameter_group_en
- 例1 値：Precipitation | Precipitation | Precipitation | Precipitation | Precipitation
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Sunshine | Wind | Temperature | Temperature | Temperature
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0058（2 列）
- 見出し：parameter_granularity
- 例1 値：Y | Y | Y | M | Y
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Y | M | M | Y | M
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_decimals, parameter_datatype, parameter_unit

## g0059（2 列）
- 見出し：parameter_decimals
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit
- 例2 値：0 | 0 | 1 | 0 | 1
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit

## g0060（2 列）
- 見出し：parameter_datatype
- 例1 値：Integer | Integer | Integer | Float | Integer
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_unit
- 例2 値：Integer | Float | Integer | Integer | Float
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_unit

## g0061（1 列）
- 見出し：parameter_unit
- 例1 値：No | No | No | % | No
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0062（1 列）
- 見出し：parameter_group_fr
- 例1 値：Température | Rayonnement | Température | Température | Précipitations
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0063（1 列）
- 見出し：parameter_unit
- 例1 値：°C | No | No | No | No
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0064（2 列）
- 見出し：PERIOD_REF
- 例1 値：2019 | 2019 | 2019 | 2019 | 2019
  - 同じ表の列：CODE_REGION, REGION, INDICATORS, UNIT_MES, VALUE, STATUS
- 例2 値：2018 | 2019 | 2018 | 2017 | 2009
  - 同じ表の列：REGION, INDICATORS, UNIT_MES, VALUE, STATUS

## g0065（1 列）
- 見出し：CODE_REGION
- 例1 値：977 | 1097 | 181 | 2544 | 2068
  - 同じ表の列：PERIOD_REF, REGION, INDICATORS, UNIT_MES, VALUE, STATUS

## g0066（2 列）
- 見出し：REGION
- 例1 値：Blauen | Anwil | Orpund | Cormoret | Trubschachen
  - 同じ表の列：PERIOD_REF, CODE_REGION, INDICATORS, UNIT_MES, VALUE, STATUS
- 例2 値：IRL | BGR | ESP | MLT | DNK
  - 同じ表の列：PERIOD_REF, INDICATORS, UNIT_MES, VALUE, STATUS

## g0067（2 列）
- 見出し：INDICATORS
- 例1 値：Ind_01_01 | Ind_01_01 | Ind_01_01 | Ind_01_01 | Ind_01_01
  - 同じ表の列：PERIOD_REF, CODE_REGION, REGION, UNIT_MES, VALUE, STATUS
- 例2 値：Ind_17_03 | Ind_04_08 | Ind_19_02 | Ind_01_14 | Ind_05_10
  - 同じ表の列：PERIOD_REF, REGION, UNIT_MES, VALUE, STATUS

## g0068（2 列）
- 見出し：UNIT_MES
- 例1 値：UM_6 | UM_6 | UM_6 | UM_6 | UM_6
  - 同じ表の列：PERIOD_REF, CODE_REGION, REGION, INDICATORS, VALUE, STATUS
- 例2 値：UM_26 | UM_2 | UM_2 | UM_18 | UM_2
  - 同じ表の列：PERIOD_REF, REGION, INDICATORS, VALUE, STATUS

## g0069（5 列）
- 見出し：STATUS
- 例1 値：A | A | A | A | A
  - 同じ表の列：PERIOD_REF, CODE_REGION, REGION, INDICATORS, UNIT_MES, VALUE
- 例2 値：A | A | A | A | A
  - 同じ表の列：PERIOD_REF, REGION, INDICATORS, UNIT_MES, VALUE

## g0070（1 列）
- 見出し：VALUE
- 例1 値：1.4 | 22000 | 1.7 | 7 | 20.18086781
  - 同じ表の列：PERIOD_REF, REGION, INDICATORS, UNIT_MES, STATUS

## g0071（1 列）
- 見出し：REF_YEAR
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：GEO_COMM, GEO_CANT, VALUE

## g0072（1 列）
- 見出し：GEO_COMM
- 例1 値：901 | 683 | 2542 | 57 | 756
  - 同じ表の列：REF_YEAR, GEO_CANT, VALUE

## g0073（1 列）
- 見出し：GEO_CANT
- 例1 値：1 | 2 | 1 | 2 | 11
  - 同じ表の列：REF_YEAR, GEO_COMM, VALUE

## g0074（1 列）
- 見出し：VALUE
- 例1 値：5.1804435341496 | 60.3320367058951 | 416.1325068365180 | 8.7864616071949 | 24.5104135043040
  - 同じ表の列：REF_YEAR, GEO_COMM, GEO_CANT

## g0075（1 列）
- 見出し：kategorie
- 例1 値：Domiziländerung (intrakommunal) | Sitzverlegung Zuzug (interkantonal) | Sitzverlegung Zuzug (interkantonal) | Sitzverlegung intrakantonal | Sitzverlegung intrakantonal
  - 同じ表の列：publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_neu_code, firmensitz_neu, firmensitz_neu_cant…, firmensitz_bisher_c…, firmensitz_bisher

## g0076（1 列）
- 見出し：publikationsdatum_shab
- 例1 値：2026-06-23 | 2026-04-22 | 2026-08-21 | 2026-06-01 | 2026-09-15
  - 同じ表の列：kategorie, journaldatum_handel…, id_shab, firmensitz_neu_code, firmensitz_neu, firmensitz_neu_cant…, firmensitz_bisher_c…, firmensitz_bisher

## g0077（1 列）
- 見出し：journaldatum_handelsregister
- 例1 値：2026-02-18 | 2026-01-26 | 2026-07-15 | 2026-06-04 | 2026-03-26
  - 同じ表の列：kategorie, publikationsdatum_s…, id_shab, firmensitz_neu_code, firmensitz_neu, firmensitz_neu_cant…, firmensitz_bisher_c…, firmensitz_bisher

## g0078（1 列）
- 見出し：id_shab
- 例1 値：1006765028 | 1006703613 | 1006630828 | 1006732585 | 1006679712
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, firmensitz_neu_code, firmensitz_neu, firmensitz_neu_cant…, firmensitz_bisher_c…, firmensitz_bisher

## g0079（1 列）
- 見出し：firmensitz_neu_code
- 例1 値：2831 | 2893 | 2773 | 2766 | 4082
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_neu, firmensitz_neu_cant…, firmensitz_bisher_c…, firmensitz_bisher

## g0080（1 列）
- 見出し：firmensitz_neu
- 例1 値：Liestal | Pratteln | Bottmingen | Reinach (BL) | Lupsingen
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_neu_code, firmensitz_neu_cant…, firmensitz_bisher_c…, firmensitz_bisher

## g0081（1 列）
- 見出し：firmensitz_neu_canton
- 例1 値：BL | BL | AG | BL | BL
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_neu_code, firmensitz_neu, firmensitz_bisher_c…, firmensitz_bisher

## g0082（1 列）
- 見出し：firmensitz_bisher_code
- 例1 値：2613 | 2773 | 2701 | 2770 | 2765
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_neu_code, firmensitz_neu, firmensitz_neu_cant…, firmensitz_bisher

## g0083（1 列）
- 見出し：firmensitz_bisher
- 例1 値：Burg im Leimental | Arisdorf | Füllinsdorf | Pratteln | Basel
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_neu_code, firmensitz_neu, firmensitz_neu_cant…, firmensitz_bisher_c…

## g0084（1 列）
- 見出し：firmensitz_bisher_canton
- 例1 値：BS | BL | BE | BS | BL
  - 同じ表の列：kategorie, publikationsdatum_s…, journaldatum_handel…, id_shab, firmensitz_neu_code, firmensitz_neu, firmensitz_neu_cant…, firmensitz_bisher_c…

## g0085（1 列）
- 見出し：dataset_id
- 例1 値：10070 | 13320 | 12190 | 13060 | 13030
  - 同じ表の列：title, title_de, title_fr, title_en, title_it, theme, theme_de, theme_fr

## g0086（1 列）
- 見出し：title
- 例1 値：Wohngebäude nach Energieträger der Heiz… | Landratswahlen: Wahlkreise | Bilanz der Wohnbevölkerung nach Gemeind… | Arealstatistik: Bodennutzung und -bedec… | Wetterstationen: Tageswerte Klimamessne…
  - 同じ表の列：dataset_id, title_de, title_fr, title_en, title_it, theme, theme_de, theme_fr

## g0087（1 列）
- 見出し：title_de
- 例1 値：OGD-Portal: Tägliche Nutzung (seit Janu… | Wohnbevölkerung nach Religionszugehörig… | Covid-19: Tägliche Tests nach Typ des T… | Überbauungsstand nach Zone, Erschliessu… | Luftqualität Station Dornach (halbstünd…
  - 同じ表の列：dataset_id, title, title_fr, title_en, title_it, theme, theme_de, theme_fr

## g0088（1 列）
- 見出し：title_fr
- 例1 値：Station météorologique de Sissach-Bütze… | Bewilligte Tagesbetreuungseinrichtungen… | Schulferien Kanton Basel-Landschaft (20… | Registre cantonal des bâtiments et des … | Bauprojekte nach Gemeinde und Quartal (…
  - 同じ表の列：dataset_id, title, title_de, title_en, title_it, theme, theme_de, theme_fr

## g0089（1 列）
- 見出し：title_en
- 例1 値：Gemeinderatsnachwahlen 2024: Anzahl Sit… | Wohnbevölkerung nach Geburtsort der Elt… | Swisslos Sportfonds: Bilanz nach Gesuch… | Covid-19: Täglich geimpfte Personen nac… | Addresses of municipal administrations
  - 同じ表の列：dataset_id, title, title_de, title_fr, title_it, theme, theme_de, theme_fr

## g0090（1 列）
- 見出し：title_it
- 例1 値：Indirizzi delle stazioni di polizia | Wohnbevölkerung nach Geschlecht, Alters… | Arealstatistik: Bodennutzung und -bedec… | Wohnbevölkerung nach Hauptsprache, Nati… | Cifre chiave dei comuni
  - 同じ表の列：dataset_id, title, title_de, title_fr, title_en, theme, theme_de, theme_fr

## g0091（1 列）
- 見出し：theme
- 例1 値：Gesundheit | Bevölkerung und Gesellschaft | Bevölkerung und Gesellschaft;Bildung, K… | Gesundheit | Bevölkerung und Gesellschaft
  - 同じ表の列：dataset_id, title, title_de, title_fr, title_en, title_it, theme_de, theme_fr

## g0092（1 列）
- 見出し：theme_de
- 例1 値：['Gesundheit'] | ['Regierung und öffentlicher Sektor'] | ['Wirtschaft und Finanzen'] | ['Gesundheit', 'Bevölkerung und Gesells… | ['Bevölkerung und Gesellschaft', 'Bildu…
  - 同じ表の列：dataset_id, title, title_de, title_fr, title_en, title_it, theme, theme_fr

## g0093（1 列）
- 見出し：theme_fr
- 例1 値：['Gouvernement et secteur public'] | ['Economie et finances'] | ['Population et société'] | ['Population et société', 'Education, c… | ['Energie']
  - 同じ表の列：dataset_id, title, title_de, title_fr, title_en, title_it, theme, theme_de

## g0094（1 列）
- 見出し：theme_en
- 例1 値：['Government and public sector'] | ['Environment'] | ['Regions and cities', 'Education, cult… | ['Government and public sector'] | ['Government and public sector']
  - 同じ表の列：dataset_id, title, title_de, title_fr, title_en, title_it, theme, theme_de

## g0095（1 列）
- 見出し：dokument_titel
- 例1 値：Text Interpellation | Text Interpellation | Vorlage des Regierungsrats | Beilage zur Vorlage: Finanzbericht PBL … | Beilage zur Vorlage: Gebäudekonzept Neu…
  - 同じ表の列：dokument_datum, geschaeft_titel, geschaeft_laufnummer

## g0096（1 列）
- 見出し：dokument_datum
- 例1 値：2026-05-07 | 2026-05-28 | 2026-08-14 | 2026-05-05 | 2026-04-15
  - 同じ表の列：dokument_titel, geschaeft_titel, geschaeft_laufnummer

## g0097（1 列）
- 見出し：geschaeft_titel
- 例1 値：Formulierte Gesetzesinitiative «BLKB – … | Zukunft Kantonsspital Basellandschaft | Anpassung Kantonaler Nutzungsplan Gymna… | Kantonale Umsetzung des indirekten Gege… | 2028
  - 同じ表の列：dokument_titel, dokument_datum, geschaeft_laufnummer

## g0098（1 列）
- 見出し：geschaeft_laufnummer
- 例1 値：2026/5036 | 2026/5084 | 2026/5312 | 2026/5777 | 2026/3195
  - 同じ表の列：dokument_titel, dokument_datum, geschaeft_titel

## g0099（2 列）
- 見出し：Geo Point
- 例1 値：47.549064736139776, 7.56805592277744 | 47.576337002560855, 7.587841020785123 | 47.585332457616886, 7.650691293490652 | 47.56114659812266, 7.590933528529995 | 47.558923822510415, 7.585009066994525
  - 同じ表の列：Geo Shape, Begegnungszonen-ID, Regime, Umsetzungsjahr, Zum Objekt navigier…
- 例2 値：47.336655803, 9.4127155088 | 47.4006088856, 9.47717024511 | 47.3807438333, 9.4266654245 | 47.4736293725, 9.46791756661 | 47.3627632445, 9.3832446689
  - 同じ表の列：Gemeinde, Gemeinde Code, Kanton, Kanton Code, Geo Shape

## g0100（1 列）
- 見出し：Geo Shape
- 例1 値：{"coordinates": [[[7.642785227534418, 4… | {"coordinates": [[[7.591989960087145, 4… | {"coordinates": [[[7.592365450841021, 4… | {"coordinates": [[[7.585570170763756, 4… | {"coordinates": [[[7.593830942285894, 4…
  - 同じ表の列：Geo Point, Begegnungszonen-ID, Regime, Umsetzungsjahr, Zum Objekt navigier…

## g0101（1 列）
- 見出し：Begegnungszonen-ID
- 例1 値：20 | 98 | 31 | 165 | 163
  - 同じ表の列：Geo Point, Geo Shape, Regime, Umsetzungsjahr, Zum Objekt navigier…

## g0102（1 列）
- 見出し：Regime
- 例1 値：Begegnungszone | Begegnungszone | Begegnungszone | Begegnungszone | Begegnungszone
  - 同じ表の列：Geo Point, Geo Shape, Begegnungszonen-ID, Umsetzungsjahr, Zum Objekt navigier…

## g0103（1 列）
- 見出し：Umsetzungsjahr
- 例1 値：vor 2001 | 2020 | 2015 | 2013 | 2026
  - 同じ表の列：Geo Point, Geo Shape, Begegnungszonen-ID, Regime, Zum Objekt navigier…

## g0104（1 列）
- 見出し：Zum Objekt navigieren
- 例1 値：https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/…
  - 同じ表の列：Geo Point, Geo Shape, Begegnungszonen-ID, Regime, Umsetzungsjahr

## g0105（1 列）
- 見出し：Anzahl Hundehalter
- 例1 値：5117 | 5615 | 5541 | 4793 | 5773
  - 同じ表の列：Jahr

## g0106（1 列）
- 見出し：Wohnviertel ID
- 例1 値：7 | 10 | 12 | 6 | 19
  - 同じ表の列：Jahr, Gemeinde, Hundebestand

## g0107（1 列）
- 見出し：Gemeinde
- 例1 値：Basel | Riehen | Kanton Basel-Stadt | Riehen | Riehen
  - 同じ表の列：Jahr, Wohnviertel ID, Hundebestand

## g0108（1 列）
- 見出し：Hundebestand
- 例1 値：227 | 375 | 330 | 206 | 7491
  - 同じ表の列：Jahr, Wohnviertel ID, Gemeinde

## g0109（1 列）
- 見出し：dokument_titel
- 例1 値：2016.RRGR.81-Abstimmungsprotokoll-Voran… | GRB – Wiederherstellung der politischen… | 2014.RRGR.420-wortlautdok-2016.01.25-13… | M-155-2014-vorstosstext-fr | 2014.0334-vortrag-19.03.2014-de
  - 同じ表の列：dokument_geschaefts…, dokument_geschaefts…, dokument_typ_deutsch, dokument_typ_franz, dokument_ziel_publi…, dokument_geschaeft_…, Übersicht vom

## g0110（1 列）
- 見出し：dokument_geschaeftstitel_deutsch
- 例1 値：Kreative Gestaltung von Tempo-30-Zonen? | Amt für Landwirtschaft und Natur; Kanto… | Brienz Rothorn Bahn AG (BRB); Kantons- … | Innovationspotenzial im Kanton Bern | Dekret über das Baubewilligungsverfahre…
  - 同じ表の列：dokument_titel, dokument_geschaefts…, dokument_typ_deutsch, dokument_typ_franz, dokument_ziel_publi…, dokument_geschaeft_…, Übersicht vom

## g0111（1 列）
- 見出し：dokument_geschaeftstitel_franz
- 例1 値：Rapport d`activité 2014 des autorités j… | Loi sur le développement du tourisme (L… | Assainissement rapide des sites contami… | Potentiel d`innovation du canton de Ber… | Election des membres de la Commission d…
  - 同じ表の列：dokument_titel, dokument_geschaefts…, dokument_typ_deutsch, dokument_typ_franz, dokument_ziel_publi…, dokument_geschaeft_…, Übersicht vom

## g0112（1 列）
- 見出し：dokument_typ_deutsch
- 例1 値：Abstimmungsprotokoll | Beilage | GRB | Abstimmungsprotokoll | GR-Wortlautdokument
  - 同じ表の列：dokument_titel, dokument_geschaefts…, dokument_geschaefts…, dokument_typ_franz, dokument_ziel_publi…, dokument_geschaeft_…, Übersicht vom

## g0113（1 列）
- 見出し：dokument_typ_franz
- 例1 値：Texte de l`intervention | Proposition de renvoi | Procès-verbal de l`élection | ACE | Document consignant les décisions du GC
  - 同じ表の列：dokument_titel, dokument_geschaefts…, dokument_geschaefts…, dokument_typ_deutsch, dokument_ziel_publi…, dokument_geschaeft_…, Übersicht vom

## g0114（1 列）
- 見出し：dokument_ziel_publikation
- 例1 値：Deutsch-Französisch | Französisch | Deutsch | Deutsch-Französisch | Französisch
  - 同じ表の列：dokument_titel, dokument_geschaefts…, dokument_geschaefts…, dokument_typ_deutsch, dokument_typ_franz, dokument_geschaeft_…, Übersicht vom

## g0115（1 列）
- 見出し：dokument_geschaeft_uid
- 例1 値：4b01836a832044a9ae9076086b07a588 | 14c02e3725f3416189178c1ef0b7f64d | 10d3de4787184a4d8846034262ddf114 | ec50b29dfa254445bd00d58f47f9183c | 0a5b227f50cd4f15aba19230bac419b4
  - 同じ表の列：dokument_titel, dokument_geschaefts…, dokument_geschaefts…, dokument_typ_deutsch, dokument_typ_franz, dokument_ziel_publi…, Übersicht vom

## g0116（2 列）
- 見出し：Übersicht vom
- 例1 値：2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00
  - 同じ表の列：dokument_titel, dokument_geschaefts…, dokument_geschaefts…, dokument_typ_deutsch, dokument_typ_franz, dokument_ziel_publi…, dokument_geschaeft_…
- 例2 値：2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00
  - 同じ表の列：mitglied_uid, beteiligung_hauptvo…

## g0117（1 列）
- 見出し：mitglied_uid
- 例1 値：862465867126426d956e10475c8b3fec | 360739082dca48b7af5cfc55145ffe16 | 74da2b142ce54b22bb39ab3b636dd3bd | 756a351a020c45ca9f9c572c13d103ec | f72abb8b906246769cfe1830491ea110
  - 同じ表の列：beteiligung_hauptvo…, Übersicht vom

## g0118（1 列）
- 見出し：beteiligung_hauptvorstoesser_mitvorstoesser
- 例1 値：Mitvorstösserin/Mitvorstösser | Hauptvorstösserin/Hauptvorstösser | Hauptvorstösserin/Hauptvorstösser | Hauptvorstösserin/Hauptvorstösser | Mitvorstösserin/Mitvorstösser
  - 同じ表の列：mitglied_uid, Übersicht vom

## g0119（1 列）
- 見出し：modell_lauf
- 例1 値：2026_03 | 2026_03 | 2026_03 | 2026_03 | 2026_03
  - 同じ表の列：indikator, einheit, region, branche, jahr, wert

## g0120（1 列）
- 見出し：indikator
- 例1 値：Wertschöpfung nominal | Wertschöpfung nominal | Wachstum reale Wertschöpfung | Wachstum reale Wertschöpfung | Wertschöpfung nominal
  - 同じ表の列：modell_lauf, einheit, region, branche, jahr, wert

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
