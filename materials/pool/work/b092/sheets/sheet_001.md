# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Main/parent/sponsoring department (where applicable)
- 例1 値：Defra | Welsh Assembly Government | MOD | H M Treasury | Ministry of Justice
  - 同じ表の列：Permanent Payroll s…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…, Total Payroll Staff…

## g0002（1 列）
- 見出し：Permanent Payroll staff FTE (as at 31 March 2010)
- 例1 値：2516 | 37 | . | 66 | 48
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…, Total Payroll Staff…

## g0003（1 列）
- 見出し：Permanent Payroll staff Headcount (as at 31 March 2010)
- 例1 値：170 | 22 | 33 | 53 | 35
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…, Total Payroll Staff…

## g0004（1 列）
- 見出し：Permanent Payroll Staff Cost (£m) (financial year 2009/10)
- 例1 値：7 | 2044 | 0 | 75 | 2
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll s…, Temporary Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…, Total Payroll Staff…

## g0005（1 列）
- 見出し：Temporary Payroll Staff FTE (as at 31 March 2010)
- 例1 値：0 | 21 | 31 | 52 | 0
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…, Total Payroll Staff…

## g0006（1 列）
- 見出し：Temporary Payroll Staff Headcount (as at 31 March 2010)
- 例1 値：. | 14 | 0 | 47 | 0
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…, Total Payroll Staff…

## g0007（1 列）
- 見出し：Temporary Payroll Staff Cost (£m) (financial year 2009/10)
- 例1 値：9 | 2 | 0 | 2 | 0
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…, Total Payroll Staff…

## g0008（1 列）
- 見出し：Total Payroll Staff FTE (as at 31 March 2010)
- 例1 値：854 | 230 | 9 | 98 | 0
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…

## g0009（1 列）
- 見出し：Total Payroll Staff Headcount (as at 31 March 2010)
- 例1 値：221 | 2164 | 624 | 2680 | 247
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…

## g0010（1 列）
- 見出し：Total Payroll Staff Cost (£m) (financial year 2009/10)
- 例1 値：3 | 89 | 3 | 2 | 25
  - 同じ表の列：Main/parent/sponsor…, Permanent Payroll s…, Permanent Payroll s…, Permanent Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Temporary Payroll S…, Total Payroll Staff…

## g0011（1 列）
- 見出し：Section B: Political & Constitutional Reform
- 例1 値：3 Pension schemes report under FRS 17 a… | 5 Total departmental spending is the su… | 4 Expenditure on tangible and intangibl… | -Current grants and subsidies to the pr… | Total Capital DEL
  - 同じ表の列：8,615, 9,047, 9,499, 9,499_2, 6,414, 10,830, 10,993, 9,661

## g0012（1 列）
- 見出し：8,615
- 例1 値：31,593 | 122,671 | 30,142 | 1,228 | 340,291
  - 同じ表の列：Section B: Politica…, 9,047, 9,499, 9,499_2, 6,414, 10,830, 10,993, 9,661

## g0013（1 列）
- 見出し：9,047
- 例1 値：122,105 | - | - | 2007-08 | 17,307
  - 同じ表の列：Section B: Politica…, 8,615, 9,499, 9,499_2, 6,414, 10,830, 10,993, 9,661

## g0014（1 列）
- 見出し：9,499
- 例1 値：143,173 | - | 41,274 | 1,600 | 136,470
  - 同じ表の列：Section B: Politica…, 8,615, 9,047, 9,499_2, 6,414, 10,830, 10,993, 9,661

## g0015（1 列）
- 見出し：9,499_2
- 例1 値：605,938 | - | Outturn | 193,485 | 1
  - 同じ表の列：Section B: Politica…, 8,615, 9,047, 9,499, 6,414, 10,830, 10,993, 9,661

## g0016（1 列）
- 見出し：6,414
- 例1 値：500,423 | - | 75,742 | - | -
  - 同じ表の列：Section B: Politica…, 8,615, 9,047, 9,499, 9,499_2, 10,830, 10,993, 9,661

