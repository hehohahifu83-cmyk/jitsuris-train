# ラベル用シート 007 / 011

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_007.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0721（1 列）
- 見出し：alphatree
- 例1 値：R | B | P | P | P
  - 同じ表の列：date1, house, str_type, suburb, pcode, species, height, dbh

## g0722（1 列）
- 見出し：species
- 例1 値：Lophostemon confertus | Melaleuca linariifolia | Lophostemon confertus | Lophostemon confertus | Allocasuarina torulosa
  - 同じ表の列：date1, house, str_type, suburb, pcode, alphatree, height, dbh

## g0723（1 列）
- 見出し：height
- 例1 値：5-10m | 10-15m | 2-5m | 0-2m | 5-10m
  - 同じ表の列：date1, house, str_type, suburb, pcode, alphatree, species, dbh

## g0724（1 列）
- 見出し：dbh
- 例1 値：100 - 250mm | 0 - 100mm | 500 - 1000mm | 0 - 100mm | 1000mm+
  - 同じ表の列：date1, house, str_type, suburb, pcode, alphatree, species, height

## g0725（1 列）
- 見出し：treearea
- 例1 値：Area 3 | Area 3 | Area 3 | Area 3 | Area 3
  - 同じ表の列：date1, house, str_type, suburb, pcode, alphatree, species, height

## g0726（1 列）
- 見出し：pole_id
- 例1 値：71 | 729 | 565 | 796 | 482
  - 同じ表の列：inspected, inspdate, house_no, suburb, located_in, restict_no, signtype, arrow_dir

## g0727（1 列）
- 見出し：inspected
- 例1 値：Unaudited | Unverified | Unverified | Unaudited | Unaudited
  - 同じ表の列：pole_id, inspdate, house_no, suburb, located_in, restict_no, signtype, arrow_dir

## g0728（1 列）
- 見出し：inspdate
- 例1 値：19/11/2010 | 23/06/2006 | 16/01/2009 | 6/03/2010 | 18/12/2007
  - 同じ表の列：pole_id, inspected, house_no, suburb, located_in, restict_no, signtype, arrow_dir

## g0729（1 列）
- 見出し：house_no
- 例1 値：0 | 271 | 115 | 42 | 0
  - 同じ表の列：pole_id, inspected, inspdate, suburb, located_in, restict_no, signtype, arrow_dir

## g0730（1 列）
- 見出し：located_in
- 例1 値：Jackson Court Shopping Centre | Sandra Street | George Street | Morang Avenue | Berkeley Street
  - 同じ表の列：pole_id, inspected, inspdate, house_no, suburb, restict_no, signtype, arrow_dir

## g0731（1 列）
- 見出し：restict_no
- 例1 値：Restriction 1 | Restriction 2 | Restriction 1 | Restriction 1 | Restriction 1
  - 同じ表の列：pole_id, inspected, inspdate, house_no, suburb, located_in, signtype, arrow_dir

## g0732（1 列）
- 見出し：signtype
- 例1 値：Clearway | No Stopping | Clearway | No Stopping | No Stopping
  - 同じ表の列：pole_id, inspected, inspdate, house_no, suburb, located_in, restict_no, arrow_dir

## g0733（1 列）
- 見出し：arrow_dir
- 例1 値：Left | Left | Right | Both | Both
  - 同じ表の列：pole_id, inspected, inspdate, house_no, suburb, located_in, restict_no, signtype

## g0734（1 列）
- 見出し：exceptions
- 例1 値：Permit Holders | Emergency Vehicles | Resident Permit Area | Permit Holders | Permit Holders
  - 同じ表の列：pole_id, inspected, inspdate, house_no, suburb, located_in, restict_no, signtype

## g0735（1 列）
- 見出し：INSP_DATE
- 例1 値：13/05/2013 | 8/05/2013 | 12/02/2010 | 10/03/2010 | 15/03/2010
  - 同じ表の列：RESERVE, SUBURB, MAPREF, TYPE, STYLE, assetid, lat, long

## g0736（1 列）
- 見出し：RESERVE
- 例1 値：DONVALE RESERVE | JOCELYN COURT RESERVE | WINBROOK COURT RESERVE | MAGGS STREET RESERVE | DIRLTON COURT RESERVE
  - 同じ表の列：INSP_DATE, SUBURB, MAPREF, TYPE, STYLE, assetid, lat, long

## g0737（1 列）
- 見出し：MAPREF
- 例1 値：47F3 | 35D10 | 48F5 | 32H9 | 48B3
  - 同じ表の列：INSP_DATE, RESERVE, SUBURB, TYPE, STYLE, assetid, lat, long

