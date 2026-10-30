# 近い教材の列の見直し（誤った列ごとに、誤りを教えた近い教材の列を上位 3 列）

形式：正解→本体の答え｜誤った列｜その値 ／ 教材の列（出どころ・付けた種類・近さ）


## account→category

- R001 b060-1052「IncomeType」: On-Street Pay and  / Off-Street Pay and / Penalty Charge Not / Parking Permits / Other - Rents
    - b「IncomeType」category 1.00: On-Street Pay and  / Other - Rents / Penalty Charge Not / Parking Permits
    - b2「Merchant Category」category 0.98: Home Supply Wareho / Hardware Equipment / Heating, Plumbing, / Tax Payments
    - b「DETAILS」category 0.98: GOVERNMENT CAR SER / PRINTING AND BINDI / HOTEL ACCOMMODATIO / TRAINING COURSE FE
- R002 b062-0260「PESA Economic Group Code」: NET PUBLIC SERVICE / OTHER RESOURCE / OTHER RESOURCE / NET PUBLIC SERVICE / PURCHASE OF GOODS 
    - b007「区分」category 0.96: うち一般歳出 / 歳入 / うち都税 / 歳出
    - b006「SUBACAO」category 0.95: 001 - EXECUÇÃO DA  / 001 - EXECUÇÃO DA  / 001 - EXECUÇÃO DA  / 001 - EXECUÇÃO DA 
    - b007「区分」category 0.94: 補償、補填及び賠償金 / 公有財産購入費 / 交際費 / 負担金補助及び交付金
- R003 b062-0319「Proclass Category」: Housing Management / Social Community C / Social Community C / REDACTED / Social Community C
    - b2「ProcurementClassification:ProclassLabel」category 0.98: Public Transport / Public Transport / Passenger Transpor / Sundries
    - b006「Revenue Category」category 0.98: Departmental / State Aid / Licenses & Permits / Departmental
    - b2「Service Category Label」category 0.98: Childrens & Educat / Central Services t / Childrens & Educat / Childrens & Educat
- R004 b060-0658「Type」: Equipment / Equipment / Equipment / Travel and subsist / Print and publishi
    - b「type」category 0.98: Regional Developme / School upgrades / Admitted Services / Training, Higher E
    - b「DETAILS」category 0.97: GOVERNMENT CAR SER / PRINTING AND BINDI / HOTEL ACCOMMODATIO / TRAINING COURSE FE
    - b008「anzsic_class」category 0.97: Paint and Coatings / Computer System De / Freight Forwarding / Furniture and Floo
- R005 b017-0331「originating_sector_en」: IAB / Procurement / SPB / ISB / PB
    - b009「Cluster」category 0.97: Finance and Servic / Councils / Family and Communi / Councils
    - b「ANZSIC Division Name」category 0.96: Other Services / Transport Postal A / Construction / Accommodation And 
    - b2「Service Category Label」category 0.96: Childrens & Educat / Central Services t / Childrens & Educat / Childrens & Educat
- R006 b055-0002「区分レベル１」: 70 / 01_資産の部 / 02_負債の部 / 75 / 02_負債の部
    - b006「SUBACAO」category 0.98: 001 - EXECUÇÃO DA  / 001 - EXECUÇÃO DA  / 001 - EXECUÇÃO DA  / 001 - EXECUÇÃO DA 
    - b006「CATEGORIA_ECONOMICA」category 0.97: 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre
    - b「Classification」category 0.97: 271430 - Informati / 271430 - Informati / 121000 - Cemetery  / 240000 - Horticult
- R007 b055-0003「区分レベル２」: 04_固定負債 / 01_資産の部 / 03_流動負債 / 01_資産の部 / 01_流動資産
    - b006「CATEGORIA_ECONOMICA」category 0.99: 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre
    - b007「DESC_CATEGORIA」category 0.98: UNIDADE DE ACOLHIM / SERVICO DE CONVIVE / SERVICO DE CONVIVE / UNIDADE DE ACOLHIM
    - b011「Category - FR」category 0.98: Biens, terrains, b / Services / Services / Biens, terrains, b
- R008 b055-0004「区分レベル３」: 12_インフラ資産 / 10_普通財産 / 02_固定資産 / 23_未払金 / 10_普通財産
    - b006「CATEGORIA_ECONOMICA」category 0.98: 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre
    - b006「CATEGORIA_ECONOMICA」category 0.98: 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre
    - syn「class」category 0.98: 返品 / 売上 / 出金 / 通常
- R009 b055-0005「区分レベル４」: 12_有形固定資産（普通財産） / 15_有形固定資産（インフラ） / 12_有形固定資産（普通財産） / 21_有価証券及出資金 / 53_端数調整
    - b006「CATEGORIA_ECONOMICA」category 0.98: 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre
    - b006「CATEGORIA_ECONOMICA」category 0.98: 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre / 3 - Despesas Corre
    - syn「class」category 0.98: 返品 / 売上 / 出金 / 通常
- R010 b055-0006「区分レベル５」: 01_現金預金 / 16_無形固定資産（インフラ） / 12_立木（行政財産） / 48_貸倒引当金 / 36_地上権（インフラ）
    - b2「ProcurementClassification:ProclassLabel」category 0.97: Public Transport / Public Transport / Passenger Transpor / Sundries
    - b006「Revenue Category」category 0.97: Departmental / State Aid / Licenses & Permits / Departmental
    - b2「Service Category Label」category 0.97: Childrens & Educat / Central Services t / Childrens & Educat / Childrens & Educat

## account→text

- R011 b060-0543「Details」: Air Travel / Training Course Fe / Air Travel / Training Course Fe / Corporate subs and
    - b002「Transfer Purpose」text 0.94: FUNDING FOR INFORM / DIRECT AND INDIREC / FUNDING PROVIDED F / SOCIAL SERVICES BL
    - b006「Objeto」text 0.94: Prestação de servi / Registro de preços / Registro de Preços / Alienação de imóve
    - b013「Staff Training」text 0.92: Temporary Staff / Work from home tri / ICT software secur / Temporary Staff
