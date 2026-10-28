# ラベル用シート 005 / 005

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_005.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0481（1 列）
- 見出し：STARTDATUM
- 例1 値：27.3.1923 | 29.7.1926 | 8.9.1941 | 3.7.1950 | 31.1.1980
  - 同じ表の列：NUTZUNGSLIZENZ, ID, PERMALINK, PERSONENART, STARTDATUM_TYP, ENDDATUM_TYP, ENDDATUM, STARTORT_TYP

## g0482（1 列）
- 見出し：ENDDATUM_TYP
- 例1 値：Todesdatum | Todesdatum | Todesdatum | Todesdatum | Todesdatum
  - 同じ表の列：NUTZUNGSLIZENZ, ID, PERMALINK, PERSONENART, STARTDATUM_TYP, STARTDATUM, ENDDATUM, STARTORT_TYP

## g0483（1 列）
- 見出し：ENDDATUM
- 例1 値：25.6.2001 | 30.6.1943 | 20.4.1953 | 7.6.1966 | 27.9.1978
  - 同じ表の列：NUTZUNGSLIZENZ, ID, PERMALINK, PERSONENART, STARTDATUM_TYP, STARTDATUM, ENDDATUM_TYP, STARTORT_TYP

## g0484（1 列）
- 見出し：STARTORT_TYP
- 例1 値：Geburtsort | Geburtsort | Geburtsort | Geburtsort | Erst-Ort
  - 同じ表の列：NUTZUNGSLIZENZ, ID, PERMALINK, PERSONENART, STARTDATUM_TYP, STARTDATUM, ENDDATUM_TYP, ENDDATUM

## g0485（1 列）
- 見出し：STARTORT
- 例1 値：Riaz (FR) | Luzern (LU) | Ebnat-Kappel (SG) | München (DEU) | Freiburg im Breisgau (DEU)
  - 同じ表の列：NUTZUNGSLIZENZ, ID, PERMALINK, PERSONENART, STARTDATUM_TYP, STARTDATUM, ENDDATUM_TYP, ENDDATUM

## g0486（1 列）
- 見出し：URHEBER
- 例1 値：Aeppli, Eva | Aeppli, Eva | Aeppli, Eva | Aeppli, Eva | Aeppli, Eva
  - 同じ表の列：ARCHIVNR, TITEL, DATIERUNG, JAHR, TECHNIK, MASSE, STANDORT, STANDORTNR

## g0487（1 列）
- 見出し：ARCHIVNR
- 例1 値：97287.01/01 | 96067 | 95720 | 93814 | 95756
  - 同じ表の列：URHEBER, TITEL, DATIERUNG, JAHR, TECHNIK, MASSE, STANDORT, STANDORTNR

## g0488（1 列）
- 見出し：TITEL
- 例1 値：La Furie triste | Fatima | Hommage à Amnesty International | Textile Figur | Ohne Titel
  - 同じ表の列：URHEBER, ARCHIVNR, DATIERUNG, JAHR, TECHNIK, MASSE, STANDORT, STANDORTNR

## g0489（1 列）
- 見出し：DATIERUNG
- 例1 値：2001 (Gesamtauflage 1979-2002) | 1960 | 8. 1977 | 1959 | 1960
  - 同じ表の列：URHEBER, ARCHIVNR, TITEL, JAHR, TECHNIK, MASSE, STANDORT, STANDORTNR

## g0490（1 列）
- 見出し：TECHNIK
- 例1 値：Seide, Kapok, Watte, Samt, Metallstab | Kohle auf Papier | Öl auf Leinwand | Seide, Kapok, Watte, Samt, Metallstab | Bronze, schwarz patiniert, 6/8, Susse F…
  - 同じ表の列：URHEBER, ARCHIVNR, TITEL, DATIERUNG, JAHR, MASSE, STANDORT, STANDORTNR

## g0491（1 列）
- 見出し：MASSE
- 例1 値：180 cm hoch | 112,5 x 46,5 cm | Masse unbekannt | 44,5 cm hoch | 135 cm hoch (sitzend)
  - 同じ表の列：URHEBER, ARCHIVNR, TITEL, DATIERUNG, JAHR, TECHNIK, STANDORT, STANDORTNR

## g0492（1 列）
- 見出し：STANDORT
- 例1 値：Moderna Museet | Museum Jean Tinguely | Museum Jean Tinguely | Garden of the Zodiac Old Market Omaha | Moderna Museet
  - 同じ表の列：URHEBER, ARCHIVNR, TITEL, DATIERUNG, JAHR, TECHNIK, MASSE, STANDORTNR

