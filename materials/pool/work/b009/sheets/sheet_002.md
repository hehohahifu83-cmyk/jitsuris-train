# ラベル用シート 002 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（5 列）
- 見出し：2020-21
- 例1 値：60 | 303 | 2 | 17 | 29
  - 同じ表の列：FIVE YEAR DATA TIME…, 2021-22, 2022-23, 2023-24, 2024-25
- 例2 値：2552 | 4434 | 42819 | 55747 | 5942
  - 同じ表の列：Jurisdiction, 2021-22, 2022-23, 2023-24, 2024-25

## g0122（4 列）
- 見出し：2021-22
- 例1 値：464 | 26646 | 24 | 4 | 3
  - 同じ表の列：FIVE YEAR DATA TIME…, 2020-21, 2022-23, 2023-24, 2024-25
- 例2 値：5571 | 61561 | 45713 | 6955 | 3322
  - 同じ表の列：Jurisdiction, 2020-21, 2022-23, 2023-24, 2024-25

## g0123（4 列）
- 見出し：2022-23
- 例1 値：48 | 3 | 189 | 267 | 1414
  - 同じ表の列：FIVE YEAR DATA TIME…, 2020-21, 2021-22, 2023-24, 2024-25
- 例2 値：3661 | 57553 | 6732 | 41985 | 5175
  - 同じ表の列：Jurisdiction, 2020-21, 2021-22, 2023-24, 2024-25

## g0124（3 列）
- 見出し：2023-24
- 例1 値：439 | 0 | 361 | 54 | 7
  - 同じ表の列：FIVE YEAR DATA TIME…, 2020-21, 2021-22, 2022-23, 2024-25
- 例2 値：4193 | 46561 | 63416 | 7480 | 5182
  - 同じ表の列：Jurisdiction, 2020-21, 2021-22, 2022-23, 2024-25

## g0125（1 列）
- 見出し：Collection_Date
- 例1 値：2018-09-09 | 2019-10-02 | 2019-12-02 | 2018-08-14 | 2020-04-14
  - 同じ表の列：Schedule_Code, Bin_Types, PickupDay, Actual_PickupDay, Comments

## g0126（1 列）
- 見出し：Schedule_Code
- 例1 値：2 | 2 | 1 | 2 | 2
  - 同じ表の列：Collection_Date, Bin_Types, PickupDay, Actual_PickupDay, Comments

