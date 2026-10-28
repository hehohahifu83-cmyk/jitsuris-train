# ラベル用シート 001 / 005

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（3 列）
- 見出し：commune_no
- 例1 値：39 | 21 | 44 | 16 | 10
  - 同じ表の列：local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc
- 例2 値：11 | 1 | 16 | 18 | 21
  - 同じ表の列：local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc

## g0002（3 列）
- 見出し：local_no
- 例1 値：1 | 1 | 12 | 1 | 1
  - 同じ表の列：commune_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc
- 例2 値：6 | 1 | 0 | 1 | 3
  - 同じ表の列：commune_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc

## g0003（1 列）
- 見出し：local-commune_nom
- 例1 値：Champel | Presinge | Corsier | Prieuré - Sécheron | Prairie-Délices
  - 同じ表の列：commune_no, local_no, electorat, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc

## g0004（2 列）
- 見出し：electorat
- 例1 値：2'919 | 416 | 4'393 | 334 | 2'252
  - 同じ表の列：commune_no, local_no, local-commune_nom, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc
- 例2 値：366 | 1'549 | 1'393 | 702 | 5'391
  - 同じ表の列：commune_no, local_no, local-commune_nom, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc

## g0005（3 列）
- 見出し：cartes-de-vote
- 例1 値：2'840 | 239 | 597 | 1'228 | 330
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, bulletins, nuls, q1_blancs, q1_blancs_pc
- 例2 値：771 | 2'166 | 1'535 | 432 | 1'196
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, bulletins, nuls, q1_blancs, q1_blancs_pc

## g0006（3 列）
- 見出し：bulletins
- 例1 値：578 | 669 | 351 | 239 | 1'092
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, nuls, q1_blancs, q1_blancs_pc
- 例2 値：216 | 186 | 238 | 2'847 | 686
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, nuls, q1_blancs, q1_blancs_pc

## g0007（3 列）
- 見出し：nuls
- 例1 値：0 | 1 | 0 | 1 | 0
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, q1_blancs, q1_blancs_pc
- 例2 値：2 | 0 | 0 | 0 | 0
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, q1_blancs, q1_blancs_pc

## g0008（3 列）
- 見出し：q1_blancs
- 例1 値：63 | 15 | 36 | 52 | 71
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs_pc
- 例2 値：7 | 5 | 2 | 7 | 31
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs_pc

## g0009（3 列）
- 見出し：q1_blancs_pc
- 例1 値：3.43% | 3.62% | 3.50% | 3.30% | 3.76%
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs
- 例2 値：0.50% | 0.87% | 1.00% | 1.39% | 0.36%
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs

## g0010（3 列）
- 見出し：q1_valables
- 例1 値：372 | 311 | 2'764 | 318 | 119
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs
- 例2 値：772 | 560 | 2'449 | 288 | 3'241
  - 同じ表の列：commune_no, local_no, local-commune_nom, electorat, cartes-de-vote, bulletins, nuls, q1_blancs

## g0011（1 列）
- 見出し：local-commune_nom
- 例1 値：Pregny-Chambsy | Are-Le Lignon | Collex-Bossy | Acacias | Veyrier
  - 同じ表の列：commune_no, local_no, electorat, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc

## g0012（1 列）
- 見出し：electorat
- 例1 値：4'351 | 1'081 | 6'261 | 6'202 | 1'757
  - 同じ表の列：commune_no, local_no, local-commune_nom, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc

## g0013（1 列）
- 見出し：local-commune_nom
- 例1 値：Acacias | Carouge | Presinge | Hermance | Jussy
  - 同じ表の列：commune_no, local_no, electorat, cartes-de-vote, bulletins, nuls, q1_blancs, q1_blancs_pc

## g0014（32 列）
- 見出し：jahr
- 例1 値：2018 | 2018 | 2018 | 2018 | 2018
  - 同じ表の列：zeithorizonttyp, quelle_gebietart, quelle_code, ziel_gebietart, ziel_code, verkehrsmittel, wert, einheit
- 例2 値：2024 | 2023 | 2024 | 2025 | 2025
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_M…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…

## g0015（1 列）
- 見出し：zeithorizonttyp
- 例1 値：modellierter Ist-Zustand | modellierter Ist-Zustand | modellierter Ist-Zustand | modellierter Ist-Zustand | modellierter Ist-Zustand
  - 同じ表の列：jahr, quelle_gebietart, quelle_code, ziel_gebietart, ziel_code, verkehrsmittel, wert, einheit

## g0016（1 列）
- 見出し：quelle_gebietart
- 例1 値：Gemeinde | Gemeinde | Gemeinde | Gemeinde | Gemeinde
  - 同じ表の列：jahr, zeithorizonttyp, quelle_code, ziel_gebietart, ziel_code, verkehrsmittel, wert, einheit

