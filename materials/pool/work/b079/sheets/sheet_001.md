# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Year
- 例1 値：ALL DAY | Route 7 (Glenelg to Darlington) | ALL DAY | Outbound Travel Speed (km/h) | Year
  - 同じ表の列：1998-1999, 1999-2000, 2000-2001, 2001-2002, 2002-2003, 2003-2004, 2004-2005, 2005-2006

## g0002（2 列）
- 見出し：1998-1999
- 例1 値：42.84 | 1998-1999 | 47.85 | 42.77 | 42.73
  - 同じ表の列：Year, 1999-2000, 2000-2001, 2001-2002, 2002-2003, 2003-2004, 2004-2005, 2005-2006
- 例2 値：1.25 | 1998-1999 | 1.31 | 11.78 | 1998-1999
  - 同じ表の列：Year, 1994-1995, 1995-1996, 1996-1997, 1997-1998, 1999-2000, 2000-2001, 2001-2002

## g0003（1 列）
- 見出し：1999-2000
- 例1 値：1999-2000 | 1999-2000 | 36.13 | 49.49 | 44.73
  - 同じ表の列：Year, 1998-1999, 2000-2001, 2001-2002, 2002-2003, 2003-2004, 2004-2005, 2005-2006

## g0004（1 列）
- 見出し：2000-2001
- 例1 値：43.53 | 44.98 | 45.71 | 37.13 | 41.83
  - 同じ表の列：Year, 1998-1999, 1999-2000, 2001-2002, 2002-2003, 2003-2004, 2004-2005, 2005-2006

## g0005（1 列）
- 見出し：2001-2002
- 例1 値：32.39 | 40.89 | 2001-2002 | 46.46 | 45.15
  - 同じ表の列：Year, 1998-1999, 1999-2000, 2000-2001, 2002-2003, 2003-2004, 2004-2005, 2005-2006

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

## g0010（1 列）
- 見出し：2006-2007
- 例1 値：45.08 | 31.30 | 35.13 | 29.99 | 2006-2007
  - 同じ表の列：Year, 1998-1999, 1999-2000, 2000-2001, 2001-2002, 2002-2003, 2003-2004, 2004-2005

## g0011（1 列）
- 見出し：Year
- 例1 値：PM PEAK | PM PEAK | ALL DAY | ALL DAY | AM PEAK
  - 同じ表の列：1994-1995, 1995-1996, 1996-1997, 1997-1998, 1998-1999, 1999-2000, 2000-2001, 2001-2002

## g0012（1 列）
- 見出し：1994-1995
- 例1 値：1994-1995 | 44.8 | 1994-1995 | 11.1 | 1.28
  - 同じ表の列：Year, 1995-1996, 1996-1997, 1997-1998, 1998-1999, 1999-2000, 2000-2001, 2001-2002

## g0013（1 列）
- 見出し：1995-1996
- 例1 値：0.38 | 0.47 | 1.27 | 47.2 | 1.39
  - 同じ表の列：Year, 1994-1995, 1996-1997, 1997-1998, 1998-1999, 1999-2000, 2000-2001, 2001-2002

## g0014（1 列）
- 見出し：1996-1997
- 例1 値：13.5 | 1.44 | 1.27 | 15.3 | 41.7
  - 同じ表の列：Year, 1994-1995, 1995-1996, 1997-1998, 1998-1999, 1999-2000, 2000-2001, 2001-2002

## g0015（1 列）
- 見出し：1997-1998
- 例1 値：1.38 | 1.51 | 723 | 0.56 | 12.3
  - 同じ表の列：Year, 1994-1995, 1995-1996, 1996-1997, 1998-1999, 1999-2000, 2000-2001, 2001-2002

## g0016（1 列）
- 見出し：1999-2000
- 例1 値：45.1 | 11.6 | 1.26 | 1999-2000 | 614
  - 同じ表の列：Year, 1994-1995, 1995-1996, 1996-1997, 1997-1998, 1998-1999, 2000-2001, 2001-2002

## g0017（1 列）
- 見出し：2000-2001
- 例1 値：622 | 2000-2001 | 794 | 11.4 | 44.4
  - 同じ表の列：Year, 1994-1995, 1995-1996, 1996-1997, 1997-1998, 1998-1999, 1999-2000, 2001-2002

