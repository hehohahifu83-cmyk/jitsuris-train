# ラベル用シート 001 / 001

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Type
- 例1 値：Road | Reserve | Road | Road | Road
  - 同じ表の列：Site, Locality, Ward, Authority, See Entry, Tree, Not in use, Unknown / uncertain

## g0002（1 列）
- 見出し：Site
- 例1 値：R0970 | R1232 | Opposite Leechs Lane, shops | R0423 | R3370
  - 同じ表の列：Type, Locality, Ward, Authority, See Entry, Tree, Not in use, Unknown / uncertain

## g0003（1 列）
- 見出し：Locality
- 例1 値：BUNH | GNPT | YNDN | MTCL | MPIE
  - 同じ表の列：Type, Site, Ward, Authority, See Entry, Tree, Not in use, Unknown / uncertain

## g0004（1 列）
- 見出し：Ward
- 例1 値：S | N | N | N | N
  - 同じ表の列：Type, Site, Locality, Authority, See Entry, Tree, Not in use, Unknown / uncertain

## g0005（1 列）
- 見出し：Authority
- 例1 値：B | C | B | B | B
  - 同じ表の列：Type, Site, Locality, Ward, See Entry, Tree, Not in use, Unknown / uncertain

## g0006（1 列）
- 見出し：See Entry
- 例1 値：Patanga Court | Civic Hall Surrounds | Elaine Avenue Reserve | Mount Callender | Ballarat Secondary College
  - 同じ表の列：Type, Site, Locality, Ward, Authority, Tree, Not in use, Unknown / uncertain

## g0007（1 列）
- 見出し：Tree
- 例1 値：2519, 3508 | 2664, 174 | 553 | 842
  - 同じ表の列：Type, Site, Locality, Ward, Authority, See Entry, Not in use, Unknown / uncertain

## g0008（1 列）
- 見出し：Not in use
- 例1 値：Y
  - 同じ表の列：Type, Site, Locality, Ward, Authority, See Entry, Tree, Unknown / uncertain

## g0009（1 列）
- 見出し：Unknown / uncertain
- 例1 値：Y
  - 同じ表の列：Type, Site, Locality, Ward, Authority, See Entry, Tree, Not in use

## g0010（1 列）
- 見出し：Beyond Maps
- 例1 値：Y | Y | Y | Y | Y
  - 同じ表の列：Type, Site, Locality, Ward, Authority, See Entry, Tree, Not in use

## g0011（1 列）
- 見出し：Executive classification
- 例1 値：Principal Band A-8 | Source: DECD VALEO system, DPC Workforc… | Notes: Executives are defined as employ… | PS Act Executive F - Untenured | Principal Band A-7
  - 同じ表の列：Number of executives

## g0012（1 列）
- 見出し：Number of executives
- 例1 値：92 | 27 | 51 | 2013 | 0
  - 同じ表の列：Executive classific…

## g0013（1 列）
- 見出し：School Number
- 例1 値：4032 | 230 | 1526 | 967 | 1045
  - 同じ表の列：Suburb

## g0014（1 列）
- 見出し：Suburb
- 例1 値：Marree | Melrose | Two Wells | Hillcrest | Andamooka
  - 同じ表の列：School Number

## g0015（1 列）
- 見出し：Category of complaint
- 例1 値：All consultancies below $10 000 each | Clearance decisions under Regulations b… | Consultancies above $10 000 each | Consultancies above $10 000 each | Clearance statistics
  - 同じ表の列：2011/12, 2012/13, 2013/14, 2015/16, 2016/17, 2017/18

## g0016（1 列）
- 見出し：2011/12
- 例1 値：0 | Business Name | 0 | 0 | 2
  - 同じ表の列：Category of complai…, 2012/13, 2013/14, 2015/16, 2016/17, 2017/18

## g0017（1 列）
- 見出し：2012/13
- 例1 値：178.23 | 2014-15 | 0 | 2016/17 | Ha Native Vegetation cleared
  - 同じ表の列：Category of complai…, 2011/12, 2013/14, 2015/16, 2016/17, 2017/18

## g0018（1 列）
- 見出し：2013/14
- 例1 値：2013/14 | Value | 300 | 341 | Trees removed
  - 同じ表の列：Category of complai…, 2011/12, 2012/13, 2015/16, 2016/17, 2017/18

