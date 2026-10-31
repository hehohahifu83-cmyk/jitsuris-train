# ラベル用シート 001 / 001

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：List
- 例1 値：New Year | New Year | New Year | New Year | New Year
  - 同じ表の列：Year, Order, Level, Award, Citation, County

## g0002（1 列）
- 見出し：Year
- 例1 値：2008 | 2008 | 2008 | 2008 | 2008
  - 同じ表の列：List, Order, Level, Award, Citation, County

## g0003（1 列）
- 見出し：Order
- 例1 値：Members of the Order of the British Emp… | Officers of the Order of the British Em… | Members of the Order of the British Emp… | Members of the Order of the British Emp… | Officers of the Order of the British Em…
  - 同じ表の列：List, Year, Level, Award, Citation, County

## g0004（1 列）
- 見出し：Level
- 例1 値：MBE | MBE | CBE | OBE | MBE
  - 同じ表の列：List, Year, Order, Award, Citation, County

## g0005（1 列）
- 見出し：Award
- 例1 値：Member of the Order of the British Empi… | Member of the Order of the British Empi… | Member of the Order of the British Empi… | Member of the Order of the British Empi… | Member of the Order of the British Empi…
  - 同じ表の列：List, Year, Order, Level, Citation, County

## g0006（1 列）
- 見出し：Citation
- 例1 値：For services to Brass Band Music. | For services to Nature Conservation in … | For charitable services. | President, Baptist World Alliance. For … | For services to the community in Eagles…
  - 同じ表の列：List, Year, Order, Level, Award, County

## g0007（1 列）
- 見出し：County
- 例1 値：Antrim | Gloucestershire | Greater Manchester | Kent | Tyne and Wear
  - 同じ表の列：List, Year, Order, Level, Award, Citation

## g0008（1 列）
- 見出し：2014-15
- 例1 値：679.2 | -0.4 | -7.7 | 35.2 | £millions
  - 同じ表の列：2013-14, variance

## g0009（1 列）
- 見出し：2013-14
- 例1 値：449.1 | 367 | 396.3 | £millions | -4.5
  - 同じ表の列：2014-15, variance

## g0010（1 列）
- 見出し：variance
- 例1 値：13.2 | 40.6 | 40.6 | 282.9 | 139.6
  - 同じ表の列：2014-15, 2013-14

## g0011（1 列）
- 見出し：Payment stream:
- 例1 値：** All net unreconciled differences are… | Total reported by government agencies f… | Type of payee: | Total reported by government agencies | Net unreconciled difference**
  - 同じ表の列：Petroleum Licence F…, OGA Levy, PRT, RFCT & SC, Mainstream CT, Payments to TCE, Payments to TCE_2, Payments to CA

## g0012（1 列）
- 見出し：Petroleum Licence Fees
- 例1 値：54.35 | OGA | 0 | Oil & Gas | 54.35
  - 同じ表の列：Payment stream:, OGA Levy, PRT, RFCT & SC, Mainstream CT, Payments to TCE, Payments to TCE_2, Payments to CA

## g0013（1 列）
- 見出し：OGA Levy
- 例1 値：1.27 | 0 | 19.99 | 21.27 | OGA
  - 同じ表の列：Payment stream:, Petroleum Licence F…, PRT, RFCT & SC, Mainstream CT, Payments to TCE, Payments to TCE_2, Payments to CA

## g0014（1 列）
- 見出し：PRT
- 例1 値：-782.29 | 0 | HMRC | 0 | Oil & Gas
  - 同じ表の列：Payment stream:, Petroleum Licence F…, OGA Levy, RFCT & SC, Mainstream CT, Payments to TCE, Payments to TCE_2, Payments to CA

## g0015（1 列）
- 見出し：RFCT & SC
- 例1 値：241.19 | 241.32 | 241.2 | 0.13 | HMRC
  - 同じ表の列：Payment stream:, Petroleum Licence F…, OGA Levy, PRT, Mainstream CT, Payments to TCE, Payments to TCE_2, Payments to CA

## g0016（1 列）
- 見出し：Mainstream CT
- 例1 値：HMRC | Other Mining & Quarrying | 0 | 4.44 | 32.78
  - 同じ表の列：Payment stream:, Petroleum Licence F…, OGA Levy, PRT, RFCT & SC, Payments to TCE, Payments to TCE_2, Payments to CA

