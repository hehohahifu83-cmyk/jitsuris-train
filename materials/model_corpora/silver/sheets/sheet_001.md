# 銀ラベルのシート 001 / 008（外の学習データの読み替え）

- **このまとまりの列は、ジツリスの決まり（LABEL_GUIDE.md v2.0）のどの種類か**を 1 つ答える。例は別々の表から最大 3 列
- まとまりの中で種類が混ざって 1 つに決められない、または例では決められない → `unknown`。人の名前・連絡先が入っている、値が崩れている → `S`
- SOTAB の列には見出しがない（Web の表の値だけ）。元の種類（Schema.org・DBpedia）は参考。WikiDBs の見出しは Wikidata の属性の名前
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 答え：末尾の雛形を、ChatGPT は `answers/sheet_001.tsv`、Grok は `answers_grok/sheet_001.tsv` に写して埋める。**相手の答えは見ない**

## g0001 — wikidbs10k：見出し「instance of」（Wikidata の型 `wikibase-entityid`）（40,448 列）
- 例1：protein（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, encoded by）
- 例2：gene（表：encoded by／同じ表の列：label, description, NCBI locus tag, Entrez Gene ID, found in taxon, subclass of）
- 例3：protein（表：encodes／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, encoded by）

## g0002 — wikidbs10k：見出し「label」（Wikidata の型 `string`）（40,446 列）
- 例1：Hypothetical protein Mb2125c | PE-PGRS family protein PE_PGRS21 Rv1087 | PE family protein PE35 Rv3872 | PE-PGRS family protein PE_PGRS1 Rv0109 | PE-PGRS family protein PE_PGRS27 Rv1450c（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：description, UniProt protein ID, subclass of, found in taxon, encoded by, has part(s)）
- 例2：PE family protein PE36 Rv3893c | PE-PGRS family protein Wag22 Rv1759c | PE-PGRS family protein PE_PGRS52 Rv3388 | PE-family protein ML0538 | PE family protein Mb1421（表：encoded by／同じ表の列：description, NCBI locus tag, Entrez Gene ID, found in taxon, subclass of, encodes）
- 例3：Hypothetical protein MAB_0149c | PE-PGRS family protein PE_PGRS7 Rv0578c | PE family protein Mb2355 | PE-PGRS family protein PE_PGRS57 Rv3514 | Hypothetical protein Mb2125c（表：encodes／同じ表の列：description, UniProt protein ID, subclass of, found in taxon, encoded by, has part(s)）

## g0003 — wikidbs10k：見出し「country」（Wikidata の型 `wikibase-entityid`）（15,403 列）
- 例1：Australia | New Zealand | United States of America | Canada（表：award for best album (genre)／同じ表の列：label, description, Freebase ID, instance of, part of, subclass of）
- 例2：Tanzania | New Zealand | Australia | Canada | United States of America（表：part／同じ表の列：label, description, instance of, topic's main catego…, official website, Freebase ID）
- 例3：Canada | United States of America | Mexico | Australia（表：2004 Champ Car season／同じ表の列：label, description, sport, point in time, instance of, pole position）

## g0004 — wikidbs10k：見出し「freebase id」（Wikidata の型 `string`）（13,110 列）
- 例1：/m/026rsbr | /m/0bgxzf | /m/03nl8c | /m/04yh4p_ | /m/0y67n09（表：award for best album (genre)／同じ表の列：label, description, instance of, country, part of, subclass of）
- 例2：/m/026vn2 | /m/09gc8hg | /m/024rg2 | /m/0152rx | /m/0ks43（表：part／同じ表の列：label, description, instance of, topic's main catego…, official website, country）
- 例3：/m/03wgxr6 | /m/03yjshb | /m/03hg3_f | /m/04054bq | /m/03ydyrf（表：2004 Champ Car season／同じ表の列：label, description, sport, point in time, instance of, country）

## g0005 — wikidbs10k：見出し「commons category」（Wikidata の型 `string`）（12,726 列）
- 例1：Las Vegas Motor Speedway | Road America | Long Beach Street Circuit | Circuit Gilles Villeneuve | Milwaukee Mile（表：physical location／同じ表の列：label, description, country, located in the admi…, coordinate location, instance of）
- 例2：Denver, Colorado | Los Angeles County, California | Monterey County, California | Nuevo León | Montreal（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, coordinate location）
- 例3：People of Cleveland, Ohio | People of Portland, Oregon | People of Long Beach, California | People of Monterey County, California | People of Nuevo León（表：Wikimedia category／同じ表の列：label, description, instance of, category combines t…, category contains）

## g0006 — wikidbs10k：見出し「part of」（Wikidata の型 `wikibase-entityid`）（12,037 列）
- 例1：Aspartic peptidase domain superfamily | Putative uncharacterized transport prot… | WD40/YVTN repeat-like-containing domain… | Histidine phosphatase superfamily, clad… | ESAT-6-like superfamily（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, encoded by）
- 例2：Alpha/Beta hydrolase fold | PE-PGRS family, N-terminal domain, prot… | WD40/YVTN repeat-like-containing domain… | membrane proteins | Aspartic peptidase domain superfamily（表：encodes／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, encoded by）
- 例3：Tanzania Music Awards | ARIA Music Awards | Country Music Association Awards | Grammy Awards | American Music Awards（表：award for best album (genre)／同じ表の列：label, description, Freebase ID, instance of, country, subclass of）

## g0007 — wikidbs10k：見出し「found in taxon」（Wikidata の型 `wikibase-entityid`）（11,877 列）
- 例1：Mycobacterium abscessus | Mycobacterium bovis AF2122/97 | Mycobacterium smegmatis str. MC2 155 | Mycobacterium leprae TN | Mycobacterium tuberculosis H37Rv（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：label, description, UniProt protein ID, subclass of, encoded by, has part(s)）
- 例2：Mycobacterium abscessus | Mycobacterium bovis AF2122/97 | Mycobacterium tuberculosis H37Rv | Mycobacterium leprae TN | Mycobacterium smegmatis str. MC2 155（表：encoded by／同じ表の列：label, description, NCBI locus tag, Entrez Gene ID, subclass of, encodes）
- 例3：Mycobacterium tuberculosis H37Rv | Mycobacterium leprae TN | Mycobacterium smegmatis str. MC2 155 | Mycobacterium abscessus | Mycobacterium bovis AF2122/97（表：encodes／同じ表の列：label, description, UniProt protein ID, subclass of, encoded by, has part(s)）

## g0008 — wikidbs10k：見出し「subclass of」（Wikidata の型 `wikibase-entityid`）（11,665 列）
- 例1：protein（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：label, description, UniProt protein ID, found in taxon, encoded by, has part(s)）
- 例2：gene（表：encoded by／同じ表の列：label, description, NCBI locus tag, Entrez Gene ID, found in taxon, encodes）
- 例3：protein（表：encodes／同じ表の列：label, description, UniProt protein ID, found in taxon, encoded by, has part(s)）

## g0009 — wikidbs10k：見出し「located in the administrative territorial entity」（Wikidata の型 `wikibase-entityid`）（9,487 列）
- 例1：Plymouth | Queensland | Portland | Long Beach | Denver（表：physical location／同じ表の列：label, description, Commons category, country, coordinate location, instance of）
- 例2：Sheboygan County | United States of America | California | Oregon | Cuyahoga County（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例3：Noguera | Segrià | Pla d'Urgell（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）

## g0010 — wikidbs10k：見出し「topic's main category」（Wikidata の型 `wikibase-entityid`）（9,306 列）
- 例1：Category:NAACP Image Awards | Category:Country Music Association Awar… | Category:GMA Dove Awards | Category:ARIA Music Awards | Category:Soul Train Music Awards（表：part／同じ表の列：label, description, instance of, official website, Freebase ID, country）
- 例2：Category:Los Angeles County, California | Category:West Allis, Wisconsin | Category:Queensland | Category:Cleveland | Category:Long Beach, California（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例3：Category:Torres de Segre | Category:Menàrguens | Category:Artesa de Lleida | Category:Montoliu de Lleida | Category:Alcoletge（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）

## g0011 — sotab_v2：元の種類 `currency`（8,395 列）
- 例1：EUR
- 例2：EUR
- 例3：GBP

## g0012 — wikidbs10k：見出し「image」（Wikidata の型 `string`）（7,736 列）
- 例1：Montreal Montage 2020.jpg | Portland, Oregon Collage.jpg | Milwaukee County Courthouse.jpg | Lago de Chapultepec.jpg | Ciudad.de.Mexico.City.Distrito.Federal.…（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Castelltossal.jpg | Lleida (40262867523).jpg | Menàrguens, Lleida.jpg | Vista aèria de Rosselló.JPG | Portella, Lérida, España, 2015-12-23, D…（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例3：20081227ALGERRI.jpg | Alcanó. Església de Sant Pere. s.XVIII … | Castell de Vinfaro.jpg | Alcarràs iglesia.jpg | Església de l'Assumpció d'Albesa.JPG（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0013 — sotab_v2：元の種類 `Date`（7,652 列）
- 例1：2013-08-01 | 2014-07-11 | 2020-07-10 | 2015-11-13 | 2020-09-18
- 例2：2018-09-20 | 2020-08-26 | 2018-05-03 | 2020-08-06 | 2019-02-07
- 例3：Aug 25, 2015 | Jan 05, 2012 | Sep 19, 2019 | Nov 13, 2018 | Nov 28, 2017

## g0014 — sotab_v2：元の種類 `price`（7,171 列）
- 例1：25.64 | 22.56 | 25.79 | 22.25 | 16.46
- 例2：11.0 | 40.0 | 19.0 | 43.0 | 39.0
- 例3：12743.0 | 1110.0 | 9990.0 | 4190.0 | 3590.0

## g0015 — sotab_v2：元の種類 `Number`（6,853 列）
- 例1：3.667 | 4.286 | 5.0 | 4.834 | 4.3
- 例2：5
- 例3：5.0 | 4.75 | 4.5 | 4.67 | 4.0

## g0016 — wikidbs10k：見出し「has part(s)」（Wikidata の型 `wikibase-entityid`）（6,559 列）
- 例1：Alpha/beta hydrolase fold-3 | PPE family, C-terminal | Aspartic peptidase, active site | NHL repeat | PE-PGRS family, N-terminal（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, encoded by）
- 例2：Alpha/beta hydrolase fold-3 | PPE family, C-terminal | NHL repeat | Aspartic peptidase, active site | PE-PGRS family, N-terminal（表：encodes／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, encoded by）
- 例3：DNA polymerase III, beta sliding clamp,… | DNA polymerase III, beta sliding clamp,… | DNA polymerase III, beta sliding clamp,…（表：DNA polymerase III, beta sliding clamp,…／同じ表の列：label, description, UniProt protein ID, found in taxon, RefSeq protein ID, encoded by）

