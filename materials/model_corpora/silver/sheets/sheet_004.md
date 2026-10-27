# 銀ラベルのシート 004 / 008（外の学習データの読み替え）

- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列
- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`
- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を、ChatGPT は `answers/sheet_004.tsv`、Grok は `answers_grok/sheet_004.tsv` に写して埋める。**相手の答えは見ない**

## g0451 — wikidbs10k：見出し「decays to」（Wikidata の型 `wikibase-entityid`）（126 列）
- 例1：iodine-134 | xenon-140 | xenon-134 | xenon-132 | iodine-133（表：isotope of iodine／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例2：fluorine-17 | fluorine-19 | sodium-34 | sodium-30 | sodium-23（表：neon／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例3：magnesium-33 | oxygen-17 | nitrogen-14 | oxygen-18 | magnesium-24（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）

## g0452 — sotab_v2：元の種類 `Museum/name`（125 列）
- 例1：Shemer Art Center &amp; Museum | USS Bowfin Submarine Museum and Park | Pima Air and Space Museum | Nordic Heritage Museum | The Huntington Library, Art Collections…（DBpedia：Museum）
- 例2：The Fabric Workshop and Museum | El Paso Museum of Art (EPMA) | The University of Arizona Museum of Art… | McMullen Museum | Museo de la Estampa del Estado de México（DBpedia：Museum）
- 例3：Eden Camp Modern History Theme Museum | We The Curious | Colchester Castle Museum | The British Museum | Royal Yacht Britannia（DBpedia：Museum）

## g0453 — wikidbs10k：見出し「manufacturer」（Wikidata の型 `wikibase-entityid`）（125 列）
- 例1：Commodore International | Flex Ltd. | Apple | Sony Interactive Entertainment | Atari Corporation（表：follows／同じ表の列：label, description, Commons category, Freebase ID, follows, followed by）
- 例2：Sportron | R10 | Videomaster | Retro Games Limited | Worlds of Wonder（表：home video game console model／同じ表の列：label, description, instance of, part of, publication date, subclass of）
- 例3：Ricoh | Agfa-Gevaert | Sony | Olympus | Leica Camera（表：digital camera product line／同じ表の列：label, description, instance of）

## g0454 — wikidbs10k：見出し「pubmed id」（Wikidata の型 `string`）（124 列）
- 例1：14527956 | 17928589 | 18950639 | 15716355 | 10559940（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）
- 例2：15377279 | 19380584 | 11457814 | 11242081 | 156362（表：citation／同じ表の列：label, description, page(s), title, author name string, publication date）
- 例3：19040639 | 15886207 | 16884737 | 16452418 | 17638697（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）

## g0455 — wikidbs10k：見出し「season of club or team」（Wikidata の型 `wikibase-entityid`）（124 列）
- 例1：Seoul Cycling Team（表：Seoul Cycling Team／同じ表の列：label, description, sport, instance of, start time, end time）
- 例2：Ineos Grenadiers（表：Ineos Grenadiers／同じ表の列：label, description, instance of, sport, UCI code of cycling…, general manager）
- 例3：Ineos Grenadiers（表：followed by／同じ表の列：label, description, instance of, sport, UCI code of cycling…, follows）

## g0456 — wikidbs10k：見出し「ehess id of a french commune」（Wikidata の型 `string`）（123 列）
- 例1：3552.0 | 23650.0 | 26207.0 | 11845.0 | 35814.0（表：administrative territorial entity／同じ表の列：label, description, instance of, Commons category, located in the admi…, coordinate location）
- 例2：15302 | 31594.0 | 28966.0 | 26207.0 | 27121（表：political border／同じ表の列：label, description, coordinate location, instance of, located in the admi…, shares border with）
- 例3：592 | 40662 | 9421 | 8760 | 20874（表：capital city／同じ表の列：label, description, official website, topic's main catego…, country, INSEE municipality …）

## g0457 — wikidbs10k：見出し「personality database profile id」（Wikidata の型 `string`）（123 列）
- 例1：50644 | 50643 | 50650 | 50654 | 50698（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：50657.0 | 50667.0 | 50656.0 | 50658.0 | 50641.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：50644.0 | 50658.0 | 50646.0 | 50679.0 | 50652.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0458 — wikidbs10k：見出し「ávvir topic id」（Wikidata の型 `string`）（121 列）
- 例1：kanada | ukraina | stuorra-britannia | espannja | polen（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：stuorra-britannia | ruotta | australia | kanada | duiska（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：duiska | stuorra-britannia | nuortariika | australia | ruotta（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0459 — wikidbs10k：見出し「time period」（Wikidata の型 `wikibase-entityid`）（120 列）
- 例1：Jōmon period（表：Jōmon Prehistoric Sites in Northern Jap…／同じ表の列：label, description, Commons category, coordinate location, instance of, country）
- 例2：1994-1995 one-year-period | 2002-2003 one-year-period | 1988-1989 one-year-period | 1999-2000 one-year-period | 1986-1987 one-year-period（表：Coppa Italia／同じ表の列：label, description, sport, on focus list of Wi…, instance of, country）
- 例3：1994-1995 one-year-period | 1990-1991 one-year-period | 1986-1987 one-year-period | 1991-1992 one-year-period | 2004-2005 one-year-period（表：followed by／同じ表の列：label, description, sport, on focus list of Wi…, instance of, country）

## g0460 — sotab_v2：元の種類 `Book/description`（119 列）
- 例1：Princess Dewi is changed into a golden … | This book features adapted motifs of Mi… | A young boy named Lloyd and his grandfa… | A lion found an injured bird in his gar… | This is a tale about the animosity betw…
- 例2：Focus on Foreign Service Authors; Writi… | Focus on The Fall of the Berlin Wall; A… | #StateToo: Ending Harassment at the Sta… | Beyond the Redesign: Can State Deliver?… | Focus on Foreign Service Authors; In Th…
- 例3：This interactive publication is created…

## g0461 — wikidbs10k：見出し「logo image」（Wikidata の型 `string`）（119 列）
- 例1：NES logo.svg | Vectorial Xbox logo.svg | Microsoft Windows Me logo.svg | Nintendo 64 logo.png | Atari 5200 logo.svg（表：follows／同じ表の列：label, description, manufacturer, Commons category, Freebase ID, follows）
- 例2：On3 Radio Logo.svg | Dasding 2011.png | Unserding Logo 2020.svg | You FM Logo 2020.svg | Radio Fritz 2020.svg（表：youth radio／同じ表の列：label, description, instance of, country, Commons category, operator）
- 例3：Rbb Logo 2017.08.svg | MDR Logo 2017.svg | Südwestrundfunk (logo).svg | BR Dachmarke.svg | WDR Dachmarke.svg（表：operator／同じ表の列：label, description, headquarters locati…, Commons category, instance of, Freebase ID）

## g0462 — wikidbs10k：見出し「median income」（Wikidata の型 `quantity`）（118 列）
- 例1：21959.0 | 38584.0 | 31617.0 | 70336.0 | 9218.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：+34822 | +43585 | +38584 | +70336 | +33333（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：+32762 | +34822 | +33333 | +38584 | +43585（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0463 — wikidbs10k：見出し「wals lect code」（Wikidata の型 `string`）（116 列）
- 例1：fin | cze | eng | kor | swe（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：dut | jpn | pol | lat | blr（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：ice | eng | cze | ctl | dut（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0464 — wikidbs10k：見出し「german regional key」（Wikidata の型 `string`）（115 列）
- 例1：096760122122 | 096610000000 | 096710136136 | 096769452452 | 064350009009（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, located in the admi…, coat of arms image）
- 例2：100410511511 | 64.0 | 081210000000 | 14.0 | 91.0（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, country, Commons category, located in the admi…）
- 例3：094630000000 | 094730158158 | 094730144144 | 094730151151 | 094730112112（表：Stimmkreis Coburg／同じ表の列：label, description, country, Commons category, GND ID, German municipality…）

## g0465 — wikidbs10k：見出し「associated electoral district」（Wikidata の型 `wikibase-entityid`）（114 列）
- 例1：canton of Châtelaillon-Plage | canton of Montrouge | canton of la Baule-Escoublac | canton of Redessan | canton of Cagnes-sur-Mer-1（表：political border／同じ表の列：label, description, coordinate location, instance of, located in the admi…, shares border with）
- 例2：canton of la Possession | canton of Chenôve | canton of Vandœuvre-lès-Nancy | canton of Choisy-le-Roi | canton of Saint-Étienne-du-Bois（表：capital city／同じ表の列：label, description, official website, topic's main catego…, country, INSEE municipality …）
- 例3：canton of Cagnes-sur-Mer-1 | canton of Asnières-sur-Seine | canton of Belleville-sur-Meuse | canton of Rezé-1 | canton of la Baule-Escoublac（表：jurisdiction／同じ表の列：label, description, official website, topic's main catego…, country, INSEE municipality …）

## g0466 — wikidbs10k：見出し「uci code of cycling team」（Wikidata の型 `string`）（113 列）
- 例1：INS | SKY | IGD（表：Ineos Grenadiers／同じ表の列：label, description, instance of, sport, general manager, follows）
- 例2：SKY | INS | IGD（表：followed by／同じ表の列：label, description, instance of, sport, follows, followed by）
- 例3：IGD | INS | SKY（表：follows／同じ表の列：label, description, instance of, sport, general manager, followed by）

## g0467 — sotab_v2：元の種類 `JobPosting/name`（112 列）
- 例1：24 Seven Talent
- 例2：ESIC Mumbai Recruitment 2020 - Walk in … | Kerala PSC Recruitment 2020 - Apply Onl… | UPPSC Recruitment 2020 - Apply Online f… | Bharathiar University Recruitment 2020 … | Amrita Vishwa Vidyapeetham Recruitment …
- 例3：2D Storyboard Revisionist | Build and Rigging Supervisor | Remote Storyboard Artist - Contract | Art Director | Lead VFX Artist:

## g0468 — wikidbs10k：見出し「abc news topic id」（Wikidata の型 `string`）（110 列）
- 例1：tennis | handball-team | soccer | fencing | swimming（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）
- 例2：tennis | athletics | volleyball | fencing | soccer（表：field of work／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）
- 例3：rowing | wrestling | modern-pentathlon | basketball | field-hockey（表：type of sport／同じ表の列：label, description, Commons category, subclass of, topic's main catego…, Freebase ID）

## g0469 — wikidbs10k：見出し「iptc newscode」（Wikidata の型 `string`）（109 列）
- 例1：mediatopic/20000849 | mediatopic/20001183 | mediatopic/20001036 | mediatopic/20000851 | mediatopic/20000958（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, Commons category, subclass of, topic's main catego…）
- 例2：mediatopic/20001037 | mediatopic/20000905 | mediatopic/20000847 | mediatopic/20000933 | mediatopic/20001068（表：type of sport／同じ表の列：label, description, subclass of, Commons category, Library of Congress…, topic's main catego…）
- 例3：mediatopic/20001038 | mediatopic/20000969 | mediatopic/20000958 | mediatopic/20000929 | mediatopic/20001071（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）

## g0470 — wikidbs10k：見出し「uk archival thesaurus id」（Wikidata の型 `string`）（108 列）
- 例1：f3/mt335/1703/2760/2058 | f3/mt335/1703/4414/1439 | f3/mt335/966/6071/3720 | f3/mt335/1703/1670/13021 | f3/mt335/5521/5856（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：f3/mt335/1703/4414/6614 | f3/mt335/1703/4413/1154 | f3/mt335/1703/4414/682 | f3/mt335/1703/2760/2058 | f3/mt335/1703/4414/1439（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：f3/mt335/1703/2760/2058 | f3/mt335/1703/4414/1439 | f3/mt335/1703/4414/4593 | f3/mt335/1703/2760/4087 | f3/mt335/1703/1670/756（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0471 — wikidbs10k：見出し「mean age」（Wikidata の型 `quantity`）（107 列）
- 例1：+36.7 | +39.0 | +42.2 | +40.1 | +38.3（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：38.2 | 42.2 | 40.9 | 40.0 | 38.7（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：+38.8 | +42.2 | +39.0 | +38.2 | +40.9（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0472 — wikidbs10k：見出し「binding energy」（Wikidata の型 `quantity`）（106 列）
- 例1：+1087649.31 | +988757.523 | +1124135.514 | +1006985.854 | +904247.928（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例2：+203051.178 | +212520.0 | +97330.832 | +211035.93 | +206873.688（表：neon／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例3：+213472.0 | +202534.925 | +234138.858 | +214837.542 | +225059.04（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）

## g0473 — wikidbs10k：見出し「mass excess」（Wikidata の型 `quantity`）（106 列）
- 例1：-89278.96179 | -87181.18 | -60202.873 | -72986.451 | -89172.156（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例2：+23986.776 | -5154.049 | +23280.117 | +31181.591 | -5731.776（表：neon／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例3：+12246.031 | -1487.4442 | -5517.79 | +1951.702 | -8417.901（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）

## g0474 — wikidbs10k：見出し「statistics canada geographic code」（Wikidata の型 `string`）（106 列）
- 例1：2473020.0 | 2423 | 2407 | 2408 | 2452（表：administrative territorial entity／同じ表の列：label, description, country, coordinate location, located in the admi…, instance of）
- 例2：2405055 | 2477060 | 2417045 | 2402902 | 2471100（表：political border／同じ表の列：label, description, country, located in the admi…, coordinate location, instance of）
- 例3：2479065 | 2457045 | 2442032 | 2472010 | 2451045（表：administrative territorial entity／同じ表の列：label, description, country, instance of, shares border with, located in the admi…）

## g0475 — wikidbs10k：見出し「gazetteer for scotland place id」（Wikidata の型 `string`）（104 列）
- 例1：counties/countyfirst13 | counties/countyfirst1 | counties/countyfirst26 | counties/countyfirst15 | counties/countyfirst28（表：historic county／同じ表の列：label, description, instance of, coordinate location, country, locator map image）
- 例2：towns/townfirst155 | towns/townfirst556 | towns/townfirst278 | towns/townfirst2064 | towns/townfirst84（表：capital city／同じ表の列：label, description, instance of, Commons category, coordinate location, twinned administrat…）
- 例3：counties/countyfirst29 | counties/countyfirst14 | counties/countyfirst30 | counties/countyfirst11 | counties/countyfirst12（表：historic county／同じ表の列：label, description, instance of, country, locator map image, GENUKI ID）

## g0476 — sotab_v2：元の種類 `Event/description`（103 列）
- 例1：By attending this course the participan… | By attending this course the participan… | Throughout our course TLILIC2001 (Licen… | By attending this course the participan… | COURSE CONTENTThis course is designed f…
- 例2：&lt;p&gt;All the benefits of deep water… | &lt;p&gt;Improve flexibility, move bett… | &lt;p&gt;The exciting Latin dances rhyt… | &lt;p&gt;This type of class experience … | &lt;p&gt;This free class will incorpora…
- 例3：&lt;p&gt;Join me for a MELT Intro Works… | &lt;p&gt;If you are new to MELT, Please… | &lt;p&gt;This class is designed for peo… | &lt;p&gt;Registration Required - $75 fo… | &lt;p&gt;All equipment is provided for …

## g0477 — wikidbs10k：見出し「imdb id」（Wikidata の型 `string`）（103 列）
- 例1：ev0000380/1999 | ev0000380/1946 | ev0000380/1995 | ev0000380/1955 | ev0000380/1962（表：Jussi Awards ceremony／同じ表の列：label, description, instance of, point in time, followed by, follows）
- 例2：ev0000380/1978 | ev0000380/2008 | ev0000380/1988 | ev0000380/1971 | ev0000380/1947（表：followed by／同じ表の列：label, description, instance of, point in time, follows, followed by）
- 例3：ev0000380/1947 | ev0000380/1971 | ev0000380/1957 | ev0000380/1979 | ev0000380/1945（表：follows／同じ表の列：label, description, instance of, follows, followed by, point in time）

## g0478 — wikidbs10k：見出し「seal image」（Wikidata の型 `string`）（103 列）
- 例1：Seal of Kansas.svg | Seal of Montana.svg | Seal of Florida.svg | Seal of Maryland (reverse).svg | Seal of California.svg（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：Seal of Maryland (reverse).svg | Seal of Illinois.svg | Reverse of the Great Seal of the Realm … | Seal of Pennsylvania.svg | Seal of Florida.svg（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：Reverse of the Great Seal of the Realm … | Seal of Maryland (reverse).svg | Seal of Pennsylvania.svg | Seal of Florida.svg | Seal of New York (state).svg（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0479 — sotab_v2：元の種類 `Hotel/description`（102 列）
- 例1：Relax in the spectacular surroundings a… | Domes Zeen Chania features a restaurant… | Occupying a prime hillside plot, the Ma… | Electra Palace Rhodes is an exquisite p… | Set amidst lush greenery, in Agios Ioan…
- 例2：Unique wilderness adventure lodge insid… | Charming cabins, couples retreat, inspi… | Experience Alaska on the Kenai Peninsul… | Featuring spectacular mountain views an… | Anglers Lodge is a family-owned and ope…
- 例3：In addition to our on-site restaurant, … | Arlington's all new Ranger Inn and Suit… | Property Location With a stay at Studio… | The Hampton Inn & Suites Arlington Nort… | The Courtyard Dallas Arlington South, o…

## g0480 — wikidbs10k：見出し「form of creative work」（Wikidata の型 `wikibase-entityid`）（101 列）
- 例1：soundtrack album | compilation soundtrack album | compilation album | studio album（表：Bee Gees' albums in chronological order／同じ表の列：label, description, instance of, performer, title, place of publication）
- 例2：song（表：audio recording／同じ表の列：label, description, instance of, title, language of work or…, composer）
- 例3：double album | compilation album | studio album | live album（表：Ornella Vanoni's albums in chronologica…／同じ表の列：label, description, MusicBrainz release…, instance of, performer, publication date）

## g0481 — wikidbs10k：見出し「language regulatory body」（Wikidata の型 `wikibase-entityid`）（101 列）
- 例1：Swedish Language Council | The National Institute of the Korean La… | Council for the Polish Language | Association of Academies of the Spanish… | Académie Française（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：Swedish Language Council | Association of Academies of the Spanish… | Latvian State Language Center | Kokugo Shingikai | Académie Française（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：Accademia della Crusca | Institute for the Languages of Finland | Council for the Polish Language | Nederlandse Taalunie | Árni Magnússon Institute for Icelandic …（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0482 — wikidbs10k：見出し「entry in abbreviations table」（Wikidata の型 `string`）（100 列）
- 例1：польск. | араб. | чеш. | фин. | нидерл.（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：франц. | белорус. | англ. | польск. | фин.（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：англ. | чеш. | исп. | дат. | франц.（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0483 — wikidbs10k：見出し「duration」（Wikidata の型 `quantity`）（99 列）
- 例1：+1（表：era／同じ表の列：label, description, instance of, start time, end time, short name）
- 例2：+1（表：era／同じ表の列：label, description, instance of, start time, end time, short name）
- 例3：+1（表：era／同じ表の列：label, description, instance of, start time, end time, short name）

## g0484 — wikidbs10k：見出し「gyldendals teaterleksikon id」（Wikidata の型 `string`）（99 列）
- 例1：Schweiz | Indonesien | Japan | Kina | Spanien（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Danmark | Belgien | Schweiz | Norge | Slovakiet（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Østrig | Schweiz | Tyskland | Danmark | Norge（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0485 — wikidbs10k：見出し「mapy.cz id」（Wikidata の型 `string`）（98 列）
- 例1：base&id=2085407 | base&id=1909423 | base&id=2085586 | base&id=2086084 | base&id=2086245（表：national nature reserve／同じ表の列：label, description, instance of, Commons category, ÚSOP code, country）
- 例2：muni&id=2075 | muni&id=931 | muni&id=4571 | dist&id=55 | muni&id=2037（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, country, LAU）
- 例3：muni&id=1145 | dist&id=31 | dist&id=53 | muni&id=2026 | dist&id=77（表：political border／同じ表の列：label, description, located in the admi…, Commons category, LAU, instance of）

## g0486 — wikidbs10k：見出し「regiowikiat id」（Wikidata の型 `string`）（96 列）
- 例1：3000 | 836 | 2544 | 3604 | 2535（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, coordinate location, located in the admi…）
- 例2：2534.0 | 3007 | 841 | 795.0 | 4432.0（表：political border／同じ表の列：label, description, country, Commons category, coordinate location, located in the admi…）
- 例3：6813 | 6812 | 6810 | 6805 | 6814（表：calendar month／同じ表の列：label, description, page banner, image, OmegaWiki Defined M…, named after）

## g0487 — wikidbs10k：見出し「connecting line」（Wikidata の型 `wikibase-entityid`）（95 列）
- 例1：Great Western Main Line | Romford to Upminster Line | Shenfield–Southend line | TfL Rail | Central line（表：Crossrail／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例2：West Ealing Loop, West Ealing Junction … | Shenfield–Southend line | Romford to Upminster Line | Slough to Windsor & Eton Line | TfL Rail（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例3：Metropolitan line | Central line | Romford to Upminster Line | Fen line | Circle line（表：terminus／同じ表の列：label, description, Commons category, coordinate location, country, instance of）

## g0488 — wikidbs10k：見出し「studied by」（Wikidata の型 `wikibase-entityid`）（94 列）
- 例1：graph theory（表：hypercube／同じ表の列：label, description, subclass of, has facet polytope）
- 例2：solid geometry | graph theory（表：facet／同じ表の列：label, description, has facet polytope, subclass of）
- 例3：French studies | Korean studies | Czech studies | Portuguese studies | Scandinavian studies（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0489 — wikidbs10k：見出し「adjacent station」（Wikidata の型 `wikibase-entityid`）（93 列）
- 例1：Seven Kings railway station | Aldgate East tube station | Ealing Broadway railway station | Heathrow Terminal 4 railway station | Belvedere railway station（表：Crossrail／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例2：Langley railway station | Baker Street tube station | Ingatestone railway station | Romford railway station | Forest Gate railway station（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例3：Goldhawk Road tube station | Chadwell Heath railway station | London Waterloo East railway station | Pudding Mill Lane | Bedminster railway station（表：terminus／同じ表の列：label, description, Commons category, coordinate location, country, instance of）

## g0490 — wikidbs10k：見出し「league」（Wikidata の型 `wikibase-entityid`）（93 列）
- 例1：NCAA Division I men's basketball（表：1989 NCAA Men's Division I Basketball T…／同じ表の列：label, description, sport, point in time, Sports-Reference.co…, participating team）
- 例2：Pac-12 Conference | NCAA Division I men's basketball | Big 12 Conference | Southeastern Conference（表：participating team／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例3：Lega Basket Serie A | NCAA Division I men's basketball | Big 12 Conference（表：winner／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）

## g0491 — wikidbs10k：見出し「authority」（Wikidata の型 `wikibase-entityid`）（92 列）
- 例1：HMP Wakefield Independent Monitoring Bo… | HMP Wolds Independent Monitoring Board | HMP Peterborough Independent Monitoring… | HMP Drake Hall Independent Monitoring B… | HMP Guys Marsh Independent Monitoring B…（表：jurisdiction／同じ表の列：label, description, instance of, coordinate location, country, inception）
- 例2：Richmond upon Thames London Borough Cou… | Greater London Authority | Sandwich Town Council | Wylam Parish Council | Prudhoe Town Council（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：Aspatria Town Council | Redruth Town Council | Perth and Kinross Council | New Mills Town Council | Sandwich Town Council（表：jurisdiction／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0492 — wikidbs10k：見出し「copyright status」（Wikidata の型 `wikibase-entityid`）（92 列）
- 例1：public domain（表：Windsor Beauties／同じ表の列：label, description, inventory number, collection, instance of, location）
- 例2：public domain（表：depicting object／同じ表の列：label, description, inventory number, collection, instance of, location）
- 例3：copyrighted（表：first appearance／同じ表の列：label, description, instance of, publication date, publisher, genre）

## g0493 — wikidbs10k：見出し「plantlist-id」（Wikidata の型 `string`）（91 列）
- 例1：kew-2493774 | ild-2663 | ild-19875 | ild-31879 | kew-80043（表：natural product／同じ表の列：label, description, taxon name, taxon rank, parent taxon, NCBI taxonomy ID）
- 例2：kew-2541602 | kew-2560862 | kew-2638973 | kew-354641 | kew-2728977（表：secretion or excretion／同じ表の列：label, description, Commons category, image, taxon name, taxon rank）
- 例3：kew-2687663 | kew-2521219 | kew-2434158 | kew-2587875 | kew-2521326（表：natural product／同じ表の列：label, description, taxon rank, taxon name, parent taxon, NCBI taxonomy ID）

## g0494 — wikidbs10k：見出し「twitter topic id」（Wikidata の型 `string`）（91 列）
- 例1：839543534990446592 | 1234530412447223809 | 1234530343669026823 | 769193663230468096 | 1204161179821600768（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, Commons category, subclass of, topic's main catego…）
- 例2：1.2602887007741542e+18 | 1.2581581155155804e+18 | 1095441021033271296 | 1.2603045952568934e+18 | 1.2600180109510164e+18（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：1255146831282966530 | 1248356249160175616 | 1260288700774154240 | 1265136644987871232 | 1254853678193733633（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0495 — wikidbs10k：見出し「enciclopèdia de l'esport català id」（Wikidata の型 `string`）（90 列）
- 例1：5850 | 13472 | 13052 | 13454 | 12285（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）
- 例2：5850 | 13454 | 7314 | 15 | 4962（表：field of work／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）
- 例3：4962 | 7683 | 7314 | 1169 | 10667（表：type of sport／同じ表の列：label, description, Commons category, subclass of, topic's main catego…, Freebase ID）

## g0496 — wikidbs10k：見出し「isomeric smiles」（Wikidata の型 `string`）（90 列）
- 例1：COC1=C(Br)[C@@H](O)[C@]2(C=C1Br)CC(C(=O… | COC1=C(Br)[C@H](O)[C@@]2(C=C1Br)CC(C(=O… | COC1=C(Br)[C@H](O)[C@@]2(C=C1Br)CC(C(=O… | COC1=C(Br)[C@H](O)[C@@]2(C=C1Br)CC(C(=O… | COC1=C(Br)[C@@H](O)[C@]2(C=C1Br)CC(C(=O…（表：spirobenzoxazoline alkaloid／同じ表の列：label, description, mass, PubChem CID, InChI, instance of）
- 例2：CC/C=C1/C[C@@H]2C=Nc3ccc(O[C@@H]4O[C@@H… | C=CC(C)(C)C1(CC2N=C(O)c3ccccc3N(C)C2=O)… | CC(=O)C1=CN2[C@@H](C1)CNC3=C(C2=O)C=CC=… | O=C1c2cc(O)cc(O)c2N[C@@H](c2c[nH]c3cccc… | CC(C)=CCc1c(O)ccc2c(C[C@@H]3NC(=O)C4=C(…（表：benzodiazepine alkaloid／同じ表の列：label, description, instance of, chemical formula, InChIKey, PubChem CID）
- 例3：CC(C)[C@@]1(O)CC[C@]2(C)C[C@H]3[C@@H]([… | C=C1CC[C@@H]2[C@@H]1C[C@@]1(C)CC[C@@H](… | COC[C@@]1(O)CC[C@@H]2/C1=C\[C@]1(C)C(=C… | COC[C@@]1(O)CC[C@@H]2C1=C[C@]1(C)C(=C(C… | C[C@@H]1[C@@H]\2CC[C@@H](/C2=C/[C@]3(CC…（表：fusicoccane diterpenoid／同じ表の列：label, description, PubChem CID, InChIKey, canonical SMILES, chemical formula）

## g0497 — sotab_v2：元の種類 `JobPosting/description`（89 列）
- 例1：<h2>Job Title:</h2>Sr. Tools Engineer, … | <h2>Job Title:</h2>Associate QA Project… | <h2>Job Title:</h2>Principal Core Engin… | <h2>Job Title:</h2>Senior Analyst, Inte… | <h2>Job Title:</h2>Front-End Developer<…
- 例2：<p>We are looking for an enthusiastic a… | <p><em>“Admiral Group is looking for a … | <p><u><strong>S</strong>trategic <stron… | <p><strong><u>Job Purpose</u></strong><… | <p><strong><u>Data Engineer</u></strong…
- 例3：<div> <div> <div> <p> <strong>About Us<… | <p>Resource Development is instrumental… | <p>Since its founding in 1919, the Inte… | <strong>Grants Manager – Family and Com… | <p> <strong>Job Summary:</strong> </p> …

## g0498 — wikidbs10k：見出し「length」（Wikidata の型 `quantity`）（86 列）
- 例1：+42 | +16.6 | +90 | +10 | +17（表：landform／同じ表の列：label, description, Dewey Decimal Class…, Commons category, instance of, coordinate location）
- 例2：+451 | +291.50 | +325 | +1232.7 | +56（表：body of water／同じ表の列：label, description, mouth of the waterc…, instance of, Commons category, country）
- 例3：+6 | +7.3 | +17 | +7.2 | +7（表：Copenhagen Super Bikeways／同じ表の列：label, description, instance of, part of, country, official website）

## g0499 — wikidbs10k：見出し「contains settlement」（Wikidata の型 `wikibase-entityid`）（86 列）
- 例1：Demmerik | Vught | Toom | Hermalen | Themaat（表：administrative territorial entity／同じ表の列：label, description, instance of, located in the admi…, country, coordinate location）
- 例2：Zaltbommel | Rukven | Horzik | Eersel | Mildert（表：political border／同じ表の列：label, description, CBS municipality co…, Commons category, flag image, coat of arms image）
- 例3：Drachtstercompagnie | Tsienzerbuorren | De Lytse Geast | Hijkersmilde | Anjum（表：administrative territorial entity／同じ表の列：label, description, Commons category, CBS municipality co…, flag image, coat of arms image）

## g0500 — wikidbs10k：見出し「home venue」（Wikidata の型 `wikibase-entityid`）（85 列）
- 例1：Prudential Center | Mitchell Center | Ford Center | WVU Coliseum | Memorial Gymnasium（表：participating team／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例2：Thomas & Mack Center | Carver–Hawkeye Arena | Williams Arena | John E. Worthen Arena | Cameron Indoor Stadium（表：winner／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例3：John Paul Jones Arena | Humphrey Coliseum | Bud Walton Arena | Carnesecca Arena | Convocation Center（表：participating team／同じ表の列：label, description, topic's main catego…, Freebase ID, instance of, parent club）

## g0501 — wikidbs10k：見出し「significant event」（Wikidata の型 `wikibase-entityid`）（85 列）
- 例1：assignment（表：coat of arms／同じ表の列：label, description, country, instance of, image, applies to jurisdic…）
- 例2：assignment（表：coat of arms／同じ表の列：label, description, country, instance of, applies to jurisdic…, image）
- 例3：capitulation | order | sinking | scuttling（表：31st U-boat Flotilla／同じ表の列：label, description, operator, instance of, conflict, vessel class）

## g0502 — wikidbs10k：見出し「present in work」（Wikidata の型 `wikibase-entityid`）（83 列）
- 例1：Sword of Yurikawa | The Addams Family | Once Upon a Time Machine | Pride and Prejudice | Enola Holmes（表：fictional mansion／同じ表の列：label, description, instance of, from narrative univ…, country）
- 例2：Pokémon（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, Pokémon index, part of, height）
- 例3：Dungeons & Dragons（表：humanoid／同じ表の列：label, description, subclass of, Fandom article ID, first appearance, from narrative univ…）

## g0503 — wikidbs10k：見出し「amsterdam code」（Wikidata の型 `string`）（82 列）
- 例1：10851 | 10142 | 11322 | 10005 | 11144（表：former grietenij／同じ表の列：label, description, instance of, country, Commons category, CBS municipality co…）
- 例2：10128 | 11284 | 10334 | 10836 | 11427（表：jurisdiction／同じ表の列：label, description, instance of, country, Commons category, CBS municipality co…）
- 例3：11081.0 | 10685.0 | 11298.0 | 11243.0 | 10182.0（表：administrative territorial entity／同じ表の列：label, description, instance of, located in the admi…, country, coordinate location）

## g0504 — wikidbs10k：見出し「cbs municipality code」（Wikidata の型 `string`）（82 列）
- 例1：0101 | 0087 | 0081 | 0062 | 0067（表：former grietenij／同じ表の列：label, description, instance of, country, Commons category, flag image）
- 例2：0085 | 0084 | 1908 | 0076 | 0082（表：jurisdiction／同じ表の列：label, description, instance of, country, Commons category, flag image）
- 例3：971.0 | 1641.0 | 437.0 | 1711.0 | 1961.0（表：administrative territorial entity／同じ表の列：label, description, instance of, located in the admi…, country, coordinate location）

## g0505 — wikidbs10k：見出し「istat id」（Wikidata の型 `string`）（82 列）
- 例1：31006 | 93044 | 30027 | 031008 | 30058（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）
- 例2：93021.0 | 32003.0 | 30011.0 | 93012.0 | 31003.0（表：political border／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）
- 例3：031003 | 030031 | 030016 | 093002 | 093021（表：administrative centre／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）

## g0506 — wikidbs10k：見出し「tv tropes identifier」（Wikidata の型 `string`）（82 列）
- 例1：VideoGame/TheLegendOfZeldaOcarinaOfTime | VideoGame/TheLegendOfZeldaTheWindWaker | VideoGame/TheLegendOfZeldaALinkToThePast | VideoGame/TheLegendOfZeldaTwilightPrinc… | VideoGame/TheLegendOfZeldaSkywardSword（表：work／同じ表の列：label, description, part of the series, genre, platform, game mode）
- 例2：UsefulNotes/Luxembourg | UsefulNotes/Germany | UsefulNotes/Belgium | UsefulNotes/Norway | UsefulNotes/Finland（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：UsefulNotes/Belgium | UsefulNotes/Austria | UsefulNotes/Germany | UsefulNotes/Switzerland | UsefulNotes/Finland（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0507 — wikidbs10k：見出し「bavarikon id」（Wikidata の型 `string`）（80 列）
- 例1：ODB_A00000248 | ODB_A00000232 | ODB_A00000396 | ODB_A00000404 | ODB_A00000251（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, located in the admi…, coat of arms image）
- 例2：ODB_A00002025 | ODB_A00002021 | ODB_A00002029 | ODB_A00002018 | ODB_A00002020（表：Stimmkreis Coburg／同じ表の列：label, description, country, Commons category, GND ID, German municipality…）
- 例3：ODB_A00002026 | ODB_A00002022 | ODB_A00002014 | ODB_A00002019 | ODB_A00002028（表：workplace／同じ表の列：label, description, country, Commons category, German municipality…, coordinate location）

## g0508 — wikidbs10k：見出し「has tense」（Wikidata の型 `wikibase-entityid`）（80 列）
- 例1：present tense | present infinitive | simple present（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：past tense | present infinitive | simple present | present tense（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：present tense | past anterior | present infinitive | simple present（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0509 — wikidbs10k：見出し「official symbol」（Wikidata の型 `wikibase-entityid`）（80 列）
- 例1：bald eagle | Northern Cardinal | Northern Mockingbird | Eastern Bluebird | American Goldfinch（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：Eschscholzia californica | American Goldfinch | bald eagle | Northern Cardinal | North American beaver（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：Eschscholzia californica | Northern Cardinal | Brown Pelican | Northern Flicker | Beautiful Nebraska（表：jurisdiction／同じ表の列：label, description, named after, Dewey Decimal Class…, topic's main Wikime…, country）

## g0510 — wikidbs10k：見出し「catholic encyclopedia id」（Wikidata の型 `string`）（79 列）
- 例1：13100c | 15464b | 10275b | 15123a | 02006b（表：patron saint／同じ表の列：label, description, Library of Congress…, Commons category, VIAF ID, ISNI）
- 例2：02745c | 03227a | 12291b | 05278a | 04558c（表：country／同じ表の列：label, description, VIAF ID, continent, Wikimedia outline, BBC Things ID）
- 例3：01724a | 15354b | 01240a | 15238a | 10785a（表：jurisdiction／同じ表の列：label, description, named after, Dewey Decimal Class…, topic's main Wikime…, country）

## g0511 — wikidbs10k：見出し「located in/on physical feature」（Wikidata の型 `wikibase-entityid`）（79 列）
- 例1：Terceira Island | Graciosa Island | São Miguel Island | Pico Island | Flores Island（表：habitats or species management protecte…／同じ表の列：label, description, country, instance of, area, IUCN protected area…）
- 例2：Ridge-and-Valley Appalachians（表：Ridge-and-Valley Appalachians／同じ表の列：label, description, instance of, coordinate location, country, elevation above sea…）
- 例3：New Guinea | British Isles | Central Europe | Fertile Crescent | Central Africa（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0512 — sotab_v2：元の種類 `CreativeWork`（78 列）
- 例1：xvwmDjiR2Eo | d_QsJYUhkr0 | 79vQp5BfRxE | ofsqnq0uglA | _prnSSvDt_Y
- 例2：Akdh3SI7lAc | 305PeZkXQVE | -GzC4v5VqR4 | si0ywzK-0Vk | y-dJKZ8U7NE
- 例3：B_SOh9UJVGw | Oz0JyNuUxA0 | zjZn6V2pUoo | y2KIxr5KWlA | _h98ES7leCI

## g0513 — wikidbs10k：見出し「doi」（Wikidata の型 `string`）（78 列）
- 例1：10.1016/S0022-5347(01)63299-3 | 10.1038/35065611 | 10.1042/BJ20041354 | 10.1016/J.DEVCEL.2011.12.008 | 10.1042/BJ2600421（表：citation／同じ表の列：label, description, page(s), title, author name string, publication date）
- 例2：10.1038/NATURE01180 | 10.1038/NI.1606 | 10.1073/PNAS.082100399 | 10.1074/JBC.M309251200 | 10.1074/JBC.M109.022392（表：citation／同じ表の列：label, description, title, PubMed ID, page(s), issue）
- 例3：10.1038/550451A | 10.1101/2020.10.26.20219089 | 10.1016/J.IMMUNI.2020.11.017 | 10.1038/S41587-020-0465-8 | 10.7554/ELIFE.27041（表：Human Cell Atlas Publications／同じ表の列：label, description, publication date, instance of, author name string, author）

## g0514 — wikidbs10k：見出し「ec enzyme number」（Wikidata の型 `string`）（76 列）
- 例1：4.2.3.40 | 4.2.3.82 | 4.2.3.73 | 4.2.3.31 | 4.2.3.139（表：carbon-oxygen lyase, acting on phosphat…／同じ表の列：label, description, instance of, subclass of, molecular function, Freebase ID）
- 例2：4.2.3.35 | 4.2.3.73 | 4.2.3.32 | 4.2.3.139 | 4.2.3.31（表：molecular function／同じ表の列：label, description, subclass of, Gene Ontology ID, exact match, instance of）
- 例3：3.1.3.43 | 3.1.3.71 | 3.1.3.45 | 3.1.3.59 | 3.1.3.44（表：molecular function／同じ表の列：label, description, Gene Ontology ID, subclass of, exact match, instance of）

## g0515 — wikidbs10k：見出し「parity quantum number」（Wikidata の型 `quantity`）（75 列）
- 例1：-1 | +1（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例2：+1 | -1（表：neon／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例3：+1（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）

## g0516 — wikidbs10k：見出し「spin quantum number」（Wikidata の型 `quantity`）（75 列）
- 例1：+2.0 | +1.5 | +2.5 | +1.0 | +4.0（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例2：+1.5 | +0.5 | +0.0 | +2.5（表：neon／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例3：+2.5 | +1.0 | +0.0 | +4.0 | +0.5（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）

## g0517 — wikidbs10k：見出し「time index」（Wikidata の型 `quantity`）（75 列）
- 例1：+1 | +11 | +5 | +3 | +2（表：Malayalam calendar／同じ表の列：label, description, follows, followed by, subclass of, instance of）
- 例2：+3 | +2 | +5 | +1 | +9（表：followed by／同じ表の列：label, description, follows, followed by, subclass of, instance of）
- 例3：+7 | +6 | +3 | +8 | +4（表：follows／同じ表の列：label, description, follows, followed by, subclass of, instance of）

## g0518 — wikidbs10k：見出し「attested in」（Wikidata の型 `wikibase-entityid`）（75 列）
- 例1：frequency of first names in the Netherl…（表：given name／同じ表の列：label, description, instance of, Commons category, family name identic…, different from）
- 例2：Biographisches Lexikon des Kaiserthums … | frequency of first names in the Netherl…（表：given name／同じ表の列：label, description, said to be the same…, instance of, language of work or…, Commons category）
- 例3：frequency of first names in the Netherl…（表：given name／同じ表の列：label, description, instance of, family name identic…, native label, writing system）

## g0519 — wikidbs10k：見出し「office held by head of the organization」（Wikidata の型 `wikibase-entityid`）（75 列）
- 例1：Cypriot Minister of Foreign Affairs | Cyprus Minister of Transport, Communica… | Cyprus Minister of Justice and Public O… | Cyprus Minister of Communications and W… | Deputy Minister of Culture（表：Government of Cyprus Republic／同じ表の列：label, description, topic's main catego…, instance of, country, topic's main templa…）
- 例2：Deputy Minister of Research, Innovation… | Cyprus Minister of Communications and W… | Cyprus Minister of Justice and Public O… | Minister of Defence | Minister of Labour and Social Insurance…（表：organization／同じ表の列：label, description, topic's main catego…, instance of, country, topic's main templa…）
- 例3：Minister of Justice | Minister of Social Policy and Equality | Minister for the Economy and Digital Tr… | Minister of Science and Innovation (Spa… | Minister for Agriculture, Fisheries and…（表：organization／同じ表の列：label, description, country, applies to jurisdic…, inception, instance of）

## g0520 — wikidbs10k：見出し「employees」（Wikidata の型 `quantity`）（74 列）
- 例1：+12325 | +975 | +2925 | +3575 | +8225（表：administrative territorial entity／同じ表の列：label, description, shares border with, coat of arms image, Commons category, country）
- 例2：2025.0 | 38175.0 | 2575.0 | 875.0 | +8225（表：political border／同じ表の列：label, description, Commons category, coat of arms image, country, located in the admi…）
- 例3：+882 | +646 | +24605 | +1161 | +5502（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）

## g0521 — wikidbs10k：見出し「state of use」（Wikidata の型 `wikibase-entityid`）（74 列）
- 例1：in use（表：Crossrail／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例2：in use（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例3：in use | out of service（表：Rapid KL／同じ表の列：label, description, instance of, Commons category, Freebase ID, country）

## g0522 — wikidbs10k：見出し「fandom wiki id」（Wikidata の型 `string`）（73 列）
- 例1：poland | sweden | canada | denmark | germany（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：us | australia | japan | united-kingdom | sweden（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：germany | australia | canada | mexico | us（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0523 — wikidbs10k：見出し「organization directed by the office or position」（Wikidata の型 `wikibase-entityid`）（73 列）
- 例1：Ministry of Education, Culture, Sports … | Deputy Ministry Of Tourism (Cyprus) | Deputy Ministry of Culture (Cyprus) | Ministry of Agriculture, Rural Developm… | Ministry of Labour and Social Insurance…（表：organization leader／同じ表の列：label, description, subclass of, applies to jurisdic…, instance of, topic's main catego…）
- 例2：Ministry of Science, Innovation and Uni… | Ministry of Development | Ministry of Health and Social Policy | Ministry of Labour and Social Affairs | Ministry of the Interior of Spain（表：Council of Ministers of Spain／同じ表の列：label, description, instance of, subclass of, country, applies to jurisdic…）
- 例3：Ministry of Economy and Finance | Ministry of Information and Tourism | Ministry of Economy | Spain. Ministerio de Industria y Energía | Ministry of Culture（表：organization leader／同じ表の列：label, description, instance of, subclass of, country, applies to jurisdic…）

## g0524 — wikidbs10k：見出し「compulsory education (maximum age)」（Wikidata の型 `quantity`）（72 列）
- 例1：+17 | +18 | +16（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：17.0 | 18.0 | 16.0（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：+17 | +16 | +18（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0525 — wikidbs10k：見出し「sports season of league or competition」（Wikidata の型 `wikibase-entityid`）（72 列）
- 例1：WTA Tour（表：part／同じ表の列：label, description, topic's main catego…, Freebase ID, point in time, sport）
- 例2：WTA Tour（表：part／同じ表の列：label, description, topic's main catego…, Freebase ID, point in time, sport）
- 例3：Island Games（表：part／同じ表の列：label, description, Freebase ID, instance of, point in time, has part(s)）

## g0526 — wikidbs10k：見出し「canonical smiles」（Wikidata の型 `string`）（71 列）
- 例1：O=C1C(OC=2C=C(O)C=C(O)C12)=CC3=CC(O)=C(… | O=C(C=CC1=CC=C2OC(C3=CC=C(O)C=C3)C(C2=C… | O=C(C=CC1=CC=C(O)C(=C1OC)CC=C(C)C)C2=CC… | O=C(C=CC1=CC(=C(O)C=C1OC)C(C(=C)C)C)C2=… | O=C(C=CC1=CC(O)=C(O)C(=C1)CC=C(C)C)C2=C…（表：3C-substituted chalcone／同じ表の列：label, description, instance of, PubChem CID, chemical formula, InChI）
- 例2：O=C(NCCCOC1=C(Br)C=C(C=C1Br)CCN)C2=NOC3… | O=C(NCCC1=CC(Br)=C(OCCCN=C(O)CCCCCCCCCC… | O=C(NCC(=O)C(O)CNC(=O)C1=NCC2(C=C(Br)C(… | O=C(NCC(O)C1=CC(Br)=C(OCC(O)CNC(=O)C2=N… | O=C(NCCCOC1=C(Br)C=C(C=C1Br)CCN(C)C)C2=…（表：spirobenzoxazoline alkaloid／同じ表の列：label, description, mass, PubChem CID, InChI, instance of）
- 例3：O=C(OCC=C(C)CCC=C(C)CCC1C(=C)CCCC1(C)C)C | O=C(OC=CC(=COC(=O)C)CCC=C(C)CCC1C(=CCCC… | ClCC(O)C1(OC(C)(CCC2C(O)(C)CCC(Br)C2(C)… | O=C(O)C(N=C(O)C=C(C=CC=C(C=CC1=C(C)CCCC… | O1C=CC(=C1)CCC=C(C)CCC2C(=C)CCCC2(C)C（表：10,15-cyclophytane diterpenoid／同じ表の列：label, description, instance of, PubChem CID, chemical formula, InChI）

## g0527 — wikidbs10k：見出し「hembygdsportalen id」（Wikidata の型 `string`）（71 列）
- 例1：47 | 204 | 298 | 27 | 12（表：administrative territorial entity／同じ表の列：label, description, shares border with, coat of arms image, Commons category, country）
- 例2：39.0 | 223.0 | 143 | 204 | 15.0（表：political border／同じ表の列：label, description, Commons category, coat of arms image, country, located in the admi…）
- 例3：8 | 4 | 121 | 277 | 308（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coat of arms image, locator map image, capital）

## g0528 — wikidbs10k：見出し「encyclopedia of china (third edition) id」（Wikidata の型 `string`）（70 列）
- 例1：27863 | 27865 | 27936 | 27871 | 27903（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：27862 | 27872 | 27904 | 27903 | 27953（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：27860 | 27863 | 27849 | 27871 | 27858（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0529 — wikidbs10k：見出し「archives at」（Wikidata の型 `wikibase-entityid`）（70 列）
- 例1：State Library and Archives of Florida | Maryland State Archives | Pennsylvania State Archives | Tennessee State Library and Archives | NJ State Archives（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例2：Minnesota Historical Society | Louisiana State Archive and Research Li… | Pennsylvania State Archives | Hawaii State Archives | Oklahoma Department of Libraries（表：jurisdiction／同じ表の列：label, description, named after, Dewey Decimal Class…, topic's main Wikime…, country）
- 例3：Illinois State Archives | West Virginia State Archives | New Mexico State Records Center and Arc… | Alaska State Archives | Ohio History Center（表：facet of／同じ表の列：label, description, named after, Dewey Decimal Class…, topic's main Wikime…, country）

## g0530 — wikidbs10k：見出し「has grammatical gender」（Wikidata の型 `wikibase-entityid`）（70 列）
- 例1：common | masculine personal | feminine | masculine（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：masculine personal | masculine animate | common | feminine | masculine（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例3：common | masculine inanimate | masculine | masculine personal | masculine animate（表：language／同じ表の列：label, description, OmegaWiki Defined M…, ISO 639-1 code, ISO 639-2 code, ISO 639-3 code）

## g0531 — wikidbs10k：見出し「twitch tag id」（Wikidata の型 `string`）（69 列）
- 例1：a6cddaba-f0ce-4526-9087-6de2f603a24d | 73cc486a-e56b-41ed-a1df-7afedbc84f6f | ab2975e3-b9ca-4b1a-a93e-fb61a5d5c3a4 | 39ee8140-901a-4762-bfca-8260dea1310f | 220eb274-ab25-425b-8a9b-826103404997（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：6ea6bca4-4712-4ab9-a906-e3336a9d8039 | 6ba1d230-e52f-4d81-b1e0-41f25a8a9f5d | e13e6734-37ae-4d85-897b-3015f0168355 | a6cddaba-f0ce-4526-9087-6de2f603a24d | f08d5873-f0c7-4912-94ba-a41933b4c141（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：9166ad14-41f1-4b04-a3b8-c8eb838c6be6 | 5647bf35-f99e-49aa-8578-0e07d936188c | a298cca5-d408-47c7-a1e7-0c76ca878bc6 | 6ea6bca4-4712-4ab9-a906-e3336a9d8039 | 0569b171-2a2b-476e-a596-5bdfb45a1327（表：language proficiency／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）

## g0532 — wikidbs10k：見出し「youtube channel id」（Wikidata の型 `string`）（69 列）
- 例1：UCo6XrNe5b6fEPay_mZMiT2g | UCw9Whg8c4El7k3J1cTYMGYg | UCsZoq1ySOu_REXre5U5qaEg | UCZFMrceU4E5E3QMNc8gE2SQ | UClpXEIOJOpDpgOWpbS-JRjg（表：work／同じ表の列：label, description, part of the series, genre, platform, game mode）
- 例2：UClAg17-gB1BTp0o4vn3GDCg | UCXnl0Wcf-K_ZhHMAUr-rueQ | UCvhBTaybdAo3dZae0hYRLhw | UCGJTYCn6bFGIOI-KIR_lEIA | UCH9NAc2DA8VcxAZteknItng（表：administrative territorial entity／同じ表の列：label, description, shares border with, coat of arms image, Commons category, country）
- 例3：UCzngZogxlG-CgJa2e3aws7A | UCT7SJ8bDVu6J6TKwdughS5g | UClAg17-gB1BTp0o4vn3GDCg | UCzITCmk7C059GtKrspk2YCQ | UCAfRLqWMnIT3perGsS2yyKw（表：political border／同じ表の列：label, description, Commons category, coat of arms image, country, located in the admi…）

## g0533 — wikidbs10k：見出し「media franchise」（Wikidata の型 `wikibase-entityid`）（69 列）
- 例1：Pokémon（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, Pokémon index, part of, height）
- 例2：Pokémon（表：Grass egg group／同じ表の列：label, description, part of, from narrative univ…, instance of, Pokémon index）
- 例3：Star Trek（表：Starfleet ship／同じ表の列：label, description, from narrative univ…, instance of, pennant number, present in work）

## g0534 — wikidbs10k：見出し「urban population」（Wikidata の型 `quantity`）（68 列）
- 例1：+131613 | +1338033 | +1817211 | +1264614 | +565393（表：administrative territorial entity／同じ表の列：label, description, country, locator map image, Commons category, topic's main catego…）
- 例2：31580 | 131613 | +2618940 | 509047 | 1817211（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）
- 例3：+2234363 | +2096406 | +2072572 | +509047 | +1539802（表：political border／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）

## g0535 — wikidbs10k：見出し「banque de noms de lieux du québec id」（Wikidata の型 `string`）（68 列）
- 例1：382684 | 382385 | 382410 | 382294 | 382356（表：floral habitat of Quebec／同じ表の列：label, description, instance of, country, located in the admi…, coordinate location）
- 例2：375779 | 57740 | 56984 | 434167 | 361730（表：administrative territorial entity／同じ表の列：label, description, country, coordinate location, located in the admi…, instance of）
- 例3：416631 | 371364 | 57678 | 51718 | 388449（表：political border／同じ表の列：label, description, country, located in the admi…, coordinate location, instance of）

## g0536 — wikidbs10k：見出し「idescat territorial code in catalonia」（Wikidata の型 `string`）（68 列）
- 例1：250100 | 252115 | 250387 | 250215 | 250138（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：252304 | 251333 | 250100 | 250117 | 250143（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：081419 | 82299 | 081516 | 081326 | 82135（表：jurisdiction／同じ表の列：label, description, Commons category, country, postal code, image）

## g0537 — wikidbs10k：見出し「location map」（Wikidata の型 `string`）（68 列）
- 例1：Tasmania in Australia.svg | Queensland in Australia.svg | Australia Victoria location map.svg | South Australia in Australia.svg | Australia Western Australia location ma…（表：jurisdiction／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）
- 例2：South Korea adm location map.svg | Geographic Map of China.png | Uk-map.svg | India-states-numbered.svg | Regionen japans.png（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, Libraries Australia…, coordinates of sout…）
- 例3：USA Utah location map.svg | South Australia in Australia.svg | Australia Victoria location map.svg | USA Colorado location map.svg | Australia Western Australia location ma…（表：administrative territorial entity／同じ表の列：label, description, country, capital, shares border with, flag image）

## g0538 — wikidbs10k：見出し「parent organization」（Wikidata の型 `wikibase-entityid`）（68 列）
- 例1：Northern Railway zone | North Central Railway zone | East Central Railway zone | Northeast Frontier Railway zone | Central Railway zone（表：Indian Railways division／同じ表の列：label, description, country, topic's main catego…, instance of, reporting mark）
- 例2：North Western Railway zone | Konkan Railway Corporation | Eastern Railway zone | South Coast Railway zone | South East Central Railway zone（表：subsidiary／同じ表の列：label, description, topic's main catego…, country, instance of, Google Knowledge Gr…）
- 例3：University of Washington College of Eng…（表：University of Washington College of Eng…／同じ表の列：label, description, instance of, located in the admi…, country, part of）

## g0539 — wikidbs10k：見出し「invasive species compendium datasheet id」（Wikidata の型 `string`）（67 列）
- 例1：108362 | 108556 | 108528 | 108542 | 108429（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, category for films …, GND ID）
- 例2：108620 | 108625 | 108621 | 108619 | 108519（表：jurisdiction／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）
- 例3：108464.0 | 108431.0 | 108528.0 | 108542.0 | 108522.0（表：country／同じ表の列：label, description, Dewey Decimal Class…, topic's main Wikime…, continent, capital）

## g0540 — wikidbs10k：見出し「sbn place id」（Wikidata の型 `string`）（67 列）
- 例1：TO0L003009 | RMLL000779 | VEAL001107 | UBOL002792 | MUSL000100（表：headquarters／同じ表の列：label, description, twinned administrat…, page banner, country, Commons category）
- 例2：MUSL000371 | MUSL002585 | UBOL003790 | TSAL000009 | UBOL001389（表：headquarters／同じ表の列：label, description, instance of, locator map image, Commons category, coordinate location）
- 例3：MUSL003684 | BVEL000279 | TO0L000791 | MUSL000736 | MUSL001954（表：administrative territorial entity／同じ表の列：label, description, twinned administrat…, country, Commons category, located in the admi…）

## g0541 — wikidbs10k：見出し「c-span organization id」（Wikidata の型 `string`）（66 列）
- 例1：3525 | 21599 | 13054 | 20929 | 15091（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：13675.0 | 20929.0 | 17192.0 | 1240.0 | 6507.0（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：1240 | 13675 | 10850 | 17192 | 3525（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0542 — wikidbs10k：見出し「google news topics id」（Wikidata の型 `string`）（66 列）
- 例1：CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFZyYTJnU0F… | CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFYwWW00U0F… | CAAqIQgKIhtDQkFTRGdvSUwyMHZNR1E1ZVRZU0F… | CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFI1WTJnU0F… | CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE4yTUhRU0F…（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFYwWW00U0F… | CAAqIQgKIhtDQkFTRGdvSUwyMHZNRGRpWDJ3U0F… | CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0V… | CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFZyY2w4U0J… | CAAqIggKIhxDQkFTRHdvSkwyMHZNRFU1Y21KNUV…（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：CAAqIQgKIhtDQkFTRGdvSUwyMHZNRGRvTXpRU0F… | CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFZyY2w4U0J… | CAAqIQgKIhtDQkFTRGdvSUwyMHZNREo0Y25rU0F… | CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0V… | CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFJ5Y21RU0F…（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0543 — wikidbs10k：見出し「unii」（Wikidata の型 `string`）（66 列）
- 例1：5C7J33MJJ1 | 34YYS7G16P | 7YC151N82L | IT7Z319PFY | O478WX4004（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：RCU76P419D | V1V998DC17 | 138LUT2DWV | L56Z1JK48B | 492225Q21H（表：product／同じ表の列：label, description, subclass of, natural product of …, image）
- 例3：LA61LWB4JH | WC73QE9274 | M30698W1LU | C1107616TR | 8XW1DS8UIR（表：secretion or excretion／同じ表の列：label, description, Commons category, image, taxon name, taxon rank）

## g0544 — wikidbs10k：見出し「category for members of a team」（Wikidata の型 `wikibase-entityid`）（66 列）
- 例1：Category:Arizona Wildcats men's basketb… | Category:UTEP Miners men's basketball p… | Category:Iowa Hawkeyes men's basketball… | Category:Florida State Seminoles men's … | Category:Stanford Cardinal men's basket…（表：participating team／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例2：Category:Georgetown Hoyas men's basketb… | Category:UTEP Miners men's basketball p… | Category:Texas Longhorns men's basketba… | Category:Evansville Purple Aces men's b… | Category:South Alabama Jaguars men's ba…（表：winner／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例3：Category:Mississippi State Bulldogs men… | Category:Nebraska Cornhuskers men's bas… | Category:LSU Tigers basketball players | Category:Utah Utes men's basketball pla… | Category:Alabama Crimson Tide men's bas…（表：participating team／同じ表の列：label, description, topic's main catego…, Freebase ID, instance of, parent club）

## g0545 — wikidbs10k：見出し「illiterate population」（Wikidata の型 `quantity`）（65 列）
- 例1：+1196494 | +1167136 | +2257685 | +516019 | +395102（表：administrative territorial entity／同じ表の列：label, description, country, locator map image, Commons category, topic's main catego…）
- 例2：269883 | +803776 | +321636 | +822138 | 470850（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）
- 例3：+803776 | +822138 | +426712 | +185964 | +442652（表：political border／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）

## g0546 — wikidbs10k：見出し「number of spoilt votes」（Wikidata の型 `quantity`）（65 列）
- 例1：+16 | +2 | +15 | +4 | +11（表：2016 Bolton Metropolitan Borough Counci…／同じ表の列：label, description, instance of, part of, country, point in time）
- 例2：22 | 13 | 26 | 25 | 23（表：followed by／同じ表の列：label, description, instance of, part of, country, follows）
- 例3：+12 | +6 | +8 | +2 | +7（表：follows／同じ表の列：label, description, instance of, part of, country, point in time）

## g0547 — wikidbs10k：見出し「lau」（Wikidata の型 `string`）（64 列）
- 例1：CZ595098 | CZ594636 | CZ584797 | CZ593711 | CZ587656（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, country, coat of arms image, Commons category）
- 例2：CZ540803 | CZ0714 | CZ571822 | CZ020B | CZ545554（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, country, instance of）
- 例3：CZ582794 | CZ0424 | CZ563552 | CZ561045 | CZ0523（表：political border／同じ表の列：label, description, located in the admi…, Commons category, instance of, Freebase ID）

## g0548 — wikidbs10k：見出し「wiki loves monuments id」（Wikidata の型 `string`）（64 列）
- 例1：06D3830011 | 06I5620001 | 06D6450001 | 06F3780002 | 06D3830013（表：castelliere／同じ表の列：label, description, instance of, country, located in the admi…, heritage designation）
- 例2：06E1240000 | 06C3270000 | 06I9040000 | 06B9400000 | 06D3240000（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）
- 例3：06I7150000 | 06D4610000 | 06B5360000 | 06D3000000 | 06D3830000（表：political border／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）

## g0549 — wikidbs10k：見出し「world flora online id」（Wikidata の型 `string`）（64 列）
- 例1：wfo-4000003661 | wfo-4000026900 | wfo-4000022199 | wfo-4000022154 | wfo-4000034901（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例2：wfo-4000002087 | wfo-4000033989 | wfo-4000034856 | wfo-4000029178 | wfo-4000032690（表：taxon／同じ表の列：label, description, Commons category, taxon rank, taxon name, image）
- 例3：wfo-4000023686 | wfo-4000034467 | wfo-4000037395 | wfo-4000021568 | wfo-4000030231（表：taxon／同じ表の列：label, description, taxon name, taxon rank, parent taxon, instance of）

## g0550 — wikidbs10k：見出し「located in the present-day administrative territorial entity」（Wikidata の型 `wikibase-entityid`）（64 列）
- 例1：Kuroishi | Tsugaru | Odate | Goshogawara | Sapporo（表：replaced entity／同じ表の列：label, description, instance of, country, located in the admi…, dissolved, abolishe…）
- 例2：Asahikawa | Kakogawa | Kimitsu | Sukagawa | Hida（表：replaced entity／同じ表の列：label, description, instance of, country, replaced by, dissolved, abolishe…）
- 例3：Otaru | Tsushima | Maizuru | Ishikari | Hakodate（表：replaced entity／同じ表の列：label, description, instance of, country, replaced by, dissolved, abolishe…）

## g0551 — wikidbs10k：見出し「rural population」（Wikidata の型 `quantity`）（63 列）
- 例1：+871607 | +1409158 | +1024794 | +2545470 | +3678226（表：administrative territorial entity／同じ表の列：label, description, country, locator map image, Commons category, topic's main catego…）
- 例2：1529831 | 1065799 | 1056929 | 882017 | 1024794（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）
- 例3：+1056929 | +798328 | +882017 | +2133124 | +1048025（表：political border／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）

## g0552 — wikidbs10k：見出し「made from material」（Wikidata の型 `wikibase-entityid`）（63 列）
- 例1：oil paint（表：Windsor Beauties／同じ表の列：label, description, inventory number, collection, instance of, location）
- 例2：oil paint（表：depicting object／同じ表の列：label, description, inventory number, collection, instance of, location）
- 例3：stone | limestone | plaster | granite | marble（表：holy water font／同じ表の列：label, description, instance of, Palissy ID, country, Commons category）

## g0553 — wikidbs10k：見出し「number of houses」（Wikidata の型 `quantity`）（62 列）
- 例1：28107.0 | 40.0 | 70.0 | 2100.0 | 600.0（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, country, LAU）
- 例2：+651 | +730 | +32143 | +147 | +23739（表：political border／同じ表の列：label, description, located in the admi…, Commons category, LAU, instance of）
- 例3：+19215 | +810 | +551 | +361 | +735（表：administrative territorial entity／同じ表の列：label, description, image, postal code, country, coordinate location）

## g0554 — wikidbs10k：見出し「kvk company id」（Wikidata の型 `string`）（62 列）
- 例1：14130475.0 | 50653466.0 | 51643324.0 | 17272738.0 | 51984997.0（表：administrative territorial entity／同じ表の列：label, description, instance of, located in the admi…, country, coordinate location）
- 例2：17285344 | 50653466.0 | 14130475.0 | 30276781.0 | 14131668（表：political border／同じ表の列：label, description, CBS municipality co…, Commons category, flag image, coat of arms image）
- 例3：24483298.0 | 8215195.0 | 8218173.0 | 14131668.0 | 9220932.0（表：administrative territorial entity／同じ表の列：label, description, shares border with, CBS municipality co…, Commons category, postal code）

## g0555 — wikidbs10k：見出し「country for sport」（Wikidata の型 `wikibase-entityid`）（62 列）
- 例1：Canada（表：Canadian women's national road cycling …／同じ表の列：label, description, instance of, country, sport, start time）
- 例2：Canada（表：followed by／同じ表の列：label, description, instance of, country, sport, follows）
- 例3：Canada（表：follows／同じ表の列：label, description, instance of, UCI code of cycling…, sport, country）

## g0556 — wikidbs10k：見出し「literate population」（Wikidata の型 `quantity`）（61 列）
- 例1：+1832189 | +1389810 | +2615443 | +1272739 | +1548738（表：administrative territorial entity／同じ表の列：label, description, country, locator map image, Commons category, topic's main catego…）
- 例2：1062553 | 923010 | 2615443 | 1037492 | 2239492（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）
- 例3：+1037492 | +2239492 | +2678548 | +1548738 | +2273457（表：political border／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）

## g0557 — wikidbs10k：見出し「italian cadastre code (municipality)」（Wikidata の型 `string`）（61 列）
- 例1：B536 | C327 | C817 | D312 | D324（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）
- 例2：F795 | A354 | D300 | A700 | C885（表：political border／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）
- 例3：D461 | B536 | A855 | D312 | I715（表：administrative centre／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）

## g0558 — wikidbs10k：見出し「record label」（Wikidata の型 `wikibase-entityid`）（61 列）
- 例1：Duchesse | Spin | Polystar | RSO Records | Polydor Records（表：Bee Gees' albums in chronological order／同じ表の列：label, description, instance of, performer, form of creative wo…, title）
- 例2：EMI（表：publishing／同じ表の列：label, description, instance of, performer, tracklist, part of）
- 例3：Sony Music | Targa | CGD East West | Vanilla | Record Bazaar（表：Ornella Vanoni's albums in chronologica…／同じ表の列：label, description, MusicBrainz release…, instance of, performer, publication date）

## g0559 — wikidbs10k：見出し「finnish municipality number」（Wikidata の型 `string`）（60 列）
- 例1：853 | 398 | 272 | 205 | 638（表：administrative territorial entity／同じ表の列：label, description, page banner, coat of arms image, Dewey Decimal Class…, shares border with）
- 例2：445.0 | 564.0 | 78.0 | 263.0 | 74.0（表：political border／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）
- 例3：148 | 205 | 638 | 398 | 297（表：jurisdiction／同じ表の列：label, description, page banner, coat of arms image, Dewey Decimal Class…, shares border with）

## g0560 — wikidbs10k：見出し「indian census area code (2011)」（Wikidata の型 `string`）（60 列）
- 例1：341 | 598 | 609 | 610 | 197（表：administrative territorial entity／同じ表の列：label, description, country, locator map image, Commons category, topic's main catego…）
- 例2：591 | 592 | 596 | 632 | 601（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）
- 例3：595 | 632 | 589 | 629 | 591（表：political border／同じ表の列：label, description, country, located in the admi…, locator map image, Commons category）

## g0561 — wikidbs10k：見出し「indicepa id」（Wikidata の型 `string`）（60 列）
- 例1：c_d461 | c_i904 | c_i562 | c_f356 | c_b536（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）
- 例2：c_d383 | c_b536 | c_d621 | c_f795 | c_a700（表：political border／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）
- 例3：c_d085 | c_a354 | c_e124 | c_f795 | c_d461（表：administrative centre／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）

## g0562 — wikidbs10k：見出し「seismic classification」（Wikidata の型 `wikibase-entityid`）（60 列）
- 例1：3 | 2（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）
- 例2：1.0 | 3.0 | 2.0（表：political border／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）
- 例3：3 | 2（表：administrative centre／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）

## g0563 — wikidbs10k：見出し「transport network」（Wikidata の型 `wikibase-entityid`）（60 列）
- 例1：London Overground | London Underground | Docklands Light Railway（表：Crossrail／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例2：Docklands Light Railway | London Underground | London Overground（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例3：Stuttgart Stadtbahn | Munich U-Bahn | Munich S-Bahn | Washington Metro | Buenos Aires Underground（表：adjacent station／同じ表の列：label, description, adjacent station, country, instance of, coordinate location）

## g0564 — wikidbs10k：見出し「coordinates of geographic center」（Wikidata の型 `globecoordinate`）（59 列）
- 例1：31.4757 | 47.0527 | 39.055 | 37.1841 | 42.9538（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：31.4757 | 44.967243394444 | 28.6305 | 42.9538 | 40.0417（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：31.4757 | 40.1907 | 40.8781 | 42.9538 | 28.6305（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0565 — wikidbs10k：見出し「issn」（Wikidata の型 `string`）（59 列）
- 例1：8750-7587 | 1534-5807 | 0021-9258 | 1476-4687 | 0022-5347（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ERA Journal ID）
- 例2：0021-9258 | 1383-5718 | 0893-228X | 0006-291X | 0031-6970（表：publishing／同じ表の列：label, description, instance of, ERA Journal ID, Scopus source ID, Danish Bibliometric…）
- 例3：0732-8494 | 0025-3049 | 1756-3224 | 0026-9395 | 0745-1415（表：publishing／同じ表の列：label, description, inception, Freebase ID, instance of, official website）

## g0566 — wikidbs10k：見出し「inventory number」（Wikidata の型 `string`）（58 列）
- 例1：RCIN 401212 | RCIN 404961 | RCIN 404962 | RCIN 404514 | RCIN 404959（表：Windsor Beauties／同じ表の列：label, description, collection, instance of, location, made from material）
- 例2：355542 | RCIN 404514 | RCIN 404961 | 1171191 | RCIN 404515（表：depicting object／同じ表の列：label, description, collection, instance of, location, made from material）
- 例3：1975.1.1718 | 1985.029 | 1985.084 | 1979.1073P | 1985.060（表：crock／同じ表の列：label, description, location, collection, instance of）

## g0567 — wikidbs10k：見出し「open civic data division id」（Wikidata の型 `string`）（58 列）
- 例1：ocd-division/country:us/state:nj | ocd-division/country:us | ocd-division/country:us/state:pa | ocd-division/country:us/state:mt | ocd-division/country:us/state:md（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：ocd-division/country:us/state:tx | ocd-division/country:us/state:md | ocd-division/country:us/state:ny | ocd-division/country:us/state:tn | ocd-division/country:us/state:fl（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：ocd-division/country:us/state:pa | ocd-division/country:us/state:ny | ocd-division/country:us/state:md | ocd-division/country:us/state:nj | ocd-division/country:us/state:fl（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0568 — wikidbs10k：見出し「basque vikidia id」（Wikidata の型 `string`）（57 列）
- 例1：Suedia | Txekia | Zeelanda_Berria | Espainia | Bulgaria（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：Mexiko | Austria | Japonia | Alemania | Kanada（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Kanada | Italia | Mexiko | Austria | Suedia（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0569 — wikidbs10k：見出し「crossref journal id」（Wikidata の型 `string`）（57 列）
- 例1：12116 | 3481 | 3866 | 25077 | 22946（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：491 | 4173 | 2511 | 101765 | 964（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：101 | 297113 | 1698 | 81438 | 43798（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0570 — wikidbs10k：見出し「issn-l」（Wikidata の型 `string`）（57 列）
- 例1：0021-9258 | 1522-1601 | 0022-3565 | 0028-0836 | 1534-5807（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：0378-7966 | 0090-9556 | 0031-6970 | 0027-8424 | 1078-0297（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：1078-8956 | 1367-4803 | 1097-6256 | 1529-2908 | 0361-8609（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0571 — wikidbs10k：見出し「opencitations bibliographic resource id」（Wikidata の型 `string`）（57 列）
- 例1：546 | 1870 | 3842 | 5232 | 16（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：2230 | 5123 | 14468 | 36218 | 16646（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：7367 | 8723 | 16 | 11529 | 6698（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0572 — wikidbs10k：見出し「scopus source id」（Wikidata の型 `string`）（57 列）
- 例1：17592 | 23086 | 23454 | 21206 | 23183（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：130044 | 21326 | 16845 | 17783 | 17592（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Danish Bibliometric…）
- 例3：17945 | 19700175140 | 21315 | 25424 | 21206（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0573 — wikidbs10k：見出し「swedish municipality code」（Wikidata の型 `string`）（57 列）
- 例1：1284 | 0381 | 1283 | 1281 | 0139（表：administrative territorial entity／同じ表の列：label, description, shares border with, coat of arms image, Commons category, country）
- 例2：125.0 | 1290 | 1280.0 | 1480.0 | 331.0（表：political border／同じ表の列：label, description, Commons category, coat of arms image, country, located in the admi…）
- 例3：2260 | 1491 | 2161.0 | 0509 | 2580.0（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）

## g0574 — wikidbs10k：見出し「distribution format」（Wikidata の型 `wikibase-entityid`）（57 列）
- 例1：Nintendo 3DS | digital distribution | digital download | Nintendo game card | ROM cartridge（表：work／同じ表の列：label, description, part of the series, genre, platform, game mode）
- 例2：vinyl record | 45 RPM 7" vinyl（表：The Single File 1978~1983／同じ表の列：label, description, performer, instance of, MusicBrainz release…, publication date）
- 例3：music streaming（表：tracklist／同じ表の列：label, description, instance of, title, performer, published in）

## g0575 — wikidbs10k：見出し「foundational text」（Wikidata の型 `wikibase-entityid`）（57 列）
- 例1：Constitution of Illinois | Constitution of Montana | Kentucky Constitution | Constitution of Ohio | United States Declaration of Independen…（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：Constitution of Texas | Constitution of California | Constitution of New Jersey | Constitution of Tennessee | New York Constitution（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：Constitution of Maryland (1867) | Constitution Act, 1867 | Constitution of Texas | Pennsylvania Constitution of 1776 | Constitution of New Jersey（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0576 — wikidbs10k：見出し「indexed in bibliographic review」（Wikidata の型 `wikibase-entityid`）（57 列）
- 例1：Scopus（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：Scopus（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：Scopus（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0577 — wikidbs10k：見出し「half-life」（Wikidata の型 `quantity`）（56 列）
- 例1：+6.6 | +81.6 | +222.0 | +0.65 | +6.58（表：isotope of iodine／同じ表の列：label, description, decays to, subclass of, instance of, atomic number）
- 例2：+31.5 | +18.9 | +197.0 | +14.8 | +3.38（表：neon／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例3：+59.1 | +14.997 | +17.0 | +109.77 | +64.49（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）

## g0578 — wikidbs10k：見出し「era journal id」（Wikidata の型 `string`）（56 列）
- 例1：14806 | 2230 | 2205 | 17479 | 3161（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：2143 | 14754 | 15027 | 2110 | 14932（表：publishing／同じ表の列：label, description, instance of, ISSN, Scopus source ID, Danish Bibliometric…）
- 例3：17479 | 39798 | 16629 | 15528 | 39747（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0579 — wikidbs10k：見出し「nlm unique id」（Wikidata の型 `string`）（56 列）
- 例1：8006263 | 8502536 | 0410462 | 0376362 | 7505876（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：9421550 | 9211735 | 1256165 | 0372516 | 0400763（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：101674869 | 101124169 | 101160857 | 7610369 | 101640192（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0580 — sotab_v2：元の種類 `LocationFeatureSpecification`（55 列）
- 例1：Accesos adaptados
- 例2：Balcón | Zona Internet/WiFi | Accesos adaptados
- 例3：Breakfast Buffet

## g0581 — wikidbs10k：見出し「eligible voters」（Wikidata の型 `quantity`）（55 列）
- 例1：+413 | +274 | +714 | +1424 | +1555（表：Catalan regional election 2015 in Segrià／同じ表の列：label, description, instance of, country, applies to jurisdic…, point in time）
- 例2：+5690 | +1475 | +427 | +52037 | +171（表：Catalan regional election 2015 in Bages／同じ表の列：label, description, instance of, country, applies to jurisdic…, point in time）
- 例3：+8060 | +7803 | +8553 | +8081 | +8810（表：2016 Bury Metropolitan Borough Council …／同じ表の列：label, description, instance of, part of, country, point in time）

## g0582 — wikidbs10k：見出し「minimum temperature record」（Wikidata の型 `quantity`）（55 列）
- 例1：-32 | -40 | -30 | -52 | -70（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：-40.0 | -34.0 | -2.0 | -63.0 | -23.0（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：-23 | -52 | -40 | -2 | -34（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0583 — wikidbs10k：見出し「jufo id」（Wikidata の型 `string`）（55 列）
- 例1：59617 | 59727 | 55681 | 55663 | 61331（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：51693 | 55693 | 59727 | 81584 | 64903（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：63774 | 63777 | 63771 | 63759 | 63772（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0584 — wikidbs10k：見出し「open library subject id」（Wikidata の型 `string`）（55 列）
- 例1：spanish_language | korean_language | finnish_language | swedish_language | french_language（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：french_language | german_language | portuguese_language | danish_language | spanish_language（表：language proficiency／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：german_language | portuguese_language | dutch_language | javanese_language | finnish_language（表：language／同じ表の列：label, description, language regulatory…, UNESCO Thesaurus ID, subclass of, Glottolog code）

## g0585 — wikidbs10k：見出し「swedish organization number」（Wikidata の型 `string`）（55 列）
- 例1：212000-0100 | 212000-1165 | 212000-0738 | 212000-1132 | 212000-0829（表：administrative territorial entity／同じ表の列：label, description, shares border with, coat of arms image, Commons category, country）
- 例2：212000-0142 | 212000-2551 | 212000-1124 | 212000-0746 | 212000-0217（表：political border／同じ表の列：label, description, Commons category, coat of arms image, country, located in the admi…）
- 例3：212000-1439 | 212000-0134 | 212000-2742 | 212000-0142 | 212000-2759（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）

## g0586 — wikidbs10k：見出し「has grammatical case」（Wikidata の型 `wikibase-entityid`）（55 列）
- 例1：genitive case | nominative case（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：nominative case | instrumental case | genitive case（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：genitive case | nominative case（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0587 — wikidbs10k：見出し「has seal, badge, or sigil」（Wikidata の型 `wikibase-entityid`）（55 列）
- 例1：Seal of Tennessee | Seal of Pennsylvania | seal of Virginia | Seal of Ohio | Great Seal of the State of Montana（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：Great Seal of the Realm | Seal of Pennsylvania | Great Seal of Canada | Seal of California | Seal of Tennessee（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：Great Seal of the Realm | Seal of New York | coat of arms of New Jersey | Great Seal of the State of Maryland | State Seal of Texas（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0588 — wikidbs10k：見出し「main regulatory text」（Wikidata の型 `wikibase-entityid`）（55 列）
- 例1：The Swedish Local Government Act（表：administrative territorial entity／同じ表の列：label, description, shares border with, coat of arms image, Commons category, country）
- 例2：The Swedish Local Government Act（表：political border／同じ表の列：label, description, Commons category, coat of arms image, country, located in the admi…）
- 例3：The Swedish Local Government Act（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）

## g0589 — wikidbs10k：見出し「maximum temperature record」（Wikidata の型 `quantity`）（54 列）
- 例1：+121 | +111 | +110 | +56.7 | +109（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：118.0 | 49.6 | 56.7 | 113.0 | 134.0（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：+56.7 | +110 | +109 | +111 | +113（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0590 — wikidbs10k：見出し「terminologia anatomica 98 id」（Wikidata の型 `string`）（54 列）
- 例1：A09.3.01.001 | A14.1.09.402 | A02.0.00.000 | A05.4.01.001 | A04.6.02.019（表：expressed in／同じ表の列：label, description, Foundational Model …, Commons category, Freebase ID, described by source）
- 例2：A05.5.01.027 | A15.2.05.001 | A11.1.00.002 | A09.1.01.001 | A09.3.01.001（表：expressed in／同じ表の列：label, description, Foundational Model …, described by source, MeSH tree code, JSTOR topic ID）
- 例3：A05.4.01.001 | A12.1.00.012 | A14.2.07.062 | A01.1.00.025 | A14.1.06.111（表：expressed in／同じ表の列：label, description, Commons category, subclass of, Freebase ID, Foundational Model …）

## g0591 — wikidbs10k：見出し「fips 5-2 numeric code (us states)」（Wikidata の型 `string`）（53 列）
- 例1：29.0 | 48.0 | 39.0 | 24.0 | 47.0（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例2：35 | 17 | 19 | 51 | 06（表：jurisdiction／同じ表の列：label, description, named after, Dewey Decimal Class…, topic's main Wikime…, country）
- 例3：38 | 13 | 55 | 56 | 25（表：facet of／同じ表の列：label, description, named after, Dewey Decimal Class…, topic's main Wikime…, country）

## g0592 — wikidbs10k：見出し「transporter classification database id」（Wikidata の型 `string`）（53 列）
- 例1：9.A.57.1.3 | 9.A.38.1.1 | 9.A.29.3.4 | 9.A.15.2.1 | 9.A.64.1.1（表：Transporters of unknown biochemical mec…／同じ表の列：label, description, UniProt protein ID, encoded by, cell component, biological process）
- 例2：9.A.57.1.4 | 9.A.38.1.1 | 9.A.63.1.1 | 9.A.55.1.1 | 9.A.11.1.1（表：encodes／同じ表の列：label, description, UniProt protein ID, encoded by, cell component, biological process）
- 例3：3.A.2.2.9 | 3.A.2.2.1 | 3.A.2.2.3 | 3.A.2.2.6 | 3.A.2.2.4（表：V-ATPase／同じ表の列：label, description, UniProt protein ID, encoded by, Ensembl protein ID, biological process）

## g0593 — wikidbs10k：見出し「general classification of race participants」（Wikidata の型 `wikibase-entityid`）（53 列）
- 例1：Amber Neben | Grace Verbeke | Chantal Blaak | Emma Johansson | Giorgia Bronzini（表：2011 in women's road cycling／同じ表の列：label, description, sport, instance of, edition number, part of）
- 例2：Liesbet De Vocht | Wendy Houvenaghel | Chantal Blaak | Adrie Visser | Grace Verbeke（表：followed by／同じ表の列：label, description, sport, instance of, follows, followed by）
- 例3：Iljo Keisse | Dylan Groenewegen | Timo Roosen | Marcel Kittel | Theo Bos（表：Tacx Pro Classic／同じ表の列：label, description, sport, instance of, edition number, part of）

## g0594 — wikidbs10k：見出し「fips 5-2 alpha code (us states)」（Wikidata の型 `string`）（52 列）
- 例1：OH | MO | MD | NY | NJ（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例2：MA | OK | AZ | WV | CT（表：jurisdiction／同じ表の列：label, description, named after, Dewey Decimal Class…, topic's main Wikime…, country）
- 例3：TX | NC | AZ | VA | FL（表：facet of／同じ表の列：label, description, named after, Dewey Decimal Class…, topic's main Wikime…, country）

## g0595 — wikidbs10k：見出し「grid id」（Wikidata の型 `string`）（52 列）
- 例1：grid.275752.0 | grid.431455.2 | grid.462207.5 | grid.421003.4 | grid.422516.6（表：publisher／同じ表の列：label, description, official website, instance of, inception, headquarters locati…）
- 例2：grid.471061.5 | grid.418547.b | grid.497160.d | grid.410862.9 | grid.410792.9（表：manufacturer／同じ表の列：label, description, industry, instance of, country, Commons category）
- 例3：grid.469470.8 | grid.414964.a | grid.42505.36 | grid.417748.9 | grid.411134.2（表：part／同じ表の列：label, description, country, instance of, Freebase ID, official website）

## g0596 — wikidbs10k：見出し「insee canton code」（Wikidata の型 `string`）（52 列）
- 例1：217 | 4421 | 3827 | 9202 | 3710（表：electoral district／同じ表の列：label, description, instance of, country, capital, locator map image）
- 例2：6014 | 2921 | 2227 | 503 | 8605（表：electoral district／同じ表の列：label, description, instance of, country, capital, locator map image）
- 例3：1413 | 8912 | 6319 | 7201 | 4109（表：electoral district／同じ表の列：label, description, capital, instance of, country, locator map image）

## g0597 — wikidbs10k：見出し「ror id」（Wikidata の型 `string`）（52 列）
- 例1：025mg0739 | 05fxhrw65 | 059dqb057 | 02scfj030 | 037mx5d24（表：publisher／同じ表の列：label, description, official website, instance of, inception, headquarters locati…）
- 例2：040pjdm93 | 05dtvab05 | 00xj9p276 | 01vaekj86 | 04rn3ph18（表：manufacturer／同じ表の列：label, description, industry, instance of, country, Commons category）
- 例3：05a15z872 | 03wfqwh68 | 004rs4477 | 05vt9qd57 | 01xfcjr43（表：part／同じ表の列：label, description, country, instance of, Freebase ID, official website）

## g0598 — wikidbs10k：見出し「bti governance index」（Wikidata の型 `quantity`）（51 列）
- 例1：5.91 | 6.01 | 4.18 | 2.77 | 2.85（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+6.88 | +6.66 | +3 | +6 | +6.21（表：country／同じ表の列：label, description, VIAF ID, continent, Wikimedia outline, BBC Things ID）
- 例3：+3.54 | +2.17 | +5.28 | +5.58 | +4.68（表：country／同じ表の列：label, description, Great Russian Encyc…, Getty Thesaurus of …, topic's main Wikime…, Wikimedia outline）

## g0599 — wikidbs10k：見出し「bti status index」（Wikidata の型 `quantity`）（51 列）
- 例1：3.63 | 5.65 | 7.15 | 5.14 | 3.58（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+8.66 | +8.85 | +5.65 | +7 | +8.7（表：country／同じ表の列：label, description, VIAF ID, continent, Wikimedia outline, BBC Things ID）
- 例3：+4.29 | +5.2 | +3.82 | +5.12 | +8.99（表：country／同じ表の列：label, description, Great Russian Encyc…, Getty Thesaurus of …, topic's main Wikime…, Wikimedia outline）

## g0600 — wikidbs10k：見出し「astronomic symbol image」（Wikidata の型 `string`）（51 列）
- 例1：Triton symbol (fixed width).svg | Ceres symbol (fixed width).svg | Titan symbol (variable width).svg | Mars symbol (fixed width).svg | Enceladus symbol (fixed width).svg（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, image）
- 例2：Dorado symbol (Moskowitz, variable widt… | Carina symbol (Moskowitz, variable widt… | Orion symbol (Moskowitz, variable width… | Tucana symbol (Moskowitz, variable widt… | Cygnus symbol (Moskowitz, variable widt…（表：constellation／同じ表の列：label, description, Commons category, topic's main catego…, Freebase ID, locator map image）
- 例3：Monoceros symbol (Moskowitz, variable w… | Cepheus symbol (Moskowitz, variable wid… | Canis Minor symbol (Moskowitz, variable… | Perseus symbol (Moskowitz, variable wid… | Aquila symbol (Moskowitz, variable widt…（表：political border／同じ表の列：label, description, Commons category, instance of, image, topic's main catego…）

## 答えの雛形

```
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
g0481	
g0482	
g0483	
g0484	
g0485	
g0486	
g0487	
g0488	
g0489	
g0490	
g0491	
g0492	
g0493	
g0494	
g0495	
g0496	
g0497	
g0498	
g0499	
g0500	
g0501	
g0502	
g0503	
g0504	
g0505	
g0506	
g0507	
g0508	
g0509	
g0510	
g0511	
g0512	
g0513	
g0514	
g0515	
g0516	
g0517	
g0518	
g0519	
g0520	
g0521	
g0522	
g0523	
g0524	
g0525	
g0526	
g0527	
g0528	
g0529	
g0530	
g0531	
g0532	
g0533	
g0534	
g0535	
g0536	
g0537	
g0538	
g0539	
g0540	
g0541	
g0542	
g0543	
g0544	
g0545	
g0546	
g0547	
g0548	
g0549	
g0550	
g0551	
g0552	
g0553	
g0554	
g0555	
g0556	
g0557	
g0558	
g0559	
g0560	
g0561	
g0562	
g0563	
g0564	
g0565	
g0566	
g0567	
g0568	
g0569	
g0570	
g0571	
g0572	
g0573	
g0574	
g0575	
g0576	
g0577	
g0578	
g0579	
g0580	
g0581	
g0582	
g0583	
g0584	
g0585	
g0586	
g0587	
g0588	
g0589	
g0590	
g0591	
g0592	
g0593	
g0594	
g0595	
g0596	
g0597	
g0598	
g0599	
g0600	
```