## g0017（1 列）
- 見出し：Payments to TCE
- 例1 値：2.53 | TCE | 0 | Oil & Gas | 2.53
  - 同じ表の列：Payment stream:, Petroleum Licence F…, OGA Levy, PRT, RFCT & SC, Mainstream CT, Payments to TCE_2, Payments to CA

## g0018（1 列）
- 見出し：Payments to TCE_2
- 例1 値：-0.01 | TCE | 0.11 | 22.22 | Other Mining & Quarrying
  - 同じ表の列：Payment stream:, Petroleum Licence F…, OGA Levy, PRT, RFCT & SC, Mainstream CT, Payments to TCE, Payments to CA

## g0019（1 列）
- 見出し：Payments to CA
- 例1 値：0 | CA | 0 | 0.44 | 0
  - 同じ表の列：Payment stream:, Petroleum Licence F…, OGA Levy, PRT, RFCT & SC, Mainstream CT, Payments to TCE, Payments to TCE_2

## g0020（1 列）
- 見出し：Total payments
- 例1 値：All | -409.24 | 14.15 | -0.02 | -395.08
  - 同じ表の列：Payment stream:, Petroleum Licence F…, OGA Levy, PRT, RFCT & SC, Mainstream CT, Payments to TCE, Payments to TCE_2

## g0021（1 列）
- 見出し：Month of Meeting
- 例1 値：Sept | Sept | Sept | July | July
  - 同じ表の列：Purpose of Meeting

## g0022（1 列）
- 見出し：Purpose of Meeting
- 例1 値：Universities update | Consultancy | Consultancy | Educational materials | Working with DfE
  - 同じ表の列：Month of Meeting

## g0023（1 列）
- 見出し：NaptanCode
- 例1 値：bstdgdg | bstpamw | bstatwd | bstdmpw | bstgmwa
  - 同じ表の列：Indicator, Bearing, NptgLocalityCode, LocalityCentre, GridType, Easting, Northing, StopType

## g0024（1 列）
- 見出し：Indicator
- 例1 値：NW-bound | S13 | A1 | NE-bound | S-bound
  - 同じ表の列：NaptanCode, Bearing, NptgLocalityCode, LocalityCentre, GridType, Easting, Northing, StopType

## g0025（1 列）
- 見出し：Bearing
- 例1 値：E | NE | NE | E | N
  - 同じ表の列：NaptanCode, Indicator, NptgLocalityCode, LocalityCentre, GridType, Easting, Northing, StopType

## g0026（1 列）
- 見出し：NptgLocalityCode
- 例1 値：E0035590 | N0077024 | E0035635 | E0035579 | E0035608
  - 同じ表の列：NaptanCode, Indicator, Bearing, LocalityCentre, GridType, Easting, Northing, StopType

## g0027（1 列）
- 見出し：LocalityCentre
- 例1 値：true | false | false | false | false
  - 同じ表の列：NaptanCode, Indicator, Bearing, NptgLocalityCode, GridType, Easting, Northing, StopType

## g0028（1 列）
- 見出し：GridType
- 例1 値：UKOS | UKOS | UKOS | UKOS | UKOS
  - 同じ表の列：NaptanCode, Indicator, Bearing, NptgLocalityCode, LocalityCentre, Easting, Northing, StopType

## g0029（1 列）
- 見出し：Easting
- 例1 値：351528 | 358969 | 357403 | 351754 | 359816
  - 同じ表の列：NaptanCode, Indicator, Bearing, NptgLocalityCode, LocalityCentre, GridType, Northing, StopType

## g0030（1 列）
- 見出し：Northing
- 例1 値：179237 | 176412 | 168230 | 174516 | 170561
  - 同じ表の列：NaptanCode, Indicator, Bearing, NptgLocalityCode, LocalityCentre, GridType, Easting, StopType

## g0031（1 列）
- 見出し：StopType
- 例1 値：BCT | BCT | BCT | BCT | BCT
  - 同じ表の列：NaptanCode, Indicator, Bearing, NptgLocalityCode, LocalityCentre, GridType, Easting, Northing

## g0032（1 列）
- 見出し：BusStopType
- 例1 値：MKD | MKD | MKD | MKD | MKD
  - 同じ表の列：NaptanCode, Indicator, Bearing, NptgLocalityCode, LocalityCentre, GridType, Easting, Northing

## g0033（1 列）
- 見出し：Date
- 例1 値：03/12/2013 | 14/10/2013 | 09/12/2013 | 25/11/2013 | 26/11/2013
  - 同じ表の列：Organisation Meetin…