## g0018（1 列）
- 見出し：2001-2002
- 例1 値：44.4 | 12.59 | 1.26 | 1.2 | 42.4
  - 同じ表の列：Year, 1994-1995, 1995-1996, 1996-1997, 1997-1998, 1998-1999, 1999-2000, 2000-2001

## g0019（1 列）
- 見出し：2002-2003
- 例1 値：39.8 | 1.26 | 2002-2003 | 13.9 | 44.2
  - 同じ表の列：Year, 1994-1995, 1995-1996, 1996-1997, 1997-1998, 1998-1999, 1999-2000, 2000-2001

## g0020（1 列）
- 見出し：MAP TITLE, STATEMENT OF RESPONSIBILITY
- 例1 値：The River Murray general plan showing l… | The River Murray general plan showing l… | The River Murray general plan showing l… | The River Murray general plan showing l… | The River Murray general plan showing l…
  - 同じ表の列：OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## g0021（1 列）
- 見出し：OTHER MAP TITLE
- 例1 値：River Murray general plan : division C,… | River Murray general plan : division I,… | River Murray general plan : division L,… | River Murray general plan : division H,… | River Murray general plan : division E,…
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE_2, MAP SCALE, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## g0022（1 列）
- 見出し：OTHER MAP TITLE_2
- 例1 値：River Murray general plan (S.A.) ; plan… | River Murray general plan (S.A.) ; plan… | River Murray general plan (S.A.) ; plan… | River Murray general plan (S.A.) ; plan… | River Murray general plan (S.A.) ; plan…
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, MAP SCALE, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## g0023（1 列）
- 見出し：MAP SCALE
- 例1 値：Scale approximately 1:9,600 | Scale approximately 1:9,600 | Scale approximately 1:9,600 | Scale approximately 1:9,600 | Scale approximately 1:9,600
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## g0024（1 列）
- 見出し：PLACE, PUBLISHER, DATE OF PUBLICATION
- 例1 値：Adelaide : Engineer-in-Chief's Departme… | Adelaide : Engineer-in-Chief's Departme… | Adelaide : Engineer-in-Chief's Departme… | Adelaide : Engineer-in-Chief's Departme… | Adelaide : Engineer-in-Chief's Departme…
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## g0025（1 列）
- 見出し：PLACE, PRINTER
- 例1 値：Adelaide : A. Vaughan, Government Photo… | Adelaide : A. Vaughan, Government Photo… | Adelaide : A. Vaughan, Government Photo… | Adelaide : A. Vaughan, Government Photo… | Adelaide : A. Vaughan, Government Photo…
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PUBLISHER, D…, FORMAT, SIZE, SERIES TITLE, SERIES INFORMATION

## g0026（1 列）
- 見出し：FORMAT, SIZE
- 例1 値：1 map on 2 sheets ; sheets 64 x 97 cm a… | 1 map on 6 sheets ; sheets 63 x 92 cm o… | 1 map on 3 sheets ; sheets 64 x 91 cm | 1 map on 4 sheets ; sheets 54 x 90 cm o… | 1 map on 3 sheets ; sheets 63 x 90 cm o…
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PUBLISHER, D…, PLACE, PRINTER, SERIES TITLE, SERIES INFORMATION

## g0027（1 列）
- 見出し：SERIES TITLE
- 例1 値：River Murray general plan (S.A.) | River Murray general plan (S.A.) | River Murray general plan (S.A.) | River Murray general plan (S.A.) | River Murray general plan (S.A.)
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES INFORMATION

## g0028（1 列）
- 見出し：SERIES INFORMATION
- 例1 値：This plan is part of a series of River … | This plan is part of a series of River … | This plan is part of a series of River … | This plan is part of a series of River … | This plan is part of a series of River …
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE

## g0029（1 列）
- 見出し：CALL NO.
- 例1 値：zsmp 835 aj 1:9 600 plan no. 13 sheets … | zsmp 835 aj 1:9 600 plan no. 9 sheets 1… | zsmp 835 aj 1:9 600 plan no. 10 sheets … | zsmp 835 aj 1:9 600 plan no. 1 sheets 1… | zsmp 835 aj 1:9 600 plan no. 3 sheets 1…
  - 同じ表の列：MAP TITLE, STATEMEN…, OTHER MAP TITLE, OTHER MAP TITLE_2, MAP SCALE, PLACE, PUBLISHER, D…, PLACE, PRINTER, FORMAT, SIZE, SERIES TITLE

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
```
