# ラベル用シート 002 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Expense Type
- 例1 値：225000-Banking and Finance | 246000-Current Grants | 246000-Current Grants | 222001-Maintenance | 265000-IT & Telecommunications
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Transaction Number, Amount, Supplier Type, Project Code

## g0122（1 列）
- 見出し：Expense Area
- 例1 値：BZ999-London Region | BZ999-London Region | DZ999-South West Region | LZ600-Transforming Justice | FZ999-Midlands Region
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Transaction Number, Amount, Supplier Type, Project Code

## g0123（1 列）
- 見出し：Transaction Number
- 例1 値：686489 | 674791 | 2090593 | 2123471 | 2106834
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Amount, Supplier Type, Project Code

## g0124（1 列）
- 見出し：Amount
- 例1 値：」27,949.10 | 」31,450.00 | 」26,106.00 | 」54,044.00 | 」232,537.53
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Supplier Type, Project Code

## g0125（1 列）
- 見出し：Supplier Type
- 例1 値：SME | SME | SME | SME | SME
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount, Project Code

## g0126（1 列）
- 見出し：Project Code
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type

## g0127（1 列）
- 見出し：Expenditure Type
- 例1 値：Programme | Programme | Programme | Programme | Programme
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type

## g0128（1 列）
- 見出し：reference
- 例1 値：374 | 242 | 177 | 231 | 304
  - 同じ表の列：geometry, listing_ref_no_QGIS, listed_building, listed-building-gra…, date_listed, entry_listed

