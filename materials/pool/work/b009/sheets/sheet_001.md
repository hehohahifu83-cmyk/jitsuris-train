# ラベル用シート 001 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：Final Dispatch Code
- 例1 値：Code 1 | Code 2 | Code 1 | Code 1 | Code 2
  - 同じ表の列：%<=15mins, AVG RT - Seconds, Total Number
- 例2 値：Code 2 | Code 1 | Code 1 | Code 2 | Code 2
  - 同じ表の列：%<=15mins, AVG RT - Seconds, Total Number

## g0002（2 列）
- 見出し：%<=15mins
- 例1 値：79.37% | 81.74% | 88.83% | 79.95% | 67.53%
  - 同じ表の列：Final Dispatch Code, AVG RT - Seconds, Total Number
- 例2 値：91.4% | 87.9% | 90.6% | 56.5% | 65.7%
  - 同じ表の列：Final Dispatch Code, AVG RT - Seconds, Total Number

## g0003（2 列）
- 見出し：AVG RT - Seconds
- 例1 値：1418 | 831 | 1747 | 744 | 1572
  - 同じ表の列：Final Dispatch Code, %<=15mins, Total Number
- 例2 値：1232 | 1712 | 1619 | 1670 | 1441
  - 同じ表の列：Final Dispatch Code, %<=15mins, Total Number

## g0004（1 列）
- 見出し：Total Number
- 例1 値：1745 | 2081 | 6248 | 1327 | 487
  - 同じ表の列：Final Dispatch Code, %<=15mins, AVG RT - Seconds

## g0005（26 列）
- 見出し：Year
- 例1 値：2013 | 2021 | 2016 | 2020 | 2024
  - 同じ表の列：Category of death, Number of deaths, Rate per 10,000 est…
- 例2 値：2018 | 2018 | 2018 | 2018 | 2018
  - 同じ表の列：MNO, UMTS900, UMTS2100, LTE700, LTE900, LTE1800, LTE2100, LTE2300

## g0006（1 列）
- 見出し：Category of death
- 例1 値：Natural causes | Undetermined | Undetermined | Undetermined | External causes
  - 同じ表の列：Year, Number of deaths, Rate per 10,000 est…

## g0007（1 列）
- 見出し：Number of deaths
- 例1 値：16 | 65 | 14 | 69 | 6
  - 同じ表の列：Year, Category of death, Rate per 10,000 est…

