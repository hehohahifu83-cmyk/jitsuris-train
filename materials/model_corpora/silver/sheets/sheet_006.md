# 銀ラベルのシート 006 / 008（外の学習データの読み替え）

- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列
- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`
- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前
- **Wikidata の型の読み方**：`wikibase-entityid` は「ほかの項目へのつながり」で、**値は名前**（首都なら都市の名前、議会なら組織の名前）。**番号（id）という意味ではない**ので、値で決める。`string` は文字列（コード・ファイル名・URL も入る）、`quantity` は数、`time` は日付、`globecoordinate` は座標、`monolingualtext` はある言語の文字
- SOTAB の元の種類は Schema.org の名前（`postalCode`＝郵便番号、`price`＝価格、`Date`＝日付、`addressLocality`＝市町村 など）。値と元の種類で LABEL_GUIDE の種類に読み替える
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を、ChatGPT は `answers/sheet_006.tsv`、Grok は `answers_grok/sheet_006.tsv` に写して埋める。**相手の答えは見ない**

## g0751 — wikidbs10k：見出し「cospar id」（Wikidata の型 `string`）（22 列）
- 例1：2004-013A | 2004-040A | 2003-016A | 2003-047A | 2001-054A（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例2：1988-104A | 1994-039A | 1994-036A | 1990-097A | 1996-011A（表：spaceflight／同じ表の列：label, description, SCN, Commons category, UTC date of spacecr…, instance of）
- 例3：1993-043A | 1995-047A | 1988-075A | 1992-026A | 1996-011A（表：follows／同じ表の列：label, description, SCN, Commons category, UTC date of spacecr…, part of）

## g0752 — wikidbs10k：見出し「cvr number」（Wikidata の型 `string`）（22 列）
- 例1：29190623 | 29189404 | 11715311 | 58271713 | 29189129（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例2：19438414 | 64942212 | 29188335 | 65120119 | 63640719（表：political border／同じ表の列：label, description, capital, country, located in the admi…, Commons category）
- 例3：26321514 | 27997716 | 69054412 | 44835010 | 52421411（表：West Zealand County／同じ表の列：label, description, coordinate location, country, Freebase ID, instance of）

## g0753 — wikidbs10k：見出し「ehak id」（Wikidata の型 `string`）（22 列）
- 例1：792.0 | 725.0 | 247.0 | 803.0 | 0060（表：administrative territorial entity／同じ表の列：label, description, Commons category, flag image, coat of arms image, country）
- 例2：0751 | 0411 | 0531 | 0318 | 0297（表：replaced entity／同じ表の列：label, description, replaced by, instance of, located in the admi…, country）
- 例3：0430 | 0725 | 0502 | 0792 | 0191（表：replacing subject／同じ表の列：label, description, Commons category, flag image, coat of arms image, country）

## g0754 — wikidbs10k：見出し「hgnc id」（Wikidata の型 `string`）（22 列）
- 例1：3012 | 3430 | 1097 | 6840 | 3236（表：biological variant of／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）
- 例2：1445 | 10592 | 6242 | 1529 | 1390（表：genetic association／同じ表の列：label, description, Entrez Gene ID, HGNC gene symbol, OMIM ID, subclass of）
- 例3：29105 | 7225 | 2277 | 2974 | 23791（表：genetic association／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）

## g0755 — wikidbs10k：見出し「lokalhistoriewiki.no id」（Wikidata の型 `string`）（22 列）
- 例1：Porsanger_kommune | Alta_kommune | Sør-Varanger_kommune | Bardu_kommune | Karasjok_kommune（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coat of arms image, Commons category, coordinate location）
- 例2：Snåsa_kommune | Overhalla_kommune | Loppa_kommune | Hemnes_kommune | Hasvik_kommune（表：political border／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）
- 例3：Kongsberg_kommune | Malvik_kommune | Stryn_kommune | Stjørdal_kommune | Lenvik_kommune（表：administrative territorial entity／同じ表の列：label, description, coat of arms image, shares border with, Commons category, coordinate location）

## g0756 — wikidbs10k：見出し「nbic taxon id」（Wikidata の型 `string`）（22 列）
- 例1：103748 | 99431 | 100718 | 79525 | 101686（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：105273 | 152510 | 105362 | 187938 | 75956（表：taxon／同じ表の列：label, description, parent taxon, image, topic's main catego…, taxon name）
- 例3：53924 | 54695 | 57666 | 53326 | 54683（表：taxon／同じ表の列：label, description, MycoBank taxon name…, Encyclopedia of Lif…, taxon rank, taxon name）

## g0757 — wikidbs10k：見出し「norwegian municipality number」（Wikidata の型 `string`）（22 列）
- 例1：5440 | 5436 | 5441 | 5033 | 5437（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coat of arms image, Commons category, coordinate location）
- 例2：5432.0 | 5438 | 5038 | 5434 | 5424.0（表：political border／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）
- 例3：4644 | 4206 | 5037 | 4620 | 3006（表：administrative territorial entity／同じ表の列：label, description, coat of arms image, shares border with, Commons category, coordinate location）

## g0758 — wikidbs10k：見出し「racing-reference track id」（Wikidata の型 `string`）（22 列）
- 例1：Burke_Lakefront_Airport | Portland_Intenational_Raceway | Streets_Of_Denver | Pacific_Place | Autodromo_Hermanos_Rodriguez（表：physical location／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例2：Charlotte_Motor_Speedway | Rockingham_Speedway | Bristol_Motor_Speedway | Dover_International_Speedway | North_Wilkesboro_Speedway（表：physical location／同じ表の列：label, description, coordinate location, country, located in the admi…, Freebase ID）
- 例3：Columbia_Speedway | Charlotte_Motor_Speedway | Bristol_Motor_Speedway | Hickory_Speedway | Rockingham_Speedway（表：physical location／同じ表の列：label, description, coordinate location, country, located in the admi…, Freebase ID）

## g0759 — wikidbs10k：見出し「scn」（Wikidata の型 `string`）（22 列）
- 例1：27440.0 | 27781.0 | 28640 | 26603.0 | 26995.0（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例2：23798 | 23139 | 22000 | 23173 | 19660（表：spaceflight／同じ表の列：label, description, COSPAR ID, Commons category, UTC date of spacecr…, instance of）
- 例3：20841 | 23665 | 25146 | 22704 | 23042（表：follows／同じ表の列：label, description, COSPAR ID, Commons category, UTC date of spacecr…, part of）

## g0760 — wikidbs10k：見出し「simc place id」（Wikidata の型 `string`）（22 列）
- 例1：0977539 | 0190495 | 0936026 | 0936931 | 0964710（表：place of birth／同じ表の列：label, description, country, located in the admi…, coordinate location, instance of）
- 例2：0942630 | 0981570 | 0028926 | 0984120 | 0782876（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, coordinate location, GeoNames ID）
- 例3：0864261 | 0298614 | 0240336 | 0239971 | 0103510（表：colony／同じ表の列：label, description, coordinate location, country, located in the admi…, instance of）

## g0761 — wikidbs10k：見出し「category related to list」（Wikidata の型 `wikibase-entityid`）（22 列）
- 例1：Category:Cultural property in Triesenbe… | Category:Cultural property in Planken | Category:Cultural property in Schaan | Category:Cultural property in Triesen | Category:Cultural property in Mauren（表：monument／同じ表の列：label, description, instance of, is a list of, country, Commons category）
- 例2：Category:Cultural property in Schellenb… | Category:Cultural property in Triesen | Category:Cultural property in Vaduz | Category:Cultural property in Mauren | Category:Cultural property in Eschen（表：Wikimedia list article／同じ表の列：label, description, instance of, is a list of, country, Commons category）
- 例3：Category:National Register of Historic … | Category:National Register of Historic … | Category:National Register of Historic … | Category:National Register of Historic … | Category:National Register of Historic …（表：monument／同じ表の列：label, description, Commons category, is a list of, country, instance of）

## g0762 — wikidbs10k：見出し「conflict」（Wikidata の型 `wikibase-entityid`）（22 列）
- 例1：World War II（表：31st U-boat Flotilla／同じ表の列：label, description, operator, instance of, vessel class, location of creation）
- 例2：World War I | World War II | Battle of Jutland | Ice Cruise of the Baltic Fleet（表：dreadnought／同じ表の列：label, description, Commons category, instance of, Freebase ID, image）
- 例3：World War II（表：33rd U-boat Flotilla／同じ表の列：label, description, Freebase ID, instance of, operator, vessel class）

## g0763 — wikidbs10k：見出し「copyright license」（Wikidata の型 `wikibase-entityid`）（22 列）
- 例1：MIT license | CC0 | GNU Affero General Public License, vers… | GNU Lesser General Public License, vers… | GNU Lesser General Public License, vers…（表：encryption software／同じ表の列：label, description, instance of, official website, programmed in）
- 例2：GNU Affero General Public License, vers… | GNU General Public License, version 3.0 | GNU Affero General Public License | GNU General Public License, version 2.0… | 3-clause BSD License（表：Internet forum software／同じ表の列：label, description, instance of, programmed in, official website, software version id…）
- 例3：GNU General Public License, version 2.0 | GNU Lesser General Public License, vers… | Mozilla Public License, version 1.1 | 2-clause BSD License | GNU Lesser General Public License, vers…（表：graphics library／同じ表の列：label, description, official website, programmed in, instance of, copyright status）

## g0764 — wikidbs10k：見出し「month of the year」（Wikidata の型 `wikibase-entityid`）（22 列）
- 例1：June | May | August | December | January（表：first Monday of the month／同じ表の列：label, description, instance of, subclass of, day of week）
- 例2：February | March | May | August | June（表：last weekday of the month／同じ表の列：label, description, instance of, subclass of）
- 例3：Fructidor | Frimaire | Thermidor | Germinal | Nivôse（表：month of the French Republican Calendar／同じ表の列：label, description, instance of, part of）

## g0765 — wikidbs10k：見出し「occupation」（Wikidata の型 `wikibase-entityid`）（22 列）
- 例1：politician（表：candidate／同じ表の列：label, description, instance of, name, member of political…, position held）
- 例2：biologist | molecular biologist | organizational founder | bioinformatician | geneticist（表：author／同じ表の列：label, description, ORCID iD, instance of）
- 例3：politician（表：candidate／同じ表の列：label, description, instance of, name, member of political…, position held）

## g0766 — wikidbs10k：見出し「original broadcaster」（Wikidata の型 `wikibase-entityid`）（22 列）
- 例1：CBS | GMA Network | Canal+ | Las Estrellas | Disney+（表：anthology series／同じ表の列：label, description, instance of, genre, country of origin, original language o…）
- 例2：NBC | Fox Broadcasting Company | TNT | American Broadcasting Company | CBS（表：series／同じ表の列：label, description, instance of, IMDb ID, genre, original language o…）
- 例3：American Broadcasting Company | NBC | Seven Network | CBS | GMA Network（表：work／同じ表の列：label, description, IMDb ID, country of origin, topic's main catego…, Freebase ID）

## g0767 — wikidbs10k：見出し「surface played on」（Wikidata の型 `wikibase-entityid`）（22 列）
- 例1：clay court | grass court | hardcourt | carpet court（表：1972 Grand Prix circuit／同じ表の列：label, description, sport, instance of, point in time, country）
- 例2：carpet court | clay court（表：1976 World Championship Tennis circuit／同じ表の列：label, description, sport, instance of, point in time, located in the admi…）
- 例3：carpet court | hardcourt（表：Lorraine Open／同じ表の列：label, description, country, sport, instance of, point in time）

## g0768 — wikidbs10k：見出し「maximum capacity」（Wikidata の型 `quantity`）（21 列）
- 例1：+35000 | 8000.0 | 12000.0 | 4000.0 | 3000.0（表：physical location／同じ表の列：label, description, instance of, located in the admi…, Commons category, coordinate location）
- 例2：+17000 | +10129 | +15400 | +17341 | +20328（表：stadium／同じ表の列：label, description, instance of, coordinate location, country, located in the admi…）
- 例3：+5500 | +15000 | +27000 | +53000 | +20000（表：physical location／同じ表の列：label, description, coordinate location, Freebase ID, located in the admi…, owned by）

## g0769 — wikidbs10k：見出し「students count」（Wikidata の型 `quantity`）（21 列）
- 例1：+119 | +3006 | +196 | +476 | +8077（表：school district of Oregon／同じ表の列：label, description, country, instance of, located in the admi…, NCES district ID）
- 例2：+11650 | +6885 | +56000 | +47090 | +14999（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例3：+30318 | +6200 | +2820 | +12002 | +9535（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）

## g0770 — wikidbs10k：見出し「czech municipality id」（Wikidata の型 `string`）（21 列）
- 例1：592005 | 544256 | 595209 | 531057 | 554782（表：headquarters／同じ表の列：label, description, instance of, country, population, flag image）
- 例2：556106.0 | 555088 | 501646.0 | 539881.0 | 554316（表：political border／同じ表の列：label, description, Commons category, located in the admi…, country, LAU）
- 例3：588296 | 590266 | 535419 | 569810 | 554782（表：capital city／同じ表の列：label, description, instance of, country, population, flag image）

## g0771 — wikidbs10k：見出し「hgnc gene symbol」（Wikidata の型 `string`）（21 列）
- 例1：EGFR | ERBB2 | ALK | KIT | PDGFRA（表：biological variant of／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）
- 例2：KCNH2 | KCNE2 | CALM1 | KCNJ5 | CALM2（表：genetic association／同じ表の列：label, description, Entrez Gene ID, HGNC ID, OMIM ID, subclass of）
- 例3：COX6A1 | PLEKHG5 | GNB4 | YARS1 | KARS1（表：genetic association／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）

## g0772 — wikidbs10k：見出し「image archive, herder institute」（Wikidata の型 `string`）（21 列）
- 例1：Q502993 | Q14960 | Q180139 | Q146351 | Q1774142（表：headquarters／同じ表の列：label, description, instance of, country, population, flag image）
- 例2：Q191805 | Q36989 | Q16506 | Q43453 | Q158239（表：capital city／同じ表の列：label, description, instance of, country, population, flag image）
- 例3：Q45581 | Q167477 | Q8018 | Q44269 | Q345（表：patron saint／同じ表の列：label, description, Commons category, instance of, topic's main catego…, Freebase ID）

## g0773 — wikidbs10k：見出し「image of design plans」（Wikidata の型 `string`）（21 列）
- 例1：Surfers Paradise Street Circuit.svg | Laguna Seca.svg | The Milwaukee Mile.svg | Fundidora Park Raceway.svg | Portland international raceway.svg（表：physical location／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例2：Michigan International Speedway track m… | Atlanta Motor Speedway.svg | NorthWilkesboroSpeedwayMap.svg | Charlotte Motor Speedway diagram.svg | Circuit Riverside.svg（表：physical location／同じ表の列：label, description, coordinate location, country, located in the admi…, Freebase ID）
- 例3：Indianapolis Oval.svg | Pocono Raceway.svg | Road America.svg | Phoenix-international-raceway.svg | Watkins Glen International Track Map.svg（表：physical location／同じ表の列：label, description, Commons category, instance of, coordinate location, country）

## g0774 — wikidbs10k：見出し「municipality code (denmark)」（Wikidata の型 `string`）（21 列）
- 例1：165.0 | 167.0 | 151.0 | 157 | 201.0（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例2：163 | 161 | 101 | 187 | 157（表：political border／同じ表の列：label, description, capital, country, located in the admi…, Commons category）
- 例3：333 | 303 | 323 | 341 | 345（表：West Zealand County／同じ表の列：label, description, coordinate location, country, Freebase ID, instance of）

## g0775 — wikidbs10k：見出し「official number of town quarter」（Wikidata の型 `string`）（21 列）
- 例1：48 | 13 | 4 | 38 | 22（表：neighbourhood of Helsinki／同じ表の列：label, description, Commons category, country, coordinate location, Freebase ID）
- 例2：16 | 14 | 22 | 9 | 6（表：quarter of Palermo／同じ表の列：label, description, Google Knowledge Gr…, instance of, population, official name）
- 例3：22 | 20 | 7 | 14 | 18（表：political border／同じ表の列：label, description, locator map image, Google Knowledge Gr…, instance of, population）

## g0776 — wikidbs10k：見出し「romeo publisher id」（Wikidata の型 `string`）（21 列）
- 例1：4 | 113 | 177 | 17 | 15（表：publisher／同じ表の列：label, description, official website, instance of, inception, headquarters locati…）
- 例2：131 | 113 | 30 | 4 | 54（表：publisher／同じ表の列：label, description, official website, VIAF ID, instance of, headquarters locati…）
- 例3：16 | 3 | 22 | 218 | 11（表：publisher／同じ表の列：label, description, Freebase ID, VIAF ID, Library of Congress…, inception）

## g0777 — wikidbs10k：見出し「distributed by」（Wikidata の型 `wikibase-entityid`）（21 列）
- 例1：Nintendo eShop（表：work／同じ表の列：label, description, part of the series, genre, platform, game mode）
- 例2：Warner Bros. Television Studios | Netflix | Walt Disney Studios Home Entertainment | Paramount Media Networks | NBCUniversal Syndication Studios（表：series／同じ表の列：label, description, instance of, IMDb ID, genre, original language o…）
- 例3：New Line Cinema | Anchor Bay Entertainment | Pyramid Saimira | UIP-Dunafilm | Miramax（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）

## g0778 — wikidbs10k：見出し「lyrics by」（Wikidata の型 `wikibase-entityid`）（21 列）
- 例1：Kate Bush（表：audio recording／同じ表の列：label, description, instance of, title, language of work or…, composer）
- 例2：Henry Carey | Eusebio Lillo | Oreste Sindici | Pedro I of Brazil | Juan León Merai（表：anthem／同じ表の列：label, description, instance of, Commons category, MusicBrainz work ID, Freebase ID）
- 例3：Maxwell Anderson | Howard Dietz | Alan Brandt | Ira Gershwin | Johnny Mercer（表：Great American Songbook／同じ表の列：label, description, MusicBrainz work ID, Freebase ID, instance of, language of work or…）

## g0779 — wikidbs10k：見出し「mountain range」（Wikidata の型 `wikibase-entityid`）（21 列）
- 例1：Sierra Madre de Chiapas | Andes | Principal Cordillera | Wilhelmina Mountains | Pacaraima Mountains（表：highest point／同じ表の列：label, description, instance of, continent, coordinate location, country）
- 例2：Yatsugatake Mountains | Tsukuba Mountains | Arakawa Mountains | Ishikari Mountains | Chūgoku Mountains（表：100 Famous Japanese Mountains／同じ表の列：label, description, instance of, Commons category, country, coordinate location）
- 例3：Tateyama Mountains | Tsukuba Mountains | Chūgoku Mountains | Kiso Mountains | Arakawa Mountains（表：highest point／同じ表の列：label, description, instance of, Commons category, coordinate location, GeoNames ID）

## g0780 — wikidbs10k：見出し「sponsor」（Wikidata の型 `wikibase-entityid`）（21 列）
- 例1：National Institute for Occupational Saf…（表：Second NIOSH solid sorbents roundtable／同じ表の列：label, description, NIOSHTIC-2 ID, publication date, author name string, instance of）
- 例2：National Institute for Occupational Saf…（表：3rd Symposium on Respirable Dust in the…／同じ表の列：label, description, NIOSHTIC-2 ID, publication date, author name string, instance of）
- 例3：National Institute for Occupational Saf…（表：7th International aerosol conference [a…／同じ表の列：label, description, NIOSHTIC-2 ID, publication date, author name string, instance of）

## g0781 — wikidbs10k：見出し「number of speakers, writers, or signers」（Wikidata の型 `quantity`）（20 列）
- 例1：1251770.0 | 10700000.0 | 27300000.0 | 7000000.0 | 2400000.0（表：Wikimedia category／同じ表の列：label, description, OmegaWiki Defined M…, ISO 639-1 code, ISO 639-2 code, ISO 639-3 code）
- 例2：23100000.0 | 753359540.0 | 5413380.0 | 4079420.0 | 208157220.0（表：Wikimedia category／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例3：9244250.0 | 23100000.0 | 208157220.0 | 2400000.0 | 753359540.0（表：Wikimedia category／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0782 — wikidbs10k：見出し「orbital period」（Wikidata の型 `quantity`）（20 列）
- 例1：88.5 | 88.7 | +92.6 | 91.9 | 92.3（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例2：+92.29 | +90.5 | +92.48 | +88.8 | +88.5（表：spaceflight／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）
- 例3：+88.4 | +90.6 | +88.6 | +92.29 | +92.4（表：follows／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）

## g0783 — wikidbs10k：見出し「code」（Wikidata の型 `string`）（20 列）
- 例1：௰௯ | ௨ | ௭ | ௩௰௭ | ௰௩（表：prime factor／同じ表の列：label, description, instance of, Commons category, numeric value, Unicode character）
- 例2：4.0 | 10.0 | 16.0 | 6.0 | 12.0（表：administrative territorial entity／同じ表の列：label, description, topic's main Wikime…, located in the admi…, shares border with, contains the admini…）
- 例3：-.-. | --.- | --.. | .. | --.（表：Italian alphabet／同じ表の列：label, description, Commons category, Unicode character, Commons gallery, part of）

## g0784 — wikidbs10k：見出し「encyclopedia of modern ukraine id」（Wikidata の型 `string`）（20 列）
- 例1：72433.0 | 32681.0 | 12857.0 | 3527.0 | 42407.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：32681.0 | 3527.0 | 42407.0 | 72433.0 | 12857.0（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：17983 | 12857 | 33439 | 11020 | 12201（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0785 — wikidbs10k：見出し「great aragonese encyclopedia id」（Wikidata の型 `string`）（20 列）
- 例1：7780 | 3353 | 1746 | 480 | 3411（表：La Franja／同じ表の列：label, description, Commons category, country, postal code, coordinate location）
- 例2：3121 | 8047 | 6522 | 10819 | 13181（表：administrative territorial entity／同じ表の列：label, description, capital, country, Commons category, coordinate location）
- 例3：7780 | 8740 | 2136 | 2339 | 4526（表：workplace／同じ表の列：label, description, Commons category, country, postal code, coordinate location）

## g0786 — wikidbs10k：見出し「imslp id」（Wikidata の型 `string`）（20 列）
- 例1：Symphony_No.44_in_D_major,_K.81/73l_(Mo… | Symphony_No.45_in_D_major,_K.95/73n_(Mo… | Symphony_No.11_in_D_major,_K.84/73q_(Mo… | Symphony_No.48_in_D_major,_K.120/111a_(… | Symphony_No.30_in_D_major,_K.202/186b_(…（表：list of compositions by Wolfgang Amadeu…／同じ表の列：label, description, instance of, part of, tonality, composer）
- 例2：Category:F_major | Category:G_major | Category:G_minor | Category:B_major | Category:D_major（表：key／同じ表の列：label, description, Commons category, Freebase ID, image, followed by）
- 例3：Category:B_major | Category:G-flat_major | Category:C-sharp_major | Category:A-flat_major | Category:B-flat_major（表：followed by／同じ表の列：label, description, Commons category, Freebase ID, image, followed by）

## g0787 — wikidbs10k：見出し「niconicopedia id」（Wikidata の型 `string`）（20 列）
- 例1：南アフリカ | アメリカ合衆国 | オーストラリア | 韓国 | イギリス（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, Libraries Australia…, coordinates of sout…）
- 例2：香港特別行政区 | 朝鮮 | ドイツ | アメリカ合衆国 | フランス（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：ロシア | 中華人民共和国 | アルゼンチン | 韓国 | イギリス（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0788 — wikidbs10k：見出し「spoken text audio」（Wikidata の型 `string`）（20 列）
- 例1：Hy-Ավստրալիա (Australia).ogg | Nl-Rusland-article.ogg | Nl-Frankrijk-article.ogg | Hy-Նորվեգիա (Norway).ogg | Nl-Verenigde Staten van Amerika-article…（表：country／同じ表の列：label, description, median income, Great Russian Encyc…, WIPO ST.3, Getty Thesaurus of …）
- 例2：Nl-3 (getal)-article.ogg | Nl-7 (getal)-article.ogg | Nl-5 (getal)-article.ogg | Nl-19 (getal)-article.ogg | Nl-13 (getal)-article.ogg（表：prime factor／同じ表の列：label, description, instance of, Commons category, numeric value, image）
- 例3：Nl-België-article.ogg | Nl-Verenigde Staten van Amerika-article… | Ru-Republic of China (intro).ogg | Nl-Volksrepubliek China-article.ogg | Nl-Verenigd Koninkrijk-article.ogg（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0789 — wikidbs10k：見出し「čsfd film id」（Wikidata の型 `string`）（20 列）
- 例1：230468 | 310289 | 282024 | 37124 | 267980（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例2：133111 | 295009 | 260861 | 242266 | 82829（表：sixth generation Chinese films／同じ表の列：label, description, IMDb ID, instance of, director, original language o…）
- 例3：490641.0 | 474470.0 | 474556.0 | 577362.0 | 483329.0（表：television series season／同じ表の列：label, description, instance of, Freebase ID, part of the series, number of episodes）

## g0790 — wikidbs10k：見出し「category for alumni of educational institution」（Wikidata の型 `wikibase-entityid`）（20 列）
- 例1：Category:Vanderbilt University alumni | Category:Providence College alumni | Category:DePaul University alumni | Category:Oklahoma City University alumni | Category:Saint Joseph's University alum…（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例2：Category:University of Chicago alumni | Category:École Normale Supérieure alumni | Category:Yale University alumni | Category:Harvard University alumni | Category:Massachusetts Institute of Tec…（表：alma mater／同じ表の列：label, description, instance of, country, Commons category, coordinate location）
- 例3：Category:Pennsylvania State University … | Category:Villanova University alumni | Category:University of Colorado Boulder… | Category:Oregon State University alumni | Category:Marquette University alumni（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）

## g0791 — wikidbs10k：見出し「developer」（Wikidata の型 `wikibase-entityid`）（20 列）
- 例1：StataCorp（表：Stata／同じ表の列：label, description, subclass of, software version id…, publication date, followed by）
- 例2：StataCorp（表：followed by／同じ表の列：label, description, subclass of, follows, software version id…, publication date）
- 例3：StataCorp（表：follows／同じ表の列：label, description, subclass of, software version id…, publication date, followed by）

## g0792 — wikidbs10k：見出し「fastest lap」（Wikidata の型 `wikibase-entityid`）（20 列）
- 例1：Bruno Junqueira | Sébastien Bourdais | Mario Domínguez | Ryan Hunter-Reay | Paul Tracy（表：2004 Champ Car season／同じ表の列：label, description, sport, point in time, instance of, country）
- 例2：Ken Wharton | Stirling Moss | Thomas Randle | Sten Pentus | Mitch Evans（表：New Zealand Grand Prix／同じ表の列：label, description, pole position, instance of, point in time, country）
- 例3：Hélio Castroneves | Sébastien Bourdais | Alex Zanardi | Paul Tracy | Juan Pablo Montoya（表：Molson Indy Vancouver／同じ表の列：label, description, sport, point in time, instance of, country）

## g0793 — wikidbs10k：見出し「has facet polytope」（Wikidata の型 `wikibase-entityid`）（20 列）
- 例1：7-cube | 13-cube | square | side | 17-cube（表：hypercube／同じ表の列：label, description, subclass of, studied by）
- 例2：10-cube | 15-cube | square | cube | 9-cube（表：facet／同じ表の列：label, description, subclass of, studied by）
- 例3：equilateral triangle | square | regular pentagon（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）

## g0794 — wikidbs10k：見出し「space launch vehicle」（Wikidata の型 `wikibase-entityid`）（20 列）
- 例1：Ariane 42L | Zenit-3SL | Proton-M | Ariane 44L | Commercial Titan III（表：JCSAT／同じ表の列：label, description, COSPAR ID, UTC date of spacecr…, SCN, instance of）
- 例2：Starship | Mercury-Redstone Launch Vehicle | Falcon 9 v1.0 | Atlas LV-3B | Space Shuttle（表：flight testing／同じ表の列：label, description, Commons category, UTC date of spacecr…, follows, followed by）
- 例3：Falcon 9 v1.0 | SM-65D Atlas | Little Joe | RM-90 Blue Scout II | Mercury-Redstone Launch Vehicle（表：followed by／同じ表の列：label, description, Commons category, UTC date of spacecr…, part of, follows）

## g0795 — wikidbs10k：見出し「used by」（Wikidata の型 `wikibase-entityid`）（20 列）
- 例1：cyclist | athletics | foil fencing | volleyball player | association football（表：use／同じ表の列：label, description, subclass of, Freebase ID, sport, Commons category）
- 例2：handball player | athletics | boxer | foil fencing | association football（表：use／同じ表の列：label, description, sport, Commons category, Freebase ID, subclass of）
- 例3：Formula One（表：physical location／同じ表の列：label, description, Commons category, instance of, coordinate location, country）

## g0796 — wikidbs10k：見出し「apni id」（Wikidata の型 `string`）（19 列）
- 例1：66663 | 94323 | 84254 | 82010 | 54555（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：73518 | 98541 | 78611 | 102123 | 80480（表：taxon／同じ表の列：label, description, taxon name, Commons category, taxon rank, image）
- 例3：80674 | 4224422 | 81289 | 59238 | 113039（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）

## g0797 — wikidbs10k：見出し「china administrative division code」（Wikidata の型 `string`）（19 列）
- 例1：11 01 05 229 | 11 01 05 242 | 11 01 05 227 | 11 01 05 235 | 11 01 15 115（表：Region (Beijing)／同じ表の列：label, description, country, coordinate location, located in the admi…, instance of）
- 例2：11 01 16 001 | 11 01 14 001 | 11 01 15 001 | 11 01 18 | 11 01 18 001（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例3：31 | 21 | 61 01 | 65 40 02 | 22 03（表：place of birth／同じ表の列：label, description, page banner, located in the admi…, country, Commons category）

## g0798 — wikidbs10k：見出し「every noise at once id」（Wikidata の型 `string`）（19 列）
- 例1：poprock | rock | jpop | hiphop | newwave（表：genre／同じ表の列：label, description, instance of, subclass of, topic's main catego…, Freebase ID）
- 例2：anarchopunk | artrock | pop | rap | poprock（表：genre／同じ表の列：label, description, Commons category, subclass of, topic's main catego…, Freebase ID）
- 例3：countrypop | southerngospel | folk | country | pop（表：genre／同じ表の列：label, description, instance of, Commons category, subclass of, topic's main catego…）

## g0799 — wikidbs10k：見出し「ibnr id」（Wikidata の型 `string`）（19 列）
- 例1：8000297 | 8000443 | 8003286 | 8005160 | 8005708（表：Hanover S-Bahn／同じ表の列：label, description, Commons category, country, image, coordinate location）
- 例2：8002634 | 8003286 | 8000808 | 8000226 | 8004868（表：adjacent station／同じ表の列：label, description, Commons category, instance of, country, coordinate location）
- 例3：5402503 | 5402506 | 5402031 | 5403766 | 5402488（表：Praha–Vrané nad Vltavou–Čerčany Dobříš …／同じ表の列：label, description, Commons category, country, instance of, coordinate location）

## g0800 — wikidbs10k：見出し「ima mineral symbol」（Wikidata の型 `string`）（19 列）
- 例1：Cnv | Jbo | Lsr | Hhb | Brsn（表：borate class of minerals／同じ表の列：label, description, Nickel-Strunz '10th…, named after, subclass of, IMA status and/or r…）
- 例2：Phn | Cqr | Usv | Krg | Ysl（表：neso-aluminofluoride minerals (3.CB.)／同じ表の列：label, description, Strunz 8th edition …, subclass of, chemical formula, Nickel-Strunz 9th e…）
- 例3：Amt | Osh | Sol | Kko | Kht（表：nesoborate mineral subclass／同じ表の列：label, description, Nickel-Strunz '10th…, subclass of, IMA status and/or r…, named after）

## g0801 — wikidbs10k：見出し「instagram location id」（Wikidata の型 `string`）（19 列）
- 例1：396738974 | 362825580 | 216563545 | 301666649 | 834148023（表：Stimmkreis Fürstenfeldbruck-Ost／同じ表の列：label, description, country, Commons category, German municipality…, coordinate location）
- 例2：250739540 | 247537927 | 396738974 | 251395532 | 294831660（表：jurisdiction／同じ表の列：label, description, country, Commons category, German municipality…, coordinate location）
- 例3：910397875 | 250739540 | 390571090 | 294831660 | 251395532（表：workplace／同じ表の列：label, description, country, Commons category, German municipality…, coordinate location）

## g0802 — wikidbs10k：見出し「logainm id」（Wikidata の型 `string`）（19 列）
- 例1：2222 | 1416810 | 1375542 | 1385574 | 1399926（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, coat of arms image, image）
- 例2：100023.0 | 100024.0 | 100031.0 | 100022.0 | 100009.0（表：administrative territorial entity／同じ表の列：label, description, page banner, located in the admi…, Commons category, licence plate code）
- 例3：100009 | 100002 | 100022 | 100018 | 100019（表：political border／同じ表の列：label, description, page banner, located in the admi…, Commons category, licence plate code）

## g0803 — wikidbs10k：見出し「nci thesaurus id」（Wikidata の型 `string`）（19 列）
- 例1：C32836 | C12389 | C12730 | C32712 | C12453（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Commons category, subclass of, Freebase ID）
- 例2：C12666 | C32078 | C12445 | C12439 | C12388（表：expressed in／同じ表の列：label, description, Foundational Model …, UBERON ID, described by source, MeSH tree code）
- 例3：C32874 | C12412 | C33483 | C12389 | C43612（表：expressed in／同じ表の列：label, description, instance of, UBERON ID, Foundational Model …, UMLS CUI）

## g0804 — wikidbs10k：見出し「publons publisher id」（Wikidata の型 `string`）（19 列）
- 例1：7 | 120 | 4 | 123 | 3（表：publisher／同じ表の列：label, description, official website, instance of, inception, headquarters locati…）
- 例2：7 | 6186 | 26 | 71 | 4（表：publisher／同じ表の列：label, description, official website, VIAF ID, instance of, headquarters locati…）
- 例3：144 | 61 | 8 | 60 | 123（表：publisher／同じ表の列：label, description, Freebase ID, VIAF ID, Library of Congress…, inception）

## g0805 — wikidbs10k：見出し「rate your music genre id」（Wikidata の型 `string`）（19 列）
- 例1：pop | eurodance | contemporary-randb | jazz | western-classical-music（表：genre／同じ表の列：label, description, instance of, subclass of, topic's main catego…, Freebase ID）
- 例2：heavy-metal | pop | hardcore-punk-1 | punk-rock | rock（表：genre／同じ表の列：label, description, Commons category, subclass of, topic's main catego…, Freebase ID）
- 例3：southern-gospel | country | pop | country-pop | traditional-folk-music（表：genre／同じ表の列：label, description, instance of, Commons category, subclass of, topic's main catego…）

## g0806 — wikidbs10k：見出し「rotten tomatoes id」（Wikidata の型 `string`）（19 列）
- 例1：m/howling_reborn | m/1131721-punisher | m/jack_ryan_shadow_recruit | m/batman_begins | m/hellraiser_2022（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例2：tv/30-rock/s05/e21 | tv/the_simpsons/s04/e18 | tv/the_simpsons/s07/e10 | tv/friends/s07/e21 | tv/friends/s08/e19（表：clip show／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例3：tv/seinfeld/s09 | tv/star_trek_the_next_generation/s03 | tv/lost/s01 | tv/the_simpsons/s13 | tv/2062/s08（表：television series season／同じ表の列：label, description, instance of, Freebase ID, part of the series, number of episodes）

## g0807 — wikidbs10k：見出し「settlement area code in sweden」（Wikidata の型 `string`）（19 列）
- 例1：1491TC111 | 0125TC102 | 2262TC106 | 0760TC105 | 2581TC112（表：capital city／同じ表の列：label, description, located in the admi…, country, coordinate location, instance of）
- 例2：1907TC102 | 1883TC101 | 1885TC104 | 1982TC101 | 0484TC104（表：capital city／同じ表の列：label, description, topic's main catego…, Commons category, country, located in the admi…）
- 例3：0117TC112 | 0883TC112 | 0127TC103 | 0136TB109 | 0115TC108（表：capital city／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0808 — wikidbs10k：見出し「swedish urban area code」（Wikidata の型 `string`）（19 列）
- 例1：TX016 | T8792 | T0150 | T4976 | T1332（表：capital city／同じ表の列：label, description, located in the admi…, country, coordinate location, instance of）
- 例2：T6008 | T6332 | T6040 | T0740 | T6212（表：capital city／同じ表の列：label, description, topic's main catego…, Commons category, country, located in the admi…）
- 例3：T0688 | T0656 | T0408 | T2132 | TX014（表：capital city／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0809 — wikidbs10k：見出し「transfermarkt match id」（Wikidata の型 `string`）（19 列）
- 例1：2271702 | 2271699 | 2271694 | 2271692 | 2271698（表：UEFA Euro 1972 qualifying Group 8／同じ表の列：label, description, instance of, participating team, attendance, referee）
- 例2：1152391 | 1152398 | 1152394 | 1152390 | 1152399（表：UEFA Euro 1976 qualifying Group 5／同じ表の列：label, description, instance of, participating team, attendance, referee）
- 例3：1089529 | 1089521 | 1089528 | 1089522 | 1089524（表：1966 FIFA World Cup qualification – UEF…／同じ表の列：label, description, instance of, participating team, part of, point in time）

## g0810 — wikidbs10k：見出し「has edition or translation」（Wikidata の型 `wikibase-entityid`）（19 列）
- 例1：De koning der kikvorschen, of de IJzere… | The Knapsack, the Hat, and the Horn | Die Bremer Stadtmusikanten | Rapunzel | Peukaloisen matkustukset（表：version, edition, or translation／同じ表の列：label, description, Freebase ID, instance of, Aarne–Thompson–Uthe…, Commons category）
- 例2：The Mouse, the Bird, and the Sausage | Jussi ja Kaisa-Liisa | The Elves and the Shoemaker | Iron Hans | The Cat and the Mouse in Partnership（表：version, edition, or translation／同じ表の列：label, description, Freebase ID, instance of, Aarne–Thompson–Uthe…, Commons category）
- 例3：ISO 80000-8:2007 Quantities and units—P… | ISO 80000-10:2009 Quantities and units—… | ISO 80000-12:2009 Quantities and units—… | ISO 80000-7:2008 Quantities and units—P… | ISO 80000-1:2009 Quantities and units—P…（表：ISO IEC 80000／同じ表の列：label, description, instance of, part of, follows, followed by）

## g0811 — wikidbs10k：見出し「ima status and/or rank」（Wikidata の型 `wikibase-entityid`）（19 列）
- 例1：approved mineral and/or valid name (A) | redefined mineral (Rd) | discredited mineral (D) | renamed mineral (Rn) | questionable (Q)（表：borate class of minerals／同じ表の列：label, description, Nickel-Strunz '10th…, named after, subclass of, crystal system）
- 例2：grandfathered mineral (G) | approved mineral and/or valid name (A)（表：neso-aluminofluoride minerals (3.CB.)／同じ表の列：label, description, Strunz 8th edition …, subclass of, chemical formula, Nickel-Strunz 9th e…）
- 例3：grandfathered mineral (G) | approved mineral and/or valid name (A)（表：nesoborate mineral subclass／同じ表の列：label, description, Nickel-Strunz '10th…, subclass of, named after, chemical formula）

## g0812 — wikidbs10k：見出し「next higher rank」（Wikidata の型 `wikibase-entityid`）（19 列）
- 例1：Grand Knight of Valour | Order of the Crown of the Realm | Air Force Medal of Malaysia | Medal of Merit | Commander of the Order of the Defender …（表：Orders, decorations, and medals of Mala…／同じ表の列：label, description, instance of, country, service ribbon image, part of）
- 例2：Grand Knight of Valour | Active Service Medal | Commander of the Order of the Defender … | Medal of Merit | Companion of the Order of Loyalty to th…（表：next higher rank／同じ表の列：label, description, instance of, country, service ribbon image, next lower rank）
- 例3：Commander of the Order of Loyalty to th… | Air Force Medal of Malaysia | Order of the Crown of the Realm | Officer of the Order of the Defender of… | Companion of the Order of Loyalty to th…（表：next lower rank／同じ表の列：label, description, instance of, country, service ribbon image, next lower rank）

## g0813 — wikidbs10k：見出し「referee」（Wikidata の型 `wikibase-entityid`）（19 列）
- 例1：Paul Bonett | Karlo Kruashvili | Todor Bechirov | Robert Héliès | János Bíróczky（表：UEFA Euro 1972 qualifying Group 8／同じ表の列：label, description, Transfermarkt match…, instance of, participating team, attendance）
- 例2：Paul Schiller | Wolfgang Riedel | Dušan Maksimović | Pavel Kazakov | Eric Smyton（表：UEFA Euro 1976 qualifying Group 5／同じ表の列：label, description, Transfermarkt match…, instance of, participating team, attendance）
- 例3：William Clements | John Meighan | Johan Einar Boström | Adolfo Bueno Perales | Petar Dzhonev（表：1966 FIFA World Cup qualification – UEF…／同じ表の列：label, description, instance of, Transfermarkt match…, participating team, part of）

## g0814 — wikidbs10k：見出し「apoapsis」（Wikidata の型 `quantity`）（18 列）
- 例1：402.0 | 252.0 | 227.0 | 387.0 | 249.0（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例2：+240 | +269 | +263.7 | +309 | +287.4（表：spaceflight／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）
- 例3：+228 | +390.0 | +240 | +390 | +340（表：follows／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）

## g0815 — wikidbs10k：見出し「number of parts of this work」（Wikidata の型 `quantity`）（18 列）
- 例1：+7 | +10 | +5 | +21 | +14（表：Bee Gees' albums in chronological order／同じ表の列：label, description, instance of, performer, form of creative wo…, title）
- 例2：+13 | +1 | +5 | +2（表：publishing／同じ表の列：label, description, instance of, performer, record label, tracklist）
- 例3：+3 | +8 | +2 | +4 | +7（表：list of compositions by Wolfgang Amadeu…／同じ表の列：label, description, instance of, part of, tonality, composer）

## g0816 — wikidbs10k：見出し「bag residence id」（Wikidata の型 `string`）（18 列）
- 例1：2445 | 3317 | 3346 | 2128 | 2266（表：physical location／同じ表の列：label, description, country, coordinate location, Commons category, located in the admi…）
- 例2：2268 | 3049 | 2267 | 1746 | 2350（表：physical location／同じ表の列：label, description, country, instance of, located in the admi…, coordinate location）
- 例3：2254 | 2251 | 2248 | 3560 | 3562（表：physical location／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0817 — wikidbs10k：見出し「danish educational institution number」（Wikidata の型 `string`）（18 列）
- 例1：167000 | 101000 | 265000 | 165000 | 190000（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例2：201000 | 163000 | 161000 | 151000 | 350000（表：political border／同じ表の列：label, description, capital, country, located in the admi…, Commons category）
- 例3：306000 | 253000 | 710000 | 746000 | 760000（表：municipality of Denmark／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）

## g0818 — wikidbs10k：見出し「democracy club candidate id」（Wikidata の型 `string`）（18 列）
- 例1：11328.0 | 18877.0 | 11683.0 | 11687.0 | 42757.0（表：candidate／同じ表の列：label, description, instance of, name, occupation, member of political…）
- 例2：14589.0 | 44290.0 | 14634.0 | 14655.0 | 14625.0（表：candidate／同じ表の列：label, description, instance of, name, occupation, member of political…）
- 例3：35723 | 44296 | 14631 | 14633 | 44324（表：political candidate／同じ表の列：label, description, instance of, name, occupation, candidacy in electi…）

## g0819 — wikidbs10k：見出し「discogs artist id」（Wikidata の型 `string`）（18 列）
- 例1：106450 | 57103 | 287175 | 198282 | 1087831（表：performing artist／同じ表の列：label, description, discography, MusicBrainz artist …, Commons category, image）
- 例2：335901 | 466241 | 172408 | 273276 | 69866（表：participant／同じ表の列：label, description, Commons category, MusicBrainz artist …, GND ID, instance of）
- 例3：273276 | 198319 | 527917 | 175489 | 669860（表：participant／同じ表の列：label, description, Commons category, MusicBrainz artist …, GND ID, instance of）

## g0820 — wikidbs10k：見出し「flybase gene id」（Wikidata の型 `string`）（18 列）
- 例1：FBgn0040950 | FBgn0085353 | FBgn0036363 | FBgn0038645 | FBgn0035412（表：encoded by／同じ表の列：label, description, Entrez Gene ID, Ensembl gene ID, Ensembl transcript …, RefSeq RNA ID）
- 例2：FBgn0041229 | FBgn0041225 | FBgn0041245 | FBgn0045473 | FBgn0041248（表：encoded by／同じ表の列：label, description, strand orientation, Ensembl transcript …, RefSeq RNA ID, Entrez Gene ID）
- 例3：FBgn0053758 | FBgn0033640 | FBgn0030074 | FBgn0039621 | FBgn0054028（表：encoded by／同じ表の列：label, description, found in taxon, NCBI locus tag, Entrez Gene ID, genomic end）

## g0821 — wikidbs10k：見出し「golden id」（Wikidata の型 `string`）（18 列）
- 例1：New_Jersey-A3J3 | Ontario-EAV3W | Canada-9NNBJ3 | California-G55V | Florida-GRAN6Z（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例2：New_Jersey-A3J3 | Maryland | Pennsylvania-4NNDW | Tennessee-AMYRX | Florida-GRAN6Z（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：Taiwan-R9N9J | Japan-NX69 | China-APPE | Soviet_Union-MNYNY | Israel-BGWEVY（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, Libraries Australia…, coordinates of sout…）

## g0822 — wikidbs10k：見出し「musicbrainz genre id」（Wikidata の型 `string`）（18 列）
- 例1：2126f16b-13b6-45c9-b02e-c63be8bbdaea | ae9b8279-3959-48d8-8a88-741a7f6d4a48 | 797e2e85-5ffd-495c-a757-8b4079052f0e | cc4cf136-5690-4ee3-a62b-b172febfe322 | 5f665615-7fb3-49d8-b541-62a7b239edbe（表：genre／同じ表の列：label, description, instance of, subclass of, topic's main catego…, Freebase ID）
- 例2：51cb9f91-e6a2-41bf-891f-e78e3f1e52ab | f6d8cadd-6a5e-4ec9-9c2b-996b5332a639 | 31be54b2-4d0c-42df-aa44-c496c7b4c3c3 | 911c7bbb-172d-4df8-9478-dbff4296e791 | e12fe025-4c13-485e-a2fe-ad5bf2cd75eb（表：genre／同じ表の列：label, description, Commons category, subclass of, topic's main catego…, Freebase ID）
- 例3：0e3fc579-2d24-4f20-9dae-736e1ec78798 | 5f665615-7fb3-49d8-b541-62a7b239edbe | 2de61e9c-de1d-47c8-999d-5b44c0cfeca1 | 2b4f0036-79a0-4ce0-a38c-4c0c8e61c579 | 08289b42-7e41-4987-9263-c28bb4c59da0（表：genre／同じ表の列：label, description, instance of, Commons category, subclass of, topic's main catego…）

## g0823 — wikidbs10k：見出し「open media database film id」（Wikidata の型 `string`）（18 列）
- 例1：27967.0 | 28620.0 | 7562.0 | 26998 | 30049.0（表：television series season／同じ表の列：label, description, instance of, Freebase ID, part of the series, number of episodes）
- 例2：7482.0 | 7486.0 | 7757.0 | 27988.0 | 6867.0（表：followed by／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例3：6238 | 28417 | 27986.0 | 27985 | 7756.0（表：follows／同じ表の列：label, description, instance of, part of the series, follows, followed by）

## g0824 — wikidbs10k：見出し「architectural style」（Wikidata の型 `wikibase-entityid`）（18 列）
- 例1：Renaissance | classicism | Egyptian Revival architecture | Neoclassical architecture | neoclassicism（表：work／同じ表の列：label, description, instance of, located in the admi…, Commons category, architect）
- 例2：Art Nouveau | Renaissance architecture | baroque architecture | Renaissance Revival architecture（表：summer residence／同じ表の列：label, description, coordinate location, instance of, located in the admi…, architect）
- 例3：Romanesque architecture | Renaissance | Neoclassical architecture | baroque architecture | Gothic architecture（表：cathedral／同じ表の列：label, description, image, coordinate location, instance of, located in the admi…）

## g0825 — wikidbs10k：見出し「fictional universe described in」（Wikidata の型 `wikibase-entityid`）（18 列）
- 例1：X-Men: Evolution | Marvel One-Shots | Touhou Project | Spooky's Jump Scare Mansion | Star Trek（表：fictional universe／同じ表の列：label, description, instance of）
- 例2：Adventure Time | Street Fighter | Grand Theft Auto III | Teenage Mutant Ninja Turtles | Saints Row（表：fictional universe／同じ表の列：label, description, instance of）
- 例3：Twin Peaks | Saints Row | Marvel One-Shots | Shrek | One Piece（表：fictional universe／同じ表の列：label, description, instance of）

## g0826 — wikidbs10k：見出し「next lower rank」（Wikidata の型 `wikibase-entityid`）（18 列）
- 例1：Companions of the Order of Loyalty to t… | Medal of the Order of the Defender of t… | Commander of the Order of the Defender … | Order of the Crown of the Realm | Active Service Medal（表：next higher rank／同じ表の列：label, description, instance of, country, service ribbon image, next higher rank）
- 例2：Companion of the Order of the Defender … | Air Force Medal of Malaysia | Member of the Order of the Defender of … | Officer of the Order of Loyalty to the … | Grand Commander of the Order of the Def…（表：next lower rank／同じ表の列：label, description, instance of, country, service ribbon image, next higher rank）
- 例3：Knight Hospitaller | Commander of the Order of George I | Commander of the Order of Chula Chom Kl… | Grand Cross of the Order of the Dannebr… | Commander of the Order of the Redeemer（表：Grand Commander／同じ表の列：label, description, instance of, part of, country, service ribbon image）

## g0827 — wikidbs10k：見出し「number of deaths」（Wikidata の型 `quantity`）（17 列）
- 例1：+815 | +33663 | +24809 | +23634 | +1（表：cause／同じ表の列：label, description, part of, country, location, coordinate location）
- 例2：+10 | +5063 | +546 | +4 | +83（表：COVID-19 pandemic in the United States／同じ表の列：label, description, part of, instance of, country, location）
- 例3：+22 | +6 | +8 | +0 | +1（表：school shooting／同じ表の列：label, description, instance of, country, point in time, location）

## g0828 — wikidbs10k：見出し「orbits completed」（Wikidata の型 `quantity`）（17 列）
- 例1：+3068 | +2940 | +2895 | +3036 | +2207（表：part／同じ表の列：label, description, start time, Commons category, follows, followed by）
- 例2：186.0 | 3040.0 | 217.0 | 5830.0 | 3170.0（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例3：2020 | +127 | 2987 | +1993 | 2975（表：followed by／同じ表の列：label, description, start time, Commons category, follows, followed by）

## g0829 — wikidbs10k：見出し「radial velocity」（Wikidata の型 `quantity`）（17 列）
- 例1：13.92 | 5.011 | -22.7 | 27.51 | 36.9（表：primary body／同じ表の列：label, description, constellation, spectral class, catalog code, instance of）
- 例2：+3406 | +3388 | +2936 | +3189 | +2984（表：[CHM2007] LDC 916／同じ表の列：label, description, catalog code, instance of, SIMBAD ID, apparent magnitude）
- 例3：+3202 | +3016 | +3314 | +3185 | +2702（表：part／同じ表の列：label, description, SIMBAD ID, instance of, declination, epoch）

## g0830 — wikidbs10k：見出し「chapter」（Wikidata の型 `string`）（17 列）
- 例1：83 | 46 | 17 | 66 | 27（表：Journey to the West／同じ表の列：label, description, language of work or…, follows, instance of, title）
- 例2：66 | 78 | 37 | 90 | 29（表：followed by／同じ表の列：label, description, language of work or…, follows, part of, instance of）
- 例3：46 | 16 | 33 | 50 | 31（表：follows／同じ表の列：label, description, language of work or…, follows, part of, instance of）

## g0831 — wikidbs10k：見出し「musicbrainz label id」（Wikidata の型 `string`）（17 列）
- 例1：d49620d1-5423-418f-8584-418936026949 | 4180adf0-cb47-497a-8db5-585f86296e25 | 63a8ddf8-a8d7-4637-aa98-4edc21d17fd7 | 6520c01d-4e68-4bc2-afb9-8178df199c10 | 7cc5eb15-03a5-460d-aacd-acd65b826ab2（表：operator／同じ表の列：label, description, headquarters locati…, Commons category, instance of, Freebase ID）
- 例2：3930d173-b232-4ff8-b2f3-568651924d98 | adde0cb6-4535-47b8-9b10-f18cc0b466ae | 5a7aaa47-952d-4729-ae60-c6091b711cab | 73f2f568-a387-4218-bddb-2cee71b0f023 | 1317e524-2a1e-4bc8-8d96-9403b74ec364（表：record label／同じ表の列：label, description, instance of, country, Discogs label ID）
- 例3：cebbb8e9-ff34-46dd-a0e5-3ca373adaea2 | 5c54e242-e485-464b-82a1-37d6288cb539 | 011d1192-6f65-45bd-85c4-0400dd45693e | f1ca0074-59ef-4850-82a4-91a6b364c81e | 8f638ddb-131a-4cc3-b3d4-7ebdac201b55（表：record label／同じ表の列：label, description, instance of, inception, Discogs label ID, country）

## g0832 — wikidbs10k：見出し「nederlands soortenregister id」（Wikidata の型 `string`）（17 列）
- 例1：118963 | 119370 | 119882 | 179131 | 119686（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：122910 | 124215 | 185713 | 123147 | 183715（表：taxon／同じ表の列：label, description, MycoBank taxon name…, Encyclopedia of Lif…, taxon rank, taxon name）
- 例3：124037.0 | 122911 | 128301.0 | 128278 | 123929.0（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g0833 — wikidbs10k：見出し「procyclingstats team id」（Wikidata の型 `string`）（17 列）
- 例1：1423&season=2013 | team-ineos-2019 | team-sky-2017 | 1423&season=2010 | 1423&season=2014（表：Ineos Grenadiers／同じ表の列：label, description, instance of, sport, UCI code of cycling…, general manager）
- 例2：1423&season=2012 | 1423&season=2011 | ineos-grenadiers-2022 | team-sky-2016 | ineos-grenadiers-2023（表：followed by／同じ表の列：label, description, instance of, sport, UCI code of cycling…, follows）
- 例3：team-sky-2016 | ineos-grenadiers-2022 | team-sky-2017 | team-ineos-2019 | 1423&season=2011（表：follows／同じ表の列：label, description, instance of, sport, UCI code of cycling…, general manager）

## g0834 — wikidbs10k：見出し「route number」（Wikidata の型 `string`）（17 列）
- 例1：5970 | 4113 | 5540 | 2250 | 3230（表：railway line／同じ表の列：label, description, country, located in the admi…, track gauge, instance of）
- 例2：1730 | 1700 | 1761 | 1732 | 2930（表：railway line／同じ表の列：label, description, Commons category, country, instance of, Freebase ID）
- 例3：5 | 10 | B1 | 7 | 3（表：Rapid KL／同じ表の列：label, description, instance of, Commons category, Freebase ID, country）

## g0835 — wikidbs10k：見出し「service ribbon image」（Wikidata の型 `string`）（17 列）
- 例1：Federation Gallantry Star ribbon medal.… | Order of Loyalty to the Crown of Malays… | Star of the Commander of Valour.gif | Air Force Medal (ribbon).gif | MY Panglima Setia Diraja - Order of the…（表：Orders, decorations, and medals of Mala…／同じ表の列：label, description, instance of, country, next higher rank, part of）
- 例2：Malaysia General Service Medal 1971.png | MY Darjah Kerabat Diraja Malaysia - Roy… | MY Darjah Yang Mulia Pangkuan Negara (D… | Medal of Merit (ribbon).gif | MY Panglima Setia Diraja - Order of the…（表：next higher rank／同じ表の列：label, description, instance of, country, next higher rank, next lower rank）
- 例3：Federation Gallantry Star ribbon medal.… | MYS Federation Loyal Service Medal.png | MY Darjah Utama Seri Mahkota Negara (Cr… | Air Force Medal (ribbon).gif | Order of Loyalty to the Crown of Malays…（表：next lower rank／同じ表の列：label, description, instance of, country, next higher rank, next lower rank）

## g0836 — wikidbs10k：見出し「srgb color hex triplet」（Wikidata の型 `string`）（17 列）
- 例1：139593 | 1964B7 | E0115F | 1E4D2B | F68933（表：Rapid KL／同じ表の列：label, description, instance of, Commons category, Freebase ID, country）
- 例2：7B107D | FFE600 | E11936 | FFD403 | 8A8988（表：transport route／同じ表の列：label, description, instance of, country, terminus, logo image）
- 例3：FEB872 | FE5B71 | FEB757 | F6EC39 | EE007D（表：erathem／同じ表の列：label, description, instance of, part of, followed by, start time）

## g0837 — wikidbs10k：見出し「tela botanica id」（Wikidata の型 `string`）（17 列）
- 例1：100993 | 100226 | 86651 | 2934 | 85941（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：104210 | 87292 | 103303 | 100992 | 87283（表：taxon／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例3：86972 | 85299 | 86006 | 84866 | 103333（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）

## g0838 — wikidbs10k：見出し「uic station code」（Wikidata の型 `string`）（17 列）
- 例1：8013732 | 8013728 | 8013555 | 8013513 | 8013444（表：Hanover S-Bahn／同じ表の列：label, description, Commons category, country, image, coordinate location）
- 例2：8013452 | 8013573 | 8013318 | 8013522 | 8023888（表：adjacent station／同じ表の列：label, description, Commons category, instance of, country, coordinate location）
- 例3：5455536 | 5455646 | 5457276 | 5455636 | 5457016（表：Praha–Vrané nad Vltavou–Čerčany Dobříš …／同じ表の列：label, description, Commons category, country, instance of, coordinate location）

## g0839 — wikidbs10k：見出し「end time」（Wikidata の型 `time`）（17 列）
- 例1：-252000000-00-00T00:00:00Z | -1000000000-00-00T00:00:00Z | -2800000000-00-00T00:00:00Z | -3200000000-00-00T00:00:00Z | -2500000000-00-00T00:00:00Z（表：followed by／同じ表の列：label, description, instance of, follows, followed by, Commons category）
- 例2：-2800000000-00-00T00:00:00Z | -2500000000-00-00T00:00:00Z | -1000000000-00-00T00:00:00Z | -1600000000-00-00T00:00:00Z | -3850000000-01-01T00:00:00Z（表：follows／同じ表の列：label, description, instance of, part of, followed by, Commons category）
- 例3：-419200000-00-00T00:00:00Z | -358900000-00-00T00:00:00Z | -1400000000-00-00T00:00:00Z | -2050000000-00-00T00:00:00Z | -2060000000-00-00T00:00:00Z（表：system／同じ表の列：label, description, instance of, start time, part of, follows）

## g0840 — wikidbs10k：見出し「mouth of the watercourse」（Wikidata の型 `wikibase-entityid`）（17 列）
- 例1：Glienicker Lake | Elbe | Rhine | Danube | Moselle（表：body of water／同じ表の列：label, description, instance of, Commons category, country, coordinate location）
- 例2：St. Lawrence River | Bay of Fundy | Loire | Aller | Aare（表：crossing／同じ表の列：label, description, instance of, Commons category, image, coordinate location）
- 例3：Crusnes | Allier | Oust | Weser | Loire（表：tributary／同じ表の列：label, description, instance of, country, coordinate location, located in the admi…）

## g0841 — wikidbs10k：見出し「vehicle」（Wikidata の型 `wikibase-entityid`）（17 列）
- 例1：Soyuz TMA-5 | Soyuz TMA-4 | STS-113 | Soyuz TM-31 | Soyuz TMA-3（表：part／同じ表の列：label, description, start time, Commons category, follows, followed by）
- 例2：Discovery | Soyuz-TMA | Endeavour | Soyuz-TM（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例3：Soyuz TMA-5 | Soyuz TMA-2 | Soyuz TMA-6 | Soyuz TMA-3 | Columbia（表：followed by／同じ表の列：label, description, start time, Commons category, follows, followed by）

## g0842 — sotab_v2：元の種類 `DayOfWeek`（16 列）
- 例1：http://schema.org/Sunday（DBpedia：day）
- 例2：http://schema.org/Monday（DBpedia：day）
- 例3：http://schema.org/Saturday | http://schema.org/Thursday | http://schema.org/Sunday | http://schema.org/Friday（DBpedia：day）

## g0843 — wikidbs10k：見出し「distance from earth」（Wikidata の型 `quantity`）（16 列）
- 例1：+54.9819 | +4.6758 | +37.8191 | +150.946 | +122.805（表：primary body／同じ表の列：label, description, constellation, instance of, catalog code, apparent magnitude）
- 例2：15.6051 | 7.2454 | 226.0 | 8.5053 | 284.876（表：primary body／同じ表の列：label, description, constellation, spectral class, catalog code, instance of）
- 例3：+60.25 | +31.92 | +60.53 | +34.36 | +54.45（表：[CHM2007] LDC 916／同じ表の列：label, description, catalog code, instance of, SIMBAD ID, apparent magnitude）

## g0844 — wikidbs10k：見出し「nominal gdp per capita」（Wikidata の型 `quantity`）（16 列）
- 例1：+39953 | +44920 | +59927 | +53253 | +33228（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, Freebase ID, instance of）
- 例2：+6408 | +3393 | +4655 | +6571 | +5823（表：economy of region／同じ表の列：label, description, topic's main catego…, instance of, Commons category, Quora topic ID）
- 例3：+75704 | +1451 | +39953 | +9951 | +8826（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, instance of, BabelNet ID）

## g0845 — wikidbs10k：見出し「periapsis」（Wikidata の型 `quantity`）（16 列）
- 例1：190.0 | 349.0 | 373.0 | 193.0 | 379.0（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例2：+302 | +202 | +384 | +194 | +190.0（表：spaceflight／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）
- 例3：+388 | +202 | +268 | +384 | +339（表：follows／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）

## g0846 — wikidbs10k：見出し「ppp gdp per capita」（Wikidata の型 `quantity`）（16 列）
- 例1：+53879.298 | +46509.717 | +51404.785 | +59927.93 | +40923.702（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, Freebase ID, instance of）
- 例2：+24747.307 | +7575.682 | +17694.202 | +13109.344 | +11612.045（表：economy of region／同じ表の列：label, description, topic's main catego…, instance of, Commons category, Quora topic ID）
- 例3：+62182.842 | +59927.93 | +29511.443 | +46509.717 | +16842.408（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, instance of, BabelNet ID）

## g0847 — wikidbs10k：見出し「allmovie title id」（Wikidata の型 `string`）（16 列）
- 例1：v248889 | v719961 | v201752 | v350392 | v326224（表：sixth generation Chinese films／同じ表の列：label, description, IMDb ID, instance of, director, original language o…）
- 例2：v284906 | v279357 | v284904 | v279318 | v279341（表：followed by／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例3：v327920 | v284928 | v327921 | v279316 | v285005（表：follows／同じ表の列：label, description, instance of, part of the series, follows, followed by）

## g0848 — wikidbs10k：見出し「cas registry number」（Wikidata の型 `string`）（16 列）
- 例1：74-83-9 | 7783-07-5 | 75-02-5 | 630-08-0 | 463-51-4（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：75-21-8 | 75-02-5 | 7803-62-5 | 630-08-0 | 68476-85-7（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：7429-92-7 | 7440-14-4 | 54085-16-4 | 7440-72-4 | 53850-35-4（表：period 7／同じ表の列：label, description, OmegaWiki Defined M…, Dewey Decimal Class…, named after, element symbol）

## g0849 — wikidbs10k：見出し「german district key」（Wikidata の型 `string`）（16 列）
- 例1：02000 | 14713 | 09162 | 12054 | 05315（表：headquarters／同じ表の列：label, description, twinned administrat…, page banner, country, Commons category）
- 例2：2000.0 | 6412.0 | 5112.0 | 1003.0 | 5119.0（表：physical location／同じ表の列：label, description, twinned administrat…, Dewey Decimal Class…, country, instance of）
- 例3：09738 | 09276 | 09672 | 09733 | 09477（表：rural district of Bavaria／同じ表の列：label, description, shares border with, located in the admi…, country, coordinate location）

## g0850 — wikidbs10k：見出し「ifla value vocabularies id」（Wikidata の型 `string`）（16 列）
- 例1：key#eb | key#f | key#gm | key#a | key#bb（表：key／同じ表の列：label, description, Commons category, Freebase ID, image, followed by）
- 例2：key#ab | key#gxm | key#b | key#c | key#e（表：followed by／同じ表の列：label, description, Commons category, Freebase ID, image, followed by）
- 例3：key#bm | key#eb | key#a | key#dm | key#am（表：key／同じ表の列：label, description, Commons category, Freebase ID, image, IMSLP ID）

## g0851 — wikidbs10k：見出し「ijf competition id」（Wikidata の型 `string`）（16 列）
- 例1：1194 | 1095 | 1057 | 1710 | 1315（表：IJF World Tour Düsseldorf／同じ表の列：label, description, sport, instance of, followed by, follows）
- 例2：1323 | 1100 | 1140 | 1060 | 1022（表：followed by／同じ表の列：label, description, sport, instance of, followed by, follows）
- 例3：1349 | 1187 | 1054 | 1707 | 1040（表：follows／同じ表の列：label, description, country, point in time, sport, instance of）

## g0852 — wikidbs10k：見出し「ine id (portugal)」（Wikidata の型 `string`）（16 列）
- 例1：110411 | 060334 | 070612 | 0502 | 150802（表：administrative territorial entity／同じ表の列：label, description, country, coordinate location, area, located in the admi…）
- 例2：502 | 140124 | 090711 | 141302 | 141703（表：administrative territorial entity／同じ表の列：label, description, country, coat of arms image, located in the admi…, coordinate location）
- 例3：1413 | 1401.0 | 1419.0 | 0509 | 1418.0（表：political border／同じ表の列：label, description, flag image, coat of arms image, Commons category, located in the admi…）

## g0853 — wikidbs10k：見出し「tv.com id」（Wikidata の型 `string`）（16 列）
- 例1：shows/drawn-together/requiem-for-a-real… | shows/drawn-together/xandir-and-tim-sit… | shows/drawn-together/super-nanny-585585 | shows/drawn-together/hot-tub-272615 | shows/drawn-together/little-orphan-hero…（表：follows／同じ表の列：label, description, instance of, part of the series, IMDb ID, part of）
- 例2：shows/days-of-our-lives | shows/the-young-and-restless | shows/neighbours | shows/as-the-world-turns | shows/general-hospital（表：work／同じ表の列：label, description, original broadcaster, IMDb ID, country of origin, topic's main catego…）
- 例3：shows/friends/season-9 | shows/friends/season-7 | shows/friends/season-8 | shows/star-trek-the-next-generation/sea… | shows/the-simpsons/season-7（表：television series season／同じ表の列：label, description, instance of, Freebase ID, part of the series, number of episodes）

## g0854 — wikidbs10k：見出し「country of registry」（Wikidata の型 `wikibase-entityid`）（16 列）
- 例1：Canada（表：His Majesty's Canadian Ship／同じ表の列：label, description, instance of, image, operator, military branch）
- 例2：Nazi Germany | Germany | Kingdom of Italy（表：31st U-boat Flotilla／同じ表の列：label, description, operator, instance of, conflict, vessel class）
- 例3：Isle of Man | Tuvalu | Spain | Canada | Panama（表：chemical tanker／同じ表の列：label, description, instance of, IMO ship number, length, Commons category）

## g0855 — wikidbs10k：見出し「dual to」（Wikidata の型 `wikibase-entityid`）（16 列）
- 例1：deltoidal hexecontahedron | rhombic triacontahedron | deltoidal icositetrahedron | triakis octahedron | rhombic dodecahedron（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）
- 例2：tetrakis hexahedron | rhombicosidodecahedron | truncated dodecahedron | cuboctahedron | disdyakis dodecahedron（表：duality／同じ表の列：label, description, Commons category, Freebase ID, has facet polytope, subclass of）
- 例3：triakis tetrahedron | deltoidal hexecontahedron | disdyakis triacontahedron | deltoidal icositetrahedron | disdyakis dodecahedron（表：depiction／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）

## g0856 — wikidbs10k：見出し「parent astronomical body」（Wikidata の型 `wikibase-entityid`）（16 列）
- 例1：scattered disc | classical Kuiper belt object | Sun（表：possible dwarf planet／同じ表の列：label, description, discoverer or inven…, instance of, orbital inclination, orbital eccentricity）
- 例2：Sun | Earth | Neptune | Mars | Saturn（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, image, topic's main catego…）
- 例3：HD 131399A | EWS 2007-BUL-513 | HD 188753A | HAT-P-13 | Natasha（表：visual artifact／同じ表の列：label, description, instance of, time of discovery o…, constellation, right ascension）

## g0857 — wikidbs10k：見出し「platform」（Wikidata の型 `wikibase-entityid`）（16 列）
- 例1：Xbox | Apple II | Sega Saturn | Mac OS 8 | System 7（表：video game retail package／同じ表の列：label, description, publication date, publisher, part of, instance of）
- 例2：Nintendo 3DS | Super Nintendo Entertainment System | Nintendo 64 | Wii U | Nintendo Switch（表：work／同じ表の列：label, description, part of the series, genre, game mode, instance of）
- 例3：PlayStation 5 | Commodore Amiga | PlayStation 4 | PlayStation 2 | Microsoft Windows（表：video game remake／同じ表の列：label, description, instance of, game mode, publication date）

## g0858 — wikidbs10k：見出し「translator」（Wikidata の型 `wikibase-entityid`）（16 列）
- 例1：Lucy Crane（表：Household stories from the collection o…／同じ表の列：label, description, instance of, author, title, publication date）
- 例2：Lucy Crane（表：followed by／同じ表の列：label, description, instance of, author, title, publication date）
- 例3：Lucy Crane（表：follows／同じ表の列：label, description, instance of, author, title, publication date）

## g0859 — wikidbs10k：見出し「real gdp growth rate」（Wikidata の型 `quantity`）（15 列）
- 例1：+2.3 | +3.3 | +1.6 | +1.5 | +0.9（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, Freebase ID, instance of）
- 例2：-2.3 | +3.3 | +2.0 | +1.4 | +3.9（表：economy of region／同じ表の列：label, description, topic's main catego…, instance of, Commons category, Quora topic ID）
- 例3：+1.6 | +1.0 | +0.0 | +1.4 | +4.4（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, instance of, BabelNet ID）

## g0860 — wikidbs10k：見出し「great encyclopedia of navarre id」（Wikidata の型 `string`）（15 列）
- 例1：14979 | 4497 | 5135 | 11531 | 10660（表：Iruñerriko Mankomunitatea／同じ表の列：label, description, country, Commons category, coat of arms image, postal code）
- 例2：15603.0 | 15633.0 | 19982.0 | 17107.0 | 7042.0（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：4497 | 14979 | 3609 | 5320 | 5682（表：workplace／同じ表の列：label, description, country, coat of arms image, postal code, coordinate location）

## g0861 — wikidbs10k：見出し「index fungorum id」（Wikidata の型 `string`）（15 列）
- 例1：204740 | 134768 | 169523 | 106356 | 157260（表：natural product／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例2：536196 | 18091 | 17597 | 17328 | 18250（表：taxon／同じ表の列：label, description, MycoBank taxon name…, Encyclopedia of Lif…, taxon rank, taxon name）
- 例3：474361 | 148413 | 205947 | 316467 | 531546（表：secretion or excretion／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g0862 — wikidbs10k：見出し「kinopoisk film id」（Wikidata の型 `string`）（15 列）
- 例1：412344.0 | 741231.0 | 1008491.0 | 1188984.0 | 977754.0（表：series／同じ表の列：label, description, instance of, IMDb ID, genre, original language o…）
- 例2：677638 | 495671 | 8062 | 1141782 | 566232（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例3：187433 | 548973 | 63628 | 425265 | 523149（表：sixth generation Chinese films／同じ表の列：label, description, IMDb ID, instance of, director, original language o…）

## g0863 — wikidbs10k：見出し「rero id」（Wikidata の型 `string`）（15 列）
- 例1：02-A000064760 | 02-A000156698 | 02-A000195025 | 02-A000074093 | 02-A000109151（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：02-A000056397 | 02-A005497057 | 02-A000050560 | 02-A016967921 | 02-A000195025（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：02-A000093456 | 02-A000156698 | 02-A000058150 | 02-A000050560 | 02-A000044436（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0864 — wikidbs10k：見出し「ted talk id」（Wikidata の型 `string`）（15 列）
- 例1：brian_dettmer_old_books_reborn_as_intri… | eddy_cartaya_my_glacier_cave_discoveries | nizar_ibrahim_how_we_unearthed_the_spin… | fredy_peccerelli_a_forensic_anthropolog… | kenneth_shinozuka_my_simple_invention_d…（表：TEDYouth talk／同じ表の列：label, description, instance of, inventory number, collection, inception）
- 例2：sergey_brin_and_larry_page_on_google | susan_savage_rumbaugh_on_apes_that_write | keith_barry_does_brain_magic | sheila_patek_clocks_the_fastest_animals | jennifer_lin_improvs_piano_magic（表：TED2004／同じ表の列：label, description, author, instance of, genre, inventory number）
- 例3：andreas_schleicher_use_data_to_build_be… | marco_tempest_a_cyber_magic_card_trick_… | heather_brooke_my_battle_to_expose_gove… | kirby_ferguson_embrace_the_remix.html | amy_cuddy_your_body_language_shapes_who…（表：TEDGlobal 2012／同じ表の列：label, description, instance of, author, publication date, inventory number）

## g0865 — wikidbs10k：見出し「terc municipality code」（Wikidata の型 `string`）（15 列）
- 例1：0802064 | 2808011 | 3021094 | 2001011 | 3012044（表：place of birth／同じ表の列：label, description, country, located in the admi…, coordinate location, instance of）
- 例2：3021093 | 1808053 | 0207 | 3007042 | 0802063（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, country, coordinate location, instance of）
- 例3：1433082 | 0603122 | 4324307033 | 0409043 | 1608062（表：administrative territorial entity／同じ表の列：label, description, country, coordinate location, located in the admi…, instance of）

## g0866 — wikidbs10k：見出し「thailand central administrative unit code」（Wikidata の型 `string`）（15 列）
- 例1：450908 | 630205 | 801503 | 840403 | 1401（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, country, instance of, postal code）
- 例2：500108 | 342003 | 18 | 320801 | 630610（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, instance of, postal code）
- 例3：321006 | 320601 | 321401 | 300701 | 441008（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, country, instance of, postal code）

## g0867 — wikidbs10k：見出し「start time」（Wikidata の型 `time`）（15 列）
- 例1：-3200000000-00-00T00:00:00Z | -251000000-00-00T00:00:00Z | -66000000-00-00T00:00:00Z | -2500000000-00-00T00:00:00Z | -541000000-00-00T00:00:00Z（表：erathem／同じ表の列：label, description, instance of, part of, followed by, sRGB color hex trip…）
- 例2：-66000000-00-00T00:00:00Z | -1600000000-00-00T00:00:00Z | -3200000000-00-00T00:00:00Z | -1000000000-00-00T00:00:00Z | -3800000000-01-01T00:00:00Z（表：followed by／同じ表の列：label, description, instance of, follows, followed by, Commons category）
- 例3：-4000000000-00-00T00:00:00Z | -2800000000-00-00T00:00:00Z | -251000000-00-00T00:00:00Z | -1600000000-00-00T00:00:00Z | -3600000000-00-00T00:00:00Z（表：follows／同じ表の列：label, description, instance of, part of, followed by, Commons category）

## g0868 — wikidbs10k：見出し「discoverer or inventor」（Wikidata の型 `wikibase-entityid`）（15 列）
- 例1：Chad Trujillo | John J. Kavelaars | David L. Rabinowitz | Arianna Gleason | Nichole M. Danzl（表：possible dwarf planet／同じ表の列：label, description, instance of, orbital inclination, orbital eccentricity, Minor Planet Center…）
- 例2：Galileo Galilei | John Frederick William Herschel | Charles Messier | Nicolas Louis de Lacaille | James Dunlop（表：stellar association／同じ表の列：label, description, constellation, Commons category, catalog code, instance of）
- 例3：Albert Ghiorso | Stanley Gerald Thompson | Marie Curie | Joint Institute for Nuclear Research | Glenn T. Seaborg（表：period 7／同じ表の列：label, description, OmegaWiki Defined M…, Dewey Decimal Class…, named after, element symbol）

## g0869 — wikidbs10k：見出し「significant place」（Wikidata の型 `wikibase-entityid`）（15 列）
- 例1：Kotzebue | Pueblo | Hammonton | Juneau | New Orleans（表：national preserve／同じ表の列：label, description, Commons category, located in the admi…, IUCN protected area…, instance of）
- 例2：Lac-Nilgaut | Sept-Îles | Forestville | Rapides-des-Joachims | Cascapédia–Saint-Jules（表：Zone d'exploitation contrôlée／同じ表の列：label, description, instance of, country, coordinate location, inception）
- 例3：Mandritsara | Farafangana | Tsiroanomandidy | Morondava | Betroka（表：special reserve of Madagascar／同じ表の列：label, description, coordinate location, IUCN protected area…, WDPA ID, instance of）

## g0870 — wikidbs10k：見出し「tracklist」（Wikidata の型 `wikibase-entityid`）（15 列）
- 例1：Hammer Horror | The Man With The Child In His Eyes | The Dreaming | Sat In Your Lap | Army Dreamers（表：The Single File 1978~1983／同じ表の列：label, description, performer, instance of, MusicBrainz release…, publication date）
- 例2：Sat In Your Lap | Army Dreamers | There Goes A Tenner | Them Heavy People | Hammer Horror（表：publishing／同じ表の列：label, description, instance of, performer, record label, part of）
- 例3：Here You Come Again | The River Unbroken | I Really Got the Feeling | Holly Jolly Christmas | I Will Always Love You（表：Dolly Parton studio album discography／同じ表の列：label, description, performer, record label, instance of, MusicBrainz release…）

## g0871 — wikidbs10k：見出し「type of orbit」（Wikidata の型 `wikibase-entityid`）（15 列）
- 例1：low Earth orbit（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例2：low Earth orbit（表：spaceflight／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）
- 例3：low Earth orbit（表：follows／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）

## g0872 — wikidbs10k：見出し「inflation rate」（Wikidata の型 `quantity`）（14 列）
- 例1：+2.1 | +1.4 | +3.4 | +1.7 | +1.2（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, Freebase ID, instance of）
- 例2：+1.4 | +12.4 | +2.2 | +0.3 | +1.8（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, instance of, BabelNet ID）
- 例3：1.3 | 1.2 | 0.7 | 0.9 | 2.2（表：economy of region／同じ表の列：label, description, Commons category, topic's main catego…, instance of, Quora topic ID）

## g0873 — wikidbs10k：見出し「poverty incidence」（Wikidata の型 `quantity`）（14 列）
- 例1：+14.00 | +25.31 | +4.61 | +13.10 | +4.19（表：component city／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例2：25.44 | 4.46 | 16.78 | 28.41 | 34.37（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, flag image, ISO 3166-2 code）
- 例3：+10.72 | +36.50 | +2.71 | +13.51 | +6.13（表：political border／同じ表の列：label, description, country, located in the admi…, locator map image, coordinate location）

## g0874 — wikidbs10k：見出し「bavarian monument map object id (architectural monument)」（Wikidata の型 `string`）（14 列）
- 例1：195350 | 164696 | 29804 | 59072 | 165781（表：Amthaus／同じ表の列：label, description, located in the admi…, country, heritage designation, instance of）
- 例2：89283 | 172357 | 89311 | 64980 | 74792（表：basement／同じ表の列：label, description, country, coordinate location, located in the admi…, instance of）
- 例3：18363 | 206951 | 218995 | 150466 | 17978（表：köblergut／同じ表の列：label, description, Bavarian monument a…, located in the admi…, country, heritage designation）

## g0875 — wikidbs10k：見出し「canmore id」（Wikidata の型 `string`）（14 列）
- 例1：262390 | 211169 | 240188 | 110985 | 240189（表：farm labourers cottage／同じ表の列：label, description, country, coordinate location, heritage designation, instance of）
- 例2：237363 | 233115 | 254377 | 254376 | 255785（表：workers cottage／同じ表の列：label, description, Historic Environmen…, coordinate location, country, heritage designation）
- 例3：267624 | 260753 | 261665 | 120981 | 283284（表：lighter／同じ表の列：label, description, instance of, coordinate location, located in the admi…, country）

## g0876 — wikidbs10k：見出し「chemspider id」（Wikidata の型 `string`）（14 列）
- 例1：17215804 | 9176 | 22420 | 13836545 | 6087（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：391 | 9605 | 275 | 9176 | 8992（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：6803 | 5889 | 6083 | 4573986 | 2005851（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0877 — wikidbs10k：見出し「discogs label id」（Wikidata の型 `string`）（14 列）
- 例1：638774 | 6621 | 203082 | 7876 | 119486（表：record label／同じ表の列：label, description, instance of, country, MusicBrainz label ID）
- 例2：1005 | 23175 | 35584 | 66362 | 102606（表：record label／同じ表の列：label, description, instance of, inception, country, MusicBrainz label ID）
- 例3：40343 | 12125 | 34032 | 39972 | 1610（表：record label／同じ表の列：label, description, instance of, inception, MusicBrainz label ID, country）

## g0878 — wikidbs10k：見出し「dsstox compound identifier」（Wikidata の型 `string`）（14 列）
- 例1：DTXCID304938 | DTXCID3031107 | DTXCID406387 | DTXCID1031094 | DTXCID001366053（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：DTXCID30637 | DTXCID406387 | DTXCID401439 | DTXCID801435 | DTXCID401434（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：DTXCID2031950 | DTXCID801332014 | DTXCID301207 | DTXCID20250 | DTXCID70679（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0879 — wikidbs10k：見出し「dsstox substance id」（Wikidata の型 `string`）（14 列）
- 例1：DTXSID7052521 | DTXSID1023992 | DTXSID1020302 | DTXSID0024008 | DTXSID0020600（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：DTXSID5023958 | DTXSID6052534 | DTXSID20872822 | DTXSID8021434 | DTXSID7052521（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：DTXSID0024187 | DTXSID5021207 | DTXSID6022422 | DTXSID9021390 | DTXSID5020601（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0880 — wikidbs10k：見出し「nickel-strunz '10th ed', review of (9th ed/ 2009 update)」（Wikidata の型 `string`）（14 列）
- 例1：6.DA.25 | 6.AC.40 | 6.AA.15 | 6.AB.70 | 6.FC.15（表：borate class of minerals／同じ表の列：label, description, named after, subclass of, IMA status and/or r…, crystal system）
- 例2：3.CB.30 | 3.CB.25 | 3.CB.20 | 3.CB.40 | 3.CB.15（表：neso-aluminofluoride minerals (3.CB.)／同じ表の列：label, description, Strunz 8th edition …, subclass of, chemical formula, Nickel-Strunz 9th e…）
- 例3：6.BB.05 | 6.FA.05 | 6.BA.15 | 6.CA.40 | 6.CA.20（表：nesoborate mineral subclass／同じ表の列：label, description, subclass of, IMA status and/or r…, named after, chemical formula）

## g0881 — wikidbs10k：見出し「odot county code」（Wikidata の型 `string`）（14 列）
- 例1：CLE | TRU | WAY | MRG | MAH（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, country, Commons category, licence plate code）
- 例2：PRE | FRA | NOB | HIG | ERI（表：political border／同じ表の列：label, description, country, Commons category, located in the admi…, licence plate code）
- 例3：WAR | PIC | PRE | BUT | ERI（表：administrative centre／同じ表の列：label, description, country, Commons category, located in the admi…, licence plate code）

## g0882 — wikidbs10k：見出し「coextensive with」（Wikidata の型 `wikibase-entityid`）（14 列）
- 例1：Western Australia | Australian Capital Territory | Tasmania | Victoria | Northern Territory（表：administrative territorial entity／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）
- 例2：Madhya Pradesh | Uttar Pradesh | Punjab | Maharashtra | National Capital Territory of Delhi（表：jurisdiction／同じ表の列：label, description, population, Getty Thesaurus of …, Wikimedia outline, GeoNames ID）
- 例3：Bihar | Jharkhand | National Capital Territory of Delhi | Arunachal Pradesh | West Bengal（表：political border／同じ表の列：label, description, instance of, shares border with, head of state, Commons category）

## g0883 — wikidbs10k：見出し「crosses」（Wikidata の型 `wikibase-entityid`）（14 列）
- 例1：Bajánsenye–Zalaegerszeg–Ukk–Boba railwa… | Yangtze | Ría de Pontevedra | Urado Bay | Takatsudo Gorge（表：rigid-frame bridge／同じ表の列：label, description, coordinate location, instance of, located in the admi…, country）
- 例2：Årstaviken | River Thames | Lilla Värtan | Junction Hollow | Karun-3 Lake（表：truss arch bridge／同じ表の列：label, description, Commons category, coordinate location, Freebase ID, instance of）
- 例3：Saint Louis River | River Mersey | Ulvsund strait | St. Clair River | Lot（表：through arch bridge／同じ表の列：label, description, Commons category, coordinate location, instance of, image）

## g0884 — wikidbs10k：見出し「crystal system」（Wikidata の型 `wikibase-entityid`）（14 列）
- 例1：tetragonal crystal system | trigonal crystal system | cubic crystal system | hexagonal crystal system | triclinic crystal system（表：borate class of minerals／同じ表の列：label, description, Nickel-Strunz '10th…, named after, subclass of, IMA status and/or r…）
- 例2：cubic crystal system | orthorhombic crystal system | monoclinic crystal system | trigonal crystal system | triclinic crystal system（表：neso-aluminofluoride minerals (3.CB.)／同じ表の列：label, description, Strunz 8th edition …, subclass of, chemical formula, Nickel-Strunz 9th e…）
- 例3：triclinic crystal system | monoclinic crystal system | trigonal crystal system | tetragonal crystal system | orthorhombic crystal system（表：nesoborate mineral subclass／同じ表の列：label, description, Nickel-Strunz '10th…, subclass of, IMA status and/or r…, named after）

## g0885 — wikidbs10k：見出し「drainage basin」（Wikidata の型 `wikibase-entityid`）（14 列）
- 例1：Danube basin | Neckar basin | Elbe Basin | Rhine basin | Weser Basin（表：body of water／同じ表の列：label, description, mouth of the waterc…, instance of, Commons category, country）
- 例2：Rhine basin | Rhône basin | Vltava Basin（表：body of water／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例3：Caspian Sea Basin | Persian Gulf Basin | Ebro Basin | Dasht-e Lut Basin | Tagus Basin（表：buttress dam／同じ表の列：label, description, Commons category, coordinate location, instance of, image）

## g0886 — wikidbs10k：見出し「location of creation」（Wikidata の型 `wikibase-entityid`）（14 列）
- 例1：Montreal | Saint John | Sorel | Lauzon | Vancouver（表：His Majesty's Canadian Ship／同じ表の列：label, description, instance of, image, operator, military branch）
- 例2：Hamburg | Gdańsk | Emden | Wilhelmshaven | Rostock（表：31st U-boat Flotilla／同じ表の列：label, description, operator, instance of, conflict, vessel class）
- 例3：Blandford Forum | Bayreuth | Mantes-la-Jolie | Boston | Adorf/Vogtl.（表：clarinet／同じ表の列：label, description, inventory number, collection, instance of, described at URL）

## g0887 — wikidbs10k：見出し「location of landing」（Wikidata の型 `wikibase-entityid`）（14 列）
- 例1：Kazakhstan | Launch and Landing Facility | Edwards Air Force Base | Kennedy Space Center（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）
- 例2：Kennedy Space Center | Launch and Landing Facility | Kazakhstan（表：spaceflight／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）
- 例3：Kazakhstan | Edwards Air Force Base（表：follows／同じ表の列：label, description, COSPAR ID, SCN, Commons category, UTC date of spacecr…）

## g0888 — wikidbs10k：見出し「declination component of proper motion」（Wikidata の型 `quantity`）（13 列）
- 例1：-184.248 | -230.952 | +2.888 | -40.6 | -1.217（表：primary body／同じ表の列：label, description, constellation, instance of, catalog code, apparent magnitude）
- 例2：-673.638 | -1063.69 | +41.382 | -1183.784 | -190.919（表：super-Earth／同じ表の列：label, description, time of discovery o…, constellation, catalog code, instance of）
- 例3：-990.311 | -215.545 | -60.151 | -84.87 | -143.768（表：primary body／同じ表の列：label, description, constellation, spectral class, catalog code, instance of）

## g0889 — wikidbs10k：見出し「orbital eccentricity」（Wikidata の型 `quantity`）（13 列）
- 例1：+0.446 | +0.177 | +0.095 | +0.047 | +0.216（表：possible dwarf planet／同じ表の列：label, description, discoverer or inven…, instance of, orbital inclination, Minor Planet Center…）
- 例2：+0.09339410 | +0.07578254213963266 | +0.0567 | +0.0151 | +0.0288（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, image）
- 例3：+0.15 | +0.336 | +0.0186 | +0.082 | +0.03（表：super-Earth／同じ表の列：label, description, time of discovery o…, constellation, catalog code, instance of）

## g0890 — wikidbs10k：見出し「parallax」（Wikidata の型 `quantity`）（13 列）
- 例1：+742.12 | +78.7565 | +33.3264 | +1.3279 | +26.4417（表：primary body／同じ表の列：label, description, constellation, instance of, catalog code, apparent magnitude）
- 例2：+42.6090 | +116.89 | +37.1787 | +5.1088 | +68.2653（表：super-Earth／同じ表の列：label, description, time of discovery o…, constellation, catalog code, instance of）
- 例3：79.5945 | 273.96 | 3.5103 | 77.2727 | 138.0171（表：primary body／同じ表の列：label, description, constellation, spectral class, catalog code, instance of）

## g0891 — wikidbs10k：見出し「right ascension component of proper motion」（Wikidata の型 `quantity`）（13 列）
- 例1：-462.056 | -586.287 | -25.939 | +82.841 | +78.493（表：primary body／同じ表の列：label, description, constellation, instance of, catalog code, apparent magnitude）
- 例2：-566.861 | +9.974 | +1131.612 | -52.423 | -94.027（表：super-Earth／同じ表の列：label, description, time of discovery o…, constellation, catalog code, instance of）
- 例3：10.96 | 138.694 | 1041.7 | -3723.0 | -11.4（表：primary body／同じ表の列：label, description, constellation, spectral class, catalog code, instance of）

## g0892 — wikidbs10k：見出し「speed」（Wikidata の型 `quantity`）（13 列）
- 例1：+47.134 | +53.310 | +42.738 | +37.193 | +42.610（表：2017 UCI Road World Championships／同じ表の列：label, description, instance of, follows, sport, part of）
- 例2：37.33 | 48.282 | 49.979 | 37.193000000000005 | 36.299（表：followed by／同じ表の列：label, description, instance of, part of, sport, country）
- 例3：+38.883 | +35.73 | +39.45 | +35.70 | +38.68（表：GP de Plouay／同じ表の列：label, description, sport, instance of, edition number, followed by）

## g0893 — wikidbs10k：見出し「atvk id」（Wikidata の型 `string`）（13 列）
- 例1：0561800 | 0905700 | 0005000 | 0961000 | 0056000（表：administrative territorial entity／同じ表の列：label, description, country, ISO 3166-2 code, coordinate location, topic's main catego…）
- 例2：51220.0 | 54010.0 | 1000.0 | 26210.0 | 46210.0（表：physical location／同じ表の列：label, description, coat of arms image, country, coordinate location, Commons category）
- 例3：26000.0 | 34421.0 | 51000.0 | 48410.0 | 47000.0（表：administrative territorial entity／同じ表の列：label, description, instance of, inception, country, located in the admi…）

## g0894 — wikidbs10k：見出し「catalogue of life in taiwan id」（Wikidata の型 `string`）（13 列）
- 例1：423677.0 | 110313.0 | 110314.0 | 423676.0 | 110321.0（表：taxon／同じ表の列：label, description, Commons category, taxon rank, image, parent taxon）
- 例2：423231 | 110258 | 110243 | 110261 | 400052（表：taxon／同じ表の列：label, description, image, taxon rank, parent taxon, taxon name）
- 例3：110309.0 | 423676.0 | 423666.0 | 110314.0 | 110313.0（表：taxon／同じ表の列：label, description, Commons category, taxon name, image, taxon rank）

## g0895 — wikidbs10k：見出し「chebi id」（Wikidata の型 `string`）（13 列）
- 例1：29389 | 36014 | 16503 | 30288 | 29308（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：48002 | 47554 | 36014 | 16842 | 30288（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：82321 | 33038 | 17296 | 34036 | 66892（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0896 — wikidbs10k：見出し「e-maapõu stratigraphy id」（Wikidata の型 `string`）（13 列）
- 例1：152.0 | 82.0 | 7.0 | 149.0 | 148.0（表：followed by／同じ表の列：label, description, instance of, follows, followed by, Commons category）
- 例2：151 | 148 | 149 | 147 | 152（表：follows／同じ表の列：label, description, instance of, part of, followed by, Commons category）
- 例3：74.0 | 227.0 | 582.0 | 249.0 | 136.0（表：followed by／同じ表の列：label, description, followed by, follows, part of, instance of）

## g0897 — wikidbs10k：見出し「eidr content id」（Wikidata の型 `string`）（13 列）
- 例1：10.5240/909B-0D87-4FEE-3312-01A3-Z | 10.5240/4BE1-D18D-85E6-A498-D4E1-A | 10.5240/4490-FD83-E5B0-3F9E-8932-8 | 10.5240/BD01-3E8D-54DF-829C-D145-I | 10.5240/E0C1-A434-54F6-5304-9B98-Y（表：clip show／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例2：10.5240/C44C-4039-2C9C-5D75-2174-D | 10.5240/C763-64CC-A10E-3788-48D3-T | 10.5240/55F0-15E1-50C8-89A9-500A-L | 10.5240/4420-EE7E-B8AA-9702-E078-9 | 10.5240/FFC3-5BDD-4645-1A9F-87F6-Y（表：television series season／同じ表の列：label, description, instance of, Freebase ID, part of the series, number of episodes）
- 例3：10.5240/68D2-18FC-1F6E-747C-1AC8-O | 10.5240/1158-28E8-622B-5F94-293A-X | 10.5240/B28C-D08B-FBE4-6822-4288-H | 10.5240/5651-1B0E-7F37-B604-C1F2-I | 10.5240/B14B-F4AD-0D85-CDF5-5C1B-0（表：followed by／同じ表の列：label, description, instance of, part of the series, follows, followed by）

## g0898 — wikidbs10k：見出し「nioshtic-2 id」（Wikidata の型 `string`）（13 列）
- 例1：00058517 | 00058520 | 00058522 | 00058521 | 00058524（表：Second NIOSH solid sorbents roundtable／同じ表の列：label, description, sponsor, publication date, author name string, instance of）
- 例2：20049437 | 20049397 | 10004834 | 20049434 | 20049422（表：3rd Symposium on Respirable Dust in the…／同じ表の列：label, description, sponsor, publication date, author name string, instance of）
- 例3：20044864 | 20044860 | 20044865 | 20044871 | 20044863（表：7th International aerosol conference [a…／同じ表の列：label, description, sponsor, publication date, author name string, instance of）

## g0899 — wikidbs10k：見出し「trakt.tv id」（Wikidata の型 `string`）（13 列）
- 例1：shows/battle-for-dream-island/seasons/2… | shows/battle-for-dream-island/seasons/4… | shows/battle-for-dream-island/seasons/2… | shows/battle-for-dream-island/seasons/1… | shows/battle-for-dream-island/seasons/4…（表：first appearance／同じ表の列：label, description, instance of, part of the series, title, season）
- 例2：shows/battle-for-dream-island/seasons/1… | shows/battle-for-dream-island/seasons/1… | shows/battle-for-dream-island/seasons/4… | shows/battle-for-dream-island/seasons/4… | shows/battle-for-dream-island/seasons/4…（表：followed by／同じ表の列：label, description, instance of, part of the series, title, season）
- 例3：shows/battle-for-dream-island/seasons/1… | shows/battle-for-dream-island/seasons/4… | shows/battle-for-dream-island/seasons/1… | shows/battle-for-dream-island/seasons/1… | shows/battle-for-dream-island/seasons/4…（表：follows／同じ表の列：label, description, instance of, part of the series, title, season）

## g0900 — wikidbs10k：見出し「category for recipients of this award」（Wikidata の型 `wikibase-entityid`）（13 列）
- 例1：Category:Fellows of the American Physic… | Category:Recipients of the Copley Medal | Category:Officiers of the Légion d'honn… | Category:Howard N. Potts Medal recipien… | Category:Recipients of the Order of Fri…（表：award／同じ表の列：label, description, country, instance of）
- 例2：Category:Recipients of the Order of the… | Category:Recipients of the Order of St.… | Category:Knights of the Golden Fleece | Category:Grand Croix of the Légion d'ho… | Category:Recipients of the National Ord…（表：award／同じ表の列：label, description, instance of, country, service ribbon image, next higher rank）
- 例3：Category:Recipients of the Order of the… | Category:Recipients of the Order of the… | Category:Recipients of the Order of the… | Category:Recipients of the Order of the… | Category:Recipients of the Order of the…（表：Order of the Precious Crown／同じ表の列：label, description, instance of, part of, inception, image）

## 答えの雛形

```
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
g0841	
g0842	
g0843	
g0844	
g0845	
g0846	
g0847	
g0848	
g0849	
g0850	
g0851	
g0852	
g0853	
g0854	
g0855	
g0856	
g0857	
g0858	
g0859	
g0860	
g0861	
g0862	
g0863	
g0864	
g0865	
g0866	
g0867	
g0868	
g0869	
g0870	
g0871	
g0872	
g0873	
g0874	
g0875	
g0876	
g0877	
g0878	
g0879	
g0880	
g0881	
g0882	
g0883	
g0884	
g0885	
g0886	
g0887	
g0888	
g0889	
g0890	
g0891	
g0892	
g0893	
g0894	
g0895	
g0896	
g0897	
g0898	
g0899	
g0900	
```