## g0034（1 列）
- 見出し：Organisation Meeting and Visits
- 例1 値：Confederation of British Industry (CBI) | Louise Ellman MP | Chancellor of the Exchequer - Rt. Hon. … | Leader of the Labour Party - Rt. Hon. E… | Civil Aviation Authority (CAA) - Dame D…
  - 同じ表の列：Date

## g0035（1 列）
- 見出し：Number of Travellers
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Total Cost ex VAT, Travel Class, Ticket Single or Re…, Travel Date, Journey Start Point, Journey Finish Point, Air Carrier

## g0036（1 列）
- 見出し：Total Cost ex VAT
- 例1 値：£73.32 | £419.75 | £197.09 | £344.82 | £54.30
  - 同じ表の列：Number of Travellers, Travel Class, Ticket Single or Re…, Travel Date, Journey Start Point, Journey Finish Point, Air Carrier

## g0037（1 列）
- 見出し：Travel Class
- 例1 値：ECONOMY | ECONOMY | ECONOMY | ECONOMY | BUSINESS
  - 同じ表の列：Number of Travellers, Total Cost ex VAT, Ticket Single or Re…, Travel Date, Journey Start Point, Journey Finish Point, Air Carrier

## g0038（1 列）
- 見出し：Ticket Single or Return
- 例1 値：Return | Return | Return | Return | Return
  - 同じ表の列：Number of Travellers, Total Cost ex VAT, Travel Class, Travel Date, Journey Start Point, Journey Finish Point, Air Carrier

## g0039（1 列）
- 見出し：Travel Date
- 例1 値：17/8/2011 | 7/6/2011 | 3/6/2011 | 13/9/2011 | 12/10/2011
  - 同じ表の列：Number of Travellers, Total Cost ex VAT, Travel Class, Ticket Single or Re…, Journey Start Point, Journey Finish Point, Air Carrier

## g0040（1 列）
- 見出し：Journey Start Point
- 例1 値：MANCHESTER | STANSTED | LONDON - LHR | LONDON - LHR | LONDON - LGW
  - 同じ表の列：Number of Travellers, Total Cost ex VAT, Travel Class, Ticket Single or Re…, Travel Date, Journey Finish Point, Air Carrier

## g0041（1 列）
- 見出し：Journey Finish Point
- 例1 値：MONTREAL | CAIRO | AMSTERDAM | MANCHESTER | MANCHESTER
  - 同じ表の列：Number of Travellers, Total Cost ex VAT, Travel Class, Ticket Single or Re…, Travel Date, Journey Start Point, Air Carrier

## g0042（1 列）
- 見出し：Air Carrier
- 例1 値：BRITISH AIRWAYS | BRITISH AIRWAYS | AIR FRANCE | BRITISH MIDLAND | FLYBE
  - 同じ表の列：Number of Travellers, Total Cost ex VAT, Travel Class, Ticket Single or Re…, Travel Date, Journey Start Point, Journey Finish Point

## g0043（1 列）
- 見出し：Sponsor Department
- 例1 値：Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions
  - 同じ表の列：Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0044（1 列）
- 見出し：Organisation
- 例1 値：Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions | Department for Work & Pensions
  - 同じ表の列：Sponsor Department, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0045（1 列）
- 見出し：Job Title
- 例1 値：Security Solutions Architect | Commercial Lawyer | .net Developer | Manager | ADC Project Manager
  - 同じ表の列：Sponsor Department, Organisation, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0046（1 列）
- 見出し：Specialism
- 例1 値：Programme and project management | Finance | Programme and project management | Programme and project management | IT
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0047（2 列）
- 見出し：Contractual Chain - i.e. Type of organisation that payments
- 例1 値：Employment Business | Employment Business | Employment Business | Employment Business | Employment Business
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Engagement length c…, Number of contract …, Lower bound, Upper bound
- 例2 値：Employment Business | Employment Business | Employment Business | Employment Business | Employment Business
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0048（1 列）
- 見出し：Engagement length category. Shows the current continuous eng
- 例1 値：0<6months ongoing | 0<6months ongoing | 3yrs<4yrs ongoing | 6months<1yr ongoing | 6months<1yr
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Number of contract …, Lower bound, Upper bound

## g0049（2 列）
- 見出し：Number of contract renewals
- 例1 値：0 | 1 | 4 | 3 | 2
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Lower bound, Upper bound
- 例2 値：6 | 10 | 6 | 0 | 10
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Lower bound, Upper bound

## g0050（1 列）
- 見出し：Lower bound
- 例1 値：£400 | £300 | £300 | £500 | £300
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Upper bound

