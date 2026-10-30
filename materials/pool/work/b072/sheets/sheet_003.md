# ラベル用シート 003 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：bilanz_view_nr
- 例1 値：3 | 2 | 3 | 1 | 3
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view, grouping

## g0242（1 列）
- 見出し：bilanz_view
- 例1 値：Neubau | Neubau | Wohnbausaldo | Neubau | Wohnbausaldo
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view_nr, grouping

## g0243（1 列）
- 見出し：grouping
- 例1 値：erstellungsart | flaeche | flaeche | flaeche | flaeche
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view_nr, bilanz_view

## g0244（1 列）
- 見出し：group_nr
- 例1 値：99 | 4 | 3 | 1 | 1
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view_nr, bilanz_view

## g0245（1 列）
- 見出し：monat
- 例1 値：12 | 12 | 12 | 12 | 12
  - 同じ表の列：jahr, stichtag, wissensstand_am, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis

## g0246（1 列）
- 見出し：wissensstand_am
- 例1 値：2024-03-31 | 2025-03-31 | 2024-03-31 | 2026-03-31 | 2018-03-31
  - 同じ表の列：jahr, monat, stichtag, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr, stadtkreis

## g0247（1 列）
- 見出し：stadtkreis
- 例1 値：Mattenbach | Veltheim | Mattenbach | Oberwinterthur | Stadt
  - 同じ表の列：jahr, monat, stichtag, wissensstand_am, geom_code, gemeinde_bfs_nr, gemeinde, stadtkreis_bfs_nr

## g0248（1 列）
- 見出し：id
- 例1 値：anderung-des-bundesgesetzes-uber-die-ar… | anderung-des-bundesgesetzes-uber-die-ar… | anderung-des-bundesgesetzes-uber-die-ar… | anderung-des-bundesgesetzes-uber-die-ar… | anderung-des-bundesgesetzes-uber-die-ar…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0249（1 列）
- 見出し：title_de_CH
- 例1 値：Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0250（1 列）
- 見出し：title_fr_CH
- 例1 値：Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0251（1 列）
- 見出し：title_it_CH
- 例1 値：Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0252（1 列）
- 見出し：title_rm_CH
- 例1 値：Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar… | Änderung des Bundesgesetzes über die Ar…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0253（4 列）
- 見出し：date
- 例1 値：2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status
- 例2 値：2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22 | 2013-09-22
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status

## g0254（3 列）
- 見出し：shortcode
- 例1 値：E3 | E3 | E3 | E3 | E3
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status
- 例2 値：K1 | K1 | K1 | K1 | K1
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status

## g0255（3 列）
- 見出し：domain
- 例1 値：federation | federation | federation | federation | federation
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status
- 例2 値：canton | canton | canton | canton | canton
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status

## g0256（3 列）
- 見出し：answer
- 例1 値：accepted | accepted | accepted | accepted | accepted
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain
- 例2 値：proposal | proposal | proposal | proposal | proposal
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain

## g0257（2 列）
- 見出し：id
- 例1 値：ja-zu-sauberem-strom-ohne-kohlekraft | ja-zu-sauberem-strom-ohne-kohlekraft | ja-zu-sauberem-strom-ohne-kohlekraft | ja-zu-sauberem-strom-ohne-kohlekraft | ja-zu-sauberem-strom-ohne-kohlekraft
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status
- 例2 値：volksinitiative-familieninitiative-steu… | volksinitiative-familieninitiative-steu… | volksinitiative-familieninitiative-steu… | volksinitiative-familieninitiative-steu… | volksinitiative-familieninitiative-steu…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0258（1 列）
- 見出し：title_de_CH
- 例1 値：Gegenvorschlag des Grossen Rates "Keine… | Volksinitiative oder Gegenvorschlag | Volksinitiative oder Gegenvorschlag | Volksinitiative oder Gegenvorschlag | Gegenvorschlag des Grossen Rates "Keine…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0259（1 列）
- 見出し：title_fr_CH
- 例1 値：Gegenvorschlag des Grossen Rates "Keine… | Gegenvorschlag des Grossen Rates "Keine… | Gegenvorschlag des Grossen Rates "Keine… | Ja zu sauberem Strom ohne Kohlekraft | Gegenvorschlag des Grossen Rates "Keine…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0260（1 列）
- 見出し：title_it_CH
- 例1 値：Controprogetto del Gran Consiglio "Ness… | Controprogetto del Gran Consiglio "Ness… | Ja zu sauberem Strom ohne Kohlekraft | Controprogetto del Gran Consiglio "Ness… | Controprogetto del Gran Consiglio "Ness…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0261（1 列）
- 見出し：title_rm_CH
- 例1 値：Ja zu sauberem Strom ohne Kohlekraft | Cuntraproposta dal cussegl grond "Nagin… | Cuntraproposta dal cussegl grond "Nagin… | Ja zu sauberem Strom ohne Kohlekraft | Ja zu sauberem Strom ohne Kohlekraft
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0262（1 列）
- 見出し：title_de_CH
- 例1 値：Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0263（1 列）
- 見出し：title_fr_CH
- 例1 値：Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0264（1 列）
- 見出し：title_it_CH
- 例1 値：Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0265（1 列）
- 見出し：title_rm_CH
- 例1 値：Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St… | Volksinitiative "Familieninitiative: St…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0266（1 列）
- 見出し：ABSTIMMTAG
- 例1 値：1991-12-08T00:00:00Z | 1981-06-14T00:00:00Z | 1991-12-08T00:00:00Z | 1985-09-22T00:00:00Z | 1995-06-25T00:00:00Z
  - 同じ表の列：STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0267（1 列）