## g0008（1 列）
- 見出し：Rate per 10,000 estimated resident population (0 to 17 years
- 例1 値：0.68 | 0.11 | 1.37 | 0.05 | 0.25
  - 同じ表の列：Year, Category of death, Number of deaths

## g0009（2 列）
- 見出し：X
- 例1 値：138.6853475 | 138.633852 | 138.6604761 | 138.6768246 | 138.6402071
  - 同じ表の列：Y, TreeID, Circumfere, TreeHeight, BotanicalN
- 例2 値：138.67118792 | 138.65168768 | 138.65126104 | 138.65754337 | 138.65361710
  - 同じ表の列：Feature, Y

## g0010（2 列）
- 見出し：Y
- 例1 値：-34.91796524 | -34.91679268 | -34.92160295 | -34.92274775 | -34.91820578
  - 同じ表の列：X, TreeID, Circumfere, TreeHeight, BotanicalN
- 例2 値：-34.92620697 | -34.92767184 | -34.93668586 | -34.94329415 | -34.94731055
  - 同じ表の列：Feature, X

## g0011（1 列）
- 見出し：TreeID
- 例1 値：742 | 242 | 754 | 780 | 27893
  - 同じ表の列：X, Y, Circumfere, TreeHeight, BotanicalN

## g0012（1 列）
- 見出し：Circumfere
- 例1 値：less than 2m | less than 2m | less than 2m | greater than 3m | less than 2m
  - 同じ表の列：X, Y, TreeID, TreeHeight, BotanicalN

## g0013（1 列）
- 見出し：TreeHeight
- 例1 値：5-10m | greater than 20m | 10-20m | 5-10m | 5m
  - 同じ表の列：X, Y, TreeID, Circumfere, BotanicalN

## g0014（1 列）
- 見出し：BotanicalN
- 例1 値：Melia azedarach | Jacaranda mimosifolia | Ulmus procera | Eucalyptus leucoxylon | Eucalyptus camaldulensis
  - 同じ表の列：X, Y, TreeID, Circumfere, TreeHeight

## g0015（1 列）
- 見出し：Reference
- 例1 値：114802 | 122162 | 121316 | 120789 | 106629
  - 同じ表の列：Gender, Suburb

## g0016（1 列）
- 見出し：Gender
- 例1 値：Desexed Female | Male | Desexed Female | Female | Male
  - 同じ表の列：Reference, Suburb

## g0017（5 列）
- 見出し：Suburb
- 例1 値：ELIZABETH SOUTH | CRAIGMORE | BLAKEVIEW | ELIZABETH DOWNS | ANGLE VALE
  - 同じ表の列：Reference, Gender
- 例2 値：Carlton North | Richmond | Fitzroy North | Fitzroy North | Fitzroy
  - 同じ表の列：date_captured, section_start, section_end, direction_1, vehicles_1, direction_2, vehicles_2, volume_per_day

## g0018（1 列）
- 見出し：Supreme Court at a glance
- 例1 値：Number of criminal circuit lodgements^ | Family Group Conference number of child… | Family conference referrals | Lodgements (other courts and tribunals)* | Total lodged**
  - 同じ表の列：2020-21, 2021-22, 2022-23, 2023-24, 2024-25

## g0019（1 列）
- 見出し：2020-21
- 例1 値：136 | 452.88 | 1486 | 36 | 1546
  - 同じ表の列：Supreme Court at a …, 2021-22, 2022-23, 2023-24, 2024-25

## g0020（1 列）
- 見出し：2021-22
- 例1 値：211491 | - | - | 2021-22 | 20.2
  - 同じ表の列：Supreme Court at a …, 2020-21, 2022-23, 2023-24, 2024-25

## g0021（1 列）
- 見出し：2022-23
- 例1 値：2022-23 | 10476 | 34.6 | 7 | 4
  - 同じ表の列：Supreme Court at a …, 2020-21, 2021-22, 2023-24, 2024-25

## g0022（1 列）
- 見出し：2023-24
- 例1 値：104 | 33 | 104.6 | 0 | 1448
  - 同じ表の列：Supreme Court at a …, 2020-21, 2021-22, 2022-23, 2024-25

## g0023（4 列）
- 見出し：2024-25
- 例1 値：103 | 8661 | 108 | 1139 | 72
  - 同じ表の列：Supreme Court at a …, 2020-21, 2021-22, 2022-23, 2023-24
- 例2 値：2772 | 63 | 15 | 390 | 1207
  - 同じ表の列：FIVE YEAR DATA TIME…, 2020-21, 2021-22, 2022-23, 2023-24

## g0024（1 列）
- 見出し：Data as of
- 例1 値：1/09/2021 | 1/09/2021 | 1/09/2021 | 1/09/2021 | 1/09/2021
  - 同じ表の列：Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0025（1 列）
- 見出し：Licence No
- 例1 値：LIQC300230155 | LIQC300238830 | LIQC300242145 | LIQC300236838 | LIQC300239837
  - 同じ表の列：Data as of, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA

## g0026（2 列）
- 見出し：Start Date
- 例1 値：8/08/1947 | 11/10/1948 | 14/05/1953 | 10/07/1958 | 14/01/1957
  - 同じ表の列：Data as of, Licence No, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap, LGA
- 例2 値：13/07/1948 | 27/02/1967 | 17/05/1957 | 01/04/1957 | 12/11/1956
  - 同じ表の列：Licence number, Licence type, Status, Trading Status, Suburb, LGA, Precinct, Extended trading

## g0027（2 列）
- 見出し：Trading Status
- 例1 値：Trading | Trading | Trading | Trading | Trading
  - 同じ表の列：Data as of, Licence No, Start Date, Type, Filter Category, SA2 Band, Subject to Cap, LGA
- 例2 値：Trading | Trading | Trading | Trading | Trading
  - 同じ表の列：Licence number, Licence type, Status, Start date, Suburb, LGA, Precinct, Extended trading

## g0028（3 列）
- 見出し：Type
- 例1 値：Club | Club | Club | Club | Club
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Filter Category, SA2 Band, Subject to Cap, LGA
- 例2 値：Indoor | Outdoor | Outdoor | Outdoor | Indoor
  - 同じ表の列：BSSID

## g0029（1 列）
- 見出し：Filter Category
- 例1 値：Club - non-gaming | Club - small | Club - small | Club - small | Club - medium
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, SA2 Band, Subject to Cap, LGA

## g0030（1 列）
- 見出し：SA2 Band
- 例1 値：1 | 1 | 1 | 2 | 2
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, Subject to Cap, LGA

## g0031（1 列）
- 見出し：Subject to Cap
- 例1 値：No | Yes | No | Yes | Yes
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, LGA

## g0032（1 列）
- 見出し：LGA
- 例1 値：Carrathool Shire Council | Lake Macquarie City Council | Northern Beaches Council | Newcastle City Council | Wollondilly Shire Council
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap

## g0033（1 列）
- 見出し：Region
- 例1 値：Metropolitan | Metropolitan | Metropolitan | Country | Country
  - 同じ表の列：Data as of, Licence No, Start Date, Trading Status, Type, Filter Category, SA2 Band, Subject to Cap

## g0034（1 列）
- 見出し：Consultancies
- 例1 値：PriceWaterhouseCoopers | PwC | JP Media | Consultancies | Infinity Ventures Pty Ltd
  - 同じ表の列：Purpose, 2018-19 $ Actual pa…, 2019-20 $ Actual pa…, 2020-21 $ Actual pa…, 2021-22 $ Actual pa…, 2022-23 $ Actual Pa…, 2023-24 $ Actual Pa…

## g0035（1 列）
- 見出し：Purpose
- 例1 値：To work with Harvard University in the … | To develop a proposal to support the de… | Total | Various | Procurement and process support for the…
  - 同じ表の列：Consultancies, 2018-19 $ Actual pa…, 2019-20 $ Actual pa…, 2020-21 $ Actual pa…, 2021-22 $ Actual pa…, 2022-23 $ Actual Pa…, 2023-24 $ Actual Pa…

## g0036（1 列）
- 見出し：2018-19 $ Actual payment
- 例1 値：$29,750 | $10,750 | $ Actual payment | $41,000 | $48 650
  - 同じ表の列：Consultancies, Purpose, 2019-20 $ Actual pa…, 2020-21 $ Actual pa…, 2021-22 $ Actual pa…, 2022-23 $ Actual Pa…, 2023-24 $ Actual Pa…

## g0037（1 列）
- 見出し：2019-20 $ Actual payment
- 例1 値：$17 462
  - 同じ表の列：Consultancies, Purpose, 2018-19 $ Actual pa…, 2020-21 $ Actual pa…, 2021-22 $ Actual pa…, 2022-23 $ Actual Pa…, 2023-24 $ Actual Pa…

## g0038（1 列）
- 見出し：2020-21 $ Actual payment
- 例1 値：$18 279
  - 同じ表の列：Consultancies, Purpose, 2018-19 $ Actual pa…, 2019-20 $ Actual pa…, 2021-22 $ Actual pa…, 2022-23 $ Actual Pa…, 2023-24 $ Actual Pa…

## g0039（1 列）
- 見出し：2021-22 $ Actual payment
- 例1 値：$8 355
  - 同じ表の列：Consultancies, Purpose, 2018-19 $ Actual pa…, 2019-20 $ Actual pa…, 2020-21 $ Actual pa…, 2022-23 $ Actual Pa…, 2023-24 $ Actual Pa…

## g0040（1 列）
- 見出し：2022-23 $ Actual Payment
- 例1 値：$11,261
  - 同じ表の列：Consultancies, Purpose, 2018-19 $ Actual pa…, 2019-20 $ Actual pa…, 2020-21 $ Actual pa…, 2021-22 $ Actual pa…, 2023-24 $ Actual Pa…

## g0041（1 列）
- 見出し：2023-24 $ Actual Payment
- 例1 値：$24,928
  - 同じ表の列：Consultancies, Purpose, 2018-19 $ Actual pa…, 2019-20 $ Actual pa…, 2020-21 $ Actual pa…, 2021-22 $ Actual pa…, 2022-23 $ Actual Pa…

## g0042（2 列）
- 見出し：Years
- 例1 値：2021-12-31 | 2011-12-31 | 2017-12-31 | 2010-12-31 | 2019-12-31
  - 同じ表の列：Number of attendees
- 例2 値：2016-06-30 | 2018-06-30 | 2023-06-30 | 2014-06-30 | 2021-06-30
  - 同じ表の列：NSW visitor expendi…

## g0043（1 列）
- 見出し：Number of attendees
- 例1 値：6,132,827 | 9,195,572 | 5,818,163 | 6,073,498 | 1,960,925
  - 同じ表の列：Years

## g0044（1 列）
- 見出し：Provider Identifier (ABN)
- 例1 値：92766868403 | 77638834599 | 88851368006 | 40300173822 | 17059209675
  - 同じ表の列：Delivery Area, Gender, Indigenous status, Commissioning Agency, Agreement Identifier, Agreement Start Date, Agreement End Date

## g0045（1 列）
- 見出し：Delivery Area
- 例1 値：Local Government Area | Local Government Area | Local Government Area | Local Government Area | Local Government Area
  - 同じ表の列：Provider Identifier…, Gender, Indigenous status, Commissioning Agency, Agreement Identifier, Agreement Start Date, Agreement End Date

## g0046（4 列）
- 見出し：Gender
- 例1 値：All | All | All | All | All
  - 同じ表の列：Provider Identifier…, Delivery Area, Indigenous status, Commissioning Agency, Agreement Identifier, Agreement Start Date, Agreement End Date
- 例2 値：F | F | F | M | F
  - 同じ表の列：Locality, Animal_Type

## g0047（1 列）
- 見出し：Indigenous status
- 例1 値：Not applicable | Not applicable | Not applicable | Not applicable | Not applicable
  - 同じ表の列：Provider Identifier…, Delivery Area, Gender, Commissioning Agency, Agreement Identifier, Agreement Start Date, Agreement End Date

## g0048（1 列）
- 見出し：Commissioning Agency
- 例1 値：Department of Family and Community Serv… | Department of Family and Community Serv… | Department of Family and Community Serv… | Department of Family and Community Serv… | Department of Family and Community Serv…
  - 同じ表の列：Provider Identifier…, Delivery Area, Gender, Indigenous status, Agreement Identifier, Agreement Start Date, Agreement End Date

## g0049（1 列）
- 見出し：Agreement Identifier
- 例1 値：04690-05 | 04904-04 | 02035-04 | 00570-05 | 05043-05
  - 同じ表の列：Provider Identifier…, Delivery Area, Gender, Indigenous status, Commissioning Agency, Agreement Start Date, Agreement End Date

## g0050（1 列）
- 見出し：Agreement Start Date
- 例1 値：01/07/2015 | 01/07/2015 | 01/07/2015 | 01/07/2015 | 01/07/2015
  - 同じ表の列：Provider Identifier…, Delivery Area, Gender, Indigenous status, Commissioning Agency, Agreement Identifier, Agreement End Date

## g0051（1 列）
- 見出し：Agreement End Date
- 例1 値：31/03/2016 | 30/06/2016 | 30/06/2018 | 30/06/2018 | 30/06/2018
  - 同じ表の列：Provider Identifier…, Delivery Area, Gender, Indigenous status, Commissioning Agency, Agreement Identifier, Agreement Start Date

## g0052（1 列）
- 見出し：dateType
- 例1 値：PARLIAMENT_SITTING | MULTI_FAITH | MULTI_FAITH | PUBLIC_HOLIDAY | MULTI_FAITH
  - 同じ表の列：important_date, publisher, source

## g0053（1 列）
- 見出し：important_date
- 例1 値：7/10/2018 | 27/02/2021 | 5/10/2019 | 5/04/2020 | 15/08/2021
  - 同じ表の列：dateType, publisher, source

## g0054（1 列）
- 見出し：publisher
- 例1 値：Faith Communities Council of Victoria | Faith Communities Council of Victoria | Faith Communities Council of Victoria | Faith Communities Council of Victoria | No Source - Generated
  - 同じ表の列：dateType, important_date, source

## g0055（1 列）
- 見出し：source
- 例1 値：http://www.faithvictoria.org.au/calendar | http://www.faithvictoria.org.au/calendar | http://www.faithvictoria.org.au/calendar | http://www.faithvictoria.org.au/calendar | http://www.faithvictoria.org.au/calendar
  - 同じ表の列：dateType, important_date, publisher

## g0056（1 列）
- 見出し：DateID
- 例1 値：201209 | 201209 | 201209 | 201209 | 201209
  - 同じ表の列：FinancialYear, LGA, District, GreenfieldLabel, GreenfieldGrowthArea, DwellingType, NetCompletion

## g0057（1 列）
- 見出し：FinancialYear
- 例1 値：2012-13 | 2012-13 | 2012-13 | 2012-13 | 2012-13
  - 同じ表の列：DateID, LGA, District, GreenfieldLabel, GreenfieldGrowthArea, DwellingType, NetCompletion

## g0058（1 列）
- 見出し：LGA
- 例1 値：Blacktown | Blacktown | Blacktown | Blacktown | Blacktown
  - 同じ表の列：DateID, FinancialYear, District, GreenfieldLabel, GreenfieldGrowthArea, DwellingType, NetCompletion

## g0059（1 列）
- 見出し：District
- 例1 値：Central City | Western City | Central City | Central City | Central City
  - 同じ表の列：DateID, FinancialYear, LGA, GreenfieldLabel, GreenfieldGrowthArea, DwellingType, NetCompletion

## g0060（1 列）
- 見出し：GreenfieldLabel
- 例1 値：Infill | Oran Park | Riverstone | Infill | Infill
  - 同じ表の列：DateID, FinancialYear, LGA, District, GreenfieldGrowthArea, DwellingType, NetCompletion

## g0061（1 列）
- 見出し：GreenfieldGrowthArea
- 例1 値：Infill | Infill | South West Growth Area | South West Growth Area | Infill
  - 同じ表の列：DateID, FinancialYear, LGA, District, GreenfieldLabel, DwellingType, NetCompletion

## g0062（1 列）
- 見出し：DwellingType
- 例1 値：Detached | Detached | Detached | Detached | Detached
  - 同じ表の列：DateID, FinancialYear, LGA, District, GreenfieldLabel, GreenfieldGrowthArea, NetCompletion

## g0063（1 列）
- 見出し：NetCompletion
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：DateID, FinancialYear, LGA, District, GreenfieldLabel, GreenfieldGrowthArea, DwellingType

## g0064（1 列）
- 見出し：AgencyCategory
- 例1 値：Transport, Roads and Maritime | Justice | Education | Transport | Transport, Roads and Maritime
  - 同じ表の列：ProjectType, Type, Location, LGA, Region, StartYear, CompletionYear, ETC

## g0065（1 列）
- 見出し：ProjectType
- 例1 値：Utilities | Transport | Government Services | Utilities | Community Services
  - 同じ表の列：AgencyCategory, Type, Location, LGA, Region, StartYear, CompletionYear, ETC

## g0066（1 列）
- 見出し：Type
- 例1 値：Work-In-Progress | Work-In-Progress | Work-In-Progress | Work-In-Progress | Work-In-Progress
  - 同じ表の列：AgencyCategory, ProjectType, Location, LGA, Region, StartYear, CompletionYear, ETC

## g0067（1 列）
- 見出し：Location
- 例1 値：Various | Various | Randwick | Sydney | Gunnedah
  - 同じ表の列：AgencyCategory, ProjectType, Type, LGA, Region, StartYear, CompletionYear, ETC

## g0068（1 列）
- 見出し：LGA
- 例1 値：Liverpool | Penrith,Liverpool | Central Coast | Sydney | Sutherland,Wingecarribee,Shellharbour
  - 同じ表の列：AgencyCategory, ProjectType, Type, Location, Region, StartYear, CompletionYear, ETC

## g0069（1 列）
- 見出し：Region
- 例1 値：Hunter | Hunter | Metropolitan Sydney | Metropolitan Sydney | Riverina-Murray,Central West and Orana,…
  - 同じ表の列：AgencyCategory, ProjectType, Type, Location, LGA, StartYear, CompletionYear, ETC

## g0070（1 列）
- 見出し：StartYear
- 例1 値：2013 | 2015 | 2016 | 2014 | 2016
  - 同じ表の列：AgencyCategory, ProjectType, Type, Location, LGA, Region, CompletionYear, ETC

## g0071（1 列）
- 見出し：CompletionYear
- 例1 値：2018 | 2020 | 2017 | n.a. | 2027
  - 同じ表の列：AgencyCategory, ProjectType, Type, Location, LGA, Region, StartYear, ETC

## g0072（1 列）
- 見出し：ETC
- 例1 値：6300 | 3382 | 185071 | 64560 | 550000
  - 同じ表の列：AgencyCategory, ProjectType, Type, Location, LGA, Region, StartYear, CompletionYear

## g0073（1 列）
- 見出し：EstSpendTo20160630
- 例1 値：67 | 18962 | 32989 | 0 | 907
  - 同じ表の列：AgencyCategory, ProjectType, Type, Location, LGA, Region, StartYear, CompletionYear

## g0074（1 列）
- 見出し：Genotype
- 例1 値：YUF16-V033 | YRD16-V045 | YUD16-V021 | YRI16-V024 | YSC16-03-142
  - 同じ表の列：Cypress, Diamante, Doongara, Jefferson, Kyeema, L205, Langi, Lemont

## g0075（1 列）
- 見出し：Cypress
- 例1 値：-0.677399016 | 0.933255143 | 0.792981474 | -0.291456402 | 0.353100562
  - 同じ表の列：Genotype, Diamante, Doongara, Jefferson, Kyeema, L205, Langi, Lemont

## g0076（1 列）
- 見出し：Diamante
- 例1 値：-0.026704122 | 0.258905324 | 0.492045695 | -0.054705255 | -0.334247118
  - 同じ表の列：Genotype, Cypress, Doongara, Jefferson, Kyeema, L205, Langi, Lemont

## g0077（1 列）
- 見出し：Doongara
- 例1 値：-0.806569953 | 0.120253647 | -0.498799953 | 0.699440851 | -0.800385873
  - 同じ表の列：Genotype, Cypress, Diamante, Jefferson, Kyeema, L205, Langi, Lemont

## g0078（1 列）
- 見出し：Jefferson
- 例1 値：0.038867341 | 0.515470408 | -0.385084254 | -0.675277698 | 0.433401016
  - 同じ表の列：Genotype, Cypress, Diamante, Doongara, Kyeema, L205, Langi, Lemont

## g0079（1 列）
- 見出し：Kyeema
- 例1 値：-0.198773303 | 0.244945485 | 0.377290256 | -0.310245869 | 0.288978578
  - 同じ表の列：Genotype, Cypress, Diamante, Doongara, Jefferson, L205, Langi, Lemont

## g0080（1 列）
- 見出し：L205
- 例1 値：-0.001167433 | -0.265356648 | 0.505718432 | -0.145843557 | 0.388829993
  - 同じ表の列：Genotype, Cypress, Diamante, Doongara, Jefferson, Kyeema, Langi, Lemont

## g0081（1 列）
- 見出し：Langi
- 例1 値：-0.195097443 | -0.254677091 | -0.110572245 | 0.068221749 | -0.81214186
  - 同じ表の列：Genotype, Cypress, Diamante, Doongara, Jefferson, Kyeema, L205, Lemont

## g0082（1 列）
- 見出し：Lemont
- 例1 値：-0.323038118 | 1.940945697 | -0.663173092 | -0.727082034 | 0.10609327
  - 同じ表の列：Genotype, Cypress, Diamante, Doongara, Jefferson, Kyeema, L205, Langi

## g0083（1 列）
- 見出し：Topaz
- 例1 値：-0.219459803 | 0.782671906 | 0.027599794 | 0.034341468 | -0.215764134
  - 同じ表の列：Genotype, Cypress, Diamante, Doongara, Jefferson, Kyeema, L205, Langi

## g0084（1 列）
- 見出し：Site
- 例1 値：North Moreton Bay | Mooloolaba | North Moreton Bay | Caloundra | Caloundra
  - 同じ表の列：SiteNumber, Seconds, DateTime, Hs, Hmax, Tp, Tz, SST

## g0085（1 列）
- 見出し：SiteNumber
- 例1 値：52 | 54 | 52 | 52 | 54
  - 同じ表の列：Site, Seconds, DateTime, Hs, Hmax, Tp, Tz, SST

## g0086（2 列）
- 見出し：Seconds
- 例1 値：1792288800 | 1792378800 | 1792204200 | 1792787400 | 1792742400
  - 同じ表の列：Site, SiteNumber, DateTime, Hs, Hmax, Tp, Tz, SST
- 例2 値：1792590000 | 1792566600 | 1792527600 | 1792282200 | 1792383000
  - 同じ表の列：Site, DateTime, Water Level, Prediction, Residual

## g0087（1 列）
- 見出し：DateTime
- 例1 値：2026-10-17T10:00:00 | 2026-10-22T03:30:00 | 2026-10-20T02:00:00 | 2026-10-24T16:30:00 | 2026-10-21T19:30:00
  - 同じ表の列：Site, SiteNumber, Seconds, Hs, Hmax, Tp, Tz, SST

## g0088（1 列）
- 見出し：Hs
- 例1 値：1.199 | 1.606 | 1.465 | 1.876 | 1.321
  - 同じ表の列：Site, SiteNumber, Seconds, DateTime, Hmax, Tp, Tz, SST

## g0089（1 列）
- 見出し：Hmax
- 例1 値：2.630 | 2.000 | 2.890 | 2.030 | 2.140
  - 同じ表の列：Site, SiteNumber, Seconds, DateTime, Hs, Tp, Tz, SST

## g0090（1 列）
- 見出し：Tp
- 例1 値：7.140 | 7.690 | 7.140 | 11.110 | 9.090
  - 同じ表の列：Site, SiteNumber, Seconds, DateTime, Hs, Hmax, Tz, SST

## g0091（1 列）
- 見出し：Tz
- 例1 値：4.651 | 5.128 | 5.063 | 5.882 | 5.634
  - 同じ表の列：Site, SiteNumber, Seconds, DateTime, Hs, Hmax, Tp, SST

## g0092（1 列）
- 見出し：SST
- 例1 値：21.75 | 21.80 | 21.85 | 21.55 | 21.80
  - 同じ表の列：Site, SiteNumber, Seconds, DateTime, Hs, Hmax, Tp, Tz

## g0093（1 列）
- 見出し：Direction
- 例1 値：87.20 | 78.80 | 77.30 | 70.30 | 68.90
  - 同じ表の列：Site, SiteNumber, Seconds, DateTime, Hs, Hmax, Tp, Tz

## g0094（5 列）
- 見出し：Year
- 例1 値：2016-17 | 2021-22 | 2013-14 | 2020-21 | 2015-16
  - 同じ表の列：Level A, Level B, Level D
- 例2 値：2018-19 | 2022-23 | 2011-12 | 2015-16 | 2019-20
  - 同じ表の列：Number of payments, Value of payments (…

## g0095（1 列）
- 見出し：Level A
- 例1 値：1 | 3 | 2 | 3 | 3
  - 同じ表の列：Year, Level B, Level D

## g0096（1 列）
- 見出し：Level B
- 例1 値：2 | 3 | 2 | 2 | 1
  - 同じ表の列：Year, Level A, Level D

## g0097（1 列）
- 見出し：Level D
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Year, Level A, Level B

## g0098（1 列）
- 見出し：Title
- 例1 値：Beerwah Library | Roma Courthouse | Caboolture Library | The Ridge Shopping Centre | Brisbane Magistrates Court
  - 同じ表の列：Location, Services, Office type, Counter type, Suburb, Fax, Mon am, Mon pm

## g0099（1 列）
- 見出し：Location
- 例1 値：Ipswich | Brisbane - South | Central Queensland | Brisbane - North | Sunshine Coast
  - 同じ表の列：Title, Services, Office type, Counter type, Suburb, Fax, Mon am, Mon pm

## g0100（1 列）
- 見出し：Services
- 例1 値：Volunteer Justice of the Peace or Commi… | Volunteer Justice of the Peace or Commi… | Volunteer Justice of the Peace or Commi… | Volunteer Justice of the Peace or Commi… | Volunteer Justice of the Peace or Commi…
  - 同じ表の列：Title, Location, Office type, Counter type, Suburb, Fax, Mon am, Mon pm

## g0101（1 列）
- 見出し：Office type
- 例1 値：Service | Service | Service | Service | Service
  - 同じ表の列：Title, Location, Services, Counter type, Suburb, Fax, Mon am, Mon pm

## g0102（1 列）
- 見出し：Counter type
- 例1 値：JPs in the community program | JPs in the community program | JPs in the community program | JPs in the community program | JPs in the community program
  - 同じ表の列：Title, Location, Services, Office type, Suburb, Fax, Mon am, Mon pm

## g0103（1 列）
- 見出し：Suburb
- 例1 値：MITCHELTON | CHINCHILLA | MOORE PARK BEACH | MOGGILL | ROMA
  - 同じ表の列：Title, Location, Services, Office type, Counter type, Fax, Mon am, Mon pm

## g0104（1 列）
- 見出し：Fax
- 例1 値：(07) 3247 5669
  - 同じ表の列：Title, Location, Services, Office type, Counter type, Suburb, Mon am, Mon pm

## g0105（1 列）
- 見出し：Mon am
- 例1 値：10:00-12:00 | 10:00-12:00 | 10:00-12:00 | 11:00-12:00 | 10:00-12:00
  - 同じ表の列：Title, Location, Services, Office type, Counter type, Suburb, Fax, Mon pm

## g0106（1 列）
- 見出し：Mon pm
- 例1 値：12:00-15:30 | 13:00-16:00 | 13:00-16:00 | 13:00-15:00 | 12:00-13:00
  - 同じ表の列：Title, Location, Services, Office type, Counter type, Suburb, Fax, Mon am

## g0107（1 列）
- 見出し：Tues am
- 例1 値：9:30-12:00 | 9:00-12:00 | 8:00-11:30 | 10:30-12:00 | 10:00-12:00
  - 同じ表の列：Title, Location, Services, Office type, Counter type, Suburb, Fax, Mon am

## g0108（1 列）
- 見出し：Time
- 例1 値：2020-07-31T23:15:16+10:00 | 2020-07-31T13:03:45+10:00 | 2020-07-31T11:17:11+10:00 | 2020-07-31T17:45:09+10:00 | 2020-07-31T13:47:15+10:00
  - 同じ表の列：Device ID, Temperature (°C), Humidity (%), Location

## g0109（1 列）
- 見出し：Device ID
- 例1 値：00137a100000a7bc | 00137a100000a7b7 | 00137a100000a7bd | 00137a100000a7b3 | 00137a100000a7bb
  - 同じ表の列：Time, Temperature (°C), Humidity (%), Location

## g0110（1 列）
- 見出し：Temperature (°C)
- 例1 値：15.73 | 14.84 | 16.07 | 15.55 | 12.94
  - 同じ表の列：Time, Device ID, Humidity (%), Location

## g0111（1 列）
- 見出し：Humidity (%)
- 例1 値：64.07 | 75.88 | 65.97 | 65.76 | 79.15
  - 同じ表の列：Time, Device ID, Temperature (°C), Location

## g0112（1 列）
- 見出し：Location
- 例1 値：-32.96457,151.69576 | -32.96501,151.700817 | -32.964044,151.694939 | -32.96863,151.69129 | -32.96614,151.69276
  - 同じ表の列：Time, Device ID, Temperature (°C), Humidity (%)

## g0113（1 列）
- 見出し：SA4 Groupings
- 例1 値：North West NSW | Central Coast, Newcastle | Regional total | NSW | Sydney-North
  - 同じ表の列：Major Cities, Inner Regional, Outer Regional, Remote, Very Remote, Total

## g0114（1 列）
- 見出し：Major Cities
- 例1 値：341 | 160 | 190 | 148 | 16
  - 同じ表の列：SA4 Groupings, Inner Regional, Outer Regional, Remote, Very Remote, Total

## g0115（1 列）
- 見出し：Inner Regional
- 例1 値：46 | 93 | 221 | 140 | 2
  - 同じ表の列：SA4 Groupings, Major Cities, Outer Regional, Remote, Very Remote, Total

## g0116（1 列）
- 見出し：Outer Regional
- 例1 値：304 | 1 | 20 | 305 | 123
  - 同じ表の列：SA4 Groupings, Major Cities, Inner Regional, Remote, Very Remote, Total

## g0117（1 列）
- 見出し：Remote
- 例1 値：9 | 35 | 26 | 35
  - 同じ表の列：SA4 Groupings, Major Cities, Inner Regional, Outer Regional, Very Remote, Total

## g0118（1 列）
- 見出し：Very Remote
- 例1 値：1 | 15 | 15 | 14
  - 同じ表の列：SA4 Groupings, Major Cities, Inner Regional, Outer Regional, Remote, Total

## g0119（2 列）
- 見出し：Total
- 例1 値：2213 | 131 | 149 | 173 | 258
  - 同じ表の列：SA4 Groupings, Major Cities, Inner Regional, Outer Regional, Remote, Very Remote
- 例2 値：688 | 2691 | 167 | 360 | 592
  - 同じ表の列：Tenure type, Very low income <$6…, Low income $603-$96…, Moderate income $96…

## g0120（1 列）
- 見出し：FIVE YEAR DATA TIME SERIES
- 例1 値：Number of attendees to education sessio… | New Matters Opened | Complaints/Information Requests | Number clients who received guardianshi… | Number clients screened for potential g…
  - 同じ表の列：2020-21, 2021-22, 2022-23, 2023-24, 2024-25

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