## g0019（1 列）
- 見出し：2015/16
- 例1 値：913 418 | 952 765.74 | 0 | 0 | 2015/16
  - 同じ表の列：Category of complai…, 2011/12, 2012/13, 2013/14, 2016/17, 2017/18

## g0020（1 列）
- 見出し：2016/17
- 例1 値：0 | 0 | 0 | 18.91 | 0
  - 同じ表の列：Category of complai…, 2011/12, 2012/13, 2013/14, 2015/16, 2017/18

## g0021（1 列）
- 見出し：2017/18
- 例1 値：0 | 0 | 2017/18 | 2017/18 | 0
  - 同じ表の列：Category of complai…, 2011/12, 2012/13, 2013/14, 2015/16, 2016/17

## g0022（1 列）
- 見出し：Date/Time
- 例1 値：14/01/2026 19:00 | 30/01/2026 16:00 | 09/01/2026 21:00 | 13/01/2026 01:00 | 17/01/2026 00:00
  - 同じ表の列：O3 UVA ppm, O3 8hr UVA ppm, NO Chemiluminescenc…, NO2 calc Chemilumin…, NOx Chemiluminescen…

## g0023（1 列）
- 見出し：O3 UVA ppm
- 例1 値：0.019 | 0.034 | 0.018 | 0.026 | 0.017
  - 同じ表の列：Date/Time, O3 8hr UVA ppm, NO Chemiluminescenc…, NO2 calc Chemilumin…, NOx Chemiluminescen…

## g0024（1 列）
- 見出し：O3 8hr UVA ppm
- 例1 値：0.022 | 0.018 | 0.029 | 0.026 | 0.024
  - 同じ表の列：Date/Time, O3 UVA ppm, NO Chemiluminescenc…, NO2 calc Chemilumin…, NOx Chemiluminescen…

## g0025（1 列）
- 見出し：NO Chemiluminescence ppm
- 例1 値：0.000 | 0.000 | 0.000 | 0.000 | 0.001
  - 同じ表の列：Date/Time, O3 UVA ppm, O3 8hr UVA ppm, NO2 calc Chemilumin…, NOx Chemiluminescen…

## g0026（1 列）
- 見出し：NO2 calc Chemiluminescence ppm
- 例1 値：0.001 | 0.001 | 0.010 | 0.003 | 0.006
  - 同じ表の列：Date/Time, O3 UVA ppm, O3 8hr UVA ppm, NO Chemiluminescenc…, NOx Chemiluminescen…

## g0027（1 列）
- 見出し：NOx Chemiluminescence ppm
- 例1 値：0.024 | 0.001 | 0.006 | 0.004 | 0.003
  - 同じ表の列：Date/Time, O3 UVA ppm, O3 8hr UVA ppm, NO Chemiluminescenc…, NO2 calc Chemilumin…

## g0028（1 列）
- 見出し：Title
- 例1 値：Key Map Brisbane and Bremer Rivers 1000… | Key Map Bremer River flood maps SF14 SF… | Key Map Bremer River flood maps SF16 SF… | Key Map Coomera and Nerang Rivers flood… | Key Map Logan and Coomera Rivers flood …
  - 同じ表の列：Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format, Copyright status

## g0029（1 列）
- 見出し：Publication Date
- 例1 値：1975 | 1974 | 1974 | 1974 | 1974
  - 同じ表の列：Title, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format, Copyright status

## g0030（1 列）
- 見出し：Map Scale
- 例1 値：0 | 100000 | 100000 | 100000 | 100000
  - 同じ表の列：Title, Publication Date, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format, Copyright status

