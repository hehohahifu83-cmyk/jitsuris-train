# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Count
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Department, Classification, PB13 Entry, PB Reform, Regulatory Function, Website, Chair, Chair's Remuneratio…

## g0002（1 列）
- 見出し：Department
- 例1 値：Department for Culture, Media and Sport | Ministry of Defence | Home Office | Department for Culture, Media and Sport | Department for Culture, Media and Sport
  - 同じ表の列：Count, Classification, PB13 Entry, PB Reform, Regulatory Function, Website, Chair, Chair's Remuneratio…

## g0003（1 列）
- 見出し：Classification
- 例1 値：Advisory NDPB | Advisory NDPB | Advisory NDPB | Advisory NDPB | Executive NDPB
  - 同じ表の列：Count, Department, PB13 Entry, PB Reform, Regulatory Function, Website, Chair, Chair's Remuneratio…

## g0004（1 列）
- 見出し：PB13 Entry
- 例1 値：FULL | FULL | FULL | FULL | FULL
  - 同じ表の列：Count, Department, Classification, PB Reform, Regulatory Function, Website, Chair, Chair's Remuneratio…

## g0005（1 列）
- 見出し：PB Reform
- 例1 値：Retain | Retain | Retain | Retain | Retain
  - 同じ表の列：Count, Department, Classification, PB13 Entry, Regulatory Function, Website, Chair, Chair's Remuneratio…

## g0006（1 列）
- 見出し：Regulatory Function
- 例1 値：No | Yes | No | Yes | No
  - 同じ表の列：Count, Department, Classification, PB13 Entry, PB Reform, Website, Chair, Chair's Remuneratio…

## g0007（1 列）
- 見出し：Website
- 例1 値：http://www.kew.org/about-kew/index.htm | http://www.justice.gov.uk/about/probati… | http://bcomm-wales.gov.uk | http://www.npia.police.uk/ | http://ccs.cabinetoffice.gov.uk/
  - 同じ表の列：Count, Department, Classification, PB13 Entry, PB Reform, Regulatory Function, Chair, Chair's Remuneratio…

## g0008（1 列）
- 見出し：Chair
- 例1 値：Elizabeth France | - | Sir David Normington GCB | CEO | Charlie Mayfield
  - 同じ表の列：Count, Department, Classification, PB13 Entry, PB Reform, Regulatory Function, Website, Chair's Remuneratio…

## g0009（1 列）
- 見出し：Chair's Remuneration (p.a. unless otherwise stated)
- 例1 値：£750 per day | £20,000 | £71,430 | £60,000-£65,000 | £25,000-£30,000
  - 同じ表の列：Count, Department, Classification, PB13 Entry, PB Reform, Regulatory Function, Website, Chair

## g0010（1 列）
- 見出し：Chief Executive / Secretary
- 例1 値：Paul Broadbent | Diane Lees | Jonathan Solly | Tim Moss | Prof Les Ebdon
  - 同じ表の列：Count, Department, Classification, PB13 Entry, PB Reform, Regulatory Function, Website, Chair

## g0011（1 列）
- 見出し：Arts
- 例1 値：ICT | Criminal justice | Youth & community services | Nursery school | Children's education
  - 同じ表の列：1

## g0012（1 列）
- 見出し：1
- 例1 値：6 | 1 | 10 | 3 | 31
  - 同じ表の列：Arts

