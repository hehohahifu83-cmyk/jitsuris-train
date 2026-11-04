# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Betriebsnummer
- 例1 値：25_73 | 27_81 | 09_22 | 67_08 | 25_38
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Betriebsart, PLZ, Ort, Bemerkung, e_eingangskoordinate, n_eingangskoordinate

## g0002（3 列）
- 見出し：BFS_Gemeindenummer
- 例1 値：2856 | 2761 | 2834 | 2829 | 2766
  - 同じ表の列：Betriebsnummer, Gemeinde, Betriebsart, PLZ, Ort, Bemerkung, e_eingangskoordinate, n_eingangskoordinate
- 例2 値：4724 | 4891 | 4811 | 4471 | 4891
  - 同じ表の列：Bezirksnummer_alt, BFS_Gemeindenummer_…, BFS_Bezirksnummer_b…, Bezirk_bis_2010, Gueltig_ab

## g0003（1 列）
- 見出し：Gemeinde
- 例1 値：Birsfelden | Reinach | Allschwil | Liestal | Lauwil
  - 同じ表の列：Betriebsnummer, BFS_Gemeindenummer, Betriebsart, PLZ, Ort, Bemerkung, e_eingangskoordinate, n_eingangskoordinate

## g0004（1 列）
- 見出し：Betriebsart
- 例1 値：Restaurant | Restaurant | Restaurant | Restaurant | Restaurant
  - 同じ表の列：Betriebsnummer, BFS_Gemeindenummer, Gemeinde, PLZ, Ort, Bemerkung, e_eingangskoordinate, n_eingangskoordinate

## g0005（2 列）
- 見出し：PLZ
- 例1 値：4144 | 4104 | 4402 | 4144 | 4102
  - 同じ表の列：Betriebsnummer, BFS_Gemeindenummer, Gemeinde, Betriebsart, Ort, Bemerkung, e_eingangskoordinate, n_eingangskoordinate
- 例2 値：8546 | 8259 | 8572 | 9573 | 9553
  - 同じ表の列：Politische_Gemeinde, BFS_Nr, Bezirk_Bezeichnung, Bezirk_Nr, Siedlung, Einwohner, Ortschaft, Primarschulgemeinde

## g0006（1 列）
- 見出し：Ort
- 例1 値：Ettingen | Muttenz | Gelterkinden | Biel-Benken | Laufen
  - 同じ表の列：Betriebsnummer, BFS_Gemeindenummer, Gemeinde, Betriebsart, PLZ, Bemerkung, e_eingangskoordinate, n_eingangskoordinate

