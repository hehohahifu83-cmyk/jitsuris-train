# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Upper bound
- 例1 値：-0.8 | -0.9 | -0.2 | 0.8 | 0.7
  - 同じ表の列：Frequency

## g0002（1 列）
- 見出し：Frequency
- 例1 値：4 | 0 | 0 | 0 | 1
  - 同じ表の列：Upper bound

## g0003（1 列）
- 見出し：DEPARTMENT
- 例1 値：South East | AO | Northern Ireland | TOTAL | North West
  - 同じ表の列：BIS

## g0004（2 列）
- 見出し：BIS
- 例1 値：108 | 6207 | 0 | 23 | 1082
  - 同じ表の列：DEPARTMENT
- 例2 値：0 | 4 | 0 | 0 | 5
  - 同じ表の列：NMO, UKSA, UKAEA, RPC, UK SBS, CITB, SFA, SLC

## g0005（1 列）
- 見出し：NMO
- 例1 値：7 | 0 | 0 | 0 | 5
  - 同じ表の列：BIS, UKSA, UKAEA, RPC, UK SBS, CITB, SFA, SLC

## g0006（1 列）
- 見出し：UKSA
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：BIS, NMO, UKAEA, RPC, UK SBS, CITB, SFA, SLC

## g0007（1 列）
- 見出し：UKAEA
- 例1 値：4 | 14 | 111 | 62 | 21
  - 同じ表の列：BIS, NMO, UKSA, RPC, UK SBS, CITB, SFA, SLC

## g0008（1 列）
- 見出し：RPC
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：BIS, NMO, UKSA, UKAEA, UK SBS, CITB, SFA, SLC

## g0009（1 列）
- 見出し：UK SBS
- 例1 値：2 | 9 | 24 | 7 | 43
  - 同じ表の列：BIS, NMO, UKSA, UKAEA, RPC, CITB, SFA, SLC

## g0010（1 列）
- 見出し：CITB
- 例1 値：2 | 1 | 8 | 2 | 2
  - 同じ表の列：BIS, NMO, UKSA, UKAEA, RPC, UK SBS, SFA, SLC

## g0011（1 列）
- 見出し：SFA
- 例1 値：3 | 7 | 6 | 3 | 38
  - 同じ表の列：BIS, NMO, UKSA, UKAEA, RPC, UK SBS, CITB, SLC

## g0012（1 列）
- 見出し：SLC
- 例1 値：6 | 0 | 0 | 0 | 6
  - 同じ表の列：BIS, NMO, UKSA, UKAEA, RPC, UK SBS, CITB, SFA

## g0013（1 列）
- 見出し：NERC
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：BIS, NMO, UKSA, UKAEA, RPC, UK SBS, CITB, SFA

## g0014（1 列）
- 見出し：Org code
- 例1 値：00W | 08R | 05L | 14L | 05N
  - 同じ表の列：Number Transitioned, Type 1 Age at Trans…, HbA1c Care Process …, Blood Pressure Care…, Kidney Care Process…, Foot Care Process -…, Retinopathy Care Pr…, Smoking Care Proces…

## g0015（1 列）
- 見出し：Number Transitioned
- 例1 値：30 | 25 | 5 | 5 | 5
  - 同じ表の列：Org code, Type 1 Age at Trans…, HbA1c Care Process …, Blood Pressure Care…, Kidney Care Process…, Foot Care Process -…, Retinopathy Care Pr…, Smoking Care Proces…

## g0016（1 列）
- 見出し：Type 1 Age at Transition
- 例1 値：18 | 17 | 18 | 17 | 17
  - 同じ表の列：Org code, Number Transitioned, HbA1c Care Process …, Blood Pressure Care…, Kidney Care Process…, Foot Care Process -…, Retinopathy Care Pr…, Smoking Care Proces…

## g0017（1 列）
- 見出し：HbA1c Care Process - Type 1
- 例1 値：5 | 5 | 5 | 5 | 5
  - 同じ表の列：Org code, Number Transitioned, Type 1 Age at Trans…, Blood Pressure Care…, Kidney Care Process…, Foot Care Process -…, Retinopathy Care Pr…, Smoking Care Proces…

