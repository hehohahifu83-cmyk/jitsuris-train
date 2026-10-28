# ラベル用シート 002 / 005

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Summe von SG 2
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Titel, Fachgebiet, Versuchszweck, Tierart, Summe von SG 0, Summe von SG 1, Summe von SG 3

## g0122（1 列）
- 見出し：Summe von SG 3
- 例1 値：0 | 0 | 0 | 0 | 10
  - 同じ表の列：Titel, Fachgebiet, Versuchszweck, Tierart, Summe von SG 0, Summe von SG 1, Summe von SG 2

## g0123（1 列）
- 見出し：Category
- 例1 値：MICE_TOTAL | ANIMALS_USED | FISH_TOTAL | FISH_GEN_ENGINEERED | ANIMALS_USED
  - 同じ表の列：Year, Count

## g0124（1 列）
- 見出し：Count
- 例1 値：1110068 | 614581 | 9319 | 112978 | 1098432
  - 同じ表の列：Year, Category

## g0125（2 列）
- 見出し：parameter_group_de
- 例1 値：Pollen | Pollen | Pollen | Pollen | Pollen
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Schnee | Schnee | Schnee | Schnee | Schnee
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0126（2 列）
- 見出し：parameter_group_fr
- 例1 値：Pollen | Pollen | Pollen | Pollen | Pollen
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Neige | Neige | Neige | Neige | Neige
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0127（2 列）
- 見出し：parameter_group_it
- 例1 値：Pollini | Pollini | Pollini | Pollini | Pollini
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Neve | Neve | Neve | Neve | Neve
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0128（2 列）
- 見出し：parameter_group_en
- 例1 値：Pollen | Pollen | Pollen | Pollen | Pollen
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Precipitation | Snow | Snow | Snow | Precipitation
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0129（3 列）
- 見出し：parameter_granularity
- 例1 値：Y | D | D | Y | Y
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_decimals, parameter_datatype, parameter_unit
- 例2 値：Y | Y | M | M | D
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_decimals, parameter_datatype, parameter_unit

## g0130（3 列）
- 見出し：parameter_decimals
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit

## g0131（3 列）
- 見出し：parameter_datatype
- 例1 値：Integer | Integer | Integer | Integer | Integer
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_unit
- 例2 値：Integer | Integer | Integer | Integer | Integer
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_unit

## g0132（1 列）
- 見出し：parameter_unit
- 例1 値：No/m3 | No/m3 | No/m3 | No/m3 | No/m3
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0133（1 列）
- 見出し：parameter_group_de
- 例1 値：Beobachtung visuell | Beobachtung visuell | Beobachtung visuell | Beobachtung visuell | Beobachtung visuell
  - 同じ表の列：parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0134（1 列）
- 見出し：parameter_group_fr
- 例1 値：Observations visuelles | Observations visuelles | Observations visuelles | Observations visuelles | Observations visuelles
  - 同じ表の列：parameter_group_de, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0135（1 列）
- 見出し：parameter_group_it
- 例1 値：Osservazioni visive | Osservazioni visive | Osservazioni visive | Osservazioni visive | Osservazioni visive
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0136（1 列）
- 見出し：parameter_group_en
- 例1 値：Visual observation | Visual observation | Visual observation | Visual observation | Visual observation
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

## g0137（1 列）
- 見出し：parameter_unit
- 例1 値：No | % | No | No | No
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0138（1 列）
- 見出し：parameter_unit
- 例1 値：mm | cm | mm | No | cm
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype

## g0139（1 列）
- 見出し：Kostenbereich
- 例1 値：Gesundheit Luft | Gebäude Luft | Gesundheit Luft | Ernteausfälle Luft | Gesundheit Luft
  - 同じ表の列：Jahr, Unterkostenbereich, Kostenart, Verkehrstrager, Verkehrsmittel, Verkehrsart, Verkehrsform, Infrastrukturtyp

## g0140（1 列）
- 見出し：Unterkostenbereich
- 例1 値：Reinigungskosten | Demenz | Atemwegserkrankungen | Atemwegserkrankungen | COPD
  - 同じ表の列：Jahr, Kostenbereich, Kostenart, Verkehrstrager, Verkehrsmittel, Verkehrsart, Verkehrsform, Infrastrukturtyp

