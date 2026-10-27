# 銀ラベルのシート 003 / 008（外の学習データの読み替え）

- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列
- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`
- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を、ChatGPT は `answers/sheet_003.tsv`、Grok は `answers_grok/sheet_003.tsv` に写して埋める。**相手の答えは見ない**

## g0301 — sotab_v2：元の種類 `unitText`（437 列）
- 例1：Kg
- 例2：grams
- 例3：Kg

## g0302 — wikidbs10k：見出し「cytogenetic location」（Wikidata の型 `string`）（420 列）
- 例1：3|3 F2.1 | 9q34.11 | 10|10 D3 | 12q13.3 | 19p13.3（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例2：8q24 | 13 B1|13 30.12 cM | 4 C5- C6|4 45.52 cM | 5q31 | 18 E3|18 51.42 cM（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例3：19 C3|19 38.75 cM | 15p11 | 10q12 | 10q24.32 | 8p21.3（表：encoded by／同じ表の列：label, description, Entrez Gene ID, Ensembl gene ID, Ensembl transcript …, RefSeq RNA ID）

## g0303 — wikidbs10k：見出し「encyclopædia universalis id」（Wikidata の型 `string`）（417 列）
- 例1：azerbaidjan | bosnie-herzegovine | portugal | norvege | paraguay（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：afghanistan | turquie | georgie | liberia | moldavie（表：jurisdiction／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：angola | france-vue-d-ensemble | coree-du-sud | vietnam | norvege（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0304 — sotab_v2：元の種類 `workHours`（413 列）
- 例1：Mon - Fri: 9:00 to 18:00
- 例2：45-50 hours a week, Monday through Satu… | nights, weekend, holidays | nights, weekends, holidays | nights, evenings, and weekends | evenings, weekends, holidays
- 例3：11: 00-19: 00 (7 hours a day), 2 days o… | Weekdays 9:00 to 18:00 (1 hour break) D… | 8:00~17:00 8:30~17:30 | Weekdays 9:00 to 18:00 (1 hour break) | Day shift 8: 00-17: 00 60 minutes break…

## g0305 — wikidbs10k：見出し「highest judicial authority」（Wikidata の型 `wikibase-entityid`）（413 列）
- 例1：Superior Court of Justice of the Grand-… | Supreme Court of the United States | Supreme Court of Cassation | Supreme Court of Morocco | Constitutional Court of Belgium（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：Supreme Court of the United Kingdom | Supreme Court of Canada | Supreme Court of Missouri | Tennessee Supreme Court | Maryland Court of Appeals（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例3：Supreme Court of Ohio | Supreme Court of the United Kingdom | New York Court of Appeals | Supreme Court of Florida | Maryland Court of Appeals（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0306 — sotab_v2：元の種類 `OccupationalExperienceRequirements`（399 列）
- 例1：0 | 3
- 例2：. Bachelor degree.. TESOL/TEFL/CELTA ce… | To be eligible for a teaching position … | APAX English is currently recruiting fu… | • Native English speaker preferred • Ba… | Graduated from University with major in…
- 例3：3 to 10 years experience. | At least 1 year experience. | At least 2 years experience. | 1 to 10 years experience. | 5 to 15 years experience.

## g0307 — wikidbs10k：見出し「event distance」（Wikidata の型 `quantity`）（381 列）
- 例1：+85 | +97 | +94 | +166 | +250（表：2004 Champ Car season／同じ表の列：label, description, sport, point in time, instance of, country）
- 例2：+193 | +174.5 | +196.5 | +87.5 | +172.5（表：1969 Tour de Suisse／同じ表の列：label, description, part of, point in time, winner, start point）
- 例3：12.0 | 225.0 | 145.0 | 174.5 | 44.0（表：followed by／同じ表の列：label, description, part of, point in time, winner, start point）

## g0308 — sotab_v2：元の種類 `Rating`（379 列）
- 例1：PG | TV-14 | R | PG-13 | TV-PG
- 例2：R | PG | Not Rated | Unrated | G
- 例3：PG | M/PG | TV-MA | PG-13 | TV-PG

## g0309 — wikidbs10k：見出し「giant bomb id」（Wikidata の型 `string`）（379 列）
- 例1：3015-5358 | 3015-5978 | 3015-1949 | 3015-6908 | 3015-1984（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, Pokémon index, part of, height）
- 例2：3035-2879 | 3035-882 | 3035-2077 | 3035-720 | 3035-1098（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：3035-197 | 3035-2258 | 3035-2882 | 3035-346 | 3035-304（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0310 — wikidbs10k：見出し「catalog code」（Wikidata の型 `string`）（378 列）
- 例1：ARG | PRT | STL | SKK | 24（表：historic county／同じ表の列：label, description, instance of, coordinate location, country, locator map image）
- 例2：HTF | LNC | CRD | GLC | YRK（表：historic county／同じ表の列：label, description, instance of, country, part of, locator map image）
- 例3：CNW | BUC | SFF | RDN | DBH（表：political border／同じ表の列：label, description, instance of, country, flag image, locator map image）

## g0311 — wikidbs10k：見出し「fips 6-4」（Wikidata の型 `string`）（365 列）
- 例1：51099 | 51193 | 51103 | 51005 | 51153（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）
- 例2：29049.0 | 29221.0 | 29107.0 | 29059.0 | 29197.0（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：29217.0 | 29075.0 | 29123.0 | 29029.0 | 29187.0（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0312 — sotab_v2：元の種類 `ProductModel`（361 列）
- 例1：RGV2305NN | UN65LS003AFXZA | WTB86201UC | VGIC53616BSS | BT703802BKGG
- 例2：4 oz. | 16oz Bottle | Small
- 例3：1145 | 1764 | 946 | 1158 | 2023

## g0313 — wikidbs10k：見出し「uberon id」（Wikidata の型 `string`）（361 列）
- 例1：0001883 | 0000922 | 0001854 | 0002661 | 0000955（表：expressed in／同じ表の列：label, description, subclass of, instance of）
- 例2：0002082 | 0000965 | 0001017 | 0000939 | 0002385（表：expressed in／同じ表の列：label, description, Freebase ID, Foundational Model …, instance of, subclass of）
- 例3：0002167 | 0002385 | 0002116 | 0002115 | 0004454（表：expressed in／同じ表の列：label, description, Freebase ID, Foundational Model …, instance of, subclass of）

## g0314 — wikidbs10k：見出し「edition humboldt digital id」（Wikidata の型 `string`）（358 列）
- 例1：H0018114 | H0004801 | H0002330 | H0000345 | H0007374（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例2：H0010421 | H0006559 | H0009596 | H0010179 | H0002381（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：H0004781 | H0008206 | H0001636 | H0000345 | H0000330（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0315 — wikidbs10k：見出し「office contested」（Wikidata の型 `wikibase-entityid`）（356 列）
- 例1：Member of the Parliament of Catalonia（表：Catalan regional election 2015 in Segrià／同じ表の列：label, description, instance of, country, applies to jurisdic…, point in time）
- 例2：Member of the Seimas | Prime Minister of Lithuania（表：Lithuanian parliamentary election／同じ表の列：label, description, instance of, Freebase ID, country, point in time）
- 例3：Prime Minister of Lithuania | Member of the Seimas（表：followed by／同じ表の列：label, description, country, instance of, point in time, followed by）

## g0316 — wikidbs10k：見出し「armeniapedia id」（Wikidata の型 `string`）（353 列）
- 例1：13389 | 4103 | 4099 | 4038 | 9760（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：4037.0 | 3950.0 | 4035.0 | 4103.0 | 4096.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：2405 | 4035 | 3960 | 4099 | 4122（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0317 — sotab_v2：元の種類 `TVEpisode/name`（324 列）
- 例1：Annedroids Season 1 Episode 9 | The Victims’ Game Season 1 Episode 4 | Grant Season 5 Episode 3 | Man with a Plan Season 4 Episode 7 | The Customer Is Always Right Season 2 E…（DBpedia：TelevisionEpisode）
- 例2：Bones Season 12 Episode 2 | The Simpsons Season 13 Episode 15 | The Simpsons Season 6 Episode 16 | Bones Season 8 Episode 23 | Supernatural Season 9 Episode 8（DBpedia：TelevisionEpisode）
- 例3：Ging's Friends x And x True Friends | Great Power x And x Ultimate Power | Taking Stock x And x Taking Action | Formidable Enemy x And x Clear Objective | The Word x Is x You（DBpedia：TelevisionEpisode）

## g0318 — wikidbs10k：見出し「female form of label」（Wikidata の型 `monolingualtext`）（322 列）
- 例1：alcaldesa de Alcanó | alcaldesa de Mayals | alcaldesa de Bell Lloch | alcaldesa de Aitona | alcaldesa de Algerri（表：office held by head of government／同じ表の列：label, description, subclass of, applies to jurisdic…, country, instance of）
- 例2：secretària d'Estat del Transport | alcaldesa de São Paulo | חברת הפרלמנט ה-58 של הממלכה המאוחדת | députée néerlandaise | diputada d'Ucraína（表：mandate／同じ表の列：label, description, subclass of, instance of, country, topic's main catego…）
- 例3：alcaldesa de Alcorcón | alcaldesa de Lloret de Mar | alcaldesa | alcaldesa de El Espinar | alcaldesa de Algaida（表：office held by head of government／同じ表の列：label, description, subclass of, applies to jurisdic…, country, instance of）

## g0319 — sotab_v2：元の種類 `Boolean`（317 列）
- 例1：true（DBpedia：boolean）
- 例2：True（DBpedia：boolean）
- 例3：true（DBpedia：boolean）

## g0320 — wikidbs10k：見出し「opencorporates id」（Wikidata の型 `string`）（317 列）
- 例1：dk/29190623 | dk/29189897 | se/212000-2361 | se/212000-0290 | se/212000-0217（表：administrative territorial entity／同じ表の列：label, description, country, capital, shares border with, Commons category）
- 例2：se/212000-1918 | se/212000-2924 | dk/29189560 | se/212000-2940 | dk/29189668（表：political border／同じ表の列：label, description, country, shares border with, capital, Commons category）
- 例3：dk/29189897 | se/212000-0217 | se/212000-2361 | se/212000-0811 | dk/29189854（表：administrative centre／同じ表の列：label, description, country, shares border with, capital, Commons category）

## g0321 — wikidbs10k：見出し「bacdive id」（Wikidata の型 `string`）（315 列）
- 例1：241.0 | 17584.0 | 136795.0 | 12871.0 | 17248.0（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：5292 | 5301 | 6559 | 14712 | 624（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例3：17796.0 | 5792.0 | 5292.0 | 2529.0 | 1599.0（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）

## g0322 — sotab_v2：元の種類 `MonetaryAmount`（314 列）
- 例1：£8.72 - 8.72 per hour | Market related | £13 - 14 per hour | DOE | £45k - 55k per year
- 例2：65.00 HOUR | 80.00 HOUR | 75.00 HOUR | 30.00 HOUR | 40.00 HOUR
- 例3：55000 | 65000 | 70000 | 130000 | 95000

## g0323 — wikidbs10k：見出し「related category」（Wikidata の型 `wikibase-entityid`）（314 列）
- 例1：Category:Portuguese pronunciation | Category:Dutch pronunciation | Category:French pronunciation | Category:Spanish pronunciation | Category:Swedish pronunciation（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：Category:Czech pronunciation | Category:Spanish pronunciation | Category:Arabic pronunciation | Category:Dutch pronunciation | Category:Bulgarian pronunciation（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：Category:Catalan pronunciation | Category:Dutch pronunciation | Category:English pronunciation | Category:Welsh pronunciation | Category:Finnish pronunciation（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0324 — wikidbs10k：見出し「jstor topic id」（Wikidata の型 `string`）（306 列）
- 例1：bacillus-anthracis | bacillus-thuringiensis | lactobacillus-casei | enterococcus-faecalis | bacillus-cereus（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：gyrus-cinguli | ovaries | achilles-tendon | thymus-hormones | spermatocytes（表：expressed in／同じ表の列：label, description, subclass of, Freebase ID, Foundational Model …, described by source）
- 例3：escherichia | haemophilus-influenzae | yersinia-pestis | shigella | yersinia-infections（表：taxon／同じ表の列：label, description, Commons category, taxon name, image, taxon rank）

## g0325 — sotab_v2：元の種類 `SportsTeam`（303 列）
- 例1：Portsmouth | IFK Gothenburg | Sporting Kansas City | Lugano | Celtic（DBpedia：SportsTeam）
- 例2：Crystal Palace | Maribor | Huddersfield | Czech Republic | Qarabag（DBpedia：SportsTeam）
- 例3：Shakhter Karagandy | BATE | Villarreal | Slavia Sofia | De Graafschap（DBpedia：SportsTeam）

## g0326 — wikidbs10k：見出し「gynopedia id」（Wikidata の型 `string`）（300 列）
- 例1：India | Switzerland | South Korea | Georgia | Russia（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例2：Germany | South Korea | Canada | Denmark | Austria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Poland | Morocco | Hong Kong | Czech Republic | Spain（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0327 — wikidbs10k：見出し「practiced by」（Wikidata の型 `wikibase-entityid`）（293 列）
- 例1：rugby league player | American football player | lacrosse player | baseball player | handball player（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, Commons category, subclass of, topic's main catego…）
- 例2：gymnast | boxer | bowls player | netballer | road cyclist（表：type of sport／同じ表の列：label, description, subclass of, Commons category, Library of Congress…, topic's main catego…）
- 例3：boxer | sport shooter | table tennis player | judoka | squash player（表：field of work／同じ表の列：label, description, subclass of, Commons category, Library of Congress…, topic's main catego…）

## g0328 — wikidbs10k：見出し「heritage designation」（Wikidata の型 `wikibase-entityid`）（290 列）
- 例1：Jardín histórico | Bien de Interés Cultural | Property of Local Relevance（表：Jardín histórico／同じ表の列：label, description, Commons category, coordinate location, image, located in the admi…）
- 例2：Grade I listed building | Grade II* listed building | Grade II listed building（表：assembly room／同じ表の列：label, description, coordinate location, country, National Heritage L…, located in the admi…）
- 例3：Bien de Interés Cultural | monument historique inscrit | Cultural Asset part of the cultural her… | Bien Catalogado of the Aragonese Cultur… | Bien Inventariado del Patrimonio Cultur…（表：conjuratory／同じ表の列：label, description, located in the admi…, instance of, country, coordinate location）

## g0329 — wikidbs10k：見出し「süddeutsche zeitung topic id」（Wikidata の型 `string`）（286 列）
- 例1：Kroatien | Schweden | Polen | Irland | Deutschland（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：Italien | Südkorea | USA | Kanada | Dänemark（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Rumänien | Irland | Russland | Bosnien-Herzegowina | Slowakei（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0330 — wikidbs10k：見出し「organizer」（Wikidata の型 `wikibase-entityid`）（285 列）
- 例1：Women's Tennis Association（表：Copa Colsanitas／同じ表の列：label, description, instance of, sport, point in time, has part(s)）
- 例2：Women's Tennis Association（表：followed by／同じ表の列：label, description, instance of, followed by, sport, point in time）
- 例3：Women's Tennis Association（表：follows／同じ表の列：label, description, instance of, followed by, follows, part of）

## g0331 — wikidbs10k：見出し「guardian topic id」（Wikidata の型 `string`）（283 列）
- 例1：world/greece | world/newzealand | world/france | world/spain | world/italy（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：world/india | world/romania | world/russia | world/ukraine | world/north-korea（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：us-news/canada | world/sweden | world/romania | world/slovenia | world/hungary（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0332 — wikidbs10k：見出し「country of origin」（Wikidata の型 `wikibase-entityid`）（283 列）
- 例1：United Kingdom | United States of America | England（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：Japan | United Kingdom | Yuan dynasty | Sweden | Ming dynasty（表：work／同じ表の列：label, description, instance of, title, narrative location）
- 例3：England | United States of America | France | Netherlands | Germany（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）

## g0333 — wikidbs10k：見出し「corporate number (japan)」（Wikidata の型 `string`）（281 列）
- 例1：2000020012246.0 | 5000020015849.0 | 2000020023078.0 | 9000020022098.0 | 1000020052094.0（表：administrative territorial entity／同じ表の列：label, description, image, instance of, located in the admi…, Commons category）
- 例2：3000020022021 | 2000020022047 | 7000020032140 | 5000020012301 | 1000020052094（表：political border／同じ表の列：label, description, Commons category, dantai code, flag image, country）
- 例3：9000020011002 | 3000020022021 | 3000020052043 | 8000020032131 | 3000020012360（表：replacing subject／同じ表の列：label, description, Commons category, dantai code, flag image, country）

## g0334 — wikidbs10k：見出し「bncf thesaurus id」（Wikidata の型 `string`）（279 列）
- 例1：6095 | 6544 | 658 | 22 | 356（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：152 | 6095 | 6546 | 356 | 70（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：6544 | 658 | 67057 | 44 | 5074（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0335 — wikidbs10k：見出し「ine municipality code」（Wikidata の型 `string`）（278 列）
- 例1：25078 | 25048 | 25912 | 25125 | 25182（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：25120 | 25251 | 25010 | 25912 | 25131（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：7004.0 | 28007.0 | 29007.0 | 38028.0 | 15030.0（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0336 — wikidbs10k：見出し「uic numerical country code」（Wikidata の型 `string`）（278 列）
- 例1：56.0 | 92.0 | 86.0 | 70.0 | 93.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：87 | 83 | 51 | 49 | 60（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：81 | 86 | 73 | 70 | 21（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0337 — wikidbs10k：見出し「dantai code」（Wikidata の型 `string`）（277 列）
- 例1：12335.0 | 22098.0 | 23078.0 | 15849.0 | 12246.0（表：administrative territorial entity／同じ表の列：label, description, image, instance of, located in the admi…, Commons category）
- 例2：012301 | 52043 | 032140 | 22012 | 052094（表：political border／同じ表の列：label, description, Commons category, flag image, country, located in the admi…）
- 例3：022047 | 022021 | 032131 | 012335 | 052043（表：replacing subject／同じ表の列：label, description, Commons category, flag image, country, located in the admi…）

## g0338 — wikidbs10k：見出し「uic alphabetical country code」（Wikidata の型 `string`）（274 列）
- 例1：LV | I | RUS | NL | DZ（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：NZ | ROK | DZ | FIN | E（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：GR | F | GB | ROK | D（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0339 — wikidbs10k：見出し「public holiday」（Wikidata の型 `wikibase-entityid`）（271 列）
- 例1：Australia Day | Victory Day | Easter Monday | Defender of the Fatherland Day | Christmas（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：Defender of the Fatherland Day | Independence Day | Yule | Victory Day | New Year's Day（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Independence Day of Ukraine | National Independence Day | Portugal Day | Yule | New Year's Day（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0340 — wikidbs10k：見出し「legal form」（Wikidata の型 `wikibase-entityid`）（270 列）
- 例1：public law corporation（表：provincial deputation／同じ表の列：label, description, instance of, inception, headquarters locati…, country）
- 例2：public law corporation（表：executive branch／同じ表の列：label, description, instance of, inception, headquarters locati…, official website）
- 例3：public-law institution | state media（表：operator／同じ表の列：label, description, headquarters locati…, Commons category, instance of, Freebase ID）

## g0341 — wikidbs10k：見出し「inspire id」（Wikidata の型 `string`）（269 列）
- 例1：ES.IGN.BDDAE.34092525226 | ES.IGN.BDDAE.34092525036 | ES.IGN.BDDAE.34092525008 | ES.IGN.BDDAE.34092525912 | ES.IGN.BDDAE.34092525033（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：ES.IGN.BDDAE.34092525131 | ES.IGN.BDDAE.34092525125 | ES.IGN.BDDAE.34092525015 | ES.IGN.BDDAE.34092525038 | ES.IGN.BDDAE.34092525230（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：ES.IGN.BDDAE.34094343092 | ES.IGN.BDDAE.34074040076 | ES.IGN.BDDAE.34100303014 | ES.IGN.BDDAE.34091717071 | ES.IGN.BDDAE.34040707004（表：jurisdiction／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0342 — wikidbs10k：見出し「historic county」（Wikidata の型 `wikibase-entityid`）（267 列）
- 例1：Aberdeenshire | County Dublin | Nairnshire | East Lothian | Selkirkshire（表：physical location／同じ表の列：label, description, instance of, coordinate location, Freebase ID, country）
- 例2：East Lothian | Fife | Argyll | Inverness-shire | Roxburghshire（表：capital city／同じ表の列：label, description, instance of, Commons category, coordinate location, twinned administrat…）
- 例3：Staffordshire | Lancashire | Norfolk | Hertfordshire | Suffolk（表：assembly room／同じ表の列：label, description, coordinate location, country, National Heritage L…, located in the admi…）

## g0343 — wikidbs10k：見出し「headquarters location」（Wikidata の型 `wikibase-entityid`）（266 列）
- 例1：Segovia | Oviedo | Tarragona | Cuenca | Palacio de la Diputación de Guadalajara（表：provincial deputation／同じ表の列：label, description, instance of, inception, country, VIAF ID）
- 例2：Hospital de la Encarnación | Edificio de la Diputación de Toledo | Granada | Diputación Provincial de Soria building | Palacio de la Diputación de Palencia（表：executive branch／同じ表の列：label, description, instance of, inception, official website, country）
- 例3：Jewell | Colton | Sisters | Vernonia | Warrenton（表：school district of Oregon／同じ表の列：label, description, country, instance of, located in the admi…, NCES district ID）

## g0344 — wikidbs10k：見出し「encyclopedia of the history of ukraine id」（Wikidata の型 `string`）（265 列）
- 例1：Shvetsiia | Brazyliia | Rosiia | Kanada | Meksyka（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：Polscha | Shvetsiia | Rosiia | Norvehiia | Latviya_respublika（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Shvejtsariia | Spolucheni_S | Frantsiia | Indija | Velyka_Brytaniia（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, Libraries Australia…, coordinates of sout…）

## g0345 — wikidbs10k：見出し「fips 55-3 (locations in the us)」（Wikidata の型 `string`）（265 列）
- 例1：29-70576 | 29-59942 | 29-57116 | 29-25768 | 29-31762（表：capital city／同じ表の列：label, description, country, instance of, coordinate location, located in the admi…）
- 例2：41-29900 | 41-03050 | 41-35700 | 41-65950 | 41-40550（表：headquarters／同じ表の列：label, description, instance of, country, located in the admi…, image）
- 例3：54-05332 | 34-29430 | 16-03160 | 02-36400 | 12-35000（表：significant place／同じ表の列：label, description, country, instance of, Commons category, located in the admi…）

## g0346 — wikidbs10k：見出し「art & architecture thesaurus id」（Wikidata の型 `string`）（263 列）
- 例1：300389311 | 300387843 | 300388633 | 300388277 | 300388256（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, PSH ID, ISO 639-2 code）
- 例2：300389336 | 300388191 | 300388696 | 300388306 | 300388770（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, ISO 639-2 code）
- 例3：300388299 | 300388306 | 300389311 | 300389291 | 300388256（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, PSH ID, ISO 639-2 code）

## g0347 — wikidbs10k：見出し「number of participants」（Wikidata の型 `quantity`）（261 列）
- 例1：+25 | +26 | +34 | +38 | +42（表：sailing at the 2004 Summer Olympics／同じ表の列：label, description, part of, instance of, follows, location）
- 例2：+25 | +38 | +34 | +40 | +54（表：followed by／同じ表の列：label, description, part of, instance of, follows, location）
- 例3：+26 | +28 | +32 | +30 | +38（表：sailing at the 2008 Summer Olympics／同じ表の列：label, description, Freebase ID, part of, instance of, follows）

## g0348 — wikidbs10k：見出し「dagens nyheter topic id」（Wikidata の型 `string`）（259 列）
- 例1：danmark | sydkorea | ryssland | australien | brasilien（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：storbritannien | ryssland | indien | frankrike | nederlanderna（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：japan | kina | indien | ryssland | sovjetunionen（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, Libraries Australia…, coordinates of sout…）

## g0349 — wikidbs10k：見出し「industry」（Wikidata の型 `wikibase-entityid`）（257 列）
- 例1：mass media | public broadcasting | broadcasting（表：operator／同じ表の列：label, description, headquarters locati…, Commons category, instance of, Freebase ID）
- 例2：railway | public transport | rail transport（表：operator／同じ表の列：label, description, Commons category, instance of, topic's main catego…, Freebase ID）
- 例3：administration publique générale（表：administrative territorial entity／同じ表の列：label, description, instance of, Commons category, located in the admi…, coordinate location）

## g0350 — wikidbs10k：見出し「mass」（Wikidata の型 `quantity`）（256 列）
- 例1：+130.905 | +115.90846 | +112.909374652 | +139.921645817 | +143.938945079（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例2：+338.115423676 | +400.094688232 | +570.079826016 | +610.18389716 | +372.099773612（表：3C-substituted chalcone／同じ表の列：label, description, instance of, PubChem CID, chemical formula, InChI）
- 例3：+34.056728 | +30.024992235 | +22.9944669 | +29.019753 | +31.033474816（表：neon／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）

## g0351 — wikidbs10k：見出し「vision of britain place id」（Wikidata の型 `string`）（256 列）
- 例1：17460 | 17330 | 17441 | 17444 | 17192（表：historic county／同じ表の列：label, description, instance of, coordinate location, country, locator map image）
- 例2：16316.0 | 16794.0 | 16318.0 | 17381.0 | 17006.0（表：capital city／同じ表の列：label, description, instance of, Commons category, coordinate location, twinned administrat…）
- 例3：17487 | 17488.0 | 17455 | 17457.0 | 17450.0（表：political border／同じ表の列：label, description, instance of, country, flag image, locator map image）

## g0352 — wikidbs10k：見出し「genre」（Wikidata の型 `wikibase-entityid`）（249 列）
- 例1：portrait（表：Windsor Beauties／同じ表の列：label, description, inventory number, collection, instance of, location）
- 例2：portrait（表：depicting object／同じ表の列：label, description, inventory number, collection, instance of, location）
- 例3：hack and slash | action-adventure game（表：work／同じ表の列：label, description, part of the series, platform, game mode, instance of）

## g0353 — wikidbs10k：見出し「toid」（Wikidata の型 `string`）（241 列）
- 例1：7000000000036552 | 7000000000030106 | 7000000000030505 | country/scotland | 7000000000030110（表：administrative territorial entity／同じ表の列：label, description, category of associa…, Curlie ID, MusicBrainz area ID, ISO 3166-2 code）
- 例2：4000000074560731.0 | 4000000074541547.0 | 4000000074555397.0 | 4000000074554571.0 | 4000000074558240.0（表：capital city／同じ表の列：label, description, instance of, Commons category, coordinate location, twinned administrat…）
- 例3：7000000000030419 | 7000000000030110 | 7000000000036552 | 7000000000029638 | 7000000000030503（表：administrative centre／同じ表の列：label, description, instance of, capital, country, ISO 3166-2 code）

## g0354 — wikidbs10k：見出し「list of monuments」（Wikidata の型 `wikibase-entityid`）（239 列）
- 例1：list of cultural properties in Solothurn | list of cultural properties in Binningen | list of cultural properties in Brugg | list of cultural properties in Davos | list of cultural properties in Crans-Mo…（表：beginning／同じ表の列：label, description, country, located in the admi…, coat of arms image, Commons category）
- 例2：National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li…（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）
- 例3：National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li…（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0355 — wikidbs10k：見出し「published in」（Wikidata の型 `wikibase-entityid`）（238 列）
- 例1：Molecular Immunology | Molecular Biology of the Cell | Nature Cell Biology | Physiological Reviews | Journal of Cell Science（表：citation／同じ表の列：label, description, title, instance of, author name string, volume）
- 例2：Nature | Journal of Biological Chemistry | Developmental Cell | Proceedings of the National Academy of … | FEBS Journal（表：citation／同じ表の列：label, description, page(s), title, author name string, publication date）
- 例3：Journey to the West（表：Journey to the West／同じ表の列：label, description, language of work or…, follows, chapter, instance of）

## g0356 — wikidbs10k：見出し「inaturalist taxon id」（Wikidata の型 `string`）（237 列）
- 例1：127425 | 81837 | 56091 | 82771 | 117431（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例2：119000 | 146949 | 535779 | 47566 | 68858（表：taxon／同じ表の列：label, description, instance of, taxon name, taxon rank, parent taxon）
- 例3：357013 | 479424 | 846252 | 337407 | 372490（表：taxon／同じ表の列：label, description, parent taxon, taxon name, Commons category, instance of）

## g0357 — sotab_v2：元の種類 `paymentAccepted`（235 列）
- 例1：ATM, Visa | American Express, ATM, Cash, Diners Clu… | American Express, ATM, Cash, Visa | Cash, Mastercard, Visa | ATM, Check
- 例2：Maestro, Visa, MasterCard, Diners Club,… | Maestro, Visa, MasterCard, Diners Club,… | Maestro, Visa, MasterCard, American Exp… | Maestro, Visa, MasterCard, Diners Club,… | Maestro, Visa, Master Card, Diners Club…
- 例3：Cash, Credit Card, Online Payments, Pay…

## g0358 — sotab_v2：元の種類 `CreativeWorkSeries`（229 列）
- 例1：Puppy Dog Pals | Reno 911! | Single Parents | The First 48 | The Trials of Gabriel Fernandez（DBpedia：TelevisionShow）
- 例2：Young Justice | The Magicians | NCIS | Friends | Siesta Key（DBpedia：TelevisionShow）
- 例3：Outback Opal Hunters | Asur | American Dad! | The Real Housewives of Beverly Hills | Under the Dome（DBpedia：TelevisionShow）

## g0359 — wikidbs10k：見出し「italian vikidia id」（Wikidata の型 `string`）（228 列）
- 例1：New_York_(stato) | Montana | California | Tennessee | Stati_Uniti_d'America（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：New_Jersey | Missouri | New_York_(stato) | Maryland | Pennsylvania（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：Stati_Uniti_d'America | Texas | Regno_Unito | Florida | Maryland（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0360 — wikidbs10k：見出し「open tree of life id」（Wikidata の型 `string`）（227 列）
- 例1：380857 | 5749134 | 762079 | 856671 | 284049（表：natural product／同じ表の列：label, description, taxon name, taxon rank, parent taxon, NCBI taxonomy ID）
- 例2：681720 | 412934 | 587223 | 841875 | 245801（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例3：216462.0 | 1006246.0 | 748359.0 | 709894 | 508058.0（表：secretion or excretion／同じ表の列：label, description, taxon name, taxon rank, parent taxon, instance of）

## g0361 — wikidbs10k：見出し「foundational model of anatomy id」（Wikidata の型 `string`）（222 列）
- 例1：7149 | 18644 | 49006 | 22541 | 5018（表：expressed in／同じ表の列：label, description, Freebase ID, instance of, UBERON ID, subclass of）
- 例2：3947 | 7207 | 14069 | 7309 | 7197（表：expressed in／同じ表の列：label, description, Freebase ID, instance of, UBERON ID, subclass of）
- 例3：19035 | 58687 | 18646 | 19386 | 61839（表：expressed in／同じ表の列：label, description, instance of, UBERON ID, subclass of）

## g0362 — wikidbs10k：見出し「start point」（Wikidata の型 `wikibase-entityid`）（222 列）
- 例1：Gstaad | Zürich | Wohlen | Bad Zurzach | Davos（表：1969 Tour de Suisse／同じ表の列：label, description, part of, point in time, event distance, winner）
- 例2：Solothurn | Brugg | Binningen | Davos | Crans-Montana（表：followed by／同じ表の列：label, description, part of, point in time, event distance, winner）
- 例3：Lugano | Wohlen | Gstaad | Brugg | Crans-Montana（表：follows／同じ表の列：label, description, part of, point in time, event distance, winner）

## g0363 — wikidbs10k：見出し「nuts code」（Wikidata の型 `string`）（220 列）
- 例1：ES414 | ES241 | ES243 | ES512 | ES431（表：jurisdiction／同じ表の列：label, description, INE municipality co…, Dewey Decimal Class…, located in the admi…, ISO 3166-2 code）
- 例2：ES11 | ES615 | ES614 | ES617 | ES23（表：political border／同じ表の列：label, description, INE municipality co…, Dewey Decimal Class…, located in the admi…, ISO 3166-2 code）
- 例3：DED51 | DE501 | DE404 | DE712 | DE6（表：headquarters／同じ表の列：label, description, twinned administrat…, page banner, country, Commons category）

## g0364 — sotab_v2：元の種類 `DeliveryMethod`（219 列）
- 例1：http://purl.org/goodrelations/v1#Delive…
- 例2：http://purl.org/goodrelations/v1#Delive…
- 例3：http://purl.org/goodrelations/v1#Delive…

## g0365 — wikidbs10k：見出し「ballotpedia id」（Wikidata の型 `string`）（216 列）
- 例1：James_City_County,_Virginia | Lancaster_County,_Virginia | Buckingham_County,_Virginia | Chesterfield_County,_Virginia | Prince_William_County,_Virginia（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）
- 例2：Vernon_County,_Missouri | Perry_County,_Missouri | Taney_County,_Missouri | Cape_Girardeau_County,_Missouri | Grundy_County,_Missouri（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：Stoddard_County,_Missouri | Wisconsin | Henry_County,_Missouri | Crawford_County,_Missouri | Morgan_County,_Missouri（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0366 — wikidbs10k：見出し「maintained by wikiproject」（Wikidata の型 `wikibase-entityid`）（216 列）
- 例1：WikiProject Canada | WikiProject Sweden | WikiProject Spain | WikiProject Denmark | WikiProject Mexico（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：WikiProject Korea/North Korea | WikiProject Spain | WikiProject Mexico | WikiProject Austria | WikiProject Germany（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：WikiProject Portugal | WikiProject Ukraine | WikiProject Netherlands | WikiProject Denmark | WikiProject Spain（表：citizenship／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0367 — wikidbs10k：見出し「facet of」（Wikidata の型 `wikibase-entityid`）（215 列）
- 例1：Ohio | California | Maryland | Ontario | Illinois（表：geography／同じ表の列：label, description, instance of, topic's main catego…, subclass of）
- 例2：Maryland | United States of America | Florida | Texas | Pennsylvania（表：aspect of history／同じ表の列：label, description, part of, topic's main catego…, instance of, Commons category）
- 例3：Jordan | United Kingdom | Israel | Tanzania | Palau（表：aspect of history／同じ表の列：label, description, Commons category, topic's main catego…, Dewey Decimal Class…, instance of）

## g0368 — wikidbs10k：見出し「has list」（Wikidata の型 `wikibase-entityid`）（215 列）
- 例1：list of state leaders in 1130 | list of state leaders in 1131 | list of state leaders in 1137 | list of state leaders in 1135 | list of state leaders in 1138（表：1130s／同じ表の列：label, description, Commons category, instance of, part of, follows）
- 例2：list of state leaders in 1136 | list of state leaders in 1131 | list of state leaders in 1132 | list of state leaders in 1138 | list of state leaders in 1139（表：followed by／同じ表の列：label, description, Commons category, instance of, part of, follows）
- 例3：list of state leaders in 1135 | list of state leaders in 1137 | list of state leaders in 1130 | list of state leaders in 1132 | list of state leaders in 1134（表：follows／同じ表の列：label, description, Commons category, instance of, part of, follows）

## g0369 — wikidbs10k：見出し「interpro id」（Wikidata の型 `string`）（213 列）
- 例1：IPR034634 | IPR002268 | IPR000500 | IPR002266 | IPR002263（表：part／同じ表の列：label, description, subclass of, has part(s), instance of）
- 例2：IPR002340 | IPR009050 | IPR002337 | IPR002339 | IPR000971（表：part／同じ表の列：label, description, instance of, subclass of, molecular function）
- 例3：IPR027417 | IPR029679 | IPR029684 | IPR029667 | IPR038475（表：part／同じ表の列：label, description, instance of）

## g0370 — wikidbs10k：見出し「national historical museums of sweden id」（Wikidata の型 `string`）（212 列）
- 例1：geo/95CDA651-011B-44EF-92F9-1F5680FD754A | geo/F9FEFF96-EEF8-45D8-BA7A-3C8BAC93164D | geo/00FF2E4F-C147-45FA-9014-EAEB7F789A58 | geo/29524C97-9BE5-40F1-A28D-8165EC98CC91 | geo/31A3F326-4945-438D-91B6-373F74E0323C（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：geo/933361E4-7716-4FCF-A651-46F11C9F04A8 | geo/5954BE73-910D-4ABC-96C2-6781831F6043 | geo/CDAE54F3-20A3-4315-94DC-E08B4171CC34 | geo/5F9893EF-C8B3-4581-B4A7-3BB27CCE3843 | geo/908A1FC7-EA72-4378-825B-2D3BDCF063C2（表：citizenship／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：geo/F12A2D49-F4E3-4724-9613-0153A717719E | geo/5D90AB82-C8CC-48CB-A3D0-49DC99487B08 | geo/95CDA651-011B-44EF-92F9-1F5680FD754A | geo/74FBD018-DA7F-4D6A-B4F8-1B7FB6F54D06 | geo/E6245871-E915-4DF9-858A-C1990D26D752（表：country／同じ表の列：label, description, Commons category, coordinate location, topic's main catego…, flag image）

## g0371 — wikidbs10k：見出し「destination point」（Wikidata の型 `wikibase-entityid`）（212 列）
- 例1：Balmberg Pass | Binningen | Brugg | Crans-Montana | Davos（表：1969 Tour de Suisse／同じ表の列：label, description, part of, point in time, event distance, winner）
- 例2：Lugano | Balmberg Pass | Solothurn | Wohlen | Bad Zurzach（表：followed by／同じ表の列：label, description, part of, point in time, event distance, winner）
- 例3：Gstaad | Balmberg Pass | Binningen | Bad Zurzach | Brugg（表：follows／同じ表の列：label, description, part of, point in time, event distance, winner）

## g0372 — wikidbs10k：見出し「series ordinal」（Wikidata の型 `string`）（208 列）
- 例1：10 | 11 | 9 | 8 | 7（表：1969 Tour de Suisse／同じ表の列：label, description, part of, point in time, event distance, winner）
- 例2：10 | 2 | 9 | 5 | 8（表：followed by／同じ表の列：label, description, part of, point in time, event distance, winner）
- 例3：7 | 4 | 10 | 9 | 5（表：follows／同じ表の列：label, description, part of, point in time, event distance, winner）

## g0373 — wikidbs10k：見出し「gadm id」（Wikidata の型 `string`）（203 列）
- 例1：CHE.1.4_1 | CHE.21_1 | CHE.23.11_1 | CHE.4.1_1 | CHE.6.20.3_1（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, coat of arms image, coordinate location）
- 例2：DEU.10.24_1 | DEU.6_1 | DEU.2.54_1 | DEU.4.14_1 | DEU.1.40_1（表：headquarters／同じ表の列：label, description, twinned administrat…, page banner, country, Commons category）
- 例3：HKG.6_1 | HKG.7_1 | HKG.10_1 | HKG.17_1 | HKG.1_1（表：district of Hong Kong／同じ表の列：label, description, shares border with, Commons category, located in the admi…, locator map image）

## g0374 — wikidbs10k：見出し「point in time」（Wikidata の型 `time`）（203 列）
- 例1：-0526-01-01T00:00:00Z | -0525-01-01T00:00:00Z | -0522-01-01T00:00:00Z | -0520-01-01T00:00:00Z | -0524-01-01T00:00:00Z（表：520s BC／同じ表の列：label, description, instance of, topic's main catego…, follows, followed by）
- 例2：-0523-01-01T00:00:00Z | -0527-01-01T00:00:00Z | -0526-01-01T00:00:00Z | -0521-01-01T00:00:00Z | -0524-01-01T00:00:00Z（表：followed by／同じ表の列：label, description, topic's main catego…, instance of, follows, followed by）
- 例3：-0522-01-01T00:00:00Z | -0529-01-01T00:00:00Z | -0528-01-01T00:00:00Z | -0521-01-01T00:00:00Z | -0526-01-01T00:00:00Z（表：follows／同じ表の列：label, description, instance of, topic's main catego…, follows, followed by）

## g0375 — wikidbs10k：見出し「participant in」（Wikidata の型 `wikibase-entityid`）（201 列）
- 例1：UCI Asia Tour 2021 | 2020 UCI Asia Tour | 2019 UCI World Ranking | 2009–10 UCI Asia Tour | 2018 UCI Asia Tour（表：Seoul Cycling Team／同じ表の列：label, description, sport, instance of, season of club or t…, start time）
- 例2：2015 UCI World Tour | 2016 UCI World Tour | 2019 Giro di Toscana | 2021 UCI World Ranking | 2013 UCI World Tour（表：Ineos Grenadiers／同じ表の列：label, description, instance of, sport, UCI code of cycling…, general manager）
- 例3：2021 UCI World Ranking | 2017 UCI World Tour | 2016 UCI World Tour | 2020 UCI World Ranking | 2012 UCI World Tour（表：followed by／同じ表の列：label, description, instance of, sport, UCI code of cycling…, follows）

## g0376 — sotab_v2：元の種類 `https://dbpedia.org/ontology/gender`（199 列）
- 例1：male
- 例2：Male | Female
- 例3：N/A

