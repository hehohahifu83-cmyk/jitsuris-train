<!-- b067：35/353 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b067.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0022（1 列）
- 見出し：site
- 例1 値：7a | 4 | 4 | 1 | 4
  - 同じ表の列：parameter, value, unit

## g0023（1 列）
- 見出し：parameter
- 例1 値：latitude | latitude | magl | latitude | magl
  - 同じ表の列：site, value, unit

## g0033（1 列）
- 見出し：schultraeger
- 例1 値：Grüningen | Affoltern a.A.-Aeugst | Hombrechtikon | Aeugst a.A. | Adliswil
  - 同じ表の列：stand, kanton, jahr, schultraeger_code, schultraeger_typ, staatsangehoerigkeit, staatsangehoerigkei…, anzahl

## g0069（1 列）
- 見出し：species
- 例1 値：Cattle | Pigeon | Cattle | Dog | Cattle
  - 同じ表の列：year, canton, diseasesGroup, diseases, count

## g0073（1 列）
- 見出し：parameter_group_it
- 例1 値：Precipitazioni | Precipitazioni | Precipitazioni | Precipitazioni | Precipitazioni
  - 同じ表の列：parameter_group_de, parameter_group_fr, parameter_group_en, parameter_granulari…, parameter_decimals, parameter_datatype, parameter_unit

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

## g0083（1 列）
- 見出し：Settimana
- 例1 値：19 | 11 | 20 | 16 | 1
  - 同じ表の列：AC, Fine, Eta, Num_Decessi, Atteso, Lim_inf, Lim_sup, Eccessi

## g0097（1 列）
- 見出し：PERIOD_REF
- 例1 値：1979/1985 | 2019 | 2018 | 2019 | 2019
  - 同じ表の列：PERIOD_COMP, REGION, INDICATORS, UNIT_MES, VALUE, STATUS, STATUS_1

## g0098（1 列）
- 見出し：PERIOD_COMP
- 例1 値：2004/2009 | 2004/2009 | 2004/2009 | 2004/2009 | 2004/2009
  - 同じ表の列：PERIOD_REF, REGION, INDICATORS, UNIT_MES, VALUE, STATUS, STATUS_1

## g0107（1 列）
- 見出し：Datensatztitel
- 例1 値：Eidgenössische und kantonale Wahlen: Ka… | Landratswahlen: Wahlkreise | OGD-Portal: Tägliche Nutzung nach Daten… | Bewohnte Wohnungen nach Bewohnertyp, Ge… | Apotheken mit Betriebsbewilligung oder …
  - 同じ表の列：Datum, Datensatz ID, Visitors, Interactions

## g0112（1 列）
- 見出し：Temperatur
- 例1 値：12.852 | 7.9051 | 21.53 | 8.5547 | 6.0567
  - 同じ表の列：Anfangszeit, Druck, Feuchte