## g0141（1 列）
- 見出し：Kostenart
- 例1 値：Immaterielle Kosten | Immaterielle Kosten | Immaterielle Kosten | Immaterielle Kosten | Wiederbesetzungskosten
  - 同じ表の列：Jahr, Kostenbereich, Unterkostenbereich, Verkehrstrager, Verkehrsmittel, Verkehrsart, Verkehrsform, Infrastrukturtyp

## g0142（1 列）
- 見出し：Verkehrstrager
- 例1 値：Schienenverkehr | Luftverkehr | Luftverkehr | Strassenverkehr | Luftverkehr
  - 同じ表の列：Jahr, Kostenbereich, Unterkostenbereich, Kostenart, Verkehrsmittel, Verkehrsart, Verkehrsform, Infrastrukturtyp

## g0143（1 列）
- 見出し：Verkehrsmittel
- 例1 値：Business Aviation | MR | Mofa | Helikopter | Pedelec
  - 同じ表の列：Jahr, Kostenbereich, Unterkostenbereich, Kostenart, Verkehrstrager, Verkehrsart, Verkehrsform, Infrastrukturtyp

## g0144（1 列）
- 見出し：Verkehrsart
- 例1 値：Güterverkehr | Personenverkehr | Güterverkehr | Personenverkehr | Personenverkehr
  - 同じ表の列：Jahr, Kostenbereich, Unterkostenbereich, Kostenart, Verkehrstrager, Verkehrsmittel, Verkehrsform, Infrastrukturtyp

## g0145（1 列）
- 見出し：Verkehrsform
- 例1 値：Motorisierter Individualverkehr | Langsamverkehr | Güterverkehr | Personenverkehr | Güterverkehr
  - 同じ表の列：Jahr, Kostenbereich, Unterkostenbereich, Kostenart, Verkehrstrager, Verkehrsmittel, Verkehrsart, Infrastrukturtyp

## g0146（1 列）
- 見出し：Infrastrukturtyp
- 例1 値：Regionalflughäfen | Strasse | Strasse | Regionalflughäfen | Landesflughäfen
  - 同じ表の列：Jahr, Kostenbereich, Unterkostenbereich, Kostenart, Verkehrstrager, Verkehrsmittel, Verkehrsart, Verkehrsform

## g0147（1 列）
- 見出し：Soziale Kosten
- 例1 値：743.9890945 | 2992344.13 | 5431.849071 | 13.13783183 | 0
  - 同じ表の列：Jahr, Kostenbereich, Unterkostenbereich, Kostenart, Verkehrstrager, Verkehrsmittel, Verkehrsart, Verkehrsform

## g0148（1 列）
- 見出し：Version 610.5281/zenodo.6517164
- 例1 値：Version 210.5281/zenodo.5702813 | Version 410.5281/zenodo.6473417 | Version 510.5281/zenodo.6475373 | Version 310.5281/zenodo.6414758 | View all 6 versions
  - 同じ表の列：Apr 8, 2022

## g0149（1 列）
- 見出し：Apr 8, 2022
- 例1 値：Apr 8, 2022 | Apr 8, 2022 | Nov 14, 2021 | Apr 8, 2022
  - 同じ表の列：Version 610.5281/ze…

## g0150（1 列）
- 見出し：Week
- 例1 値：35 | 11 | 9 | 10 | 41
  - 同じ表の列：Year, Ending, Age, NoDeaths_EP, Expected, LowerB, UpperB, Diff

## g0151（1 列）
- 見出し：Ending
- 例1 値：07.07.2024 | 11.04.2010 | 17.04.2022 | 14.09.2025 | 16.11.2014
  - 同じ表の列：Year, Week, Age, NoDeaths_EP, Expected, LowerB, UpperB, Diff

## g0152（1 列）
- 見出し：Age
- 例1 値：65+ | 0-64 | 0-64 | 0-64 | 0-64
  - 同じ表の列：Year, Week, Ending, NoDeaths_EP, Expected, LowerB, UpperB, Diff

## g0153（1 列）
- 見出し：NoDeaths_EP
- 例1 値：159 | 961 | 172 | 170 | 156
  - 同じ表の列：Year, Week, Ending, Age, Expected, LowerB, UpperB, Diff

## g0154（1 列）
- 見出し：Expected
- 例1 値：1156 | 168 | 161 | 159 | 173
  - 同じ表の列：Year, Week, Ending, Age, NoDeaths_EP, LowerB, UpperB, Diff

