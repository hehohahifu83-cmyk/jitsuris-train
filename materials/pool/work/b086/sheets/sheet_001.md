# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：DESTINATION
- 例1 値：Serco Group plc | Washington | DESTINATION | London | DESTINATION
  - 同じ表の列：PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost 」

## g0002（1 列）
- 見出し：PURPOSE
- 例1 値：Official meeting | PURPOSE | Spring Sunningdale | Official meeting with senior judiciary | Business continuity - Cancellation char…
  - 同じ表の列：DESTINATION, TRAVEL, OTHER (Including Ho…, Total Cost 」

## g0003（1 列）
- 見出し：TRAVEL
- 例1 値：」450.26 | 」3,785.57 | TRAVEL | Type of Hospitality Received | TRAVEL
  - 同じ表の列：DESTINATION, PURPOSE, OTHER (Including Ho…, Total Cost 」

## g0004（1 列）
- 見出し：OTHER (Including Hospitality Given)
- 例1 値：OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given)
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, Total Cost 」

## g0005（1 列）
- 見出し：Total Cost 」
- 例1 値：267.14 | 63 | 14.2 | 1,522.57 | Total Cost 」
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, OTHER (Including Ho…

## g0006（1 列）
- 見出し：Mode of travel
- 例1 値：RAIL | RAIL | HOTEL | AIR | AIR
  - 同じ表の列：Date of departure, Duration of stay, Destination, City of accommodati…, Class of travel, Base Sales includin…

## g0007（1 列）
- 見出し：Date of departure
- 例1 値：04/04/2013 | 15/05/2013 | 22/04/2013 | 10/07/2013 | 28/06/2013
  - 同じ表の列：Mode of travel, Duration of stay, Destination, City of accommodati…, Class of travel, Base Sales includin…

## g0008（1 列）
- 見出し：Duration of stay
- 例1 値：1 | 1 | 2 | 2 | 6
  - 同じ表の列：Mode of travel, Date of departure, Destination, City of accommodati…, Class of travel, Base Sales includin…

## g0009（1 列）
- 見出し：Destination
- 例1 値：Da Vinci | Dublin | Amsterdam | London Heathrow Airport | Dublin
  - 同じ表の列：Mode of travel, Date of departure, Duration of stay, City of accommodati…, Class of travel, Base Sales includin…

## g0010（1 列）
- 見出し：City of accommodation
- 例1 値：BRUSSELS | Shanghai | Cape Town | Helsinki | Beijing
  - 同じ表の列：Mode of travel, Date of departure, Duration of stay, Destination, Class of travel, Base Sales includin…

## g0011（1 列）
- 見出し：Class of travel
- 例1 値：ECONOMY | DISCOUNT ECONOMY | DISCOUNT ECONOMY | DISCOUNT ECONOMY | STANDARD PREMIER
  - 同じ表の列：Mode of travel, Date of departure, Duration of stay, Destination, City of accommodati…, Base Sales includin…

## g0012（1 列）
- 見出し：Base Sales including Tax
- 例1 値：30 | 353.1 | 1357.9 | 219 | 2948.05
  - 同じ表の列：Mode of travel, Date of departure, Duration of stay, Destination, City of accommodati…, Class of travel

## g0013（1 列）
- 見出し：HM Revenue and Customs Senior Officials Travel Report
- 例1 値：Name of Official | Ms J Granger | Mr A Cole | Mr J Harra | Mr J Harra
  - 同じ表の列：1st March 2013 to 3…

## g0014（1 列）
- 見出し：1st March 2013 to 30th June 2013
- 例1 値：Gdansk | Zurich | Los Angeles/San Francisco | Zurich | Moscow
  - 同じ表の列：HM Revenue and Cust…

## g0015（1 列）
- 見出し：Date
- 例1 値：2021-07-08 | 2021-09-21 | 2021-09-06 | 2021-09-28 | 2021-09-06
  - 同じ表の列：Purpose of meeting

## g0016（1 列）
- 見出し：Purpose of meeting
- 例1 値：To discuss the UK Government's proposal… | To discuss the UK Government's cultural… | To discuss prosperity initiatives in NI | To discuss the work of Women in Busines… | To discuss the commissioning of abortio…
  - 同じ表の列：Date

## g0017（1 列）
- 見出し：Date
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Type of Hospitality…

## g0018（1 列）
- 見出し：Type of Hospitality received
- 例1 値：Nil return | Nil return | Nil return | Nil return | Nil return
  - 同じ表の列：Date

## g0019（1 列）
- 見出し：Product Type
- 例1 値：AIR | AIR | AIR | AIR | HOTEL
  - 同じ表の列：Depart Date, Trip Duration (days), Arrival Airport, Hotel City, Class of Service, Base Sales

## g0020（1 列）
- 見出し：Depart Date
- 例1 値：21/07/2013 | 16/07/2013 | 03/09/2013 | 15/09/2013 | 07/08/2013
  - 同じ表の列：Product Type, Trip Duration (days), Arrival Airport, Hotel City, Class of Service, Base Sales

## g0021（1 列）
- 見出し：Trip Duration (days)
- 例1 値：1 | 2 | 2 | 9 | 2
  - 同じ表の列：Product Type, Depart Date, Arrival Airport, Hotel City, Class of Service, Base Sales

## g0022（1 列）
- 見出し：Arrival Airport
- 例1 値：Hanover | Dulles | Da Vinci | London Heathrow Airport | London Heathrow Airport
  - 同じ表の列：Product Type, Depart Date, Trip Duration (days), Hotel City, Class of Service, Base Sales

## g0023（1 列）
- 見出し：Hotel City
- 例1 値：ARLINGTON | Vilnius | NEW YORK | AIX EN PROVENCE | Norfolk
  - 同じ表の列：Product Type, Depart Date, Trip Duration (days), Arrival Airport, Class of Service, Base Sales

## g0024（1 列）
- 見出し：Class of Service
- 例1 値：STANDARD | DISCOUNT ECONOMY | DISCOUNT ECONOMY | DISCOUNT BUSINESS | PREMIUM ECONOMY
  - 同じ表の列：Product Type, Depart Date, Trip Duration (days), Arrival Airport, Hotel City, Base Sales

## g0025（1 列）
- 見出し：Base Sales
- 例1 値：60 | -7265 | 0 | 101 | 3483
  - 同じ表の列：Product Type, Depart Date, Trip Duration (days), Arrival Airport, Hotel City, Class of Service

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
```
