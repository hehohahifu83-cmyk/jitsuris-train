# Grok の銀ラベル：見直してほしいまとまり（2026-10-28 Claude）

**この一覧は、シートに書いてある情報（Wikidata の型・見出し・SOTAB の元の種類）と Grok 自身の答えだけから機械的に選びました。ChatGPT の答えは使っていません。**
答えを決めるものではありません。シートで値を見て、LABEL_GUIDE.md v2.0 とシート冒頭の読み方で決め直してください（見直して元のままが正しければ、そのままでよい）。

- id にするのは、値が**ほかのものを指すコード・番号**のときだけ（Freebase ID、Ensembl gene id など）
- 値が名前なら、その名前の種類（都市・国・地域 → address、組織・会社・大学・ブランド → org、決まった選択肢 → category、製品 → product、人の名前が入る → S）
- 値が数・量なら quantity／amount／rate（割合 0.14 などは rate）、日付なら date

## A. Wikidata の型 `wikibase-entityid`（値は名前）なのに id にしたもの（137）

| まとまり | シート | 見出し・元の種類 | 型 |
| --- | --- | --- | --- |
| g0034 | 001 | strand orientation | wikibase-entityid |
| g0035 | 001 | encodes | wikibase-entityid |
| g0036 | 001 | parent taxon | wikibase-entityid |
| g0040 | 001 | located in time zone | wikibase-entityid |
| g0043 | 001 | follows | wikibase-entityid |
| g0044 | 001 | followed by | wikibase-entityid |
| g0062 | 001 | cell component | wikibase-entityid |
| g0067 | 001 | sport | wikibase-entityid |
| g0080 | 001 | described by source | wikibase-entityid |
| g0081 | 001 | category for maps | wikibase-entityid |
| g0082 | 001 | on focus list of wikimedia project | wikibase-entityid |
| g0083 | 001 | taxon rank | wikibase-entityid |
| g0088 | 001 | office held by head of government | wikibase-entityid |
| g0091 | 001 | contains the administrative territorial entity | wikibase-entityid |
| g0121 | 001 | flag | wikibase-entityid |
| g0124 | 001 | language used | wikibase-entityid |
| g0127 | 001 | official language | wikibase-entityid |
| g0128 | 001 | legislative body | wikibase-entityid |
| g0160 | 002 | anthem | wikibase-entityid |
| g0161 | 002 | highest point | wikibase-entityid |
| g0163 | 002 | demographics of topic | wikibase-entityid |
| g0164 | 002 | category for films shot at this location | wikibase-entityid |
| g0167 | 002 | history of topic | wikibase-entityid |
| g0168 | 002 | geography of topic | wikibase-entityid |
| g0171 | 002 | wikimedia outline | wikibase-entityid |
| g0172 | 002 | currency | wikibase-entityid |
| g0177 | 002 | replaces | wikibase-entityid |
| g0180 | 002 | applies to jurisdiction | wikibase-entityid |
| g0182 | 002 | lowest point | wikibase-entityid |
| g0185 | 002 | office held by head of state | wikibase-entityid |
| g0189 | 002 | diplomatic relation | wikibase-entityid |
| g0190 | 002 | executive body | wikibase-entityid |
| g0198 | 002 | top-level internet domain | wikibase-entityid |
| g0202 | 002 | driving side | wikibase-entityid |
| g0207 | 002 | expressed in | wikibase-entityid |
| g0210 | 002 | electrical plug type | wikibase-entityid |
| g0212 | 002 | basic form of government | wikibase-entityid |
| g0213 | 002 | has quality | wikibase-entityid |
| g0220 | 002 | culture | wikibase-entityid |
| g0323 | 003 | related category | wikibase-entityid |
| g0327 | 003 | practiced by | wikibase-entityid |
| g0328 | 003 | heritage designation | wikibase-entityid |
| g0330 | 003 | organizer | wikibase-entityid |
| g0332 | 003 | country of origin | wikibase-entityid |
| g0339 | 003 | public holiday | wikibase-entityid |
| g0340 | 003 | legal form | wikibase-entityid |
| g0342 | 003 | historic county | wikibase-entityid |
| g0343 | 003 | headquarters location | wikibase-entityid |
| g0349 | 003 | industry | wikibase-entityid |
| g0352 | 003 | genre | wikibase-entityid |
| g0354 | 003 | list of monuments | wikibase-entityid |
| g0355 | 003 | published in | wikibase-entityid |
| g0362 | 003 | start point | wikibase-entityid |
| g0366 | 003 | maintained by wikiproject | wikibase-entityid |
| g0367 | 003 | facet of | wikibase-entityid |
| g0368 | 003 | has list | wikibase-entityid |
| g0371 | 003 | destination point | wikibase-entityid |
| g0375 | 003 | participant in | wikibase-entityid |
| g0380 | 003 | field of this occupation | wikibase-entityid |
| g0383 | 003 | replaced by | wikibase-entityid |
| g0392 | 003 | cites work | wikibase-entityid |
| g0393 | 003 | indigenous to | wikibase-entityid |
| g0394 | 003 | part of the series | wikibase-entityid |
| g0648 | 005 | located in the statistical territorial entity | wikibase-entityid |
| g0649 | 005 | prime factor | wikibase-entityid |
| g0654 | 005 | has part(s) of the class | wikibase-entityid |
| g0655 | 005 | properties for this type | wikibase-entityid |
| g0656 | 005 | terminus | wikibase-entityid |
| g0660 | 005 | takes place in fictional universe | wikibase-entityid |
| g0666 | 005 | epoch | wikibase-entityid |
| g0667 | 005 | has grammatical mood | wikibase-entityid |
| g0672 | 005 | connecting service | wikibase-entityid |
| g0673 | 005 | connects with | wikibase-entityid |
| g0674 | 005 | historical region | wikibase-entityid |
| g0677 | 005 | edition or translation of | wikibase-entityid |
| g0678 | 005 | has subsidiary | wikibase-entityid |
| g0686 | 005 | track gauge | wikibase-entityid |
| g0690 | 005 | color | wikibase-entityid |
| g0691 | 005 | field of work | wikibase-entityid |
| g0777 | 006 | distributed by | wikibase-entityid |
| g0778 | 006 | lyrics by | wikibase-entityid |
| g0779 | 006 | mountain range | wikibase-entityid |
| g0780 | 006 | sponsor | wikibase-entityid |
| g0790 | 006 | category for alumni of educational institution | wikibase-entityid |
| g0791 | 006 | developer | wikibase-entityid |
| g0792 | 006 | fastest lap | wikibase-entityid |
| g0793 | 006 | has facet polytope | wikibase-entityid |
| g0794 | 006 | space launch vehicle | wikibase-entityid |
| g0795 | 006 | used by | wikibase-entityid |
| g0810 | 006 | has edition or translation | wikibase-entityid |
| g0811 | 006 | ima status and/or rank | wikibase-entityid |
| g0812 | 006 | next higher rank | wikibase-entityid |
| g0813 | 006 | referee | wikibase-entityid |
| g0824 | 006 | architectural style | wikibase-entityid |
| g0825 | 006 | fictional universe described in | wikibase-entityid |
| g0826 | 006 | next lower rank | wikibase-entityid |
| g0840 | 006 | mouth of the watercourse | wikibase-entityid |
| g0841 | 006 | vehicle | wikibase-entityid |
| g0929 | 007 | dedicated to | wikibase-entityid |
| g0930 | 007 | diocese | wikibase-entityid |
| g0931 | 007 | income classification (philippines) | wikibase-entityid |
| g0932 | 007 | köppen climate classification | wikibase-entityid |
| g0933 | 007 | maintained by | wikibase-entityid |
| g0934 | 007 | victory | wikibase-entityid |
| g0958 | 007 | depicted by | wikibase-entityid |
| g0959 | 007 | location of formation | wikibase-entityid |
| g0960 | 007 | operating area | wikibase-entityid |
| g0985 | 007 | aspect ratio (w:h) | wikibase-entityid |
| g0986 | 007 | candidacy in election | wikibase-entityid |
| g0987 | 007 | cathedral | wikibase-entityid |
| g0988 | 007 | christian liturgical rite | wikibase-entityid |
| g0989 | 007 | has effect | wikibase-entityid |
| g0990 | 007 | instrumentation | wikibase-entityid |
| g0991 | 007 | military branch | wikibase-entityid |
| g0992 | 007 | symptoms and signs | wikibase-entityid |
| g1084 | 008 | affiliation | wikibase-entityid |
| g1085 | 008 | class of station | wikibase-entityid |
| g1086 | 008 | discography | wikibase-entityid |
| g1087 | 008 | game mode | wikibase-entityid |
| g1088 | 008 | has vertex figure | wikibase-entityid |
| g1089 | 008 | health specialty | wikibase-entityid |
| g1090 | 008 | legislated by | wikibase-entityid |
| g1091 | 008 | notation | wikibase-entityid |
| g1092 | 008 | organized response related to outbreak | wikibase-entityid |
| g1093 | 008 | programmed in | wikibase-entityid |
| g1094 | 008 | taxonomic type | wikibase-entityid |
| g1095 | 008 | theme music | wikibase-entityid |
| g1133 | 008 | appears in the heritage monument list | wikibase-entityid |
| g1134 | 008 | brand | wikibase-entityid |
| g1135 | 008 | cover art by | wikibase-entityid |
| g1136 | 008 | cpu | wikibase-entityid |
| g1137 | 008 | fabrication method | wikibase-entityid |
| g1138 | 008 | points classification | wikibase-entityid |
| g1139 | 008 | production company | wikibase-entityid |
| g1140 | 008 | stage classification | wikibase-entityid |
| g1141 | 008 | taxon range | wikibase-entityid |
| g1142 | 008 | template has topic | wikibase-entityid |