## g0155（1 列）
- 見出し：LowerB
- 例1 値：142 | 138 | 136 | 151 | 147
  - 同じ表の列：Year, Week, Ending, Age, NoDeaths_EP, Expected, UpperB, Diff

## g0156（1 列）
- 見出し：UpperB
- 例1 値：213 | 191 | 223 | 207 | 210
  - 同じ表の列：Year, Week, Ending, Age, NoDeaths_EP, Expected, LowerB, Diff

## g0157（1 列）
- 見出し：Diff
- 例1 値：. | . | . | . | .
  - 同じ表の列：Year, Week, Ending, Age, NoDeaths_EP, Expected, LowerB, UpperB

## g0158（2 列）
- 見出し：TIME_PERIOD
- 例1 値：2026-W01 | 2026-W01 | 2026-W01 | 2026-W01 | 2026-W01
  - 同じ表の列：GEO, AGE, SEX, OBS_STATUS, OBS_VALUE
- 例2 値：2026-W02 | 2026-W02 | 2026-W03 | 2026-W02 | 2026-W01
  - 同じ表の列：GEO, AGE, SEX, OBS_STATUS, OBS_VALUE

## g0159（1 列）
- 見出し：GEO
- 例1 値：CH023 | CH054 | CH051 | CH013 | CH012
  - 同じ表の列：TIME_PERIOD, AGE, SEX, OBS_STATUS, OBS_VALUE

## g0160（1 列）
- 見出し：AGE
- 例1 値：Y50T54 | Y40T44 | Y20T24 | Y25T29 | Y10T14
  - 同じ表の列：TIME_PERIOD, GEO, SEX, OBS_STATUS, OBS_VALUE

## g0161（2 列）
- 見出し：SEX
- 例1 値：T | F | F | T | F
  - 同じ表の列：TIME_PERIOD, GEO, AGE, OBS_STATUS, OBS_VALUE
- 例2 値：M | M | T | T | F
  - 同じ表の列：TIME_PERIOD, GEO, AGE, OBS_STATUS, OBS_VALUE

## g0162（2 列）
- 見出し：OBS_STATUS
- 例1 値：P | P | P | P | P
  - 同じ表の列：TIME_PERIOD, GEO, AGE, SEX, OBS_VALUE
- 例2 値：P | P | P | P | P
  - 同じ表の列：TIME_PERIOD, GEO, AGE, SEX, OBS_VALUE

## g0163（2 列）
- 見出し：OBS_VALUE
- 例1 値：7 | 14 | 1 | 32 | 0
  - 同じ表の列：TIME_PERIOD, GEO, AGE, SEX, OBS_STATUS
- 例2 値：9 | 1 | 12 | 48 | 1
  - 同じ表の列：TIME_PERIOD, GEO, AGE, SEX, OBS_STATUS

## g0164（1 列）
- 見出し：GEO
- 例1 値：CH05 | CH05 | CH | CH05 | CH04
  - 同じ表の列：TIME_PERIOD, AGE, SEX, OBS_STATUS, OBS_VALUE

## g0165（1 列）
- 見出し：AGE
- 例1 値：Y70T74 | Y60T64 | Y30T34 | Y85T89 | _T
  - 同じ表の列：TIME_PERIOD, GEO, SEX, OBS_STATUS, OBS_VALUE

## g0166（1 列）
- 見出し：monitoring_program
- 例1 値：BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_SG
  - 同じ表の列：station_number, latidude, date_of_probing, parameter_type, value, lower_LOD, unit

## g0167（1 列）
- 見出し：station_number
- 例1 値：CH22092 | CH21070 | CH21082 | CH21057 | CH21024
  - 同じ表の列：monitoring_program, latidude, date_of_probing, parameter_type, value, lower_LOD, unit

## g0168（1 列）
- 見出し：latidude
- 例1 値：45.9922 | 46.4463 | 45.988 | 46.1655 | 46.12
  - 同じ表の列：monitoring_program, station_number, date_of_probing, parameter_type, value, lower_LOD, unit

## g0169（1 列）
- 見出し：date_of_probing
- 例1 値：2008-08-04T00:00:00 | 2008-07-10T00:00:00 | 2008-07-01T00:00:00 | 2007-07-17T00:00:00 | 2007-08-27T00:00:00
  - 同じ表の列：monitoring_program, station_number, latidude, parameter_type, value, lower_LOD, unit

