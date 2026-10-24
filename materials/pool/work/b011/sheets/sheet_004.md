# ラベル用シート 004 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_004.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0361（2 列）
- 見出し：location
- 例1 値：Nullarbor Plain | Nullarbor Plain | Mt Drygalski | Mt Drygalski | Azorella Peninsula
  - 同じ表の列：species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments
- 例2 値：W Stornes | W Stornes | S Broknes | N Stornes | NE Stornes
  - 同じ表の列：lake_id, altitude, lake_area, catchment_area, maximum_depth, dimensions, distance_from_polar…, geology

## g0362（1 列）
- 見出し：species
- 例1 値：South Georgian Diving Petrel | South Georgian Diving Petrel | ANARE | Subantarctic Skua | South Georgian Diving Petrel
  - 同じ表の列：location, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0363（1 列）
- 見出し：id
- 例1 値：point_48 | line_18 | polygon_16 | polygon_11 | polygon_19
  - 同じ表の列：location, species, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0364（1 列）
- 見出し：feature
- 例1 値：Nest | Nest | Colony | Nest | Colony
  - 同じ表の列：location, species, id, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0365（1 列）
- 見出し：observation_date
- 例1 値：2000-12-03 | 2000-12-15 | 2000-11-19 | 2000-11-02 | 2000-11-17
  - 同じ表の列：location, species, id, feature, observation_date_ye…, observation_date_mo…, observation_date_day, comments

## g0366（1 列）
- 見出し：observation_date_year
- 例1 値：2000 | 2000 | 2001 | 2000 | 2000
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_mo…, observation_date_day, comments

## g0367（1 列）
- 見出し：observation_date_month
- 例1 値：1 | 1 | 1 | 12 | 12
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_day, comments

## g0368（1 列）
- 見出し：observation_date_day
- 例1 値：11 | 29 | 19 | 12 | 15
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, comments

## g0369（1 列）
- 見出し：comments
- 例1 値：Colony extends 10m to S | Northern extent of SGDP burrows onto AP | Colony 5 EJW/HJA | Veg north of this line | Needs work with aerial photographs
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day

## g0370（1 列）
- 見出し：data_type
- 例1 値：point | point | polygon | point | point
  - 同じ表の列：location, species, id, feature, observation_date, observation_date_ye…, observation_date_mo…, observation_date_day

## g0371（2 列）
- 見出し：Question
- 例1 値：13 | 12 | 1 | 23 | 4
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：26 | 21 | 28 | 16 | 27
  - 同じ表の列：Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0372（1 列）
- 見出し：Question_Text
- 例1 値：How much should the government spend on… | The Australian constitution should reco… | The government's parental leave pay sho… | The national budget deficit should be r… | Australia should spend more on foreign …
  - 同じ表の列：Question, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0373（2 列）
- 見出し：category1_definition_1
- 例1 値：Much Less | Strongly disagree | Strongly disagree | Strongly disagree | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Much Less | Strongly disagree | Strongly disagree | Much Less | Strongly disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0374（2 列）
- 見出し：category1_definition_2
- 例1 値：Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat Less | Somewhat disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree | Somewhat disagree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0375（1 列）
- 見出し：category1_definition_3
- 例1 値：Neutral | Neutral | Neutral | Neutral | Neutral
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0376（2 列）
- 見出し：category1_definition_4
- 例1 値：Somewhat more | Somewhat agree | Somewhat more | Somewhat agree | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Somewhat more | Somewhat agree | Somewhat agree | Somewhat agree | Somewhat agree
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0377（2 列）
- 見出し：category1_definition_5
- 例1 値：Strongly agree | Strongly agree | Strongly agree | Much more | Much more
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Strongly agree | Much more | Strongly agree | Strongly agree | Much more
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0378（2 列）
- 見出し：category1_definition_DK
- 例1 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…
- 例2 値：Dont Know | Dont Know | Dont Know | Dont Know | Dont Know
  - 同じ表の列：Question, Question_Text, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…, category1_definitio…

## g0379（1 列）
- 見出し：Month
- 例1 値：2014-07-13T00:00:00 | 2014-10-13T00:00:00 | 2014-01-14T00:00:00 | 2014-08-13T00:00:00 | 2014-11-13T00:00:00
  - 同じ表の列：Traffic Source, Views, Visits

## g0380（1 列）
- 見出し：Traffic Source
- 例1 値：External | External | External | External | External
  - 同じ表の列：Month, Views, Visits