## g0017 — wikidbs10k：見出し「locator map image」（Wikidata の型 `string`）（6,488 列）
- 例1：MEX orthographic.svg | California in United States.svg | Multnomah County Oregon Incorporated an… | Montreal au Quebec.png | Map of California highlighting Los Ange…（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Localització de Corbins respecte del Se… | Localització de Soses respecte del Segr… | Lérida OSM 01.png | Localització d'Alfés respecte del Segri… | Localització de la Portella respecte de…（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, coordinate location）
- 例3：Localització d'Algerri respecte de la N… | Localització de Menàrguens respecte de … | Localització de Torregrossa respecte de… | Lérida OSM 01.png | Localització de Torres de Segre respect…（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0018 — wikidbs10k：見出し「official website」（Wikidata の型 `string`）（6,480 列）
- 例1：https://www.theamas.com | https://www.univision.com/especiales/pr… | https://www.latingrammy.com/en | http://doveawards.com | http://www.cmaworld.com/（表：part／同じ表の列：label, description, instance of, topic's main catego…, Freebase ID, country）
- 例2：https://nv.gov/ | http://www.townplymouth.com | http://www.SheboyganCounty.com | http://www.cdmx.gob.mx | http://en.presidencia.gob.mx/（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例3：http://www.ccnoguera.cat/algerri/ | http://www.torrefarrera.cat | https://albatarrec.cat/ | http://www.alcoletge.cat | https://www.paeria.cat/（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）

## g0019 — wikidbs10k：見出し「uniprot protein id」（Wikidata の型 `string`）（6,432 列）
- 例1：Q79FK4 | Q79FJ9 | I6Y2J4 | Q79FP0 | Q6MWV6（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：label, description, subclass of, found in taxon, encoded by, has part(s)）
- 例2：Q79FL8 | I6XHM5 | P9WIF1 | I6YG87 | Q6MWW9（表：encodes／同じ表の列：label, description, subclass of, found in taxon, encoded by, has part(s)）
- 例3：Q87TQ6 | A0A0H3E9Z5 | Q8A810 | Q9JXS8 | A6GYK6（表：DNA polymerase III, beta sliding clamp,…／同じ表の列：label, description, found in taxon, RefSeq protein ID, encoded by, subclass of）

## g0020 — wikidbs10k：見出し「encoded by」（Wikidata の型 `wikibase-entityid`）（6,422 列）
- 例1：PE-PGRS family protein PE_PGRS35 Rv1983 | PE-PGRS family protein PE_PGRS14 Rv0834c | PE-PGRS family protein PE_PGRS46 Rv2634c | PE family protein PE14 Rv1214c | PE-PGRS family protein PE_PGRS12 Rv0832（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, has part(s)）
- 例2：PE family protein PE7 Rv0916c | PE-PGRS family protein PE_PGRS19 Rv1067c | PE family protein PE5 Rv0285 | PE-PGRS family protein PE_PGRS35 Rv1983 | lipase LipX Rv1169c（表：encodes／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, has part(s)）
- 例3：DNA polymerase III subunit beta BN117_4… | DNA polymerase III subunit beta SSUBM40… | DNA polymerase III subunit beta tll2349 | DNA polymerase III subunit beta AMED_00… | DNA polymerase III subunit beta MSMEG_0…（表：DNA polymerase III, beta sliding clamp,…／同じ表の列：label, description, UniProt protein ID, found in taxon, RefSeq protein ID, subclass of）

## g0021 — wikidbs10k：見出し「refseq protein id」（Wikidata の型 `string`）（6,402 列）
- 例1：YP_177710 | YP_177759 | YP_177794 | NP_301390 | YP_177847（表：PE-PGRS family, N-terminal domain, prot…／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, encoded by）
- 例2：NP_301390 | YP_177867 | YP_177749 | YP_178019 | YP_177792（表：encodes／同じ表の列：label, description, UniProt protein ID, subclass of, found in taxon, encoded by）
- 例3：YP_053242 | YP_405579 | YP_169085 | NP_869246 | YP_002247870（表：DNA polymerase III, beta sliding clamp,…／同じ表の列：label, description, UniProt protein ID, found in taxon, encoded by, subclass of）

## g0022 — wikidbs10k：見出し「area」（Wikidata の型 `quantity`）（6,236 列）
- 例1：+12308 | +423970.0 | +1972550 | 286380.0 | 213.58732200000003（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：8.5 | 5.9 | 20.5 | 21.6 | +37.60（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例3：20.3 | 66.9 | 8.5 | 21.0 | 212.3（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0023 — sotab_v2：元の種類 `Duration`（5,887 列）
- 例1：1 hour | Duration: 1 hour | Duration: 1 hour and 3 minutes
- 例2：PD1TH0M0
- 例3：P[0]-[0]-[0]T[23]:[0]:[59] | P[0]-[0]-[0]T[6]:[0]:[0] | P[0]-[0]-[3]T[3]:[0]:[0] | P[0]-[0]-[4]T[23]:[0]:[59] | P[0]-[0]-[4]T[3]:[0]:[0]

## g0024 — wikidbs10k：見出し「population」（Wikidata の型 `quantity`）（5,827 列）
- 例1：781 | 1109 | 1890 | 2217 | 300（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：3040 | 1890 | 1109 | 774 | 240（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：+800653 | +284293 | +668405 | +52984 | +73969（表：place of birth／同じ表の列：label, description, Commons category, country, image, located in the admi…）

## g0025 — wikidbs10k：見出し「viaf id」（Wikidata の型 `string`）（5,617 列）
- 例1：155934080.0 | 141907131 | 133677400 | 154775570 | 133225995（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：316734846.0 | 277069272 | 158499941.0 | 137213896 | 316734354.0（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例3：316733637.0 | 316874718.0 | 316735300.0 | 146629031.0 | 155902283.0（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0026 — sotab_v2：元の種類 `DateTime`（5,420 列）
- 例1：2018-01-03 13:41:56 | 2020-09-01 14:19:06 | 2014-04-02 15:33:56 | 2015-04-01 12:45:05 | 2017-04-10 11:55:56（DBpedia：dateTime）
- 例2：4/16/2013 1:54:00 PM | 6/26/2012 12:57:00 PM | 7/8/2019 2:29:00 PM | 10/24/2012 1:19:00 PM | 10/10/2011 5:17:00 PM（DBpedia：dateTime）
- 例3：2017-02-13T23:00:00Z | 2018-11-20T23:00:00Z | 2014-09-10T22:00:00Z | 1984-04-30T22:00:00Z | 2011-06-02T22:00:00Z（DBpedia：dateTime）

## g0027 — sotab_v2：元の種類 `Mass`（4,778 列）
- 例1：38 g | 20 g | 8 g | 41 g | 60 g（DBpedia：mass）
- 例2：39 milligrams cholesterol | 8 milligrams cholesterol | 4 milligrams cholesterol | 140 milligrams cholesterol | 59 milligrams cholesterol（DBpedia：mass）
- 例3：16 g | 34 g | 13 g | 10 g | 3 g（DBpedia：mass）

## g0028 — wikidbs10k：見出し「shares border with」（Wikidata の型 `wikibase-entityid`）（4,675 列）
- 例1：Manitowoc County | Urban agglomeration of Longueuil | Morelos | California | Bellflower（表：administrative territorial entity／同じ表の列：label, description, country, flag image, Commons category, coordinate location）
- 例2：Maials | Alfés | Torregrossa | Llardecans | Massalcoreig（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例3：Albesa | Serós | Aitona | Alguaire | Gimenells i el Pla de la Font（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0029 — wikidbs10k：見出し「molecular function」（Wikidata の型 `wikibase-entityid`）（4,618 列）
- 例1：nucleotidyltransferase activity | transferase activity | DNA binding | 3'-5' exonuclease activity | DNA-directed DNA polymerase activity（表：DNA polymerase III, beta sliding clamp,…／同じ表の列：label, description, UniProt protein ID, found in taxon, RefSeq protein ID, encoded by）
- 例2：nucleotide binding | phosphatidylinositol phosphate kinase a… | ATP binding | calcium ion binding | transferase activity（表：Phosphatidylinositol-4-phosphate 5-kina…／同じ表の列：label, description, Ensembl protein ID, encoded by, UniProt protein ID, biological process）
- 例3：calcium ion binding | nucleotide binding | transferase activity | ATP binding（表：encodes／同じ表の列：label, description, found in taxon, UniProt protein ID, encoded by, RefSeq protein ID）

## g0030 — wikidbs10k：見出し「biological process」（Wikidata の型 `wikibase-entityid`）（4,441 列）
- 例1：DNA replication | DNA biosynthetic process | nucleic acid phosphodiester bond hydrol…（表：DNA polymerase III, beta sliding clamp,…／同じ表の列：label, description, UniProt protein ID, found in taxon, RefSeq protein ID, encoded by）
- 例2：protein localization | phosphatidylinositol phosphate biosynth… | fibroblast migration | megakaryocyte development | phosphatidylinositol metabolic process（表：Phosphatidylinositol-4-phosphate 5-kina…／同じ表の列：label, description, Ensembl protein ID, encoded by, UniProt protein ID, molecular function）
- 例3：phosphorylation | phosphatidylinositol metabolic process | endocytosis | phosphatidylinositol phosphate biosynth… | regulation of autophagy（表：encodes／同じ表の列：label, description, found in taxon, UniProt protein ID, encoded by, RefSeq protein ID）

## g0031 — wikidbs10k：見出し「entrez gene id」（Wikidata の型 `string`）（4,438 列）
- 例1：909139 | 885988 | 885730 | 885921 | 886745（表：encoded by／同じ表の列：label, description, NCBI locus tag, found in taxon, subclass of, encodes）
- 例2：1799546 | 3252571 | 879244 | 3092204 | 11636964（表：encoded by／同じ表の列：label, description, found in taxon, subclass of, encodes, NCBI locus tag）
- 例3：116723.0 | 37356.0 | 79837.0 | 117150.0 | 560360.0（表：encoded by／同じ表の列：label, description, HomoloGene ID, RefSeq RNA ID, ortholog, encodes）

