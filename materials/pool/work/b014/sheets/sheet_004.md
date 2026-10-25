# ラベル用シート 004 / 008

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_004.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0361（1 列）
- 見出し：mapref
- 例1 値：33 H4 | 34 A7 | 33 A5 | 48 B3 | 34 H2
  - 同じ表の列：location, between_, school, hours, lat

## g0362（1 列）
- 見出し：hours
- 例1 値：8:15am-9:00am / 3:15pm-4:00pm | 8:15am-9:00am / 3:15pm-4:00pm | 8:25am-9:10am / 3:20pm-4:05pm | 8:25am-9:10am / 3:15pm-4:00pm | 8:15am-9:00am / 3:15pm-4:00pm
  - 同じ表の列：location, between_, school, mapref, lat

## g0363（1 列）
- 見出し：01. RecordID
- 例1 値：766 | 814 | 192 | 412 | 894
  - 同じ表の列：EventNumber, 04. Water Year, 09. a_ Geographic I…, EA, Sub(Multisub_Listed), Child(multiChild_li…, 10. SDL_Code, WRPA_CODE

## g0364（1 列）
- 見出し：EventNumber
- 例1 値：211 | 747 | 61 | 579 | 716
  - 同じ表の列：01. RecordID, 04. Water Year, 09. a_ Geographic I…, EA, Sub(Multisub_Listed), Child(multiChild_li…, 10. SDL_Code, WRPA_CODE

## g0365（1 列）
- 見出し：04. Water Year
- 例1 値：2014-15 | 2015-16 | 2014-15 | 2015-16 | 2018-19
  - 同じ表の列：01. RecordID, EventNumber, 09. a_ Geographic I…, EA, Sub(Multisub_Listed), Child(multiChild_li…, 10. SDL_Code, WRPA_CODE

## g0366（1 列）
- 見出し：09. a_ Geographic Identifier
- 例1 値：Macquarie Marshes | Lower Moonie River and fringing wetlands | Berri Evaporation Basin | Goulburn River | Dumaresq-Macintyre River channel
  - 同じ表の列：01. RecordID, EventNumber, 04. Water Year, EA, Sub(Multisub_Listed), Child(multiChild_li…, 10. SDL_Code, WRPA_CODE

## g0367（1 列）
- 見出し：EA
- 例1 値：Lower Murray wetlands (Victorian Murray) | Lower Murray Wetlands (SA Murray) | Booligal Wetlands | Weir Pool Manipulation | Murrumbidgee
  - 同じ表の列：01. RecordID, EventNumber, 04. Water Year, 09. a_ Geographic I…, Sub(Multisub_Listed), Child(multiChild_li…, 10. SDL_Code, WRPA_CODE

## g0368（1 列）
- 見出し：Sub(Multisub_Listed)
- 例1 値：Edward-Wakool system | NA | Border Rivers Water Management Area | Wimmera wetlands | Edward-Wakool system
  - 同じ表の列：01. RecordID, EventNumber, 04. Water Year, 09. a_ Geographic I…, EA, Child(multiChild_li…, 10. SDL_Code, WRPA_CODE

## g0369（1 列）
- 見出し：Child(multiChild_listed)
- 例1 値：Yarrein Creek | NA | Poyner | Cardross Lakes | NA
  - 同じ表の列：01. RecordID, EventNumber, 04. Water Year, 09. a_ Geographic I…, EA, Sub(Multisub_Listed), 10. SDL_Code, WRPA_CODE

## g0370（1 列）
- 見出し：10. SDL_Code
- 例1 値：SS9 | SS15 | SS14 | SS14 | SS20
  - 同じ表の列：01. RecordID, EventNumber, 04. Water Year, 09. a_ Geographic I…, EA, Sub(Multisub_Listed), Child(multiChild_li…, WRPA_CODE

## g0371（1 列）
- 見出し：WRPA_CODE
- 例1 値：SW10 | SW4 | SW6 | SW6 | SW4
  - 同じ表の列：01. RecordID, EventNumber, 04. Water Year, 09. a_ Geographic I…, EA, Sub(Multisub_Listed), Child(multiChild_li…, 10. SDL_Code

## g0372（1 列）
- 見出し：JointWater
- 例1 値：Single Event | Single Event | Single Event | Single Event | Single Event
  - 同じ表の列：01. RecordID, EventNumber, 04. Water Year, 09. a_ Geographic I…, EA, Sub(Multisub_Listed), Child(multiChild_li…, 10. SDL_Code

## g0373（1 列）
- 見出し：Funding agency
- 例1 値：DPC | DPC | DPC | DPC
  - 同じ表の列：Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0374（1 列）
- 見出し：Program title
- 例1 値：Year of Outback Tourism Events Program | Exporter Market Engagement Program | Honouring our Veterans Grants Program | Honouring our Veterans Grants Program
  - 同じ表の列：Funding agency, Sub-program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0375（1 列）
- 見出し：Sub-program title
- 例1 値：Community Grants | NA | Capital Works Grants
  - 同じ表の列：Funding agency, Program title, Purpose, Category1, Category2, Category3, Client group1, Client group2

## g0376（1 列）
- 見出し：Purpose
- 例1 値：The program delivers significant commem… | In 2019 and 2020, grants have been avai… | The program delivers major and minor ca… | The program will provide access to mark…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Category1, Category2, Category3, Client group1, Client group2

## g0377（1 列）
- 見出し：Category1
- 例1 値：Business and industry | Community support | Community support | Community support
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category2, Category3, Client group1, Client group2

## g0378（1 列）
- 見出し：Category2
- 例1 値：Employment and jobs | Recreation, sport and arts
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category3, Client group1, Client group2

## g0379（1 列）
- 見出し：Category3
- 例1 値：Business and industry
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0380（1 列）
- 見出し：Client group1
- 例1 値：Exporters | All Queenslanders | Community groups | All Queenslanders
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group2

## g0381（1 列）
- 見出し：Client group2
- 例1 値：Non-government organisations | Businesses | Businesses | Non-government organisations
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

## g0382（1 列）
- 見出し：Client group3
- 例1 値：Creative or performing arts | Veterans and family | Veterans and family
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Category3, Client group1

## g0383（1 列）
- 見出し：Date Received
- 例1 値：02-Jul-25 | 07-Aug-25 | 05-Jun-26 | 05-Dec-25 | 17-Dec-25
  - 同じ表の列：Value, Reasons for accepti…

## g0384（1 列）
- 見出し：Value
- 例1 値：250.00 | 300.00 | 1,100.00 | 6,000.00 | 550.00
  - 同じ表の列：Date Received, Reasons for accepti…

## g0385（1 列）
- 見出し：Reasons for accepting gift (what is the benefit to the Queen
- 例1 値：To continue to strengthen and build rel… | To continue to strengthen and build rel… | To continue to strengthen and build rel… | To continue to strengthen and build rel… | To continue to strengthen and build rel…
  - 同じ表の列：Date Received, Value

## g0386（1 列）
- 見出し：itemid
- 例1 値：478236 | 478286 | 478162 | 478287 | 478280
  - 同じ表の列：title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0387（1 列）
- 見出し：title
- 例1 値：Detail survey maps [Sydney] [cartograph… | Detail survey maps [Sydney] [cartograph… | Detail survey maps [Sydney] [cartograph… | Detail survey maps [Sydney] [cartograph… | Detail survey maps [Sydney] [cartograph…
  - 同じ表の列：itemid, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0388（1 列）
- 見出し：caption
- 例1 値：Danks' Block No.170; Lessey's Block No.… | People's Palace Block No.178; Hotel Syd… | Union Band Block No.119, 10.5.21 (b&w) | People's Palace Block No.178; Hotel Syd… | Cowan's Block No.136; Clifford Love Blo…
  - 同じ表の列：itemid, title, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0389（1 列）
- 見出し：creator
- 例1 値：Fire and Accident Underwriters Associat… | Fire and Accident Underwriters Associat… | Fire and Accident Underwriters Associat… | Fire and Accident Underwriters Associat… | Fire and Accident Underwriters Associat…
  - 同じ表の列：itemid, title, caption, albumnumber, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0390（1 列）
- 見出し：albumnumber
- 例1 値：862883 | 862883 | 862883 | 862883 | 862883
  - 同じ表の列：itemid, title, caption, creator, dateofwork, collectionitemlink, digitalitemlink, digitalordernumber

## g0391（1 列）
- 見出し：dateofwork
- 例1 値：1919-1940 | 1919-1940 | 1919-1940 | 1919-1940 | 1919-1940
  - 同じ表の列：itemid, title, caption, creator, albumnumber, collectionitemlink, digitalitemlink, digitalordernumber

## g0392（1 列）
- 見出し：collectionitemlink
- 例1 値：http://library.sl.nsw.gov.au/record=b22… | http://library.sl.nsw.gov.au/record=b22… | http://library.sl.nsw.gov.au/record=b22… | http://library.sl.nsw.gov.au/record=b22… | http://library.sl.nsw.gov.au/record=b22…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, digitalitemlink, digitalordernumber

## g0393（1 列）
- 見出し：digitalitemlink
- 例1 値：http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?… | http://library.sl.nsw.gov.au/search~S2?…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalordernumber

## g0394（1 列）
- 見出し：digitalordernumber
- 例1 値：a1358126 | a1358109 | a1358031 | a1358118 | a1358132
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink

## g0395（1 列）
- 見出し：thumbnaillink
- 例1 値：http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1… | http://acms.sl.nsw.gov.au/_DAMt/image/1…
  - 同じ表の列：itemid, title, caption, creator, albumnumber, dateofwork, collectionitemlink, digitalitemlink

## g0396（1 列）
- 見出し：Business Category
- 例1 値：Dance Class/Club | Dance Class/Club | Calisthenics,Dance Class/Club | Dance Class/Club | Bowling Club,Dance Class/Club,Recreatio…
  - 同じ表の列：Suburb, State, LGA, Region

## g0397（1 列）
- 見出し：LGA
- 例1 値：Greater Geelong | Boroondara | Kingston , Bayside | Kingston , Glen Eira | Greater Dandenong
  - 同じ表の列：Suburb, State, Business Category, Region

## g0398（1 列）
- 見出し：Region
- 例1 値：Southern Metro | Barwon S/W | Southern Metro | Eastern Metro | Gippsland
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0399（1 列）
- 見出し：X Co-Ordinate
- 例1 値：142.7843152 | 142.1618306 | 145.6496427 | 141.6083424 | 144.9901303
  - 同じ表の列：Suburb, Y Co-Ordinate

## g0400（1 列）
- 見出し：Y Co-Ordinate
- 例1 値：-38.23718195 | -37.68284279 | -36.55583827 | -37.799486 | -38.38083013
  - 同じ表の列：Suburb, X Co-Ordinate

## g0401（1 列）
- 見出し：Location
- 例1 値：market place - shire office & council c… | saleyards | public lighting | botanical gardens pump | pump
  - 同じ表の列：id, suburb, kwh, ton_co2, geometry

## g0402（1 列）
- 見出し：kwh
- 例1 値：53797 | 10601 | 24877 | 11423 | 11985
  - 同じ表の列：id, Location, suburb, ton_co2, geometry

## g0403（1 列）
- 見出し：ton_co2
- 例1 値：27 | 12 | 43 | 59 | 22
  - 同じ表の列：id, Location, suburb, kwh, geometry

## g0404（1 列）
- 見出し：geometry
- 例1 値：POINT (142.036051508404 -37.74174776265… | POINT (142.020751293775 -37.74072526537… | POINT (142.024331289094 -37.74206940545… | POINT (142.020088464141 -37.73264268024… | POINT (142.291660547255 -37.87328047174…
  - 同じ表の列：id, Location, suburb, kwh, ton_co2

## g0405（1 列）
- 見出し：link
- 例1 値：https://www.facebook.com/pages/grangebu… | http://mycricket.cricket.com.au/common/… | http://www.foxsportspulse.com/club_info… | http://www.speedwayaustralia.net.au/com… | http://mycricket.cricket.com.au/common/…
  - 同じ表の列：type

## g0406（1 列）
- 見出し：wheelchair
- 例1 値：no | yes | no | no | no
  - 同じ表の列：lat, lon, operator

## g0407（1 列）
- 見出し：operator
- 例1 値：southern grampians shire council | private | private | southern grampians shire council | southern grampians shire council
  - 同じ表の列：lat, lon, wheelchair

## g0408（1 列）
- 見出し：Heading
- 例1 値：A GALLANT FLIER. | THE AUSTRALIAN FLYIKG CORPS. How the Me… | THE AUSTRALIANS AIRCRAFT ADVENTURES. FI… | A LONG FLIGHT. CAIRO TO KARACHI. LONDON… | SOLDIERS BUILDING APPEAL (Continued).
  - 同じ表の列：Category, Title, Page, Date, TrovePageUrl, Illustrated, WordCount, Relevance

## g0409（1 列）
- 見出し：Category
- 例1 値：Article | Article | Article | Article | Article
  - 同じ表の列：Heading, Title, Page, Date, TrovePageUrl, Illustrated, WordCount, Relevance

## g0410（1 列）
- 見出し：Title
- 例1 値：The Register (Adelaide, SA : 1901 - 192… | The Advertiser (Adelaide, SA : 1889 - 1… | Observer (Adelaide, SA : 1905 - 1931) | The Register (Adelaide, SA : 1901 - 192… | Observer (Adelaide, SA : 1905 - 1931)
  - 同じ表の列：Heading, Category, Page, Date, TrovePageUrl, Illustrated, WordCount, Relevance

## g0411（1 列）
- 見出し：TrovePageUrl
- 例1 値：https://trove.nla.gov.au/ndp/del/page/4… | https://trove.nla.gov.au/ndp/del/page/1… | https://trove.nla.gov.au/ndp/del/page/9… | https://trove.nla.gov.au/ndp/del/page/4… | https://trove.nla.gov.au/ndp/del/page/4…
  - 同じ表の列：Heading, Category, Title, Page, Date, Illustrated, WordCount, Relevance

## g0412（1 列）
- 見出し：Illustrated
- 例1 値：N | N | N | N | N
  - 同じ表の列：Heading, Category, Title, Page, Date, TrovePageUrl, WordCount, Relevance

## g0413（1 列）
- 見出し：WordCount
- 例1 値：95 | 697 | 169 | 1632 | 1518
  - 同じ表の列：Heading, Category, Title, Page, Date, TrovePageUrl, Illustrated, Relevance

## g0414（1 列）
- 見出し：Relevance
- 例1 値：very relevant | very relevant | very relevant | very relevant | very relevant
  - 同じ表の列：Heading, Category, Title, Page, Date, TrovePageUrl, Illustrated, WordCount

## g0415（1 列）
- 見出し：title
- 例1 値：Wondering | Sister of pal o&apos; mine | The canaries | The Viceroy tea waltz | Valencia
  - 同じ表の列：id, creator, innopac, link, coverage_place, coverage_region, fileBrowse, original_format

## g0416（1 列）
- 見出し：creator
- 例1 値：Fewster, Jack | Linger, Carl, 1810-1862 | Knox, W. R. (William Robert) | Schrader, Otto W. | Fewster, Jack
  - 同じ表の列：id, title, innopac, link, coverage_place, coverage_region, fileBrowse, original_format

## g0417（1 列）
- 見出し：innopac
- 例1 値：http://www.catalog.slsa.sa.gov.au/recor… | http://www.catalog.slsa.sa.gov.au/recor… | http://www.catalog.slsa.sa.gov.au/recor… | http://www.catalog.slsa.sa.gov.au/recor… | http://www.catalog.slsa.sa.gov.au/recor…
  - 同じ表の列：id, title, creator, link, coverage_place, coverage_region, fileBrowse, original_format

## g0418（1 列）
- 見出し：link
- 例1 値：http://www.samemory.sa.gov.au/site/page… | http://www.samemory.sa.gov.au/site/page… | http://www.samemory.sa.gov.au/site/page… | http://www.samemory.sa.gov.au/site/page… | http://www.samemory.sa.gov.au/site/page…
  - 同じ表の列：id, title, creator, innopac, coverage_place, coverage_region, fileBrowse, original_format

## g0419（1 列）
- 見出し：coverage_place
- 例1 値：Dardanelles | Dardanelles | Dardanelles | Dardanelles
  - 同じ表の列：id, title, creator, innopac, link, coverage_region, fileBrowse, original_format

## g0420（1 列）
- 見出し：coverage_region
- 例1 値：Riverland and Murraylands | Adelaide city | Adelaide city | Adelaide city | Riverland and Murraylands
  - 同じ表の列：id, title, creator, innopac, link, coverage_place, fileBrowse, original_format

## g0421（1 列）
- 見出し：fileBrowse
- 例1 値：<link>http://images.slsa.sa.gov.au/same… | <link>http://images.slsa.sa.gov.au/same… | <link>http://images.slsa.sa.gov.au/same… | <link>http://images.slsa.sa.gov.au/same… | <link>http://images.slsa.sa.gov.au/same…
  - 同じ表の列：id, title, creator, innopac, link, coverage_place, coverage_region, original_format

## g0422（1 列）
- 見出し：original_format
- 例1 値：Sheet music | Sheet music | Sheet music | Sheet music | Sheet music
  - 同じ表の列：id, title, creator, innopac, link, coverage_place, coverage_region, fileBrowse

## g0423（1 列）
- 見出し：publisher
- 例1 値：J. von Bertouch | S. Marshall, | Jack Fewster Ltd., | Hussey &amp; Gillingham | G.A. Payne?
  - 同じ表の列：id, title, creator, innopac, link, coverage_place, coverage_region, fileBrowse

## g0424（1 列）
- 見出し：Applications unfinished at year end
- 例1 値：UNIVERSITIES - within 30 day timeframe | STATE - overdue | STATE - not overdue | UNIVERSITIES - not overdue | STATE - within 30 day timeframe
  - 同じ表の列：2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0425（1 列）
- 見出し：2024-25
- 例1 値：1608 | 17 | 3 | 1193 | 1
  - 同じ表の列：Applications unfini…, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0426（1 列）
- 見出し：2023-24
- 例1 値：915 | 873 | 3 | 2 | 26
  - 同じ表の列：Applications unfini…, 2024-25, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0427（1 列）
- 見出し：2022-23
- 例1 値：845 | 780 | 41 | 1 | 4
  - 同じ表の列：Applications unfini…, 2024-25, 2023-24, 2021-22, 2020-21, 2019-20, 2018-19, 2017-18

## g0428（1 列）
- 見出し：2021-22
- 例1 値：7 | 589 | 31 | 2843 | 273
  - 同じ表の列：Applications unfini…, 2024-25, 2023-24, 2022-23, 2020-21, 2019-20, 2018-19, 2017-18

## g0429（1 列）
- 見出し：2020-21
- 例1 値：34 | 2523 | 691 | 7 | 1
  - 同じ表の列：Applications unfini…, 2024-25, 2023-24, 2022-23, 2021-22, 2019-20, 2018-19, 2017-18

## g0430（1 列）
- 見出し：2019-20
- 例1 値：2306 | 12 | 145 | 38 | 666
  - 同じ表の列：Applications unfini…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2018-19, 2017-18

## g0431（1 列）
- 見出し：2018-19
- 例1 値：624 | 7 | 2 | 2391 | 38
  - 同じ表の列：Applications unfini…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2017-18

## g0432（1 列）
- 見出し：2017-18
- 例1 値：22 | 2082 | 3 | 8 | 129
  - 同じ表の列：Applications unfini…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g0433（1 列）
- 見出し：2016-17
- 例1 値：2 | 7 | 680 | 67 | 94
  - 同じ表の列：Applications unfini…, 2024-25, 2023-24, 2022-23, 2021-22, 2020-21, 2019-20, 2018-19

## g0434（1 列）
- 見出し：No. of access applications made by Members of Parliament
- 例1 値：1242 | 1816 | 461 | 1782 | 2459
  - 同じ表の列：Year

## g0435（2 列）
- 見出し：RECORD #(BIBLIO)
- 例1 値：b18624376 | b19643652 | b19245245 | b19595074 | b17709593
  - 同じ表の列：TITLE, AUTHOR, ADDITIONAL AUTHOR
- 例2 値：b37242295 | b19172424 | b37099632 | b33855432 | b27395984
  - 同じ表の列：MAT TYPE

## g0436（1 列）
- 見出し：TITLE
- 例1 値：Carnarvon [cartographic material] | Map showing the gold mining leases in t… | Townsite of Chinokup, Kojonup District … | Manjedal [cartographic material] | Australia Occidentale ed isola di Van D…
  - 同じ表の列：RECORD #(BIBLIO), AUTHOR, ADDITIONAL AUTHOR

## g0437（1 列）
- 見出し：AUTHOR
- 例1 値：Western Australia. Department of Lands … | Western Australia. Department of Lands … | Western Australia. Department of Lands … | Western Australia. Department of Lands … | Western Australia. Department of Lands …
  - 同じ表の列：RECORD #(BIBLIO), TITLE, ADDITIONAL AUTHOR

## g0438（1 列）
- 見出し：ADDITIONAL AUTHOR
- 例1 値：Edward Stanford Ltd. | Western Australia. Parliament. Minutes … | H.E.C. Robinson Pty. Ltd.^"Gledden & Ma… | Patterson A. W. | Western Australian Company.
  - 同じ表の列：RECORD #(BIBLIO), TITLE, AUTHOR

## g0439（1 列）
- 見出し：MAT TYPE
- 例1 値：Ephemera | Ephemera | Poster | Poster | Poster
  - 同じ表の列：RECORD #(BIBLIO)

## g0440（1 列）
- 見出し：Bib record number
- 例1 値：b24361318 | b24410901 | b24481944 | b2440536x | b24482602
  - 同じ表の列：Call number, Date, Subject: People, Subject: topical, Collection

## g0441（1 列）
- 見出し：Call number
- 例1 値：BA1611/760, 761, 1434 | BA1611/1143 | BA1611/365-371, 628-633, 1023-1025 | BA1611/948, 949, 953 | BA1611/950, 951, 952
  - 同じ表の列：Bib record number, Date, Subject: People, Subject: topical, Collection

## g0442（1 列）
- 見出し：Date
- 例1 値：1990? | 1991-1993. | 1982-1987 | 1993 | 1988
  - 同じ表の列：Bib record number, Call number, Subject: People, Subject: topical, Collection

## g0443（1 列）
- 見出し：Subject: People
- 例1 値：Stirling, James, | Pericles, Leon; Pericles, Leon, | Haynes, George; Haynes, George, | Stirling, James, | Durack, Elizabeth,
  - 同じ表の列：Bib record number, Call number, Date, Subject: topical, Collection

## g0444（1 列）
- 見出し：Subject: topical
- 例1 値：Hospitals; Hospitals; Online image. | Artists; Painters; Artists' studios; At… | Streetscapes; Online image. | Artists; Online image. | Diamond mines and mining; Online image.
  - 同じ表の列：Bib record number, Call number, Date, Subject: People, Collection

## g0445（1 列）
- 見出し：Collection
- 例1 値：Richard Woldendorp collection of photog… | Richard Woldendorp collection of photog… | Richard Woldendorp collection of photog… | Richard Woldendorp collection of photog… | Richard Woldendorp collection of photog…
  - 同じ表の列：Bib record number, Call number, Date, Subject: People, Subject: topical

## g0446（1 列）
- 見出し：Zone
- 例1 値：E | A | D | B | C
  - 同じ表の列：FZ_MinArea

## g0447（1 列）
- 見出し：FZ_MinArea
- 例1 値：80HA | 40HA | 100HA | 80HA | 40HA
  - 同じ表の列：Zone

## g0448（1 列）
- 見出し：No.
- 例1 値：19 | 12 | 25 | 19 | 13
  - 同じ表の列：Feature, Hotlink, X, Y

## g0449（1 列）
- 見出し：Feature
- 例1 値：Trenching | Longwood Railway Platform | The track.. | Enter the swamp | A fine set of views
  - 同じ表の列：No., Hotlink, X, Y

## g0450（1 列）
- 見出し：Hotlink
- 例1 値：https://www.strathbogie.vic.gov.au/imag… | https://www.strathbogie.vic.gov.au/imag… | https://www.strathbogie.vic.gov.au/imag… | https://www.strathbogie.vic.gov.au/imag… | https://www.strathbogie.vic.gov.au/imag…
  - 同じ表の列：No., Feature, X, Y

## g0451（1 列）
- 見出し：X
- 例1 値：145.50088134397444 | 144.9905281891836 | 145.12134999675567 | 144.9772302755026 | 145.7248459289873
  - 同じ表の列：No., Feature, Hotlink, Y

## g0452（1 列）
- 見出し：Y
- 例1 値：-36.70773333854668 | -36.63792073679112 | -36.86462775079218 | -36.76913908093041 | -36.825708022331746
  - 同じ表の列：No., Feature, Hotlink, X

## g0453（1 列）
- 見出し：Financial Year
- 例1 値：2015-16 | 2014-15 | 2014-15 | 2016-17 | 2016-17
  - 同じ表の列：Type of flow, Country, Sector, ExpenseInThousands

## g0454（2 列）
- 見出し：Type of flow
- 例1 値：ODA | ODA | ODA | ODA | ODA
  - 同じ表の列：Financial Year, Country, Sector, ExpenseInThousands
- 例2 値：OOF | ODA | ODA | ODA | ODA
  - 同じ表の列：Financial Year, Country, Sector, Expense $'000

## g0455（1 列）
- 見出し：Country
- 例1 値：Samoa | Zambia | Laos | Vanuatu | Ghana
  - 同じ表の列：Financial Year, Type of flow, Sector, ExpenseInThousands

## g0456（2 列）
- 見出し：Sector
- 例1 値：31181 | 31163 | 31182 | 31161 | 31193
  - 同じ表の列：Financial Year, Type of flow, Country, ExpenseInThousands
- 例2 値：31320 | 31181 | 31182 | 23050 | 31140
  - 同じ表の列：Financial Year, Type of flow, Country, Expense $'000

## g0457（1 列）
- 見出し：ExpenseInThousands
- 例1 値：0.2 | 3601.3 | 109.6 | 120.6 | 41.9
  - 同じ表の列：Financial Year, Type of flow, Country, Sector

## g0458（1 列）
- 見出し：Financial Year
- 例1 値：2014/15 | 2014/15 | 2014/15 | 2014/15 | 2014/15
  - 同じ表の列：Type of flow, Country, Sector, Expense $'000

## g0459（1 列）
- 見出し：Country
- 例1 値：Fiji | Vanuatu | Global Unspecified | Tonga | Asia Unspecified
  - 同じ表の列：Financial Year, Type of flow, Sector, Expense $'000

## g0460（1 列）
- 見出し：Expense $'000
- 例1 値：85 | 22.5 | 43 | 3.7 | 48.6
  - 同じ表の列：Financial Year, Type of flow, Country, Sector

## g0461（1 列）
- 見出し：spot_shd
- 例1 値：2.69 m | 3.48 m | 3.32 m | 4.21 m | 5.79 m
  - 同じ表の列：id, lat, lon, spot_ahd

## g0462（1 列）
- 見出し：spot_ahd
- 例1 値：67.07 m | 66.85 m | 67.12 m | 66.73 m | 67.3 m
  - 同じ表の列：id, lat, lon, spot_shd

## g0463（1 列）
- 見出し：Quarter
- 例1 値：Dec 2022 Qtr | Dec 2024 Qtr | Dec 2023 Qtr | Dec 2023 Qtr | Jun 2023 Qtr
  - 同じ表の列：Landfill Site, Construction and De…, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Commercial and Indu…, Green Waste Diverte…

## g0464（1 列）
- 見出し：Landfill Site
- 例1 値：Bluewater Transfer Station | Magnetic Island Transfer Station | Stuart Landfill | Magnetic Island Transfer Station | Bluewater Transfer Station
  - 同じ表の列：Quarter, Construction and De…, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Commercial and Indu…, Green Waste Diverte…

## g0465（1 列）
- 見出し：Construction and Demolition Diverted (Tonnes)
- 例1 値：0 | 8988.99 | 52.85 | 10.149999999999999 | 9788.47
  - 同じ表の列：Quarter, Landfill Site, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Commercial and Indu…, Green Waste Diverte…

## g0466（1 列）
- 見出し：Construction and Demolition Landfilled (Tonnes)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Quarter, Landfill Site, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Commercial and Indu…, Green Waste Diverte…

## g0467（1 列）
- 見出し：Construction and Demolition Total (Tonnes)
- 例1 値：31524.680000000004 | 49354.76645000001 | 22570.725000000013 | 110.4 | 9830.330000000002
  - 同じ表の列：Quarter, Landfill Site, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Commercial and Indu…, Green Waste Diverte…

## g0468（1 列）
- 見出し：Commercial and Industrial Diverted (Tonnes)
- 例1 値：221.22 | 56.370000000000005 | 491.4 | 0.2 | 172.25
  - 同じ表の列：Quarter, Landfill Site, Construction and De…, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Green Waste Diverte…

## g0469（1 列）
- 見出し：Commercial and Industrial Landfilled (Tonnes)
- 例1 値：0 | 20842.024999999994 | 15344.830132 | 0 | 0
  - 同じ表の列：Quarter, Landfill Site, Construction and De…, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Green Waste Diverte…

## g0470（1 列）
- 見出し：Commercial and Industrial Total (Tonnes)
- 例1 値：79.99499999999999 | 315.75 | 124.23999999999998 | 0.02 | 123.23999999999997
  - 同じ表の列：Quarter, Landfill Site, Construction and De…, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Green Waste Diverte…

## g0471（1 列）
- 見出し：Green Waste Diverted (Tonnes)
- 例1 値：207.55 | 3122.7 | 186.2999999999999 | 2792.1499999999996 | 44.8
  - 同じ表の列：Quarter, Landfill Site, Construction and De…, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Commercial and Indu…

## g0472（1 列）
- 見出し：Green Waste Landfilled (Tonnes)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Quarter, Landfill Site, Construction and De…, Construction and De…, Construction and De…, Commercial and Indu…, Commercial and Indu…, Commercial and Indu…

## g0473（1 列）
- 見出し：Animal Type
- 例1 値：Cat | Cat | Cat | Cat | Cat
  - 同じ表の列：Breed, Gender, Desexed, Suburb, Electoral Division, Registration Year

## g0474（1 列）
- 見出し：Breed
- 例1 値：Maine Coon Cross | Domestic Short Hair | Unknown - Cat | Domestic Short Hair | Ragdoll
  - 同じ表の列：Animal Type, Gender, Desexed, Suburb, Electoral Division, Registration Year

## g0475（1 列）
- 見出し：Gender
- 例1 値：Male | Female | Male | Female | Male
  - 同じ表の列：Animal Type, Breed, Desexed, Suburb, Electoral Division, Registration Year

## g0476（1 列）
- 見出し：Desexed
- 例1 値：Yes | No | Yes | Yes | Yes
  - 同じ表の列：Animal Type, Breed, Gender, Suburb, Electoral Division, Registration Year

## g0477（1 列）
- 見出し：Electoral Division
- 例1 値：Division 10 | Division 1 | Division 1 | Division 1 | Division 1
  - 同じ表の列：Animal Type, Breed, Gender, Desexed, Suburb, Registration Year

## g0478（1 列）
- 見出し：Registration Year
- 例1 値：2026 | 2026 | 2026 | 2026 | 2026
  - 同じ表の列：Animal Type, Breed, Gender, Desexed, Suburb, Electoral Division

## g0479（1 列）
- 見出し：Date
- 例1 値：2021-06-01 00:00:00 | 2023-07-01 00:00:00 | 2025-11-01 00:00:00 | 2020-06-01 00:00:00 | 2023-03-01 00:00:00
  - 同じ表の列：Adopted, Reclaimed

## g0480（1 列）
- 見出し：Adopted
- 例1 値：102 | 61 | 68 | 66 | 116
  - 同じ表の列：Date, Reclaimed

## 答えの雛形

```
g0361	
g0362	
g0363	
g0364	
g0365	
g0366	
g0367	
g0368	
g0369	
g0370	
g0371	
g0372	
g0373	
g0374	
g0375	
g0376	
g0377	
g0378	
g0379	
g0380	
g0381	
g0382	
g0383	
g0384	
g0385	
g0386	
g0387	
g0388	
g0389	
g0390	
g0391	
g0392	
g0393	
g0394	
g0395	
g0396	
g0397	
g0398	
g0399	
g0400	
g0401	
g0402	
g0403	
g0404	
g0405	
g0406	
g0407	
g0408	
g0409	
g0410	
g0411	
g0412	
g0413	
g0414	
g0415	
g0416	
g0417	
g0418	
g0419	
g0420	
g0421	
g0422	
g0423	
g0424	
g0425	
g0426	
g0427	
g0428	
g0429	
g0430	
g0431	
g0432	
g0433	
g0434	
g0435	
g0436	
g0437	
g0438	
g0439	
g0440	
g0441	
g0442	
g0443	
g0444	
g0445	
g0446	
g0447	
g0448	
g0449	
g0450	
g0451	
g0452	
g0453	
g0454	
g0455	
g0456	
g0457	
g0458	
g0459	
g0460	
g0461	
g0462	
g0463	
g0464	
g0465	
g0466	
g0467	
g0468	
g0469	
g0470	
g0471	
g0472	
g0473	
g0474	
g0475	
g0476	
g0477	
g0478	
g0479	
g0480	
```