## g0031（1 列）
- 見出し：Map preview
- 例1 値：https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview filesiz…, Download link, Download filesize (…, Download Format, Copyright status

## g0032（1 列）
- 見出し：Map preview filesize (Megabytes)
- 例1 値：0.53 | 0.43 | 0.02 | 0.6 | 0.55
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Download link, Download filesize (…, Download Format, Copyright status

## g0033（1 列）
- 見出し：Download link
- 例1 値：https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat… | https://apps.information.qld.gov.au/dat…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download filesize (…, Download Format, Copyright status

## g0034（1 列）
- 見出し：Download filesize (Megabytes)
- 例1 値：5.91 | 8.29 | 6.08 | 0.1 | 4.68
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download Format, Copyright status

## g0035（1 列）
- 見出し：Download Format
- 例1 値：Digital format: image---jpeg Original f… | Digital format: image---jpeg Original f… | Digital format: image---jpeg Original f… | Digital format: image---jpeg Original f… | Digital format: image---jpeg Original f…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Copyright status

## g0036（1 列）
- 見出し：Copyright status
- 例1 値：CREATIVE COMMONS ATTRIBUTION | CREATIVE COMMONS ATTRIBUTION | CREATIVE COMMONS ATTRIBUTION | CREATIVE COMMONS ATTRIBUTION | CREATIVE COMMONS ATTRIBUTION
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format

## g0037（1 列）
- 見出し：Conditions of Use
- 例1 値：This material is licensed under Creativ… | This material is licensed under Creativ… | This material is licensed under Creativ… | This material is licensed under Creativ… | This material is licensed under Creativ…
  - 同じ表の列：Title, Publication Date, Map Scale, Map preview, Map preview filesiz…, Download link, Download filesize (…, Download Format

## g0038（1 列）
- 見出し：LHN/Hospital
- 例1 値：Northern Adelaide Local Health Network | Southern Adelaide Local Health Network | Country Health SA Local Health Network | Note: | Data source: Health Information Portal …
  - 同じ表の列：2012-13, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18

## g0039（1 列）
- 見出し：2012-13
- 例1 値：10,685 | 2,811 | 9,138 | 3,913 | 1,793
  - 同じ表の列：LHN/Hospital, 2013-14, 2014-15, 2015-16, 2016-17, 2017-18

## g0040（1 列）
- 見出し：2013-14
- 例1 値：2,692 | Sep Quarter | 2,636 | 16,396 | 11,049
  - 同じ表の列：LHN/Hospital, 2012-13, 2014-15, 2015-16, 2016-17, 2017-18

## g0041（1 列）
- 見出し：2014-15
- 例1 値：1,785 | 3,163 | 11,171 | Sep Quarter | 16,623
  - 同じ表の列：LHN/Hospital, 2012-13, 2013-14, 2015-16, 2016-17, 2017-18

## g0042（1 列）
- 見出し：2015-16
- 例1 値：20,373 | 9,293 | Sep Quarter | 16,525 | 3,385
  - 同じ表の列：LHN/Hospital, 2012-13, 2013-14, 2014-15, 2016-17, 2017-18

## g0043（1 列）
- 見出し：2016-17
- 例1 値：8,875 | 17,702 | 3,755 | 11,849 | 1,917
  - 同じ表の列：LHN/Hospital, 2012-13, 2013-14, 2014-15, 2015-16, 2017-18

## g0044（1 列）
- 見出し：2017-18
- 例1 値：10,407 | Sep Quarter | 3,452 | 11,665 | 10,290
  - 同じ表の列：LHN/Hospital, 2012-13, 2013-14, 2014-15, 2015-16, 2016-17

## g0045（1 列）
- 見出し：Inspections
- 例1 値：Follow-up inspections | Inspections from complaints | Inspections conducted | Number of businesses
  - 同じ表の列：Food safety risk cl…

## g0046（1 列）
- 見出し：Food safety risk classification
- 例1 値：2235 | 524 | P1 | 4867 | 6922
  - 同じ表の列：Inspections

## g0047（1 列）
- 見出し：No.
- 例1 値：4 | 5 | 3 | No. = Number; D = Descriptive evidence … | 2
  - 同じ表の列：Month and Year, Organism, Exposure setting, No. ill, No. laboratory conf…, Evidence

## g0048（1 列）
- 見出し：Month and Year
- 例1 値：Jan-20 | Jan-20 | Nov-19 | Sep-19 | Apr-20
  - 同じ表の列：No., Organism, Exposure setting, No. ill, No. laboratory conf…, Evidence

## g0049（1 列）
- 見出し：Organism
- 例1 値：S. Tm RDNC | S. Saintpaul | S. Tm 9 | S.Tm 9 | S.Tm 9
  - 同じ表の列：No., Month and Year, Exposure setting, No. ill, No. laboratory conf…, Evidence

## g0050（1 列）
- 見出し：Exposure setting
- 例1 値：Primary production | Restaurant | Take away | Private residence | Restaurant
  - 同じ表の列：No., Month and Year, Organism, No. ill, No. laboratory conf…, Evidence

## g0051（1 列）
- 見出し：No. ill
- 例1 値：5 | 2 | 5 | 5 | 45
  - 同じ表の列：No., Month and Year, Organism, Exposure setting, No. laboratory conf…, Evidence

## g0052（1 列）
- 見出し：No. laboratory confirmed
- 例1 値：5 | 5 | 2 | 5 | 45
  - 同じ表の列：No., Month and Year, Organism, Exposure setting, No. ill, Evidence

## g0053（1 列）
- 見出し：Evidence
- 例1 値：D | D, M | D, S, M | D | D
  - 同じ表の列：No., Month and Year, Organism, Exposure setting, No. ill, No. laboratory conf…

## g0054（1 列）
- 見出し：Year
- 例1 値：2005 | 2012 | 2015 | 2009 | 2002
  - 同じ表の列：Flora, Invertebrates, Birds, Mammals, Fish, Reptiles, Frogs

## g0055（1 列）
- 見出し：Flora
- 例1 値：68 | 74 | 109 | 110 | 59
  - 同じ表の列：Year, Invertebrates, Birds, Mammals, Fish, Reptiles, Frogs

## g0056（1 列）
- 見出し：Invertebrates
- 例1 値：48 | 18 | 44 | 9 | 51
  - 同じ表の列：Year, Flora, Birds, Mammals, Fish, Reptiles, Frogs

## g0057（1 列）
- 見出し：Birds
- 例1 値：13 | 0 | 8 | 17 | 17
  - 同じ表の列：Year, Flora, Invertebrates, Mammals, Fish, Reptiles, Frogs

## g0058（1 列）
- 見出し：Mammals
- 例1 値：20 | 17 | 11 | 21 | 13
  - 同じ表の列：Year, Flora, Invertebrates, Birds, Fish, Reptiles, Frogs

## g0059（1 列）
- 見出し：Fish
- 例1 値：24 | 24 | 21 | 0 | 20
  - 同じ表の列：Year, Flora, Invertebrates, Birds, Mammals, Reptiles, Frogs

## g0060（1 列）
- 見出し：Reptiles
- 例1 値：10 | 4 | 1 | 1 | 1
  - 同じ表の列：Year, Flora, Invertebrates, Birds, Mammals, Fish, Frogs

## g0061（1 列）
- 見出し：Frogs
- 例1 値：0 | 2 | 0 | 1 | 2
  - 同じ表の列：Year, Flora, Invertebrates, Birds, Mammals, Fish, Reptiles

## g0062（1 列）
- 見出し：All perpetrators
- 例1 値：Cohabiting partner | Total | Stranger | Boyfriend/girlfriend/date | Other known person
  - 同じ表の列：Sexual violence ('0…, Total women ('000)

## g0063（1 列）
- 見出し：Sexual violence ('000)
- 例1 値：30.2 | 45.2 | 44.2 | 75.8 | 171.6
  - 同じ表の列：All perpetrators, Total women ('000)

## g0064（1 列）
- 見出し：Total women ('000)
- 例1 値：9373.5 | 9373.5 | 9373.5 | 9373.5 | 9373.5
  - 同じ表の列：All perpetrators, Sexual violence ('0…

## g0065（1 列）
- 見出し：Product
- 例1 値：2016 | 2008 | 2000 | 2005 | 2013
  - 同じ表の列：Biomass, Fossil fuels, Metal ores, Non-metallic minera…, Total (All categori…

## g0066（1 列）
- 見出し：Biomass
- 例1 値：123151500 | 115963800 | 143881300 | 155334000 | 160529000
  - 同じ表の列：Product, Fossil fuels, Metal ores, Non-metallic minera…, Total (All categori…

## g0067（1 列）
- 見出し：Fossil fuels
- 例1 値：293902600 | 177606200 | 259703000 | 271479400 | 150781700
  - 同じ表の列：Product, Biomass, Metal ores, Non-metallic minera…, Total (All categori…

## g0068（1 列）
- 見出し：Metal ores
- 例1 値：266467900 | 302076600 | 266050900 | 256568800 | 226979500
  - 同じ表の列：Product, Biomass, Fossil fuels, Non-metallic minera…, Total (All categori…

## g0069（1 列）
- 見出し：Non-metallic minerals
- 例1 値：239904800 | 250629600 | 204783600 | 163091800 | 163166300
  - 同じ表の列：Product, Biomass, Fossil fuels, Metal ores, Total (All categori…

## g0070（1 列）
- 見出し：Total (All categories)
- 例1 値：1018331700 | 693829900 | 739419600 | 805827600 | 847159300
  - 同じ表の列：Product, Biomass, Fossil fuels, Metal ores, Non-metallic minera…

## g0071（1 列）
- 見出し：Year_Month
- 例1 値：Jul-17 | Jul-16 | Apr-17 | Jun-17 | Dec-16
  - 同じ表の列：Card_type, Line, Trip

## g0072（1 列）
- 見出し：Card_type
- 例1 値：School Student | Free Travel | Concession | School Student | Sgl Trip Ferry Adult
  - 同じ表の列：Year_Month, Line, Trip

## g0073（1 列）
- 見出し：Line
- 例1 値：F6 Mosman Bay | F1 Manly | F6 Mosman Bay | F4 Darling Harbour | F6 Mosman Bay
  - 同じ表の列：Year_Month, Card_type, Trip

## g0074（1 列）
- 見出し：Trip
- 例1 値：1049 | 110594 | 56 | 578 | 23518
  - 同じ表の列：Year_Month, Card_type, Line

## g0075（1 列）
- 見出し：OBJECTID
- 例1 値：132 | 63 | 47 | 151 | 157
  - 同じ表の列：population, adii, ability, access, affordability

## g0076（1 列）
- 見出し：population
- 例1 値：7981 | 130 | 32399 | 2103 | 14126
  - 同じ表の列：OBJECTID, adii, ability, access, affordability

## g0077（1 列）
- 見出し：adii
- 例1 値：75.08 | 69.37 | 71.94 | 69.31 | 72.98
  - 同じ表の列：OBJECTID, population, ability, access, affordability

## g0078（1 列）
- 見出し：ability
- 例1 値：59.57155759 | 57.40453406 | 57.5221269 | 62.30107506 | 56.76138745
  - 同じ表の列：OBJECTID, population, adii, access, affordability

## g0079（1 列）
- 見出し：access
- 例1 値：71.48391668 | 77.1043073 | 73.8941338 | 72.21972016 | 75.78754599
  - 同じ表の列：OBJECTID, population, adii, ability, affordability

## g0080（1 列）
- 見出し：affordability
- 例1 値：91.56970722 | 91.95508654 | 89.57560502 | 89.83991236 | 92.24108993
  - 同じ表の列：OBJECTID, population, adii, ability, access

## g0081（1 列）
- 見出し：Six_Cities22
- 例1 値：Total GMA* | ** Remainder GMA LGAs of Dungog, Single… | Total Sydney | Eastern Harbour City | *GMA Transport for NSW Greater Metropol…
  - 同じ表の列：Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0082（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2021
- 例1 値：1,196,330.31600 | 535,028.74800 | 3,962,219.53902 | 778,407.35730 | 2,509,766.42130
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0083（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2022
- 例1 値：778,362.84380 | 300,092.53510 | 1,181,105.90700 | 542,331.13300 | 154,303.68380
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0084（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2023
- 例1 値：4,216,387.84952 | 212,785.51820 | 318,318.66920 | 807,299.11440 | 583,815.02590
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0085（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2024
- 例1 値：600,290.44310 | 1,230,867.76500 | 3,459,793.67990 | 165,808.21300 | 44,707.77680
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0086（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2025
- 例1 値：205,582.51470 | 167,351.77280 | 2,731,099.81500 | 44,294.62793 | 4,302,708.07383
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0087（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2026
- 例1 値：2,762,437.30270 | 168,306.25900 | 1,235,608.02200 | 328,030.50980 | 44,528.80621
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0088（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2027
- 例1 値：210,939.51460 | 629,413.12760 | 836,008.01070 | 169,894.80070 | 3,564,685.09902
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0089（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2028
- 例1 値：171,698.56400 | 45,219.51648 | 214,454.49020 | 4,463,243.09378 | 337,276.71730
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

## g0090（1 列）
- 見出し：Emp_Wkf_POPD_15+yrs_2029
- 例1 値：963,977.38350 | 173,273.05480 | 847,353.49270 | 651,945.91510 | 341,466.13440
  - 同じ表の列：Six_Cities22, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…, Emp_Wkf_POPD_15+yrs…

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
```