## g0032 — wikidbs10k：見出し「genomic end」（Wikidata の型 `string`）（4,429 列）
- 例1：2944984 | 1607971 | 1619683 | 1992576 | 336309（表：encoded by／同じ表の列：label, description, NCBI locus tag, Entrez Gene ID, found in taxon, subclass of）
- 例2：272657 | 496115 | 2448212 | 2843 | 4341（表：encoded by／同じ表の列：label, description, found in taxon, Entrez Gene ID, subclass of, encodes）
- 例3：32473794.0 | 95106930.0 | 130693076.0 | 23003484.0 | 24533236.0（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, ortholog）

## g0033 — wikidbs10k：見出し「genomic start」（Wikidata の型 `string`）（4,429 列）
- 例1：1561463 | 2087970 | 1301754 | 2061177 | 1339002（表：encoded by／同じ表の列：label, description, NCBI locus tag, Entrez Gene ID, found in taxon, subclass of）
- 例2：1545 | 1325852 | 1799 | 1925 | 1676（表：encoded by／同じ表の列：label, description, found in taxon, Entrez Gene ID, subclass of, encodes）
- 例3：2398843.0 | 5358522.0 | 10892465.0 | 151197949.0 | 130683158.0（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, ortholog）

## g0034 — wikidbs10k：見出し「strand orientation」（Wikidata の型 `wikibase-entityid`）（4,428 列）
- 例1：reverse strand | forward strand（表：encoded by／同じ表の列：label, description, NCBI locus tag, Entrez Gene ID, found in taxon, subclass of）
- 例2：forward strand | reverse strand（表：encoded by／同じ表の列：label, description, found in taxon, Entrez Gene ID, subclass of, encodes）
- 例3：forward strand | reverse strand（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, ortholog）

## g0035 — wikidbs10k：見出し「encodes」（Wikidata の型 `wikibase-entityid`）（4,425 列）
- 例1：PE-PGRS family protein PE_PGRS31 Rv1768 | Hypothetical PE family protein MAB_2231c | PE-PGRS family protein PE_PGRS40 Rv2371 | PE-PGRS family protein PE_PGRS3 Rv0278c | PE-family protein ML0538（表：encoded by／同じ表の列：label, description, NCBI locus tag, Entrez Gene ID, found in taxon, subclass of）
- 例2：DNA polymerase III subunit beta XCC0002 | DNA polymerase III subunit beta ECL_000… | DNA polymerase III subunit beta Taci_00… | DNA polymerase III subunit beta AHA_0002 | DNA polymerase III subunit beta gvip446（表：encoded by／同じ表の列：label, description, found in taxon, Entrez Gene ID, subclass of, NCBI locus tag）
- 例3：Phosphatidylinositol-4-phosphate 5-kina… | Phosphatidylinositol-5-phosphate 4-kina… | phosphatidylinositol-4-phosphate 5-kina… | Phosphatidylinositol-5-phosphate 4-kina… | Phosphatidylinositol-5-phosphate 4-kina…（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, ortholog）

## g0036 — wikidbs10k：見出し「parent taxon」（Wikidata の型 `wikibase-entityid`）（4,374 列）
- 例1：Chloroflexus aurantiacus | Legionella pneumophila | Mesoplasma florum | Neisseria meningitidis | Pseudomonas putida（表：natural product／同じ表の列：label, description, taxon name, NCBI taxonomy ID, instance of, Gram staining）
- 例2：Deinococcus radiodurans | Enterococcus faecium | Streptococcus mutans | Chloroflexus aurantiacus | Mycobacterium smegmatis（表：natural product／同じ表の列：label, description, taxon name, instance of, NCBI taxonomy ID, Gram staining）
- 例3：Shewanella oneidensis | Mesorhizobium ciceri | Aeromonas hydrophila | Pseudomonas syringae | Rhodospirillum rubrum（表：natural product／同じ表の列：label, description, taxon name, instance of, NCBI taxonomy ID, Gram staining）

## g0037 — wikidbs10k：見出し「ncbi taxonomy id」（Wikidata の型 `string`）（4,338 列）
- 例1：243090 | 169963 | 194439 | 167539 | 362948（表：natural product／同じ表の列：label, description, taxon name, parent taxon, instance of, Gram staining）
- 例2：402612 | 243275 | 210007 | 83332 | 233413（表：natural product／同じ表の列：label, description, taxon name, instance of, parent taxon, Gram staining）
- 例3：312309 | 160488 | 269796 | 223283 | 380703（表：natural product／同じ表の列：label, description, taxon name, instance of, parent taxon, Gram staining）

## g0038 — sotab_v2：元の種類 `URL`（4,259 列）
- 例1：files/assets/cover300.jpg | /files/assets/cover300.jpg
- 例2：files/assets/cover300.jpg
- 例3：http://7thheaven.nl/foto/download/novem… | http://7thheaven.nl/foto/download/Oktob… | http://7thheaven.nl/foto/download/janua… | http://7thheaven.nl/foto/download/aug16… | http://7thheaven.nl/foto/download/mei16…

## g0039 — sotab_v2：元の種類 `MusicAlbum/name`（4,171 列）
- 例1：Change Me As We Go | https://23rdhr.com/album/467550/perfect… | Home for the Holidays | Perfect Strangers | Singles
- 例2：Justin Moore | A Classical Mood | Public Publication (EP) | Double Live | Super Dude I
- 例3：What If It Does - Single | Bad With Me | 4th + Main EP | Imagine This Christmas - Single | Imagine This Christmas - EP

## g0040 — wikidbs10k：見出し「located in time zone」（Wikidata の型 `wikibase-entityid`）（4,142 列）
- 例1：Eastern Time Zone | UTC+10:00 | UTC−08:00 | Central Time Zone | UTC−07:00（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Central Time Zone | China Standard Time | UTC+07:00 | UTC+04:00 | UTC+03:00（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：UTC+02:00 | UTC−01:00 | Central European Time | UTC−06:00 | UTC+01:00（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0041 — sotab_v2：元の種類 `ItemAvailability`（4,071 列）
- 例1：https://schema.org/OnlineOnly
- 例2：Awaiting stock. | Delivery Usually In 5-10 Working Days | Delivery usually in 2-6 working days. | Delivery Usually In 6-15 Working Days | Not currently available.
- 例3：OutOfStock | InStock

## g0042 — sotab_v2：元の種類 `MusicRecording/name`（3,913 列）
- 例1：The End Of The World | The Submarine (Chapter 1) | This Is Ponderous | A Father's Day | The Magnificent Tree
- 例2：Ninja Papes // 4.13.20 | Ninja Papes - Lockdown UKG (pt. 2) 2020 | Ninja Papes @ 2ST // 1.28.2020 | Ninja Papes 7.24.19 // 2Step Tuesdays | Ninja Papes @ 2StepTues // 10.01.19
- 例3：Inhuman | Bright Eyes | Alternative Facts | The Day You Dreamed | Punk Rock Fight Song (For Telly)

## g0043 — wikidbs10k：見出し「follows」（Wikidata の型 `wikibase-entityid`）（3,867 列）
- 例1：2028 Japanese Badminton Championships | 1966 Japanese Badminton Championships | 2020 Japanese Badminton Championships | 1990 Japanese Badminton Championships | 1960 Japanese Badminton Championships（表：Japanese Badminton Championships／同じ表の列：label, description, sport, country, point in time, followed by）
- 例2：2018 Japanese Badminton Championships | 1983 Japanese Badminton Championships | 1948 Japanese Badminton Championships | 1975 Japanese Badminton Championships | 2027 Japanese Badminton Championships（表：followed by／同じ表の列：label, description, sport, country, point in time, followed by）
- 例3：2020 Japanese Badminton Championships | 1966 Japanese Badminton Championships | 1982 Japanese Badminton Championships | 1968 Japanese Badminton Championships | 2008 Japanese Badminton Championships（表：follows／同じ表の列：label, description, sport, country, point in time, followed by）

## g0044 — wikidbs10k：見出し「followed by」（Wikidata の型 `wikibase-entityid`）（3,848 列）
- 例1：2024 Japanese Badminton Championships | 2000 Japanese Badminton Championships | 2020 Japanese Badminton Championships | 1982 Japanese Badminton Championships | 1978 Japanese Badminton Championships（表：Japanese Badminton Championships／同じ表の列：label, description, sport, country, point in time, follows）
- 例2：1974 Japanese Badminton Championships | 1996 Japanese Badminton Championships | 1993 Japanese Badminton Championships | 2014 Japanese Badminton Championships | 2001 Japanese Badminton Championships（表：followed by／同じ表の列：label, description, sport, country, point in time, follows）
- 例3：1961 Japanese Badminton Championships | 2001 Japanese Badminton Championships | 2030 Japanese Badminton Championships | 1975 Japanese Badminton Championships | 2029 Japanese Badminton Championships（表：follows／同じ表の列：label, description, sport, country, point in time, follows）

## g0045 — sotab_v2：元の種類 `IdentifierAT`（3,783 列）
- 例1：9788833350130.0 | 9789953892047.0 | 9789933352257.0 | 9789922901350.0 | 9789933351144.0
- 例2：9781469233017.0 | 9780060552930.0 | 9781504654791.0 | 9780967529301.0 | 9781840187076.0
- 例3：9789384625979.0 | 9780684860473.0 | 9780593064030.0 | 9780670919536.0 | 9780141988511.0

## g0046 — sotab_v2：元の種類 `Event/name`（3,705 列）
- 例1：Washington Nationals vs. Philadelphia P… | Washington Nationals vs. Philadelphia P… | Washington Nationals vs. Milwaukee Brew… | Washington Nationals vs. Milwaukee Brew… | Washington Nationals vs. Miami Marlins …
- 例2：My Best Friend’s Wedding the Musical st… | Cock Sparrer at The Fleece in Bristol o… | Ross Noble: Humournoid at The Bristol H… | The House Magicians Comedy and Magic Sh… | Dick Whittington at The Bristol Hippodr…
- 例3：2021 ICMA Annual Conference - Portland/… | 3CMA Webinar - Social Media Management … | ICMA Annual Conference - Nashville/Davi… | 3CMA Keynote Webinar | Never Let a Good… | Savannah/Chatham County, GA Regional Co…

## g0047 — wikidbs10k：見出し「library of congress authority id」（Wikidata の型 `string`）（3,677 列）
- 例1：n79086863 | n78095330 | n50046728 | n50061223 | n80132975（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：n79021528 | n80070818 | n79023005 | n81017756 | n79049551（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：sh85054594 | n80061791 | n78085423 | n79131071 | n79039880（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0048 — wikidbs10k：見出し「gram staining」（Wikidata の型 `wikibase-entityid`）（3,673 列）
- 例1：Gram-negative bacteria | gram-positive bacteria（表：natural product／同じ表の列：label, description, taxon name, parent taxon, NCBI taxonomy ID, instance of）
- 例2：gram-positive bacteria | Gram-negative bacteria（表：natural product／同じ表の列：label, description, taxon name, instance of, parent taxon, NCBI taxonomy ID）
- 例3：Gram-negative bacteria（表：natural product／同じ表の列：label, description, taxon name, instance of, parent taxon, NCBI taxonomy ID）