## g0377 — wikidbs10k：見出し「reactome id」（Wikidata の型 `string`）（194 列）
- 例1：R-HSA-1660517 | R-HSA-1660516 | R-HSA-1660510 | R-HSA-1660514 | R-HSA-1660502（表：PI Metabolism／同じ表の列：label, description, found in taxon, instance of, cites work, part of）
- 例2：R-HSA-5263628 | R-HSA-445700 | R-HSA-9620103 | R-HSA-9708104 | R-HSA-5263633（表：Smooth Muscle Contraction／同じ表の列：label, description, found in taxon, instance of, part of, exact match）
- 例3：R-HSA-1500761 | R-HSA-1222363 | R-HSA-1222594 | R-HSA-1500804 | R-HSA-1222583（表：Tolerance by Mtb to nitric oxide produc…／同じ表の列：label, description, cites work, instance of, found in taxon, part of）

## g0378 — wikidbs10k：見出し「gss code (2011)」（Wikidata の型 `string`）（193 列）
- 例1：S12000050 | E12000007 | S12000017 | S92000003 | S12000010（表：administrative territorial entity／同じ表の列：label, description, category of associa…, Curlie ID, MusicBrainz area ID, ISO 3166-2 code）
- 例2：S19000517 | S20000101 | S20000479 | S20000426 | S20000352（表：capital city／同じ表の列：label, description, instance of, Commons category, coordinate location, twinned administrat…）
- 例3：S12000010 | E92000001 | S12000017 | S12000035 | S12000033（表：administrative centre／同じ表の列：label, description, instance of, capital, country, ISO 3166-2 code）