## g0170（1 列）
- 見出し：parameter_type
- 例1 値：E. coli | E. coli | E. coli | E. coli | E. coli
  - 同じ表の列：monitoring_program, station_number, latidude, date_of_probing, value, lower_LOD, unit

## g0171（1 列）
- 見出し：value
- 例1 値：10 | 10 | 31 | 20 | 10
  - 同じ表の列：monitoring_program, station_number, latidude, date_of_probing, parameter_type, lower_LOD, unit

## g0172（1 列）
- 見出し：lower_LOD
- 例1 値：10 | 10 | 10 | 10 | 10
  - 同じ表の列：monitoring_program, station_number, latidude, date_of_probing, parameter_type, value, unit

## g0173（1 列）
- 見出し：unit
- 例1 値：CFU/100ml | CFU/100ml | CFU/100ml | CFU/100ml | CFU/100ml
  - 同じ表の列：monitoring_program, station_number, latidude, date_of_probing, parameter_type, value, lower_LOD

## g0174（1 列）
- 見出し：Anzahl von fact_kurs_hist_sid
- 例1 値：74 | 69 | 104 | 1 | 237
  - 同じ表の列：Jahr

## g0175（1 列）
- 見出し：year_key
- 例1 値：2016 | 2020 | 2025 | 2020 | 2024
  - 同じ表の列：taetigkeitsbereich_…, taetigkeitsbereich_…, taetigkeitsbereich_…, Summe von eib_einsa…, Summe von eib_activ…

## g0176（1 列）
- 見出し：taetigkeitsbereich_de
- 例1 値：2 Sozialwesen | 5 Landwirtschaft | 6 Entwicklungszusammenarbeit und humani… | 8 Schulwesen: Vorschulstufe bis Sekunda… | 7 Bewältigung von Katastrophen und Notl…
  - 同じ表の列：year_key, taetigkeitsbereich_…, taetigkeitsbereich_…, Summe von eib_einsa…, Summe von eib_activ…

## g0177（1 列）
- 見出し：taetigkeitsbereich_fr
- 例1 値：5 Agriculture | 1 Santé | 4 Protection de la nature et de l'envir… | 5 Agriculture | 7 Prévention et maîtrise des catastroph…
  - 同じ表の列：year_key, taetigkeitsbereich_…, taetigkeitsbereich_…, Summe von eib_einsa…, Summe von eib_activ…

## g0178（1 列）
- 見出し：taetigkeitsbereich_it
- 例1 値：2 Servizi sociali | 7 IVorbeugung und Bewältigung von Katas… | 8 Scuola, dal livello prescolastico al … | 1 Sanità | 4 Protezione dell'ambiente e della natu…
  - 同じ表の列：year_key, taetigkeitsbereich_…, taetigkeitsbereich_…, Summe von eib_einsa…, Summe von eib_activ…

## g0179（1 列）
- 見出し：Summe von eib_einsatzplatz_verfuegt
- 例1 値：0 | 37 | 9 | 24 | 36
  - 同じ表の列：year_key, taetigkeitsbereich_…, taetigkeitsbereich_…, taetigkeitsbereich_…, Summe von eib_activ…

## g0180（1 列）
- 見出し：Summe von eib_active_flag
- 例1 値：4 | 7 | 3 | 7 | 1358
  - 同じ表の列：year_key, taetigkeitsbereich_…, taetigkeitsbereich_…, taetigkeitsbereich_…, Summe von eib_einsa…

## g0181（2 列）
- 見出し：hh
- 例1 値：staat | staat | ktn | ktn | staat
  - 同じ表の列：model, variable, jahr, source
- 例2 値：ktn | ktn | ktn | ktn | ktn
  - 同じ表の列：arten, jahr, value, dim, unit, model

## g0182（2 列）
- 見出し：model
- 例1 値：fs | fs | fs | fs | fs
  - 同じ表の列：hh, variable, jahr, source
- 例2 値：gfs | gfs | gfs | gfs | gfs
  - 同じ表の列：arten, jahr, value, dim, hh, unit

## g0183（1 列）
- 見出し：variable
- 例1 値：ausgaben_ord | ausgaben | ausgaben | saldo | saldo_ord
  - 同じ表の列：hh, model, jahr, source

