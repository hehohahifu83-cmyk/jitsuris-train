<!-- b079：10/29 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b079.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0003（1 列）
- 見出し：1999-2000
- 例1 値：1999-2000 | 1999-2000 | 36.13 | 49.49 | 44.73
  - 同じ表の列：Year, 1998-1999, 2000-2001, 2001-2002, 2002-2003, 2003-2004, 2004-2005, 2005-2006

## g0004（1 列）
- 見出し：2000-2001
- 例1 値：43.53 | 44.98 | 45.71 | 37.13 | 41.83
  - 同じ表の列：Year, 1998-1999, 1999-2000, 2001-2002, 2002-2003, 2003-2004, 2004-2005, 2005-2006

## g0006（1 列）
- 見出し：2002-2003
- 例1 値：40.71 | 43.14 | 42.84 | 41.07 | 45.31
  - 同じ表の列：Year, 1998-1999, 1999-2000, 2000-2001, 2001-2002, 2003-2004, 2004-2005, 2005-2006

## g0007（1 列）
- 見出し：2003-2004
- 例1 値：41.47 | 40.65 | 44.08 | 45.07 | 2003-2004
  - 同じ表の列：Year, 1998-1999, 1999-2000, 2000-2001, 2001-2002, 2002-2003, 2004-2005, 2005-2006

## g0008（1 列）
- 見出し：2004-2005
- 例1 値：45.63 | 33.80 | 46.14 | 2004-2005 | 39.86
  - 同じ表の列：Year, 1998-1999, 1999-2000, 2000-2001, 2001-2002, 2002-2003, 2003-2004, 2005-2006

## g0009（1 列）
- 見出し：2005-2006
- 例1 値：44.21 | 37.46 | 47.46 | 38.57 | 43.62
  - 同じ表の列：Year, 1998-1999, 1999-2000, 2000-2001, 2001-2002, 2002-2003, 2003-2004, 2004-2005

## g0015（1 列）
- 見出し：1997-1998
- 例1 値：1.38 | 1.51 | 723 | 0.56 | 12.3
  - 同じ表の列：Year, 1994-1995, 1995-1996, 1996-1997, 1998-1999, 1999-2000, 2000-2001, 2001-2002

## g0020（1 列）
- 見出し：MAP TITLE, STATEMENT OF RESPONSIBILITY
- 例1 値：The River Murray general plan showing l… | The River Murray general plan showing l… | The River Murray general plan showing l… | The River Murray general plan showing l… | The River Murray general plan showing l…
  - 同じ表の列：OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## g0023（1 列）
- 見出し：MAP SCALE
- 例1 値：Scale approximately 1:9,600 | Scale approximately 1:9,600 | Scale approximately 1:9,600 | Scale approximately 1:9,600 | Scale approximately 1:9,600
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## g0024（1 列）
- 見出し：PLACE, PUBLISHER, DATE OF PUBLICATION
- 例1 値：Adelaide : Engineer-in-Chief's Departme… | Adelaide : Engineer-in-Chief's Departme… | Adelaide : Engineer-in-Chief's Departme… | Adelaide : Engineer-in-Chief's Departme… | Adelaide : Engineer-in-Chief's Departme…
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## 答えの雛形

```
g0003	
g0004	
g0006	
g0007	
g0008	
g0009	
g0015	
g0020	
g0023	
g0024	
```
