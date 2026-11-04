# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：STATISTIC
- 例1 値：VSA87 | VSA87 | VSA87 | VSA87 | VSA87
  - 同じ表の列：Statistic, TLIST(A1), Year, C02199V02655, Sex of Infant, C01935V02367, Period of Gestation, UNIT

## g0002（1 列）
- 見出し：Statistic
- 例1 値：Births Registered | Births Registered | Births Registered | Births Registered | Births Registered
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02199V02655, Sex of Infant, C01935V02367, Period of Gestation, UNIT

## g0003（3 列）
- 見出し：TLIST(A1)
- 例1 値：2016 | 2009 | 2010 | 2014 | 2013
  - 同じ表の列：STATISTIC, Statistic, Year, C02199V02655, Sex of Infant, C01935V02367, Period of Gestation, UNIT
- 例2 値：2000 | 1999 | 2001 | 2002 | 2001
  - 同じ表の列：STATISTIC, Statistic, Year, C02514V03045, UNIT, VALUE

## g0004（3 列）
- 見出し：Year
- 例1 値：2011 | 2017 | 2012 | 2017 | 2012
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), C02199V02655, Sex of Infant, C01935V02367, Period of Gestation, UNIT
- 例2 値：2002 | 2002 | 1998 | 1999 | 1999
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), C02514V03045, UNIT, VALUE

## g0005（1 列）
- 見出し：C02199V02655
- 例1 値：- | 2 | 1 | - | 1
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, Sex of Infant, C01935V02367, Period of Gestation, UNIT

## g0006（1 列）
- 見出し：Sex of Infant
- 例1 値：Female | Both sexes | Both sexes | Both sexes | Male
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, C01935V02367, Period of Gestation, UNIT

## g0007（1 列）
- 見出し：C01935V02367
- 例1 値：14 | 3 | 11 | 3 | 4
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex of Infant, Period of Gestation, UNIT

## g0008（1 列）
- 見出し：Period of Gestation
- 例1 値：32-35 weeks | 36-39 weeks | All gestation periods | Under 28 weeks | Under 28 weeks
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex of Infant, C01935V02367, UNIT

## g0009（3 列）
- 見出し：UNIT
- 例1 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex of Infant, C01935V02367, Period of Gestation
- 例2 値：Number | Number | Number | Number | Number
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02514V03045, VALUE

## g0010（3 列）
- 見出し：VALUE
- 例1 値：617 | 263 | 15436 | 75554 | 15538
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex of Infant, C01935V02367, Period of Gestation
- 例2 値：117 | 21 | 24 | 68 | 49
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02514V03045, UNIT

## g0011（2 列）
- 見出し：STATISTIC
- 例1 値：VSA11C01 | VSA11C01 | VSA11C01 | VSA11C01 | VSA11C01
  - 同じ表の列：Statistic, TLIST(A1), Year, C02514V03045, UNIT, VALUE
- 例2 値：VSA10C01 | VSA10C01 | VSA10C01 | VSA10C01 | VSA10C01
  - 同じ表の列：Statistic, TLIST(A1), Year, C02512V03041, UNIT, VALUE

## g0012（2 列）
- 見出し：Statistic
- 例1 値：Rank of Name in Ireland | Rank of Name in Ireland | Rank of Name in Ireland | Rank of Name in Ireland | Rank of Name in Ireland
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02514V03045, UNIT, VALUE
- 例2 値：Rank of Name in Ireland | Rank of Name in Ireland | Rank of Name in Ireland | Rank of Name in Ireland | Rank of Name in Ireland
  - 同じ表の列：STATISTIC, TLIST(A1), Year, C02512V03041, UNIT, VALUE

## g0013（1 列）
- 見出し：C02514V03045
- 例1 値：165 | 13 | 98 | 110 | 340
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, UNIT, VALUE

## g0014（1 列）
- 見出し：C02512V03041
- 例1 値：220 | 19 | 94 | 2475 | 175
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, UNIT, VALUE

## g0015（1 列）
- 見出し：GIS ID
- 例1 値：38 | 35 | 36 | 15 | 34
  - 同じ表の列：DCC Ref, Artwork, Artist's Dates, Date of Work, Type, Medium, Dimensions, Inscription

## g0016（1 列）
- 見出し：DCC Ref
- 例1 値：DPA27.06 | DPA27.07 | DPA27.02 | DPA27.01 | DPA45
  - 同じ表の列：GIS ID, Artwork, Artist's Dates, Date of Work, Type, Medium, Dimensions, Inscription

