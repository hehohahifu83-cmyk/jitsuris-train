# 判断の説明 001 / 006（1 列ずつ、くわしく）

今の仕組みが「不明」と答えたか、種類を取り違えた列です。人がどう考えて種類を決めるかを、決め方の規則（C3 の判断のルール）に移したいので、**考えた順にくわしく**書いてください。

- LABEL_GUIDE.md（v2.1）の判定の順番（①列名・単位 → ②表の題名 → ③同じ表の列 → ④値の形）で、それぞれから**何が読めたか・読めなかったか**を書く。読めなければ「なし」
- 「迷った種類」には、候補に上がった別の種類と、それを退けた理由を書く（例：「amount も考えたが、通貨の記号も単位の列もなく、値が整数の小さい数なので quantity」）
- 「規則にするなら」は、ほかの表にも当てはまる言い方で 1〜2 文。当てはまらない例（その規則で誤りそうな列）も書く。規則にできないなら「できない（理由）」
- 決め手は次から 1 つ：見出しの語・単位の列・表の題名・同じ表の列名・値の形・決められない。使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- **見ないもの**：`research/unknown/columns.jsonl`・`misses.jsonl`・`sheet_index.json`・`explain/index.json`・`compare*`・`candidates*`・`findings.md`（正解と今の仕組みの答えが入っている）、Grok の答え、モデルの予測
- 答え：末尾の雛形を写して埋め、`research/unknown/explain/answers_chatgpt/explain_001.md` に置く。見出し（`## x0001` など）と各行の頭（`- 種類：` など）は変えない

## x0001 — 見出し「GEO_CANT」
- 値：1 | 1 | 1 | 2 | 2 | 2 | 2 | 2
- 同じ表の列名：REF_YEAR, GEO_COMM, VALUE

## x0002 — 見出し「kategorie_sortierung」
- 値：1 | 1 | 1 | 3 | 2 | 1 | 1 | 1
- 同じ表の列名：jahr, datum, gemeinde_nummer, bezirk_nummer, verteilzone, analyt, kategorie, einheit, quelle

## x0003 — 見出し「Id Of Disease Category」
- 値：disease_14 | disease_14 | disease_14 | disease_14 | disease_14 | disease_11 | disease_3 | disease_14
- 同じ表の列名：Year, Canton, Id Of Animal Category, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Experiment Category

## x0004 — 見出し「parameter_decimals」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granularity, parameter_datatype, parameter_unit

## x0005 — 見出し「sitzung_titel」
- 値：61. Sitzung | 61. Sitzung | 60. Sitzung | 59. Sitzung | 59. Sitzung | 57. Sitzung | 57. Sitzung | 57. Sitzung
- 同じ表の列名：sitzung_startdatum, traktandum_titel, traktandum_nummer, traktandum_geschaeft, sitzung_id

## x0006 — 見出し「abkuerzung」
- 値：UPI,Unique Person Identificati… | ZEMIS | InfoStar | PISA | MOFIS | MILVA | AKS_GB | KEP
- 同じ表の列名：definition

## x0007 — 見出し「parameter_decimals」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granularity, parameter_datatype, parameter_unit

## x0008 — 見出し「parameter_decimals」
- 値：3 | 1 | 1 | 1 | 0 | 0 | 1 | 1
- 同じ表の列名：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granularity, parameter_datatype, parameter_unit

## x0009 — 見出し「Degree of severity 2」
- 値：243 | 72 | 0 | 0 | 0 | 41 | 8 | 427
- 同じ表の列名：Year, Canton, Id Of Animal Category, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 3, Id Experiment Category, Id Of Disease Category

## x0010 — 見出し「Extending Agency」
- 値：3 | 3 | 3 | 3 | 3 | 3 | 3 | 3
- 同じ表の列名：Donor Project Number, Project Title, Nature of Submission, Benefitting Country Code, Input Sector code, Channel of Delivery Code, Type of Flow, Type of Finance, Type of Aid

## x0011 — 見出し「kategorie_sortierung」
- 値：1 | 1 | 2 | 1 | 2 | 5 | 2 | 1
- 同じ表の列名：gruppe, gruppe_id, analyt, analyt_id, kategorie, einheit, farbcode, start_datum, end_datum

## x0012 — 見出し「No. laboratory confirmed」
- 値：5 | 45 | 5 | 5 | 2
- 表の題名：2019-20 Foodborne Disease Investigations
- 同じ表の列名：No., Month and Year, Organism, Exposure setting, No. ill, Evidence