## g0017（1 列）
- 見出し：10,830
- 例1 値：4,781 | 19,296 | - | - | -
  - 同じ表の列：Section B: Politica…, 8,615, 9,047, 9,499, 9,499_2, 6,414, 10,993, 9,661

## g0018（1 列）
- 見出し：10,993
- 例1 値：3,143 | - | - | 6,876 | 46,877
  - 同じ表の列：Section B: Politica…, 8,615, 9,047, 9,499, 9,499_2, 6,414, 10,830, 9,661

## g0019（1 列）
- 見出し：9,661
- 例1 値：34,500 | - | - | - | 313,125
  - 同じ表の列：Section B: Politica…, 8,615, 9,047, 9,499, 9,499_2, 6,414, 10,830, 10,993

## g0020（1 列）
- 見出し：92,396
- 例1 値：52,734 | -544 | 123,820 | 496,228 | -
  - 同じ表の列：Section B: Politica…, 8,615, 9,047, 9,499, 9,499_2, 6,414, 10,830, 10,993

## g0021（1 列）
- 見出し：NY09
- 例1 値：BD09 | BD09 | BD11 | NY11 | NY09
  - 同じ表の列：6%

## g0022（1 列）
- 見出し：6%
- 例1 値：7.60% | 23 | 7 | 20 | 7.40%
  - 同じ表の列：NY09

## g0023（1 列）
- 見出し：Core Training delivered in-house between April 11 and March
- 例1 値：Leadership and Management Part 2 - G6/7 | Performance Appraisal for New Managers … | Leadership and Management Part 1 - G6/7 | Total | * fewer than 10 staff showing
  - 同じ表の列：Total number who at…, Grade, Gender, Ethnic Origin, Disability, Sexual Orientation, Religion or Belief, Working Pattern

## g0024（1 列）
- 見出し：Total number who attended the courses
- 例1 値：29 | 210 | 14 | 129 | 38
  - 同じ表の列：Core Training deliv…, Grade, Gender, Ethnic Origin, Disability, Sexual Orientation, Religion or Belief, Working Pattern

## g0025（1 列）
- 見出し：Grade
- 例1 値：* | * | * | AA/AO/EA | *
  - 同じ表の列：Core Training deliv…, Total number who at…, Gender, Ethnic Origin, Disability, Sexual Orientation, Religion or Belief, Working Pattern

## g0026（1 列）
- 見出し：Gender
- 例1 値：10 | 54 | 64 | * | Male
  - 同じ表の列：Core Training deliv…, Total number who at…, Grade, Ethnic Origin, Disability, Sexual Orientation, Religion or Belief, Working Pattern

## g0027（1 列）
- 見出し：Ethnic Origin
- 例1 値：14 | White | * | 15 | 73
  - 同じ表の列：Core Training deliv…, Total number who at…, Grade, Gender, Disability, Sexual Orientation, Religion or Belief, Working Pattern

## g0028（1 列）
- 見出し：Disability
- 例1 値：Disabled | 11 | * | 11 | *
  - 同じ表の列：Core Training deliv…, Total number who at…, Grade, Gender, Ethnic Origin, Sexual Orientation, Religion or Belief, Working Pattern

## g0029（1 列）
- 見出し：Sexual Orientation
- 例1 値：* | 15 | 136 | 15 | 106
  - 同じ表の列：Core Training deliv…, Total number who at…, Grade, Gender, Ethnic Origin, Disability, Religion or Belief, Working Pattern

## g0030（1 列）
- 見出し：Religion or Belief
- 例1 値：Declared | 15 | 11 | 14 | 140
  - 同じ表の列：Core Training deliv…, Total number who at…, Grade, Gender, Ethnic Origin, Disability, Sexual Orientation, Working Pattern

## g0031（1 列）
- 見出し：Working Pattern
- 例1 値：Full-time | 16 | 11 | 18 | 142
  - 同じ表の列：Core Training deliv…, Total number who at…, Grade, Gender, Ethnic Origin, Disability, Sexual Orientation, Religion or Belief

## g0032（1 列）
- 見出し：Age Band
- 例1 値：14 | 14 | 25 and under | * | *
  - 同じ表の列：Core Training deliv…, Total number who at…, Grade, Gender, Ethnic Origin, Disability, Sexual Orientation, Religion or Belief

