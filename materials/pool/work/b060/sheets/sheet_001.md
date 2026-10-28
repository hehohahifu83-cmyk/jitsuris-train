# ラベル用シート 001 / 006

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（23 列）
- 見出し：OrganisationURI
- 例1 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus
- 例2 値：http://opendatacommunities.org/doc/dist… | http://opendatacommunities.org/doc/dist… | http://opendatacommunities.org/doc/dist… | http://opendatacommunities.org/doc/dist… | http://opendatacommunities.org/doc/dist…
  - 同じ表の列：SiteReference, SiteplanURL - Colum…, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0002（4 列）
- 見出し：OrganisationLabel
- 例1 値：Amber Valley | Amber Valley | Amber Valley | Amber Valley | Amber Valley
  - 同じ表の列：OrganisationURI, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus
- 例2 値：Ealing Council | Ealing Council | Ealing Council | Ealing Council | Ealing Council
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0003（10 列）
- 見出し：SiteReference
- 例1 値：BFLR0062 | BFLR0066 | BFLR0065 | BFLR0052 | BFLR0061
  - 同じ表の列：OrganisationURI, OrganisationLabel, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable, PlanningStatus
- 例2 値：BFR032 | BFR022 | BFR036 | BFR026 | BFR023
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0004（8 列）
- 見出し：CoordinateReferenceSystem
- 例1 値：ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, GeoX, GeoY, Hectares, Deliverable, PlanningStatus
- 例2 値：OSGB36 | OSGB36 | OSGB36 | OSGB36 | OSGB36
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, GeoX, GeoY, Hectares, Deliverable

## g0005（9 列）
- 見出し：GeoX
- 例1 値：-1.242263628 | -1.3242221 | -1.231909855 | -1.241181093 | -1.201222157
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoY, Hectares, Deliverable, PlanningStatus
- 例2 値：-2.2962572 | -2.2938523 | -2.2775686 | -2.2979473 | -2.3103401
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, Hectares, Deliverable, PlanningStatus, PermissionType

## g0006（13 列）
- 見出し：GeoY
- 例1 値：53.00424554 | 53.00112039 | 53.01367102 | 53.02599252 | 53.05472843
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, Hectares, Deliverable, PlanningStatus
- 例2 値：53.517244 | 53.590939 | 53.516176 | 53.595487 | 53.595328
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoX, Hectares, Deliverable, PlanningStatus, PermissionType

## g0007（22 列）
- 見出し：Hectares
- 例1 値：2.01 | 0.09 | 6.02 | 1.12 | 46.9
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Deliverable, PlanningStatus
- 例2 値：0.34 | 0.19 | 4.13 | 0.25 | 0.75
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL - Colum…, GeoY, GeoX, PlanningStatus, PermissionType, PermissionDate

## g0008（13 列）
- 見出し：Deliverable
- 例1 値：yes | yes | yes | yes | yes
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, PlanningStatus
- 例2 値：YES | YES | YES | YES | YES
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL - Colum…, GeoY, GeoX, Hectares, PlanningStatus, PermissionType

## g0009（5 列）
- 見出し：PlanningStatus
- 例1 値：permissioned | permissioned | permissioned | permissioned | permissioned
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable
- 例2 値：permissioned | permissioned | permissioned | permissioned | permissioned
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL - Colum…, GeoY, GeoX, Hectares, PermissionType, PermissionDate

## g0010（10 列）
- 見出し：PermissionType
- 例1 値：full planning permission | outline planning permission | outline planning permission | full planning permission | full planning permission
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable
- 例2 値：full planning permission | outline planning permission | full planning permission | full planning permission | full planning permission
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, Deliverable, PlanningStatus

## g0011（1 列）
- 見出し：Valuation Band Range
- 例1 値：Valuation Band Range | <」50 000-」99 999 | <」50 000-」99 999 | 」100 000-」299 999 | 」100 000-」299 999
  - 同じ表の列：Intervening Bands, Dwelling Values, Total based on EUV-…, Average based on EU…, Total based on Mark…, Average based on Ma…, % occupied dwellings, % vacated dwellings

## g0012（1 列）
- 見出し：Intervening Bands
- 例1 値：Intervening Bands | 」60 000-」69 999 | <」50 000 | 」140 000-」159 999 | 」70 000-」79 999
  - 同じ表の列：Valuation Band Range, Dwelling Values, Total based on EUV-…, Average based on EU…, Total based on Mark…, Average based on Ma…, % occupied dwellings, % vacated dwellings

## g0013（1 列）
- 見出し：Dwelling Values
- 例1 値：Total Number social housing dwellings | Total Number social housing dwellings | 3661 | 3206 | Dwelling Values
  - 同じ表の列：Valuation Band Range, Intervening Bands, Total based on EUV-…, Average based on EU…, Total based on Mark…, Average based on Ma…, % occupied dwellings, % vacated dwellings

## g0014（1 列）
- 見出し：Total based on EUV-SH Values
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Valuation Band Range, Intervening Bands, Dwelling Values, Average based on EU…, Total based on Mark…, Average based on Ma…, % occupied dwellings, % vacated dwellings