## g0049 — sotab_v2：元の種類 `addressLocality`（3,662 列）
- 例1：Berlin
- 例2：Niagara Falls
- 例3：Wethersfield | Niantic | Bloomfield | Hamden | Avon

## g0050 — wikidbs10k：見出し「worldcat identities id」（Wikidata の型 `string`）（3,639 列）
- 例1：lccn-n79007500 | lccn-n80046731 | lccn-n79055157 | lccn-n79100226 | lccn-n78095330（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：viaf-235482277 | lccn-n81035836 | lccn-n79007233 | lccn-n79054515 | lccn-n79021528（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：lccn-n78085423 | lccn-n79006404 | lccn-n79054515 | lccn-n79021783 | viaf-127412899（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0051 — wikidbs10k：見出し「national library of israel j9u id」（Wikidata の型 `string`）（3,463 列）
- 例1：987007269139705171 | 9.870075526534052e+17 | 987007559520305171 | 9.870075618047052e+17 | 9.870075501923052e+17（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：987007554807405171 | 987007550348505171 | 987007561817905171 | 987007564354705171 | 987007564232105171（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：987007564238105171 | 987007564231005171 | 987007564324405171 | 987007554897405171 | 987007565251505171（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0052 — sotab_v2：元の種類 `addressRegion`（3,331 列）
- 例1：CT | Connecticut
- 例2：New York | Washington | California | Michigan | Oregon
- 例3：Nevada | Florida | Québec | Grand Est | Hauts-de-France

## g0053 — sotab_v2：元の種類 `weight`（3,320 列）
- 例1：Weight
- 例2：140 - 160 lbs [60 - 70 kg] | 100 - 120 lbs [46 - 55 kg] | 90 - 100 lbs [40 - 45 kg] | 180 - 200 lbs [80 - 90 kg] | 200 - 225 lbs [90 - 100 kg]
- 例3：182 lb (83 kg) | 176 lb (80 kg) | 138 lb (63 kg) | 94 lb (43 kg) | 127 lb (58 kg)

## g0054 — wikidbs10k：見出し「capital」（Wikidata の型 `wikibase-entityid`）（3,310 列）
- 例1：Buenos Aires | San Juan | Tunis | Sucre | Belmopan（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Amsterdam | Ljubljana | Pyongyang | Washington, D.C. | Tehran（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Palermo | Lisbon | Tobruk | Thessaloniki | Poznań（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, Commons category, country, coordinate location）

## g0055 — sotab_v2：元の種類 `Country`（3,297 列）
- 例1：United States of America
- 例2：Oklahoma City, OK | Ottawa, Ontario | US | Albuquerque, New Mexico | South San Francisco, California
- 例3：FR | US | CA

## g0056 — wikidbs10k：見出し「gnd id」（Wikidata の型 `string`）（3,276 列）
- 例1：4039058-5 | 4040188-1 | 4003900-6 | 5006497-6 | 1029167966（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：4042203-3 | 4078541-5 | 4055964-6 | 4012694-8 | 4014499-9（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：4027833-5 | 4058794-0 | 4022153-2 | 4042203-3 | 4078704-7（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, category of associa…, emergency phone num…）

## g0057 — sotab_v2：元の種類 `Organization`（3,251 列）
- 例1：Olive Ann Burns | Kenneth Roberts | Deborah Levy Tom McCarthy | Diane Chamberlain | Leslie Householder（DBpedia：Organisation）
- 例2：Bram Stoker | James P. Kraft | Barbara Freethy | Linda Lael Miller | Robyn Donald（DBpedia：Organisation）
- 例3：Brooke McGlothlin Cliff Graham | William Bottrell | Norah Hérols | Paul Jacobs Saul Landau | Maureen Ogle（DBpedia：Organisation）

## g0058 — wikidbs10k：見出し「inaturalist place id」（Wikidata の型 `string`）（3,249 列）
- 例1：8228 | 6944 | 7352 | 7161 | 8858（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：7305 | 8147 | 7506 | 6857 | 7312（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：2927 | 13489 | 744 | 1070 | 618（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）

## g0059 — wikidbs10k：見出し「coat of arms image」（Wikidata の型 `string`）（3,219 列）
- 例1：Escut d'Artesa de Lleida.svg | Escut de Torregrossa.svg | Escut d'Albatàrrec.svg | Escut de Vilanova de Segrià.svg | Escut de Llardecans.svg（表：jurisdiction／同じ表の列：label, description, country, postal code, locator map image, coordinate location）
- 例2：Escut d'Alcarràs.svg | Escut de Llardecans.svg | Escut d'Alguaire.svg | Escut d'Algerri.svg | Escut de Vilanova de Segrià.svg（表：political border／同じ表の列：label, description, Commons category, country, postal code, coordinate location）
- 例3：Royal Coat of Arms of Canada.svg | Emblem of Uzbekistan.svg | Coat of arms of the Commonwealth of Pue… | Coat of arms of the Dominican Republic.… | Coat of arms of Latvia.svg（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0060 — wikidbs10k：見出し「ncbi locus tag」（Wikidata の型 `string`）（3,187 列）
- 例1：Rv0335c | ML2534 | Rv1646 | Rv0742 | Rv1651c（表：encoded by／同じ表の列：label, description, Entrez Gene ID, found in taxon, subclass of, encodes）
- 例2：STM3837 | SPy_0003 | XCC0002 | Dtur_1551 | NGR_c36750（表：encoded by／同じ表の列：label, description, found in taxon, Entrez Gene ID, subclass of, encodes）
- 例3：AMED_0011 | DVU2875 | BT_4547 | BT_1944 | BN117_2222（表：encoded by／同じ表の列：label, description, subclass of, found in taxon, Entrez Gene ID, encodes）

## g0061 — wikidbs10k：見出し「native label」（Wikidata の型 `monolingualtext`）（3,180 列）
- 例1：Denver County | United States of America | Queensland | Portland | México（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Hilari | Josep Antoni | Albert | María | Sebastià（表：given name／同じ表の列：label, description, instance of, writing system, language of work or…, said to be the same…）
- 例3：United States of America | Lietuva | Монгол Улс | Suid-Afrika | República Argentina（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0062 — wikidbs10k：見出し「cell component」（Wikidata の型 `wikibase-entityid`）（3,150 列）
- 例1：cytoplasm | DNA polymerase III complex（表：DNA polymerase III, beta sliding clamp,…／同じ表の列：label, description, UniProt protein ID, found in taxon, RefSeq protein ID, encoded by）
- 例2：cytoplasm | nucleus | cytosol | cell projection | mRNA cleavage and polyadenylation speci…（表：encodes／同じ表の列：label, description, found in taxon, UniProt protein ID, encoded by, RefSeq protein ID）
- 例3：cytoplasm | cellular component | cell junction | transcription regulator complex | RNA polymerase II transcription regulat…（表：MAD homology 1, Dwarfin-type, protein f…／同じ表の列：label, description, UniProt protein ID, Ensembl protein ID, molecular function, biological process）

## g0063 — sotab_v2：元の種類 `priceRange`（3,058 列）
- 例1：$104 - $279
- 例2：$100-$2,000
- 例3：$100-$25,000

## g0064 — sotab_v2：元の種類 `Book/name`（2,928 列）
- 例1：Blink | A Bíblia de Vendas | Marketing para Negócios de Sucesso | The Sleep Revolution | A Venda Desafiadora
- 例2：è Liquor || ↠ PDF Read by ☆ Poppy Z. Br… | Unlimited [Fiction Book] ☆ Once Upon a … | Best Download [Antony John] ñ Thou Shal… | ✓ The Good Earth || Ã PDF Download by ↠… | ☆ Zombie-Loan, Vol. 1 || ☆ PDF Download…
- 例3：Depression | Hermann Cohen | Demian | Gouden Daden | A Knight of the Seven Kingdoms

## g0065 — wikidbs10k：見出し「archinform location id」（Wikidata の型 `string`）（2,913 列）
- 例1：18415.0 | 2966 | 3109.0 | 1217.0 | 3058（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：2974 | 3053 | 3328 | 3056 | 2986（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：3010 | 3038 | 2983 | 3055 | 3043（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0066 — wikidbs10k：見出し「quora topic id」（Wikidata の型 `string`）（2,894 列）
- 例1：Cleveland-OH | Mexico | Australia | Mexico-City-4 | Montréal-QC-Canada（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Antigua-and-Barbuda | Chile | Eritrea | Venezuela | Uzbekistan（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：The-United-States-of-America | Sweden | West-Germany | Nazi-Germany | Russia（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0067 — wikidbs10k：見出し「sport」（Wikidata の型 `wikibase-entityid`）（2,806 列）
- 例1：auto racing | formula racing（表：2004 Champ Car season／同じ表の列：label, description, point in time, instance of, country, pole position）
- 例2：badminton（表：Japanese Badminton Championships／同じ表の列：label, description, country, point in time, followed by, follows）
- 例3：badminton（表：followed by／同じ表の列：label, description, country, point in time, followed by, follows）

## g0068 — sotab_v2：元の種類 `category`（2,762 列）
- 例1：primary
- 例2：primary
- 例3：primary

## g0069 — sotab_v2：元の種類 `Movie/name`（2,597 列）
- 例1：Filmage: The Story of Descendents/All | Mission Istaanbul | Dante's Inferno: An Animated Epic | These Amazing Shadows | Street Society
- 例2：Millennial Killer (2020) | Climax (2020) | The Screaming Silent (2020) | Overnight (2020) | La rivincita (2020)
- 例3：В 6 часов вечера после войны | Последний самурай | Укрощение строптивого | Унесенные ветром | Илья Муромец

## g0070 — sotab_v2：元の種類 `Product/name`（2,583 列）
- 例1：Resin and Iron | Iron-Birchwood | Stainless Steel | Steel And Crystal | Wrought Iron-Wood
- 例2：Prospector XL | 2B Ice Decal - Black | 2B Ice Decal - White | Fast Draw | 2B Hoodie
- 例3：Angus Boots | Little Blue Lamb - Blue Mary Jane Baby … | Mason Shoe | Little Blue Lamb - Pink Boot | Little Blue Lamb - Fleece Boot

