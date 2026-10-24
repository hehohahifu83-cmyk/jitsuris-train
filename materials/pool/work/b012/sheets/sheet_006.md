# ラベル用シート 006 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_006.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0601（3 列）
- 見出し：region
- 例1 値：Dublin | Dublin | Connacht | Leinster | Connacht
  - 同じ表の列：id, date, todaywww, tonightwww, tomorrowwww
- 例2 値：Western | Atlantic | Quebec | Ontario | Atlantic
  - 同じ表の列：Fiscal Year, City, Province, Community Type, Grant Or Contributi…, Amount Approved, Presenter Type, Disciplines

## g0602（1 列）
- 見出し：todaywww
- 例1 値：Mainly dry and fresh today with a mix o… | Mostly cloudy this evening with scatter… | Good warm sunny spells this evening. Li… | Cloudier skies will bring outbreaks of … | Tuesday will bring a mix of cloud and s…
  - 同じ表の列：id, date, region, tonightwww, tomorrowwww

## g0603（1 列）
- 見出し：tonightwww
- 例1 値：Tonight will remain mostly cloudy but d… | Dry in most areas tonight. Lowest tempe… | Any showers will die out this evening a… | Overall dry tonight but there will be s… | Any patchy light rain and drizzle will …
  - 同じ表の列：id, date, region, todaywww, tomorrowwww

## g0604（1 列）
- 見出し：tomorrowwww
- 例1 値：Tomorrow, Friday will start cloudy and … | Tomorrow Sunday will be warm. It will b… | The rain will clear the east coast duri… | Tomorrow, Friday will start cloudy and … | Sunday should stay dry with sunny spell…
  - 同じ表の列：id, date, region, todaywww, tonightwww