## g0017（1 列）
- 見出し：quelle_code
- 例1 値：1 | 1 | 2 | 2 | 2
  - 同じ表の列：jahr, zeithorizonttyp, quelle_gebietart, ziel_gebietart, ziel_code, verkehrsmittel, wert, einheit

## g0018（1 列）
- 見出し：ziel_gebietart
- 例1 値：Gemeinde | Gemeinde | Gemeinde | Gemeinde | Gemeinde
  - 同じ表の列：jahr, zeithorizonttyp, quelle_gebietart, quelle_code, ziel_code, verkehrsmittel, wert, einheit

## g0019（1 列）
- 見出し：ziel_code
- 例1 値：245 | 13 | 224 | 4 | 8
  - 同じ表の列：jahr, zeithorizonttyp, quelle_gebietart, quelle_code, ziel_gebietart, verkehrsmittel, wert, einheit

## g0020（1 列）
- 見出し：verkehrsmittel
- 例1 値：oev | oev | miv | miv | oev
  - 同じ表の列：jahr, zeithorizonttyp, quelle_gebietart, quelle_code, ziel_gebietart, ziel_code, wert, einheit

## g0021（4 列）
- 見出し：wert
- 例1 値：90 | 0 | 626 | 0 | 0
  - 同じ表の列：jahr, zeithorizonttyp, quelle_gebietart, quelle_code, ziel_gebietart, ziel_code, verkehrsmittel, einheit
- 例2 値：25292 | 93053 | 363116 | 59972 | 200050
  - 同じ表の列：Jahr, Deponietyp, Einheit

## g0022（1 列）
- 見出し：einheit
- 例1 値：Personenwege an einem durchschnittliche… | Personenwege an einem durchschnittliche… | Personenwege an einem durchschnittliche… | Personenwege an einem durchschnittliche… | Personenwege an einem durchschnittliche…
  - 同じ表の列：jahr, zeithorizonttyp, quelle_gebietart, quelle_code, ziel_gebietart, ziel_code, verkehrsmittel, wert

## g0023（1 列）
- 見出し：gebietsstand
- 例1 値：2019 | 2019 | 2019 | 2019 | 2019
  - 同じ表の列：jahr, zeithorizonttyp, quelle_gebietart, quelle_code, ziel_gebietart, ziel_code, verkehrsmittel, wert

## g0024（4 列）
- 見出し：BFS_NR
- 例1 値：38 | 34 | 195 | 295 | 69
  - 同じ表の列：GEO_LEVEL_LEVEL, JAHR, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_M…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…
- 例2 値：31 | 5 | 39 | 2 | 10
  - 同じ表の列：GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Wo…, Ueberbauungsgrad_Mi…, Ueberbauungsgrad_Ar…, Ueberbauungsgrad_Zo…, Ueberbauungsgrad_Ge…, Einheit

## g0025（3 列）
- 見出し：GEO_LEVEL_LEVEL
- 例1 値：3 | 3 | 3 | 3 | 3
  - 同じ表の列：BFS_NR, JAHR, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_M…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…
- 例2 値：3 | 3 | 3 | 3 | 3
  - 同じ表の列：BFS_NR, JAHR, Ueberbauungsgrad_Wo…, Ueberbauungsgrad_Mi…, Ueberbauungsgrad_Ar…, Ueberbauungsgrad_Zo…, Ueberbauungsgrad_Ge…, Einheit

## g0026（1 列）
- 見出し：GFLRES_Ueberbaute_Wohnzonen
- 例1 値：81.5 | 19.8 | 118.7 | 263.2 | 181.3
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, GFLRES_Ueberbaute_M…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…

## g0027（1 列）
- 見出し：GFLRES_Ueberbaute_Mischzonen
- 例1 値：8.3 | 31.2 | 10.4 | 59.6 | 2412.6
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…

## g0028（1 列）
- 見出し：GFLRES_Ueberbaute_Arbeitszonen
- 例1 値：0 | 328.3 | 0 | 147.9 | 450.1
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_M…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…

## g0029（1 列）
- 見出し：GFLRES_Nicht_Ueberbaute_Wohnzonen
- 例1 値：635.1 | 9.4 | 340.9 | 55.9 | 0
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_M…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…

## g0030（1 列）
- 見出し：GFLRES_Nicht_Ueberbaute_Mischzonen
- 例1 値：10.9 | 2.1 | 7.6 | 7.5 | 5.4
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_M…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…

## g0031（1 列）
- 見出し：GFLRES_Nicht_Ueberbaute_Arbeitszonen
- 例1 値：2.6 | 17.7 | 530.1 | 86.5 | 13.9
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_M…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…