## g0379 — wikidbs10k：見出し「new zealand organisms register id」（Wikidata の型 `string`）（193 列）
- 例1：32116111-135c-49ec-8149-57f5d7852c3f | 9c4126a8-6312-4118-b38d-a3b52faa738e | 00e3f95c-e293-4eed-b219-d2e5257a96ea | 5ccf28c7-8503-4500-b39a-29876be9d904 | 4b5b50f7-b7e9-44c2-8441-99008d828af2（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：f5eaafab-517c-45aa-81d4-8621b304d373 | bb94751c-bb26-4894-b858-b1b82be82961 | cf012e80-9da5-4fe5-9402-47feed5cd3a4 | 7443fb52-185f-440b-96c1-7c21df8c9d9d | 507532e6-d254-4597-8dba-9c8254b63b6e（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例3：173e62bf-ffa0-480d-9487-5295d1c2287a | a74e3123-4581-4ac3-a203-69199188cbd3 | 23d61159-b6e6-43dd-8246-77321ff5ea9f | 18b0303d-81c3-4442-b594-929ce543c5bf | df5ada9b-c2ff-4bd7-872f-fc9d08825a06（表：taxon／同じ表の列：label, description, taxon rank, taxon name, parent taxon, Freebase ID）

## g0380 — wikidbs10k：見出し「field of this occupation」（Wikidata の型 `wikibase-entityid`）（193 列）
- 例1：economics | management | critique | study of history | writing（表：occupation／同じ表の列：label, description, subclass of, Commons category, instance of, GND ID）
- 例2：squash | judo | field hockey | rugby | amateur wrestling（表：intentional human activity／同じ表の列：label, description, topic's main catego…, subclass of, instance of, Commons category）
- 例3：association football | yachting | handball | water polo | volleyball（表：intentional human activity／同じ表の列：label, description, instance of, subclass of, topic's main catego…, Commons category）