## g0015（1 列）
- 見出し：Average based on EUV-SH Values
- 例1 値：50490 | Average based on EUV-SH Values | 0 | 53754 | 0
  - 同じ表の列：Valuation Band Range, Intervening Bands, Dwelling Values, Total based on EUV-…, Total based on Mark…, Average based on Ma…, % occupied dwellings, % vacated dwellings

## g0016（1 列）
- 見出し：Total based on Market Values
- 例1 値：715 | 34 | 0 | 452 | 733
  - 同じ表の列：Valuation Band Range, Intervening Bands, Dwelling Values, Total based on EUV-…, Average based on EU…, Average based on Ma…, % occupied dwellings, % vacated dwellings

## g0017（1 列）
- 見出し：Average based on Market Values
- 例1 値：65198.56 | 44535.4 | Average based on Market Values | 125388.97 | 93932.2
  - 同じ表の列：Valuation Band Range, Intervening Bands, Dwelling Values, Total based on EUV-…, Average based on EU…, Total based on Mark…, % occupied dwellings, % vacated dwellings

## g0018（1 列）
- 見出し：% occupied dwellings
- 例1 値：% occupied dwellings | 1 | 0.9938 | 0.9934 | 1
  - 同じ表の列：Valuation Band Range, Intervening Bands, Dwelling Values, Total based on EUV-…, Average based on EU…, Total based on Mark…, Average based on Ma…, % vacated dwellings

## g0019（1 列）
- 見出し：% vacated dwellings
- 例1 値：0.0062 | % vacated dwellings | 0.0066
  - 同じ表の列：Valuation Band Range, Intervening Bands, Dwelling Values, Total based on EUV-…, Average based on EU…, Total based on Mark…, Average based on Ma…, % occupied dwellings

## g0020（3 列）
- 見出し：OrganisationCode
- 例1 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：Date Approved, Service, Portfolio, Type, Review Date, Current?, Link
- 例2 値：http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr… | http://opendatacommunities.org/id/distr…
  - 同じ表の列：EffectiveDate, FinancialYear, Department, Payee, Language, Amount

## g0021（1 列）
- 見出し：Date Approved
- 例1 値：11/12/2007 | 31/03/2006 | 01/11/2012 | 21/03/2016 | 01/03/2005
  - 同じ表の列：OrganisationCode, Service, Portfolio, Type, Review Date, Current?, Link

## g0022（1 列）
- 見出し：Service
- 例1 値：Regulatory & Leisure Services | Financial Services | Regulatory & Leisure Services | Corporate Services | Regulatory & Leisure Services
  - 同じ表の列：OrganisationCode, Date Approved, Portfolio, Type, Review Date, Current?, Link

## g0023（1 列）
- 見出し：Portfolio
- 例1 値：Finance, Efficiency & Assets | Partnerships & Corporate Services | Neighbourhood & Environmental Services | Neighbourhood & Environmental Services | Partnerships & Corporate Services
  - 同じ表の列：OrganisationCode, Date Approved, Service, Type, Review Date, Current?, Link

## g0024（1 列）
- 見出し：Type
- 例1 値：Strategy | Strategy | Policy | Policy | Policy
  - 同じ表の列：OrganisationCode, Date Approved, Service, Portfolio, Review Date, Current?, Link

## g0025（2 列）
- 見出し：Review Date
- 例1 値：01/04/2018 | 01/01/2020 | 01/02/2016 | 01/03/2018 | 01/02/2020
  - 同じ表の列：OrganisationCode, Date Approved, Service, Portfolio, Type, Current?, Link