## g0184（1 列）
- 見出し：source
- 例1 値：Rechnung | Vorhandene Daten | Rechnung | Rechnung | Rechnung
  - 同じ表の列：hh, model, variable, jahr

## g0185（1 列）
- 見出し：country_code
- 例1 値：BGR | AUT | CHE | BRA | BGR
  - 同じ表の列：indicator, jahr, unit, source

## g0186（1 列）
- 見出し：indicator
- 例1 値：staatsquote | staatsquote | defizit_ueberschuss | einnahmenquote | defizit_ueberschuss
  - 同じ表の列：country_code, jahr, unit, source

## g0187（1 列）
- 見出し：unit
- 例1 値：percent_gdp | percent_gdp | percent_gdp | percent_gdp | percent_gdp
  - 同じ表の列：country_code, indicator, jahr, source

## g0188（1 列）
- 見出し：source
- 例1 値：IMF Goverment Finance Statistics (GFS),… | IMF Goverment Finance Statistics (GFS),… | OECD Economic Outlook 119 (June 2026); … | IMF Goverment Finance Statistics (GFS),… | IMF Goverment Finance Statistics (GFS),…
  - 同じ表の列：country_code, indicator, jahr, unit

## g0189（1 列）
- 見出し：arten
- 例1 値：2822 | 2612 | 251 | 252 | 2631
  - 同じ表の列：jahr, value, dim, hh, unit, model

## g0190（1 列）
- 見出し：value
- 例1 値：321756756.29 | 212745767.66 | 5692937402.27 | 2427147132.88 | 5535580034.26
  - 同じ表の列：arten, jahr, dim, hh, unit, model

## g0191（1 列）
- 見出し：dim
- 例1 値：aufwand | aufwand | aufwand | aufwand | ertrag
  - 同じ表の列：arten, jahr, value, hh, unit, model

## g0192（1 列）
- 見出し：unit
- 例1 値：CHF | CHF | CHF | CHF | CHF
  - 同じ表の列：arten, jahr, value, dim, hh, model

## g0193（1 列）
- 見出し：Stucktitel
- 例1 値：Biografie: Ein Spiel | Wilhelm Tell für die Schule | Die Collagierte Zeit. Ingeborg Bachmann… | Santa Cruz | Jonas und sein Veteran. Ein Palaver
  - 同じ表の列：Land, Sprache

## g0194（1 列）
- 見出し：Land
- 例1 値：SVK | FIN | ITA | LUX | ZAF
  - 同じ表の列：Stucktitel, Sprache

## g0195（1 列）
- 見出し：Sprache
- 例1 値：cat | lva | slv | ara | gre
  - 同じ表の列：Stucktitel, Land

## g0196（1 列）
- 見出し：Eidgenoessischer_Gebaeudeidentifikator
- 例1 値：40325 | 35535 | 39373 | 34866 | 35401
  - 同じ表の列：Kanton, BFS_NR, Eidgenoessischer_Gr…, Grundbuchkreisnummer, Grundstuecksnummer, Amtliche_Gebaeudenu…, E-Gebaeudekoordinate, N-Gebaeudekoordinate

## g0197（1 列）
- 見出し：Eidgenoessischer_Grundstuecksidentifikator
- 例1 値：CH727792876157 | CH830877670123 | CH933477877922 | CH259908776773 | CH795577903542
  - 同じ表の列：Eidgenoessischer_Ge…, Kanton, BFS_NR, Grundbuchkreisnummer, Grundstuecksnummer, Amtliche_Gebaeudenu…, E-Gebaeudekoordinate, N-Gebaeudekoordinate

## g0198（1 列）
- 見出し：Grundbuchkreisnummer
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Eidgenoessischer_Ge…, Kanton, BFS_NR, Eidgenoessischer_Gr…, Grundstuecksnummer, Amtliche_Gebaeudenu…, E-Gebaeudekoordinate, N-Gebaeudekoordinate

## g0199（1 列）
- 見出し：Grundstuecksnummer
- 例1 値：8114 | 427 | 4059 | 3352 | 4792
  - 同じ表の列：Eidgenoessischer_Ge…, Kanton, BFS_NR, Eidgenoessischer_Gr…, Grundbuchkreisnummer, Amtliche_Gebaeudenu…, E-Gebaeudekoordinate, N-Gebaeudekoordinate

