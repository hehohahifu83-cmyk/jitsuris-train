# ラベル用シート 002 / 003

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Suburb
- 例1 値：Collingwood | Melbourne | Bendigo | Thomastown | Brunswick East
  - 同じ表の列：State, Business Category, LGA, Region

## g0122（2 列）
- 見出し：State
- 例1 値：VIC | VIC | VIC | VIC | VIC
  - 同じ表の列：Suburb, Business Category, LGA, Region
- 例2 値：NSW | NSW | NSW | NSW | NSW
  - 同じ表の列：id, type, city

## g0123（1 列）
- 見出し：Business Category
- 例1 値：Martial Arts,State body | Martial Arts,State body | Martial Arts | Martial Arts | Martial Arts
  - 同じ表の列：Suburb, State, LGA, Region

## g0124（1 列）
- 見出し：LGA
- 例1 値：Monash (C) | Nillumbik (S) | Wyndham (C); Melton (S); Brimbank (C) | Stonnington (C); Boroondara (C) | Whittlesea (C)
  - 同じ表の列：Suburb, State, Business Category, Region

## g0125（1 列）
- 見出し：Region
- 例1 値：Barwon S/W | North and West Metropolitan Region | Eastern Metropolitan Region | North and West Metropolitan Region | North and West Metropolitan Region
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0126（1 列）
- 見出し：ref
- 例1 値：BR12087 | BR8073 | BR5081 | BR4089 | BR1073
  - 同じ表の列：culvert type

## g0127（1 列）
- 見出し：culvert type
- 例1 値：Major Culvert | Major Culvert | Major Culvert | Major Culvert | Major Culvert
  - 同じ表の列：ref

## g0128（1 列）
- 見出し：Feature
- 例1 値：Guard rails, wrought iron Please see re… | H20 Stint Map, comprising stainless ste… | The Coronation Lamp, lit 1902, a painte… | A Pair of Sir William Armstrong rifled … | Anuradha Petel (Gate) Giffard St Entran…
  - 同じ表の列：feature_type, Artist, CulturalSignificance, Dimensions, Location

## g0129（1 列）
- 見出し：feature_type
- 例1 値：Public Art | Public Art | Public Art | Public Art | Public Art
  - 同じ表の列：Feature, Artist, CulturalSignificance, Dimensions, Location

## g0130（1 列）
- 見出し：Artist
- 例1 値：McKinnon, Elizabeth | Taylor, Simon | Unknown | Unknown | Unknown
  - 同じ表の列：Feature, feature_type, CulturalSignificance, Dimensions, Location

## g0131（1 列）
- 見出し：CulturalSignificance
- 例1 値：Site specific commissioned work with ar… | Historic & social significance , Clark … | Historic significance | see 316.1 | Historic significance. Commemorates the…
  - 同じ表の列：Feature, feature_type, Artist, Dimensions, Location

## g0132（1 列）
- 見出し：Dimensions
- 例1 値：00 x 00 | Height 206cm | 400cm height approx | Central Gates 550 x 380 cm Side Posts 3… | 00 x 00
  - 同じ表の列：Feature, feature_type, Artist, CulturalSignificance, Location

## g0133（1 列）
- 見出し：Location
- 例1 値：Grounds | Grounds | Roundabout | Park | Grounds
  - 同じ表の列：Feature, feature_type, Artist, CulturalSignificance, Dimensions

## g0134（1 列）
- 見出し：DOC_DATE
- 例1 値：24 Jan 1929 | 14 Apr 1927 | 3 Jan 1923 | 1^May 22 1922 | 1 Jan 1920
  - 同じ表の列：YEAR, REMARKS

## g0135（3 列）
- 見出し：YEAR
- 例1 値：1920 | 1920 | 1920 | 1927 | 1921
  - 同じ表の列：DOC_DATE, REMARKS
- 例2 値：1855 | 1854 | 1857 | 1856 | 1854
  - 同じ表の列：TRIAL_PLACE, OFFENSE, TRIAL_DATE, PP_ID, VERDICT

## g0136（1 列）
- 見出し：REMARKS
- 例1 値：with family | with family | with family | with family | with family
  - 同じ表の列：DOC_DATE, YEAR

## g0137（1 列）
- 見出し：TRIAL_PLACE
- 例1 値：Hobart town | Hobart town | Oatlands | Hobart town | Hobart town
  - 同じ表の列：OFFENSE, TRIAL_DATE, PP_ID, YEAR, VERDICT

