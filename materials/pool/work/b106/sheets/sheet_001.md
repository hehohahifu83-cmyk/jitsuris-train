# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Tool Ref
- 例1 値：HMG1890 | HMG2073 | HMG1909 | HMG1832 | HMG2042
  - 同じ表の列：Department, Basis for expenditu…, Total Value request…, Total Value Approve…, Date of approval

## g0002（1 列）
- 見出し：Department
- 例1 値：MoD | MoD | MoD | MoD | MoD
  - 同じ表の列：Tool Ref, Basis for expenditu…, Total Value request…, Total Value Approve…, Date of approval

## g0003（1 列）
- 見出し：Basis for expenditure approval
- 例1 値：On 2 Nov 11, the Government published a… | R-Cloud is an online marketplace for Sc… | MoD are seeking approval at FBC stage l… | CDE sources innovative technologies via… | A new Portal is required to address the…
  - 同じ表の列：Tool Ref, Department, Total Value request…, Total Value Approve…, Date of approval

## g0004（1 列）
- 見出し：Total Value requested (£)
- 例1 値：£550,000 | £7,820,000 | £109,000 | £4,500,000 | £423,000
  - 同じ表の列：Tool Ref, Department, Basis for expenditu…, Total Value Approve…, Date of approval

## g0005（1 列）
- 見出し：Total Value Approved (£)
- 例1 値：£677,000 | £110,000 | £7,820,000 | £150,000 | £3,320,000
  - 同じ表の列：Tool Ref, Department, Basis for expenditu…, Total Value request…, Date of approval

## g0006（1 列）
- 見出し：Date of approval
- 例1 値：23/02/2015 | 31/03/2015 | 04/03/2015 | 17/02/2015 | 17/03/2015
  - 同じ表の列：Tool Ref, Department, Basis for expenditu…, Total Value request…, Total Value Approve…

## g0007（1 列）
- 見出し：AUDIT_YEAR
- 例1 値：2020_21 | 2020_21 | 2020_21 | 2020_21 | 2020_21
  - 同じ表の列：org_level, org_code, category, breakdown, numerator, denominator, percentage

## g0008（1 列）
- 見出し：org_level
- 例1 値：CCG/LHB | CCG/LHB | CCG/LHB | CCG/LHB | CCG/LHB
  - 同じ表の列：AUDIT_YEAR, org_code, category, breakdown, numerator, denominator, percentage

## g0009（1 列）
- 見出し：org_code
- 例1 値：00T | 00X | 00R | 00V | 00N
  - 同じ表の列：AUDIT_YEAR, org_level, category, breakdown, numerator, denominator, percentage

## g0010（1 列）
- 見出し：category
- 例1 値：HbA1c <= 58 mmol/mol by Age band | Diabetes duration | Care processes | Smoking status | Diabetes duration
  - 同じ表の列：AUDIT_YEAR, org_level, org_code, breakdown, numerator, denominator, percentage

## g0011（1 列）
- 見出し：breakdown
- 例1 値：albumin measured | Severely obese | 5 - least deprived | HbA1c value unknown | Flash
  - 同じ表の列：AUDIT_YEAR, org_level, org_code, category, numerator, denominator, percentage

## g0012（1 列）
- 見出し：numerator
- 例1 値：100 | 535 | 310 | 85 | 160
  - 同じ表の列：AUDIT_YEAR, org_level, org_code, category, breakdown, denominator, percentage

## g0013（1 列）
- 見出し：denominator
- 例1 値：695 | 710 | 710 | 1505 | 5
  - 同じ表の列：AUDIT_YEAR, org_level, org_code, category, breakdown, numerator, percentage

## g0014（1 列）
- 見出し：percentage
- 例1 値：0.735294118 | 4.983388704 | 28.57142857 | 8.823529412 | 37.5
  - 同じ表の列：AUDIT_YEAR, org_level, org_code, category, breakdown, numerator, denominator

## g0015（1 列）
- 見出し：CCG LHB code
- 例1 値：07Y | 99M | 03M | 07P | 02N
  - 同じ表の列：Year, Practice count, Practices submitted…, Participation (%)

## g0016（1 列）
- 見出し：Year
- 例1 値：2016_17 | 2016_17 | 2016_17 | 2016_17 | 2016_17
  - 同じ表の列：CCG LHB code, Practice count, Practices submitted…, Participation (%)

## g0017（1 列）
- 見出し：Practice count
- 例1 値：33 | 56 | 48 | 26 | 21
  - 同じ表の列：CCG LHB code, Year, Practices submitted…, Participation (%)

## g0018（1 列）
- 見出し：Practices submitted/extracted
- 例1 値：21 | 23 | 22 | 20 | 12
  - 同じ表の列：CCG LHB code, Year, Practice count, Participation (%)

## g0019（1 列）
- 見出し：Participation (%)
- 例1 値：81.63265306 | 80.95238095 | 100 | 100 | 100
  - 同じ表の列：CCG LHB code, Year, Practice count, Practices submitted…

## g0020（1 列）
- 見出し：Delayed transfers of care per 100,000 people - Plymouth
- 例1 値：5.6 | 11.5 | 6.9 | 11 | 11.3
  - 同じ表の列：Minimum all english…, Average for all eng…, Maximum for all eng…

## g0021（1 列）
- 見出し：Minimum all english unitary authorities
- 例1 値：0.9 | 2.3 | 0.8 | 2.3 | 0.7
  - 同じ表の列：Delayed transfers o…, Average for all eng…, Maximum for all eng…

## g0022（1 列）
- 見出し：Average for all english unitary authorities
- 例1 値：6.4 | 8.8 | 12.1 | 13.7 | 5.3
  - 同じ表の列：Delayed transfers o…, Minimum all english…, Maximum for all eng…

## g0023（1 列）
- 見出し：Maximum for all english unitary authorities
- 例1 値：19.1 | 25.3 | 37.5 | 23.1 | 36.7
  - 同じ表の列：Delayed transfers o…, Minimum all english…, Average for all eng…

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
```