## g0381（2 列）
- 見出し：Views
- 例1 値：4 | 15 | 73254 | 241 | 2200297
  - 同じ表の列：Month, Traffic Source, Visits
- 例2 値：6 | 39 | 7 | 2 | 7
  - 同じ表の列：Dataset Title, Visits, Resource downloads, Dataset formats

## g0382（2 列）
- 見出し：Visits
- 例1 値：3 | 2 | 4 | 2 | 2
  - 同じ表の列：Month, Traffic Source, Views
- 例2 値：1 | 5 | 0 | 5 | 1
  - 同じ表の列：Dataset Title, Views, Resource downloads, Dataset formats

## g0383（3 列）
- 見出し：Month
- 例1 値：Nov-85 | Oct-85 | Jun-85 | Nov-85 | Apr-85
  - 同じ表の列：Airline, Port_Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes), Mail_Out_(tonnes)
- 例2 値：Dec-17 | Dec-09 | Dec-05 | Dec-08 | Dec-93
  - 同じ表の列：Males 15-24 unemplo…, Males 25-34 unemplo…, Males 35-44 unemplo…, Males 45-54 unemplo…, Males 55-64 unemplo…, Males 65 and over u…, Males 15 and over u…, Males 15-64 unemplo…

## g0384（1 列）
- 見出し：Airline
- 例1 値：Air Caledonie | Qantas Airways | Air New Zealand | Cathay Pacific Airways | Air China
  - 同じ表の列：Month, Port_Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes), Mail_Out_(tonnes)

## g0385（1 列）
- 見出し：Port_Country
- 例1 値：France | Malaysia | Fiji | Fiji | Zimbabwe
  - 同じ表の列：Month, Airline, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes), Mail_Out_(tonnes)

## g0386（2 列）
- 見出し：Passengers_In
- 例1 値：627 | 1423 | 296 | 84 | 1718
  - 同じ表の列：Month, Airline, Port_Country, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes), Mail_Out_(tonnes)
- 例2 値：0 | 130 | 108 | 6456 | 6064
  - 同じ表の列：Month, AustralianPort, ForeignPort, Country, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes)

## g0387（1 列）
- 見出し：Freight_In_(tonnes)
- 例1 値：20.504 | 1.9 | 71.082 | 7.559 | 230.926
  - 同じ表の列：Month, Airline, Port_Country, Passengers_In, Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes), Mail_Out_(tonnes)

## g0388（2 列）
- 見出し：Mail_In_(tonnes)
- 例1 値：0.14 | 0.454 | 0.163 | 0 | 0
  - 同じ表の列：Month, Airline, Port_Country, Passengers_In, Freight_In_(tonnes), Passengers_Out, Freight_Out_(tonnes), Mail_Out_(tonnes)
- 例2 値：0 | 0.001 | 0 | 0 | 0
  - 同じ表の列：Month, AustralianPort, ForeignPort, Country, Passengers_In, Freight_In_(tonnes), Passengers_Out, Freight_Out_(tonnes)

## g0389（2 列）
- 見出し：Passengers_Out
- 例1 値：1112 | 76 | 0 | 1932 | 8
  - 同じ表の列：Month, Airline, Port_Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Freight_Out_(tonnes), Mail_Out_(tonnes)
- 例2 値：11 | 1513 | 147 | 1854 | 1427
  - 同じ表の列：Month, AustralianPort, ForeignPort, Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Freight_Out_(tonnes)

## g0390（2 列）
- 見出し：Freight_Out_(tonnes)
- 例1 値：67.966 | 54.801 | 224.614 | 3.313 | 238.439
  - 同じ表の列：Month, Airline, Port_Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Mail_Out_(tonnes)
- 例2 値：71.681 | 0.288 | 3.855 | 16.588 | 11.117
  - 同じ表の列：Month, AustralianPort, ForeignPort, Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out

## g0391（1 列）
- 見出し：Mail_Out_(tonnes)
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Month, Airline, Port_Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes)

## g0392（21 列）
- 見出し：Year
- 例1 値：1985 | 1985 | 1985 | 1985 | 1985
  - 同じ表の列：Month, Airline, Port_Country, Passengers_In, Freight_In_(tonnes), Mail_In_(tonnes), Passengers_Out, Freight_Out_(tonnes)
- 例2 値：2020 | 2018 | 2025 | 2024 | 2023
  - 同じ表の列：Average Age