## g0032（1 列）
- 見出し：Einheit
- 例1 値：1000m2 | 1000m2 | 1000m2 | 1000m2 | 1000m2
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, GFLRES_Ueberbaute_W…, GFLRES_Ueberbaute_M…, GFLRES_Ueberbaute_A…, GFLRES_Nicht_Ueberb…, GFLRES_Nicht_Ueberb…

## g0033（1 列）
- 見出し：Ueberbauungsgrad_Wohnzonen
- 例1 値：84.7 | 94.1 | 88.9 | 87.5 | 90.4
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Mi…, Ueberbauungsgrad_Ar…, Ueberbauungsgrad_Zo…, Ueberbauungsgrad_Ge…, Einheit

## g0034（1 列）
- 見出し：Ueberbauungsgrad_Mischzonen
- 例1 値：84 | 91 | 86.3 | 95.9 | 90.7
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Wo…, Ueberbauungsgrad_Ar…, Ueberbauungsgrad_Zo…, Ueberbauungsgrad_Ge…, Einheit

## g0035（1 列）
- 見出し：Ueberbauungsgrad_Arbeitszonen
- 例1 値：55.9 | 71.4 | 89.8 | 90.6 | 74.2
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Wo…, Ueberbauungsgrad_Mi…, Ueberbauungsgrad_Zo…, Ueberbauungsgrad_Ge…, Einheit

## g0036（1 列）
- 見出し：Ueberbauungsgrad_Zone_OeBa
- 例1 値：49 | 100 | 100 | 48.2 | 100
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Wo…, Ueberbauungsgrad_Mi…, Ueberbauungsgrad_Ar…, Ueberbauungsgrad_Ge…, Einheit

## g0037（1 列）
- 見出し：Ueberbauungsgrad_Gesamt
- 例1 値：90 | 77.8 | 87.6 | 77.3 | 72.4
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Wo…, Ueberbauungsgrad_Mi…, Ueberbauungsgrad_Ar…, Ueberbauungsgrad_Zo…, Einheit

## g0038（1 列）
- 見出し：Einheit
- 例1 値：% | % | % | % | %
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Ueberbauungsgrad_Wo…, Ueberbauungsgrad_Mi…, Ueberbauungsgrad_Ar…, Ueberbauungsgrad_Zo…, Ueberbauungsgrad_Ge…

## g0039（1 列）
- 見出し：Einwohner_pro_ha_Wohnzone
- 例1 値：51.9 | 54 | 27.5 | 43.9 | 33.7
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Einwohner_pro_ha_Mi…, Einwohner_pro_ha_Ar…, Einwohner_pro_ha_Ge…, Beschaeftigte_pro_h…, Beschaeftigte_pro_h…

## g0040（1 列）
- 見出し：Einwohner_pro_ha_Mischzone
- 例1 値：32.2 | 71.4 | 58.1 | 50.9 | 72.9
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Einwohner_pro_ha_Wo…, Einwohner_pro_ha_Ar…, Einwohner_pro_ha_Ge…, Beschaeftigte_pro_h…, Beschaeftigte_pro_h…

## g0041（1 列）
- 見出し：Einwohner_pro_ha_Arbeitszone
- 例1 値：1.4 | 2.8 | 1.7 | 3.8 | 0.6
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Einwohner_pro_ha_Wo…, Einwohner_pro_ha_Mi…, Einwohner_pro_ha_Ge…, Beschaeftigte_pro_h…, Beschaeftigte_pro_h…

## g0042（1 列）
- 見出し：Einwohner_pro_ha_Gesamt
- 例1 値：48.9 | 47 | 40.6 | 42.8 | 43.9
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Einwohner_pro_ha_Wo…, Einwohner_pro_ha_Mi…, Einwohner_pro_ha_Ar…, Beschaeftigte_pro_h…, Beschaeftigte_pro_h…

## g0043（1 列）
- 見出し：Beschaeftigte_pro_ha_Wohnzone
- 例1 値：4.9 | 3.8 | 2.9 | 4.6 | 4.8
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Einwohner_pro_ha_Wo…, Einwohner_pro_ha_Mi…, Einwohner_pro_ha_Ar…, Einwohner_pro_ha_Ge…, Beschaeftigte_pro_h…

## g0044（1 列）
- 見出し：Beschaeftigte_pro_ha_Mischzone
- 例1 値：8.1 | 17.3 | 49.5 | 12.6 | 4.5
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Einwohner_pro_ha_Wo…, Einwohner_pro_ha_Mi…, Einwohner_pro_ha_Ar…, Einwohner_pro_ha_Ge…, Beschaeftigte_pro_h…

## g0045（1 列）
- 見出し：Beschaeftigte_pro_ha_Arbeitszone
- 例1 値：31.3 | 148.3 | 44.9 | 95.7 | 88.6
  - 同じ表の列：BFS_NR, GEO_LEVEL_LEVEL, JAHR, Einwohner_pro_ha_Wo…, Einwohner_pro_ha_Mi…, Einwohner_pro_ha_Ar…, Einwohner_pro_ha_Ge…, Beschaeftigte_pro_h…