## g0738（1 列）
- 見出し：TYPE
- 例1 値：Park Bench | Bin | Park Bench | Taps | Sculpture
  - 同じ表の列：INSP_DATE, RESERVE, SUBURB, MAPREF, STYLE, assetid, lat, long

## g0739（1 列）
- 見出し：STYLE
- 例1 値：Timber slat & cast iron frame | Steel Pedestal with circular | Timber sleeper bench | Timber slat & cast iron frame | Timber slat & cast iron frame
  - 同じ表の列：INSP_DATE, RESERVE, SUBURB, MAPREF, TYPE, assetid, lat, long

## g0740（1 列）
- 見出し：assetid
- 例1 値：PF1346 | PF356 | PF1791 | PF1922 | PF2266
  - 同じ表の列：INSP_DATE, RESERVE, SUBURB, MAPREF, TYPE, STYLE, lat, long

## g0741（1 列）
- 見出し：Dy
- 例1 値：12 | 5 | 15 | 4 | 7
  - 同じ表の列：Mn, Year, 424202A, 424201A, 424002_, 424001_, 423204_, 423201A

## g0742（1 列）
- 見出し：Mn
- 例1 値：11 | 9 | 4 | 3 | 2
  - 同じ表の列：Dy, Year, 424202A, 424201A, 424002_, 424001_, 423204_, 423201A

## g0743（1 列）
- 見出し：424202A
- 例1 値：0 | 49 | 8212 | 0 | 0
  - 同じ表の列：Dy, Mn, Year, 424201A, 424002_, 424001_, 423204_, 423201A

## g0744（1 列）
- 見出し：424201A
- 例1 値：0 | Site | 33767 | 40 | 5
  - 同じ表の列：Dy, Mn, Year, 424202A, 424002_, 424001_, 423204_, 423201A

## g0745（1 列）
- 見出し：424002_
- 例1 値：1 | 601 | 1 | 1 | 198
  - 同じ表の列：Dy, Mn, Year, 424202A, 424201A, 424001_, 423204_, 423201A

## g0746（1 列）
- 見出し：424001_
- 例1 値：9 | 23964 | 15 | 586 | 994
  - 同じ表の列：Dy, Mn, Year, 424202A, 424201A, 424002_, 423204_, 423201A

## g0747（1 列）
- 見出し：423204_
- 例1 値：1 | 213 | 8BROOMG | 0 | 0
  - 同じ表の列：Dy, Mn, Year, 424202A, 424201A, 424002_, 424001_, 423201A

## g0748（1 列）
- 見出し：423201A
- 例1 値："412016 Wallamundry Creek@Offtake Islan… | 16 | 0 | 0 | "419012 Namoi@Boggabri"
  - 同じ表の列：Dy, Mn, Year, 424202A, 424201A, 424002_, 424001_, 423204_

## g0749（1 列）
- 見出し：423203A
- 例1 値：35 | 0 | 0 | 0 | 0
  - 同じ表の列：Dy, Mn, Year, 424202A, 424201A, 424002_, 424001_, 423204_

## g0750（1 列）
- 見出し：Water Year
- 例1 値：2011 | 1999 | 2003 | 2013 | 2000
  - 同じ表の列：ID, value, Catchment, inflow

## g0751（1 列）
- 見出し：value
- 例1 値：0.120470361 | 0.741200847 | 0.599051633 | 0.288718088 | 0.161220242
  - 同じ表の列：Water Year, ID, Catchment, inflow

## g0752（1 列）
- 見出し：Catchment
- 例1 値：Namoi | Namoi | Overall North | Murrumbidgee | Warrego
  - 同じ表の列：Water Year, ID, value, inflow

## g0753（1 列）
- 見出し：inflow
- 例1 値：3170664.688 | 1.38E+07 | 1074258.388 | 281129.8013 | 743698.2467
  - 同じ表の列：Water Year, ID, value, Catchment

## g0754（1 列）
- 見出し：Column1
- 例1 値：1/05/1912 | 21/03/1913 | 5/04/1912 | 27/12/1912 | 20/01/1913
  - 同じ表の列：Barwon-Darling, Border Rivers, Campaspe, Condamine-Balonne, Eastern Mt Lofty Ra…, Goulburn-Broken, Gwydir, Lachlan

## g0755（1 列）
- 見出し：Barwon-Darling
- 例1 値：785.3630261 | 887.5525065 | 169.9822435 | 190.871403 | 261.409707
  - 同じ表の列：Column1, Border Rivers, Campaspe, Condamine-Balonne, Eastern Mt Lofty Ra…, Goulburn-Broken, Gwydir, Lachlan

