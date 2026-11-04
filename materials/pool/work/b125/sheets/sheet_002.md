# ラベル用シート 002 / 002

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（3 列）
- 見出し：SUBURB
- 例1 値：MCLAREN VALE | SEACOMBE GARDENS | GLANVILLE | UNLEY PARK | CROYDON PARK
  - 同じ表の列：8788_GREEN, 8788_COVER, 8889_GREEN, 8889_COVER, 8990_GREEN, 8990_COVER, 9091_GREEN, 9091_COVER
- 例2 値：ALTONA MEADOWS | SPOTSWOOD | SEABROOK | NEWPORT | ALTONA MEADOWS
  - 同じ表の列：Location

## 答えの雛形

```
g0001	
```
