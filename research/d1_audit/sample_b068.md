<!-- b068：10/67 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b068.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0006（1 列）
- 見出し：Total, All Recipients, Thousands of Dollars
- 例1 値：29219249 | 36578 | 641094 | 15844 | 761262
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0007（1 列）
- 見出し：Less than $5,000, Number
- 例1 値：168440 | 250 | 80 | 16710 | 360
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…, $10,000 to $14,999,…

## g0011（1 列）
- 見出し：$10,000 to $14,999, Number
- 例1 値：90 | 13350 | 5110 | 160 | 9270
  - 同じ表の列：Province or Territo…, Total, All Recipien…, Total, All Recipien…, Less than $5,000, N…, Less than $5,000, T…, $5,000 to $9,999, N…, $5,000 to $9,999, T…, $10,000 to $14,999,…

## g0027（1 列）
- 見出し：Collection Time/Duree d'echantillonnage (s)
- 例1 値：78420 | 604800 | 86395 | 86100 | 675900
  - 同じ表の列：Location/Emplacement, Province/Province, Collection Start/De…, AirVolume/Volume d'…, Cs-134 Activity/Cs-…, Cs-134 Uncertainty/…, Cs-136 Activity/Cs-…, Cs-136 Uncertainty/…

## g0034（1 列）
- 見出し：Health Canada ID# / Sante Canada ID#
- 例1 値：44056 | 44059 | 44057 | 44036 | 44058
  - 同じ表の列：Location/Emplacement, Weight/Poids (kg), Collection Date / D…, Count date / date d…, Method/Methode, Counting time/temps…, Cs-137 Activity/ Cs…, Cs-137 Uncertainty …

## g0044（1 列）
- 見出し：PROV
- 例1 値：QC | NB | MB | QC | ON
  - 同じ表の列：EMPGR, AREA, LANG, Q1, O_Q1, Q2, Q2NET, Q3

## g0055（1 列）
- 見出し：STYPE
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：QUEST, LANG, QF, Q1, Q2, Q3A, Q3B, Q4A

## g0056（1 列）
- 見出し：QF
- 例1 値：6 | 6 | 6 | 10 | 5
  - 同じ表の列：QUEST, STYPE, LANG, Q1, Q2, Q3A, Q3B, Q4A

## g0060（1 列）
- 見出し：Q4B
- 例1 値：5 | 7 | 5 | 7 | 7
  - 同じ表の列：QUEST, STYPE, LANG, QF, Q1, Q2, Q3A, Q3B

## g0064（1 列）
- 見出し：question_value_f
- 例1 値：Dans une certaine mesure | Dans une faible mesure | Tous les répondants | Dans une large mesure | Dans une certaine mesure
  - 同じ表の列：dept_f, dept_e, question, question_value_e, shr_w_resp, total_w_resp

## 答えの雛形

```
g0006	
g0007	
g0011	
g0027	
g0034	
g0044	
g0055	
g0056	
g0060	
g0064	
```