## g0381 — wikidbs10k：見出し「ipni plant id」（Wikidata の型 `string`）（189 列）
- 例1：503113-1 | 494336-1 | 606368-1 | 854675-1 | 851544-1（表：natural product／同じ表の列：label, description, taxon name, taxon rank, parent taxon, NCBI taxonomy ID）
- 例2：19808-1 | 22503-1 | 295478-2 | 30027054-2 | 327220-2（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例3：7004-1 | 99597-3 | 9619-1 | 30275681-2 | 77126727-1（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g0382 — wikidbs10k：見出し「tropicos id」（Wikidata の型 `string`）（189 列）
- 例1：22800744 | 100469946 | 21300900 | 21300910 | 13019856（表：natural product／同じ表の列：label, description, taxon name, taxon rank, parent taxon, NCBI taxonomy ID）
- 例2：40015478 | 40007100 | 35000216 | 40011147 | 40008681（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例3：9200572.0 | 18401720.0 | 4100071.0 | 2710604.0 | 50241850.0（表：secretion or excretion／同じ表の列：label, description, taxon name, taxon rank, parent taxon, instance of）

## g0383 — wikidbs10k：見出し「replaced by」（Wikidata の型 `wikibase-entityid`）（188 列）
- 例1：Aomori | Tsugaru | Sapporo | Odate | Kuroishi（表：replaced entity／同じ表の列：label, description, instance of, country, located in the admi…, dissolved, abolishe…）
- 例2：Florida | Pennsylvania | New York | New Jersey | Ontario（表：replaced entity／同じ表の列：label, description, topic's main catego…, Freebase ID, inception, dissolved, abolishe…）
- 例3：Hussein Fahri Pasha Cabinet | 3rd Mamdouh Salem's ministry | Ali Lotfy Ministry | Kamal Hassan Ali Ministry | Second Mustafa Riad Pasha Cabinet（表：Cabinet of Egypt／同じ表の列：label, description, instance of, dissolved, abolishe…, inception, replaces）