## g0051（1 列）
- 見出し：Upper bound
- 例1 値：£599 | £899 | £399 | £899 | £599
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound

## g0052（2 列）
- 見出し：Payment methods
- 例1 値：per day | per day | per day | per day | per day
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound
- 例2 値：per day | per day | per day | per day | per day
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound

## g0053（1 列）
- 見出し：Subject
- 例1 値：Construction Industry Scheme (CIS): Dea… | PAYE and NICs payment deadline: Third Q… | Deadline for filing forms P9D P11D P11D… | PAYE and Class 1 National Insurance Con… | PAYE and Class 1 National Insurance Con…
  - 同じ表の列：Start Date, End Date

## g0054（1 列）
- 見出し：Start Date
- 例1 値：2011-10-22 | 2011-05-31 | 2011-04-05 | 2011-04-21 | 2011-05-22
  - 同じ表の列：Subject, End Date

## g0055（1 列）
- 見出し：End Date
- 例1 値：2011-04-05 | 2011-05-22 | 2011-06-22 | 2011-12-22 | 2011-06-19
  - 同じ表の列：Subject, Start Date

## g0056（1 列）
- 見出し：Jun-08
- 例1 値：72.8 | 1.7 | 73 | 1.7 | 78.3
  - 同じ表の列：Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0057（1 列）
- 見出し：Sep-08
- 例1 値：80.6 | 1.7 | 1.9 | 73.9 | 74
  - 同じ表の列：Jun-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0058（1 列）
- 見出し：Dec-08
- 例1 値：1.8 | 1.7 | 74.9 | 68.8 | 1.7
  - 同じ表の列：Jun-08, Sep-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0059（1 列）
- 見出し：Mar-09
- 例1 値：74.5 | 76 | 82.7 | 1.8 | 70.8
  - 同じ表の列：Jun-08, Sep-08, Dec-08, Jun-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0060（1 列）
- 見出し：Jun-09
- 例1 値：82.6 | 1.8 | 1.8 | 76.5 | 1.7
  - 同じ表の列：Jun-08, Sep-08, Dec-08, Mar-09, Sep-09, Dec-09, Mar-10, Jun-10

## g0061（1 列）
- 見出し：Sep-09
- 例1 値：75.6 | 68.2 | 81.8 | 1.9 | 1.7
  - 同じ表の列：Jun-08, Sep-08, Dec-08, Mar-09, Jun-09, Dec-09, Mar-10, Jun-10

## g0062（1 列）
- 見出し：Dec-09
- 例1 値：75.3 | 75.3 | 1.6 | 1.7 | 68.7
  - 同じ表の列：Jun-08, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Mar-10, Jun-10

## g0063（1 列）
- 見出し：Mar-10
- 例1 値：83 | 1.9 | 1.7 | 75.3 | 69.7
  - 同じ表の列：Jun-08, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Jun-10

## g0064（1 列）
- 見出し：Jun-10
- 例1 値：2 | 1.7 | 1.7 | 81 | 74.2
  - 同じ表の列：Jun-08, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10

## g0065（1 列）
- 見出し：Sep-10
- 例1 値：64.7 | 72.5 | 73.1 | 79.5 | 1.8
  - 同じ表の列：Jun-08, Sep-08, Dec-08, Mar-09, Jun-09, Sep-09, Dec-09, Mar-10

## g0066（1 列）
- 見出し：For publication
- 例1 値：HM Treasury | HM Treasury | HM Treasury | HM Treasury | HM Treasury
  - 同じ表の列：Drop-downs

## g0067（1 列）
- 見出し：Drop-downs
- 例1 値：Medicine | Finance | IT | HR | Other
  - 同じ表の列：For publication

## g0068（1 列）
- 見出し：Dept Code
- 例1 値：Dept047 | Dept025 | Dept090 | Dept041 | Dept048
  - 同じ表の列：COFOG level 1, HMT Functional Clas…, Programme Object Gr…, Programme Object Gr…, ID or non-ID, CAP or CUR, CG, LG or PC, NUTS 1 region

## g0069（1 列）
- 見出し：COFOG level 1
- 例1 値：1. General public services | 10. Social protection | 10. Social protection | 7. Health | 4. Economic affairs
  - 同じ表の列：Dept Code, HMT Functional Clas…, Programme Object Gr…, Programme Object Gr…, ID or non-ID, CAP or CUR, CG, LG or PC, NUTS 1 region