## g0013（1 列）
- 見出し：Public Services Network Programme
- 例1 値：CO | 30/01/2015 | 1.05 | 1.05 | The Public Services Network is creating…
  - 同じ表の列：National Cyber Secu…, National Citizen Se…, Electoral Registrat…, G-Cloud Programme (…

## g0014（1 列）
- 見出し：National Cyber Security Programme
- 例1 値：CO | 01/04/2011 | 01/04/2015 | 650 | Amber
  - 同じ表の列：Public Services Net…, National Citizen Se…, Electoral Registrat…, G-Cloud Programme (…

## g0015（1 列）
- 見出し：National Citizen Service
- 例1 値：01/10/2011 | National Citizen Service (NCS) is a fla… | 31/12/2014 | The programme is currently delivered in… | CO
  - 同じ表の列：Public Services Net…, National Cyber Secu…, Electoral Registrat…, G-Cloud Programme (…

## g0016（1 列）
- 見出し：Electoral Registration Transformation Programme
- 例1 値：The Programme has been reset for the im… | 01/01/2016 | The Electoral Registration Transformati… | 218.227 | 5.9
  - 同じ表の列：Public Services Net…, National Cyber Secu…, National Citizen Se…, G-Cloud Programme (…

## g0017（1 列）
- 見出し：G-Cloud Programme (covers Data Centre Consolidation and Appl
- 例1 値：CO | Implementing the Government Cloud, Clou… | 0.58 | 31/10/2011 | The Programme has delivered a viable Cl…
  - 同じ表の列：Public Services Net…, National Cyber Secu…, National Citizen Se…, Electoral Registrat…

## g0018（1 列）
- 見出し：Resource PFI
- 例1 値：0 | 9.3 | 0 | 12.2 | 0
  - 同じ表の列：Resource DEL, Capital DEL, Total Departmental …

## g0019（1 列）
- 見出し：Resource DEL
- 例1 値：39.637 | 25.226 | 45.567 | 49.928999999999995 | 16.019999999999996
  - 同じ表の列：Resource PFI, Capital DEL, Total Departmental …

## g0020（1 列）
- 見出し：Capital DEL
- 例1 値：13.087 | 0.301 | 42.96900000000001 | 0 | 284.174
  - 同じ表の列：Resource PFI, Resource DEL, Total Departmental …

## g0021（1 列）
- 見出し：Total Departmental Expentidure Limit
- 例1 値：46.480000000000004 | 15 | 387.728 | 118.133 | 45.567
  - 同じ表の列：Resource PFI, Resource DEL, Capital DEL

## g0022（1 列）
- 見出し：Post Date
- 例1 値：13/04/2011 | 19/04/2011 | 05/04/2011 | 26/04/2011 | 26/04/2011
  - 同じ表の列：Amount, Reference Number

## g0023（1 列）
- 見出し：Amount
- 例1 値：£960.00 | £11,431.06 | £19,633.65 | £570.84 | £1,182.00
  - 同じ表の列：Post Date, Reference Number

## g0024（1 列）
- 見出し：Reference Number
- 例1 値：7.40853E+22 | 7.4929E+22 | 7.48305E+22 | 7.46786E+22 | 7.46786E+22
  - 同じ表の列：Post Date, Amount

## g0025（1 列）
- 見出し：Department
- 例1 値：DFID | DFID | DFID | DFID | DFID
  - 同じ表の列：Entity, Transaction Date, Amount Published, Expense Type Publis…, Expense Area Publis…

## g0026（1 列）
- 見出し：Entity
- 例1 値：DFID | DFID | DFID | DFID | DFID
  - 同じ表の列：Department, Transaction Date, Amount Published, Expense Type Publis…, Expense Area Publis…

## g0027（1 列）
- 見出し：Transaction Date
- 例1 値：16/04/2012 | 26/04/2012 | 30/04/2012 | 30/04/2012 | 16/04/2012
  - 同じ表の列：Department, Entity, Amount Published, Expense Type Publis…, Expense Area Publis…

## g0028（1 列）
- 見出し：Amount Published
- 例1 値：£38,512 | £1,199 | £4,953 | £594 | £2,712
  - 同じ表の列：Department, Entity, Transaction Date, Expense Type Publis…, Expense Area Publis…

## g0029（1 列）
- 見出し：Expense Type Published
- 例1 値：Hotels - Accommodation only | Secure staff accommodation | Other shared service charges | Technical and Advisory Services | Aid Programme - Humanitarian Material R…
  - 同じ表の列：Department, Entity, Transaction Date, Amount Published, Expense Area Publis…

## g0030（1 列）
- 見出し：Expense Area Published
- 例1 値：Human Resources,Security & Facilities D… | Asia, Caribbean and Overseas Territories | East and Central Africa | Research and Evidence Division | International Finance Division
  - 同じ表の列：Department, Entity, Transaction Date, Amount Published, Expense Type Publis…

## g0031（1 列）
- 見出し：SPENDING
- 例1 値：Financial Indicators | of which Capital DEL | Purchase of goods and services within R… | Net Book Value [% variance of Actual v … | Total Annually Managed Expenditure (AME)
  - 同じ表の列：PEOPLE

## g0032（1 列）
- 見出し：PEOPLE
- 例1 値：Whole Department Family - Workforce Size | Contingent Labour [Total full-time equi… | Workforce Diversity [Senior Civil Serva… | Workforce Diversity [Total %] | Theme scores (%)
  - 同じ表の列：SPENDING

## g0033（2 列）
- 見出し：Organisation type
- 例1 値：Ministerial Department | Executive Non-Departmental Public Body | Executive Non-Departmental Public Body
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…
- 例2 値：Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Ministerial Department
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0034（2 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Northern Ireland Office | Northern Ireland Office | Northern Ireland Office
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…
- 例2 値：Northern Ireland Office | Northern Ireland Office | Northern Ireland Office
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0035（2 列）
- 見出し：Payroll staff
- 例1 値：1 | Headcount | AO/AA | 9 | 1
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…
- 例2 値：AO/AA | Headcount | 1 | 9
  - 同じ表の列：Organisation type, Main, parent or spo…, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0036（2 列）
- 見出し：Number of non-payroll staff (contingent labour and consultan
- 例1 値：Agency staff (clerical/admin) | Headcount | 1
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…
- 例2 値：Agency staff (clerical/admin) | Headcount | 1 | 1
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0037（2 列）
- 見出し：Grand Total (workforce numbers)
- 例1 値：168 | 15 | Headcount | 8
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…
- 例2 値：6 | 167 | Headcount | 15
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0038（2 列）
- 見出し：Payroll staff costs
- 例1 値：Salary | £66,072.32 | £29,969.96 | £697,099.17
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…, Comments (NB: These…
- 例2 値：£51,101.32 | £792,050.12 | £16,978.58 | Salary
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…

## g0039（2 列）
- 見出し：Non-Payroll staff (contingent labour/consultancy) costs
- 例1 値：Total monthly cost of contingent labour… | £5,167.16
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…, Comments (NB: These…
- 例2 値：£2,294.47 | £2,312.35 | Total monthly cost of contingent labour…
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Grand Total paybill…

## g0040（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：£992,875.55 | £41,142.50 | £97,266.89
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Comments (NB: These…

## g0041（1 列）
- 見出し：Comments (NB: These will be published alongside your row of
- 例1 値：Commissioners excluded. | Dedicated Mechanism | Commissioners excluded.
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…, Grand Total paybill…

## g0042（1 列）
- 見出し：Grand Total paybill/staffing (payroll and non-payroll) costs
- 例1 値：£73,137.90 | £1,028,458.64 | £25,799.71
  - 同じ表の列：Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs, Non-Payroll staff (…

## g0043（1 列）
- 見出し：Budget
- 例1 値：Notes: (1) For more information on time… | Accuracy of Cash Forecasting ( +/-, %) | Total Annually Managed Expenditure (AME) | of which Capital DEL | Payroll within Resource DEL
  - 同じ表の列：£million, Common Areas of Spe…, Q4 2010-11, 2010-11, Input Indicators, Current, Previous, Current_2

## g0044（1 列）
- 見出し：£million
- 例1 値：2 | 4,130 | 9,687 | 2010-11 Outturn | 2,460
  - 同じ表の列：Budget, Common Areas of Spe…, Q4 2010-11, 2010-11, Input Indicators, Current, Previous, Current_2

## g0045（1 列）
- 見出し：Common Areas of Spend
- 例1 値：Voluntary and community sector (VCS)/Sm… | Corporate Service Cost | Project E Queen Elizabeth Class Aircraf… | Project D Type 45 Destroyer (£million) | Project C Astute Submarine (£million)
  - 同じ表の列：Budget, £million, Q4 2010-11, 2010-11, Input Indicators, Current, Previous, Current_2

## g0046（1 列）
- 見出し：Q4 2010-11
- 例1 値：.. Q2 2011-12 | .. Q2 2011-12 | .. Q2 2011-12 | 8.17 | 4,476
  - 同じ表の列：Budget, £million, Common Areas of Spe…, 2010-11, Input Indicators, Current, Previous, Current_2

## g0047（1 列）
- 見出し：2010-11
- 例1 値：94.1 | 6,700 | 4,476 | 84.6 | 812
  - 同じ表の列：Budget, £million, Common Areas of Spe…, Q4 2010-11, Input Indicators, Current, Previous, Current_2

## g0048（1 列）
- 見出し：Input Indicators
- 例1 値：9 Percentage of Service personnel (Offi… | 7b Percentage of non-front line costs v… | 7 Percentage of Service personnel that … | 4 Average percentage by which the cost … | 6 Cost / Benefit ratio of the major cha…
  - 同じ表の列：Budget, £million, Common Areas of Spe…, Q4 2010-11, 2010-11, Current, Previous, Current_2

## g0049（1 列）
- 見出し：Current
- 例1 値：.. Q3 2011-12 | 92 | 25/14/15 | Current | .. Q2 2011-12
  - 同じ表の列：Budget, £million, Common Areas of Spe…, Q4 2010-11, 2010-11, Input Indicators, Previous, Current_2

## g0050（1 列）
- 見出し：Previous
- 例1 値：. | 28 | . | . | 0.15%
  - 同じ表の列：Budget, £million, Common Areas of Spe…, Q4 2010-11, 2010-11, Input Indicators, Current, Current_2

## g0051（1 列）
- 見出し：Current_2
- 例1 値：. | 25 | 9,350 | 8 | 270
  - 同じ表の列：Budget, £million, Common Areas of Spe…, Q4 2010-11, 2010-11, Input Indicators, Current, Previous

## g0052（1 列）
- 見出し：Previous_2
- 例1 値：78 | 16,690 | 9,510 | 63,620 | 25
  - 同じ表の列：Budget, £million, Common Areas of Spe…, Q4 2010-11, 2010-11, Input Indicators, Current, Previous

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
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
```
