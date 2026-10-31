<!-- b066：24/236 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b066.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0004（1 列）
- 見出し：DESTINATION
- 例1 値：Sunningdale | Rome | London | Sunningdale | London
  - 同じ表の列：PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost 」

## g0011（1 列）
- 見出し：TRAVEL
- 例1 値：Type of Hospitality Received | Reception | Air | Air | 120.30
  - 同じ表の列：DESTINATION, PURPOSE, OTHER (Including Ho…, Total Cost 」

## g0013（1 列）
- 見出し：Total Cost 」
- 例1 値：0.00 | 48.38 | Total Cost 」 | 46.58 | 0.00
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, OTHER (Including Ho…

## g0038（1 列）
- 見出し：Engineering
- 例1 値：Gas Industry | Signmaking | MES Plumbing | Glass Industry Occupations | Laboratory Technicians
  - 同じ表の列：10, 20, 10_2, -

## g0043（1 列）
- 見出し：RespondentID
- 例1 値：2158452114 | 1927668614 | 1994086335 | 1918374918 | 1931648267
  - 同じ表の列：CollectorID, StartDate, EndDate, Which of the follow…, Which of the follow…, Which geographical …, Is education, learn…, Do you provide any …

## g0052（1 列）
- 見出し：Which of the following people does your organisation target
- 例1 値：1. People with learning difficulties | 1. People with learning difficulties | 1. People with learning difficulties | 1. People with learning difficulties | 1. People with learning difficulties
  - 同じ表の列：RespondentID, CollectorID, StartDate, EndDate, Which of the follow…, Which of the follow…, Which geographical …, Is education, learn…

## g0056（1 列）
- 見出し：Control
- 例1 値：Monitor | Monitor | Control | Monitor | Monitor
  - 同じ表の列：Owning Dept/ALB Dep…, Value (£) (excludin…, Approval date

## g0068（1 列）
- 見出し：DESTINATION
- 例1 値：- | London Office | London Office | London Office | London Office
  - 同じ表の列：DATES, PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost £

## g0083（1 列）
- 見出し：Class of travel
- 例1 値：Standard | Standard | Standard | Standard | Standard
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Accomodation/Meals, Other (including ho…, Cost of travel, Total cost, includi…

## g0089（2 列）
- 見出し：Main department
- 例1 値：Department for Transport | Department for Transport | Department for Transport | Department for Transport | Department for Transport
  - 同じ表の列：Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…
- 例2 値：Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence
  - 同じ表の列：Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…, Comments

## g0094（1 列）
- 見出し：In-year: Number of staff in delegated grades receiving an in
- 例1 値：0 | 0 | 653 | 0 | 0
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…

## g0109（1 列）
- 見出し：Child Custody
- 例1 値：0 | 0 | 0 | 0 | <=5
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access

## g0113（1 列）
- 見出し：Payroll staff AO/AA Headcount
- 例1 値：144 | 18 | 34 | 748
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0118（1 列）
- 見出し：Payroll staff Other, unknown or unspecified Headcount
- 例1 値：5 | 0 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…

## g0126（1 列）
- 見出し：Programme Printing
- 例1 値：」0.00 | 」0.00 | 」0.00 | 」870.00 | 」0.00
  - 同じ表の列：Date, Country, Position Held, Accommodation, Transport (incl air…, Venue/production, Hospitality, Staff costs

## g0128（1 列）
- 見出し：Hospitality
- 例1 値：」1,220.89 | 」0.00 | 」0.00 | 」0.00 | 」0.00
  - 同じ表の列：Date, Country, Position Held, Accommodation, Transport (incl air…, Programme Printing, Venue/production, Staff costs

## g0148（1 列）
- 見出し：OTHER (Including Hospitality Given)
- 例1 値：OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | £47.48 | £210.58 | £144.70
  - 同じ表の列：DATES, DESTINATION, PURPOSE, TRAVEL, Total Cost £

## g0153（1 列）
- 見出し：Exceptions for period 01 November 2010 to 30 September 2011
- 例1 値：Advertising and marketing | Moratorium | Advertising and marketing
  - 同じ表の列：Advertising & Marke…

## g0155（1 列）
- 見出し：Exceptions for period 01 November 2010 to 30 September 2011
- 例1 値：UK Border Agency | Equality and Human Rights Commission | Crime & Policing Group | National Police Improvement Agency | Finance & Commercial/CPG
  - 同じ表の列：Consultancy

## g0168（1 列）
- 見出し：Information for SCS on non-standard contracts
- 例1 値：27 | Number of SCS on non-standard contracts…
  - 同じ表の列：Main department, Organisation, Delegated grades on…, SCS on standard con…, Comments

## g0195（1 列）
- 見出し：Effective data
- 例1 値：19/20 | 21/22 | 22/23 | 23/24 | 20/21
  - 同じ表の列：Pay Multiple

## g0200（1 列）
- 見出し：EffectiveDate
- 例1 値：18/11/2016 | 18/11/2016 | 18/11/2016 | 18/11/2016 | 18/11/2016
  - 同じ表の列：OrganisationLabel, OrganisationURI, UPRN, UniqueAssetIdentity, PostTown, CoordinateReference…, GeoX, GeoY

## g0203（1 列）
- 見出し：CoordinateReferenceSystem
- 例1 値：OSGB36 | OSGB36 | OSGB36 | OSGB36 | OSGB36
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, UPRN, UniqueAssetIdentity, PostTown, GeoX, GeoY

## g0234（1 列）
- 見出し：Payroll staff costs
- 例1 値：Salary | 」1,375,013.87 | 」1,386,180.66 | 」1,384,412.76 | 」1,370,122.07
  - 同じ表の列：Effective Date, Organisation type, Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Non-Payroll staff (…, Grand Total paybill…

## 答えの雛形

```
g0004	
g0011	
g0013	
g0038	
g0043	
g0052	
g0056	
g0068	
g0083	
g0089	
g0094	
g0109	
g0113	
g0118	
g0126	
g0128	
g0148	
g0153	
g0155	
g0168	
g0195	
g0200	
g0203	
g0234	
```
