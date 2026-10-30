# ラベル用シート 003 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：gemeinde_code
- 例1 値：61 | 3 | 154 | 4 | 136
  - 同じ表の列：gebietstyp_code

## g0242（1 列）
- 見出し：szenario
- 例1 値：Beobachtung | Beobachtung | Beobachtung | Beobachtung | Beobachtung
  - 同じ表の列：region, jahr, staatsan, alter, anzahl

## g0243（1 列）
- 見出し：region
- 例1 値：Glattal | Furttal | Furttal | Glattal | Glattal
  - 同じ表の列：szenario, jahr, staatsan, alter, anzahl

## g0244（1 列）
- 見出し：staatsan
- 例1 値：CH | CH | CH | CH | CH
  - 同じ表の列：szenario, region, jahr, alter, anzahl

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
```