## B. Wikidata の型が数・日付・座標（`quantity`・`time`・`globecoordinate`）なのに id にしたもの（74）

| まとまり | シート | 見出し・元の種類 | 型 |
| --- | --- | --- | --- |
| g0072 | 001 | elevation above sea level | quantity |
| g0169 | 002 | coordinates of easternmost point | globecoordinate |
| g0174 | 002 | coordinates of southernmost point | globecoordinate |
| g0175 | 002 | coordinates of westernmost point | globecoordinate |
| g0192 | 002 | human development index | quantity |
| g0205 | 002 | mains voltage | quantity |
| g0206 | 002 | total fertility rate | quantity |
| g0211 | 002 | life expectancy | quantity |
| g0224 | 002 | democracy index | quantity |
| g0347 | 003 | number of participants | quantity |
| g0350 | 003 | mass | quantity |
| g0374 | 003 | point in time | time |
| g0462 | 004 | median income | quantity |
| g0471 | 004 | mean age | quantity |
| g0472 | 004 | binding energy | quantity |
| g0473 | 004 | mass excess | quantity |
| g0483 | 004 | duration | quantity |
| g0498 | 004 | length | quantity |
| g0515 | 004 | parity quantum number | quantity |
| g0516 | 004 | spin quantum number | quantity |
| g0517 | 004 | time index | quantity |
| g0520 | 004 | employees | quantity |
| g0524 | 004 | compulsory education (maximum age) | quantity |
| g0534 | 004 | urban population | quantity |
| g0545 | 004 | illiterate population | quantity |
| g0546 | 004 | number of spoilt votes | quantity |
| g0551 | 004 | rural population | quantity |
| g0553 | 004 | number of houses | quantity |
| g0556 | 004 | literate population | quantity |
| g0564 | 004 | coordinates of geographic center | globecoordinate |
| g0577 | 004 | half-life | quantity |
| g0581 | 004 | eligible voters | quantity |
| g0582 | 004 | minimum temperature record | quantity |
| g0589 | 004 | maximum temperature record | quantity |
| g0598 | 004 | bti governance index | quantity |
| g0599 | 004 | bti status index | quantity |
| g0643 | 005 | carbon footprint | quantity |
| g0644 | 005 | number of decimal digits | quantity |
| g0650 | 005 | numeric value | quantity |
| g0651 | 005 | retirement age | quantity |
| g0679 | 005 | declination | quantity |
| g0680 | 005 | right ascension | quantity |
| g0687 | 005 | attendance | quantity |
| g0692 | 005 | number of matches played/races/starts | quantity |
| g0768 | 006 | maximum capacity | quantity |
| g0769 | 006 | students count | quantity |
| g0781 | 006 | number of speakers, writers, or signers | quantity |
| g0782 | 006 | orbital period | quantity |
| g0814 | 006 | apoapsis | quantity |
| g0815 | 006 | number of parts of this work | quantity |
| g0827 | 006 | number of deaths | quantity |
| g0828 | 006 | orbits completed | quantity |
| g0829 | 006 | radial velocity | quantity |
| g0839 | 006 | end time | time |
| g0843 | 006 | distance from earth | quantity |
| g0844 | 006 | nominal gdp per capita | quantity |
| g0845 | 006 | periapsis | quantity |
| g0846 | 006 | ppp gdp per capita | quantity |
| g0935 | 007 | number of episodes | quantity |
| g0936 | 007 | number of platform faces | quantity |
| g0962 | 007 | melting point | quantity |
| g0963 | 007 | number of constituencies | quantity |
| g0993 | 007 | number of pages | quantity |
| g1097 | 008 | admission rate | quantity |
| g1098 | 008 | albedo | quantity |
| g1099 | 008 | boiling point | quantity |
| g1100 | 008 | effective temperature | quantity |
| g1101 | 008 | number of seasons | quantity |
| g1143 | 008 | admission yield rate | quantity |
| g1144 | 008 | event interval | quantity |
| g1145 | 008 | maximum sustained winds | quantity |
| g1146 | 008 | redshift | quantity |
| g1147 | 008 | semi-major axis of an orbit | quantity |
| g1148 | 008 | term length of office | quantity |