## g0119（2 列）
- 見出し：Geo Shape
- 例1 値：{"coordinates": [[[7.590740106990192, 4… | {"coordinates": [[[7.586705685763728, 4… | {"coordinates": [[[7.587760666756755, 4… | {"coordinates": [[[7.589198970151025, 4… | {"coordinates": [[[7.589478035488302, 4…
  - 同じ表の列：Geo Point, Fussgängerzonen-ID, Regime, Zum Objekt navigier…
- 例2 値：{"coordinates": [[[7.592234657243623, 4… | {"coordinates": [[[7.596971742897135, 4… | {"coordinates": [[[7.594647883042579, 4… | {"coordinates": [[[7.588712113188724, 4… | {"coordinates": [[[7.588330345162404, 4…
  - 同じ表の列：Geo Point, Objekt-ID, Infos, Zufahrt, Zum Objekt navigier…

## g0147（1 列）
- 見出し：geschaeft_typ_deutsch
- 例1 値：Motion | Interpellation | Ernennung / Wahl | Motion | Kreditgeschäft GR
  - 同じ表の列：geschaeft_nr, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0151（1 列）
- 見出し：geschaeft_vorberatende_kommission_uid
- 例1 値：1ea6c3cf0fde4b5283eb9dab423b160b | f2cb74be68324391a0ab07a565d1ce98 | da02607aa637486b91e4e64a34b77f06 | da02607aa637486b91e4e64a34b77f06 | da02607aa637486b91e4e64a34b77f06
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0164（1 列）
- 見出し：geo_point
- 例1 値：46.6998577038841, 8.84528576935237 | 46.6923784361034, 9.55654847554976 | 46.8549502078628, 9.50525183143168 | 46.7837414170555, 9.81397212233962 | 46.7986066454662, 9.82642563332892
  - 同じ表の列：projekttragerschaft, infrastruktur, gemeinde

## g0175（1 列）
- 見出し：monat_jahr
- 例1 値：2026-09 | 2026-08 | 2026-08 | 2026-09 | 2026-06
  - 同じ表の列：jahr, monat, altersklasse, staat_d, kreis, quartiergruppe, anzahl

## g0187（1 列）
- 見出し：nicht_teilgenommen
- 例1 値：72 | 210 | 379 | 33 | 118
  - 同じ表の列：datum, bfsnr, gemeinde, politischerkreis, quartiergruppen, altersklassen, teilgenommen, stimmbeteiligung

## g0191（1 列）
- 見出し：Geschäftsnummer
- 例1 値：61.13.37 | 22.07.06 | 32.15.01B | 12.11.02 | 51.19.107
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsart ID, Federführung ID, process_state_id, Eröffnung, Abschluss, letzte Änderung

## g0203（1 列）
- 見出し：geschaftstitel
- 例1 値：Kantonsbürgerrechtsgesuche per 23. Mai … | Ersatzwahl von zwei Mitgliedern der Jus… | Interpellation von Carmen Haag vom 12. … | Beschluss betreffend Genehmigung der "Ä… | Motion Ruth Mettler und Ernst Ritzi gem…
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, geschaeftsnummer, grg_nummer, geschaftsart, kennung, sachbegriff_grgeko_1, status

## g0237（1 列）
- 見出し：designation
- 例1 値：Parking | Parkplätze | Parking | Parkplatz | Parking
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0243（1 列）
- 見出し：kaderstufe
- 例1 値：Mittleres Kader | Mittleres Kader | Kein Kader | Mittleres Kader | Oberes Kader
  - 同じ表の列：jahr, direktion_code, personalgruppe, kennzahl, wert, einheit

## g0248（1 列）
- 見出し：Signatur
- 例1 値：SLA-Glauser-B-1-SCN-08 | SLA-Glauser-B-1-MUR-01 | SLA-Glauser-E-03-B-1-MUEL-21 | SLA-Glauser-B-1-MES-02 | SLA-Glauser-A-1/74
  - 同じ表の列：ID, AutorIn, Titel, Titelvariante, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung

## g0261（1 列）
- 見出し：Institutionstyp
- 例1 値：Bibliothek | Bibliothek | Bibliothek | Bibliothek | Bibliothek
  - 同じ表の列：ISIL, Status, Mutterinstitution, VZ-Sigel, VZ-Code, Institutionskategor…, Grossregion, Adresszusatz

## g0268（1 列）
- 見出し：Titel
- 例1 値：Rilke, Rainer Maria an Wunderly-Volkart… | Rilke, Rainer Maria an Reinhart, Georg;… | Rilke, Rainer Maria an Forrer, Anita (S… | Rilke, Rainer Maria an Clavel, Fanny; K… | Rilke, Rainer Maria an Schoenauer, H. (…
  - 同じ表の列：ID, Signatur, AutorIn, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Kollation

## g0269（1 列）
- 見出し：Ort
- 例1 値：Muzot | Gut Schönauburg bei Pratteln | Genf | Locarno | München
  - 同じ表の列：ID, Signatur, AutorIn, Titel, Datierung_von, Datierung_bis, Datierung_Bemerkung, Kollation

## g0282（1 列）
- 見出し：Maximum Windgeschwindigkeit
- 例1 値：4.095 | 1.6866666666666668 | 1.7983333333333331 | 1.0766666666666667 | 1.9016666666666666
  - 同じ表の列：Sensor ID, Gemessen am, Standort, Y Orientation Angle, X Orientation Angle, Windgeschwindigkeit, Windrichtung, Windgeschwindigkeit…

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

## g0315（3 列）
- 見出し：date
- 例1 値：2013-06-09 | 2013-06-09 | 2013-06-09 | 2013-06-09 | 2013-06-09
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status
- 例2 値：2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status

## g0321（1 列）
- 見出し：title_fr_CH
- 例1 値：Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0323（1 列）
- 見出し：title_rm_CH
- 例1 値：Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W… | Volksinitiative "Ja zur Aufhebung der W…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

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

## 答えの雛形

```
g0022	
g0023	
g0033	
g0069	
g0073	
g0075	
g0076	
g0083	
g0097	
g0098	
g0107	
g0112	
g0119	
g0147	
g0151	
g0164	
g0175	
g0187	
g0191	
g0203	
g0237	
g0243	
g0248	
g0261	
g0268	
g0269	
g0282	
g0300	
g0301	
g0315	
g0321	
g0323	
g0334	
g0335	
g0336	
```