## x0013 — 見出し「nfr」
- 値：5A | 5A | 5A | 5A | 5D | 5C | 5C | 5C
- 同じ表の列名：jahr, hauptgruppe, untergruppe, thg, thg_agg, quelle, einheit, einheit_lang, stand

## x0014 — 見出し「Question」
- 値：Q1 | Q10 | Q1 | Q10 | Q10 | Q10 | Q9 | Q10
- 同じ表の列名：UKPRN, UPIN, Age_Band, Survey_Type, Score, OrgLowest, OrgMiddle, OrgHighest, AllLowest

## x0015 — 見出し「verteilzone」
- 値：261_LZ | 261_LZ | 261_LZ | 220_ZHa | 261_LZ | 261_LZ | 261_LZ | 261_LZ
- 同じ表の列名：jahr, datum, gemeinde_nummer, bezirk_nummer, analyt, kategorie, kategorie_sortierung, einheit, quelle

## x0016 — 見出し「Arrest/Detention > Assault with Weapon」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault, Arrest/Detention > Child Porno…, Arrest/Detention > Child Sex, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immigration, Arrest/Detention > Modern Slav…, Arrest/Detention > Murder / Ma…

## x0017 — 見出し「Degree of severity 1」
- 値：0 | 247 | 752 | 0 | 72 | 0 | 0 | 138
- 同じ表の列名：Year, Canton, Id Of Animal Category, Genetically Modified, Degree of severity 0, Degree of severity 2, Degree of severity 3, Id Experiment Category, Id Of Disease Category

## x0018 — 見出し「sessionssitzung_uhrzeit」
- 値：09.00-11.45 | 13.30-16.30 | 17.00-19.00 | 09.00-11.45 | 13.30-16.00 | 13.30-16.30 | 17.00-19.00 | 17.05-19.00
- 同じ表の列名：session_uid, sessionssitzung_datum, sessionssitzung_bezeichnung, Übersicht vom

## x0019 — 見出し「Signatur」
- 値：GS-GUGE-BIEDERMANN-A-9 | GS-GUGE-BLEULER-C-1 | GS-GUGE-DUNKER-BA-E-12 | GS-GUGE-DUNKER-BA-E-13 | GS-GUGE-ENGELBRECHT-C-6 | GS-GUGE-ENGELBRECHT-C-7 | GS-GUGE-ENGELBRECHT-C-8 | GS-GUGE-HACKERT-A-1
- 同じ表の列名：ID, KünstlerIn, Titel, Inhalt_Kurzbeschreibung, Titelvariante, Datierung_von, Datierung_bis, Serientitel, Farbe

## x0020 — 見出し「No.」
- 値：1 | 2 | 3 | 4 | 5 | No. = Number; D = Descriptive …
- 表の題名：2019-20 Foodborne Disease Investigations
- 同じ表の列名：Month and Year, Organism, Exposure setting, No. ill, No. laboratory confirmed, Evidence

## x0021 — 見出し「verantwortlichkeit_abkuerzung」
- 値：KTTGWH | KTTGWH | KTTGWH | KTTGWH | BAFU | KTTGWH | KTTGWH | KTTGWH
- 同じ表の列名：obj_id, parameter, einheit, gueltig_von, gueltig_bis, qualitaet, verantwortlichkeit_organisatio…, verantwortlichkeit_abteilung, messgruppierung_ortsbezeichnun…

## x0022 — 見出し「listed_building」
- 値：1072858 | 1361954 | 1072793 | 1072806 | 1361995 | 1072860 | 1163200 | 1361950
- 同じ表の列名：reference, geometry, notes, uprns, entry_date, start_date

## x0023 — 見出し「parameter_decimals」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granularity, parameter_datatype, parameter_unit

## x0024 — 見出し「Arrest/Detention > Child Sex」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Sep-20, Arrest/Detention > Assault, Arrest/Detention > Assault wit…, Arrest/Detention > Child Porno…, Arrest/Detention > Drugs, Arrest/Detention > Fraud, Arrest/Detention > Immigration, Arrest/Detention > Modern Slav…, Arrest/Detention > Murder / Ma…

## x0025 — 見出し「Neither satisfied or dissatisfied」
- 値：7 | 4 | 5 | 3 | 6 | 8 | 8 | 2
- 同じ表の列名：Week commencing, Transactions – online, Completion rate, User satisfaction, Very dissatisfied, Dissatisfied, Satisfied, Very satisfied

## x0026 — 見出し「Degree of severity 3」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Year, Canton, Id Of Animal Category, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Id Experiment Category, Id Of Disease Category