## g0756（1 列）
- 見出し：Border Rivers
- 例1 値：729.7694479 | 450.5900445 | 435.5967912 | 527.1139251 | 40621.56139
  - 同じ表の列：Column1, Barwon-Darling, Campaspe, Condamine-Balonne, Eastern Mt Lofty Ra…, Goulburn-Broken, Gwydir, Lachlan

## g0757（1 列）
- 見出し：Campaspe
- 例1 値：141.5041069 | 842.2877084 | 344.2628924 | 1125.473632 | 169.5402502
  - 同じ表の列：Column1, Barwon-Darling, Border Rivers, Condamine-Balonne, Eastern Mt Lofty Ra…, Goulburn-Broken, Gwydir, Lachlan

## g0758（1 列）
- 見出し：Condamine-Balonne
- 例1 値：454.1696216 | 1672.182573 | 508.6927605 | 506.4000224 | 481.1387754
  - 同じ表の列：Column1, Barwon-Darling, Border Rivers, Campaspe, Eastern Mt Lofty Ra…, Goulburn-Broken, Gwydir, Lachlan

## g0759（1 列）
- 見出し：Eastern Mt Lofty Ranges
- 例1 値：333.8950907 | 169.5897669 | 317.7365603 | 308.5470313 | 147.0872886
  - 同じ表の列：Column1, Barwon-Darling, Border Rivers, Campaspe, Condamine-Balonne, Goulburn-Broken, Gwydir, Lachlan

## g0760（1 列）
- 見出し：Goulburn-Broken
- 例1 値：10664.83877 | 3956.801614 | 62182.9128 | 2125.992254 | 10962.21333
  - 同じ表の列：Column1, Barwon-Darling, Border Rivers, Campaspe, Condamine-Balonne, Eastern Mt Lofty Ra…, Gwydir, Lachlan

## g0761（1 列）
- 見出し：Gwydir
- 例1 値：768.8264736 | 567.8519597 | 222.5130516 | 682.4945442 | 603.861785
  - 同じ表の列：Column1, Barwon-Darling, Border Rivers, Campaspe, Condamine-Balonne, Eastern Mt Lofty Ra…, Goulburn-Broken, Lachlan

## g0762（1 列）
- 見出し：Lachlan
- 例1 値：1348.564611 | 1899.857598 | 2269.885658 | 1948.61338 | 1578.734488
  - 同じ表の列：Column1, Barwon-Darling, Border Rivers, Campaspe, Condamine-Balonne, Eastern Mt Lofty Ra…, Goulburn-Broken, Gwydir

## g0763（1 列）
- 見出し：Loddon
- 例1 値：410.5182352 | 257.1367964 | 955.8987594 | 443.4813688 | 579.7879788
  - 同じ表の列：Column1, Barwon-Darling, Border Rivers, Campaspe, Condamine-Balonne, Eastern Mt Lofty Ra…, Goulburn-Broken, Gwydir

## g0764（1 列）
- 見出し：Number of students
- 例1 値：HSC Award (Aboriginal students) | NSW government school HSC completions b… | Students who completed one or more HSC … | Students who completed one or more HSC … | HSC Award (All students)
  - 同じ表の列：2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023

## g0765（1 列）
- 見出し：Processor/manufacturer
- 例1 値：Cook-chill food short shelf-life proces… | Oils and fats processing | Seafood processing - mollusc processing | Egg processing | Meat processing Abattoir/Boning Room
  - 同じ表の列：Total businesses, Businesses inspected, Businesses requirin…, Written warnings is…, Improvement notices…, Prohibition orders …, Expiations issued, Prosecutions

## g0766（1 列）
- 見出し：Total businesses
- 例1 値：11 | 6 | 6 | 11 | 154
  - 同じ表の列：Processor/manufactu…, Businesses inspected, Businesses requirin…, Written warnings is…, Improvement notices…, Prohibition orders …, Expiations issued, Prosecutions

## g0767（1 列）
- 見出し：Businesses inspected
- 例1 値：2 | 280 | 37 | 0 | 2
  - 同じ表の列：Processor/manufactu…, Total businesses, Businesses requirin…, Written warnings is…, Improvement notices…, Prohibition orders …, Expiations issued, Prosecutions

## g0768（1 列）
- 見出し：Businesses requiring enforcement action
- 例1 値：0 | 24 | 0 | 2 | 0
  - 同じ表の列：Processor/manufactu…, Total businesses, Businesses inspected, Written warnings is…, Improvement notices…, Prohibition orders …, Expiations issued, Prosecutions

## g0769（1 列）
- 見出し：Written warnings issued
- 例1 値：24 | 0 | 1 | 1 | 0
  - 同じ表の列：Processor/manufactu…, Total businesses, Businesses inspected, Businesses requirin…, Improvement notices…, Prohibition orders …, Expiations issued, Prosecutions

