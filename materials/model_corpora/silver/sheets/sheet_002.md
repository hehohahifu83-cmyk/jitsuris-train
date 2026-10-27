# 銀ラベルのシート 002 / 008（外の学習データの読み替え）

- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列
- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`
- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を、ChatGPT は `answers/sheet_002.tsv`、Grok は `answers_grok/sheet_002.tsv` に写して埋める。**相手の答えは見ない**

## g0151 — wikidbs10k：見出し「ensembl gene id」（Wikidata の型 `string`）（1,044 列）
- 例1：FBgn0039924 | ENSMUSG00000024867 | ENSRNOG00000005138 | ENSMUSG00000025417 | ENSG00000107242（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, ortholog）
- 例2：ENSDARG00000063544 | ENSMUSG00000024867 | ENSMUSG00000018547 | ENSG00000166908 | FBgn0034789（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, HomoloGene ID, chromosome）
- 例3：ENSG00000169271 | ENSRNOG00000010524 | FBgn0001229 | FBgn0001227 | ENSMUSG00000006221（表：encoded by／同じ表の列：label, description, Entrez Gene ID, RefSeq RNA ID, Ensembl transcript …, encodes）

## g0152 — wikidbs10k：見出し「coat of arms」（Wikidata の型 `wikibase-entityid`）（1,043 列）
- 例1：coat of arms of Barbados | coat of arms of Switzerland | coat of arms of Argentina | Blue Sky with a White Sun | Emblem of Ethiopia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Great Seal of the United States | coat of arms of Belgium | coat of arms of Russia | coat of arms of Luxembourg | coat of arms of Poland（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：coat of arms of Slovakia | coat of arms of Namibia | coat of arms of North Macedonia | emblem of Tajikistan | coat of arms of Spain（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0153 — sotab_v2：元の種類 `Brand`（1,039 列）
- 例1：Brevistay（DBpedia：brand）
- 例2：Citadines Apart'hotel | lyf | Others（DBpedia：brand）
- 例3：Evenia Hotels（DBpedia：brand）

## g0154 — wikidbs10k：見出し「coordinates of northernmost point」（Wikidata の型 `globecoordinate`）（1,038 列）
- 例1：51.50508 | 46.88 | 56.171861111111 | 23.28 | 52.379528888889（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：55.0584 | 37.55 | 37.08 | 33.15 | 50.182794（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：34.94229794 | 34.75241462 | 34.95893121 | 34.91583503 | 34.80088471（表：Limassol District／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）

## g0155 — wikidbs10k：見出し「ensembl transcript id」（Wikidata の型 `string`）（1,038 列）
- 例1：ENSDART00000014787 | ENSDART00000192980 | ENST00000498783 | ENSMUST00000018691 | YDR208W_mRNA（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, ortholog）
- 例2：ENSMUST00000025800 | FBtr0071900 | ENSMUST00000013970 | ENST00000498783 | ENSDART00000020859（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例3：F38E11.2.1 | ENSMUST00000102486 | ENSMUST00000034562 | ENSRNOT00000051317 | FBtr0076454（表：encoded by／同じ表の列：label, description, Entrez Gene ID, Ensembl gene ID, RefSeq RNA ID, encodes）

## g0156 — wikidbs10k：見出し「krugosvet article」（Wikidata の型 `string`）（1,037 列）
- 例1：strany_mira/ESTONIYA.html | strany_mira/PERU.html | strany_mira/ANTIGUA_I_BARBUDA.html | strany-mira/serbiya | strany_mira/MAROKKO.html（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：strany_mira/SHVETSIYA.html | strany_mira/UKRAINA.html | strany_mira/ITALIYA.html | strany_mira/ALZHIR.html | strany_mira/SIRIYA.html（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：strany-mira/kanada | strany_mira/SOEDINENNIE_SHTATI_AMERIKI.… | Earth_sciences/geografiya/SOEDINENNOE_K… | strany_mira/AVSTRALIYA.html | strany_mira/ARMENIYA.html（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0157 — wikidbs10k：見出し「iab code」（Wikidata の型 `string`）（1,036 列）
- 例1：1234 | 1274 | 1382 | 1248 | 1409（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：1412 | 1420 | 1455 | 1272 | 1317（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：1412 | 1335 | 1400 | 1331 | 1295（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0158 — wikidbs10k：見出し「continent」（Wikidata の型 `wikibase-entityid`）（1,031 列）
- 例1：Asia | Europe | North America | Africa | South America（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Asia | Africa | North America | Europe（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Asia | Europe | North America | Insular Oceania | South America（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0159 — wikidbs10k：見出し「local dialing code」（Wikidata の型 `string`）（1,025 列）
- 例1：32.0 | 91.0 | 61.0 | 56.0 | 81.0（表：location or destination point／同じ表の列：label, description, country, instance of, located in the admi…, Commons category）
- 例2：033 | 081 | 091 | 032 | 061（表：beginning／同じ表の列：label, description, country, located in the admi…, coat of arms image, Commons category）
- 例3：636.0 | 618.0 | 573.0 | 217.0 | 314.0（表：capital city／同じ表の列：label, description, country, instance of, coordinate location, located in the admi…）

## g0160 — wikidbs10k：見出し「anthem」（Wikidata の型 `wikibase-entityid`）（1,024 列）
- 例1：Forged from the Love of Liberty | Il Canto degli Italiani | National Anthem of Colombia | Namibia, Land of the Brave | National Anthem of Bolivia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：State Anthem of the Soviet Union | Himnusz | Swiss Psalm | The Star-Spangled Banner | Maamme（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：State Anthem of the Kyrgyz Republic | National Anthem of Peru | National anthem of Tajikistan | Advance Australia Fair | Du gamla, du fria（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0161 — wikidbs10k：見出し「highest point」（Wikidata の型 `wikibase-entityid`）（1,009 列）
- 例1：Mount Pico smakulada | Mount Fuji | Galdhøpiggen | Mount Elbrus | Jebel ech Chambi（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Mount Everest | Mount Pico smakulada | Mount Tahat | Mount Hermon | Jebel ech Chambi（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Torre Cerredo | Mesa de los Tres Reyes | Cerro Calderón | Peña Prieta | Serra do Faro（表：political border／同じ表の列：label, description, INE municipality co…, Dewey Decimal Class…, located in the admi…, ISO 3166-2 code）

## g0162 — wikidbs10k：見出し「gacs id」（Wikidata の型 `string`）（1,008 列）
- 例1：757 | 745 | 11158 | 223 | 355（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：364 | 601 | 193 | 577 | 55（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：310 | 160 | 199 | 250 | 574（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0163 — wikidbs10k：見出し「demographics of topic」（Wikidata の型 `wikibase-entityid`）（1,007 列）
- 例1：demographics of Trinidad and Tobago | demographics of Japan | demographics of Germany | demographics of Mongolia | demographics of Iceland（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：demographics of Spain | demographics of Luxembourg | demographics of Switzerland | demographics of Germany | demographics of Tunisia（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：demographics of Kyrgyzstan | demographics of Chile | demographics of Spain | demographics of Slovakia | demographics of Senegal（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0164 — wikidbs10k：見出し「category for films shot at this location」（Wikidata の型 `wikibase-entityid`）（1,005 列）
- 例1：Category:Films shot in New Zealand | Category:Films shot in Singapore | Category:Films shot in the Czech Republ… | Category:Films shot in Belize | Category:Films shot in Eritrea（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Category:Films shot in the Czech Republ… | Category:Films shot in the United States | Category:Films shot in Switzerland | Category:Films shot in Egypt | Category:Films shot in Yugoslavia（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Category:Films shot in Jordan | Category:Films shot in China | Category:Films shot in Israel | Category:Films shot in Germany | Category:Films shot in North Macedonia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0165 — wikidbs10k：見出し「github topic」（Wikidata の型 `string`）（1,002 列）
- 例1：croatia | morocco | uzbekistan | ireland | argentina（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：finland | russia | slovenia | portugal | syria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：estonia | kazakhstan | senegal | canada | china（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0166 — wikidbs10k：見出し「museum-digital place id」（Wikidata の型 `string`）（1,000 列）
- 例1：6670 | 4022 | 276 | 9646 | 2407（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：197 | 841 | 589 | 2407 | 209（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：8426 | 209 | 4022 | 197 | 2996（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0167 — wikidbs10k：見出し「history of topic」（Wikidata の型 `wikibase-entityid`）（999 列）
- 例1：history of Portugal | history of Mongolia | history of Taiwan | history of Paraguay | history of Thailand（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：history of Spain | history of Germany | history of Italy | history of Luxembourg | history of Turkey（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：history of the United Kingdom | history of Slovakia | history of Canada | History of Ukraine | history of the Czech lands（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0168 — wikidbs10k：見出し「geography of topic」（Wikidata の型 `wikibase-entityid`）（988 列）
- 例1：geography of Azerbaijan | geography of Lithuania | geography of Poland | geography of Costa Rica | geography of Romania（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：geography of the Soviet Union | geography of Ukraine | geography of Spain | geography of Germany | geography of Turkey（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：geography of Azerbaijan | geography of Namibia | geography of China | geography of Morocco | geography of France（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0169 — wikidbs10k：見出し「coordinates of easternmost point」（Wikidata の型 `globecoordinate`）（979 列）
- 例1：40.66620273 | 56.27805488 | 8.3230929 | 23.49999976 | 32.51311（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：42.29053051 | 46.46978084 | 49.805742 | 49.55060726 | 52.48106832（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：34.87287868 | 34.78095219 | 34.76201924 | 34.66383828 | 34.6918859（表：Limassol District／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）

## g0170 — wikidbs10k：見出し「klexikon article id」（Wikidata の型 `string`）（977 列）
- 例1：Slowakei | Iran | Kasachstan | Schweden | Malaysia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Syrien | Türkei | Finnland | Tunesien | Großbritannien（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Schweden | Kanada | Brasilien | Peru | Australien（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0171 — wikidbs10k：見出し「wikimedia outline」（Wikidata の型 `wikibase-entityid`）（976 列）
- 例1：outline of Singapore | outline of Canada | outline of Romania | outline of South Korea | outline of Taiwan（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：outline of Turkey | outline of Syria | outline of Germany | outline of Malta | outline of the United States（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：outline of Jordan | outline of Serbia | outline of Senegal | outline of Kyrgyzstan | outline of Azerbaijan（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0172 — wikidbs10k：見出し「currency」（Wikidata の型 `wikibase-entityid`）（969 列）
- 例1：Japanese yen | Barbadian dollar | Belize dollar | Paraguayan guaraní | new shekel（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：solidus | euro | Soviet ruble | hryvnia | pound sterling（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Russian ruble | rupiah | renminbi | United States dollar | Nuevo sol（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0173 — wikidbs10k：見出し「namuwiki id」（Wikidata の型 `string`）（968 列）
- 例1：나미비아 | 튀니지 | 쿠바 | 대한민국 | 도미니카 공화국（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：벨기에 | 폴란드 | 독일 | 우크라이나 | 네덜란드（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：우크라이나 | 아르메니아 | 북마케도니아 | 카자흐스탄 | 프랑스（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0174 — wikidbs10k：見出し「coordinates of southernmost point」（Wikidata の型 `globecoordinate`）（966 列）
- 例1：47.2700279 | -56.53826 | 55.336944444444 | 13.740194444444 | 49.00263222（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：37.67337596 | 49.44775 | 49.95673883 | 44.386416666667 | 45.73703926（表：country／同じ表の列：label, description, Great Russian Encyc…, GND ID, category of associa…, emergency phone num…）
- 例3：34.86057276 | 34.73150417 | 34.79612494 | 34.93608052 | 34.82511372（表：Limassol District／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）

## g0175 — wikidbs10k：見出し「coordinates of westernmost point」（Wikidata の型 `globecoordinate`）（966 列）
- 例1：27.704167 | 52.283166666667 | 39.69181618 | 54.45826455 | 48.38066809（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：51.05110016 | 46.29772959 | 27.704167 | 50.25239141 | 39.90666652（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：34.71628986 | 34.66414764 | 34.84436061 | 34.6938342 | 34.8704974（表：Limassol District／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）

## g0176 — wikidbs10k：見出し「treccani's dizionario di storia id」（Wikidata の型 `string`）（964 列）
- 例1：grecia | bulgaria | gran-bretagna | kazakistan | ucraina（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：svezia | polonia | finlandia | malta | ungheria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：indonesia | australia | birmania | cina | canada（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0177 — wikidbs10k：見出し「replaces」（Wikidata の型 `wikibase-entityid`）（962 列）
- 例1：Portuguese Empire | Ukrainian Soviet Socialist Republic | Russian Soviet Federative Socialist Rep… | Thirteen Colonies | Kingdom of Finland（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：Empire of Brazil | United Kingdom of the Netherlands | Latvian Soviet Socialist Republic | German Confederation | Congress Poland（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Province of Canada | United Kingdom of Great Britain and Ire… | Irish Free State | Korea | Lithuanian Soviet Socialist Republic（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0178 — wikidbs10k：見出し「unicode character」（Wikidata の型 `string`）（957 列）
- 例1：🇧🇴 | 🇳🇦 | 🇳🇴 | 🇲🇦 | 🇦🇷（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：🇵🇹 | 🇵🇱 | 🇪🇬 | 🇮🇹 | 🇭🇺（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：🇮🇩 | 🇰🇿 | 🇦🇲 | 🇷🇺 | 🇮🇱（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0179 — wikidbs10k：見出し「eurovoc id」（Wikidata の型 `string`）（956 列）
- 例1：4662 | 3401 | 1519 | 5876 | 888（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：4580 | 4320 | 2286 | 888 | 3774（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：5892 | 5693 | 1532 | 5040 | 4160（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0180 — wikidbs10k：見出し「applies to jurisdiction」（Wikidata の型 `wikibase-entityid`）（950 列）
- 例1：Vilanova de Segrià | Alfarràs | Gimenells i el Pla de la Font | Sarroca de Lleida | Almatret（表：Catalan regional election 2015 in Segrià／同じ表の列：label, description, instance of, country, point in time, office contested）
- 例2：Menàrguens | Torregrossa | Vilanova de Segrià | Lleida | Alfés（表：office held by head of government／同じ表の列：label, description, subclass of, country, instance of, female form of label）
- 例3：United Kingdom | Kingdom of the Netherlands | Kingdom of Denmark | The Hague | District of Columbia（表：mandate／同じ表の列：label, description, subclass of, instance of, country, topic's main catego…）

## g0181 — wikidbs10k：見出し「hashtag」（Wikidata の型 `string`）（947 列）
- 例1：Sweden | UnitedKingdom | Uzbekistan | Portugal | Netherlands（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Spain | CzechRepublic | China | Iran | Portugal（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Deutschland | SouthAfrica | China | Kyrgyzstan | France（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0182 — wikidbs10k：見出し「lowest point」（Wikidata の型 `wikibase-entityid`）（947 列）
- 例1：Lake Maggiore | Étang de Lavalduc | Lagunillas | North Slob | Atlantic Ocean（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Caspian Sea | Elbe | Ayding Lake | Adriatic Sea | Neuendorf-Sachsenbande（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Baltic Sea | Neuendorf-Sachsenbande | Dead Sea | Arctic Ocean | Caspian Sea（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0183 — wikidbs10k：見出し「edition number」（Wikidata の型 `string`）（945 列）
- 例1：60 | 49 | 33 | 44 | 19（表：Japanese Badminton Championships／同じ表の列：label, description, sport, country, point in time, followed by）
- 例2：30 | 60 | 24 | 67 | 18（表：followed by／同じ表の列：label, description, sport, country, point in time, followed by）
- 例3：33 | 38 | 47 | 64 | 42（表：follows／同じ表の列：label, description, sport, country, point in time, followed by）

## g0184 — wikidbs10k：見出し「stw thesaurus for economics id」（Wikidata の型 `string`）（929 列）
- 例1：17746-5 | 17749-6 | 17927-1 | 17915-1 | 17590-3（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：17746-5 | 16989-5 | 17039-2 | 17104-3 | 17198-3（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：17915-1 | 18012-3 | 17829-1 | 17500-2 | 17935-2（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0185 — wikidbs10k：見出し「office held by head of state」（Wikidata の型 `wikibase-entityid`）（927 列）
- 例1：president of Germany | President of the Czech Republic | President of Ecuador | president of Bolivia | Yang di-Pertuan Agong（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：President of the United States | President of Ukraine | President of the Soviet Union | President of Syria | Supreme Leader of Iran（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：President of Israel | President of Ukraine | King of Morocco | President of Myanmar | President of Armenia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0186 — wikidbs10k：見出し「ysa id」（Wikidata の型 `string`）（926 列）
- 例1：Y106260 | Y105182 | Y108649 | Y108007 | Y105111（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Y105037 | Y108901 | Y104984 | Y107664 | Y105573（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Y94383 | Y105078 | Y122768 | Y94479 | Y105098（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0187 — wikidbs10k：見出し「brockhaus enzyklopädie online id」（Wikidata の型 `string`）（924 列）
- 例1：serbien | luxemburg-20 | neuseeland | vereinigte-staaten-von-amerika | el-salvador（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：schweiz | frankreich | luxemburg-20 | tunesien | iran（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Belarus | sudafrika | brasilien | senegal-20 | jordanien（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0188 — sotab_v2：元の種類 `Energy`（920 列）
- 例1：555 kcal | 279 kcal | 200 kcal | 269 kcal | 376 kcal（DBpedia：energy）
- 例2：195 calories | 119 | 304 calories | 228 calories | 214（DBpedia：energy）
- 例3：327 kcal | 191 kcal | 205 kcal | 37 kcal | 250 kcal（DBpedia：energy）

## g0189 — wikidbs10k：見出し「diplomatic relation」（Wikidata の型 `wikibase-entityid`）（919 列）
- 例1：Afghanistan | Canada | Argentina | European Union | Germany（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Afghanistan | Luxembourg | United States of America | France | Yemen（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：United States of America | Donetsk People's Republic | Albania | European Union | Argentina（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0190 — wikidbs10k：見出し「executive body」（Wikidata の型 `wikibase-entityid`）（918 列）
- 例1：Council of Ministers | Executive Yuan | Government of Puerto Rico | Government of Luxembourg | Government of Croatia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Diputación Provincial de Pontevedra | Gipuzkoa Foral Council | Diputación Provincial de Cuenca | Diputación Provincial de Guadalajara | Diputación Provincial de Canarias（表：jurisdiction／同じ表の列：label, description, INE municipality co…, Dewey Decimal Class…, located in the admi…, ISO 3166-2 code）
- 例3：Diputación Provincial de Ciudad Real | Government of the Principality of Astur… | Diputación Provincial de Soria | Provincial Deputation of Málaga | Diputación Provincial de Almería（表：political border／同じ表の列：label, description, INE municipality co…, Dewey Decimal Class…, located in the admi…, ISO 3166-2 code）

## g0191 — wikidbs10k：見出し「wikisimpsons id」（Wikidata の型 `string`）（917 列）
- 例1：48345 | 48461 | 41871 | 16275 | 48596（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：16278 | 48597 | 48357 | 17522 | 48553（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：41871.0 | 16589.0 | 48356.0 | 20934.0 | 48372.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0192 — wikidbs10k：見出し「human development index」（Wikidata の型 `quantity`）（916 列）
- 例1：+0.858 | +0.805 | +0.937 | +0.936 | +0.764（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+0.937 | +0.930 | +0.905 | +0.918 | +0.774（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：+0.802 | +0.919 | +0.713 | +0.822 | +0.890（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0193 — sotab_v2：元の種類 `Language`（911 列）
- 例1：en-US | es-MX | pt-BR
- 例2：English
- 例3：fr | es | it | en | pt

## g0194 — wikidbs10k：見出し「spanish vikidia id」（Wikidata の型 `string`）（910 列）
- 例1：China | Costa_Rica | Ecuador | Namibia | Eritrea（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Túnez | República_Checa | Ucrania | Eslovenia | Hungría（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Kazajistán | Reino_Unido | Canadá | Armenia | Namibia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0195 — wikidbs10k：見出し「yle topic id」（Wikidata の型 `string`）（910 列）
- 例1：18-176394 | 18-199405 | 18-193871 | 18-174749 | 18-178301（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：18-174340 | 18-195299 | 18-192750 | 18-199405 | 18-202741（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：18-166989 | 18-170954 | 18-202873 | 18-199102 | 18-168817（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0196 — wikidbs10k：見出し「le monde diplomatique subject id」（Wikidata の型 `string`）（906 列）
- 例1：pays/belgique | pays/chili | pays/trinitetobago | pays/suede | pays/maurice（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：pays/hongrie | pays/chine | pays/malte | pays/france | pays/russie（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：pays/israel | pays/senegal | pays/canada | pays/maroc | pays/azerbaidjan（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0197 — wikidbs10k：見出し「country calling code」（Wikidata の型 `string`）（902 列）
- 例1：+45 | +886 | +64 | +61 | +57（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+44 | +218 | +352 | +213 | +33（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：+55 | +44 | +421 | +972 | +420（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0198 — wikidbs10k：見出し「top-level internet domain」（Wikidata の型 `wikibase-entityid`）（901 列）
- 例1：.ru | .dz | .az | .dk | .be（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：.ly | .fi | .de | .yu | .tr（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：.na | .br | .il | .ru | .ca（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0199 — wikidbs10k：見出し「iso 3166-1 alpha-2 code」（Wikidata の型 `string`）（900 列）
- 例1：EE | AU | DE | BY | MU（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：CZ | IT | FI | PT | YU（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：JO | IL | CZ | SU | SE（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0200 — wikidbs10k：見出し「iso 3166-1 alpha-3 code」（Wikidata の型 `string`）（900 列）
- 例1：SWE | PRY | LVA | TTO | CHL（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：SWE | EGY | PRT | UKR | TUN（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：FRA | JOR | ITA | SVK | AUS（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0201 — wikidbs10k：見出し「iso 3166-1 numeric code」（Wikidata の型 `string`）（900 列）
- 例1：764 | 642 | 516 | 300 | 348（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：804 | 012 | 442 | 156 | 840（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：710 | 276 | 031 | 807 | 076（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0202 — wikidbs10k：見出し「driving side」（Wikidata の型 `wikibase-entityid`）（900 列）
- 例1：right | left（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：right | left（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：left | right（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0203 — wikidbs10k：見出し「hds id」（Wikidata の型 `string`）（897 列）
- 例1：003478 | 011196 | 003367 | 042855 | 003411（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：003405 | 003364 | 003352 | 003353 | 011196（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：50194 | 8327 | 1681 | 7689 | 1851（表：location or destination point／同じ表の列：label, description, country, instance of, located in the admi…, Commons category）

## g0204 — wikidbs10k：見出し「ioc country code」（Wikidata の型 `string`）（896 列）
- 例1：ANT | UKR | TUN | BAR | ARG（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：RUS | NED | UKR | POL | EGY（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：NAM | RSA | FRA | TJK | BRA（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0205 — wikidbs10k：見出し「mains voltage」（Wikidata の型 `quantity`）（891 列）
- 例1：+100 | +115 | +120 | +230 | +240（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+120 | +220 | +230 | +127（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：+127 | +220 | +120 | +230（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0206 — wikidbs10k：見出し「total fertility rate」（Wikidata の型 `quantity`）（891 列）
- 例1：+2.363 | +2.968 | +1.931 | +1.707 | +1.57（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+1.35 | +1.38 | +2.2 | +1.83 | +1.979（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：+3.522 | +1.99 | +5.09 | +1.8615 | +1.89（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0207 — wikidbs10k：見出し「expressed in」（Wikidata の型 `wikibase-entityid`）（891 列）
- 例1：testicle | ganglionic eminence | bone marrow cells | jejunum | retinal pigment epithelium（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, ortholog）
- 例2：anterior horn of spinal cord | olfactory tubercle | retinal pigment epithelium | mirror | internal carotid artery（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例3：testicle | muscle tissue | heart | central nervous system | esophagus（表：encoded by／同じ表の列：label, description, Entrez Gene ID, Ensembl gene ID, RefSeq RNA ID, Ensembl transcript …）

## g0208 — wikidbs10k：見出し「homologene id」（Wikidata の型 `string`）（888 列）
- 例1：69032.0 | 93492.0 | 115614.0 | 23484.0 | 100644.0（表：encoded by／同じ表の列：label, description, Entrez Gene ID, RefSeq RNA ID, ortholog, encodes）
- 例2：45457.0 | 133909.0 | 69032.0 | 93492.0 | 133909（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, chromosome）
- 例3：31310.0 | 4313.0 | 137677.0 | 4079.0 | 21196.0（表：encoded by／同じ表の列：label, description, Entrez Gene ID, Ensembl gene ID, RefSeq RNA ID, Ensembl transcript …）

## g0209 — wikidbs10k：見出し「statoids id」（Wikidata の型 `string`）（887 列）
- 例1：ucz | utn | uve | ucu | uhu（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：uus | usi | udz | ugr | ulu（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：umk | ucz | ucn | urs | ude（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0210 — wikidbs10k：見出し「electrical plug type」（Wikidata の型 `wikibase-entityid`）（887 列）
- 例1：Europlug | NEMA 1-15 | BS 1363 | AC power plugs and sockets: British and… | AS/NZS 3112（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：NEMA 1-15 | Type E | Europlug | Schuko | BS 1363（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Schuko | BS 1363 | NEMA 5-15 | Europlug | AS/NZS 3112（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0211 — wikidbs10k：見出し「life expectancy」（Wikidata の型 `quantity`）（885 列）
- 例1：+78.69024 | +71.314 | +75.675 | +82.5 | +74.52927（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+81.1 | +80.79 | +78.69024 | +75.731 | +71.685（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：+72.3 | +67.146 | +73.82683 | +82.60 | +69.191（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0212 — wikidbs10k：見出し「basic form of government」（Wikidata の型 `wikibase-entityid`）（885 列）
- 例1：presidential system | single-party system | directorial system | federal parliamentary republic | constitutional monarchy（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：dictatorship | directorial system | feudal monarchy | federal parliamentary republic | Islamic Republic（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：semi-presidential system | representative democracy | constitutional monarchy | soviet republic | democratic republic（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0213 — wikidbs10k：見出し「has quality」（Wikidata の型 `wikibase-entityid`）（885 列）
- 例1：free country | partly free country | not-free country（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：partly free country | not-free country | free country（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：partly free country | free country | not-free country（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0214 — wikidbs10k：見出し「wipo st.3」（Wikidata の型 `string`）（879 列）
- 例1：KR | BE | CO | ZA | FR（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：SI | EG | PT | HU | NL（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：RU | PE | SN | ZA | DE（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0215 — wikidbs10k：見出し「maritime identification digits」（Wikidata の型 `string`）（876 列）
- 例1：624 | 436 | 625 | 277 | 304（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：272 | 263 | 445 | 422 | 224（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：265 | 216 | 438 | 270 | 226（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0216 — wikidbs10k：見出し「the world factbook country id」（Wikidata の型 `string`）（871 列）
- 例1：dominican-republic | sweden | united-states | slovakia | czechia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：czechia | iran | syria | united-states | belgium（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：ukraine | canada | chile | united-kingdom | armenia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0217 — wikidbs10k：見出し「tasteatlas id」（Wikidata の型 `string`）（870 列）
- 例1：USA | bulgaria | spain | tunisia | albania（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：malta | iran | germany | finland | syria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：spain | czech-republic | myanmar | israel | germany（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0218 — wikidbs10k：見出し「civicus monitor country entry」（Wikidata の型 `string`）（869 列）
- 例1：rwanda | paraguay | russia | bulgaria | bahamas（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：switzerland | china | italy | sweden | luxembourg（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：sweden | estonia | azerbaijan | united-states-america | belarus（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0219 — wikidbs10k：見出し「itu/iso/iec object identifier」（Wikidata の型 `string`）（867 列）
- 例1：2.16.688 | 2.16.364 | 2.16.348 | 2.16.196 | 2.16.756（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：2.16.616 | 2.16.804 | 2.16.203 | 2.16.620 | 2.16.470（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：2.16.807 | 2.16.710 | 2.16.688 | 2.16.124 | 2.16.398（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0220 — wikidbs10k：見出し「culture」（Wikidata の型 `wikibase-entityid`）（867 列）
- 例1：culture of the Bahamas | culture of Slovakia | culture of Sweden | culture of Andorra | culture of New Zealand（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：culture of the United Kingdom | Chinese culture | culture of Turkey | culture of Libya | culture of Algeria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：culture of the Czech Republic | culture of Slovakia | culture of Israel | culture of Brazil | culture of Jordan（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0221 — wikidbs10k：見出し「postimees topic id」（Wikidata の型 `string`）（861 列）
- 例1：47228 | 1209 | 3927 | 3997 | 149（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：2647 | 3997 | 7811 | 2505 | 11991（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：18664 | 8497 | 5122 | 20174 | 2883（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0222 — wikidbs10k：見出し「insee countries and foreign territories code」（Wikidata の型 `string`）（859 列）
- 例1：99317 | 99226 | 99114 | 99253 | 99118（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：99142 | 99139 | 99137 | 99116 | 99208（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：99231 | 99156 | 99121 | 99127 | 99311（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0223 — wikidbs10k：見出し「bbc news topic id」（Wikidata の型 `string`）（857 列）
- 例1：cdl8n2edxeet | cx1m7zg0gzdt | cywd23g04get | c8nq32jw8yjt | cz4pr2gd580t（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：cywd23g0q1mt | c302m85qenvt | cjnwl8q4ggwt | c302m85q5xzt | cx1m7zg01xyt（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：cnx753jej07t | c302m85qenyt | cmj34zmwxv0t | c1038wnxe4rt | c77jz3md4rwt（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0224 — wikidbs10k：見出し「democracy index」（Wikidata の型 `quantity`）（853 列）
- 例1：+3.38 | +7.51 | +7.16 | +8.16 | +7.90（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+1.95 | +7.92 | +7.39 | +1.08 | +4.48（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：+7.24 | +3.49 | +5.49 | +9.24 | +2.59（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0225 — wikidbs10k：見出し「itu letter code」（Wikidata の型 `string`）（853 列）
- 例1：NMB | ROU | TUR | ISL | ETH（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：EGY | SYR | S | LUX | KRE（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：BLR | S | CZE | INS | B（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0226 — wikidbs10k：見出し「dr topic id」（Wikidata の型 `string`）（852 列）
- 例1：kroatien | island | namibia | thailand | australien（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：tjekkiet | usa | storbritannien | schweiz | malta（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：sydafrika | rusland | sverige | indonesien | italien（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0227 — wikidbs10k：見出し「obo gazetteer id」（Wikidata の型 `string`）（850 列）
- 例1：00002948 | 00002954 | 00002933 | 00002901 | 00002635（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：00002937 | 00000562 | 00002955 | 00002474 | 00002646（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：00000913 | 00004941 | 00002825 | 00000565 | 00006886（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0228 — wikidbs10k：見出し「central bank」（Wikidata の型 `wikibase-entityid`）（847 列）
- 例1：Central Bank of Argentina | De Nederlandsche Bank | Bank of Albania | South African Reserve Bank | Central Bank of The Bahamas（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Bank of Estonia | Bank of Namibia | Central Bank of Brazil | Bank of Canada | Bank of France（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Reserve Bank of India | Central Bank of Brazil | Swiss National Bank | Central Bank of Chile | South African Reserve Bank（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, topic's main Wikime…）

## g0229 — wikidbs10k：見出し「fast id」（Wikidata の型 `string`）（845 列）
- 例1：1205190 | 1208963 | 1205213 | 1206148 | 1204166（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：1206830 | 1260664 | 1204543 | 1205669 | 1223630（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：1205362.0 | 1210276.0 | 1204543.0 | 1205261.0 | 1210272.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0230 — wikidbs10k：見出し「gnis id」（Wikidata の型 `string`）（845 列）
- 例1：1501502 | 1480111 | 1673675 | 1480179 | 1779803（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）
- 例2：758547 | 758556 | 722309 | 766317 | 723933（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：758558 | 758509 | 758512 | 758496 | 758561（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0231 — wikidbs10k：見出し「zhihu topic id」（Wikidata の型 `string`）（845 列）
- 例1：19557502 | 19586942 | 19592266 | 20007252 | 19627981（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：19551627 | 20007230 | 19642259 | 19592266 | 20004553（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：19592266.0 | 20007328.0 | 19554996.0 | 19552320.0 | 19574145.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0232 — sotab_v2：元の種類 `EventAttendanceModeEnumeration`（844 列）
- 例1：https://schema.org/OnlineEventAttendanc… | https://schema.org/OfflineEventAttendan…
- 例2：https://schema.org/OfflineEventAttendan… | https://schema.org/OnlineEventAttendanc…
- 例3：https://schema.org/OfflineEventAttendan…

## g0233 — wikidbs10k：見出し「new york times topic id」（Wikidata の型 `string`）（835 列）
- 例1：destination/thailand | destination/ecuador | destination/israel | destination/mongolia | destination/paraguay（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：destination/tajikistan | destination/armenia | destination/macedonia | destination/spain | destination/italy（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：destination/liberia | destination/angola | destination/finland | destination/france | destination/united-states（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0234 — wikidbs10k：見出し「writing system」（Wikidata の型 `wikibase-entityid`）（825 列）
- 例1：Latin script（表：given name／同じ表の列：label, description, instance of, native label, language of work or…, said to be the same…）
- 例2：Ukrainian alphabet | Latin script（表：given name／同じ表の列：label, description, instance of, said to be the same…, different from, native label）
- 例3：Latin script | Cyrillic script（表：family name／同じ表の列：label, description, different from, native label, Caverphone, Commons category）

## g0235 — sotab_v2：元の種類 `EducationalOccupationalCredential`（823 列）
- 例1：• Degree in Computer Science, Informati… | • Higher Diploma or above in Human Reso… | • Degree holder in Accounting or Financ… | • Degree holder in Accounting, Finance … | • Possess CS/LLB or ICSA qualification …
- 例2：* Desire to be a part of the game-chang… | * Must be age 18 and obtained high scho… | * Builds experience with solutions-base… | * Achievement driven; enjoy competition… | * Must be abe to speak English face-to-…
- 例3：<table><thead><tr><th style=\"width: 21… | <p>Master Degree in Sociology with Ph.D… | <table style=\"width: 100%;\"><thead><t… | <table><thead><tr><th style=\"width: 32… | <p>Ph. D. in Statistics from a reputed …

## g0236 — wikidbs10k：見出し「gini coefficient」（Wikidata の型 `quantity`）（823 列）
- 例1：+36.1 | +63.1 | +45.4 | +47.7 | +35.2（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+34.9 | +41.9 | +25.4 | +31.7 | +36.1（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：+25.2 | +31.7 | +27.8 | +59.1 | +32.8（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0237 — wikidbs10k：見出し「wolfram language entity code」（Wikidata の型 `string`）（817 列）
- 例1：Entity["AdministrativeDivision", {"Alle… | Entity["AdministrativeDivision", {"Virg… | Entity["AdministrativeDivision", {"Buck… | Entity["AdministrativeDivision", {"Ches… | Entity["AdministrativeDivision", {"Lanc…（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）
- 例2：Entity["Isotope", "Xenon132"] | Entity["Isotope", "Iodine130"] | Entity["Isotope", "Xenon130"] | Entity["Isotope", "Antimony108"] | Entity["Isotope", "Xenon135"]（表：decays to／同じ表の列：label, description, subclass of, instance of, atomic number, neutron number）
- 例3：Entity["Surname", "Aiken"] | Entity["Surname", "Majchrowski"] | Entity["Surname", "Bowser"] | Entity["Surname", "Khan"] | Entity["Surname", "Meijer"]（表：family name／同じ表の列：label, description, different from, native label, writing system, Caverphone）

## g0238 — wikidbs10k：見出し「twinned administrative body」（Wikidata の型 `wikibase-entityid`）（811 列）
- 例1：Berlin | Vilnius | Aubigny-sur-Nère | Tallinn | Munich（表：capital city／同じ表の列：label, description, instance of, Commons category, coordinate location, image）
- 例2：Bern | Iffezheim | Liverpool | Skopje | Halmstad Municipality（表：administrative territorial entity／同じ表の列：label, description, locator map image, coordinate location, instance of, located in the admi…）
- 例3：Eskişehir | Iwanuma | Pachuca | Ahmedabad | Tapa Rural Municipality（表：capital city／同じ表の列：label, description, country, instance of, Commons category, coordinate location）

## g0239 — wikidbs10k：見出し「national library of israel id (old)」（Wikidata の型 `string`）（807 列）
- 例1：000984039 | 000977248 | 000975694 | 000975849 | 000983256（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：975586.0 | 983119.0 | 751421.0 | 128739.0 | 977240.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：000986005 | 000081338 | 000975636 | 000975650 | 000984450（表：jurisdiction／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0240 — wikidbs10k：見出し「happy planet index score」（Wikidata の型 `quantity`）（804 列）
- 例1：+46.5 | +47.6 | +50.9 | +50.5 | +41.9（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+41.9 | +40.2 | +36.8 | +46.8 | +52.7（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：60.1 | 45.6 | 54.3 | 51.3 | 37.4（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0241 — wikidbs10k：見出し「per capita income」（Wikidata の型 `quantity`）（803 列）
- 例1：+41255 | +39788 | +38926 | +28048 | +42298（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）
- 例2：66967.0 | 18655.0 | 19745.0 | 40249.0 | 30078.0（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：29671 | 30078 | 25237 | 20810 | 27778（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0242 — wikidbs10k：見出し「m.49 code」（Wikidata の型 `string`）（797 列）
- 例1：398 | 756 | 170 | 646 | 036（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：036 | 276 | 826 | 076 | 124（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：276.0 | 410.0 | 710.0 | 124.0 | 246.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0243 — wikidbs10k：見出し「grove art online id」（Wikidata の型 `string`）（792 列）
- 例1：T060834 | T074737 | T041544 | T016513 | T010288（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：T007414 | T087081 | T093040 | T016513 | T068860（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：T082574 | T007388 | T066591 | T045172 | T020982（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0244 — wikidbs10k：見出し「hasc」（Wikidata の型 `string`）（789 列）
- 例1：CH.ZH.ZH | CH.TI | CH.AG.BG | CH.GR.PD | CH.SO.LB（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, coat of arms image, coordinate location）
- 例2：US.VA.AL | US.VA.CD | US.VA.BK | US.VA | US.VA.VI（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）
- 例3：US.MO.SV | US.MO.CK | US.MO.MD | US.MO.SL | US.MO.TA（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0245 — wikidbs10k：見出し「ortholog」（Wikidata の型 `wikibase-entityid`）（786 列）
- 例1：Pip5kl1 | PIP5K1C | Pip4k2c | Pip5k1a | ppk-2（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, encodes）
- 例2：Pip4k2c | Pip5kl1 | PIP5K1C | pip5k1ab | PIP5K59B（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例3：Smad5 | Smad3 | Smad9 | Nfix | smad1（表：encoded by／同じ表の列：label, description, Entrez Gene ID, Ensembl gene ID, HomoloGene ID, RefSeq RNA ID）

## g0246 — wikidbs10k：見出し「comic vine id」（Wikidata の型 `string`）（779 列）
- 例1：4020-55928 | 4020-57479 | 4020-55916 | 4020-56325 | 4020-55820（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：4020-55950 | 4020-55868 | 4020-55853 | 4020-64500 | 4020-56325（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：4005-113167 | 4005-69322 | 4005-155574 | 4005-113642 | 4005-81685（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, Pokémon index, part of, height）

## g0247 — wikidbs10k：見出し「joconde location id」（Wikidata の型 `string`）（772 列）
- 例1：T84-252 | T84-3194 | T84-305 | T84-3549 | T84-302（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：T84-3563 | T84-303 | T84-3504 | T84-742 | T84-473（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：T84-742 | T84-3562 | T84-694 | T84-3601 | T84-372（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0248 — wikidbs10k：見出し「water as percent of area」（Wikidata の型 `quantity`）（770 列）
- 例1：+4.3 | +20.5 | +1.7918 | +3.1 | +0.7（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）
- 例2：1.3838 | 3.3781 | 4.2446 | 0.0758 | 2.6415（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：3.2 | 10.5 | 0.1 | 0.4 | 1.1（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0249 — sotab_v2：元の種類 `ItemList`（755 列）
- 例1：Jahmiel Winning Download | Ship Bollard Manufacturers Mail | Tick Tock Feat 24Kgoldn Clean Bandit Ma… | List Turkey Bathtub Manufacturers Mail | The Cuppycake Song Buddy Castle（DBpedia：List）
- 例2：Sydney Renae Mp3 Download | All About The Bass Home Free | I Bring Me Mp3 Download | Show Me The Meaning Lyrics | Beyonce Formation Mp3 Free Download（DBpedia：List）
- 例3：Tujhme Rab Dikhta Hai Mp3 Song Download… | Macklemore Ryan Lewis Thrift Shop Feat … | Gold Devaraj Ghibran Alagiya Sirukki Fr… | Pritam Arijit Singh Shashwat Singh Haan… | Www Pakistani Naat Mp3 Download（DBpedia：List）

## g0250 — wikidbs10k：見出し「gs1 country code」（Wikidata の型 `string`）（750 列）
- 例1：476 | 760-769 | 626 | 530 | 780（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：867 | 619 | 540-549 | 622 | 590（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：611 | 780 | 460-469 | 500-509 | 858（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0251 — wikidbs10k：見出し「analysis & policy observatory term id」（Wikidata の型 `string`）（749 列）
- 例1：3006 | 14159 | 19723 | 12832 | 8956（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：9479 | 2978 | 13562 | 2988 | 9496（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：37862.0 | 2996.0 | 1.0 | 6713.0 | 9496.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0252 — wikidbs10k：見出し「category of people buried here」（Wikidata の型 `wikibase-entityid`）（748 列）
- 例1：Category:Burials in Venezuela | Category:Burials in Hungary | Category:Burials in Estonia | Category:Burials in Denmark | Category:Burials in Costa Rica（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Category:Burials in Sweden | Category:Burials in the United Kingdom | Category:Burials in Canada | Category:Burials in Afghanistan | Category:Burials in Finland（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：Category:Burials in Slovakia | Category:Burials in Finland | Category:Burials in the United States | Category:Burials in Turkey | Category:Burials in Latvia（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0253 — sotab_v2：元の種類 `Time`（732 列）
- 例1：T07:00（DBpedia：time）
- 例2：18:00:00 | 12:00:00 | 06:00:00（DBpedia：time）
- 例3：14:00:00 | 16:00:00 | 12:00:00 | 15:00:00（DBpedia：time）

## g0254 — wikidbs10k：見出し「unemployment rate」（Wikidata の型 `quantity`）（732 列）
- 例1：+3 | +9.4 | +5 | +15 | +19（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+25 | +5 | +4 | +5.2 | +3（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：4.0 | 6.7 | 16.0 | 5.0 | 6.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0255 — sotab_v2：元の種類 `Restaurant/name`（723 列）
- 例1：Denver ChopHouse &amp; Brewery | Mangia Nashville | The Free Bird | Culina at the Four Seasons Los Angeles … | Kendrick's（DBpedia：Restaurant）
- 例2：Gilbert's Chowder House | Nara Sushi | Ricetta's Pizzeria | Becky's Diner | RACHELS L'OSTERIA（DBpedia：Restaurant）
- 例3：Las Brazas Mexican Restaurant | Pizza Patron | El Bucanero - Embassy | Tribeca | Bun N Barrel San Antonio, TX（DBpedia：Restaurant）

## g0256 — wikidbs10k：見出し「motto text」（Wikidata の型 `monolingualtext`）（721 列）
- 例1：حرية، كرامة، عدالة، نظام | Beats to your rhythm | بالشّعب وللشّعب | 홍익인간(弘益人間): 널리 인간을 이롭게 하라 | Vienybė težydi（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Hospitality Beyond Borders | ǃke e: ǀxarra ǁke | In God We Trust | الله، الوطن، الملك | Пролетарии всех стран, соединяйтесь!（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Yurtta sulh, cihanda sulh | Arrive and revive | Made in Italy | Reveal your own Russia | Hospitality Beyond Borders（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0257 — wikidbs10k：見出し「openalex id」（Wikidata の型 `string`）（711 列）
- 例1：C2780101333 | C91986751 | C2779991468 | C2779066085 | C2779740085（表：expressed in／同じ表の列：label, description, Freebase ID, Foundational Model …, instance of, UBERON ID）
- 例2：C2779489039 | C2776662696 | C2779306812 | C2780239966 | C2777677444（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例3：V37672443 | V30525748 | V181568219 | V125754415 | V140889577（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）

## g0258 — wikidbs10k：見出し「urban electric transit country id」（Wikidata の型 `string`）（705 列）
- 例1：64 | 22 | 109 | 5 | 10（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：29 | 101 | 59 | 51 | 33（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：10 | 32 | 24 | 105 | 13（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0259 — wikidbs10k：見出し「vat rate」（Wikidata の型 `quantity`）（679 列）
- 例1：+17 | +13 | +15 | +12.5 | +6（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+13 | +10 | +15 | +25 | +20（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：7.7 | 10.0 | 20.0 | 24.0 | 19.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0260 — wikidbs10k：見出し「bbc things id」（Wikidata の型 `string`）（668 列）
- 例1：92eba8f1-9743-449a-b23c-36e14dfe79e9 | 39267b85-1784-4f4b-80ed-f8cb4a35f337 | db8d6c6f-13c2-44d7-963c-54c06ab0da36 | 48b721b7-2c98-4339-bd9a-968da6653c87 | b8ecc08b-60d7-4eff-b4a0-b6aa5b206e95（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：b18269a2-6d2e-46ed-a021-372a7b03377a | 4bc7e064-44b5-4f17-870c-8bf927f0c9bd | 15f1bcf6-b6ab-48e8-b708-efed41e43d31 | 1791445f-977a-4e6d-b490-51f84bb4fc52 | 03ef2794-4827-470e-b6dd-eec233217405（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：82857f8e-8134-462a-bb32-b7b14f4eab75 | 2e3befc0-e70a-41c7-b6cb-2f8f0d69a7db | b67450e8-ed1d-434b-b01b-8aa7e159381e | 3deb0e53-87ed-4c7d-97c8-d53b5ab50359 | c0adb26a-0bdb-4f42-8c12-7d41b56986de（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0261 — wikidbs10k：見出し「jewish encyclopedia id (russian)」（Wikidata の型 `string`）（668 列）
- 例1：12251 | 12548 | 11122 | 12084 | 10050（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：12531 | 13843 | 13826 | 11302 | 14791（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：14001 | 14791 | 14344 | 12646 | 10720（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0262 — wikidbs10k：見出し「marriageable age」（Wikidata の型 `quantity`）（662 列）
- 例1：+21 | +17 | +20 | +0 | +19（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+0 | +18 | +20 | +21 | +16（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：+21 | +16 | +0 | +17 | +20（表：jurisdiction／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0263 — wikidbs10k：見出し「english vikidia id」（Wikidata の型 `string`）（659 列）
- 例1：Belgium | Ukraine | Italy | China | Germany（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：France | Germany | Chile | Mexico | United_Kingdom（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：Australia | Syria | Hungary | Ukraine | Switzerland（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0264 — wikidbs10k：見出し「open data portal」（Wikidata の型 `wikibase-entityid`）（653 列）
- 例1：Afghanistan Open Data project | GovData | Open Data Philippines | Canada Open Data portal | Chile’s Public Data Portal（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例2：Open Data Philippines | data.public.lu | data.go.jp | Open Data DK | Open data portal Hungary（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Open Data Portal Russia | data.gov.tw | Open data portal Slovenien | Bangladesh Open Data | GovData（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0265 — wikidbs10k：見出し「world encyclopedia of puppetry arts id」（Wikidata の型 `string`）（641 列）
- 例1：myanmar | estonia | kazakhstan | germany | slovakia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：liberia | canada | china | finland | sweden（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：united-states-of-america | australia | algeria | japan | bulgaria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0266 — wikidbs10k：見出し「der spiegel topic id」（Wikidata の型 `string`）（639 列）
- 例1：russland | schweden | ukraine | tschechien | brasilien（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：indien | angola | schweiz | spanien | volksrepublik_china（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：schweden | oesterreich | estland | belarus | polen（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0267 — wikidbs10k：見出し「refseq genome id」（Wikidata の型 `string`）（639 列）
- 例1：NC_000012.12 | NC_051345 | NC_000069 | NC_051342 | NT_033778（表：chromosome／同じ表の列：label, description, found in taxon, instance of）
- 例2：NT_037436 | NC_005107 | NC_000005.10 | NC_000071 | NC_051336（表：chromosome／同じ表の列：label, description, found in taxon, instance of）
- 例3：NC_051352 | NC_007112 | NC_007133 | NC_000013.11 | NT_033777（表：chromosome／同じ表の列：label, description, found in taxon, instance of）

## g0268 — wikidbs10k：見出し「alltrails trail id」（Wikidata の型 `string`）（638 列）
- 例1：switzerland | luxembourg | el-salvador | latvia | paraguay（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：brazil | denmark | switzerland | luxembourg | algeria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：spain | new-zealand | germany | czech-republic | hungary（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0269 — sotab_v2：元の種類 `CategoryCode`（631 列）
- 例1：Construction | Landscape
- 例2：Management | A3 Smart Home | Roadside Service and Automotive | Marketing and Digital Services | A3Ventures
- 例3：Housekeeping | Customer Care | Chemical Engineer | Fashion Designer | Office Assistant

## g0270 — wikidbs10k：見出し「asc leiden thesaurus id」（Wikidata の型 `string`）（626 列）
- 例1：294922253 | 294939792 | 294912452 | 294918175 | 297778617（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：294899545 | 29490249X | 294904255 | 294939792 | 294904271（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：294911715 | 294939857 | 294901094 | 294942807 | 294932275（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0271 — wikidbs10k：見出し「treccani id」（Wikidata の型 `string`）（625 列）
- 例1：cuba | polonia | cile | ecuador | ungheria（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：svezia | paesi-bassi | iran | russia | lussemburgo（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：bielorussia | serbia | senegal | svezia | cile（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0272 — wikidbs10k：見出し「number of out-of-school children」（Wikidata の型 `quantity`）（624 列）
- 例1：+29418 | +5693 | +178653 | +45430 | +4330276（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+198438 | +37720 | +33041 | +48258 | +1815742（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：228797.0 | 18425.0 | 35822.0 | 117710.0 | 1378723.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0273 — wikidbs10k：見出し「age of majority」（Wikidata の型 `quantity`）（612 列）
- 例1：+19 | +20 | +16 | +21 | +18（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：+16 | +18 | +17 | +21（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：20.0 | 18.0 | 19.0 | 21.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0274 — wikidbs10k：見出し「schoenberg database of manuscripts place id」（Wikidata の型 `string`）（605 列）
- 例1：4020 | 868 | 1527 | 629 | 4073（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：971.0 | 924.0 | 967.0 | 13.0 | 12.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：3360 | 1065 | 1527 | 3484 | 3345（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0275 — wikidbs10k：見出し「category combines topics」（Wikidata の型 `wikibase-entityid`）（598 列）
- 例1：Cleveland | Denver | Montreal | Nuevo León | Nevada（表：Wikimedia category／同じ表の列：label, description, Commons category, instance of, category contains）
- 例2：Zürich | Lugano | Davos | person related to this place（表：Wikimedia category／同じ表の列：label, description, instance of, category contains）
- 例3：Esbjerg Municipality | Minnesota | Uppsala Municipality | Varde Municipality | Oklahoma（表：Wikimedia category／同じ表の列：label, description, instance of, category contains）

## g0276 — wikidbs10k：見出し「fandom article id」（Wikidata の型 `string`）（597 列）
- 例1：it.pokemon:Honedge | pokemon:Duraludon | it.pokemon:Lunatone | it.pokemon:Ferroseed | it.pokemon:Porygon-Z（表：Mineral egg group／同じ表の列：label, description, from narrative univ…, Pokémon index, part of, height）
- 例2：world-sports-results:Diving | world-sports-results:Field_Hockey | world-sports-results:Badminton | world-sports-results:Judo | world-sports-results:Table_Tennis（表：type of sport／同じ表の列：label, description, subclass of, Commons category, Library of Congress…, topic's main catego…）
- 例3：world-sports-results:Gymnastics | world-sports-results:Netball | world-sports-results:Field_Hockey | world-sports-results:Diving | world-sports-results:Judo（表：field of work／同じ表の列：label, description, subclass of, Commons category, Library of Congress…, topic's main catego…）

## g0277 — sotab_v2：元の種類 `SportsEvent/name`（585 列）
- 例1：Huddersfield Town vs Norwich | Derby vs Reading | Oldham vs Leyton Orient | Bolton vs Bristol Rovers | Dynamo Kiev vs Lugano（DBpedia：SportsEvent）
- 例2：Mallorca vs Alaves | West Ham vs Cardiff | Ferencvaros vs Ludogorets | Amiens vs Monaco | Barcelona vs Getafe（DBpedia：SportsEvent）
- 例3：Warriors FC vs Dark Side of the maMoon | #5 4S City FC vs #6 Clockwork Orange | #2 Blue Army vs #3 Mean Joe Greens | Sky High vs Dark Side of the maMoon | CHAMPIONSHIP: #2 Blue Army vs #4 Wizard…（DBpedia：SportsEvent）

## g0278 — wikidbs10k：見出し「category contains」（Wikidata の型 `wikibase-entityid`）（585 列）
- 例1：human（表：Wikimedia category／同じ表の列：label, description, Commons category, instance of, category combines t…）
- 例2：human（表：Wikimedia category／同じ表の列：label, description, instance of, category combines t…）
- 例3：human（表：Wikimedia category／同じ表の列：label, description, instance of, category combines t…）

## g0279 — wikidbs10k：見出し「idai.gazetteer id」（Wikidata の型 `string`）（579 列）
- 例1：2281890 | 2283234 | 2044274 | 2042642 | 2086604（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：2088790 | 2281887 | 2042950 | 2290558 | 2076466（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：2293102.0 | 2064998.0 | 2064739.0 | 2086335.0 | 2285871.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0280 — wikidbs10k：見出し「colon classification」（Wikidata の型 `string`）（565 列）
- 例1：SG--55 | SG--579 | SG--594 | SG--931 | SG--72（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例2：SG--5931 | SG--541 | SG--5932 | SG--594 | SG--53（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：SG--5932 | SG--7913 | SG--59226 | SG--53 | SG--671（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0281 — wikidbs10k：見出し「pm20 geo code」（Wikidata の型 `string`）（562 列）
- 例1：E66 | A30 | E26 | E71 | A10（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：A40d | B40 | C19 | A54 | B94（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：E97 | E20 | C56 | D30 | A53（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0282 — sotab_v2：元の種類 `openingHours`（560 列）
- 例1：Mo,Tu,We,Th,Fr,Sat,Sun 07:00-23:45
- 例2：Mo,Tu,We,Th,Fr,Sa,Su 00:00-24:00 | Mo-Su 00:00-24:00
- 例3：Mo, Tu, We, Th, Fr, Sa 9.30:00-20:00

## g0283 — sotab_v2：元の種類 `CreativeWork/name`（558 列）
- 例1：Lucas（DBpedia：WrittenWork）
- 例2：Trish F. | Marlene T. | Richard & Jerrita L. | Mike A. | Gary B.（DBpedia：WrittenWork）
- 例3：His Dark Materials S01 E05 | Love with Flaws Episode 01 | The Good Doctor Season 1 Episode 2 | Wu Assassins Season 01 Episode 07 | The Good Doctor Season 1 Episode 16（DBpedia：WrittenWork）

## g0284 — wikidbs10k：見出し「iso 3166-2 code」（Wikidata の型 `string`）（552 列）
- 例1：GB-ELN | GB-SCB | GB-SCT | GB-ABD | GB-AGB（表：administrative territorial entity／同じ表の列：label, description, category of associa…, Curlie ID, MusicBrainz area ID, capital）
- 例2：GB-NLK | GB-ELN | GB-SCT | GB-AGB | GB-PKN（表：administrative centre／同じ表の列：label, description, instance of, capital, country, Commons category）
- 例3：ES-LU | ES-CU | US-PR | ES-VA | ES-P（表：jurisdiction／同じ表の列：label, description, INE municipality co…, Dewey Decimal Class…, located in the admi…, Commons category）

## g0285 — wikidbs10k：見出し「ne.se id」（Wikidata の型 `string`）（545 列）
- 例1：filippinerna | frankrike | kina | brasilien | united-states（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例2：marocko | united-kingdom | polen | danmark | tyskland（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：united-states | italien | ryska-federationen | australien-(allmän-art) | israel（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0286 — wikidbs10k：見出し「located in or next to body of water」（Wikidata の型 `wikibase-entityid`）（539 列）
- 例1：Atlantic Ocean（表：landform／同じ表の列：label, description, Dewey Decimal Class…, Commons category, instance of, coordinate location）
- 例2：English Channel | Drake Passage | Greenland Sea | Sea of Japan | Pentland Firth（表：ocean current／同じ表の列：label, description, instance of）
- 例3：Western Bug | Indian Ocean | South China Sea | Neusiedl Lake | Lake Constance（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0287 — wikidbs10k：見出し「nalt id」（Wikidata の型 `string`）（535 列）
- 例1：15678 | 15788 | 13932 | 39649 | 14302（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：11928.0 | 19855.0 | 24927.0 | 3005.0 | 13932.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）
- 例3：11924.0 | 16491.0 | 6360.0 | 15678.0 | 38637.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0288 — wikidbs10k：見出し「female population」（Wikidata の型 `quantity`）（534 列）
- 例1：4557 | 150 | 189 | 657 | 1645（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：366 | 403 | 1233 | 893 | 150（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：3749.0 | 750.0 | 7415.0 | 730.0 | 39933.0（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0289 — wikidbs10k：見出し「male population」（Wikidata の型 `quantity`）（527 列）
- 例1：+68657 | +1140 | 1791 | 251 | 150（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：855 | 440 | 119 | 68657 | 1150（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：740.0 | 621.0 | 4048.0 | 4557.0 | 9677.0（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0290 — wikidbs10k：見出し「bhcl uuid」（Wikidata の型 `string`）（517 列）
- 例1：7aacabd6-5c8f-42d5-be3d-92b7cb480bb4 | ffd382be-2f2b-4c19-ae5a-6ba50f65aec5 | 0235138e-838e-4a77-b45b-068626936bab | 7c672690-aa08-4e09-99eb-de5486282524 | 8863bd00-37e2-411b-9a76-5f5cafa29284（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：dfe028fd-2642-4bb8-aaec-32be15dcbed0 | 973d6c80-d1e5-4830-a9cf-2529a3cddd3a | c08becbc-31e5-48c5-8c76-80899bc99154 | 2bde846d-48ca-4ac0-880c-91f4fe24c210 | 011cc308-763e-4aaf-8611-dcad3976bb78（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：371a777b-a6f6-47cb-8062-48c7528e2a82 | 6367e562-de12-41e5-b93e-39cc551085c2 | c1a19b5d-fced-41a5-969d-b31e87e44a30 | 55d59c10-4620-4958-a631-756bf10f2ff8 | d4a959c9-c688-4606-a2f3-ac84bec2fa04（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0291 — wikidbs10k：見出し「topic's main template」（Wikidata の型 `wikibase-entityid`）（513 列）
- 例1：Template:Yamhill County, Oregon | Template:Baker County, Oregon | Template:Umatilla County, Oregon | Template:Wasco County, Oregon | Template:Columbia County, Oregon（表：administrative territorial entity／同じ表の列：label, description, instance of, country, located in the admi…, image）
- 例2：Template:Jefferson County, Oregon | Template:Douglas County, Oregon | Template:Coos County, Oregon | Template:Lincoln County, Oregon | Template:Linn County, Oregon（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, named after）
- 例3：Template:Infobox competitive diver | Template:Infobox gymnast | Template:Infobox boxer | Template:Infobox weightlifter | Template:Infobox field hockey player（表：intentional human activity／同じ表の列：label, description, topic's main catego…, subclass of, field of this occup…, instance of）

## g0292 — sotab_v2：元の種類 `Photograph`（510 列）
- 例1：http://406united.org/wp-content/uploads… | http://406united.org/wp-content/uploads… | http://406united.org/wp-content/uploads… | http://406united.org/wp-content/uploads… | http://406united.org/wp-content/uploads…
- 例2：https://mlbisntj5wcs.i.optimole.com/fu0… | https://mlbisntj5wcs.i.optimole.com/fu0… | https://mlbisntj5wcs.i.optimole.com/fu0… | https://mlbisntj5wcs.i.optimole.com/40l… | https://mlbisntj5wcs.i.optimole.com/fu0…
- 例3：https://afrikagora.com/wp-content/uploa… | https://afrikagora.com/wp-content/uploa… | https://afrikagora.com/wp-content/uploa… | https://afrikagora.com/wp-content/uploa… | https://afrikagora.com/wp-content/uploa…

## g0293 — wikidbs10k：見出し「title」（Wikidata の型 `monolingualtext`）（506 列）
- 例1：ArPIKfyve homomeric and heteromeric int… | Mammalian cell morphology and endocytic… | The human phosphatidylinositol phosphat… | The TIPE (TNFAIP8) family in inflammati… | Type I phosphatidylinositol-4-phosphate…（表：citation／同じ表の列：label, description, instance of, author name string, published in, volume）
- 例2：NO-independent regulatory site on solub… | Cinaciguat, a soluble guanylate cyclase… | Invited review: cross-bridge regulation… | The distribution of heavy-chain isoform… | Mibefradil block of cloned T-type calci…（表：citation／同じ表の列：label, description, page(s), author name string, publication date, issue）
- 例3：Journal of Pharmacology and Experimenta… | Nature | Biochemical Journal | Developmental Cell | The Journal of Urology（表：publishing／同じ表の列：label, description, instance of, official website, Freebase ID, ISSN）

## g0294 — sotab_v2：元の種類 `https://dbpedia.org/ontology/Place`（500 列）
- 例1：http://www.abonlineshop.com/calendar/ev… | http://www.abonlineshop.com/calendar/ev… | http://www.abonlineshop.com/calendar/ev… | http://www.abonlineshop.com/calendar/ev… | http://www.abonlineshop.com/calendar/ev…
- 例2：Palma Cathedral Light Show Contest | Vegan First Steps | Sobrasada Festival: Campos | European Hot Air Balloon Championships … | St. Valentine's Day
- 例3：Temple, Corbès | Le village, Brignon | Stade Pibarot, chemin des sports, 3010 … | Place Eugène Daufès, Saint-Hilaire-de-B… | Atuech