## g0200（1 列）
- 見出し：Amtliche_Gebaeudenummer
- 例1 値：10100197 | 11200704 | 11500904 | 11400536 | 08901162
  - 同じ表の列：Eidgenoessischer_Ge…, Kanton, BFS_NR, Eidgenoessischer_Gr…, Grundbuchkreisnummer, Grundstuecksnummer, E-Gebaeudekoordinate, N-Gebaeudekoordinate

## g0201（1 列）
- 見出し：E-Gebaeudekoordinate
- 例1 値：2675353.834 | 2675427.344 | 2699506.246 | 2708800.732 | 2702703.065
  - 同じ表の列：Eidgenoessischer_Ge…, Kanton, BFS_NR, Eidgenoessischer_Gr…, Grundbuchkreisnummer, Grundstuecksnummer, Amtliche_Gebaeudenu…, N-Gebaeudekoordinate

## g0202（1 列）
- 見出し：N-Gebaeudekoordinate
- 例1 値：1255073.858 | 1241243.975 | 1237413.089 | 1244194.862 | 1239962.783
  - 同じ表の列：Eidgenoessischer_Ge…, Kanton, BFS_NR, Eidgenoessischer_Gr…, Grundbuchkreisnummer, Grundstuecksnummer, Amtliche_Gebaeudenu…, E-Gebaeudekoordinate

## g0203（1 列）
- 見出し：Koordinatenherkunft_Code
- 例1 値：901 | 901 | 901 | 901 | 901
  - 同じ表の列：Eidgenoessischer_Ge…, Kanton, BFS_NR, Eidgenoessischer_Gr…, Grundbuchkreisnummer, Grundstuecksnummer, Amtliche_Gebaeudenu…, E-Gebaeudekoordinate

## g0204（1 列）
- 見出し：label
- 例1 値：züric | abwassermonitoring | Ehe | Fussball | wollishofen
  - 同じ表の列：nb_visits, nb_hits, nb_hits_with_time_g…, min_time_generation, max_time_generation, sum_time_spent, bounce_count, exit_nb_visits

## g0205（1 列）
- 見出し：nb_visits
- 例1 値：2 | 6 | 2 | 3 | 3
  - 同じ表の列：label, nb_hits, nb_hits_with_time_g…, min_time_generation, max_time_generation, sum_time_spent, bounce_count, exit_nb_visits

## g0206（1 列）
- 見出し：nb_hits
- 例1 値：6 | 6 | 5 | 8 | 2
  - 同じ表の列：label, nb_visits, nb_hits_with_time_g…, min_time_generation, max_time_generation, sum_time_spent, bounce_count, exit_nb_visits

## g0207（1 列）
- 見出し：nb_hits_with_time_generation
- 例1 値：0 | 0 | 0 | 1 | 1
  - 同じ表の列：label, nb_visits, nb_hits, min_time_generation, max_time_generation, sum_time_spent, bounce_count, exit_nb_visits

## g0208（1 列）
- 見出し：min_time_generation
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：label, nb_visits, nb_hits, nb_hits_with_time_g…, max_time_generation, sum_time_spent, bounce_count, exit_nb_visits

## g0209（1 列）
- 見出し：max_time_generation
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：label, nb_visits, nb_hits, nb_hits_with_time_g…, min_time_generation, sum_time_spent, bounce_count, exit_nb_visits

## g0210（1 列）
- 見出し：sum_time_spent
- 例1 値：15 | 34 | 1238 | 1 | 0
  - 同じ表の列：label, nb_visits, nb_hits, nb_hits_with_time_g…, min_time_generation, max_time_generation, bounce_count, exit_nb_visits

## g0211（1 列）
- 見出し：bounce_count
- 例1 値：2 | 0 | 0 | 0 | 0
  - 同じ表の列：label, nb_visits, nb_hits, nb_hits_with_time_g…, min_time_generation, max_time_generation, sum_time_spent, exit_nb_visits

## g0212（1 列）
- 見出し：exit_nb_visits
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：label, nb_visits, nb_hits, nb_hits_with_time_g…, min_time_generation, max_time_generation, sum_time_spent, bounce_count