## g0046（1 列）
- 見出し：Gemeinde_Nr
- 例1 値：41 | 23 | 6 | 89 | 90
  - 同じ表の列：Jahr, Gemeinde, Abfallart, Wert, Einheit

## g0047（1 列）
- 見出し：Gemeinde
- 例1 値：Bäretswil | Dielsdorf | Affoltern a.A. | Rafz | Niederhasli
  - 同じ表の列：Jahr, Gemeinde_Nr, Abfallart, Wert, Einheit

## g0048（1 列）
- 見出し：Abfallart
- 例1 値：Karton | Papier + Karton falls nicht separat ang… | Kunststoffe | Textilien | Strassensammlerschlämme
  - 同じ表の列：Jahr, Gemeinde_Nr, Gemeinde, Wert, Einheit

## g0049（1 列）
- 見出し：Wert
- 例1 値：NA | 56 | 21 | 23 | 235
  - 同じ表の列：Jahr, Gemeinde_Nr, Gemeinde, Abfallart, Einheit

## g0050（3 列）
- 見出し：Einheit
- 例1 値：Tonnen | Tonnen | Tonnen | Tonnen | Tonnen
  - 同じ表の列：Jahr, Gemeinde_Nr, Gemeinde, Abfallart, Wert
- 例2 値：Prozent | Prozent | Personen | Personen | Prozent
  - 同じ表の列：jahr, metrik, wert

## g0051（1 列）
- 見出し：starttime
- 例1 値：2020-03-05 08:50 | 2020-03-02 03:20 | 2020-03-04 07:10 | 2020-03-07 14:30 | 2020-03-01 00:50
  - 同じ表の列：site, masl, magl, x, y, sensor, temperature, humidity

## g0052（1 列）
- 見出し：site
- 例1 値：Bülach - Feldermösli | Bülach - Feldermösli | Bülach - Feldermösli | Bülach - Feldermösli | Bülach - Feldermösli
  - 同じ表の列：starttime, masl, magl, x, y, sensor, temperature, humidity

## g0053（1 列）
- 見出し：masl
- 例1 値：417 | 417 | 417 | 417 | 417
  - 同じ表の列：starttime, site, magl, x, y, sensor, temperature, humidity

## g0054（1 列）
- 見出し：magl
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：starttime, site, masl, x, y, sensor, temperature, humidity

## g0055（1 列）
- 見出し：x
- 例1 値：2682216 | 2682216 | 2682216 | 2682216 | 2682216
  - 同じ表の列：starttime, site, masl, magl, y, sensor, temperature, humidity

## g0056（1 列）
- 見出し：y
- 例1 値：1262843 | 1262843 | 1262843 | 1262843 | 1262843
  - 同じ表の列：starttime, site, masl, magl, x, sensor, temperature, humidity

## g0057（1 列）
- 見出し：sensor
- 例1 値：531 | 531 | 531 | 531 | 531
  - 同じ表の列：starttime, site, masl, magl, x, y, temperature, humidity

## g0058（1 列）
- 見出し：temperature
- 例1 値：7.15 | 8.1 | 2.35 | 1.13 | 4.87
  - 同じ表の列：starttime, site, masl, magl, x, y, sensor, humidity

## g0059（1 列）
- 見出し：humidity
- 例1 値：78.54 | 86.21 | 87.12 | 75.4 | 84.29
  - 同じ表の列：starttime, site, masl, magl, x, y, sensor, temperature

## g0060（1 列）
- 見出し：Deponietyp
- 例1 値：Typ B (Inertstoff) | Typ E (Reaktorstoff) | Typ D (Schlacke) | Typ B (Inertstoff) | Typ E (Reaktorstoff)
  - 同じ表の列：Jahr, Wert, Einheit

## g0061（1 列）
- 見出し：Einheit
- 例1 値：Tonnen (t) | Tonnen (t) | Tonnen (t) | Tonnen (t) | Tonnen (t)
  - 同じ表の列：Jahr, Deponietyp, Wert

## g0062（4 列）
- 見出し：Stand
- 例1 値：2026-10-27 | 2026-10-27 | 2026-10-27 | 2026-10-27 | 2026-10-27
  - 同じ表の列：Stand_Gemeindegrenz…, Bezirk, Gemeinde_BFSCode, Gemeinde, Total_Abschluss_gym…, Total_19_Jahre_alt, Maturitaetsquote_gy…
- 例2 値：2026-10-27 | 2026-10-27 | 2026-10-27 | 2026-10-27 | 2026-10-27
  - 同じ表の列：kanton, jahr, abschlusstyp, anzahl