## g0393（6 列）
- 見出し：OBJECTID
- 例1 値：2276 | 2441 | 2978 | 2350 | 2705
  - 同じ表の列：Type, DATE_, Length, CREATED_DA
- 例2 値：8 | 3 | 1 | 4 | 6
  - 同じ表の列：Administrative_Auth…, Town, Eircode, County, Services_Available, Website, Opening_Hours_Monday, Opening_Hours_Tuesd…

## g0394（1 列）
- 見出し：Type
- 例1 値：On Road | Off Road | On Road | Off Road | On Road
  - 同じ表の列：OBJECTID, DATE_, Length, CREATED_DA

## g0395（1 列）
- 見出し：DATE_
- 例1 値：2009 | 2013 | 2015 | 2008 | 2009
  - 同じ表の列：OBJECTID, Type, Length, CREATED_DA

## g0396（1 列）
- 見出し：Length
- 例1 値：230 | 258 | 198 | 955 | 347
  - 同じ表の列：OBJECTID, Type, DATE_, CREATED_DA

## g0397（1 列）
- 見出し：CREATED_DA
- 例1 値：12/03/2015 | 12/03/2015 | 12/03/2015 | 13/03/2015 | 13/03/2015
  - 同じ表の列：OBJECTID, Type, DATE_, Length

## g0398（1 列）
- 見出し：COGG
- 例1 値：Y | Y | N | Y | Y
  - 同じ表の列：long, lat

## g0399（8 列）
- 見出し：long
- 例1 値：144.466362246937 | 144.323749808252 | 144.347212167434 | 144.324520907402 | 144.410721667682
  - 同じ表の列：COGG, lat
- 例2 値：143.884521 | 143.758713 | 143.825216 | 144.042493 | 143.825216
  - 同じ表の列：Complex_Type, Facility_Type, Bookable_Item, Assessment_No, Number, Locality, Post_Code, Home_Clubs

## g0400（1 列）
- 見出し：Zone
- 例1 値：RH | R | RCE | Con | CSTCON
  - 同じ表の列：Number of Properties

## g0401（1 列）
- 見出し：Number of Properties
- 例1 値：286 | 1696 | 2987 | 1195 | 28
  - 同じ表の列：Zone

## g0402（1 列）
- 見出し：lat, lon
- 例1 値：-37.827293113, 145.00101761 | -37.790985832, 144.9854569 | -37.794337922, 144.99098755 | -37.829629108, 145.02253525 | -37.784701809, 144.98381871
  - 同じ表の列：genus, species, dbh, height, common, location, ref, maturity

## g0403（3 列）
- 見出し：genus
- 例1 値：Phoenix | Ulmus | Quercus | Quercus | Corymbia
  - 同じ表の列：lat, lon, species, dbh, height, common, location, ref, maturity
- 例2 値：Quercus | Ulmus | Platanus | Corymbia | Eucalyptus
  - 同じ表の列：lat, long, tree_id, feature_id, significan, species, common_nam, area

## g0404（1 列）
- 見出し：species
- 例1 値：U. minor 'Atinia' | U. minor 'Atinia' | E. mannifera | E. cladocalyx | U. minor 'Atinia'
  - 同じ表の列：lat, lon, genus, dbh, height, common, location, ref, maturity

## g0405（1 列）
- 見出し：dbh
- 例1 値：154 | 52 | 69 | 54 | 80
  - 同じ表の列：lat, lon, genus, species, height, common, location, ref, maturity

## g0406（1 列）
- 見出し：height
- 例1 値：13 | 24 | 10 | 23 | 20
  - 同じ表の列：lat, lon, genus, species, dbh, common, location, ref, maturity

## g0407（1 列）
- 見出し：common
- 例1 値：London Plane | Canary Island Date Palm | Spotted Gum | Holm Oak | Cockspur Coral
  - 同じ表の列：lat, lon, genus, species, dbh, height, location, ref, maturity

## g0408（1 列）
- 見出し：location
- 例1 値：residential | other | park | street | other
  - 同じ表の列：lat, lon, genus, species, dbh, height, common, ref, maturity

## g0409（4 列）
- 見出し：ref
- 例1 値：41 | 186 | 162 | 116 | 118
  - 同じ表の列：lat, lon, genus, species, dbh, height, common, location, maturity
- 例2 値：84216 | 84677 | 84440 | 84304 | 85236
  - 同じ表の列：type, desc, long