## g0071 — wikidbs10k：見出し「encyclopædia britannica online id」（Wikidata の型 `string`）（2,505 列）
- 例1：place/Queensland-state-Australia | place/Long-Beach-California | place/California-state | place/Nevada-state | place/West-Allis（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：place/Croatia | place/Greece | place/Thailand | place/Spain | place/Barbados（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：place/Byzantine-Empire | place/Tunisia | place/Czech-Republic | place/Portugal | place/Syria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0072 — wikidbs10k：見出し「elevation above sea level」（Wikidata の型 `quantity`）（2,476 列）
- 例1：199.0 | 2250.0 | 30.0 | 222.0 | 152.0（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：259 | 252 | 202 | 197 | 137（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例3：237 | 119 | 196 | 258 | 147（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0073 — sotab_v2：元の種類 `postalCode`（2,376 列）
- 例1：6109 | 9955 | 6489 | 6519 | 6010
- 例2：48458 | 74006 | 19464 | 74146 | 74301
- 例3：68000 | 89109 | 33635 | 60210 | G1X 4S6

## g0074 — sotab_v2：元の種類 `LocalBusiness/name`（2,315 列）
- 例1：HomeServe USA | Liberty Home Guard | The Home Service Club | Endurance Home Warranty | AFC Home Club
- 例2：247Customerservicenumber
- 例3：3-D Bail Bonds, Inc. | 3-D Bail Bonds, Inc | 3-D Bail Bonds | 3-D Bail Bonds Niantic CT | 3-D Bail Bonds Wethersfield CT

## g0075 — wikidbs10k：見出し「flag image」（Wikidata の型 `string`）（2,298 列）
- 例1：Flag of California.svg | Flag of Montreal.svg | Flag of Mexico.svg | Flag of Nuevo Leon.svg | Flag of Australia (converted).svg（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, Commons category, coordinate location）
- 例2：Flag of Bulgaria.svg | Flag of Greece.svg | Flag of Canada (Pantone).svg | Flag of Romania.svg | Flag of the Czech Republic.svg（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Flag of the Czech Republic.svg | Flag of the United Kingdom (3-5).svg | Flag of Hungary.svg | Flag of Luxembourg.svg | Flag of Tunisia.svg（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0076 — wikidbs10k：見出し「nkcr aut id」（Wikidata の型 `string`）（2,257 列）
- 例1：ge131211 | ge129703 | ge134148 | ge128512 | ge130064（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：ge131496 | ge131576 | ge129895 | ge128525 | ge128576（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：ge128882 | ge131168 | ge131211 | ge130512 | ge128695（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0077 — wikidbs10k：見出し「genbank assembly accession number」（Wikidata の型 `string`）（2,219 列）
- 例1：GCA_000091545.1 | GCA_000299455.1 | GCA_000027305.1 | GCA_000006965.1 | GCA_000008485.1（表：natural product／同じ表の列：label, description, taxon name, parent taxon, NCBI taxonomy ID, instance of）
- 例2：GCA_000009925.1 | GCA_000024905.1 | GCA_000203835.1 | GCA_000146165.2 | GCA_000240185.2（表：natural product／同じ表の列：label, description, taxon name, instance of, parent taxon, NCBI taxonomy ID）
- 例3：GCA_000014805.1 | GCA_000007765.2 | GCA_000185905.1 | GCA_000012245.1 | GCA_000007565.2（表：natural product／同じ表の列：label, description, taxon name, instance of, parent taxon, NCBI taxonomy ID）

## g0078 — wikidbs10k：見出し「exact match」（Wikidata の型 `string`）（2,208 列）
- 例1：http://purl.obolibrary.org/obo/GO_00464… | http://purl.obolibrary.org/obo/GO_00468… | http://purl.obolibrary.org/obo/GO_00081… | http://purl.obolibrary.org/obo/GO_00358… | http://purl.obolibrary.org/obo/GO_00068…（表：biological process／同じ表の列：label, description, Gene Ontology ID, subclass of, instance of）
- 例2：http://purl.obolibrary.org/obo/GO_00052… | http://purl.obolibrary.org/obo/GO_00080… | http://purl.obolibrary.org/obo/GO_00428… | http://purl.obolibrary.org/obo/GO_00310… | http://purl.obolibrary.org/obo/GO_00510…（表：molecular function／同じ表の列：label, description, Gene Ontology ID, subclass of, instance of）
- 例3：http://purl.obolibrary.org/obo/GO_00021… | http://purl.obolibrary.org/obo/GO_00001… | http://purl.obolibrary.org/obo/GO_00190… | http://purl.obolibrary.org/obo/GO_00015… | http://purl.obolibrary.org/obo/GO_00082…（表：biological process／同じ表の列：label, description, Gene Ontology ID, subclass of, instance of）

## g0079 — wikidbs10k：見出し「page banner」（Wikidata の型 `string`）（2,172 列）
- 例1：Losangeles skyline banner.jpg | Portland rose test gardens banner.jpg | Antelope Valley banner.jpg | Red Rock Canyon, Nevada banner.jpg | Monterey county banner Bixby Creek Brid…（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Capela Das Almas Oporto Banner.jpg | Uluru-Kata Tjuta banner Uluru Sunset.jpg | Eritrea banner Eritrean railway bridge.… | Turkey banner Suleymaniye Mosque.jpg | Czech Republic WV banner.jpg（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Kompsatos river bridge, Thrace.jpg | Palmyra banner 2.jpg | Ötlingen - Panoramaansicht klein banner… | Malta Valletta banner.jpg | Egypt banner Camels and pyramids.jpg（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0080 — wikidbs10k：見出し「described by source」（Wikidata の型 `wikibase-entityid`）（2,119 列）
- 例1：Vlastenský slovník historický | Sytin Military Encyclopedia | Brockhaus and Efron Encyclopedic Dictio… | Larousse Encyclopedia online | Ottův slovník naučný（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Encyclopædia Britannica 11th edition | Catholic Encyclopedia | Real'nyj slovar' klassicheskih drevnost… | Bible Encyclopedia of Archimandrite Nic… | Vlastenský slovník historický（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Brockhaus and Efron Encyclopedic Dictio… | Svensk uppslagsbok | Armenian Soviet Encyclopedia | Great Soviet Encyclopedia (1969–1978) | The Nuttall Encyclopædia（表：eponym／同じ表の列：label, description, Freebase ID, instance of, topic's main catego…, Library of Congress…）

## g0081 — wikidbs10k：見出し「category for maps」（Wikidata の型 `wikibase-entityid`）（2,102 列）
- 例1：Category:Maps of Los Angeles County, Ca… | Category:Maps of Mexico City | Category:Maps of Montreal | Category:Maps of Nevada | Category:Maps of California（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Category:Maps of Italy | Category:Maps of Venezuela | Category:Maps of Estonia | Category:Maps of Poland | Category:Maps of Switzerland（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Category:Maps of Syria | Category:Maps of Libya | Category:Maps of Finland | Category:Maps of Yugoslavia | Category:Maps of Malta（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0082 — wikidbs10k：見出し「on focus list of wikimedia project」（Wikidata の型 `wikibase-entityid`）（1,993 列）
- 例1：WikiProject Badminton/tournament focus …（表：Japanese Badminton Championships／同じ表の列：label, description, sport, country, point in time, followed by）
- 例2：WikiProject Badminton/tournament focus …（表：followed by／同じ表の列：label, description, sport, country, point in time, followed by）
- 例3：WikiProject Badminton/tournament focus …（表：follows／同じ表の列：label, description, sport, country, point in time, followed by）

## g0083 — wikidbs10k：見出し「taxon rank」（Wikidata の型 `wikibase-entityid`）（1,989 列）
- 例1：genus | pathovar | species（表：taxon／同じ表の列：label, description, parent taxon, taxon name, instance of, Freebase ID）
- 例2：species（表：taxon／同じ表の列：label, description, taxon name, NCBI taxonomy ID, parent taxon, Freebase ID）
- 例3：subgenus | species | subspecies | family | subfamily（表：taxon／同じ表の列：label, description, parent taxon, taxon name, instance of, ITIS TSN）

## g0084 — wikidbs10k：見出し「store norske leksikon id」（Wikidata の型 `string`）（1,988 列）
- 例1：Portland_-_Oregon | Queensland | Australia | Cleveland_-_by_i_Ohio | Nevada（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Venezuela | Iran | Nederland | Spania | Belgia（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Spania | Nederland | Ukraina | Egypt | Kilikia（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0085 — sotab_v2：元の種類 `CoordinateAT`（1,982 列）
- 例1：32.29876 | 25.03709 | 48.7177 | 34.047098 | 34.14522
- 例2：-97.081568 | -97.087419 | -97.072756 | -97.1232773 | -97.056753
- 例3：-82.848795 | -82.8504951 | -82.7346021 | -82.8504982 | -82.7636481

## g0086 — wikidbs10k：見出し「gbif taxon id」（Wikidata の型 `string`）（1,950 列）
- 例1：5908955.0 | 5427664.0 | 3219881 | 3222868.0 | 3222442（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：5427664 | 3228377 | 3221980 | 3220708 | 3222868（表：taxon／同じ表の列：label, description, taxon name, taxon rank, NCBI taxonomy ID, parent taxon）
- 例3：5427577.0 | 3224889 | 3225137.0 | 5428214.0 | 3222823.0（表：taxon／同じ表の列：label, description, parent taxon, taxon name, instance of, taxon rank）

## g0087 — wikidbs10k：見出し「musicbrainz area id」（Wikidata の型 `string`）（1,917 列）
- 例1：ab47b3b2-838d-463c-9907-30dcd3438d65 | 720f8272-6ba3-48f7-b78e-14cd2641c2cf | fce9c7ad-fedb-45d8-83c7-236865aaf0b5 | 891cfa2f-b1ce-4b48-b8c3-28d9219c99e7 | e183ffae-1d35-4c78-b552-957535e40af1（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：e2bd38a1-c5ad-4dd4-b9a4-0632ff3be7ae | 7016d578-65d4-4c86-afd7-d84515395a03 | 942a57cb-6cb9-4b71-9c23-960aea254beb | 49ecc6f5-47a6-4072-b9d1-e71370e3e6e8 | d124ea95-eda8-45e3-b7ff-5c631da1c511（表：beginning／同じ表の列：label, description, country, located in the admi…, coat of arms image, Commons category）
- 例3：02e01cf9-b0ed-4286-ac6d-16989f92ced6 | 7c4947a8-a63f-478d-9f07-4ba95de10d9d | 21834e17-8606-4e10-af5c-76d5d668eba9 | 73ae3ba2-e0e0-45db-98a0-3c477f8a1ccf | bfd4eb5c-06fd-428d-a5a2-8e892c065213（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）