## g0138（1 列）
- 見出し：OFFENSE
- 例1 値：Attempt to commit sodomy | Attempt to commit sodomy | Assault | Illegally pawning | Larceny
  - 同じ表の列：TRIAL_PLACE, TRIAL_DATE, PP_ID, YEAR, VERDICT

## g0139（1 列）
- 見出し：TRIAL_DATE
- 例1 値：8 Dec 1854 | 3 Jan 1855 | 4 Nov 1856 | 1 Nov 1855 | 28 Apr 1855
  - 同じ表の列：TRIAL_PLACE, OFFENSE, PP_ID, YEAR, VERDICT

## g0140（1 列）
- 見出し：PP_ID
- 例1 値：99731 | 95767 | 99939 | 99656 | 97648
  - 同じ表の列：TRIAL_PLACE, OFFENSE, TRIAL_DATE, YEAR, VERDICT

## g0141（1 列）
- 見出し：VERDICT
- 例1 値：Not guilty | Summarily | Guilty | Guilty | Guilty of assault
  - 同じ表の列：TRIAL_PLACE, OFFENSE, TRIAL_DATE, PP_ID, YEAR

## g0142（1 列）
- 見出し：AuthorisationReference
- 例1 値：00376J | 0111504C | 03134J | 01084J | 02009E
  - 同じ表の列：PostalTownSuburb, PostalPostalCode, PostalStateDescript…, PostalCountryDescri…, StatutoryClassDesc, AuthorisationTypeDe…, AuthorisationStatus…, AllocationClassDesc

## g0143（1 列）
- 見出し：PostalTownSuburb
- 例1 値：NERANG | BLACKALL | MOUNT NATHAN | BLACKALL | CANUNGRA
  - 同じ表の列：AuthorisationRefere…, PostalPostalCode, PostalStateDescript…, PostalCountryDescri…, StatutoryClassDesc, AuthorisationTypeDe…, AuthorisationStatus…, AllocationClassDesc

## g0144（1 列）
- 見出し：PostalPostalCode
- 例1 値：4630 | 4491 | 4821 | 4480 | 4480
  - 同じ表の列：AuthorisationRefere…, PostalTownSuburb, PostalStateDescript…, PostalCountryDescri…, StatutoryClassDesc, AuthorisationTypeDe…, AuthorisationStatus…, AllocationClassDesc

## g0145（1 列）
- 見出し：PostalStateDescription
- 例1 値：QLD | QLD | QLD | QLD | QLD
  - 同じ表の列：AuthorisationRefere…, PostalTownSuburb, PostalPostalCode, PostalCountryDescri…, StatutoryClassDesc, AuthorisationTypeDe…, AuthorisationStatus…, AllocationClassDesc

## g0146（1 列）
- 見出し：PostalCountryDescription
- 例1 値：Australia | Australia | Australia | Australia | Australia
  - 同じ表の列：AuthorisationRefere…, PostalTownSuburb, PostalPostalCode, PostalStateDescript…, StatutoryClassDesc, AuthorisationTypeDe…, AuthorisationStatus…, AllocationClassDesc

## g0147（1 列）
- 見出し：StatutoryClassDesc
- 例1 値：Water Licence | Water Licence | Water Licence | Water Licence | Water Licence
  - 同じ表の列：AuthorisationRefere…, PostalTownSuburb, PostalPostalCode, PostalStateDescript…, PostalCountryDescri…, AuthorisationTypeDe…, AuthorisationStatus…, AllocationClassDesc

## g0148（1 列）
- 見出し：AuthorisationTypeDesc
- 例1 値：Licence to take water | Licence to take water | Licence to interfere by impounding-Emba… | Licence to take water | Licence to take water
  - 同じ表の列：AuthorisationRefere…, PostalTownSuburb, PostalPostalCode, PostalStateDescript…, PostalCountryDescri…, StatutoryClassDesc, AuthorisationStatus…, AllocationClassDesc

## g0149（1 列）
- 見出し：AuthorisationStatusDesc
- 例1 値：Issued | Issued | Issued | Issued | Issued
  - 同じ表の列：AuthorisationRefere…, PostalTownSuburb, PostalPostalCode, PostalStateDescript…, PostalCountryDescri…, StatutoryClassDesc, AuthorisationTypeDe…, AllocationClassDesc

