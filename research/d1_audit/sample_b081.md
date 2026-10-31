<!-- b081：16/157 グループ -->
# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `research/d1_audit/answers_b081.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0014（1 列）
- 見出し：Start date of trip
- 例1 値：21/09/2016 | 31/08/2016 | 16/09/2016 | 07/07/2016 | 26/09/2016
  - 同じ表の列：Duration of Visit (…, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/ Meals, Total cost, includi…

## g0015（1 列）
- 見出し：Duration of Visit (Days)
- 例1 値：1 | 1 | 1 | 2 | 1
  - 同じ表の列：Start date of trip, Destination, Purpose of trip, Mode of transport, Class of travel, Accommodation/ Meals, Total cost, includi…

## g0017（1 列）
- 見出し：Purpose of trip
- 例1 値：Meeting with European Officials | Meeting with European Officials | Meeting with European Officials | Meeting with European Officials | Meeting with European Officials
  - 同じ表の列：Start date of trip, Duration of Visit (…, Destination, Mode of transport, Class of travel, Accommodation/ Meals, Total cost, includi…

## g0028（1 列）
- 見出し：1 - Aid/effectiveness
- 例1 値：Table 1.3: G8 Multilateral Debt Relief | Table 1.2: G8 bilateral & imputed multi… | Additional table | Figure 6.3: G8 disbursements to educati… | Annex C
  - 同じ表の列：Notes/source

## g0032（1 列）
- 見出し：Feb-12
- 例1 値：100.00% | 100.00% | 99.78% | 99.75% | 99.30%
  - 同じ表の列：Percentage paid wit…, Jan-12, Mar-12, Apr-12, May-12, Jun-12, Jul-12, Aug-12

## g0044（1 列）
- 見出し：Easting
- 例1 値：372632 | 318653 | 315080 | 372198 | 295679
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Northing, CreationDateTime, ModificationDateTime, RevisionNumber

## g0045（1 列）
- 見出し：Northing
- 例1 値：167528 | 195270 | 177839 | 422650 | 168981
  - 同じ表の列：NptgLocalityCode, AdministrativeAreaC…, NptgDistrictCode, SourceLocalityType, Easting, CreationDateTime, ModificationDateTime, RevisionNumber

## g0064（1 列）
- 見出し：Expense Area
- 例1 値：DG CHANGE & DELIVERY | DG CHANGE & DELIVERY | DG CHANGE & DELIVERY | DG CHANGE & DELIVERY | DG CHANGE & DELIVERY
  - 同じ表の列：Department Family, Entity, Payment Date, Expense Type, Transactions Number, Amount (」)

## g0071（2 列）
- 見出し：Payroll staff AO/AA Headcount
- 例1 値：133 | 0 | 487 | 0 | 0
  - 同じ表の列：Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…, Non-payroll Staff A…
- 例2 値：197 | 12 | 604 | 1 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0092（1 列）
- 見出し：Exceptions for period 01 November 2010 to 30 September 2011
- 例1 値：Department | Home Office | Home Office | Home Office | Home Office
  - 同じ表の列：ICT

## g0093（1 列）
- 見出し：Posting Date
- 例1 値：13/04/2011 | 04/04/2011 | 18/04/2011 | 04/04/2011 | 08/04/2011
  - 同じ表の列：Transaction Amount

## g0132（1 列）
- 見出し：listed-building-grade
- 例1 値：II | II | II | II | II
  - 同じ表の列：reference, geometry, listing_ref_no_QGIS, listed_building, date_listed, entry_listed

## g0137（1 列）
- 見出し：Document Type (i.e Area Appraisal
- 例1 値：Map | Appraisal | Map | Map | Map
  - 同じ表の列：Reference, Conservation Area, Geometry, start-date, designation-date, entry-date

## g0142（1 列）
- 見出し：Directorate/ Service Responsible
- 例1 値：Economy & Environment | Economy & Environment | Link4Life | Economy & Environment | Link4Life
  - 同じ表の列：Purpose of Spend, Start Date, End Date, Award Amount (」), Registered Charity …, RBC Grant Reference

## g0143（1 列）
- 見出し：Start Date
- 例1 値：01/07/2014 | 01/04/2014 | 01/04/2014 | 01/04/2014 | 01/04/2014
  - 同じ表の列：Purpose of Spend, Directorate/ Servic…, End Date, Award Amount (」), Registered Charity …, RBC Grant Reference

## g0152（1 列）
- 見出し：StartDate
- 例1 値：01/04/2010 | 25/11/2016 | 01/04/2017 | 01/04/2016 | 01/04/2017
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, TitileOfOpportunity, EndDate, ReviewDate, Extension(IfApplica…, EstimatedValue」

## 答えの雛形

```
g0014	
g0015	
g0017	
g0028	
g0032	
g0044	
g0045	
g0064	
g0071	
g0092	
g0093	
g0132	
g0137	
g0142	
g0143	
g0152	
```