## g0088 — wikidbs10k：見出し「office held by head of government」（Wikidata の型 `wikibase-entityid`）（1,869 列）
- 例1：mayor of Sarroca | mayor of Bell-lloc d'Urgell | mayor of Alguaire | mayor of Roselló | mayor of Vilanova de Segriá（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：mayor of Menàrguens | mayor of Vilanova de Segriá | mayor of Almacelles | mayor of Torregrosa | mayor of Alguaire（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：Prime Minister of the Netherlands | Prime Minister of Luxembourg | Prime Minister of Singapore | Chief Executive of Hong Kong | President of El Salvador（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0089 — wikidbs10k：見出し「gran enciclopèdia catalana id」（Wikidata の型 `string`）（1,841 列）
- 例1：0042296 | 52299.0 | 0025184 | 46600.0 | 38398.0（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：5711 | 2942 | 30887 | 41169 | 1409（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例3：39244 | 37639 | 0002742 | 41169 | 61965（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）

## g0090 — wikidbs10k：見出し「microsoft academic id」（Wikidata の型 `string`）（1,831 列）
- 例1：2778514504 | 2778937882 | 150149183 | 2778249958 | 529278444（表：expressed in／同じ表の列：label, description, Freebase ID, Foundational Model …, instance of, UBERON ID）
- 例2：2778643871 | 2776737010 | 2781170380.0 | 2780679087.0 | 2777082638.0（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例3：2776145723 | 2778434524 | 2781171107 | 2910030998 | 2780465316（表：expressed in／同じ表の列：label, description, Freebase ID, Foundational Model …, instance of, UBERON ID）

## g0091 — wikidbs10k：見出し「contains the administrative territorial entity」（Wikidata の型 `wikibase-entityid`）（1,793 列）
- 例1：Southern Denmark | Berat County | North East Community Development Council | Attica Region | Alajuela Province（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Lisbon | Adana Province | Borsod-Abaúj-Zemplén County | Baden-Württemberg | Macau（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Maryville | Jonesboro | Fredericktown | Corydon | St. Joseph（表：political border／同じ表の列：label, description, Commons category, country, located in the admi…, coordinate location）

## g0092 — wikidbs10k：見出し「itis tsn」（Wikidata の型 `string`）（1,747 列）
- 例1：956990 | 957570 | 965992.0 | 958096 | 963300.0（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：965863 | 77 | 707771 | 961851 | 969188（表：taxon／同じ表の列：label, description, taxon name, taxon rank, NCBI taxonomy ID, parent taxon）
- 例3：965278.0 | 957284 | 9751.0 | 960000.0 | 957972（表：taxon／同じ表の列：label, description, parent taxon, taxon name, instance of, taxon rank）

## g0093 — wikidbs10k：見出し「irmng id」（Wikidata の型 `string`）（1,692 列）
- 例1：10032996.0 | 10031928.0 | 1065971 | 11734129.0 | 1059226（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：11187463 | 11035984 | 10029731 | 11215115 | 11837581（表：taxon／同じ表の列：label, description, taxon name, taxon rank, NCBI taxonomy ID, parent taxon）
- 例3：1058625 | 11390431.0 | 10032888.0 | 1048036 | 11294268.0（表：taxon／同じ表の列：label, description, parent taxon, taxon name, instance of, taxon rank）

## g0094 — wikidbs10k：見出し「mesh descriptor id」（Wikidata の型 `string`）（1,687 列）
- 例1：D000333 | D012247 | D059128 | D011549 | D014736（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：D006194 | D001441 | D016957 | D016935 | D000070077（表：taxon／同じ表の列：label, description, taxon name, taxon rank, NCBI taxonomy ID, parent taxon）
- 例3：D010568 | D005002 | D008436 | D009520 | D009426（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0095 — wikidbs10k：見出し「online pwn encyclopedia id」（Wikidata の型 `string`）（1,670 列）
- 例1：4169101 | 3891834.0 | 3964959.0 | 3948952.0 | 4168998（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：4168996 | 4169036 | 4169107 | 4575169 | 4168999（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：4169029 | 4169176 | 3888716 | 4169085 | 4169037（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0096 — wikidbs10k：見出し「den store danske id」（Wikidata の型 `string`）（1,651 列）
- 例1：Mexico | USA | Montréal | Portland | Nuevo_León（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Chile | Rwanda | Norge | Puerto_Rico | Kroatien（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Tyskland | Egypten | Belgien | Grækenland | Slovenien（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0097 — wikidbs10k：見出し「geoshape」（Wikidata の型 `string`）（1,645 列）
- 例1：Data:Guatemala.map | Data:Iceland.map | Data:Turkey.map | Data:Slovakia.map | Data:Puerto Rico.map（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Data:Iran.map | Data:China.map | Data:Spain.map | Data:Italia.map | Data:North Korea.map（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Data:Edinburgh.map | Data:Scottish Borders.map | Data:Aberdeen.map | Data:Dublin.map | Data:Perthshire and Kinross.map（表：administrative territorial entity／同じ表の列：label, description, category of associa…, Curlie ID, MusicBrainz area ID, ISO 3166-2 code）

## g0098 — wikidbs10k：見出し「catalogue of life id」（Wikidata の型 `string`）（1,635 列）
- 例1：64ZVX | 4X4JS | 5BBVL | 4SJJ6 | 4P3SS（表：taxon／同じ表の列：label, description, taxon rank, parent taxon, taxon name, instance of）
- 例2：4P3SS | Z36K | 3C8Y | 4P3S2 | 5YBW（表：taxon／同じ表の列：label, description, parent taxon, taxon name, instance of, taxon rank）
- 例3：BS9Y | 44W74 | 64ZVX | YQRC | 3VGJ4（表：taxon／同じ表の列：label, description, taxon name, taxon rank, Freebase ID, NCBI taxonomy ID）

## g0099 — wikidbs10k：見出し「licence plate code」（Wikidata の型 `string`）（1,594 列）
- 例1：L（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：L（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：MEX | AZ | MS | BS | BDS（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0100 — wikidbs10k：見出し「yso id」（Wikidata の型 `string`）（1,581 列）
- 例1：105182 | 107990 | 105206 | 105092 | 94309（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：105111 | 105209 | 105280 | 105078 | 107664（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：105092 | 108126 | 107592 | 107665 | 107479（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0101 — wikidbs10k：見出し「kbpedia id」（Wikidata の型 `string`）（1,575 列）
- 例1：Slovakia | Ukraine | Rwanda | DominicanRepublic | Iran（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Netherlands | Italy | NaziGermany | Germany | France（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Graciosa-Island | SaoTome-Island | Pico-Island | Terceira-Island | SaoMiguel-Island（表：landform／同じ表の列：label, description, Dewey Decimal Class…, Commons category, instance of, coordinate location）

## g0102 — wikidbs10k：見出し「factgrid item id」（Wikidata の型 `string`）（1,549 列）
- 例1：Q343674 | Q346742 | Q343261 | Q343652 | Q343336（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：Q343350 | Q343336 | Q350523 | Q356543 | Q343610（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：Q21437 | Q87678 | Q83841 | Q92300 | Q82634（表：administrative territorial entity／同じ表の列：label, description, country, Commons category, located in the admi…, coat of arms image）

## g0103 — sotab_v2：元の種類 `Place/name`（1,530 列）
- 例1：Fletcher’s Cove Boathouse | Online event | Nationals Park | Constitution Avenue | Ford's Theatre
- 例2：Bristol Hippodrome | The Redgrave Theatre in Bristol | The Prince Street Social | Bristol Old Vic | The Fleece
- 例3：Event Location | Columbus/Franklin County, Ohio | Coastal Georgia Botanical Gardens - Uni… | Portland/Multnomah County, Oregon | Nashville/Davidson County, Tennessee

## g0104 — sotab_v2：元の種類 `QuantitativeValue`（1,509 列）
- 例1：1.0 | 11.0 | 59.0 | 23.0 | 32.0
- 例2：1
- 例3：3.0 | 10.0 | 7.0 | 12.0 | 25.0

## g0105 — sotab_v2：元の種類 `OfferItemCondition`（1,493 列）
- 例1：https://schema.org/NewCondition
- 例2：http://schema.org/Condition
- 例3：UsedCondition

## g0106 — sotab_v2：元の種類 `Recipe/name`（1,476 列）
- 例1：CINNAMON APPLE MONKEY BREAD | GRILLED CAJUN SALMON with CUCUMBER LIME… | Cajun Shrimp Tacos with Spicy Remoulade | Strawberry Margarita Crisp | Red White and Bleu Burgers
- 例2：Cuban Style Ceviche with Red Pepper Res… | Coconut-Lime Stuffed Dates: A Moana Ins… | Beer Butt Chicken: A Recipe Inspired by… | Cozy Cone Buffalo Ranch Popcorn: A Cars… | Hulk Smash Potatoes: A Thor: Ragnarok I…
- 例3：Roasted Salsa | Bok Choy & Smoked Sausage Ragu | Caprese Martini Recipe | Springfield-Style Cashew Chicken | Banana Nutella Grilled Cheese Sandwich

## g0107 — wikidbs10k：見出し「commons gallery」（Wikidata の型 `string`）（1,462 列）
- 例1：Venezuela | Australia | Lietuva | Costa Rica | Монгол улс（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：United Kingdom | Sverige | Commons:الجزائر / ⴷⵣⴰⵢⵔ | Jugoslavija | Deutschland（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Česko | မြန်မာပြည် | United States | Canada | España（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0108 — wikidbs10k：見出し「wordnet 3.1 synset id」（Wikidata の型 `string`）（1,442 列）
- 例1：09021852-n | 08757039-n | 08784821-n | 08738314-n | 08975399-n（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：08723211-n | 08968866-n | 08879115-n | 09028783-n | 08930441-n（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：08949695-n | 09033521-n | 08740839-n | 09045691-n | 09067337-n（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0109 — wikidbs10k：見出し「gene ontology id」（Wikidata の型 `string`）（1,425 列）
- 例1：GO:0046488 | GO:0010506 | GO:0016310 | GO:0006897 | GO:0007286（表：biological process／同じ表の列：label, description, subclass of, exact match, instance of）
- 例2：GO:0019901 | GO:0008047 | GO:0031005 | GO:0046872 | GO:0005212（表：molecular function／同じ表の列：label, description, subclass of, exact match, instance of）
- 例3：GO:0001541 | GO:0008285 | GO:0002119 | GO:0060689 | GO:0071560（表：biological process／同じ表の列：label, description, subclass of, exact match, instance of）