## g0150（1 列）
- 見出し：AllocationClassDesc
- 例1 値：Unsupplemented Water | Unsupplemented Water | Unsupplemented Water | Unsupplemented Water | Unsupplemented Water
  - 同じ表の列：AuthorisationRefere…, PostalTownSuburb, PostalPostalCode, PostalStateDescript…, PostalCountryDescri…, StatutoryClassDesc, AuthorisationTypeDe…, AuthorisationStatus…

## g0151（1 列）
- 見出し：IsActive
- 例1 値：YES | YES | YES | YES | YES
  - 同じ表の列：AuthorisationRefere…, PostalTownSuburb, PostalPostalCode, PostalStateDescript…, PostalCountryDescri…, StatutoryClassDesc, AuthorisationTypeDe…, AuthorisationStatus…

## g0152（1 列）
- 見出し：Recycled water scheme
- 例1 値：Karana Downs STP Recycled Water Scheme | North Rockhampton Recycled Water Scheme | Nanango Golf Club Irrigation Scheme | Mossman WWTP Recycled Water Scheme | Burrum Heads Reuse Scheme
  - 同じ表の列：Scheme reference nu…, Recycled water prov…, Scheme type, Scheme manager

## g0153（1 列）
- 見出し：Scheme reference number
- 例1 値：SRN032 | SRN113 | SRN197 | SRN210 | SRN004
  - 同じ表の列：Recycled water sche…, Recycled water prov…, Scheme type, Scheme manager

## g0154（1 列）
- 見出し：Recycled water provider
- 例1 値：Rockhampton Regional Council | Cook Shire Council | The Star Entertainment Qld Limited T/A … | Toowoomba Regional Council | Townsville City Council
  - 同じ表の列：Recycled water sche…, Scheme reference nu…, Scheme type, Scheme manager

## g0155（1 列）
- 見出し：Scheme type
- 例1 値：Single Entity | Single Entity | Single Entity | Single Entity | Single Entity
  - 同じ表の列：Recycled water sche…, Scheme reference nu…, Recycled water prov…, Scheme manager

## g0156（1 列）
- 見出し：Scheme manager
- 例1 値：No | No | No | No | No
  - 同じ表の列：Recycled water sche…, Scheme reference nu…, Recycled water prov…, Scheme type

## g0157（1 列）
- 見出し：Department
- 例1 値：Fire and Emergency Services* | Tourism and Sport* | TOTAL | Youth Justice* | Education
  - 同じ表の列：Category, Total ($)

## g0158（1 列）
- 見出し：Category
- 例1 値：1,972 | Campaign ($) | $538,498.70 | 1,585,795 | 46,360,085
  - 同じ表の列：Department, Total ($)

## g0159（1 列）
- 見出し：Total ($)
- 例1 値：1,615,514 | 54,220 | 1,972 | 1,677,577 | 3,970,143
  - 同じ表の列：Department, Category

## g0160（2 列）
- 見出し：id
- 例1 値：325 | 27 | 421 | 299 | 383
  - 同じ表の列：map, lat, lon, created at, updated at
- 例2 値：1495 | 1502 | 1499 | 1501 | 1491
  - 同じ表の列：type, city, state

## g0161（1 列）
- 見出し：map
- 例1 値：5281 | 11910 | 6449 | 6449 | 8570
  - 同じ表の列：id, lat, lon, created at, updated at

## g0162（1 列）
- 見出し：created at
- 例1 値：1/04/2022 0:03 | 1/07/2022 5:21 | 29/03/2022 4:24 | 5/04/2022 0:11 | 31/03/2022 1:48
  - 同じ表の列：id, map, lat, lon, updated at

## g0163（1 列）
- 見出し：updated at
- 例1 値：22/09/2022 22:08 | 23/11/2022 5:27 | 22/09/2022 22:28 | 23/06/2022 4:01 | 17/06/2022 5:04
  - 同じ表の列：id, map, lat, lon, created at

## g0164（1 列）
- 見出し：Consumer
- 例1 値：Microbiological contamination | Undeclared allergens | TOTAL | SA only | Recalls affecting SA
  - 同じ表の列：58

## g0165（1 列）
- 見出し：58
- 例1 値：49 | 0 | 50 | 3 | 86
  - 同じ表の列：Consumer

## g0166（1 列）
- 見出し：Booking Ref
- 例1 値：5777 | 5485 | 5973 | 5292 | 4832
  - 同じ表の列：Is it a Sports Park?, Extended Booking, Type of Function, Number of participa…, Duration Days, Duration Hours, 10 working days min…, No of weekdays betw…