## g0410（1 列）
- 見出し：maturity
- 例1 値：Mature | Mature | Mature | Mature | Mature
  - 同じ表の列：lat, lon, genus, species, dbh, height, common, location, ref

## g0411（1 列）
- 見出し：updated
- 例1 値：2012-08-16 | 2012-10-08 | 2012-10-04 | 2012-08-29 | 2012-10-03
  - 同じ表の列：lat, lon, genus, species, dbh, height, common, location, ref

## g0412（4 列）
- 見出し：suburb
- 例1 値：Timboon | Lismore | Camperdown | Terang | Cobden
  - 同じ表の列：assetType, lon, lat, fme_feature_type
- 例2 値：Shepparton | Balranald | Rylstone | Collarenebri | Riverwood
  - 同じ表の列：uniqueID, title, state, locationInstructions, driveThroughTesting, wheelchairAccessible, walkInAllowed, bookingRequired

## g0413（2 列）
- 見出し：assetType
- 例1 値：Toddlers Pool | Toddlers Pool | Toddlers Pool | Toddlers Pool | Toddlers Pool
  - 同じ表の列：suburb, lon, lat, fme_feature_type
- 例2 値：Main Pool | Main Pool | Main Pool | Main Pool | Main Pool
  - 同じ表の列：suburb, lon, lat, fme_feature_type

## g0414（2 列）
- 見出し：fme_feature_type
- 例1 値：dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings
  - 同じ表の列：suburb, assetType, lon, lat
- 例2 値：dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings | dbo.Buildings
  - 同じ表の列：suburb, assetType, lon, lat

## g0415（1 列）
- 見出し：ApplStandard
- 例1 値：Greenhouse and Energy Minimum Standards… | Greenhouse and Energy Minimum Standards… | Greenhouse and Energy Minimum Standards… | Greenhouse and Energy Minimum Standards… | Greenhouse and Energy Minimum Standards…
  - 同じ表の列：Brand, Labelled energy con…, CompartGrVol, CompartType, Configuration, Country, Depth, Designation

## g0416（1 列）
- 見出し：Brand
- 例1 値：KMBrand | Bunnings Australia | Bunnings Australia | Bunnings Australia | Bunnings Australia
  - 同じ表の列：ApplStandard, Labelled energy con…, CompartGrVol, CompartType, Configuration, Country, Depth, Designation

## g0417（1 列）
- 見出し：Labelled energy consumption (kWh/year)
- 例1 値：1265 | 1265 | 2230 | 1288 | 1288
  - 同じ表の列：ApplStandard, Brand, CompartGrVol, CompartType, Configuration, Country, Depth, Designation

## g0418（1 列）
- 見出し：CompartGrVol
- 例1 値：20 | 20 | 20 | 20 | 20
  - 同じ表の列：ApplStandard, Brand, Labelled energy con…, CompartType, Configuration, Country, Depth, Designation

## g0419（1 列）
- 見出し：CompartType
- 例1 値：Wine storage | Wine storage | Wine storage | Wine storage | Wine storage
  - 同じ表の列：ApplStandard, Brand, Labelled energy con…, CompartGrVol, Configuration, Country, Depth, Designation

## g0420（1 列）
- 見出し：Configuration
- 例1 値：Upright | Upright | Upright | Upright | Upright
  - 同じ表の列：ApplStandard, Brand, Labelled energy con…, CompartGrVol, CompartType, Country, Depth, Designation

## g0421（1 列）
- 見出し：Country
- 例1 値：Australia, New Zealand | Australia, New Zealand | Australia, New Zealand | Australia, New Zealand | Australia, New Zealand
  - 同じ表の列：ApplStandard, Brand, Labelled energy con…, CompartGrVol, CompartType, Configuration, Depth, Designation

## g0422（1 列）
- 見出し：Depth
- 例1 値：10.83 | 16.89 | 16.89 | 23.82 | 10.83
  - 同じ表の列：ApplStandard, Brand, Labelled energy con…, CompartGrVol, CompartType, Configuration, Country, Designation

## g0423（1 列）
- 見出し：Designation
- 例1 値：Cooled appliance | Cooled appliance | Cooled appliance | Cooled appliance | Cooled appliance
  - 同じ表の列：ApplStandard, Brand, Labelled energy con…, CompartGrVol, CompartType, Configuration, Country, Depth

