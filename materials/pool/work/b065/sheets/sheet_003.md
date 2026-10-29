# ラベル用シート 003 / 003

- LABEL_GUIDE v2.1 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_003.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0241（1 列）
- 見出し：Organisation
- 例1 値：Defence Electronic and Components Agency | Defence Science and Technology Laborato… | UK Hydrographic Office | Ministry of Defence | Royal Fleet Auxilary
  - 同じ表の列：Main department, Delegated grades, SCS on standard con…, Information for SCS…, Comments

## g0242（1 列）
- 見出し：Delegated grades
- 例1 値：」96,284,000 | 」1,155,895,066 | 」192,481,571 | Annual Paybill (delegated grades for fi… | 」15,428,000
  - 同じ表の列：Main department, Organisation, SCS on standard con…, Information for SCS…, Comments

## g0243（1 列）
- 見出し：SCS on standard contracts
- 例1 値：」18,322,781 | Annual SCS Paybill for those SCS on sta…
  - 同じ表の列：Main department, Organisation, Delegated grades, Information for SCS…, Comments

## g0244（1 列）
- 見出し：Information for SCS on non-standard terms
- 例1 値：Number of SCS on non-standard performan… | 2
  - 同じ表の列：Main department, Organisation, Delegated grades, SCS on standard con…, Comments

## g0245（1 列）
- 見出し：Comments
- 例1 値：There were 426 employees who qualified … | As Cabinet Office are aware, MOD Main t… | The RFA does not operate an in year per… | Spend on NCPRP is higher than 1.52% amo…
  - 同じ表の列：Main department, Organisation, Delegated grades, SCS on standard con…, Information for SCS…

## g0246（1 列）
- 見出し：Transaction Posting Date
- 例1 値：18/05/2011 | 20/05/2011 | 01/06/2011 | 05/04/2011 | 12/05/2011
  - 同じ表の列：Transaction Amount

## g0247（1 列）
- 見出し：Transaction Amount
- 例1 値：1,373.75 | 907.20 | 512.96 | 548.98 | -1,899.83
  - 同じ表の列：Transaction Posting…

## g0248（1 列）
- 見出し：Purchase Order Number
- 例1 値：d1046885 | d1046069 | q1003008 | q1003265 | d1045504
  - 同じ表の列：Order date, Total_Value, Service

## g0249（1 列）
- 見出し：Order date
- 例1 値：17/12/2014 | 16/12/2014 | 18/11/2014 | 14/10/2014 | 23/12/2014
  - 同じ表の列：Purchase Order Numb…, Total_Value, Service

## g0250（1 列）
- 見出し：Total_Value
- 例1 値：」147,000.00 | 」5,000.00 | 」17,998.24 | 」7,525.00 | 」50,500.00
  - 同じ表の列：Purchase Order Numb…, Order date, Service

## g0251（1 列）
- 見出し：Service
- 例1 値：FINANCE SERVICES | ECONOMY AND ENVIRONMENT | ECONOMY AND ENVIRONMENT | PHYSICAL DIS & OLDER PEOPLE | CHILDREN担 SOCIAL CARE
  - 同じ表の列：Purchase Order Numb…, Order date, Total_Value

## g0252（1 列）
- 見出し：Reference
- 例1 値：A4D-2 | A4D-3 | A4D-1 | A4D-4 | A4D-5
  - 同じ表の列：Geometry, UPRN, Permitted-Developme…, Entry-Date, Start-Date, End-Date

## g0253（1 列）
- 見出し：Geometry
- 例1 値：MULTIPOLYGON (((388124.91 413865.960000… | MULTIPOLYGON (((391664.059374837 413029… | MULTIPOLYGON (((387512.91 416484.54,387… | MULTIPOLYGON (((387512.91 416484.54,387… | MULTIPOLYGON (((387679.66 406346.44,387…
  - 同じ表の列：Reference, UPRN, Permitted-Developme…, Entry-Date, Start-Date, End-Date

## g0254（1 列）
- 見出し：UPRN
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Reference, Geometry, Permitted-Developme…, Entry-Date, Start-Date, End-Date

## g0255（1 列）
- 見出し：Permitted-Development- Rights
- 例1 値：4B | 18B | 1A;1C;1D;1H;2A | 4B | 2B
  - 同じ表の列：Reference, Geometry, UPRN, Entry-Date, Start-Date, End-Date

## g0256（1 列）
- 見出し：Entry-Date
- 例1 値：26/09/1991 | 09/04/1992 | 01/07/1975 | 09/11/1989 | 02/06/1980
  - 同じ表の列：Reference, Geometry, UPRN, Permitted-Developme…, Start-Date, End-Date

## g0257（1 列）
- 見出し：Start-Date
- 例1 値：09/11/1989 | 09/04/1992 | 02/06/1980 | 26/09/1991 | 01/07/1975
  - 同じ表の列：Reference, Geometry, UPRN, Permitted-Developme…, Entry-Date, End-Date

## g0258（1 列）
- 見出し：End-Date
- 例1 値：22/08/2005
  - 同じ表の列：Reference, Geometry, UPRN, Permitted-Developme…, Entry-Date, Start-Date

## g0259（1 列）
- 見出し：FID
- 例1 値：lp_2030_sangs_revised2025.5 | lp_2030_sangs_revised2025.13 | lp_2030_sangs_revised2025.11 | lp_2030_sangs_revised2025.9 | lp_2030_sangs_revised2025.4
  - 同じ表の列：id_0, id, status

## g0260（1 列）
- 見出し：id_0
- 例1 値：8 | 1 | 11 | 6 | 2
  - 同じ表の列：FID, id, status

## g0261（1 列）
- 見出し：id
- 例1 値：13 | 5 | 12 | 15 | 10
  - 同じ表の列：FID, id_0, status

## g0262（1 列）
- 見出し：status
- 例1 値：Existing | Existing | Existing | Existing | Existing
  - 同じ表の列：FID, id_0, id

## g0263（1 列）
- 見出し：Year
- 例1 値：2024/25 | 2017/18 | 2022/23 | 2018/19 | 2016/17
  - 同じ表の列：%

## g0264（1 列）
- 見出し：%
- 例1 値：96.89% | 96.25% | 97.72% | 97.83% | 94.48%
  - 同じ表の列：Year

## g0265（3 列）
- 見出し：ExtractDate
- 例1 値：04/09/2014 | 04/09/2014 | 04/09/2014 | 04/09/2014 | 04/09/2014
  - 同じ表の列：OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CoordinateReference…, GeoX, GeoY, GeoPointLicensingURL
- 例2 値：18/12/2014 | 18/12/2014 | 18/12/2014 | 18/12/2014 | 18/12/2014
  - 同じ表の列：OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, MonthOfClaim, MonthPaid, ExpenseType, Amount

## g0266（3 列）
- 見出し：OrganisationLabel
- 例1 値：South Lakeland | South Lakeland | South Lakeland | South Lakeland | South Lakeland
  - 同じ表の列：ExtractDate, OrganisationURI, ServiceTypeURI, ServiceTypeLabel, CoordinateReference…, GeoX, GeoY, GeoPointLicensingURL
- 例2 値：South Lakeland | South Lakeland | South Lakeland | South Lakeland | South Lakeland
  - 同じ表の列：ExtractDate, OrganisationURI, ServiceTypeURI, ServiceTypeLabel, MonthOfClaim, MonthPaid, ExpenseType, Amount

## g0267（3 列）
- 見出し：ServiceTypeURI
- 例1 値：http://id.esd.org.uk/service/579 | http://id.esd.org.uk/service/579 | http://id.esd.org.uk/service/579 | http://id.esd.org.uk/service/579 | http://id.esd.org.uk/service/579
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeLabel, CoordinateReference…, GeoX, GeoY, GeoPointLicensingURL
- 例2 値：http://id.esd.org.uk/service/1656 | http://id.esd.org.uk/service/1028 | http://id.esd.org.uk/service/1656 | http://id.esd.org.uk/service/1656 | http://id.esd.org.uk/service/1028
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeLabel, MonthOfClaim, MonthPaid, ExpenseType, Amount

## g0268（2 列）
- 見出し：ServiceTypeLabel
- 例1 値：Public toilets | Public toilets | Public toilets | Public toilets | Public toilets
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, CoordinateReference…, GeoX, GeoY, GeoPointLicensingURL
- 例2 値：Premises Licence | Premises Licence | Premises Licence | Premises Licence | Premises Licence
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, CaseReference, CaseDate, ServiceTypeURI, EntertainmentTypeURI, EntertainmentTypeLa…

## g0269（1 列）
- 見出し：GeoPointLicensingURL
- 例1 値：http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/… | http://www.nationalarchives.gov.uk/doc/…
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CoordinateReference…, GeoX, GeoY

## g0270（1 列）
- 見出し：Category
- 例1 値：Female and male | Female and male | Female and male | Female and male | Female and male
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, CoordinateReference…, GeoX, GeoY

## g0271（1 列）
- 見出し：ServiceTypeLabel
- 例1 値：Members - allowances | Members - allowances | Staff- busines travel | Members - allowances | Staff- busines travel
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, MonthOfClaim, MonthPaid, ExpenseType, Amount

## g0272（1 列）
- 見出し：MonthOfClaim
- 例1 値：Sep-14 | Oct-14 | Aug-14 | Sep-14 | Aug-14
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, MonthPaid, ExpenseType, Amount

## g0273（1 列）
- 見出し：MonthPaid
- 例1 値：Dec-14 | Dec-14 | Oct-14 | Oct-14 | Nov-14
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, MonthOfClaim, ExpenseType, Amount

## g0274（1 列）
- 見出し：ExpenseType
- 例1 値：Car mileage | Public Transport | Subsistence | Rail Equivalent (car used but paid seco… | Essential user lump sum
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, MonthOfClaim, MonthPaid, Amount

## g0275（1 列）
- 見出し：Amount
- 例1 値：7.20 | 1181.70 | 7765.85 | 6.30 | 1327.50
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, ServiceTypeURI, ServiceTypeLabel, MonthOfClaim, MonthPaid, ExpenseType

## g0276（1 列）
- 見出し：CaseReference
- 例1 値：PL(A)0611 | PL(A)0157 | PL(A)0478 | PL(A)0595 | PL(A)0705
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, CaseDate, ServiceTypeURI, ServiceTypeLabel, EntertainmentTypeURI, EntertainmentTypeLa…

## g0277（1 列）
- 見出し：CaseDate
- 例1 値：19/04/2006 | 26/10/2005 | 11/01/2010 | 08/12/2005 | 13/10/2005
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, CaseReference, ServiceTypeURI, ServiceTypeLabel, EntertainmentTypeURI, EntertainmentTypeLa…

## g0278（1 列）
- 見出し：EntertainmentTypeURI
- 例1 値：http://id.esd.org.uk/entertainment/5|ht… | http://id.esd.org.uk/entertainment/5|ht… | http://id.esd.org.uk/entertainment/8 | http://id.esd.org.uk/entertainment/5|ht… | http://id.esd.org.uk/entertainment/5|ht…
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, CaseReference, CaseDate, ServiceTypeURI, ServiceTypeLabel, EntertainmentTypeLa…

## g0279（1 列）
- 見出し：EntertainmentTypeLabel
- 例1 値：Indoor sporting events|Performances of … | Live music|Recorded music | Films|Indoor sporting events|Recorded m… | Films|Indoor sporting events|Live music… | Plays|Films|Indoor sporting events|Live…
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, CaseReference, CaseDate, ServiceTypeURI, ServiceTypeLabel, EntertainmentTypeURI

## g0280（1 列）
- 見出し：LateNightRefreshment
- 例1 値：FALSE | TRUE | FALSE | FALSE | FALSE
  - 同じ表の列：ExtractDate, OrganisationURI, OrganisationLabel, CaseReference, CaseDate, ServiceTypeURI, ServiceTypeLabel, EntertainmentTypeURI

## g0281（1 列）
- 見出し：SiteReference
- 例1 値：16/00921/FUL | ALT15 | 17/01845/FUL | 17/01955/OUT | MSA11
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0282（1 列）
- 見出し：GeoX
- 例1 値：1.156828 | 1.273837 | 1.109537 | 1.156717 | 1.287144
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoY, Hectares, Deliverable

## g0283（1 列）
- 見出し：PlanningStatus
- 例1 値：permissioned | permissioned | not permissioned | not permissioned | permissioned
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares

## g0284（1 列）
- 見出し：Transaction Date
- 例1 値：15.01.18 | 17.01.18 | 08.01.18 | 12.01.18 | 12.01.18
  - 同じ表の列：Total

## g0285（1 列）
- 見出し：Total
- 例1 値：702.00 | 755.32 | 964.93 | 890.15 | 919.62
  - 同じ表の列：Transaction Date

## g0286（1 列）
- 見出し：Department family
- 例1 値：The National Archives | The National Archives | The National Archives | The National Archives | The National Archives
  - 同じ表の列：Entity, Date of payment, Directorate, Transaction referen…, Amount paid, Contract Number, Expenditure Type

## g0287（1 列）
- 見出し：Entity
- 例1 値：The National Archives | The National Archives | The National Archives | The National Archives | The National Archives
  - 同じ表の列：Department family, Date of payment, Directorate, Transaction referen…, Amount paid, Contract Number, Expenditure Type

## g0288（1 列）
- 見出し：Directorate
- 例1 値：Procurement | Finance | Estates | Web Archiving | Human Resources
  - 同じ表の列：Department family, Entity, Date of payment, Transaction referen…, Amount paid, Contract Number, Expenditure Type

## g0289（1 列）
- 見出し：Transaction reference
- 例1 値：153105 | 152959 | 152856 | 153077 | 152842
  - 同じ表の列：Department family, Entity, Date of payment, Directorate, Amount paid, Contract Number, Expenditure Type

## g0290（1 列）
- 見出し：Amount paid
- 例1 値：64,650.12 | 11,738.25 | 134,137.57 | 23,701.39 | 341,145.00
  - 同じ表の列：Department family, Entity, Date of payment, Directorate, Transaction referen…, Contract Number, Expenditure Type

## g0291（1 列）
- 見出し：Contract Number
- 例1 値：CM499 | CM888 | CM939 | CM939
  - 同じ表の列：Department family, Entity, Date of payment, Directorate, Transaction referen…, Amount paid, Expenditure Type

## g0292（1 列）
- 見出し：Expenditure Type
- 例1 値：Administration | Administration | Programme | Programme | Programme
  - 同じ表の列：Department family, Entity, Date of payment, Directorate, Transaction referen…, Amount paid, Contract Number

## 答えの雛形

```
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
g0249	
g0250	
g0251	
g0252	
g0253	
g0254	
g0255	
g0256	
g0257	
g0258	
g0259	
g0260	
g0261	
g0262	
g0263	
g0264	
g0265	
g0266	
g0267	
g0268	
g0269	
g0270	
g0271	
g0272	
g0273	
g0274	
g0275	
g0276	
g0277	
g0278	
g0279	
g0280	
g0281	
g0282	
g0283	
g0284	
g0285	
g0286	
g0287	
g0288	
g0289	
g0290	
g0291	
g0292	
```