## g0167（1 列）
- 見出し：Is it a Sports Park?
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：Booking Ref, Extended Booking, Type of Function, Number of participa…, Duration Days, Duration Hours, 10 working days min…, No of weekdays betw…

## g0168（1 列）
- 見出し：Extended Booking
- 例1 値：Yes | Yes | Yes | Yes | Yes
  - 同じ表の列：Booking Ref, Is it a Sports Park?, Type of Function, Number of participa…, Duration Days, Duration Hours, 10 working days min…, No of weekdays betw…

## g0169（1 列）
- 見出し：Type of Function
- 例1 値：Special Event | Other | Wedding/Commitment Ceremony | Other | Other
  - 同じ表の列：Booking Ref, Is it a Sports Park?, Extended Booking, Number of participa…, Duration Days, Duration Hours, 10 working days min…, No of weekdays betw…

## g0170（1 列）
- 見出し：Number of participants
- 例1 値：80 | 25 | 60 | 70 | 80
  - 同じ表の列：Booking Ref, Is it a Sports Park?, Extended Booking, Type of Function, Duration Days, Duration Hours, 10 working days min…, No of weekdays betw…

## g0171（1 列）
- 見出し：Duration Days
- 例1 値：0 | 0 | 14 | 0 | 0
  - 同じ表の列：Booking Ref, Is it a Sports Park?, Extended Booking, Type of Function, Number of participa…, Duration Hours, 10 working days min…, No of weekdays betw…

## g0172（1 列）
- 見出し：Duration Hours
- 例1 値：2 | 4 | 2 | 9.5 | 2
  - 同じ表の列：Booking Ref, Is it a Sports Park?, Extended Booking, Type of Function, Number of participa…, Duration Days, 10 working days min…, No of weekdays betw…

## g0173（1 列）
- 見出し：10 working days minimum
- 例1 値：ok | ok | ok | ok | ok
  - 同じ表の列：Booking Ref, Is it a Sports Park?, Extended Booking, Type of Function, Number of participa…, Duration Days, Duration Hours, No of weekdays betw…

## g0174（1 列）
- 見出し：No of weekdays between received & start date
- 例1 値：68 | 224 | 51 | 32 | 325
  - 同じ表の列：Booking Ref, Is it a Sports Park?, Extended Booking, Type of Function, Number of participa…, Duration Days, Duration Hours, 10 working days min…

## g0175（1 列）
- 見出し：Park Suburb
- 例1 値：Labrador | Burleigh Heads | Burleigh Heads | Varsity Lakes | Hope Island
  - 同じ表の列：Booking Ref, Is it a Sports Park?, Extended Booking, Type of Function, Number of participa…, Duration Days, Duration Hours, 10 working days min…

## g0176（1 列）
- 見出し：type
- 例1 値：POINT | POINT | POINT | POINT | POINT
  - 同じ表の列：id, city, state

## g0177（1 列）
- 見出し：date
- 例1 値：5/01/2015 0:00 | 11/01/2015 12:00 | 9/02/2015 18:00 | 6/01/2015 19:00 | 8/01/2015 1:00
  - 同じ表の列：Period, Day, NOX, CO, PM2.5

## g0178（1 列）
- 見出し：Period
- 例1 値：2015 to before COVID | 2015 to before COVID | 2015 to before COVID | 2015 to before COVID | 2015 to before COVID
  - 同じ表の列：date, Day, NOX, CO, PM2.5

## g0179（1 列）
- 見出し：Day
- 例1 値：Monday | Friday | Thursday | Tuesday | Wednesday
  - 同じ表の列：date, Period, NOX, CO, PM2.5

## g0180（1 列）
- 見出し：NOX
- 例1 値：0.014 | 0.032 | 0.02 | 0.016 | 0.018
  - 同じ表の列：date, Period, Day, CO, PM2.5

## g0181（1 列）
- 見出し：CO
- 例1 値：0.14 | 0.19 | 0.25 | 0.33 | 0.3
  - 同じ表の列：date, Period, Day, NOX, PM2.5

## g0182（1 列）
- 見出し：PM2.5
- 例1 値：5.4 | 3.5 | -0.8 | 1.2 | 6.2
  - 同じ表の列：date, Period, Day, NOX, CO