## g0384 — wikidbs10k：見出し「plants of the world online id」（Wikidata の型 `string`）（187 列）
- 例1：urn:lsid:ipni.org:names:606506-1 | urn:lsid:ipni.org:names:496941-1 | urn:lsid:ipni.org:names:606368-1 | urn:lsid:ipni.org:names:854675-1 | urn:lsid:ipni.org:names:496952-1（表：natural product／同じ表の列：label, description, taxon name, taxon rank, parent taxon, NCBI taxonomy ID）
- 例2：urn:lsid:ipni.org:names:22025-1 | urn:lsid:ipni.org:names:22503-1 | urn:lsid:ipni.org:names:1911-1 | urn:lsid:ipni.org:names:331730-2 | urn:lsid:ipni.org:names:19808-1（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例3：urn:lsid:ipni.org:names:30000630-2 | urn:lsid:ipni.org:names:30275681-2 | urn:lsid:ipni.org:names:7004-1 | urn:lsid:ipni.org:names:327393-2 | urn:lsid:ipni.org:names:279485-1（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g0385 — wikidbs10k：見出し「marine regions geographic id」（Wikidata の型 `string`）（186 列）
- 例1：2389 | 4247 | 1908 | 1904 | 4307（表：body of water／同じ表の列：label, description, instance of, VIAF ID, part of, Commons category）
- 例2：3384.0 | 2101.0 | 2098.0 | 2172.0 | 2237.0（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：2170 | 2172 | 2101 | 2098 | 2120（表：citizenship／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0386 — sotab_v2：元の種類 `RestrictedDiet`（185 列）
- 例1：LowFatDiet | LowCalorieDiet | VeganDiet | VegetarianDiet | GlutenFreeDiet
- 例2：VegetarianDiet | GlutenFreeDiet | VeganDiet
- 例3：VeganDiet | GlutenFreeDiet

## g0387 — wikidbs10k：見出し「icon」（Wikidata の型 `string`）（183 列）
- 例1：Lacrosse pictogram.svg | Basketball pictogram.svg | Football pictogram.svg | Bandy pictogram.svg | Ice hockey pictogram.svg（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, Commons category, subclass of, topic's main catego…）
- 例2：Boxing pictogram.svg | Athletics pictogram.svg | Badminton pictogram.svg | Judo pictogram.svg | Table tennis pictogram.svg（表：type of sport／同じ表の列：label, description, subclass of, Commons category, Library of Congress…, topic's main catego…）
- 例3：Weightlifting pictogram.svg | Shooting pictogram.svg | Diving pictogram.svg | Wrestling pictogram.svg | Rugby union pictogram.svg（表：field of work／同じ表の列：label, description, subclass of, Commons category, Library of Congress…, topic's main catego…）

## g0388 — wikidbs10k：見出し「glottolog code」（Wikidata の型 `string`）（181 列）
- 例1：swed1254 | stan1290 | stan1293 | kore1280 | stan1288（表：language／同じ表の列：label, description, Great Russian Encyc…, Art & Architecture …, PSH ID, ISO 639-2 code）
- 例2：stan1288 | bulg1262 | nucl1643 | arab1395 | finn1318（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Art & Architecture …, ISO 639-2 code）
- 例3：slov1268 | stan1290 | poli1260 | ital1282 | czec1258（表：language／同じ表の列：label, description, Great Russian Encyc…, Art & Architecture …, PSH ID, ISO 639-2 code）

## g0389 — wikidbs10k：見出し「ietf language tag」（Wikidata の型 `string`）（181 列）
- 例1：en | pt | ko | fr | cs（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：es | ar | en | nl | be（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：it | da | pl | ca | es（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0390 — wikidbs10k：見出し「iso 639-3 code」（Wikidata の型 `string`）（180 列）
- 例1：por | swe | eng | ces | kor（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：est | tur | ces | swe | ukr（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：fra | slv | fin | cat | eng（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0391 — wikidbs10k：見出し「ethnologue.com language code」（Wikidata の型 `string`）（178 列）
- 例1：pol | ara | spa | fin | fra（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：bul | est | spa | eng | ukr（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：ces | fra | cat | fin | dan（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0392 — wikidbs10k：見出し「cites work」（Wikidata の型 `wikibase-entityid`）（173 列）
- 例1：The type Ialpha inositol polyphosphate … | ArPIKfyve homomeric and heteromeric int… | Type I phosphatidylinositol-4-phosphate… | Phosphatidylinositol transfer proteins:… | Type I phosphatidylinositol-4,5-bisphos…（表：PI Metabolism／同じ表の列：label, description, found in taxon, Reactome ID, instance of, part of）
- 例2：Phosphoinositide kinases. | The road taken: past and future foundat… | Cloning and subcellular localization of… | Stabilized phosphatidylinositol-5-phosp… | Identification of a novel domain in two…（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）
- 例3：Invited review: cross-bridge regulation… | Mibefradil block of cloned T-type calci… | In vivo imaging of molecular interactio… | Membrane repair defects in muscular dys… | Contribution of aldehyde dehydrogenase …（表：Smooth Muscle Contraction／同じ表の列：label, description, found in taxon, Reactome ID, instance of, part of）

## g0393 — wikidbs10k：見出し「indigenous to」（Wikidata の型 `wikibase-entityid`）（172 列）
- 例1：Finland | Portugal | Kymenlaakso | Brussels-Capital Region | England（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：Finland | England | Maramureș County | Slovakia | Turks（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：Schleswig-Holstein | England | Czech Republic | Brussels-Capital Region | Wales（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0394 — wikidbs10k：見出し「part of the series」（Wikidata の型 `wikibase-entityid`）（170 列）
- 例1：The Legend of Zelda（表：work／同じ表の列：label, description, genre, platform, game mode, instance of）
- 例2：Quantum Leap | The 100 | Raising Dion | The Big Bang Theory | The Umbrella Academy（表：season finale／同じ表の列：label, description, instance of, follows, followed by, IMDb ID）
- 例3：The Blacklist | The X-Files | hart aber fair | Servant | Mord mit Aussicht（表：television series season／同じ表の列：label, description, instance of, number of episodes, has part(s), original language o…）

## g0395 — wikidbs10k：見出し「mesh tree code」（Wikidata の型 `string`）（169 列）
- 例1：B03.353.750.737.872.750 | B03.353.750.250.250.300 | B03.300.390.400.158.218.252 | B03.353.750.450.475.850 | B03.353.750.737.872.100（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：A03.556.875.875.440 | A10.615.284.981 | A08.186.211.180.497.342.650 | A05.360.319.114.630 | A06.407.747.608（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Foundational Model …, described by source, JSTOR topic ID）
- 例3：A10.549.750 | A08.186.211.180.590.500 | A07.231.114.186.200.210 | A07.015.114.186.200.230 | A08.186.211.132.659.687（表：expressed in／同じ表の列：label, description, Terminologia Anatom…, Commons category, subclass of, Freebase ID）

## g0396 — wikidbs10k：見出し「main subject」（Wikidata の型 `wikibase-entityid`）（168 列）
- 例1：biochemistry | pharmacology | cell biology | urology | science（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：Mycobacterium tuberculosis | Escherichia coli | macrophage | cell biology | Mycobacterium smegmatis（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）
- 例3：science | mutation | biochemistry | pharmacology | chemistry（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）

## g0397 — wikidbs10k：見出し「psh id」（Wikidata の型 `string`）（166 列）
- 例1：6752 | 6748 | 6756 | 6746 | 6759（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, ISO 639-2 code）
- 例2：6751 | 6754 | 6760 | 6759 | 13956（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, ISO 639-2 code）
- 例3：10044 | 9942 | 9986 | 9948 | 9988（表：field of work／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）