- 見出し：STAT_VORLAGE_ID
- 例1 値：10 | 1968 | 1732 | 1763 | 138
  - 同じ表の列：ABSTIMMTAG, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0268（1 列）
- 見出し：BFS_VORLAGE_ID
- 例1 値：339 | 305 | 345 | 337 | 439
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0269（1 列）
- 見出し：VORLAGE_KURZBEZ
- 例1 値：Bundesbeschluss über die Revision der B… | Gesetz über die hauswirtschaftliche For… | Gegenentwurf zur Volksinitiative Eidgen… | Gesetz über die Zürcher Kantonalbank (R… | Bundesbeschluss über die Neuregelung be…
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0270（1 列）
- 見出し：VORLAGE_LANGBEZ
- 例1 値：Volksinitiative «für eine finanziell tr… | Einführungsgesetz zum Bundesgesetz über… | Kantonsverfassung (Änderung) | Volksinitiative «für eine gerechte Best… | Verfassungsgesetz über die Änderung der…
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0271（1 列）
- 見出し：VORLAGENART_ID
- 例1 値：3 | 2 | 1 | 3 | 1
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_BEZ, THEMA_ID, THEMA

## g0272（1 列）
- 見出し：VORLAGENART_BEZ
- 例1 値：Volksinitiative | Volksinitiative | Obligatorisches Referendum | Obligatorisches Referendum | Obligatorisches Referendum
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, THEMA_ID, THEMA

## g0273（1 列）
- 見出し：THEMA_ID
- 例1 値：3 | 4 | 11 | 10 | 1
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA

## g0274（1 列）
- 見出し：THEMA
- 例1 値：Öffentliche Finanzen,Verkehr und Infras… | Wirtschaft,Soziale Fragen – Sozialpolit… | Staatsordnung | Umwelt und Lebensraum,Soziale Fragen – … | Kultur – Religion – Medien
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID

## g0275（1 列）
- 見出し：ABSTIMMUNGSART_ID
- 例1 値：1 | 2 | 2 | 1 | 1
  - 同じ表の列：ABSTIMMTAG, STAT_VORLAGE_ID, BFS_VORLAGE_ID, VORLAGE_KURZBEZ, VORLAGE_LANGBEZ, VORLAGENART_ID, VORLAGENART_BEZ, THEMA_ID

## g0276（1 列）
- 見出し：erfassung
- 例1 値：2025-12-01 17:37:54.869745 | 2026-09-17 16:19:32.338846 | 2025-11-28 09:58:15.564892 | 2025-09-10 11:41:29.839399 | 2025-07-24 07:59:59.947075
  - 同じ表の列：nutzertyp, anfragetyp, thema, kanal, zeitaufwand, mitarbeiter

## g0277（1 列）
- 見出し：nutzertyp
- 例1 値：Verwaltung (kommunal, kantonal, nationa… | Firma | Privatperson | Organisation (Verband u. Kirchen, inter… | Firma
  - 同じ表の列：erfassung, anfragetyp, thema, kanal, zeitaufwand, mitarbeiter

## g0278（1 列）
- 見出し：anfragetyp
- 例1 値：Anderes | Anderes | Datenverfügbarkeit | Technisches | Interne Weiterleitung
  - 同じ表の列：erfassung, nutzertyp, thema, kanal, zeitaufwand, mitarbeiter

## g0279（1 列）
- 見出し：thema
- 例1 値：Sonstiges | Finanzen | Haushalte | Steuern | Gebäude/Wohnungen
  - 同じ表の列：erfassung, nutzertyp, anfragetyp, kanal, zeitaufwand, mitarbeiter

## g0280（1 列）
- 見出し：kanal
- 例1 値：Email | Telefon | Telefon | Email | Telefon
  - 同じ表の列：erfassung, nutzertyp, anfragetyp, thema, zeitaufwand, mitarbeiter

## g0281（1 列）
- 見出し：zeitaufwand
- 例1 値：30 | 30 | 5 | 60 | 5
  - 同じ表の列：erfassung, nutzertyp, anfragetyp, thema, kanal, mitarbeiter

## g0282（1 列）
- 見出し：mitarbeiter
- 例1 値：M09 | M04 | M08 | M12 | M09
  - 同じ表の列：erfassung, nutzertyp, anfragetyp, thema, kanal, zeitaufwand

## g0283（1 列）
- 見出し：br_abschnitt_desc
- 例1 値：Alle Branchen | Alle Branchen | Alle Branchen | Alle Branchen | Alle Branchen
  - 同じ表の列：br_abschnitt_code, wirtschaftssektor_d…, wirtschaftssektor_c…, location, date, value

## g0284（1 列）
- 見出し：br_abschnitt_code
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：br_abschnitt_desc, wirtschaftssektor_d…, wirtschaftssektor_c…, location, date, value

## g0285（1 列）
- 見出し：wirtschaftssektor_desc
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：br_abschnitt_desc, br_abschnitt_code, wirtschaftssektor_c…, location, date, value

## g0286（1 列）
- 見出し：wirtschaftssektor_code
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：br_abschnitt_desc, br_abschnitt_code, wirtschaftssektor_d…, location, date, value

## g0287（1 列）
- 見出し：location
- 例1 値：CH | CH | CH | CH | CH
  - 同じ表の列：br_abschnitt_desc, br_abschnitt_code, wirtschaftssektor_d…, wirtschaftssektor_c…, date, value

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
```
