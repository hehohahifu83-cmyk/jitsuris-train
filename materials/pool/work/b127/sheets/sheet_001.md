# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：2012-13
- 例1 値：100 | 0 | 1 | 12.2 | 2.7
  - 同じ表の列：2013-14

## g0002（1 列）
- 見出し：2013-14
- 例1 値：457.2 | 114.8 | 0 | 1.8 | 100
  - 同じ表の列：2012-13

## 答えの雛形

```
g0001	
g0002	
```