## g0213（1 列）
- 見出し：sum_daily_nb_uniq_visitors
- 例1 値：5 | 2 | 5 | 2 | 2
  - 同じ表の列：label, nb_visits, nb_hits, nb_hits_with_time_g…, min_time_generation, max_time_generation, sum_time_spent, bounce_count

## g0214（2 列）
- 見出し：Kategorie
- 例1 値：Kulturschaffende | Kulturschaffende | Kulturschaffende | Kulturschaffende | Kulturschaffende
  - 同じ表の列：Sparte, Nachgefragt, Beschluss, Status, Eingangsdatum, Beschlussdatum, ID
- 例2 値：Kultur | Sport | Sport | Denkmalpflege | Sport
  - 同じ表の列：id, jahr, unterstutztes_proje…, begunstigte, beitrag_chf_pro_pro…

## g0215（1 列）
- 見出し：Sparte
- 例1 値：Tanz/Theater | Musik | Musik | Musik | Musik
  - 同じ表の列：Kategorie, Nachgefragt, Beschluss, Status, Eingangsdatum, Beschlussdatum, ID

## g0216（1 列）
- 見出し：Nachgefragt
- 例1 値：20900 | 6000 | 1000 | 42300 | 1335000
  - 同じ表の列：Kategorie, Sparte, Beschluss, Status, Eingangsdatum, Beschlussdatum, ID

## g0217（1 列）
- 見出し：Beschluss
- 例1 値：600 | 2800 | 0 | 24600 | 6000
  - 同じ表の列：Kategorie, Sparte, Nachgefragt, Status, Eingangsdatum, Beschlussdatum, ID

## g0218（6 列）
- 見出し：Status
- 例1 値：Ablehnung | Ausbezahlt | Ablehnung | Ablehnung | Ausbezahlt
  - 同じ表の列：Kategorie, Sparte, Nachgefragt, Beschluss, Eingangsdatum, Beschlussdatum, ID
- 例2 値：laufend | laufend | laufend | laufend | laufend
  - 同じ表の列：Titel, Datum, Verwaltungsebene, Typ, Total der Gemeinden, Ausgezählte Gemeind…, Letzte Änderung, Stimmbeteiligung

## g0219（1 列）
- 見出し：Eingangsdatum
- 例1 値：2020-04-14 | 2020-09-17 | 2020-04-14 | 2020-04-29 | 2020-09-14
  - 同じ表の列：Kategorie, Sparte, Nachgefragt, Beschluss, Status, Beschlussdatum, ID

## g0220（1 列）
- 見出し：Beschlussdatum
- 例1 値：2020-07-10 | 2020-07-21 | 2020-09-03 | 2020-06-09 | 2020-06-17
  - 同じ表の列：Kategorie, Sparte, Nachgefragt, Beschluss, Status, Eingangsdatum, ID

## g0221（1 列）
- 見出し：ID
- 例1 値：7bef0b22 | e6a54389 | b74f0cfc | 54a04e9b | 3c0bc424
  - 同じ表の列：Kategorie, Sparte, Nachgefragt, Beschluss, Status, Eingangsdatum, Beschlussdatum

## g0222（1 列）
- 見出し：Stichtag
- 例1 値：2019-08-31T00:00:00 | 2023-03-31T00:00:00 | 2016-08-31T00:00:00 | 2019-02-28T00:00:00 | 2019-11-30T00:00:00
  - 同じ表の列：Kennzahl, Wert

## g0223（1 列）
- 見出し：Kennzahl
- 例1 値：Total Fondsvolumen | Total Fondsvolumen | Total Fondsvolumen | Total Fondsvolumen | Total Fondsvolumen
  - 同じ表の列：Stichtag, Wert

## g0224（1 列）
- 見出し：Wert
- 例1 値：46677757005.336395 | 127270072779.47827 | 138245391016.21417 | 45051472559.95336 | 68014111475.11671
  - 同じ表の列：Stichtag, Kennzahl

## g0225（1 列）
- 見出し：raumeinheit
- 例1 値：Kanton | Kanton | Kanton | Kanton | Kanton
  - 同じ表の列：jahr, gesamtausgaben, bruttoinlandprodukt, staatsquote_in_proz…

## g0226（1 列）
- 見出し：gesamtausgaben
- 例1 値：13542518.95 | 14369818.41 | 11390570.95 | 12261002.31 | 11178312.28
  - 同じ表の列：jahr, raumeinheit, bruttoinlandprodukt, staatsquote_in_proz…

