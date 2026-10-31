# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Publication of tenders- monthly and cumulative analysis
- 例1 値：DCMS | DEFRA | DfID | DWP | Cabinet Office
  - 同じ表の列：DATA PERIOD: July 2…

## g0002（1 列）
- 見出し：DATA PERIOD: July 2013-September 2013
- 例1 値：Large increase in workload, tenders wer… | Departmental comment | Commerical confidentiality | Tenders not required to be published as… | In preparation: Waiting client/supplier…
  - 同じ表の列：Publication of tend…

## g0003（1 列）
- 見出し：SPEND BY BUDGET TYPE
- 例1 値：Running the estate | Policy and policy implementation | Total Spend | Procurement costs | SPEND BY TYPE OF INTERNAL OPERATION
  - 同じ表の列：TOTAL

## g0004（1 列）
- 見出し：TOTAL
- 例1 値：」millions* | 388.8 | 169 | 26.2 | 133.3
  - 同じ表の列：SPEND BY BUDGET TYPE

## g0005（1 列）
- 見出し：Department
- 例1 値：Senior Salaries Review Board | Boundary Commission for Wales | Buying Solutions | CO | Cabinet Office - Buying Solutions
  - 同じ表の列：Moratorium, Total Value request…, Total Value approve…, Basis for Exception, Date of Update

## g0006（1 列）
- 見出し：Moratorium
- 例1 値：0 | CO - Cabinet Office (Core Depatment) | 0 | 0 | 0
  - 同じ表の列：Department, Total Value request…, Total Value approve…, Basis for Exception, Date of Update

## g0007（1 列）
- 見出し：Total Value requested (」m)
- 例1 値：Sustainable Procurement Training Needs … | 0 | 197,000 | 48,000 | 197,000
  - 同じ表の列：Department, Moratorium, Total Value approve…, Basis for Exception, Date of Update

## g0008（1 列）
- 見出し：Total Value approved (」m)
- 例1 値：」28,750 | Value | 」42,388 | 0 | 0
  - 同じ表の列：Department, Moratorium, Total Value request…, Basis for Exception, Date of Update

## g0009（1 列）
- 見出し：Basis for Exception
- 例1 値：4 | July | September | 0 | September
  - 同じ表の列：Department, Moratorium, Total Value request…, Total Value approve…, Date of Update

## g0010（1 列）
- 見出し：Date of Update
- 例1 値：4 | 0 | HEO/SEO (FTE) | 0 | 0
  - 同じ表の列：Department, Moratorium, Total Value request…, Total Value approve…, Basis for Exception

## g0011（1 列）
- 見出し：Department
- 例1 値：MoD | MoD | MoD | MoD | MoD
  - 同じ表の列：HNG Ref No, Basis for expenditu…, Total Value Approve…, Date of approval

## g0012（1 列）
- 見出し：HNG Ref No
- 例1 値：HMG2952 | HMG2528a | HMG2846 | HMG2981 | HMG2971
  - 同じ表の列：Department, Basis for expenditu…, Total Value Approve…, Date of approval

## g0013（1 列）
- 見出し：Basis for expenditure approval
- 例1 値：MOD have previously completed the launc… | MOD requesting 」129,260k for their care… | The RAF website is being redeveloped in… | There is an on-going need to provide in… | EMPORIUM is expected to develop and del…
  - 同じ表の列：Department, HNG Ref No, Total Value Approve…, Date of approval

## g0014（1 列）
- 見出し：Total Value Approved (」)
- 例1 値：」10,109,144 | 」21,000 | 」23,160,000 | 」30,000 | 」53,400
  - 同じ表の列：Department, HNG Ref No, Basis for expenditu…, Date of approval

## g0015（1 列）
- 見出し：Date of approval
- 例1 値：May-16 | May-16 | Jun-16 | May-16 | May-16
  - 同じ表の列：Department, HNG Ref No, Basis for expenditu…, Total Value Approve…

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
```
