# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：TIME_PERIOD
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：GDENR, RANG_GDE, VALUE, PCT_GDE, OBS_STATUS

## g0002（1 列）
- 見出し：GDENR
- 例1 値：2 | 2 | 2 | 2 | 1
  - 同じ表の列：TIME_PERIOD, RANG_GDE, VALUE, PCT_GDE, OBS_STATUS

## g0003（1 列）
- 見出し：RANG_GDE
- 例1 値：432 | 163 | 250 | 328 | 250
  - 同じ表の列：TIME_PERIOD, GDENR, VALUE, PCT_GDE, OBS_STATUS

## g0004（1 列）
- 見出し：VALUE
- 例1 値：5 | 6 | 3 | 4 | 7
  - 同じ表の列：TIME_PERIOD, GDENR, RANG_GDE, PCT_GDE, OBS_STATUS

## g0005（1 列）
- 見出し：PCT_GDE
- 例1 値：0.20 | 0.04 | 0.15 | 0.03 | 0.20
  - 同じ表の列：TIME_PERIOD, GDENR, RANG_GDE, VALUE, OBS_STATUS

## g0006（1 列）
- 見出し：OBS_STATUS
- 例1 値：A | A | A | A | A
  - 同じ表の列：TIME_PERIOD, GDENR, RANG_GDE, VALUE, PCT_GDE

## g0007（1 列）
- 見出し：BETRIEBSTAG
- 例1 値：2026-10-29T00:00:00 | 2026-10-29T00:00:00 | 2026-10-29T00:00:00 | 2026-10-29T00:00:00 | 2026-10-29T00:00:00
  - 同じ表の列：FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT, ZUSATZFAHRT_TF

## g0008（1 列）
- 見出し：FAHRT_BEZEICHNER
- 例1 値：80:07____:63553:000 | 80:07____:57632:000 | 80:07____:57632:000 | 80:07____:57632:000 | 80:07____:57644:000
  - 同じ表の列：BETRIEBSTAG, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT, ZUSATZFAHRT_TF

## g0009（1 列）
- 見出し：BETREIBER_ID
- 例1 値：80:07____ | 80:07____ | 80:07____ | 80:07____ | 80:07____
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT, ZUSATZFAHRT_TF

## g0010（1 列）
- 見出し：BETREIBER_ABK
- 例1 値：DB | DB | DB | DB | DB
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT, ZUSATZFAHRT_TF

## g0011（1 列）
- 見出し：PRODUKT_ID
- 例1 値：Zug | Zug | Zug | Zug | Zug
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT, ZUSATZFAHRT_TF

## g0012（1 列）
- 見出し：LINIEN_ID
- 例1 値：63550 | 63558 | 63559 | 63551 | 57649
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT, ZUSATZFAHRT_TF

## g0013（1 列）
- 見出し：LINIEN_TEXT
- 例1 値：RERE7 | RERE7 | RERE7 | RERE75 | RB
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, VERKEHRSMITTEL_TEXT, ZUSATZFAHRT_TF

## g0014（1 列）
- 見出し：VERKEHRSMITTEL_TEXT
- 例1 値：RE | RE | RE | RE | RE
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, ZUSATZFAHRT_TF

## g0015（1 列）
- 見出し：ZUSATZFAHRT_TF
- 例1 値：false | false | false | false | false
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT

## g0016（1 列）
- 見出し：FAELLT_AUS_TF
- 例1 値：false | false | false | false | false
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT

## g0017（1 列）
- 見出し：Niederflurigkeit_Fahrzeug
- 例1 値：% 5 = nicht barrierefrei | ja | % -1 = kein Wert verfügbar (ungültige A… | % Legende BfR-Statust | nein_HL
  - 同じ表の列：Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0018（1 列）
- 見出し：Gebundenheit_Fahrzeug
- 例1 値：ug | ug | sg | sg | sg
  - 同じ表の列：Niederflurigkeit_Fa…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0019（1 列）
- 見出し：sg_Autonomie
- 例1 値：5 | 2 | -1 | 1 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0020（1 列）
- 見出し：sg_Rampeneinsatz
- 例1 値：-1 | -1 | 2 | 2 | 5
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0021（1 列）
- 見出し：sg_Voranmeldung
- 例1 値：2 | 3 | 3 | -1 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_keinZugang, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0022（1 列）
- 見出し：sg_keinZugang
- 例1 値：-1 | -1 | 5 | 2 | 5
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0023（1 列）
- 見出し：sg_keineInfo
- 例1 値：-1 | -1 | 2 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, ug_Autonomie, ug_Rampeneinsatz

## g0024（1 列）
- 見出し：ug_Autonomie
- 例1 値：-1 | 5 | 2 | -1 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Rampeneinsatz

## g0025（1 列）
- 見出し：ug_Rampeneinsatz
- 例1 値：-1 | 2 | 2 | -1 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie

## g0026（1 列）
- 見出し：ug_Voranmeldung
- 例1 値：2 | -1 | 5 | -1 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie

## g0027（1 列）
- 見出し：ID
- 例1 値：11792 | 11836 | 11776 | 11763 | 11841
  - 同じ表の列：Hausnr., PLZ, Gemeinde, Eventplatze, Nutzungsmoglichkeit, Gebiet, Stromanschluss, Nutzungsart

## g0028（1 列）
- 見出し：Hausnr.
- 例1 値：1 | 1 | 16 | 19 | 2
  - 同じ表の列：ID, PLZ, Gemeinde, Eventplatze, Nutzungsmoglichkeit, Gebiet, Stromanschluss, Nutzungsart

## g0029（1 列）
- 見出し：PLZ
- 例1 値：9000 | 9000 | 9000 | 9000 | 9000
  - 同じ表の列：ID, Hausnr., Gemeinde, Eventplatze, Nutzungsmoglichkeit, Gebiet, Stromanschluss, Nutzungsart

## g0030（1 列）
- 見出し：Gemeinde
- 例1 値：St. Gallen | St. Gallen | St. Gallen | St. Gallen | St. Gallen
  - 同じ表の列：ID, Hausnr., PLZ, Eventplatze, Nutzungsmoglichkeit, Gebiet, Stromanschluss, Nutzungsart

## g0031（1 列）
- 見出し：Eventplatze
- 例1 値：Optiker Ryser | Bohl / Coop City | Blumenmarkt | Grüningerplatz | Industrie- und Handelskammer Vorplatz
  - 同じ表の列：ID, Hausnr., PLZ, Gemeinde, Nutzungsmoglichkeit, Gebiet, Stromanschluss, Nutzungsart

## g0032（1 列）
- 見出し：Nutzungsmoglichkeit
- 例1 値：Standaktionen,Kleinere Anlässe | Standaktionen | Standaktionen | Standaktionen,Kleinere Anlässe | Standaktionen,Kleinere Anlässe,Grosse A…
  - 同じ表の列：ID, Hausnr., PLZ, Gemeinde, Eventplatze, Gebiet, Stromanschluss, Nutzungsart

## g0033（1 列）
- 見出し：Gebiet
- 例1 値：Mittlere Altstadt | Mittlere Altstadt | Bahnhof, Neumarkt, Stadtlounge | Mittlere Altstadt | Marktplatz, Bohl
  - 同じ表の列：ID, Hausnr., PLZ, Gemeinde, Eventplatze, Nutzungsmoglichkeit, Stromanschluss, Nutzungsart

## g0034（1 列）
- 見出し：Stromanschluss
- 例1 値：Strom nicht vorhanden | Strom vorhanden | Strom vorhanden | Strom nicht vorhanden | Strom vorhanden
  - 同じ表の列：ID, Hausnr., PLZ, Gemeinde, Eventplatze, Nutzungsmoglichkeit, Gebiet, Nutzungsart

## g0035（1 列）
- 見出し：Nutzungsart
- 例1 値：Nicht kommerzielle Nutzung | Nicht kommerzielle Nutzung | Nicht kommerzielle Nutzung | Nicht kommerzielle Nutzung | Kommerzielle Nutzung,Nicht kommerzielle…
  - 同じ表の列：ID, Hausnr., PLZ, Gemeinde, Eventplatze, Nutzungsmoglichkeit, Gebiet, Stromanschluss

## g0036（1 列）
- 見出し：Gewichtsbeschrankung
- 例1 値：keine | keine | keine | keine | 16 Tonnen
  - 同じ表の列：ID, Hausnr., PLZ, Gemeinde, Eventplatze, Nutzungsmoglichkeit, Gebiet, Stromanschluss

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
```