## g0227（1 列）
- 見出し：bruttoinlandprodukt
- 例1 値：152930932.5 | 141721613.6 | 148710709.9 | 140136373.3 | 144486878.1
  - 同じ表の列：jahr, raumeinheit, gesamtausgaben, staatsquote_in_proz…

## g0228（1 列）
- 見出し：staatsquote_in_prozent
- 例1 値：8.4 | 8.7 | 9.1 | 8.5 | 8.7
  - 同じ表の列：jahr, raumeinheit, gesamtausgaben, bruttoinlandprodukt

## g0229（1 列）
- 見出し：GEFIS_EINHEIT
- 例1 値：810700E | 816400E | 814200E | 812400E | 810200E
  - 同じ表の列：INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG

## g0230（1 列）
- 見出し：INDIKATOR_ID
- 例1 値：Fremdkapital | Fremdkapital | Fremdkapital | Fremdkapital | Fremdkapital
  - 同じ表の列：GEFIS_EINHEIT, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG

## g0231（1 列）
- 見出し：INDIKATOR_JAHR
- 例1 値：202 Langfristige Schulden [Fr./Einw.] | 202 Langfristige Schulden [Fr./Einw.] | 202 Langfristige Schulden [Fr./Einw.] | 202 Langfristige Schulden [Fr./Einw.] | 202 Langfristige Schulden [Fr./Einw.]
  - 同じ表の列：GEFIS_EINHEIT, INDIKATOR_ID, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG

## g0232（1 列）
- 見出し：INDIKATOR_VALUE
- 例1 値：2012 | 2015 | 2013 | 1997 | 2012
  - 同じ表の列：GEFIS_EINHEIT, INDIKATOR_ID, INDIKATOR_JAHR, EINHEIT_KURZ, EINHEIT_LANG

## g0233（1 列）
- 見出し：EINHEIT_KURZ
- 例1 値：4761 | 1075 | 2664 | 3141 | 8363
  - 同じ表の列：GEFIS_EINHEIT, INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_LANG

## g0234（1 列）
- 見出し：EINHEIT_LANG
- 例1 値：Fr./Einw. | Fr./Einw. | Fr./Einw. | Fr./Einw. | Fr./Einw.
  - 同じ表の列：GEFIS_EINHEIT, INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ

## g0235（1 列）
- 見出し：gruppe
- 例1 値：Per- und polyfluorierte Alkylsubstanzen… | Kontaminanten, sonstige | Kontaminanten, sonstige | Kontaminanten, sonstige | Natürliche Inhaltsstoffe
  - 同じ表の列：gruppe_id, analyt, analyt_id, kategorie, kategorie_sortierung, einheit, farbcode, start_datum

## g0236（1 列）
- 見出し：gruppe_id
- 例1 値：1 | 3 | 3 | 1 | 3
  - 同じ表の列：gruppe, analyt, analyt_id, kategorie, kategorie_sortierung, einheit, farbcode, start_datum

## g0237（1 列）
- 見出し：analyt
- 例1 値：Chlorothalonil R417888 (Sulfonsäure) | Acesulfam-K | Chlorothalonil R417888 (Sulfonsäure) | Acesulfam-K | Perfluoroctansulfonsäure (PFOS)
  - 同じ表の列：gruppe, gruppe_id, analyt_id, kategorie, kategorie_sortierung, einheit, farbcode, start_datum

## g0238（1 列）
- 見出し：analyt_id
- 例1 値：3 | 11 | 16 | 9 | 4
  - 同じ表の列：gruppe, gruppe_id, analyt, kategorie, kategorie_sortierung, einheit, farbcode, start_datum

## g0239（1 列）
- 見出し：kategorie
- 例1 値：0.02 - <0.04 | 0.7 - <1.0 | 0.06 - <0.08 | <0.02 | <0.1
  - 同じ表の列：gruppe, gruppe_id, analyt, analyt_id, kategorie_sortierung, einheit, farbcode, start_datum

## g0240（1 列）
- 見出し：kategorie_sortierung
- 例1 値：1 | 3 | 3 | 4 | 1
  - 同じ表の列：gruppe, gruppe_id, analyt, analyt_id, kategorie, einheit, farbcode, start_datum

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
