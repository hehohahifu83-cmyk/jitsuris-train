# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Authorisation Number
- 例1 値：A000092/26 | A000004/26 | A001637/26 | A004895/26 | A003319/26
  - 同じ表の列：Expiry Date, County, Post Code, Financial Instituti…

## g0002（1 列）
- 見出し：Expiry Date
- 例1 値：20270518 | 20261103 | 20270610 | 20261217 | 20270608
  - 同じ表の列：Authorisation Number, County, Post Code, Financial Instituti…

## g0003（1 列）
- 見出し：County
- 例1 値：Co. Carlow | Co.Kildare | Co. Westmeath | Co. Mayo | Kildare
  - 同じ表の列：Authorisation Number, Expiry Date, Post Code, Financial Instituti…

## g0004（1 列）
- 見出し：Post Code
- 例1 値：K67 Px34 | V9421K8 | K67E9K2 | A92 R6Vk | X91 H306
  - 同じ表の列：Authorisation Number, Expiry Date, County, Financial Instituti…

## g0005（1 列）
- 見出し：Financial Institutions
- 例1 値：Allied Irish Banks plc & AIB Leasing Lt… | Bank of Ireland Finance,Close Brothers … | Close Brothers Finance DAC trading as C… | Allied Irish Banks plc & AIB Leasing Lt… | Allied Irish Banks plc & AIB Leasing Lt…
  - 同じ表の列：Authorisation Number, Expiry Date, County, Post Code

## g0006（1 列）
- 見出し：unsafe_
- 例1 値：Eugene F. Collins | i) The payments above exclude VAT | ii) Legal Advisory fees, while paid by … | Home Building Finance Ireland Q4 2021 p… | iii) Some expenditure may be excluded i…
  - 同じ表の列：unsafe__2, unsafe__3

## g0007（2 列）
- 見出し：unsafe__2
- 例1 値：Loan Administration Costs | Description | Facility Professional Fees
  - 同じ表の列：unsafe_, unsafe__3
- 例2 値：Loan Administration Costs | Loan Administration Costs | Loan Administration Costs | Loan Administration Costs | Description
  - 同じ表の列：unsafe_, unsafe__3

## g0008（2 列）
- 見出し：unsafe__3
- 例1 値：33,000.00 | Payment Amount € | 74,527.93
  - 同じ表の列：unsafe_, unsafe__2
- 例2 値：48,837.86 | 39,036.55 | 54,410.42 | Payment Amount € | 51,730.19
  - 同じ表の列：unsafe_, unsafe__2

## g0009（1 列）
- 見出し：unsafe_
- 例1 値：i) The payments above exclude VAT | Fexco Asset Finance UC | Supplier | Fexco Asset Finance UC | Fexco Asset Finance UC
  - 同じ表の列：unsafe__2, unsafe__3

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
```
