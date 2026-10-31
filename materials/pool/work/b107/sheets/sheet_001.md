# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Type
- 例1 値：Guest of Government | Guest of Government | Guest of Government | Guest of Government | State Visit
  - 同じ表の列：Date, Country, Accomodation, Transportation, Interpretation, Hospitality, Total

## g0002（1 列）
- 見出し：Date
- 例1 値：11 - 12 December 2014 | 16 - 18 June 2014 | 8-10 February 2015 | 8 - 11 April 2014 | 4 - 6 December 2014
  - 同じ表の列：Type, Country, Accomodation, Transportation, Interpretation, Hospitality, Total

## g0003（1 列）
- 見出し：Country
- 例1 値：Germany | Pakistan | Egypt | Germany | Ireland
  - 同じ表の列：Type, Date, Accomodation, Transportation, Interpretation, Hospitality, Total

## g0004（1 列）
- 見出し：Accomodation
- 例1 値：N/A | 22900.33 | 3126.1 | 63971.99 | N/A
  - 同じ表の列：Type, Date, Country, Transportation, Interpretation, Hospitality, Total

## g0005（1 列）
- 見出し：Transportation
- 例1 値：1740.04 | 5390.45 | 1927.67 | 3970.48 | 50921.17
  - 同じ表の列：Type, Date, Country, Accomodation, Interpretation, Hospitality, Total

## g0006（1 列）
- 見出し：Interpretation
- 例1 値：N/A | 4002.9 | N/A | N/A | N/A
  - 同じ表の列：Type, Date, Country, Accomodation, Transportation, Hospitality, Total

## g0007（1 列）
- 見出し：Hospitality
- 例1 値：N/A | N/A | N/A | N/A | 43463.76
  - 同じ表の列：Type, Date, Country, Accomodation, Transportation, Interpretation, Total

## g0008（1 列）
- 見出し：Total
- 例1 値：29073.94 | 5530.74 | 158356.92 | 24791.68 | 3020.67
  - 同じ表の列：Type, Date, Country, Accomodation, Transportation, Interpretation, Hospitality

## g0009（1 列）
- 見出し：Serial number of Parking Charge
- 例1 値：PL11136686 | PL11132379 | PL11133382 | PL20129579 | PL21130868
  - 同じ表の列：Current progression…, Parking Offence dat…, Status of Parking F…, Current balance, Issue event, Type of Parking Off…, Parking Offence Col…

## g0010（1 列）
- 見出し：Current progression of Parking Fine
- 例1 値：0200 - F - PRE NTO - PAID IN FULL | 0200 - F - PRE NTO - PAID IN FULL | 0200 - F - PRE NTO - PAID IN FULL | 0544 - F - CANCELLED - GENERAL REASON | 8591 - F - WRITTEN OFF OUTSTANDING MONI…
  - 同じ表の列：Serial number of Pa…, Parking Offence dat…, Status of Parking F…, Current balance, Issue event, Type of Parking Off…, Parking Offence Col…

## g0011（1 列）
- 見出し：Parking Offence date & time
- 例1 値：12/07/2013 19:26 | 15/04/2013 14:48 | 19/07/2013 11:04 | 08/07/2013 13:04 | 04/06/2013 13:57
  - 同じ表の列：Serial number of Pa…, Current progression…, Status of Parking F…, Current balance, Issue event, Type of Parking Off…, Parking Offence Col…

## g0012（1 列）
- 見出し：Status of Parking Fine
- 例1 値：Closed | Closed | Closed | Closed | Closed
  - 同じ表の列：Serial number of Pa…, Current progression…, Parking Offence dat…, Current balance, Issue event, Type of Parking Off…, Parking Offence Col…

## g0013（1 列）
- 見出し：Current balance
- 例1 値：£0.00 | £0.00 | £0.00 | £0.00 | £0.00
  - 同じ表の列：Serial number of Pa…, Current progression…, Parking Offence dat…, Status of Parking F…, Issue event, Type of Parking Off…, Parking Offence Col…

## g0014（1 列）
- 見出し：Issue event
- 例1 値：ATV | ATV | ATV | ATV | ATV
  - 同じ表の列：Serial number of Pa…, Current progression…, Parking Offence dat…, Status of Parking F…, Current balance, Type of Parking Off…, Parking Offence Col…

## g0015（1 列）
- 見出し：Type of Parking Offence
- 例1 値：83 No Valid P&D Ticket | 82 Ticket Expired | 12 No Residents Permit | 06 No Ticket | 12 No Residents Permit
  - 同じ表の列：Serial number of Pa…, Current progression…, Parking Offence dat…, Status of Parking F…, Current balance, Issue event, Parking Offence Col…

## g0016（1 列）
- 見出し：Parking Offence Colour
- 例1 値：Silver | Blue | Silver | White | Silver
  - 同じ表の列：Serial number of Pa…, Current progression…, Parking Offence dat…, Status of Parking F…, Current balance, Issue event, Type of Parking Off…

## g0017（1 列）
- 見出し：Cars or Vans per household composition in Plymouth 2011
- 例1 値：Other household types | One family only: Lone parent household | Household Composition | One person household: Aged 65 and over | All categories: Household composition
  - 同じ表の列：All categories: Car…, No cars or vans in …, 1 car or van in hou…, 2 or more cars or v…

## g0018（1 列）
- 見出し：All categories: Car or van availability
- 例1 値：20,318 | 19,518 | 34,317 | 13,403 | 6,172
  - 同じ表の列：Cars or Vans per ho…, No cars or vans in …, 1 car or van in hou…, 2 or more cars or v…

## g0019（1 列）
- 見出し：No cars or vans in household
- 例1 値：30,438 | 3,818 | 17,774 | 4,529 | 4,317
  - 同じ表の列：Cars or Vans per ho…, All categories: Car…, 1 car or van in hou…, 2 or more cars or v…

## g0020（1 列）
- 見出し：1 car or van in household
- 例1 値：49,904 | 4,625 | 15,415 | 9,925 | 19,816
  - 同じ表の列：Cars or Vans per ho…, All categories: Car…, No cars or vans in …, 2 or more cars or v…

## g0021（1 列）
- 見出し：2 or more cars or vans in household
- 例1 値：9,407 | 4,113 | 197 | 4,755 | 931
  - 同じ表の列：Cars or Vans per ho…, All categories: Car…, No cars or vans in …, 1 car or van in hou…

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
```
