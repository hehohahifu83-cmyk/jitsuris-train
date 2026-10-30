# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Sir Jeremy Heywood's External Meetings January 2014
- 例1 値：Rothschild - Discussion on Business Iss… | Newsnight - Discussion on the Civil Ser… | Beacon UK - Discussion on Mental Health… | Accenture - To discuss youth unemployme… | Sikh Community Leaders - Discussion on …
  - 同じ表の列：Sir Jeremy Heywood'…, Sir Jeremy Heywood'…

## g0002（1 列）
- 見出し：Sir Jeremy Heywood's External Meetings February 2014
- 例1 値：Information Commissioner - Discussion o… | Anglo American plc, Laing O’Rourke and … | Hugo Swire & Sikh Community Leaders - M… | Centrica - Introductory meeting with ne… | Network Rail - Introductory meeting wit…
  - 同じ表の列：Sir Jeremy Heywood'…, Sir Jeremy Heywood'…

## g0003（1 列）
- 見出し：Sir Jeremy Heywood's External Meetings March 2014
- 例1 値：The Guardian - Discussion on the Civil … | Marks & Spencer - Discussion on ‘Way to… | Tesco - Discussion on UK Economy | Deutsche Bank - Discussion on Financial… | Citibank - Introductory meeting with ne…
  - 同じ表の列：Sir Jeremy Heywood'…, Sir Jeremy Heywood'…

## g0004（1 列）
- 見出し：DESTINATION
- 例1 値：Sunningdale | Rome | London | Sunningdale | London
  - 同じ表の列：PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost 」