## g0770（1 列）
- 見出し：Improvement notices issued
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Processor/manufactu…, Total businesses, Businesses inspected, Businesses requirin…, Written warnings is…, Prohibition orders …, Expiations issued, Prosecutions

## g0771（1 列）
- 見出し：Prohibition orders issued
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Processor/manufactu…, Total businesses, Businesses inspected, Businesses requirin…, Written warnings is…, Improvement notices…, Expiations issued, Prosecutions

## g0772（1 列）
- 見出し：Expiations issued
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Processor/manufactu…, Total businesses, Businesses inspected, Businesses requirin…, Written warnings is…, Improvement notices…, Prohibition orders …, Prosecutions

## g0773（1 列）
- 見出し：Prosecutions
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Processor/manufactu…, Total businesses, Businesses inspected, Businesses requirin…, Written warnings is…, Improvement notices…, Prohibition orders …, Expiations issued

## g0774（1 列）
- 見出し：Agency
- 例1 値：Australian Institute of Health and Welf… | Department of Education and Training | Department of Veterans' Affairs | Department of Health | Department of Social Services
  - 同じ表の列：Frequency

## g0775（1 列）
- 見出し：Frequency
- 例1 値：Various | Various | Various | Various | Various
  - 同じ表の列：Agency

## g0776（1 列）
- 見出し：E315
- 例1 値：F | F | F | F | F
  - 同じ表の列：E550, E089, E310, ATSI, B461, E358D

## g0777（1 列）
- 見出し：E550
- 例1 値：2007 | 2007 | 2007 | 2007 | 2007
  - 同じ表の列：E315, E089, E310, ATSI, B461, E358D

## g0778（1 列）
- 見出し：E089
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：E315, E550, E310, ATSI, B461, E358D

## g0779（1 列）
- 見出し：E310
- 例1 値：10 | 10 | 10 | 10 | 10
  - 同じ表の列：E315, E550, E089, ATSI, B461, E358D

## g0780（1 列）
- 見出し：ATSI
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：E315, E550, E089, E310, B461, E358D

## g0781（1 列）
- 見出し：B461
- 例1 値：1 | 8 | 5 | 8 | 8
  - 同じ表の列：E315, E550, E089, E310, ATSI, E358D

## g0782（1 列）
- 見出し：E358D
- 例1 値：1 | 1 | 2 | 1 | 2
  - 同じ表の列：E315, E550, E089, E310, ATSI, B461

## g0783（1 列）
- 見出し：LGA
- 例1 値：Corangamite | West Wimmerahire | Yarra Ranges | Whitehorse , Manningham | Glen Eira
  - 同じ表の列：Suburb, State, Business Category, Region