## g0493（1 列）
- 見出し：STANDORTNR
- 例1 値：12384359 | 12384359 | 12384359 | 12406645 | 12384359
  - 同じ表の列：URHEBER, ARCHIVNR, TITEL, DATIERUNG, JAHR, TECHNIK, MASSE, STANDORT

## g0494（1 列）
- 見出し：BESITZERNR
- 例1 値：12396363 | 13059752 | 13310362 | 12900550 | 12900550
  - 同じ表の列：URHEBER, ARCHIVNR, TITEL, DATIERUNG, JAHR, TECHNIK, MASSE, STANDORT

## g0495（1 列）
- 見出し：organisationseinheit
- 例1 値：Bildungsdirektion | Bildungsdirektion | Finanzdirektion | Baudirektion | Direktion der Justiz und des Innern
  - 同じ表の列：jahr, gesuche_haengig_jan, gesuche_total, zugang_uneingeschra…, zugang_teilweise_ge…, zugang_vollstaendig…, anderweitige_erledi…, gesuche_haengig_dez

## g0496（1 列）
- 見出し：gesuche_haengig_jan
- 例1 値：10 | 5 | 1 | 5 | 2
  - 同じ表の列：jahr, organisationseinheit, gesuche_total, zugang_uneingeschra…, zugang_teilweise_ge…, zugang_vollstaendig…, anderweitige_erledi…, gesuche_haengig_dez

## g0497（1 列）
- 見出し：gesuche_total
- 例1 値：4 | 173 | 24 | 266 | 25
  - 同じ表の列：jahr, organisationseinheit, gesuche_haengig_jan, zugang_uneingeschra…, zugang_teilweise_ge…, zugang_vollstaendig…, anderweitige_erledi…, gesuche_haengig_dez

## g0498（1 列）
- 見出し：zugang_uneingeschraenkt_gewaehrt
- 例1 値：11 | 10 | 101 | 10 | 7
  - 同じ表の列：jahr, organisationseinheit, gesuche_haengig_jan, gesuche_total, zugang_teilweise_ge…, zugang_vollstaendig…, anderweitige_erledi…, gesuche_haengig_dez

## g0499（1 列）
- 見出し：zugang_teilweise_gewaehrt
- 例1 値：13 | 15 | 1 | 14 | 5
  - 同じ表の列：jahr, organisationseinheit, gesuche_haengig_jan, gesuche_total, zugang_uneingeschra…, zugang_vollstaendig…, anderweitige_erledi…, gesuche_haengig_dez

## g0500（1 列）
- 見出し：zugang_vollstaendig_abgelehnt
- 例1 値：2 | 4 | 2 | 56 | 1
  - 同じ表の列：jahr, organisationseinheit, gesuche_haengig_jan, gesuche_total, zugang_uneingeschra…, zugang_teilweise_ge…, anderweitige_erledi…, gesuche_haengig_dez

## g0501（1 列）
- 見出し：anderweitige_erledigung
- 例1 値：15 | 1 | 7 | 1 | 4
  - 同じ表の列：jahr, organisationseinheit, gesuche_haengig_jan, gesuche_total, zugang_uneingeschra…, zugang_teilweise_ge…, zugang_vollstaendig…, gesuche_haengig_dez

## g0502（1 列）
- 見出し：gesuche_haengig_dez
- 例1 値：3 | 4 | 1 | 4 | 2
  - 同じ表の列：jahr, organisationseinheit, gesuche_haengig_jan, gesuche_total, zugang_uneingeschra…, zugang_teilweise_ge…, zugang_vollstaendig…, anderweitige_erledi…

## g0503（1 列）
- 見出し：gre_id
- 例1 値：c0658eb00fe84980bef6e7068c165ac6 | 083c8a9f8740460080ffd8b31ef78873 | 875e056fdbc24dd2acd0985406c45cc3 | add2970931b2454dbbb8f149ec43fb42 | 54dc23fd3bcc46ba860debc8b4676a7f
  - 同じ表の列：gre_kategorie, gre_anzahl, gre_inaktiv, gre_aktualitaet

## g0504（1 列）
- 見出し：gre_kategorie
- 例1 値：Fraktion | Kommission | Ausschuss | weiteres Gremium | Fraktion
  - 同じ表の列：gre_id, gre_anzahl, gre_inaktiv, gre_aktualitaet

## g0505（1 列）
- 見出し：gre_anzahl
- 例1 値：17 | 13 | 13 | 13 | 13
  - 同じ表の列：gre_id, gre_kategorie, gre_inaktiv, gre_aktualitaet

## g0506（1 列）
- 見出し：gre_inaktiv
- 例1 値：Nein | Nein | Ja | Ja | Nein
  - 同じ表の列：gre_id, gre_kategorie, gre_anzahl, gre_aktualitaet