## C. Wikidata の型 `string` で、見出しが「… id」「… code」「… number」「identifier」で終わるのに unknown にしたもの（142）

| まとまり | シート | 見出し・元の種類 | 型 |
| --- | --- | --- | --- |
| g0226 | 002 | dr topic id | string |
| g0227 | 002 | obo gazetteer id | string |
| g0229 | 002 | fast id | string |
| g0230 | 002 | gnis id | string |
| g0231 | 002 | zhihu topic id | string |
| g0233 | 002 | new york times topic id | string |
| g0237 | 002 | wolfram language entity code | string |
| g0242 | 002 | m.49 code | string |
| g0243 | 002 | grove art online id | string |
| g0246 | 002 | comic vine id | string |
| g0247 | 002 | joconde location id | string |
| g0250 | 002 | gs1 country code | string |
| g0251 | 002 | analysis & policy observatory term id | string |
| g0257 | 002 | openalex id | string |
| g0258 | 002 | urban electric transit country id | string |
| g0260 | 002 | bbc things id | string |
| g0263 | 002 | english vikidia id | string |
| g0265 | 002 | world encyclopedia of puppetry arts id | string |
| g0266 | 002 | der spiegel topic id | string |
| g0267 | 002 | refseq genome id | string |
| g0300 | 002 | encyclopedia of life id | string |
| g0397 | 003 | psh id | string |
| g0400 | 003 | eppo code | string |
| g0401 | 003 | facebook places id | string |
| g0403 | 003 | australian educational vocabulary id | string |
| g0407 | 003 | siren number | string |
| g0410 | 003 | géopatronyme id | string |
| g0413 | 003 | biblioteca nacional de españa id | string |
| g0414 | 003 | insee municipality code | string |
| g0416 | 003 | olympedia event id | string |
| g0417 | 003 | wikimedia language code | string |
| g0418 | 003 | cgndb unique id | string |
| g0419 | 003 | facebook id | string |
| g0420 | 003 | posix locale identifier | string |
| g0424 | 003 | ringgold id | string |
| g0425 | 003 | lingua libre id | string |
| g0427 | 003 | iso 639-2 code | string |
| g0434 | 003 | iso 639-1 code | string |
| g0701 | 005 | isds id | string |
| g0703 | 005 | simbad id | string |
| g0704 | 005 | wdpa id | string |
| g0707 | 005 | discogs master id | string |
| g0709 | 005 | omim id | string |
| g0710 | 005 | vision of britain unit id | string |
| g0718 | 005 | dyntaxa id | string |
| g0719 | 005 | wormbase gene id | string |
| g0725 | 005 | african plant database id | string |
| g0726 | 005 | gns unique feature id | string |
| g0727 | 005 | judoinside competition id | string |
| g0730 | 005 | sports-reference.com college basketball box score id | string |
| g0732 | 005 | brazilian electoral unit id | string |
| g0733 | 005 | brazilian municipality code | string |
| g0735 | 005 | data commons id | string |
| g0736 | 005 | mouse genome informatics id | string |
| g0742 | 005 | australian statistical geography 2011 id | string |
| g0743 | 005 | australian statistical geography 2016 id | string |
| g0744 | 005 | musicbrainz work id | string |
| g0745 | 005 | soato id | string |
| g0746 | 005 | station code | string |
| g0747 | 005 | trap danmark id | string |
| g0752 | 006 | cvr number | string |
| g0757 | 006 | norwegian municipality number | string |
| g0851 | 006 | ijf competition id | string |
| g0853 | 006 | tv.com id | string |
| g0860 | 006 | great encyclopedia of navarre id | string |
| g0861 | 006 | index fungorum id | string |
| g0862 | 006 | kinopoisk film id | string |
| g0863 | 006 | rero id | string |
| g0864 | 006 | ted talk id | string |
| g0865 | 006 | terc municipality code | string |
| g0866 | 006 | thailand central administrative unit code | string |
| g0875 | 006 | canmore id | string |
| g0876 | 006 | chemspider id | string |
| g0877 | 006 | discogs label id | string |
| g0878 | 006 | dsstox compound identifier | string |
| g0879 | 006 | dsstox substance id | string |
| g0881 | 006 | odot county code | string |
| g0893 | 006 | atvk id | string |
| g0894 | 006 | catalogue of life in taiwan id | string |
| g0895 | 006 | chebi id | string |
| g0896 | 006 | e-maapõu stratigraphy id | string |
| g0897 | 006 | eidr content id | string |
| g0898 | 006 | nioshtic-2 id | string |
| g0899 | 006 | trakt.tv id | string |
| g0908 | 007 | ec number | string |
| g1001 | 007 | hrvatska enciklopedija id | string |
| g1003 | 007 | integrated postsecondary education data system id | string |
| g1004 | 007 | kansaspedia id | string |
| g1005 | 007 | mdws place id | string |
| g1006 | 007 | mondo id | string |
| g1007 | 007 | mérimée id | string |
| g1008 | 007 | pladias id | string |
| g1009 | 007 | serial number | string |
| g1010 | 007 | songkick artist id | string |
| g1011 | 007 | stadiumdb identifier | string |
| g1012 | 007 | thegamesdb platform id | string |
| g1013 | 007 | times higher education world university id | string |
| g1014 | 007 | tmdb movie id | string |
| g1015 | 007 | youtube video id | string |
| g1029 | 007 | biolib taxon id | string |
| g1030 | 007 | cals encyclopedia of arkansas id | string |
| g1032 | 007 | cycling archives race id | string |
| g1033 | 007 | danish urban area code | string |
| g1034 | 007 | ebiodiversity id | string |
| g1035 | 007 | elstat geographical code | string |
| g1036 | 007 | isfdb title id | string |
| g1037 | 007 | montreux jazz festival concert id | string |
| g1038 | 007 | museu paulista objects id | string |
| g1039 | 007 | npca id | string |
| g1040 | 007 | observation.org id | string |
| g1041 | 007 | ofdb film id | string |
| g1042 | 007 | park alpha code | string |
| g1043 | 007 | software version identifier | string |
| g1046 | 007 | taxref id | string |
| g1047 | 007 | vascan id | string |
| g1048 | 007 | webb-site organization id | string |
| g1153 | 008 | bg ekatte place id | string |
| g1154 | 008 | china railway tmis station code | string |
| g1155 | 008 | crunchbase organization id | string |
| g1156 | 008 | douban film id | string |
| g1157 | 008 | filmaffinity id | string |
| g1158 | 008 | fleet or registration number | string |
| g1159 | 008 | floraweb id | string |
| g1160 | 008 | fossilworks taxon id | string |
| g1161 | 008 | gamecip platform id | string |
| g1163 | 008 | gepris organization id | string |
| g1164 | 008 | glyphwiki id | string |
| g1165 | 008 | guía digital del patrimonio cultural de andalucía identifier | string |
| g1167 | 008 | iaph code | string |
| g1168 | 008 | ibtracs cyclone id | string |
| g1169 | 008 | international jewish cemetery project id | string |
| g1171 | 008 | kladr id | string |
| g1172 | 008 | koatuu identifier | string |
| g1173 | 008 | lfds object id | string |
| g1175 | 008 | metacritic id | string |
| g1177 | 008 | mobygames game id | string |
| g1178 | 008 | nhs organisation data service id | string |
| g1179 | 008 | opus number | string |
| g1180 | 008 | palissy id | string |
| g1181 | 008 | protected buildings register in finland building id | string |
| g1182 | 008 | protected buildings register in finland id | string |
| g1183 | 008 | railscot location id | string |

## D. SOTAB の元の種類が番号・コードではないのに id にしたもの（12）

| まとまり | シート | 見出し・元の種類 | 型 |
| --- | --- | --- | --- |
| g0188 | 002 | Energy | sotab |
| g0193 | 002 | Language | sotab |
| g0317 | 003 | TVEpisode/name | sotab |
| g0319 | 003 | Boolean | sotab |
| g0322 | 003 | MonetaryAmount | sotab |
| g0325 | 003 | SportsTeam | sotab |
| g0357 | 003 | paymentAccepted | sotab |
| g0358 | 003 | CreativeWorkSeries | sotab |
| g0364 | 003 | DeliveryMethod | sotab |
| g0376 | 003 | https://dbpedia.org/ontology/gender | sotab |
| g0386 | 003 | RestrictedDiet | sotab |
| g0842 | 006 | DayOfWeek | sotab |