## g0424（1 列）
- 見出し：FF Vol
- 例1 値：20.0 | 20.0 | 20.0 | 20.0 | 20.0
  - 同じ表の列：ApplStandard, Brand, Labelled energy con…, CompartGrVol, CompartType, Configuration, Country, Depth

## g0425（1 列）
- 見出し：Employment Category
- 例1 値：Education & Children's Services Act | Education & Children's Services Act | Education & Children's Services Act | Education & Children's Services Act | Education & Children's Services Act
  - 同じ表の列：Role, Measure, fin_year, Headcount

## g0426（1 列）
- 見出し：Role
- 例1 値：Preschool Directors and Preschool Teach… | School services officers providing admi… | Corporate employees in the Department f… | Aboriginal community education officers… | Groundspeople and bus drivers employed …
  - 同じ表の列：Employment Category, Measure, fin_year, Headcount

## g0427（1 列）
- 見出し：Measure
- 例1 値：Revised contingent workforce | Total workforce | Total workforce | Contingent workforce | Contingent adjustment
  - 同じ表の列：Employment Category, Role, fin_year, Headcount

## g0428（1 列）
- 見出し：fin_year
- 例1 値：2024 | 2021 | 2025 | 2018 | 2025
  - 同じ表の列：Employment Category, Role, Measure, Headcount

## g0429（1 列）
- 見出し：Headcount
- 例1 値：204 | 24 | 168 | 583 | 454
  - 同じ表の列：Employment Category, Role, Measure, fin_year

## g0430（1 列）
- 見出し：Parent Contract ID
- 例1 値：CN3616118 | CN3654193 | CN3616121 | CN3566794 | CN3583008
  - 同じ表の列：Contract ID, Publish Date, Start Date, End Date, Value, Amendment Date, Amendment Start Date, Amendments Value

## g0431（1 列）
- 見出し：Contract ID
- 例1 値：CN3626003 | CN3606085 | CN3650320 | CN3638533 | CN3693065
  - 同じ表の列：Parent Contract ID, Publish Date, Start Date, End Date, Value, Amendment Date, Amendment Start Date, Amendments Value

## g0432（1 列）
- 見出し：Publish Date
- 例1 値：2020-06-19T00:00:00 | 2020-03-27T00:00:00 | 2020-03-13T00:00:00 | 2020-03-31T00:00:00 | 2020-02-21T00:00:00
  - 同じ表の列：Parent Contract ID, Contract ID, Start Date, End Date, Value, Amendment Date, Amendment Start Date, Amendments Value

## g0433（1 列）
- 見出し：Start Date
- 例1 値：2019-10-11T00:00:00 | 2019-08-30T00:00:00 | 2020-06-29T00:00:00 | 2020-02-17T00:00:00 | 2020-04-17T00:00:00
  - 同じ表の列：Parent Contract ID, Contract ID, Publish Date, End Date, Value, Amendment Date, Amendment Start Date, Amendments Value

## g0434（1 列）
- 見出し：End Date
- 例1 値：2020-12-01T00:00:00 | 2020-06-30T00:00:00 | 2020-03-03T00:00:00 | 2020-06-30T00:00:00 | 2019-12-31T00:00:00
  - 同じ表の列：Parent Contract ID, Contract ID, Publish Date, Start Date, Value, Amendment Date, Amendment Start Date, Amendments Value

## g0435（4 列）
- 見出し：Value
- 例1 値：11544.72 | 10846 | 68200 | 65991.18 | 15895
  - 同じ表の列：Parent Contract ID, Contract ID, Publish Date, Start Date, End Date, Amendment Date, Amendment Start Date, Amendments Value
- 例2 値：343 | 1.3 | 2.1 | 2.5 | 341
  - 同じ表の列：STATISTIC, Statistic, TLIST(A1), Year, C02199V02655, Sex, C02842V03416, HSE Regions

## g0436（1 列）
- 見出し：Amendment Date
- 例1 値：2019-07-01T00:00:00 | 2020-01-22T00:00:00 | 2020-06-11T00:00:00 | 2019-07-30T00:00:00 | 2019-07-31T00:00:00
  - 同じ表の列：Parent Contract ID, Contract ID, Publish Date, Start Date, End Date, Value, Amendment Start Date, Amendments Value

## g0437（1 列）
- 見出し：Amendment Start Date
- 例1 値：2019-07-01T00:00:00 | 2016-08-01T00:00:00 | 2018-07-01T00:00:00 | 2018-07-01T00:00:00 | 2019-06-01T00:00:00
  - 同じ表の列：Parent Contract ID, Contract ID, Publish Date, Start Date, End Date, Value, Amendment Date, Amendments Value