## g0507（1 列）
- 見出し：gre_aktualitaet
- 例1 値：2026-09-23 | 2026-09-23 | 2026-09-23 | 2026-09-23 | 2026-09-23
  - 同じ表の列：gre_id, gre_kategorie, gre_anzahl, gre_inaktiv

## g0508（1 列）
- 見出し：measured_at
- 例1 値：2026-03-29T03:00:00.065000+00:00 | 2026-03-22T23:00:00.060000+00:00 | 2026-04-12T08:00:00.047000+00:00 | 2026-04-16T03:00:00.067000+00:00 | 2026-03-24T07:00:00.062000+00:00
  - 同じ表の列：device_id, location, data_temperature, geo_point_2d

## g0509（1 列）
- 見出し：device_id
- 例1 値：98edb4d1-224d-47de-b72c-437b206bfe8b | d9214375-a19a-431c-a44c-36583196a994 | 8e57626e-3eb9-49fb-af45-374874889f14 | 1ce55ad9-694e-41e0-8586-3d470e7f28c0 | 8e57626e-3eb9-49fb-af45-374874889f14
  - 同じ表の列：measured_at, location, data_temperature, geo_point_2d

## g0510（1 列）
- 見出し：location
- 例1 値：{"coordinates": [9.38449, 47.42613], "t… | {"coordinates": [9.37406, 47.42486], "t… | {"coordinates": [9.37879, 47.44099], "t… | {"coordinates": [9.37074, 47.42328], "t… | {"coordinates": [9.339444444444444, 47.…
  - 同じ表の列：measured_at, device_id, data_temperature, geo_point_2d

## g0511（1 列）
- 見出し：data_temperature
- 例1 値：8.545506795247396 | 6.820055643717448 | 13.614158630371094 | 4.91 | 8.183682759602865
  - 同じ表の列：measured_at, device_id, location, geo_point_2d

## g0512（1 列）
- 見出し：Geschaeft_GUID
- 例1 値：16178eb0e07f4d52ba70cfdec26b55fb | 86e9681378044ad68d9a049cdc69476d | 89ababccf7b74edd9e57de004b583bd0 | 844bfdde364346df99871d3660194483 | c78c5f18d0e447b68c1d1daf731f7413
  - 同じ表の列：Einreichedatum, Geschaeftstyp, Aktenplan

## g0513（1 列）
- 見出し：Einreichedatum
- 例1 値：2025-04-23 | 2023-12-15 | 2022-04-07 | 2025-05-16 | 2022-11-21
  - 同じ表の列：Geschaeft_GUID, Geschaeftstyp, Aktenplan

## g0514（1 列）
- 見出し：Geschaeftstyp
- 例1 値：Bevölkerungsvorstoss | Bevölkerungsvorstoss | Bevölkerungsvorstoss | Bevölkerungsvorstoss | Bevölkerungsvorstoss
  - 同じ表の列：Geschaeft_GUID, Einreichedatum, Aktenplan

## g0515（1 列）
- 見出し：Aktenplan
- 例1 値：132.55 Abstimmungen, Wahlen, Petitionen… | 132.55 Abstimmungen, Wahlen, Petitionen… | 132.55 Abstimmungen, Wahlen, Petitionen… | 132.55 Abstimmungen, Wahlen, Petitionen… | 132.55 Abstimmungen, Wahlen, Petitionen…
  - 同じ表の列：Geschaeft_GUID, Einreichedatum, Geschaeftstyp

## g0516（1 列）
- 見出し：Bezeichnung
- 例1 値：Stadtparlament | Stadtparlament | Stadtparlament | Stadtparlament | Stadtparlament
  - 同じ表の列：Mitglied_Status, Funktion, Partei, Sitzplatz, Eintrittsdatum, Austrittsdatum, Beruf, Bild

## g0517（1 列）
- 見出し：Mitglied_Status
- 例1 値：Ehemalig | Ehemalig | Ehemalig | Ehemalig | Ehemalig
  - 同じ表の列：Bezeichnung, Funktion, Partei, Sitzplatz, Eintrittsdatum, Austrittsdatum, Beruf, Bild

## g0518（1 列）
- 見出し：Funktion
- 例1 値：Mitglied | Mitglied | Mitglied | Mitglied | Mitglied
  - 同じ表の列：Bezeichnung, Mitglied_Status, Partei, Sitzplatz, Eintrittsdatum, Austrittsdatum, Beruf, Bild

## g0519（1 列）
- 見出し：Partei
- 例1 値：SP | EVP | CVP | Grüne | SP
  - 同じ表の列：Bezeichnung, Mitglied_Status, Funktion, Sitzplatz, Eintrittsdatum, Austrittsdatum, Beruf, Bild

## g0520（1 列）
- 見出し：Sitzplatz
- 例1 値：50 | 30 | 53 | 41 | 4
  - 同じ表の列：Bezeichnung, Mitglied_Status, Funktion, Partei, Eintrittsdatum, Austrittsdatum, Beruf, Bild

## g0521（1 列）
- 見出し：Eintrittsdatum
- 例1 値：2014-10-14 | 2009-01-01 | 2023-01-01 | 2021-01-01 | 2001-01-01
  - 同じ表の列：Bezeichnung, Mitglied_Status, Funktion, Partei, Sitzplatz, Austrittsdatum, Beruf, Bild

## g0522（1 列）
- 見出し：Austrittsdatum
- 例1 値：2012-03-01 | 2003-12-11 | 2021-01-01 | 2018-03-01 | 2019-02-01
  - 同じ表の列：Bezeichnung, Mitglied_Status, Funktion, Partei, Sitzplatz, Eintrittsdatum, Beruf, Bild

## g0523（1 列）
- 見出し：Beruf
- 例1 値：Rechtsanwältin / Mediatorin SAV | Pflegefachfrau HF, klassische Homöopath… | dipl. Wirtschaftsprüfer | Raum- und Verkehrsplaner | Geschäftsleiterin VCS SG/AP
  - 同じ表の列：Bezeichnung, Mitglied_Status, Funktion, Partei, Sitzplatz, Eintrittsdatum, Austrittsdatum, Bild

## g0524（1 列）
- 見出し：Bild
- 例1 値：https://daten.stadt.sg.ch/api/v2/catalo… | https://daten.stadt.sg.ch/api/v2/catalo… | https://daten.stadt.sg.ch/api/v2/catalo… | https://daten.stadt.sg.ch/api/v2/catalo… | https://daten.stadt.sg.ch/api/v2/catalo…
  - 同じ表の列：Bezeichnung, Mitglied_Status, Funktion, Partei, Sitzplatz, Eintrittsdatum, Austrittsdatum, Beruf

## g0525（2 列）
- 見出し：zeitpunkt
- 例1 値：2026-01-09T14:00:00+01:00 | 2026-01-09T16:45:00+01:00 | 2026-01-08T01:30:00+01:00 | 2026-01-06T21:45:00+01:00 | 2026-01-07T15:00:00+01:00
  - 同じ表の列：lastgang_kwh
- 例2 値：2023-01-01T20:30:00+01:00 | 2023-01-01T22:45:00+01:00 | 2023-01-01T03:45:00+01:00 | 2023-01-02T09:45:00+01:00 | 2023-01-02T11:15:00+01:00
  - 同じ表の列：energietraeger, lastgang_kwh

## g0526（2 列）
- 見出し：lastgang_kwh
- 例1 値：0.09 | 0.0 | 0.0 | 0.0 | 1.587
  - 同じ表の列：zeitpunkt
- 例2 値：0.0 | 155.878 | 0.0 | 154.878 | 684.443
  - 同じ表の列：zeitpunkt, energietraeger

## g0527（1 列）
- 見出し：energietraeger
- 例1 値：wasser | photovoltaik | thermisch | photovoltaik | photovoltaik
  - 同じ表の列：zeitpunkt, lastgang_kwh

## g0528（1 列）
- 見出し：gemeinde_bfs_nr
- 例1 値：230 | 230 | 230 | 230 | 230
  - 同じ表の列：gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, richtung, spur_nr, lat

## g0529（1 列）
- 見出し：anlage_nr
- 例1 値：2be45cdaaa2d54d45d7acea1ec6efe0b | bda81f33d038f8d70122e7f481b53020 | 1f938943f17180f6edc271cbcb378039 | 0790984be7042b7cba782aa0a73f7ae4 | bda81f33d038f8d70122e7f481b53020
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_typ, zeit_von, zeit_bis, richtung, spur_nr, lat

## g0530（1 列）
- 見出し：anlage_typ
- 例1 値：Velo | Velo | Velo | Velo | Velo
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, zeit_von, zeit_bis, richtung, spur_nr, lat

## g0531（2 列）
- 見出し：zeit_von
- 例1 値：2026-10-23T21:00:00+01 | 2026-10-25T00:00:00+01 | 2026-10-25T00:00:00+01 | 2026-10-26T19:00:00+01 | 2026-10-27T21:00:00+01
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_bis, richtung, spur_nr, lat
- 例2 値：2025-01-11T18:00:00+01 | 2025-01-23T18:00:00+01 | 2025-01-19T12:00:00+01 | 2025-01-31T16:00:00+01 | 2025-01-12T21:00:00+01
  - 同じ表の列：datum, zeit_bis, gemeinde_code, raumplanungsregion_…, anzahl_velos, spur_richtung, messstelle_id, messstelle_laengeng…

## g0532（2 列）
- 見出し：zeit_bis
- 例1 値：2026-10-23T18:59:59+01 | 2026-10-24T20:59:59+01 | 2026-10-26T13:59:59+01 | 2026-10-23T20:59:59+01 | 2026-10-25T01:59:59+01
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, richtung, spur_nr, lat
- 例2 値：2025-01-31T08:59:59+01 | 2025-01-06T06:59:59+01 | 2025-01-07T09:59:59+01 | 2025-02-01T13:59:59+01 | 2025-01-05T00:59:59+01
  - 同じ表の列：datum, zeit_von, gemeinde_code, raumplanungsregion_…, anzahl_velos, spur_richtung, messstelle_id, messstelle_laengeng…

## g0533（1 列）
- 見出し：richtung
- 例1 値：S | N | N | S | N
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, spur_nr, lat

## g0534（1 列）
- 見出し：spur_nr
- 例1 値：1.0 | 1.0 | 1.0 | 2.0 | 1.0
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, richtung, lat

## g0535（1 列）
- 見出し：lat
- 例1 値：47.47721998360666 | 47.49039567504859 | 47.49333465808204 | 47.49039567504859 | 47.49711006385951
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, richtung, spur_nr

## g0536（1 列）
- 見出し：lon
- 例1 値：8.717188185700442 | 8.72656101567254 | 8.725398797174437 | 8.717188185700442 | 8.70307288823233
  - 同じ表の列：gemeinde_bfs_nr, gemeinde, anlage_nr, anlage_typ, zeit_von, zeit_bis, richtung, spur_nr

## g0537（1 列）
- 見出し：id
- 例1 値：teilrevision-des-finanzhaushaltsgesetze… | teilrevision-des-finanzhaushaltsgesetze… | teilrevision-des-finanzhaushaltsgesetze… | teilrevision-des-finanzhaushaltsgesetze… | teilrevision-des-finanzhaushaltsgesetze…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0538（1 列）
- 見出し：title_de_CH
- 例1 値：Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0539（1 列）
- 見出し：title_fr_CH
- 例1 値：Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0540（1 列）
- 見出し：title_it_CH
- 例1 値：Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0541（1 列）
- 見出し：title_rm_CH
- 例1 値：Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze… | Teilrevision des Finanzhaushaltsgesetze…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0542（3 列）
- 見出し：date
- 例1 値：2013-03-03 | 2013-03-03 | 2013-03-03 | 2013-03-03 | 2013-03-03
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status
- 例2 値：2013-03-03 | 2013-03-03 | 2013-03-03 | 2013-03-03 | 2013-03-03
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status

## g0543（3 列）
- 見出し：shortcode
- 例1 値：K1 | K1 | K1 | K1 | K1
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status
- 例2 値：E2 | E2 | E2 | E2 | E2
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status

## g0544（3 列）
- 見出し：domain
- 例1 値：canton | canton | canton | canton | canton
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status
- 例2 値：federation | federation | federation | federation | federation
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status

## g0545（3 列）
- 見出し：answer
- 例1 値：rejected | rejected | rejected | rejected | rejected
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain
- 例2 値：accepted | accepted | accepted | accepted | accepted
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain

## g0546（2 列）
- 見出し：id
- 例1 値：volksinitiative-vom-26.-februar-2008-ge… | volksinitiative-vom-26.-februar-2008-ge… | volksinitiative-vom-26.-februar-2008-ge… | volksinitiative-vom-26.-februar-2008-ge… | volksinitiative-vom-26.-februar-2008-ge…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status
- 例2 値：bundesbeschluss-vom-15.-juni-2012-uber-… | bundesbeschluss-vom-15.-juni-2012-uber-… | bundesbeschluss-vom-15.-juni-2012-uber-… | bundesbeschluss-vom-15.-juni-2012-uber-… | bundesbeschluss-vom-15.-juni-2012-uber-…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0547（1 列）
- 見出し：title_de_CH
- 例1 値：Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0548（1 列）
- 見出し：title_fr_CH
- 例1 値：Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0549（1 列）
- 見出し：title_it_CH
- 例1 値：Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0550（1 列）
- 見出し：title_rm_CH
- 例1 値：Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g… | Volksinitiative vom 26. Februar 2008 "g…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0551（1 列）
- 見出し：title_de_CH
- 例1 値：Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über …
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0552（1 列）
- 見出し：title_fr_CH
- 例1 値：Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über …
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0553（1 列）
- 見出し：title_it_CH
- 例1 値：Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über …
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0554（1 列）
- 見出し：title_rm_CH
- 例1 値：Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über … | Bundesbeschluss vom 15. Juni 2012 über …
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0555（1 列）
- 見出し：fallstruktur
- 例1 値：Kinder und junge Erwachsene | Andere | Elternteil mit 2 Kindern | Andere | Andere
  - 同じ表の列：jahr, metrik, wert, einheit

## g0556（2 列）
- 見出し：metrik
- 例1 値：Verteilung | Verteilung | Anzahl | Verteilung | Anzahl
  - 同じ表の列：jahr, fallstruktur, wert, einheit
- 例2 値：Anzahl | Anzahl | Verteilung | Anzahl | Verteilung
  - 同じ表の列：jahr, bildungsabschluss, wert, einheit

## g0557（1 列）
- 見出し：einheit
- 例1 値：Prozent | Fälle | Prozent | Prozent | Prozent
  - 同じ表の列：jahr, fallstruktur, metrik, wert

## g0558（1 列）
- 見出し：metrik
- 例1 値：Anzahl (beziehende Kinder und nicht ver… | Bezugsquote (beziehende Kinder und nich… | Bezugsquote (beziehende Kinder und nich… | Bezugsquote (beziehende Kinder und nich… | Bezugsquote (beziehende Kinder und nich…
  - 同じ表の列：jahr, wert, einheit

## g0559（1 列）
- 見出し：bildungsabschluss
- 例1 値：keine Angabe | keine Angabe | keine Angabe | keine Angabe | Sekundarstufe II
  - 同じ表の列：jahr, metrik, wert, einheit

## g0560（1 列）
- 見出し：gemeinde_code
- 例1 値：295 | 295 | 295 | 295 | 295
  - 同じ表の列：datum, zeit_von, zeit_bis, raumplanungsregion_…, anzahl_velos, spur_richtung, messstelle_id, messstelle_laengeng…

## g0561（1 列）
- 見出し：raumplanungsregion_code
- 例1 値：106 | 106 | 106 | 106 | 106
  - 同じ表の列：datum, zeit_von, zeit_bis, gemeinde_code, anzahl_velos, spur_richtung, messstelle_id, messstelle_laengeng…

## g0562（1 列）
- 見出し：anzahl_velos
- 例1 値：0 | 0 | 8 | 0 | 2
  - 同じ表の列：datum, zeit_von, zeit_bis, gemeinde_code, raumplanungsregion_…, spur_richtung, messstelle_id, messstelle_laengeng…

## g0563（1 列）
- 見出し：spur_richtung
- 例1 値：Horgen | Horgen | Horgen | Horgen | Horgen
  - 同じ表の列：datum, zeit_von, zeit_bis, gemeinde_code, raumplanungsregion_…, anzahl_velos, messstelle_id, messstelle_laengeng…

## g0564（1 列）
- 見出し：messstelle_id
- 例1 値：523 | 523 | 523 | 523 | 523
  - 同じ表の列：datum, zeit_von, zeit_bis, gemeinde_code, raumplanungsregion_…, anzahl_velos, spur_richtung, messstelle_laengeng…

## g0565（1 列）
- 見出し：messstelle_laengengrad_WGS84
- 例1 値：8.618849128063152 | 8.618849128063152 | 8.618849128063152 | 8.618849128063152 | 8.618849128063152
  - 同じ表の列：datum, zeit_von, zeit_bis, gemeinde_code, raumplanungsregion_…, anzahl_velos, spur_richtung, messstelle_id

## g0566（1 列）
- 見出し：messstelle_breitengrad_WGS84
- 例1 値：47.25365358150552 | 47.25365358150552 | 47.25365358150552 | 47.25365358150552 | 47.25365358150552
  - 同じ表の列：datum, zeit_von, zeit_bis, gemeinde_code, raumplanungsregion_…, anzahl_velos, spur_richtung, messstelle_id

## g0567（1 列）
- 見出し：PK     Û¬2]OäÕòÝ= Ý=    SIPV_MN_CARTO_GG_25.csvï»¿VEGE
- 例1 値：Cultures | Cultures | Cultures | Cultures | Cultures
  - 同じ表の列：CODE_25, OBJECTID, SHAPE_AREA

## g0568（1 列）
- 見出し：CODE_25
- 例1 値：10 | 10 | 10 | 10 | 10
  - 同じ表の列：PK     Û¬2]OäÕò…, OBJECTID, SHAPE_AREA

## g0569（1 列）
- 見出し：OBJECTID
- 例1 値：151 | 533 | 395 | 178 | 310
  - 同じ表の列：PK     Û¬2]OäÕò…, CODE_25, SHAPE_AREA

## g0570（1 列）
- 見出し：SHAPE_AREA
- 例1 値：4826.379075895 | 4949.62814097 | 24013.77751192 | 76303.668649105 | 17587.777225045
  - 同じ表の列：PK     Û¬2]OäÕò…, CODE_25, OBJECTID

## g0571（1 列）
- 見出し：library_call_number
- 例1 値：Zürich, ZB, Handschriftenabteilung, LKR… | Zürich, ZB, Handschriftenabteilung, LKR… | Zürich, ZB, Handschriftenabteilung, LKR… | Zürich, ZB, Handschriftenabteilung, LKR… | Zürich, ZB, Handschriftenabteilung, LKR…
  - 同じ表の列：digital_reproduction, title, place_of_publicatio…, date_of_publication…, date_of_publication…, series, digital_reproductio…, digital_object_iden…

## g0572（1 列）
- 見出し：digital_reproduction
- 例1 値：https://doi.org/10.7891/e-manuscripta-1… | https://doi.org/10.7891/e-manuscripta-1… | https://doi.org/10.7891/e-manuscripta-1… | https://doi.org/10.7891/e-manuscripta-1… | https://doi.org/10.7891/e-manuscripta-1…
  - 同じ表の列：library_call_number, title, place_of_publicatio…, date_of_publication…, date_of_publication…, series, digital_reproductio…, digital_object_iden…

## g0573（1 列）
- 見出し：title
- 例1 値：Nachtzedel Januar - Dezember 1788 | Nachtzedel Januar - Dezember 1782 | Nachtzedel Januar - Dezember 1784 | Nachtzedel Januar - Dezember 1785 | Nachtzedel Januar - Dezember 1781
  - 同じ表の列：library_call_number, digital_reproduction, place_of_publicatio…, date_of_publication…, date_of_publication…, series, digital_reproductio…, digital_object_iden…

## g0574（1 列）
- 見出し：place_of_publication_or_production
- 例1 値：Zürich | Zürich | Zürich | Zürich | Zürich
  - 同じ表の列：library_call_number, digital_reproduction, title, date_of_publication…, date_of_publication…, series, digital_reproductio…, digital_object_iden…

## g0575（1 列）
- 見出し：date_of_publication_or_production
- 例1 値：01.01.1782 - 30.12.1782 | 02.01.1785 - 30.12.1785 | 01.01.1784 - 30.12.1784 | 01.01.1791 - 31.12.1791 | 01.01.1783 - 30.12.1783
  - 同じ表の列：library_call_number, digital_reproduction, title, place_of_publicatio…, date_of_publication…, series, digital_reproductio…, digital_object_iden…

## g0576（1 列）
- 見出し：date_of_publication_or_production_standardised
- 例1 値：1787 | 1791 | 1780 | 1785 | 1790
  - 同じ表の列：library_call_number, digital_reproduction, title, place_of_publicatio…, date_of_publication…, series, digital_reproductio…, digital_object_iden…

## g0577（1 列）
- 見出し：series
- 例1 値：Meldelisten für in Zürich übernachtende… | Meldelisten für in Zürich übernachtende… | Meldelisten für in Zürich übernachtende… | Meldelisten für in Zürich übernachtende… | Meldelisten für in Zürich übernachtende…
  - 同じ表の列：library_call_number, digital_reproduction, title, place_of_publicatio…, date_of_publication…, date_of_publication…, digital_reproductio…, digital_object_iden…

## g0578（1 列）
- 見出し：digital_reproduction_copyright
- 例1 値：pdm | pdm | pdm | pdm | pdm
  - 同じ表の列：library_call_number, digital_reproduction, title, place_of_publicatio…, date_of_publication…, date_of_publication…, series, digital_object_iden…

## g0579（1 列）
- 見出し：digital_object_identifier
- 例1 値：10.7891/e-manuscripta-171527 | 10.7891/e-manuscripta-173797 | 10.7891/e-manuscripta-172952 | 10.7891/e-manuscripta-173270 | 10.7891/e-manuscripta-172499
  - 同じ表の列：library_call_number, digital_reproduction, title, place_of_publicatio…, date_of_publication…, date_of_publication…, series, digital_reproductio…

## g0580（1 列）
- 見出し：digital_platform
- 例1 値：e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch
  - 同じ表の列：library_call_number, digital_reproduction, title, place_of_publicatio…, date_of_publication…, date_of_publication…, series, digital_reproductio…

## g0581（1 列）
- 見出し：catalog_id_swisscovery
- 例1 値：990036361810205508 | 990036361810205508 | 990036361810205508 | 990036362010205508 | 990036362010205508
  - 同じ表の列：page_id_erara, erara_page_view, swisscovery_link, pubdate, pubdate_from, pubdate_to, creator, publisher

## g0582（1 列）
- 見出し：page_id_erara
- 例1 値：27043782 | 26304523 | 26045808 | 26357119 | 25570700
  - 同じ表の列：catalog_id_swisscov…, erara_page_view, swisscovery_link, pubdate, pubdate_from, pubdate_to, creator, publisher

## g0583（1 列）
- 見出し：erara_page_view
- 例1 値：https://www.e-rara.ch/doi/10.3931/e-rar… | https://www.e-rara.ch/doi/10.3931/e-rar… | https://www.e-rara.ch/doi/10.3931/e-rar… | https://www.e-rara.ch/doi/10.3931/e-rar… | https://www.e-rara.ch/doi/10.3931/e-rar…
  - 同じ表の列：catalog_id_swisscov…, page_id_erara, swisscovery_link, pubdate, pubdate_from, pubdate_to, creator, publisher

## g0584（1 列）
- 見出し：swisscovery_link
- 例1 値：https://uzb.swisscovery.slsp.ch/discove… | https://uzb.swisscovery.slsp.ch/discove… | https://uzb.swisscovery.slsp.ch/discove… | https://uzb.swisscovery.slsp.ch/discove… | https://uzb.swisscovery.slsp.ch/discove…
  - 同じ表の列：catalog_id_swisscov…, page_id_erara, erara_page_view, pubdate, pubdate_from, pubdate_to, creator, publisher

## g0585（1 列）
- 見出し：pubdate
- 例1 値：1680 | 1680 | 1656 | 1680 | 1656
  - 同じ表の列：catalog_id_swisscov…, page_id_erara, erara_page_view, swisscovery_link, pubdate_from, pubdate_to, creator, publisher

## g0586（1 列）
- 見出し：pubdate_from
- 例1 値：1644 | 1647 | 1647 | 1645 | 1647
  - 同じ表の列：catalog_id_swisscov…, page_id_erara, erara_page_view, swisscovery_link, pubdate, pubdate_to, creator, publisher

## g0587（1 列）
- 見出し：pubdate_to
- 例1 値：1647 | 1664 | 1664 | 1664 | 1664
  - 同じ表の列：catalog_id_swisscov…, page_id_erara, erara_page_view, swisscovery_link, pubdate, pubdate_from, creator, publisher

## g0588（1 列）
- 見出し：creator
- 例1 値：Janssonius Offizin | Martini, Martino | Janssonius Offizin | Janssonius Offizin | Janssonius Offizin
  - 同じ表の列：catalog_id_swisscov…, page_id_erara, erara_page_view, swisscovery_link, pubdate, pubdate_from, pubdate_to, publisher

## g0589（1 列）
- 見出し：publisher
- 例1 値：Blaeu, Willem Janszoon | Blaeu, Willem Janszoon | Blaeu, Willem Janszoon | Blaeu, Willem Janszoon | Blaeu, Willem Janszoon
  - 同じ表の列：catalog_id_swisscov…, page_id_erara, erara_page_view, swisscovery_link, pubdate, pubdate_from, pubdate_to, creator

## g0590（1 列）
- 見出し：reference
- 例1 値：Novus atlas absolutissimus : das ist, G… | Le théâtre du monde, ou, Nouvel atlas c… | Novus atlas absolutissimus : das ist, G… | Novus atlas absolutissimus : das ist, G… | Novus atlas absolutissimus : das ist, G…
  - 同じ表の列：catalog_id_swisscov…, page_id_erara, erara_page_view, swisscovery_link, pubdate, pubdate_from, pubdate_to, creator

## 答えの雛形

```
g0481	
g0482	
g0483	
g0484	
g0485	
g0486	
g0487	
g0488	
g0489	
g0490	
g0491	
g0492	
g0493	
g0494	
g0495	
g0496	
g0497	
g0498	
g0499	
g0500	
g0501	
g0502	
g0503	
g0504	
g0505	
g0506	
g0507	
g0508	
g0509	
g0510	
g0511	
g0512	
g0513	
g0514	
g0515	
g0516	
g0517	
g0518	
g0519	
g0520	
g0521	
g0522	
g0523	
g0524	
g0525	
g0526	
g0527	
g0528	
g0529	
g0530	
g0531	
g0532	
g0533	
g0534	
g0535	
g0536	
g0537	
g0538	
g0539	
g0540	
g0541	
g0542	
g0543	
g0544	
g0545	
g0546	
g0547	
g0548	
g0549	
g0550	
g0551	
g0552	
g0553	
g0554	
g0555	
g0556	
g0557	
g0558	
g0559	
g0560	
g0561	
g0562	
g0563	
g0564	
g0565	
g0566	
g0567	
g0568	
g0569	
g0570	
g0571	
g0572	
g0573	
g0574	
g0575	
g0576	
g0577	
g0578	
g0579	
g0580	
g0581	
g0582	
g0583	
g0584	
g0585	
g0586	
g0587	
g0588	
g0589	
g0590	
```
