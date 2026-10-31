# ラベル用シート 002 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：bilanz_view_nr
- 例1 値：4 | 4 | 2 | 1 | 1
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view, grouping

## g0122（1 列）
- 見出し：bilanz_view
- 例1 値：Umzug | Zuzug | Wanderungssaldo | Zuzug | Wanderungssaldo
  - 同じ表の列：jahr, geom_code, stadtkreis_bfs_nr, stadtkreis, quartier_bfs_nr, quartier, bilanz_view_nr, grouping

## 答えの雛形

```
g0121	
g0122	
```