## g0183（1 列）
- 見出し：Library control number
- 例1 値：b23769014 | b23808251 | b23748898 | b23779238 | b23757085
  - 同じ表の列：Collection number, Author, Published date, URLs

## g0184（1 列）
- 見出し：Collection number
- 例1 値：BA1628/122-129 | BA1621/405,427,440,534-535,539,623,710 | BA1621/494-495,499 | BA1621/273 | BA1621/201
  - 同じ表の列：Library control num…, Author, Published date, URLs

## g0185（1 列）
- 見出し：Author
- 例1 値：Parnell, Beryl, | Illustrations Ltd, | Parnell, Beryl, | Lee, Dorothy, | Parnell, Beryl,
  - 同じ表の列：Library control num…, Collection number, Published date, URLs

## g0186（1 列）
- 見出し：Published date
- 例1 値：1962-1963. | 1962 | 1962 | 1962 | 1962
  - 同じ表の列：Library control num…, Collection number, Author, URLs

## g0187（1 列）
- 見出し：URLs
- 例1 値：http://www.slwa.wa.gov.au/images/pd257/… | http://www.slwa.wa.gov.au/images/pd257/… | http://www.slwa.wa.gov.au/images/pd257/… | http://www.slwa.wa.gov.au/images/pd257/… | http://www.slwa.wa.gov.au/images/pd280/…
  - 同じ表の列：Library control num…, Collection number, Author, Published date

## g0188（1 列）
- 見出し：RECORD # Obit
- 例1 値：b18574166 | b18300145 | b18060560 | b18089252 | b18583398
  - 同じ表の列：SUMMARY, Date, Original source of …, Reference for Obitu…, Record # source of …, Link to Obit entry …, Link to Source of O…

## g0189（1 列）
- 見出し：SUMMARY
- 例1 値：Obituary of Teresa Lacy of Mt. Elizabet… | Obituary of Narrogin farmer. | Obituary of longtime Brookton resident.… | Brief obituary. | Obituary of vet and author of books on …
  - 同じ表の列：RECORD # Obit, Date, Original source of …, Reference for Obitu…, Record # source of …, Link to Obit entry …, Link to Source of O…

## g0190（1 列）
- 見出し：Date
- 例1 値：1937 | 1999 | 1999 | 1997 | 1985
  - 同じ表の列：RECORD # Obit, SUMMARY, Original source of …, Reference for Obitu…, Record # source of …, Link to Obit entry …, Link to Source of O…

## g0191（1 列）
- 見出し：Original source of Obituary
- 例1 値：West Australian. | Westerly. | The Sunday times. | Legacy in W.A. | West Australian.
  - 同じ表の列：RECORD # Obit, SUMMARY, Date, Reference for Obitu…, Record # source of …, Link to Obit entry …, Link to Source of O…

## g0192（1 列）
- 見出し：Reference for Obituary
- 例1 値：Vol. 5, No. 16, (4/9/1996), p. 4, 994.1… | 19 Nov. 1998, p. 4-5, 994.12/ROC | Dec. 1998, p. 12, 362.828 FOC, | Vol. 120 (December 1996) p.4-6 369.29 T… | 30 Jan. 1914, p.3d
  - 同じ表の列：RECORD # Obit, SUMMARY, Date, Original source of …, Record # source of …, Link to Obit entry …, Link to Source of O…

## g0193（1 列）
- 見出し：Record # source of obit
- 例1 値：b16809348 | b15243047 | b16809348 | b1674696x | b1143840x
  - 同じ表の列：RECORD # Obit, SUMMARY, Date, Original source of …, Reference for Obitu…, Link to Obit entry …, Link to Source of O…

## g0194（1 列）
- 見出し：Link to Obit entry on SLWA catalogue
- 例1 値：https://encore.slwa.wa.gov.au/iii/encor… | https://encore.slwa.wa.gov.au/iii/encor… | https://encore.slwa.wa.gov.au/iii/encor… | https://encore.slwa.wa.gov.au/iii/encor… | https://encore.slwa.wa.gov.au/iii/encor…
  - 同じ表の列：RECORD # Obit, SUMMARY, Date, Original source of …, Reference for Obitu…, Record # source of …, Link to Source of O…