## g0007（1 列）
- 見出し：Bemerkung
- 例1 値：z. Zt. geschlossen | z. Zt. 10 Plätze mit Alkohol | (ehemals Vereinswirtschaft "Offside Mus… | z. Zt. geschlossen | * z. Zt. alkoholfrei mit max. 10 Plätzen
  - 同じ表の列：Betriebsnummer, BFS_Gemeindenummer, Gemeinde, Betriebsart, PLZ, Ort, e_eingangskoordinate, n_eingangskoordinate

## g0008（1 列）
- 見出し：e_eingangskoordinate
- 例1 値：2629862.949 | 2608875.424 | 2613493.461 | 2622324.38 | 2637550.087
  - 同じ表の列：Betriebsnummer, BFS_Gemeindenummer, Gemeinde, Betriebsart, PLZ, Ort, Bemerkung, n_eingangskoordinate

## g0009（1 列）
- 見出し：n_eingangskoordinate
- 例1 値：1260335.493 | 1264732.802 | 1251793.115 | 1266250.244 | 1260942.132
  - 同じ表の列：Betriebsnummer, BFS_Gemeindenummer, Gemeinde, Betriebsart, PLZ, Ort, Bemerkung, e_eingangskoordinate

## g0010（1 列）
- 見出し：koordinaten
- 例1 値：47.34850050842573, 7.764673242737458 | 47.463550788531414, 7.841245948557026 | 47.46312422077073, 7.811646033499359 | 47.49036764680149, 7.61956671603751 | 47.5546345441182, 7.619268252996977
  - 同じ表の列：Betriebsnummer, BFS_Gemeindenummer, Gemeinde, Betriebsart, PLZ, Ort, Bemerkung, e_eingangskoordinate

## g0011（1 列）
- 見出し：Kürzel
- 例1 値：A.5.4.1 | I.2 | A.4.3 | A.4.8.6 | K
  - 同じ表の列：Direktion, Abfrageberechtigte …, Aufgabenbereich, RRB-Nr. (Anschluss), Beschluss, GS-Nr., GS-Link, Inkrafttreten

## g0012（1 列）
- 見出し：Direktion
- 例1 値：Extern | Extern | VGD | Extern | SID
  - 同じ表の列：Kürzel, Abfrageberechtigte …, Aufgabenbereich, RRB-Nr. (Anschluss), Beschluss, GS-Nr., GS-Link, Inkrafttreten

## g0013（1 列）
- 見出し：Abfrageberechtigte Stelle
- 例1 値：Kantonales Sozialamt | Römisch-katholische Kirchgemeinden | Verwaltungen der Einwohnergemeinden | Verwaltungen der Einwohnergemeinden | Amt für Daten und Statistik
  - 同じ表の列：Kürzel, Direktion, Aufgabenbereich, RRB-Nr. (Anschluss), Beschluss, GS-Nr., GS-Link, Inkrafttreten

## g0014（1 列）
- 見出し：Aufgabenbereich
- 例1 値：Hauptabteilung Betreibungs- und Konkurs… | Eigene Mitglieder | Eigene Mitglieder | Amt für Militär und Bevölkerungsschutz | Abteilung Bürgerrecht
  - 同じ表の列：Kürzel, Direktion, Abfrageberechtigte …, RRB-Nr. (Anschluss), Beschluss, GS-Nr., GS-Link, Inkrafttreten

## g0015（1 列）
- 見出し：RRB-Nr. (Anschluss)
- 例1 値：2019-1264 | 2014-1391 | 2015-0673 | 2019-1264 | 2014-1391
  - 同じ表の列：Kürzel, Direktion, Abfrageberechtigte …, Aufgabenbereich, Beschluss, GS-Nr., GS-Link, Inkrafttreten

## g0016（1 列）
- 見出し：Beschluss
- 例1 値：2014-09-23 | 2015-01-27 | 2014-09-23 | 2017-10-17 | 2014-09-23
  - 同じ表の列：Kürzel, Direktion, Abfrageberechtigte …, Aufgabenbereich, RRB-Nr. (Anschluss), GS-Nr., GS-Link, Inkrafttreten

## g0017（1 列）
- 見出し：GS-Nr.
- 例1 値：2022.055 | 2017.052 | 2014.064 | 2016.081 | 2014.064
  - 同じ表の列：Kürzel, Direktion, Abfrageberechtigte …, Aufgabenbereich, RRB-Nr. (Anschluss), Beschluss, GS-Link, Inkrafttreten

## g0018（1 列）
- 見出し：GS-Link
- 例1 値：https://bl.clex.ch/app/de/change_docume… | https://bl.clex.ch/app/de/change_docume… | https://bl.clex.ch/app/de/change_docume… | https://bl.clex.ch/app/de/change_docume… | https://bl.clex.ch/app/de/change_docume…
  - 同じ表の列：Kürzel, Direktion, Abfrageberechtigte …, Aufgabenbereich, RRB-Nr. (Anschluss), Beschluss, GS-Nr., Inkrafttreten

## g0019（1 列）
- 見出し：Inkrafttreten
- 例1 値：2014-10-01 | 2019-10-01 | 2022-03-01 | 2014-10-01 | 2015-02-01
  - 同じ表の列：Kürzel, Direktion, Abfrageberechtigte …, Aufgabenbereich, RRB-Nr. (Anschluss), Beschluss, GS-Nr., GS-Link

## g0020（1 列）
- 見出し：Letzte Änderung
- 例1 値：2021-04-01 | 2024-02-01 | 2022-12-01 | 2019-01-01 | 2022-06-01
  - 同じ表の列：Kürzel, Direktion, Abfrageberechtigte …, Aufgabenbereich, RRB-Nr. (Anschluss), Beschluss, GS-Nr., GS-Link

## g0021（1 列）
- 見出し：Bezirksnummer_alt
- 例1 値：2002 | 2002 | 2004 | 2005 | 2002
  - 同じ表の列：BFS_Gemeindenummer_…, BFS_Bezirksnummer_b…, Bezirk_bis_2010, BFS_Gemeindenummer, Gueltig_ab

## g0022（1 列）
- 見出し：BFS_Gemeindenummer_alt
- 例1 値：4884 | 4688 | 4555 | 4510 | 4937
  - 同じ表の列：Bezirksnummer_alt, BFS_Bezirksnummer_b…, Bezirk_bis_2010, BFS_Gemeindenummer, Gueltig_ab

## g0023（2 列）
- 見出し：BFS_Bezirksnummer_bis_2010
- 例1 値：2006 | 2004 | 2008 | 2005 | 2002
  - 同じ表の列：Bezirksnummer_alt, BFS_Gemeindenummer_…, Bezirk_bis_2010, BFS_Gemeindenummer, Gueltig_ab
- 例2 値：2006 | 2007 | 2003 | 2005 | 2007
  - 同じ表の列：BFS_Bezirksnummer, Bezirk, BFS_Gemeindenummer, Gemeinde, Sortierung_in_Bezirk, Bezirk_bis_2010

## g0024（2 列）
- 見出し：Bezirk_bis_2010
- 例1 値：Bischofszell | Weinfelden | Weinfelden | Kreuzlingen | Weinfelden
  - 同じ表の列：Bezirksnummer_alt, BFS_Gemeindenummer_…, BFS_Bezirksnummer_b…, BFS_Gemeindenummer, Gueltig_ab
- 例2 値：Weinfelden | Bischofszell | Kreuzlingen | Weinfelden | Bischofszell
  - 同じ表の列：BFS_Bezirksnummer, Bezirk, BFS_Gemeindenummer, Gemeinde, Sortierung_in_Bezirk, BFS_Bezirksnummer_b…

## g0025（1 列）
- 見出し：Gueltig_ab
- 例1 値：1995-01-01 | 1995-01-01 | 1995-01-01 | 1995-12-31 | 1995-01-01
  - 同じ表の列：Bezirksnummer_alt, BFS_Gemeindenummer_…, BFS_Bezirksnummer_b…, Bezirk_bis_2010, BFS_Gemeindenummer

## g0026（1 列）
- 見出し：BFS_Bezirksnummer
- 例1 値：2011 | 2011 | 2012 | 2013 | 2013
  - 同じ表の列：Bezirk, BFS_Gemeindenummer, Gemeinde, Sortierung_in_Bezirk, Bezirk_bis_2010, BFS_Bezirksnummer_b…

## g0027（1 列）
- 見出し：Bezirk
- 例1 値：Weinfelden | Münchwilen | Frauenfeld | Arbon | Arbon
  - 同じ表の列：BFS_Bezirksnummer, BFS_Gemeindenummer, Gemeinde, Sortierung_in_Bezirk, Bezirk_bis_2010, BFS_Bezirksnummer_b…

## g0028（1 列）
- 見出し：Gemeinde
- 例1 値：Affeltrangen | Berg | Kesswil | Kradolf-Schönenberg | Birwinken
  - 同じ表の列：BFS_Bezirksnummer, Bezirk, BFS_Gemeindenummer, Sortierung_in_Bezirk, Bezirk_bis_2010, BFS_Bezirksnummer_b…

## g0029（1 列）
- 見出し：Sortierung_in_Bezirk
- 例1 値：77 | 48 | 30 | 80 | 53
  - 同じ表の列：BFS_Bezirksnummer, Bezirk, BFS_Gemeindenummer, Gemeinde, Bezirk_bis_2010, BFS_Bezirksnummer_b…

## g0030（1 列）
- 見出し：Politische_Gemeinde
- 例1 値：Hüttwilen | Birwinken | Kemmental | Kradolf-Schönenberg | Thundorf
  - 同じ表の列：BFS_Nr, Bezirk_Bezeichnung, Bezirk_Nr, Siedlung, Einwohner, PLZ, Ortschaft, Primarschulgemeinde

## g0031（1 列）
- 見出し：BFS_Nr
- 例1 値：4806 | 4406 | 4726 | 4591 | 4656
  - 同じ表の列：Politische_Gemeinde, Bezirk_Bezeichnung, Bezirk_Nr, Siedlung, Einwohner, PLZ, Ortschaft, Primarschulgemeinde

## g0032（1 列）
- 見出し：Bezirk_Bezeichnung
- 例1 値：Weinfelden | Weinfelden | Weinfelden | Münchwilen | Kreuzlingen
  - 同じ表の列：Politische_Gemeinde, BFS_Nr, Bezirk_Nr, Siedlung, Einwohner, PLZ, Ortschaft, Primarschulgemeinde

## g0033（1 列）
- 見出し：Bezirk_Nr
- 例1 値：2012 | 2012 | 2012 | 2015 | 2014
  - 同じ表の列：Politische_Gemeinde, BFS_Nr, Bezirk_Bezeichnung, Siedlung, Einwohner, PLZ, Ortschaft, Primarschulgemeinde

## g0034（1 列）
- 見出し：Siedlung
- 例1 値：Kronberg | Thurfeld | Schwärzi (Homburg) | Murkart | Engelswilen
  - 同じ表の列：Politische_Gemeinde, BFS_Nr, Bezirk_Bezeichnung, Bezirk_Nr, Einwohner, PLZ, Ortschaft, Primarschulgemeinde

## g0035（1 列）
- 見出し：Einwohner
- 例1 値：20 | x | x | x | 9
  - 同じ表の列：Politische_Gemeinde, BFS_Nr, Bezirk_Bezeichnung, Bezirk_Nr, Siedlung, PLZ, Ortschaft, Primarschulgemeinde

## g0036（1 列）
- 見出し：Ortschaft
- 例1 値：Oberwangen | Schönenberg an der Thur | Schweizersholz | Kaltenbach | Braunau
  - 同じ表の列：Politische_Gemeinde, BFS_Nr, Bezirk_Bezeichnung, Bezirk_Nr, Siedlung, Einwohner, PLZ, Primarschulgemeinde

## g0037（1 列）
- 見出し：Primarschulgemeinde
- 例1 値：Fischingen | Herdern-Dettighofen | Eschlikon | Neunforn | Nollen
  - 同じ表の列：Politische_Gemeinde, BFS_Nr, Bezirk_Bezeichnung, Bezirk_Nr, Siedlung, Einwohner, PLZ, Ortschaft

## g0038（1 列）
- 見出し：Sekundarschulgemeinde
- 例1 値：Amriswil-Hefenhofen-Sommeri | Arbon | Weinfelden | Hüttwilen | Eschenz
  - 同じ表の列：Politische_Gemeinde, BFS_Nr, Bezirk_Bezeichnung, Bezirk_Nr, Siedlung, Einwohner, PLZ, Ortschaft

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
```