## g0017（1 列）
- 見出し：Artwork
- 例1 値：Seán Russell Memorial | Another Sphere | Éire | Sentinel | Bernardo O'Higgins
  - 同じ表の列：GIS ID, DCC Ref, Artist's Dates, Date of Work, Type, Medium, Dimensions, Inscription

## g0018（1 列）
- 見出し：Artist's Dates
- 例1 値：1876-1943 | 1932-1994 | b.1943 b. 1956 | b.1943 b. 1956 | b. 1940
  - 同じ表の列：GIS ID, DCC Ref, Artwork, Date of Work, Type, Medium, Dimensions, Inscription

## g0019（1 列）
- 見出し：Date of Work
- 例1 値：1996.0 | 2009.0 | 1988.0 | 1983.0 | 1985.0
  - 同じ表の列：GIS ID, DCC Ref, Artwork, Artist's Dates, Type, Medium, Dimensions, Inscription

## g0020（1 列）
- 見出し：Type
- 例1 値：sculpture | sculpture | sculpture | sculpture | sculpture
  - 同じ表の列：GIS ID, DCC Ref, Artwork, Artist's Dates, Date of Work, Medium, Dimensions, Inscription

## g0021（1 列）
- 見出し：Medium
- 例1 値：bronze | stainless steel | metal | bronze, gas, glass, granite, steel | bronze
  - 同じ表の列：GIS ID, DCC Ref, Artwork, Artist's Dates, Date of Work, Type, Dimensions, Inscription

## g0022（1 列）
- 見出し：Dimensions
- 例1 値：100 x 230 x 80cm | 35 x 60cm | base of sculpture: 110 x 75cm | 35 x 60cm | 350cm tall
  - 同じ表の列：GIS ID, DCC Ref, Artwork, Artist's Dates, Date of Work, Type, Medium, Inscription

## g0023（1 列）
- 見出し：Inscription
- 例1 値：yes | yes | yes | yes | no
  - 同じ表の列：GIS ID, DCC Ref, Artwork, Artist's Dates, Date of Work, Type, Medium, Dimensions

## g0024（1 列）
- 見出し：Signed
- 例1 値：no | no | no | no | yes, outside of back right chair leg
  - 同じ表の列：GIS ID, DCC Ref, Artwork, Artist's Dates, Date of Work, Type, Medium, Dimensions

## g0025（1 列）
- 見出し：BC_Ref
- 例1 値：CN1216/12 | CN1068/13 | CN1449/12 | CN1797/12 | CN1048/12
  - 同じ表の列：Application_Type, App_Date, Decision, LAT, LONG

## g0026（1 列）
- 見出し：Application_Type
- 例1 値：Commencement Notice | 7 Day Notice | Commencement Notice | Commencement Notice | 7 Day Notice
  - 同じ表の列：BC_Ref, App_Date, Decision, LAT, LONG

## g0027（1 列）
- 見出し：App_Date
- 例1 値：20130114 | 20130125 | 20120404 | 20130130 | 20130116
  - 同じ表の列：BC_Ref, Application_Type, Decision, LAT, LONG

## g0028（1 列）
- 見出し：Decision
- 例1 値：Registered (CN's Only) | Registered (CN's Only) | Registered (CN's Only) | Registered (CN's Only) | Registered (CN's Only)
  - 同じ表の列：BC_Ref, Application_Type, App_Date, LAT, LONG

## g0029（1 列）
- 見出し：LAT
- 例1 値：-6.2750270199 | -6.2042808085 | -6.2661538165 | -6.2827662228 | -6.2096048922
  - 同じ表の列：BC_Ref, Application_Type, App_Date, Decision, LONG

## g0031（1 列）
- 見出し：Current Cert Expiry Date
- 例1 値：2016-09-30T00:00:00 | 2013-08-19T00:00:00 | 2013-11-05T00:00:00 | 2013-12-18T00:00:00 | 2014-02-04T00:00:00
  - 同じ表の列：Title, Organisation

## g0032（1 列）
- 見出し：Title
- 例1 値：Mrs. | Mr. | Mr | Mr. | Mr.
  - 同じ表の列：Current Cert Expiry…, Organisation

## g0033（1 列）
- 見出し：Organisation
- 例1 値：Coyle Cleaners | VIP Cleaners | Fatima Community Launderette Ltd | Marlowe Cleaners (Red Group Internation… | Excel Dry Cleaners
  - 同じ表の列：Current Cert Expiry…, Title

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
g0031	
g0032	
g0033	
```