## g0195（1 列）
- 見出し：Link to Source of Obit on SLWA catalogue
- 例1 値：https://encore.slwa.wa.gov.au/iii/encor… | https://encore.slwa.wa.gov.au/iii/encor… | https://encore.slwa.wa.gov.au/iii/encor… | https://encore.slwa.wa.gov.au/iii/encor… | https://encore.slwa.wa.gov.au/iii/encor…
  - 同じ表の列：RECORD # Obit, SUMMARY, Date, Original source of …, Reference for Obitu…, Record # source of …, Link to Obit entry …

## g0196（1 列）
- 見出し：Record number
- 例1 値：.b31088880 | .b31086469 | .b31088107 | .b31087784 | .b31087966
  - 同じ表の列：Call number, Title, Published, Subject - Topical, Series, Link

## g0197（1 列）
- 見出し：Call number
- 例1 値：1364B/158 | 1364B/50 | 1364B/52 | 1364B/102 | 1364B/133
  - 同じ表の列：Record number, Title, Published, Subject - Topical, Series, Link

## g0198（1 列）
- 見出し：Title
- 例1 値：In loving memory of Pte. Lewis Edward O… | In loving memory of Sergt. Ernest Willi… | In loving memory of Pte. Percival Ernes… | In loving memory of Private Harry Moore… | In loving memory of Driver Herbert Alex…
  - 同じ表の列：Record number, Call number, Published, Subject - Topical, Series, Link

## g0199（1 列）
- 見出し：Published
- 例1 値：1917 | 1918 | 1917 | 1918 | 1917
  - 同じ表の列：Record number, Call number, Title, Subject - Topical, Series, Link

## g0200（1 列）
- 見出し：Subject - Topical
- 例1 値：Soldiers;Online image. | Soldiers;Online image. | Soldiers;Online image. | Soldiers;Online image. | Soldiers;Online image.
  - 同じ表の列：Record number, Call number, Title, Published, Series, Link

## g0201（1 列）
- 見出し：Series
- 例1 値：Collection of "In Memoriam" cards with … | Collection of "In Memoriam" cards with … | Collection of "In Memoriam" cards with … | Collection of "In Memoriam" cards with … | Collection of "In Memoriam" cards with …
  - 同じ表の列：Record number, Call number, Title, Published, Subject - Topical, Link

## g0202（1 列）
- 見出し：Link
- 例1 値：http://purl.slwa.wa.gov.au/slwa_b310939… | http://purl.slwa.wa.gov.au/slwa_b310877… | http://purl.slwa.wa.gov.au/slwa_b311052… | http://purl.slwa.wa.gov.au/slwa_b310940… | http://purl.slwa.wa.gov.au/slwa_b311045…
  - 同じ表の列：Record number, Call number, Title, Published, Subject - Topical, Series

## g0203（3 列）
- 見出し：ogr_fid
- 例1 値：61 | 93 | 60 | 166 | 160
  - 同じ表の列：zone_code, zone_statu
- 例2 値：175 | 519 | 310 | 145 | 155
  - 同じ表の列：pfi, schemecode, lga_code, lga, zone_num, zonestatus, zone_code, zone_desc

## g0204（3 列）
- 見出し：zone_code
- 例1 値：UFZ | UFZ | UFZ | UFZ | UFZ
  - 同じ表の列：ogr_fid, zone_statu
- 例2 値：UFZ | UFZ | UFZ | UFZ | UFZ
  - 同じ表の列：ogr_fid, pfi, schemecode, lga_code, lga, zone_num, zonestatus, zone_desc

## g0205（2 列）
- 見出し：zone_statu
- 例1 値：p | p | p | p | p
  - 同じ表の列：ogr_fid, zone_code
- 例2 値：p | p | p | p | p
  - 同じ表の列：ogr_fid, zone_code

## g0206（1 列）
- 見出し：pfi
- 例1 値：3086749 | 3086738 | 3086838 | 3086752 | 3086748
  - 同じ表の列：ogr_fid, schemecode, lga_code, lga, zone_num, zonestatus, zone_code, zone_desc

## g0207（1 列）
- 見出し：schemecode
- 例1 値：ZN | ZN | ZN | ZN | ZN
  - 同じ表の列：ogr_fid, pfi, lga_code, lga, zone_num, zonestatus, zone_code, zone_desc

## g0208（1 列）
- 見出し：lga_code
- 例1 値：364 | 364 | 364 | 364 | 364
  - 同じ表の列：ogr_fid, pfi, schemecode, lga, zone_num, zonestatus, zone_code, zone_desc

