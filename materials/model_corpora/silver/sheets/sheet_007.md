# 銀ラベルのシート 007 / 008（外の学習データの読み替え）

- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列
- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`
- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を、ChatGPT は `answers/sheet_007.tsv`、Grok は `answers_grok/sheet_007.tsv` に写して埋める。**相手の答えは見ない**

## g0901 — wikidbs10k：見出し「item operated」（Wikidata の型 `wikibase-entityid`）（13 列）
- 例1：airliner | 5-AT Trimotor（表：5-AT Trimotor fleet／同じ表の列：label, description, instance of, country, operator, part of）
- 例2：Model 41 Lark | Johnson Flying Service fleet | Airbus A300 | National Air Transport fleet | Douglas DC-2（表：operator／同じ表の列：label, description, instance of, country, Freebase ID, inception）
- 例3：5-AT Trimotor | Airbus A320 family | Douglas DC-6 | Airbus A330 | Boeing 707（表：Northwest Airlines fleet／同じ表の列：label, description, instance of, country, operator, quantity）

## g0902 — wikidbs10k：見出し「tonality」（Wikidata の型 `wikibase-entityid`）（13 列）
- 例1：E-flat major | G major | E major | C major | B-flat major（表：anthem／同じ表の列：label, description, instance of, Commons category, MusicBrainz work ID, Freebase ID）
- 例2：B major | B-flat major | A minor | G major | E-flat major（表：list of compositions by Wolfgang Amadeu…／同じ表の列：label, description, instance of, part of, composer, MusicBrainz work ID）
- 例3：A-flat major | G major | A major | F major | C major（表：anthem／同じ表の列：label, description, MusicBrainz work ID, Freebase ID, country, instance of）

## g0903 — wikidbs10k：見出し「total produced」（Wikidata の型 `quantity`）（12 列）
- 例1：+547 | +268 | +240 | +259 | +207（表：Cessna 310 320／同じ表の列：label, description, instance of, subclass of, based on）
- 例2：+200 | +225 | +547 | +245 | +148（表：based on／同じ表の列：label, description, instance of, subclass of, based on）
- 例3：1050.0 | 338.0 | 607.0 | 694.0 | 9693.0（表：operator／同じ表の列：label, description, Commons category, manufacturer, Freebase ID, image）

## g0904 — wikidbs10k：見出し「watershed area」（Wikidata の型 `quantity`）（12 列）
- 例1：+47960 | +7431 | +8370 | +14000 | +580.7（表：body of water／同じ表の列：label, description, mouth of the waterc…, instance of, Commons category, country）
- 例2：+1512 | +98000 | +229.07 | +28000 | +341（表：body of water／同じ表の列：label, description, country, located in the admi…, Commons category, coordinate location）
- 例3：+6512 | +90000 | +265.6 | +14321 | +10995（表：crossing／同じ表の列：label, description, instance of, Commons category, image, coordinate location）

## g0905 — wikidbs10k：見出し「australian statistical geography 2021 id」（Wikidata の型 `string`）（12 列）
- 例1：LGA22410 | LGA23430 | LGA27170 | LGA23670 | LGA25810（表：local government area of Victoria／同じ表の列：label, description, instance of, country, located in the admi…, coordinate location）
- 例2：SAL21206 | SAL21586 | SAL20516 | SAL22750 | SAL10317（表：capital city／同じ表の列：label, description, coordinate location, country, located in the admi…, GeoNames ID）
- 例3：LGA24780 | LGA27350 | LGA21610 | LGA26490 | LGA24970（表：administrative territorial entity／同じ表の列：label, description, country, capital, shares border with, located in the admi…）

## g0906 — wikidbs10k：見出し「big cartoon database id」（Wikidata の型 `string`）（12 列）
- 例1：87481 | 113636 | 113628 | 87476 | 87475（表：list of Drawn Together episodes／同じ表の列：label, description, instance of, part of the series, IMDb ID, part of）
- 例2：87481 | 113631 | 87468 | 87478 | 87476（表：followed by／同じ表の列：label, description, instance of, part of, title, part of the series）
- 例3：113635 | 87480 | 113625 | 87477 | 113636（表：follows／同じ表の列：label, description, instance of, part of the series, IMDb ID, part of）

## g0907 — wikidbs10k：見出し「catholic hierarchy diocese id」（Wikidata の型 `string`）（12 列）
- 例1：syma | bdea | adsm | kasm | mvml（表：Eastern Catholic eparchy／同じ表の列：label, description, instance of, country, chairperson, member count）
- 例2：gati | monq | keew | mola | anti（表：jurisdiction／同じ表の列：label, description, Commons category, official website, Freebase ID, instance of）
- 例3：gati | baie | hemo | vall | sher（表：diocese／同じ表の列：label, description, Commons category, official website, Freebase ID, instance of）

## g0908 — wikidbs10k：見出し「ec number」（Wikidata の型 `string`）（12 列）
- 例1：207-306-5 | 211-128-3 | 206-382-7 | 200-001-8 | 200-817-4（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：200-867-7 | 232-066-3 | 620-578-3 | 200-817-4 | 200-813-2（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：200-316-0 | 201-765-5 | 203-439-8 | 204-661-8 | 231-150-7（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0909 — wikidbs10k：見出し「echa substance infocard id」（Wikidata の型 `string`）（12 列）
- 例1：100.000.002 | 100.029.071 | 100.000.748 | 100.010.118 | 100.000.740（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：100.290.757 | 100.029.331 | 100.029.055 | 100.039.021 | 100.000.748（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：100.000.429 | 100.000.756 | 100.013.770 | 100.000.317 | 100.000.239（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0910 — wikidbs10k：見出し「file extension」（Wikidata の型 `string`）（12 列）
- 例1：7z（表：7z／同じ表の列：label, description, instance of, edition number, part of, described by source）
- 例2：7z（表：replaced entity／同じ表の列：label, description, instance of, part of, edition number, described by source）
- 例3：7z（表：replacing subject／同じ表の列：label, description, instance of, part of, edition number, described by source）

## g0911 — wikidbs10k：見出し「global anabaptist mennonite encyclopedia online id」（Wikidata の型 `string`）（12 列）
- 例1：Colombia | France | Peru | South America | Brazil（表：political border／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Japan | Belgium | Ukraine | Italy | Netherlands（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：Denmark | France | United States of America | Congo, Democratic Republic of | Netherlands（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0912 — wikidbs10k：見出し「indian census area code (2001)」（Wikidata の型 `string`）（12 列）
- 例1：21 | 10 | 09 | 03 | 27（表：jurisdiction／同じ表の列：label, description, population, Getty Thesaurus of …, Wikimedia outline, GeoNames ID）
- 例2：10 | 19.0 | 24.0 | 13.0 | 32.0（表：political border／同じ表の列：label, description, instance of, shares border with, head of state, Commons category）
- 例3：01 | 08 | 02 | 24 | 03（表：jurisdiction／同じ表の列：label, description, country, Commons category, topic's main catego…, Freebase ID）

## g0913 — wikidbs10k：見出し「mathworld identifier」（Wikidata の型 `string`）（12 列）
- 例1：SmallRhombicuboctahedron | TruncatedTetrahedron | SnubCubicGraph | Cuboctahedron | Icosidodecahedron（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）
- 例2：TriakisTetrahedralGraph | TruncatedOctahedralGraph | TruncatedIcosahedralGraph | TetrakisHexahedralGraph | SmallRhombicosidodecahedralGraph（表：depicting object／同じ表の列：label, description, instance of, depicts, studied by, has part(s) of the …）
- 例3：TetrakisHexahedron | TriakisTetrahedron | TruncatedTetrahedron | TruncatedCube | PentagonalHexecontahedron（表：duality／同じ表の列：label, description, Commons category, Freebase ID, has facet polytope, dual to）

## g0914 — wikidbs10k：見出し「muziekweb performer id」（Wikidata の型 `string`）（12 列）
- 例1：M00000013144 | M00000074617 | M00000201305 | M00000393611 | M00000298045（表：participant／同じ表の列：label, description, Commons category, MusicBrainz artist …, GND ID, instance of）
- 例2：M00000357341 | M00000014982 | M00000063761 | M00000186050 | M00000008787（表：participant／同じ表の列：label, description, Commons category, MusicBrainz artist …, GND ID, instance of）
- 例3：M00000175519 | M00000098175 | M00000357341 | M00000039546 | M00000023643（表：participant／同じ表の列：label, description, VIAF ID, GND ID, ISNI, Freebase ID）

## g0915 — wikidbs10k：見出し「nickel-strunz 9th edition (updated 2009)」（Wikidata の型 `string`）（12 列）
- 例1：3.CB.45 | 3.CB.30 | 3.CB.50 | 3.CB.35 | 3.CB.15（表：neso-aluminofluoride minerals (3.CB.)／同じ表の列：label, description, Strunz 8th edition …, subclass of, chemical formula, Nickel-Strunz '10th…）
- 例2：6.EA.05 | 6.BA.15 | 6.CA.20 | 6.FA.25 | 6.FA.05（表：nesoborate mineral subclass／同じ表の列：label, description, Nickel-Strunz '10th…, subclass of, IMA status and/or r…, named after）
- 例3：4.GB.35 | 4.FE.15 | 4.GB.25 | 4.FL.40 | 4.FJ.05（表：hydroxide auxiliary subclass of minerals／同じ表の列：label, description, Strunz 8th edition …, subclass of, IMA status and/or r…, Nickel-Strunz '10th…）

## g0916 — wikidbs10k：見出し「ovo id」（Wikidata の型 `string`）（12 列）
- 例1：OVO002073 | OVO002014 | OVO002075 | OVO002183 | OVO002139（表：administrative territorial entity／同じ表の列：label, description, country, located in the admi…, coat of arms image, coordinate location）
- 例2：OVO002199 | OVO002003 | OVO002054 | OVO002066 | OVO002083（表：political border／同じ表の列：label, description, Commons category, located in the admi…, flag image, coat of arms image）
- 例3：OVO002160 | OVO002031 | OVO002157 | OVO002185 | OVO002032（表：administrative centre／同じ表の列：label, description, Commons category, located in the admi…, flag image, coat of arms image）

## g0917 — wikidbs10k：見出し「philippine standard geographic code」（Wikidata の型 `string`）（12 列）
- 例1：34900000 | 030000000 | 160300000 | 153600000 | 74600000（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, flag image, ISO 3166-2 code）
- 例2：045600000 | 015500000 | 030000000 | 021500000 | 010000000（表：indigenous people／同じ表の列：label, description, GeoNames ID, Curlie ID, country, capital）
- 例3：061914000 | 083747000 | 153803000 | 045624000 | 035416000（表：capital city／同じ表の列：label, description, local dialing code, country, located in the admi…, Commons category）

## g0918 — wikidbs10k：見出し「pm20 folder id」（Wikidata の型 `string`）（12 列）
- 例1：co/003494 | co/042590 | co/008979 | co/011461 | co/059123（表：manufacturer／同じ表の列：label, description, headquarters locati…, Commons category, instance of, Freebase ID）
- 例2：co/050410 | co/011364 | co/054377 | co/018039 | co/053700（表：eponym／同じ表の列：label, description, headquarters locati…, instance of, Freebase ID, Commons category）
- 例3：co/008979 | co/042241 | co/011461 | co/042269 | co/041524（表：manufacturer／同じ表の列：label, description, headquarters locati…, instance of, Freebase ID, topic's main catego…）

## g0919 — wikidbs10k：見出し「pmcid」（Wikidata の型 `string`）（12 列）
- 例1：8330521 | 2423414 | 5727417 | 5241200 | 5656681（表：source of information／同じ表の列：label, description, PubMed ID, instance of, title, published in）
- 例2：7788060 | 3750907 | 3888616 | 4338742 | 3397467（表：consensus development conference procee…／同じ表の列：label, description, PubMed ID, DOI, instance of, title）
- 例3：6743376 | 7482799 | 1617120 | 5486926 | 7797543（表：historical article／同じ表の列：label, description, instance of, PubMed ID, title, published in）

## g0920 — wikidbs10k：見出し「production code」（Wikidata の型 `string`）（12 列）
- 例1：101 | 311 | 301 | 107 | 302（表：list of Drawn Together episodes／同じ表の列：label, description, instance of, part of the series, IMDb ID, part of）
- 例2：203 | 208 | 206 | 103 | 307（表：followed by／同じ表の列：label, description, instance of, part of, title, part of the series）
- 例3：214 | 201 | 202 | 301 | 103（表：follows／同じ表の列：label, description, instance of, part of the series, IMDb ID, part of）

## g0921 — wikidbs10k：見出し「road number」（Wikidata の型 `string`）（12 列）
- 例1：C99 | C97 | C81 | C94 | C84（表：Copenhagen Super Bikeways／同じ表の列：label, description, instance of, part of, country, official website）
- 例2：19 | 73 | 176 | 372 | 10（表：of／同じ表の列：label, description, instance of, country, located in the admi…, transport network）
- 例3：E9 | 423 | 74 | 451 | E88（表：connects with／同じ表の列：label, description, Commons category, country, instance of, located in the admi…）

## g0922 — wikidbs10k：見出し「route map」（Wikidata の型 `string`）（12 列）
- 例1：Great Western Main Line map.png | Greenford branch line.png | West Anglia Main Line.png | District Line.svg | North London line.png（表：railway line／同じ表の列：label, description, Commons category, country, instance of, located in the admi…）
- 例2：SFS Hannover-Berlin.png | DB 1730 railway map.png | DB 1770 railway map.png | DB 1761 railway map.png | DB 2970 railway map.png（表：railway line／同じ表の列：label, description, Commons category, country, instance of, Freebase ID）
- 例3：MYS Route Map MON.svg | MYS Route Map LRT KJL.svg | MYS Route Map KOM SL v2.svg | MYS Route Map ERL.svg | Rapid KL BRT Sunway Line dynamic route …（表：Rapid KL／同じ表の列：label, description, instance of, Commons category, Freebase ID, country）

## g0923 — wikidbs10k：見出し「spanish cultural heritage thesauri id」（Wikidata の型 `string`）（12 列）
- 例1：materias/1000788 | materias/1000928 | materias/1008434 | materias/1002603 | materias/1003019（表：material／同じ表の列：label, description, subclass of, Commons category, BNCF Thesaurus ID, GND ID）
- 例2：materias/1000780 | materias/1003473 | materias/1000983 | materias/1001118 | materias/1003027（表：material／同じ表の列：label, description, Commons category, subclass of, Freebase ID, image）
- 例3：materias/1000928 | materias/1181267 | materias/1006427 | materias/1000795 | materias/1008571（表：material／同じ表の列：label, description, Commons category, Freebase ID, image, subclass of）

## g0924 — wikidbs10k：見出し「thetvdb episode id」（Wikidata の型 `string`）（12 列）
- 例1：6701124 | 6701122 | 6701162 | 6701145 | 8394426（表：first appearance／同じ表の列：label, description, instance of, part of the series, title, season）
- 例2：8394427.0 | 6701148 | 6701150.0 | 8394434 | 6701146.0（表：followed by／同じ表の列：label, description, instance of, part of the series, title, season）
- 例3：8394429 | 6701137 | 6701146 | 6701166 | 6701136（表：follows／同じ表の列：label, description, instance of, part of the series, title, season）

## g0925 — wikidbs10k：見出し「wcspf id」（Wikidata の型 `string`）（12 列）
- 例1：213948 | 188193 | 200648 | 106320 | 100819（表：natural product／同じ表の列：label, description, taxon rank, taxon name, parent taxon, PlantList-ID）
- 例2：291258 | 306804 | 290958 | 291223 | 306669（表：natural product／同じ表の列：label, description, taxon rank, taxon name, parent taxon, PlantList-ID）
- 例3：200684 | 200552 | 200594 | 200927 | 200756（表：natural product／同じ表の列：label, description, taxon name, taxon rank, PlantList-ID, instance of）

## g0926 — wikidbs10k：見出し「world heritage site id」（Wikidata の型 `string`）（12 列）
- 例1：1632-003 | 1632-012 | 1632-005 | 1632-015 | 1632-013（表：Jōmon Prehistoric Sites in Northern Jap…／同じ表の列：label, description, Commons category, coordinate location, instance of, country）
- 例2：669-940 | 669-887 | 669-911 | 669-965 | 669-864（表：Way of Saint James in the province of A…／同じ表の列：label, description, coordinate location, country, instance of, located in the admi…）
- 例3：669-212 | 669-189 | 669-200 | 669-244 | 669-209（表：Way of Saint James in Navarre／同じ表の列：label, description, coordinate location, country, instance of, located in the admi…）

## g0927 — wikidbs10k：見出し「yard number」（Wikidata の型 `string`）（12 列）
- 例1：491 | 398 | 2503 | 530 | 667（表：31st U-boat Flotilla／同じ表の列：label, description, operator, instance of, conflict, vessel class）
- 例2：105 | 2579 | 1043 | 5 | 155（表：liberty ship／同じ表の列：label, description, instance of, manufacturer, Google Knowledge Gr…）
- 例3：314 | 368 | 352 | 189 | 369（表：33rd U-boat Flotilla／同じ表の列：label, description, Freebase ID, instance of, operator, vessel class）

## g0928 — wikidbs10k：見出し「youtube playlist id」（Wikidata の型 `string`）（12 列）
- 例1：OLAK5uy_nysBxNvc5Kuz0kRx8N8WdjTJPuixfVr… | OLAK5uy_ktmhevtYZH42tQtot1RG4sGTZkSdgXA… | OLAK5uy_mFyBhiWFLh4KEFX3uz6NbNQfOzZT3J-… | OLAK5uy_n0YkAQl55qa9W6RVIthaPu7wdpZvov6… | OLAK5uy_ka_04m092ScuuWRPhV7SPQE3de_z9Yy…（表：Lara Fabian discography／同じ表の列：label, description, follows, followed by, performer, MusicBrainz release…）
- 例2：OLAK5uy_nSovZlN0_LW4ROsHXCHAbh0bZMPxv-S… | OLAK5uy_kmSx_zmBZTohutzCkanijzbKhWH6F7d… | OLAK5uy_nby_mZXt4Bq0388uF_cByRCVBo1fnof… | OLAK5uy_ktmhevtYZH42tQtot1RG4sGTZkSdgXA… | OLAK5uy_mFyBhiWFLh4KEFX3uz6NbNQfOzZT3J-…（表：followed by／同じ表の列：label, description, instance of, follows, MusicBrainz release…, Discogs master ID）
- 例3：OLAK5uy_nPktm29Ta80EfnLp4aST8q0TGD4EFM0… | OLAK5uy_mq_wcLR1Gmh-C-6KumemQouIjIMmcut… | OLAK5uy_nby_mZXt4Bq0388uF_cByRCVBo1fnof… | OLAK5uy_lGMnRmKB0qAq-vKPvdIAI3pR5qaNWfF… | OLAK5uy_kmSx_zmBZTohutzCkanijzbKhWH6F7d…（表：follows／同じ表の列：label, description, follows, followed by, performer, MusicBrainz release…）

## g0929 — wikidbs10k：見出し「dedicated to」（Wikidata の型 `wikibase-entityid`）（12 列）
- 例1：Taima Mandala | Shaka Nyorai | Bhaiṣajyaguru Buddha | Guan Yin | Seven Lucky Gods（表：part／同じ表の列：label, description, official website, Commons category, coordinate location, Freebase ID）
- 例2：Five Wisdom King | Cintāmaṇicakra | Amitābha Buddha | Shaka Nyorai | Vaiśravaṇa（表：headquarters／同じ表の列：label, description, Commons category, coordinate location, Freebase ID, instance of）
- 例3：Cawrdaf | Saint Nicholas | Saint Edeyrn | Elaeth | Twrog（表：parish church／同じ表の列：label, description, Commons category, coordinate location, country, instance of）

## g0930 — wikidbs10k：見出し「diocese」（Wikidata の型 `wikibase-entityid`）（12 列）
- 例1：Diocese of Bangor（表：Diocese of Bangor／同じ表の列：label, description, instance of, country, coordinate location, historic county）
- 例2：Diocese of Bangor（表：religious administrative territorial en…／同じ表の列：label, description, instance of, country, coordinate location, historic county）
- 例3：Diocese of Saint-Jean-Longueuil | Diocese of Joliette | Diocese of Antigonish | Roman Catholic Archdiocese of Sherbrooke | Diocese of Valleyfield（表：cathedral／同じ表の列：label, description, instance of, religion or worldvi…, country, located in the admi…）

## g0931 — wikidbs10k：見出し「income classification (philippines)」（Wikidata の型 `wikibase-entityid`）（12 列）
- 例1：5th city income class | 6th city income class | 3rd city income class | 1st city income class | 1st municipal income class（表：component city／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例2：4th city income class | 5th municipal income class | 4th municipal income class | 3rd municipal income class | 1st city income class（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, flag image, ISO 3166-2 code）
- 例3：3rd municipal income class | 3rd city income class | 2nd city income class | 2nd municipal income class | 4th city income class（表：political border／同じ表の列：label, description, country, located in the admi…, locator map image, coordinate location）

## g0932 — wikidbs10k：見出し「köppen climate classification」（Wikidata の型 `wikibase-entityid`）（12 列）
- 例1：tropical monsoon climate | tropical rainforest climate | tropical climate（表：component city／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例2：tropical monsoon climate | tropical climate | tropical rainforest climate（表：administrative territorial entity／同じ表の列：label, description, Commons category, country, flag image, ISO 3166-2 code）
- 例3：tropical monsoon climate | tropical climate | tropical rainforest climate | tropical savanna climate（表：political border／同じ表の列：label, description, country, located in the admi…, locator map image, coordinate location）

## g0933 — wikidbs10k：見出し「maintained by」（Wikidata の型 `wikibase-entityid`）（12 列）
- 例1：Trenord（表：treno RegioExpress／同じ表の列：label, description, instance of, country, located in the admi…, part of）
- 例2：Ferrovienord | Rete Ferroviaria Italiana（表：terminus／同じ表の列：label, description, country, instance of, coordinate location, image）
- 例3：Queen's University Libraries | University of Manitoba Archives & Speci… | Trent University Archives | Health Sciences Centre (Winnipeg) Archi… | Library and Archives Canada（表：Canadian Archive of Women in STEM／同じ表の列：label, description, instance of, main subject, described at URL, level of description）

## g0934 — wikidbs10k：見出し「victory」（Wikidata の型 `wikibase-entityid`）（12 列）
- 例1：Eurovision Song Contest 2003 | Eurovision Song Contest 2002 | Eurovision Song Contest 1987 | Festival da Canção | Eurovision Song Contest 1994（表：winner／同じ表の列：label, description, instance of, participant in）
- 例2：1960–61 Cypriot First Division | 1944–45 Cypriot First Division | 1940–41 Cypriot First Division | 2003-04 Cypriot Cup | 1950–51 Cypriot First Division（表：participating team／同じ表の列：label, description, instance of, home venue, league, head coach）
- 例3：1950–51 Cypriot First Division | 1966–67 Cypriot First Division | 1935–36 Cypriot First Division | 1982–83 Cypriot Second Division | 1989–90 Cypriot Cup（表：winner／同じ表の列：label, description, instance of, home venue, league, head coach）

## g0935 — wikidbs10k：見出し「number of episodes」（Wikidata の型 `quantity`）（11 列）
- 例1：8.0 | 41.0 | 138.0 | 17.0 | 27.0（表：television series season／同じ表の列：label, description, instance of, part of the series, has part(s), original language o…）
- 例2：38.0 | 100.0 | 193.0 | 327.0 | 12.0（表：series／同じ表の列：label, description, instance of, IMDb ID, genre, original language o…）
- 例3：+8903 | +13.872 | +10755 | +13858 | +296（表：work／同じ表の列：label, description, original broadcaster, IMDb ID, country of origin, topic's main catego…）

## g0936 — wikidbs10k：見出し「number of platform faces」（Wikidata の型 `quantity`）（11 列）
- 例1：+2 | +1 | +4（表：Cercanías Murcia Alicante／同じ表の列：label, description, part of, Commons category, coordinate location, country）
- 例2：+1 | +3 | +2 | +4（表：Istanbul Tram／同じ表の列：label, description, inception, instance of, country, located in the admi…）
- 例3：+3 | +2 | +4（表：adjacent station／同じ表の列：label, description, instance of, located in the admi…, country, connecting line）

## g0937 — wikidbs10k：見出し「bag public space id」（Wikidata の型 `string`）（11 列）
- 例1：0737300000000382 | 1699300000000331 | 1731300000000515 | 0737300000000168 | 0683300000287228（表：street／同じ表の列：label, description, postal code, instance of, coordinate location, located in the admi…）
- 例2：0361300000001360 | 0398300000000556 | 0458300000001128 | 0383300000000072 | 0373300000000010（表：street／同じ表の列：label, description, instance of, coordinate location, located in the admi…, location）
- 例3：0200300022474490 | 0200300002247234 | 0200300022471098 | 0200300022513253 | 0200300022481998（表：street／同じ表の列：label, description, postal code, instance of, coordinate location, located in the admi…）

## g0938 — wikidbs10k：見出し「cinemagia title id」（Wikidata の型 `string`）（11 列）
- 例1：496763.0 | 700739 | 496837.0 | 700737.0 | 496811.0（表：followed by／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例2：496872.0 | 496835.0 | 496809.0 | 493402.0 | 496761（表：follows／同じ表の列：label, description, instance of, part of the series, follows, followed by）
- 例3：502652 | 502655 | 502656 | 502659 | 502653（表：The Final Chapter／同じ表の列：label, description, IMDb ID, part of the series, director, screenwriter）

## g0939 — wikidbs10k：見出し「crossref funder id」（Wikidata の型 `string`）（11 列）
- 例1：100007160 | 100007185 | 100007270 | 100009496 | 100006537（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例2：100007618 | 100006919 | 100005492 | 501100000765 | 100007015（表：alma mater／同じ表の列：label, description, instance of, country, Commons category, coordinate location）
- 例3：501100000666 | 100010361 | 100010359 | 100010367 | 501100000747（表：Wikimedia category／同じ表の列：label, description, Commons category, instance of, country, topic's main catego…）

## g0940 — wikidbs10k：見出し「czech ndop taxon id」（Wikidata の型 `string`）（11 列）
- 例1：94365.0 | 18410.0 | 78877.0 | 18696.0 | 17474.0（表：secretion or excretion／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：986.0 | 34395.0 | 34358.0 | 34359.0 | 34364.0（表：symbol／同じ表の列：label, description, taxon rank, IUCN conservation s…, Commons category, taxon name）
- 例3：35879 | 40646 | 37061 | 38386 | 37995（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）

## g0941 — wikidbs10k：見出し「disease ontology id」（Wikidata の型 `string`）（11 列）
- 例1：DOID:0110644 | DOID:0050434 | DOID:0110655 | DOID:2842 | DOID:0110651（表：long QT syndrome／同じ表の列：label, description, subclass of, OMIM ID, instance of, health specialty）
- 例2：DOID:0080294 | DOID:0110206 | DOID:0110202 | DOID:0110199 | DOID:0110203（表：Charcot-Marie-Tooth disease intermediat…／同じ表の列：label, description, instance of, subclass of, Orphanet ID, ICD-10-CM）
- 例3：DOID:9784 | DOID:12549 | DOID:3292 | DOID:7427 | DOID:4411（表：notifiable disease／同じ表の列：label, description, Commons category, DiseasesDB, eMedicine ID, Freebase ID）

## g0942 — wikidbs10k：見出し「gcatholic diocese id」（Wikidata の型 `string`）（11 列）
- 例1：batr0 | alep4 | latt1 | koth0 | rama0（表：Eastern Catholic eparchy／同じ表の列：label, description, instance of, Catholic Hierarchy …, country, chairperson）
- 例2：vall3 | queb0 | hear0 | rouy0 | gati0（表：jurisdiction／同じ表の列：label, description, Commons category, official website, Freebase ID, instance of）
- 例3：keew0 | otta0 | anti3 | zjea0 | hear0（表：diocese／同じ表の列：label, description, Commons category, official website, Freebase ID, instance of）

## g0943 — wikidbs10k：見出し「hsdb id」（Wikidata の型 `string`）（11 列）
- 例1：548 | 517 | 5206 | 2508 | 807（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：1030 | 533 | 169 | 903 | 164（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：811 | 540 | 56 | 1117 | 43（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0944 — wikidbs10k：見出し「indian financial system code」（Wikidata の型 `string`）（11 列）
- 例1：DLXB0000009 | DLXB0000217 | DLXB0000220 | DLXB0000223 | DLXB0000222（表：Dhanlaxmi Bank branch／同じ表の列：label, description, operator, country, located in the admi…, instance of）
- 例2：TJSB0000025 | TJSB0000122 | TJSB0000001 | TJSB0000051 | TJSB0000045（表：TJSB Sahakari Bank branch／同じ表の列：label, description, operator, country, located in the admi…, instance of）
- 例3：NTBL0HAR097 | NTBL0DEL076 | NTBL0LUC041 | NTBL0GUR051 | NTBL0DEH113（表：Nainital Bank Branch／同じ表の列：label, description, operator, country, located in the admi…, instance of）

## g0945 — wikidbs10k：見出し「insee department code」（Wikidata の型 `string`）（11 列）
- 例1：974.0 | 13.0 | 75.0 | 973.0 | 14.0（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, topic's main Wikime…, Commons category, country）
- 例2：971 | 14 | 973 | 976 | 28（表：physical location／同じ表の列：label, description, Dewey Decimal Class…, topic's main Wikime…, Commons category, country）
- 例3：46 | 24 | 88 | 09 | 08（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, named after, Commons category, country）

## g0946 — wikidbs10k：見出し「internet game database platform id」（Wikidata の型 `string`）（11 列）
- 例1：gba | ps2 | psp | amiga | ps5（表：computing platform／同じ表の列：label, description, developer, Commons category, logo image, topic's main catego…）
- 例2：snes--1 | wii | nds | gba | 3ds（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例3：gbc | gba | wiiu | snes--1 | ngc（表：follows／同じ表の列：label, description, manufacturer, Commons category, follows, followed by）

## g0947 — wikidbs10k：見出し「legal citation of this text」（Wikidata の型 `string`）（11 列）
- 例1：Act No. 21 of 1980 | Act No. 5 of 1980 | Act No. 67 of 1980 | Act No. 16 of 1980 | Act No. 49 of 1980（表：list of Acts of the Parliament of India…／同じ表の列：label, description, instance of, country, applies to jurisdic…, legislated by）
- 例2：President's Act No. 1 of 1977 | President's Act No. 10 of 1976 | President's Act No. 9 of 1976 | President's Act No. 15 of 1976 | President's Act No. 2 of 1991（表：Act of the President of India／同じ表の列：label, description, instance of, applies to jurisdic…, publication date, effective date）
- 例3：Act No. 41 of 1976 | Act No. 8 of 1993 | Act No. 36 of 1984 | Act No. 31 of 1975 | Act No. 21 of 1992（表：based on／同じ表の列：label, description, instance of, applies to jurisdic…, enacted date, legislated by）

## g0948 — wikidbs10k：見出し「libraries australia id」（Wikidata の型 `string`）（11 列）
- 例1：35242950 | 35219734 | 35460408 | 35562417 | 36102391（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, coordinates of sout…, New York Times topi…）
- 例2：35653496 | 35098056 | 35242950 | 35237752 | 35219734（表：country／同じ表の列：label, description, Great Russian Encyc…, participant in, coordinates of sout…, New York Times topi…）
- 例3：35632716 | 35562335 | 35620224 | 36589794 | 35561043（表：award／同じ表の列：label, description, Commons category, instance of, inception, topic's main catego…）

## g0949 — wikidbs10k：見出し「mobygames platform id」（Wikidata の型 `string`）（11 列）
- 例1：amiga | windows | wii-u | ps3 | nintendo-ds（表：computing platform／同じ表の列：label, description, developer, Commons category, logo image, topic's main catego…）
- 例2：switch | nes | wii | arcade | snes（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例3：n64 | wii-u | gamecube | gameboy-color | nes（表：follows／同じ表の列：label, description, manufacturer, Commons category, follows, followed by）

## g0950 — wikidbs10k：見出し「national library of latvia id」（Wikidata の型 `string`）（11 列）
- 例1：000095495 | 000201070 | 000179395 | 000199750 | 000126170（表：aspect of history／同じ表の列：label, description, Commons category, topic's main catego…, Freebase ID, instance of）
- 例2：52291.0 | 55435.0 | 53087.0 | 51862.0 | 48014.0（表：field of work／同じ表の列：label, description, Dewey Decimal Class…, BNCF Thesaurus ID, topic's main catego…, NDL Authority ID）
- 例3：000139618 | 000162866 | 000042006 | 000142149 | 000135101（表：administrative territorial entity／同じ表の列：label, description, country, ISO 3166-2 code, coordinate location, topic's main catego…）

## g0951 — wikidbs10k：見出し「researchgate publication id」（Wikidata の型 `string`）（11 列）
- 例1：11610396 | 24026929 | 14260333 | 224865281 | 13415464（表：citation／同じ表の列：label, description, page(s), title, author name string, publication date）
- 例2：279067486 | 234067569 | 15582647 | 10924543 | 13807052（表：citation／同じ表の列：label, description, PubMed ID, instance of, title, published in）
- 例3：23296638 | 11031507 | 259155758 | 24282624 | 234698533（表：citation／同じ表の列：label, description, PubMed ID, instance of, title, published in）

## g0952 — wikidbs10k：見出し「spdx license id」（Wikidata の型 `string`）（11 列）
- 例1：ISC | OpenSSL | LGPL-2.1-or-later | AGPL-3.0-only | LGPL-2.1-only（表：license／同じ表の列：label, description, approved by, short name, instance of）
- 例2：GPL-3.0-only | BSD-3-Clause | BSD-4-Clause | GPL-2.0-or-later | MIT（表：license／同じ表の列：label, description, publication date, approved by, short name, instance of）
- 例3：BSD-2-Clause | LGPL-2.1-only | MIT | GPL-3.0-only | BSD-2-Clause-FreeBSD（表：license／同じ表の列：label, description, approved by, short name, full work available…, instance of）

## g0953 — wikidbs10k：見出し「strunz 8th edition (series id, updated)」（Wikidata の型 `string`）（11 列）
- 例1：III/C.03 | III/B.03 | III/C.02（表：neso-aluminofluoride minerals (3.CB.)／同じ表の列：label, description, subclass of, chemical formula, Nickel-Strunz 9th e…, Nickel-Strunz '10th…）
- 例2：V/H.04 | V/H.02 | V/H.18 | V/H.01 | V/H.17（表：nesoborate mineral subclass／同じ表の列：label, description, Nickel-Strunz '10th…, subclass of, IMA status and/or r…, named after）
- 例3：IV/F.07 | IV/H.02 | IV/H.01 | IV/F.04 | IV/H.03（表：hydroxide auxiliary subclass of minerals／同じ表の列：label, description, Nickel-Strunz 9th e…, subclass of, IMA status and/or r…, Nickel-Strunz '10th…）

## g0954 — wikidbs10k：見出し「traffic sign」（Wikidata の型 `string`）（11 列）
- 例1：BE-N25.svg | NLD-N310.svg | NLD-N300.svg | BE-R0.svg | Texas PA 1502.svg（表：crossing／同じ表の列：label, description, instance of, located in the admi…, country, OpenStreetMap relat…）
- 例2：BE-R0.svg | BE-R9.svg | China Expwy G9910 sign with name.svg | China Expwy G4202 sign with name.svg | BE-R1.svg（表：motorway ring road／同じ表の列：label, description, located in the admi…, instance of, country, road number）
- 例3：NLD-N11.svg | NL-A50.svg | NLD-N289.svg | NL-N36.png | NL-A4.svg（表：rijksweg／同じ表の列：label, description, country, route map, located in the admi…, terminus）

## g0955 — wikidbs10k：見出し「uvl platform id」（Wikidata の型 `string`）（11 列）
- 例1：106 | 189 | 203 | 129 | 147（表：computing platform／同じ表の列：label, description, developer, Commons category, logo image, topic's main catego…）
- 例2：147 | 5 | 204 | 104 | 187（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例3：38 | 196 | 6 | 104 | 90（表：follows／同じ表の列：label, description, manufacturer, Commons category, follows, followed by）

## g0956 — wikidbs10k：見出し「verspreidingsatlas.nl id」（Wikidata の型 `string`）（11 列）
- 例1：0216000 | 614000.0 | 0076000 | 607000.0 | 0647000（表：taxon／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：0746 | 0319 | 0560 | 1037 | 0279（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例3：6310 | 6140 | 6557 | 6322 | 6238（表：taxon／同じ表の列：label, description, parent taxon, taxon name, taxon rank, image）

## g0957 — wikidbs10k：見出し「zvg number」（Wikidata の型 `string`）（11 列）
- 例1：1110 | 1640 | 41070 | 500075 | 41220（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：1110 | 16100 | 13290 | 4900 | 1640（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：34020 | 34050 | 510308 | 19480 | 20130（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0958 — wikidbs10k：見出し「depicted by」（Wikidata の型 `wikibase-entityid`）（11 列）
- 例1：cuboctahedral graph | truncated Icosahedral graph | truncated dodecahedral graph | icosidodecahedral graph | truncated tetrahedral graph（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）
- 例2：small triakis octahedral graph | truncated cubical graph | snub cubical graph | icosidodecahedral graph | disdyakis triacontahedral graph（表：duality／同じ表の列：label, description, Commons category, Freebase ID, has facet polytope, dual to）
- 例3：icosidodecahedral graph | truncated tetrahedral graph | truncated cubical graph | great rhombicuboctahedral graph | snub cubical graph（表：depiction／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）

## g0959 — wikidbs10k：見出し「location of formation」（Wikidata の型 `wikibase-entityid`）（11 列）
- 例1：Bologna | Dresden | Krasnogorsk | Suwa | Saint Petersburg（表：manufacturer／同じ表の列：label, description, Commons category, country, headquarters locati…, instance of）
- 例2：Wellington | Taipei | Barranquilla | Helsinki | Abu Dhabi（表：operator／同じ表の列：label, description, instance of, airline hub, item operated, country）
- 例3：Victoria | Quebec City | Calgary | Trois-Rivières | Toronto（表：Royal Canadian Armoured Corps／同じ表の列：label, description, country, instance of, conflict, official website）

## g0960 — wikidbs10k：見出し「operating area」（Wikidata の型 `wikibase-entityid`）（11 列）
- 例1：Bahia（表：organization／同じ表の列：label, description, instance of, country, applies to jurisdic…, field of work）
- 例2：Algeria | Namibia | Wallis and Futuna | Trinidad and Tobago | Saint Vincent and the Grenadines（表：rugby union governing body／同じ表の列：label, description, sport, official website, inception, instance of）
- 例3：Central America | Earth | Northern America and Mexico | worldwide | Metropolitan France（表：member／同じ表の列：label, description, Freebase ID, inception, official website, instance of）

## g0961 — wikidbs10k：見出し「subtitle」（Wikidata の型 `monolingualtext`）（10 列）
- 例1：একটি উন্মুক্ত পাঠাগার | Fontes liberi | Perpustakaan bebas | Slobodna biblioteka | Det frie biblioteket（表：Wikisource language edition／同じ表の列：label, description, official website, instance of, Wikimedia database …, language of work or…）
- 例2：Til Corporal Mollberg. | Til Systrarna på then Konungsliga Djurg… | Til Cajsa Stina | Som är ett soliloquium, då Fredman låg … | Öfver Bredströmskans och Movitz melanch…（表：Fredman's Epistles／同じ表の列：label, description, instance of, country of origin, language of work or…, follows）
- 例3：Om des sista Ögnekast på Ulla Winblad v… | Angående Bröllopet hos Bensvarfvars. | som är et Fägne-spel på Fader Didriks n… | Til Movitz, när elden var lös i hans Qv… | Öfver Bredströmskans och Movitz melanch…（表：followed by／同じ表の列：label, description, follows, instance of, country of origin, language of work or…）

## g0962 — wikidbs10k：見出し「melting point」（Wikidata の型 `quantity`）（10 列）
- 例1：-229 | -267 | -87 | -137 | -144（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：-219 | -153 | -213 | -179 | -218（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：-137 | -62 | -96 | +203 | +182（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0963 — wikidbs10k：見出し「number of constituencies」（Wikidata の型 `quantity`）（10 列）
- 例1：11 | 15 | 36 | 23 | 24（表：legislature／同じ表の列：label, description, topic's main catego…, instance of, country, applies to jurisdic…）
- 例2：+28 | +19 | +36 | +13 | +25（表：district council of Hong Kong／同じ表の列：label, description, Commons category, topic's main catego…, instance of, country）
- 例3：+34 | +39 | +13 | +19 | +36（表：legislature／同じ表の列：label, description, topic's main catego…, Commons category, instance of, country）

## g0964 — wikidbs10k：見出し「3d model」（Wikidata の型 `string`）（10 列）
- 例1：Icosidodecahedron wireframe.stl | Truncated cuboctahedron wireframe.stl | Snub dodecahedron wireframe.stl | Snub cube.stl | Truncated cube.stl（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）
- 例2：Rhombicosidodecahedron.stl | Snub cube.stl | Truncated tetrahedron.stl | Triakis tetrahedron.stl | Truncated icosidodecahedron.stl（表：duality／同じ表の列：label, description, Commons category, Freebase ID, has facet polytope, dual to）
- 例3：Icosidodecahedron wireframe.stl | Truncated cuboctahedron wireframe.stl | Truncated cube.stl | Snub dodecahedron wireframe.stl | Truncated icosidodecahedron.stl（表：depiction／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）

## g0965 — wikidbs10k：見出し「aiatsis place thesaurus id」（Wikidata の型 `string`）（10 列）
- 例1：6 | 5 | 3715 | 7 | 9（表：topic／同じ表の列：label, description, Commons category, flag image, coat of arms image, VIAF ID）
- 例2：8 | 3 | 7 | 5 | 4（表：administrative territorial entity／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）
- 例3：4 | 11 | 7 | 5 | 1（表：jurisdiction／同じ表の列：label, description, locator map image, topic's main Wikime…, country, capital）

## g0966 — wikidbs10k：見出し「audio」（Wikidata の型 `string`）（10 列）
- 例1：Anthem of Ecuador.ogg | United States Navy Band - ¡Oh, gloria i… | Norway (National Anthem).ogg | Marcha Real-Royal March by US Navy Band… | Wilhelmus koor.oga（表：anthem／同じ表の列：label, description, instance of, Commons category, MusicBrainz work ID, Freebase ID）
- 例2：Gǒng Jīn'ōu.ogg | A Portuguesa.ogg | Hino da Carta.ogg | National anthem of South Korea, perform… | Monaco National Anthem.ogg（表：anthem／同じ表の列：label, description, MusicBrainz work ID, Freebase ID, country, instance of）
- 例3：United States Navy Band - Gloria al Bra… | Star Spangled Banner instrumental.ogg | National Anthem of Dominica by US Navy … | Antigua and Barbuda National Anthem.ogg | United States Navy Band - O Land of Bea…（表：anthem／同じ表の列：label, description, Freebase ID, image, instance of, tonality）

## g0967 — wikidbs10k：見出し「bavarian monument authority id」（Wikidata の型 `string`）（10 列）
- 例1：D-1-82-116-53 | D-1-76-164-99 | D-5-73-134-85 | D-1-81-130-417 | D-1-84-141-41（表：köblergut／同じ表の列：label, description, located in the admi…, country, heritage designation, instance of）
- 例2：D-1-7637-0417 | D-7-8227-0156 | D-4-5832-0152 | D-6-5628-0105 | D-6-5929-0072（表：Stadtpfarrkirche／同じ表の列：label, description, coordinate location, country, instance of, located in the admi…）
- 例3：D-1-8143-0104 | D-1-7234-0139 | D-5-6432-0179 | D-1-7535-0183 | D-5-6532-0034（表：Wasserburgstall／同じ表の列：label, description, country, coordinate location, instance of, located in the admi…）

## g0968 — wikidbs10k：見出し「bowers acronym」（Wikidata の型 `string`）（10 列）
- 例1：tic | snic | tid | tut | girco（表：archimedean solid／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）
- 例2：ti | rhote | pedid | siddykat | srid（表：duality／同じ表の列：label, description, Commons category, Freebase ID, has facet polytope, dual to）
- 例3：ti | girco | snid | tut | grid（表：depiction／同じ表の列：label, description, Commons category, Freebase ID, subclass of, image）

## g0969 — wikidbs10k：見出し「cinii books author id」（Wikidata の型 `string`）（10 列）
- 例1：DA00906755 | DA02962247 | DA01369312 | DA00701402 | DA00516998（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：DA01369312 | DA00990252 | DA00516998 | DA00906755 | DA02943005（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：DA00906755 | DA0114862X | DA01369312 | DA00516998 | DA00701402（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）

## g0970 — wikidbs10k：見出し「encyclopedia of alabama id」（Wikidata の型 `string`）（10 列）
- 例1：h-1195 | h-1196 | h-1168 | h-1199 | h-1287（表：physical location／同じ表の列：label, description, Commons category, country, located in the admi…, named after）
- 例2：h-1323 | h-1318 | h-1202 | h-1298 | h-1370（表：political border／同じ表の列：label, description, Commons category, located in the admi…, country, coordinate location）
- 例3：h-1196 | h-1195 | h-1331 | h-1336 | h-1206（表：administrative territorial entity／同じ表の列：label, description, Commons category, located in the admi…, country, coordinate location）

## g0971 — wikidbs10k：見出し「europeana fashion vocabulary id」（Wikidata の型 `string`）（10 列）
- 例1：10504 | 10545 | 10556 | 10577 | 10547（表：material／同じ表の列：label, description, subclass of, Commons category, BNCF Thesaurus ID, GND ID）
- 例2：10293 | 10076 | 10510 | 10042 | 10028（表：depiction／同じ表の列：label, description, Commons category, subclass of, image, Art & Architecture …）
- 例3：10597 | 10381 | 10428 | 10352 | 10373（表：material／同じ表の列：label, description, Freebase ID, Commons category, Art & Architecture …, image）

## g0972 — wikidbs10k：見出し「icsc id」（Wikidata の型 `string`）（10 列）
- 例1：0155 | 0082 | 0284 | 0560 | 0564（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：0687 | 0284 | 0109 | 1390 | 0127（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：0341 | 1578 | 1432 | 0015 | 0076（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0973 — wikidbs10k：見出し「launchbox games database platform id」（Wikidata の型 `string`）（10 列）
- 例1：218 | 50 | 16 | 33 | 34（表：computing platform／同じ表の列：label, description, developer, Commons category, logo image, topic's main catego…）
- 例2：31 | 33 | 27 | 25 | 29（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例3：34 | 25 | 27 | 29 | 53（表：follows／同じ表の列：label, description, manufacturer, Commons category, follows, followed by）

## g0974 — wikidbs10k：見出し「library of congress demographic group terms id」（Wikidata の型 `string`）（10 列）
- 例1：dg2015060082 | dg2016060192 | dg2016060033 | dg2016060201 | dg2016060359（表：intentional human activity／同じ表の列：label, description, Commons category, field of this occup…, topic's main catego…, GND ID）
- 例2：dg2016060190 | dg2015060212 | dg2017060146 | dg2015060131 | dg2016060063（表：occupation／同じ表の列：label, description, instance of, Commons category, GND ID, field of this occup…）
- 例3：dg2016060021 | dg2016060063 | dg2016060190 | dg2016060387 | dg2016060321（表：intentional human activity／同じ表の列：label, description, instance of, subclass of, field of this occup…, female form of label）

## g0975 — wikidbs10k：見出し「musicbrainz artist id」（Wikidata の型 `string`）（10 列）
- 例1：2a63a6e5-d494-4dce-aeb8-75b7af13220a | 5dca4d22-d6c8-4e70-8ca1-4543e43353c7 | f6d3e508-fcc9-4712-8a63-83d26098777c | 9f381a6f-44ac-4016-be50-75ec8e6a592f | 4b585938-f271-45e2-b19a-91c634b5e396（表：performing artist／同じ表の列：label, description, discography, Commons category, image, Freebase ID）
- 例2：463f056c-56bf-429d-b3a3-f8fe467c427d | c8dbbadb-f5f1-449c-8827-43d00a73fe89 | f22942a1-6f70-4f48-866e-238cb2308fbd | 56abaa47-0101-463b-b37e-e961136fec39 | dd77b8da-cdc7-46b8-8a7f-10894ca0490e（表：performing artist／同じ表の列：label, description, instance of, Discogs artist ID, work period (start), genre）
- 例3：f4857fb9-e255-4dc6-bd01-e4ca7cc68544 | 9b7d4216-b59d-443f-8c35-95f28b371056 | 708cad63-631f-4a77-92fe-c046bb02d0c3 | 00ef990b-098d-4bf6-897b-708e35638854 | 5b032b22-6131-44c8-bccc-aae7006eec3a（表：performing artist／同じ表の列：label, description, instance of, genre, Freebase ID, Discogs artist ID）

## g0976 — wikidbs10k：見出し「niosh pocket guide id」（Wikidata の型 `string`）（10 列）
- 例1：0336 | 0300 | 0400 | 0556 | 0657（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：0660 | 0662 | 0116 | 0105 | 0657（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：0622 | 0628 | 0293 | 0599 | 0014（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, RTECS number, has effect）

## g0977 — wikidbs10k：見出し「nrhp reference number」（Wikidata の型 `string`）（10 列）
- 例1：86003260 | 98000949 | 100006934 | 87001387 | 07001265（表：downtown／同じ表の列：label, description, instance of, country, located in the admi…, image）
- 例2：100002519 | 100001720 | 06000069 | 05000630 | 07000943（表：Rosenwald School／同じ表の列：label, description, coordinate location, country, located in the admi…, heritage designation）
- 例3：03001116 | 66000131 | 98000887 | 84003855 | 03001199（表：hall and parlor house／同じ表の列：label, description, coordinate location, country, located in the admi…, instance of）

## g0978 — wikidbs10k：見出し「recreation.gov gateway id」（Wikidata の型 `string`）（10 列）
- 例1：13950 | 2809 | 2952 | 2944 | 2726（表：national preserve／同じ表の列：label, description, Commons category, located in the admi…, IUCN protected area…, instance of）
- 例2：14760 | 15149 | 15107 | 15105 | 14750（表：Utah state park／同じ表の列：label, description, Commons category, instance of, coordinate location, country）
- 例3：13661 | 13612 | 2746 | 13643 | 13613（表：National Scenic Byway／同じ表の列：label, description, instance of, country, America's Byways ro…, located in the admi…）

## g0979 — wikidbs10k：見出し「relief location map」（Wikidata の型 `string`）（10 列）
- 例1：Ibaraki-ken géolocalisation relief.svg | Kochi géolocalisation relief.svg | Saitama-ken géolocalisation relief.svg | Ishikawa géolocalisation relief.svg | Fukui géolocalisation relief.svg（表：located in the present-day administrati…／同じ表の列：label, description, population, country, capital, shares border with）
- 例2：Fukuoka géolocalisation relief.svg | Kagoshima géolocalisation relief.svg | Chiba-ken géolocalisation relief.svg | Osaka géolocalisation relief.svg | Ehime géolocalisation relief.svg（表：political border／同じ表の列：label, description, population, coordinate location, instance of, shares border with）
- 例3：South Korea Topography.png | Deutschland topo.jpg | Uk topo en.jpg | Japan relief location map with side map… | India relief location map.jpg（表：country of origin／同じ表の列：label, description, Great Russian Encyc…, participant in, Libraries Australia…, coordinates of sout…）

## g0980 — wikidbs10k：見出し「rtecs number」（Wikidata の型 `string`）（10 列）
- 例1：LY4900000 | KH7525000 | FO3000000 | OA7700000 | CG6475000（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：CG6475000 | KW0560000 | FO3000000 | KU9625000 | KH7525000（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：PC8575000 | FG4900000 | BZ5410000 | BW6650000 | TX6475000（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, has effect）

## g0981 — wikidbs10k：見出し「siruta code」（Wikidata の型 `string`）（10 列）
- 例1：69919 | 70325 | 130543 | 40205 | 83641（表：municipality seat of Romania／同じ表の列：label, description, country, coordinate location, population, instance of）
- 例2：161794 | 270 | 127 | 163 | 70352（表：administrative territorial entity／同じ表の列：label, description, pronunciation audio, located in time zone, Commons category, coat of arms image）
- 例3：63394 | 86687 | 87638 | 95060 | 13169（表：administrative centre／同じ表の列：label, description, pronunciation audio, located in time zone, Commons category, coat of arms image）

## g0982 — wikidbs10k：見出し「the met object id」（Wikidata の型 `string`）（10 列）
- 例1：237719 | 447995 | 240846 | 453335 | 236593（表：pilgrim flask／同じ表の列：label, description, collection, on focus list of Wi…, instance of）
- 例2：240056 | 246585 | 254301 | 248176 | 254351（表：kylix／同じ表の列：label, description, instance of, collection, image, on focus list of Wi…）
- 例3：347 | 351 | 204938 | 40738 | 188904（表：wash basin／同じ表の列：label, description, image, instance of, collection）

## g0983 — wikidbs10k：見出し「transfermarkt team id」（Wikidata の型 `string`）（10 列）
- 例1：1402 | 829 | 18945 | 429 | 3899（表：participating team／同じ表の列：label, description, instance of, home venue, league, head coach）
- 例2：2784.0 | 24326.0 | 3899.0 | 1402.0 | 24926.0（表：winner／同じ表の列：label, description, instance of, home venue, league, head coach）
- 例3：720 | 2420 | 3557 | 336 | 3468（表：occupant／同じ表の列：label, description, instance of, Commons category, home venue, topic's main catego…）

## g0984 — wikidbs10k：見出し「videogamegeek platform id」（Wikidata の型 `string`）（10 列）
- 例1：4425 | 4434 | 10763 | 4734 | 5857（表：computing platform／同じ表の列：label, description, developer, Commons category, logo image, topic's main catego…）
- 例2：4430 | 4440 | 4734 | 4423 | 4425（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例3：4734 | 4441 | 4430 | 4422 | 5857（表：followed by／同じ表の列：label, description, instance of, manufacturer, image, Commons category）

## g0985 — wikidbs10k：見出し「aspect ratio (w:h)」（Wikidata の型 `wikibase-entityid`）（10 列）
- 例1：2:1 | 3:2 | 5:3（表：flag／同じ表の列：label, description, image, Commons category, Freebase ID, applies to jurisdic…）
- 例2：16:9（表：first appearance／同じ表の列：label, description, instance of, part of the series, title, season）
- 例3：16:9（表：followed by／同じ表の列：label, description, instance of, part of the series, title, season）

## g0986 — wikidbs10k：見出し「candidacy in election」（Wikidata の型 `wikibase-entityid`）（10 列）
- 例1：2018 Bury Metropolitan Borough Council … | 2016 Bury Metropolitan Borough Council … | 2018 Bury Metropolitan Borough Council … | 2016 Bury Metropolitan Borough Council … | 2021 Bury Metropolitan Borough Council …（表：political candidate／同じ表の列：label, description, instance of, name, occupation, Democracy Club cand…）
- 例2：2019 European Parliament election in No… | 2022 Trafford Metropolitan Borough Coun… | 2018 Trafford Metropolitan Borough Coun… | 2016 Trafford Metropolitan Borough Coun… | 2016 Trafford Metropolitan Borough Coun…（表：political candidate／同じ表の列：label, description, Democracy Club cand…, instance of, name, occupation）
- 例3：2016 Trafford Metropolitan Borough Coun… | 2022 Trafford Metropolitan Borough Coun… | 2018 Manchester City Council election i… | 2017 Greater Manchester mayoral election | 2019 European Parliament election in No…（表：political candidate／同じ表の列：label, description, instance of, name, Democracy Club cand…, occupation）

## g0987 — wikidbs10k：見出し「cathedral」（Wikidata の型 `wikibase-entityid`）（10 列）
- 例1：Notre-Dame-de-Fourvière Cathedral | Our Lady of the Sacred Heart Cathedral | Notre-Dame-de-l'Assomption Roman Cathol… | St. John Eudes Cathedral, Baie-Comeau | St Charles Borromeo Cathedral（表：jurisdiction／同じ表の列：label, description, Commons category, official website, Freebase ID, instance of）
- 例2：Notre-Dame Cathedral Basilica, Ottawa | Cathedral of St Teresa of Avila | Mary, Queen of the World Cathedral | Our Lady of the Sacred Heart Cathedral | St Joseph Cathedral（表：diocese／同じ表の列：label, description, Commons category, official website, Freebase ID, instance of）
- 例3：Mary, Queen of the World Cathedral | St. John Eudes Cathedral, Baie-Comeau | Basilique-Cathédrale Sainte-Cécile | St Joseph Cathedral | Our Lady of the Sacred Heart Cathedral（表：organization／同じ表の列：label, description, instance of, official website, Freebase ID, Commons category）

## g0988 — wikidbs10k：見出し「christian liturgical rite」（Wikidata の型 `wikibase-entityid`）（10 列）
- 例1：Roman Rite | Latin liturgical rite（表：jurisdiction／同じ表の列：label, description, Commons category, official website, Freebase ID, instance of）
- 例2：Latin liturgical rite | Roman Rite（表：diocese／同じ表の列：label, description, Commons category, official website, Freebase ID, instance of）
- 例3：Roman Rite | Latin liturgical rite（表：organization／同じ表の列：label, description, instance of, official website, Freebase ID, Commons category）

## g0989 — wikidbs10k：見出し「has effect」（Wikidata の型 `wikibase-entityid`）（10 列）
- 例1：chlorine dioxide exposure | methanethiol exposure | Ethylene oxide exposure | formaldehyde exposure | silane exposure（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：MAPP gas exposure | exposure to liquefied petroleum gas | methanethiol exposure | Ethylene oxide exposure | methylacetylene exposure（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：Methoxychlor exposure | 1,1-Dichloroethene exposure | formaldehyde exposure | Tert-Butyl chromate exposure | Dieldrin exposure（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g0990 — wikidbs10k：見出し「instrumentation」（Wikidata の型 `wikibase-entityid`）（10 列）
- 例1：voice（表：Winterreise／同じ表の列：label, description, instance of, form of creative wo…, composer, genre）
- 例2：voice（表：derivative work／同じ表の列：label, description, instance of, form of creative wo…, composer, genre）
- 例3：classical guitar | cello | flute | horn | piano（表：musical repertoire／同じ表の列：label, description, subclass of）

## g0991 — wikidbs10k：見出し「military branch」（Wikidata の型 `wikibase-entityid`）（10 列）
- 例1：Royal Canadian Navy（表：His Majesty's Canadian Ship／同じ表の列：label, description, instance of, image, operator, part of）
- 例2：United States Army Reserve | United States Army（表：parent company／同じ表の列：label, description, Commons category, country, Freebase ID, conflict）
- 例3：Canadian Army（表：Royal Canadian Armoured Corps／同じ表の列：label, description, country, instance of, conflict, official website）

## g0992 — wikidbs10k：見出し「symptoms and signs」（Wikidata の型 `wikibase-entityid`）（10 列）
- 例1：malaise | low-grade fever | poisoning | polyarthritis | fever（表：alphavirus infections／同じ表の列：label, description, has cause, subclass of, health specialty, instance of）
- 例2：headache | fatigue | malaise | dizziness | chest tightness（表：effect／同じ表の列：label, description, subclass of, has cause, afflicts, route of administra…）
- 例3：poisoning | polyarthritis | malaise | low-grade fever | prodrome（表：arbovirosis／同じ表の列：label, description, health specialty, subclass of, has cause, instance of）

## g0993 — wikidbs10k：見出し「number of pages」（Wikidata の型 `quantity`）（9 列）
- 例1：29.0 | 37.0 | 19.0 | 34.0 | 58.0（表：version, edition, or translation／同じ表の列：label, description, instance of, title, publication date, edition number）
- 例2：+12 | +37 | +29 | +11 | +55（表：source of information／同じ表の列：label, description, instance of, RfC ID, title, language of work or…）
- 例3：+45 | +95 | +125 | +85 | +126（表：source of information／同じ表の列：label, description, instance of, title, publication date, full work available…）

## g0994 — wikidbs10k：見出し「agrovoc id」（Wikidata の型 `string`）（9 列）
- 例1：c_1236 | c_7252 | c_4471 | c_2905 | c_870（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：c_1229 | c_8068 | c_7593 | c_4533 | c_15070（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, category for films …, GND ID）
- 例3：c_8114 | c_15070 | c_1229 | c_3373 | c_8068（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, category for films …, GND ID）

## g0995 — wikidbs10k：見出し「courage id」（Wikidata の型 `string`）（9 列）
- 例1：35510 | 13372 | 54967 | 10229 | 44294（表：grey literature／同じ表の列：label, description, instance of, collection, language of work or…, inception）
- 例2：16768 | 8598 | 39098 | 59540 | 4438（表：collection／同じ表の列：label, description, instance of, language of work or…, street address, inception）
- 例3：8178 | 55460 | 29111 | 49735 | 51211（表：voice recording／同じ表の列：label, description, instance of, inception, collection, language of work or…）

## g0996 — wikidbs10k：見出し「czech neighbourhood id code」（Wikidata の型 `string`）（9 列）
- 例1：19321 | 173231 | 41220 | 159417 | 126918（表：administrative territorial entity／同じ表の列：label, description, image, postal code, country, coordinate location）
- 例2：101681 | 189103 | 404853 | 54151 | 181803（表：administrative territorial entity／同じ表の列：label, description, Commons category, coordinate location, postal code, instance of）
- 例3：36501 | 27448 | 22705 | 72559 | 151416（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, coordinate location, Commons category, instance of）

## g0997 — wikidbs10k：見出し「enzyklopädie des europäischen ostens id」（Wikidata の型 `string`）（9 列）
- 例1：dbf0 | 35b3 | 542c | c071 | c0ba（表：language／同じ表の列：label, description, OmegaWiki Defined M…, ISO 639-1 code, ISO 639-2 code, ISO 639-3 code）
- 例2：dbf0 | b4e0 | 542c | b6cf | c0ba（表：research／同じ表の列：label, description, OmegaWiki Defined M…, ISO 639-1 code, ISO 639-2 code, ISO 639-3 code）
- 例3：c0ba | b6cf | 6664 | b4e0 | c071（表：Wikimedia category／同じ表の列：label, description, OmegaWiki Defined M…, ISO 639-1 code, ISO 639-2 code, ISO 639-3 code）

## g0998 — wikidbs10k：見出し「finess id」（Wikidata の型 `string`）（9 列）
- 例1：750002008.0 | 140013988.0 | 970102000.0 | 970200861.0 | 970402004.0（表：administrative territorial entity／同じ表の列：label, description, Dewey Decimal Class…, topic's main Wikime…, Commons category, country）
- 例2：970200861.0 | 750002008.0 | 280000779.0 | 970402004.0 | 130006570.0（表：physical location／同じ表の列：label, description, Dewey Decimal Class…, topic's main Wikime…, Commons category, country）
- 例3：390786994 | 890972250 | 800006710 | 310789144 | 160007373（表：physical location／同じ表の列：label, description, Dewey Decimal Class…, named after, topic's main Wikime…, Commons category）

## g0999 — wikidbs10k：見出し「gamefaqs platform id」（Wikidata の型 `string`）（9 列）
- 例1：ds | gba | xboxone | tg16 | iphone（表：computing platform／同じ表の列：label, description, developer, Commons category, logo image, topic's main catego…）
- 例2：n64 | wii | 3ds | switch | gameboy（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例3：n64 | wii | gameboy | snes | ds（表：followed by／同じ表の列：label, description, instance of, manufacturer, image, Commons category）

## g1000 — wikidbs10k：見出し「gamekult platform id」（Wikidata の型 `string`）（9 列）
- 例1：160001 | 160075 | 160034 | 160113 | 160032（表：computing platform／同じ表の列：label, description, developer, Commons category, logo image, topic's main catego…）
- 例2：160041 | 160011 | 160017 | 160018 | 160034（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例3：160009 | 160018 | 160091 | 160015 | 160106（表：followed by／同じ表の列：label, description, instance of, manufacturer, image, Commons category）

## g1001 — wikidbs10k：見出し「hrvatska enciklopedija id」（Wikidata の型 `string`）（9 列）
- 例1：28030.0 | 56332.0 | 56303.0 | 39962.0 | 30143.0（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例2：4677.0 | 56303.0 | 30143.0 | 28030.0 | 44490.0（表：facet of／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, New York Times topi…, GND ID）
- 例3：64260.0 | 63387.0 | 3683.0 | 46604.0 | 47764.0（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g1002 — wikidbs10k：見出し「ima number, broad sense」（Wikidata の型 `string`）（9 列）
- 例1：IMA2012-099 | IMA2005-044 | IMA1978-065 | IMA1989-023 | IMA2015-036（表：laueite mineral group／同じ表の列：label, description, Nickel-Strunz '10th…, subclass of, IMA status and/or r…, named after）
- 例2：IMA2017-073 | IMA1971-007 | IMA1971-004 | IMA1971-008 | IMA1971-006（表：zippeite mineral group／同じ表の列：label, description, Nickel-Strunz 9th e…, subclass of, chemical formula, IMA status and/or r…）
- 例3：IMA2014-069 | IMA1976 s.p. | IMA2021-108 | IMA2011-093 | IMA2019-108（表：cerite mineral group／同じ表の列：label, description, subclass of, IMA status and/or r…, type locality (geol…, crystal system）

## g1003 — wikidbs10k：見出し「integrated postsecondary education data system id」（Wikidata の型 `string`）（9 列）
- 例1：170976 | 144740 | 186131 | 221999 | 156125（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例2：213367 | 239105 | 143358 | 236595 | 216597（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）
- 例3：198385 | 152390 | 141325 | 161086 | 192749（表：liberal arts college in the United Stat…／同じ表の列：label, description, instance of, coordinate location, country, topic's main catego…）

## g1004 — wikidbs10k：見出し「kansaspedia id」（Wikidata の型 `string`）（9 列）
- 例1：15283 | 15277 | 15325 | 15312 | 15281（表：county of Kansas／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例2：15355.0 | 15285.0 | 15289.0 | 15332.0 | 15262.0（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：15330.0 | 15286.0 | 15323.0 | 15345.0 | 17702.0（表：administrative centre／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g1005 — wikidbs10k：見出し「mdws place id」（Wikidata の型 `string`）（9 列）
- 例1：011 | 004 | 017 | 031 | 005（表：jurisdiction／同じ表の列：label, description, population, Getty Thesaurus of …, Wikimedia outline, GeoNames ID）
- 例2：003 | 31.0 | 23.0 | 029 | 005（表：political border／同じ表の列：label, description, instance of, shares border with, head of state, Commons category）
- 例3：013 | 017 | 027 | 023 | 004（表：jurisdiction／同じ表の列：label, description, country, Commons category, topic's main catego…, Freebase ID）

## g1006 — wikidbs10k：見出し「mondo id」（Wikidata の型 `string`）（9 列）
- 例1：MONDO:0012012 | MONDO:0036484 | MONDO:0014154 | MONDO:0019548 | MONDO:0014467（表：Charcot-Marie-Tooth disease intermediat…／同じ表の列：label, description, instance of, subclass of, Orphanet ID, ICD-10-CM）
- 例2：MONDO:0012414 | MONDO:0019262 | MONDO:0012588 | MONDO:0008767 | MONDO:0015674（表：neuronal ceroid lipofuscinosis／同じ表の列：label, description, exact match, instance of, Orphanet ID, UMLS CUI）
- 例3：MONDO:0033044 | MONDO:0009571 | MONDO:0011296 | MONDO:0011821 | MONDO:0012695（表：Meckel syndrome／同じ表の列：label, description, instance of, subclass of, OMIM ID, genetic association）

## g1007 — wikidbs10k：見出し「mérimée id」（Wikidata の型 `string`）（9 列）
- 例1：PA00090535 | PA00109895 | IA22003434 | PA00098448 | PA00102004（表：Fanum／同じ表の列：label, description, instance of, Commons category, coordinate location, country）
- 例2：PA49000004 | PA00114617 | PA00116514 | PA00109635 | PA00117455（表：Salt cellar／同じ表の列：label, description, instance of, country, located in the admi…, Commons category）
- 例3：PA00087119 | PA00109957 | PA00104301 | PA00104593 | PA16000005（表：seigniorial home／同じ表の列：label, description, instance of, country, located in the admi…, Commons category）

## g1008 — wikidbs10k：見出し「pladias id」（Wikidata の型 `string`）（9 列）
- 例1：3219 | 2715 | 3640 | 2189 | 4000（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例2：870 | 772 | 621 | 413 | 464（表：taxon／同じ表の列：label, description, parent taxon, taxon name, taxon rank, image）
- 例3：3640 | 3252 | 1921 | 5130 | 4923（表：symbol／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g1009 — wikidbs10k：見出し「serial number」（Wikidata の型 `string`）（9 列）
- 例1：3233 | 2593 | 3142 | 3315 | 2465（表：Shay locomotive／同じ表の列：label, description, instance of, track gauge, Commons category, image）
- 例2：9076 | 16539 | 2925 | 2311 | 2269（表：Prussian P 8／同じ表の列：label, description, located in the admi…, instance of, country, part of）
- 例3：B1070 | B1031 | B1029 | B1065 | B1019（表：Falcon 9 booster／同じ表の列：label, description, Commons category, instance of, country of origin, manufacturer）

## g1010 — wikidbs10k：見出し「songkick artist id」（Wikidata の型 `string`）（9 列）
- 例1：898969 | 388471 | 531168 | 292712 | 538293（表：performing artist／同じ表の列：label, description, discography, MusicBrainz artist …, Commons category, image）
- 例2：268425 | 227030 | 240656 | 400904 | 417271（表：performing artist／同じ表の列：label, description, instance of, MusicBrainz artist …, genre, Freebase ID）
- 例3：219458 | 419152 | 219937 | 265781 | 521305（表：performing artist／同じ表の列：label, description, VIAF ID, MusicBrainz artist …, instance of, Freebase ID）

## g1011 — wikidbs10k：見出し「stadiumdb identifier」（Wikidata の型 `string`）（9 列）
- 例1：den/parken_stadion | mlt/ta_qali_stadium | alb/stadiumi_qemal_stafa | por/estadio_dom_afonso_henriques | por/estadio_da_luz（表：physical location／同じ表の列：label, description, coordinate location, Freebase ID, instance of, maximum capacity）
- 例2：alb/arena_kombetare | den/parken_stadion | por/estadio_dom_afonso_henriques | por/estadio_do_dragao | por/estadio_municipal_de_braga（表：stadium／同じ表の列：label, description, coordinate location, Freebase ID, instance of, maximum capacity）
- 例3：kor/jeju_world_cup_stadium | kor/suwon_world_cup_stadium | kor/daejeon_world_cup_stadium | jpn/shizuoka_ecopa_stadium | kor/guus_hiddink_stadium（表：physical location／同じ表の列：label, description, Commons category, coordinate location, Freebase ID, maximum capacity）

## g1012 — wikidbs10k：見出し「thegamesdb platform id」（Wikidata の型 `string`）（9 列）
- 例1：13 | 2 | 4980 | 11 | 1（表：computing platform／同じ表の列：label, description, developer, Commons category, logo image, topic's main catego…）
- 例2：5 | 4912 | 2 | 3 | 4（表：computing platform／同じ表の列：label, description, subclass of, Freebase ID, topic's main catego…, Commons category）
- 例3：4950 | 5 | 6 | 41 | 2（表：follows／同じ表の列：label, description, manufacturer, Commons category, follows, followed by）

## g1013 — wikidbs10k：見出し「times higher education world university id」（Wikidata の型 `string`）（9 列）
- 例1：saint-josephs-university | university-san-francisco | university-houston | vanderbilt-university | university-dayton（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例2：marquette-university | university-colorado-boulder | seattle-university | oregon-state-university | villanova-university（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）
- 例3：university-akron | university-sussex | stanford-university | university-colorado-boulder | university-pittsburgh（表：employer／同じ表の列：label, description, instance of, country, Commons category, coordinate location）

## g1014 — wikidbs10k：見出し「tmdb movie id」（Wikidata の型 `string`）（9 列）
- 例1：929 | 746808 | 36557 | 143136 | 13207（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例2：17422 | 256106 | 288740 | 12659 | 11492（表：sixth generation Chinese films／同じ表の列：label, description, IMDb ID, instance of, director, original language o…）
- 例3：768325 | 194246 | 775690 | 638128 | 776167（表：Enrique Carreras filmography／同じ表の列：label, description, IMDb ID, instance of, original language o…, director）

## g1015 — wikidbs10k：見出し「youtube video id」（Wikidata の型 `string`）（9 列）
- 例1：gs3lqEJHSnA | g0wCF04ddnw | MiZ8V3NHwfM | U4sp10HUI6Y | gu8nQFHHD9w（表：first appearance／同じ表の列：label, description, instance of, part of the series, title, season）
- 例2：FDoY1zaWB4I | wluh0U2wZuY | KOUP8AGYdr8 | mHq89x2z2Lc | oav0TXI6bqc（表：followed by／同じ表の列：label, description, instance of, part of the series, title, season）
- 例3：PigChYq_FrM | 26FJTtLOu2s | g0wCF04ddnw | BQBmKvRd0B0 | gI40pUTzGPI（表：follows／同じ表の列：label, description, instance of, part of the series, title, season）

## g1016 — wikidbs10k：見出し「carnegie classification of institutions of higher education」（Wikidata の型 `wikibase-entityid`）（9 列）
- 例1：master's colleges and universities: lar… | doctoral university: higher research ac… | doctoral university: highest research a… | doctoral university: moderate research …（表：organization／同じ表の列：label, description, Commons category, inception, instance of, topic's main catego…）
- 例2：doctoral university: moderate research … | master's colleges and universities: lar… | master's colleges and universities: med… | doctoral university: highest research a… | doctoral university: higher research ac…（表：organization／同じ表の列：label, description, Commons category, instance of, topic's main catego…, coordinate location）
- 例3：baccalaureate colleges: diverse fields | baccalaureate colleges: arts and scienc… | master's colleges and universities: med… | master's colleges and universities: sma… | baccalaureate/associate's colleges: mix…（表：liberal arts college in the United Stat…／同じ表の列：label, description, instance of, coordinate location, country, topic's main catego…）

## g1017 — wikidbs10k：見出し「fare zone」（Wikidata の型 `wikibase-entityid`）（9 列）
- 例1：London fare zone 6 | London fare zone 1 | London fare zone 9 | London fare zone 3 | London fare zone 12（表：Crossrail／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例2：London fare zone 3 | London fare zone 5 | London fare zone Contactless-only | London fare zone 1 | London fare zone 12（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例3：London fare zone 1（表：London station group／同じ表の列：label, description, instance of, country, connecting line, Commons category）

## g1018 — wikidbs10k：見出し「list related to category」（Wikidata の型 `wikibase-entityid`）（9 列）
- 例1：list of cultural property in Balzers | list of cultural property in Eschen | list of cultural property in Ruggell | list of cultural property in Schaan | list of cultural property in Triesen（表：Wikimedia category／同じ表の列：label, description, instance of, category contains, Commons category）
- 例2：National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li…（表：Wikimedia category／同じ表の列：label, description, instance of, Commons category）
- 例3：National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li… | National Register of Historic Places li…（表：Wikimedia category／同じ表の列：label, description, instance of, Commons category）

## g1019 — wikidbs10k：見出し「located on linear feature」（Wikidata の型 `wikibase-entityid`）（9 列）
- 例1：Heathrow Link Line, Heathrow Terminal 5… | Heathrow Link Line, Tunnel portal to Te… | Liverpool Street and Norwich Line, Live… | Dalston Kingsland Hackney Wick and Nort… | North Kent Loop（表：Crossrail／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例2：Heathrow Link Line, Tunnel portal to Te… | West Ealing Loop, West Ealing Junction … | Dalston Kingsland Hackney Wick and Nort… | Moorgate to Carlton Junction Line (Midl… | Liverpool Street and Norwich Line, Live…（表：adjacent station／同じ表の列：label, description, Commons category, coordinate location, country, instance of）
- 例3：Kettenbach-Leitgraben | Ludwig Canal | Pilsach-Leitgraben（表：inlet structure／同じ表の列：label, description, instance of, country, located in the admi…, coordinate location）

## g1020 — wikidbs10k：見出し「type locality (geology)」（Wikidata の型 `wikibase-entityid`）（9 列）
- 例1：Ivigtuut cryolite deposit | Yenisei Range | Cornelia shaft, Hagendorf South open cut | Yaroslavskoye tin deposit | Karasug REE-Sr-Ba-Fe-fluorite deposit（表：neso-aluminofluoride minerals (3.CB.)／同じ表の列：label, description, Strunz 8th edition …, subclass of, chemical formula, Nickel-Strunz 9th e…）
- 例2：pegmatite No. 22, Gottcha claim | Franklin | Harstigen mine | Big creek | Zimapán（表：apatite mineral group／同じ表の列：label, description, subclass of, chemical formula, named after, crystal system）
- 例3：Foote Lithium Co. mine | Cornelia shaft, Hagendorf South open cut | Clay canyon, Fairfield | Bol'shoi Tatkul' lake | Bou Azer district（表：laueite mineral group／同じ表の列：label, description, Nickel-Strunz '10th…, subclass of, IMA status and/or r…, named after）

## g1021 — wikidbs10k：見出し「voice actor」（Wikidata の型 `wikibase-entityid`）（9 列）
- 例1：Michael Huang（表：first appearance／同じ表の列：label, description, instance of, part of the series, title, season）
- 例2：Michael Huang（表：followed by／同じ表の列：label, description, instance of, part of the series, title, season）
- 例3：Michael Huang（表：follows／同じ表の列：label, description, instance of, part of the series, title, season）

## g1022 — wikidbs10k：見出し「wheel arrangement」（Wikidata の型 `wikibase-entityid`）（9 列）
- 例1：4-6-2（表：SR Merchant Navy class／同じ表の列：label, description, instance of, manufacturer, named after, Commons category）
- 例2：0-4-4-4-0T | 0-4-4-0T（表：Shay locomotive／同じ表の列：label, description, instance of, track gauge, Commons category, image）
- 例3：4-6-0（表：Prussian P 8／同じ表の列：label, description, located in the admi…, instance of, country, part of）

## g1023 — wikidbs10k：見出し「wikidata property」（Wikidata の型 `wikibase-entityid`）（9 列）
- 例1：asteroid | Montebello sul Sangro | Jacqueline Cochran | Category:Cathedrals in Belgium | Bolho（表：list of lights／同じ表の列：label, description, instance of, publisher）
- 例2：Syria | Franciszek Karpiński | Waldbröl | Hemel Hempstead | Brunswick（表：sports database／同じ表の列：label, description, instance of）
- 例3：Astronotinae | Leonardo da Vinci | Marshall Islands | October 29 | Osdorf（表：historic preservation／同じ表の列：label, description, country, subclass of）

## g1024 — wikidbs10k：見出し「number of cases」（Wikidata の型 `quantity`）（8 列）
- 例1：+41 | +8 | +208921 | +4794287 | +16（表：cause／同じ表の列：label, description, part of, country, location, coordinate location）
- 例2：+550 | +22838110 | +11 | +38 | +29（表：COVID-19 pandemic in the United States／同じ表の列：label, description, part of, instance of, country, location）
- 例3：+2697159 | +401527 | +1301860 | +1 | +16104（表：COVID-19 pandemic in Europe／同じ表の列：label, description, part of, country, instance of, number of deaths）

## g1025 — wikidbs10k：見出し「radius」（Wikidata の型 `quantity`）（8 列）
- 例1：+1737.1 | +1353.4 | +6051.8 | +2574 | +252.1（表：located on astronomical body／同じ表の列：label, description, named after, Commons category, parent astronomical…, image）
- 例2：0.38 | 0.98 | 0.85899913 | 0.5570991999999999 | 0.7929999999999999（表：primary body／同じ表の列：label, description, constellation, spectral class, catalog code, instance of）
- 例3：+1353.4 | +2634.1 | +262.7 | +2439.7 | +3389.50（表：located on astronomical body／同じ表の列：label, description, apparent magnitude, orbital eccentricity, GND ID, parent astronomical…）

## g1026 — wikidbs10k：見出し「time-weighted average exposure limit」（Wikidata の型 `quantity`）（8 列）
- 例1：+0.2 | +0.5 | +1800 | +0.6 | +0.4（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：+0.4 | +1650 | +40 | +0.1 | +7（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：+250 | +350 | +200 | +240 | +300（表：Class IC flammable liquid／同じ表の列：label, description, chemical structure, CAS Registry Number, canonical SMILES, Commons category）

## g1027 — wikidbs10k：見出し「vapor pressure」（Wikidata の型 `quantity`）（8 列）
- 例1：+9.5 | +1 | +5.1 | +39.5 | +5.2（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：+35 | +14.9 | +5 | +1.46 | +3.3（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：+58 | +19 | +0.0000002 | +0.0000003 | +38（表：occupational carcinogen／同じ表の列：label, description, Freebase ID, instance of, NIOSH Pocket Guide …, RTECS number）

## g1028 — wikidbs10k：見出し「visitors per year」（Wikidata の型 `quantity`）（8 列）
- 例1：+1000 | +2668 | +700 | +6398 | +2891（表：archaeological artifact museum／同じ表の列：label, description, instance of, country, coordinate location, image）
- 例2：+29526 | +12299 | +25766 | +5048 | +26074（表：part／同じ表の列：label, description, instance of, country, Federal-State Coope…, street address）
- 例3：+48034 | +25268 | +33956 | +68895 | +4843（表：Okanagan Regional Library District／同じ表の列：label, description, country, located in the admi…, part of, coordinate location）

## g1029 — wikidbs10k：見出し「biolib taxon id」（Wikidata の型 `string`）（8 列）
- 例1：59721.0 | 155254.0 | 60603.0 | 59669.0 | 60563.0（表：secretion or excretion／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：1827.0 | 1696.0 | 1759.0 | 8866.0 | 20894.0（表：symbol／同じ表の列：label, description, taxon rank, IUCN conservation s…, Commons category, taxon name）
- 例3：3417 | 40435 | 41465 | 38966 | 41509（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）

## g1030 — wikidbs10k：見出し「cals encyclopedia of arkansas id」（Wikidata の型 `string`）（8 列）
- 例1：little-river-county-785 | mississippi-county-791 | van-buren-county-817 | fulton-county-769 | chicot-county-753（表：county of Arkansas／同じ表の列：label, description, located in the admi…, Commons category, country, coordinate location）
- 例2：montgomery-county-793 | pope-county-801 | faulkner-county-767 | madison-county-788 | woodruff-county-815（表：political border／同じ表の列：label, description, located in the admi…, shares border with, Commons category, country）
- 例3：boone-county-749 | perry-county-796 | carroll-county-752 | washington-county-813 | crittenden-county-762（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, Commons category, country, coordinate location）

## g1031 — wikidbs10k：見出し「chemical structure」（Wikidata の型 `string`）（8 列）
- 例1：Cyanogen.png | Chlorine dioxide.svg | Methanethiol.svg | DiboraneSchema.png | Stibine.png（表：flammable gas／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例2：Hydrogen selenide.svg | Cobalt tetracarbonyl hydride.svg | Ethylene-oxide-2D-skeletal.svg | Schwefelwasserstoff.svg | Propyne.png（表：cause／同じ表の列：label, description, instance of, chemical formula, Commons category, canonical SMILES）
- 例3：2-Hexanone V.1.svg | Pentaborane.png | Nitroethane.svg | Tetraethyl orthosilicate.svg | Cumol.svg（表：Class IC flammable liquid／同じ表の列：label, description, CAS Registry Number, canonical SMILES, Commons category, instance of）

## g1032 — wikidbs10k：見出し「cycling archives race id」（Wikidata の型 `string`）（8 列）
- 例1：103006 | 103017 | 103008 | 103009 | 103016（表：Challenge Desgrange-Colombo／同じ表の列：label, description, point in time, sport, winner, has part(s)）
- 例2：103008 | 103007 | 103017 | 103014 | 103016（表：followed by／同じ表の列：label, description, point in time, sport, winner, has part(s)）
- 例3：103012 | 103006 | 97508 | 103014 | 103007（表：follows／同じ表の列：label, description, point in time, sport, instance of, followed by）

## g1033 — wikidbs10k：見出し「danish urban area code」（Wikidata の型 `string`）（8 列）
- 例1：10474 | 10482 | 10391 | 10002 | 10421（表：capital city／同じ表の列：label, description, coordinate location, country, located in the admi…, instance of）
- 例2：11045 | 10113 | 10583 | 10298 | 11048（表：capital city／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）
- 例3：10491 | 10383 | 10110 | 10886 | 10342（表：capital city／同じ表の列：label, description, country, coordinate location, Commons category, located in the admi…）

## g1034 — wikidbs10k：見出し「ebiodiversity id」（Wikidata の型 `string`）（8 列）
- 例1：132975.0 | 155190.0 | 145502.0 | 156738.0 | 131173.0（表：secretion or excretion／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：72338.0 | 57790.0 | 51921.0 | 72518.0 | 98429.0（表：symbol／同じ表の列：label, description, taxon rank, IUCN conservation s…, Commons category, taxon name）
- 例3：209847 | 4806 | 5501 | 3309 | 5907（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）

## g1035 — wikidbs10k：見出し「elstat geographical code」（Wikidata の型 `string`）（8 列）
- 例1：4806 | 4612 | 4803 | 5103 | 4908（表：administrative territorial entity／同じ表の列：label, description, OpenStreetMap relat…, country, instance of, located in the admi…）
- 例2：3204 | 35 | 44 | 3601 | 3602（表：administrative territorial entity／同じ表の列：label, description, coordinate location, country, instance of, located in the admi…）
- 例3：4807 | 4801 | 5101 | 4501 | 4804（表：administrative territorial entity／同じ表の列：label, description, OpenStreetMap relat…, country, instance of, located in the admi…）

## g1036 — wikidbs10k：見出し「isfdb title id」（Wikidata の型 `string`）（8 列）
- 例1：34137 | 34139 | 34154 | 34148 | 34157（表：Isaac Asimov Presents The Great SF Stor…／同じ表の列：label, description, genre, editor, part of, instance of）
- 例2：34151 | 29183 | 35596 | 34150 | 34154（表：followed by／同じ表の列：label, description, editor, part of, genre, instance of）
- 例3：996687 | 34149 | 34140 | 29183 | 34138（表：follows／同じ表の列：label, description, genre, editor, part of, instance of）

## g1037 — wikidbs10k：見出し「montreux jazz festival concert id」（Wikidata の型 `string`）（8 列）
- 例1：4170 | 2248 | 2268 | 2282 | 2293（表：Montreux Jazz Festival 1987／同じ表の列：label, description, instance of, part of, point in time, location）
- 例2：946 | 1940 | 138 | 867 | 132（表：Montreux Jazz Festival 1982／同じ表の列：label, description, instance of, part of, point in time, location）
- 例3：626 | 113 | 672 | 118 | 104（表：Montreux Jazz Festival 1981／同じ表の列：label, description, instance of, part of, point in time, location）

## g1038 — wikidbs10k：見出し「museu paulista objects id」（Wikidata の型 `string`）（8 列）
- 例1：escrita-escritorio-escola-114 | escrita-escritorio-escola-9 | escrita-escritorio-escola-35 | escrita-escritorio-escola-36 | escrita-escritorio-escola-19（表：office supply／同じ表の列：label, description, instance of, made from material, inventory number, location）
- 例2：escrita-escritorio-escola-116 | escrita-escritorio-escola-126 | escrita-escritorio-escola-79 | escrita-escritorio-escola-76 | escrita-escritorio-escola-42（表：stationery／同じ表の列：label, description, instance of, made from material, location, collection）
- 例3：bonecas-0s-275 | bonecas-0s-168 | bonecas-0s-6 | bonecas-0s-280 | bonecas-0s-241（表：doll clothes／同じ表の列：label, description, instance of, collection, inventory number, image）

## g1039 — wikidbs10k：見出し「npca id」（Wikidata の型 `string`）（8 列）
- 例1：timucuan-ecological-historic-preserve | lake-clark-national-park-preserve | new-river-gorge-national-river | mojave-national-preserve | glacier-bay-national-park-preserve（表：national preserve／同じ表の列：label, description, Commons category, located in the admi…, IUCN protected area…, instance of）
- 例2：birmingham-civil-rights | george-washington-carver-national-monum… | bandelier-national-monument | great-falls-park | cedar-breaks-national-monument（表：National Park System unit／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）
- 例3：boston-african-american-national-histor… | hampton-national-historic-site | fort-scott-national-historic-site | lincoln-home-national-historic-site | fort-bowie-national-historic-site（表：National Historic Site／同じ表の列：label, description, Commons category, NRHP reference numb…, coordinate location, country）

## g1040 — wikidbs10k：見出し「observation.org id」（Wikidata の型 `string`）（8 列）
- 例1：75392.0 | 79919.0 | 418.0 | 428.0 | 417.0（表：symbol／同じ表の列：label, description, taxon rank, IUCN conservation s…, Commons category, taxon name）
- 例2：7563 | 6979 | 2521 | 6518 | 6994（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例3：7181 | 2535 | 2424 | 2697 | 6509（表：symbol／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g1041 — wikidbs10k：見出し「ofdb film id」（Wikidata の型 `string`）（8 列）
- 例1：11633 | 184640 | 239352 | 317228 | 163394（表：film reboot／同じ表の列：label, description, IMDb ID, director, cast member, screenwriter）
- 例2：109941 | 214134 | 173186 | 131175 | 215965（表：sixth generation Chinese films／同じ表の列：label, description, IMDb ID, instance of, director, original language o…）
- 例3：29428 | 66692 | 97162 | 17510 | 19456（表：work／同じ表の列：label, description, original broadcaster, IMDb ID, country of origin, topic's main catego…）

## g1042 — wikidbs10k：見出し「park alpha code」（Wikidata の型 `string`）（8 列）
- 例1：GLBA | PINE | NERI | MOJA | GAAR（表：national preserve／同じ表の列：label, description, Commons category, located in the admi…, IUCN protected area…, instance of）
- 例2：KAWW | FOST | TICA | VICR | TUZI（表：National Park System unit／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）
- 例3：FILA | TUAI | FOSC | SAIR | MANZ（表：National Historic Site／同じ表の列：label, description, Commons category, NRHP reference numb…, coordinate location, country）

## g1043 — wikidbs10k：見出し「software version identifier」（Wikidata の型 `string`）（8 列）
- 例1：11.1 | 2.1 | 10.0 | 11.0 | 2.0（表：Stata／同じ表の列：label, description, subclass of, developer, publication date, followed by）
- 例2：1.1 | 2.1 | 13.1 | 4.0 | 14.0（表：followed by／同じ表の列：label, description, subclass of, follows, publication date, developer）
- 例3：13.0 | 6.0 | 1.0 | 2.05 | 14.1（表：follows／同じ表の列：label, description, subclass of, developer, publication date, followed by）

## g1044 — wikidbs10k：見出し「spectral class」（Wikidata の型 `string`）（8 列）
- 例1：M0V | pulsar | K0V | K3V | M2.5（表：primary body／同じ表の列：label, description, constellation, catalog code, instance of, Freebase ID）
- 例2：B9.5III | B3V | B1III-IV | B0.5IV + B1V | F5Iab:（表：navigational star／同じ表の列：label, description, constellation, instance of, catalog code, Freebase ID）
- 例3：G6III | K0 | G5 III SB | G5V | K3V（表：Ursa Major Moving Group／同じ表の列：label, description, constellation, catalog code, instance of, SIMBAD ID）

## g1045 — wikidbs10k：見出し「statistical service of cyprus geocode」（Wikidata の型 `string`）（8 列）
- 例1：5011 | 5132 | 5134 | 5324 | 5305（表：Limassol District／同じ表の列：label, description, Commons category, country, coordinate location, located in the admi…）
- 例2：5103.0 | 5212.0 | 5131.0 | 5323.0 | 5222.0（表：political border／同じ表の列：label, description, coordinate location, located in time zone, GeoNames ID, locator map image）
- 例3：5131.0 | 5222.0 | 5213.0 | 5136.0 | 5316.0（表：jurisdiction／同じ表の列：label, description, coordinate location, located in time zone, GeoNames ID, locator map image）

## g1046 — wikidbs10k：見出し「taxref id」（Wikidata の型 `string`）（8 列）
- 例1：48479.0 | 510311.0 | 31678.0 | 48691.0 | 42644.0（表：secretion or excretion／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）
- 例2：61153.0 | 4010.0 | 60630.0 | 60686.0 | 61699.0（表：symbol／同じ表の列：label, description, taxon rank, IUCN conservation s…, Commons category, taxon name）
- 例3：105817 | 129906 | 116759 | 87720 | 92282（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）

## g1047 — wikidbs10k：見出し「vascan id」（Wikidata の型 `string`）（8 列）
- 例1：3281 | 4171 | 4222 | 6701 | 2963（表：symbol／同じ表の列：label, description, taxon rank, taxon name, image, Commons category）
- 例2：1609 | 1383 | 1029 | 1515 | 1467（表：taxon／同じ表の列：label, description, parent taxon, taxon name, taxon rank, image）
- 例3：4606 | 5496 | 2963 | 6701 | 7169（表：symbol／同じ表の列：label, description, taxon rank, taxon name, Commons category, image）

## g1048 — wikidbs10k：見出し「webb-site organization id」（Wikidata の型 `string`）（8 列）
- 例1：27091 | 22567 | 27099 | 27090 | 27096（表：legislature／同じ表の列：label, description, topic's main catego…, instance of, country, applies to jurisdic…）
- 例2：27096 | 27090 | 25325 | 27088 | 27097（表：district council of Hong Kong／同じ表の列：label, description, Commons category, topic's main catego…, instance of, country）
- 例3：22567 | 27088 | 27096 | 27097 | 27098（表：legislature／同じ表の列：label, description, topic's main catego…, Commons category, instance of, country）

## g1049 — wikidbs10k：見出し「award received」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：Croix de guerre 1914–1918（表：political border／同じ表の列：label, description, Commons category, country, INSEE municipality …, located in the admi…）
- 例2：Croix de guerre 1914–1918（表：jurisdiction／同じ表の列：label, description, Commons category, country, INSEE municipality …, located in the admi…）
- 例3：royal charter（表：livery company／同じ表の列：label, description, instance of, country, office held by head…, Freebase ID）

## g1050 — wikidbs10k：見出し「broadcast by」（Wikidata の型 `wikibase-entityid`）（8 列）
- 例1：FloGrappling（表：Brazilian Jiu Jitsu Competition／同じ表の列：label, description, instance of, country, organizer, point in time）
- 例2：FloGrappling（表：followed by／同じ表の列：label, description, instance of, country, organizer, point in time）
- 例3：FloGrappling（表：follows／同じ表の列：label, description, instance of, country, sport, organizer）

## 答えの雛形

```
g0901	
g0902	
g0903	
g0904	
g0905	
g0906	
g0907	
g0908	
g0909	
g0910	
g0911	
g0912	
g0913	
g0914	
g0915	
g0916	
g0917	
g0918	
g0919	
g0920	
g0921	
g0922	
g0923	
g0924	
g0925	
g0926	
g0927	
g0928	
g0929	
g0930	
g0931	
g0932	
g0933	
g0934	
g0935	
g0936	
g0937	
g0938	
g0939	
g0940	
g0941	
g0942	
g0943	
g0944	
g0945	
g0946	
g0947	
g0948	
g0949	
g0950	
g0951	
g0952	
g0953	
g0954	
g0955	
g0956	
g0957	
g0958	
g0959	
g0960	
g0961	
g0962	
g0963	
g0964	
g0965	
g0966	
g0967	
g0968	
g0969	
g0970	
g0971	
g0972	
g0973	
g0974	
g0975	
g0976	
g0977	
g0978	
g0979	
g0980	
g0981	
g0982	
g0983	
g0984	
g0985	
g0986	
g0987	
g0988	
g0989	
g0990	
g0991	
g0992	
g0993	
g0994	
g0995	
g0996	
g0997	
g0998	
g0999	
g1000	
g1001	
g1002	
g1003	
g1004	
g1005	
g1006	
g1007	
g1008	
g1009	
g1010	
g1011	
g1012	
g1013	
g1014	
g1015	
g1016	
g1017	
g1018	
g1019	
g1020	
g1021	
g1022	
g1023	
g1024	
g1025	
g1026	
g1027	
g1028	
g1029	
g1030	
g1031	
g1032	
g1033	
g1034	
g1035	
g1036	
g1037	
g1038	
g1039	
g1040	
g1041	
g1042	
g1043	
g1044	
g1045	
g1046	
g1047	
g1048	
g1049	
g1050	
```