## g0398 — wikidbs10k：見出し「category for the view of the item」（Wikidata の型 `wikibase-entityid`）（163 列）
- 例1：Category:Views of the province of Cádiz | Category:Views of the province of A Cor… | Category:Views of Álava-Araba | Category:Views of the province of Barce… | Category:Views of Alt Camp（表：political border／同じ表の列：label, description, INE municipality co…, Dewey Decimal Class…, located in the admi…, ISO 3166-2 code）
- 例2：Category:Views of Jaén | Category:Views of Albacete | Category:Views of the province of Girona | Category:Views of the province of Huesca | Category:Views of the province of Salam…（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, flag image, coat of arms image）
- 例3：Category:Views of Kwai Tsing District | Category:Views of Eastern District, Hon… | Category:Views of Yuen Long District | Category:Views of North District, Hong … | Category:Views of Tsuen Wan District（表：district of Hong Kong／同じ表の列：label, description, shares border with, Commons category, located in the admi…, locator map image）

## g0399 — sotab_v2：元の種類 `Recipe/description`（162 列）
- 例1：<p class=\"p1\">Do you love adding chee… | <p class=\"p1\">These Apple Chips are p… | Healthier dessert recipe, indulge in th… | To understand the level of crunchiness … | This recipe is really easy and is the p…
- 例2：Here is a delicious weekday dinner fill… | A delicious soup recipe packed with chi… | A healthy breakfast option for people o… | A light bubbly Christmas cocktail with … | A taste of Mardi Gras for breakfast or …
- 例3：How to make a homemade graham cracker c… | Blueberry Buttermilk Pancakes from scra… | How to make homemade ham gravy with cor… | Chocolate sandwich cookies are a favori… | How to make chocolaty heart shaped Vale…

## g0400 — wikidbs10k：見出し「eppo code」（Wikidata の型 `string`）（160 列）
- 例1：1TEPG | 1OCNG | 1DOJG | 1GYCG | 1EPHG（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Commons category, image）
- 例2：ESCHCO | PSDMSX | 1YERSG | 1ENTBG | AGRBTU（表：taxon／同じ表の列：label, description, taxon name, image, taxon rank, parent taxon）
- 例3：1RATTG | 1BRDRG | PSDMSX | 1RHABF | RIZBJA（表：taxon／同じ表の列：label, description, parent taxon, taxon name, Commons category, instance of）

## g0401 — wikidbs10k：見出し「facebook places id」（Wikidata の型 `string`）（160 列）
- 例1：108597575831927 | 109443045741694 | 108100545884661 | 109377799083423 | 899998603358698（表：Limassol District／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）
- 例2：103406119699791.0 | 109661199057125.0 | 410950462248619.0 | 107652272597510.0 | 113207895360794.0（表：political border／同じ表の列：label, description, coordinate location, located in time zone, GeoNames ID, locator map image）
- 例3：286230344894871.0 | 113207895360794.0 | 109193525773825.0 | 104138922957256.0 | 112430865439015.0（表：jurisdiction／同じ表の列：label, description, coordinate location, located in time zone, GeoNames ID, locator map image）

## g0402 — wikidbs10k：見出し「trunk prefix」（Wikidata の型 `string`）（160 列）
- 例1：06 | 1 | 8 | 0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：8.0 | 0.0 | 1.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：8 | 0（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, Libraries Australia…, coordinates of sout…）

## g0403 — wikidbs10k：見出し「australian educational vocabulary id」（Wikidata の型 `string`）（159 列）
- 例1：scot/7435 | scot/4734 | scot/5401 | scot/1490 | scot/7434（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：scot/6971 | scot/7439 | scot/7435 | scot/4734 | scot/305（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：scot/9048 | scot/41 | scot/1910 | scot/90 | scot/9273（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）

## g0404 — wikidbs10k：見出し「ethnologue language status」（Wikidata の型 `wikibase-entityid`）（158 列）
- 例1：1 National | 0 International（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：0 International | 1 National（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：0 International | 1 National | 2 Provincial（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0405 — wikidbs10k：見出し「regulates (molecular biology)」（Wikidata の型 `wikibase-entityid`）（158 列）
- 例1：DNA metabolic process | receptor catabolic process | pectin catabolic process | starch metabolic process | cellulose catabolic process（表：negative regulation of macromolecule me…／同じ表の列：label, description, Gene Ontology ID, subclass of, exact match, instance of）
- 例2：post-translational protein modification | histone modification | peptidyl-cysteine S-nitrosylation | protein glycosylation | protein polyglycylation（表：positive regulation of protein modifica…／同じ表の列：label, description, Gene Ontology ID, subclass of, exact match, instance of）
- 例3：glutathione biosynthetic process | inositol phosphate biosynthetic process | DNA biosynthetic process | sphingolipid biosynthetic process | dopamine biosynthetic process（表：regulation of cellular biosynthetic pro…／同じ表の列：label, description, Gene Ontology ID, subclass of, exact match, instance of）

## g0406 — wikidbs10k：見出し「german municipality key」（Wikidata の型 `string`）（156 列）
- 例1：09676452 | 09676133 | 09671111 | 06435015 | 09661000（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, located in the admi…, coat of arms image）
- 例2：10041100 | 02000000 | 04011000 | 08111000 | 12054000（表：headquarters／同じ表の列：label, description, twinned administrat…, page banner, country, Commons category）
- 例3：09473112 | 09473151 | 09473132 | 09473153 | 09473120（表：Stimmkreis Coburg／同じ表の列：label, description, country, Commons category, GND ID, coordinate location）

## g0407 — wikidbs10k：見出し「siren number」（Wikidata の型 `string`）（156 列）
- 例1：222100018.0 | 215403957.0 | 215505454.0 | 214401093.0 | 210200630.0（表：administrative territorial entity／同じ表の列：label, description, instance of, Commons category, located in the admi…, coordinate location）
- 例2：219400785.0 | 219200466.0 | 211800503.0 | 211800289 | 211300058（表：political border／同じ表の列：label, description, coordinate location, instance of, located in the admi…, shares border with）
- 例3：210104436 | 210100046 | 214800708 | 210103503 | 215500430（表：capital city／同じ表の列：label, description, official website, topic's main catego…, country, INSEE municipality …）

## g0408 — wikidbs10k：見出し「atomic number」（Wikidata の型 `quantity`）（155 列）
- 例1：+53（表：isotope of iodine／同じ表の列：label, description, decays to, subclass of, instance of, neutron number）
- 例2：+50 | +52 | +54 | +51 | +53（表：decays to／同じ表の列：label, description, subclass of, instance of, neutron number, spin quantum number）
- 例3：+10（表：neon／同じ表の列：label, description, subclass of, instance of, neutron number, spin quantum number）

## g0409 — wikidbs10k：見出し「uses」（Wikidata の型 `wikibase-entityid`）（155 列）
- 例1：penalty flag | baseball | handball | association football kit | bandy ball（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, Commons category, subclass of, topic's main catego…）
- 例2：bicycle | judogi | swimming pool | foil | handball（表：type of sport／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）
- 例3：tennis court | bicycle | association football kit | athletics track | handball（表：field of work／同じ表の列：label, description, OpenStreetMap tag o…, topic's main Wikime…, Commons category, BNCF Thesaurus ID）

## g0410 — wikidbs10k：見出し「géopatronyme id」（Wikidata の型 `string`）（154 列）
- 例1：MEIJER | BREWER | AIKEN | DORIA | HALSEMA（表：family name／同じ表の列：label, description, different from, native label, writing system, Caverphone）
- 例2：DEREK | JOHN | MARTIN | DANIEL | CAROL（表：family name identical to this given name／同じ表の列：label, description, instance of, different from, said to be the same…, writing system）
- 例3：MICHAEL | SEBASTIAN | MARTIN | WERNER | WOLFGANG（表：family name identical to this given name／同じ表の列：label, description, instance of, Soundex, Cologne phonetics, Caverphone）

## g0411 — wikidbs10k：見出し「neutron number」（Wikidata の型 `quantity`）（152 列）
- 例1：+89 | +90 | +78 | +74 | +63（表：isotope of iodine／同じ表の列：label, description, decays to, subclass of, instance of, atomic number）
- 例2：+69 | +56 | +64 | +79 | +61（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, spin quantum number）
- 例3：+15 | +24 | +13 | +18 | +20（表：neon／同じ表の列：label, description, subclass of, instance of, atomic number, spin quantum number）

## g0412 — wikidbs10k：見出し「ballots cast」（Wikidata の型 `quantity`）（150 列）
- 例1：+1555 | +576 | +673 | +241 | +1227（表：Catalan regional election 2015 in Segrià／同じ表の列：label, description, instance of, country, applies to jurisdic…, point in time）
- 例2：+3445 | +3034 | +4502 | +3090 | +3277（表：2016 Bolton Metropolitan Borough Counci…／同じ表の列：label, description, instance of, part of, country, point in time）
- 例3：3574 | 3270 | 4034 | 4531 | 3989（表：followed by／同じ表の列：label, description, instance of, part of, country, follows）

## g0413 — wikidbs10k：見出し「biblioteca nacional de españa id」（Wikidata の型 `string`）（150 列）
- 例1：XX146251 | XX139737 | XX113345 | XX253984 | XX128453（表：executive branch／同じ表の列：label, description, instance of, inception, headquarters locati…, official website）
- 例2：XX451208 | XX4575410 | XX451000 | XX4575389 | XX451164（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：XX4575384 | XX198590 | XX4575366 | XX454068 | XX450959（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0414 — wikidbs10k：見出し「insee municipality code」（Wikidata の型 `string`）（150 列）
- 例1：75115.0 | 92075.0 | 30189.0 | 6123.0 | 97411.0（表：administrative territorial entity／同じ表の列：label, description, instance of, Commons category, located in the admi…, coordinate location）
- 例2：21231 | 18050.0 | 55545 | 48023.0 | 75106.0（表：political border／同じ表の列：label, description, coordinate location, instance of, located in the admi…, shares border with）
- 例3：78498 | 48070 | 02722 | 55043 | 44143（表：capital city／同じ表の列：label, description, official website, topic's main catego…, country, Commons category）

## g0415 — sotab_v2：元の種類 `Product/description`（149 列）
- 例1：Used 24' gondola run with base and 24 a… | Bottom Shelf Label Holder Price include… | Reconditioned 4' gondola run with base … | Used Light Gray 16' gondola run 60\"H x… | Reconditioned 24' gondola run with base…
- 例2：Bleach VS Naruto 2.9 is a fighting game… | You can play One Piece VS Naruto 4.0 on… | Fight the most famous heroes in the his… | The fourth part is the favorite of our … | Masked Forces counter strike 1.6 warzon…
- 例3：146 images. Riley self shot nude set in… | Lexi and Alyssa play in the park | 22 year old Samantha hanging out in pub… | Pepper, Cassandra and Ashley having fun… | Cassandra candid shots in public