## g0063（1 列）
- 見出し：Stand_Gemeindegrenzen
- 例1 値：2014 | 2016 | 2017 | 2018 | 2016
  - 同じ表の列：Stand, Bezirk, Gemeinde_BFSCode, Gemeinde, Total_Abschluss_gym…, Total_19_Jahre_alt, Maturitaetsquote_gy…

## g0064（1 列）
- 見出し：Bezirk
- 例1 値：Bezirk Andelfingen | Bezirk Horgen | Bezirk Andelfingen | Bezirk Pfäffikon | Bezirk Bülach
  - 同じ表の列：Stand, Stand_Gemeindegrenz…, Gemeinde_BFSCode, Gemeinde, Total_Abschluss_gym…, Total_19_Jahre_alt, Maturitaetsquote_gy…

## g0065（1 列）
- 見出し：Gemeinde_BFSCode
- 例1 値：41 | 120 | 35 | 10 | 221
  - 同じ表の列：Stand, Stand_Gemeindegrenz…, Bezirk, Gemeinde, Total_Abschluss_gym…, Total_19_Jahre_alt, Maturitaetsquote_gy…

## g0066（1 列）
- 見出し：Gemeinde
- 例1 値：Langnau am Albis | Pfungen | Uetikon am See | Marthalen | Andelfingen
  - 同じ表の列：Stand, Stand_Gemeindegrenz…, Bezirk, Gemeinde_BFSCode, Total_Abschluss_gym…, Total_19_Jahre_alt, Maturitaetsquote_gy…

## g0067（1 列）
- 見出し：Total_Abschluss_gymnasial
- 例1 値：33 | 62 | 32 | 303 | 73
  - 同じ表の列：Stand, Stand_Gemeindegrenz…, Bezirk, Gemeinde_BFSCode, Gemeinde, Total_19_Jahre_alt, Maturitaetsquote_gy…

## g0068（1 列）
- 見出し：Total_19_Jahre_alt
- 例1 値：29 | 48 | 37 | 41 | 26
  - 同じ表の列：Stand, Stand_Gemeindegrenz…, Bezirk, Gemeinde_BFSCode, Gemeinde, Total_Abschluss_gym…, Maturitaetsquote_gy…

## g0069（1 列）
- 見出し：Maturitaetsquote_gymnasial
- 例1 値：16.22 | 16.67 | 19.58 | 23.54 | 19.64
  - 同じ表の列：Stand, Stand_Gemeindegrenz…, Bezirk, Gemeinde_BFSCode, Gemeinde, Total_Abschluss_gym…, Total_19_Jahre_alt

## g0070（5 列）
- 見出し：kanton
- 例1 値：zh | zh | zh | zh | zh
  - 同じ表の列：stand, jahr, abschlusstyp, anzahl
- 例2 値：zh | zh | zh | zh | zh
  - 同じ表の列：stand, jahr, bildungsfeld, berufsmaturitaetstyp, anzahl

## g0071（1 列）
- 見出し：abschlusstyp
- 例1 値：Berufsmaturität (BM1) | Gymnasiale Maturität | Passerelle | Kauffrau/Kaufmann EFZ mit BM1 (HMS) | Informatikerin/Informatiker EFZ mit BM1…
  - 同じ表の列：stand, kanton, jahr, anzahl

## g0072（5 列）
- 見出し：anzahl
- 例1 値：50 | 3017 | 1053 | 3191 | 32
  - 同じ表の列：stand, kanton, jahr, abschlusstyp
- 例2 値：504 | 1549 | 43 | 260 | 13217
  - 同じ表の列：stand, kanton, jahr, bildungsfeld, berufsmaturitaetstyp

## g0073（1 列）
- 見出し：bildungsfeld
- 例1 値：Geisteswissenschaften und Künste | Dienstleistungen | Wirtschaft, Verwaltung und Recht | Wirtschaft, Verwaltung und Recht | Sozialwissenschaften, Journalismus und …
  - 同じ表の列：stand, kanton, jahr, berufsmaturitaetstyp, anzahl

## g0074（1 列）
- 見出し：berufsmaturitaetstyp
- 例1 値：Total | Berufsfachschule (ohne BM) | BM1 | Berufsfachschule (ohne BM) | BM2
  - 同じ表の列：stand, kanton, jahr, bildungsfeld, anzahl