## g0209（1 列）
- 見出し：lga
- 例1 値：STRATHBOGIE | STRATHBOGIE | STRATHBOGIE | STRATHBOGIE | STRATHBOGIE
  - 同じ表の列：ogr_fid, pfi, schemecode, lga_code, zone_num, zonestatus, zone_code, zone_desc

## g0210（1 列）
- 見出し：zone_num
- 例1 値：5008 | 5008 | 5008 | 5008 | 5008
  - 同じ表の列：ogr_fid, pfi, schemecode, lga_code, lga, zonestatus, zone_code, zone_desc

## g0211（1 列）
- 見出し：zonestatus
- 例1 値：g | g | g | g | g
  - 同じ表の列：ogr_fid, pfi, schemecode, lga_code, lga, zone_num, zone_code, zone_desc

## g0212（1 列）
- 見出し：zone_desc
- 例1 値：URBAN FLOODWAY ZONE | URBAN FLOODWAY ZONE | URBAN FLOODWAY ZONE | URBAN FLOODWAY ZONE | URBAN FLOODWAY ZONE
  - 同じ表の列：ogr_fid, pfi, schemecode, lga_code, lga, zone_num, zonestatus, zone_code

## g0213（1 列）
- 見出し：gaz_b_date
- 例1 値：2006/04/27 | 2006/04/27 | 2006/04/27 | 2006/04/27 | 2006/04/27
  - 同じ表の列：ogr_fid, pfi, schemecode, lga_code, lga, zone_num, zonestatus, zone_code