## g0438（1 列）
- 見出し：Amendments Value
- 例1 値：526035.4 | 669279.36 | 640512.61 | 1488703 | 169200.35
  - 同じ表の列：Parent Contract ID, Contract ID, Publish Date, Start Date, End Date, Value, Amendment Date, Amendment Start Date

## g0439（1 列）
- 見出し：Agency Ref ID
- 例1 値：4500000026.0 | POC00936 | GCRN946629 | 4500000324.0 | 42002976.0
  - 同じ表の列：Parent Contract ID, Contract ID, Publish Date, Start Date, End Date, Value, Amendment Date, Amendment Start Date

## g0440（1 列）
- 見出し：Category/nature of fraud
- 例1 値：Missing funds/property | Maladministration / Misconduct | Missing funds/property | Maladministration / Misconduct | Missing funds/property
  - 同じ表の列：Financial Year, Quantity

## g0441（2 列）
- 見出し：Financial Year
- 例1 値：2016-17 | 2017-18 | 2014-15 | 2015-16 | 2014-15
  - 同じ表の列：Category/nature of …, Quantity
- 例2 値：2017-18 | 2024-25 | 2020-21 | 2022-23 | 2015-16
  - 同じ表の列：Threshold amount ($)

## g0442（1 列）
- 見出し：Quantity
- 例1 値：1 | 2 | 1 | 0 | 4
  - 同じ表の列：Category/nature of …, Financial Year

## g0443（1 列）
- 見出し：Contractor
- 例1 値：Adrian Gardiner Electrical Pty Ltd | Curtin University Of Western Australia | Private Contractor | Dept. Of Economic Development | Micron Shearing Pty Ltd
  - 同じ表の列：Purpose, Value

## g0444（1 列）
- 見出し：Purpose
- 例1 値：PIRSA site maintenance | Seed research (various projects) | Code of Practice development (Lucerne) | ICT Application development | De-suckering vineyard Nuriootpa researc…
  - 同じ表の列：Contractor, Value

## g0445（1 列）
- 見出し：Value
- 例1 値：$16,579 | $12,980 | $12,582 | $13,239 | $31,504
  - 同じ表の列：Contractor, Purpose

## g0446（1 列）
- 見出し：Publication
- 例1 値：Income support customers: a statistical… | Income support customers: a statistical… | Income support customers: a statistical… | Income support customers: a statistical… | Income support customers: a statistical…
  - 同じ表の列：Table, Extract, Payment, Payment_Type, Source, Theme_1, Measure_1, Theme_2

## g0447（1 列）
- 見出し：Table
- 例1 値：Table 7: Disability Support Pension cus… | Table 1: Summary of income support reci… | Table 1: Summary of income support reci… | Table 19: Carer Payment customers by st… | Table 20: Carer Allowance customers by …
  - 同じ表の列：Publication, Extract, Payment, Payment_Type, Source, Theme_1, Measure_1, Theme_2

## g0448（1 列）
- 見出し：Extract
- 例1 値：FY 2010 | FY 2010 | FY 2010 | FY 2010 | FY 2010
  - 同じ表の列：Publication, Table, Payment, Payment_Type, Source, Theme_1, Measure_1, Theme_2

## g0449（1 列）
- 見出し：Payment
- 例1 値：Wife Pension | Carer Payment | All | Disability Support Pension | Age Pension
  - 同じ表の列：Publication, Table, Extract, Payment_Type, Source, Theme_1, Measure_1, Theme_2

## g0450（1 列）
- 見出し：Payment_Type
- 例1 値：All | Supplementary Payment | Income Support Payment | Supplementary Payment | Supplementary Payment
  - 同じ表の列：Publication, Table, Extract, Payment, Source, Theme_1, Measure_1, Theme_2