## g0295 — wikidbs10k：見出し「soundex」（Wikidata の型 `string`）（497 列）
- 例1：S100 | H520 | S320 | F520 | N240（表：given name／同じ表の列：label, description, instance of, said to be the same…, different from, native label）
- 例2：F652 | J200 | M240 | J250 | J500（表：given name／同じ表の列：label, description, instance of, language of work or…, said to be the same…, different from）
- 例3：S536 | J500 | S315 | J535 | D540（表：given name／同じ表の列：label, description, instance of, Commons category, family name identic…, different from）

## g0296 — wikidbs10k：見出し「sapa id」（Wikidata の型 `string`）（478 列）
- 例1：p/5b1c3353-d71a-4332-8d68-e5a8677e49f3 | p/fb946e5a-462a-465f-b0f6-78cb64335814 | p/2a527805-1906-45c0-8c33-4bdc62a8a686 | p/e66911f2-c78d-4019-bcab-9c8550dc7549 | p/f0005076-8ed9-4872-bc9e-825c66e1a42e（表：location or destination point／同じ表の列：label, description, country, instance of, located in the admi…, Commons category）
- 例2：p/5b1c3353-d71a-4332-8d68-e5a8677e49f3 | p/bff99a18-801b-4d72-a59a-3031a5be6876 | p/98a7d24e-911e-4577-8fec-92199fcaf5a6 | p/c17c15da-3267-4e67-9294-aef9907184fc | p/150568e5-ef9a-497a-8a5f-d9ad6da07b17（表：beginning／同じ表の列：label, description, country, located in the admi…, coat of arms image, Commons category）
- 例3：p/a7cbf121-4ac8-4cbd-af7d-4d6d25cd7efb | p/2c7c5d3c-429b-4118-b4dd-27ceb6b2f525 | p/b4bc3740-2d3e-4ce2-875c-a2f6eb090a45 | p/6e9a29b2-b744-4c53-8aa8-88a6a2b46d78 | p/4d375393-126c-44d3-8078-1dd92b4c2fb5（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0297 — wikidbs10k：見出し「railway traffic side」（Wikidata の型 `wikibase-entityid`）（458 列）
- 例1：right | left（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：right | left（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：right | left（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0298 — wikidbs10k：見出し「larousse id」（Wikidata の型 `string`）（449 列）
- 例1：pays/wd/109569 | pays/wd/145805 | pays/Finlande/119533 | pays/wd/107410 | pays/États-Unis/118570（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：autre-region/wd/149106 | autre-region/wd/137533 | autre-region/wd/126636 | autre-region/wd/119733 | pays/Canada/111051（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例3：autre-region/wd/135117 | autre-region/wd/146431 | autre-region/wd/126636 | autre-region/wd/135940 | pays/Canada/111051（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0299 — wikidbs10k：見出し「the top tens id」（Wikidata の型 `string`）（446 列）
- 例1：255 | 263 | 238 | 266 | 234（表：place of birth／同じ表の列：label, description, country, located in the admi…, Freebase ID, coordinate location）
- 例2：234.0 | 41.0 | 252.0 | 240.0 | 245.0（表：facet of／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）
- 例3：250 | 240 | 258 | 263 | 41（表：replacing subject／同じ表の列：label, description, Dewey Decimal Class…, country, shares border with, capital）

## g0300 — wikidbs10k：見出し「encyclopedia of life id」（Wikidata の型 `string`）（441 列）
- 例1：973141.0 | 11700329 | 97174 | 973240 | 2486019.0（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：97585 | 975360.0 | 83389 | 2847355 | 973510.0（表：taxon／同じ表の列：label, description, parent taxon, taxon name, instance of, taxon rank）
- 例3：2912748 | 975361 | 975366 | 976074 | 974137（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）

## 答えの雛形

```
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
g0241	
g0242	
g0243	
g0244	
g0245	
g0246	
g0247	
g0248	
g0249	
g0250	
g0251	
g0252	
g0253	
g0254	
g0255	
g0256	
g0257	
g0258	
g0259	
g0260	
g0261	
g0262	
g0263	
g0264	
g0265	
g0266	
g0267	
g0268	
g0269	
g0270	
g0271	
g0272	
g0273	
g0274	
g0275	
g0276	
g0277	
g0278	
g0279	
g0280	
g0281	
g0282	
g0283	
g0284	
g0285	
g0286	
g0287	
g0288	
g0289	
g0290	
g0291	
g0292	
g0293	
g0294	
g0295	
g0296	
g0297	
g0298	
g0299	
g0300	
```