## g0416 — wikidbs10k：見出し「olympedia event id」（Wikidata の型 `string`）（148 列）
- 例1：11096 | 11138 | 11075 | 11033 | 11012（表：sailing at the 2004 Summer Olympics／同じ表の列：label, description, part of, instance of, follows, number of participa…）
- 例2：10807 | 10660 | 10786 | 10828 | 10702（表：follows／同じ表の列：label, description, part of, instance of, point in time, sport）
- 例3：11075 | 11117 | 11159 | 10991 | 10949（表：followed by／同じ表の列：label, description, part of, instance of, follows, number of participa…）

## g0417 — wikidbs10k：見出し「wikimedia language code」（Wikidata の型 `string`）（148 列）
- 例1：cs | pl | fi | sv | fr（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：cs | pl | es | uk | tr（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：it | fr | da | cy | is（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0418 — wikidbs10k：見出し「cgndb unique id」（Wikidata の型 `string`）（147 列）
- 例1：ESFOC | ESELQ | ESFFP | ESEYH | ESDRC（表：floral habitat of Quebec／同じ表の列：label, description, instance of, country, located in the admi…, coordinate location）
- 例2：EHLEQ | ESBHD | ERJDP | EKTTX | EPILV（表：administrative territorial entity／同じ表の列：label, description, country, coordinate location, located in the admi…, instance of）
- 例3：ENODO | EIAZX | ERGUP | EQKZW | EIAON（表：political border／同じ表の列：label, description, country, located in the admi…, coordinate location, instance of）

## g0419 — wikidbs10k：見出し「facebook id」（Wikidata の型 `string`）（147 列）
- 例1：mairie18e | mairiedu20 | mairiedu15 | mairiedu16 | mairie19（表：administrative territorial entity／同じ表の列：label, description, instance of, Commons category, located in the admi…, coordinate location）
- 例2：CBS | nbc | itv | netflix | ABSCBNnetwork（表：television channel／同じ表の列：label, description, inception, Commons category, instance of, official website）
- 例3：departement13 | CalvadosDep | RegionGuadeloupe | paris | regionreunion（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, topic's main Wikime…, Commons category, country）

## g0420 — wikidbs10k：見出し「posix locale identifier」（Wikidata の型 `string`）（146 列）
- 例1：cs | en | pt | fr | ar（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：es | ar | bg | pt | ja（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：fi | fr | it | nl | cs（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0421 — wikidbs10k：見出し「linguistic typology」（Wikidata の型 `wikibase-entityid`）（145 列）
- 例1：subject–object–verb | subject–verb–object（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：free-order language | subject–object–verb | subject–verb–object（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：subject–object–verb | verb–subject–object | subject–verb–object（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0422 — wikidbs10k：見出し「electorate」（Wikidata の型 `quantity`）（144 列）
- 例1：+115483 | +17974 | +8326 | +15057 | +14043（表：jurisdiction／同じ表の列：label, description, located in the admi…, country, instance of, Commons category）
- 例2：+6423 | +28945 | +17612 | +46336 | +29500（表：political border／同じ表の列：label, description, country, coordinate location, Commons category, Freebase ID）
- 例3：+50070 | +12435 | +12458 | +23531 | +31384（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, GeoNames ID, instance of）

## g0423 — wikidbs10k：見出し「chemical formula」（Wikidata の型 `string`）（144 列）
- 例1：C30H22O9 | C20H18O5 | C30H18O12 | C24H22O8 | C22H22O4（表：3C-substituted chalcone／同じ表の列：label, description, instance of, PubChem CID, InChI, InChIKey）
- 例2：C27H29Br4N7O7 | C21H24Br3N3O5 | C22H24Br3N3O4 | C22H25Br4N3O7 | C21H23Br4N3O6（表：spirobenzoxazoline alkaloid／同じ表の列：label, description, mass, PubChem CID, InChI, instance of）
- 例3：C15H16N2O3 | C24H21N3O2 | C15H14N2O3 | C14H16N2O2 | C17H16N2O3（表：benzodiazepine alkaloid／同じ表の列：label, description, instance of, InChIKey, isomeric SMILES, PubChem CID）

## g0424 — wikidbs10k：見出し「ringgold id」（Wikidata の型 `string`）（144 列）
- 例1：113464.0 | 96228.0 | 114424 | 143640 | 146380.0（表：political border／同じ表の列：label, description, page banner, Commons category, located in the admi…, country）
- 例2：143549 | 146378 | 115535 | 146380 | 99569（表：administrative centre／同じ表の列：label, description, Commons category, located in the admi…, country, shares border with）
- 例3：60059 | 535372 | 73191 | 374816 | 53264（表：publisher／同じ表の列：label, description, official website, Freebase ID, headquarters locati…, instance of）

## g0425 — wikidbs10k：見出し「lingua libre id」（Wikidata の型 `string`）（143 列）
- 例1：Q386 | Q219 | Q298 | Q22 | Q126（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：Q35 | Q298 | Q303 | Q44 | Q302（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：Q35 | Q141 | Q22 | Q203 | Q298（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0426 — wikidbs10k：見出し「compulsory education (minimum age)」（Wikidata の型 `quantity`）（142 列）
- 例1：5.0 | 6.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：+5 | +7 | +6（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：+6 | +5 | +7（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0427 — wikidbs10k：見出し「iso 639-2 code」（Wikidata の型 `string`）（142 列）
- 例1：por | dut | eng | pol | ara（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：bel | dut | ara | hun | est（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：wel | spa | ces | fre | ice（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0428 — wikidbs10k：見出し「page(s)」（Wikidata の型 `string`）（141 列）
- 例1：52689-99 | 16834-16839 | 1441-1474 | 301-311 | 393-404（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）
- 例2：302-308 | 515-29 | 769-777 | 421–426 | 15894-15902（表：citation／同じ表の列：label, description, title, author name string, publication date, issue）
- 例3：583–593 | 3364-3366 | 9416–9426 | 1303–1314 | 6333-6338（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）

## g0429 — wikidbs10k：見出し「volume」（Wikidata の型 `string`）（141 列）
- 例1：1 | 46 | 16 | 273 | 6（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）
- 例2：385 | 160 | 159 | 284 | 260（表：citation／同じ表の列：label, description, page(s), title, author name string, publication date）
- 例3：45 | 5 | 374 | 280 | 188（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）

## g0430 — wikidbs10k：見出し「is a list of」（Wikidata の型 `wikibase-entityid`）（141 列）
- 例1：National Register of Historic Places（表：monument／同じ表の列：label, description, Commons category, country, instance of）
- 例2：Pokémon species | fictional character（表：part／同じ表の列：label, description, instance of, has part(s)）
- 例3：National Register of Historic Places（表：monument／同じ表の列：label, description, Commons category, country, instance of）

## g0431 — wikidbs10k：見出し「participating team」（Wikidata の型 `wikibase-entityid`）（141 列）
- 例1：BC Vignanello | Acqui Badminton | SC Meran | BC Pyrgi Santa Marinella | Forze Armate（表：Coppa Italia／同じ表の列：label, description, sport, on focus list of Wi…, instance of, country）
- 例2：Georgia Tech Yellow Jackets men's baske… | Michigan Wolverines men's basketball | Syracuse Orange men's basketball | Minnesota Golden Gophers men's basketba… | Arkansas Razorbacks men's basketball（表：1989 NCAA Men's Division I Basketball T…／同じ表の列：label, description, sport, point in time, league, Sports-Reference.co…）
- 例3：Lothian | Glasgow | West Strathclyde | West of Scotland | Midland（表：Scottish Team Badminton Championships／同じ表の列：label, description, instance of, country, sport, competition class）

## g0432 — wikidbs10k：見出し「category for films in this language」（Wikidata の型 `wikibase-entityid`）（140 列）
- 例1：Category:Dutch-language films | Category:Finnish-language films | Category:Czech-language films | Category:Swedish-language films | Category:French-language films（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：Category:Swedish-language films | Category:Polish-language films | Category:Finnish-language films | Category:Czech-language films | Category:Dutch-language films（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：Category:Danish-language films | Category:Dutch-language films | Category:Welsh-language films | Category:Czech-language films | Category:Polish-language films（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0433 — wikidbs10k：見出し「male form of label」（Wikidata の型 `monolingualtext`）（138 列）
- 例1：ممثل | Kolumnist | публицист | سياسي | منفذ（表：occupation／同じ表の列：label, description, subclass of, Commons category, field of this occup…, instance of）
- 例2：Waasserballspiller | Volleyballspiller | متسابق يخت | Handballspiller | Liichtathlet（表：intentional human activity／同じ表の列：label, description, instance of, subclass of, field of this occup…, topic's main catego…）
- 例3：natistulo | atirador desportivo | баскетболист | Judoka | ginnasta artistico（表：intentional human activity／同じ表の列：label, description, instance of, subclass of, field of this occup…, Commons category）

## g0434 — wikidbs10k：見出し「iso 639-1 code」（Wikidata の型 `string`）（138 列）
- 例1：es | pl | ko | en | sv（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：lv | pl | fi | bg | ja（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：is | pl | es | en | it（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0435 — wikidbs10k：見出し「publisher」（Wikidata の型 `wikibase-entityid`）（137 列）
- 例1：National Academy of Sciences | American Society for Pharmacology and E… | Portland Press | Oxford University Press | Nature Portfolio（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例2：American Chemical Society | Academic Press | National Academy of Sciences | Lippincott Williams & Wilkins | American Society for Pharmacology and E…（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, Scopus source ID）
- 例3：Books That Work | MicroProse | Infogrames Interactive | Nintendo | IBM（表：video game retail package／同じ表の列：label, description, platform, publication date, part of, instance of）

## g0436 — wikidbs10k：見出し「distribution map」（Wikidata の型 `string`）（136 列）
- 例1：Distribution-sv.png | Anglospeak (subnational version).svg | Detailed SVG map of the Lusophone world… | Detailed SVG map of the Hispanophone wo… | Map of Czech language.svg（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：Detailed SVG map of the Lusophone world… | Idioma bielorruso.png | Rozsireni madarstiny.PNG | Bul1.png | Latvaldialekti.svg（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：Anglospeak (subnational version).svg | Finnish language map, detailed areas.png | Siaradwyr y Gymraeg ym Mhrif Ardaloedd … | Detailed SVG map of the Hispanophone wo… | Map of Czech language.svg（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0437 — wikidbs10k：見出し「inchikey」（Wikidata の型 `string`）（136 列）
- 例1：TVUGLERLRIQATC-BJMVGYQFSA-N | HUSLZNYNWSUNJK-VBXOUWBXSA-N | KAZSKMJFUPEHHW-UHFFFAOYSA-N | DRHHMLLFTQIHIJ-UHFFFAOYSA-N | QRXMETOOCJOASL-OKGZUJFWSA-N（表：3C-substituted chalcone／同じ表の列：label, description, instance of, PubChem CID, chemical formula, InChI）
- 例2：KCVKPVRAUSPLPZ-MMMKZMAHSA-N | CFXBKEVRDPAWHM-ZBUVAEISSA-N | SYYVXQOWLOEXDU-TUXGATLDSA-N | FTTKFBVNRPXAKA-BZFILIQBSA-N | JGFXDUSJSHIVCW-BDYUSTAISA-N（表：spirobenzoxazoline alkaloid／同じ表の列：label, description, mass, PubChem CID, InChI, instance of）
- 例3：SNAVUESMLHTSHM-HNNXBMFYSA-N | ILVPUOFERZHGNR-MQJVFOOVSA-N | QVMOQPKRVNMMQP-PCAWENJQSA-N | QYBGEUDXQJVALS-KRWDZBQOSA-N | QEILHZZUMSPTRX-KWQFWETISA-N（表：benzodiazepine alkaloid／同じ表の列：label, description, instance of, chemical formula, isomeric SMILES, PubChem CID）

