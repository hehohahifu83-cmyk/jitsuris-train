<!-- b077：10/36 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b077.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0005（1 列）
- 見出し：PCT_GDE
- 例1 値：0.20 | 0.04 | 0.15 | 0.03 | 0.20
  - 同じ表の列：TIME_PERIOD, GDENR, RANG_GDE, VALUE, OBS_STATUS

## g0007（1 列）
- 見出し：BETRIEBSTAG
- 例1 値：2026-10-29T00:00:00 | 2026-10-29T00:00:00 | 2026-10-29T00:00:00 | 2026-10-29T00:00:00 | 2026-10-29T00:00:00
  - 同じ表の列：FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT, ZUSATZFAHRT_TF

## g0015（1 列）
- 見出し：ZUSATZFAHRT_TF
- 例1 値：false | false | false | false | false
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT

## g0016（1 列）
- 見出し：FAELLT_AUS_TF
- 例1 値：false | false | false | false | false
  - 同じ表の列：BETRIEBSTAG, FAHRT_BEZEICHNER, BETREIBER_ID, BETREIBER_ABK, PRODUKT_ID, LINIEN_ID, LINIEN_TEXT, VERKEHRSMITTEL_TEXT

## g0018（1 列）
- 見出し：Gebundenheit_Fahrzeug
- 例1 値：ug | ug | sg | sg | sg
  - 同じ表の列：Niederflurigkeit_Fa…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0019（1 列）
- 見出し：sg_Autonomie
- 例1 値：5 | 2 | -1 | 1 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0021（1 列）
- 見出し：sg_Voranmeldung
- 例1 値：2 | 3 | 3 | -1 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_keinZugang, sg_keineInfo, ug_Autonomie, ug_Rampeneinsatz

## g0023（1 列）
- 見出し：sg_keineInfo
- 例1 値：-1 | -1 | 2 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, ug_Autonomie, ug_Rampeneinsatz

## g0025（1 列）
- 見出し：ug_Rampeneinsatz
- 例1 値：-1 | 2 | 2 | -1 | -1
  - 同じ表の列：Niederflurigkeit_Fa…, Gebundenheit_Fahrze…, sg_Autonomie, sg_Rampeneinsatz, sg_Voranmeldung, sg_keinZugang, sg_keineInfo, ug_Autonomie

## g0028（1 列）
- 見出し：Hausnr.
- 例1 値：1 | 1 | 16 | 19 | 2
  - 同じ表の列：ID, PLZ, Gemeinde, Eventplatze, Nutzungsmoglichkeit, Gebiet, Stromanschluss, Nutzungsart

## 答えの雛形

```
g0005	
g0007	
g0015	
g0016	
g0018	
g0019	
g0021	
g0023	
g0025	
g0028	
```
