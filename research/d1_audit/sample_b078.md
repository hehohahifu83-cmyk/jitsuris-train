<!-- b078：15/150 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b078.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0013（1 列）
- 見出し：Raum
- 例1 値：innen | innen | aussen | innen | undifferenziert
  - 同じ表の列：Jahr, Art, Typ, Subtyp, Anzahl_stuecke_exkl…

## g0017（1 列）
- 見出し：Region
- 例1 値：AR | TG | GE | BE | OW
  - 同じ表の列：Jahr, Massnahmenbereich, Auszahlungen_CHF

## g0018（1 列）
- 見出し：Massnahmenbereich
- 例1 値：Systemsanierung | Systemsanierung | Neubau | Haustechnik | Neubau
  - 同じ表の列：Jahr, Region, Auszahlungen_CHF

## g0024（1 列）
- 見出し：SOURCE
- 例1 値：SVGW | SVGW | SVGW | SVGW | SVGW
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VALUE_PERIOD, UNIT_VALUE, VALUE, STATUS

## g0034（1 列）
- 見出し：OBS_CONFIDENCE
- 例1 値：10.2 | 7.1 | 11.7 | 14.4 | 7.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VALUE_PERIOD, UNIT_VALUE, VALUE

## g0084（1 列）
- 見出し：Ende Zeitspanne
- 例1 値：03:00 | 03:00 | 03:00 | 03:00 | 03:00
  - 同じ表の列：Monat, Wochentag, Start Zeitspanne, Gemeinde, Wohnviertel-ID, Wohnviertel, Bezirks-ID, Bezirk

## g0094（1 列）
- 見出し：KONFESSION_BEZEICHNUNG
- 例1 値：Römisch-katholisch | Evangelisch-reformiert | Römisch-katholisch | Evangelisch-reformiert | Römisch-katholisch
  - 同じ表の列：BFS_NR_GEMEINDE, BEZIRK_NR, JAHR, KONFESSION_CODE, ANZAHL_PERSONEN

## g0095（1 列）
- 見出し：ANZAHL_PERSONEN
- 例1 値：991 | 178 | 636 | 243 | 253
  - 同じ表の列：BFS_NR_GEMEINDE, BEZIRK_NR, JAHR, KONFESSION_CODE, KONFESSION_BEZEICHN…

## g0101（1 列）
- 見出し：EINWOHNER_0_19
- 例1 値：171 | 195 | 351 | 277 | 84
  - 同じ表の列：POLITISCHE_GEMEINDE, BFS_NR_GEMEINDE, BEZIRK_NR, ORTSCHAFT, EINWOHNER_TOTAL, EINWOHNER_MAENNER, EINWOHNER_FRAUEN, EINWOHNER_20_39

## g0105（1 列）
- 見出し：gemeinde
- 例1 値：Märstetten | Kreuzlingen | Ermatingen | Münchwilen | Erlen
  - 同じ表の列：datum, bfs_nr_gemeinde, bfs_bezirksnummer, bezirk, stimmberechtigte, stiausweiseurne, stiausweisevorzeitig, stiausweisebriefgue…

## g0108（1 列）
- 見出し：stimmberechtigte
- 例1 値：971 | 1790 | 2429 | 648 | 828
  - 同じ表の列：datum, bfs_nr_gemeinde, gemeinde, bfs_bezirksnummer, bezirk, stiausweiseurne, stiausweisevorzeitig, stiausweisebriefgue…

## g0117（1 列）
- 見出し：Abfuhrgebiet
- 例1 値：I | I | I | A | B
  - 同じ表の列：Monat_Jahr, Abfallfraktion, Unterkategorie, Entsorgungsart, Annahmestelle, Deponie Anlieferung, Gewicht in kg, Gewicht in t

## g0123（1 列）
- 見出し：9.31375951405936;"{""coordinates"": [[[9.307090061837643
- 例1 値：9.365121403431786;"{""coordinates"": [[… | 9.315297312563432;"{""coordinates"": [[… | 9.397102013250862;"{""coordinates"": [[… | 9.313572737090757;"{""coordinates"": [[… | 9.329127833707489;"{""coordinates"": [[…
  - 同じ表の列：47.405118100467725, 47.40741171431594], [9.307573482562857, 47.407389545005465], [9.3089221279932, 47.40732766784259], [9.309532118396758, 47.40725079057819]

## g0129（1 列）
- 見出し：[9.309532118396758
- 例1 値：[9.337986476636276 | [9.306822996002063 | [9.339488910016744 | [9.307248624672889 | [9.404432869139425
  - 同じ表の列：47.405118100467725, 9.31375951405936;"{…, 47.40741171431594], [9.307573482562857, 47.407389545005465], [9.3089221279932, 47.40732766784259], 47.40725079057819]

## g0146（2 列）
- 見出し：grouping
- 例1 値：lebensphase | haushaltstyp | haushaltstyp | lebensphase | haushaltstyp
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, whg_bauj_group_nr, whg_bauj_group
- 例2 値：haushaltstyp | lebensphase | lebensphase | lebensphase | lebensphase
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, haushalt_wohndauer_…, haushalt_wohndauer

## 答えの雛形

```
g0013	
g0017	
g0018	
g0024	
g0034	
g0084	
g0094	
g0095	
g0101	
g0105	
g0108	
g0117	
g0123	
g0129	
g0146	
```
