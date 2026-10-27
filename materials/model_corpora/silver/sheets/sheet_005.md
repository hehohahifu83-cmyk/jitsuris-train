# 銀ラベルのシート 005 / 008（外の学習データの読み替え）

- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列
- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`
- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を、ChatGPT は `answers/sheet_005.tsv`、Grok は `answers_grok/sheet_005.tsv` に写して埋める。**相手の答えは見ない**

## g0601 — wikidbs10k：見出し「danish bibliometric research indicator (bfi) sno/cno」（Wikidata の型 `string`）（51 列）
- 例1：2298 | 5884 | 12242 | 2921 | 7307（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：704 | 13305 | 8453 | 10566 | 11982（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：7390 | 7641 | 14974 | 10255 | 3956（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0602 — wikidbs10k：見出し「danish bibliometric research indicator level」（Wikidata の型 `string`）（51 列）
- 例1：2 | 1（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：2 | 1（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：2 | 1（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0603 — wikidbs10k：見出し「ta98 latin term」（Wikidata の型 `string`）（51 列）
- 例1：corpus amygdaloideum | testis | ileum | m. triceps brachii | systema skeletale（表：expressed in／同じ表の列：label, description, Foundational Model …, Terminologia Anatom…, Commons category, Freebase ID）
- 例2：lens | n. suralis | thymus | lobus anterior | nucleus supraopticus（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Foundational Model …, described by source, MeSH tree code）
- 例3：tendo calcaneus | gyrus cinguli | Arteria carotis interna | oesophagus | thymus（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Commons category, subclass of, Freebase ID）

## g0604 — wikidbs10k：見出し「parent club」（Wikidata の型 `wikibase-entityid`）（51 列）
- 例1：Memphis Tigers | Florida State Seminoles | Georgetown Hoyas | Seton Hall Pirates | Colorado State Rams（表：participating team／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例2：Arizona Wildcats | UTEP Miners | Duke Blue Devils | South Alabama Jaguars | Illinois Fighting Illini（表：winner／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例3：Princeton Tigers | Florida State Seminoles | Iowa Hawkeyes | LSU Tigers | Mississippi State Bulldogs（表：participating team／同じ表の列：label, description, topic's main catego…, Freebase ID, instance of, league）

## g0605 — wikidbs10k：見出し「linkedin organization id」（Wikidata の型 `string`）（50 列）
- 例1：ostersunds-kommun | stockholmsstad | umea-kommun | partille-kommun | lunds-kommun（表：administrative territorial entity／同じ表の列：label, description, shares border with, coat of arms image, Commons category, country）
- 例2：provincie-noord-brabant | provincie-gelderland | provincie-flevoland | provincie-overijssel | provincie-groningen（表：jurisdiction／同じ表の列：label, description, locator map image, coordinate location, instance of, contains the admini…）
- 例3：ljusdals-kommun | stockholmsstad | sundsvalls-kommun | jarfallakommun | -nge-kommun（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）

## g0606 — wikidbs10k：見出し「sports-reference.com college basketball school id」（Wikidata の型 `string`）（50 列）
- 例1：missouri/men | evansville/men | texas-el-paso/men | syracuse/men | louisville/men（表：participating team／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例2：evansville/men | arkansas/men | duke/men | louisiana-tech/men | nevada-las-vegas/men（表：winner／同じ表の列：label, description, topic's main catego…, instance of, official website, sport）
- 例3：nebraska/men | princeton/men | michigan-state/men | syracuse/men | connecticut/men（表：participating team／同じ表の列：label, description, topic's main catego…, Freebase ID, instance of, parent club）

## g0607 — wikidbs10k：見出し「scilit journal id」（Wikidata の型 `string`）（49 列）
- 例1：44846 | 35147 | 149 | 205203 | 169162（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：180202 | 1592510 | 520133 | 126354 | 1770368（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）
- 例3：2130 | 44846 | 100270 | 98240 | 602353（表：publishing／同じ表の列：label, description, instance of, Freebase ID, ISSN, ERA Journal ID）

## g0608 — wikidbs10k：見出し「natural product of taxon」（Wikidata の型 `wikibase-entityid`）（49 列）
- 例1：sugar beet | Benincasa | Allium cepa | Tuber | Cucumis sativus（表：product／同じ表の列：label, description, subclass of, image, UNII）
- 例2：cassava | Brassica oleracea var. botrytis | Citrullus lanatus var. lanatus | Allium ampeloprasum var. porrum | Oryza sativa（表：natural product／同じ表の列：label, description, subclass of, image, WordNet 3.1 Synset …）
- 例3：Angelica dahurica | Phellodendron amurense | Coptis japonica | Citrus × aurantium | Chinese peony（表：keigairengyoto／同じ表の列：label, description, instance of, KEGG ID, PubChem Substance I…, subclass of）

## g0609 — wikidbs10k：見出し「pactols thesaurus id」（Wikidata の型 `string`）（48 列）
- 例1：pcrt0Ez5Vv3Vm3 | pcrtiOMGsqH92p | pcrtJalayzhciB | pcrtGFLAWgSypG | pcrtz7kHpmkZ8I（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例2：pcrt3KtdnXPGUg | pcrtcWoSlbWLE0 | pcrtkn1hAXHveS | pcrtSkipOsBGML | pcrtjzKlry0LZi（表：material／同じ表の列：label, description, subclass of, Commons category, BNCF Thesaurus ID, GND ID）
- 例3：pcrtTsFUpot5O5 | pcrt1urpl6axh0 | pcrt4J7FjGwrcR | pcrtuzhI7VazjA | pcrtgrOmZOUoPZ（表：facet of／同じ表の列：label, description, OmegaWiki Defined M…, BNCF Thesaurus ID, Commons category, image）

## g0610 — wikidbs10k：見出し「religion or worldview」（Wikidata の型 `wikibase-entityid`）（48 列）
- 例1：Judaism | Christianity | Catholic Church（表：patron saint／同じ表の列：label, description, Library of Congress…, Commons category, VIAF ID, ISNI）
- 例2：Kegon | Daitoku-ji school | Tōji Shingon-shū | East Asian Yogācāra | Shingon Buddhism（表：part／同じ表の列：label, description, official website, Commons category, coordinate location, Freebase ID）
- 例3：Shingon-shū Chizan-ha | Shingon-shu Buzan-ha | Kōyasan Shingon-shū | Tōji Shingon-shū | Shingon-shū Daigo-ha（表：Shingon sect eighteen Motoyama／同じ表の列：label, description, Commons category, coordinate location, Freebase ID, instance of）

## g0611 — wikidbs10k：見出し「bulbapedia article id」（Wikidata の型 `string`）（47 列）
- 例1：Baltoy_(Pokémon) | Dhelmise_(Pokémon) | Copperajah_(Pokémon) | Coalossal_(Pokémon) | Voltorb_(Pokémon)（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, Pokémon index, part of, height）
- 例2：Victreebel_(Pokémon) | Ivysaur_(Pokémon) | Weepinbell_(Pokémon) | Cottonee_(Pokémon) | Steenee_(Pokémon)（表：Grass egg group／同じ表の列：label, description, part of, from narrative univ…, instance of, Pokémon index）
- 例3：Xerneas_(Pokémon) | Mawile_(Pokémon) | Cutiefly_(Pokémon) | Mr._Mime_(Pokémon) | Togepi_(Pokémon)（表：fairy-type Pokémon／同じ表の列：label, description, instance of, part of, from narrative univ…, Pokémon index）

## g0612 — wikidbs10k：見出し「original language of film or tv show」（Wikidata の型 `wikibase-entityid`）（47 列）
- 例1：English | Japanese | French | Spanish | Filipino（表：anthology series／同じ表の列：label, description, instance of, genre, country of origin, original broadcaster）
- 例2：Japanese | English | Swedish | German（表：season finale／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例3：Japanese | German | Swedish | English | Arabic（表：television series season／同じ表の列：label, description, instance of, part of the series, number of episodes, has part(s)）

## g0613 — wikidbs10k：見出し「product or material produced」（Wikidata の型 `wikibase-entityid`）（47 列）
- 例1：terrestrial television（表：operator／同じ表の列：label, description, headquarters locati…, Commons category, instance of, Freebase ID）
- 例2：garlic | edible mushroom | cabbage | spinach | yam（表：growing of vegetables and melons, roots…／同じ表の列：label, description, instance of, subclass of, image）
- 例3：still camera | computer keyboard | printer | consumer electronics | single-lens reflex camera（表：manufacturer／同じ表の列：label, description, industry, instance of, country, Commons category）

## g0614 — wikidbs10k：見出し「flora of china id」（Wikidata の型 `string`）（46 列）
- 例1：200015350.0 | 200017769.0 | 120248.0 | 200020285.0 | 200008034.0（表：secretion or excretion／同じ表の列：label, description, Commons category, image, taxon name, taxon rank）
- 例2：107435 | 125778 | 107946 | 124944 | 104853（表：taxon／同じ表の列：label, description, Commons category, taxon rank, taxon name, image）
- 例3：106736 | 114356 | 104693 | 120129 | 122138（表：taxon／同じ表の列：label, description, image, Freebase ID, Commons category, taxon name）

## g0615 — wikidbs10k：見出し「annual number of weddings」（Wikidata の型 `quantity`）（45 列）
- 例1：851 | 564 | 958 | 533 | +97（表：administrative territorial entity／同じ表の列：label, description, instance of, Commons category, located in the admi…, coordinate location）
- 例2：97.0 | 9021.0 | 2686.0 | 7609.0 | 590.0（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, topic's main Wikime…, Commons category, country）
- 例3：1492 | 2308 | 1017 | 346 | 590（表：physical location／同じ表の列：label, description, Dewey Decimal Class…, topic's main Wikime…, Commons category, country）

## g0616 — wikidbs10k：見出し「height」（Wikidata の型 `quantity`）（45 列）
- 例1：+390 | +40 | +0.90 | +280 | +140（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, Pokémon index, part of, color）
- 例2：+124.1 | +124.9 | +124.3 | +124.5 | +124.4（表：Windsor Beauties／同じ表の列：label, description, inventory number, collection, instance of, location）
- 例3：+124.1 | +124.3 | +125.9 | +124.4 | +125.8（表：depicting object／同じ表の列：label, description, inventory number, collection, instance of, location）

## g0617 — wikidbs10k：見出し「number of seats」（Wikidata の型 `quantity`）（45 列）
- 例1：37 | 29 | 15 | 22 | 39（表：legislature／同じ表の列：label, description, topic's main catego…, instance of, country, applies to jurisdic…）
- 例2：+29 | +25 | +17 | +21 | +41（表：district council of Hong Kong／同じ表の列：label, description, Commons category, topic's main catego…, instance of, country）
- 例3：+39 | +34 | +41 | +29 | +22（表：legislature／同じ表の列：label, description, topic's main catego…, Commons category, instance of, country）

## g0618 — wikidbs10k：見出し「total valid votes」（Wikidata の型 `quantity`）（45 列）
- 例1：+909 | +215 | +223 | +162 | +866（表：Catalan regional election 2015 in Segrià／同じ表の列：label, description, instance of, country, applies to jurisdic…, point in time）
- 例2：+3085 | +4498 | +3029 | +3566 | +3944（表：2016 Bolton Metropolitan Borough Counci…／同じ表の列：label, description, instance of, part of, country, point in time）
- 例3：4113 | 3268 | 2782 | 3370 | 3699（表：followed by／同じ表の列：label, description, instance of, part of, country, follows）

## g0619 — wikidbs10k：見出し「utc timezone offset」（Wikidata の型 `quantity`）（45 列）
- 例1：+3 | +5.5 | -5 | +0 | +1（表：time zone／同じ表の列：label, description, Freebase ID, instance of, Commons category, image）
- 例2：-5 | +3 | +2 | +0 | +8（表：time zone／同じ表の列：label, description, instance of, Freebase ID, said to be the same…, image）
- 例3：-3 | -1 | +2 | -10 | -5（表：time zone／同じ表の列：label, description, Freebase ID, instance of, Commons category, image）

## g0620 — wikidbs10k：見出し「acnp journal id」（Wikidata の型 `string`）（45 列）
- 例1：2109559 | 2393 | 2350 | 2165396 | 2702（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：81379 | 885 | 600 | 14119 | 12620（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：1016986 | 857995 | 1068492 | 3310670 | 2721（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0621 — wikidbs10k：見出し「ipa transcription」（Wikidata の型 `string`）（45 列）
- 例1：ɪˈtaljɪjə | (j)ɪˈponjɪjə | ˈstuɾbɾɪtɑːnɪɑ | ˈʂvjet͡sɨjə | ɐfˈstraljɪjə（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：ʉːɛˈsɑː | ˈmexiko | ˈʂvjet͡sɨjə | (j)ɪˈponjɪjə | ɪˈtaljɪjə（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：ˈnɔɾgə | ɐfˈstraljɪjə | kɾuːˈɑtsɪɑ | ˈbjeljɡjɪjə | ˈaɪəɹlənd（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, category for films …, GND ID）

## g0622 — wikidbs10k：見出し「ta2 id」（Wikidata の型 `string`）（45 列）
- 例1：366 | 5456 | 3576 | 2887 | 2471（表：expressed in／同じ表の列：label, description, Foundational Model …, Terminologia Anatom…, Commons category, Freebase ID）
- 例2：3470 | 6798 | 6586 | 2914 | 3855（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Foundational Model …, described by source, MeSH tree code）
- 例3：2662 | 148 | 4369 | 5881 | 4463（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Commons category, subclass of, Freebase ID）

## g0623 — wikidbs10k：見出し「characters」（Wikidata の型 `wikibase-entityid`）（45 列）
- 例1：Guan Yin | Eight Vajradharas | Xuanzang | Emperor Taizong of Tang | Zhenyuan Daxian（表：Journey to the West／同じ表の列：label, description, language of work or…, follows, chapter, instance of）
- 例2：Xuanzang | Rulai Buddha | Eight Vajradharas | Bull Demon King | Sun Wukong（表：followed by／同じ表の列：label, description, language of work or…, follows, part of, chapter）
- 例3：Xuanzang | Jade Emperor | Golden-haired Hou | Guan Yin | Taibai Jinxing（表：follows／同じ表の列：label, description, language of work or…, follows, part of, chapter）

## g0624 — wikidbs10k：見出し「ethnic group」（Wikidata の型 `wikibase-entityid`）（45 列）
- 例1：Germans | Mestizos in Mexico | Japanese people | Austrians | White Americans（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：English people | Austrians | Mestizos in Mexico | Germans | White Americans（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Brancos | Spaniards | Indo-Aryan peoples | White Americans | European people（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0625 — wikidbs10k：見出し「voting system」（Wikidata の型 `wikibase-entityid`）（45 列）
- 例1：first-past-the-post voting（表：2016 Bolton Metropolitan Borough Counci…／同じ表の列：label, description, instance of, part of, country, point in time）
- 例2：Plurality-at-large | first-past-the-post voting（表：followed by／同じ表の列：label, description, instance of, part of, country, follows）
- 例3：first-past-the-post voting（表：follows／同じ表の列：label, description, instance of, part of, country, point in time）

## g0626 — wikidbs10k：見出し「uniprot journal id」（Wikidata の型 `string`）（44 列）
- 例1：1175 | 0973 | 0708 | 1610 | 1222（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：1541 | 0451 | 1610 | 2027 | 0174（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：1422 | 2910 | 1270 | 4078 | 1412（表：publishing／同じ表の列：label, description, official website, Freebase ID, instance of, ISSN）

## g0627 — wikidbs10k：見出し「usda plants id」（Wikidata の型 `string`）（44 列）
- 例1：ERYTH | LONCH | DORST | MORUS | TEPHR（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例2：DACA6 | IPOMO | ALAM | CUCUM | BROL（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例3：CIGL | PISA6 | CUMA3 | ALSTR | RASA2（表：natural product／同じ表の列：label, description, taxon name, taxon rank, instance of, parent taxon）

## g0628 — wikidbs10k：見出し「opposite of」（Wikidata の型 `wikibase-entityid`）（44 列）
- 例1：Category:Deaths in Austria | Category:Deaths in Sweden | Category:Deaths in Mexico | Category:Deaths in Italy | Category:Death in Japan（表：place of birth／同じ表の列：label, description, instance of, category combines t…, category contains, Commons category）
- 例2：Category:Films set in Brazil | Category:Films set in Paraguay | Category:Films set in the Caribbean | Category:Films set in Uruguay | Category:Films set in French Guiana（表：category for films shot at this location／同じ表の列：label, description, instance of, category combines t…, category contains）
- 例3：Category:Births in London | Category:Births in The Hague | Category:Births in New Delhi | Category:Births in Port of Spain | Category:Births in Gibraltar（表：place of death／同じ表の列：label, description, instance of, category combines t…, category contains）

## g0629 — wikidbs10k：見出し「place of publication」（Wikidata の型 `wikibase-entityid`）（44 列）
- 例1：United States of America | Japan | California（表：video game retail package／同じ表の列：label, description, platform, publication date, publisher, part of）
- 例2：London（表：Household stories from the collection o…／同じ表の列：label, description, instance of, author, translator, title）
- 例3：London（表：followed by／同じ表の列：label, description, instance of, author, translator, title）

## g0630 — wikidbs10k：見出し「google arts & culture entity id」（Wikidata の型 `string`）（43 列）
- 例1：m07ssc | m05r4w | m09c7w0 | m07t21 | m0345h（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：m09c7w0 | m0345h | m07ssc | m0f8l9c | m06mkj（表：country／同じ表の列：label, description, Great Russian Encyc…, participant in, coordinates of sout…, New York Times topi…）
- 例3：m0345h | m04g61 | m02vzc | m0154j | m09c7w0（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0631 — wikidbs10k：見出し「pole position」（Wikidata の型 `wikibase-entityid`）（42 列）
- 例1：Paul Tracy | Ryan Hunter-Reay | Sébastien Bourdais | Patrick Carpentier | Bruno Junqueira（表：2004 Champ Car season／同じ表の列：label, description, sport, point in time, instance of, country）
- 例2：Dave Marcis | David Pearson | Benny Parsons | Buddy Baker | Darrell Waltrip（表：1976 NASCAR Winston Cup Series／同じ表の列：label, description, sport, point in time, instance of, part of）
- 例3：Tom Pistone | Buddy Baker | LeeRoy Yarbrough | David Pearson | Richard Petty（表：1966 NASCAR Grand National Series／同じ表の列：label, description, sport, point in time, instance of, part of）

## g0632 — wikidbs10k：見出し「genuki id」（Wikidata の型 `string`）（41 列）
- 例1：sct/ABD | sct/INV | sct/STI | sct/PER | sct/FIF（表：historic county／同じ表の列：label, description, instance of, coordinate location, country, locator map image）
- 例2：sct/BEW | sct/SUT | sct/MLN | sct/ANS | sct/STI（表：historic county／同じ表の列：label, description, instance of, country, locator map image, Gazetteer for Scotl…）
- 例3：sct/LKS/Bothwell | sct/RFW/Eastwood | sct/LKS/Glasgow | sct/KRS/Fossoway | sct/RFW/Neilston（表：part／同じ表の列：label, description, instance of, country, Vision of Britain u…, located in the admi…）

## g0633 — wikidbs10k：見出し「iconclass notation」（Wikidata の型 `string`）（41 列）
- 例1：73B2 | 73A42 | 73B93 | 73A31 | 73A6（表：topic／同じ表の列：label, description, Commons category, Freebase ID, instance of, image）
- 例2：23I11 | 23I32 | 23I21 | 23I23 | 23I42（表：calendar month／同じ表の列：label, description, page banner, image, OmegaWiki Defined M…, named after）
- 例3：23I22 | 23I13 | 23I21 | 23I31 | 23I23（表：followed by／同じ表の列：label, description, page banner, OmegaWiki Defined M…, named after, follows）

## g0634 — wikidbs10k：見出し「anidb tag id」（Wikidata の型 `string`）（40 列）
- 例1：1670 | 997 | 637 | 2758 | 1406（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）
- 例2：1406 | 1004 | 2758 | 183 | 637（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, subclass of, Commons category, BNCF Thesaurus ID）
- 例3：1004.0 | 2757.0 | 3209.0 | 2760.0 | 183.0（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, Commons category, subclass of, BNCF Thesaurus ID）

## g0635 — wikidbs10k：見出し「tdv i̇slam ansiklopedisi id」（Wikidata の型 `string`）（40 列）
- 例1：ispanya | kazakistan | afganistan | hindistan | italya（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：romanya | belcika | hindistan | avustralya | pakistan（表：country／同じ表の列：label, description, Great Russian Encyc…, participant in, population, Getty Thesaurus of …）
- 例3：kafirun-suresi | karia-suresi | ahkaf-suresi | rum-suresi | fussilet-suresi（表：surah／同じ表の列：label, description, instance of, Freebase ID, Commons category, has edition or tran…）

## g0636 — wikidbs10k：見出し「patron saint」（Wikidata の型 `wikibase-entityid`）（40 列）
- 例1：Saint Nicholas | Anthony the Great | Our Lady of the Rosary | Assumption of Mary | Michael（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）
- 例2：Martin of Tours | Ambrose | Faustinus and Jovita | Victor Maurus | Gervasius and Protasius（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）
- 例3：Anselm of Lucca | Nativity of Mary | John the Baptist | Lawrence of Rome | Paul the Apostle（表：political border／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）

## g0637 — wikidbs10k：見出し「administrative code of indonesia」（Wikidata の型 `string`）（38 列）
- 例1：51.05.02 | 51.05.03.2002 | 51.07.04.2001 | 51.03.02 | 51.03.03（表：administrative territorial entity／同じ表の列：label, description, instance of, country, GeoNames ID, coordinate location）
- 例2：14.03 | 71.0 | 11.06 | 82.01 | 75.71.02（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, flag image, Commons category, country）
- 例3：72.08 | 71.0 | 33.0 | 82.0 | 35.0（表：political border／同じ表の列：label, description, instance of, located in the admi…, capital, country）

## g0638 — wikidbs10k：見出し「democracy club election id」（Wikidata の型 `string`）（38 列）
- 例1：local.bolton.horwich-and-blackrod.2016-… | local.bolton.heaton-and-lostock.2016-05… | local.bolton.westhoughton-north-and-che… | local.bolton.horwich-north-east.2016-05… | local.bolton.harper-green.2016-05-05（表：2016 Bolton Metropolitan Borough Counci…／同じ表の列：label, description, instance of, part of, country, point in time）
- 例2：local.bolton.westhoughton-south.2019-05… | local.bolton.bromley-cross.2019-05-02 | local.bolton.harper-green.2018-05-03 | local.bolton.kearsley.2018-05-03 | local.bolton.westhoughton-north-and-che…（表：followed by／同じ表の列：label, description, instance of, part of, country, follows）
- 例3：local.bolton.great-lever.2016-05-05 | local.bolton.westhoughton-south.2016-05… | local.bolton.rumworth.2016-05-05 | local.bolton.halliwell.2016-05-05 | local.bolton.tonge-with-the-haulgh.2016…（表：follows／同じ表の列：label, description, instance of, part of, country, point in time）

## g0639 — wikidbs10k：見出し「procyclingstats race id」（Wikidata の型 `string`）（38 列）
- 例1：247661 | 269763 | 150091 | 255551 | 172795（表：GP Slovenian Istria／同じ表の列：label, description, instance of, follows, sport, part of）
- 例2：116767 | 116894 | 116976 | 116780 | 116895（表：2013 UCI World Tour／同じ表の列：label, description, follows, instance of, Freebase ID, followed by）
- 例3：139014 | 139156 | 139155 | 139078 | 139033（表：followed by／同じ表の列：label, description, winner, followed by, instance of, Freebase ID）

## g0640 — wikidbs10k：見出し「statistics indonesia area code」（Wikidata の型 `string`）（38 列）
- 例1：5106040012 | 32 | 5105020 | 5105010013 | 5104060006（表：administrative territorial entity／同じ表の列：label, description, instance of, country, GeoNames ID, administrative code…）
- 例2：32.0 | 21.0 | 6472031.0 | 2171.0 | 8271012.0（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, flag image, Commons category, country）
- 例3：3508.0 | 5103.0 | 31.0 | 72.0 | 3509.0（表：political border／同じ表の列：label, description, instance of, located in the admi…, capital, country）

## g0641 — wikidbs10k：見出し「un/locode」（Wikidata の型 `string`）（38 列）
- 例1：ITINI | ITFAA | ITZWT | ITBXI | ITMTB（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, postal code, shares border with）
- 例2：ITDAA | ITBXI | ITCDQ | ITUGG | ITOSE（表：political border／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）
- 例3：ITBXI | ITINI | ITCMD | ITFIU | ITUGG（表：administrative centre／同じ表の列：label, description, postal code, shares border with, located in time zone, local dialing code）

## g0642 — wikidbs10k：見出し「has use」（Wikidata の型 `wikibase-entityid`）（38 列）
- 例1：food | spice | medicinal plant | vegetable（表：secretion or excretion／同じ表の列：label, description, Commons category, image, taxon name, taxon rank）
- 例2：Telugu | Amharic | Northern Sami | Georgian | Inupiaq（表：Braille／同じ表の列：label, description, Freebase ID, instance of）
- 例3：Industrial Waste Dam | Boa Saúde | industrial sector（表：dam with more than 70 meters and less t…／同じ表の列：label, description, volume as quantity, height, located in the admi…, coordinate location）

## g0643 — wikidbs10k：見出し「carbon footprint」（Wikidata の型 `quantity`）（37 列）
- 例1：339866.83 | 112134.41 | 321198.11 | 91869.83 | 104857.75（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, Commons category, country, ISO 3166-2 code）
- 例2：+141123.72 | +31975.2 | +195536.05 | +321198.11 | +112134.41（表：administrative centre／同じ表の列：label, description, located in the admi…, Commons category, country, ISO 3166-2 code）
- 例3：+134667.13 | +152069.47 | +110685.64 | +118086.94 | +88172.71（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, ISO 3166-2 code, located in the admi…）

## g0644 — wikidbs10k：見出し「number of decimal digits」（Wikidata の型 `quantity`）（37 列）
- 例1：+2 | +3 | +1 | +4（表：octagonal number／同じ表の列：label, description, instance of, Commons category, numeric value, KIT Linked Open Num…）
- 例2：+1 | +2（表：prime factor／同じ表の列：label, description, instance of, Commons category, numeric value, Unicode character）
- 例3：+4 | +1 | +2 | +3（表：centered pentagonal number／同じ表の列：label, description, instance of, Commons category, numeric value, KIT Linked Open Num…）

## g0645 — wikidbs10k：見出し「historical gazetteer (gov) id」（Wikidata の型 `string`）（37 列）
- 例1：object_320278 | object_1073196 | object_291964 | object_214200 | object_1071272（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, country, coordinate location, instance of）
- 例2：SENHA1JN59RF | NEUALZJN59RG | ALTOR1JN59QJ | KELEI1JN58WW | BURAN1JN59PI（表：administrative territorial entity／同じ表の列：label, description, topic's main catego…, country, Commons category, German municipality…）
- 例3：PERACHJN68JG | object_334008 | object_320864 | object_300287 | object_300323（表：Stimmkreis Altötting／同じ表の列：label, description, country, German municipality…, Commons category, coordinate location）

## g0646 — wikidbs10k：見出し「icd-11 (foundation)」（Wikidata の型 `string`）（37 列）
- 例1：1002532547 | 1708923236 | 1086407971 | 657365008 | 1036497592（表：expressed in／同じ表の列：label, description, Foundational Model …, Terminologia Anatom…, Commons category, Freebase ID）
- 例2：980718560 | 72252748 | 1814741078 | 430791912 | 198809973（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Commons category, subclass of, Freebase ID）
- 例3：704682604 | 328366540 | 198809973 | 720032908 | 2062516965（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Foundational Model …, described by source, instance of）

## g0647 — wikidbs10k：見出し「tabular population」（Wikidata の型 `string`）（37 列）
- 例1：Data:Population FR Q16627292.tab | Data:Population FR Q18413907.tab | Data:Population FR Q18123.tab | Data:Population FR Q788136.tab | Data:Population FR Q763536.tab（表：electoral district／同じ表の列：label, description, instance of, country, INSEE canton code, capital）
- 例2：Data:Population FR Q17177247.tab | Data:Population FR Q17623428.tab | Data:Population FR Q16912418.tab | Data:Population FR Q20670936.tab | Data:Population FR Q17623037.tab（表：electoral district／同じ表の列：label, description, instance of, country, INSEE canton code, capital）
- 例3：Data:Population FR Q1638325.tab | Data:Population FR Q1724340.tab | Data:Population FR Q976535.tab | Data:Population FR Q17623628.tab | Data:Population FR Q19606787.tab（表：electoral district／同じ表の列：label, description, capital, instance of, country, INSEE canton code）

## g0648 — wikidbs10k：見出し「located in the statistical territorial entity」（Wikidata の型 `wikibase-entityid`）（37 列）
- 例1：Ilha do Faial | Ilha do Pico | Ilha de Santa Maria | Ilha da Graciosa | Ilha de São Miguel（表：landform／同じ表の列：label, description, Dewey Decimal Class…, Commons category, instance of, coordinate location）
- 例2：Dayton metropolitan area | Seattle metropolitan area | Louisville metropolitan area | Atlanta–Sandy Springs–Alpharetta metrop… | Minneapolis–Saint Paul（表：physical location／同じ表の列：label, description, population, GND ID, instance of, country）
- 例3：Oklahoma City metropolitan area | Wichita Falls metropolitan area | Washtenaw County | Providence metropolitan area | Greater Los Angeles Area（表：administrative territorial entity／同じ表の列：label, description, twinned administrat…, GND ID, Commons category, country）

## g0649 — wikidbs10k：見出し「prime factor」（Wikidata の型 `wikibase-entityid`）（37 列）
- 例1：43 | 7 | 37 | 17 | 53（表：octagonal number／同じ表の列：label, description, instance of, Commons category, numeric value, KIT Linked Open Num…）
- 例2：23 | 43 | 13 | 53 | 19（表：prime factor／同じ表の列：label, description, instance of, Commons category, numeric value, Unicode character）
- 例3：2 | 181 | 1381 | 4951 | 23（表：centered pentagonal number／同じ表の列：label, description, instance of, Commons category, numeric value, KIT Linked Open Num…）

## g0650 — wikidbs10k：見出し「numeric value」（Wikidata の型 `quantity`）（36 列）
- 例1：+4720 | +44 | +176 | +1680 | +1408（表：octagonal number／同じ表の列：label, description, instance of, Commons category, KIT Linked Open Num…, number of decimal d…）
- 例2：+5 | +53 | +37 | +17 | +47（表：prime factor／同じ表の列：label, description, instance of, Commons category, Unicode character, KIT Linked Open Num…）
- 例3：+3901 | +951 | +526 | +8556 | +7701（表：centered pentagonal number／同じ表の列：label, description, instance of, Commons category, KIT Linked Open Num…, number of decimal d…）

## g0651 — wikidbs10k：見出し「retirement age」（Wikidata の型 `quantity`）（36 列）
- 例1：62.0 | 67.0 | 58.0 | 60.0 | 65.0（表：country／同じ表の列：label, description, coat of arms image, currency, flag image, Dewey Decimal Class…）
- 例2：+62 | +57 | +66.33 | +66 | +65.25（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：+60 | +65 | +63 | +66 | +62（表：country of origin／同じ表の列：label, description, page banner, member of, topic's main Wikime…, capital）

## g0652 — wikidbs10k：見出し「kegg id」（Wikidata の型 `string`）（36 列）
- 例1：D06768 | D06748 | D06736 | D06787 | D06706（表：keigairengyoto／同じ表の列：label, description, instance of, natural product of …, PubChem Substance I…, subclass of）
- 例2：D06706 | D06748 | D06703 | D00092 | D06727（表：natural product／同じ表の列：label, description, instance of, natural product of …, PubChem Substance I…, subclass of）
- 例3：D04365 | D06752 | D06758 | D06739 | D06764（表：goshakusan／同じ表の列：label, description, instance of, natural product of …, PubChem Substance I…, subclass of）

## g0653 — wikidbs10k：見出し「orthodox encyclopedia id」（Wikidata の型 `string`）（36 列）
- 例1：372674 | 2661908.0 | 2040510.0 | 2057274.0 | 1470175.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：1841141 | 114180 | 2001914 | 293910 | 187963（表：citizenship／同じ表の列：label, description, native label, driving side, topic's main Wikime…, category for people…）
- 例3：2057274.0 | 2040510.0 | 63028.0 | 2562792.0 | 529087.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0654 — wikidbs10k：見出し「has part(s) of the class」（Wikidata の型 `wikibase-entityid`）（36 列）
- 例1：merchant vessel（表：national merchant marine fleet／同じ表の列：label, description, instance of, part of, country）
- 例2：route nationale | French autoroute（表：Road network in France／同じ表の列：label, description, country, located in the admi…, instance of, subclass of）
- 例3：vertex（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）

## g0655 — wikidbs10k：見出し「properties for this type」（Wikidata の型 `wikibase-entityid`）（36 列）
- 例1：10 Hygiea | Yaroslavl | Calera de Tango | Rostov Oblast | Caligula（表：intentional human activity／同じ表の列：label, description, instance of, subclass of, field of this occup…, topic's main catego…）
- 例2：Calera de Tango | 10 Hygiea | Cher | Daniel Morgan | Pterophyllum altum（表：intentional human activity／同じ表の列：label, description, instance of, subclass of, female form of label, field of this occup…）
- 例3：July 21 | Rostov Oblast | 10 Hygiea | 1999 | Daniel Morgan（表：intentional human activity／同じ表の列：label, description, instance of, field of this occup…, subclass of, topic's main catego…）

## g0656 — wikidbs10k：見出し「terminus」（Wikidata の型 `wikibase-entityid`）（36 列）
- 例1：Liverpool Street station | Cambridge railway station | Charing Cross railway station | Liverpool Street and Norwich Line, Live… | Greenford station（表：railway line／同じ表の列：label, description, Commons category, country, instance of, located in the admi…）
- 例2：Lillerød | Ryparken station | City Hall Square | Farum | Ballerup（表：Copenhagen Super Bikeways／同じ表の列：label, description, instance of, part of, country, official website）
- 例3：USJ 7 station | Ampang LRT station | Tanjung Malim railway station | Kwasa Damansara MRT station | Gombak LRT station（表：Rapid KL／同じ表の列：label, description, instance of, Commons category, Freebase ID, country）

## g0657 — wikidbs10k：見出し「id (mms)」（Wikidata の型 `string`）（35 列）
- 例1：XA1XY9 | XA5GG8 | XA0828 | XA4947 | XA0QT6（表：expressed in／同じ表の列：label, description, Foundational Model …, Terminologia Anatom…, Commons category, Freebase ID）
- 例2：XA78C0 | XA7XU8 | XA0828 | XA5R12 | XA8373（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Commons category, subclass of, Freebase ID）
- 例3：XA8EC5 | XA46Q2 | XA8PW4 | XA5766 | XA8373（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Foundational Model …, described by source, instance of）

## g0658 — wikidbs10k：見出し「label in sign language」（Wikidata の型 `string`）（35 列）
- 例1：Csc-agost-spreadthesign.ogv | Csc-desembre-spreadthesign.ogv | Csc-gener-spreadthesign.ogv | Csc-maig-spreadthesign.ogv | Csc-novembre-spreadthesign.ogv（表：calendar month／同じ表の列：label, description, page banner, image, OmegaWiki Defined M…, named after）
- 例2：Csc-abril-spreadthesign.ogv | Csc-maig-spreadthesign.ogv | Csc-març-spreadthesign.ogv | Csc-agost-spreadthesign.ogv | Csc-novembre-spreadthesign.ogv（表：followed by／同じ表の列：label, description, page banner, OmegaWiki Defined M…, named after, follows）
- 例3：Csc-setembre-spreadthesign.ogv | Csc-gener-spreadthesign.ogv | Csc-novembre-spreadthesign.ogv | Csc-juliol-spreadthesign.ogv | Csc-agost-spreadthesign.ogv（表：follows／同じ表の列：label, description, page banner, image, OmegaWiki Defined M…, named after）

## g0659 — wikidbs10k：見出し「oktmo id」（Wikidata の型 `string`）（35 列）
- 例1：11701000 | 78000000 | 92701000001.0 | 45000000.0 | 04701000（表：administrative territorial entity／同じ表の列：label, description, instance of, coat of arms image, flag, twinned administrat…）
- 例2：40360000 | 78701000001 | 40397000 | 92701000001 | 04701000001（表：capital city／同じ表の列：label, description, instance of, coat of arms image, flag, twinned administrat…）
- 例3：35715000001 | 35726000001 | 35718000001 | 35729000001 | 67000000（表：jurisdiction／同じ表の列：label, description, page banner, Commons category, country, coordinate location）

## g0660 — wikidbs10k：見出し「takes place in fictional universe」（Wikidata の型 `wikibase-entityid`）（35 列）
- 例1：Sly Cooper universe | Manhunt universe | The Last of Us universe | Adventure Time universe | The Powerpuff Girls universe（表：work／同じ表の列：label, description, instance of, publisher, genre, official website）
- 例2：Star Trek universe | Kelvin Timeline（表：work／同じ表の列：label, description, instance of, part of the series, characters, title）
- 例3：Marvel Cinematic Universe | Scooby Doo universe | Half-Life universe | Kingdom Hearts universe | Water Margin universe（表：work／同じ表の列：label, description, Freebase ID, instance of, country of origin, title）

## g0661 — wikidbs10k：見出し「catchphrase」（Wikidata の型 `monolingualtext`）（34 列）
- 例1：Kommunen med livskvalitet, det självkla… | I en liten kommun blir människan stor | I Ljusdal är det möjligt | En skön, grön ö / Din hälsa | Borås – of course（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）
- 例2：Ge idéerna plats | Ljuset vid Vättern | Kulturens övärld | The Capital of Scandinavia | Sveriges närmaste stad（表：political border／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）
- 例3：I en liten kommun blir människan stor | Sveriges geografiska centrum | Kulturens övärld | Lätt att leva | Rum för själen（表：jurisdiction／同じ表の列：label, description, located in the admi…, coat of arms image, shares border with, Commons category）

## g0662 — wikidbs10k：見出し「early modern letters online location id」（Wikidata の型 `string`）（34 列）
- 例1：b82db615-6917-4296-bb58-f6afca279bc5 | d9b29744-9a05-49d8-babd-7837aa09f998 | 7fd0970e-bae1-4865-bdbf-e993d1bfa883 | 8fd413e7-3c9a-4abf-806f-369d9e9869c2 | e22610af-1960-457a-aa5e-25d2fae97c05（表：headquarters／同じ表の列：label, description, twinned administrat…, page banner, country, Commons category）
- 例2：834b862c-67b9-44a9-bbf5-ea8738d6ac07 | b82db615-6917-4296-bb58-f6afca279bc5 | ae5440ad-0030-41ed-b2e3-c74d8b57d854 | 139dec04-c84a-403e-bf5b-57c9ab6c70e7 | 724a8a54-5982-49cd-a4f5-8f149017f44d（表：workplace／同じ表の列：label, description, page banner, Dewey Decimal Class…, twinned administrat…, country）
- 例3：688c9343-7208-41cb-8997-a4c2d3a429e6 | 4e7d0d7c-a13d-4322-8fc6-38913f845be3 | 766b9d1d-54aa-4e29-9f0b-2f480ab07a07 | 6384628b-5503-4282-93c9-7a079cb58b30 | 3b33aed2-40bc-48a9-baa0-3ff78ba4a5aa（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0663 — wikidbs10k：見出し「genedb id」（Wikidata の型 `string`）（34 列）
- 例1：PF3D7_1342900.1 | PF3D7_1456000.1 | PF3D7_1408200.1 | PF3D7_0802100.1 | PF3D7_1429200.1（表：Ethylene-responsive element binding pro…／同じ表の列：label, description, instance of, subclass of, UniProt protein ID, encoded by）
- 例2：PF3D7_1466400 | PF3D7_1107800 | PF3D7_0404100 | PF3D7_1222600 | PF3D7_1456000（表：encoded by／同じ表の列：label, description, instance of, subclass of, encodes, ortholog）
- 例3：PmUG01_11049400 | PRELSG_1438200 | PRCDC_0515900 | PGAL8A_00513500 | PRELSG_0936800（表：orthology／同じ表の列：label, description, instance of, subclass of, found in taxon, chromosome）

## g0664 — wikidbs10k：見出し「kit linked open numbers id」（Wikidata の型 `string`）（34 列）
- 例1：2465 | 280 | 341 | 9976 | 3400（表：octagonal number／同じ表の列：label, description, instance of, Commons category, numeric value, number of decimal d…）
- 例2：47 | 13 | 43 | 11 | 5（表：prime factor／同じ表の列：label, description, instance of, Commons category, numeric value, Unicode character）
- 例3：6 | 4101 | 3331 | 1501 | 766（表：centered pentagonal number／同じ表の列：label, description, instance of, Commons category, numeric value, number of decimal d…）

## g0665 — wikidbs10k：見出し「nis/ins code」（Wikidata の型 `string`）（34 列）
- 例1：41011 | 44021 | 62063 | 42004 | 53053（表：beginning／同じ表の列：label, description, image, located in the admi…, Commons category, country）
- 例2：83034 | 25072 | 92094B | 58001 | 21002（表：location or destination point／同じ表の列：label, description, Commons category, located in the admi…, coat of arms image, coordinate location）
- 例3：24094 | 64065 | 21004 | 25014 | 13017（表：political border／同じ表の列：label, description, topic's main catego…, image, country, located in the admi…）

## g0666 — wikidbs10k：見出し「epoch」（Wikidata の型 `wikibase-entityid`）（34 列）
- 例1：J2000.0（表：stellar association／同じ表の列：label, description, constellation, Commons category, catalog code, instance of）
- 例2：J2000.0（表：Polar／同じ表の列：label, description, constellation, catalog code, instance of, SIMBAD ID）
- 例3：J2000.0（表：substellar object／同じ表の列：label, description, instance of, constellation, SIMBAD ID, right ascension）

## g0667 — wikidbs10k：見出し「has grammatical mood」（Wikidata の型 `wikibase-entityid`）（34 列）
- 例1：subjunctive | indicative（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：indicative | subjunctive（表：language proficiency／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：indicative | subjunctive（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0668 — wikidbs10k：見出し「linguasphere code」（Wikidata の型 `string`）（33 列）
- 例1：41-AAA-a | 45-AAA-a | 52-ABA | 51-AAA-i | 12-AAC（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：41-AAA-a | 52-ACB-a | 52-ABA | 52-AAA-cc | 51-AAA-b（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例3：41-BAA-a | 53-AAA-ea | 51-AAA-i | 51-AAA-q | 51-AAA-b（表：language proficiency／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）

## g0669 — wikidbs10k：見出し「oclc control number」（Wikidata の型 `string`）（33 列）
- 例1：46655943 | 05585193 | 01586310 | 01532962 | 1606914（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：01784380 | 1482120 | 41916239 | 20379572 | 1532958（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：1536396 | 1532958 | 1606914 | 1569056 | 43473694（表：publishing／同じ表の列：label, description, instance of, Freebase ID, ISSN, ERA Journal ID）

## g0670 — wikidbs10k：見出し「pubchem substance id (sid)」（Wikidata の型 `string`）（33 列）
- 例1：47208354 | 47208382 | 47208399 | 47208340 | 47208419（表：keigairengyoto／同じ表の列：label, description, instance of, natural product of …, KEGG ID, subclass of）
- 例2：47208340 | 47208399 | 17398076 | 47208382 | 47208419（表：natural product／同じ表の列：label, description, instance of, natural product of …, KEGG ID, subclass of）
- 例3：47208434 | 47208354 | 47208390 | 47208403 | 47208395（表：goshakusan／同じ表の列：label, description, instance of, natural product of …, KEGG ID, subclass of）

## g0671 — wikidbs10k：見出し「racing-reference race id」（Wikidata の型 `string`）（33 列）
- 例1：2004_Toyota_Grand_Prix_of_Long_Beach/R | 2004_U.S._Bank_Presents_the_Cleveland_G… | 2004_Gran_Premio_Telmex_Tecate_Presente… | 2004_Molson_Indy_Toronto/R | 2004_Champ_Car_Grand_Prix_of_Portland/R（表：2004 Champ Car season／同じ表の列：label, description, sport, point in time, instance of, country）
- 例2：1976-02/W | 1976-10/W | 1976-12/W | 1976-27/W | 1976-21/W（表：1976 NASCAR Winston Cup Series／同じ表の列：label, description, sport, point in time, instance of, part of）
- 例3：1966-05/W | 1966-20/W | 1966-28/W | 1966-41/W | 1966-43/W（表：1966 NASCAR Grand National Series／同じ表の列：label, description, sport, point in time, instance of, part of）

## g0672 — wikidbs10k：見出し「connecting service」（Wikidata の型 `wikibase-entityid`）（33 列）
- 例1：Piccadilly line | TfL Rail | Elizabeth line | Romford to Upminster | Tower Gateway/Beckton service（表：Crossrail／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例2：Romford to Upminster | TfL Rail | District line | Elizabeth line | Bakerloo line（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例3：S1 (Hannover) | S4 (Hanover) | InterCityExpress | RE 1 | S2 (Hannover)（表：Hanover S-Bahn／同じ表の列：label, description, Commons category, country, image, coordinate location）

## g0673 — wikidbs10k：見出し「connects with」（Wikidata の型 `wikibase-entityid`）（33 列）
- 例1：Allerheiligentor | Friedberger Tor | Bockenheimer Anlage | Willy-Brandt-Platz | Opernplatz（表：Frankfurt city ring route／同じ表の列：label, description, Commons category, instance of, country, located in the admi…）
- 例2：Eschenheimer Tor | Lange Straße | Taunusanlage | Willy-Brandt-Platz | Untermainanlage（表：connects with／同じ表の列：label, description, instance of, country, located in the admi…, part of）
- 例3：Tōhoku Shinkansen | Nippō Main Line | San’yō Main Line | Sekihoku Main Line | Hokuriku Main Line（表：railway line／同じ表の列：label, description, Commons category, Freebase ID, track gauge, country）

## g0674 — wikidbs10k：見出し「historical region」（Wikidata の型 `wikibase-entityid`）（33 列）
- 例1：Moravia | Bohemia | Czech Silesia（表：administrative territorial entity／同じ表の列：label, description, image, postal code, country, coordinate location）
- 例2：Bohemia | Czech Silesia | Moravia（表：headquarters／同じ表の列：label, description, instance of, country, population, flag image）
- 例3：Silesia | Moravia | Czech Silesia | Bohemia（表：political border／同じ表の列：label, description, Commons category, located in the admi…, country, LAU）

## g0675 — wikidbs10k：見出し「quebec municipalities geographical code」（Wikidata の型 `string`）（32 列）
- 例1：1023.0 | 10060.0 | 73020.0 | 71040.0 | 31045.0（表：administrative territorial entity／同じ表の列：label, description, country, coordinate location, located in the admi…, instance of）
- 例2：58227 | 85045 | 37067 | 73010 | 17045（表：political border／同じ表の列：label, description, country, located in the admi…, coordinate location, instance of）
- 例3：95032.0 | 97007.0 | 57010.0 | 59010.0 | 29073.0（表：administrative territorial entity／同じ表の列：label, description, country, instance of, shares border with, located in the admi…）

## g0676 — wikidbs10k：見出し「reddit topic id」（Wikidata の型 `string`）（32 列）
- 例1：india | new_zealand | germany | brazil | spain（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：sweden | denmark | ukraine | spain | united_states_of_america（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：italy | germany | mexico | sweden | united_states_of_america（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0677 — wikidbs10k：見出し「edition or translation of」（Wikidata の型 `wikibase-entityid`）（32 列）
- 例1：The Juniper Tree | Rumplestiltskin | The Pack of Ragamuffins | The Mouse, the Bird, and the Sausage | Clever Elsie（表：Household stories from the collection o…／同じ表の列：label, description, instance of, author, translator, title）
- 例2：Rotkäppchen | The Dog and the Sparrow | The Wedding of Mrs. Fox | Rapunzel | Brother and Sister（表：followed by／同じ表の列：label, description, instance of, author, translator, title）
- 例3：Trusty John | The Hare's Bride | Little Briar Rose | The Six Swans | Rumplestiltskin（表：follows／同じ表の列：label, description, instance of, author, translator, title）

## g0678 — wikidbs10k：見出し「has subsidiary」（Wikidata の型 `wikibase-entityid`）（32 列）
- 例1：Jaipur railway division | Delhi railway division | Danapur railway division | Alipurduar railway division | Mumbai CR railway division（表：parent company／同じ表の列：label, description, instance of, country, reporting mark, official website）
- 例2：Biomedical Laboratory Research and Deve… | IRS Criminal Investigation | Federal Reserve Police | United States Postal Service Office of … | Walter Reed National Military Medical C…（表：parent company／同じ表の列：label, description, VIAF ID, Commons category, GND ID, topic's main catego…）
- 例3：Bureau of the Fiscal Service | Federal Emergency Management Agency | Office of Inspector General, Board of G… | United States Postal Service Office of … | IRS Criminal Investigation（表：organization／同じ表の列：label, description, VIAF ID, Commons category, GND ID, topic's main catego…）

## g0679 — wikidbs10k：見出し「declination」（Wikidata の型 `quantity`）（31 列）
- 例1：-66.9267 | +41.317 | -61.2607000 | -71.2500 | -66.3674139（表：stellar association／同じ表の列：label, description, constellation, Commons category, catalog code, instance of）
- 例2：+8.92085405857780 | +10.495250 | -57.63956422753850 | -5.45247673606210 | -25.73937933412028（表：Polar／同じ表の列：label, description, constellation, catalog code, instance of, SIMBAD ID）
- 例3：-16.87160917054750 | +1.3104667 | +20.86910679546083 | +17.89509606554777 | -2.61833（表：substellar object／同じ表の列：label, description, instance of, constellation, SIMBAD ID, right ascension）

## g0680 — wikidbs10k：見出し「right ascension」（Wikidata の型 `quantity`）（31 列）
- 例1：+81.8458 | +81.9333 | +87.2292 | +80.4250 | +84.2656958（表：stellar association／同じ表の列：label, description, constellation, Commons category, catalog code, instance of）
- 例2：+274.05522772574220 | +82.13615150332380 | +22.21893531746420 | +169.31634919216540 | +85.70333885637470（表：Polar／同じ表の列：label, description, constellation, catalog code, instance of, SIMBAD ID）
- 例3：+293.82779300 | +151.66991850367668 | +286.97141527970870 | +270.854000 | +221.527583（表：substellar object／同じ表の列：label, description, instance of, constellation, SIMBAD ID, declination）

## g0681 — wikidbs10k：見出し「coden」（Wikidata の型 `string`）（31 列）
- 例1：JPETAB | EHJODF | FJEOAC | JBCHA3 | NATUAS（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：ABBIA4 | PHMCEE | BBRCA9 | PNASA6 | EJCPAS（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：JONRA9 | DIAEAZ | JPETAB | MOENEN | BBRCA9（表：publishing／同じ表の列：label, description, instance of, Freebase ID, ISSN, ERA Journal ID）

## g0682 — wikidbs10k：見出し「eci lok sabha constituency code」（Wikidata の型 `string`）（31 列）
- 例1：S22-1 | S22-11 | S22-15 | S22-16 | S22-20（表：jurisdiction／同じ表の列：label, description, instance of, located in the admi…, has part(s), country）
- 例2：S12-17 | S12-26 | S12-7 | S12-20 | S12-28（表：jurisdiction／同じ表の列：label, description, located in the admi…, country, instance of, Freebase ID）
- 例3：S25-1 | S25-11 | S25-23 | S25-42 | S25-16（表：jurisdiction／同じ表の列：label, description, coordinate location, located in the admi…, country, instance of）

## g0683 — wikidbs10k：見出し「okato id」（Wikidata の型 `string`）（31 列）
- 例1：40280501.0 | 65436 | 65436000000.0 | 40000000000.0 | 78401000000.0（表：administrative territorial entity／同じ表の列：label, description, instance of, coat of arms image, flag, twinned administrat…）
- 例2：65436000000 | 40280501 | 45000000000 | 11401000000 | 78401000000（表：capital city／同じ表の列：label, description, instance of, coat of arms image, flag, twinned administrat…）
- 例3：65 | 92257 | 25 | 78 | 75（表：administrative territorial entity／同じ表の列：label, description, country, capital, shares border with, head of government）

## g0684 — wikidbs10k：見出し「os grid reference」（Wikidata の型 `string`）（31 列）
- 例1：NS485635 | NO115235 | NT275735 | NT511739 | NT5756（表：capital city／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）
- 例2：SH424765 | SH33197996 | SH5976277089 | SH353373 | SH3715690481（表：administrative territorial entity／同じ表の列：label, description, country, coordinate location, topic's main catego…, instance of）
- 例3：SH591482 | SH33197996 | SH6076 | SH3715690481 | SH353373（表：physical location／同じ表の列：label, description, country, coordinate location, topic's main catego…, instance of）

## g0685 — wikidbs10k：見出し「umls cui」（Wikidata の型 `string`）（31 列）
- 例1：C0014876 | C0018827 | C0018427 | C0001074 | C0018563（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Commons category, subclass of, Freebase ID）
- 例2：C0024109 | C0224440 | C0022378 | C0043425 | C0021853（表：expressed in／同じ表の列：label, description, Foundational Model …, UBERON ID, described by source, MeSH tree code）
- 例3：C0037857 | C0018787 | C0225706 | C0225870 | C0039597（表：expressed in／同じ表の列：label, description, instance of, UBERON ID, Foundational Model …, NCI Thesaurus ID）

## g0686 — wikidbs10k：見出し「track gauge」（Wikidata の型 `wikibase-entityid`）（31 列）
- 例1：1435 mm track gauge（表：railway line／同じ表の列：label, description, Commons category, country, instance of, located in the admi…）
- 例2：1676 mm track gauge | 5 ft 3 in gauge | 1067 mm track gauge | 1000 mm track gauge | 1435 mm track gauge（表：railway line／同じ表の列：label, description, country, instance of, Freebase ID, located in the admi…）
- 例3：1676 mm track gauge | 1435 mm track gauge（表：railway line／同じ表の列：label, description, country, located in the admi…, instance of, route number）

## g0687 — wikidbs10k：見出し「attendance」（Wikidata の型 `quantity`）（30 列）
- 例1：+50000 | +29500 | +16000 | +55000 | +12000（表：1976 NASCAR Winston Cup Series／同じ表の列：label, description, sport, point in time, instance of, part of）
- 例2：+45000 | +15000 | +90000 | +10000 | +46200（表：1966 NASCAR Grand National Series／同じ表の列：label, description, sport, point in time, instance of, part of）
- 例3：+60448 | +18812 | +63300 | +8507 | +52204（表：UEFA Euro 1972 qualifying Group 8／同じ表の列：label, description, Transfermarkt match…, instance of, participating team, referee）

## g0688 — wikidbs10k：見出し「national heritage list for england number」（Wikidata の型 `string`）（30 列）
- 例1：1375290 | 1058402 | 1394144 | 1031011 | 1297309（表：assembly room／同じ表の列：label, description, coordinate location, country, located in the admi…, heritage designation）
- 例2：1287355 | 1063686 | 1038424 | 1276887 | 1243561（表：buttercross／同じ表の列：label, description, coordinate location, country, heritage designation, instance of）
- 例3：1042387 | 1085770 | 1005210 | 1130885 | 1021183（表：quadrangular castle／同じ表の列：label, description, image, instance of, inception, country）

## g0689 — wikidbs10k：見出し「woeid」（Wikidata の型 `string`）（30 列）
- 例1：19344 | 19450 | 15127 | 18614 | 20440（表：capital city／同じ表の列：label, description, located in the admi…, instance of, GND ID, country）
- 例2：19450.0 | 18614.0 | 21228.0 | 27238.0 | 24502.0（表：capital city／同じ表の列：label, description, Commons category, coordinate location, country, located in the admi…）
- 例3：729337.0 | 727422.0 | 730399.0 | 731178.0 | 727151（表：political border／同じ表の列：label, description, Commons category, CBS municipality co…, country, flag image）

## g0690 — wikidbs10k：見出し「color」（Wikidata の型 `wikibase-entityid`）（30 列）
- 例1：green | blue | yellow | white | red（表：flag／同じ表の列：label, description, country, instance of, image, applies to jurisdic…）
- 例2：blue | yellow | grey | white | red（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, Pokémon index, part of, height）
- 例3：black and white | color（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）

## g0691 — wikidbs10k：見出し「field of work」（Wikidata の型 `wikibase-entityid`）（30 列）
- 例1：criminology | economics | chemistry | forensic anthropology | construction（表：Texas State University／同じ表の列：label, description, instance of, part of, official website）
- 例2：materials science | electrical engineering | bioengineering | industrial engineering | chemical engineering（表：University of Washington College of Eng…／同じ表の列：label, description, instance of, located in the admi…, country, part of）
- 例3：materials science | statistics | bioengineering | computer science | engineering（表：George R. Brown School of Engineering／同じ表の列：label, description, official website, country, located in the admi…, instance of）

## g0692 — wikidbs10k：見出し「number of matches played/races/starts」（Wikidata の型 `quantity`）（29 列）
- 例1：30 | 8 | 45 | 33 | 46（表：physical location／同じ表の列：label, description, Commons category, instance of, coordinate location, country）
- 例2：+36（表：part／同じ表の列：label, description, sport, sports season of le…, instance of, point in time）
- 例3：+240 | +306 | +380（表：event／同じ表の列：label, description, instance of, country, edition number, sport）

## g0693 — wikidbs10k：見出し「digdag id」（Wikidata の型 `string`）（29 列）
- 例1：121039 | 121028 | 120737 | 121023 | 120740（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例2：121038 | 121022 | 120732 | 120727 | 121011（表：political border／同じ表の列：label, description, capital, country, located in the admi…, Commons category）
- 例3：120787 | 120792 | 120798 | 120786 | 120782（表：West Zealand County／同じ表の列：label, description, coordinate location, country, Freebase ID, instance of）

## g0694 — wikidbs10k：見出し「musicbrainz release group id」（Wikidata の型 `string`）（29 列）
- 例1：0fc49bf9-a30c-44fa-8ca9-9b0d29742353 | 09f50b84-8630-303a-99f7-f82483feea0a | c5f46f6e-078d-379c-8de1-4fdb52a85f1d | 0a25ce41-a4f1-49ae-b5bc-fcd772cb7abd | c9a82cbb-2fe4-42bf-8934-130a6a18cf97（表：The Single File 1978~1983／同じ表の列：label, description, performer, instance of, publication date, Discogs master ID）
- 例2：a6fa8e8e-6f52-4479-8c07-5d91cd7dccf2 | dbec233e-a5e6-4d63-aba5-a98fa74ecc7d | aaf42f51-e28a-475a-bc8b-0651b5d5797a | a6007d36-8dca-3e2b-8ad6-a2528d45f481 | a9cf8289-effb-3bc8-b409-b2b291cf7965（表：Ornella Vanoni's albums in chronologica…／同じ表の列：label, description, instance of, performer, publication date, Discogs master ID）
- 例3：60c39751-22be-43f9-9cc7-a80e095466b1 | 6a7af514-9fe1-340f-848c-02e8b910d128 | dc472fed-2300-4a3d-9f5a-d43707eda0d6 | 6950d7ff-56e5-3e89-9b04-47bedc04c65d | 189cfbd5-21ec-3b20-85da-9cf965832ece（表：followed by／同じ表の列：label, description, instance of, performer, publication date, follows）

## g0695 — wikidbs10k：見出し「new zealand gazetteer place id」（Wikidata の型 `string`）（29 列）
- 例1：14997 | 15025 | 15008 | 58071 | 15006（表：district of New Zealand／同じ表の列：label, description, country, coordinate location, instance of, GeoNames ID）
- 例2：15033.0 | 15038 | 14966.0 | 14973 | 14972（表：administrative territorial entity／同じ表の列：label, description, population, GeoNames ID, category of associa…, MusicBrainz area ID）
- 例3：14997.0 | 15034.0 | 14998.0 | 14966.0 | 15010.0（表：political border／同じ表の列：label, description, locator map image, country, coordinate location, located in the admi…）

## g0696 — wikidbs10k：見出し「swiss municipality code」（Wikidata の型 `string`）（29 列）
- 例1：2765.0 | 3851.0 | 6253.0 | 5192.0 | 4095.0（表：location or destination point／同じ表の列：label, description, country, instance of, located in the admi…, Commons category）
- 例2：6253 | 4323 | 2765 | 0261 | 4095（表：beginning／同じ表の列：label, description, country, located in the admi…, coat of arms image, Commons category）
- 例3：1605 | 1603 | 1626 | 1628 | 1606（表：physical location／同じ表の列：label, description, Commons category, locator map image, postal code, located in time zone）

## g0697 — wikidbs10k：見出し「whatdotheyknow organisation id」（Wikidata の型 `string`）（29 列）
- 例1：hmp_canterbury_imb | hmp_rochester_imb | hmp_askham_grange_imb | hmp_dartmoor_imb | hmp_cardiff_imb（表：Independent Monitoring Board／同じ表の列：label, description, instance of, country, official website, inception）
- 例2：hmp_wealstun_imb | hmp_bristol_imb | hmp_lancaster_farms_imb | hmp_sudbury_imb | hmp_kirklevington_grange_imb（表：governing body／同じ表の列：label, description, instance of, country, official website, inception）
- 例3：leeds_city_council | cheshire_west_and_chester_council | broomhaugh_and_riding_parish_council | penarth_town_council | brading_town_council（表：governing body／同じ表の列：label, description, instance of, country, applies to jurisdic…, official website）

## g0698 — wikidbs10k：見出し「czech registration id」（Wikidata の型 `string`）（28 列）
- 例1：06680003 | 03299309 | 03421970 | 27242617 | 65413261（表：non-bank consumer credit provider／同じ表の列：label, description, instance of, headquarters locati…, country, legal form）
- 例2：00262978 | 00290629 | 00238295 | 00299308 | 00244732（表：headquarters／同じ表の列：label, description, instance of, country, population, flag image）
- 例3：00297488 | 581852.0 | 241041.0 | 48527459.0 | 572594.0（表：political border／同じ表の列：label, description, Commons category, located in the admi…, country, LAU）

## g0699 — wikidbs10k：見出し「external data available at」（Wikidata の型 `string`）（28 列）
- 例1：https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni…（表：location or destination point／同じ表の列：label, description, country, instance of, located in the admi…, Commons category）
- 例2：https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni…（表：beginning／同じ表の列：label, description, country, located in the admi…, coat of arms image, Commons category）
- 例3：https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni… | https://ld.geo.admin.ch/boundaries/muni…（表：administrative territorial entity／同じ表の列：label, description, country, instance of, located in the admi…, Commons category）

## g0700 — wikidbs10k：見出し「famous birthdays id」（Wikidata の型 `string`）（28 列）
- 例1：october7 | march19 | november30 | august15 | january17（表：feast day／同じ表の列：label, description, Commons category, instance of, part of, Commons gallery）
- 例2：year/2007 | year/2005 | year/2002 | year/2008 | year/2009（表：2000s／同じ表の列：label, description, Commons category, instance of, part of, follows）
- 例3：year/2007 | year/2004 | year/2003 | year/2010 | year/2002（表：followed by／同じ表の列：label, description, Commons category, instance of, part of, follows）

## g0701 — wikidbs10k：見出し「isds id」（Wikidata の型 `string`）（28 列）
- 例1：b753awp | 55zk83u | qvbee6f | 7rn826m | x3cv8at（表：non-bank consumer credit provider／同じ表の列：label, description, instance of, headquarters locati…, country, Czech Registration …）
- 例2：ukzbx4z | a7kbrrn | tkvbdnm | kjgb4yx | 2gubtq5（表：headquarters／同じ表の列：label, description, instance of, country, population, flag image）
- 例3：7zhb6tn | 6qqb5u2 | u3kbfuf | nbzajvm | zqhaskc（表：political border／同じ表の列：label, description, Commons category, located in the admi…, country, LAU）

## g0702 — wikidbs10k：見出し「pokémon index」（Wikidata の型 `string`）（28 列）
- 例1：299 | 878 | 713 | 563 | 478（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, part of, height, color）
- 例2：556 | 182 | 547 | 548 | 708（表：Grass egg group／同じ表の列：label, description, part of, from narrative univ…, instance of, height）
- 例3：756 | 670 | 547 | 861 | 788（表：fairy-type Pokémon／同じ表の列：label, description, instance of, part of, from narrative univ…, Bulbapedia article …）

## g0703 — wikidbs10k：見出し「simbad id」（Wikidata の型 `string`）（28 列）
- 例1：NGC 1869 | NGC 1955 | NAME beta Pic Moving Group | NGC 2001 | NGC 1937（表：stellar association／同じ表の列：label, description, constellation, Commons category, catalog code, instance of）
- 例2：MACHO 154.29038.66 | CRTS J081030.6+002429 | V* AI Tri | CRTS J032855.0+052253 | V* V1309 Ori（表：Polar／同じ表の列：label, description, constellation, catalog code, instance of, right ascension）
- 例3：EWS 2011-BLG-203 | HD 87646b | ROTSE3 J160213.1-021311.7 | TVLM 213-56230 | NAME BD+46 2629Ab（表：substellar object／同じ表の列：label, description, instance of, constellation, right ascension, declination）

## g0704 — wikidbs10k：見出し「wdpa id」（Wikidata の型 `string`）（28 列）
- 例1：388965 | 555545787 | 555545798 | 555545795 | 388962（表：habitats or species management protecte…／同じ表の列：label, description, country, instance of, area, IUCN protected area…）
- 例2：371072 | 371941 | 22484 | 3056 | 1008（表：national preserve／同じ表の列：label, description, Commons category, located in the admi…, IUCN protected area…, instance of）
- 例3：555550111 | 342043 | 342078 | 342097 | 342052（表：national nature reserve／同じ表の列：label, description, instance of, Commons category, ÚSOP code, country）

## g0705 — wikidbs10k：見出し「constellation」（Wikidata の型 `wikibase-entityid`）（28 列）
- 例1：Centaurus | Ursa Major | Monoceros | Sagittarius | Mensa（表：stellar association／同じ表の列：label, description, Commons category, catalog code, instance of, image）
- 例2：Hercules | Hydra | Lyra | Cetus | Libra（表：Polar／同じ表の列：label, description, catalog code, instance of, SIMBAD ID, right ascension）
- 例3：Aquarius | Orion | Leo | Libra | Puppis（表：substellar object／同じ表の列：label, description, instance of, SIMBAD ID, right ascension, declination）

## g0706 — wikidbs10k：見出し「day of week」（Wikidata の型 `wikibase-entityid`）（28 列）
- 例1：Sunday（表：feast day／同じ表の列：label, description, Commons category, instance of, part of, Commons gallery）
- 例2：Monday（表：first Monday of the month／同じ表の列：label, description, instance of, subclass of, month of the year）
- 例3：Sunday | Monday（表：recurring entity／同じ表の列：label, description, instance of, subclass of）

## g0707 — wikidbs10k：見出し「discogs master id」（Wikidata の型 `string`）（27 列）
- 例1：332806 | 28552 | 751163 | 28601 | 28560（表：The Single File 1978~1983／同じ表の列：label, description, performer, instance of, MusicBrainz release…, publication date）
- 例2：399031 | 480789 | 528466 | 706088 | 530063（表：Ornella Vanoni's albums in chronologica…／同じ表の列：label, description, MusicBrainz release…, instance of, performer, publication date）
- 例3：291171 | 264633 | 1046970 | 1046968 | 304718（表：Glen Campbell US albums discography／同じ表の列：label, description, MusicBrainz release…, instance of, AllMusic album ID, title）

## g0708 — wikidbs10k：見出し「iso 4 abbreviation」（Wikidata の型 `string`）（27 列）
- 例1：J. Biol. Chem. | Eur. Heart J. | Nature | FEBS J. | Biochem. J.（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：Eur. J. Clin. Pharmacol. | Drug Metab. Dispos. | J. Biol. Chem. | Arch. Biochem. Biophys. | Chem. Res. Toxicol.（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：Neurosci. Lett. | EMBO J. | Mol. Cell. Biol. | Biochem. Biophys. Res. Commun. | J. Membr. Biol.（表：publishing／同じ表の列：label, description, publisher, instance of, official website, Freebase ID）

## g0709 — wikidbs10k：見出し「omim id」（Wikidata の型 `string`）（27 列）
- 例1：131550 | 176872 | 164757 | 173490 | 608537（表：biological variant of／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）
- 例2：613693 | 616247 | 613695 | 220400 | 601005（表：long QT syndrome／同じ表の列：label, description, subclass of, instance of, health specialty, Disease Ontology ID）
- 例3：604001 | 114180 | 600734 | 114182 | 114205（表：genetic association／同じ表の列：label, description, Entrez Gene ID, HGNC gene symbol, HGNC ID, subclass of）

## g0710 — wikidbs10k：見出し「vision of britain unit id」（Wikidata の型 `string`）（27 列）
- 例1：10398939.0 | 10284977 | 10400727.0 | 10148194.0 | 10067080.0（表：administrative territorial entity／同じ表の列：label, description, instance of, located in the admi…, GeoNames ID, GSS code (2011)）
- 例2：10171003 | 10316923 | 10289075 | 10013240 | 10018961（表：jurisdiction／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：10360717.0 | 10360109.0 | 10359557.0 | 10362106.0 | 10358875.0（表：capital city／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）

## g0711 — wikidbs10k：見出し「is the study of」（Wikidata の型 `wikibase-entityid`）（27 列）
- 例1：Czech | Estonian | Polish | Bulgarian | Ukrainian（表：academic discipline／同じ表の列：label, description, subclass of, instance of）
- 例2：human behavior | astronomical object | society | mathematical object | ecological concept（表：facet of／同じ表の列：label, description, OmegaWiki Defined M…, BNCF Thesaurus ID, Commons category, image）
- 例3：society | technique | mathematical object | condition | chemical compound（表：academic discipline／同じ表の列：label, description, OmegaWiki Defined M…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）

## g0712 — wikidbs10k：見出し「iucn protected areas category」（Wikidata の型 `wikibase-entityid`）（27 列）
- 例1：IUCN category IV: Habitat/Species Manag…（表：habitats or species management protecte…／同じ表の列：label, description, country, instance of, area, official name）
- 例2：IUCN category V: Protected Landscape/Se… | IUCN category II: National Park | IUCN category III: Natural Monument or …（表：national preserve／同じ表の列：label, description, Commons category, located in the admi…, instance of, Freebase ID）
- 例3：IUCN category IV: Habitat/Species Manag… | IUCN category III: Natural Monument or … | IUCN category Ib: Wilderness Area | IUCN category Ia: Strict Nature Reserve（表：national nature reserve／同じ表の列：label, description, instance of, Commons category, ÚSOP code, country）

## g0713 — wikidbs10k：見出し「season」（Wikidata の型 `wikibase-entityid`）（27 列）
- 例1：Teenage Mutant Ninja Turtles (1987 TV s… | Maybrit Illner, season 21 | Markus Lanz, season 12 | The Mentalist, season 3 | Shameless, season 1（表：season finale／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例2：Mord mit Aussicht, season 3 | Grey's Anatomy, season 9 | NCIS, season 15 | Nix Festes, season 2 | The 100, season 4（表：followed by／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例3：Grey's Anatomy, season 17 | Shameless, season 9 | Maybrit Illner, season 21 | The Vampire Diaries, season 6 | 30 Rock, season 3（表：follows／同じ表の列：label, description, instance of, part of the series, follows, followed by）

## g0714 — wikidbs10k：見出し「vessel class」（Wikidata の型 `wikibase-entityid`）（27 列）
- 例1：Mackenzie-class destroyer | River-class frigate | Tribal-class destroyer | Oberon-class submarine | Annapolis-class destroyer（表：His Majesty's Canadian Ship／同じ表の列：label, description, instance of, image, operator, military branch）
- 例2：German Type VIIC submarine | Type XXI submarine | German Type IID submarine | Type IXC/40 submarine | German Type VII C/41 submarine（表：31st U-boat Flotilla／同じ表の列：label, description, operator, instance of, conflict, location of creation）
- 例3：Helgoland-class battleship | Nassau-class battleship | Courbet-class battleship | Andrea Doria-class battleship | Conte di Cavour-class battleship（表：dreadnought／同じ表の列：label, description, Commons category, instance of, Freebase ID, image）

## g0715 — wikidbs10k：見出し「apparent magnitude」（Wikidata の型 `quantity`）（26 列）
- 例1：-2.94 | -4.8 | +15.1 | -12.747 | +11.8（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, image）
- 例2：+14.53 | +19.01 | +17.538 | +17.0 | +19.66（表：Polar／同じ表の列：label, description, constellation, catalog code, instance of, SIMBAD ID）
- 例3：+5.55 | +14.7239 | +8.76 | +15.4 | +8.25（表：primary body／同じ表の列：label, description, constellation, instance of, catalog code, SIMBAD ID）

## g0716 — wikidbs10k：見出し「number of platform tracks」（Wikidata の型 `quantity`）（26 列）
- 例1：+5 | +9 | +4 | +2 | +1（表：Hanover S-Bahn／同じ表の列：label, description, Commons category, country, image, coordinate location）
- 例2：+3 | +1 | +4 | +9 | +12（表：adjacent station／同じ表の列：label, description, Commons category, instance of, country, coordinate location）
- 例3：+7 | +2 | +1 | +5 | +3（表：Praha–Vrané nad Vltavou–Čerčany Dobříš …／同じ表の列：label, description, Commons category, country, instance of, coordinate location）

## g0717 — wikidbs10k：見出し「commons institution page」（Wikidata の型 `string`）（26 列）
- 例1：Diputación Provincial de Almería | Diputación Provincial de Huelva | Deputación Provincial de Pontevedra | Diputación Provincial of Ciudad Real | Diputación Provincial de Córdoba（表：executive branch／同じ表の列：label, description, instance of, inception, headquarters locati…, official website）
- 例2：Duomo, Pistoia | Museo Civico e Diocesano d'Arte Sacra, … | Società di Esecutori di Pie Disposizion… | San Domenico, Arezzo | Ognissanti, Florence（表：collection／同じ表の列：label, description, Commons category, instance of, image, country）
- 例3：Convent of Fuligno, Florence | Galleria dell'Accademia (Florence) | Loggia del Bigallo, Florence | Minneapolis Institute of Art | Museo di Arte Sacra, San Casciano in Va…（表：has works in the collection／同じ表の列：label, description, official website, Commons category, instance of, image）

## g0718 — wikidbs10k：見出し「dyntaxa id」（Wikidata の型 `string`）（26 列）
- 例1：6011365 | 1006421 | 2002417 | 220442 | 1006087（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：2002525 | 2002476 | 1001192 | 2003508 | 1001126（表：taxon／同じ表の列：label, description, MycoBank taxon name…, Encyclopedia of Lif…, taxon rank, taxon name）
- 例3：3035.0 | 3475.0 | 4937.0 | 4723.0 | 2979.0（表：secretion or excretion／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g0719 — wikidbs10k：見出し「wormbase gene id」（Wikidata の型 `string`）（26 列）
- 例1：WBGene00005589 | WBGene00005536 | WBGene00005528 | WBGene00005539 | WBGene00005577（表：encoded by／同じ表の列：label, description, found in taxon, NCBI locus tag, Entrez Gene ID, genomic end）
- 例2：WBGene00005938 | WBGene00005907 | WBGene00005937 | WBGene00005917 | WBGene00005958（表：encoded by／同じ表の列：label, description, Ensembl gene ID, Ensembl transcript …, RefSeq RNA ID, Entrez Gene ID）
- 例3：WBGene00009312 | WBGene00021565 | WBGene00009614 | WBGene00021298 | WBGene00011783（表：encoded by／同じ表の列：label, description, found in taxon, NCBI locus tag, Entrez Gene ID, chromosome）

## g0720 — wikidbs10k：見出し「based on」（Wikidata の型 `wikibase-entityid`）（26 列）
- 例1：Star Trek: The Original Series | Star Trek is... | Star Trek | Star Trek: The Next Generation（表：series／同じ表の列：label, description, instance of, takes place in fict…, media franchise, genre）
- 例2：Cessna 310C | Cessna 310J | Cessna 310I | Cessna 310B | Cessna 310L（表：Cessna 310 320／同じ表の列：label, description, instance of, subclass of, total produced）
- 例3：Cessna 310K | Cessna 310C | Cessna 310H | Cessna 310F | Cessna 310（表：based on／同じ表の列：label, description, instance of, subclass of, total produced）

## g0721 — wikidbs10k：見出し「this taxon is source of」（Wikidata の型 `wikibase-entityid`）（26 列）
- 例1：melon | globe artichoke | garlic | iceberg lettuce | Saccharum Granorum（表：secretion or excretion／同じ表の列：label, description, taxon name, taxon rank, parent taxon, instance of）
- 例2：Scutellariae Radix | liquorice root | Phellodendri Cortex | Schizonepetae Spica | Aurantii Fructus Immaturus（表：secretion or excretion／同じ表の列：label, description, Commons category, image, taxon name, taxon rank）
- 例3：ginger | Cinnamomi Cortex | Ephedrae Herba | Atractylodis Lanceae Rhizoma | Angelicae Radix（表：secretion or excretion／同じ表の列：label, description, Commons category, image, taxon name, taxon rank）

## g0722 — wikidbs10k：見出し「prize money」（Wikidata の型 `quantity`）（25 列）
- 例1：+66250 | +35000 | +30000 | +25000 | +50000（表：1972 Grand Prix circuit／同じ表の列：label, description, sport, instance of, point in time, country）
- 例2：+320000 | +118600 | +60000 | +100000（表：1976 World Championship Tennis circuit／同じ表の列：label, description, sport, instance of, point in time, located in the admi…）
- 例3：+85000 | +50000 | +93400 | +75000 | +100000（表：Lorraine Open／同じ表の列：label, description, country, sport, instance of, point in time）

## g0723 — wikidbs10k：見出し「water area」（Wikidata の型 `quantity`）（25 列）
- 例1：0.035506 | 0.041137 | 0.098696 | 1.169598 | 0.396406（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, country, instance of, Commons category）
- 例2：0.0 | 0.7884 | 0.035506 | 0.135748 | 0.295199（表：capital city／同じ表の列：label, description, Dewey Decimal Class…, country, instance of, Commons category）
- 例3：0.22299899999999998 | 0.184501 | 0.167924 | 0.197204 | 2.9318（表：capital city／同じ表の列：label, description, country, instance of, coordinate location, Commons category）

## g0724 — wikidbs10k：見出し「width」（Wikidata の型 `quantity`）（25 列）
- 例1：+17.5 | +7.8 | +16 | +0.32 | +6.7（表：landform／同じ表の列：label, description, Dewey Decimal Class…, Commons category, instance of, coordinate location）
- 例2：+103.0 | +102.7 | +101.2 | +101.8 | +101.6（表：Windsor Beauties／同じ表の列：label, description, inventory number, collection, instance of, location）
- 例3：+101.0 | +101.3 | +123.5 | +102.7 | +101.6（表：depicting object／同じ表の列：label, description, inventory number, collection, instance of, location）

## g0725 — wikidbs10k：見出し「african plant database id」（Wikidata の型 `string`）（25 列）
- 例1：189826 | 194953 | 187948 | 27247 | 191667（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：188253 | 189827 | 191887 | 193634 | 191690（表：taxon／同じ表の列：label, description, taxon name, Commons category, taxon rank, image）
- 例3：190995 | 189958 | 188625 | 192667 | 191674（表：taxon／同じ表の列：label, description, taxon rank, Commons category, image, parent taxon）

## g0726 — wikidbs10k：見出し「gns unique feature id」（Wikidata の型 `string`）（25 列）
- 例1：10723924 | -235720 | -238525 | -242038 | 10724427（表：replacing subject／同じ表の列：label, description, Commons category, dantai code, country, located in the admi…）
- 例2：10724438 | -248499 | -225483 | -246526 | -236032（表：located in the present-day administrati…／同じ表の列：label, description, Commons category, dantai code, country, located in the admi…）
- 例3：-231558.0 | -226599.0 | -226439.0 | -233906.0 | -247050.0（表：administrative territorial entity／同じ表の列：label, description, BabelNet ID, office held by head…, native label, MusicBrainz area ID）

## g0727 — wikidbs10k：見出し「judoinside competition id」（Wikidata の型 `string`）（25 列）
- 例1：14180 | 5793 | 5903 | 5238 | 5228（表：Pan American Judo Championships／同じ表の列：label, description, sport, instance of, sports season of le…, point in time）
- 例2：9347 | 5239 | 5233 | 1063 | 11143（表：followed by／同じ表の列：label, description, sport, instance of, sports season of le…, point in time）
- 例3：9881 | 14180 | 1455 | 5228 | 4410（表：follows／同じ表の列：label, description, sport, instance of, sports season of le…, point in time）

## g0728 — wikidbs10k：見出し「libris-uri」（Wikidata の型 `string`）（25 列）
- 例1：wt798x9f33sdv3p | 53hkj6mp5hgzjd3 | khwzxm2321g72mt | sq466dbb4qsk383 | mkz10nf529zbmt7（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, Libraries Australia…, coordinates of sout…）
- 例2：0xbddljj0wdngtx | 97mpn0ft3gmr61w | khwzxm2321g72mt | xv8b9vvg52nbbxp | nl0229c6538hjvc（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：wt798n7f3w1qqfn | 31fhhm1m1z54n3r | 31fhhmzm02pf7xc | khwzxx6325m2b1c | 31fhgh3m0gvmt0n（表：administrative territorial entity／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）

## g0729 — wikidbs10k：見出し「mgi gene symbol」（Wikidata の型 `string`）（25 列）
- 例1：Kit | Map2k1 | Erbb2 | Alk | Dpyd（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例2：Egfr | Mlh1 | Pdgfra | Map2k1 | Kit（表：encoded by／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例3：Cav3 | Cacna1c | Kcne2 | Scn4b | Scn5a（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）

## g0730 — wikidbs10k：見出し「sports-reference.com college basketball box score id」（Wikidata の型 `string`）（25 列）
- 例1：1989-03-23-indiana | 1989-03-17-creighton | 1989-03-17-notre-dame | 1989-03-19-michigan | 1989-03-17-georgetown（表：1989 NCAA Men's Division I Basketball T…／同じ表の列：label, description, sport, point in time, league, participating team）
- 例2：1991-03-17-arizona-state | 1991-03-15-depaul | 1991-03-15-alabama | 1991-03-14-florida-state | 1991-04-01-duke（表：1991 NCAA Men's Division I Basketball T…／同じ表の列：label, description, sport, point in time, league, participating team）
- 例3：1965-03-08-connecticut | 1965-03-12-north-carolina-state | 1965-03-20-michigan | 1965-03-12-oklahoma-city | 1965-03-08-providence（表：1965 NCAA Men's Division I Basketball T…／同じ表の列：label, description, location, sport, point in time, participating team）

## g0731 — wikidbs10k：見出し「tabular case data」（Wikidata の型 `string`）（25 列）
- 例1：Data:COVID-19 (STCenter)/US/Q111859.tab | Data:COVID-19 (STCenter)/US/Q111913.tab | Data:COVID-19 (STCenter)/US/Q240621.tab | Data:COVID-19 (STCenter)/US/Q485448.tab | Data:COVID-19 (STCenter)/US/Q485795.tab（表：2020 COVID-19 pandemic in Iowa／同じ表の列：label, description, location, country, part of, instance of）
- 例2：Data:COVID-19/Cases/CA.tab | Data:COVID-19 (STCenter)/QA/Q846.tab | Data:COVID-19 (STCenter)/US/Q1408.tab | Data:COVID-19 (STCenter)/PL/Q36.tab | Data:COVID-19 (STCenter)/ET/Q115.tab（表：cause／同じ表の列：label, description, part of, country, location, coordinate location）
- 例3：Data:COVID-19 (STCenter)/US/Q495201.tab | Data:COVID-19 (STCenter)/US/Q495629.tab | Data:COVID-19 (STCenter)/US/Q491702.tab | Data:COVID-19 (STCenter)/US/Q495216.tab | Data:COVID-19 (STCenter)/US/Q489273.tab（表：2020 COVID-19 pandemic in South Dakota／同じ表の列：label, description, location, country, part of, instance of）

## g0732 — wikidbs10k：見出し「brazilian electoral unit id」（Wikidata の型 `string`）（24 列）
- 例1：45993 | 56138 | 56065 | 56910 | 41238（表：jurisdiction／同じ表の列：label, description, located in the admi…, country, instance of, Commons category）
- 例2：56456 | 56499 | 33472 | 56774 | 56995（表：political border／同じ表の列：label, description, country, coordinate location, Commons category, Freebase ID）
- 例3：93017 | 93297 | 61220 | 49212 | 51330（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, GeoNames ID, instance of）

## g0733 — wikidbs10k：見出し「brazilian municipality code」（Wikidata の型 `string`）（24 列）
- 例1：3203346 | 3549904 | 3105608 | 2313302 | 3204807（表：jurisdiction／同じ表の列：label, description, located in the admi…, country, instance of, Commons category）
- 例2：3203056 | 3205150 | 3200136 | 3200201 | 3200409（表：political border／同じ表の列：label, description, country, coordinate location, Commons category, Freebase ID）
- 例3：3130101 | 3146107 | 3109006 | 3157203 | 3118007（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, GeoNames ID, instance of）

## g0734 — wikidbs10k：見出し「collage image」（Wikidata の型 `string`）（24 列）
- 例1：Changhua County Montage.png | Taitung County Montage.png | Nantou County Montage.png | Pingtung County Montage.png | Yilan County Montage.png（表：administrative territorial entity／同じ表の列：label, description, category for people…, country, Commons category, instance of）
- 例2：MonterreyCollage.jpg | Collage of Landmarks in Richmond, Virgi… | Dallas Collage Montage.png | Philadelphia Montage by Jleon 0310.jpg | Denver Montage.jpg（表：administrative territorial entity／同じ表の列：label, description, coordinate location, instance of, head of government, postal code）
- 例3：Oklahoma City montage.png | JXFL2011N.png | MilwaukeeCollage 2.png | StLouisMontage.jpg | SanJose Infobox Pic Montage.jpg（表：physical location／同じ表の列：label, description, population, GND ID, instance of, country）

## g0735 — wikidbs10k：見出し「data commons id」（Wikidata の型 `string`）（24 列）
- 例1：country/JPN | country/ITA | country/GBR | country/DEU | country/BEL（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：country/UKR | country/NOR | country/CMR | country/USA | country/CHN（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, category for films …, GND ID）
- 例3：country/GBR | country/CHE | country/POL | country/CHN | country/ITA（表：country／同じ表の列：label, description, Great Russian Encyc…, WIPO ST.3, population, Getty Thesaurus of …）

## g0736 — wikidbs10k：見出し「mouse genome informatics id」（Wikidata の型 `string`）（24 列）
- 例1：MGI:1346866 | MGI:96677 | MGI:88190 | MGI:95410 | MGI:101938（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例2：MGI:95410 | MGI:97530 | MGI:1346866 | MGI:88190 | MGI:101938（表：encoded by／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例3：MGI:104744 | MGI:98251 | MGI:2687406 | MGI:96673 | MGI:103013（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）

## g0737 — wikidbs10k：見出し「genetic association」（Wikidata の型 `wikibase-entityid`）（24 列）
- 例1：neuroblastoma, susceptibility to, 3 | glioma | phaeochromocytoma | colorectal cancer | Mismatch repair cancer syndrome（表：biological variant of／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）
- 例2：KCNH2 | CACNA1C | AKAP9 | SNTA1 | KCNE1（表：long QT syndrome／同じ表の列：label, description, subclass of, OMIM ID, instance of, health specialty）
- 例3：long QT syndrome 3 | long QT syndrome | long QT syndrome 12 | schizophrenia | short QT syndrome（表：genetic association／同じ表の列：label, description, Entrez Gene ID, HGNC gene symbol, HGNC ID, OMIM ID）

## g0738 — wikidbs10k：見出し「occupant」（Wikidata の型 `wikibase-entityid`）（24 列）
- 例1：Colorado Buffaloes women's basketball | Oregon State Beavers | Peoria Rivermen | Penn State Nittany Lions basketball | Philadelphia Flyers（表：stadium／同じ表の列：label, description, instance of, coordinate location, country, located in the admi…）
- 例2：Córdoba City Hall | Ateca City Council | València City Hall | Soria City council | Ayuntamiento de Cartagena（表：headquarters／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：human | Slash | Evil Turtles（表：fictional location／同じ表の列：label, description, instance of, from narrative univ…, Fandom article ID, media franchise）

## g0739 — wikidbs10k：見出し「presenter」（Wikidata の型 `wikibase-entityid`）（24 列）
- 例1：Carrie Crowley | Anke Engelke | Denise Fabre | Maria Menounos | Mirjam Weichselbraun（表：event／同じ表の列：label, description, winner, participant, Commons category, topic's main catego…）
- 例2：Stefan Raab（表：Bundesvision Song Contest／同じ表の列：label, description, instance of, country of origin, point in time, follows）
- 例3：Stefan Raab（表：follows／同じ表の列：label, description, instance of, country of origin, point in time, follows）

## g0740 — wikidbs10k：見出し「highest break」（Wikidata の型 `quantity`）（23 列）
- 例1：+140 | +103 | +136 | +142 | +129（表：World Snooker Championship／同じ表の列：label, description, Freebase ID, instance of, location, winner）
- 例2：133.0 | 143.0 | 128.0 | 129.0 | 115.0（表：followed by／同じ表の列：label, description, Freebase ID, instance of, location, winner）
- 例3：129.0 | 141.0 | 46.0 | 101.0 | 108.0（表：follows／同じ表の列：label, description, Freebase ID, instance of, location, winner）

## g0741 — wikidbs10k：見出し「orbital inclination」（Wikidata の型 `quantity`）（23 列）
- 例1：+11.041 | +29.4529 | +38.07519 | +13.333 | +23.9（表：possible dwarf planet／同じ表の列：label, description, discoverer or inven…, instance of, orbital eccentricity, Minor Planet Center…）
- 例2：+129.812 | +0.009 | +3.39467605 | +26.04 | +17.14001206（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, image）
- 例3：+51.64 | 51.65 | 51.6 | 51.57 | 51.64（表：vessel／同じ表の列：label, description, Commons category, instance of, image, Freebase ID）

## g0742 — wikidbs10k：見出し「australian statistical geography 2011 id」（Wikidata の型 `string`）（23 列）
- 例1：3 | UCL802001 | 2 | 5 | 6（表：topic／同じ表の列：label, description, Commons category, flag image, coat of arms image, VIAF ID）
- 例2：3 | 6 | 7 | 5 | 8（表：administrative territorial entity／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）
- 例3：5 | 1 | LGA11400 | 4 | ILOC90300101（表：administrative territorial entity／同じ表の列：label, description, locator map image, country, capital, Commons category）

## g0743 — wikidbs10k：見出し「australian statistical geography 2016 id」（Wikidata の型 `string`）（23 列）
- 例1：5 | 3 | 1 | 6 | 2（表：topic／同じ表の列：label, description, Commons category, flag image, coat of arms image, VIAF ID）
- 例2：4 | 8 | 2 | 7 | 5（表：administrative territorial entity／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）
- 例3：LGA11400 | 7 | 8 | LGA58330 | 2（表：administrative territorial entity／同じ表の列：label, description, locator map image, country, capital, Commons category）

## g0744 — wikidbs10k：見出し「musicbrainz work id」（Wikidata の型 `string`）（23 列）
- 例1：35e427cf-96c2-35f9-878f-c9f8befe067b | bca058b4-fbca-37e6-89ba-b1cabdda4292 | 4082df8a-5962-3dec-81fc-84c89e303f36 | a1e640cc-d0e5-3402-9417-2001f57206c3 | 1fb957ca-feca-3b3d-a665-07336c3aa794（表：audio recording／同じ表の列：label, description, instance of, title, language of work or…, composer）
- 例2：f379a627-0415-38de-ab4c-bd23b4eef493 | 4919c776-e2e8-32b4-83de-0ed63fff912e | ed115452-eaf0-3844-b090-7e57eb5d80c0 | 92825287-3cc3-3dd4-8635-35fa457a45b8 | 8c26c2a2-755f-4305-83ee-50189e5dbfcd（表：anthem／同じ表の列：label, description, instance of, Commons category, Freebase ID, country）
- 例3：74fdb581-6197-405d-8833-0109a98f38bf | eea70810-5b5d-408c-a169-9ece28098a57 | 5732ceeb-027e-4353-9460-e284d12591b6 | e699d5fa-17ab-4a20-a75b-3e377f9327fe | 7db37810-1e8f-4191-9388-dab90e62d736（表：Hamilton／同じ表の列：label, description, instance of, part of, performer, follows）

## g0745 — wikidbs10k：見出し「soato id」（Wikidata の型 `string`）（23 列）
- 例1：3210000000 | 1240000000 | 1258000000 | 6225000000 | 4233000000（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, Commons category, located in the admi…）
- 例2：6236000000 | 7230000000 | 3256000000 | 2238000000 | 2210000000（表：political border／同じ表の列：label, description, flag, country, Commons category, located in the admi…）
- 例3：3218501000 | 4246501000 | 6234501000 | 3243501000 | 7410000000（表：capital city／同じ表の列：label, description, flag, Commons category, flag image, country）

## g0746 — wikidbs10k：見出し「station code」（Wikidata の型 `string`）（23 列）
- 例1：6803 | 2551 | 1586 | 25 | 5933（表：Hanover S-Bahn／同じ表の列：label, description, Commons category, country, image, coordinate location）
- 例2：2565 | 2544 | 415 | 2765 | 1587（表：adjacent station／同じ表の列：label, description, Commons category, instance of, country, coordinate location）
- 例3：69104 | 62002 | 07003 | 06100 | 06008（表：Cercanías Murcia Alicante／同じ表の列：label, description, part of, Commons category, coordinate location, country）

## g0747 — wikidbs10k：見出し「trap danmark id」（Wikidata の型 `string`）（23 列）
- 例1：Gentofte_Kommune | Furesø_Kommune | Ballerup_Kommune | Albertslund_Kommune | Ishøj_Kommune（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例2：Kongens_Lyngby | Frederikssund | Albertslund | København | Ishøj（表：eponym／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例3：Fredensborg_Kommune | Vallensbæk_Kommune | Ballerup_Kommune | Allerød_Kommune | Herlev_Kommune（表：political border／同じ表の列：label, description, capital, country, located in the admi…, Commons category）

## g0748 — wikidbs10k：見出し「worms-id for taxa」（Wikidata の型 `string`）（23 列）
- 例1：413112 | 184857 | 169687 | 169702 | 169649（表：natural product／同じ表の列：label, description, parent taxon, instance of, taxon name, taxon rank）
- 例2：567871 | 138618 | 131771 | 169698 | 169631（表：taxon／同じ表の列：label, description, ITIS TSN, taxon name, instance of, taxon rank）
- 例3：172 | 100054 | 100211.0 | 583053.0 | 571261.0（表：taxon／同じ表の列：label, description, Commons category, image, taxon rank, parent taxon）

## g0749 — wikidbs10k：見出し「has cause」（Wikidata の型 `wikibase-entityid`）（23 列）
- 例1：2020 COVID-19 pandemic in Louisiana | COVID-19 pandemic in Venezuela | 2020 COVID-19 pandemic in Guernsey | 2020 COVID-19 pandemic in Ontario | 2020 COVID-19 pandemic in Jamaica（表：social distancing／同じ表の列：label, description, instance of, start time, announcement date, applies to jurisdic…）
- 例2：2020 COVID-19 pandemic in Rhode Island | 2020 COVID-19 pandemic in Liechtenstein | COVID-19 pandemic in Colombia | 2020 COVID-19 pandemic in Vermont | 2020 COVID-19 pandemic in the Bahamas（表：countermeasure／同じ表の列：label, description, instance of, applies to jurisdic…, start time, announcement date）
- 例3：Mayaro virus | O'nyong'nyong virus | Venezuelan equine encephalitis virus | Chikungunya virus | Sindbis virus（表：alphavirus infections／同じ表の列：label, description, subclass of, health specialty, instance of, disease transmissio…）

## g0750 — wikidbs10k：見出し「code of household registration and conscription information」（Wikidata の型 `string`）（22 列）
- 例1：10020 | 10004 | 09007 | 10018 | 10002（表：administrative territorial entity／同じ表の列：label, description, category for people…, country, Commons category, instance of）
- 例2：10008010 | 10016.0 | 10000.0 | 10015.0 | 10020.0（表：administrative territorial entity／同じ表の列：label, description, country, contains the admini…, located in the admi…, coordinate location）
- 例3：10018020 | 63000 | 10017010 | 10004010 | 10014010（表：headquarters／同じ表の列：label, description, coordinate location, Freebase ID, GeoNames ID, instance of）

## 答えの雛形

```
g0601	
g0602	
g0603	
g0604	
g0605	
g0606	
g0607	
g0608	
g0609	
g0610	
g0611	
g0612	
g0613	
g0614	
g0615	
g0616	
g0617	
g0618	
g0619	
g0620	
g0621	
g0622	
g0623	
g0624	
g0625	
g0626	
g0627	
g0628	
g0629	
g0630	
g0631	
g0632	
g0633	
g0634	
g0635	
g0636	
g0637	
g0638	
g0639	
g0640	
g0641	
g0642	
g0643	
g0644	
g0645	
g0646	
g0647	
g0648	
g0649	
g0650	
g0651	
g0652	
g0653	
g0654	
g0655	
g0656	
g0657	
g0658	
g0659	
g0660	
g0661	
g0662	
g0663	
g0664	
g0665	
g0666	
g0667	
g0668	
g0669	
g0670	
g0671	
g0672	
g0673	
g0674	
g0675	
g0676	
g0677	
g0678	
g0679	
g0680	
g0681	
g0682	
g0683	
g0684	
g0685	
g0686	
g0687	
g0688	
g0689	
g0690	
g0691	
g0692	
g0693	
g0694	
g0695	
g0696	
g0697	
g0698	
g0699	
g0700	
g0701	
g0702	
g0703	
g0704	
g0705	
g0706	
g0707	
g0708	
g0709	
g0710	
g0711	
g0712	
g0713	
g0714	
g0715	
g0716	
g0717	
g0718	
g0719	
g0720	
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
```
