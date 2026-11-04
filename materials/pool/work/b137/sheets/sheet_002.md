# ラベル用シート 002 / 002

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0016（1 列）
- 見出し：Link
- 例1 値：https://www.dora.lib4ri.ch/eawag/island… | https://energie.tg.ch/public/upload/ass… | https://wires.onlinelibrary.wiley.com/d… | https://www.klimaschutz.bs.ch/informati… | https://thermdis.eawag.ch/static/templa…
  - 同じ表の列：Id, Titel, Ausgabejahr, Auftraggeber, Kanton

## g0017（1 列）
- 見出し：Date
- 例1 値：2012-12-31 | 2017-12-31 | 2016-12-31 | 2020-12-31 | 2010-12-31
  - 同じ表の列：Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0041（3 列）
- 見出し：OBJECTID
- 例1 値：3 | 20 | 6 | 55 | 68
  - 同じ表の列：NOM_DU_LIEU, STRUCTURE_PORTEUSE, ZONE_GEOGRAPHIQUE, VILLE_OU_COMMUNE, WEBSITE, EQUIPEMENTS, SERVICES, TYPES_ESPACE
- 例2 値：52 | 41 | 21 | 38 | 28
  - 同じ表の列：LIEU_DIT, SHAPE_AREA, SHAPE_LEN

## g0046（1 列）
- 見出し：WEBSITE
- 例1 値：https://www.multiburo.com/adresse/multi… | https://www.businesscenter-01.com/en/ | https://www.regus.com/de-ch/switzerland… | https://mousse-space.ch/ | https://www.maconciergerielocale.com/co…
  - 同じ表の列：OBJECTID, NOM_DU_LIEU, STRUCTURE_PORTEUSE, ZONE_GEOGRAPHIQUE, VILLE_OU_COMMUNE, EQUIPEMENTS, SERVICES, TYPES_ESPACE

## g0057（1 列）
- 見出し：Gemeinde
- 例1 値：Birsfelden | Pratteln | Bubendorf | Münchenstein | Wahlen
  - 同じ表の列：BFS_Gemeindenummer, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Alter, Anzahl_Plätze_Tages…

## g0059（3 列）
- 見出し：PLZ
- 例1 値：4106 | 4142 | 4402 | 4153 | 4415
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, Ort, Trägerschaft, Rechtsform, Alter, Anzahl_Plätze_Tages…
- 例2 値：4415 | 4402 | 4133 | 4410 | 4107
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, Ort, Website, Datenquelle, e_eingangskoordinate, n_eingangskoordinate

## g0060（1 列）
- 見出し：Ort
- 例1 値：Augst | Aesch | Birsfelden | Reinach | Allschwil
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Trägerschaft, Rechtsform, Alter, Anzahl_Plätze_Tages…

## g0067（1 列）
- 見出し：Kategorie
- 例1 値：Spielgruppe | Spielgruppe | Spielgruppe | Spielgruppe | Spielgruppe
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate, n_eingangskoordinate

## g0068（1 列）
- 見出し：Ort
- 例1 値：Birsfelden | Frenkendorf | Ormalingen | Liesberg Dorf | Oberwil (BL)
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Website, Datenquelle, e_eingangskoordinate, n_eingangskoordinate

## g0069（1 列）
- 見出し：Website
- 例1 値：https://www.kiekebu.com/spielgruppekiek… | https://spielgruppe-dschungelhuus.ch | https://www.kunterbunt-oberdorf.ch | https://wurzelpurzel-wahlen.jimdofree.c… | https://frauenverein-lausen.ch
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Datenquelle, e_eingangskoordinate, n_eingangskoordinate

## g0082（2 列）
- 見出し：Datum
- 例1 値：2021-09-26 | 2025-09-28 | 2022-02-13 | 2020-09-27 | 2020-09-27
  - 同じ表の列：Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal
- 例2 値：2026-06-14 | 2026-03-08 | 2022-05-15 | 2021-06-13 | 2026-03-08
  - 同じ表の列：Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0088（1 列）
- 見出し：Gemeinde
- 例1 値：Bettingen | Basel | Auslandschweizer | Basel | Basel
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Wahllokal-ID, Wahllokal

## g0094（1 列）
- 見出し：Gemeinde
- 例1 値：Auslandschweizer/-innen | Bettingen | Bettingen | Basel-Stadt | Basel
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, ID, Resultattyp

## 答えの雛形

```
g0016	
g0017	
g0041	
g0046	
g0057	
g0059	
g0060	
g0067	
g0068	
g0069	
g0082	
g0088	
g0094	
```