## g0784（1 列）
- 見出し：Region
- 例1 値：Eastern Metropolitan Region | Eastern Metro | Eastern Metro | Southern Metro | Barwon S/W
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0785（1 列）
- 見出し：Workplace injury claims
- 例1 値：Seriously injured workers* | Number of notifiable incidents (WHS Act… | * number of claimants assessed during t… | Number of provisional improvement, impr… | Significant injuries (where lost time e…
  - 同じ表の列：2021-22, 2020-21, 2019-20, 2018-19

## g0786（1 列）
- 見出し：2021-22
- 例1 値：$848,127 | $301,441 | 0 | 9 | 0
  - 同じ表の列：Workplace injury cl…, 2020-21, 2019-20, 2018-19

## g0787（1 列）
- 見出し：2020-21
- 例1 値：0 | 0 | 2020-21 | 7.27 | $250,475
  - 同じ表の列：Workplace injury cl…, 2021-22, 2019-20, 2018-19

## g0788（2 列）
- 見出し：2019-20
- 例1 値：0 | 2019-20 | 20 | 2019-20 | 0
  - 同じ表の列：Workplace injury cl…, 2021-22, 2020-21, 2018-19
- 例2 値：91 | 0 | 2019-20 | 5409 | 4
  - 同じ表の列：Performance indicat…, 2020-21, 2018-19, 2017-2018, 2016-2017, 2015-2016

## g0789（1 列）
- 見出し：2018-19
- 例1 値：0 | 1 | $718,918 | 8.5 | 2018-19
  - 同じ表の列：Workplace injury cl…, 2021-22, 2020-21, 2019-20

## g0790（1 列）
- 見出し：WKT_Geometry
- 例1 値：POINT (142.023587159786 -37.74091353559… | POINT (142.021478446001 -37.73997168234… | POINT (142.021072460022 -37.74030287130… | POINT (142.022178872574 -37.73961150765… | POINT (142.024061513292 -37.74148914168…
  - 同じ表の列：lat, long, ref

## g0791（1 列）
- 見出し：species
- 例1 値：lagunaria patersonii | prunus cerasifera | melaleuca sp. | prunus sp. | quercus robur
  - 同じ表の列：ref, common, height, crown, maturity, location, locality, lat

## g0792（1 列）
- 見出し：common
- 例1 値：unkown gum | unkown gum | manchurian pear | black cherry plum | hawthorn
  - 同じ表の列：ref, species, height, crown, maturity, location, locality, lat

## g0793（2 列）
- 見出し：height
- 例1 値：5 | 7 | 2 | 22 | 3
  - 同じ表の列：ref, species, common, crown, maturity, location, locality, lat
- 例2 値：12 | 14 | 3 | 14 | 8
  - 同じ表の列：lat, lon, species, common, dbh, crown, crown_min, crown_max

## g0794（2 列）
- 見出し：crown
- 例1 値：10 | 5 | 8 | 4 | 0
  - 同じ表の列：ref, species, common, height, maturity, location, locality, lat
- 例2 値：12 | 9 | 11 | 5 | 7
  - 同じ表の列：lat, lon, species, common, dbh, crown_min, crown_max, height

## g0795（1 列）
- 見出し：maturity
- 例1 値：mature | mature | mature | mature | mature
  - 同じ表の列：ref, species, common, height, crown, location, locality, lat

## g0796（1 列）
- 見出し：location
- 例1 値：king street | andrews street | andrews street | king street | clifford street
  - 同じ表の列：ref, species, common, height, crown, maturity, locality, lat

## g0797（1 列）
- 見出し：locality
- 例1 値：hamilton city | hamilton city | hamilton city | hamilton city | hamilton city
  - 同じ表の列：ref, species, common, height, crown, maturity, location, lat

## g0798（1 列）
- 見出し：Performance indicators
- 例1 値：Staff | Public library One Card members | Complaints - category of complaints by … | Contractors | Number of instances
  - 同じ表の列：2020-21, 2019-20, 2018-19, 2017-2018, 2016-2017, 2015-2016

## g0799（1 列）
- 見出し：2020-21
- 例1 値：0 | 2020-21 | 180 | 10 | 6
  - 同じ表の列：Performance indicat…, 2019-20, 2018-19, 2017-2018, 2016-2017, 2015-2016

## g0800（1 列）
- 見出し：2018-19
- 例1 値：0 | 0 | 62 | 29749.00 | 0
  - 同じ表の列：Performance indicat…, 2020-21, 2019-20, 2017-2018, 2016-2017, 2015-2016

## g0801（1 列）
- 見出し：2017-2018
- 例1 値：0 | 3 | 0 | 628 | 2017-2018
  - 同じ表の列：Performance indicat…, 2020-21, 2019-20, 2018-19, 2016-2017, 2015-2016

## g0802（1 列）
- 見出し：2016-2017
- 例1 値：0 | 0 | 696 | 593949 | 0
  - 同じ表の列：Performance indicat…, 2020-21, 2019-20, 2018-19, 2017-2018, 2015-2016

## g0803（1 列）
- 見出し：2015-2016
- 例1 値：2015-2016 | 2015-2016 | 2015-2016 | 0 | 0
  - 同じ表の列：Performance indicat…, 2020-21, 2019-20, 2018-19, 2017-2018, 2016-2017

## g0804（1 列）
- 見出し：RECORD #
- 例1 値：b21126392 | b20418140 | b20669380 | b29202358 | b20577461
  - 同じ表の列：XML, TITLE, Dates/publication d…, Series/Collection, IMAGE

## g0805（1 列）
- 見出し：XML
- 例1 値：http://www.catalog.slsa.sa.gov.au/xreco… | http://www.catalog.slsa.sa.gov.au/xreco… | http://www.catalog.slsa.sa.gov.au/xreco… | http://www.catalog.slsa.sa.gov.au/xreco… | http://www.catalog.slsa.sa.gov.au/xreco…
  - 同じ表の列：RECORD #, TITLE, Dates/publication d…, Series/Collection, IMAGE

## g0806（1 列）
- 見出し：TITLE
- 例1 値：Railway Bridge, Murray Bridge | Torrens Gorge Aqueduct | Currie Street, Adelaide | Adelaide Arcade | Bridge workers, Murray Bridge
  - 同じ表の列：RECORD #, XML, Dates/publication d…, Series/Collection, IMAGE

## g0807（1 列）
- 見出し：Dates/publication details
- 例1 値：[approximately 1880] | [approximately 1870] | [approximately 1880] | [approximately 1870] | [approximately 1872]
  - 同じ表の列：RECORD #, XML, TITLE, Series/Collection, IMAGE

## g0808（1 列）
- 見出し：Series/Collection
- 例1 値：Woodforde Collection;Sweet Collection | Acre 736 Collection | Album Collection | Album Collection | Beulah Park Collection
  - 同じ表の列：RECORD #, XML, TITLE, Dates/publication d…, IMAGE

## g0809（1 列）
- 見出し：IMAGE
- 例1 値：http://collections.slsa.sa.gov.au/mpcim… | http://collections.slsa.sa.gov.au/mpcim… | http://collections.slsa.sa.gov.au/mpcim… | http://collections.slsa.sa.gov.au/mpcim… | http://collections.slsa.sa.gov.au/mpcim…
  - 同じ表の列：RECORD #, XML, TITLE, Dates/publication d…, Series/Collection

## g0810（2 列）
- 見出し：2020-21
- 例1 値：1133 | 11 | 1 | 4 | 2972
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2019-20, 2018-19, 2017-18, 2016-17
- 例2 値：2246 | 12 | 4063 | 231 | 106
  - 同じ表の列：Length of processin…, 2024-25, 2023-24, 2022-23, 2021-22, 2019-20, 2018-19, 2017-18

## g0811（2 列）
- 見出し：2019-20
- 例1 値：3597 | 7 | 983 | 24 | 235
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2018-19, 2017-18, 2016-17
- 例2 値：87 | 2498 | 9 | 10 | 13
  - 同じ表の列：Length of processin…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2018-19, 2017-18

## g0812（2 列）
- 見出し：2018-19
- 例1 値：689 | 86 | 296 | 0 | 3450
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2017-18, 2016-17
- 例2 値：2209 | 162 | 4 | 7 | 3
  - 同じ表の列：Length of processin…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2017-18

## g0813（1 列）
- 見出し：2015-16
- 例1 値：1671 | 108 | 1 | 6 | 4337
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0814（1 列）
- 見出し：Sector, application category
- 例1 値：UNIVERSITIES - Non-personal | LOCAL - Personal | LOCAL - Non-personal | UNIVERSITIES - Personal | STATE - Non-personal
  - 同じ表の列：2024-25 - partial r…, 2024-25 - release r…, 2023-24 - partial r…, 2023-24 - release r…, 2022-23 - partial r…, 2022-23 - release r…, 2022-23 - transferr…, 2022-23 - withdrawn…

## g0815（1 列）
- 見出し：2024-25 - partial release
- 例1 値：164 | 97 | 37 | 805 | 16
  - 同じ表の列：Sector, application…, 2024-25 - release r…, 2023-24 - partial r…, 2023-24 - release r…, 2022-23 - partial r…, 2022-23 - release r…, 2022-23 - transferr…, 2022-23 - withdrawn…

## g0816（1 列）
- 見出し：2024-25 - release refused
- 例1 値：2 | 458 | 0 | 1182 | 26
  - 同じ表の列：Sector, application…, 2024-25 - partial r…, 2023-24 - partial r…, 2023-24 - release r…, 2022-23 - partial r…, 2022-23 - release r…, 2022-23 - transferr…, 2022-23 - withdrawn…

## g0817（1 列）
- 見出し：2023-24 - partial release
- 例1 値：30 | 4605 | 24 | 945 | 80
  - 同じ表の列：Sector, application…, 2024-25 - partial r…, 2024-25 - release r…, 2023-24 - release r…, 2022-23 - partial r…, 2022-23 - release r…, 2022-23 - transferr…, 2022-23 - withdrawn…

## g0818（1 列）
- 見出し：2023-24 - release refused
- 例1 値：773 | 550 | 2 | 1 | 26
  - 同じ表の列：Sector, application…, 2024-25 - partial r…, 2024-25 - release r…, 2023-24 - partial r…, 2022-23 - partial r…, 2022-23 - release r…, 2022-23 - transferr…, 2022-23 - withdrawn…

## g0819（1 列）
- 見出し：2022-23 - partial release
- 例1 値：135 | 3 | 61 | 13 | 729
  - 同じ表の列：Sector, application…, 2024-25 - partial r…, 2024-25 - release r…, 2023-24 - partial r…, 2023-24 - release r…, 2022-23 - release r…, 2022-23 - transferr…, 2022-23 - withdrawn…

## g0820（1 列）
- 見出し：2022-23 - release refused
- 例1 値：35 | 1 | 0 | 814 | 15
  - 同じ表の列：Sector, application…, 2024-25 - partial r…, 2024-25 - release r…, 2023-24 - partial r…, 2023-24 - release r…, 2022-23 - partial r…, 2022-23 - transferr…, 2022-23 - withdrawn…

## g0821（1 列）
- 見出し：2022-23 - transferred
- 例1 値：107 | 0 | 0 | 0 | 3
  - 同じ表の列：Sector, application…, 2024-25 - partial r…, 2024-25 - release r…, 2023-24 - partial r…, 2023-24 - release r…, 2022-23 - partial r…, 2022-23 - release r…, 2022-23 - withdrawn…

## g0822（1 列）
- 見出し：2022-23 - withdrawn/closed
- 例1 値：0 | 19 | 892 | 283 | 0
  - 同じ表の列：Sector, application…, 2024-25 - partial r…, 2024-25 - release r…, 2023-24 - partial r…, 2023-24 - release r…, 2022-23 - partial r…, 2022-23 - release r…, 2022-23 - transferr…

## g0823（1 列）
- 見出し：2021-22 - partial release
- 例1 値：382 | 53 | 3268 | 16 | 9
  - 同じ表の列：Sector, application…, 2024-25 - partial r…, 2024-25 - release r…, 2023-24 - partial r…, 2023-24 - release r…, 2022-23 - partial r…, 2022-23 - release r…, 2022-23 - transferr…

## g0824（1 列）
- 見出し：Length of processing time
- 例1 値：UNIVERSITIES - more than 30 days | LOCAL - outside of timeframe | STATE - more than 30 days | UNIVERSITIES - within timeframe (not ex… | STATE - within timeframe (extended)
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0825（3 列）
- 見出し：itemid
- 例1 値：902821 | 480022 | 887141 | 480033 | 480032
  - 同じ表の列：title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber
- 例2 値：403562 | 412747 | 403703 | 412747 | 412904
  - 同じ表の列：title, creator, collectionitemlink, digitalitemlink, albumnumber, transcriptlink, dateofwork, digitalordernumber

## g0826（1 列）
- 見出し：title
- 例1 値：[Bradley's manuscript charts] [cartogra… | [Bradley's manuscript charts] [cartogra… | [Bradley's manuscript charts] [cartogra… | [Bradley's manuscript charts] [cartogra… | Chart of the track of the Waaksaamheidt…
  - 同じ表の列：itemid, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0827（1 列）
- 見出し：caption
- 例1 値：Chart 1. Southern Hemisphere | Chart 9. Islands discover'd in the Waaz… | The Western or Atlantic Ocean [cartogra… | Chart 14. An Eye Sketch of the road on … | Chart 12. A Chart of the discoveries ma…
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0828（1 列）
- 見出し：creator
- 例1 値：Shortland, Thomas George. | Fowkes, Francis. | Bradley, William, 1758-1833. | Bradley, William, 1758-1833. | Bradley, William, 1758-1833.
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0829（3 列）
- 見出し：albumnumber
- 例1 値：889870 | 862353 | 862353 | 862353 | 913724
  - 同じ表の列：itemid, title, caption, creator, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber
- 例2 値：823394 | 823591 | 823394 | 823394 | 823591
  - 同じ表の列：itemid, title, creator, collectionitemlink, digitalitemlink, transcriptlink, dateofwork, digitalordernumber

## g0830（1 列）
- 見出し：dateofwork
- 例1 値：[1792?] | [1792?] | 1789?. | [1792?] | [1789?]
  - 同じ表の列：itemid, title, caption, creator, albumnumber, collectionitemlink, digitalitemlink, digitalordernumber

## g0831（3 列）
- 見出し：collectionitemlink
- 例1 値：http://library.sl.nsw.gov.au/record=b20… | http://library.sl.nsw.gov.au/record=b20… | http://library.sl.nsw.gov.au/record=b20… | http://library.sl.nsw.gov.au/record=b27… | http://library.sl.nsw.gov.au/record=b20…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, digitalitemlink, digitalordernumber
- 例2 値：http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta… | http://acms.sl.nsw.gov.au/item/itemDeta…
  - 同じ表の列：itemid, title, creator, digitalitemlink, albumnumber, transcriptlink, dateofwork, digitalordernumber

## g0832（3 列）
- 見出し：digitalitemlink
- 例1 値：http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalordernumber
- 例2 値：http://acms.sl.nsw.gov.au/album/albumVi… | http://acms.sl.nsw.gov.au/album/albumVi… | http://acms.sl.nsw.gov.au/album/albumVi… | http://acms.sl.nsw.gov.au/album/albumVi… | http://acms.sl.nsw.gov.au/album/albumVi…
  - 同じ表の列：itemid, title, creator, collectionitemlink, albumnumber, transcriptlink, dateofwork, digitalordernumber

## g0833（3 列）
- 見出し：digitalordernumber
- 例1 値：a127078 | a160004 | a160009 | a160010 | a1528984
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink
- 例2 値：a138190 | a1085063 | a1085145 | a1085128 | a138509
  - 同じ表の列：itemid, title, creator, collectionitemlink, digitalitemlink, albumnumber, transcriptlink, dateofwork

## g0834（3 列）
- 見出し：thumbnaillink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/2… | http://acms.sl.nsw.gov.au/_DAMt/image/1…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink
- 例2 値：http://acms.sl.nsw.gov.au/_DAMt/image/2… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1…
  - 同じ表の列：itemid, title, creator, collectionitemlink, digitalitemlink, albumnumber, transcriptlink, dateofwork

## g0835（1 列）
- 見出し：title
- 例1 値：Collection 01: Arthur Bowes-Smyth, illu… | Margaret Blackburn - Letters (14) recei… | Collection 02: William Bradley - Journa… | Margaret Blackburn - Letters (14) recei… | Collection 02: William Bradley - Journa…
  - 同じ表の列：itemid, creator, collectionitemlink, digitalitemlink, albumnumber, transcriptlink, dateofwork, digitalordernumber

## g0836（1 列）
- 見出し：creator
- 例1 値：Bradley, William, ca. 1757-1833 | Bradley, William, ca. 1757-1833 | Blackburn, David, 1753-1795 Blackburn, … | Bradley, William, ca. 1757-1833 | Bowes Smyth, Arthur, 1750-1790
  - 同じ表の列：itemid, title, collectionitemlink, digitalitemlink, albumnumber, transcriptlink, dateofwork, digitalordernumber

## g0837（1 列）
- 見出し：transcriptlink
- 例1 値：http://acms.sl.nsw.gov.au/_transcript/2… | http://acms.sl.nsw.gov.au/_transcript/2… | http://acms.sl.nsw.gov.au/_transcript/2… | http://acms.sl.nsw.gov.au/_transcript/2… | http://acms.sl.nsw.gov.au/_transcript/2…
  - 同じ表の列：itemid, title, creator, collectionitemlink, digitalitemlink, albumnumber, dateofwork, digitalordernumber

## g0838（1 列）
- 見出し：dateofwork
- 例1 値：1787-1789 | 1787-1792 | 1787-1789 | 1787-1791 | 1787-1789
  - 同じ表の列：itemid, title, creator, collectionitemlink, digitalitemlink, albumnumber, transcriptlink, digitalordernumber

## g0839（1 列）
- 見出し：title
- 例1 値：Australian Gas Light Company Sydney pla… | Australian Gas Light Company Sydney pla… | Australian Gas Light Company Sydney pla… | Australian Gas Light Company Sydney pla… | Australian Gas Light Company Sydney pla…
  - 同じ表の列：itemid, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0840（1 列）
- 見出し：caption
- 例1 値：Sheet 7. Centring on Kent and Market St… | Sheet 8. Centring on Kent and Bathurst … | Sheet 2. Centring on Darling Point | Sheet 11. Centring on Cleveland and Wat… | Sheet 14. Centring on King and Clarence…
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## 答えの雛形

```
g0721	
g0722	
g0723	
g0724	
g0725	
g0726	
g0727	
g0728	
g0729	
g0730	
g0731	
g0732	
g0733	
g0734	
g0735	
g0736	
g0737	
g0738	
g0739	
g0740	
g0741	
g0742	
g0743	
g0744	
g0745	
g0746	
g0747	
g0748	
g0749	
g0750	
g0751	
g0752	
g0753	
g0754	
g0755	
g0756	
g0757	
g0758	
g0759	
g0760	
g0761	
g0762	
g0763	
g0764	
g0765	
g0766	
g0767	
g0768	
g0769	
g0770	
g0771	
g0772	
g0773	
g0774	
g0775	
g0776	
g0777	
g0778	
g0779	
g0780	
g0781	
g0782	
g0783	
g0784	
g0785	
g0786	
g0787	
g0788	
g0789	
g0790	
g0791	
g0792	
g0793	
g0794	
g0795	
g0796	
g0797	
g0798	
g0799	
g0800	
g0801	
g0802	
g0803	
g0804	
g0805	
g0806	
g0807	
g0808	
g0809	
g0810	
g0811	
g0812	
g0813	
g0814	
g0815	
g0816	
g0817	
g0818	
g0819	
g0820	
g0821	
g0822	
g0823	
g0824	
g0825	
g0826	
g0827	
g0828	
g0829	
g0830	
g0831	
g0832	
g0833	
g0834	
g0835	
g0836	
g0837	
g0838	
g0839	
g0840	
```