## x0027 — 見出し「Id Of Animal Category」
- 値：animal_1 | animal_1 | animal_1 | animal_2 | animal_2 | animal_1 | animal_1 | animal_1
- 同じ表の列名：Year, Canton, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Experiment Category, Id Of Disease Category

## x0028 — 見出し「Degree of severity 0」
- 値：0 | 12 | 200 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：Year, Canton, Id Of Animal Category, Genetically Modified, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Experiment Category, Id Of Disease Category

## x0029 — 見出し「GOR CODE」
- 値：H | H | H | H | H | H | H | H
- 同じ表の列名：LSOA CODE, PRE 2009 LA CODE, POST 2009 LA CODE, IMD SCORE, RANK OF IMD SCORE (where 1 is …, INCOME SCORE, RANK OF INCOME SCORE (where 1 …, EMPLOYMENT SCORE, RANK OF EMPLOYMENT SCORE (wher…

## x0030 — 見出し「Gemeinde_Nr」
- 値：5 | 7 | 12 | 23 | 27 | 31 | 37 | 37
- 同じ表の列名：Jahr, Gemeinde, Abfallart, Wert, Einheit

## x0031 — 見出し「id2」
- 値：city | europe | rebgasse | aeschen | claramatte | centralbahn | bahnhofsued | elisabethen
- 同じ表の列名：Titel, Publikationszeit, Anzahl frei, Total, Anteil frei, Auslastung, Auslastung in Prozent, Link, geo_point_2d

## x0032 — 見出し「parameter_decimals」
- 値：0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
- 同じ表の列名：parameter_group_de, parameter_group_fr, parameter_group_it, parameter_group_en, parameter_granularity, parameter_datatype, parameter_unit

## x0033 — 見出し「batch」
- 値：1 | 1 | 2 | 2 | 2 | 1 | 1 | 1
- 表の題名：Reducing pest risk in birch wood products - The effective heat treatme…
- 同じ表の列名：treeLocation, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, bathPosition, vialPosition, replicate

## x0034 — 見出し「Semaine」
- 値：16 | 7 | 41 | 8 | 40 | 29 | 2 | 6
- 同じ表の列名：AC, Fin, Age, Nombre_Deces, Attendu, Lim_min, Lim_sup, Exces

## x0035 — 見出し「traktandum_start_behandlung_uhrzeit」
- 値：13.30-16.30 | 13.30-16.30 | 09.00-11.45 | 09.00-11.45 | 09.00-11.45 | 13.30-16.00 | 09.00–11.45 | 13.30–16.30
- 同じ表の列名：session_uid, traktandum_nummer, traktandum_geschaeft_nr, traktandum_start_behandlung_da…, traktandum_beschluss_uhrzeit, traktandum_beschluss_deutsch, traktandum_beschluss_franz, traktandum_beschlussdetail_deu…, traktandum_beschlussdetail_fra…

## x0036 — 見出し「Id Experiment Category」
- 値：experiment_2 | experiment_2 | experiment_2 | experiment_2 | experiment_51 | experiment_1 | experiment_1 | experiment_2
- 同じ表の列名：Year, Canton, Id Of Animal Category, Genetically Modified, Degree of severity 0, Degree of severity 1, Degree of severity 2, Degree of severity 3, Id Of Disease Category

## x0037 — 見出し「Extending Agency」
- 値：3 | 3 | 3 | 3 | 3 | 3 | 3 | 3
- 同じ表の列名：Donor Project Number, Project Title, Nature of Submission, Benefitting Country Code, Input Sector code, Channel of Delivery Code, Type of Flow, Type of Finance, Type of Aid

## 答えの雛形

```markdown
## x0001
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0002
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0003
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0004
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0005
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0006
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0007
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0008
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0009
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0010
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0011
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0012
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0013
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0014
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0015
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0016
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0017
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0018
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0019
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0020
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0021
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0022
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0023
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0024
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0025
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0026
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0027
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0028
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0029
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0030
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0031
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0032
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0033
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0034
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0035
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0036
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

## x0037
- 種類：
- 決め手：
- ①列名・単位の語から読めること：
- ②表の題名から読めること：
- ③同じ表の列名から読めること：
- ④値の形から読めること：
- 迷った種類と、それを退けた理由：
- 自信が低い・決められないなら、その理由と、何があれば決められたか：
- 規則にするなら（「列名が…で、値が…なら…。ただし…のときは除く」の形で。当てはまらない例も）：
- 確信：高・中・低

```
