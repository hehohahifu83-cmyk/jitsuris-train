# 銀ラベルのシート 008 / 008（外の学習データの読み替え）

- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列
- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`
- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を、ChatGPT は `answers/sheet_008.tsv`、Grok は `answers_grok/sheet_008.tsv` に写して埋める。**相手の答えは見ない**

## g1051 — wikidbs10k：見出し「conferred by」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：United Nations Office on Drugs and Crime | United Nations Industrial Development O… | United Nations Development Programme | UNESCO | Food and Agriculture Organization（表：Goodwill Ambassador／同じ表の列：label, description, instance of, subclass of）
- 例2：Pamplona City Hall | Ayuntamiento de Cartagena | Zaragoza City Hall | Madrid City Hall | Córdoba City Hall（表：Adoptive Son／同じ表の列：label, description, instance of, subclass of）
- 例3：Emperor of Japan（表：Order of the Precious Crown／同じ表の列：label, description, instance of, part of, inception, category for recipi…）

## g1052 — wikidbs10k：見出し「feast day」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：November 30 | October 7 | March 19 | July 4 | January 17（表：patron saint／同じ表の列：label, description, Library of Congress…, Commons category, VIAF ID, ISNI）
- 例2：November 8 | December 6 | June 24 | August 28 | June 13（表：patron saint／同じ表の列：label, description, Commons category, instance of, topic's main catego…, Freebase ID）
- 例3：September 8 | August 15 | November 30 | November 8 | July 15（表：eponym／同じ表の列：label, description, Commons category, instance of, described by source, image）

## g1053 — wikidbs10k：見出し「located on astronomical body」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：Mercury | Pluto | Enceladus | Ceres | Moon（表：planitia／同じ表の列：label, description, coordinate location, instance of, Gazetteer of Planet…, length）
- 例2：Pluto | Titan | Moon | Mars（表：lacus／同じ表の列：label, description, instance of, named after, Gazetteer of Planet…, length）
- 例3：Moon | Callisto | Ganymede | 4 Vesta | Rhea（表：crater chain／同じ表の列：label, description, instance of, Gazetteer of Planet…, length, Google Knowledge Gr…）

## g1054 — wikidbs10k：見出し「position held」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：member of Bolton Metropolitan Borough C…（表：candidate／同じ表の列：label, description, instance of, name, occupation, member of political…）
- 例2：member of Bury Metropolitan Borough Cou… | Member of the 58th Parliament of the Un…（表：candidate／同じ表の列：label, description, instance of, name, occupation, member of political…）
- 例3：member of the European Parliament | member of Trafford Metropolitan Borough…（表：candidate／同じ表の列：label, description, Democracy Club cand…, instance of, name, occupation）

## g1055 — wikidbs10k：見出し「programming paradigm」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：constraint programming | object-oriented programming | logic programming | procedural programming | systems programming（表：functional programming language／同じ表の列：label, description, instance of, Freebase ID, inception, official website）
- 例2：prototype-based programming | generic programming | dataflow programming | object-oriented programming | functional programming（表：object-based language／同じ表の列：label, description, instance of, official website, Freebase ID, inception）
- 例3：imperative programming | declarative programming | stack-oriented programming | constraint programming | multi-paradigm programming（表：multi-paradigm programming language／同じ表の列：label, description, instance of, official website, Freebase ID, influenced by）

## g1056 — wikidbs10k：見出し「recording or performance of」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：The Man With the Child in His Eyes | Wow | December Will Be Magic Again | Breathing | Sat In Your Lap（表：tracklist／同じ表の列：label, description, instance of, title, performer, published in）
- 例2：Prelude no. 16 in B-flat minor, Op. 28 | Hungarian Rhapsody No. 15 | Hungarian Rhapsody No. 12 | Poissons d'or | Waltz No. 7 in C-sharp minor, Op. 64, N…（表：music roll release／同じ表の列：label, description, instance of, title, catalog code, performer）
- 例3：You're the Only One | Think About Love | Starting Over Again | All I Can Do | Love Is Like a Butterfly（表：tracklist／同じ表の列：label, description, instance of, title, has quality, performer）

## g1057 — wikidbs10k：見出し「set in period」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：Hyborian Age（表：Conan non-canonical works／同じ表の列：label, description, instance of, author, genre, publication date）
- 例2：24th century（表：The Final Chapter／同じ表の列：label, description, IMDb ID, part of the series, director, screenwriter）
- 例3：24th century（表：follows／同じ表の列：label, description, IMDb ID, part of the series, instance of, country of origin）

## g1058 — wikidbs10k：見出し「terminus location」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：Ōyamazaki | Nantan | Tsuruga | Kameoka | Ikeda（表：of／同じ表の列：label, description, instance of, country, located in the admi…, transport network）
- 例2：Miyazu | Suita | Maizuru | Nantan | Osaka（表：connects with／同じ表の列：label, description, Commons category, country, instance of, located in the admi…）
- 例3：Yokkaichi | Chūō-ku | Kyoto | Ayabe | Maizuru（表：terminus／同じ表の列：label, description, instance of, coordinate location, country, located in the admi…）

## g1059 — wikidbs10k：見出し「tributary」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：Diemel | Murr | Woblitz | Regnitz | Nied（表：body of water／同じ表の列：label, description, mouth of the waterc…, instance of, Commons category, country）
- 例2：Seiche | Naugatuck River | Madawaska River | Mga | Pienne（表：crossing／同じ表の列：label, description, instance of, Commons category, image, coordinate location）
- 例3：Una River | Loison | Acheneau | Chicopee River | Seiche（表：river mouth／同じ表の列：label, description, Commons category, instance of, coordinate location, country）

## g1060 — wikidbs10k：見出し「density」（Wikidata の型 `quantity`）（7 列）
- 例1：+1.85 | +2.162 | +3.344 | +5.427 | +5.243（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, image）
- 例2：+3.456 | +3.344 | +1.8344 | +1.237 | +3933（表：located on astronomical body／同じ表の列：label, description, apparent magnitude, orbital eccentricity, GND ID, parent astronomical…）
- 例3：+0.99 | +0.62 | +0.92 | +0.88 | +0.81（表：Class IC flammable liquid／同じ表の列：label, description, chemical structure, CAS Registry Number, canonical SMILES, Commons category）

## g1061 — wikidbs10k：見出し「number of cylinders」（Wikidata の型 `quantity`）（7 列）
- 例1：+3（表：SR Merchant Navy class／同じ表の列：label, description, instance of, manufacturer, named after, Commons category）
- 例2：+3（表：Shay locomotive／同じ表の列：label, description, instance of, track gauge, Commons category, image）
- 例3：+2（表：Prussian P 8／同じ表の列：label, description, located in the admi…, instance of, country, part of）

## g1062 — wikidbs10k：見出し「number of seats in legislature」（Wikidata の型 `quantity`）（7 列）
- 例1：+30 | +5 | +4 | +60 | +3（表：2016 Moroccan general election／同じ表の列：label, description, instance of, country, office contested, point in time）
- 例2：+2 | +3 | +4 | +6 | +5（表：follows／同じ表の列：label, description, point in time, candidate, office contested, instance of）
- 例3：+5 | +4 | +6 | +3 | +2（表：followed by／同じ表の列：label, description, instance of, country, office contested, point in time）

## g1063 — wikidbs10k：見出し「topographic prominence」（Wikidata の型 `quantity`）（7 列）
- 例1：+3957 | +3980 | +5509 | +3098 | +2776（表：highest point／同じ表の列：label, description, instance of, continent, coordinate location, country）
- 例2：830.0 | 788.0 | 841.0 | 477.0 | 880.0（表：highest point／同じ表の列：label, description, instance of, coordinate location, country, elevation above sea…）
- 例3：+5885 | +6961 | +6155 | +4892 | +4741（表：Seven Summits／同じ表の列：label, description, country, instance of, Commons category, GND ID）

## g1064 — wikidbs10k：見出し「belgian species list id」（Wikidata の型 `string`）（7 列）
- 例1：56181 | 58720 | 55586 | 55585 | 58731（表：taxon／同じ表の列：label, description, MycoBank taxon name…, Encyclopedia of Lif…, taxon rank, taxon name）
- 例2：55962 | 29892.0 | 56878.0 | 56342.0 | 55941（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例3：2643 | 23609 | 23933 | 2600 | 23805（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）

## g1065 — wikidbs10k：見出し「bien de interés cultural (bic) code」（Wikidata の型 `string`）（7 列）
- 例1：RI-52-0000024 | RI-52-0000088 | RI-52-0000042 | RI-52-0000052 | RI-52-0000087（表：Jardín histórico／同じ表の列：label, description, Commons category, coordinate location, image, located in the admi…）
- 例2：RI-51-0000627 | RI-51-0000339 | RI-51-0000967 | RI-51-0000054 | RI-51-0000771（表：cathedral／同じ表の列：label, description, located in the admi…, Commons category, Freebase ID, instance of）
- 例3：RI-51-0011168 | RI-51-0004439 | RI-51-0009287 | RI-51-0000367 | RI-51-0009133（表：cultural heritage in Alicante／同じ表の列：label, description, image, instance of, part of, Commons category）

## g1066 — wikidbs10k：見出し「common database on designated areas id」（Wikidata の型 `string`）（7 列）
- 例1：555545783 | 388922 | 555545787 | 388949 | 555545785（表：habitats or species management protecte…／同じ表の列：label, description, country, instance of, area, IUCN protected area…）
- 例2：342078 | 341999 | 342085 | 342030 | 342042（表：national nature reserve／同じ表の列：label, description, instance of, Commons category, ÚSOP code, country）
- 例3：6257 | 20642 | 12396 | 178272 | 6297（表：regional natural park／同じ表の列：label, description, Commons category, WDPA ID, IUCN protected area…, country）

## g1067 — wikidbs10k：見出し「dane code」（Wikidata の型 `string`）（7 列）
- 例1：66682 | 25290 | 73001 | 15516 | 05148（表：beginning／同じ表の列：label, description, country, coordinate location, instance of, Freebase ID）
- 例2：05390 | 17001 | 76834 | 66001 | 25019（表：location or destination point／同じ表の列：label, description, Commons category, flag image, country, coordinate location）
- 例3：25899 | 25307 | 25183 | 25843 | 25386（表：capital city／同じ表の列：label, description, country, coordinate location, instance of, Freebase ID）

## g1068 — wikidbs10k：見出し「document file on wikimedia commons」（Wikidata の型 `string`）（7 列）
- 例1：Sura50.pdf | Sura101.pdf | Sura54.pdf | Sura106.pdf | Sura12.pdf（表：surah／同じ表の列：label, description, instance of, Freebase ID, Commons category, has edition or tran…）
- 例2：People's Mujahedin of Iran, Political-M… | People's Mujahedin of Iran, Political-M… | People's Mujahedin of Iran, Political-M… | People's Mujahedin of Iran, Political-M… | People's Mujahedin of Iran, Political-M…（表：shabnameh／同じ表の列：label, description, instance of, distribution format, publication date, author）
- 例3：People's Mujahedin of Iran, Political-M… | AttemptedAssassinationofAmericanDiploma… | People's Mujahedin of Iran, Political-M… | People's Mujahedin of Iran, Political-M… | People's Mujahedin of Iran, Political-M…（表：followed by／同じ表の列：label, description, follows, instance of, author, country of origin）

## g1069 — wikidbs10k：見出し「gazetteer of planetary nomenclature id」（Wikidata の型 `string`）（7 列）
- 例1：1993 | 195 | 38 | 2968 | 14591（表：planitia／同じ表の列：label, description, coordinate location, instance of, located on astronom…, length）
- 例2：14319 | 14769 | 14314 | 14773 | 14655（表：lacus／同じ表の列：label, description, instance of, named after, located on astronom…, length）
- 例3：1069 | 1073 | 406 | 15063 | 1954（表：crater chain／同じ表の列：label, description, located on astronom…, instance of, length, Google Knowledge Gr…）

## g1070 — wikidbs10k：見出し「historic environment scotland id」（Wikidata の型 `string`）（7 列）
- 例1：LB81 | LB14761 | LB13158 | LB606 | LB1434（表：farm labourers cottage／同じ表の列：label, description, country, coordinate location, heritage designation, instance of）
- 例2：LB25497 | LB29887 | LB12425 | LB29886 | LB37281（表：workers cottage／同じ表の列：label, description, coordinate location, country, heritage designation, instance of）
- 例3：SM7739 | SM7680 | SM11638 | SM9728 | SM11639（表：scheduled section of Antonine Wall／同じ表の列：label, description, country, heritage designation, located in the admi…, coordinate location）

## g1071 — wikidbs10k：見出し「icd-10-cm」（Wikidata の型 `string`）（7 列）
- 例1：I45.8 | G72.3（表：long QT syndrome／同じ表の列：label, description, subclass of, OMIM ID, instance of, health specialty）
- 例2：G60.0（表：Charcot-Marie-Tooth disease intermediat…／同じ表の列：label, description, instance of, subclass of, Orphanet ID, MonDO ID）
- 例3：G40.3 | E75.4（表：neuronal ceroid lipofuscinosis／同じ表の列：label, description, exact match, instance of, MonDO ID, Orphanet ID）

## g1072 — wikidbs10k：見出し「israeli cbs municipal id」（Wikidata の型 `string`）（7 列）
- 例1：מא04 | מא32 | מא18 | מא42 | מא71（表：regional council of Israel／同じ表の列：label, description, coordinate location, topic's main catego…, Freebase ID, instance of）
- 例2：9800 | 3000 | 8500 | 6900 | 0078（表：administrative territorial entity／同じ表の列：label, description, population, VIAF ID, GeoNames ID, country）
- 例3：1195 | 1226 | 0442 | 1314 | 3765（表：community settlement／同じ表の列：label, description, coordinate location, Freebase ID, instance of, country）

## g1073 — wikidbs10k：見出し「iswc」（Wikidata の型 `string`）（7 列）
- 例1：T-010.003.127-3 | T-010.003.143-3 | T-010.003.112-6 | T-900.018.623-2 | T-010.003.106-8（表：audio recording／同じ表の列：label, description, instance of, title, language of work or…, composer）
- 例2：T-070.134.721-8 | T-070.136.682-6 | T-010.433.575-2 | T-901.131.693-1 | T-070.049.355-5（表：Great American Songbook／同じ表の列：label, description, MusicBrainz work ID, Freebase ID, instance of, language of work or…）
- 例3：T-902.848.093-5 | T-071.335.045-8 | T-003.104.922-5 | T-011.715.931-5 | T-902.149.817-9（表：arrangement on a work of the public dom…／同じ表の列：label, description, performer, instance of, MusicBrainz work ID, title）

## g1074 — wikidbs10k：見出し「libraries.org id」（Wikidata の型 `string`）（7 列）
- 例1：11466 | 11454 | 61465 | 11452 | 11468（表：Riverside County Library／同じ表の列：label, description, instance of, coordinate location, country, located in the admi…）
- 例2：15318 | 15332 | 15334 | 15322 | 15316（表：Sacramento Public Library／同じ表の列：label, description, location, Google Maps Custome…, country, fax number）
- 例3：15114 | 15149 | 15142 | 15135 | 15150（表：Los Angeles Public Library／同じ表の列：label, description, coordinate location, country, located in the admi…, instance of）

## g1075 — wikidbs10k：見出し「lumiere film id」（Wikidata の型 `string`）（7 列）
- 例1：115144.0 | 98960.0 | 125649.0 | 114113.0 | 115107.0（表：series／同じ表の列：label, description, instance of, IMDb ID, genre, original language o…）
- 例2：30449 | 24051 | 46829 | 80465 | 222245（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例3：82903 | 190833 | 195100 | 244226 | 23550（表：sequel film／同じ表の列：label, description, follows, instance of, IMDb ID, original language o…）

## g1076 — wikidbs10k：見出し「musicbrainz place id」（Wikidata の型 `string`）（7 列）
- 例1：b79276f3-e62a-4186-8041-e61cc9fe993b | 7f567c0c-8d6b-48b5-855f-366f87874587 | 875540e8-9d2c-4568-8477-923856def444 | 6028d8f8-46cb-483a-b084-13720bfb62dc | fbca5bc1-946f-4af2-a402-94efab2afb04（表：employer／同じ表の列：label, description, instance of, country, Commons category, coordinate location）
- 例2：6d7d3f1d-7603-481e-83fa-361b448190e2 | 4a7586d5-7a35-4f5b-b800-b38a2f2a464f | 4a8d38ac-0773-455b-afc5-d96e13ff78a5 | be1479b7-d0af-4283-a6fc-25567c940e6f | e0e36b52-c845-4e22-82e1-2648af3655fa（表：thesis／同じ表の列：label, description, Commons category, instance of, coordinate location, topic's main catego…）
- 例3：8b1037aa-7f49-4437-883a-ba1a63b74384 | 170f333b-b79c-4b78-88ac-e86647e039ae | fb27d6aa-38ad-4924-9e85-d06c9dc7cde4 | 248f0b72-aa41-4ced-abff-1d8952dbd55a | 4fa96d0a-2e9e-40b5-905c-8e30ce2dfea2（表：organization／同じ表の列：label, description, Commons category, instance of, coordinate location, country）

## g1077 — wikidbs10k：見出し「national park foundation id」（Wikidata の型 `string`）（7 列）
- 例1：craters-moon-national-monument-and-pres… | aniakchak-national-monument-and-preserve | great-sand-dunes-national-park-and-pres… | tallgrass-prairie-national-preserve | jean-lafitte-national-historic-park-pre…（表：national preserve／同じ表の列：label, description, Commons category, located in the admi…, IUCN protected area…, instance of）
- 例2：grand-canyon-parashant-national-monument | agate-fossil-beds-national-monument | white-house-and-presidents-park | birmingham-civil-rights-national-monume… | timpanogos-cave-national-monument（表：National Park System unit／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）
- 例3：eleanor-roosevelt-national-historic-site | william-howard-taft-national-historic-s… | andersonville-national-historic-site | boston-african-american-national-histor… | carl-sandburg-home-national-historic-si…（表：National Historic Site／同じ表の列：label, description, Commons category, NRHP reference numb…, coordinate location, country）

## g1078 — wikidbs10k：見出し「natureserve explorer id」（Wikidata の型 `string`）（7 列）
- 例1：2.1062653 | 2.1063273 | 2.911871 | 2.121953 | 2.1073112999999997（表：secretion or excretion／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：2.150845 | 2.160538 | 2.147862 | 2.134734 | 2.134974（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例3：2.150433 | 2.160538 | 2.139637 | 2.155094 | 2.142075（表：symbol／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g1079 — wikidbs10k：見出し「pepc park id」（Wikidata の型 `string`）（7 列）
- 例1：13 | 387 | 391 | 330 | 21（表：national preserve／同じ表の列：label, description, Commons category, located in the admi…, IUCN protected area…, instance of）
- 例2：212 | 92 | 240 | 345 | 318（表：National Park System unit／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）
- 例3：397 | 272 | 232 | 320 | 350（表：National Historic Site／同じ表の列：label, description, Commons category, NRHP reference numb…, coordinate location, country）

## g1080 — wikidbs10k：見出し「romanization of belarusian (2007 system)」（Wikidata の型 `string`）（7 列）
- 例1：Drahičyn | Orša | Slonim | Polacak | Kaściukovičy（表：capital city／同じ表の列：label, description, flag, Commons category, flag image, country）
- 例2：Vialiejka | Kapyĺ | Niaśviž | Mazyr | Ščučyn（表：capital city／同じ表の列：label, description, Commons category, flag image, coat of arms image, country）
- 例3：Drahičyn | Tamašoŭka | Drybin | Kamaryn | Daŭhinaŭ（表：urban settlement in Belarus／同じ表の列：label, description, Commons category, coordinate location, GeoNames ID, postal code）

## g1081 — wikidbs10k：見出し「spotify artist id」（Wikidata の型 `string`）（7 列）
- 例1：0lZoBs4Pzo7R89JM9lxwoT | 6YH4dTGIZZvVO55Sb3095Q | 3grHWM9bx2E9vwJCdlRv9O | 72OaDtakiy6yFqkt4TsiFt | 4U7lXyKdSf1JbM1aXvsodC（表：performing artist／同じ表の列：label, description, discography, MusicBrainz artist …, Commons category, image）
- 例2：54R6Y0I7jGUCveDTtI21nb | 562Od3CffWedyz2BbeYWVn | 3ICflSq6ZgYAIrm2CTkfVP | 1gv1pJZUv6mZIaYRezXE3C | 0JTujDbHVqhWAGl06aaW78（表：performing artist／同じ表の列：label, description, discography, MusicBrainz artist …, Commons category, image）
- 例3：3IJCdgkBZbieocLZ4e94GZ | 1xs6WFotNQSXweo0GXrS0O | 1R52cwGf75yTf7I3Q0Irf8 | 52zMTJCKluDlFwMQWmccY7 | 5LWkv2hDbDwZL3zNwZYNPx（表：performing artist／同じ表の列：label, description, Commons category, MusicBrainz artist …, instance of, genre）

## g1082 — wikidbs10k：見出し「spotify track id」（Wikidata の型 `string`）（7 列）
- 例1：1OeyUaxsSWYqJEzH81X3ue | 1PtXEYrahu8Vg2rhpJBoqt | 6OmdWLjlx4BIDGEO8BZlqH | 1EfdsCcge41LcPtSpkZJ50 | 1hbB7wFZ28n5vOfMEEY2Jw（表：tracklist／同じ表の列：label, description, instance of, title, performer, published in）
- 例2：1DLfR4MOfLYbV6v3xrmWa8 | 3lXyAQ0kekAvY5LodpWmUs | 1WHNqqRWhJVZIdCScFKtl5 | 2qFIJT5hjqaNFA1GKwl9me | 6SHI6STEW51cQkAXBRpLNj（表：Hamilton／同じ表の列：label, description, instance of, part of, MusicBrainz work ID, performer）
- 例3：2sEq2rC3ynYsT49x7utWnd | 6SHI6STEW51cQkAXBRpLNj | 68Ijc4fPmT3P5BN6Vrl2s2 | 1dZutYKh4BtPlxbC81wV34 | 7qfoq1JFKBUEIvhqOHzuqX（表：followed by／同じ表の列：label, description, instance of, part of, performer, MusicBrainz work ID）

## g1083 — wikidbs10k：見出し「utah history encyclopedia id」（Wikidata の型 `string`）（7 列）
- 例1：s/SEVIER_COUNTY | j/JUAB_COUNTY | e/EMERY_COUNTY | b/BEAVER_COUNTY | i/IRON_COUNTY（表：administrative territorial entity／同じ表の列：label, description, country, capital, shares border with, named after）
- 例2：d/DAGGETT_COUNTY | s/SUMMIT_COUNTY | r/RICH_COUNTY | s/SANPETE_COUNTY | u/UINTAH_COUNTY（表：administrative centre／同じ表の列：label, description, country, capital, shares border with, named after）
- 例3：g/GRAND_COUNTY | w/WASATCH_COUNTY | t/TOOELE_COUNTY | j/JUAB_COUNTY | m/MORGAN_COUNTY（表：county of Utah／同じ表の列：label, description, country, Commons category, located in the admi…, coordinate location）

## g1084 — wikidbs10k：見出し「affiliation」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：Lagos State University | Babcock University | Aminu Kano Teaching Hospital | Ladoke Akintola University of Technology | Obafemi Awolowo University Teaching Hos…（表：tertiary referral hospital／同じ表の列：label, description, official website, instance of, country, located in the admi…）
- 例2：Sweet Adelines International（表：barbershop quartet／同じ表の列：label, description, instance of, described at URL, victory, genre）
- 例3：Sweet Adelines International（表：winner／同じ表の列：label, description, instance of, described at URL, victory, genre）

## g1085 — wikidbs10k：見出し「class of station」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：Category C1 railway station | Category A railway station | Category B railway station | Category E railway station（表：London station group／同じ表の列：label, description, instance of, country, connecting line, Commons category）
- 例2：1st class station | 4th class station | Top Class station | 3rd class station（表：Chengdu railway junction／同じ表の列：label, description, Commons category, country, instance of, connecting line）
- 例3：Top Class station | 3rd class station | 4th class station（表：adjacent station／同じ表の列：label, description, instance of, country, connecting line, located in the admi…）

## g1086 — wikidbs10k：見出し「discography」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：One Ok Rock discography | Kenny Chesney discography | Metallica discography | Adele discography | Superbus discography（表：performing artist／同じ表の列：label, description, MusicBrainz artist …, Commons category, image, Freebase ID）
- 例2：Madness discography | Kanye West discography | Travis Scott discography | Chicane discography | Connie Francis discography（表：performing artist／同じ表の列：label, description, instance of, MusicBrainz artist …, genre, Freebase ID）
- 例3：Bob Dylan discography | Sam Cooke discography | Peter, Paul and Mary discography | Rod Stewart discography | Vince Guaraldi discography（表：performing artist／同じ表の列：label, description, MusicBrainz artist …, Commons category, image, instance of）

## g1087 — wikidbs10k：見出し「game mode」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：single-player video game（表：work／同じ表の列：label, description, part of the series, genre, platform, instance of）
- 例2：single-player video game | multiplayer video game | co-op mode（表：video game remake／同じ表の列：label, description, instance of, platform, publication date）
- 例3：multiplayer video game | hotseat | single-player video game（表：work／同じ表の列：label, description, instance of, publisher, developer, genre）

## g1088 — wikidbs10k：見出し「has vertex figure」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：small stellated dodecahedron | great stellated dodecahedron | great dodecahedron | regular dodecahedron | great icosahedron（表：star regular polychoron／同じ表の列：label, description, subclass of, image, has facet polytope, dual to）
- 例2：regular icosahedron | great icosahedron | small stellated dodecahedron | regular tetrahedron | great stellated dodecahedron（表：duality／同じ表の列：label, description, subclass of, image, has facet polytope, dual to）
- 例3：6-simplex | 10-simplex | pentachoron | triangle | line segment（表：simplex／同じ表の列：label, description, has facet polytope, Freebase ID, subclass of, has part(s) of the …）

## g1089 — wikidbs10k：見出し「health specialty」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：infectious diseases（表：alphavirus infections／同じ表の列：label, description, has cause, subclass of, instance of, disease transmissio…）
- 例2：cardiology | neurology（表：long QT syndrome／同じ表の列：label, description, subclass of, OMIM ID, instance of, Disease Ontology ID）
- 例3：veterinary medicine | infectious diseases（表：arbovirosis／同じ表の列：label, description, subclass of, has cause, instance of, disease transmissio…）

## g1090 — wikidbs10k：見出し「legislated by」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：Parliament of India（表：list of Acts of the Parliament of India…／同じ表の列：label, description, instance of, country, applies to jurisdic…, legal citation of t…）
- 例2：President of India 🚩⚔️🚩（表：Act of the President of India／同じ表の列：label, description, instance of, applies to jurisdic…, legal citation of t…, publication date）
- 例3：Parliament of India（表：based on／同じ表の列：label, description, instance of, applies to jurisdic…, enacted date, legal citation of t…）

## g1091 — wikidbs10k：見出し「notation」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：♌︎ | ♉︎ | ♈︎ | ♊ | ♍︎（表：occidental astrological sign／同じ表の列：label, description, Commons category, Freebase ID, instance of, image）
- 例2：♑︎ | ♋︎ | ♈︎ | ♍︎ | ♊（表：followed by／同じ表の列：label, description, Commons category, Freebase ID, instance of, image）
- 例3：♌︎ | ♏︎ | ♒︎ | ♓ | ♐︎（表：based on／同じ表の列：label, description, Commons category, topic's main catego…, instance of, Freebase ID）

## g1092 — wikidbs10k：見出し「organized response related to outbreak」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：2020 Virginia stay-at-home order | 2020 Republika Srpska COVID-19 closing … | 2020 The Bahamas COVID-19 curfew | 2020 Nebraska COVID-19 social distancing | 2020 Egypt COVID-19 travel ban（表：cause／同じ表の列：label, description, part of, country, location, coordinate location）
- 例2：2020 Utah COVID-19 declaration of publi… | 2020 United States Virgin Islands COVID… | 2020 Alaska stay-at-home order | 2020 Arkansas COVID-19 closing of educa… | 2020 Wyoming COVID-19 closing of educat…（表：COVID-19 pandemic in the United States／同じ表の列：label, description, part of, instance of, country, location）
- 例3：2020 Turkey COVID-19 travel restrictions | 2020 United Kingdom COVID-19 curfew | 2020 Spain COVID-19 curfew | 2020 Luxembourg COVID-19 travel restric… | 2020 Belgium COVID-19 social distancing（表：COVID-19 pandemic in Europe／同じ表の列：label, description, part of, country, number of cases, instance of）

## g1093 — wikidbs10k：見出し「programmed in」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：JavaScript | Python | C++ | C++11 | C#（表：encryption software／同じ表の列：label, description, instance of, copyright license, official website）
- 例2：Perl | Python | PHP | Rust | JavaScript（表：Internet forum software／同じ表の列：label, description, instance of, copyright license, official website, software version id…）
- 例3：JavaScript | Objective-C | C++ | Python | C（表：graphics library／同じ表の列：label, description, official website, copyright license, instance of, copyright status）

## g1094 — wikidbs10k：見出し「taxonomic type」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：Triticum aestivum | Micromonospora | Klebsiella pneumoniae | Micrococcus | Streptomyces（表：taxon／同じ表の列：label, description, Commons category, image, taxon rank, parent taxon）
- 例2：Lactarius torminosus | Armillaria mellea | Conocybe tenera | Boletus igniarius | Orchis（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, Commons category, image）
- 例3：Pseudomonas | Legionella | Elizabethkingia meningoseptica | Pasteurella | Rickettsia（表：taxon／同じ表の列：label, description, taxon name, Commons category, image, taxon rank）

## g1095 — wikidbs10k：見出し「theme music」（Wikidata の型 `wikibase-entityid`）（7 列）
- 例1：bass 8ths sample.wav | music of four's 3D hand（表：first appearance／同じ表の列：label, description, instance of, part of the series, title, season）
- 例2：bass 8ths sample.wav | music of four's 3D hand | Gibberish!!（表：followed by／同じ表の列：label, description, instance of, part of the series, title, season）
- 例3：music of four's 3D hand | bass 8ths sample.wav（表：follows／同じ表の列：label, description, instance of, part of the series, title, season）

## g1096 — wikidbs10k：見出し「unit symbol」（Wikidata の型 `monolingualtext`）（6 列）
- 例1：N m s | C/m2 | kg m/s | m−1 | Кл·м（表：unit of measurement／同じ表の列：label, description, instance of, measured physical q…, conversion to SI un…, Wolfram Language un…）
- 例2：$MN | ریال | د.ع | ¥ | ₱（表：unit of account／同じ表の列：label, description, Commons category, central bank/issuer, Freebase ID, instance of）
- 例3：P | Ba | St | Gal | dyn（表：centimeter–gram–second system of units／同じ表の列：label, description, instance of, part of, measured physical q…, conversion to SI un…）

## g1097 — wikidbs10k：見出し「admission rate」（Wikidata の型 `quantity`）（6 列）
- 例1：+0.14 | +0.63 | +0.12 | +0.06 | +0.81（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例2：+0.78 | +0.83 | +0.70 | +0.73 | +0.31（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）
- 例3：+0.57 | +0.55 | +0.35 | +0.0702 | +0.52（表：liberal arts college in the United Stat…／同じ表の列：label, description, instance of, coordinate location, country, topic's main catego…）

## g1098 — wikidbs10k：見出し「albedo」（Wikidata の型 `quantity`）（6 列）
- 例1：+0.136 | +0.090 | +0.689 | +0.76 | +0.071（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, image）
- 例2：+0.090 | +0.76 | +0.43 | +0.4228 | +0.65（表：located on astronomical body／同じ表の列：label, description, apparent magnitude, orbital eccentricity, GND ID, parent astronomical…）
- 例3：+0.06 | +0.071 | +0.044 | +0.43 | +0.6（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, time of discovery o…）

## g1099 — wikidbs10k：見出し「boiling point」（Wikidata の型 `quantity`）（6 列）
- 例1：-6 | +38 | +43 | -9 | -1（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：-169 | -12 | -135 | -127 | -6（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：+269 | +140 | +320 | +306 | +281（表：Class IC flammable liquid／同じ表の列：label, description, chemical structure, CAS Registry Number, canonical SMILES, Commons category）

## g1100 — wikidbs10k：見出し「effective temperature」（Wikidata の型 `quantity`）（6 列）
- 例1：+4698 | +8868.667 | +6050 | +5717.0 | +5364（表：primary body／同じ表の列：label, description, constellation, instance of, catalog code, apparent magnitude）
- 例2：4404.0 | 5527.0 | 4858.0 | 4158.0 | 5787.0（表：primary body／同じ表の列：label, description, constellation, spectral class, catalog code, instance of）
- 例3：+4742 | +12360 | +4155 | +9430 | +13960（表：navigational star／同じ表の列：label, description, constellation, instance of, catalog code, Freebase ID）

## g1101 — wikidbs10k：見出し「number of seasons」（Wikidata の型 `quantity`）（6 列）
- 例1：19.0 | 9.0 | 3.0 | 11.0 | 15.0（表：series／同じ表の列：label, description, instance of, IMDb ID, genre, original language o…）
- 例2：+45 | +72 | +58 | +9 | +54（表：work／同じ表の列：label, description, original broadcaster, IMDb ID, country of origin, topic's main catego…）
- 例3：+2 | +1（表：Kamen Rider Series／同じ表の列：label, description, genre, IMDb ID, Freebase ID, instance of）

## g1102 — wikidbs10k：見出し「aics chemical id (being deleted)」（Wikidata の型 `string`）（6 列）
- 例1：2755 | 4788 | 1083 | 1857 | 5449（表：Class IC flammable liquid／同じ表の列：label, description, chemical structure, CAS Registry Number, canonical SMILES, Commons category）
- 例2：2854 | 1036 | 2656 | 2946 | 2341（表：cause／同じ表の列：label, description, chemical structure, CAS Registry Number, canonical SMILES, Commons category）
- 例3：2865 | 758 | 927 | 2705 | 4078（表：Class IB flammable liquid／同じ表の列：label, description, RTECS number, CAS Registry Number, EC number, chemical formula）

## g1103 — wikidbs10k：見出し「chembl id」（Wikidata の型 `string`）（6 列）
- 例1：CHEMBL45462 | CHEMBL16200 | CHEMBL443470 | CHEMBL45354 | CHEMBL269630（表：Class IC flammable liquid／同じ表の列：label, description, chemical structure, CAS Registry Number, canonical SMILES, Commons category）
- 例2：CHEMBL3187409 | CHEMBL155926 | CHEMBL816 | CHEMBL3187981 | CHEMBL1398949（表：cause／同じ表の列：label, description, chemical structure, CAS Registry Number, canonical SMILES, Commons category）
- 例3：CHEMBL1357 | CHEMBL22587 | CHEMBL27 | CHEMBL606 | CHEMBL91（表：essential medicine／同じ表の列：label, description, Freebase ID, DrugBank ID, ATC code, NDF-RT ID）

## g1104 — wikidbs10k：見出し「chgis id」（Wikidata の型 `string`）（6 列）
- 例1：41113 | 42308 | 85157 | 1118 | 130（表：ancestral home／同じ表の列：label, description, instance of, country, located in the admi…）
- 例2：33512 | 9604 | 32336 | 111020 | 9516（表：administrative territorial entity／同じ表の列：label, description, country, instance of）
- 例3：122334 | 43491 | 122677 | 973 | 40409（表：ting／同じ表の列：label, description, instance of, country, located in the admi…）

## g1105 — wikidbs10k：見出し「conway polyhedron notation」（Wikidata の型 `string`）（6 列）
- 例1：bD | aC | eC | sC | aD（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）
- 例2：kD | eC | gC | eD | tI（表：duality／同じ表の列：label, description, Commons category, Freebase ID, has facet polytope, dual to）
- 例3：tC | sC | aD | eD | aC（表：depiction／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）

## g1106 — wikidbs10k：見出し「cq ranking women's race id」（Wikidata の型 `string`）（6 列）
- 例1：4596 | 2694 | 10042 | 15994 | 6259（表：Croatia National Road Cycling Champions…／同じ表の列：label, description, instance of, country, sport, point in time）
- 例2：13676 | 4596 | 11466 | 3859 | 7949（表：followed by／同じ表の列：label, description, instance of, sport, country, point in time）
- 例3：7949 | 6259 | 11466 | 20364 | 4596（表：follows／同じ表の列：label, description, instance of, sport, country, point in time）

## g1107 — wikidbs10k：見出し「czech district id」（Wikidata の型 `string`）（6 列）
- 例1：3404.0 | 3708.0 | 3207.0 | 3209.0 | 3714.0（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, ISO 3166-2 code, OpenStreetMap relat…）
- 例2：3208 | 3508 | 3305 | 3402 | 3303（表：districts of the Czech Republic／同じ表の列：label, description, instance of, country, population, Commons category）
- 例3：3212.0 | 3701.0 | 3710.0 | 3605.0 | 3804.0（表：political border／同じ表の列：label, description, Commons category, located in the admi…, country, LAU）

## g1108 — wikidbs10k：見出し「dreadnought project page」（Wikidata の型 `string`）（6 列）
- 例1：Courbet_Class_Battleship_(1911) | Bellerophon_Class_Battleship_(1907) | Andrea_Doria_Class_Battleship_(1912) | Orion_Class_Battleship_(1910) | Pennsylvania_Class_Battleship_(1915)（表：vessel class／同じ表の列：label, description, Commons category, instance of, subclass of, topic's main catego…）
- 例2：H.M.S._Havock_(1893) | H.M.S._Hardy_(1895) | H.M.S._Swordfish_(1895) | H.M.S._Ferret_(1893) | H.M.S._Banshee_(1894)（表：A-class destroyer／同じ表の列：label, description, topic's main catego…, instance of, subclass of, Freebase ID）
- 例3：H.M.S._Havock_(1893) | H.M.S._Fervent_(1895) | H.M.S._Conflict_(1894) | H.M.S._Ferret_(1893) | H.M.S._Banshee_(1894)（表：eponym／同じ表の列：label, description, instance of, manufacturer, vessel class, short name）

## g1109 — wikidbs10k：見出し「eunis id for species」（Wikidata の型 `string`）（6 列）
- 例1：189121 | 172457 | 178871 | 153132 | 189099（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例2：185219 | 165045 | 175866 | 184226 | 178871（表：symbol／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例3：163691.0 | 171391.0 | 172115.0 | 192448.0 | 164206.0（表：secretion or excretion／同じ表の列：label, description, taxon name, taxon rank, image, Commons category）

## g1110 — wikidbs10k：見出し「fifa country code」（Wikidata の型 `string`）（6 列）
- 例1：ENG | ALG | IND | PRK | LVA（表：women's national under-17 association f…／同じ表の列：label, description, sport, competition class, instance of, country for sport）
- 例2：TGA | FRO | USA | FIJ | CHN（表：proprietor／同じ表の列：label, description, Freebase ID, instance of, sport, country）
- 例3：BAH | IND | CMR | TAH | IRN（表：national beach soccer team／同じ表の列：label, description, sport, owned by, instance of, country）

## g1111 — wikidbs10k：見出し「galaxy morphological type」（Wikidata の型 `string`）（6 列）
- 例1：SB0 | -2.0 | 3.5 | Sa | SBa（表：[CHM2007] LDC 916／同じ表の列：label, description, catalog code, instance of, SIMBAD ID, apparent magnitude）
- 例2：dIrr IV/BCD | Irr | ImIV-V | E2 | 10（表：Local Group／同じ表の列：label, description, instance of, part of, Freebase ID, constellation）
- 例3：SAcd | SBcd | Sb | E-SO | SAm（表：[CHM2007] LDC 867／同じ表の列：label, description, image, constellation, Commons category, catalog code）

## g1112 — wikidbs10k：見出し「handbook of texas id」（Wikidata の型 `string`）（6 列）
- 例1：hcc01 | hcb11 | hck03 | hcm12 | hcw01（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, Commons category, country, coordinate location）
- 例2：hcd09 | hcw11 | hcb03 | hcv02 | hck02（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：hch06 | hcw10 | hcb07 | hch19 | hca02（表：administrative centre／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g1113 — wikidbs10k：見出し「heritage gazetteer of libya id」（Wikidata の型 `string`）（6 列）
- 例1：1342 | 2061 | 1327 | 1298 | 1363（表：Late Antiquity／同じ表の列：label, description, part of, instance of, country, coordinate location）
- 例2：1368 | 1304 | 2083 | 1380 | 1300（表：Cyrenaica／同じ表の列：label, description, country, instance of, coordinate location, part of）
- 例3：1440 | 1306 | 1058 | 1077 | 911（表：part／同じ表の列：label, description, country, instance of）

## g1114 — wikidbs10k：見出し「hov-id」（Wikidata の型 `string`）（6 列）
- 例1：28146 | 24037 | 11162 | 4105 | 5241（表：administrative territorial entity／同じ表の列：label, description, country, coordinate location, located in the admi…, GeoNames ID）
- 例2：17041 | 3293 | 29099 | 23190 | 27079（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, German municipality…, coordinate location）
- 例3：16005 | 14004 | 28064 | 24025 | 11290（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, coordinate location, instance of）

## g1115 — wikidbs10k：見出し「imo ship number」（Wikidata の型 `string`）（6 列）
- 例1：9466726 | 9790672 | 9753648 | 9452775 | 9365269（表：chemical tanker／同じ表の列：label, description, instance of, length, Commons category, service entry）
- 例2：6509371 | 8601915 | 7023104 | 8969044 | 8306486（表：car ferry／同じ表の列：label, description, instance of, Commons category, image, manufacturer）
- 例3：5266489 | 7525918 | 6715102 | 6510887 | 7232406（表：Seebäderschiff／同じ表の列：label, description, Commons category, instance of, image, draft）

## g1116 — wikidbs10k：見出し「isil」（Wikidata の型 `string`）（6 列）
- 例1：JP-1001790 | JP-1002849 | JP-1000591 | JP-1002579 | JP-1000561（表：municipal library of Japan／同じ表の列：label, description, instance of, country, official website, image）
- 例2：JP-1002958 | JP-1002771 | JP-1000599 | JP-1000440 | JP-1002299（表：prefectural library of Japan／同じ表の列：label, description, instance of, coordinate location, country, postal code）
- 例3：DE-Bre1 | DE-Ma25 | DE-2191 | DE-1951 | DE-2367（表：archives／同じ表の列：label, description, Commons category, GND ID, instance of, country）

## g1117 — wikidbs10k：見出し「iso 15924 alpha-4 code」（Wikidata の型 `string`）（6 列）
- 例1：Qaai | Qaaq | Qabi | Qabo | Qaap（表：ISO 15924／同じ表の列：label, description, part of, instance of, authority, inception）
- 例2：Qabk | Qaah | Qabw | Qaaz | Qaal（表：followed by／同じ表の列：label, description, instance of, part of, inception, authority）
- 例3：Qaae | Qabo | Qabg | Qabs | Qaav（表：follows／同じ表の列：label, description, instance of, part of, authority, ISO 15924 numeric c…）

## g1118 — wikidbs10k：見出し「iso 15924 numeric code」（Wikidata の型 `string`）（6 列）
- 例1：921 | 906 | 928 | 940 | 937（表：ISO 15924／同じ表の列：label, description, part of, instance of, authority, inception）
- 例2：909 | 935 | 926 | 915 | 903（表：followed by／同じ表の列：label, description, instance of, part of, inception, authority）
- 例3：923 | 914 | 905 | 910 | 932（表：follows／同じ表の列：label, description, instance of, part of, authority, ISO 15924 alpha-4 c…）

## g1119 — wikidbs10k：見出し「letterboxd film id」（Wikidata の型 `string`）（6 列）
- 例1：blue-lagoon-the-awakening | hellraiser-2022 | doom-annihilation | mad-max-fury-road | the-mummy-1999（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例2：pickpocket-1997 | tuyas-marriage | on-the-beat-1995 | useless | in-love-we-trust（表：sixth generation Chinese films／同じ表の列：label, description, IMDb ID, instance of, director, original language o…）
- 例3：superman-ii | 12-rounds-2-reloaded | superman-iv-the-quest-for-peace | batman-v-superman-dawn-of-justice | batman-the-dark-knight-returns-part-2（表：sequel film／同じ表の列：label, description, follows, instance of, IMDb ID, original language o…）

## g1120 — wikidbs10k：見出し「mext school code」（Wikidata の型 `string`）（6 列）
- 例1：D201210300010 | D240321700014 | D211210300018 | D228210000012 | D213299900031（表：Secondary education school of Japan／同じ表の列：label, description, coordinate location, instance of, inception, country）
- 例2：G138110110488 | G106110101263 | G124110107265 | G146110111726 | G122110106419（表：college of technology in Japan／同じ表の列：label, description, coordinate location, instance of, country, NDL Authority ID）
- 例3：H123310000106 | H123310000080 | H108320300021 | H123310000437 | H110310000156（表：professional training college／同じ表の列：label, description, country, instance of, located in the admi…）

## g1121 — wikidbs10k：見出し「naif id」（Wikidata の型 `string`）（6 列）
- 例1：499 | 401 | 606 | 602 | 199（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, image）
- 例2：301 | 604 | 801 | 2000004 | 199（表：located on astronomical body／同じ表の列：label, description, apparent magnitude, orbital eccentricity, GND ID, parent astronomical…）
- 例3：299 | 2025143 | 2000021 | 2002867 | 401（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, time of discovery o…）

## g1122 — wikidbs10k：見出し「nomenclature for museum cataloging」（Wikidata の型 `string`）（6 列）
- 例1：14458 | 14561 | 14510 | 14490 | 12614（表：use／同じ表の列：label, description, Commons category, subclass of, Freebase ID, image）
- 例2：2356 | 2373 | 2361 | 2587 | 2662（表：depiction／同じ表の列：label, description, Commons category, subclass of, image, Art & Architecture …）
- 例3：14531 | 14458 | 12131 | 14510 | 14501（表：use／同じ表の列：label, description, image, subclass of, sport, Commons category）

## g1123 — wikidbs10k：見出し「onestop id」（Wikidata の型 `string`）（6 列）
- 例1：s-9vfgpy2sy4-dfwairportterminalbstation | s-9q9zbjz7f2-stockton | s-dn6m9rj3bb-riverfrontstation | s-9whj4qr0qs-belenstation | s-9qbejfrrgr-sonomacountyairportsmart（表：terminus／同じ表の列：label, description, coordinate location, country, located in the admi…, instance of）
- 例2：r-dr4ed-foxchaseline | r-dr4e-trentonline | r-dr47-media~elwynline | r-dr4e9-chestnuthillwestline | r-dr4e2-cynwydline（表：SEPTA Regional Rail／同じ表の列：label, description, Commons category, instance of, country, image）
- 例3：s-dr41sjtuxj-newarkamtrak | s-dr4e392krb-suburbanstation | s-dr4ebxdvyu-chestnuthillwest | s-dr4e3ymu7p-templeuniversity | s-dr4e302479-pennmedicinestation（表：terminus／同じ表の列：label, description, instance of, country, located in the admi…, adjacent station）

## g1124 — wikidbs10k：見出し「rate your music artist id」（Wikidata の型 `string`）（6 列）
- 例1：venetian-snares | good_clean_fun | process-is-dead | merzbow | mika-vainio（表：performing artist／同じ表の列：label, description, instance of, Discogs artist ID, work period (start), MusicBrainz artist …）
- 例2：lana-del-rey | ruben_rada | jamiroquai | julieta_venegas | iggy_azalea（表：performing artist／同じ表の列：label, description, instance of, MusicBrainz artist …, genre, Freebase ID）
- 例3：royksopp | roots_manuva | la_roux | dave_ralph | john_digweed（表：performing artist／同じ表の列：label, description, VIAF ID, MusicBrainz artist …, instance of, Freebase ID）

## g1125 — wikidbs10k：見出し「reporting mark」（Wikidata の型 `string`）（6 列）
- 例1：LKO | KUR | SBP | BPL | ASN（表：Indian Railways division／同じ表の列：label, description, country, topic's main catego…, instance of, parent organization）
- 例2：NER | SER | NFR | WCR | SECR（表：parent company／同じ表の列：label, description, instance of, country, has subsidiary, official website）
- 例3：BCT | APDJ | JP | IZN | BSP（表：subsidiary／同じ表の列：label, description, topic's main catego…, country, instance of, parent organization）

## g1126 — wikidbs10k：見出し「rijksmonument id」（Wikidata の型 `string`）（6 列）
- 例1：23724 | 513649 | 509452 | 35949 | 528458（表：Frisian farmhouse／同じ表の列：label, description, country, located in the admi…, coordinate location, image）
- 例2：420215 | 524036 | 524034 | 527309 | 527304（表：casemate／同じ表の列：label, description, instance of, part of, country, coordinate location）
- 例3：15943 | 38043 | 478203 | 37477 | 478326（表：Low German house／同じ表の列：label, description, country, coordinate location, heritage designation, image）

## g1127 — wikidbs10k：見出し「schläfli symbol」（Wikidata の型 `string`）（6 列）
- 例1：r{4,3} | t{3,3} | rr{4,3} | rr{5,3} | t{4,3}（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）
- 例2：tr{5,3} | r{4,3} | sr{4,3} | tr{4,3} | t{3,3}（表：depiction／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）
- 例3：{3,5,5/2} | {5/2,5,5/2} | {3,5/2,5} | {5/2,3,5} | {5,3,5/2}（表：star regular polychoron／同じ表の列：label, description, subclass of, image, has facet polytope, has vertex figure）

## g1128 — wikidbs10k：見出し「spotify album id」（Wikidata の型 `string`）（6 列）
- 例1：2bVr7AMmHlGmRtCI1A0cwf | 2CqqKibOf37WJgzmzvIrpc | 5IBEe4vD4ebuCzSlkCPiOi | 3DmfyjtfDRxMUCdoTgEWoz | 0R7Uw1tUUbWlV53BGKfjQ4（表：Glen Campbell US albums discography／同じ表の列：label, description, MusicBrainz release…, instance of, AllMusic album ID, title）
- 例2：34CsUCcaxu6Yorde5fRdTU | 4BKzjaLggvfdOTNo1fvgFM | 2fVaEkBaNRH9eDSYuThyA5 | 4kvVqavqTyVWqXURC0fRqF | 0Zk8n6BlFd7NEpMB3FiBf0（表：Booba discography／同じ表の列：label, description, instance of, record label, performer, follows）
- 例3：5TPqe17ygLtC7PhuSxAKdL | 2liUgYwfNNBPAoIpO2ny0z | 6yEGlMQ1AkXeDPERJTv2aN | 2dCUtmJ3qBS5nP2maHsGAf | 2fVaEkBaNRH9eDSYuThyA5（表：followed by／同じ表の列：label, description, performer, record label, instance of, MusicBrainz release…）

## g1129 — wikidbs10k：見出し「the encyclopedia of oklahoma history and culture id」（Wikidata の型 `string`）（6 列）
- 例1：TU008 | OK039 | WA035 | PI016 | BR028（表：county of Oklahoma／同じ表の列：label, description, Commons category, country, located in the admi…, named after）
- 例2：LO005 | PA025 | LA025 | PI016 | CR008（表：political border／同じ表の列：label, description, country, Commons category, located in the admi…, capital）
- 例3：HU002 | MC017 | GA017 | CO035 | KI019（表：administrative centre／同じ表の列：label, description, Commons category, country, located in the admi…, named after）

## g1130 — wikidbs10k：見出し「the video games museum system id」（Wikidata の型 `string`）（6 列）
- 例1：115 | 17 | 62 | 29 | 81（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例2：29 | 33 | 18 | 115 | 17（表：followed by／同じ表の列：label, description, instance of, manufacturer, image, Commons category）
- 例3：114 | 115 | 93 | 31 | 62（表：computing platform／同じ表の列：label, description, image, Commons category, manufacturer, follows）

## g1131 — wikidbs10k：見出し「tmdb tv series id」（Wikidata の型 `string`）（6 列）
- 例1：67198 | 88055 | 2284 | 4018 | 4614（表：series／同じ表の列：label, description, instance of, IMDb ID, genre, original language o…）
- 例2：910 | 874 | 1451 | 881 | 875（表：work／同じ表の列：label, description, original broadcaster, IMDb ID, country of origin, topic's main catego…）
- 例3：126456 | 129987 | 214856 | 125259 | 125048（表：Kamen Rider Series／同じ表の列：label, description, genre, IMDb ID, Freebase ID, instance of）

## g1132 — wikidbs10k：見出し「vglist video game id」（Wikidata の型 `string`）（6 列）
- 例1：1608 | 35320 | 20286 | 1618 | 411（表：work／同じ表の列：label, description, part of the series, genre, platform, game mode）
- 例2：11 | 28594 | 1934 | 341 | 2690（表：work／同じ表の列：label, description, instance of, publisher, developer, genre）
- 例3：16642 | 9683 | 10563 | 32643 | 32983（表：Star Trek video game／同じ表の列：label, description, instance of, genre, platform, publication date）

## g1133 — wikidbs10k：見出し「appears in the heritage monument list」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：Liste der Bodendenkmäler in Dingolfing | Liste der Bodendenkmäler in Dinkelsbühl | Liste der Bodendenkmäler in Rosenheim | Liste der Bodendenkmäler in Ellingen | Liste der Bodendenkmäler in Forchheim（表：Stadtpfarrkirche／同じ表の列：label, description, coordinate location, country, instance of, located in the admi…）
- 例2：Cultural heritage monuments in Ybbs an … | Cultural heritage monuments in Enzenkir… | Cultural heritage monuments in Obritzbe… | Cultural heritage monuments in Atzenbru… | Cultural heritage monuments in Baden, L…（表：Hausberg／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）
- 例3：Liste der Bodendenkmäler in Mitterskirc… | Liste der Bodendenkmäler in Illesheim | Liste der Bodendenkmäler in Pfaffing | Liste der Bodendenkmäler in Ramerberg | Liste der Bodendenkmäler in Grafing bei…（表：Wasserburgstall／同じ表の列：label, description, country, coordinate location, instance of, located in the admi…）

## g1134 — wikidbs10k：見出し「brand」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：Hyundai Motor Company | Pontiac | Maserati | Dacia | Daihatsu（表：mid-size car／同じ表の列：label, description, manufacturer, Commons category, instance of, image）
- 例2：Peugeot | SEAT | Zhiguli | Volkswagen | Fiat（表：C-segment／同じ表の列：label, description, Commons category, instance of, manufacturer, image）
- 例3：DeWALT | Milwaukee Electric Tool Corporation | Craftsman | Skil | Ryobi（表：circular saw model／同じ表の列：label, description, subclass of, instance of, audio, image）

## g1135 — wikidbs10k：見出し「cover art by」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：John Byrne | John Romita Jr.（表：The Dark Phoenix Saga／同じ表の列：label, description, instance of, part of the series, author, editor）
- 例2：John Byrne | John Romita Jr.（表：followed by／同じ表の列：label, description, instance of, part of, part of the series, author）
- 例3：George Pérez | John Byrne | John Romita Jr.（表：follows／同じ表の列：label, description, instance of, part of the series, author, editor）

## g1136 — wikidbs10k：見出し「cpu」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：R3000 | NEC VR4300 | Xenon | Ricoh 2A03 | Intel 80286（表：follows／同じ表の列：label, description, manufacturer, Commons category, Freebase ID, follows）
- 例2：NVIDIA Tegra X1 | NEC VR4300 | Gekko | ARM7TDMI | Ricoh 5A22（表：followed by／同じ表の列：label, description, instance of, manufacturer, image, Commons category）
- 例3：Pentium III | ARM Cortex-A9 | Original Nintendo 3DS CPU | PlayStation 4 APU | SuperH（表：computing platform／同じ表の列：label, description, image, Commons category, manufacturer, follows）

## g1137 — wikidbs10k：見出し「fabrication method」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：tapestry weaving（表：verdure／同じ表の列：label, description, instance of, inception, made from material, country）
- 例2：fresco painting（表：Cycle of the Life of the Christ／同じ表の列：label, description, Commons category, image, instance of, creator）
- 例3：watercolor（表：Town maps by Fredrik Adolf Wiblingen／同じ表の列：label, description, instance of, inception, depicts, collection）

## g1138 — wikidbs10k：見出し「points classification」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：Marta Bastianelli | Rasa Leleivytė（表：Aromitalia Basso Bikes Vaiano／同じ表の列：label, description, season of club or t…, country, instance of, sport）
- 例2：Greta Marturano | Nadia Quagliotto | Maja Perinovic | Soraya Paladin | Chiara Pierobon（表：Top Girls Fassa Bortolo／同じ表の列：label, description, instance of, sport, country, official name）
- 例3：Mossana Debesai | Kseniya Dobrynina | Jolanda Neff | Maryna Ivaniuk | Līna Svarinska（表：Servetto–Stradalli Cycle–Alurecycling／同じ表の列：label, description, instance of, sport, country, official name）

## g1139 — wikidbs10k：見出し「production company」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：Warner Bros. Animation | Spyglass Media Group | Metro-Goldwyn-Mayer | Warner Bros. | Warner Premiere（表：sequel film／同じ表の列：label, description, follows, instance of, IMDb ID, original language o…）
- 例2：Metro-Goldwyn-Mayer | Warner Bros. Animation | Warner Bros. | Warner Bros. Home Entertainment | WWE Studios（表：follows／同じ表の列：label, description, followed by, director, IMDb ID, original language o…）
- 例3：Warner Premiere | Warner Bros. Animation | WWE Studios | Spyglass Media Group | Warner Bros.（表：followed by／同じ表の列：label, description, follows, instance of, IMDb ID, original language o…）

## g1140 — wikidbs10k：見出し「stage classification」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：Kaden Groves | Eduard Michael Grosu | Dušan Rajović | Brenton Jones | Onur Balkan（表：2018 Tour of Qinghai Lake／同じ表の列：label, description, part of, country, followed by, sport）
- 例2：Jacob Tipper | Kaden Groves | Brenton Jones | Dušan Rajović | Onur Balkan（表：followed by／同じ表の列：label, description, part of, country, follows, followed by）
- 例3：Hernán Aguirre | Dušan Rajović | Onur Balkan | Daniel López | Georgios Boúglas（表：follows／同じ表の列：label, description, part of, country, followed by, sport）

## g1141 — wikidbs10k：見出し「taxon range」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：Beijing | People's Republic of China（表：secretion or excretion／同じ表の列：label, description, Commons category, image, taxon name, taxon rank）
- 例2：People's Republic of China | Beijing | Shanghai（表：secretion or excretion／同じ表の列：label, description, taxon name, taxon rank, image, Commons category）
- 例3：Beijing | People's Republic of China（表：secretion or excretion／同じ表の列：label, description, Encyclopedia of Lif…, instance of, image, taxon rank）

## g1142 — wikidbs10k：見出し「template has topic」（Wikidata の型 `wikibase-entityid`）（6 列）
- 例1：lacrosse player | bodybuilder | taekwondo athlete | water polo player | volleyball player（表：Template:Infobox sportsperson／同じ表の列：label, description, instance of, subclass of）
- 例2：sheep breed | cat breed | pig breed | donkey breed | chicken breed（表：Template:Infobox animal breed／同じ表の列：label, description, instance of, subclass of）
- 例3：torpedo | missile | mine | hand grenade | cartridge（表：Template:Infobox weapon／同じ表の列：label, description, instance of, subclass of）

## g1143 — wikidbs10k：見出し「admission yield rate」（Wikidata の型 `quantity`）（5 列）
- 例1：+0.36 | +0.16 | +0.17 | +0.4 | +0.08（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例2：+0.12 | +0.17 | +0.16 | +0.21 | +0.22（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）
- 例3：+0.1 | +0.34 | +0.28 | +0.7 | +0.15（表：liberal arts college in the United Stat…／同じ表の列：label, description, instance of, coordinate location, country, topic's main catego…）

## g1144 — wikidbs10k：見出し「event interval」（Wikidata の型 `quantity`）（5 列）
- 例1：+1（表：key event／同じ表の列：label, description, Commons category, topic's main catego…, Freebase ID, image）
- 例2：+1（表：sports league／同じ表の列：label, description, instance of, country, topic's main catego…, Freebase ID）
- 例3：1.0 | +1（表：sports league／同じ表の列：label, description, instance of, country, topic's main catego…, Freebase ID）

## g1145 — wikidbs10k：見出し「maximum sustained winds」（Wikidata の型 `quantity`）（5 列）
- 例1：+135 | +165 | +90 | +91 | +175（表：category 2 hurricane／同じ表の列：label, description, instance of, start time, end time, HURDAT identifier）
- 例2：+130 | +23 | +38 | +195 | +100（表：2019 Pacific typhoon season／同じ表の列：label, description, instance of, part of, start time, lowest atmospheric …）
- 例3：+75 | +25 | +85 | +30 | +100（表：followed by／同じ表の列：label, description, instance of, Digital Typhoon typ…, start time, end time）

## g1146 — wikidbs10k：見出し「redshift」（Wikidata の型 `quantity`）（5 列）
- 例1：+0.01032727 | +0.010 | +0.009266 | +0.010040 | +0.011148（表：[CHM2007] LDC 916／同じ表の列：label, description, catalog code, instance of, SIMBAD ID, apparent magnitude）
- 例2：+0.00263 | +0.00407 | +0.004723 | +0.004113 | +0.002568（表：[CHM2007] LDC 867／同じ表の列：label, description, image, constellation, Commons category, catalog code）
- 例3：+0.011855 | +0.012442 | +0.014530 | +0.012789 | +0.015738（表：[TSK2008] 487／同じ表の列：label, description, catalog code, galaxy morphologica…, instance of, SIMBAD ID）

## g1147 — wikidbs10k：見出し「semi-major axis of an orbit」（Wikidata の型 `quantity`）（5 列）
- 例1：+39.0866463 | +43.5871986 | +38.9632116 | +47.0992744 | +43.4896446（表：possible dwarf planet／同じ表の列：label, description, discoverer or inven…, instance of, orbital inclination, orbital eccentricity）
- 例2：+0.015439 | +0.0454 | +0.46 | +0.134 | +0.0607（表：super-Earth／同じ表の列：label, description, time of discovery o…, constellation, catalog code, instance of）
- 例3：+0.033 | +1.046 | +0.0505 | +0.143 | +0.0172（表：secondary body／同じ表の列：label, description, time of discovery o…, constellation, catalog code, instance of）

## g1148 — wikidbs10k：見出し「term length of office」（Wikidata の型 `quantity`）（5 列）
- 例1：+2 | +1（表：bâtonnier／同じ表の列：label, description, country, instance of, female form of label, subclass of）
- 例2：+2 | +1（表：organization leader／同じ表の列：label, description, instance of, subclass of, part of, inception）
- 例3：+4（表：office held by head of government／同じ表の列：label, description, subclass of, country, part of, instance of）

## g1149 — wikidbs10k：見出し「aerial view」（Wikidata の型 `string`）（5 列）
- 例1：Aerial view of north jakarta.jpg | Tokyo 2017-09-18 (36532024423).jpg | Macau, China.jpg | Guangzhou, China (5461525106).jpg | Kuala Lumpur, Malaysia Astronaut Imager…（表：physical location／同じ表の列：label, description, locator map image, coordinate location, instance of, shares border with）
- 例2：Moscow Urban Agglomeration, Russia, Lan… | Tokyo 2017-09-18 (36532024423).jpg | London by Sentinel-2.jpg | Deutschland-berlin.jpg | Iss047e099713 lrg Manila.jpg（表：capital city／同じ表の列：label, description, topic's main Wikime…, instance of, twinned administrat…, ISNI）
- 例3：Japan- Tochigi, Nikko mountain range Ch… | Utsunomiya city center area Aerial phot… | Ajigauracho cropped GSI CKT20125-C11-50… | FujiTonegawa.jpg | Sano city center area Aerial photograph…（表：political border／同じ表の列：label, description, image, Commons category, dantai code, country）

## g1150 — wikidbs10k：見出し「allociné film id」（Wikidata の型 `string`）（5 列）
- 例1：184684 | 275131 | 181716 | 223543 | 29284（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例2：219262 | 194073 | 38505 | 41125 | 214031（表：sequel film／同じ表の列：label, description, follows, instance of, IMDb ID, original language o…）
- 例3：961 | 878 | 27442 | 915 | 263679（表：follows／同じ表の列：label, description, followed by, director, IMDb ID, original language o…）

## g1151 — wikidbs10k：見出し「bangladesh administrative division code (2017-)」（Wikidata の型 `string`）（5 列）
- 例1：45 72 | 30 54 | 50 81 | 20 13 | 50 10（表：District of Bangladesh／同じ表の列：label, description, country, ISO 3166-2 code, coordinate location, located in the admi…）
- 例2：45 89 | 40 50 | 50 81 | 40 57 | 20 03（表：political border／同じ表の列：label, description, country, ISO 3166-2 code, coordinate location, located in the admi…）
- 例3：20 22 49 77 | 20 30 51 65 | 20 19 54 75 | 20 75 36 60 | 20 13 95 85（表：municipality of Bangladesh／同じ表の列：label, description, coordinate location, country, instance of, located in the admi…）

## g1152 — wikidbs10k：見出し「bavarian monument map object id (ground monument)」（Wikidata の型 `string`）（5 列）
- 例1：823772 | 162904 | 877481 | 681008 | 215686（表：Stadtpfarrkirche／同じ表の列：label, description, coordinate location, country, instance of, located in the admi…）
- 例2：84461 | 80558 | 186105 | 122115 | 54916（表：Wasserburgstall／同じ表の列：label, description, country, coordinate location, instance of, located in the admi…）
- 例3：770867 | 727016 | 642422 | 545024 | 877572（表：Hospital church／同じ表の列：label, description, coordinate location, instance of, country, heritage designation）

## g1153 — wikidbs10k：見出し「bg ekatte place id」（Wikidata の型 `string`）（5 列）
- 例1：10971 | 67653 | 40909 | 66425 | 83510（表：oblast seat／同じ表の列：label, description, twinned administrat…, Dewey Decimal Class…, country, located in the admi…）
- 例2：VRC | SZR31 | MON29 | SLS31 | RSE（表：administrative territorial entity／同じ表の列：label, description, country, instance of, Freebase ID, coordinate location）
- 例3：SLS | SLV | VRC10 | RAZ | SHU30（表：administrative centre／同じ表の列：label, description, country, located in the admi…, capital, Commons category）

## g1154 — wikidbs10k：見出し「china railway tmis station code」（Wikidata の型 `string`）（5 列）
- 例1：12170 | 12707 | 11612 | 11609 | 11369（表：Beijing railway junction／同じ表の列：label, description, located in the admi…, adjacent station, instance of, country）
- 例2：10001 | 13385 | 12170 | 21152 | 11389（表：adjacent station／同じ表の列：label, description, located in the admi…, adjacent station, country, Commons category）
- 例3：21110 | 21089 | 22670 | 21086 | 29321（表：adjacent station／同じ表の列：label, description, country, instance of, connecting line, coordinate location）

## g1155 — wikidbs10k：見出し「crunchbase organization id」（Wikidata の型 `string`）（5 列）
- 例1：adaptive-athletics-at-uh | providence-college | vanderbilt-university | university-of-san-francisco-school-of-l… | university-of-michigan（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例2：villanova-university-school-of-law | oregon-state-university-corvallis | marquette-university | university-of-san-francisco-school-of-l… | canisius-college（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）
- 例3：stanford-graduate-school-of-business | arizona-state-university | columbia-university-school-of-social-wo… | deming-center-for-entrepreneurship | the-school-of-engineering-at-stanford-u…（表：employer／同じ表の列：label, description, instance of, country, Commons category, coordinate location）

## g1156 — wikidbs10k：見出し「douban film id」（Wikidata の型 `string`）（5 列）
- 例1：1304129 | 1302343 | 3212398 | 1307591 | 1306969（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例2：3053521 | 26972258 | 1307528 | 1394495 | 1300436（表：sixth generation Chinese films／同じ表の列：label, description, IMDb ID, instance of, director, original language o…）
- 例3：4905028 | 26374776 | 34984272 | 1293572 | 24750534（表：sequel film／同じ表の列：label, description, follows, instance of, IMDb ID, original language o…）

## g1157 — wikidbs10k：見出し「filmaffinity id」（Wikidata の型 `string`）（5 列）
- 例1：117377 | 934628 | 786572 | 737820 | 858984（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例2：712627 | 767137 | 863467 | 796392 | 750331（表：Treehouse of Horror XI-XX／同じ表の列：label, description, Freebase ID, follows, followed by, instance of）
- 例3：863467 | 767137 | 272377 | 796392 | 152687（表：followed by／同じ表の列：label, description, Freebase ID, follows, followed by, instance of）

## g1158 — wikidbs10k：見出し「fleet or registration number」（Wikidata の型 `string`）（5 列）
- 例1：21C9 | 21C18 | 21C6 | 35028 | 35027（表：SR Merchant Navy class／同じ表の列：label, description, instance of, manufacturer, named after, Commons category）
- 例2：11 | 2 | 3 | 4 | 5（表：Shay locomotive／同じ表の列：label, description, instance of, track gauge, Commons category, image）
- 例3：2412 | 2458 | 2586 | 2421 | 2535（表：Prussian P 8／同じ表の列：label, description, located in the admi…, instance of, country, part of）

## g1159 — wikidbs10k：見出し「floraweb id」（Wikidata の型 `string`）（5 列）
- 例1：2609 | 26634 | 3859 | 2481 | 3436（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例2：1630 | 4170 | 6402 | 26634 | 3436（表：symbol／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例3：6402 | 2029 | 3436 | 1007 | 26634（表：symbol／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g1160 — wikidbs10k：見出し「fossilworks taxon id」（Wikidata の型 `string`）（5 列）
- 例1：104235.0 | 48848.0 | 52604.0 | 160980.0 | 149382.0（表：symbol／同じ表の列：label, description, taxon rank, IUCN conservation s…, Commons category, taxon name）
- 例2：57432 | 124183.0 | 41248.0 | 41331.0 | 40375.0（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例3：55065 | 83628 | 55062 | 369914 | 55068（表：secretion or excretion／同じ表の列：label, description, taxon rank, parent taxon, taxon name, Commons category）

## g1161 — wikidbs10k：見出し「gamecip platform id」（Wikidata の型 `string`）（5 列）
- 例1：1127 | 1038 | 1122 | 1037 | 1042（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例2：1130 | 1038 | 1127 | 1042 | 1139（表：follows／同じ表の列：label, description, manufacturer, Commons category, follows, followed by）
- 例3：1121 | 1042 | 1029 | 1139 | 1038（表：followed by／同じ表の列：label, description, instance of, manufacturer, image, Commons category）

## g1162 — wikidbs10k：見出し「gene atlas image」（Wikidata の型 `string`）（5 列）
- 例1：PBB GE MAP2K1 202670 at fs.png | PBB GE VHL 203844 at fs.png | PBB GE PDGFRA 203131 at fs.png | PBB GE DPYD 204646 at fs.png | PBB GE ERBB2 210930 s at.png（表：biological variant of／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）
- 例2：PBB GE JPH3 220188 at fs.png | PBB GE ATXN1 203231 s at fs.png | PBB GE FTL 213187 x at fs.png | PBB GE VPS13A 214785 at fs.png | PBB GE ATXN2 202622 s at fs.png（表：genetic association／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）
- 例3：PBB GE TITF1 210673 x at fs.png | PBB GE TBP 203135 at fs.png | PBB GE ATXN3 205416 s at fs.png | PBB GE ATXN1 203231 s at fs.png | PBB GE ATXN2 202622 s at fs.png（表：encoded by／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, Ensembl transcript …）

## g1163 — wikidbs10k：見出し「gepris organization id」（Wikidata の型 `string`）（5 列）
- 例1：10653 | 10684 | 10678 | 63894553 | 10650（表：Fraunhofer institute／同じ表の列：label, description, coordinate location, country, located in the admi…, GND ID）
- 例2：10787 | 10666 | 10679 | 10146 | 10656（表：Fraunhofer Society／同じ表の列：label, description, coordinate location, country, instance of, part of）
- 例3：10119 | 10272 | 10215 | 10233 | 10045（表：part／同じ表の列：label, description, Freebase ID, topic's main catego…, Commons category, image）

## g1164 — wikidbs10k：見出し「glyphwiki id」（Wikidata の型 `string`）（5 列）
- 例1：u2807 | u281d | u281b | u280b | u2811（表：depicting object／同じ表の列：label, description, Unicode character, instance of, Unicode block, Freebase ID）
- 例2：u5f97-g | u6c6a-g | u8005 | u5144 | u4e4b-g（表：standard hanzi in mainland China／同じ表の列：label, description, instance of, Unicode code point, stroke count, radical）
- 例3：u280f | u2819 | u2817 | u280b | u281a（表：depicting object／同じ表の列：label, description, Unicode character, instance of, Unicode block, Freebase ID）

## g1165 — wikidbs10k：見出し「guía digital del patrimonio cultural de andalucía identifier」（Wikidata の型 `string`）（5 列）
- 例1：i17157 | i19235 | i17832 | i18342 | i19124（表：cilla／同じ表の列：label, description, country, located in the admi…, IAPH code, native label）
- 例2：i19613 | i22091 | i19632 | i19770 | i9643（表：alcazaba／同じ表の列：label, description, located in the admi…, coordinate location, country, instance of）
- 例3：i23576 | i19025 | i17 | i642 | i23574（表：Granaries in Spain／同じ表の列：label, description, located in the admi…, country, instance of, IAPH code）

## g1166 — wikidbs10k：見出し「html entity」（Wikidata の型 `string`）（5 列）
- 例1：&#x2809; | &#x280e; | &#x2807; | &#x2819; | &#x281e;（表：depicting object／同じ表の列：label, description, Unicode character, instance of, Unicode block, Freebase ID）
- 例2：&#x5c9a; | &#x5317; | &#x4e5f; | &#x674e; | &#x626c;（表：standard hanzi in mainland China／同じ表の列：label, description, instance of, Unicode code point, stroke count, radical）
- 例3：&#x280b; | &#x2803; | &#x2827; | &#x2813; | &#x2811;（表：depicting object／同じ表の列：label, description, Unicode character, instance of, Unicode block, Freebase ID）

## g1167 — wikidbs10k：見出し「iaph code」（Wikidata の型 `string`）（5 列）
- 例1：01110170001 | 01410600102 | 01410600101 | 01410580058 | 01410390145（表：cilla／同じ表の列：label, description, country, Guía Digital del Pa…, located in the admi…, native label）
- 例2：01040450001 | 01040290068 | 01110120065 | 01040130146 | 01180890003（表：alcazaba／同じ表の列：label, description, located in the admi…, coordinate location, country, instance of）
- 例3：01410090041 | 01181750001 | 01140420005 | 01180130002 | 01140210693（表：Granaries in Spain／同じ表の列：label, description, located in the admi…, country, instance of, Guía Digital del Pa…）

## g1168 — wikidbs10k：見出し「ibtracs cyclone id」（Wikidata の型 `string`）（5 列）
- 例1：1976266N13220 | 1970286N25292 | 2018218N14255 | 1990191N10266 | 1990216N13281（表：category 2 hurricane／同じ表の列：label, description, instance of, start time, end time, HURDAT identifier）
- 例2：2019239N14130 | 2019356N06140 | 2019245N15170 | 2019258N15151 | 2019233N15132（表：2019 Pacific typhoon season／同じ表の列：label, description, instance of, part of, start time, lowest atmospheric …）
- 例3：2019233N15132 | 2019258N15151 | 2019356N06140 | 2019292N10157 | 2019245N15170（表：followed by／同じ表の列：label, description, instance of, Digital Typhoon typ…, start time, end time）

## g1169 — wikidbs10k：見出し「international jewish cemetery project id」（Wikidata の型 `string`）（5 列）
- 例1：australia/queensland | australia/new-south-wales | usa/oregon-or | australia/victoria | australia/south-australia（表：administrative territorial entity／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）
- 例2：australia/new-south-wales | australia/western-australia | australia/tasmania | australia/northern-territory | australia/south-australia（表：jurisdiction／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）
- 例3：canada/quebec-qc | canada/newfoundland-a-labrador-nf | canada/ontario-on | canada/nunavut-nu | canada/british-columbia-bc（表：physical location／同じ表の列：label, description, replaces, Dewey Decimal Class…, capital, shares border with）

## g1170 — wikidbs10k：見出し「isbn-13」（Wikidata の型 `string`）（5 列）
- 例1：978-0-85484-097-7 | 978-0-85484-122-6 | 978-0-902238-97-8 | 978-0-85484-084-7 | 978-1-910195-02-4（表：oral history book／同じ表の列：label, description, instance of, part of the series, publisher, official website）
- 例2：978-0-7309-6083-6 | 978-0-7309-6080-5 | 978-1-921703-31-7 | 978-0-7309-6088-1 | 978-0-7309-6074-4（表：trail map／同じ表の列：label, description, instance of, part of, followed by, official website）
- 例3：978-0-7309-6088-1 | 978-1-921703-30-0 | 978-0-7309-6081-2 | 978-0-7309-6075-1 | 978-0-7309-6067-6（表：followed by／同じ表の列：label, description, instance of, part of, follows, official website）

## g1171 — wikidbs10k：見出し「kladr id」（Wikidata の型 `string`）（5 列）
- 例1：4000000000000 | 6700000000000 | 5700000000000 | 7300000000000 | 5600000000000（表：administrative territorial entity／同じ表の列：label, description, country, capital, shares border with, head of government）
- 例2：5400000000000.0 | 2900000000000.0 | 7200000000000.0 | 6900000000000 | 200000000000.0（表：political border／同じ表の列：label, description, flag image, coat of arms image, flag, Commons category）
- 例3：7400000000000 | 7800000000000 | 5900000000000 | 2400000000000 | 7700000000000（表：administrative territorial entity／同じ表の列：label, description, located in time zone, official website, instance of, shares border with）

## g1172 — wikidbs10k：見出し「koatuu identifier」（Wikidata の型 `string`）（5 列）
- 例1：111200000 | 111700000 | 110300000 | 110900000 | 111300000（表：jurisdiction／同じ表の列：label, description, page banner, Commons category, country, coordinate location）
- 例2：1210100000.0 | 524555100.0 | 6810100000.0 | 6122410100.0 | 524155100.0（表：capital city／同じ表の列：label, description, Commons category, coat of arms image, country, coordinate location）
- 例3：6810100000 | 510100000 | 7410700000 | 6310100000 | 7310100000（表：capital city／同じ表の列：label, description, Commons category, flag image, country, coordinate location）

## g1173 — wikidbs10k：見出し「lfds object id」（Wikidata の型 `string`）（5 列）
- 例1：09270598 | 08962066 | 08962408 | 09274028 | 09272627（表：Kretscham／同じ表の列：label, description, instance of, coordinate location, inception, heritage designation）
- 例2：09301827 | 09302515 | 09232979 | 09301822 | 09305849（表：asset group／同じ表の列：label, description, instance of, Commons category, country, coordinate location）
- 例3：09254814 | 09272355 | 09254701 | 09272456 | 09274451（表：factor house／同じ表の列：label, description, instance of, coordinate location, heritage designation, country）

## g1174 — wikidbs10k：見出し「library of congress control number (lccn) (bibliographic)」（Wikidata の型 `string`）（5 列）
- 例1：82643856 | 92660504 | 2001229974 | 00244513 | 61065129（表：publishing／同じ表の列：label, description, official website, instance of, ISSN, OCLC control number）
- 例2：26011128 | 92660504 | 66009876 | 74641498 | 2004243956（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）
- 例3：51031430 | 17024346 | 06046735 | a50001900 | 26011128（表：publishing／同じ表の列：label, description, instance of, ISSN, ERA Journal ID, OCLC control number）

## g1175 — wikidbs10k：見出し「metacritic id」（Wikidata の型 `string`）（5 列）
- 例1：tv/friends/season-4 | tv/friends/season-8 | tv/star-trek-the-next-generation/season… | tv/the-simpsons/season-6 | tv/friends/season-7（表：television series season／同じ表の列：label, description, instance of, Freebase ID, part of the series, number of episodes）
- 例2：movie/zootopia | tv/doctor-who-1963 | game/pc/grand-theft-auto-iii | game/pc/the-elder-scrolls-v-skyrim | game/pc/lego-city-undercover（表：work／同じ表の列：label, description, IMDb ID, instance of, publication date, country of origin）
- 例3：tv/the-simpsons/season-13 | tv/the-simpsons/season-17 | tv/the-simpsons/season-12 | tv/the-simpsons/season-11 | tv/the-simpsons/season-15（表：television series season／同じ表の列：label, description, instance of, Freebase ID, part of the series, number of episodes）

## g1176 — wikidbs10k：見出し「mime type」（Wikidata の型 `string`）（5 列）
- 例1：application/x-shockwave-flash（表：Small Web Format family／同じ表の列：label, description, instance of, file extension, PRONOM file format …, edition or translat…）
- 例2：application/x-shockwave-flash（表：replacing subject／同じ表の列：label, description, instance of, file extension, PRONOM file format …, edition or translat…）
- 例3：application/x-shockwave-flash（表：replaced entity／同じ表の列：label, description, instance of, file extension, PRONOM file format …, edition or translat…）

## g1177 — wikidbs10k：見出し「mobygames game id」（Wikidata の型 `string`）（5 列）
- 例1：legend-of-zelda-a-link-between-worlds | legend-of-zelda-majoras-mask | legend-of-zelda-the-wind-waker | legend-of-zelda-breath-of-the-wild | legend-of-zelda-twilight-princess（表：work／同じ表の列：label, description, part of the series, genre, platform, game mode）
- 例2：mario-luigi-partners-in-time | super-mario-bros-2 | wario-land-super-mario-land-3 | super-mario-bros-3 | luigis-mansion（表：work／同じ表の列：label, description, instance of, publisher, developer, genre）
- 例3：animal-crossing | animal-crossing-new-leaf | dbutsu-no-mori | animal-crossing-pocket-camp | animal-crossing-new-horizons（表：work／同じ表の列：label, description, instance of, publisher, genre, official website）

## g1178 — wikidbs10k：見出し「nhs organisation data service id」（Wikidata の型 `string`）（5 列）
- 例1：719 | 706 | 725 | 731 | 712（表：administrative territorial entity／同じ表の列：label, description, Commons category, ISO 3166-2 code, coordinate location, country）
- 例2：615 | 321 | 509 | 417 | 914（表：unitary authority in England／同じ表の列：label, description, country, instance of, UK Parliament thesa…, applies to jurisdic…）
- 例3：316 | 306 | 406 | 512 | 814（表：part／同じ表の列：label, description, country, instance of, ISNI, Ringgold ID）

## g1179 — wikidbs10k：見出し「opus number」（Wikidata の型 `string`）（5 列）
- 例1：89, No. 3 | 89, No. 1 | 89, No. 16 | 89, No. 9 | 89, No. 4（表：Winterreise／同じ表の列：label, description, instance of, form of creative wo…, composer, genre）
- 例2：89, No. 1 | 89, No. 22 | 89, No. 2 | 89, No. 19 | 89, No. 14（表：derivative work／同じ表の列：label, description, instance of, form of creative wo…, composer, genre）
- 例3：10, No. 11 | 10, No. 6 | 10, No. 8 | 10, No. 4 | 10, No. 7（表：Études, Op. 10／同じ表の列：label, description, tempo marking, tonality, audio, part of）

## g1180 — wikidbs10k：見出し「palissy id」（Wikidata の型 `string`）（5 列）
- 例1：PM65000450 | PM03000025 | PM03000665 | PM75000025 | PM01000076（表：holy water font／同じ表の列：label, description, instance of, made from material, country, Commons category）
- 例2：PM49000196 | PM63000989 | PM17000775 | PM72000515 | PM89001825（表：verdure／同じ表の列：label, description, instance of, inception, made from material, fabrication method）
- 例3：PM68001823 | PM68001839 | PM68001856 | PM68001824 | PM68001985（表：Phaeton body／同じ表の列：label, description, instance of, country, heritage designation, located in the admi…）

## g1181 — wikidbs10k：見出し「protected buildings register in finland building id」（Wikidata の型 `string`）（5 列）
- 例1：304696 | 304746 | 304831 | 304777 | 304691（表：wooden bell tower／同じ表の列：label, description, instance of, coordinate location, located in the admi…, country）
- 例2：305046.0 | 304986.0 | 305080.0 | 305290.0 | 305127.0（表：part／同じ表の列：label, description, instance of, country, coordinate location, image）
- 例3：304130 | 303999 | 304041 | 304020 | 307633（表：railway inspector's house／同じ表の列：label, description, located in the admi…, instance of, country, permanent building …）

## g1182 — wikidbs10k：見出し「protected buildings register in finland id」（Wikidata の型 `string`）（5 列）
- 例1：200689 | 200705 | 200630 | 200615 | 200760（表：wooden bell tower／同じ表の列：label, description, instance of, coordinate location, located in the admi…, country）
- 例2：200695.0 | 200559.0 | 200850.0 | 200891.0 | 200643.0（表：part／同じ表の列：label, description, instance of, country, coordinate location, image）
- 例3：200306.0 | 200298.0 | 200363.0 | 200305.0 | 200370.0（表：part／同じ表の列：label, description, coordinate location, country, instance of, image）

## g1183 — wikidbs10k：見出し「railscot location id」（Wikidata の型 `string`）（5 列）
- 例1：L/Longbenton | M/Monkseaton | W/West_Monkseaton | W/West_Jesmond | W/Whitley_Bay（表：British Rail／同じ表の列：label, description, part of, Commons category, instance of, Freebase ID）
- 例2：S/South_Gosforth | C/Cullercoats | P/Percy_Main | W/West_Monkseaton | M/Monkseaton（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例3：W/Whitley_Bay | W/Wansbeck_Road | J/Jesmond | C/Callerton_Parkway | S/South_Gosforth（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）

## g1184 — wikidbs10k：見出し「swedish open cultural heritage uri」（Wikidata の型 `string`）（5 列）
- 例1：uu/srdb/9a7f7482-468c-46a2-a482-d6cd92a… | uu/srdb/487c1330-19d1-4df2-bf6a-75725d2… | raa/fmi/10101500180001 | raa/fmi/10232900170001 | uu/srdb/adbd36b3-40c7-4cd2-9320-9c12d63…（表：runestone／同じ表の列：label, description, instance of, country, image, coordinate location）
- 例2：raa/bbr/21300000013053 | raa/bbr/21300000014200 | raa/bbr/21300000012796 | raa/bbr/21300000013584 | raa/bbr/21300000012801（表：listed building in Sweden／同じ表の列：label, description, Commons category, located in the admi…, coordinate location, instance of）
- 例3：raa/fmi/10030601160001 | raa/fmi/10032700660001 | uu/srdb/103abc40-d7eb-4c7b-90ef-56cd2e0… | uu/srdb/7744a4f2-d37b-4ba5-afb3-40ecd4d… | raa/fmi/10037001240001（表：Ingvar runestones／同じ表の列：label, description, coordinate location, instance of, country, located in the admi…）

## g1185 — wikidbs10k：見出し「unicode code point」（Wikidata の型 `string`）（5 列）
- 例1：280D | 280B | 2813 | 2809 | 281F（表：depicting object／同じ表の列：label, description, Unicode character, instance of, Unicode block, Freebase ID）
- 例2：5B57 | 5F97 | 8005 | 5317 | 572D（表：standard hanzi in mainland China／同じ表の列：label, description, instance of, stroke count, radical, Unicode block）
- 例3：2803 | 283A | 281A | 280B | 2815（表：depicting object／同じ表の列：label, description, Unicode character, instance of, Unicode block, Freebase ID）

## g1186 — wikidbs10k：見出し「afflicts」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：blood | circulatory system | central nervous system | human eye | liver（表：effect／同じ表の列：label, description, subclass of, has cause, route of administra…, symptoms and signs）
- 例2：liver | blood | respiratory system | urinary bladder | skin（表：effect／同じ表の列：label, description, subclass of, has cause, route of administra…, symptoms and signs）
- 例3：skin | human eye（表：effect／同じ表の列：label, description, subclass of, has cause, route of administra…, symptoms and signs）

## g1187 — wikidbs10k：見出し「category for employees of the organization」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：Category:Hessischer Rundfunk people | Category:Saarländischer Rundfunk people | Category:Bayerischer Rundfunk people | Category:Radio Bremen people | Category:Norddeutscher Rundfunk people（表：operator／同じ表の列：label, description, headquarters locati…, Commons category, instance of, Freebase ID）
- 例2：Category:University of San Francisco fa… | Category:Seattle University faculty | Category:Pennsylvania State University … | Category:University of Colorado Boulder… | Category:University of Iowa faculty（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）
- 例3：Category:Stanford University faculty | Category:Academics of the University of… | Category:University of Oklahoma faculty | Category:Arizona State University facul… | Category:University of Colorado faculty（表：employer／同じ表の列：label, description, instance of, country, Commons category, coordinate location）

## g1188 — wikidbs10k：見出し「derivative work」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：Im Dorfe | Die Nebensonnen | Gute Nacht | Irrlicht | Das Wirtshaus（表：lyrics／同じ表の列：label, description, instance of, form of creative wo…, author, copyright status）
- 例2：Kamen Rider W Returns | Kamen Rider Agito: Project G4 | Super Hero Taisen GP: Kamen Rider 3 | Kamen Rider Fourze the Movie: Space, He… | Kamen Rider Kuuga（表：followed by／同じ表の列：label, description, genre, Freebase ID, instance of, country of origin）
- 例3：Heisei Riders vs. Shōwa Riders: Kamen R… | Super Hero Taisen GP: Kamen Rider 3 | Kamen Rider Zero-One: REAL×TIME | Kamen Rider Kabuto: God Speed Love | Kamen Rider Hibiki & The Seven Senki（表：based on／同じ表の列：label, description, genre, Freebase ID, instance of, country of origin）

## g1189 — wikidbs10k：見出し「general manager」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：Dave Brailsford（表：Ineos Grenadiers／同じ表の列：label, description, instance of, sport, UCI code of cycling…, follows）
- 例2：Dave Brailsford（表：followed by／同じ表の列：label, description, instance of, sport, UCI code of cycling…, follows）
- 例3：Dave Brailsford（表：follows／同じ表の列：label, description, instance of, sport, UCI code of cycling…, followed by）

## g1190 — wikidbs10k：見出し「of」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：Kyoto Prefectural Road Route 455 | Kyoto Prefectural Road Route 73 | Kyoto Prefectural Road Route 10 | Kyoto Prefectural Road Route 9 | Japan National Route 173（表：follows／同じ表の列：label, description, instance of, country, located in the admi…, postal code）
- 例2：Japan National Route 190 | Yamaguchi Prefectural Road Route 25 | Japan National Route 2 | Yamaguchi Prefectural Road Route 214 | municipal road（表：followed by／同じ表の列：label, description, coordinate location, instance of, country, located in the admi…）
- 例3：Hiroshima Prefectural Road Route 81 | Hiroshima Prefectural Road Route 367 | Japan National Route 317 | Japan National Route 196（表：followed by／同じ表の列：label, description, instance of, coordinate location, country, located in the admi…）

## g1191 — wikidbs10k：見出し「official color」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：blue | green | black | red | yellow（表：participating team／同じ表の列：label, description, instance of, home venue, league, head coach）
- 例2：blue | green | yellow | red | black（表：winner／同じ表の列：label, description, instance of, home venue, league, head coach）
- 例3：sky blue | yellow | azure | crimson | black（表：contrada of Siena／同じ表の列：label, description, instance of, Commons category, motto text, located in the admi…）

## g1192 — wikidbs10k：見出し「officially opened by」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：Hirohito | Charles Curtis | Adolf Hitler | Roh Tae-woo | Juan Carlos I of Spain（表：part／同じ表の列：label, description, country, Commons category, oath made by, instance of）
- 例2：Juho Kusti Paasikivi | Hirohito | Naruhito | Roh Tae-woo | William Deane（表：part／同じ表の列：label, description, Commons category, oath made by, topic's main catego…, GND ID）
- 例3：Duke Henry of Mecklenburg-Schwerin | Ronald Reagan | Edward VII | Prince Philip, Duke of Edinburgh | Gustaf V of Sweden（表：followed by／同じ表の列：label, description, country, Commons category, oath made by, GND ID）

## g1193 — wikidbs10k：見出し「operating system」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：macOS | cross-platform | MS-DOS | Linux | AmigaOS-like operating system（表：file manager／同じ表の列：label, description, instance of）
- 例2：Android Lollipop | Android | Android Nougat | EMUI | Android Pie（表：phablet／同じ表の列：label, description, instance of, subclass of, manufacturer）
- 例3：cross-platform | Windows 98 | Linux | Windows 7 | Windows 8（表：audio software／同じ表の列：label, description, official website, instance of）

## g1194 — wikidbs10k：見出し「route diagram」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：Template:Greenford Branch Line RDT | Template:Piccadilly line RDT | Template:District Line RDT | Template:Great Eastern main line RDT | Template:Central line RDT（表：railway line／同じ表の列：label, description, Commons category, country, instance of, located in the admi…）
- 例2：Template:Rapid Rail network | Template:Kajang Line | Template:KLIA Ekspres Line | Template:BRT Sunway Line | Template:KL Monorail Line（表：Rapid KL／同じ表の列：label, description, instance of, Commons category, Freebase ID, country）
- 例3：Template:London to Aylesbury Line | East Coast Main Line diagram | Template:Bakerloo line RDT | Template:South Eastern main line | Template:Thameslink（表：railway line／同じ表の列：label, description, country, located in the admi…, instance of, topic's main catego…）

## g1195 — wikidbs10k：見出し「route of administration」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：inhalation administration（表：effect／同じ表の列：label, description, subclass of, has cause, afflicts, symptoms and signs）
- 例2：inhalation administration（表：effect／同じ表の列：label, description, subclass of, has cause, afflicts, symptoms and signs）
- 例3：inhalation administration（表：effect／同じ表の列：label, description, subclass of, has cause, afflicts, symptoms and signs）

## g1196 — wikidbs10k：見出し「set in environment」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：fictional planet | desert | fictional moon（表：work／同じ表の列：label, description, instance of, genre, Freebase ID, distribution format）
- 例2：fictional country（表：Conan non-canonical works／同じ表の列：label, description, instance of, author, genre, publication date）
- 例3：fictional planet | casino hotel（表：The Final Chapter／同じ表の列：label, description, IMDb ID, part of the series, director, screenwriter）

## g1197 — wikidbs10k：見出し「standards body」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：International Organization for Standard…（表：ISO IEC 80000／同じ表の列：label, description, instance of, has edition or tran…, part of, follows）
- 例2：International Organization for Standard…（表：followed by／同じ表の列：label, description, instance of, has edition or tran…, part of, follows）
- 例3：International Organization for Standard…（表：version, edition, or translation／同じ表の列：label, description, instance of, title, publication date, edition number）

## g1198 — wikidbs10k：見出し「unesco language status」（Wikidata の型 `wikibase-entityid`）（5 列）
- 例1：1 safe（表：original language／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, ISO 639-2 code）
- 例2：2 vulnerable | 1 safe（表：Wikimedia category／同じ表の列：label, description, Great Russian Encyc…, Glottolog code, Art & Architecture …, ISO 639-2 code）
- 例3：1 safe | 2 vulnerable（表：language／同じ表の列：label, description, language regulatory…, ISO 639-1 code, ISO 639-2 code, ISO 639-3 code）

## 答えの雛形

```
g1051	
g1052	
g1053	
g1054	
g1055	
g1056	
g1057	
g1058	
g1059	
g1060	
g1061	
g1062	
g1063	
g1064	
g1065	
g1066	
g1067	
g1068	
g1069	
g1070	
g1071	
g1072	
g1073	
g1074	
g1075	
g1076	
g1077	
g1078	
g1079	
g1080	
g1081	
g1082	
g1083	
g1084	
g1085	
g1086	
g1087	
g1088	
g1089	
g1090	
g1091	
g1092	
g1093	
g1094	
g1095	
g1096	
g1097	
g1098	
g1099	
g1100	
g1101	
g1102	
g1103	
g1104	
g1105	
g1106	
g1107	
g1108	
g1109	
g1110	
g1111	
g1112	
g1113	
g1114	
g1115	
g1116	
g1117	
g1118	
g1119	
g1120	
g1121	
g1122	
g1123	
g1124	
g1125	
g1126	
g1127	
g1128	
g1129	
g1130	
g1131	
g1132	
g1133	
g1134	
g1135	
g1136	
g1137	
g1138	
g1139	
g1140	
g1141	
g1142	
g1143	
g1144	
g1145	
g1146	
g1147	
g1148	
g1149	
g1150	
g1151	
g1152	
g1153	
g1154	
g1155	
g1156	
g1157	
g1158	
g1159	
g1160	
g1161	
g1162	
g1163	
g1164	
g1165	
g1166	
g1167	
g1168	
g1169	
g1170	
g1171	
g1172	
g1173	
g1174	
g1175	
g1176	
g1177	
g1178	
g1179	
g1180	
g1181	
g1182	
g1183	
g1184	
g1185	
g1186	
g1187	
g1188	
g1189	
g1190	
g1191	
g1192	
g1193	
g1194	
g1195	
g1196	
g1197	
g1198	
```