## g0075（1 列）
- 見出し：Departement
- 例1 値：EDI | EDA | EDA | EDA | PARL,BR,BK
  - 同じ表の列：Verwaltungseinheit …, Lieferant (Auftragn…, Ort, Beschaffungsgegenst…, Vergabeverfahren, Vertragsbeginn, Vertragsende, Auftragsvolumen ink…

## g0076（1 列）
- 見出し：Verwaltungseinheit (Auftraggeber)
- 例1 値：EDA | EDA | BAG | BAG | EDA
  - 同じ表の列：Departement, Lieferant (Auftragn…, Ort, Beschaffungsgegenst…, Vergabeverfahren, Vertragsbeginn, Vertragsende, Auftragsvolumen ink…

## g0077（1 列）
- 見出し：Lieferant (Auftragnehmer)
- 例1 値：Arxys GmbH | Abdeljalil Akkari | Olivier Haener | Itech Consult AG | clavis IT ag
  - 同じ表の列：Departement, Verwaltungseinheit …, Ort, Beschaffungsgegenst…, Vergabeverfahren, Vertragsbeginn, Vertragsende, Auftragsvolumen ink…

## g0078（1 列）
- 見出し：Ort
- 例1 値：Bern | Zürich | St. Gallen | Basel | Paris
  - 同じ表の列：Departement, Verwaltungseinheit …, Lieferant (Auftragn…, Beschaffungsgegenst…, Vergabeverfahren, Vertragsbeginn, Vertragsende, Auftragsvolumen ink…

## g0079（1 列）
- 見出し：Beschaffungsgegenstand
- 例1 値：Dienstleistungen im Zusammenhang mit Pe… | Informatikdienstleistungen im Bereich I… | Diverse Dienstleistungen für die öffent… | Informationsarbeit | Personalverleih und temporäres Personal…
  - 同じ表の列：Departement, Verwaltungseinheit …, Lieferant (Auftragn…, Ort, Vergabeverfahren, Vertragsbeginn, Vertragsende, Auftragsvolumen ink…

## g0080（1 列）
- 見出し：Vergabeverfahren
- 例1 値：Freihändiges Verfahren | Freihändiges Verfahren | Offenes Verfahren | Freihändiges Verfahren | Freihändiges Verfahren
  - 同じ表の列：Departement, Verwaltungseinheit …, Lieferant (Auftragn…, Ort, Beschaffungsgegenst…, Vertragsbeginn, Vertragsende, Auftragsvolumen ink…

## g0081（1 列）
- 見出し：Vertragsbeginn
- 例1 値：20.06.2023 | 01.07.2023 | 06.12.2023 | 01.12.2023 | 01.03.2023
  - 同じ表の列：Departement, Verwaltungseinheit …, Lieferant (Auftragn…, Ort, Beschaffungsgegenst…, Vergabeverfahren, Vertragsende, Auftragsvolumen ink…

## g0082（1 列）
- 見出し：Vertragsende
- 例1 値：31.12.2024 | 31.12.2025 | 31.07.2027 | 31.12.2023 | 30.04.2027
  - 同じ表の列：Departement, Verwaltungseinheit …, Lieferant (Auftragn…, Ort, Beschaffungsgegenst…, Vergabeverfahren, Vertragsbeginn, Auftragsvolumen ink…

## g0083（1 列）
- 見出し：Auftragsvolumen inkl. MwSt in CHF
- 例1 値：157498.95 | 165634 | 50543 | 440876.49 | 107000
  - 同じ表の列：Departement, Verwaltungseinheit …, Lieferant (Auftragn…, Ort, Beschaffungsgegenst…, Vergabeverfahren, Vertragsbeginn, Vertragsende

## g0084（1 列）
- 見出し：Versicherer
- 例1 値：343 | 376 | 1529 | 1386 | 923
  - 同じ表の列：Kanton, Geschaftsjahr, Durchschnittsbestand

## g0085（1 列）
- 見出し：Geschaftsjahr
- 例1 値：2019 | 2019 | 2019 | 2019 | 2019
  - 同じ表の列：Versicherer, Kanton, Durchschnittsbestand

## g0086（1 列）
- 見出し：Durchschnittsbestand
- 例1 値：336.0699999 | 169.01 | 1305.0658 | 5.17 | 47.1
  - 同じ表の列：Versicherer, Kanton, Geschaftsjahr

## g0087（1 列）
- 見出し：institution
- 例1 値：Les Hôpitaux Universitaires de Genève H… | Les Hôpitaux Universitaires de Genève H… | Les Hôpitaux Universitaires de Genève H… | Les Hôpitaux Universitaires de Genève H… | Les Hôpitaux Universitaires de Genève H…
  - 同じ表の列：indicator, taux observe 2019-2…, taux attendu 2019-2…, SMR 2019-2023, nombre de cas 2019-…, taux observe 2024, taux attendu 2024, SMR 2024

## g0088（1 列）
- 見出し：indicator
- 例1 値：B.1.16.P DP infarctus cérébral avec réé… | A.7.21.P OP des carotides en cas de rem… | A.7.32.M Remplacement isolé de valve ao… | A.2.1.MrG DP insuffisance cardiaque (âg… | A.7.22.P OP isolée des carotides en cas…
  - 同じ表の列：institution, taux observe 2019-2…, taux attendu 2019-2…, SMR 2019-2023, nombre de cas 2019-…, taux observe 2024, taux attendu 2024, SMR 2024

## g0089（1 列）
- 見出し：taux observe 2019-2023
- 例1 値：0.0% | 2.7% | 0.7% | 10.0% | 23.1%
  - 同じ表の列：institution, indicator, taux attendu 2019-2…, SMR 2019-2023, nombre de cas 2019-…, taux observe 2024, taux attendu 2024, SMR 2024

## g0090（1 列）
- 見出し：taux attendu 2019-2023
- 例1 値：3.0% | 0.1% | 5.3% | * | *
  - 同じ表の列：institution, indicator, taux observe 2019-2…, SMR 2019-2023, nombre de cas 2019-…, taux observe 2024, taux attendu 2024, SMR 2024

## g0091（1 列）
- 見出し：SMR 2019-2023
- 例1 値：* | * | 0.0 | * | *
  - 同じ表の列：institution, indicator, taux observe 2019-2…, taux attendu 2019-2…, nombre de cas 2019-…, taux observe 2024, taux attendu 2024, SMR 2024

## g0092（1 列）
- 見出し：nombre de cas 2019-2023
- 例1 値：2 | 820 | 75 | 1'554 | 141
  - 同じ表の列：institution, indicator, taux observe 2019-2…, taux attendu 2019-2…, SMR 2019-2023, taux observe 2024, taux attendu 2024, SMR 2024

## g0093（1 列）
- 見出し：taux observe 2024
- 例1 値：83.5% | 83.8% | 3.6% | 4.7% | 7.4%
  - 同じ表の列：institution, indicator, taux observe 2019-2…, taux attendu 2019-2…, SMR 2019-2023, nombre de cas 2019-…, taux attendu 2024, SMR 2024

## g0094（1 列）
- 見出し：taux attendu 2024
- 例1 値：0.7% | 0.0% | * | * | 4.1%
  - 同じ表の列：institution, indicator, taux observe 2019-2…, taux attendu 2019-2…, SMR 2019-2023, nombre de cas 2019-…, taux observe 2024, SMR 2024

## g0095（1 列）
- 見出し：SMR 2024
- 例1 値：0.0 | 1.5 | 0.0 | 0.0 | 1.0
  - 同じ表の列：institution, indicator, taux observe 2019-2…, taux attendu 2019-2…, SMR 2019-2023, nombre de cas 2019-…, taux observe 2024, taux attendu 2024

## g0096（1 列）
- 見出し：nombre de cas 2024
- 例1 値：8 | 1'332 | 211 | 2 | 285
  - 同じ表の列：institution, indicator, taux observe 2019-2…, taux attendu 2019-2…, SMR 2019-2023, nombre de cas 2019-…, taux observe 2024, taux attendu 2024

## g0097（1 列）
- 見出し：KT
- 例1 値：VD | VD | SG | BE | AG
  - 同じ表の列：Inst, Adr, Ort, AnzStand, KT_Standort, Ort_Standort, LA

## g0098（1 列）
- 見出し：Inst
- 例1 値：Paracelsus­Spital Richterswil AG | Klinik Gais AG Kardiale Rehabilitation,… | EOC Ente ospedaliero cantonale | Reha Rheinfelden | Ostschweizer Kinderspital
  - 同じ表の列：KT, Adr, Ort, AnzStand, KT_Standort, Ort_Standort, LA

## g0099（1 列）
- 見出し：Adr
- 例1 値：Bolligenstrasse 111 | Route de Chêne 26 | Asylstrasse 19 | Frankentalerstrasse 55 | St. Katharinental
  - 同じ表の列：KT, Inst, Ort, AnzStand, KT_Standort, Ort_Standort, LA

## g0100（1 列）
- 見出し：Ort
- 例1 値：4915 St. Urban | 2000 Neuchâtel | 3072 Ostermundigen | 4915 St. Urban | 4500 Solothurn
  - 同じ表の列：KT, Inst, Adr, AnzStand, KT_Standort, Ort_Standort, LA

## g0101（1 列）
- 見出し：AnzStand
- 例1 値：2 | 2 | 5 | 8 | 4
  - 同じ表の列：KT, Inst, Adr, Ort, KT_Standort, Ort_Standort, LA

## g0102（1 列）
- 見出し：KT_Standort
- 例1 値：GE | SG | BE | ZH | BE
  - 同じ表の列：KT, Inst, Adr, Ort, AnzStand, Ort_Standort, LA

## g0103（1 列）
- 見出し：Ort_Standort
- 例1 値：3402 Burgdorf | 4054 Basel | 2107 Couvet | 7212 Seewis Dorf | 4500 Solothurn
  - 同じ表の列：KT, Inst, Adr, Ort, AnzStand, KT_Standort, LA

## g0104（1 列）
- 見出し：LA
- 例1 値：Amb, Stat | Amb, Stat | Amb, Stat | Amb | Amb
  - 同じ表の列：KT, Inst, Adr, Ort, AnzStand, KT_Standort, Ort_Standort

## g0105（4 列）
- 見出し：Year
- 例1 値：2013 | 2013 | 2013 | 2013 | 2013
  - 同じ表の列：Canton, Id Of Animal Catego…, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Experiment Categ…
- 例2 値：2019 | 2022 | 2015 | 2017 | 2023
  - 同じ表の列：Category, Count

## g0106（1 列）
- 見出し：Canton
- 例1 値：FR | VD | VD | VD | VD
  - 同じ表の列：Year, Id Of Animal Catego…, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Experiment Categ…

## g0107（1 列）
- 見出し：Id Of Animal Category
- 例1 値：animal_1 | animal_2 | animal_1 | animal_1 | animal_1
  - 同じ表の列：Year, Canton, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Experiment Categ…

## g0108（1 列）
- 見出し：Genetically Modified
- 例1 値：gm_0 | gm_0 | gm_0 | gm_0 | gm_1
  - 同じ表の列：Year, Canton, Id Of Animal Catego…, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Experiment Categ…

## g0109（1 列）
- 見出し：Degree of severity 0
- 例1 値：10 | 0 | 61 | 0 | 0
  - 同じ表の列：Year, Canton, Id Of Animal Catego…, Genetically Modified, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Experiment Categ…

## g0110（1 列）
- 見出し：Degree of severity 1
- 例1 値：0 | 0 | 6 | 0 | 4
  - 同じ表の列：Year, Canton, Id Of Animal Catego…, Genetically Modified, Degree of severity 0, Degree of severity 2, Degree of severity 3, Id Experiment Categ…

## g0111（1 列）
- 見出し：Degree of severity 2
- 例1 値：7 | 0 | 1267 | 0 | 0
  - 同じ表の列：Year, Canton, Id Of Animal Catego…, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 3, Id Experiment Categ…

## g0112（1 列）
- 見出し：Degree of severity 3
- 例1 値：29 | 0 | 0 | 0 | 0
  - 同じ表の列：Year, Canton, Id Of Animal Catego…, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Id Experiment Categ…

## g0113（1 列）
- 見出し：Id Experiment Category
- 例1 値：experiment_2 | experiment_2 | experiment_1 | experiment_1 | experiment_1
  - 同じ表の列：Year, Canton, Id Of Animal Catego…, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3

## g0114（1 列）
- 見出し：Id Of Disease Category
- 例1 値：disease_14 | disease_3 | disease_14 | disease_3 | disease_14
  - 同じ表の列：Year, Canton, Id Of Animal Catego…, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3

## g0115（1 列）
- 見出し：Titel
- 例1 値：Engineering of axially vascularized hum… | Embryotoxizitäts- und Teratogenitätsstu… | Cartilage resurfacing with fetal cells … | Auswirkung einer Langzeitsedierung mitt… | Beeinflussbarkeit der Sepsis-assoziiert…
  - 同じ表の列：Fachgebiet, Versuchszweck, Tierart, Summe von SG 0, Summe von SG 1, Summe von SG 2, Summe von SG 3

## g0116（1 列）
- 見出し：Fachgebiet
- 例1 値：Oncology | Toxicology | Intensivmedizin | Toxicology | Education
  - 同じ表の列：Titel, Versuchszweck, Tierart, Summe von SG 0, Summe von SG 1, Summe von SG 2, Summe von SG 3

## g0117（1 列）
- 見出し：Versuchszweck
- 例1 値：Anderer Zusammenhang | Recherche biologique fondamentale | Grundlagenforschung | Biological (including medical) studies … | Entdeckung, Entwicklung und Qualitätsko…
  - 同じ表の列：Titel, Fachgebiet, Tierart, Summe von SG 0, Summe von SG 1, Summe von SG 2, Summe von SG 3

## g0118（1 列）
- 見出し：Tierart
- 例1 値：Mice gm /Souris gm | Mice / Souris | Cats / Katze / Chats | Mice / Souris | Rats
  - 同じ表の列：Titel, Fachgebiet, Versuchszweck, Summe von SG 0, Summe von SG 1, Summe von SG 2, Summe von SG 3

## g0119（1 列）
- 見出し：Summe von SG 0
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Titel, Fachgebiet, Versuchszweck, Tierart, Summe von SG 1, Summe von SG 2, Summe von SG 3

## g0120（1 列）
- 見出し：Summe von SG 1
- 例1 値：3 | 307 | 0 | 0 | 44
  - 同じ表の列：Titel, Fachgebiet, Versuchszweck, Tierart, Summe von SG 0, Summe von SG 2, Summe von SG 3

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