## g0018（1 列）
- 見出し：Blood Pressure Care Process - Type 1
- 例1 値：5 | 5 | 5 | 10 | 10
  - 同じ表の列：Org code, Number Transitioned, Type 1 Age at Trans…, HbA1c Care Process …, Kidney Care Process…, Foot Care Process -…, Retinopathy Care Pr…, Smoking Care Proces…

## g0019（1 列）
- 見出し：Kidney Care Process - Type 1
- 例1 値：5 | 5 | 5 | 5 | 5
  - 同じ表の列：Org code, Number Transitioned, Type 1 Age at Trans…, HbA1c Care Process …, Blood Pressure Care…, Foot Care Process -…, Retinopathy Care Pr…, Smoking Care Proces…

## g0020（1 列）
- 見出し：Foot Care Process - Type 1
- 例1 値：5 | 10 | 5 | 5 | 40
  - 同じ表の列：Org code, Number Transitioned, Type 1 Age at Trans…, HbA1c Care Process …, Blood Pressure Care…, Kidney Care Process…, Retinopathy Care Pr…, Smoking Care Proces…

## g0021（1 列）
- 見出し：Retinopathy Care Process - Type 1
- 例1 値：5 | 5 | 5 | 10 | Pre - transition
  - 同じ表の列：Org code, Number Transitioned, Type 1 Age at Trans…, HbA1c Care Process …, Blood Pressure Care…, Kidney Care Process…, Foot Care Process -…, Smoking Care Proces…

## g0022（1 列）
- 見出し：Smoking Care Process - Type 1
- 例1 値：5 | 5 | 0 | 5 | 5
  - 同じ表の列：Org code, Number Transitioned, Type 1 Age at Trans…, HbA1c Care Process …, Blood Pressure Care…, Kidney Care Process…, Foot Care Process -…, Retinopathy Care Pr…

## g0023（1 列）
- 見出し：BMI Care Process - Type 1
- 例1 値：25 | 5 | 5 | 15 | 5
  - 同じ表の列：Org code, Number Transitioned, Type 1 Age at Trans…, HbA1c Care Process …, Blood Pressure Care…, Kidney Care Process…, Foot Care Process -…, Retinopathy Care Pr…

## g0024（1 列）
- 見出し：Hospital/ organisation code
- 例1 値：RWEAA | RVJ | RJC02 | RVW | RWA01
  - 同じ表の列：Number of people on…, Number of people wi…, Number of people wi…, Number of people wi…, Care Process Comple…, Care Process Comple…, Target achievement …, Target achievement …

## g0025（1 列）
- 見出し：Number of people on Insulin pump
- 例1 値：290 | 70 | 30 | 135 | 145
  - 同じ表の列：Hospital/ organisat…, Number of people wi…, Number of people wi…, Number of people wi…, Care Process Comple…, Care Process Comple…, Target achievement …, Target achievement …

## g0026（1 列）
- 見出し：Number of people with Type 1 diabetes on an Insulin pump
- 例1 値：50 | 65 | 745 | 5 | 525
  - 同じ表の列：Hospital/ organisat…, Number of people on…, Number of people wi…, Number of people wi…, Care Process Comple…, Care Process Comple…, Target achievement …, Target achievement …

## g0027（1 列）
- 見出し：Number of people with Type 2 and other diabetes on an Insuli
- 例1 値：5 | 0 | 15 | 15 | 0
  - 同じ表の列：Hospital/ organisat…, Number of people on…, Number of people wi…, Number of people wi…, Care Process Comple…, Care Process Comple…, Target achievement …, Target achievement …