- 例2 値：12/01/2015 | 26/01/2015 | 26/01/2015 | 26/01/2015 | 26/01/2015
  - 同じ表の列：Record UID, Contract Ref No, Directorate/ Servic…, Start Date, End Date (Includes …, Estimated Maximum A…

## g0026（1 列）
- 見出し：Current?
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：OrganisationCode, Date Approved, Service, Portfolio, Type, Review Date, Link

## g0027（1 列）
- 見出し：Link
- 例1 値：http://w3.blaby.gov.uk/decision-making/… | http://w3.blaby.gov.uk/decision-making/… | http://w3.blaby.gov.uk/decision-making/… | http://w3.blaby.gov.uk/decision-making/… | http://w3.blaby.gov.uk/decision-making/…
  - 同じ表の列：OrganisationCode, Date Approved, Service, Portfolio, Type, Review Date, Current?

## g0028（4 列）
- 見出し：EffectiveDate
- 例1 値：01/12/2017 | 01/12/2017 | 01/12/2017 | 01/12/2017 | 01/12/2017
  - 同じ表の列：OrganisationCode, FinancialYear, Department, Payee, Language, Amount
- 例2 値：12/01/2018 | 22/01/2015 | 12/01/2018 | 22/01/2015 | 22/01/2015
  - 同じ表の列：OrganisationCode, PayMultipleFactor, RemunerationValue, Ratio, Period, ModelCalculation, OrganisationType, PayPolicyStatementU…

## g0029（1 列）
- 見出し：FinancialYear
- 例1 値：2012/13 | 2017/18 | 2013/14 | 2017/18 | 2013/14
  - 同じ表の列：OrganisationCode, EffectiveDate, Department, Payee, Language, Amount

## g0030（2 列）
- 見出し：Department
- 例1 値：Corporate Fraud | Environmental Health | Communications | Corporate Fraud | Licencing
  - 同じ表の列：OrganisationCode, EffectiveDate, FinancialYear, Payee, Language, Amount
- 例2 値：Communities | finance | ch Exec | DCLS | ch Exec
  - 同じ表の列：MCC, date, Net Amount

## g0031（1 列）
- 見出し：Payee
- 例1 値：MK Transcribing Services | Leicester City Council | Vista | Leicester City Council | Vista
  - 同じ表の列：OrganisationCode, EffectiveDate, FinancialYear, Department, Language, Amount

## g0032（1 列）
- 見出し：Language
- 例1 値：Telephone Interpreting Service - Annual… | BSL Interpretation | Braille | Transcription of Interview Tapes | Slovakian
  - 同じ表の列：OrganisationCode, EffectiveDate, FinancialYear, Department, Payee, Amount

## g0033（1 列）
- 見出し：Amount
- 例1 値：」17.00 | 」168.00 | 」150.00 | 」295.00 | 」120.00
  - 同じ表の列：OrganisationCode, EffectiveDate, FinancialYear, Department, Payee, Language

## g0034（1 列）
- 見出し：PayMultipleFactor
- 例1 値：Highest remuneration pay|Lowest remuner… | Highest remuneration pay|Median pay | Highest remuneration pay|Mean pay | Highest remuneration pay|Median pay | Highest remuneration pay|Lowest remuner…
  - 同じ表の列：OrganisationCode, EffectiveDate, RemunerationValue, Ratio, Period, ModelCalculation, OrganisationType, PayPolicyStatementU…

## g0035（1 列）
- 見出し：RemunerationValue
- 例1 値：96642|24780 | 88771|22417 | 100000|24876 | 100000|24155 | 97604|15896
  - 同じ表の列：OrganisationCode, EffectiveDate, PayMultipleFactor, Ratio, Period, ModelCalculation, OrganisationType, PayPolicyStatementU…

## g0036（1 列）
- 見出し：Ratio
- 例1 値：6.78:1 | 3.3:1 | 7.2:1 | 4.14:1 | 4.64:1
  - 同じ表の列：OrganisationCode, EffectiveDate, PayMultipleFactor, RemunerationValue, Period, ModelCalculation, OrganisationType, PayPolicyStatementU…

## g0037（1 列）
- 見出し：Period
- 例1 値：2014/15 | 2012/13 | 2015/16 | 2013/14 | 2017/18
  - 同じ表の列：OrganisationCode, EffectiveDate, PayMultipleFactor, RemunerationValue, Ratio, ModelCalculation, OrganisationType, PayPolicyStatementU…

## g0038（1 列）
- 見出し：ModelCalculation
- 例1 値：4 | 1 | 4 | 3 | 3
  - 同じ表の列：OrganisationCode, EffectiveDate, PayMultipleFactor, RemunerationValue, Ratio, Period, OrganisationType, PayPolicyStatementU…

## g0039（1 列）
- 見出し：OrganisationType
- 例1 値：DC | DC | DC | DC | DC
  - 同じ表の列：OrganisationCode, EffectiveDate, PayMultipleFactor, RemunerationValue, Ratio, Period, ModelCalculation, PayPolicyStatementU…

## g0040（1 列）
- 見出し：PayPolicyStatementURL
- 例1 値：http://w3.blaby.gov.uk/decision-making/… | http://w3.blaby.gov.uk/decision-making/… | http://w3.blaby.gov.uk/decision-making/… | http://w3.blaby.gov.uk/decision-making/… | http://w3.blaby.gov.uk/decision-making/…
  - 同じ表の列：OrganisationCode, EffectiveDate, PayMultipleFactor, RemunerationValue, Ratio, Period, ModelCalculation, OrganisationType

## g0041（3 列）
- 見出し：SiteReference
- 例1 値：16 | 15 | 11 | 60 | 27
  - 同じ表の列：OrganisationURI, SiteplanURL - Colum…, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：693 | 372 | 408 | 252 | 692
  - 同じ表の列：OrganisationURI, GeoY, GeoX, SiteplanURL, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0042（1 列）
- 見出し：SiteplanURL - Column D
- 例1 値：https://west-norfolk-consult.objective.… | https://west-norfolk-consult.objective.… | https://west-norfolk-consult.objective.… | https://west-norfolk-consult.objective.… | https://west-norfolk-consult.objective.…
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate

## g0043（10 列）
- 見出し：GeoY
- 例1 値：340648 | 303173 | 325270 | 300095 | 320125
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL - Colum…, GeoX, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：223124 | 221653 | 221997 | 222874 | 222717
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoX, Hectares, Deliverable

## g0044（9 列）
- 見出し：GeoX
- 例1 値：559682 | 573296 | 562188 | 562137 | 561928
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL - Colum…, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：394827 | 395564 | 393651 | 395017 | 395712
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, SiteplanURL, CoordinateReference…, GeoY, Hectares, Deliverable

## g0045（4 列）
- 見出し：PermissionType
- 例1 値：full planning permission | full planning permission | other | full planning permission | full planning permission
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL - Colum…, GeoY, GeoX, Hectares, PlanningStatus, PermissionDate
- 例2 値：full planning permission | outline planning permission | other | full planning permission | other
  - 同じ表の列：OrganisationURI, SiteReference, GeoX, GeoY, Hectares, PlanningStatus, PermissionDate, PlanningHistory

## g0046（9 列）
- 見出し：PermissionDate
- 例1 値：08/02/2017 | 17/02/2016 | 21/06/2007 | 02/05/2019 | 29/03/2018
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL - Colum…, GeoY, GeoX, Hectares, PlanningStatus, PermissionType
- 例2 値：05/02/2021 | 19/05/2022 | 16/11/2015 | 02/09/2021 | 29/03/2019
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, Deliverable, PlanningStatus

## g0047（1 列）
- 見出し：Body
- 例1 値：Bristol City council | Bristol City council | Bristol City council | Bristol City council | Bristol City council
  - 同じ表の列：Amount, Pay Date, Transaction Number

## g0048（3 列）
- 見出し：Amount
- 例1 値：18,925.00 | 5,337.30 | 6,056.16 | 2,215.84 | 5,300.00
  - 同じ表の列：Body, Pay Date, Transaction Number
- 例2 値：3,950.17 | 26,869.18 | 59,014.63 | 9,567.32 | 38,430.00
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number

## g0049（1 列）
- 見出し：Pay Date
- 例1 値：27/01/2020 | 16/01/2020 | 13/01/2020 | 02/01/2020 | 23/01/2020
  - 同じ表の列：Body, Amount, Transaction Number

## g0050（17 列）
- 見出し：Transaction Number
- 例1 値：92193684 | 30764109 | 30770299 | 30770482 | 30769467
  - 同じ表の列：Body, Amount, Pay Date
- 例2 値：1121690 | 1121444 | 1120748 | 1120690 | 1121690
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Amount

## g0051（1 列）
- 見出し：Organisation Label
- 例1 値：Broadland | Broadland | Broadland | Broadland | Broadland
  - 同じ表の列：Parish, Site Reference, Easting, Northing, Hectares, Deliverable, Planning Status, Permission Type

## g0052（2 列）
- 見出し：Parish
- 例1 値：Aylsham | Hellesdon | Aylsham | Thorpe St Andrew | Thorpe St Andrew
  - 同じ表の列：Organisation Label, Site Reference, Easting, Northing, Hectares, Deliverable, Planning Status, Permission Type
- 例2 値：Bramerton | Wymondham | Tivetshall St Mary | Costessey | Wymondham
  - 同じ表の列：District, PropUse, Alt_Ref, PlanningSt, Brownfield, Easting, Northing, Weblink

## g0053（1 列）
- 見出し：Site Reference
- 例1 値：B/DRA/004 | B/AYL/001 | B/HOR/002 | B/AYL/0003 | B/HEL/001
  - 同じ表の列：Organisation Label, Parish, Easting, Northing, Hectares, Deliverable, Planning Status, Permission Type

## g0054（4 列）
- 見出し：Easting
- 例1 値：618149 | 625809 | 620503 | 625384 | 635350
  - 同じ表の列：Organisation Label, Parish, Site Reference, Northing, Hectares, Deliverable, Planning Status, Permission Type
- 例2 値：526630 | 526630 | 526630 | 530121 | 530121
  - 同じ表の列：Site Code, Site Type, Bulletin Date, Bulletin Date Forma…, NO2 Air Quality Band, NO2 Air Quality Ind…, Latest Capture, Latest Week

## g0055（3 列）
- 見出し：Northing
- 例1 値：313200 | 323835 | 320100 | 308185 | 317653
  - 同じ表の列：Organisation Label, Parish, Site Reference, Easting, Hectares, Deliverable, Planning Status, Permission Type
- 例2 値：183894 | 182335 | 182256 | 181588 | 181601
  - 同じ表の列：Building Number, Unit Count, Responsible Authori…, Ward Code, Easting, Spatial Accuracy, Location, Organisation URI

## g0056（1 列）
- 見出し：Planning Status
- 例1 値：Permissioned | Permissioned | Permissioned | Permissioned | Permissioned
  - 同じ表の列：Organisation Label, Parish, Site Reference, Easting, Northing, Hectares, Deliverable, Permission Type

## g0057（1 列）
- 見出し：Permission Type
- 例1 値：Reserved matters approval | Full planning permission | Full planning permission | Reserved matters approval | Outline planning permission
  - 同じ表の列：Organisation Label, Parish, Site Reference, Easting, Northing, Hectares, Deliverable, Planning Status

## g0058（1 列）
- 見出し：Permission Date
- 例1 値：30/03/2023 | 18/09/2015 | 24/10/2016 | 14/03/2025 | 20/05/2020
  - 同じ表の列：Organisation Label, Parish, Site Reference, Easting, Northing, Hectares, Deliverable, Planning Status

## g0059（1 列）
- 見出し：SiteReference
- 例1 値：HL/2890/00 | HL/2264/00 | HL/2178/00 | HL/2492/00 | HL/3178/00
  - 同じ表の列：OrganisationURI, SiteplanURL, GeoY, GeoX, Hectares, Deliverable, PlanningStatus, PermissionType

## g0060（15 列）
- 見出し：SiteplanURL
- 例1 値：http://maps.bury.gov.uk/webmaplayers8/M… | http://maps.bury.gov.uk/webmaplayers8/M… | http://maps.bury.gov.uk/webmaplayers8/M… | http://maps.bury.gov.uk/webmaplayers8/M… | http://maps.bury.gov.uk/webmaplayers8/M…
  - 同じ表の列：OrganisationURI, SiteReference, GeoY, GeoX, Hectares, Deliverable, PlanningStatus, PermissionType
- 例2 値：https://maps.cheltenham.gov.uk/map/Auro… | https://maps.cheltenham.gov.uk/map/Auro… | https://maps.cheltenham.gov.uk/map/Auro… | https://maps.cheltenham.gov.uk/map/Auro… | https://maps.cheltenham.gov.uk/map/Auro…
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0061（14 列）
- 見出し：PlanningStatus
- 例1 値：not permissioned | permissioned | not permissioned | not permissioned | not permissioned
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, GeoY, GeoX, Hectares, Deliverable, PermissionType
- 例2 値：not permissioned | not permissioned | permissioned | permissioned | not permissioned
  - 同じ表の列：organisationuri, sitereference, hectares, permissiontype, permissiondate, deliverable, netdwellingsrangefr…, netdwellingsrangeto

## g0062（1 列）
- 見出し：sitereference
- 例1 値：C420 | C270 | N67b | C335 | R195
  - 同じ表の列：organisationuri, hectares, planningstatus, permissiontype, permissiondate, deliverable, netdwellingsrangefr…, netdwellingsrangeto

## g0063（4 列）
- 見出し：permissiondate
- 例1 値：2017-05-21 | 2023-03-30 | 2021-03-01 | 2017-04-19 | 2017-10-03
  - 同じ表の列：organisationuri, sitereference, hectares, planningstatus, permissiontype, deliverable, netdwellingsrangefr…, netdwellingsrangeto
- 例2 値：2023-02-15 | 2023-11-15 | 2021-08-11 | 2023-10-12 | 2018-12-05
  - 同じ表の列：OrganisationURI, OrganisationLabel, SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus

## g0064（1 列）
- 見出し：netdwellingsrangefrom
- 例1 値：3 | 44 | 8 | 25 | 23
  - 同じ表の列：organisationuri, sitereference, hectares, planningstatus, permissiontype, permissiondate, deliverable, netdwellingsrangeto

## g0065（1 列）
- 見出し：netdwellingsrangeto
- 例1 値：8 | 20 | 40 | 9 | 6
  - 同じ表の列：organisationuri, sitereference, hectares, planningstatus, permissiontype, permissiondate, deliverable, netdwellingsrangefr…

## g0066（1 列）
- 見出し：firstaddeddate
- 例1 値：2022-12-12 | 2017-09-01 | 2023-12-12 | 2017-09-01 | 2021-12-20
  - 同じ表の列：organisationuri, sitereference, hectares, planningstatus, permissiontype, permissiondate, deliverable, netdwellingsrangefr…

## g0067（1 列）
- 見出し：OrganisationURI
- 例1 値：http://statistics.data.gov.uk/id/local-… | http://statistics.data.gov.uk/id/local-… | http://statistics.data.gov.uk/id/local-… | http://statistics.data.gov.uk/id/local-… | http://statistics.data.gov.uk/id/local-…
  - 同じ表の列：OrganisationLabel, Organisation Unit, TransactionNumber, Invoice Ref., Expense Type, Purpose, Payment Date, Amount

## g0068（5 列）
- 見出し：OrganisationLabel
- 例1 値：Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council
  - 同じ表の列：OrganisationURI, Organisation Unit, TransactionNumber, Invoice Ref., Expense Type, Purpose, Payment Date, Amount
- 例2 値：Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council
  - 同じ表の列：OrganisationURI, SiteReference, SiteplanURL, CoordinateReference…, GeoX, GeoY, Hectares, Deliverable

## g0069（1 列）
- 見出し：Organisation Unit
- 例1 値：Telephones | Cemetery, Crematorium and Churchyards | Adaptations for the Disabled (CBC) | Car Parks - Off Street Operations | General Fund Balance Sheet
  - 同じ表の列：OrganisationURI, OrganisationLabel, TransactionNumber, Invoice Ref., Expense Type, Purpose, Payment Date, Amount

## g0070（1 列）
- 見出し：TransactionNumber
- 例1 値：10031534 | 14075136 | 14074944 | 14074718 | 14075029
  - 同じ表の列：OrganisationURI, OrganisationLabel, Organisation Unit, Invoice Ref., Expense Type, Purpose, Payment Date, Amount

## g0071（1 列）
- 見出し：Invoice Ref.
- 例1 値：7402588218 | 36510 | Bank Transactions | 28920 | 1890
  - 同じ表の列：OrganisationURI, OrganisationLabel, Organisation Unit, TransactionNumber, Expense Type, Purpose, Payment Date, Amount

## g0072（1 列）
- 見出し：Expense Type
- 例1 値：R1100-URB101 | C1107-CAH035 | R4000-ECD101 | R4408-FIE040 | R2083-REC111
  - 同じ表の列：OrganisationURI, OrganisationLabel, Organisation Unit, TransactionNumber, Invoice Ref., Purpose, Payment Date, Amount

## g0073（1 列）
- 見出し：Purpose
- 例1 値：IT - Purchase of Hardware | Water Services - Metered | Construction | Contract Cleaning | Services - Fees and Charges
  - 同じ表の列：OrganisationURI, OrganisationLabel, Organisation Unit, TransactionNumber, Invoice Ref., Expense Type, Payment Date, Amount

## g0074（2 列）
- 見出し：Payment Date
- 例1 値：31/01/2020 | 17/01/2020 | 17/01/2020 | 03/01/2020 | 13/01/2020
  - 同じ表の列：OrganisationURI, OrganisationLabel, Organisation Unit, TransactionNumber, Invoice Ref., Expense Type, Purpose, Amount
- 例2 値：11/12/2014 | 02/10/2014 | 18/12/2014 | 04/12/2014 | 20/11/2014
  - 同じ表の列：Organisation, Service Area, Cost Centre, Expense Type, Transaction No., Amount, Capital Revenue, Supplier ID

## g0075（5 列）
- 見出し：Amount
- 例1 値：672.00 | 92,884.88 | 1,035.82 | 1,739.75 | 516.60
  - 同じ表の列：OrganisationURI, OrganisationLabel, Organisation Unit, TransactionNumber, Invoice Ref., Expense Type, Purpose, Payment Date
- 例2 値：23,225.27 | 35,604.50 | 103,081.08 | 334.00 | 57,953.12
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, VAT Included

## g0076（1 列）
- 見出し：Project Reference
- 例1 値：CBC0048P | CBC0012P | CBC0135P | CBC0262P | CBC0181P
  - 同じ表の列：Start Date, End Date, Extension Date, Recurring Procureme…, Value, Classification, Supplier Classifica…, Annual Value

## g0077（1 列）
- 見出し：Start Date
- 例1 値：18-Oct-17 | 16-Jul-19 | 29-May-20 | 03-Feb-21 | 01-Feb-18
  - 同じ表の列：Project Reference, End Date, Extension Date, Recurring Procureme…, Value, Classification, Supplier Classifica…, Annual Value

## g0078（1 列）
- 見出し：End Date
- 例1 値：17-Oct-22 | 30-Jan-21 | 30-Jul-20 | 31-Dec-21 | 01-Sep-20
  - 同じ表の列：Project Reference, Start Date, Extension Date, Recurring Procureme…, Value, Classification, Supplier Classifica…, Annual Value

## g0079（1 列）
- 見出し：Extension Date
- 例1 値：31-Oct-21 | 24-Mar-24 | 01-May-21 | 11-Sep-19 | 01-Jan-18
  - 同じ表の列：Project Reference, Start Date, End Date, Recurring Procureme…, Value, Classification, Supplier Classifica…, Annual Value

## g0080（1 列）
- 見出し：Recurring Procurement
- 例1 値：FALSE | FALSE | FALSE | FALSE | FALSE
  - 同じ表の列：Project Reference, Start Date, End Date, Extension Date, Value, Classification, Supplier Classifica…, Annual Value

## g0081（1 列）
- 見出し：Value
- 例1 値：£42,580.00 | £249,600.00 | £150,000.00 | £173,233.00 | £33,016.20
  - 同じ表の列：Project Reference, Start Date, End Date, Extension Date, Recurring Procureme…, Classification, Supplier Classifica…, Annual Value

## g0082（1 列）
- 見出し：Classification
- 例1 値：Services | Works | Works | Services | Works
  - 同じ表の列：Project Reference, Start Date, End Date, Extension Date, Recurring Procureme…, Value, Supplier Classifica…, Annual Value

## g0083（1 列）
- 見出し：Supplier Classification (SME etc)
- 例1 値：SME | SME | SME | SME | SME
  - 同じ表の列：Project Reference, Start Date, End Date, Extension Date, Recurring Procureme…, Value, Classification, Annual Value

## g0084（1 列）
- 見出し：Annual Value
- 例1 値：£0.00 | £0.00 | £17,000.00 | £0.00 | £0.00
  - 同じ表の列：Project Reference, Start Date, End Date, Extension Date, Recurring Procureme…, Value, Classification, Supplier Classifica…

## g0085（1 列）
- 見出し：Option to Extend?
- 例1 値：No | No | No | No | Yes
  - 同じ表の列：Project Reference, Start Date, End Date, Extension Date, Recurring Procureme…, Value, Classification, Supplier Classifica…

## g0086（6 列）
- 見出し：Department Family
- 例1 値：Ministry of justice | Ministry of justice | Ministry of justice | Ministry of justice | Ministry of justice
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount
- 例2 値：Crown Prosecution Service | Crown Prosecution Service | Crown Prosecution Service | Crown Prosecution Service | Crown Prosecution Service
  - 同じ表の列：Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount, VAT Included

## g0087（7 列）
- 見出し：Entity
- 例1 値：CAFCASS | CAFCASS | CAFCASS | CAFCASS | CAFCASS
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount
- 例2 値：DFID | DFID | DFID | DFID | DFID
  - 同じ表の列：Department Family, Transaction Date, Expense Type, Expense Area, Transaction Number, Amount

## g0088（21 列）
- 見出し：Date
- 例1 値：25/01/2023 | 30/01/2023 | 06/01/2023 | 30/01/2023 | 23/01/2023
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Supplier, Transaction Number, Amount
- 例2 値：27/09/2017 | 21/09/2017 | 13/09/2017 | 15/09/2017 | 13/09/2017
  - 同じ表の列：Department Family, Entity, Expense Type, Expense Area, Supplier, Transaction Number, Amount, VAT Included

## g0089（1 列）
- 見出し：Expense Type
- 例1 値：Agency Practitioners | Contact rechargeable | Temp Business Support Staff | Rent | N-Cnt Computer Srvcs & Maint
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, Amount

## g0090（2 列）
- 見出し：Expense Area
- 例1 値：HQ | HQ | Op Service Areas | HQ | HQ
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, Amount
- 例2 値：South East Area | Specialist Fraud Division | Corporate | Corporate | Special Crime Division
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Supplier, Transaction Number, Amount, VAT Included

## g0091（1 列）
- 見出し：Supplier
- 例1 値：Community Resourcing Ltd t/a Retinue Sol | VSC Plus Ltd t/a Virtual Staff College | University of Warwick Science Park | Jigsaw24 | Child Action Northwest
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount

## g0092（1 列）
- 見出し：Carehome
- 例1 値：Homecroft | Fairmount Nursing Home | Turning Point | The Flowers Ltd | Abbeyfield Grove House
  - 同じ表の列：Town

## g0093（1 列）
- 見出し：Town
- 例1 値：Bradford | Bradford | Baildon | Bradford | Bradford
  - 同じ表の列：Carehome

## g0094（5 列）
- 見出し：PlanningHistory
- 例1 値：http://planning.cornwall.gov.uk/online-… | http://planning.cornwall.gov.uk/online-… | http://planning.cornwall.gov.uk/online-… | http://planning.cornwall.gov.uk/online-… | http://planning.cornwall.gov.uk/online-…
  - 同じ表の列：OrganisationURI, SiteReference, GeoX, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate
- 例2 値：https://publicaccess.guildford.gov.uk/o… | https://publicaccess.guildford.gov.uk/o… | https://publicaccess.guildford.gov.uk/o… | https://publicaccess.guildford.gov.uk/o… | https://publicaccess.guildford.gov.uk/o…
  - 同じ表の列：OrganisationURI, SiteReference, GeoX, GeoY, SiteplanURL, Hectares, PlanningStatus, PermissionType

## g0095（1 列）
- 見出し：Measure
- 例1 値：Magistrates' Court - Percentage of GPs … | All data relates to the performance of … | Employee Engagement Index* | Crown Court - Conviction Rate | 1. CPS data are available through its C…
  - 同じ表の列：16/17-Q1, 16/17-Q2, 16/17-Q3, 16/17-Q4

## g0096（1 列）
- 見出し：16/17-Q1
- 例1 値：83.1% | 8.2 | 2.93 | 5.47 | 75.8%
  - 同じ表の列：Measure, 16/17-Q2, 16/17-Q3, 16/17-Q4

## g0097（1 列）
- 見出し：16/17-Q2
- 例1 値：83.2% | 2.96 | 70.3% | 83.3% | 84.2%
  - 同じ表の列：Measure, 16/17-Q1, 16/17-Q3, 16/17-Q4

## g0098（1 列）
- 見出し：16/17-Q3
- 例1 値：84.6% | 83.2% | 75.5% | 8.2 | 1.69
  - 同じ表の列：Measure, 16/17-Q1, 16/17-Q2, 16/17-Q4

## g0099（1 列）
- 見出し：16/17-Q4
- 例1 値：85.5% | 83.4% | 3.52 | 76.4% | 57.6%
  - 同じ表の列：Measure, 16/17-Q1, 16/17-Q2, 16/17-Q3

## g0100（3 列）
- 見出し：Entity
- 例1 値：Crown Prosecution Service | Crown Prosecution Service | Crown Prosecution Service | Crown Prosecution Service | Crown Prosecution Service
  - 同じ表の列：Department Family, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount, VAT Included
- 例2 値：Department of Health | Department of Health | Department of Health | Department of Health | Department of Health
  - 同じ表の列：Departmental Family, Date, Expense Type, Expense Area, Supplier, Amount

## g0101（1 列）
- 見出し：Expense Type
- 例1 値：Transcriptions And Translation | Ordinary Witness Expenses | Crown Court Graduated Fee Scheme | Logica contract | Facilities Management
  - 同じ表の列：Department Family, Entity, Date, Expense Area, Supplier, Transaction Number, Amount, VAT Included

## g0102（5 列）
- 見出し：Supplier
- 例1 値：Clarity Travel Management | Clarity Travel Management | Brooke D | CBAC Services Rochford | Laws Simon
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Transaction Number, Amount, VAT Included
- 例2 値：BARINGA PARTNERS LLP | Cheesecake Energy Ltd | AI Build Ltd | Gemserv Limited | Gemserv Limited
  - 同じ表の列：Date of Payment, Expense Type, Expense Area, Transaction Number, Amount, Supplier Type

## g0103（1 列）
- 見出し：VAT Included
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount

## g0104（2 列）
- 見出し：Supplier Type
- 例1 値：Not available | Not available | Not available | Not available | Not available
  - 同じ表の列：Department Family, Entity, Date, Expense Type, Expense Area, Supplier, Transaction Number, Amount
- 例2 値：Public Sector | Public Sector
  - 同じ表の列：Department family, Entity, Date, Expense type, Expense area, Supplier, Transaction number, Amount

## g0105（1 列）
- 見出し：Transaction Type
- 例1 値：Individual GPC | Individual GPC | Individual GPC | Individual GPC | Individual GPC
  - 同じ表の列：Transaction Date, Transaction Referen…, Merchant, Total

## g0106（3 列）
- 見出し：Transaction Date
- 例1 値：05/04/2016 | 31/08/2016 | 31/08/2016 | 03/05/2016 | 06/08/2016
  - 同じ表の列：Transaction Type, Transaction Referen…, Merchant, Total
- 例2 値：15/08/2023 | 01/08/2023 | 18/08/2023 | 21/08/2023 | 31/08/2023
  - 同じ表の列：Transaction Referen…, Merchant, Total

## g0107（3 列）
- 見出し：Transaction Reference
- 例1 値：DECC4744589117 | DECC4798279709 | DECC4735284823 | BIS86464 | DECC4852180919
  - 同じ表の列：Transaction Type, Transaction Date, Merchant, Total
- 例2 値：DESNZ1154441 | DESNZ1159897 | DESNZ1162739 | DESNZ1163927 | DESNZ1154957
  - 同じ表の列：Transaction Date, Merchant, Total

## g0108（1 列）
- 見出し：Merchant
- 例1 値：Conference Solutions | Chartered Institute Of Management Accou… | Atlassian, Sydney | Amazon Web Services | Lyreco Uk Ltd
  - 同じ表の列：Transaction Type, Transaction Date, Transaction Referen…, Total

## g0109（1 列）
- 見出し：Total
- 例1 値：549.61 | 545.23 | 1104.00 | 594.00 | 1675.01
  - 同じ表の列：Transaction Type, Transaction Date, Transaction Referen…, Merchant

## g0110（1 列）
- 見出し：GMPP ID Number
- 例1 値：CO_0022_1819-Q4 | FCO_0011_1718-Q3 | MOD_0117_1718-Q2 | MOD_0077_1213-Q1 | DH_0060_1617-Q1
  - 同じ表の列：SRO

## g0111（1 列）
- 見出し：SRO
- 例1 値：Matthew Lodge | Matthew Lodge | Tim Hodgson | Paul Marshall | Cavendish Elithorn
  - 同じ表の列：GMPP ID Number

## g0112（2 列）
- 見出し：Department
- 例1 値：Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and…
  - 同じ表の列：Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Net Total
- 例2 値：Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and…
  - 同じ表の列：Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0113（1 列）
- 見出し：Entity
- 例1 値：Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and… | Department for Business, Innovation and…
  - 同じ表の列：Department, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number, Net Total

## g0114（8 列）
- 見出し：Date of Payment
- 例1 値：01/02/2011 | 08/02/2011 | 02/02/2011 | 01/02/2011 | 07/02/2011
  - 同じ表の列：Department, Entity, Expense Type, Expense Area, Supplier, Transaction Number, Net Total
- 例2 値：14/08/2023 | 15/08/2023 | 16/08/2023 | 02/08/2023 | 04/08/2023
  - 同じ表の列：Expense Type, Expense Area, Supplier, Transaction Number, Amount, Supplier Type

## g0115（1 列）
- 見出し：Expense Type
- 例1 値：Mobile Phones | Criminal Law and Prosecution Work | Air Fares - Overseas (Programme) | Air Fares - Overseas (Programme) | Mobile Line Rental
  - 同じ表の列：Department, Entity, Date of Payment, Expense Area, Supplier, Transaction Number, Net Total

## g0116（1 列）
- 見出し：Expense Area
- 例1 値：Chief Economic Advisor &BRE Group - Bet… | Ministerial and Parliamentary Support T… | Legal, People & Communications Group - … | Knowledge and Innovation Group - Resear… | Knowledge and Innovation Group - UK Spa…
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Supplier, Transaction Number, Net Total

## g0117（1 列）
- 見出し：Supplier
- 例1 値：Personal Expense, Name Witheld. | UNITE THE UNION - AMICUS SECTION | BRITISH TELECOMMUNICATIONS plc (BT) | THE PARLIAMENTARY AND SCIENTIFIC COMMIT… | PARITY RESOURCES LTD
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Transaction Number, Net Total

## g0118（1 列）
- 見出し：Net Total
- 例1 値：81.3 | 30 | 140 | 8.2 | 312.47
  - 同じ表の列：Department, Entity, Date of Payment, Expense Type, Expense Area, Supplier, Transaction Number

## g0119（1 列）
- 見出し：Organisation type
- 例1 値：Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Crown Non Departmental Public Body | Non-Ministerial Department | Executive Non-Departmental Public Body
  - 同じ表の列：Main, parent or spo…, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs…, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

## g0120（1 列）
- 見出し：Main, parent or sponsoring department:
- 例1 値：Department for Business, Innovation & S… | Department for Business, Innovation & S… | Department for Business, Innovation & S… | Department for Business, Innovation & S… | Department for Business, Innovation & S…
  - 同じ表の列：Organisation type, Payroll staff, Number of non-payro…, Grand Total (workfo…, Payroll staff costs…, Non-Payroll staff (…, Grand Total paybill…, Comments and notes

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
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