## g0438 — wikidbs10k：見出し「pubchem cid」（Wikidata の型 `string`）（136 列）
- 例1：75306643 | 162918115 | 77908593 | 11949444 | 162911273（表：3C-substituted chalcone／同じ表の列：label, description, instance of, chemical formula, InChI, InChIKey）
- 例2：162965981 | 162931898 | 162893198 | 10372965 | 162999667（表：spirobenzoxazoline alkaloid／同じ表の列：label, description, mass, InChI, instance of, chemical formula）
- 例3：551139 | 6443556 | 139588816 | 49788445 | 151569（表：benzodiazepine alkaloid／同じ表の列：label, description, instance of, chemical formula, InChIKey, isomeric SMILES）

## g0439 — wikidbs10k：見出し「abs ascl 2011 code」（Wikidata の型 `string`）（133 列）
- 例1：1201 | 4202 | 3602 | 2101 | 2303（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：3403 | 4301 | 1601 | 3502 | 4202（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：1501 | 2301 | 1201 | 1103 | 1502（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0440 — wikidbs10k：見出し「cna topic id」（Wikidata の型 `string`）（133 列）
- 例1：germany | south-africa | china | south-korea | israel（表：country／同じ表の列：label, description, Great Russian Encyc…, WIPO ST.3, population, Getty Thesaurus of …）
- 例2：italy | north-korea | austria | japan | australia（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：australia | italy | japan | canada | germany（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0441 — wikidbs10k：見出し「gost 7.75–97 code」（Wikidata の型 `string`）（133 列）
- 例1：фин 740 | исп 230 | нид 495 | чеш 790 | фра 745（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）
- 例2：пол 540 | лаш 385 | эст 850 | фра 745 | шве 805（表：language／同じ表の列：label, description, Great Russian Encyc…, Commons category, Glottolog code, Art & Architecture …）
- 例3：фра 745 | пол 540 | слв 610 | исп 230 | чеш 790（表：language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, PSH ID）

## g0442 — sotab_v2：元の種類 `Movie/description`（132 列）
- 例1：Danny Lupo, manager of the Sun Gym in 1… | Featuring never-before-seen footage, co… | Five young mutants, just discovering th… | When his daughter is kidnapped, a retir… | Ed Hemsler spends his life preparing fo…
- 例2：After accidentally stumbling into his u… | A group of friends’ attempt to repair t… | Artemis Fowl, a young criminal prodigy,… | Milla, a seriously ill teenager falls i… | Ben Marcus “Michael Jr.”, a former stan…
- 例3：At the height of the First World War, t… | Sophie Deraspe’s adaptation of the clas… | An adventure-loving couple convince the… | A crime/thriller about two old friends … | A one night stand turns into a living n…

## g0443 — wikidbs10k：見出し「french public service directory id」（Wikidata の型 `string`）（132 列）
- 例1：ile-de-france/seine-saint-denis/mairie-… | auvergne-rhone-alpes/ain/mairie-01249-01 | hauts-de-france/aisne/mairie-02064-01 | pays-de-la-loire/loire-atlantique/mairi… | ile-de-france/hauts-de-seine/mairie-920…（表：administrative territorial entity／同じ表の列：label, description, instance of, Commons category, located in the admi…, coordinate location）
- 例2：auvergne-rhone-alpes/ain/mairie-01038-01 | ile-de-france/hauts-de-seine/mairie-920… | ile-de-france/val-d-oise/mairie-95277-01 | ile-de-france/hauts-de-seine/mairie-920… | nouvelle-aquitaine/vienne/mairie-86007-…（表：political border／同じ表の列：label, description, coordinate location, instance of, located in the admi…, shares border with）
- 例3：nouvelle-aquitaine/charente-maritime/ma… | bourgogne-franche-comte/cote-d-or/mairi… | auvergne-rhone-alpes/ain/mairie-01249-01 | la-reunion/reunion/mairie-97408-01 | auvergne-rhone-alpes/ain/mairie-01443-01（表：capital city／同じ表の列：label, description, official website, topic's main catego…, country, INSEE municipality …）

## g0444 — wikidbs10k：見出し「successful candidate」（Wikidata の型 `wikibase-entityid`）（131 列）
- 例1：Champak Mistry | Clifford Morris | Asif Ibrahim | Christine Wild | Martin Donaghy（表：2016 Bolton Metropolitan Borough Counci…／同じ表の列：label, description, instance of, part of, country, point in time）
- 例2：Stuart Haslam | Ismail Ibrahim | Maureen Flitcroft | Martin McMulkin | Mudasir Dean（表：followed by／同じ表の列：label, description, instance of, part of, country, follows）
- 例3：Debbie Newall | Anna-Marie Watters | Jackie Radcliffe | Rees Gibbon | Martin Donaghy（表：follows／同じ表の列：label, description, instance of, part of, country, point in time）

## g0445 — wikidbs10k：見出し「collection」（Wikidata の型 `wikibase-entityid`）（129 列）
- 例1：Royal Collection（表：Windsor Beauties／同じ表の列：label, description, inventory number, instance of, location, made from material）
- 例2：National Trust | Royal Collection（表：depicting object／同じ表の列：label, description, inventory number, instance of, location, made from material）
- 例3：Documents of the Bethlen Gábor Foundati… | Periodical Auseklis Collection | Operation Tuškanac in the Croatian Stat… | Censored Theatre and Cinema Ad-hoc Coll… | Pavel Doronin Collection at SIS Archive…（表：grey literature／同じ表の列：label, description, instance of, COURAGE ID, language of work or…, inception）

## g0446 — wikidbs10k：見出し「inchi」（Wikidata の型 `string`）（128 列）
- 例1：InChI=1S/C23H22O6/c1-23(2)10-9-16-18(29… | InChI=1S/C30H22O8/c31-19-6-1-17(2-7-19)… | InChI=1S/C20H20O6/c1-20(2)18(25)9-12-7-… | InChI=1S/C21H22O4/c1-13(2)14(3)18-11-16… | InChI=1S/C21H22O4/c1-14(2)4-11-18-20(24…（表：3C-substituted chalcone／同じ表の列：label, description, instance of, PubChem CID, chemical formula, InChIKey）
- 例2：InChI=1S/C26H30Br4N4O7/c1-39-19-13(27)8… | InChI=1S/C24H26Br4N4O8/c1-37-17-11(25)7… | InChI=1S/C27H36Br4N4O10/c1-40-26(41-2)1… | InChI=1S/C24H24Br4N4O9/c1-38-17-11(25)5… | InChI=1S/C24H26Br4N4O8/c1-37-17-11(25)7…（表：spirobenzoxazoline alkaloid／同じ表の列：label, description, mass, PubChem CID, instance of, chemical formula）
- 例3：InChI=1S/C15H18N2O/c1-2-5-11-8-12-9-16-… | InChI=1S/C12H14N2O3/c15-9-5-1-3-7-10(9)… | InChI=1S/C16H20N2O4/c1-4-9-5-12-15(22-3… | InChI=1S/C14H18N2O5/c1-20-12-4-8-9(5-11… | InChI=1S/C15H16N2O3/c1-3-9-6-10-7-16-13…（表：benzodiazepine alkaloid／同じ表の列：label, description, instance of, chemical formula, InChIKey, isomeric SMILES）

## g0447 — wikidbs10k：見出し「social media followers」（Wikidata の型 `quantity`）（127 列）
- 例1：+12300 | +3788 | +50000 | +3693 | +7580（表：publisher／同じ表の列：label, description, official website, instance of, inception, headquarters locati…）
- 例2：7237 | 13269 | 7421 | 3376 | 10009（表：administrative territorial entity／同じ表の列：label, description, instance of, Commons category, located in the admi…, coordinate location）
- 例3：+543461 | +7490000 | +3267312 | +998000 | +21446888（表：television channel／同じ表の列：label, description, inception, Commons category, instance of, official website）

## g0448 — wikidbs10k：見出し「catalan vikidia id」（Wikidata の型 `string`）（127 列）
- 例1：Camerun | Palau | Alemanya | Papua_Nova_Guinea | Jordània（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Perú | Xile | Veneçuela | Costa_Rica | Equador（表：country／同じ表の列：label, description, VIAF ID, continent, Wikimedia outline, BBC Things ID）
- 例3：Mèxic | Alemanya | Austràlia | Àustria | Corea_del_Nord（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0449 — wikidbs10k：見出し「tripadvisor id」（Wikidata の型 `string`）（127 列）
- 例1：8149200 | 12869277 | 8551819 | 23553285 | 10317891（表：Jōmon Prehistoric Sites in Northern Jap…／同じ表の列：label, description, Commons category, coordinate location, instance of, country）
- 例2：8400890 | 8403161 | 8635557 | 2044221 | 8322453（表：operator／同じ表の列：label, description, Commons category, instance of, topic's main catego…, Freebase ID）
- 例3：28967 | 28956 | 153339 | 28946 | 28937（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）

## g0450 — wikidbs10k：見出し「issue」（Wikidata の型 `string`）（126 列）
- 例1：43 | 1-2 | 29 | 5 | Pt 19（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）
- 例2：23 | 6 | Pt 3 | 2 | 4（表：citation／同じ表の列：label, description, page(s), title, author name string, publication date）
- 例3：5 | Pt 3 | 3 | 15 | 4（表：citation／同じ表の列：label, description, title, instance of, author name string, published in）

## 答えの雛形

```
g0301	
g0302	
g0303	
g0304	
g0305	
g0306	
g0307	
g0308	
g0309	
g0310	
g0311	
g0312	
g0313	
g0314	
g0315	
g0316	
g0317	
g0318	
g0319	
g0320	
g0321	
g0322	
g0323	
g0324	
g0325	
g0326	
g0327	
g0328	
g0329	
g0330	
g0331	
g0332	
g0333	
g0334	
g0335	
g0336	
g0337	
g0338	
g0339	
g0340	
g0341	
g0342	
g0343	
g0344	
g0345	
g0346	
g0347	
g0348	
g0349	
g0350	
g0351	
g0352	
g0353	
g0354	
g0355	
g0356	
g0357	
g0358	
g0359	
g0360	
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
```