## g0605（1 列）
- 見出し：registration_assessment_transaction
- 例1 値：Number of employees records returned by… | Property Transacations - Non-Residentia… | Property Transacations - Residential (d… | Number of employers on register | Bookmaking premises
  - 同じ表の列：year, amount__

## g0606（1 列）
- 見出し：amount__
- 例1 値：509 | 600 | 263590 | 28683 | 96990
  - 同じ表の列：registration_assess…, year

## g0607（2 列）
- 見出し：Doc
- 例1 値：TableA | TableA | TableA | TableA | TableA
  - 同じ表の列：Heading, Ref, Exp, Inc, PY, OBJECTID
- 例2 値：TableD | TableD | TableD | TableD | TableD
  - 同じ表の列：Heading, Ref, desc, Inc, PY, Sort, OBJECTID

## g0608（2 列）
- 見出し：Heading
- 例1 値：1 | 1 | 3 | 1 | 1
  - 同じ表の列：Doc, Ref, Exp, Inc, PY, OBJECTID
- 例2 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Doc, Ref, desc, Inc, PY, Sort, OBJECTID

## g0609（1 列）
- 見出し：Ref
- 例1 値：CAL | B | E | G | F
  - 同じ表の列：Doc, Heading, Exp, Inc, PY, OBJECTID

## g0610（1 列）
- 見出し：Exp
- 例1 値：8591700 | 3123200 | 18471800 | 5326100 | 4712600
  - 同じ表の列：Doc, Heading, Ref, Inc, PY, OBJECTID

## g0611（1 列）
- 見出し：Inc
- 例1 値：155566 | -6181700 | -1129000 | -938700 | -1129000
  - 同じ表の列：Doc, Heading, Ref, Exp, PY, OBJECTID

## g0612（1 列）
- 見出し：PY
- 例1 値：135900 | 4405300 | 146600 | -1115000 | -11070000
  - 同じ表の列：Doc, Heading, Ref, Exp, Inc, OBJECTID

## g0613（5 列）
- 見出し：OBJECTID
- 例1 値：11 | 9 | 6 | 2 | 7
  - 同じ表の列：Doc, Heading, Ref, Exp, Inc, PY
- 例2 値：802 | 1355 | 679 | 1462 | 1733
  - 同じ表の列：ADMINTYPEN, ADMINAREAN, LOC_CODE, Locality, AdminType, AdminArea, loaddate, supplydate

## g0614（1 列）
- 見出し：X
- 例1 値：-6.6138762712363 | -6.69015997667621 | -6.61867787575479 | -6.61644971105992 | -6.63106855147676
  - 同じ表の列：Y, ENTITY_ID, CLASSCODE, NAT_GRID_E, NAT_GRID_N, RMP_PROP, CO_ID, WEBNOTES

## g0615（1 列）
- 見出し：Y
- 例1 値：52.9616824642128 | 52.9639543157037 | 52.9688643904683 | 52.9336223191039 | 52.9461719822787
  - 同じ表の列：X, ENTITY_ID, CLASSCODE, NAT_GRID_E, NAT_GRID_N, RMP_PROP, CO_ID, WEBNOTES

## g0616（1 列）
- 見出し：ENTITY_ID
- 例1 値：WI00936 | WI01222 | WI01296 | WI03128 | WI01269
  - 同じ表の列：X, Y, CLASSCODE, NAT_GRID_E, NAT_GRID_N, RMP_PROP, CO_ID, WEBNOTES

## g0617（1 列）
- 見出し：CLASSCODE
- 例1 値：CAIR | ENCL | ENCL | CAIR | ENCL
  - 同じ表の列：X, Y, ENTITY_ID, NAT_GRID_E, NAT_GRID_N, RMP_PROP, CO_ID, WEBNOTES

## g0618（1 列）
- 見出し：NAT_GRID_E
- 例1 値：293053 | 287893 | 292782 | 291934 | 291932
  - 同じ表の列：X, Y, ENTITY_ID, CLASSCODE, NAT_GRID_N, RMP_PROP, CO_ID, WEBNOTES

## g0619（1 列）
- 見出し：NAT_GRID_N
- 例1 値：188281 | 188149 | 190030 | 189322 | 195956
  - 同じ表の列：X, Y, ENTITY_ID, CLASSCODE, NAT_GRID_E, RMP_PROP, CO_ID, WEBNOTES

## g0620（1 列）
- 見出し：RMP_PROP
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：X, Y, ENTITY_ID, CLASSCODE, NAT_GRID_E, NAT_GRID_N, CO_ID, WEBNOTES

## g0621（1 列）
- 見出し：CO_ID
- 例1 値：32 | 32 | 32 | 32 | 32
  - 同じ表の列：X, Y, ENTITY_ID, CLASSCODE, NAT_GRID_E, NAT_GRID_N, RMP_PROP, WEBNOTES

## g0622（1 列）
- 見出し：WEBNOTES
- 例1 値：Situated on a marked S-facing slope, 25… | National Monument in state guardianship… | Situated on the summit of a ridge. Oval… | In a largely forested area within the S… | Situated in forestry on a marked W-faci…
  - 同じ表の列：X, Y, ENTITY_ID, CLASSCODE, NAT_GRID_E, NAT_GRID_N, RMP_PROP, CO_ID

## g0623（1 列）
- 見出し：ZON_ID
- 例1 値：R147120 | R147044 | R147120 | R146956 | R147120
  - 同じ表の列：X, Y, ENTITY_ID, CLASSCODE, NAT_GRID_E, NAT_GRID_N, RMP_PROP, CO_ID

## g0624（2 列）
- 見出し：Date-Time
- 例1 値：2007-03-27 08:28:00 | 2007-03-27 09:26:00 | 2007-03-27 11:46:00 | 2007-03-27 10:20:00 | 2007-03-27 02:08:00
  - 同じ表の列：Lat, Lon, UV_Index
- 例2 値：2007-10-11 10:56:00 | 2007-10-11 12:47:00 | 2007-10-11 10:33:00 | 2007-10-11 13:58:00 | 2007-10-11 02:38:00
  - 同じ表の列：Lat, Lon, UV_Index

## g0625（2 列）
- 見出し：UV_Index
- 例1 値：05.91 | 01.33 | 06.14 | 00.00 | 02.45
  - 同じ表の列：Date-Time, Lat, Lon
- 例2 値：00.46 | 02.37 | 00.04 | 00.03 | 00.03
  - 同じ表の列：Date-Time, Lat, Lon

## g0626（1 列）
- 見出し：Tariff item Unit: $ per litre of alcohol
- 例1 値：Last modified: | 3.5 | 2 | 3.1 | 3.6
  - 同じ表の列：From 2 February 2026, From 3 August 2026

## g0627（1 列）
- 見出し：From 2 February 2026
- 例1 値：From 2 February 2026 | 107.99 | 100.85 | Free | Free
  - 同じ表の列：Tariff item Unit: $…, From 3 August 2026

## g0628（1 列）
- 見出し：From 3 August 2026
- 例1 値：QC 63605 | From 3 August 2026 | From 3 August 2026 | 110.15 | 110.15
  - 同じ表の列：Tariff item Unit: $…, From 2 February 2026

## g0629（1 列）
- 見出し：Request Type
- 例1 値：HGBKG - Hard/Green Waste Booking | HGBKG - Hard/Green Waste Booking | HGBKG - Hard/Green Waste Booking | HGBKG - Hard/Green Waste Booking | HGBKG - Hard/Green Waste Booking
  - 同じ表の列：Financial Year, Month, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…

## g0630（1 列）
- 見出し：Financial Year
- 例1 値：2013/2014 | 2012/2013 | 2016/2017 | 2017/2018 | 2017/2018
  - 同じ表の列：Request Type, Month, MonthYear, CalendarYear, Suburb, NumberOfRequests_Re…

## g0631（1 列）
- 見出し：MonthYear
- 例1 値：Apr-2017 | Jun-2018 | Aug-2013 | Aug-2014 | Apr-2014
  - 同じ表の列：Request Type, Financial Year, Month, CalendarYear, Suburb, NumberOfRequests_Re…

## g0632（1 列）
- 見出し：CalendarYear
- 例1 値：CY 2015 | CY 2013 | CY 2014 | CY 2011 | CY 2014
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, Suburb, NumberOfRequests_Re…

## g0633（1 列）
- 見出し：Suburb
- 例1 値：ST KILDA EAST | SOUTH MELBOURNE | ST KILDA EAST | ALBERT PARK | RIPPONLEA
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, CalendarYear, NumberOfRequests_Re…

## g0634（1 列）
- 見出し：NumberOfRequests_Received
- 例1 値：1 | 45 | 28 | 7 | 1
  - 同じ表の列：Request Type, Financial Year, Month, MonthYear, CalendarYear, Suburb

## g0635（1 列）
- 見出し：B_Geocode
- 例1 値：GAVIC420541384 | GANSW710287087 | GANSW710287164 | GAVIC420122079 | GASA_416461662
  - 同じ表の列：B_Suburb, B_State, CRT_CertificateNumb…, CRT_UTC_IssueDate, CRT_UTC_CurrentTo, CRT_UTC_SubmissionD…, CRT_Nabers_Referenc…, CRT_Nabers_StarRati…

## g0636（1 列）
- 見出し：CRT_UTC_IssueDate
- 例1 値：24/04/2024 | 27/07/2024 | 20/05/2024 | 10/04/2024 | 11/08/2024
  - 同じ表の列：B_Suburb, B_State, B_Geocode, CRT_CertificateNumb…, CRT_UTC_CurrentTo, CRT_UTC_SubmissionD…, CRT_Nabers_Referenc…, CRT_Nabers_StarRati…

## g0637（1 列）
- 見出し：CRT_UTC_CurrentTo
- 例1 値：24/08/2025 | 3/07/2025 | 7/05/2025 | 30/05/2025 | 30/06/2025
  - 同じ表の列：B_Suburb, B_State, B_Geocode, CRT_CertificateNumb…, CRT_UTC_IssueDate, CRT_UTC_SubmissionD…, CRT_Nabers_Referenc…, CRT_Nabers_StarRati…

## g0638（1 列）
- 見出し：CRT_UTC_SubmissionDate
- 例1 値：8/05/2024 18:02 | 8/06/2024 14:00 | 11/04/2024 15:45 | 26/08/2024 12:55 | 13/05/2024 19:52
  - 同じ表の列：B_Suburb, B_State, B_Geocode, CRT_CertificateNumb…, CRT_UTC_IssueDate, CRT_UTC_CurrentTo, CRT_Nabers_Referenc…, CRT_Nabers_StarRati…

## g0639（1 列）
- 見出し：CRT_Nabers_ReferenceNumber
- 例1 値：OF31973 | OF30686 | OF31715 | OF30692 | OF33073
  - 同じ表の列：B_Suburb, B_State, B_Geocode, CRT_CertificateNumb…, CRT_UTC_IssueDate, CRT_UTC_CurrentTo, CRT_UTC_SubmissionD…, CRT_Nabers_StarRati…

## g0640（1 列）
- 見出し：CRT_Nabers_StarRating
- 例1 値：3 | 5 | 5 | 2.5 | 3.5
  - 同じ表の列：B_Suburb, B_State, B_Geocode, CRT_CertificateNumb…, CRT_UTC_IssueDate, CRT_UTC_CurrentTo, CRT_UTC_SubmissionD…, CRT_Nabers_Referenc…

## g0641（1 列）
- 見出し：CRT_Nabers_RatedArea
- 例1 値：24020.54 | 26721.64 | 15578.32 | 10969.95 | 624.73
  - 同じ表の列：B_Suburb, B_State, B_Geocode, CRT_CertificateNumb…, CRT_UTC_IssueDate, CRT_UTC_CurrentTo, CRT_UTC_SubmissionD…, CRT_Nabers_Referenc…

## g0642（2 列）
- 見出し：Seq
- 例1 値：251 | 540 | 11 | 367 | 294
  - 同じ表の列：Defect Number, DateRaised, RaisedBy, PrimaryLocation, LocationCategory, ResponseTime, DefectScore, TargetDate
- 例2 値：10 | 8 | 11 | 12 | 4
  - 同じ表の列：Y, X

## g0643（1 列）
- 見出し：Defect Number
- 例1 値：DN00821 | DN00266 | DN00183 | DN00190 | DN00408
  - 同じ表の列：Seq, DateRaised, RaisedBy, PrimaryLocation, LocationCategory, ResponseTime, DefectScore, TargetDate

## g0644（1 列）
- 見出し：DateRaised
- 例1 値：16/01/2018 12:00:00 AM | 13/10/2017 12:06:00 PM | 16/01/2018 12:00:00 AM | 7/11/2017 11:06:00 AM | 9/08/2017 1:58:00 PM
  - 同じ表の列：Seq, Defect Number, RaisedBy, PrimaryLocation, LocationCategory, ResponseTime, DefectScore, TargetDate

## g0645（1 列）
- 見出し：RaisedBy
- 例1 値：［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］ | ［個人名のため削除］
  - 同じ表の列：Seq, Defect Number, DateRaised, PrimaryLocation, LocationCategory, ResponseTime, DefectScore, TargetDate

## g0646（1 列）
- 見出し：PrimaryLocation
- 例1 値：James St | Baillie St | Sunnyside Ave | Golf Course Rd | Rose St
  - 同じ表の列：Seq, Defect Number, DateRaised, RaisedBy, LocationCategory, ResponseTime, DefectScore, TargetDate

## g0647（1 列）
- 見出し：LocationCategory
- 例1 値：ARTERIAL | COLLECTOR | ARTERIAL | ACCESS | ACCESS
  - 同じ表の列：Seq, Defect Number, DateRaised, RaisedBy, PrimaryLocation, ResponseTime, DefectScore, TargetDate

## g0648（1 列）
- 見出し：ResponseTime
- 例1 値：28.0000 | 60.0000 | 365.0000 | 365.0000 | 60.0000
  - 同じ表の列：Seq, Defect Number, DateRaised, RaisedBy, PrimaryLocation, LocationCategory, DefectScore, TargetDate

## g0649（1 列）
- 見出し：DefectScore
- 例1 値：0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000
  - 同じ表の列：Seq, Defect Number, DateRaised, RaisedBy, PrimaryLocation, LocationCategory, ResponseTime, TargetDate

## g0650（1 列）
- 見出し：TargetDate
- 例1 値：29/05/2018 12:00:00 AM | 13/02/2018 12:00:00 AM | 13/02/2018 12:00:00 AM | 13/02/2018 12:00:00 AM | 13/02/2018 12:00:00 AM
  - 同じ表の列：Seq, Defect Number, DateRaised, RaisedBy, PrimaryLocation, LocationCategory, ResponseTime, DefectScore

## g0651（1 列）
- 見出し：JobNumber
- 例1 値：3 | 3 | 3 | 3 | 3
  - 同じ表の列：Seq, Defect Number, DateRaised, RaisedBy, PrimaryLocation, LocationCategory, ResponseTime, DefectScore

## g0652（1 列）
- 見出し：ADMINTYPEN
- 例1 値：LOCALITY | LOCALITY | LOCALITY | LOCALITY | LOCALITY
  - 同じ表の列：OBJECTID, ADMINAREAN, LOC_CODE, Locality, AdminType, AdminArea, loaddate, supplydate

## g0653（1 列）
- 見出し：ADMINAREAN
- 例1 値：KIN KIN, NOOSA SHIRE | LAKE MACDONALD, NOOSA SHIRE | TINBEERWAH, NOOSA SHIRE | NOOSAVILLE, NOOSA SHIRE | SUNRISE BEACH, NOOSA SHIRE
  - 同じ表の列：OBJECTID, ADMINTYPEN, LOC_CODE, Locality, AdminType, AdminArea, loaddate, supplydate

## g0654（1 列）
- 見出し：LOC_CODE
- 例1 値：1646 | 697 | 4018 | 4008 | 2292
  - 同じ表の列：OBJECTID, ADMINTYPEN, ADMINAREAN, Locality, AdminType, AdminArea, loaddate, supplydate

## g0655（1 列）
- 見出し：Locality
- 例1 値：NOOSA NORTH SHORE | RINGTAIL CREEK | DOONAN | PINBARREN | COOTHARABA
  - 同じ表の列：OBJECTID, ADMINTYPEN, ADMINAREAN, LOC_CODE, AdminType, AdminArea, loaddate, supplydate

## g0656（1 列）
- 見出し：AdminType
- 例1 値：LOCAL GOVERNMENT | LOCAL GOVERNMENT | LOCAL GOVERNMENT | LOCAL GOVERNMENT | LOCAL GOVERNMENT
  - 同じ表の列：OBJECTID, ADMINTYPEN, ADMINAREAN, LOC_CODE, Locality, AdminArea, loaddate, supplydate

## g0657（1 列）
- 見出し：AdminArea
- 例1 値：NOOSA SHIRE | NOOSA SHIRE | NOOSA SHIRE | NOOSA SHIRE | NOOSA SHIRE
  - 同じ表の列：OBJECTID, ADMINTYPEN, ADMINAREAN, LOC_CODE, Locality, AdminType, loaddate, supplydate

## g0658（1 列）
- 見出し：loaddate
- 例1 値：20180918 | 20180918 | 20180918 | 20180918 | 20180918
  - 同じ表の列：OBJECTID, ADMINTYPEN, ADMINAREAN, LOC_CODE, Locality, AdminType, AdminArea, supplydate

## g0659（1 列）
- 見出し：supplydate
- 例1 値：20180918 | 20180918 | 20180918 | 20180918 | 20180918
  - 同じ表の列：OBJECTID, ADMINTYPEN, ADMINAREAN, LOC_CODE, Locality, AdminType, AdminArea, loaddate

## g0660（1 列）
- 見出し：verifydate
- 例1 値：20180918 | 20180918 | 20180918 | 20180918 | 20180918
  - 同じ表の列：OBJECTID, ADMINTYPEN, ADMINAREAN, LOC_CODE, Locality, AdminType, AdminArea, loaddate

## g0661（1 列）
- 見出し：Agency (Dept or Stat Body)
- 例1 値：QLeave | QLeave | QLeave | QLeave | QLeave
  - 同じ表の列：Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0662（1 列）
- 見出し：Award contract date
- 例1 値：2026-04-07 00:00:00 | 2026-03-11 00:00:00 | 2025-07-04 00:00:00 | 2025-09-02 00:00:00 | 2026-06-03 00:00:00
  - 同じ表の列：Agency (Dept or Sta…, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0663（1 列）
- 見出し：Contract value
- 例1 値：17500 | 83333.6 | 48714 | 14000 | 92608.64
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0664（2 列）
- 見出し：Variation to contract (Yes/No)
- 例1 値：No | No | No | Yes | No
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…
- 例2 値：No | Yes | No | Yes | Yes
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Specific confidenti…, Procurement Method, Limited Tendering R…, Form of contract, Number of offers so…

## g0665（1 列）
- 見出し：Specific confidentiality provision used
- 例1 値：ICT Professional services | Licenses & subscriptions | Recruitment Services | Training Services | ICT Professional services
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Procurement method, Reason for use of l…, Form of contract, Number of offers so…

## g0666（1 列）
- 見出し：Procurement method
- 例1 値：SOA | SOA | Single quote procurement | RFQ | N/A
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Reason for use of l…, Form of contract, Number of offers so…

## g0667（1 列）
- 見出し：Reason for use of limited tendering
- 例1 値：SOA | SOA | SOA | Exemption | SOA
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Form of contract, Number of offers so…

## g0668（1 列）
- 見出し：Form of contract
- 例1 値：QITC - General | SOA QDP0059-19 Order form | Short Form - Contract Details | QITC - Comprehensive | QITC Comprehensive - ICTSS.1303B
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Number of offers so…

## g0669（2 列）
- 見出し：Number of offers sought
- 例1 値：1 | 4 | 1 | 1 | 1
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement method, Reason for use of l…, Form of contract
- 例2 値：6
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement Method, Limited Tendering R…, Form of contract

## g0670（1 列）
- 見出し：Agency (Dept or Stat Body)
- 例1 値：Queensland Reconstruction Authority | Queensland Reconstruction Authority | Queensland Reconstruction Authority | Queensland Reconstruction Authority | Queensland Reconstruction Authority
  - 同じ表の列：Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement Method, Limited Tendering R…, Form of contract, Number of offers so…

## g0671（1 列）
- 見出し：Award contract date
- 例1 値：2025-09-30T00:00:00 | 2025-09-12T00:00:00 | 2025-11-11T00:00:00 | 2026-01-28T00:00:00 | 2026-01-23T00:00:00
  - 同じ表の列：Agency (Dept or Sta…, Contract value, Variation to contra…, Specific confidenti…, Procurement Method, Limited Tendering R…, Form of contract, Number of offers so…

## g0672（1 列）
- 見出し：Contract value
- 例1 値：$46,200 | $96,880 | $498,825 | $576,861 | $16,633,946
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Variation to contra…, Specific confidenti…, Procurement Method, Limited Tendering R…, Form of contract, Number of offers so…

## g0673（1 列）
- 見出し：Specific confidentiality provision in use
- 例1 値：No | No | No | No | No
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Procurement Method, Limited Tendering R…, Form of contract, Number of offers so…

## g0674（1 列）
- 見出し：Procurement Method
- 例1 値：Open | Selective | Limited | Open | Selective
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Limited Tendering R…, Form of contract, Number of offers so…

## g0675（1 列）
- 見出し：Limited Tendering Reason
- 例1 値：Article XIII (c)(ii)
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement Method, Form of contract, Number of offers so…

## g0676（1 列）
- 見出し：Form of contract
- 例1 値：SOA Order - ICT Products and Services, …
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement Method, Limited Tendering R…, Number of offers so…

## g0677（1 列）
- 見出し：Evaluation criteria and weightings
- 例1 値：Service Delivery 18%; Operations Manage…
  - 同じ表の列：Agency (Dept or Sta…, Award contract date, Contract value, Variation to contra…, Specific confidenti…, Procurement Method, Limited Tendering R…, Form of contract

## g0678（1 列）
- 見出し：search_abbr
- 例1 値：ST | AV | ST | AV | ST
  - 同じ表の列：locality, x, y, lga_code, src

## g0679（2 列）
- 見出し：locality
- 例1 値：STAWELL | RAINBOW | HAVEN | STAWELL | MARNOO
  - 同じ表の列：search_abbr, x, y, lga_code, src
- 例2 値：Anglesea | Winchelsea | Lorne | Torquay | Torquay
  - 同じ表の列：Holes, Long, Lat

## g0680（2 列）
- 見出し：x
- 例1 値：141.29192325 | 142.1939495 | 142.21109159 | 142.20513674 | 142.35996137
  - 同じ表の列：search_abbr, locality, y, lga_code, src
- 例2 値：142.197216981100 | 142.199621028060 | 142.197209891186 | 142.198242209452 | 142.200235794349
  - 同じ表の列：Seq, Y

## g0681（2 列）
- 見出し：y
- 例1 値：-37.0655883499997 | -36.7112101599997 | -35.6084193799997 | -37.0646957299997 | -36.7894118299997
  - 同じ表の列：search_abbr, locality, x, lga_code, src
- 例2 値：-36.716557180108 | -36.720657644535 | -36.713005353596 | -36.712208760248 | -36.718624277768
  - 同じ表の列：Seq, X

## g0682（1 列）
- 見出し：lga_code
- 例1 値：357 | 359 | 301 | 301 | 357
  - 同じ表の列：search_abbr, locality, x, y, src

## g0683（1 列）
- 見出し：src
- 例1 値：2 | 2 | 2 | 2 | 2
  - 同じ表の列：search_abbr, locality, x, y, lga_code

## g0684（1 列）
- 見出し：Watershed_BassinVersant
- 例1 値：2 | 1 | 1 | 2 | 3
  - 同じ表の列：Year_Annee, Month_Mois, Day_Jour, NH4_N

## g0685（1 列）
- 見出し：Year_Annee
- 例1 値：1996 | 2010 | 1996 | 2011 | 2011
  - 同じ表の列：Watershed_BassinVer…, Month_Mois, Day_Jour, NH4_N

## g0686（1 列）
- 見出し：Month_Mois
- 例1 値：3 | 3 | 4 | 3 | 3
  - 同じ表の列：Watershed_BassinVer…, Year_Annee, Day_Jour, NH4_N

## g0687（1 列）
- 見出し：Day_Jour
- 例1 値：11 | 10 | 23 | 10 | 22
  - 同じ表の列：Watershed_BassinVer…, Year_Annee, Month_Mois, NH4_N

## g0688（1 列）
- 見出し：NH4_N
- 例1 値：0.27 | 0.07 | 0.14 | 4.54 | 0.1
  - 同じ表の列：Watershed_BassinVer…, Year_Annee, Month_Mois, Day_Jour

## g0689（2 列）
- 見出し：Sample No. - No. d'echantillon
- 例1 値：CFP2023-0037 | CFP2023-0021 | CFP2023-0011 | CFP2023-0032 | CFP2023-0008
  - 同じ表の列：Sampling Region - R…, Function, Fonction, Origin, Origine, Product, Produit, Organic - Biologique
- 例2 値：CFP2022-0012 | CFP2022-0010 | CFP2022-0026 | CFP2022-0026 | CFP2022-0001
  - 同じ表の列：Function, Fonction, Origin, Origine, Product, Produit, Organic - Biologique, Date Sampled - Date…

## g0690（1 列）
- 見出し：Sampling Region - Region d'echantillonnage
- 例1 値：ONTARIO | ONTARIO | ONTARIO | ONTARIO | ONTARIO
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Organic - Biologique

## g0691（2 列）
- 見出し：Function
- 例1 値：Unknown | Import | Unknown | Domestic | Domestic
  - 同じ表の列：Sample No. - No. d'…, Sampling Region - R…, Fonction, Origin, Origine, Product, Produit, Organic - Biologique
- 例2 値：Import | Import | Domestic | Domestic | Import
  - 同じ表の列：Sample No. - No. d'…, Fonction, Origin, Origine, Product, Produit, Organic - Biologique, Date Sampled - Date…

## g0692（2 列）
- 見出し：Fonction
- 例1 値：Domestique | Importé | Importé | Importé | Importé
  - 同じ表の列：Sample No. - No. d'…, Sampling Region - R…, Function, Origin, Origine, Product, Produit, Organic - Biologique
- 例2 値：Inconnu | Inconnu | Importé | Inconnu | Domestique
  - 同じ表の列：Sample No. - No. d'…, Function, Origin, Origine, Product, Produit, Organic - Biologique, Date Sampled - Date…

## g0693（1 列）
- 見出し：Origin
- 例1 値：MEXICO | UNKNOWN | CHILE | UNKNOWN | CANADA
  - 同じ表の列：Sample No. - No. d'…, Sampling Region - R…, Function, Fonction, Origine, Product, Produit, Organic - Biologique

## g0694（1 列）
- 見出し：Origine
- 例1 値：CHILI | INCONNU | INCONNU | CHILI | CHILI
  - 同じ表の列：Sample No. - No. d'…, Sampling Region - R…, Function, Fonction, Origin, Product, Produit, Organic - Biologique

## g0695（1 列）
- 見出し：Product
- 例1 値：Infant Food (non-cereal) | Infant Food (non-cereal) | Infant Food (non-cereal) | Infant Food (non-cereal) | Infant Food (non-cereal)
  - 同じ表の列：Sample No. - No. d'…, Sampling Region - R…, Function, Fonction, Origin, Origine, Produit, Organic - Biologique

## g0696（1 列）
- 見出し：Produit
- 例1 値：Aliments pour nourrisson (non-céréales) | Aliments pour nourrisson (non-céréales) | Aliments pour nourrisson (non-céréales) | Aliments pour nourrisson (non-céréales) | Aliments pour nourrisson (non-céréales)
  - 同じ表の列：Sample No. - No. d'…, Sampling Region - R…, Function, Fonction, Origin, Origine, Product, Organic - Biologique

## g0697（2 列）
- 見出し：Organic - Biologique
- 例1 値：Yes - Oui | No - Non | Yes - Oui | No - Non | Yes - Oui
  - 同じ表の列：Sample No. - No. d'…, Sampling Region - R…, Function, Fonction, Origin, Origine, Product, Produit
- 例2 値：No - Non | No - Non | No - Non | No - Non | No - Non
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Date Sampled - Date…

## g0698（2 列）
- 見出し：Date Sampled - Date d'echantillonage
- 例1 値：21-Feb-2024 | 21-Feb-2024 | 21-Feb-2024 | 21-Feb-2024 | 21-Feb-2024
  - 同じ表の列：Sample No. - No. d'…, Sampling Region - R…, Function, Fonction, Origin, Origine, Product, Produit
- 例2 値：09-Nov-22 | 09-Nov-22 | 09-Nov-22 | 09-Nov-22 | 09-Nov-22
  - 同じ表の列：Sample No. - No. d'…, Function, Fonction, Origin, Origine, Product, Produit, Organic - Biologique

## g0699（1 列）
- 見出し：Year | Annee
- 例1 値：2011 | 2014 | 2017 | 2019 | 2013
  - 同じ表の列：Sample Type (Englis…, Sample Type (French…, Statistical Quantit…, Statistical Quantit…, <, Result | Resultat, Units | Unites

## g0700（1 列）
- 見出し：Sample Type (English) | Type d'echantillon (anglais)
- 例1 値：Atmospheric Releases | Liquid Releases | Atmospheric Releases | Atmospheric Releases | Atmospheric Releases
  - 同じ表の列：Year | Annee, Sample Type (French…, Statistical Quantit…, Statistical Quantit…, <, Result | Resultat, Units | Unites

## g0701（1 列）
- 見出し：Sample Type (French) | Type d'echantillon (francais)
- 例1 値：Rejets atmosphériques | Rejets atmosphériques | Rejets liquides | Rejets liquides | Rejets atmosphériques
  - 同じ表の列：Year | Annee, Sample Type (Englis…, Statistical Quantit…, Statistical Quantit…, <, Result | Resultat, Units | Unites

## g0702（1 列）
- 見出し：Statistical Quantity (English) | Quantite statistique (angla
- 例1 値：Weekly Average | Weekly Average | Monthly Average | Weekly Average | Monthly Average
  - 同じ表の列：Year | Annee, Sample Type (Englis…, Sample Type (French…, Statistical Quantit…, <, Result | Resultat, Units | Unites

## g0703（1 列）
- 見出し：Statistical Quantity (French) | Quantite statistique (franca
- 例1 値：Moyenne Hebdomadaire | Moyenne Mensuelle | Moyenne Hebdomadaire | Moyenne Hebdomadaire | Moyenne Mensuelle
  - 同じ表の列：Year | Annee, Sample Type (Englis…, Sample Type (French…, Statistical Quantit…, <, Result | Resultat, Units | Unites

## g0704（1 列）
- 見出し：<
- 例1 値：< | < | < | < | <
  - 同じ表の列：Year | Annee, Sample Type (Englis…, Sample Type (French…, Statistical Quantit…, Statistical Quantit…, Result | Resultat, Units | Unites

## g0705（1 列）
- 見出し：Result | Resultat
- 例1 値：1.29E+04 | 4.19E+05 | 4.30E+07 | 1.34E+11 | 5.38E+12
  - 同じ表の列：Year | Annee, Sample Type (Englis…, Sample Type (French…, Statistical Quantit…, Statistical Quantit…, <, Units | Unites

## g0706（1 列）
- 見出し：Units | Unites
- 例1 値：Bq/mo | Bq/wk | Bq/sem | Bq/wk | Bq/sem | Bq/mo | Bq/mo
  - 同じ表の列：Year | Annee, Sample Type (Englis…, Sample Type (French…, Statistical Quantit…, Statistical Quantit…, <, Result | Resultat

## g0707（1 列）
- 見出し：Jurisdiction
- 例1 値：Nunavut | British Columbia | Ontario | Northwest Territories | Nova Scotia
  - 同じ表の列：2019, 2020, 2021, 2022, 2023

## g0708（1 列）
- 見出し：2019
- 例1 値：43820 | 2040 | 10330 | 24970 | 3990
  - 同じ表の列：Jurisdiction, 2020, 2021, 2022, 2023

## g0709（1 列）
- 見出し：2020
- 例1 値：274900 | 0 | 220 | 42880 | 3970
  - 同じ表の列：Jurisdiction, 2019, 2021, 2022, 2023

## g0710（1 列）
- 見出し：2021
- 例1 値：44800 | 1370 | 70 | 150 | 26220
  - 同じ表の列：Jurisdiction, 2019, 2020, 2022, 2023

## g0711（1 列）
- 見出し：2022
- 例1 値：1060 | 115270 | 100 | 291750 | 230
  - 同じ表の列：Jurisdiction, 2019, 2020, 2021, 2023

## g0712（1 列）
- 見出し：2023
- 例1 値：190 | 280 | 140 | 39110 | 2240
  - 同じ表の列：Jurisdiction, 2019, 2020, 2021, 2022

## g0713（1 列）
- 見出し：Age Range / Tranche d'age
- 例1 値：45 - 54 | <25 | Unknown / Inconnu | 55+ | 35 - 44
  - 同じ表の列：11-Dec, 2012/13, 2013/14, 2014/15, 2015/16, 2016/17, 2017/18, 2018/19

## g0714（1 列）
- 見出し：11-Dec
- 例1 値：238 | 576 | 44 | 540 | 658
  - 同じ表の列：Age Range / Tranche…, 2012/13, 2013/14, 2014/15, 2015/16, 2016/17, 2017/18, 2018/19

## g0715（1 列）
- 見出し：2012/13
- 例1 値：261 | 31 | 629 | 548 | 2137
  - 同じ表の列：Age Range / Tranche…, 11-Dec, 2013/14, 2014/15, 2015/16, 2016/17, 2017/18, 2018/19

## g0716（1 列）
- 見出し：2013/14
- 例1 値：689 | 2242 | 674 | 304 | 45
  - 同じ表の列：Age Range / Tranche…, 11-Dec, 2012/13, 2014/15, 2015/16, 2016/17, 2017/18, 2018/19

## g0717（1 列）
- 見出し：2014/15
- 例1 値：712 | 500 | 2240 | 306 | 682
  - 同じ表の列：Age Range / Tranche…, 11-Dec, 2012/13, 2013/14, 2015/16, 2016/17, 2017/18, 2018/19

## g0718（1 列）
- 見出し：2015/16
- 例1 値：438 | 43 | 754 | 341 | 2227
  - 同じ表の列：Age Range / Tranche…, 11-Dec, 2012/13, 2013/14, 2014/15, 2016/17, 2017/18, 2018/19

## g0719（1 列）
- 見出し：2016/17
- 例1 値：796 | 2310 | 55 | 387 | 447
  - 同じ表の列：Age Range / Tranche…, 11-Dec, 2012/13, 2013/14, 2014/15, 2015/16, 2017/18, 2018/19

## g0720（1 列）
- 見出し：2017/18
- 例1 値：82 | 393 | 2468 | 28 | 828
  - 同じ表の列：Age Range / Tranche…, 11-Dec, 2012/13, 2013/14, 2014/15, 2015/16, 2016/17, 2018/19

## 答えの雛形

```
g0601	
g0602	
g0603	
g0604	
g0605	
g0606	
g0607	
g0608	
g0609	
g0610	
g0611	
g0612	
g0613	
g0614	
g0615	
g0616	
g0617	
g0618	
g0619	
g0620	
g0621	
g0622	
g0623	
g0624	
g0625	
g0626	
g0627	
g0628	
g0629	
g0630	
g0631	
g0632	
g0633	
g0634	
g0635	
g0636	
g0637	
g0638	
g0639	
g0640	
g0641	
g0642	
g0643	
g0644	
g0645	
g0646	
g0647	
g0648	
g0649	
g0650	
g0651	
g0652	
g0653	
g0654	
g0655	
g0656	
g0657	
g0658	
g0659	
g0660	
g0661	
g0662	
g0663	
g0664	
g0665	
g0666	
g0667	
g0668	
g0669	
g0670	
g0671	
g0672	
g0673	
g0674	
g0675	
g0676	
g0677	
g0678	
g0679	
g0680	
g0681	
g0682	
g0683	
g0684	
g0685	
g0686	
g0687	
g0688	
g0689	
g0690	
g0691	
g0692	
g0693	
g0694	
g0695	
g0696	
g0697	
g0698	
g0699	
g0700	
g0701	
g0702	
g0703	
g0704	
g0705	
g0706	
g0707	
g0708	
g0709	
g0710	
g0711	
g0712	
g0713	
g0714	
g0715	
g0716	
g0717	
g0718	
g0719	
g0720	
```