## g0070（1 列）
- 見出し：HMT Functional Classification
- 例1 値：4. Economic affairs - of which: enterpr… | 8. Recreation, culture and religion | 4. Economic affairs - of which: enterpr… | 1. General public services - of which: … | 4. Economic affairs - of which: agricul…
  - 同じ表の列：Dept Code, COFOG level 1, Programme Object Gr…, Programme Object Gr…, ID or non-ID, CAP or CUR, CG, LG or PC, NUTS 1 region

## g0071（1 列）
- 見出し：Programme Object Group
- 例1 値：P06 S260101 | P22 S020601 | PSX S159010 | P43 S130201 | P43 S280119
  - 同じ表の列：Dept Code, COFOG level 1, HMT Functional Clas…, Programme Object Gr…, ID or non-ID, CAP or CUR, CG, LG or PC, NUTS 1 region

## g0072（1 列）
- 見出し：Programme Object Group Alias
- 例1 値：PSX S154406 Museums and galleries (cash… | PO Ministry of Justice | P06 S260102 Food standards agency - HQ | P43 S280118 Lone Parents Addition | P31CCL VOTE RFR CCL1
  - 同じ表の列：Dept Code, COFOG level 1, HMT Functional Clas…, Programme Object Gr…, ID or non-ID, CAP or CUR, CG, LG or PC, NUTS 1 region

## g0073（1 列）
- 見出し：ID or non-ID
- 例1 値：ID | ID | ID | ID | ID
  - 同じ表の列：Dept Code, COFOG level 1, HMT Functional Clas…, Programme Object Gr…, Programme Object Gr…, CAP or CUR, CG, LG or PC, NUTS 1 region

## g0074（1 列）
- 見出し：CAP or CUR
- 例1 値：CUR | CUR | CUR | CUR | CAP
  - 同じ表の列：Dept Code, COFOG level 1, HMT Functional Clas…, Programme Object Gr…, Programme Object Gr…, ID or non-ID, CG, LG or PC, NUTS 1 region

## g0075（1 列）
- 見出し：CG, LG or PC
- 例1 値：CG | CG | CG | CG | CG
  - 同じ表の列：Dept Code, COFOG level 1, HMT Functional Clas…, Programme Object Gr…, Programme Object Gr…, ID or non-ID, CAP or CUR, NUTS 1 region

## g0076（1 列）
- 見出し：NUTS 1 region
- 例1 値：ENGLAND_South East | SCOTLAND | ENGLAND_East Midlands | ENGLAND_Yorkshire and the Humber | ENGLAND_South East
  - 同じ表の列：Dept Code, COFOG level 1, HMT Functional Clas…, Programme Object Gr…, Programme Object Gr…, ID or non-ID, CAP or CUR, CG, LG or PC

## g0077（1 列）
- 見出し：2004-05
- 例1 値：0.443730880952431 | 0.04488011081639475 | 0 | 0.0923088157894737 | 0
  - 同じ表の列：Dept Code, COFOG level 1, HMT Functional Clas…, Programme Object Gr…, Programme Object Gr…, ID or non-ID, CAP or CUR, CG, LG or PC

## g0078（1 列）
- 見出し：Year of Issue
- 例1 値：2009 | 2002 | 2005 | 2004 | 2004
  - 同じ表の列：Court, Gender, Asbo on application…, Age_Group, ASBOs issued

## g0079（1 列）
- 見出し：Court
- 例1 値：Bexley Magistrates' Court | Blackburn Darwen and Ribble Valley Magi… | Bexley Magistrates' Court | Calderdale Magistrates' Court | Bury Magistrates' Court
  - 同じ表の列：Year of Issue, Gender, Asbo on application…, Age_Group, ASBOs issued

## g0080（1 列）
- 見出し：Gender
- 例1 値：Male | Male | Female | Male | Male
  - 同じ表の列：Year of Issue, Court, Asbo on application…, Age_Group, ASBOs issued

## g0081（1 列）
- 見出し：Asbo on application or conviction
- 例1 値：Application | Application | Conviction | Application | Application
  - 同じ表の列：Year of Issue, Court, Gender, Age_Group, ASBOs issued

## g0082（1 列）
- 見出し：Age_Group
- 例1 値：10 to 17 | 10 to 17 | 18+ | 10 to 17 | 18+
  - 同じ表の列：Year of Issue, Court, Gender, Asbo on application…, ASBOs issued

## g0083（1 列）
- 見出し：ASBOs issued
- 例1 値：2 | 6 | 1 | 1 | 1
  - 同じ表の列：Year of Issue, Court, Gender, Asbo on application…, Age_Group

## g0084（1 列）
- 見出し：Title
- 例1 値：Agreement between the Government of the… | Multilateral protocol on the privileges… | Convention on the United Kingdom of Gre… | Counterinsurgency: exposing the myths o… | British social attitudes : the 26th rep…
  - 同じ表の列：Place, Date, Edition, Author, Publisher

## g0085（1 列）
- 見出し：Place
- 例1 値：Simon & Schuster, | London | London | TSO, | London
  - 同じ表の列：Title, Date, Edition, Author, Publisher

## g0086（1 列）
- 見出し：Date
- 例1 値：2013 | 2013 | 2010 | 2012 | 2013
  - 同じ表の列：Title, Place, Edition, Author, Publisher

## g0087（1 列）
- 見出し：Edition
- 例1 値：5th ed. | 3rd ed. | 2009-10 | rev'd | 4th & 5th ed., 2012
  - 同じ表の列：Title, Place, Date, Author, Publisher

## g0088（1 列）
- 見出し：Author
- 例1 値：POTTER, WILLIAM MARES, DAVID R | BELLAMY, ALEX J WILLIAMS, PAUL GRIFFIN,… | LIEVEN, ANATOL | MYERS, STEWART C BREALEY, RICHARD A ALL… | BURLEIGH, MICHAEL
  - 同じ表の列：Title, Place, Date, Edition, Publisher

## g0089（1 列）
- 見出し：Publisher
- 例1 値：Allen Lane, | TSO, | The Stationery Office | TSO, | TSO,
  - 同じ表の列：Title, Place, Date, Edition, Author

## g0090（1 列）
- 見出し：Activity
- 例1 値：60956 | 1237017 | 102089 | 3285 | 335671
  - 同じ表の列：Unit Cost

## g0091（1 列）
- 見出し：Unit Cost
- 例1 値：269.09831183909336 | 58.84329230277606 | 27.513104365232 | 814.2791396803888 | 50.38558936671012
  - 同じ表の列：Activity

## g0092（1 列）
- 見出し：Reference
- 例1 値：CR01076 | CR00916 | CR00676 | CR00899 | CR00531/1
  - 同じ表の列：Contract Title, Value pa, Expiry date

## g0093（1 列）
- 見出し：Contract Title
- 例1 値：Maintenance: Eclipse III Call Managemen… | Norwich site internet service | Support: Digital Archive | Remote Hosting | Support: Fax Server
  - 同じ表の列：Reference, Value pa, Expiry date

## g0094（1 列）
- 見出し：Value pa
- 例1 値：1129.15 | 2807 | 19965 | 100627.88 | 15429.35
  - 同じ表の列：Reference, Contract Title, Expiry date

## g0095（1 列）
- 見出し：Expiry date
- 例1 値：40359 | 40330 | 40158 | 40268 | 40268
  - 同じ表の列：Reference, Contract Title, Value pa

## g0096（1 列）
- 見出し：Sponsor Department
- 例1 値：UK Export Finance | UK Export Finance | UK Export Finance | UK Export Finance | UK Export Finance
  - 同じ表の列：Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0097（1 列）
- 見出し：Organisation
- 例1 値：UK Export Finance | UK Export Finance | UK Export Finance | UK Export Finance | UK Export Finance
  - 同じ表の列：Sponsor Department, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0098（1 列）
- 見出し：Job Title
- 例1 値：IT Specialist | IT Specialist | IT Specialist | Specialist Contractor | Specialist Contractor
  - 同じ表の列：Sponsor Department, Organisation, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0099（1 列）
- 見出し：Specialism
- 例1 値：IT | IT | IT | IT | Operational delivery
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound, Upper bound

## g0100（1 列）
- 見出し：Engagement length category. Shows the current continuous eng
- 例1 値：4yrs<5yrs | 1yr<2yrs | 6months<1yr | 2yrs<3yrs | 2yrs<3yrs
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Number of contract …, Lower bound, Upper bound

## g0101（1 列）
- 見出し：Lower bound
- 例1 値：500 | 500 | 500 | 500 | 400
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Upper bound

## g0102（1 列）
- 見出し：Upper bound
- 例1 値：499 | 599 | 399 | 599 | 699
  - 同じ表の列：Sponsor Department, Organisation, Job Title, Specialism, Contractual Chain -…, Engagement length c…, Number of contract …, Lower bound

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
```