## g0110 — wikidbs10k：見出し「great russian encyclopedia online id」（Wikidata の型 `string`）（1,425 列）
- 例1：1906527 | 2082520 | 3590227 | 2701630 | 5595796（表：country／同じ表の列：label, description, population, Getty Thesaurus of …, topic's main Wikime…, Wikimedia outline）
- 例2：4684558 | 2162146 | 4245858 | 2019712 | 4692537（表：country／同じ表の列：label, description, coordinates of sout…, GND ID, category of associa…, emergency phone num…）
- 例3：2247323 | 2032993 | 2026445 | 2018403 | 3657248（表：country／同じ表の列：label, description, population, Getty Thesaurus of …, topic's main Wikime…, coordinates of sout…）

## g0111 — wikidbs10k：見出し「bibliothèque nationale de france id」（Wikidata の型 `string`）（1,424 列）
- 例1：120017040 | 11864872z | 12363401c | 11865672n | 119772596（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：12210949t | 12205186t | 11872746v | 152385422 | 12526183z（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：119411873 | 11864655t | 118635857 | 118636082 | 11931184v（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0112 — wikidbs10k：見出し「curlie id」（Wikidata の型 `string`）（1,423 列）
- 例1：Regional/North_America/United_States/Wi… | Regional/North_America/United_States/Ca… | Regional/North_America/United_States/Ca… | Regional/North_America/United_States/Ne… | Regional/North_America/United_States/Ca…（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：Regional/South_America/Ecuador/ | Regional/Europe/Czech_Republic/ | Regional/Asia/Kazakhstan/ | Regional/Europe/Ukraine/ | Regional/Asia/Taiwan/（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：Regional/Europe/United_Kingdom/Scotland… | Regional/Europe/United_Kingdom/Scotland… | Regional/Europe/United_Kingdom/Scotland… | Regional/Europe/United_Kingdom/Scotland/ | Regional/Europe/United_Kingdom/Scotland…（表：administrative territorial entity／同じ表の列：label, description, category of associa…, MusicBrainz area ID, ISO 3166-2 code, capital）

## g0113 — sotab_v2：元の種類 `unitCode`（1,417 列）
- 例1：INH
- 例2：INH
- 例3：MTR

## g0114 — sotab_v2：元の種類 `Distance`（1,414 列）
- 例1：Height（DBpedia：distance）
- 例2：152.0 | 161.0 | 167.0 | 172.0 | 166.0（DBpedia：distance）
- 例3：4' 11\" (151 cm) | 5' 2\" (159 cm) | 5' 8\" (175 cm) | 5' 7\" (171 cm) | 4' 11\" (150 cm)（DBpedia：distance）

## g0115 — wikidbs10k：見出し「ndl authority id」（Wikidata の型 `string`）（1,407 列）
- 例1：00566755 | 00567491 | 00571513 | 00565932 | 00564831（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：00560706 | 00569442 | 00577333 | 00871907 | 00569699（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：00570825 | 00743732 | 00871911 | 00561571 | 00573068（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0116 — wikidbs10k：見出し「french vikidia id」（Wikidata の型 `string`）（1,396 列）
- 例1：Australie | Paraguay | Mexique | Grèce | Érythrée（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Algérie | Grèce | Pologne | Syrie | Union_des_républiques_socialistes_sovié…（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Kirghizistan | République_tchèque | Chine | Canada | Estonie（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0117 — sotab_v2：元の種類 `EventStatusType`（1,365 列）
- 例1：https://schema.org/EventScheduled
- 例2：https://schema.org/EventScheduled
- 例3：EventScheduled

## g0118 — wikidbs10k：見出し「dewey decimal classification」（Wikidata の型 `string`）（1,348 列）
- 例1：2--7287 | 2--68 | 2--4935 | 2--892 | 2--51（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：2--4615 | 2--4622 | 2--4681 | 2--46761 | 2--46357（表：jurisdiction／同じ表の列：label, description, INE municipality co…, located in the admi…, ISO 3166-2 code, Commons category）
- 例3：2--4617 | 2--4611 | 2--4624 | 2--4684 | 2--6711（表：political border／同じ表の列：label, description, INE municipality co…, located in the admi…, ISO 3166-2 code, Commons category）

## g0119 — wikidbs10k：見出し「ensembl protein id」（Wikidata の型 `string`）（1,345 列）
- 例1：ENSRNOP00000061758 | ENSMUSP00000013970 | ENSP00000265382 | ENSP00000300432 | ENSP00000480776（表：Phosphatidylinositol-4-phosphate 5-kina…／同じ表の列：label, description, encoded by, UniProt protein ID, biological process, molecular function）
- 例2：ENSP00000347032 | ENSMUSP00000102852 | ENSMUSP00000006912 | ENSRNOP00000063506 | ENSRNOP00000017989（表：encodes／同じ表の列：label, description, found in taxon, UniProt protein ID, encoded by, RefSeq protein ID）
- 例3：FBpp0312159 | ENSDARP00000104334 | Y46H3A.3a | FBpp0076223 | FBpp0072009（表：Alpha crystallin Heat shock protein／同じ表の列：label, description, UniProt protein ID, encoded by, has part(s), found in taxon）

## g0120 — wikidbs10k：見出し「fips 10-4 (countries and regions)」（Wikidata の型 `string`）（1,339 列）
- 例1：HR | TH | ER | PL | CH（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：GR | MT | KN | PL | IR（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：UKV8 | UKT9 | UKV3 | EI07 | UKT6（表：administrative territorial entity／同じ表の列：label, description, category of associa…, Curlie ID, MusicBrainz area ID, ISO 3166-2 code）

## g0121 — wikidbs10k：見出し「flag」（Wikidata の型 `wikibase-entityid`）（1,328 列）
- 例1：flag of Australia | flag of Denmark | flag of Latvia | flag of Russia | flag of Iran（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：flag of Sweden | flag of Malta | flag of the Czech Republic | flag of the United Kingdom | flag of North Korea（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：flag of Lancashire | flag of Lincolnshire | flag of Norfolk | flag of Suffolk | flag of Somerset（表：historic county／同じ表の列：label, description, instance of, country, part of, locator map image）

## g0122 — wikidbs10k：見出し「demonym」（Wikidata の型 `monolingualtext`）（1,310 列）
- 例1：lleidatà | Menarguí, menarguina | Puigverdí, puigverdina | Vilanoví, vilanovina | Albesà, albesana; albesenc, albesenca（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：Alguairenc, alguairenca | Torregrossí, torregrossina | Alcanonès, alcanonesa | Alcarrassí, Alcarrassina | Bell-lloquí, bell-lloquina（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：ruandai | szingapúri | Let | mauritiusi | griechisch（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0123 — wikidbs10k：見出し「u.s. national archives identifier」（Wikidata の型 `string`）（1,285 列）
- 例1：10035835 | 10045294 | 10035825 | 10044840 | 10044480（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：10035761 | 10046273 | 10044938 | 10035812 | 10046275（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：10042341 | 10040124 | 10036370 | 10045105 | 10036599（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）

## g0124 — wikidbs10k：見出し「language used」（Wikidata の型 `wikibase-entityid`）（1,275 列）
- 例1：standard French | Thai | Estonian Sign Language | Latvian | Standard Taiwanese Mandarin（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Latin | Middle Persian | standard French | Spanish | Soi（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Spanish | Swabian | Tajik | Hunsrik | Estonian Sign Language（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0125 — sotab_v2：元の種類 `BookFormatType`（1,258 列）
- 例1：Unknown Binding | Trade Paperback | Paperback | Board Book | Boxed Set
- 例2：Ebook
- 例3：E-book | CD-Audio | Hardback | eBooks | Other Format

## g0126 — sotab_v2：元の種類 `Review`（1,255 列）
- 例1：It was one my best childhood books I us… | This book is exactly what I needed to i… | As I study English Literature this has … | Top | This book is quite useful particularly …
- 例2：What's up everyone! Welcome to Beyond T… | What's up everyone! Welcome to Beyond T… | After the first issue of The Orville, I… | What's up everyone! Welcome to Beyond T… | What's up everyone! Welcome to Beyond T…
- 例3：This dystopian science fiction thriller… | In Trump the Press: Don Surber's take o… | I heard about this book on the radio ye… | I was shocked to hear of Antonin Scalia… | This is not a review - just an interest…

## g0127 — wikidbs10k：見出し「official language」（Wikidata の型 `wikibase-entityid`）（1,247 列）
- 例1：Catalan（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：Catalan（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：Dutch | Thai | Spanish | Tigrinya | Italian（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0128 — wikidbs10k：見出し「legislative body」（Wikidata の型 `wikibase-entityid`）（1,246 列）
- 例1：Parliament of Croatia | Parliament of Morocco | Parliament of Romania | United States Congress | Verkhovna Rada（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Assembly of the Republic | Bundesrat | Cortes Generales | Parliament of the United Kingdom | Hellenic Parliament（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Parliament of South Africa | Supreme Soviet of the Soviet Union | Riigikogu | National Assembly of Azerbaijan | National Congress of Brazil（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0129 — wikidbs10k：見出し「omegawiki defined meaning」（Wikidata の型 `string`）（1,245 列）
- 例1：7933 | 8351 | 154360 | 5755 | 7845（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：6764 | 8000 | 154503 | 7965 | 5809（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：5748 | 8375 | 5776 | 8003 | 8531（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0130 — wikidbs10k：見出し「eu knowledge graph item id」（Wikidata の型 `string`）（1,202 列）
- 例1：Q15 | Q375 | Q623 | Q3 | Q715（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Q313 | Q921 | Q17 | Q10 | Q18（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Q2520626 | Q2514739 | Q2519085 | Q2528463 | Q2536647（表：administrative territorial entity／同じ表の列：label, description, located in the admi…, country, coordinate location, instance of）

## g0131 — wikidbs10k：見出し「babelnet id」（Wikidata の型 `string`）（1,183 列）
- 例1：14869249n | 14757419n | 16269351n | 16055533n | 14581021n（表：Japanese Badminton Championships／同じ表の列：label, description, sport, country, point in time, followed by）
- 例2：14872983n | 14757572n | 14872754n | 27639492n | 16055533n（表：followed by／同じ表の列：label, description, sport, country, point in time, followed by）
- 例3：16149127n | 14873048n | 14779403n | 16269337n | 14872670n（表：follows／同じ表の列：label, description, sport, country, point in time, followed by）