- R012 b064-0164「e」: Inheritance and gi / Revenue shares for / Transportation and / Old age and surviv / Extraordinary expe
    - b「Description of Goods (Purpose of expendi」text 0.91: Capital Expenditur / Furniture and Equi / Professional Fees / Professional Fees
    - b013「Purpose」text 0.90: Common User Facili / Common User Facili / Common User Facili / Survey Services
    - b「description_entente」text 0.89: VETR,A,FOURNITURE  / SPAG,Z,PRESTATION  / ENPC,Z,Fourniture  / INEL,Z,ACQUISITION

## address→category

- R013 b022-0014「Floor ID」: GROUND FLOOR / GROUND FLOOR / BASEMENT 1 / BASEMENT 1 / LEVEL 1
    - b013「ID」category 0.97: Regional Road Obje / National Road Obje / Leinster Outer Orb / National Road Obje
    - b012「SITC 3 digit」category 0.97: 012 Meat (excl bee / 012 Meat (excl bee / 024 Cheese & curd / 037 Seafood, prepa
    - b011「Zone」category 0.97: RH / R / RCE / Con
- R014 b036-0141「Location」: Grounds / Grounds / Roundabout / Park / Grounds
    - b003「提供エリア」category 0.96: 施設建物内 / 施設建物内 / 施設建物内 / 施設建物内
    - b003「提供エリア」category 0.96: 施設内 / 施設内 / 施設内 / 施設内
    - b006「提供エリア」category 0.96: 館内の一部のエリア / 館内の一部のエリア / 館内の一部のエリア / 館内の一部のエリア
- R015 b017-0057「QUALCOU」: COM / RWA / BFA / TUV / KNA
    - b008「UNIT」category 0.96: AAU / AAU / AAU / AAU
    - b006「veteran_cert」category 0.96: SVOB / SVOB / SVOB, SDVOB / SVOB, SDVOB
    - b006「forma_doenca」category 0.96: SG / SRAG / SG / SG
- R016 b017-0286「Site」: Grizzly / Grizzly / Grizzly / Grizzly / Grizzly
    - b013「dev_site」category 0.91: Gateways - SHRCC / Gateways - SHRCC / Gateways - SHRCC / Gateways - SHRCC
    - b003「ST_TYPE」category 0.91: Inlet / Inlet / Inlet / Inlet
    - b013「dev_site」category 0.89: Weather Stations - / Weather Stations - / Weather Stations - / Weather Stations -
- R017 b064-0356「designation」: Halte d'Albeuve / Hauptzugang / Haupteingang / Point de référence / Hauptzugang
    - b「Designation-fr」category 0.97: District / Comté / Ville / Ville
    - b「Designation-fr」category 0.95: Village / District / Territoire non org / Ville
    - b011「Function/Category」category 0.95: Recreation Parklan / Recreation Parklan / Not Applicable / Not Applicable
- R018 b064-0004「georegion」: CHFL / CHFL / CHFL / CHFL / CHFL
    - b「Jurisdiction」category 0.94: FEDERAL / FEDERAL / FEDERAL / FEDERAL
    - b010「ROAD_EDGE_TYPE」category 0.92: GCCC TYPE D / GCCC TYPE J / GCCC TYPE D / GCCC TYPE D
    - b011「Region@」category 0.92: Non-metro / Metro / Metro / Non-metro
- R019 b064-0014「georegion」: CHFL / CHFL / CHFL / CHFL / CHFL
    - b「Jurisdiction」category 0.95: FEDERAL / FEDERAL / FEDERAL / FEDERAL
    - b011「Region@」category 0.92: Non-metro / Metro / Metro / Non-metro
    - b010「ROAD_EDGE_TYPE」category 0.92: GCCC TYPE D / GCCC TYPE J / GCCC TYPE D / GCCC TYPE D
- R020 b064-0225「lage_auf_dem_stockwerk」: links / links / links / rechts / links
    - b008「Water Condition」category 0.99: Medium Flow / Medium Flow / Medium Flow / Low Flow
    - b006「height_field_unit」category 0.98: in / in / in / in
    - b「Shell_hardness_Duret饑de_la_carapace」category 0.98: hard / hard / hard / hard
- R021 b064-0325「richtung」: nach Kreuzlingen / nach Schaffhausen / nach Lengwil / nach Amlikon / nach Steinach
    - b013「Route」category 0.93: Adelaide - Canberr / Brisbane - Darwin / Coffs Harbour - Sy / Melbourne - Mildur
    - b008「Topography」category 0.88: Flat / Flat with slight r / Flat / Flat with one smal
    - g「Namespace」category 0.86: Debug / Debug / Debug / Debug
- R022 b064-0224「stockwerk_bezeichnung」: 5. Stock / 3. Stock / Parterre inkl. Hoc / 2. Stock / 4. Stock
    - b010「Club_Venue_Sports」category 0.93: Athletics / Tennis / Australian Rules / Tennis
    - b014「Intended_Destination」category 0.90: Transfer to Non-Go / Transfer to SA Gov / unknown / Interstate/Oversea
    - b006「提供エリア」category 0.90: 館内の一部のエリア / 館内の一部のエリア / 館内の一部のエリア / 館内の一部のエリア

## address→id

- R023 b063-0206「GEO」: CH023 / CH054 / CH051 / CH013 / CH012
    - b006「mtfcc20」id 0.98: G5020 / G5020 / G5020 / G5020
    - b2「STATISTIC」id 0.98: HS180 / HS180 / HS180 / HS180
    - b010「LOG_TYPE」id 0.98: SQ03 / SQ03 / SQ03 / SQ03
- R024 b064-0251「PLZ」: 4057 / 4053 / 4057 / 4051 / 4053
    - b004「KEY_CODE」id 0.98: 28206 / 28220 / 28207 / 28586
    - b007「KEY_CODE」id 0.98: 434430060 / 434430180 / 434430070 / 434430160
    - b007「KEY_CODE」id 0.98: 434470950 / 434470020 / 434470150 / 434470140
- R025 b064-0222「administrative_wohnungsnummer」: W13 / 1052 / A1802g / 502 / 503
    - syn「officeNumber」id 0.99: #7795 / #2870 / #7851 / #4241
    - syn「officeNumber」id 0.99: A16997 / A95702 / A55510 / 
    - b005「町字ID」id 0.98: 253 / 42 / 832 / 847
- R026 b064-0274「betrieb_plz」: 7250 / 7504 / 7260 / 7270 / 7270
    - b004「SUBDIVISION ID」id 0.98: 590 / 1336 / 2503 / 13106
    - b007「ID_ROTA_CICLOVIARIA」id 0.98: 14825 / 11292 / 13286 / 14365
    - b003「SUBDIVISION ID」id 0.98: 1217 / 2437 / 2849 / 648
- R027 b063-0355「eingangsnummer_gebaeude」: 31 / 191 / 9 / 12 / 4
    - b005「行政区番号」id 0.99: 10 / 12 / 9 / 16
    - b010「基準地番号（連番）」id 0.99: 5 / 6 / 9 / 3
    - b004「NO」id 0.99: 4 / 5 / 1 / 7
- R028 b064-0221「eingangsnummer_gebaeude」: 93 / 1 / 99 / 42 / 4
    - b010「OBJECTID」id 0.99: 69 / 19 / 88 / 49
    - b009「OBJECTID」id 0.99: 58 / 108 / 1 / 29
    - b011「OBJECTID」id 0.99: 30 / 9 / 90 / 102
- R029 b063-0331「haus_nr」: 9 / 9 / 17 / 12 / 9
    - b008「Station No.」id 0.99: 35 / 6 / 27 / 19
    - b005「NO」id 0.99: 4 / 12 / 19 / 1
    - b005「町字ID」id 0.99: 253 / 42 / 832 / 847
- R030 b063-0330「plz」: 8245 / 8180 / 8001 / 8180 / 8002
    - g「Medcode」id 0.95: 812.0 / 10531.0 / 93526.0 / 6238.0
    - b006「SUBBACIA」id 0.95: 4111105 / 4140007 / 4140803 / 4130001
    - syn「ロット番号」id 0.95: 42687946 / 31638937 / 94217673 / 79630738
- R031 b063-0462「plz」: 9322 / 8590 / 9320 / 9320 / 9320
    - b013「sa2_5digitcode_2016」id 0.98: 11584 / 11521 / 21358 / 21457
    - b009「4-digit ANZSCO code」id 0.98: 5999 / 4115 / 5619 / 1413
    - b007「ID_ROTA_CICLOVIARIA」id 0.98: 14825 / 11292 / 13286 / 14365
- R032 b064-0184「plz」: 
    - b「Uadm Requerant」id 0.94: 4907 / 4204 / 4905 / 4204
    - b006「receita」id 0.91: 11125007 / 11130341 / 16110103 / 11220105
    - b010「AHRI」id 0.91: 210448841 / 8849330 / 215864380 / 0

## address→org

- R033 b017-0230「FSA」: A2N / A1K / V6Y / V9R / T3C
    - b005「名称_カナ」org 0.94: キノカワシヤクショ ホンチョウシャ / コカワダイ５ブンダンダイ３ブショウボ / モモヤマダイ３ブンダンダイ１５ブショ / ナガタショウガッコウ
    - b010「CRAS」org 0.93: CRAS VILA SENHOR D / CRAS VILA BIQUINHA / CRAS APOLONIA / CRAS LAGOA
    - b007「名称かな表記」org 0.93: てんすいこそだてほっとるーむ / たまなしたいめいこそだてしえんせんた / たまっこらんど / るーてるきっずひろば
- R034 b065-0221「Local Authority」: Manchester / Bolton / Bolton / Manchester / Bolton
    - b011「Local Authority」org 0.98: Sligo (County Coun / Cavan (County Coun / Clare (County Coun / Roscommon (County 
    - b006「団体名」org 0.98: 阪南市 / 学校法人いづみ学園 / 社会福祉法人 阪南福祉会 / 阪南市
    - b006「団体名」org 0.98: 公益社団法人沖縄県精神保健福祉会連合 / 沖縄市 / 沖縄市 / 社会福祉法人大信福祉会
- R035 b065-0123「Second Tier Authority」: Redcar and Clevela / Middlesbrough / Middlesbrough / Middlesbrough / Redcar and Clevela
    - b2「Health Service Executive Area」org 0.97: HSE-Dublin/Mid-Lei / HSE-Dublin/North-E / HSE-Dublin/North-E / HSE-West
    - b007「運営主体」org 0.97: ヘアールームRAGU / (福)敬愛福祉会 / (福)光徳寺福祉会 / 玉名市
    - b005「建物名称」org 0.96: 田篭コミュニティセンター / 吉井コミュニティセンター（吉井白壁会 / 千年コミュニティセンター / 小塩コミュニティセンター (小塩ほた
- R036 b055-0293「名称」: 学田公園野球場 / 三原台温水プール / びくに公園庭球場・多目的広場 / 中村南スポーツ交流センター / 光が丘体育館
    - b008「名称_通称」org 0.99: 杉十小温水プール / 松ノ木運動場 / 和田堀公園プール / 高円寺みんなの体育館
    - b012「名称」org 0.99: 押立庭球場 / 寿町庭球場 / 押立体育館 / 栄町体育館
    - b008「名称」org 0.99: 笹塚高架下施設 / 代々木西原公園庭球場 / 二子玉川区民運動施設 / 猿楽トレーニングジム

## address→other

- R037 b017-0168「Prov/Terr」: 
    - b011「Station_Chainage」other 0.82: 28510 / 4834 / 22816 / 11786
    - g「oldalSzam」other 0.79: 26 / 196 / 158 / 186
    - b009「area」other 0.78: 1.02 / 0.28 / 2.17 / 10.22

## address→text

- R038 b035-0010「profile」: Southbank (high ri / Carlton (high rise / Parkville (high ri / Melbourne (CBD) (h / Carlton (high rise
    - b007「都 市 概 要」text 0.92: 韓国の最北端、ソウル特別市の北西約3 / オーストラリアのニューサウスウェール / 大分県南西部の九重連峰の北部に位置す / 中国遼寧省の省都で、面積は12,86
    - b004「アクセス方法」text 0.91: 大溝小学校敷地内 / 木佐木小学校敷地内 / 大莞小学校敷地内
    - b「Location」text 0.90: Car Park / Across from Roe Ph / At Bus Stop / Touring Site Car P

## amount→id

- R039 b063-0276「Beschluss」: 
    - b「Projet Investi」id 0.92: 55862 / 60110 / 71350 / 68272
    - b「Uadm Requerant」id 0.84: 4907 / 4204 / 4905 / 4204
    - b008「ICN」id 0.80: 260 / 801 / 140 / 648

## amount→quantity

- R040 b063-0275「Nachgefragt」: 
    - b013「Family income between $15,000 - $19,999 」quantity 0.93: 4270 / 50890 / 14310 / 5650
    - b013「Carer Allowance」quantity 0.93: 3210 / 4675 / 3225 / 4610
    - b006「ParentLabFor」quantity 0.91: 1,419 / 30,445 / 2,768 / 894

## category→account

- R041 b063-0579「Aufgabengebiet (de)」: Soziale Wohlfahrt / Institutionelle un / Institutionelle un / Institutionelle un / Institutionelle un
    - b「Pro Class Description」account 0.96: Education Library  / Works - Constructi / Human Resources Tr / Human Resources Tr
    - b008「区分２」account 0.96: 公営企業貸付金元利収 / 繰入金 / 災害復旧事業費支出金 / 災害復旧事業費支出金
    - b007「項目」account 0.96: 消防費 / 消防費 / 消防費 / 消防費
- R042 b026-0003「Core Responsibility」: Future Force Desig / Defence Team / Operations / Procurement of Cap / Defence Team
    - b2「Purpose」account 0.95: Furniture for offi / Heritage Open Days / Core service suppo / Safety Surface in 
    - b「Purpose」account 0.95: Grants / Services - credit  / Services - Profess / Roof Repairs
    - syn「プロジェクト」account 0.95: 水道光熱費 /  /  / 営業部
- R043 b026-0009「Core Responsibility」: Operations / Defence Team / Ready Forces / Defence Team / Operations
    - b「Payment Description」account 0.96: Rent buildings - n / Equipment support  / Medical health ser / Utilities consumed
    - b2「Purpose」account 0.96: TPP - Major Extern / Tree Work / Building Works / Services - Fees an
    - b「Service Description (F)」account 0.96: EFM Materials / Funded Grounds Mtn / Capital
- R044 b060-0757「Inspection or regulatory remit」: Maintained schools / Early years and ch / Maintained schools / Early years and ch / Early years and ch
    - b2「SERVICE_RESPONSABLE」account 0.96: Grands parcs / Grands parcs / Grands parcs / Habitation
    - b012「項目２」account 0.93: 賃借料等 / 旅費関係 / 賃借料等 / 旅費関係
    - b「Pro Class Description」account 0.93: Consultancy / Human Resources Tr / Information Commun / Information Commun
- R045 b063-0187「Kostenart」: Immaterielle Koste / Immaterielle Koste / Immaterielle Koste / Immaterielle Koste / Wiederbesetzungsko
    - b013「Expense type」account 0.97: Administered Expen / Administered Expen / Departmental Expen / Administered Expen
    - b002「Category」account 0.97: Other Ordinary Mai / Salaries and Wages / Salaries and Wages / Other Ordinary Mai
    - b008「区分２」account 0.97: 公営企業貸付金元利収 / 繰入金 / 災害復旧事業費支出金 / 災害復旧事業費支出金
- R046 b063-0185「Kostenbereich」: Gesundheit Luft / Gebäude Luft / Gesundheit Luft / Ernteausfälle Luft / Gesundheit Luft
    - b002「Category」account 0.98: Other Ordinary Mai / Salaries and Wages / Salaries and Wages / Other Ordinary Mai
    - syn「部門」account 0.98: 買掛金 / 消耗品費 / 現金 / Sales
    - b2「MerchantCategory」account 0.98: Residential Care / Boarding Out Fees / Residential Care / Residential Care
- R047 b026-0004「Program」: Ombudsman / Ready Air and Spac / Ready Naval Forces / Defence Materiel M / Naval Bases
    - b「Pro Class Description」account 0.95: Consultancy / Human Resources Tr / Information Commun / Information Commun
    - b2「desc_」account 0.95: Commercial Waste W / Recreation/Amenity / Domestic Waste Wat / Domestic Refuse Ch
    - b011「Subcategory - EN」account 0.95: Acquisition of mac / Professional and s / Materials and supp / Acquisition of mac
- R048 b017-0312「Service」: Data Centre Facili / Data Centre Facili / Data Centre Facili / Data Centre Facili / Data Centre Facili
    - b2「SERVICE_RESPONSABLE」account 0.92: Grands parcs / Grands parcs / Grands parcs / Habitation
    - b「Purpose」account 0.91: POSTAGE / ALCOHOL & DRUGS / PRINTING / GAS
    - b「Description of Goods (Purpose of expendi」account 0.90: Care Payments / Fees and Charges / Fees and Charges / Information and Co
- R049 b062-0431「ServiceCategoryLabel」: Business rates acc / Business rates acc / Business rates acc / Business rates acc / Business rates acc
    - b「ProcurementClassification:ProclassLabel」account 0.98: Uniforms / Not Elsewhere Clas / Commercial / Commercial
    - b012「区分」account 0.97: 特別会計臨海基盤 / 公営企業計 / 公営企業市場 / 特別会計母子父子福祉
    - b005「会計名称」account 0.96: 介護保険特別会計（介護サービス事業勘 / 介護保険特別会計（介護サービス事業勘 / 介護保険特別会計（介護サービス事業勘 / 介護保険特別会計（介護サービス事業勘
- R050 b017-0296「Service_FR」: 
    - b「Type/Narrative of Supply (E)」account 0.87: Accommodation / Parking / Accommodation / Accommodation
    - b「Description」account 0.87: Living support gra / Non-Premises - cos / Provisions - Gener / Vehicle hire
    - b「Purpose」account 0.87: POSTAGE / ALCOHOL & DRUGS / PRINTING / GAS
- R051 b017-0178「Tax gap component」: 
    - b「ProcurementClassification:ProclassLabel」account 0.88: Uniforms / Not Elsewhere Clas / Commercial / Commercial
    - b013「tax_type_or_activity_area」account 0.86: Sheriff Enforcemen / Sheriff Enforcemen / Self-assessed Inco / Excise - Vehicle R
    - syn「［貸方セグメント］」account 0.86: 
- R052 b063-0186「Unterkostenbereich」: Reinigungskosten / Demenz / Atemwegserkrankung / Atemwegserkrankung / COPD
    - b007「項目」account 0.98: 消防費 / 消防費 / 消防費 / 消防費
    - b011「Subcategory - EN」account 0.97: Acquisition of mac / Professional and s / Materials and supp / Acquisition of mac
    - b009「Level_5」account 0.97: A.4 - Postal And T / - Grants-in-aid / - Grants To Health / - Childcare
- R053 b060-0186「policy_area」: Fisheries, Aquacul / Construction produ / Fisheries, Aquacul / Environment (Waste / Construction produ
    - b012「項目２」account 0.94: 賃借料等 / 旅費関係 / 賃借料等 / 旅費関係
    - b010「Asset Workgroup」account 0.94: Infrastructure Ope / Infrastructure Ope / Infrastructure Ope / Infrastructure Ope
    - b2「SERVICE_RESPONSABLE」account 0.94: Grands parcs / Grands parcs / Grands parcs / Habitation

## category→address

- R054 b065-0223「Is the site Brownfield, Greenfield or a 」: Brownfield / Brownfield / Brownfield / Greenfield / Brownfield
    - b014「Location」address 0.94: market place - shi / saleyards / public lighting / botanical gardens 
    - b003「市区町村名」address 0.92: 知名町 / 知名町 / 知名町 / 知名町
    - b012「Where do you live?」address 0.92: Outside Australia / Victoria, Metro / Victoria, Metro / Victoria, Metro
- R055 b065-0191「Region」: Middle East and No / Multilateral Agree / Multilateral Agree / Africa / Europe
    - b011「Region」address 0.99: North and West Met / North and West Met / Barwon S/W / North and West Met
    - b008「Region」address 0.99: Southern Metro / Eastern Metropolit / North and West Met / Southern Metro
    - b010「Region」address 0.99: North and West Met / Eastern Metropolit / North and West Met / North and West Met
- R056 b063-0495「designation」: 
    - b014「Park」address 0.86: GNP / GNP / GNP / GNP
    - b013「property_type」address 0.86: Howgate house / Metropolitan Gas C / New Australian Ele / State School No. 1
    - b010「circuit」address 0.84: NA / Midland Circuit / NA / South Eastern Circ
- R057 b055-0040「地域」: 民間等（焼却施設） / 多摩地域（自治体焼却施設） / 多摩地域（自治体焼却施設） / 23区内（自治体焼却施設） / 23区内（自治体焼却施設）
    - b014「Location」address 0.94: market place - shi / saleyards / public lighting / botanical gardens 
    - b003「市区町村名」address 0.94: 知名町 / 知名町 / 知名町 / 知名町
    - b012「Where do you live?」address 0.94: Outside Australia / Victoria, Metro / Victoria, Metro / Victoria, Metro
- R058 b055-0014「都分類地区１」: 多摩 / 区部 / 区部 / 区部 / 区部
    - b014「Electoral Division」address 0.93: Division 10 / Division 1 / Division 1 / Division 1
    - b2「DIVISION」address 0.91: Omagh / Omagh / Omagh / Omagh
    - b009「Precinct」address 0.89: Sydney CBD Precinc / Sydney CBD Precinc / Sydney CBD Precinc / Sydney CBD Precinc
- R059 b055-0015「都分類地区２」: その他区 / その他区 / その他区 / その他区 / 都心５区
    - b009「地域名」address 0.98: H地区 / E地区 / A地区 / G地区
    - b013「Region」address 0.97: Eastern Metropolit / North and West Met / North and West Met / Southern Metropoli
    - b009「Region」address 0.97: North and West Met / North and West Met / Eastern Metropolit / North and West Met

## category→amount

- R060 b064-0178「finances」: 
    - syn「Unit Cost（必須）」amount 0.92: 30 / 10 / 30 / 0
    - b「Bonus Details」amount 0.88: 0 / 0 / 0 / 0
    - syn「」amount 0.86:  / 0 / 0 / 0

## category→id

- R061 b063-0207「AGE」: 
    - b「Tournée」id 0.82: 060 / 060 / 060 / 060
    - b012「中分類」id 0.80: 2 / 1 / 4 / 5
    - b007「CG」id 0.80: 7 / 8 / 7 / 8
- R062 b063-0213「AGE」: 
    - b006「地区割」id 0.78: 3 / 1 / 3 / 1
    - b012「中分類」id 0.77: 2 / 1 / 4 / 5
    - b「Tournée」id 0.77: 060 / 060 / 060 / 060
- R063 b062-0256「Control Budget Code」: 
    - b011「Economic Object Code」id 0.89: 1172 / 444 / 813 / 473
    - b2「Cost Centre」id 0.85: 10094 / 10086 / 10123 / 10098
    - syn「契約コード」id 0.85: 
- R064 b017-0065「MEASURE」: LICENSENURSE / LICENSENURSE / LICENSENURSE / LICENSENURSE / PRACNURSE
    - b014「MEASURE」id 0.99: LICENSEDEN / PRACDEN / LICENSEDEN / LICENSEDEN
    - b010「FISHERY_ID」id 0.99: FSQ / FSQ / FSQ / FSQ
    - b004「reason_id」id 0.99: 0 / 0 / 0 / 0
- R065 b065-0202「Type of Aid」: 
    - b2「SMOKE_CONT」id 0.98: C08 / C10 / C06 / G22
    - b013「Heading」id 0.97: 1 / 1 / 1 / 1
    - b012「Heading」id 0.97: 1 / 1 / 3 / 1
- R066 b063-0217「monitoring_program」: 
    - b009「Column」id 0.80: TRAN / TRAN / HER / NBCS
    - b009「TECHTYPE」id 0.79: GAMCAM / GAMCAM / GAMCAM / RTEQUIP
    - b013「FIELDSTUDY」id 0.77: PHARMA / PHARMA / NURSING / PHARMA

## category→org

- R067 b026-0033「developed_by_en」: Vendor / Government of Cana / Government of Cana / Government of Cana / Open source
    - b2「Operator」org 0.96: CityEV / CityEV / CityEV / CityEV
    - b010「届出先」org 0.95: [sanitize] / 経済産業省 / [sanitize] / 特定行政庁
    - b008「Airline」org 0.94: All Airlines / QantasLink / QantasLink / Virgin Australia
- R068 b026-0034「developed_by_fr」: Gouvernement du Ca / Gouvernement du Ca / Gouvernement du Ca / Fournisseur / Gouvernement du Ca
    - b006「Contractor」org 0.98: Maverick Construct / National Grid / National Grid / National Grid
    - b006「developer」org 0.98: City of Boston / Mass General Hospi / The Community Buil / Boston Communities
    - b009「publisher」org 0.98: Faith Communities  / Faith Communities  / Faith Communities  / Faith Communities 
- R069 b063-0162「parameter_group_it」: Pollini / Pollini / Pollini / Pollini / Pollini
    - syn「ブランド」org 0.85: 
    - syn「ブランド」org 0.85: 
    - syn「Brand2」org 0.85: 丸山銀行 / 工業さくら / 中央銀行 / 工業ミナト

## category→other

- R070 b016-0054「5」: 
    - g「ブロモホルム」other 0.89: 小3位 / 2 / 0 / 0
    - b014「Species/user types」other 0.88: Empty / Empty / Empty / Empty
    - b2「科名」other 0.88: シノブゴケ科 / ナガハシゴケ科 / ヤスデゴケ科 / ヒムロゴケ科
- R071 b017-0255「Family_Famille」: 
    - b2「目名」other 0.91: キセルゴケ目 / ホンマゴケ目 / ホンマゴケ目 / ホウオウゴケ目
    - b2「科名」other 0.91: シノブゴケ科 / ナガハシゴケ科 / ヤスデゴケ科 / ヒムロゴケ科
    - b009「Species_Desc」other 0.89: Sorbus aucuparia / Fraxinus excelsior / Tilia cordata 'Gre / Tilia cordata
- R072 b017-0347「Rank」: 
    - g「Abstract Rank」other 0.96: 44 / 21 / 3 / 2
    - g「dag-stage」other 0.91: 6 / 6 / 6 / 6
    - g「_status_」other 0.88: 0.0 / 0.0 / 0.0 / 0.0
- R073 b063-0714「digital_platform」: 
    - b2「ServicesFunctionCode」other 0.86: http://id.esd.org. / http://id.esd.org. / http://id.esd.org. / http://id.esd.org.
    - g「spotify_url」other 0.86: Not Found / spotify:track:2m3Z / spotify:track:3Ffx / Not Found
    - g「spotify_url」other 0.86: spotify:track:7kxs / spotify:track:1MTJ / spotify:track:6OW0 / Not Found
- R074 b064-0177「energy」: 
    - g「一般細菌」other 0.87: 0 / 0 / 0 / 0
    - g「大腸菌※」other 0.87: 0 / 0 / 0 / 0
    - g「臭気」other 0.86: 0 / 0 / 0 / 0
- R075 b016-0032「前5日間平均気温の品質情報」: 
    - g「臭気」other 0.96: 0 / 0 / 0 / 0
    - g「臭気」other 0.96: 0 / 0 / 0 / 0
    - g「CitesPerAuthor」other 0.95: 0 / 0 / 0 / 0

## category→product

- R076 b017-0144「Product」: Flavour Packet - D / Flavour Packet - D / Flavour Packet - D / Flavour Packet - D / Flavour Packet - D
    - b011「Product」product 0.98: Infant Formula - D / Infant Formula - D / Infant Formula - D / Infant Formula - D
    - b013「Product」product 0.96: Infant Formula - D / Cereal - Adult / Cereal - Adult / Infant Food - Cere
    - j「品目」product 0.96: ― / 青果物類 / 青果物類 / 一般食料品（酒を含む）
- R077 b017-0163「Product」: Bakery Product - B / Infant Formula - D / Bran - Wheat / Cereal - Children / Infant Food - Cere
    - b013「Product」product 0.98: Infant Formula - D / Cereal - Adult / Cereal - Adult / Infant Food - Cere
    - b013「Produit」product 0.98: Céréales - Enfants / Préparation pour n / Figue / Figue
    - b011「Product」product 0.97: Infant Formula - D / Infant Formula - D / Infant Formula - D / Infant Formula - D
- R078 b055-0202「回収可能品目」: 新聞、雑誌・雑がみ、段ボール、その他 / 新聞、雑誌・雑がみ、段ボール、その他 / 新聞、雑誌・雑がみ、段ボール / 新聞、雑誌・雑がみ、段ボール、その他 / 新聞、雑誌・雑がみ、段ボール、その他
    - b012「回収品目」product 0.99: 紙パック,食品トレイ（白色）,食品ト / 製品プラスチック※無印良品の製品のみ / 紙パック,食品トレイ（白色）,びん※ / ペットボトル,ペットボトルキャップ,
    - b011「ゴミの品目_英字」product 0.98: Soap solid/powder / Needles (sewing ne / Slatted wood / Artificial anus St
    - j「品目」product 0.98: ― / 青果物類 / 青果物類 / 一般食料品（酒を含む）

## category→quantity

- R079 b016-0058「9」: 
    - syn「」quantity 0.92: 3 / 12 / 1 / 2
    - syn「」quantity 0.92: 2 / 1 / 10 / 4
    - b006「NUM_UNID_ANDAMENTO」quantity 0.91: 0 / 0 / 0 / 0
- R080 b063-0199「Age」: 
    - b011「abstudy__living_allowance_」quantity 0.95: <20 / <20 / 31 / <20
    - g「EmployeeCount」quantity 0.94: 1 / 1 / 1 / 1
    - b2「Term-Deposit-Day-Count-Nombre-de-jour-du」quantity 0.94: 1 / 1 / 1 / 1
- R081 b064-0139「Age」: 
    - b011「abstudy__living_allowance_」quantity 0.95: <20 / <20 / 31 / <20
    - b2「Want to live in this parish & need 4+ be」quantity 0.93: 7 / 5 / 4 / 7
    - syn「」quantity 0.93: 2 / 2 / 1 / 5
- R082 b064-0174「crime」: 
    - b013「BBQ」quantity 0.95: 2 / 1 / 2 / 0
    - g「Comments」quantity 0.94: 0 / 0 / 0 / 0
    - g「背景_休日フラグ の個別のカウント」quantity 0.94: 0 / 0 / 0 / 1

## category→tax_class

- R083 b023-0072「Tariff」: DPTI owned CLER / SAPN owned LED PLC / DPTI owned Energy  / DPTI owned Metered / SAPN owned SLUoS
    - syn「貸方インボイス区分」tax_class 0.73: 
    - syn「貸方インボイス区分」tax_class 0.73: 
    - syn「適格請求書」tax_class 0.73: 対象外 / 対象外 / 適格 / 対象外

## category→text

- R084 b016-0004「@Caption」: 国家公務員 / 公務員数総計 / 国家公務員 / 国家公務員 / （注）1 国家公務員の数は、2を除き
    - b010「内容」text 0.96: 一色及び濁り（目視でも可）、消毒の残 / 防火設備についての損傷、腐食その他の / 建築物の敷地及び構造等についての損傷 / 建築設備についての損傷、腐食その他の
    - b009「Comments」text 0.96: Incomplete records / Incomplete records
    - b006「subject」text 0.96: On the message and / On the message and / Message and order  / On the message and
- R085 b064-0380「Datierung_Bemerkung」: geschätzt
    - b009「Terme operationnel」text 0.92: Date de la cérémon / Mineurs présentant / Date de débarqueme / Evaluation
    - syn「startDateTimeRemarks」text 0.92: 
    - b「Notes」text 0.91: Office Holder 3 da / Office Holder / Office Holder 3 da
- R086 b036-0233「Demographics」: Highest quintile h / Mother born overse / Has a disability o / Father born in oth / No non-school qual
    - b008「unsafe_」text 0.97: Higher education e / Total researchers  / HERD as a % of GNP / Researchers (HC) p
    - b008「Greater_Risk_Question」text 0.95: N/A / Currently frequent / Drank soda or pop / Did not use birth 
    - b005「Topic」text 0.95: Self-rated health  / Severe joint pain  / Eating 3 or more v / Eating 3 or more v
- R087 b062-0438「DiscretionaryReliefDescription」: Reoccupation Rate  / Rural Relief / Rural Relief / Rural Relief
    - b013「Outcome」text 0.82: Outcome 2: Facilit / Outcome 3: Improve / Outcome 1: A just  / Outcome 2: An effi
    - b007「Specific Outcomes of the Program and Tax」text 0.80: Project benefits t / Project benefits t / Project benefits t / Project benefits t
    - b010「Outcome」text 0.80: Outcome 1: Provide / Outcome 4: Good go / Outcome 1: More su / Outcome 2: Support
- R088 b023-0084「Main destination」: Part-time work(%) / VET cert IV+(%) / NILFET(%) / Looking for work( / Part-time work(%)
    - b004「利用対象者」text 0.92: 松阪市在住で保育園・幼稚園・こども園 / 松阪市在住で保育園・幼稚園・こども園 / 幼稚園などに通ってみえないお子さんと / 松阪市在住で保育園・幼稚園・こども園
    - b006「提供エリア」text 0.92: アクセスポイントから半径30ｍ以内 / アクセスポイントから半径30ｍ以内 / アクセスポイントから半径30ｍ以内 / アクセスポイントから半径30ｍ以内
    - b「無料送迎＿送迎先（自宅・自宅以外）」text 0.91: 自宅以外 : 当院バス時刻表記載 / 自宅以外 : 千早駅～千早病院（香椎 / 施設（デイサービス、デイケア等）
- R089 b062-0437「MandatoryReliefDescription」: Rural Public House / Post office Mandat / Post office Mandat
    - b007「valores_possiveis」text 0.94: 1 a 10 / Compras, Congresso / 1 a 10 / Sim, Nao
    - b012「PERIODO_VALIDO_REGRA_OPERACAO」text 0.92: 08:00 ÀS 18:00 H / 08:00 ÀS 18:00 H / 08:00 ÀS 18:00 H / 08:00 ÀS 18:00 H
    - b013「PERIODO_VALIDO_REGRA_OPERACAO」text 0.92: 08:00 ÀS 18:00 H / 08:00 ÀS 18:00 H / 08:00 ÀS 18:00 H / 08:00 ÀS 18:00 H
- R090 b036-0274「PURPOSE」: Aid to Navigation / Aid to Navigation / Aid to Navigation / Aid to Navigation / Aid to Navigation
    - g「ReadcodeDescr」text 0.92: Pubertal bleeding  / Heavy periods / H/O: polymenorrhoe / Menorrhagia
    - b002「Transfer Purpose」text 0.91: FUNDING FOR INFORM / DIRECT AND INDIREC / FUNDING PROVIDED F / SOCIAL SERVICES BL
    - b006「Objeto」text 0.91: Prestação de servi / Registro de preços / Registro de Preços / Alienação de imóve
- R091 b035-0038「Reason for enforcement activity」: FSP not audited at / FSP not revised so / Total / FSP not prepared,  / FSP audit report n
    - b2「[No.21]自由記述」text 0.95: 特になし / 特になし / 未だ検討に至っていないことから、現段 / 特になし
    - b004「開催パターン」text 0.95: 毎年7月に開催 / 毎年10月に開催 / 毎年３月に開催 / 毎年9月に開催
    - b010「内容」text 0.95: 一色及び濁り（目視でも可）、消毒の残 / 防火設備についての損傷、腐食その他の / 建築物の敷地及び構造等についての損傷 / 建築設備についての損傷、腐食その他の
- R092 b017-0136「Structure」: 
    - b008「DESC」text 0.84: Ken Harrison Reser / East Lake Drive / Steggall Park Foot / Off-Leash Dog Park
    - b003「提供エリア」text 0.81: 1F(ロビー、レストラン、情報コーナ / 1F及び2F / 本庁舎１F情報コーナー / 図書館内
    - b013「TITLE」text 0.80: Railway Bridge, Mu / Torrens Gorge Aque / Currie Street, Ade / Adelaide Arcade
- R093 b064-0230「Themen」: Geographie,Mobilit / Bevölkerung / Geographie,Mobilit / Geographie,Mobilit / Mobilität und Verk
    - b006「subject」text 0.98: On the message and / On the message and / Message and order  / On the message and
    - b2「データセット_キーワード」text 0.97: 美容;美容所;美容院 / ホテル;旅館 / 美容;美容所;美容院 / 美容;美容所;美容院
    - b010「データセット_キーワード」text 0.97: 財政 / 統計 / 計画 / 統計・教育・文化芸術・生涯学習
- R094 b017-0258「TraitValueDescription_DescriptionValeurT」: rhizomes / layering / layering / not applicable / absent
    - b2「HabitatDescription」text 0.90: Moderate energy in / Laminaria hyperbor / Laminaria hyperbor / Loose-lying mats o
    - g「Setting」text 0.88: Maximum spindle sp / Step pulse invert / Z-axis maximum rat / Invert step enable
    - b014「type_or_title」text 0.87: Painting / Musical Compositio / Something New/The  / Pabhsaeir Inis Meá
- R095 b063-0242「source」: IMF Goverment Fina / IMF Goverment Fina / OECD Economic Outl / IMF Goverment Fina / IMF Goverment Fina
    - b011「Source」text 0.94: Centrelink adminis / Centrelink and DVA / Centrelink and DVA / Centrelink adminis
    - b007「状況」text 0.91: 羆の足跡を発見 / 子羆を目撃 / 羆を目撃 / 羆を目撃
    - g「cause_of_invalid_ranking」text 0.90: compares lupascu20 / compares mendonca2 / compares to mendon / compares to mendon
- R096 b060-0187「territorial_application_of_reul」: #NA / GB only (England & / UK wide / GB only (England & / UK wide
    - b003「提供エリア」text 0.92: 1F(ロビー、レストラン、情報コーナ / 1F及び2F / 本庁舎１F情報コーナー / 図書館内
    - b004「アクセス方法」text 0.88: 大溝小学校敷地内 / 木佐木小学校敷地内 / 大莞小学校敷地内
    - b012「wind__area_1_」text 0.88: Southerly force 4  / Northwest force 5  / Southwest force 4  / West force 4 to 5,
- R097 b055-0507「利用可能日時特記事項」: 夜間利用可能 / 夜間利用可能 / 夜間利用可能 / 夜間利用可能 / 夜間利用可能
    - b004「備考」text 0.98: ※住宅型有料老人ホーム / ※有料老人ホーム、住特 / 備考 / ※有料老人ホーム、住特
    - j「備考」text 0.98: 単価契約 / 単価契約 / 単価契約
    - b011「備考」text 0.98: 休会中 / 休会中 / 休会中 / 休会中

## date→quantity

- R098 b064-0137「Semaine」: 18 / 41 / 42 / 35 / 23
    - b008「tavg__mean_wave_period___seconds_」quantity 0.95: 4.1 / 6.1 / 5.0 / 4.4
    - b008「tsig__significant_period___seconds_」quantity 0.95: 7.7 / 6.9 / 7.5 / 6.5
    - b011「FISHING_TIME」quantity 0.94: 2.5 / 2.5 / 3.42 / 2.5

## date→text

- R099 b063-0400「sessionssitzung_uhrzeit」: 13.30–16.30 / 13.30-16.30 / 13.00-16.35 / 09.00-11.45 / 17.00-19.00
    - b008「Thurs am」text 0.94: 8:30 - 12:30 / 9:00 - 13:00 / 8:30 / 8:30 - 13:00
    - b012「開館時間」text 0.93: 利用時間 午前9時から午後5時
    - b013「Opening_Hours_Mon_Open」text 0.93: 10:00AM / 09:00AM / 09:00AM / 10:00AM
- R100 b063-0392「traktandum_start_behandlung_uhrzeit」: 13.30–16.00 / 13.30–16.30 / 13.30-16.30 / 13.30-16.30 / 09.00–11.45
    - b008「Thurs am」text 0.90: 8:30 - 12:30 / 9:00 - 13:00 / 8:30 / 8:30 - 13:00
    - b013「Opening_Hours_Mon_Open」text 0.90: 10:00AM / 09:00AM / 09:00AM / 10:00AM
    - b012「開館時間」text 0.89: 利用時間 午前9時から午後5時

## id→address

- R101 b063-0071「Gemeinde_Nr」: 41 / 23 / 6 / 89 / 90
    - b010「HOUSE_NO」address 0.96: 3 / 15 / 437 / 2
    - b013「house_no」address 0.96: 0 / 271 / 115 / 42
    - b006「NUMERO」address 0.95: 1200.0 / 56.0 / 170.0 / 65.0
- R102 b060-0831「listed_building」: 1072816 / 1072810 / 1072805 / 1072764 / 1361942
    - syn「cityBlock」address 0.96: 2191883 / 7511033 / 2057122 / 2976594
    - syn「」address 0.95: 1311837 / 6182634 / 3829168 / 9081842
    - syn「」address 0.95: 5864650 / 2633745 / 2411491 / 9896059

## id→category

- R103 b064-0147「GEO_CANT」: 11 / 10 / 1 / 2 / 2
    - syn「」category 0.94: 3 / 3 / 9 / 3
    - syn「」category 0.94: 3 / 3 / 3 / 9
    - b009「MMM2019」category 0.94: 1 / 1 / 1 / 1
- R104 b060-0205「GOR CODE」: H / H / H / H / H
    - b013「treatment_code」category 0.98: S / C / SH / C
    - b2「LABEL」category 0.98: G1 / T / T / T
    - b2「Class_4」category 0.97: 1 / 1 / 1 / 1
- R105 b063-0147「Id Experiment Category」: experiment_2 / experiment_2 / experiment_1 / experiment_1 / experiment_1
    - b014「CLASS」category 0.98: FISH_CLEAN_STATION / FISH_CLEAN_STATION / FISH_CLEAN_STATION / FISH_CLEAN_STATION
    - b「Decision Category」category 0.98: PRE / PRE / PRE / PRE
    - b007「NIVEL_PROTECAO」category 0.98: PROTECAO SOCIAL BA / PROTECAO SOCIAL BA / PROTECAO SOCIAL ES / PROTECAO SOCIAL BA
- R106 b063-0141「Id Of Animal Category」: animal_1 / animal_2 / animal_1 / animal_1 / animal_1
    - b013「Type」category 0.99: club / club / club / club
    - b012「dev_type」category 0.99: device / device / device / device
    - b003「学校種」category 0.99: B1(小学校) / B1(小学校) / B1(小学校) / A2(こども)
- R107 b063-0148「Id Of Disease Category」: disease_14 / disease_3 / disease_14 / disease_3 / disease_14
    - b「Decision Type」category 0.98: F.PAROLE-PR.REL / F.PAROLE-PR.REL / F.PAROLE-PR.REL / F.PAROLE-PR.REL
    - b008「Class」category 0.98: 1 / 1 / 1 / 1
    - b003「Class」category 0.98: 1 / 1 / 2 / 1
- R108 b015-0047「No.」: 4 / 5 / 3 / No. = Number; D =  / 2
    - b010「NUM_MODE_TRANSPORT」category 0.98: 1 / 1 / 1 / 1
    - b011「DEMO8」category 0.98: 2 / 2 / 2 / 2
    - b011「asgc_ra」category 0.97: 1 / 2 / 2 / 0
- R109 b060-0900「Question」: Q1 / Q10 / Q10 / Q1 / Q10
    - b010「Datum/ EPSG」category 0.90: GDA2020 / GDA2020 / GDA2020 / GDA94
    - b009「MEPSComp」category 0.89: MEPS 2019 / MEPS 2019 / MEPS 2020 / MEPS 2019
    - b006「ballot_title_2」category 0.88: BOT 01-0260 PCO / HOLLYWOOD PCO / RNT 11-0354 PCO / ROUNDTABLE PCO
- R110 b054-0001「STATISTIC」: MIDWIVES / MIDWIVES / MIDWIVES / MIDWIVES / MIDWIVES
    - b010「Statistic」category 0.96: New House Guarante / New House Guarante / New House Guarante / New House Guarante
    - b006「vote」category 0.96: Y / Y / NP / N
    - b004「FILING FREQUENCY」category 0.96: L / L / L / L
- R111 b064-0168「abkuerzung」: PuM / MOFIS / UPI,Unique Person  / BD / GD
    - b2「conservation_area_site_id」category 0.90: not in conservatio / not in conservatio / not in conservatio / not in conservatio
    - b013「TraitCode」category 0.88: SLA / LDMC / Leaf_N / LA
    - g「source_vocabulary_id」category 0.87: JNJ_CPRD_TEST_ENT / JNJ_CPRD_TEST_ENT / JNJ_CPRD_TEST_ENT / JNJ_CPRD_TEST_ENT
- R112 b017-0263「batch」: 1 / NA / NA / NA / NA
    - b013「Bin」category 0.97: 1 / 1 / 0 / 1
    - b010「FOREST」category 0.96: 1 / 1 / 1 / 1
    - b009「INES Level」category 0.95: 0 / N/A / N/A / 0
- R113 b063-0372「id2」: storchen / claramatte / steinen / rebgasse / centralbahn
    - b2「TREETYPE」category 0.87: VAR / VAR / HCHES / VAR
    - b008「Parameter」category 0.86: Alkalinity Bicarbo / BGA Algalscan / Alkalinity Bicarbo / Alkalinity Bicarbo
    - b2「Projection」category 0.83: WGS84 / WGS84 / WGS84 / WGS84
- R114 b063-0300「kategorie_sortierung」: 1 / 3 / 3 / 4 / 1
    - b009「CD_CLASS_VEH」category 0.98: 2 / 2 / 2 / 2
    - b014「教育機関_本分校」category 0.98: 1 / 4 / 4 / 1
    - b009「Level B」category 0.98: 2 / 3 / 2 / 2
- R115 b064-0197「kategorie_sortierung」: 1 / 1 / 1 / 1 / 1
    - b003「本分校」category 0.99: 1 / 1 / 1 / 1
    - b003「本分校」category 0.99: 1 / 1 / 1 / 1
    - b2「Class_4」category 0.99: 1 / 1 / 1 / 1
- R116 b064-0046「nfr」: 5C / 5D / 3B / 5A / 3A
    - b「Base Layer 1」category 0.97: 1 / 1 / 1 / 1
    - b「Base Layer 1」category 0.97: 1 / 1 / 1 / 1
    - b「Base Layer 2」category 0.97: 2 / 0 / 2 / 2
- R117 b023-0120「traffic_direction_seq」: 0 / 0 / 0 / 0 / 1
    - b010「MEDIUM_TYPE」category 0.95: 11 / 1 / 1 / 1
    - b014「Category」category 0.93: 1 / 6 / 4 / 5
    - b014「Carriageway」category 0.93: 3 / 3 / 3 / 1
- R118 b064-0194「verteilzone」: 261_LZ / 261_LZ / 261_LZ / 261_LZ / 261_LZ
    - b「Base Layer 1」category 0.98: 1 / 1 / 1 / 1
    - b「Base Layer 3」category 0.98: 3 / 0 / 3 / 3
    - b「Base Layer 1」category 0.98: 1 / 1 / 1 / 1
- R119 b019-0010「大分類」: H / L / F / Q / T
    - syn「カテゴリー」category 0.99: false /  / false / true
    - b2「TPTREECAT」category 0.99: T / G / T / T
    - b008「AADT_Intervention_Category」category 0.99: Cat C / Cat C / Cat C / Cat C

## id→org

- R120 b062-0186「Extending Agency」: 3 / 3 / 3 / 3 / 3
    - b013「Agencies」org 0.93: ARENA / ARENA / ARENA / ARENA
    - b008「Airline」org 0.93: All Airlines / QantasLink / QantasLink / Virgin Australia
    - syn「Brand2」org 0.92: 丸山銀行 / 工業さくら / 中央銀行 / 工業ミナト
- R121 b065-0193「Extending Agency」: 3 / 3 / 3 / 3 / 3
    - b013「Agencies」org 0.93: ARENA / ARENA / ARENA / ARENA
    - b008「Airline」org 0.93: All Airlines / QantasLink / QantasLink / Virgin Australia
    - syn「Brand2」org 0.92: 丸山銀行 / 工業さくら / 中央銀行 / 工業ミナト
- R122 b064-0384「Signatur」: GS-GUGE-STADTTORE- / GS-GUGE-JOYEUX-WEX / GS-GUGE-FEYERABEND / GS-GUGE-DIKENMANN- / GS-GUGE-JOYEUX-WEX
    - b007「施設名称_英字」org 0.94: honda community le / acty cocobunji / namiki community l / honda community le
    - b005「名称_カナ」org 0.93: キノカワシヤクショ ホンチョウシャ / コカワダイ５ブンダンダイ３ブショウボ / モモヤマダイ３ブンダンダイ１５ブショ / ナガタショウガッコウ
    - b004「投票所_名称（英字）」org 0.93: minamisentashukaij / uchizatokokaido / yamashibakominkan / kawaguchikomyunite
- R123 b064-0320「verantwortlichkeit_abkuerzung」: KTTGWH / KTTGWH / KTTGWH / BAFU / KTTGWH
    - b007「GESTOR」org 0.86: BHBUS/MOVE: BHTRAN / SETOP / BHTRANS / BHBUS/MOVE: BHTRAN
    - b013「Agencies」org 0.86: ARENA / ARENA / ARENA / ARENA
    - b007「Orgao」org 0.85: GP / PGM / SMRI / GP

## id→other

- R124 b060-0393「Body」: 
    - b2「Body」other 1.00: http://statistics. / http://statistics. / http://statistics. / http://statistics.
    - b2「Body」other 1.00: http://statistics. / http://statistics. / http://statistics. / http://statistics.
    - b「Body」other 1.00: http://statistics. / http://statistics. / http://statistics. / http://statistics.
- R125 b060-0737「SiteReference」: 
    - b007「リソース名」other 0.93: 240001_groundwater / 240001_jinko_visio / 240001_kaigoin_you / 240001_shirubar_ji
    - b011「Station_Chainage」other 0.92: 28510 / 4834 / 22816 / 11786
    - g「spotify_url」other 0.90: spotify:track:7kxs / spotify:track:1MTJ / spotify:track:6OW0 / Not Found
- R126 b015-0007「Tree」: 
    - g「oldalSzam」other 0.91: 26 / 196 / 158 / 186
    - g「volume」other 0.90: 15.0 / 15.0 / 15.0
    - b011「dbh」other 0.90: 154 / 52 / 69 / 54
- R127 b017-0269「bathPosition」: 
    - g「dag-stage」other 0.91: 6 / 6 / 6 / 6
    - g「digits」other 0.90: 4 / 4 / 4 / 4
    - g「ブロモホルム」other 0.86: 小3位 / 2 / 0 / 0
- R128 b060-0860「organisati」: 
    - b「OrganisationURI」other 0.99: http://opendatacom / http://opendatacom / http://opendatacom / http://opendatacom
    - b008「dataURL」other 0.99: http://www.ga.gov. / http://www.ga.gov. / http://www.ga.gov. / http://www.ga.gov.
    - b「OrganisationURI」other 0.99: http://opendatacom / http://opendatacom / http://opendatacom / http://opendatacom

## id→quantity

- R129 b064-0155「NO_COMPLEMENTAIRE」: 
    - b006「NUM_UNID_ANDAMENTO」quantity 0.97: 0 / 0 / 0 / 0
    - b003「NO UNITS」quantity 0.96: 2 / 2 / 1 / 2
    - b011「映画会」quantity 0.95: 2 / 8 / 4 / 1
- R130 b063-0117「Versicherer」: 
    - b011「State Government」quantity 0.95: 4058 / 10278 / 7918 / 4069
    - b005「病院」quantity 0.95: 697 / 727 / 695 / 652
    - g「西第５（北崎支所）」quantity 0.95: 313 / 294 / 287 / 244
- R131 b064-0160「funk」: 
    - g「control」quantity 0.95: 42 / 0 / 6 / 0
    - b014「Pika.sum」quantity 0.94: 4 / 4 / 4 / 0
    - syn「点数」quantity 0.93: 5 / 2 / 5 / 10
- R132 b017-0271「replicate」: 
    - b008「1」quantity 0.97: 9 / 5 / 8 / 3
    - b013「p_certified」quantity 0.96: 33 / 46 / 1 / 76
    - b003「NO UNITS」quantity 0.96: 2 / 2 / 1 / 2

## id→text

- R133 b064-0210「sitzung_titel」: 53. Sitzung / 57. Sitzung / 57. Sitzung / 59. Sitzung / 55. Sitzung
    - b014「名称」text 0.74: ぎかいのトビラ第145号 / ぎかいのトビラ第143号 / ぎかいのトビラ第147号 / ぎかいのトビラ第144号
    - b2「SCHEDULE_LINE_17」text 0.74: 9 - 43, 49, 59 - 6 / 33 - 73 & 81 & 163 / Class of Fireplace / Air Act 1956 and k
    - b013「根拠」text 0.74: 情報公開条例第22条第1号 / 情報公開条例第22条第3号-1 / 情報公開条例第22条第3号-2 / 情報公開条例第22条第3号-2

## org→account

- R134 b063-0108「Departement」: EDI / EDA / EDA / EDA / PARL,BR,BK
    - g「Facility」account 0.96: PSYCH / PSYCH / PSYCH / PSYCH
    - b006「DEPARTMENT」account 0.95: GREATER BR AIRPORT / CLERK OF COURT / EMPLOY BR WORKFORC / EMPLOY BR WORKFORC
    - syn「Department（任意）」account 0.95: 
- R135 b060-0345「Department」: DECC / DECC / DECC / DECC / DECC
    - b007「Division/Sitegroup」account 0.97: Boston Public Work / Boston Public Work / Boston Public Work / Boston Public Work
    - b009「Dept_Level_1」account 0.97: Environment, Clima / Taoiseach's Group / Tourism, Culture,  / Environment, Clima
    - syn「Department（任意）」account 0.97: 
- R136 b065-0203「Department」: FCO / FCO / FCO / FCO / FCO
    - b007「Division/Sitegroup」account 0.98: Boston Public Work / Boston Public Work / Boston Public Work / Boston Public Work
    - b009「Dept_Level_1」account 0.98: Environment, Clima / Taoiseach's Group / Tourism, Culture,  / Environment, Clima
    - b006「DEPARTMENT」account 0.98: GREATER BR AIRPORT / CLERK OF COURT / EMPLOY BR WORKFORC / EMPLOY BR WORKFORC
- R137 b036-0166「Department」: Fire and Emergency / Tourism and Sport* / TOTAL / Youth Justice* / Education
    - b2「Department」account 0.99: Adults and Health / Adults and Health / Adults and Health / Adults and Health
    - b2「Department」account 0.99: Adults and Health / Adults and Health / Adults and Health / Adults and Health
    - b「Department」account 0.99: School Funding and / Housing / Adult Social Care / Transp Highways & 
- R138 b062-0073「Department Family」: Communities & Loca / Communities & Loca / Communities & Loca / Communities & Loca / Communities & Loca
    - b006「ORGAO_ENTIDADE」account 0.97: Secretaria Municip / Secretaria Municip / Secretaria Municip / Secretaria Municip
    - b009「Dept_Level_1」account 0.97: Environment, Clima / Taoiseach's Group / Tourism, Culture,  / Environment, Clima
    - b「Department」account 0.97: Communities / DCLS / DCLS / Finance
- R139 b060-0800「Department family」: Communities And Lo / Communities And Lo / Communities And Lo / Communities And Lo / Communities And Lo
    - b006「ORGAO_ENTIDADE」account 0.96: Secretaria Municip / Secretaria Municip / Secretaria Municip / Secretaria Municip
    - b009「Dept_Level_1」account 0.96: Environment, Clima / Taoiseach's Group / Tourism, Culture,  / Environment, Clima
    - b「Department」account 0.96: Communities / DCLS / DCLS / Finance
- R140 b065-0244「Main, parent or sponsoring department」: Home Office / Home Office / Home Office / Home Office / Home Office
    - b007「Department」account 0.95: PWD / BPS / PWD / Fire
    - syn「管理部門」account 0.92: 
    - b006「Department」account 0.91: PWDx / PWDx / PWDx / PWDx
- R141 b060-0980「Parent Department」: Export Credits Gua / Export Credits Gua / Export Credits Gua / Export Credits Gua / Export Credits Gua
    - b006「LocalDestino」account 0.95: PBH/SUOUVI / PBH/SUOUVI / PBH/SUOUVI / PBH/SUOUVI
    - j「貸方部門」account 0.93: 部門B / 部門B / 部門B
    - b005「会計名称」account 0.93: 介護保険特別会計（介護サービス事業勘 / 介護保険特別会計（介護サービス事業勘 / 介護保険特別会計（介護サービス事業勘 / 介護保険特別会計（介護サービス事業勘
- R142 b062-0109「Supplier」: 
    - b006「LocalDestino」account 0.83: PBH/SUOUVI / PBH/SUOUVI / PBH/SUOUVI / PBH/SUOUVI
    - b006「Setor_Tipo_de_Veiculo」account 0.83: SMSA_GEURE / GP / SMSA_DRES_O / FPMZB
    - b2「SERVICE_RESPONSABLE」account 0.83: Grands parcs / Grands parcs / Grands parcs / Habitation
- R143 b063-0109「Verwaltungseinheit (Auftraggeber)」: EDA / EDA / BAG / BAG / EDA
    - syn「管理部門」account 0.92: 
    - b007「Department」account 0.91: PWD / BPS / PWD / Fire
    - b006「LocalDestino」account 0.90: PBH/SUOUVI / PBH/SUOUVI / PBH/SUOUVI / PBH/SUOUVI
- R144 b063-0601「organisationseinheit」: Bildungsdirektion / Bildungsdirektion / Finanzdirektion / Baudirektion / Direktion der Just
    - b010「Business Unit」account 0.98: Capital Delivery / Social Housing Del / Social Housing Del / REGIONAL
    - b006「管理」account 0.98: 環境課 / 住民管理 / 住民管理 / 環境課
    - syn「部門」account 0.97: Cash / 普通預金 / 売掛金 / 

## org→address

- R145 b036-0055「Centre」: Brown Hill SCC / Sebastopol SCC / Ballarat South SCC / North Ballarat SCC / Wendouree SCC
    - b014「Station」address 0.97: Petewawa / London / Infocentre / London
    - b008「Test Centre」address 0.97: Newcastlewest / Birr / Kilrush / Raheny
    - b004「投票所_投票区名」address 0.97: 八幡市第２２投票所 / 八幡市第６投票所 / 八幡市第１３投票所 / 八幡市第１１投票所
- R146 b055-0074「市場名」: 淀橋市場 / 足立市場 / 北足立市場 / 板橋市場 / 食肉市場
    - b008「名称」address 0.97: 新宿区立新宿中央公園フットサル施設 / 新宿区立四谷スポーツスクエア / 妙正寺川公園運動広場 / 新宿区立大久保スポーツプラザ
    - b008「名称」address 0.97: 月島スポーツプラザ / 豊海テニス場 / 総合スポーツセンター / 月島運動場
    - b008「名称」address 0.97: 武蔵野プール（屋外） / 武蔵野温水プール / 武蔵野総合体育館 / 武蔵野庭球場
- R147 b055-0110「警察署名」: 昭島 / 尾久 / 牛込 / 蒲田 / 新宿
    - b004「団体名」address 0.99: 垂水市 / 垂水市 / 垂水市 / 垂水市
    - b003「団体名」address 0.99: 壱岐市 / 壱岐市 / 壱岐市 / 壱岐市
    - b003「団体名」address 0.99: 高島市 / 高島市 / 高島市 / 高島市

## org→category

- R148 b017-0304「Data Source」: Bell/SSC / Bell/SSC / SSC / Bell/SSC / Bell/SSC
    - b013「Source」category 0.95: Existing Destinati / ARENA - Driving th / Existing Destinati / Existing Destinati
    - b008「DataSource」category 0.95: YRBSS / YRBSS / YRBSS / YRBSS
    - b006「DataSource」category 0.95: BRFSS / BRFSS / BRFSS / BRFSS
- R149 b060-0287「Department Family」: DFID / DFID / DFID / DFID / DFID
    - b012「借入先」category 0.85: 公募 / 公募 / 公募 / 公募
    - b009「Portfolio Dept?」category 0.83: YES / YES / YES / YES
    - syn「ブランド」category 0.82: 2 / 3 / 2 / 9
- R150 b060-0515「Department Family」: Home Office / Home Office / Home Office / Home Office / Home Office
    - b014「Maintain」category 0.87: City of Ballarat / Tenant / City of Ballarat / Tenant
    - b003「診療科」category 0.86: 内科他 / 消化器内科他 / 産婦人科 / 内科他
    - b012「dept_f」category 0.85: Fonction Publique  / Fonction Publique  / Fonction Publique  / Fonction Publique 
- R151 b062-0268「Department Family」: Land Registry / Land Registry / Land Registry / Land Registry / Land Registry
    - b009「AgencyCategory」category 0.83: Transport, Roads a / Justice / Education / Transport
    - b008「Government」category 0.82: Aust Govt / Aust Govt / Aust Govt / Aust Govt
    - b2「ÉTAT」category 0.82: Assujetti / Assujetti / Assujetti / Assujetti
- R152 b050-0009「MAKE_DESC」: AIR RIDE / ALDOM / ALFA ROMEO / ALDOM / ALFA ROMEO
    - syn「Seller Brand」category 0.84: 
    - syn「Card Brand」category 0.84: 3 / 9 / 9 / 9
    - syn「vendor_brand」category 0.82: 
- R153 b060-0981「Organisation」: Export Credits Gua / Export Credits Gua / Export Credits Gua / Export Credits Gua / Export Credits Gua
    - b008「Government」category 0.87: Aust Govt / Aust Govt / Aust Govt / Aust Govt
    - b007「区分」category 0.85: 山前南地域体育館 / スポーツ交流館 / 総合体育館 / 武道体育館
    - b012「借入先」category 0.84: 公募 / 公募 / 公募 / 公募
- R154 b036-0069「operator」: COGG / COGG / COGG / COGG / COGG
    - g「PulseSequenceType」category 0.94: EPI / EPI / EPI / EPI
    - g「journal_pcode」category 0.94: nphoton / nphoton / nphoton / nphoton
    - b010「GIS_ACQUISITION_METHOD」category 0.94: UN / CAPEX / CONTR / UN
- R155 b062-0070「trading_bloc」: #NA / the ASEAN / the EU / the Mercosur / #NA
    - b013「sub_category」category 0.87: Cared for other ch / Count of families / $300 - $399 / Somali
    - b008「Zone」category 0.86: Central Zone / Central Zone / Northern Zone / Western Zone
    - b2「Beneficiary Location:Geographic Code Typ」category 0.86: LAD / LAD / LAD / LAD

## org→person

- R156 b063-0722「creator」: Janssonius Offizin / Martini, Martino / Janssonius Offizin / Janssonius Offizin / Janssonius Offizin
    - g「Author」person 0.97: adrianwaj / kyro / mynameishere / aswanson
    - g「creator」person 0.96: Shine, James M. et / Abeliovich, Asa; G / Bansal, Kanika, et / Reyes, Pablo Alexa
    - syn「Owner」person 0.95: スズキ ハナコ /  /  / スズキ ハナコ

## org→text

- R157 b050-0040「Title」: Queensland Motorcy / Top Rider GC / Motorcycle Masters / Coastal Motorcycle / Stay Upright
    - b008「Title」text 0.98: Camperdown Show / Camperdown Rotary  / Australia Day cele / Inner Varnika
    - b「Title」text 0.98: Web ePayment Porta / Commonwealth lease / DMO Negotiation Se / Civil Engineering 
    - b「DTF Publication Title」text 0.97: Croxton Special Sc / Yan Yean Road / Warburton Police S / Glen Huntly Primar

## product→text

- R158 b060-0177「service」: 
    - b「Product-English-Name-Nom-anglais-du-Prod」text 0.77: Canada Revenue Age / New Brunswick Chil / Elections Canada - / Canada Pension Pla
    - b009「Nom du service」text 0.75: Signalement d'un i / Installations de T / Aide et informatio / Service de mainten
    - syn「Opportunity Name1」text 0.72: ﾌﾘｺﾐ ｻｸﾗｼﾖｳｼﾞ / サンプル送付 / 振込手数料 / 備考なし

## quantity→amount

- R159 b017-0346「Amount per Container」: 
    - syn「商品小計」amount 0.88: 10 / 0 / 10 / 0
    - b011「粗大ごみ回収料金」amount 0.85: 100 / 100 / 100 / 300
    - b「生活援助＿目安時間単価（円／1時間）」amount 0.84: 8,250円／１時間 / 3,500円／１時間 / 1,000円／１時間 / 3,850円／１時間
- R160 b062-0035「EW_Total_Company_NSA」: 
    - b008「Total Allocated」amount 0.92: 2113 / 16394.4 / 846.81 / 4900
- R161 b015-0082「Emp_Wkf_POPD_15+yrs_2021」: 
    - b2「Refunds-prev-yrs-exp_Recouv-deps-exs-ant」amount 0.98: 35 / 975 / 0 / 25154
    - b012「DESC_CARG_NAO_REALIZ」amount 0.98: 150.385,51 / 221.897,17 / 208.687,21 / 377.681,87
    - b2「2022/23」amount 0.98: 3,682,000 / 164,383 / - / 4,611,300
- R162 b015-0083「Emp_Wkf_POPD_15+yrs_2022」: 
    - b012「DESC_CARG_NAO_REALIZ」amount 0.98: 150.385,51 / 221.897,17 / 208.687,21 / 377.681,87
    - b014「Retirement Pension」amount 0.98: 134.97 / 1,178.77 / 727.08 / 775
    - b2「Annual Sales 2013」amount 0.98: 538,427 / 194,408 / 732,835
- R163 b015-0084「Emp_Wkf_POPD_15+yrs_2023」: 
    - b012「DESC_CARG_NAO_REALIZ」amount 0.98: 150.385,51 / 221.897,17 / 208.687,21 / 377.681,87
    - b012「Value of exports」amount 0.98: 18,641 / 207,768 / 50,125 / 19,317
    - b006「REALIZADO」amount 0.98: 5.608,48 / 7.039.325,84 / 1.156.821,19 / 0
- R164 b015-0085「Emp_Wkf_POPD_15+yrs_2024」: 
    - b014「Retirement Pension」amount 0.98: 134.97 / 1,178.77 / 727.08 / 775
    - b2「Annual Sales 2013」amount 0.98: 538,427 / 194,408 / 732,835
    - b2「Annual Sales 2014」amount 0.98: 598,502 / 222,592 / 821,094
- R165 b015-0086「Emp_Wkf_POPD_15+yrs_2025」: 
    - b012「DESC_CARG_NAO_REALIZ」amount 0.98: 150.385,51 / 221.897,17 / 208.687,21 / 377.681,87
    - b2「Annual Sales 2014」amount 0.98: 598,502 / 222,592 / 821,094
    - b014「Retirement Pension」amount 0.98: 134.97 / 1,178.77 / 727.08 / 775
- R166 b015-0087「Emp_Wkf_POPD_15+yrs_2026」: 
    - b012「DESC_CARG_NAO_REALIZ」amount 0.98: 150.385,51 / 221.897,17 / 208.687,21 / 377.681,87
    - b2「Annual Sales 2014」amount 0.98: 598,502 / 222,592 / 821,094
    - b2「Refunds-prev-yrs-exp_Recouv-deps-exs-ant」amount 0.98: 35 / 975 / 0 / 25154
- R167 b015-0088「Emp_Wkf_POPD_15+yrs_2027」: 
    - b2「2022/23」amount 0.98: 3,682,000 / 164,383 / - / 4,611,300
    - b009「平成27年度(千円)」amount 0.98: 48361 / 693 / 19582 / 9479
    - b2「Refunds-prev-yrs-exp_Recouv-deps-exs-ant」amount 0.97: 35 / 975 / 0 / 25154
- R168 b015-0089「Emp_Wkf_POPD_15+yrs_2028」: 
    - b006「REALIZADO」amount 0.98: 5.608,48 / 7.039.325,84 / 1.156.821,19 / 0
    - b012「DESC_CARG_NAO_REALIZ」amount 0.98: 150.385,51 / 221.897,17 / 208.687,21 / 377.681,87
    - b014「Children of Disabled or Deceased Contrib」amount 0.98: 218.5 / 255.03 / 224.62 / 264.53
- R169 b015-0090「Emp_Wkf_POPD_15+yrs_2029」: 
    - b012「DESC_CARG_NAO_REALIZ」amount 0.98: 150.385,51 / 221.897,17 / 208.687,21 / 377.681,87
    - b006「REALIZADO」amount 0.98: 5.608,48 / 7.039.325,84 / 1.156.821,19 / 0
    - b014「Retirement Pension」amount 0.98: 134.97 / 1,178.77 / 727.08 / 775
- R170 b015-0067「Fossil fuels」: 
    - b「Australian Sourced Goods」amount 0.89: 6956468949 / 5980643678 / 9782606966 / 6876377213
    - b「Overseas Sourced Goods」amount 0.86: 5243983315 / 8279109738 / 6216567762 / 8751360145
    - syn「supplierNetTotal」amount 0.85: 
- R171 b015-0070「Total (All categories)」: 
    - syn「」amount 0.95: 28,020 / 6490 / 5290 / 7,670
    - syn「」amount 0.94: 392,140 / 64,300 / 282100 / 52690
    - b006「非分割」amount 0.93: 12592633416.0 / 12364491271.0 / 11663756101.0 / 12101717804.0
- R172 b017-0171「Total - All Returns /Total - Toutes les 」: 
    - b2「Return-on-investments_Revenus-de-placeme」amount 0.95: 0 / 0 / 832 / 109094
    - b2「VALUE」amount 0.95: 203 / 4243 / 2505 / 140
- R173 b063-0322「kumsum」: 
    - syn「」amount 0.94: 6670 / 4310 /  / 4840
    - syn「」amount 0.87: 12040 / 22,690 / 390520 / 42930
    - syn「」amount 0.85: 28,020 / 6490 / 5290 / 7,670

## quantity→category

- R174 b065-0212「Arrest/Detention > Assault with Weapon」: 0 / 0 / 0 / 0 / 0
    - b2「Foreign Vehicle」category 0.97: 0 / 0 / 0 / 0
    - syn「accompaniedByGuideDogsAndServiceDogs」category 0.97: 0 / 1 / 2 / 1
    - g「Education」category 0.96: 5 / 2 / 4 / 3
- R175 b065-0214「Arrest/Detention > Child Sex」: 0 / 0 / 0 / 0 / 0
    - b014「Teacher Size of School」category 0.95: 19 teachers / 19 teachers / 16 teachers / 16 teachers
    - g「Attrition」category 0.95: 1 / 0 / 0
    - b010「TEMPO_PERMANENCIA」category 0.95: 1 HORA(S) / 1 HORA(S) / 1 HORA(S) / 1 HORA(S)
- R176 b022-0064「Count of Vehicle ROIDs」: 1 / 1 / 1 / 1 / 2
    - b006「PUBLIC_FLG」category 0.96: 1 / 1 / 1 / 1
    - b010「TESSELLATE」category 0.94: 1 / 1 / 1 / 1
    - b010「NUM_MODE_TRANSPORT」category 0.94: 1 / 1 / 1 / 1
- R177 b063-0143「Degree of severity 0」: 10 / 0 / 61 / 0 / 0
    - b2「potential_epc_score_known」category 0.92: 0 / 1 / 1 / 1
    - b2「epc_rating_known」category 0.92: 1 / 1 / 1 / 0
    - b2「potential_epc_rating_known」category 0.90: 0 / 1 / 0 / 1
- R178 b063-0144「Degree of severity 1」: 0 / 0 / 6 / 0 / 4
    - b2「epc_rating_known」category 0.92: 1 / 1 / 1 / 0
    - b011「Trunk Circumference」category 0.92: Less than 2m / Less than 2m / Less than 2m / Less than 2m
    - b014「LUMquintile」category 0.91: 1 / 5 / 4 / 1
- R179 b063-0145「Degree of severity 2」: 7 / 0 / 1267 / 0 / 0
    - b2「epc_rating_known」category 0.91: 1 / 1 / 1 / 0
    - b2「potential_epc_score_known」category 0.91: 0 / 1 / 1 / 1
    - g「Hydrozoa_indet」category 0.90: 0 / 0 / 0 / 0
- R180 b063-0146「Degree of severity 3」: 29 / 0 / 0 / 0 / 0
    - b2「epc_rating_known」category 0.93: 1 / 1 / 1 / 0
    - b011「Trunk Circumference」category 0.91: Less than 2m / Less than 2m / Less than 2m / Less than 2m
    - b2「potential_epc_score_known」category 0.91: 0 / 1 / 1 / 1
- R181 b060-0706「Neither satisfied or dissatisfied」: 3 / 8 / 3 / 8 / 9
    - syn「Pay Frequency」category 0.90: 0 / 2 / 1 / 2
    - b2「potential_epc_score_known」category 0.88: 0 / 1 / 1 / 1
    - syn「」category 0.88: 10 / 10 / 20 / 20
- R182 b015-0052「No. laboratory confirmed」: 5 / 5 / 2 / 5 / 45
    - b009「MMM2019」category 0.95: 1 / 1 / 1 / 1
    - b011「PT」category 0.95: 2 / 5 / 5 / 6
    - b010「RESULT」category 0.94: 1 / 1 / 1 / 1
- R183 b035-0039「Written warnings」: 1 / 0 / 0 / 0 / 1
    - syn「車椅子可」category 0.96: 10 / 10 / 10 / 20
    - g「貸切可能」category 0.96: 1 / 1 / 0
    - b2「Foreign Vehicle」category 0.95: 0 / 0 / 0 / 0
- R184 b023-0029「education_and_training」: 0 / 0 / 0 / 1 / 0
    - g「Education」category 0.95: 4 / 2 / 3 / 4
    - b「無料送迎＿提供サービス＿通院」category 0.94: 1 / 1
    - g「Education」category 0.94: 5 / 2 / 4 / 3
- R185 b023-0040「education_and_training」: 2 / 0 / 0 / 0 / 2
    - g「Education」category 0.95: 5 / 2 / 4 / 3
    - g「Education」category 0.95: 4 / 2 / 3 / 4
    - syn「accompaniedByGuideDogsAndServiceDogs」category 0.94: 0 / 1 / 2 / 1
- R186 b063-0165「parameter_decimals」: 0 / 0 / 0 / 0 / 0
    - g「Hydrozoa_indet」category 0.92: 0 / 0 / 0 / 0
    - b008「Decimals」category 0.89: 2 / 2 / 2 / 2
    - b013「val_cal」category 0.89: 1 / 1 / 1 / 1
- R187 b063-0173「parameter_decimals」: 0 / 0 / 0 / 0 / 0
    - g「Hydrozoa_indet」category 0.92: 0 / 0 / 0 / 0
    - b008「Decimals」category 0.89: 2 / 2 / 2 / 2
    - b013「val_cal」category 0.89: 1 / 1 / 1 / 1
- R188 b063-0181「parameter_decimals」: 0 / 0 / 1 / 0 / 0
    - g「Hydrozoa_indet」category 0.93: 0 / 0 / 0 / 0
    - b008「Decimals」category 0.91: 2 / 2 / 2 / 2
    - b011「Chlorophyll [quality]」category 0.90: 1020 / 1020 / 1020 / 1020
- R189 b064-0109「parameter_decimals」: 0 / 0 / 0 / 0 / 0
    - g「Hydrozoa_indet」category 0.92: 0 / 0 / 0 / 0
    - b008「Decimals」category 0.89: 2 / 2 / 2 / 2
    - b013「val_cal」category 0.89: 1 / 1 / 1 / 1
- R190 b064-0117「parameter_decimals」: 0 / 1 / 0 / 0 / 1
    - g「Hydrozoa_indet」category 0.93: 0 / 0 / 0 / 0
    - b008「Decimals」category 0.92: 2 / 2 / 2 / 2
    - b011「Chlorophyll [quality]」category 0.92: 1020 / 1020 / 1020 / 1020
- R191 b023-0047「vehicle_class_1」: 1 / 20 / 2 / 49 / 6
    - b010「品目階層Item_Class」category 0.90: 3 / 2 / 11 / 4
    - b014「Class」category 0.88: No Code Allocated / No Code Allocated / No Code Allocated / PG-District
    - b「Type de matériel」category 0.88: 73 / 73 / 73 / 73
- R192 b023-0048「vehicle_class_2」: 0 / 0 / 0 / 0 / 1
    - syn「在庫タイプ」category 0.98: 1 /  /  / 2
    - b2「Class_1」category 0.98: 0 / 0 / 0 / 0
    - syn「Order type」category 0.98: 2 /  / 2 / 
- R193 b023-0049「vehicle_class_3」: 0 / 3 / 20 / 6 / 5
    - b010「品目階層Item_Class」category 0.95: 3 / 2 / 11 / 4
    - syn「在庫タイプ」category 0.94: 1 /  /  / 2
    - b007「group」category 0.94: 10 / 13 / 11 / 6
- R194 b023-0050「vehicle_class_4」: 2 / 0 / 0 / 0 / 0
    - b2「Class_1」category 0.98: 0 / 0 / 0 / 0
    - syn「在庫タイプ」category 0.98: 1 /  /  / 2
    - b2「Class_2」category 0.98: 0 / 0 / 0 / 0
- R195 b023-0051「vehicle_class_5」: 0 / 0 / 0 / 0 / 0
    - b2「Class_1」category 0.98: 0 / 0 / 0 / 0
    - b2「Class_2」category 0.98: 0 / 0 / 0 / 0
    - syn「在庫タイプ」category 0.98: 1 /  /  / 2
- R196 b020-0039「管理職」: 1 / 1 / 2 / 2 / 3
    - syn「役職」category 0.99: 2 / 0 / 1 / 1
    - b「身体介護」category 0.97: 1 / 1 / 1 / 1
    - b2「tenure_known」category 0.97: 1 / 0 / 1 / 0

## quantity→other

- R197 b063-0135「AnzStand」: 
    - b010「tj_ncv」other 0.95: 10437 / 23520 / 4621 / 2469
    - b008「ElevationfromSeaLevel(inm)」other 0.94: 290 / 78 / 66 / 281
    - b014「Lon」other 0.94: 149.2 / 149.2 / 149.2 / 149.2
- R198 b015-0066「Biomass」: 
    - b006「awater20」other 0.90: 0.000000000000000 / 0.000000000000000 / 0.000000000000000 / 0.000000000000000
    - g「総観場3」other 0.88: -9999 / -9999 / -9999 / -9999
    - b「Km budgété」other 0.87: 0 / 0 / 0 / 0
- R199 b065-0074「Dwellings value」: 
    - b001「１世帯当たり人口 （人）」other 0.90: 4.5 / 4.58 / 4.53 / 4.83
    - b012「A」other 0.90: 129 / N/A / 137 / 119
    - g「Metabolic rate」other 0.89: 1777 / 1300 / 1132 / 1248
- R200 b064-0142「Lim_min」: 
    - g「被害域長さ(100m)最小」other 0.97: 127 / 20 / 12 / 31
    - b2「A2 Floorspace Gains sqm」other 0.97: 1,036 / 266 / 459 / 492
    - b006「Volume (Cb ft)」other 0.97: 13708.5 / 7611 / 3735.75 / 5689.125
- R201 b063-0202「LowerB」: 
    - b012「A」other 0.96: 129 / N/A / 137 / 119
    - g「五島」other 0.94: 31 / 2 / 3 / 5
    - b011「dbh」other 0.94: 154 / 52 / 69 / 54
- R202 b015-0068「Metal ores」: 
    - b006「awater20」other 0.92: 0.000000000000000 / 0.000000000000000 / 0.000000000000000 / 0.000000000000000
    - g「oldalSzam」other 0.90: 26 / 196 / 158 / 186
    - g「総観場3」other 0.90: -9999 / -9999 / -9999 / -9999
- R203 b015-0069「Non-metallic minerals」: 
    - b006「awater20」other 0.92: 0.000000000000000 / 0.000000000000000 / 0.000000000000000 / 0.000000000000000
    - g「oldalSzam」other 0.92: 26 / 196 / 158 / 186
    - b006「Total Site Energy Usage (kBtu)」other 0.91: 8150639.2 / 1047153.4 / 1541785.8 / 1738018.2
- R204 b017-0019「TOTAL_SHEEP_MOUNTAIN」: 
    - b006「池沼」other 0.97: 309 / 317 / 319 / 310
    - b009「LENGTH_OF_GILLNET」other 0.97: 44232460 / 7400 / 32483878 / 6000
    - b011「Length」other 0.97: 230 / 258 / 198 / 955
- R205 b063-0325「vj_abs_kumsum」: 
    - b011「units_supplied_household_exemption_MWh」other 0.86: 4051556.442 / 3526537.182 / 4311253.371 / 3271393.994
    - b011「total_units_supplied_MWh」other 0.84: 25034927 / 26178504 / 28691093 / 25188253
    - b011「units_supplied_household_use_renewable_s」other 0.83: 5293214.36 / 5214627.006 / 3563262.558 / 5369666.957
- R206 b063-0323「vj_abs_n」: 
    - b011「total_units_supplied_MWh」other 0.92: 25034927 / 26178504 / 28691093 / 25188253
    - b011「units_supplied_household_use_renewable_s」other 0.90: 5293214.36 / 5214627.006 / 3563262.558 / 5369666.957
    - b011「units_supplied_electricity_generation_MW」other 0.90: 17585 / 10687 / 54270 / 17379

## quantity→rate

- R207 b060-0260「01:30」: 
    - b010「VALUE」rate 0.84: 93 / 89 / 91 / 93
    - b2「VALUE」rate 0.80: 0 / 36 / 18 / 15
- R208 b060-0263「03:00」: 
    - b2「VALUE」rate 0.85: 0 / 36 / 18 / 15
- R209 b060-0265「04:00」: 
    - b007「Cumulative Reduction in Trash Tonnage Si」rate 0.90: 41.87 / 37.66 / 39.6 / 43.42
    - b011「loans_to_households_for_house_purchase__」rate 0.87: 3.97 / 4.04 / .. / ..
    - b2「VALUE」rate 0.86: 5.4 / 2.3 / 20.7 / 0
- R210 b015-0063「Sexual violence ('000)」: 
    - b009「抽出件数(%)」rate 0.93: 12.3 / 9.7 / 7.8 / 4.6
    - b010「VALUE」rate 0.92: 93 / 89 / 91 / 93
    - syn「frequency」rate 0.90: 

## rate→other

- R211 b065-0050「Got none of what I wanted」: 
    - b008「Value」other 0.95: 10.4 / 160.0 / 0.01 / 245.5
    - b010「VALUE」other 0.94: 153.9 / 12.1 / 92.5 / 65.1
    - b005「Average Violations Per Unit」other 0.94: 0.52 / 1.33 / 0.63 / 0.27
- R212 b065-0049「Got some of what I wanted」: 
    - b008「Value」other 0.96: 10.4 / 160.0 / 0.01 / 245.5
    - b010「VALUE」other 0.94: 153.9 / 12.1 / 92.5 / 65.1
    - b008「Total ROI supplies」other 0.94: 147.765403 / 173.609757 / 127.39119099999999 / 199.152582
- R213 b063-0125「SMR 2019-2023」: 
    - b2「Health Deprivation and Disability 2010」other 0.97: 0.67 / -0.73 / -0.6 / 0.31
    - b005「測定値」other 0.97: 0.015 / 0.018 / 0.016 / 0.018
    - g「dbpedia_score」other 0.97: 0.0 / 1.0 / 1.0 / 0.0
- R214 b063-0129「SMR 2024」: 
    - g「硝酸態窒素及び亜硝酸態窒素」other 0.98: 0.9 / 0.4 / 0.4 / 0.6
    - b005「測定値」other 0.98: 0.015 / 0.018 / 0.016 / 0.018
    - g「硝酸態窒素及び亜硝酸態窒素」other 0.97: 0.4 / 0.5 / 0.4 / 0.5
- R215 b063-0326「vj_rel_kumsum」: 
    - b009「Jefferson」other 0.96: 0.038867341 / 0.515470408 / -0.385084254 / -0.675277698
    - b005「測定値」other 0.96: 0.015 / 0.018 / 0.016 / 0.018
    - g「not_danceable」other 0.96: 0.909833014011 / 0.945312380791 / 0.869928061962 / 0.947217404842
- R216 b063-0324「vj_rel_n」: 
    - g「lnVR_upper」other 0.99: 0.0705282276104203 / 0.224181899743515 / 0.296494017666062 / 0.201361794986349
    - g「not_danceable」other 0.98: 0.909833014011 / 0.945312380791 / 0.869928061962 / 0.947217404842
    - b009「Kyeema」other 0.98: -0.198773303 / 0.244945485 / 0.377290256 / -0.310245869

## text→account

- R217 b056-0012「Program title」: Government managed / RentConnect Tenanc / Youth Foyer / Bond Loans / Home Assist Secure
    - b014「Sub-program title」account 0.91: Community Grants / NA / Capital Works Gran
    - b「Description of Goods (Purpose of expendi」account 0.86: Care Payments / Fees and Charges / Fees and Charges / Information and Co
    - b2「Type of Expenditure」account 0.86: Purchase of extern / All other innovati / Purchase of extern / All expenditure on
- R218 b056-0023「Sub-program title」: Aboriginal and Tor / Dispute resolution / Legal Aid Queensla / Civil Court Fees / Free Will Making
    - b010「Program」account 0.93: Program 1.1: Emplo / Program 1.1: Feder / Program 1.2: Austr / Program 1.11: Drou
    - b「Description of Goods (Purpose of expendi」account 0.93: Care Payments / Fees and Charges / Fees and Charges / Information and Co
    - b2「Description of Goods (Purpose of expendi」account 0.93: Care Payments / Fees and Charges / Security / Care Payments
- R219 b056-0043「Sub-program title」: Round 4 / Land Rental Rebate / Round 2 / Round 1 / Collaborative Expl
    - b「Description」account 0.90: Living support gra / Non-Premises - cos / Provisions - Gener / Vehicle hire
    - b「Description of Goods (Purpose of expendi」account 0.89: Care Payments / Fees and Charges / Fees and Charges / Information and Co
    - b2「Description of Goods (Purpose of expendi」account 0.87: Care Payments / Fees and Charges / Security / Care Payments

## text→address

- R220 b063-0449「richtung」: zum Kreisel Spange / zum Marktplatz / nach Weinfelden / zum Marktplatz / nach Weinfelden
    - b012「路線名」address 0.88: 主要地方道第32号八王子五日市線 / 主要地方道第47号八王子町田線 / 一般都道第173号上館日野線 / 一般都道第173号上館日野線
    - b013「str_type」address 0.88: Rd / Gr / Crt / Dr
    - b008「路線名」address 0.83: （主40）さいたま東村山線 / （主59）八王子武蔵村山線 / （一253）保谷狭山自動車道 / （主43）立川東大和線

## text→category

- R221 b064-0291「Abstimmungsgegenstand」: Rückweisungsantrag / Gesamtabstimmung / Eintreten / Rückweisungsantrag / Antrag der SP-GRÜ-
    - b006「CASE_TITLE」category 0.96: Street Light Outag / Park Maintenance:  / Unsatisfactory Liv / General Lighting R
    - b010「Claim」category 0.95: PTSD (Single Condi / PTSD (Single Condi / PTSD (Single Condi / Hearing Loss (Sing
    - b005「支援内容」category 0.95: 玉名市災害ボランティアセンター / り災・被災証明書の受付窓口 / り災・被災証明書の受付窓口 / 災害ごみ仮置き場
- R222 b036-0139「CulturalSignificance」: Site specific comm / Historic & social  / Historic significa / see 316.1 / Historic significa
    - b010「SITUACAO」category 0.94: Possui Relatório T / Fase de aproximaçã / Instaurado o proce / Titulação da área 
    - b012「Universe」category 0.94: Total Population / Total Workers aged / Total population a / Total Workers aged
    - b003「データセット_キーワード」category 0.94: 調査 / 調査 / 工業;統計 / 調査
- R223 b050-0039「Evaluation criteria and weightings」: Company Overview, 
    - b010「SITUACAO」category 0.91: Possui Relatório T / Fase de aproximaçã / Instaurado o proce / Titulação da área 
    - b008「Title complement」category 0.90: Insurance corporat / Non financial corp / Insurance corporat / Deposit taking cor
    - g「GroupingTerm」category 0.90: Heart / Behaviour / Behaviour / Hematology
- R224 b023-0108「Life Guard Service」: There is one lifeg / There is one lifeg / There is one lifeg / There are 1-2 life / There is one lifeg
    - b006「駐車場情報」category 0.96: 無し / 無し / 無し / 駐車スペース20台・身障者用駐車場1
    - b2「CONTRAVENTION」category 0.94: 40 IN DISABLED BAY / 11 PARKED WITHOUT  / 01 PARKED IN A RES / 12 PARKED IN A RES
    - b010「holiday」category 0.94: ANZAC Day; Good Fr / ANZAC Day; Good Fr / ANZAC Day; Good Fr / ANZAC Day; Good Fr
- R225 b060-0137「Measure」: Magistrates' Court / All data relates t / Employee Engagemen / Crown Court - Conv / 1. CPS data are av
    - b011「区分３」category 0.95: 実施率（％） / 勧告（件） / 実施 / 対象（箇所）
    - b2「Statistic Label」category 0.95: Percentage of New  / New Entrants to Hi / Percentage of New  / Percentage of New 
    - b010「Indicator」category 0.94: DEATHS BY SUICIDE / CANCER CASES / LOW BIRTHWEIGHT / DIABETES CASES
- R226 b063-0595「TECHNIK」: Seide, Kapok, Watt / Kohle auf Papier / Öl auf Leinwand / Seide, Kapok, Watt / Bronze, schwarz pa
    - syn「Shipping Method Title」category 0.94: 
    - b011「material」category 0.92: Not Applicable / Timber bench seat / Timber Steel / Timber seat with b
    - b013「PrimTech」category 0.92: Hydrogen / Pumped Hydro Energ / Solar Thermal / Enabling
- R227 b056-0063「Target」: >= 80% completed w / >= 80% completed w / >= 80% completed w / >= 80% completed w / >= 80% completed w
    - b003「データセット_キーワード」category 0.93: 調査 / 調査 / 工業;統計 / 調査
    - b003「データセット_キーワード」category 0.92: 位置情報・子育て・児童クラブ・児童館 / 年齢別人口 / 位置情報・公民館・放課後子ども教室 / 位置情報・町営駐車場
    - b004「利用可能曜日」category 0.92: 第３月曜日除く / 年中無休 / 12/29〜1/3を除く / 12/29〜1/3を除く
- R228 b056-0066「Target」: >= 80% completed w / >= 80% completed w / >= 80% completed w / >= 80% completed w / >= 80% completed w
    - b003「データセット_キーワード」category 0.93: 調査 / 調査 / 工業;統計 / 調査
    - b003「データセット_キーワード」category 0.92: 位置情報・子育て・児童クラブ・児童館 / 年齢別人口 / 位置情報・公民館・放課後子ども教室 / 位置情報・町営駐車場
    - b004「利用可能曜日」category 0.92: 第３月曜日除く / 年中無休 / 12/29〜1/3を除く / 12/29〜1/3を除く
- R229 b063-0560「Titelvariante」: Lokalisierung unsi
    - b010「holiday」category 0.90: ANZAC Day; Good Fr / ANZAC Day; Good Fr / ANZAC Day; Good Fr / ANZAC Day; Good Fr
    - b003「定休日」category 0.89: 月 / 土日祝 / 土日祝 / 土日祝
    - b005「開催パターン」category 0.89: 毎年5月頃に開催 / 毎年2月に開催予定 / 毎年9月に開催 / 毎年10月に開催
- R230 b022-0048「indicator」: Square metres of p / Own-source revenue / Number of mental h / Subjective Wellbei / Kilometres of ligh
    - b006「Indicator」category 0.96: Up-to-date cervica / Disability status  / Average hours of s / Ever had chronic o
    - b002「Measure」category 0.93: Coronary heart dis / Lack of social and / Mammography use am / Food insecurity in
    - b008「Statistic」category 0.93: Important Factors  / Important Factors  / Important Factors  / Important Factors 
- R231 b022-0038「indicator_descriptor」: Percentage of the  / Percentage of comm / Energy (electricit / Percentage of the  / Number of cell pho
    - b006「Indicator」category 0.92: Up-to-date cervica / Disability status  / Average hours of s / Ever had chronic o
    - b002「Measure」category 0.89: Coronary heart dis / Lack of social and / Mammography use am / Food insecurity in
    - b010「SITUACAO」category 0.89: Possui Relatório T / Fase de aproximaçã / Instaurado o proce / Titulação da área 
- R232 b063-0263「label」: züric / abwassermonitoring / Ehe / Fussball / wollishofen
    - b010「feature」category 0.93: Nest / Timber with iron / Spit Bay camp boun / Nests
    - b010「Instrument」category 0.93: Imageur tout-ciel / Ionosonde digitale / Imageur tout-ciel / FESOÿ
    - b010「type」category 0.92: Activity Frame / Swing / Shadesail / Spring Rider
- R233 b062-0362「plan」: Runnymede 2030 Loc / Runnymede 2030 Loc / Runnymede 2030 Loc / Runnymede 2030 Loc / Runnymede 2030 Loc
    - b「class-title_en」category 0.83: Domestic pet treat / Cut flowers / Fibrous crop seeds / Spice crop seeds a
    - b2「Item」category 0.81: Capital grants to  / Capital grants to  / Subsidies - Centra / Subsidies - Grants
    - b「family-title_fr」category 0.81: Minéraux, minerais / Animaux vivants / Minéraux, minerais / Semences, bulbes, 
- R234 b062-0358「plan」: 
    - b「class-title_en」category 0.82: Domestic pet treat / Cut flowers / Fibrous crop seeds / Spice crop seeds a
    - b2「Item」category 0.82: Capital grants to  / Capital grants to  / Subsidies - Centra / Subsidies - Grants
    - b「family-title_fr」category 0.81: Minéraux, minerais / Animaux vivants / Minéraux, minerais / Semences, bulbes, 
- R235 b064-0318「qualitaet」: Messgenauigkeit: + / Ablesegenauigkeit: / Messgenauigkeit: + / Ablesegenauigkeit: / Messgenauigkeit: +
    - b002「Measure」category 0.94: Coronary heart dis / Lack of social and / Mammography use am / Food insecurity in
    - b008「Metric」category 0.92: Resources With Bro / High Value Dataset / ga:avgSessionDurat / totalUsers
    - b006「Measure」category 0.92: Taking medicine fo / Binge drinking amo / Visits to doctor f / High blood pressur
- R236 b063-0711「series」: Meldelisten für in / Meldelisten für in / Meldelisten für in / Meldelisten für in / Meldelisten für in
    - b006「ballot_title_2」category 0.91: BOT 01-0260 PCO / HOLLYWOOD PCO / RNT 11-0354 PCO / ROUNDTABLE PCO
    - b2「Funding_Line」category 0.90: Adult Skills Budge / Adult Skills Budge / 24+ Advanced Learn / Adult Skills Budge
    - b006「CASE_TITLE」category 0.90: Street Light Outag / Park Maintenance:  / Unsatisfactory Liv / General Lighting R
- R237 b064-0433「short_title_de_CH」: Ernährungsinitiati / Ernährungsinitiati / Ernährungsinitiati / Ernährungsinitiati / Ernährungsinitiati
    - b004「実施サービス」category 0.94: 居宅療養管理指導;介護予防居宅療養管 / 訪問看護;訪問リハビリテーション;居 / 居宅療養管理指導;介護予防居宅療養管 / 訪問看護;居宅療養管理指導;介護予防
    - b008「用途」category 0.93: 官公署及び出先機関、警察署及び派出所 / 住居併用店舗・事務所（物販・飲食・美 / 野菜、穀物、生花、苗木など草本性植物 / 右記の併用工場、作業所併用住宅
    - b014「Title」category 0.93: Chief Executive Of / SVP, Legal and Com / Principal Officer / President and Chie
- R238 b064-0436「short_title_rm_CH」: Iniziativa d’alime / Iniziativa d’alime / Iniziativa d’alime / Iniziativa d’alime / Iniziativa d’alime
    - b006「CASE_TITLE」category 0.95: Street Light Outag / Park Maintenance:  / Unsatisfactory Liv / General Lighting R
    - b004「実施サービス」category 0.95: 居宅療養管理指導;介護予防居宅療養管 / 訪問看護;訪問リハビリテーション;居 / 居宅療養管理指導;介護予防居宅療養管 / 訪問看護;居宅療養管理指導;介護予防
    - b010「holiday」category 0.95: ANZAC Day; Good Fr / ANZAC Day; Good Fr / ANZAC Day; Good Fr / ANZAC Day; Good Fr
- R239 b064-0429「title_de_CH」: Ernährungsinitiati / Ernährungsinitiati / Ernährungsinitiati / Ernährungsinitiati / Ernährungsinitiati
    - b013「title_en」category 0.93: President / Acting Chief Trans / President / Vice-President, Pr
    - b014「Title」category 0.93: Chief Executive Of / SVP, Legal and Com / Principal Officer / President and Chie
    - b006「ballot_title_1」category 0.93: Precinct Committee / Precinct Committee / Precinct Committee / Precinct Committee
- R240 b064-0432「title_rm_CH」: Iniziativa d’alime / Iniziativa d’alime / Iniziativa d’alime / Iniziativa d’alime / Iniziativa d’alime
    - b006「CASE_TITLE」category 0.95: Street Light Outag / Park Maintenance:  / Unsatisfactory Liv / General Lighting R
    - b010「Claim」category 0.95: PTSD (Single Condi / PTSD (Single Condi / PTSD (Single Condi / Hearing Loss (Sing
    - b007「利用可能曜日」category 0.95: 月火水木金 / 12月29日から 翌年1月3日以外 / 年中無休 / 月火水木金
- R241 b063-0396「traktandum_beschlussdetail_deutsch」: Ziffer 1: Ablehnun / Ziffer 1: Annahme  / Annahme: 144 Ja, 0 / Annahme: 85 Ja, 60 / Ziffer 1: Annahme 
    - b013「indicateur de resultats ministeriels」category 0.91: Pourcentage du tem / Pourcentage du tem / Pourcentage du tem / Pourcentage du tem
    - b014「PAL*の低減率」category 0.91: 20%以上 / 15%以上 / 15%以上 / 10%以上
    - b2「Grant Expenditure Rate」category 0.90: Band 4 Non-Adjacen / Student Part-Time  / Band 4 Adjacent / 50% tuition fees o
- R242 b063-0397「traktandum_beschlussdetail_franz」: Chiffre 1 : adopti / Chiffre 1 : adopti / Chiffre 1 : rejet  / Adoption : 133 oui / avec charges
    - b008「Statistic」category 0.93: Important Factors  / Important Factors  / Important Factors  / Important Factors 
    - b2「CONTRAVENTION」category 0.91: 40 IN DISABLED BAY / 11 PARKED WITHOUT  / 01 PARKED IN A RES / 12 PARKED IN A RES
    - b003「データセット_キーワード」category 0.91: 調査 / 調査 / 工業;統計 / 調査
- R243 b064-0253「Öffnungszeiten」: Gemäss Webseite / Gemäss Webseite / Gemäss Webseite / gemäss Webseite / Gemäss Webseite
    - b008「用途」category 0.96: 官公署及び出先機関、警察署及び派出所 / 住居併用店舗・事務所（物販・飲食・美 / 野菜、穀物、生花、苗木など草本性植物 / 右記の併用工場、作業所併用住宅
    - b005「支援内容」category 0.96: 玉名市災害ボランティアセンター / り災・被災証明書の受付窓口 / り災・被災証明書の受付窓口 / 災害ごみ仮置き場
    - b004「実施サービス」category 0.96: 居宅療養管理指導;介護予防居宅療養管 / 訪問看護;訪問リハビリテーション;居 / 居宅療養管理指導;介護予防居宅療養管 / 訪問看護;居宅療養管理指導;介護予防
- R244 b055-0139「対象」: すべての保育所職員、幼稚園教職員、学 / 訪問看護ステーション職員、介護保険・ / 医師会会員及び看護師、保育所等の看護 / すべての保育所職員、幼稚園教職員、学 / すべての保育所職員、幼稚園教職員、学
    - b008「Title complement」category 0.94: Insurance corporat / Non financial corp / Insurance corporat / Deposit taking cor
    - b004「利用可能曜日」category 0.94: 第３月曜日除く / 年中無休 / 12/29〜1/3を除く / 12/29〜1/3を除く
    - b009「事項」category 0.93: 検査・相談体制の充実 / 療養支援体制の確保 / 調査・研究の推進 / 計(千円)
- R245 b055-0144「指標「ひまわり」の糖尿病関連項目より」: (1)／外来診療／経口糖尿病薬の導入 / (7)／患者教育／糖尿病患者への運動 / (3)／外来診療／インスリン療法の導 / (2)／外来診療／経口糖尿病薬で血糖 / (6)／患者教育／糖尿病患者への栄養
    - b003「データセット_キーワード」category 0.96: 一覧・位置情報・子育て施設 / 食品・食品営業許可施設・食品等営業許 / 一覧・中学校区・小学校区・教育 / 選挙・開票結果
    - b「データセット_キーワード」category 0.96: 大気;汚染 / ホテル;旅館 / 大気;汚染 / 大気;汚染
    - b003「項目」category 0.95: クラウド / コラボレーション / データを読む・説明する / 顧客価値の変化

## text→date

- R246 b064-0370「Datierung_Bemerkung」: 
    - b005「開催日時（表示用）」date 0.95: 12月19日（日）午後１時 / ９月15日（水）午前10時、16日（ / ９月12日（日）午前９時＝雨天中止 / ８月27日（金）午後２時
    - b004「終了時間」date 0.95: 17:00 / 17:00（3月～6月、10月、11 / 17:00 / 18:00（物産館） 18:00（レ
    - b013「Opening_Hours_Tue_Open」date 0.95: 1:00PM / 10:00AM / 05:00AM / 9:00AM

## text→other

- R247 b064-0372「Widmung」: 
    - g「mood」other 0.87: 12.0 / 12.0 / 12.0 / 12.0
    - g「Method」other 0.87: FromCircleRadius / FromCentigramsPerM / TryParse / ToString
    - b008「Elevation」other 0.85: 158 to 199m / Between 168 and 23 / 159 to 184m / 136 to 155mm

## text→person

- R248 b064-0366「Titel」: Reinhart, Josef an / Wöhler, Friedrich  / Lumière, Louis an  / Schomburgk, Richar / Kirchhoff, Gustav 
    - g「Authors」person 0.80: H Kakizaki, MO Fra / James W. Grau, J.  / YS Nout, MH Schmid / WC de Groat, N Yos
    - g「trackback_author_nick」person 0.79: dvtlite / rachel_rwr / madamjrose / jdgalvin
    - g「creator」person 0.79: Shine, James M. et / Abeliovich, Asa; G / Bansal, Kanika, et / Reyes, Pablo Alexa
