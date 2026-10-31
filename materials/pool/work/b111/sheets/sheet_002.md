# ラベル用シート 002 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（3 列）
- 見出し：INDIKATOR_ID
- 例1 値：613 | 613 | 613 | 613 | 613
  - 同じ表の列：BFS_NR, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG
- 例2 値：612 | 612 | 612 | 612 | 612
  - 同じ表の列：BFS_NR, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG

## g0122（3 列）
- 見出し：INDIKATOR_JAHR
- 例1 値：2009 | 2012 | 2012 | 2007 | 2003
  - 同じ表の列：BFS_NR, INDIKATOR_ID, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG
- 例2 値：2003 | 2017 | 2015 | 2020 | 2003
  - 同じ表の列：BFS_NR, INDIKATOR_ID, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG

## g0123（3 列）
- 見出し：INDIKATOR_VALUE
- 例1 値：0.0 | 0.0 | 0.0 | 0.0 | 0.9
  - 同じ表の列：BFS_NR, INDIKATOR_ID, INDIKATOR_JAHR, EINHEIT_KURZ, EINHEIT_LANG
- 例2 値：26.3 | 0.9 | 0.0 | 0.0 | 4.3
  - 同じ表の列：BFS_NR, INDIKATOR_ID, INDIKATOR_JAHR, EINHEIT_KURZ, EINHEIT_LANG

## g0124（3 列）
- 見出し：EINHEIT_KURZ
- 例1 値：% | % | % | % | %
  - 同じ表の列：BFS_NR, INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_LANG
- 例2 値：% | % | % | % | %
  - 同じ表の列：BFS_NR, INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_LANG

## g0125（3 列）
- 見出し：EINHEIT_LANG
- 例1 値：Prozent | Prozent | Prozent | Prozent | Prozent
  - 同じ表の列：BFS_NR, INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ
- 例2 値：Prozent | Prozent | Prozent | Prozent | Prozent
  - 同じ表の列：BFS_NR, INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
```