## g0214（1 列）
- 見出し：Demographics
- 例1 値：Highest quintile household weekly income | Mother born overseas | Has a disability or long-term health co… | Father born in other countries | No non-school qualification
  - 同じ表の列：Physical violence (…, Total violence ('00…, Emotional abuse ('0…, Total ever-partnere…

## g0215（1 列）
- 見出し：Physical violence ('000)
- 例1 値：118 | 20.1 | 33.8 | 27.8 | 15.1
  - 同じ表の列：Demographics, Total violence ('00…, Emotional abuse ('0…, Total ever-partnere…

## g0216（1 列）
- 見出し：Total violence ('000)
- 例1 値：155.9 | 113.5 | 27.7 | 92.2 | 63.1
  - 同じ表の列：Demographics, Physical violence (…, Emotional abuse ('0…, Total ever-partnere…

## g0217（1 列）
- 見出し：Emotional abuse ('000)
- 例1 値：333.9 | 65 | 451.5 | 97 | 85.8
  - 同じ表の列：Demographics, Physical violence (…, Total violence ('00…, Total ever-partnere…

## g0218（1 列）
- 見出し：Total ever-partnered woman ('000)
- 例1 値：3476.4 | 1242.8 | 1155.7 | 855.5 | 5045.8
  - 同じ表の列：Demographics, Physical violence (…, Total violence ('00…, Emotional abuse ('0…

## g0219（1 列）
- 見出し：Tradeunionmembershipinmainjob
- 例1 値：884.8 | 800.8 | 858.2 | 1547.2 | 1570.4
  - 同じ表の列：Year, Tradeuniondensityin…

## g0220（1 列）
- 見出し：Tradeuniondensityinmainjob
- 例1 値：15.9 | 17.8 | 18.4 | 13.3 | 18.4
  - 同じ表の列：Year, Tradeunionmembershi…

## g0221（1 列）
- 見出し：Month
- 例1 値：Feb-19 | Jul-18 | Aitkenvale Library extended hours comme… | Jun-18 | Nov-16
  - 同じ表の列：Aitkenvale Branch, Thuringowa Branch, Home Library Service, Total Library Branc…

## g0222（3 列）
- 見出し：Aitkenvale Branch
- 例1 値：16303 | 47622 | 46278 | 49791 | 48819
  - 同じ表の列：Month, Thuringowa Branch, Home Library Service, Total Library Branc…
- 例2 値：147 | 272 | 195 | 144 | 151
  - 同じ表の列：Month, Riverway Branch, Thuringowa Branch, Home Library Service, Total Library Branc…

## g0223（3 列）
- 見出し：Thuringowa Branch
- 例1 値：57912 | 62485 | 59104 | 59979 | 63900
  - 同じ表の列：Month, Aitkenvale Branch, Home Library Service, Total Library Branc…
- 例2 値：158 | 120 | 175 | 103 | 126
  - 同じ表の列：Month, Aitkenvale Branch, Riverway Branch, Home Library Service, Total Library Branc…

## g0224（2 列）
- 見出し：Home Library Service
- 例1 値：680 | 683 | 685 | 683 | 687
  - 同じ表の列：Month, Aitkenvale Branch, Thuringowa Branch, Total Library Branc…
- 例2 値：2 | 1 | 1 | 1 | 1
  - 同じ表の列：Month, Aitkenvale Branch, Riverway Branch, Thuringowa Branch, Total Library Branc…

## g0225（3 列）
- 見出し：Total Library Branches
- 例1 値：141337 | 39815 | 60927 | 129102 | 153210
  - 同じ表の列：Month, Aitkenvale Branch, Thuringowa Branch, Home Library Service
- 例2 値：551 | 625 | 360 | 445 | 490
  - 同じ表の列：Month, Aitkenvale Branch, Riverway Branch, Thuringowa Branch, Home Library Service

## g0226（1 列）
- 見出し：Month
- 例1 値：Aug-26 | Feb-23 | May-26 | Sep-19 | Mar-17
  - 同じ表の列：Aitkenvale Branch, Riverway Branch, Thuringowa Branch, Home Library Service, Total Library Branc…

## g0227（2 列）
- 見出し：Riverway Branch
- 例1 値：213 | 166 | 204 | 418 | 289
  - 同じ表の列：Month, Aitkenvale Branch, Thuringowa Branch, Home Library Service, Total Library Branc…
- 例2 値：14393 | 17183 | 19149 | 15080 | 16788
  - 同じ表の列：Month, Aitkenvale Branch, Thuringowa Branch, Total Library Branc…

## g0228（1 列）
- 見出し：Month
- 例1 値：Aug-16 | Dec-24 | Aug-17 | During January 2021 the Mobile Library … | Sep-26
  - 同じ表の列：Aitkenvale Branch, Riverway Branch, Thuringowa Branch, Total Library Branc…

## g0229（1 列）
- 見出し：Funding agency
- 例1 値：DTET | DTET | DTET | DTET | DTET
  - 同じ表の列：Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2, Client group3

## g0230（1 列）
- 見出し：Program title
- 例1 値：Gateway to Industry Schools | Regional Jobs Commitees | Skilling Queenslanders for Work | Aviation Strategy | Skilling Queenslanders for Work
  - 同じ表の列：Funding agency, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2, Client group3

## g0231（1 列）
- 見出し：Sub-program title
- 例1 値：Ready for Work | First Start - Councils | Youth Skills | Get Set for Work | Skill Up
  - 同じ表の列：Funding agency, Program title, Purpose, Category1, Category2, Client group1, Client group2, Client group3

## g0232（1 列）
- 見出し：Purpose
- 例1 値：This program provides public funding di… | Provides wage subsidies to local counci… | Funds community based organisations to … | Funds community based organisations to … | Back to Work has a range of financial a…
  - 同じ表の列：Funding agency, Program title, Sub-program title, Category1, Category2, Client group1, Client group2, Client group3

## g0233（1 列）
- 見出し：Category1
- 例1 値：Education and training | Education and training | Employment and jobs | Business and industry | Education and training
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category2, Client group1, Client group2, Client group3

## g0234（1 列）
- 見出し：Category2
- 例1 値：Employment and jobs | Employment and jobs | Employment and jobs | Employment and jobs | Employment and jobs
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Client group1, Client group2, Client group3

## g0235（1 列）
- 見出し：Client group1
- 例1 値：Jobseekers | Government | Jobseekers | Employers | Jobseekers
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group2, Client group3

## g0236（1 列）
- 見出し：Client group2
- 例1 値：Jobseekers | Employees | Employees | Students | Employees
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group3

## g0237（1 列）
- 見出し：Client group3
- 例1 値：Jobseekers | Jobseekers | Employees | Jobseekers | Employees
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0238（1 列）
- 見出し：Client group4
- 例1 値：Businesses | Businesses | Businesses
  - 同じ表の列：Funding agency, Program title, Sub-program title, Purpose, Category1, Category2, Client group1, Client group2

## g0239（1 列）
- 見出し：GTFS from DIVA
- 例1 値：5801 | 2455 | 5387 | 5782 | 5046
  - 同じ表の列：GTFS from Operator

## g0240（1 列）
- 見出し：GTFS from Operator
- 例1 値：5653 | 5174 | 5414 | 5040 | 5682
  - 同じ表の列：GTFS from DIVA

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
