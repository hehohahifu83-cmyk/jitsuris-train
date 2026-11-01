# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Date
- 例1 値：09/11/2025 | 13/09/2025 - 14/09/2025 | Dates TBC | 23/08/2025 | 26/06/2025
  - 同じ表の列：Event, Department

## g0002（1 列）
- 見出し：Event
- 例1 値：Strength of Spirit Games - the Rehabili… | West End Carnival | City Centre Christmas Lights Switch On | Britains Ocean City Running Festival | Christmas Market
  - 同じ表の列：Date, Department

## g0003（1 列）
- 見出し：Department
- 例1 値：PCCC | CCC | PCC/Live Nation | PCC | PCC/Taurus Events
  - 同じ表の列：Date, Event

## g0004（1 列）
- 見出し：Project Reference
- 例1 値：CF23_24-005 | CF23 24-014 | CF23 24-017 | CF23 24-016 | CF23 24-006
  - 同じ表の列：Ward, Total Pledged by CCF, Number of Supporters, Final Total Raised, Date Project Closed, Swtiched to Forever…

## g0005（1 列）
- 見出し：Ward
- 例1 値：City wide | City Wide | City wide | Sutton and Mount Gold | Chaddlewood
  - 同じ表の列：Project Reference, Total Pledged by CCF, Number of Supporters, Final Total Raised, Date Project Closed, Swtiched to Forever…

## g0006（1 列）
- 見出し：Total Pledged by CCF
- 例1 値：£800.00 | £2,600.00 | £7,500.00 | £5,000.00 | £6,250.00
  - 同じ表の列：Project Reference, Ward, Number of Supporters, Final Total Raised, Date Project Closed, Swtiched to Forever…

## g0007（1 列）
- 見出し：Number of Supporters
- 例1 値：35 | 37 | 38 | 50 | 149
  - 同じ表の列：Project Reference, Ward, Total Pledged by CCF, Final Total Raised, Date Project Closed, Swtiched to Forever…

## g0008（1 列）
- 見出し：Final Total Raised
- 例1 値：£1,666.00 | £16,194.00 | £14,373.00 | £36,699.00 | £11,745.00
  - 同じ表の列：Project Reference, Ward, Total Pledged by CCF, Number of Supporters, Date Project Closed, Swtiched to Forever…

## g0009（1 列）
- 見出し：Date Project Closed
- 例1 値：16/04/2024 | 11/04/2024 | 11/08/2023 | 21/09/2023 | 19/04/2024
  - 同じ表の列：Project Reference, Ward, Total Pledged by CCF, Number of Supporters, Final Total Raised, Swtiched to Forever…

## g0010（1 列）
- 見出し：Swtiched to Forever Funding?
- 例1 値：Yes | No | Yes | No | No
  - 同じ表の列：Project Reference, Ward, Total Pledged by CCF, Number of Supporters, Final Total Raised, Date Project Closed

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
```