## g0127（1 列）
- 見出し：Bin_Types
- 例1 値：General Waste (Blue Lid) & Organics (Gr… | General Waste (Blue Lid) & Organics (Gr… | General Waste (Blue Lid) & Organics (Gr… | General Waste (Blue Lid) & Organics (Gr… | General Waste (Blue Lid) & Organics (Gr…
  - 同じ表の列：Collection_Date, Schedule_Code, PickupDay, Actual_PickupDay, Comments

## g0128（1 列）
- 見出し：PickupDay
- 例1 値：Saturday | Wednesday | Wednesday | Friday | Wednesday
  - 同じ表の列：Collection_Date, Schedule_Code, Bin_Types, Actual_PickupDay, Comments

## g0129（1 列）
- 見出し：Actual_PickupDay
- 例1 値：NULL | NULL | NULL | NULL | NULL
  - 同じ表の列：Collection_Date, Schedule_Code, Bin_Types, PickupDay, Comments

## g0130（1 列）
- 見出し：Comments
- 例1 値：NULL | NULL | NULL | NULL | NULL
  - 同じ表の列：Collection_Date, Schedule_Code, Bin_Types, PickupDay, Actual_PickupDay

## g0131（1 列）
- 見出し：2019-20
- 例1 値：Contractors with a value below $10,000 … | Total contractors combined | Central Adelaide Local Health Network | Total Contractors | South Australian Ambulance Service
  - 同じ表の列：Purpose, Value

## g0132（1 列）
- 見出し：Purpose
- 例1 値：Fees for Health Pathway Services | Fees for cervical screening self-collec… | Machinery of Government Project | Fees for Evaluating community, neighbou… | Perform a rapid review of mental health…
  - 同じ表の列：2019-20, Value

## g0133（1 列）
- 見出し：Value
- 例1 値：$982,243.00 | $1,024,082.00 | 45,000 | 168,787 | 37,000
  - 同じ表の列：2019-20, Purpose

## g0134（1 列）
- 見出し：Date
- 例1 値：31-May-18 | 31-May-18 | 31-May-18 | 31-May-18 | 31-May-18
  - 同じ表の列：Capacity__ML_, Volume_today__ML_, Average_Volume_this…

## g0135（1 列）
- 見出し：Capacity__ML_
- 例1 値：44435 | 2935 | 15715 | 18685 | 4711
  - 同じ表の列：Date, Volume_today__ML_, Average_Volume_this…

## g0136（1 列）
- 見出し：Volume_today__ML_
- 例1 値：10282.63 | 28473.83 | 7963.76 | 2030.75 | 2090.6
  - 同じ表の列：Date, Capacity__ML_, Average_Volume_this…

## g0137（1 列）
- 見出し：Average_Volume_this_Month
- 例1 値：28961.14 | 8046.49 | 4076.05 | 21743.88 | 8073.9
  - 同じ表の列：Date, Capacity__ML_, Volume_today__ML_

## g0138（1 列）
- 見出し：Tenure type
- 例1 値：Rented: TOTAL | Rented: Public | Rented: Private and not stated | Rented: Public | Being purchased (incl rent/buy)
  - 同じ表の列：Very low income <$6…, Low income $603-$96…, Moderate income $96…, Total

## g0139（1 列）
- 見出し：Very low income <$603 per wk
- 例1 値：2868 | 0 | 2032 | 4056 | 461
  - 同じ表の列：Tenure type, Low income $603-$96…, Moderate income $96…, Total

## g0140（1 列）
- 見出し：Low income $603-$964 per wk
- 例1 値：140 | 31381 | 0 | 35 | 512
  - 同じ表の列：Tenure type, Very low income <$6…, Moderate income $96…, Total

## g0141（1 列）
- 見出し：Moderate income $965-$1446 per wk
- 例1 値：256 | 3 | 291 | 17 | 27
  - 同じ表の列：Tenure type, Very low income <$6…, Low income $603-$96…, Total

## g0142（1 列）
- 見出し：No of Engagements
- 例1 値：Operations Educational Tours, Visits & … | Operations Educational Tours, Visits & … | No Attended | Home Fire Safety Presentation | Total
  - 同じ表の列：2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23

## g0143（1 列）
- 見出し：2015-16
- 例1 値：197 | 2015-16 | 862 | 56 708 | 665
  - 同じ表の列：No of Engagements, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23

## g0144（1 列）
- 見出し：2016-17
- 例1 値：671 | 2016-17 | 3 303 | 100 | 64 197
  - 同じ表の列：No of Engagements, 2015-16, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23

## g0145（1 列）
- 見出し：2017-18
- 例1 値：2 769 | 104 | 81 922 | 2017-18 | 84 691
  - 同じ表の列：No of Engagements, 2015-16, 2016-17, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23

## g0146（1 列）
- 見出し：2018-19
- 例1 値：83 206 | 78 088 | 969 | 166 | 2018-19
  - 同じ表の列：No of Engagements, 2015-16, 2016-17, 2017-18, 2019-20, 2020-21, 2021-22, 2022-23

## g0147（1 列）
- 見出し：2019-20
- 例1 値：91 | 510 | 2019-20 | 5 815 | 117 321
  - 同じ表の列：No of Engagements, 2015-16, 2016-17, 2017-18, 2018-19, 2020-21, 2021-22, 2022-23

## g0148（1 列）
- 見出し：2020-21
- 例1 値：147 | 0 | 147 | 4 306 | 0
  - 同じ表の列：No of Engagements, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2021-22, 2022-23

## g0149（1 列）
- 見出し：2021-22
- 例1 値：172 | 3 688 | 2021-22 | 118 378 | 105
  - 同じ表の列：No of Engagements, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2022-23

## g0150（1 列）
- 見出し：2022-23
- 例1 値：125 345 | 656 | 152 | 2022-23 | 504
  - 同じ表の列：No of Engagements, 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22

## g0151（1 列）
- 見出し：Reason for fee waiver, by sector
- 例1 値：LOCAL - financial disadvantage | LOCAL - Other | UNIVERSITIES - Other | LOCAL - Fee reduced | UNIVERSITIES - Fee reduced
  - 同じ表の列：No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0152（1 列）
- 見出し：No. of waivers/reductions 2024-25
- 例1 値：532 | 5213 | 36 | 64 | 1
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0153（1 列）
- 見出し：No. of waivers/reductions 2023-24
- 例1 値：830 | 2 | 163 | 45 | 17
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0154（1 列）
- 見出し：No. of waivers/reductions 2022-23
- 例1 値：0 | 36 | 1839 | 0 | 147
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0155（1 列）
- 見出し：No. of waivers/reductions 2017-18
- 例1 値：799 | 0 | 8 | 1 | 161
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0156（1 列）
- 見出し：No. of waivers/reductions 2016-17
- 例1 値：17 | 10 | 0 | 1 | 377
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0157（1 列）
- 見出し：No. of waivers/reductions 2015-16
- 例1 値：0 | 13 | 219 | 0 | 371
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0158（1 列）
- 見出し：No. of waivers/reductions 2014-15
- 例1 値：28 | 1 | 473 | 22 | 19
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0159（1 列）
- 見出し：No. of waivers/reductions 2013-14
- 例1 値：0 | 11 | 637 | 0 | 5
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0160（1 列）
- 見出し：No. of waivers/reductions 2012-13
- 例1 値：6 | 18 | 1017 | 17 | 10
  - 同じ表の列：Reason for fee waiv…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…, No. of waivers/redu…

## g0161（1 列）
- 見出し：Number of payments
- 例1 値：3,224 | 8,602 | 9,644 | 9,789 | 10,648
  - 同じ表の列：Year, Value of payments (…

## g0162（1 列）
- 見出し：Value of payments ($ million)
- 例1 値：30 | 163 | 26.4 | 190.3 | 108.1
  - 同じ表の列：Year, Number of payments

## g0163（1 列）
- 見出し：Nil to report
- 例1 値：Nil to report | Nil to report | Consultancies above $10 000 each | Consultancies with a contract value bel… | Consultancies below $10 000 each
  - 同じ表の列：Number, Total $

## g0164（1 列）
- 見出し：Number
- 例1 値：Number | n/a | n/a | n/a | n/a
  - 同じ表の列：Nil to report, Total $

## g0165（1 列）
- 見出し：Total $
- 例1 値：Total $ | Total $ | Total $ | 20 050 | Total $
  - 同じ表の列：Nil to report, Number

## g0166（1 列）
- 見出し：Row
- 例1 値：107 | 185 | 12 | 219 | 16
  - 同じ表の列：CaseID, Segment6, SubmittedDate, ResponseTimeMinutes, SQ1, SQ1_OTH, SQ2, SQ3

## g0167（1 列）
- 見出し：CaseID
- 例1 値：136 | 130 | 168 | 121 | 58
  - 同じ表の列：Row, Segment6, SubmittedDate, ResponseTimeMinutes, SQ1, SQ1_OTH, SQ2, SQ3

## g0168（1 列）
- 見出し：Segment6
- 例1 値：Partial User Sydney | Partial User Sydney | Non User Sydney | Partial User Sydney | Full User Sydney
  - 同じ表の列：Row, CaseID, SubmittedDate, ResponseTimeMinutes, SQ1, SQ1_OTH, SQ2, SQ3

## g0169（1 列）
- 見出し：SubmittedDate
- 例1 値：25-Jan-23 | 25-Jan-23 | 25-Jan-23 | 25-Jan-23 | 25-Jan-23
  - 同じ表の列：Row, CaseID, Segment6, ResponseTimeMinutes, SQ1, SQ1_OTH, SQ2, SQ3

## g0170（1 列）
- 見出し：ResponseTimeMinutes
- 例1 値：14.65783333 | 6.219333333 | 7.841 | 21.42433333 | 21.41883333
  - 同じ表の列：Row, CaseID, Segment6, SubmittedDate, SQ1, SQ1_OTH, SQ2, SQ3

## g0171（1 列）
- 見出し：SQ1
- 例1 値：Male | Female | Female | Female | Female
  - 同じ表の列：Row, CaseID, Segment6, SubmittedDate, ResponseTimeMinutes, SQ1_OTH, SQ2, SQ3

## g0172（1 列）
- 見出し：SQ1_OTH
- 例1 値：NA | NA | NA | NA | NA
  - 同じ表の列：Row, CaseID, Segment6, SubmittedDate, ResponseTimeMinutes, SQ1, SQ2, SQ3

## g0173（1 列）
- 見出し：SQ2
- 例1 値：1990 | 1993 | 1999 | 1995 | 1986
  - 同じ表の列：Row, CaseID, Segment6, SubmittedDate, ResponseTimeMinutes, SQ1, SQ1_OTH, SQ3

## g0174（1 列）
- 見出し：SQ3
- 例1 値：Other NSW | Other NSW | Other NSW | Sydney | Sydney
  - 同じ表の列：Row, CaseID, Segment6, SubmittedDate, ResponseTimeMinutes, SQ1, SQ1_OTH, SQ2

## g0175（1 列）
- 見出し：SQ4
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：Row, CaseID, Segment6, SubmittedDate, ResponseTimeMinutes, SQ1, SQ1_OTH, SQ2

## g0176（1 列）
- 見出し：BSSID
- 例1 値：f8:4f:57:37:dc:20 | 50:17:FF:DC:93:A0 | 0c:68:03:32:33:40 | 50:17:FF:DC:94:A0 | 50:17:FF:DC:C3:E0
  - 同じ表の列：Type

## g0177（1 列）
- 見出し：OID
- 例1 値：154 | 378 | 314 | 828 | 283
  - 同じ表の列：VALUE, COUNT, FOR_TEN, FOR_CATEGO, FOREST, STATE, FIRE_1617, FIRE_1718

## g0178（4 列）
- 見出し：VALUE
- 例1 値：641 | 15 | 400 | 299 | 393
  - 同じ表の列：OID, COUNT, FOR_TEN, FOR_CATEGO, FOREST, STATE, FIRE_1617, FIRE_1718
- 例2 値：196 | 17 | 17771 | 7838 | 25
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02451V02968, County, C02669V03229, Nationality of Pupil

## g0179（2 列）
- 見出し：COUNT
- 例1 値：1585 | 143116 | 30802 | 4905 | 24293
  - 同じ表の列：OID, VALUE, FOR_TEN, FOR_CATEGO, FOREST, STATE, FIRE_1617, FIRE_1718
- 例2 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Agency, Application Accesss, Application Outcome, Application Transfe…, Calendar Year, Cluster, Decision, Fiscal Year

## g0180（1 列）
- 見出し：FOR_TEN
- 例1 値：PRIV | OCL | PRIV | PRIV | OCL
  - 同じ表の列：OID, VALUE, COUNT, FOR_CATEGO, FOREST, STATE, FIRE_1617, FIRE_1718

## g0181（1 列）
- 見出し：FOR_CATEGO
- 例1 値：Native forest | Native forest | Native forest | Native forest | Native forest
  - 同じ表の列：OID, VALUE, COUNT, FOR_TEN, FOREST, STATE, FIRE_1617, FIRE_1718

## g0182（1 列）
- 見出し：FOREST
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：OID, VALUE, COUNT, FOR_TEN, FOR_CATEGO, STATE, FIRE_1617, FIRE_1718

## g0183（8 列）
- 見出し：STATE
- 例1 値：Qld | Qld | Qld | Qld | NT
  - 同じ表の列：OID, VALUE, COUNT, FOR_TEN, FOR_CATEGO, FOREST, FIRE_1617, FIRE_1718
- 例2 値：WA | WA | NSW | NSW | WA
  - 同じ表の列：ABN, Town_City, Country, Charity_Website, Registration_Date, Date_Organisation_E…, Charity_Size, Number_of_Responsib…

## g0184（1 列）
- 見出し：FIRE_1617
- 例1 値：P | U | U | P | U
  - 同じ表の列：OID, VALUE, COUNT, FOR_TEN, FOR_CATEGO, FOREST, STATE, FIRE_1718

## g0185（1 列）
- 見出し：FIRE_1718
- 例1 値：U | P | U | U | U
  - 同じ表の列：OID, VALUE, COUNT, FOR_TEN, FOR_CATEGO, FOREST, STATE, FIRE_1617

## g0186（1 列）
- 見出し：FIRE_1819
- 例1 値：P | U | P | U | P
  - 同じ表の列：OID, VALUE, COUNT, FOR_TEN, FOR_CATEGO, FOREST, STATE, FIRE_1617

## g0187（1 列）
- 見出し：MNO
- 例1 値：Optus | Optus | Optus | Optus | Optus
  - 同じ表の列：Year, UMTS900, UMTS2100, LTE700, LTE900, LTE1800, LTE2100, LTE2300

## g0188（1 列）
- 見出し：UMTS900
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Year, MNO, UMTS2100, LTE700, LTE900, LTE1800, LTE2100, LTE2300

## g0189（1 列）
- 見出し：UMTS2100
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Year, MNO, UMTS900, LTE700, LTE900, LTE1800, LTE2100, LTE2300

## g0190（1 列）
- 見出し：LTE700
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Year, MNO, UMTS900, UMTS2100, LTE900, LTE1800, LTE2100, LTE2300

## g0191（1 列）
- 見出し：LTE900
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Year, MNO, UMTS900, UMTS2100, LTE700, LTE1800, LTE2100, LTE2300

## g0192（1 列）
- 見出し：LTE1800
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Year, MNO, UMTS900, UMTS2100, LTE700, LTE900, LTE2100, LTE2300

## g0193（1 列）
- 見出し：LTE2100
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Year, MNO, UMTS900, UMTS2100, LTE700, LTE900, LTE1800, LTE2300

## g0194（1 列）
- 見出し：LTE2300
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Year, MNO, UMTS900, UMTS2100, LTE700, LTE900, LTE1800, LTE2100

## g0195（1 列）
- 見出し：LTE2600
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Year, MNO, UMTS900, UMTS2100, LTE700, LTE900, LTE1800, LTE2100

## g0196（1 列）
- 見出し：ABN
- 例1 値：24998086842 | 71990561840 | 70588983437 | 41645428600 | 58144836077
  - 同じ表の列：Town_City, State, Country, Charity_Website, Registration_Date, Date_Organisation_E…, Charity_Size, Number_of_Responsib…

## g0197（1 列）
- 見出し：Town_City
- 例1 値：Dubbo | Altona | Upper Coomera | Melbourne | Palmyra
  - 同じ表の列：ABN, State, Country, Charity_Website, Registration_Date, Date_Organisation_E…, Charity_Size, Number_of_Responsib…

## g0198（1 列）
- 見出し：Country
- 例1 値：Australia | Australia | Australia | Australia | Australia
  - 同じ表の列：ABN, Town_City, State, Charity_Website, Registration_Date, Date_Organisation_E…, Charity_Size, Number_of_Responsib…

## g0199（1 列）
- 見出し：Charity_Website
- 例1 値：https://rccharity.net.au/ | warcq.org | https://auhklink.com/ | uqies.com | www.maltesewelfare.com.au
  - 同じ表の列：ABN, Town_City, State, Country, Registration_Date, Date_Organisation_E…, Charity_Size, Number_of_Responsib…

## g0200（1 列）
- 見出し：Registration_Date
- 例1 値：24/02/2021 | 11/02/2018 | 11/09/2024 | 10/12/2020 | 23/03/2021
  - 同じ表の列：ABN, Town_City, State, Country, Charity_Website, Date_Organisation_E…, Charity_Size, Number_of_Responsib…

## g0201（1 列）
- 見出し：Date_Organisation_Established
- 例1 値：23/03/2021 | 20/03/2025 | 26/09/1904 | 07/12/2020 | 27/04/2021
  - 同じ表の列：ABN, Town_City, State, Country, Charity_Website, Registration_Date, Charity_Size, Number_of_Responsib…

## g0202（1 列）
- 見出し：Charity_Size
- 例1 値：Small | Small | Small | Small | Small
  - 同じ表の列：ABN, Town_City, State, Country, Charity_Website, Registration_Date, Date_Organisation_E…, Number_of_Responsib…

## g0203（1 列）
- 見出し：Number_of_Responsible_Persons
- 例1 値：3 | 4 | 5 | 5 | 7
  - 同じ表の列：ABN, Town_City, State, Country, Charity_Website, Registration_Date, Date_Organisation_E…, Charity_Size

## g0204（1 列）
- 見出し：Financial_Year_End
- 例1 値：31-Dec | 30-Jun | 30-Jun | 30-Jun | 30-Jun
  - 同じ表の列：ABN, Town_City, State, Country, Charity_Website, Registration_Date, Date_Organisation_E…, Charity_Size

## g0205（1 列）
- 見出し：AR_number
- 例1 値：AR 43646 | AR 38625 | AR 75350 | AR 17780 | AR 57420
  - 同じ表の列：Lat, Lon, Year_gazetted_est_c…, Years_of_operation_…, Reference, Parish_Maps, Type

## g0206（9 列）
- 見出し：Lat
- 例1 値：-28.2401 | -29.5171 | -29.8186 | -30.0851 | -30.2989
  - 同じ表の列：AR_number, Lon, Year_gazetted_est_c…, Years_of_operation_…, Reference, Parish_Maps, Type
- 例2 値：-39.95100403 | -38.692745 | -31.653381 | -28.86076164 | -37.77695847
  - 同じ表の列：id, resourceType, title, startDate, endDate, lon, author, Evacuated

## g0207（5 列）
- 見出し：Lon
- 例1 値：143.5876 | 149.8195 | 152.7201 | 153.1316 | 152.8095
  - 同じ表の列：AR_number, Lat, Year_gazetted_est_c…, Years_of_operation_…, Reference, Parish_Maps, Type
- 例2 値：143.6531067 | 150.3315277 | 130.8186646 | 149.4580078 | 151.6669617
  - 同じ表の列：id, resourceType, title, startDate, endDate, lat, author, Evacuated

## g0208（1 列）
- 見出し：Year_gazetted_est_closure
- 例1 値：-1910 | 1909-1931 | 1957- | 1964- | 1893-1957
  - 同じ表の列：AR_number, Lat, Lon, Years_of_operation_…, Reference, Parish_Maps, Type

## g0209（1 列）
- 見出し：Years_of_operation_as_mission
- 例1 値：1950-1967 | 1936-1967 | 1932-1967 | 1906-1967 | 1911-1924
  - 同じ表の列：AR_number, Lat, Lon, Year_gazetted_est_c…, Reference, Parish_Maps, Type

## g0210（1 列）
- 見出し：Reference
- 例1 値：Felton, 2013, p.198 | Felton, 2013, p.244 | Felton, 2013, p.277 | Felton, 2013, p.172 | Felton, 2013, p.111
  - 同じ表の列：AR_number, Lat, Lon, Year_gazetted_est_c…, Years_of_operation_…, Parish_Maps, Type

## g0211（1 列）
- 見出し：Parish_Maps
- 例1 値：New South Wales Department of Lands 189… | New South Wales Department of Lands 195… | New South Wales Department of Lands 194… | New South Wales Department of Lands 188… | New South Wales Department of Lands 188…
  - 同じ表の列：AR_number, Lat, Lon, Year_gazetted_est_c…, Years_of_operation_…, Reference, Type

## g0212（1 列）
- 見出し：Type
- 例1 値：Reserves | Reserves | Camps | Unknown location reserves | Childrens homes
  - 同じ表の列：AR_number, Lat, Lon, Year_gazetted_est_c…, Years_of_operation_…, Reference, Parish_Maps

## g0213（1 列）
- 見出し：mort
- 例1 値：PHN503 | REM4 | GCC2GMEL | SEG4 | PHN306
  - 同じ表の列：category, geography, year, sex, deaths, population, crude_rate_per_1000…, age_standardised_ra…

## g0214（1 列）
- 見出し：category
- 例1 値：Socioeconomic group | Remoteness area | Greater Capital City Statistical Areas … | Greater Capital City Statistical Areas … | Socioeconomic group
  - 同じ表の列：mort, geography, year, sex, deaths, population, crude_rate_per_1000…, age_standardised_ra…

## g0215（1 列）
- 見出し：geography
- 例1 値：Quintile 4 | Australia (total) | Remote Australia | North Western Melbourne | Unknown/missing
  - 同じ表の列：mort, category, year, sex, deaths, population, crude_rate_per_1000…, age_standardised_ra…

## g0216（1 列）
- 見出し：sex
- 例1 値：Males | Persons | Males | Males | Persons
  - 同じ表の列：mort, category, geography, year, deaths, population, crude_rate_per_1000…, age_standardised_ra…

## g0217（1 列）
- 見出し：deaths
- 例1 値：161,300 | 4,264 | 234 | 11 | 88,801
  - 同じ表の列：mort, category, geography, year, sex, population, crude_rate_per_1000…, age_standardised_ra…

## g0218（1 列）
- 見出し：population
- 例1 値：2,765,999 | 1,470,219 | 123,492 | 50,847 | 796,567
  - 同じ表の列：mort, category, geography, year, sex, deaths, crude_rate_per_1000…, age_standardised_ra…

## g0219（1 列）
- 見出し：crude_rate_per_100000
- 例1 値：512.4 | 920 | 884.5 | 710.3 | 571.6
  - 同じ表の列：mort, category, geography, year, sex, deaths, population, age_standardised_ra…

## g0220（1 列）
- 見出し：age_standardised_rate_per_100000
- 例1 値：559.8 | 451.3 | 464.7 | 559.9 | 696.5
  - 同じ表の列：mort, category, geography, year, sex, deaths, population, crude_rate_per_1000…

## g0221（1 列）
- 見出し：rate_ratio
- 例1 値：1 | 1.07 | 0.92 | 1.37 | 1.07
  - 同じ表の列：mort, category, geography, year, sex, deaths, population, crude_rate_per_1000…

## g0222（1 列）
- 見出し：Total Number
- 例1 値：856 | 3,870 | 5,128 | 3,012 | 14,021
  - 同じ表の列：Final Dispatch Code, %<=15mins, AVG RT - Seconds

## g0223（1 列）
- 見出し：Organisation
- 例1 値：Horsham Regional Art Gallery | Artlink Australia | The Torch Project | St Martins Youth Arts Centre | Cultural Development Network
  - 同じ表の列：Type, Suburb/Town, Website

## g0224（1 列）
- 見出し：Type
- 例1 値：Gallery & Museum | Arts Space | Literary Magazine | Theatre | Production Company
  - 同じ表の列：Organisation, Suburb/Town, Website

## g0225（1 列）
- 見出し：Suburb/Town
- 例1 値：Horsham | North Carlton | Fitzroy | South Yarra | North Fitzroy
  - 同じ表の列：Organisation, Type, Website

## g0226（1 列）
- 見出し：Website
- 例1 値：http://www.lindenarts.org/ | http://www.historyvictoria.org.au | http://www.conical.org.au/ | http://www.thecapital.com.au | http://www.warrnambool.vic.gov.au/Page/…
  - 同じ表の列：Organisation, Type, Suburb/Town

## g0227（15 列）
- 見出し：id
- 例1 値：494 | 628 | 4658 | 37 | 4212
  - 同じ表の列：resourceType, title, startDate, endDate, lat, lon, author, Evacuated
- 例2 値：1287 | 1293 | 1343 | 1331 | 1216
  - 同じ表の列：lat, long, project_type, location, lga, cwlth_state_funding, project_status, recovery_type

## g0228（1 列）
- 見出し：resourceType
- 例1 値：Disaster Event | Disaster Event | Disaster Event | Disaster Event | Disaster Event
  - 同じ表の列：id, title, startDate, endDate, lat, lon, author, Evacuated

## g0229（1 列）
- 見出し：title
- 例1 値：Cyclone Tracy | Shipwreck - Postboy | Industrial - Mount St Canice | Epidemic - Bubonic Plague Sydney | Bushfire - Victoria
  - 同じ表の列：id, resourceType, startDate, endDate, lat, lon, author, Evacuated

## g0230（1 列）
- 見出し：startDate
- 例1 値：11/20/1989 0:00 | 10/24/1999 0:00 | 1/16/2002 0:00 | 8/18/2002 0:00 | 06/02/1851 00:00:00
  - 同じ表の列：id, resourceType, title, endDate, lat, lon, author, Evacuated

## g0231（1 列）
- 見出し：endDate
- 例1 値：12/31/1968 0:00 | 24/08/1857 00:00:00 | 1/5/1975 0:00 | 5/9/2006 0:00 | 8/13/1907 0:00
  - 同じ表の列：id, resourceType, title, startDate, lat, lon, author, Evacuated

## g0232（1 列）
- 見出し：Evacuated
- 例1 値：100 | 200000 | 11000 | 3000 | 6000
  - 同じ表の列：id, resourceType, title, startDate, endDate, lat, lon, author

## g0233（1 列）
- 見出し：Homeless
- 例1 値：300 | 100 | 41000 | 5000 | 5000
  - 同じ表の列：id, resourceType, title, startDate, endDate, lat, lon, author

## g0234（1 列）
- 見出し：Month
- 例1 値：Jul-19 | Jul-19 | Jul-19 | Jul-19 | Jul-19
  - 同じ表の列：State, Type of personal in…, In a business or co…, Industry of Employm…, Number of people en…

## g0235（1 列）
- 見出し：State
- 例1 値：Victoria | New South Wales | Victoria | Victoria | New South Wales
  - 同じ表の列：Month, Type of personal in…, In a business or co…, Industry of Employm…, Number of people en…

## g0236（1 列）
- 見出し：Type of personal insolvency administration
- 例1 値：Debtor's petition | Sequestration order | Total personal insolvencies | Debt agreement | Deceased estate
  - 同じ表の列：Month, State, In a business or co…, Industry of Employm…, Number of people en…

## g0237（1 列）
- 見出し：In a business or company
- 例1 値：Total | Total | Yes | Total | Total
  - 同じ表の列：Month, State, Type of personal in…, Industry of Employm…, Number of people en…

## g0238（1 列）
- 見出し：Industry of Employment
- 例1 値：Transport, postal and warehousing | Public administration and safety | Not engaged in any remunerative employm… | Manufacturing | Mining
  - 同じ表の列：Month, State, Type of personal in…, In a business or co…, Number of people en…

## g0239（1 列）
- 見出し：Number of people entering a new personal insolvency
- 例1 値：0 | 16 | 2 | 2 | 28
  - 同じ表の列：Month, State, Type of personal in…, In a business or co…, Industry of Employm…

## g0240（1 列）
- 見出し：FISHERY
- 例1 値：ETBF | HMI | SBTF | SSJF | NPF
  - 同じ表の列：GEAR, BOATS, YEAR, NUMBER_OF_SHOTS, HOURS_TRAWLED, HOURS_FISHED, NUMBER_OF_HOOKS, LENGTH_OF_GILLNET

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
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
g0195	
g0196	
g0197	
g0198	
g0199	
g0200	
g0201	
g0202	
g0203	
g0204	
g0205	
g0206	
g0207	
g0208	
g0209	
g0210	
g0211	
g0212	
g0213	
g0214	
g0215	
g0216	
g0217	
g0218	
g0219	
g0220	
g0221	
g0222	
g0223	
g0224	
g0225	
g0226	
g0227	
g0228	
g0229	
g0230	
g0231	
g0232	
g0233	
g0234	
g0235	
g0236	
g0237	
g0238	
g0239	
g0240	
```