## g0132 — wikidbs10k：見出し「uk parliament thesaurus id」（Wikidata の型 `string`）（1,175 列）
- 例1：9140 | 8349 | 12742 | 13183 | 11071（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：12000 | 11326 | 13557 | 11042 | 13405（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：13526.0 | 8204.0 | 418557.0 | 8402.0 | 418560.0（表：administrative territorial entity／同じ表の列：label, description, category of associa…, Curlie ID, MusicBrainz area ID, ISO 3166-2 code）

## g0133 — wikidbs10k：見出し「geonlp id」（Wikidata の型 `string`）（1,152 列）
- 例1：h9S4H5 | JHeUq9 | fASBLK | kgQk3d | tS4mSy（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：g2rMOU | Elq5jF | 1xYMqN | nQoqX3 | BrJ5eQ（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：1ZxXtX | NImcn9 | hOIv1y | aGCXIq | h9S4H5（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0134 — wikidbs10k：見出し「location」（Wikidata の型 `wikibase-entityid`）（1,151 列）
- 例1：Circuit Gilles Villeneuve | Las Vegas Motor Speedway | WeatherTech Raceway Laguna Seca | Portland International Raceway | Surfers Paradise Street Circuit（表：2004 Champ Car season／同じ表の列：label, description, sport, point in time, instance of, country）
- 例2：Kingdom of England | Kingdom of Ireland | Kilsyth | Aberdeen | Perth（表：Wars of the Three Kingdoms／同じ表の列：label, description, Freebase ID, part of, instance of, point in time）
- 例3：Azores（表：habitats or species management protecte…／同じ表の列：label, description, country, instance of, area, IUCN protected area…）

## g0135 — wikidbs10k：見出し「topic's main wikimedia portal」（Wikidata の型 `wikibase-entityid`）（1,142 列）
- 例1：Portal:Mongolia | Portal:Ethiopia | Portal:Thailand | Portal:Bolivia | Portal:Hungary（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, Wikimedia outline）
- 例2：Portal:Malta | Portal:North Korea | Portal:Libya | Portal:Hungary | Portal:Greece（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Portal:Namibia | Portal:Kyrgyzstan | Portal:Armenia | Portal:Kazakhstan | Portal:Israel（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, coordinates of sout…）

## g0136 — wikidbs10k：見出し「interlingual index id」（Wikidata の型 `string`）（1,140 列）
- 例1：i82686 | i82905 | i84066 | i83342 | i83751（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：i83894 | i83817 | i83502 | i84044 | i83107（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：i84044 | i84024 | i83244 | i83107 | i83831（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0137 — wikidbs10k：見出し「capital of」（Wikidata の型 `wikibase-entityid`）（1,117 列）
- 例1：Olofström Municipality | Fredericia Municipality | County Limerick | Ekerö Municipality | Vesthimmerland Municipality（表：capital city／同じ表の列：label, description, instance of, country, located in the admi…, Commons category）
- 例2：Clark County | Vernon County | St. Clair County | Morgan County | Lawrence County（表：capital city／同じ表の列：label, description, country, instance of, coordinate location, located in the admi…）
- 例3：Anne Arundel County | England | Aberdeen City | Scottish Borders | Perth and Kinross（表：capital city／同じ表の列：label, description, instance of, Commons category, coordinate location, twinned administrat…）

## g0138 — wikidbs10k：見出し「google knowledge graph id」（Wikidata の型 `string`）（1,116 列）
- 例1：/g/155pltvz | /g/11x983mfg | /g/11x9804xm | /g/15dp6gbl | /g/155sbgry（表：Japanese Badminton Championships／同じ表の列：label, description, sport, country, point in time, followed by）
- 例2：/g/11c605t2lw | /g/11n8rz5bzz | /g/155rpybj | /g/11t31w7l7x | /g/11x987cy_（表：followed by／同じ表の列：label, description, sport, country, point in time, followed by）
- 例3：/g/11x97zcq9 | /g/11r8t1pyn6 | /g/11t31w7l7x | /g/11x9844dq | /g/155r19c2（表：follows／同じ表の列：label, description, sport, country, point in time, followed by）

## g0139 — wikidbs10k：見出し「loc and marc vocabularies id」（Wikidata の型 `string`）（1,116 列）
- 例1：countries/be | countries/au | countries/th | countries/hk | countries/ag（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：countries/sw | countries/ly | countries/lu | countries/tu | countries/sp（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：countries/br | countries/gw | countries/bl | countries/xxc | countries/ur（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0140 — wikidbs10k：見出し「refseq rna id」（Wikidata の型 `string`）（1,116 列）
- 例1：NM_001009967 | NM_001128702 | NM_008845 | NM_001004579 | XM_011538747（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, ortholog, encodes）
- 例2：NM_001089353 | NM_054097 | NM_001005775 | NM_001042621 | NM_065099（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例3：NM_006308 | NM_014365 | NM_001031943 | NM_031607 | NM_013868（表：encoded by／同じ表の列：label, description, Entrez Gene ID, Ensembl gene ID, Ensembl transcript …, encodes）

## g0141 — wikidbs10k：見出し「competition class」（Wikidata の型 `wikibase-entityid`）（1,109 列）
- 例1：national championship（表：Japanese Badminton Championships／同じ表の列：label, description, sport, country, point in time, followed by）
- 例2：national championship（表：followed by／同じ表の列：label, description, sport, country, point in time, followed by）
- 例3：national championship（表：follows／同じ表の列：label, description, sport, country, point in time, followed by）

## g0142 — wikidbs10k：見出し「chromosome」（Wikidata の型 `wikibase-entityid`）（1,106 列）
- 例1：rat chromosome 7 | Danio rerio chromosome 23 | mouse chromosome 10 | Danio rerio chromosome 8 | human chromosome 19（表：encoded by／同じ表の列：label, description, Entrez Gene ID, HomoloGene ID, RefSeq RNA ID, ortholog）
- 例2：rat chromosome 1 | mouse chromosome 3 | Danio rerio chromosome 10 | mouse chromosome 2 | Rattus norvegicus chromosome 10（表：orthology／同じ表の列：label, description, Entrez Gene ID, subclass of, Ensembl gene ID, HomoloGene ID）
- 例3：human chromosome 7 | mouse chromosome 9 | Danio rerio chromosome 15 | Rattus norvegicus chromosome 12 | Caenorhabditis elegans chromosome V（表：encoded by／同じ表の列：label, description, Entrez Gene ID, Ensembl gene ID, RefSeq RNA ID, Ensembl transcript …）

## g0143 — sotab_v2：元の種類 `Hotel/name`（1,093 列）
- 例1：GenX Sundaram | GenX Rameshwaram, Deoghar | Pinnacle by 1589 Hotels | GenX Bhavnagar | Clarks Collection Jaipur（DBpedia：Hotel）
- 例2：Ebne Sina | Narcis BnB | Viana Hotel | Adib Almamalek Hotel | Jolfa Hotel（DBpedia：Hotel）
- 例3：Ibis Constantine | O'Callaghan Eliott Hotel | Hyatt Place Pasadena | Riviera Towers | Arcadia 408（DBpedia：Hotel）

## g0144 — wikidbs10k：見出し「rkd thesaurus id」（Wikidata の型 `string`）（1,091 列）
- 例1：287 | 1634 | 456 | 6448 | 5337（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例2：25339 | 26187 | 7126 | 410 | 2823（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：6974.0 | 3539.0 | 15590.0 | 456.0 | 3025.0（表：country／同じ表の列：label, description, demonym, official name, Dewey Decimal Class…, central bank）

## g0145 — wikidbs10k：見出し「subreddit」（Wikidata の型 `string`）（1,086 列）
- 例1：longbeach | australia | Denver | LACounty | MexicoCity（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, flag image, Commons category）
- 例2：hungary | suomi | czech | belgium | costarica（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例3：es | poland | belgium | france | hungary（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）

## g0146 — wikidbs10k：見出し「economy of topic」（Wikidata の型 `wikibase-entityid`）（1,082 列）
- 例1：economy of Venezuela | economy of Bosnia and Herzegovina | economy of Belarus | economy of Namibia | economy of the United States（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：economy of Sweden | economy of Russia | economy of Egypt | economy of Greece | economy of Algeria（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：economy of Canada | economy of France | economy of Jordan | economy of Spain | economy of Tajikistan（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0147 — wikidbs10k：見出し「unesco thesaurus id」（Wikidata の型 `string`）（1,077 列）
- 例1：concept832 | concept793 | concept777 | concept709 | concept923（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：concept914 | concept910 | concept923 | concept718 | concept917（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：concept806 | concept891 | concept830 | concept834 | concept794（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0148 — wikidbs10k：見出し「pronunciation audio」（Wikidata の型 `string`）（1,065 列）
- 例1：Lb-Éisträich.ogg | En-au-Australia.ogg | Lb-Amerika.ogg | Lb-Namibia.ogg | Lb-Irland.ogg（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：Rm-sursilv-Svizra.flac | Lb-Vereenegt Kinnekräich.ogg | Lb-Nordkorea.ogg | Lb-Finnland.ogg | Lb-Libyen.ogg（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：Lb-Brasilien.ogg | Lb-Kirgisistan.ogg | Sk-Slovensko.ogg | De-Deutschland.ogg | He-Medinat Israel.ogg（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## g0149 — wikidbs10k：見出し「number of households」（Wikidata の型 `quantity`）（1,064 列）
- 例1：137.0 | 189.0 | 29.0 | 60.0 | 33.0（表：jurisdiction／同じ表の列：label, description, country, coat of arms image, postal code, locator map image）
- 例2：91.0 | 44.0 | 23.0 | 189.0 | 63.0（表：political border／同じ表の列：label, description, Commons category, country, coat of arms image, postal code）
- 例3：+5948 | +6529 | +7910 | +9387 | +144159（表：administrative territorial entity／同じ表の列：label, description, country, shares border with, capital, named after）

## g0150 — wikidbs10k：見出し「idref id」（Wikidata の型 `string`）（1,062 列）
- 例1：133263886 | 026588919 | 026398206 | 154019917 | 026438658（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）
- 例2：026376296 | 026360608 | 026389908 | 026357240 | 02658347X（表：country／同じ表の列：label, description, Great Russian Encyc…, coordinates of sout…, GND ID, category of associa…）
- 例3：030685435 | 026389908 | 027944913 | 027222950 | 026392275（表：country／同じ表の列：label, description, Great Russian Encyc…, population, Getty Thesaurus of …, topic's main Wikime…）

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
g0053	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
```