## g0005（1 列）
- 見出し：PURPOSE
- 例1 値：Ministry of Defence/Foreign & Commonwea… | PURPOSE | Spring Sunningdale | PURPOSE | Meeting with senior official
  - 同じ表の列：DESTINATION, TRAVEL, OTHER (Including Ho…, Total Cost 」

## g0006（2 列）
- 見出し：TRAVEL
- 例1 値：Lunch | Air | Dinner | Air | TRAVEL
  - 同じ表の列：DESTINATION, PURPOSE, OTHER (Including Ho…, Total Cost 」
- 例2 値：Breakfast | Reception | Reception | Dinner | Dinner
  - 同じ表の列：DATES, DESTINATION, PURPOSE, OTHER (Including Ho…, Total Cost £

## g0007（1 列）
- 見出し：OTHER (Including Hospitality Given)
- 例1 値：OTHER (Including Hospitality Given) | 」259.48 | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given)
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, Total Cost 」

## g0008（1 列）
- 見出し：Total Cost 」
- 例1 値：17.33 | 1,005.68 | 8 | Total Cost 」 | Total Cost 」
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, OTHER (Including Ho…

## g0009（1 列）
- 見出し：DESTINATION
- 例1 値：Beijing | London | London | DESTINATION | Goldman Sachs
  - 同じ表の列：PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost 」

## g0010（1 列）
- 見出し：PURPOSE
- 例1 値：Meetings with senior government officia… | Visit to staff | Journey cancelled due to Ministerial me… | Use of official car | PURPOSE
  - 同じ表の列：DESTINATION, TRAVEL, OTHER (Including Ho…, Total Cost 」

## g0011（1 列）
- 見出し：TRAVEL
- 例1 値：Type of Hospitality Received | Reception | Air | Air | 120.30
  - 同じ表の列：DESTINATION, PURPOSE, OTHER (Including Ho…, Total Cost 」

## g0012（1 列）
- 見出し：OTHER (Including Hospitality Given)
- 例1 値：OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given) | OTHER (Including Hospitality Given)
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, Total Cost 」

## g0013（1 列）
- 見出し：Total Cost 」
- 例1 値：0.00 | 48.38 | Total Cost 」 | 46.58 | 0.00
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, OTHER (Including Ho…

## g0014（1 列）
- 見出し：Organisation
- 例1 値：Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council
  - 同じ表の列：OrganisationLabel, Organisation_2, OrganisationLabel_2, UPRN, AssetCode, PostTown, GeoX, GeoY

## g0015（1 列）
- 見出し：OrganisationLabel
- 例1 値：23UB | 23UB | 23UB | 23UB | 23UB
  - 同じ表の列：Organisation, Organisation_2, OrganisationLabel_2, UPRN, AssetCode, PostTown, GeoX, GeoY

## g0016（1 列）
- 見出し：Organisation_2
- 例1 値：Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council | Cheltenham Borough Council
  - 同じ表の列：Organisation, OrganisationLabel, OrganisationLabel_2, UPRN, AssetCode, PostTown, GeoX, GeoY

## g0017（1 列）
- 見出し：OrganisationLabel_2
- 例1 値：23UB | 23UB | 23UB | 23UB | 23UB
  - 同じ表の列：Organisation, OrganisationLabel, Organisation_2, UPRN, AssetCode, PostTown, GeoX, GeoY

## g0018（1 列）
- 見出し：UPRN
- 例1 値：010012809856 | 010012809838 | 010012809557 | 200002676518 | 100121370433
  - 同じ表の列：Organisation, OrganisationLabel, Organisation_2, OrganisationLabel_2, AssetCode, PostTown, GeoX, GeoY

## g0019（1 列）
- 見出し：AssetCode
- 例1 値：09/00200/Land | 09/00667/Land and Building | 13/00008/Land | 09/00054/Land and Building | 09/05040/Land and Building
  - 同じ表の列：Organisation, OrganisationLabel, Organisation_2, OrganisationLabel_2, UPRN, PostTown, GeoX, GeoY

## g0020（2 列）
- 見出し：PostTown
- 例1 値：Cheltenham | Cheltenham | Cheltenham | Cheltenham | Cheltenham
  - 同じ表の列：Organisation, OrganisationLabel, Organisation_2, OrganisationLabel_2, UPRN, AssetCode, GeoX, GeoY
- 例2 値：Ambleside | Bowness | Kendal | Ulverston | Windermere
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, UPRN, UniqueAssetIdentity, CoordinateReference…, GeoX, GeoY

## g0021（2 列）
- 見出し：GeoX
- 例1 値：395265 | 391309 | 394723 | 394876 | 395339
  - 同じ表の列：Organisation, OrganisationLabel, Organisation_2, OrganisationLabel_2, UPRN, AssetCode, PostTown, GeoY
- 例2 値：341008 | 351586 | 328916 | 321276 | 353279
  - 同じ表の列：OrganisationLabel, OrganisationURI, EffectiveDate, UPRN, UniqueAssetIdentity, PostTown, CoordinateReference…, GeoY

## g0022（1 列）
- 見出し：GeoY
- 例1 値：223787 | 222923 | 222857 | 222516 | 219796
  - 同じ表の列：Organisation, OrganisationLabel, Organisation_2, OrganisationLabel_2, UPRN, AssetCode, PostTown, GeoX

## g0023（1 列）
- 見出し：TenureType
- 例1 値：Freehold | Freehold | Freehold | Freehold | Freehold
  - 同じ表の列：Organisation, OrganisationLabel, Organisation_2, OrganisationLabel_2, UPRN, AssetCode, PostTown, GeoX

## g0024（1 列）
- 見出し：BP
- 例1 値：Natasha Zappone / Amy Watkins | Jonathan Green | Paul Farthing | Paul Farthing | Natasha Zappone / Amy Watkins
  - 同じ表の列：Title, Procurement Category, Estimated Start dat…, Procurement Referen…, Estimated value ran…

## g0025（1 列）
- 見出し：Title
- 例1 値：Revision of DIT's methodology | Building Materials Surveys 2020/21 | Allowance Calculator | Cumulative Environmental Impacts of Off… | Eyecare Provision
  - 同じ表の列：BP, Procurement Category, Estimated Start dat…, Procurement Referen…, Estimated value ran…

## g0026（1 列）
- 見出し：Procurement Category
- 例1 値：Prof Services - Other | Prof Services - Other | Research | Research | Prof Services - Other
  - 同じ表の列：BP, Title, Estimated Start dat…, Procurement Referen…, Estimated value ran…

## g0027（1 列）
- 見出し：Estimated Start date of requirement
- 例1 値：Start Date not yet Confirmed | 0 to 6 Months | 0 to 6 Months | 0 to 6 Months | 0 to 6 Months
  - 同じ表の列：BP, Title, Procurement Category, Procurement Referen…, Estimated value ran…

## g0028（1 列）
- 見出し：Procurement Reference number, once live
- 例1 値：(blank) | (blank) | (blank) | (blank) | (blank)
  - 同じ表の列：BP, Title, Procurement Category, Estimated Start dat…, Estimated value ran…

## g0029（1 列）
- 見出し：Estimated value range of the contract
- 例1 値：£1M to £5M | £10k to £500K | £10k to £500K | £10k to £500K | £10k to £500K
  - 同じ表の列：BP, Title, Procurement Category, Estimated Start dat…, Procurement Referen…

## g0030（2 列）
- 見出し：Permanent secretary
- 例1 値：Alex Chisholm | Alex Chisholm | Alex Chisholm | Alex Chisholm | Alex Chisholm
  - 同じ表の列：Date, Purpose of meeting
- 例2 値：Dave Hartnett | Dave Hartnett | Dave Hartnett | Dave Hartnett | Dave Hartnett
  - 同じ表の列：Date, Purpose of meeting

## g0031（2 列）
- 見出し：Date
- 例1 値：August 2017 | July 2017 | August 2017 | July 2017 | July 2017
  - 同じ表の列：Permanent secretary, Purpose of meeting
- 例2 値：May 2010 | May 2010 | May 2010 | May 2010 | May 2010
  - 同じ表の列：Minister, Purpose of meeting

## g0032（1 列）
- 見出し：Purpose of meeting
- 例1 値：To discuss Brexit | To discuss Brexit and Industrial Strate… | To discuss Blockchain | To discuss Energy | To discuss Energy
  - 同じ表の列：Permanent secretary, Date

## g0033（1 列）
- 見出し：Grade
- 例1 値：Total number of employees eligible for … | Table 2: HR Performance Data 2012-2013 | C | D | Total Number of people awarded a bonus
  - 同じ表の列：Total, Women, Ethnic Minority, Disabled

## g0034（1 列）
- 見出し：Total
- 例1 値：142 | 42 | 18 | 106 | 4
  - 同じ表の列：Grade, Women, Ethnic Minority, Disabled

## g0035（1 列）
- 見出し：Women
- 例1 値：125 (42.2%) | 146 (64.0%) | 41 (39.8%) | 21 (50.0%) | Men
  - 同じ表の列：Grade, Total, Ethnic Minority, Disabled

## g0036（1 列）
- 見出し：Ethnic Minority
- 例1 値：36 (49.3%) | 8 (7.5%) | 5 (11.9%) | 24 (8.1%) | 1 (3.7%)
  - 同じ表の列：Grade, Total, Women, Disabled

## g0037（1 列）
- 見出し：Disabled
- 例1 値：7 (2.4%) | Ethnic Minority | 8 (5.6%) | 21 (9.2%) | 0
  - 同じ表の列：Grade, Total, Women, Ethnic Minority

## g0038（1 列）
- 見出し：Engineering
- 例1 値：Gas Industry | Signmaking | MES Plumbing | Glass Industry Occupations | Laboratory Technicians
  - 同じ表の列：10, 20, 10_2, -

## g0039（1 列）
- 見出し：10
- 例1 値：- | - | - | - | -
  - 同じ表の列：Engineering, 20, 10_2, -

## g0040（1 列）
- 見出し：20
- 例1 値：- | - | 100 | - | -
  - 同じ表の列：Engineering, 10, 10_2, -

## g0041（1 列）
- 見出し：10_2
- 例1 値：10 | - | - | - | -
  - 同じ表の列：Engineering, 10, 20, -

## g0042（1 列）
- 見出し：-
- 例1 値：- | 10 | - | - | -
  - 同じ表の列：Engineering, 10, 20, 10_2

## g0043（1 列）
- 見出し：RespondentID
- 例1 値：2158452114 | 1927668614 | 1994086335 | 1918374918 | 1931648267
  - 同じ表の列：CollectorID, StartDate, EndDate, Which of the follow…, Which of the follow…, Which geographical …, Is education, learn…, Do you provide any …

## g0044（1 列）
- 見出し：CollectorID
- 例1 値：28515407 | 28515407 | 28515407 | 28515407 | 28515407
  - 同じ表の列：RespondentID, StartDate, EndDate, Which of the follow…, Which of the follow…, Which geographical …, Is education, learn…, Do you provide any …

## g0045（1 列）
- 見出し：StartDate
- 例1 値：07/31/2012 | 07/31/2012 | 08/01/2012 | 07/31/2012 | 08/17/2012
  - 同じ表の列：RespondentID, CollectorID, EndDate, Which of the follow…, Which of the follow…, Which geographical …, Is education, learn…, Do you provide any …

## g0046（1 列）
- 見出し：EndDate
- 例1 値：08/17/2012 | 08/15/2012 | 08/22/2012 | 07/31/2012 | 08/30/2012
  - 同じ表の列：RespondentID, CollectorID, StartDate, Which of the follow…, Which of the follow…, Which geographical …, Is education, learn…, Do you provide any …

## g0047（1 列）
- 見出し：Which of the following categories best describes your organi
- 例1 値：1. Registered Charity | 1. Registered Charity | 1. Registered Charity | 1. Registered Charity | 1. Registered Charity
  - 同じ表の列：RespondentID, CollectorID, StartDate, EndDate, Which of the follow…, Which geographical …, Is education, learn…, Do you provide any …

## g0048（1 列）
- 見出し：Which of the following activities does your organisation und
- 例1 値：1. Business and Professional Associatio…
  - 同じ表の列：RespondentID, CollectorID, StartDate, EndDate, Which of the follow…, Which geographical …, Is education, learn…, Do you provide any …

## g0049（1 列）
- 見出し：Which geographical level does your organisation operate at?
- 例1 値：1. Neighbourhood or community | 1. Neighbourhood or community | 1. Neighbourhood or community | 1. Neighbourhood or community | 1. Neighbourhood or community
  - 同じ表の列：RespondentID, CollectorID, StartDate, EndDate, Which of the follow…, Which of the follow…, Is education, learn…, Do you provide any …

## g0050（1 列）
- 見出し：Is education, learning or teaching one of your aims as set o
- 例1 値：1. Yes | 1. Yes | 1. Yes | 1. Yes | 1. Yes
  - 同じ表の列：RespondentID, CollectorID, StartDate, EndDate, Which of the follow…, Which of the follow…, Which geographical …, Do you provide any …

## g0051（1 列）
- 見出し：Do you provide any of the following services in relation to
- 例1 値：1. Outreach Activities | 1. Outreach Activities | 1. Outreach Activities | 1. Outreach Activities | 1. Outreach Activities
  - 同じ表の列：RespondentID, CollectorID, StartDate, EndDate, Which of the follow…, Which of the follow…, Which geographical …, Is education, learn…

## g0052（1 列）
- 見出し：Which of the following people does your organisation target
- 例1 値：1. People with learning difficulties | 1. People with learning difficulties | 1. People with learning difficulties | 1. People with learning difficulties | 1. People with learning difficulties
  - 同じ表の列：RespondentID, CollectorID, StartDate, EndDate, Which of the follow…, Which of the follow…, Which geographical …, Is education, learn…

## g0053（1 列）
- 見出し：Owning Dept/ALB Department
- 例1 値：DESNZ | DESNZ | DESNZ | Great British Nuclear (DESNZ) | Ofgem (DESNZ)
  - 同じ表の列：Value (£) (excludin…, Approval date, Control

## g0054（1 列）
- 見出し：Value (£) (excluding VAT)
- 例1 値：£17,500,000 | £1,594,000 | £79,353 | £1,698,740 | £2,143,057
  - 同じ表の列：Owning Dept/ALB Dep…, Approval date, Control

## g0055（1 列）
- 見出し：Approval date
- 例1 値：12/07/2023 | 09/08/2023 | 31/07/2023 | 09/08/2023 | 09/08/2023
  - 同じ表の列：Owning Dept/ALB Dep…, Value (£) (excludin…, Control

## g0056（1 列）
- 見出し：Control
- 例1 値：Monitor | Monitor | Control | Monitor | Monitor
  - 同じ表の列：Owning Dept/ALB Dep…, Value (£) (excludin…, Approval date

## g0057（1 列）
- 見出し：Reference Number
- 例1 値：con_4873 | con_4766 | prj_1830 | con_2874 | con_1890
  - 同じ表の列：Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0058（1 列）
- 見出し：Business Area
- 例1 値：International Net Zero - International … | Digital | Communications | Science & Innovation for Climate & Ener… | Industrial Decarbonisation & Emissions …
  - 同じ表の列：Reference Number, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0059（1 列）
- 見出し：Contract Title
- 例1 値：National Atmospheric Emissions Inventor… | CLU Records Management | Radiation Monitoring Network | VMWare Workspace One | Climate Innovation Pull Facility
  - 同じ表の列：Reference Number, Business Area, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0060（1 列）
- 見出し：Commercial Strategy
- 例1 値：New requirement | New requirement | Re-procurement (different scope) | Re-procurement (same scope) | Re-procurement (same scope)
  - 同じ表の列：Reference Number, Business Area, Contract Title, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0061（1 列）
- 見出し：Procurement Start Date
- 例1 値：15/06/2025 | 03/07/2025 | 01/03/2024 | 22/10/2025 | 01/04/2024
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Contract Commenceme…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0062（1 列）
- 見出し：Contract Commencement Date
- 例1 値：12/12/2025 | 03/07/2026 | 26/01/2026 | 30/08/2025 | 16/05/2024
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, New Contract End Da…, Value of New Contra…, Procurement Sourcin…

## g0063（1 列）
- 見出し：New Contract End Date
- 例1 値：12/01/2027 | 07/04/2026 | 25/05/2028 | 31/05/2028 | 03/07/2033
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, Value of New Contra…, Procurement Sourcin…

## g0064（1 列）
- 見出し：Value of New Contract (Excluding Options)
- 例1 値：3,205,468 | 2,170,000 | £2,000,000 | 2,334,208 | 80,000,000
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Procurement Sourcin…

## g0065（1 列）
- 見出し：Procurement Sourcing Route
- 例1 値：Framework | TBC | Framework - CCS | Framework | TBC
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…

## g0066（1 列）
- 見出し：Category
- 例1 値：IT | Specialist Software (Non-SaaS);Speciali… | IT Management and Change | World Aid | World Programmes;World Aid
  - 同じ表の列：Reference Number, Business Area, Contract Title, Commercial Strategy, Procurement Start D…, Contract Commenceme…, New Contract End Da…, Value of New Contra…

## g0067（1 列）
- 見出し：DATES
- 例1 値：25-Feb | Date | NONE | 10/3 – 11/3 | HOSPITALITY RECORD January – March 2013
  - 同じ表の列：DESTINATION, PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost £

## g0068（1 列）
- 見出し：DESTINATION
- 例1 値：- | London Office | London Office | London Office | London Office
  - 同じ表の列：DATES, PURPOSE, TRAVEL, OTHER (Including Ho…, Total Cost £

## g0069（1 列）
- 見出し：PURPOSE
- 例1 値：Induction meetings | EMC | AC and induction | PURPOSE | Courier charges
  - 同じ表の列：DATES, DESTINATION, TRAVEL, OTHER (Including Ho…, Total Cost £

## g0070（1 列）
- 見出し：TRAVEL
- 例1 値：- | Air | - | - | 102.5
  - 同じ表の列：DATES, DESTINATION, PURPOSE, OTHER (Including Ho…, Total Cost £

## g0071（1 列）
- 見出し：OTHER (Including Hospitality Given)
- 例1 値：- | - | - | OTHER (Including Hospitality Given) | 148.99
  - 同じ表の列：DATES, DESTINATION, PURPOSE, TRAVEL, Total Cost £

## g0072（1 列）
- 見出し：Total Cost £
- 例1 値：275.31 | Total Cost £ | 148.99 | 20.15 | 38.7
  - 同じ表の列：DATES, DESTINATION, PURPOSE, TRAVEL, OTHER (Including Ho…

## g0073（1 列）
- 見出し：Date of Meeting
- 例1 値：02/09/2010 | 02/09/2010 | 21/10/2010 | 13/09/2010 | 29/09/2010
  - 同じ表の列：Purpose of Meeting

## g0074（1 列）
- 見出し：Purpose of Meeting
- 例1 値：2010 World Bank/IMF Annual Meetings | DFID work on forestry | Discussion of MDG Summit | CDC policy | Commission for Africa and Open Universi…
  - 同じ表の列：Date of Meeting

## g0075（1 列）
- 見出し：Outturn
- 例1 値：- | 1,060,382 | - | - | -
  - 同じ表の列：Outturn_2

## g0076（1 列）
- 見出し：Outturn_2
- 例1 値：- | 1,758,696 | 7,870,142 | - | 725,796
  - 同じ表の列：Outturn

## g0077（1 列）
- 見出し：Date
- 例1 値：2018-03-06 | 2018-03-12 | 2018-01-09 | 2018-01-22 | 2018-01-24
  - 同じ表の列：Purpose of meeting

## g0078（2 列）
- 見出し：Purpose of meeting
- 例1 値：Roundtable discussion | Roundtable discussion | Roundtable discussion | Roundtable discussion | PAC Meeting
  - 同じ表の列：Date
- 例2 値：Introductory meeting | Introductory meeting | Introductory meeting | Introductory meeting | Introductory meeting
  - 同じ表の列：Minister, Date

## g0079（1 列）
- 見出し：Start date of trip
- 例1 値：2018-03-06 | 2018-03-15 | 2018-01-16 | 2018-02-07 | 2018-02-19
  - 同じ表の列：Duration of Visit (…, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Cost of travel, Total cost, includi…

## g0080（1 列）
- 見出し：Duration of Visit (Days)
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Start date of trip, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Cost of travel, Total cost, includi…

## g0081（1 列）
- 見出し：Purpose of trip
- 例1 値：Conference Attendance | Site Visit | visit to Royal Sovereign Lighthouse | Site Visit | Operational Activity
  - 同じ表の列：Start date of trip, Duration of Visit (…, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Cost of travel, Total cost, includi…

## g0082（1 列）
- 見出し：Mode of transport
- 例1 値：Rail | Rail | Rail | Rail | Rail
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Class of travel, Accomodation/Meals, Other (including ho…, Cost of travel, Total cost, includi…

## g0083（1 列）
- 見出し：Class of travel
- 例1 値：Standard | Standard | Standard | Standard | Standard
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Accomodation/Meals, Other (including ho…, Cost of travel, Total cost, includi…

## g0084（1 列）
- 見出し：Accomodation/Meals
- 例1 値：NIL | 」178.44 | NIL | 」7.68 | NIL
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Class of travel, Other (including ho…, Cost of travel, Total cost, includi…

## g0085（1 列）
- 見出し：Other (including hospitality given)
- 例1 値：NIL | NIL | NIL | NIL | NIL
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Cost of travel, Total cost, includi…

## g0086（1 列）
- 見出し：Cost of travel
- 例1 値：」26.60 | NIL | 」15.90 | 」18.60 | 」75.98
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Total cost, includi…

## g0087（1 列）
- 見出し：Total cost, including all visas, accommodation, travel, meal
- 例1 値：」6.55 | 」75.00 | 」26.50 | 」30.30 | 」57.60
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Cost of travel

## g0088（1 列）
- 見出し：Total Cost of Use of Official Secure Car
- 例1 値：NIL | NIL | NIL | NIL | NIL
  - 同じ表の列：Start date of trip, Duration of Visit (…, Purpose of trip, Mode of transport, Class of travel, Accomodation/Meals, Other (including ho…, Cost of travel

## g0089（2 列）
- 見出し：Main department
- 例1 値：Department for Transport | Department for Transport | Department for Transport | Department for Transport | Department for Transport
  - 同じ表の列：Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…
- 例2 値：Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence | Ministry of Defence
  - 同じ表の列：Organisation, Delegated grades on…, SCS on standard con…, Information for SCS…, Comments

## g0090（1 列）
- 見出し：Organisation
- 例1 値：Driving Standards Agency | Maritime and Coastguard Agency | Vehicle Certification Agency | Driver and Vehicle Licensing Agency | Department for Transport
  - 同じ表の列：Main department, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…

## g0091（1 列）
- 見出し：Annual Paybill (delegated grades for financial year 2013/14
- 例1 値：」84,119,748 | 」81,699,989 | 」104,332,000 | 」153,857,343 | 」42,321,409
  - 同じ表の列：Main department, Organisation, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…

## g0092（1 列）
- 見出し：Headcount (delegated grades as at 31 March 2014) for delega
- 例1 値：1073 | 163 | 1635 | 2267 | 5609
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, In-year: Cost of in…, In-year: Number of …, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…

## g0093（1 列）
- 見出し：In-year: Cost of in-year NCPRP for delegated grades (」s) for
- 例1 値：」0 | 」4,600 | 」0 | 」78,917 | 」0
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Number of …, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…

## g0094（1 列）
- 見出し：In-year: Number of staff in delegated grades receiving an in
- 例1 値：0 | 0 | 653 | 0 | 0
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…

## g0095（1 列）
- 見出し：In-year: Number of staff in delegated grades receiving an in
- 例1 値：0.0% | 7.4% | 0.0% | 0.0% | 18.9%
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Median NCP…, End of year: Cost o…

## g0096（1 列）
- 見出し：In-year: Median NCPRP for those receiving an in-year NCPRP f
- 例1 値：」500 | 」0 | 」0 | 」350 | 」0
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Number of …, End of year: Cost o…

## g0097（1 列）
- 見出し：End of year: Cost of end of year NCPRP for delegated grades
- 例1 値：」88,999 | 」384,059 | 」747,035 | 」10,250 | 」6,101,536
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Number of …, In-year: Median NCP…

## g0098（1 列）
- 見出し：End of year: Number of staff in delegated grades receiving a
- 例1 値：399 | 238 | 11 | 818 | 485
  - 同じ表の列：Main department, Organisation, Annual Paybill (del…, Headcount (delegate…, In-year: Cost of in…, In-year: Number of …, In-year: Number of …, In-year: Median NCP…

## g0099（2 列）
- 見出し：Date of Meeting
- 例1 値：Mar | Mar | Mar | Mar
  - 同じ表の列：Purpose of Meeting
- 例2 値：July | July | May | June | July
  - 同じ表の列：Minister, Purpose of Meeting

## g0100（1 列）
- 見出し：Purpose of Meeting
- 例1 値：Strategic Partnership Development | Universal Credit | Introductory Meeting | Strategic Partnership Development
  - 同じ表の列：Date of Meeting

## g0101（1 列）
- 見出し：Oct-10
- 例1 値：St. Petersburg | Jerusalem | Kinshasa | Seattle | Hong Kong Contact Centre
  - 同じ表の列：Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access, Child Custody

## g0102（1 列）
- 見出し：Abduction
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Oct-10, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access, Child Custody

## g0103（1 列）
- 見出し：Arrest/Detention - Child Sex
- 例1 値：0 | <=5 | 0 | 0 | 0
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access, Child Custody

## g0104（1 列）
- 見出し：Arrest/Detention - Drugs
- 例1 値：0 | 0 | <=5 | 0 | 0
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access, Child Custody

## g0105（1 列）
- 見出し：Arrest/Detention - General
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access, Child Custody

## g0106（1 列）
- 見出し：Arrest/Detention - Immigration
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access, Child Custody

## g0107（1 列）
- 見出し：Child Abduction
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child - Access, Child Custody

## g0108（1 列）
- 見出し：Child - Access
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child Custody

## g0109（1 列）
- 見出し：Child Custody
- 例1 値：0 | 0 | 0 | 0 | <=5
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access

## g0110（1 列）
- 見出し：Death - Accidental
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Oct-10, Abduction, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Arrest/Detention - …, Child Abduction, Child - Access

## g0111（1 列）
- 見出し：Organisation Type
- 例1 値：Executive Non-Departmental Public Body | Executive Non-Departmental Public Body | Executive Agency | Executive Agency | Executive Non-Departmental Public Body
  - 同じ表の列：Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0112（1 列）
- 見出し：Main, parent or sponsoring department
- 例1 値：Foreign and Commonwealth Office | Foreign and Commonwealth Office | Foreign and Commonwealth Office | Foreign and Commonwealth Office | Foreign and Commonwealth Office
  - 同じ表の列：Organisation Type, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0113（1 列）
- 見出し：Payroll staff AO/AA Headcount
- 例1 値：144 | 18 | 34 | 748
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0114（1 列）
- 見出し：Payroll staff EO Headcount
- 例1 値：17 | 7 | 780 | 149 | 189
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0115（1 列）
- 見出し：Payroll staff SEO/HEO Headcount
- 例1 値：1624 | 461 | 13 | 722 | 3
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0116（1 列）
- 見出し：Payroll staff Grade 6/7 Headcount
- 例1 値：1 | 1193 | 11 | 132 | 263
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff SCS H…, Payroll staff Other…, Payroll staff Total…

## g0117（1 列）
- 見出し：Payroll staff SCS Headcount
- 例1 値：410 | 1 | 2 | 9 | 60
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff Other…, Payroll staff Total…

## g0118（1 列）
- 見出し：Payroll staff Other, unknown or unspecified Headcount
- 例1 値：5 | 0 | 0
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Total…

## g0119（1 列）
- 見出し：Payroll staff Total Employees Headcount
- 例1 値：1,212 | 0 | 21 | 5 | 935
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

## g0120（1 列）
- 見出し：Non-payroll Staff Agency staff (clerical/admin) Headcount
- 例1 値：1 | 54 | 34 | 129
  - 同じ表の列：Organisation Type, Main, parent or spo…, Payroll staff AO/AA…, Payroll staff EO He…, Payroll staff SEO/H…, Payroll staff Grade…, Payroll staff SCS H…, Payroll staff Other…

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