## g0028（1 列）
- 見出し：Number of people with Type 1 diabetes (overall not limited b
- 例1 値：495 | 1060 | 830 | 395 | 1165
  - 同じ表の列：Hospital/ organisat…, Number of people on…, Number of people wi…, Number of people wi…, Care Process Comple…, Care Process Comple…, Target achievement …, Target achievement …

## g0029（1 列）
- 見出し：Care Process Completion for those with Type 1 diabetes on an
- 例1 値：98.27586207 | 92.30769231 | 100 | 87.5 | 80
  - 同じ表の列：Hospital/ organisat…, Number of people on…, Number of people wi…, Number of people wi…, Number of people wi…, Care Process Comple…, Target achievement …, Target achievement …

## g0030（1 列）
- 見出し：Care Process Completion for those with Type 1 diabetes not o
- 例1 値：73 | 94.51612903 | 88.77005348 | 78.89908257 | 96.59090909
  - 同じ表の列：Hospital/ organisat…, Number of people on…, Number of people wi…, Number of people wi…, Number of people wi…, Care Process Comple…, Target achievement …, Target achievement …

## g0031（1 列）
- 見出し：Target achievement for those with Type 1 diabetes on an insu
- 例1 値：8.333333333 | 9.259259259 | 6.666666667 | 10.52631579 | 6.818181818
  - 同じ表の列：Hospital/ organisat…, Number of people on…, Number of people wi…, Number of people wi…, Number of people wi…, Care Process Comple…, Care Process Comple…, Target achievement …

## g0032（1 列）
- 見出し：Target achievement for those with Type 1 diabetes not on an
- 例1 値：7.067345341 | 11.11111111 | 10.17699115 | 8.724832215 | 5.063291139
  - 同じ表の列：Hospital/ organisat…, Number of people on…, Number of people wi…, Number of people wi…, Number of people wi…, Care Process Comple…, Care Process Comple…, Target achievement …

## g0033（1 列）
- 見出し：HbA1c values
- 例1 値：64.72972973 | 64.82954344 | 60.10526316 | 66.46666667 | 65.64835165
  - 同じ表の列：Hospital/ organisat…, Number of people on…, Number of people wi…, Number of people wi…, Number of people wi…, Care Process Comple…, Care Process Comple…, Target achievement …

## g0034（1 列）
- 見出し：CCG LHB code
- 例1 値：05T | 05A | 03R | 03T | 02Y
  - 同じ表の列：Year, Practice count, Practices submitted…, Participation (%)

## g0035（1 列）
- 見出し：Year
- 例1 値：2017_18 | 2017_18 | 2017_18 | 2017_18 | 2017_18
  - 同じ表の列：CCG LHB code, Practice count, Practices submitted…, Participation (%)

## g0036（1 列）
- 見出し：Practice count
- 例1 値：31 | 39 | 33 | 56 | 23
  - 同じ表の列：CCG LHB code, Year, Practices submitted…, Participation (%)

## g0037（1 列）
- 見出し：Practices submitted/extracted
- 例1 値：38 | 49 | 23 | 30 | 29
  - 同じ表の列：CCG LHB code, Year, Practice count, Participation (%)

## g0038（1 列）
- 見出し：Participation (%)
- 例1 値：100 | 100 | 100 | 100 | 100
  - 同じ表の列：CCG LHB code, Year, Practice count, Practices submitted…

## g0039（1 列）
- 見出し：MondayOpen
- 例1 値：10:00 | 08:30 | 08:30 | 08:30 | 08:30
  - 同じ表の列：MondayClose, TuesdayOpen, TuesdayClose, WednesdayOpen, WednesdayClose, ThursdayOpen, ThursdayClose, FridayOpen

## g0040（1 列）
- 見出し：MondayClose
- 例1 値：18:00 | 18:00 | 18:00 | 18:00 | 18:00
  - 同じ表の列：MondayOpen, TuesdayOpen, TuesdayClose, WednesdayOpen, WednesdayClose, ThursdayOpen, ThursdayClose, FridayOpen

## g0041（1 列）
- 見出し：TuesdayOpen
- 例1 値：08:30 | 08:30 | 08:30 | 08:30 | 09:30
  - 同じ表の列：MondayOpen, MondayClose, TuesdayClose, WednesdayOpen, WednesdayClose, ThursdayOpen, ThursdayClose, FridayOpen

## g0042（1 列）
- 見出し：TuesdayClose
- 例1 値：18:00 | 18:00 | 17:00 | 17:00 | 18:00
  - 同じ表の列：MondayOpen, MondayClose, TuesdayOpen, WednesdayOpen, WednesdayClose, ThursdayOpen, ThursdayClose, FridayOpen

## g0043（1 列）
- 見出し：WednesdayOpen
- 例1 値：09:00 | closed | 08:30 | 08:30 | 08:30
  - 同じ表の列：MondayOpen, MondayClose, TuesdayOpen, TuesdayClose, WednesdayClose, ThursdayOpen, ThursdayClose, FridayOpen

## g0044（1 列）
- 見出し：WednesdayClose
- 例1 値：17:00 | 17:00 | 18:00 | 18:00 | 18:00
  - 同じ表の列：MondayOpen, MondayClose, TuesdayOpen, TuesdayClose, WednesdayOpen, ThursdayOpen, ThursdayClose, FridayOpen

## g0045（1 列）
- 見出し：ThursdayOpen
- 例1 値：08:30 | 10:00 | 08:30 | 09:30 | 14:00
  - 同じ表の列：MondayOpen, MondayClose, TuesdayOpen, TuesdayClose, WednesdayOpen, WednesdayClose, ThursdayClose, FridayOpen

## g0046（1 列）
- 見出し：ThursdayClose
- 例1 値：20:00 | 17:00 | 20:00 | 17:00 | 17:00
  - 同じ表の列：MondayOpen, MondayClose, TuesdayOpen, TuesdayClose, WednesdayOpen, WednesdayClose, ThursdayOpen, FridayOpen

## g0047（1 列）
- 見出し：FridayOpen
- 例1 値：10:00 | 08:30 | 08:30 | 09:30 | 08:30
  - 同じ表の列：MondayOpen, MondayClose, TuesdayOpen, TuesdayClose, WednesdayOpen, WednesdayClose, ThursdayOpen, ThursdayClose

## g0048（1 列）
- 見出し：FridayClose
- 例1 値：18:00 | 17:00 | 18:00 | 18:00 | 18:00
  - 同じ表の列：MondayOpen, MondayClose, TuesdayOpen, TuesdayClose, WednesdayOpen, WednesdayClose, ThursdayOpen, ThursdayClose

## g0049（1 列）
- 見出し：2018-01-01
- 例1 値：1837 | 2636 | 227 | 155 | 773
  - 同じ表の列：2018-01-08, 2018-01-15, 2018-01-22, 2018-01-29, 2018-02-05, 2018-02-12, 2018-02-19, 2018-02-26

## g0050（1 列）
- 見出し：2018-01-08
- 例1 値：155 | 455 | 363 | 319 | 2096
  - 同じ表の列：2018-01-01, 2018-01-15, 2018-01-22, 2018-01-29, 2018-02-05, 2018-02-12, 2018-02-19, 2018-02-26

## g0051（1 列）
- 見出し：2018-01-15
- 例1 値：1729 | 362 | 208 | 608 | 552
  - 同じ表の列：2018-01-01, 2018-01-08, 2018-01-22, 2018-01-29, 2018-02-05, 2018-02-12, 2018-02-19, 2018-02-26

## g0052（1 列）
- 見出し：2018-01-22
- 例1 値：2172 | 422 | 0 | 199 | 673
  - 同じ表の列：2018-01-01, 2018-01-08, 2018-01-15, 2018-01-29, 2018-02-05, 2018-02-12, 2018-02-19, 2018-02-26

## g0053（1 列）
- 見出し：2018-01-29
- 例1 値：408 | 287 | 1612 | 192 | 242
  - 同じ表の列：2018-01-01, 2018-01-08, 2018-01-15, 2018-01-22, 2018-02-05, 2018-02-12, 2018-02-19, 2018-02-26

## g0054（1 列）
- 見出し：2018-02-05
- 例1 値：1432 | 7 | 626 | 141 | 154
  - 同じ表の列：2018-01-01, 2018-01-08, 2018-01-15, 2018-01-22, 2018-01-29, 2018-02-12, 2018-02-19, 2018-02-26

## g0055（1 列）
- 見出し：2018-02-12
- 例1 値：893 | 118 | 337 | 2669 | 1981
  - 同じ表の列：2018-01-01, 2018-01-08, 2018-01-15, 2018-01-22, 2018-01-29, 2018-02-05, 2018-02-19, 2018-02-26

## g0056（1 列）
- 見出し：2018-02-19
- 例1 値：522 | 2483 | 229 | 170 | 185
  - 同じ表の列：2018-01-01, 2018-01-08, 2018-01-15, 2018-01-22, 2018-01-29, 2018-02-05, 2018-02-12, 2018-02-26

## g0057（1 列）
- 見出し：2018-02-26
- 例1 値：275 | 1162 | 113 | 431 | 151
  - 同じ表の列：2018-01-01, 2018-01-08, 2018-01-15, 2018-01-22, 2018-01-29, 2018-02-05, 2018-02-12, 2018-02-19

## g0058（1 列）
- 見出し：2018-03-05
- 例1 値：187 | 283 | 2753 | 2304 | 266
  - 同じ表の列：2018-01-01, 2018-01-08, 2018-01-15, 2018-01-22, 2018-01-29, 2018-02-05, 2018-02-12, 2018-02-19

## g0059（1 列）
- 見出し：Date
- 例1 値：05/07/2016 | 05/07/2016 | 09/08/2016 | 09/08/2016 | 05/07/2016
  - 同じ表の列：Transect, Quadrat, TQcode, Species, DAFOR (D, A, F, O o…, Shrub cover N (0-5), Shrub cover E (0-5), Shrub cover S (0-5)

## g0060（1 列）
- 見出し：Transect
- 例1 値：1 | 1 | 3 | 1 | 3
  - 同じ表の列：Date, Quadrat, TQcode, Species, DAFOR (D, A, F, O o…, Shrub cover N (0-5), Shrub cover E (0-5), Shrub cover S (0-5)

## g0061（1 列）
- 見出し：Quadrat
- 例1 値：4 | 3 | 1 | 7 | 3
  - 同じ表の列：Date, Transect, TQcode, Species, DAFOR (D, A, F, O o…, Shrub cover N (0-5), Shrub cover E (0-5), Shrub cover S (0-5)

## g0062（1 列）
- 見出し：TQcode
- 例1 値：T1Q1 | T2Q5 | T1Q3 | T1Q6 | T1Q4
  - 同じ表の列：Date, Transect, Quadrat, Species, DAFOR (D, A, F, O o…, Shrub cover N (0-5), Shrub cover E (0-5), Shrub cover S (0-5)

## g0063（1 列）
- 見出し：Species
- 例1 値：Enchanter's nightshade | Wood avens | Wood avens | Bluebell | Bramble
  - 同じ表の列：Date, Transect, Quadrat, TQcode, DAFOR (D, A, F, O o…, Shrub cover N (0-5), Shrub cover E (0-5), Shrub cover S (0-5)

## g0064（1 列）
- 見出し：DAFOR (D, A, F, O or R)
- 例1 値：R | O | R | R | R
  - 同じ表の列：Date, Transect, Quadrat, TQcode, Species, Shrub cover N (0-5), Shrub cover E (0-5), Shrub cover S (0-5)

## g0065（1 列）
- 見出し：Shrub cover N (0-5)
- 例1 値：2 | 2 | 0 | 4 | 5
  - 同じ表の列：Date, Transect, Quadrat, TQcode, Species, DAFOR (D, A, F, O o…, Shrub cover E (0-5), Shrub cover S (0-5)

## g0066（1 列）
- 見出し：Shrub cover E (0-5)
- 例1 値：3 | 3 | 5 | 4 | 5
  - 同じ表の列：Date, Transect, Quadrat, TQcode, Species, DAFOR (D, A, F, O o…, Shrub cover N (0-5), Shrub cover S (0-5)

## g0067（1 列）
- 見出し：Shrub cover S (0-5)
- 例1 値：5 | 1 | 2 | 3 | 3
  - 同じ表の列：Date, Transect, Quadrat, TQcode, Species, DAFOR (D, A, F, O o…, Shrub cover N (0-5), Shrub cover E (0-5)

## g0068（1 列）
- 見出し：Shrub cover W (0-5)
- 例1 値：3 | 3 | 4 | 0 | 4
  - 同じ表の列：Date, Transect, Quadrat, TQcode, Species, DAFOR (D, A, F, O o…, Shrub cover N (0-5), Shrub cover E (0-5)

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
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
g0068	
```
