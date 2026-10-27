# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：list_name
- 例1 値：yk45i75 | yk45i75 | yk45i75 | fz2pa27 | fz2pa27
  - 同じ表の列：name, label

## g0002（1 列）
- 見出し：name
- 例1 値：room_temperatu | elevated_tempe | cryo_temperatu | celsius | kelvin
  - 同じ表の列：list_name, label

## g0003（1 列）
- 見出し：label
- 例1 値：Room Temperature | Elevated Temperature | Cryo Temperature | Celsius | Kelvin
  - 同じ表の列：list_name, name

## 答えの雛形

```
g0001	
g0002	
g0003	
```