## g0129（2 列）
- 見出し：geometry
- 例1 値：MULTIPOLYGON (((-2.11817296870082 53.59… | MULTIPOLYGON (((-2.03085386199532 53.62… | MULTIPOLYGON (((-2.15359745555794 53.61… | MULTIPOLYGON (((-2.06034059214772 53.65… | MULTIPOLYGON (((-2.10671655483845 53.62…
  - 同じ表の列：reference, listing_ref_no_QGIS, listed_building, listed-building-gra…, date_listed, entry_listed
- 例2 値：MULTIPOLYGON (((-2.0724210932188 53.604… | MULTIPOLYGON (((-2.20618674484506 53.58… | MULTIPOLYGON (((-2.20999365490671 53.54… | MULTIPOLYGON (((-2.08561889902248 53.66… | MULTIPOLYGON (((-2.16216472166044 53.61…
  - 同じ表の列：Reference, Conservation Area, Document Type (i.e …, start-date, designation-date, entry-date

## g0130（1 列）
- 見出し：listing_ref_no_QGIS
- 例1 値：1483/2/19 | 45809 | 20455 | 19511 | 1470832
  - 同じ表の列：reference, geometry, listed_building, listed-building-gra…, date_listed, entry_listed

## g0131（1 列）
- 見出し：listed_building
- 例1 値：1084286 | 1068467 | 1356233 | 1084292 | 1068515
  - 同じ表の列：reference, geometry, listing_ref_no_QGIS, listed-building-gra…, date_listed, entry_listed

## g0132（1 列）
- 見出し：listed-building-grade
- 例1 値：II | II | II | II | II
  - 同じ表の列：reference, geometry, listing_ref_no_QGIS, listed_building, date_listed, entry_listed

## g0133（1 列）
- 見出し：date_listed
- 例1 値：12/02/1985 | 12/02/1985 | 12/02/1985 | 12/02/1985 | 23/04/1986
  - 同じ表の列：reference, geometry, listing_ref_no_QGIS, listed_building, listed-building-gra…, entry_listed

## g0134（1 列）
- 見出し：entry_listed
- 例1 値：12/02/1985 | 23/04/1986 | 23/04/1986 | 23/04/1986 | 23/03/1987
  - 同じ表の列：reference, geometry, listing_ref_no_QGIS, listed_building, listed-building-gra…, date_listed

## g0135（1 列）
- 見出し：Reference
- 例1 値：CA4 | CA8 | CA1 | CA16 | CA6
  - 同じ表の列：Conservation Area, Geometry, Document Type (i.e …, start-date, designation-date, entry-date

## g0136（1 列）
- 見出し：Conservation Area
- 例1 値：CA20 | CA19 | CA11 | CA22 | CA7
  - 同じ表の列：Reference, Geometry, Document Type (i.e …, start-date, designation-date, entry-date

## g0137（1 列）
- 見出し：Document Type (i.e Area Appraisal
- 例1 値：Map | Appraisal | Map | Map | Map
  - 同じ表の列：Reference, Conservation Area, Geometry, start-date, designation-date, entry-date

## g0138（1 列）
- 見出し：start-date
- 例1 値：06/12/2017 | 06/07/2011 | 21/06/2006 | 18/03/2011 | 31/03/1982
  - 同じ表の列：Reference, Conservation Area, Geometry, Document Type (i.e …, designation-date, entry-date

## g0139（1 列）
- 見出し：designation-date
- 例1 値：26/05/2009 | 01/12/1974 | 01/09/1974 | 06/07/2011 | 07/11/2012
  - 同じ表の列：Reference, Conservation Area, Geometry, Document Type (i.e …, start-date, entry-date

## g0140（1 列）
- 見出し：entry-date
- 例1 値：21/06/2006 | 10/07/2013 | 30/06/1905 | 12/09/2006 | 14/11/2006
  - 同じ表の列：Reference, Conservation Area, Geometry, Document Type (i.e …, start-date, designation-date

## g0141（1 列）
- 見出し：Purpose of Spend
- 例1 値：Delivery of arts activities | Contribution towards a Tour de France E… | Back to Work scheme offering help and s… | Financial inclusion workshops for priva… | Delivery of arts activities
  - 同じ表の列：Directorate/ Servic…, Start Date, End Date, Award Amount (」), Registered Charity …, RBC Grant Reference

## g0142（1 列）
- 見出し：Directorate/ Service Responsible
- 例1 値：Economy & Environment | Economy & Environment | Link4Life | Economy & Environment | Link4Life
  - 同じ表の列：Purpose of Spend, Start Date, End Date, Award Amount (」), Registered Charity …, RBC Grant Reference

## g0143（1 列）
- 見出し：Start Date
- 例1 値：01/07/2014 | 01/04/2014 | 01/04/2014 | 01/04/2014 | 01/04/2014
  - 同じ表の列：Purpose of Spend, Directorate/ Servic…, End Date, Award Amount (」), Registered Charity …, RBC Grant Reference

## g0144（1 列）
- 見出し：End Date
- 例1 値：31/03/2015 | 31/03/2015 | 31/03/2015 | 31/03/2015 | 31/03/2015
  - 同じ表の列：Purpose of Spend, Directorate/ Servic…, Start Date, Award Amount (」), Registered Charity …, RBC Grant Reference

## g0145（1 列）
- 見出し：Award Amount (」)
- 例1 値：58883.00 | 6016.00 | 200.00 | 2500.00 | 5000.00
  - 同じ表の列：Purpose of Spend, Directorate/ Servic…, Start Date, End Date, Registered Charity …, RBC Grant Reference

## g0146（1 列）
- 見出し：Registered Charity Number
- 例1 値：1047613 | 1040176 | 1001570 | 1156946 | na
  - 同じ表の列：Purpose of Spend, Directorate/ Servic…, Start Date, End Date, Award Amount (」), RBC Grant Reference

## g0147（1 列）
- 見出し：RBC Grant Reference
- 例1 値：RBC 2014/40 | RBC 2014/3 | RBC 2014/23 | RBC 2014/12 | RBC 2014/9
  - 同じ表の列：Purpose of Spend, Directorate/ Servic…, Start Date, End Date, Award Amount (」), Registered Charity …

## g0148（1 列）
- 見出し：ExtractDate
- 例1 値：22/02/2017 | 22/02/2017 | 22/02/2017 | 22/02/2017 | 22/02/2017
  - 同じ表の列：OrganisationURI, OrganisationLabel, TitileOfOpportunity, StartDate, EndDate, ReviewDate, Extension(IfApplica…, EstimatedValue」

## g0149（1 列）
- 見出し：OrganisationURI
- 例1 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：ExtractDate, OrganisationLabel, TitileOfOpportunity, StartDate, EndDate, ReviewDate, Extension(IfApplica…, EstimatedValue」

## g0150（1 列）
- 見出し：OrganisationLabel
- 例1 値：South Lakeland | South Lakeland | South Lakeland | South Lakeland | South Lakeland
  - 同じ表の列：ExtractDate, OrganisationURI, TitileOfOpportunity, StartDate, EndDate, ReviewDate, Extension(IfApplica…, EstimatedValue」

## g0151（1 列）
- 見出し：TitileOfOpportunity
- 例1 値：Roof Anchors maintenance | Service Risers | Flood Impact Works (Rothay Park) - Cons… | Treasury Management Advice | Development Delivery Advisory Partner
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, StartDate, EndDate, ReviewDate, Extension(IfApplica…, EstimatedValue」

## g0152（1 列）
- 見出し：StartDate
- 例1 値：01/04/2010 | 25/11/2016 | 01/04/2017 | 01/04/2016 | 01/04/2017
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, TitileOfOpportunity, EndDate, ReviewDate, Extension(IfApplica…, EstimatedValue」

## g0153（1 列）
- 見出し：EndDate
- 例1 値：31/03/2027 | 31/03/2018 | 31/03/2019 | 31/03/2020 | 31/03/2018
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, TitileOfOpportunity, StartDate, ReviewDate, Extension(IfApplica…, EstimatedValue」

## g0154（1 列）
- 見出し：ReviewDate
- 例1 値：02/01/2018 | 31/03/2017 | 31/03/2019 | 30/09/2015 | 02/01/2018
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, TitileOfOpportunity, StartDate, EndDate, Extension(IfApplica…, EstimatedValue」

## g0155（1 列）
- 見出し：Extension(IfApplicable)
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, TitileOfOpportunity, StartDate, EndDate, ReviewDate, EstimatedValue」

## g0156（1 列）
- 見出し：EstimatedValue」
- 例1 値：100K-OJEU | 10-100K | 100K-OJEU | <10K | 10-100K
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, TitileOfOpportunity, StartDate, EndDate, ReviewDate, Extension(IfApplica…

## g0157（1 列）
- 見出し：ProcurementProcess
- 例1 値：Quotes | Tender | Tender | Quotes | Tender
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, TitileOfOpportunity, StartDate, EndDate, ReviewDate, Extension(IfApplica…

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
g0155	
g0156	
g0157	
```