## g0451（1 列）
- 見出し：Source
- 例1 値：Centrelink administrative data (Departm… | Centrelink and DVA administrative data | Centrelink and DVA administrative data | Centrelink administrative data | Centrelink administrative data
  - 同じ表の列：Publication, Table, Extract, Payment, Payment_Type, Theme_1, Measure_1, Theme_2

## g0452（1 列）
- 見出し：Theme_1
- 例1 値：As at June | As at June | Age (years) | Duration | Payment status Current-automatically as…
  - 同じ表の列：Publication, Table, Extract, Payment, Payment_Type, Source, Measure_1, Theme_2

## g0453（1 列）
- 見出し：Measure_1
- 例1 値：Lebanon | 2008 | Other | 2004 | Queensland
  - 同じ表の列：Publication, Table, Extract, Payment, Payment_Type, Source, Theme_1, Theme_2

## g0454（1 列）
- 見出し：Theme_2
- 例1 値：Adult | Male | Payment Type | Payment Type | Female
  - 同じ表の列：Publication, Table, Extract, Payment, Payment_Type, Source, Theme_1, Measure_1

## g0455（1 列）
- 見出し：Measure_2
- 例1 値：No. | No. | No. | Age Pension (incl. Dept of Veterans’ Af… | No.
  - 同じ表の列：Publication, Table, Extract, Payment, Payment_Type, Source, Theme_1, Measure_1

## g0456（1 列）
- 見出し：Business_Date
- 例1 値：2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01
  - 同じ表の列：Day_of_Week, Day_Type, Mode, Train_Number, Group, Direction, Origin_Station, Destination_Station

## g0457（1 列）
- 見出し：Day_of_Week
- 例1 値：Monday | Monday | Monday | Monday | Monday
  - 同じ表の列：Business_Date, Day_Type, Mode, Train_Number, Group, Direction, Origin_Station, Destination_Station

## g0458（1 列）
- 見出し：Day_Type
- 例1 値：School Holiday | School Holiday | School Holiday | School Holiday | School Holiday
  - 同じ表の列：Business_Date, Day_of_Week, Mode, Train_Number, Group, Direction, Origin_Station, Destination_Station

## g0459（1 列）
- 見出し：Mode
- 例1 値：Metro Trains | Metro Trains | Metro Trains | Metro Trains | Metro Trains
  - 同じ表の列：Business_Date, Day_of_Week, Day_Type, Train_Number, Group, Direction, Origin_Station, Destination_Station

## g0460（1 列）
- 見出し：Train_Number
- 例1 値：1675 | 3208 | 4409 | 5865 | C431
  - 同じ表の列：Business_Date, Day_of_Week, Day_Type, Mode, Group, Direction, Origin_Station, Destination_Station

## g0461（1 列）
- 見出し：Group
- 例1 値：Hurstbridge-Montmorency | Mernda-Rushall | Hurstbridge-Montmorency | Mernda-Rushall | Alamein-Riversdale
  - 同じ表の列：Business_Date, Day_of_Week, Day_Type, Mode, Train_Number, Direction, Origin_Station, Destination_Station

## g0462（1 列）
- 見出し：Direction
- 例1 値：D | D | U | D | D
  - 同じ表の列：Business_Date, Day_of_Week, Day_Type, Mode, Train_Number, Group, Origin_Station, Destination_Station

## g0463（1 列）
- 見出し：Origin_Station
- 例1 値：Frankston | Laverton | Flinders Street | East Pakenham | Frankston
  - 同じ表の列：Business_Date, Day_of_Week, Day_Type, Mode, Train_Number, Group, Direction, Destination_Station

## g0464（1 列）
- 見出し：Destination_Station
- 例1 値：Glen Waverley | Flinders Street | Flinders Street | Flinders Street | Reservoir
  - 同じ表の列：Business_Date, Day_of_Week, Day_Type, Mode, Train_Number, Group, Direction, Origin_Station

## g0465（1 列）
- 見出し：Station_Chainage
- 例1 値：28510 | 4834 | 22816 | 11786 | 5413
  - 同じ表の列：Business_Date, Day_of_Week, Day_Type, Mode, Train_Number, Group, Direction, Origin_Station

## g0466（4 列）
- 見出し：Year
- 例1 値：1989-90 | 1989-90 | 1989-90 | 1989-90 | 1989-90
  - 同じ表の列：Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2
- 例2 値：2019-20 | 2017-18 | 2015-16 | 2023-24 | 2016-17
  - 同じ表の列：Consultants, Purpose, Value

## g0467（2 列）
- 見出し：Trade type
- 例1 値：Total Exports | Total Exports | Total Exports | Total Exports | Total Exports
  - 同じ表の列：Year, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2
- 例2 値：Total Imports | Total Imports | Total Imports | Total Imports | Total Imports
  - 同じ表の列：Year, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2

## g0468（2 列）
- 見出し：TRIEC 1 digit
- 例1 値：1 Primary Products | 1 Primary Products | 1 Primary Products | 1 Primary Products | 1 Primary Products
  - 同じ表の列：Year, Trade type, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2
- 例2 値：1 Primary Products | 1 Primary Products | 1 Primary Products | 1 Primary Products | 1 Primary Products
  - 同じ表の列：Year, Trade type, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2

## g0469（2 列）
- 見出し：TRIEC 2 digit
- 例1 値：11 Primary products - Unprocessed | 11 Primary products - Unprocessed | 11 Primary products - Unprocessed | 11 Primary products - Unprocessed | 12 Primary products - Processed
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2
- 例2 値：11 Primary products - Unprocessed | 12 Primary products - Processed | 11 Primary products - Unprocessed | 12 Primary products - Processed | 12 Primary products - Processed
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2

## g0470（2 列）
- 見出し：TRIEC 3 digit
- 例1 値：111 Primary products - Unprocessed - Fo… | 114 Primary products - Unprocessed - Ot… | 111 Primary products - Unprocessed - Fo… | 121 Primary products - Processed - Food | 112 Primary products - Unprocessed - Mi…
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2
- 例2 値：121 Primary products - Processed - Food | 111 Primary products - Unprocessed - Fo… | 113 Primary products - Unprocessed - Fu… | 122 Primary products - Processed - Mine… | 121 Primary products - Processed - Food
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 4 digit, Partner Country, Geographic level 1, Geographic level 2

## g0471（1 列）
- 見出し：TRIEC 4 digit
- 例1 値：1131 Coal anthracite & bituminous | 1119 Unprocessed food nes | 1121 Iron ore & concentrates | 1113 Vegetables fruit & nuts fresh chil… | 1213 Dairy products processed
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, Partner Country, Geographic level 1, Geographic level 2

## g0472（1 列）
- 見出し：Partner Country
- 例1 値：Japan | Samoa | Fiji | Unidentified | Guam
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Geographic level 1, Geographic level 2

## g0473（1 列）
- 見出し：Geographic level 1
- 例1 値：Africa | Oceania & Antarctica | Asia | Africa | Asia
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 2

## g0474（1 列）
- 見出し：Geographic level 2
- 例1 値：Caribbean | Latin America | Middle East | Northern & Western Europe | Northern & Western Europe
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0475（1 列）
- 見出し：Geographic level 3
- 例1 値：Other Pacific Islands | Other Pacific Islands | Northern Europe | Western Europe | Southern Asia
  - 同じ表の列：Year, Trade type, TRIEC 1 digit, TRIEC 2 digit, TRIEC 3 digit, TRIEC 4 digit, Partner Country, Geographic level 1

## g0476（8 列）
- 見出し：Suburb
- 例1 値：Carlton | Ringwood | Doveton | Broadmeadows | Box Hill
  - 同じ表の列：State, Business Category, LGA, Region
- 例2 値：ALTONA NORTH | WILLIAMSTOWN | WILLIAMSTOWN | ALTONA NORTH | NEWPORT
  - 同じ表の列：Location, Numberof, BicycleRackMaterial

## g0477（2 列）
- 見出し：Business Category
- 例1 値：Swimming Pool | Swimming Club | State body,Swimming Club | Swimming Club | Fitness centre,Swimming Pool
  - 同じ表の列：Suburb, State, LGA, Region
- 例2 値：Martial Arts,State body | State body | State body | State body | State body
  - 同じ表の列：Suburb, State, LGA, Region

## g0478（1 列）
- 見出し：LGA
- 例1 値：Frankston (C) | Greater Geelong | Wyndham,Melton,Brimbank | Frankston (C); Casey (C) | Moonee Valley (C)
  - 同じ表の列：Suburb, State, Business Category, Region

## g0479（1 列）
- 見出し：Region
- 例1 値：North and West Metropolitan Region | North and West Metropolitan Region | Barwon S/W | North and West Metropolitan Region | Eastern Metro
  - 同じ表の列：Suburb, State, Business Category, LGA

## g0480（1 列）
- 見出し：Timestamp
- 例1 値：2023-08-16 20:30:00 | 2023-08-16 05:00:00 | 2023-08-07 08:30:00 | 2023-08-19 22:00:00 | 2023-08-08 05:30:00
  - 同じ表の列：Record number, Average Water Speed, Average Water Direc…, Chlorophyll, Chlorophyll [qualit…, Temperature, Temperature [qualit…, Dissolved Oxygen

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
