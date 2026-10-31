<!-- b072：29/287 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b072.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0005（3 列）
- 見出し：georegion_type
- 例1 値：CHFL | CHFL | grossregion | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, type
- 例2 値：CHFL | CHFL | CHFL | CHFL | CHFL
  - 同じ表の列：valueCategory, temporal, temporal_type, georegion, agegroup, agegroup_type, sex, type

## g0028（2 列）
- 見出し：Wert
- 例1 値：206 | 875 | 13781977 | 2034073 | 13658213
  - 同じ表の列：Fahrzeugtyp, Jahr, Indikator, Einheit
- 例2 値：113270 | 70173 | 121700 | 126062 | 566075
  - 同じ表の列：Jahr, Energiesektor, Energieträger, Einheit

## g0036（1 列）
- 見出し：Type of Slaughter
- 例1 値：Sanitary | Normal | Sanitary | Normal | Normal
  - 同じ表の列：Year, Canton, Species, Origin of animal, Fitness for consump…, Count

## g0051（1 列）
- 見出し：diff
- 例1 値：-585 | -13 | -3 | 387 | -129
  - 同じ表の列：BVD_AMPEL, TIMESTEP, N_FARMS, total_per_day, percentage

## g0059（2 列）
- 見出し：parameter_decimals
- 例1 値：1 | 0 | 0 | 0 | 0
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit
- 例2 値：0 | 0 | 1 | 0 | 1
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granulari…, parameter_datatype, parameter_unit

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

## g0068（2 列）
- 見出し：UNIT_MES
- 例1 値：UM_6 | UM_6 | UM_6 | UM_6 | UM_6
  - 同じ表の列：PERIOD_REF, CODE_REGION, REGION, INDICATORS, VALUE, STATUS
- 例2 値：UM_26 | UM_2 | UM_2 | UM_18 | UM_2
  - 同じ表の列：PERIOD_REF, REGION, INDICATORS, VALUE, STATUS

## g0071（1 列）
- 見出し：REF_YEAR
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：GEO_COMM, GEO_CANT, VALUE

## g0094（1 列）
- 見出し：theme_en
- 例1 値：['Government and public sector'] | ['Environment'] | ['Regions and cities', 'Education, cult… | ['Government and public sector'] | ['Government and public sector']
  - 同じ表の列：dataset_id, title, title_de, title_fr, title_en, title_it, theme, theme_de

## g0098（1 列）
- 見出し：geschaeft_laufnummer
- 例1 値：2026/5036 | 2026/5084 | 2026/5312 | 2026/5777 | 2026/3195
  - 同じ表の列：dokument_titel, dokument_datum, geschaeft_titel

## g0116（2 列）
- 見出し：Übersicht vom
- 例1 値：2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00
  - 同じ表の列：dokument_titel, dokument_geschaefts…, dokument_geschaefts…, dokument_typ_deutsch, dokument_typ_franz, dokument_ziel_publi…, dokument_geschaeft_…
- 例2 値：2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00 | 2026-10-30 00:00
  - 同じ表の列：mitglied_uid, beteiligung_hauptvo…

## g0118（1 列）
- 見出し：beteiligung_hauptvorstoesser_mitvorstoesser
- 例1 値：Mitvorstösserin/Mitvorstösser | Hauptvorstösserin/Hauptvorstösser | Hauptvorstösserin/Hauptvorstösser | Hauptvorstösserin/Hauptvorstösser | Mitvorstösserin/Mitvorstösser
  - 同じ表の列：mitglied_uid, Übersicht vom

## g0121（1 列）
- 見出し：einheit
- 例1 値：Veränderung ggü. Vorjahr in %, zu Preis… | In CHF, zu laufenden Preisen | In CHF, zu laufenden Preisen | In CHF, zu laufenden Preisen | In CHF, zu laufenden Preisen
  - 同じ表の列：modell_lauf, indikator, region, branche, jahr, wert

## g0134（1 列）
- 見出し：service
- 例1 値：aup | klv | hwt | klv | klv
  - 同じ表の列：year, provider, service_type, age_class, hours

## g0184（1 列）
- 見出し：height
- 例1 値：22.0 | 8.0 | 16.0 | 22.0 | 12.0
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual

## g0190（1 列）
- 見出し：referencePointType
- 例1 値：PLATFORM | PLATFORM | MAIN_STATION_ENTRANCE | MAIN_STATION_ENTRANCE | MAIN_STATION_ENTRANCE
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, validFrom, validTo

## g0194（1 列）
- 見出し：elementSloid
- 例1 値：ch:1:sloid:6128:758331 | ch:1:sloid:7270:0:859564 | ch:1:sloid:5373::02 | ch:1:sloid:7069:53857 | ch:1:sloid:8321:0:886771
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, referencePointSloid, tactileVisualMarks, contrastingAreas, stepFreeAccess, referencePointEleme…, validFrom

## g0204（1 列）
- 見出し：Datierung_von
- 例1 値：1898 | 190204 | 1899 | 1900 | 1901
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_bis, Farbe, Orientierung_Form

## g0207（1 列）
- 見出し：Orientierung_Form
- 例1 値：Vertikal | Vertikal | Horizontal | Vertikal | Vertikal
  - 同じ表の列：ID, Signatur, FotografIn, Titel, Inhalt_Kurzbeschrei…, Datierung_von, Datierung_bis, Farbe

## g0209（1 列）
- 見出し：objectid
- 例1 値：2 | 33 | 10 | 20 | 16
  - 同じ表の列：leistung_in_kwp, modultyp, leistung_modul_in_wp, anzahl_module, wechselrichterleist…, flache, link, geo_point_2d

## g0220（1 列）
- 見出し：Gemeinde Code
- 例1 値：3022 | 3214 | 4421 | 3006 | 3102
  - 同じ表の列：Gemeinde, Kanton, Kanton Code, Geo Point, Geo Shape

## g0235（1 列）
- 見出し：stadtkreis
- 例1 値：Töss | Seen | Töss | Stadt | Töss
  - 同じ表の列：jahr, stichtag, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, quartier_bfs_nr, quartier

## g0245（1 列）
- 見出し：monat
- 例1 値：12 | 12 | 12 | 12 | 12
  - 同じ表の列：jahr, stichtag, wissensstand_am, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis

## g0253（4 列）
- 見出し：date
- 例1 値：2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status
- 例2 値：2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status

## g0261（1 列）
- 見出し：title_rm_CH
- 例1 値：Ja zu sauberem Strom ohne Kohlekraft | Cuntraproposta dal cussegl grond "Nagin… | Cuntraproposta dal cussegl grond "Nagin… | Ja zu sauberem Strom ohne Kohlekraft | Ja zu sauberem Strom ohne Kohlekraft
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0262（1 列）
- 見出し：title_de_CH
- 例1 値：Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0265（1 列）
- 見出し：title_rm_CH
- 例1 値：Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0273（1 列）
- 見出し：THEMA_ID
- 例1 値：3 | 4 | 11 | 10 | 1
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA

## 答えの雛形

```
g0005	
g0028	
g0036	
g0051	
g0059	
g0065	
g0066	
g0068	
g0071	
g0094	
g0098	
g0116	
g0118	
g0121	
g0134	
g0184	
g0190	
g0194	
g0204	
g0207	
g0209	
g0220	
g0235	
g0245	
g0253	
g0261	
g0262	
g0265	
g0273	
```