## g0033（1 列）
- 見出し：Total Grants
- 例1 値：of which: UN agencies | Guaranteed Export Credits | Direct Investment | Total flows as a percentage of GNI | Regional development banks
  - 同じ表の列：5 002, 4 973, 5 214, 5 207, 5 427, 5 408

## g0034（1 列）
- 見出し：5 002
- 例1 値：.. | 0 | .. | 5 416 | 371
  - 同じ表の列：Total Grants, 4 973, 5 214, 5 207, 5 427, 5 408

## g0035（1 列）
- 見出し：4 973
- 例1 値：106 | 8 440 | 0.57 | 5 191 | 217
  - 同じ表の列：Total Grants, 5 002, 5 214, 5 207, 5 427, 5 408

## g0036（1 列）
- 見出し：5 214
- 例1 値：440 | 1 412 | 1 514 | 698 | 239
  - 同じ表の列：Total Grants, 5 002, 4 973, 5 207, 5 427, 5 408

## g0037（1 列）
- 見出し：5 207
- 例1 値：0 | 1 184 | 20 228 | - 25 | - 37
  - 同じ表の列：Total Grants, 5 002, 4 973, 5 214, 5 427, 5 408

## g0038（1 列）
- 見出し：5 427
- 例1 値：1 421 | 1 169 | 40 | 1 885 | 6 486
  - 同じ表の列：Total Grants, 5 002, 4 973, 5 214, 5 207, 5 408

## g0039（1 列）
- 見出し：5 408
- 例1 値：442 | 1 169 | 8 788 | 0.56 | 40 044
  - 同じ表の列：Total Grants, 5 002, 4 973, 5 214, 5 207, 5 427

## g0040（1 列）
- 見出し：2007/08
- 例1 値：247 683 | 6 027 115 | 262 731 | 296 940 | 1 990 184
  - 同じ表の列：2008/09, 2009/10, 2010/11, 2011/12 1

## g0041（1 列）
- 見出し：2008/09
- 例1 値：2 277 358 | 573 652 | 3 283 996 | 1 407 901 | 310 659
  - 同じ表の列：2007/08, 2009/10, 2010/11, 2011/12 1

## g0042（1 列）
- 見出し：2009/10
- 例1 値：252 101 | 1 424 089 | 7 766 602 | 3 958 263 | 2 748 766
  - 同じ表の列：2007/08, 2008/09, 2010/11, 2011/12 1

## g0043（1 列）
- 見出し：2010/11
- 例1 値：4 248 018 | 5 311 859 | 3 221 673 | 219 457 | 417 317
  - 同じ表の列：2007/08, 2008/09, 2009/10, 2011/12 1

## g0044（1 列）
- 見出し：2011/12 1
- 例1 値：434 462 | 4 204 114 | 3 257 724 | 7 682 191 | 633 102
  - 同じ表の列：2007/08, 2008/09, 2009/10, 2010/11

## g0045（1 列）
- 見出し：Nov-18
- 例1 値：Dushanbe | Seoul | Sarajevo | Monrovia | Oslo
  - 同じ表の列：Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0046（1 列）
- 見出し：Arrest/Detention > Assault
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0047（1 列）
- 見出し：Arrest/Detention > Assault with Weapon
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0048（1 列）
- 見出し：Arrest/Detention > Child Pornography
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0049（1 列）
- 見出し：Arrest/Detention > Child Sex
- 例1 値：0 | 0 | <=5 | 0 | 0
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0050（1 列）
- 見出し：Arrest/Detention > Drugs
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0051（1 列）
- 見出し：Arrest/Detention > Fraud
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0052（1 列）
- 見出し：Arrest/Detention > General
- 例1 値：0 | <=5 | 0 | 0 | 0
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0053（1 列）
- 見出し：Arrest/Detention > Immigration
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

## g0054（1 列）
- 見出し：Arrest/Detention > Modern Slavery / Human Trafficking
- 例1 値：0 | 0 | 0 | 0 | 7
  - 同じ表の列：Nov-18, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …, Arrest/Detention > …

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
g0053	
g0054	
```
