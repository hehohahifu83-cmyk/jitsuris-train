# 割れている組の見直し 007（LABEL_GUIDE v2.2）

同じ陣・同じ列名なのに種類が割れている組。判断するのは「少ないほうの列」（番号つき）。
`answers/split_NNN.tsv` に少ないほうの列 1 列ずつ 1 行：`gid`・`col`（番号）・`label`（付けるべき種類。今のままなら今の種類、決められなければ unknown）・`reason`。
今のラベルは参考。v2.2 の決まりと、その列の表・値・同じ表の列から決める。表が違って意味が違えば、割れたままでよい。

## G181　b014「Audit Area」（2 列：category 1・address 1）

多いほうの category の例：

- Recycling Stations / Recycling Stations / Recycling Stations / Recycling Stations / Recycling Stations / Recycling Stations / Recycling Stations / Recycling Stations（同じ表：Date・Point of Inspection・Compliance Yes/No (1/0)・Comments on Non-Compliance）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | WHMIS Labels / WHMIS Labels / WHMIS Labels / WHMIS Labels / WHMIS Labels / WHMIS Labels / Cleaning Room / Cleaning Room | Date・Point of Inspection・Compliance Yes/No (1/0)・Comments | c5c0d840a0/download/whmis-label-and-cleaning-room-audits.csv |

## G182　b014「Point of Inspection」（2 列：address 1・category 1）

多いほうの address の例：

- 2nd Floor (Cafeteria) / Training Centre / 2nd Floor (Cafeteria) / Door to Front Hangar Entrance / Helicopter Shop / Training Centre / Door to Front Hangar Entrance / Training Centre（同じ表：Date・Audit Area・Compliance Yes/No (1/0)・Comments on Non-Compliance）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | All Areas / Hangar by Engine Repair / Helicopter shop / All Areas / All Areas / Hangar in front of Stores / 2 pairs nitrile gloves / 1 spare face shield visor | Date・Audit Area・Compliance Yes/No (1/0)・Comments | c5c0d840a0/download/whmis-label-and-cleaning-room-audits.csv |

## G183　b016「@Caption」（3 列：org 1・category 1・date 1）

多いほうの org の例：

- 府省名 / 法務省 / 財務省 / 国税庁 / 厚生労働省 / 農林水産省 / 林野庁 / 経済産業省（同じ表：短期従事状況（2014年）・ja）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | 区分 / 公務員数総計 / 地方公務員 / 国家公務員 / 国家公務員 / 国家公務員 / 国家公務員 / 国家公務員 | 国家公務員及び地方公務員の種類と数・ja | https://www.jinji.go.jp/content/900011664.csv |
| 3 | date | @Creator / @Date / @Language / @@Title / @@Unit /  / xsd:string / 2003.03 | 通信サービス加入契約数の推移 | umu.go.jp/johotsusintokei/whitepaper/ja/r02/csv/n1101010.csv |

## G184　b017「Area」（2 列：other 1・address 1）

多いほうの other の例：

- 3.73 / 3.18 / 3.02 / 43.28 / 4.72 / 2.15 / 2.71 / 10.49（同じ表：Report Date・County・measurement_unit__ha_・Decision・Decision Date・Latest Appeal Date・GPC Category・eis_eia_required）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | Carlow Kilkenny South Tipperary / Cavan Monaghan / Cork / Donegal / Dublin North / Dublin City North / Dublin South Central / Dublin South East Wicklow | RegionID・AreaID・Year・Jan・Feb・Mar・Apr・May | ther-placement-type-with-an-allocated-social-worker-2018.csv |

## G185　b017「STATISTIC」（6 列：id 4・category 2）

多いほうの id の例：

- EDA36 / EDA36 / EDA36 / EDA36 / EDA36 / EDA36 / EDA36 / EDA36（同じ表：Statistic・TLIST(A1)・Year・C02199V02655・Sex・UNIT・VALUE）
- EDA96 / EDA96 / EDA96 / EDA96 / EDA96 / EDA96 / EDA96 / EDA96（同じ表：Statistic・TLIST(A1)・Year・C02199V02655・Sex・C02505V03033・Details of Results・UNIT）
- HSQ08C1 / HSQ08C1 / HSQ08C1 / HSQ08C1 / HSQ08C1 / HSQ08C1 / HSQ08C2 / HSQ08C2（同じ表：Statistic・TLIST(Q1)・Quarter・C02350V02827・House Type New or Second hand・UNIT・VALUE）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | category | STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE / STOCKNURSE | Statistic Label・YEAR・Year・TRNGTYPE・Type of training・QUALCOU・UNIT・VALUE | s/7edf5f10/JQ06_-_Stock_of_Nurses_by_country_of_training.csv |
| 4 | category | NURSES / NURSES / NURSES / NURSES / NURSES / NURSES / NURSES / NURSES | Statistic Label・YEAR・Year・MEASURE・Measure・UNIT・VALUE・FLAG | ://assets.gov.ie/static/documents/29420abf/JQ05_-_Nurses.csv |

## G186　b017「VALUE」（5 列：quantity 4・rate 1）

多いほうの quantity の例：

- 288 / 671 / 394 / 1489 / 473 / 182 / 369 / 1624（同じ表：STATISTIC・Statistic・TLIST(A1)・Year・C02199V02655・Sex・C02505V03033・Details of Results）
- . / . / . / . / . / . / . / .（同じ表：STATISTIC・Statistic Label・YEAR・Year・TRNGTYPE・Type of training・QUALCOU・UNIT）
- 64072 / 67808 / 72543 / 76558 / 77090 / 41233 / 42937 / 44822（同じ表：STATISTIC・Statistic Label・YEAR・Year・MEASURE・Measure・UNIT・FLAG）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | rate | 67.5 / 71.8 / 67.3 / 76.3 / 67.5 / 73.8 / 78.9 / 72 | STATISTIC・Statistic・TLIST(A1)・Year・C02199V02655・Sex・UNIT | pi.restful/PxStat.Data.Cube_API.ReadDataset/EDA36/CSV/1.0/en |

## G187　b017「Produit」（3 列：product 2・category 1）

多いほうの product の例：

- Paquet de saveurs - séchés / Paquet de saveurs - séchés / Paquet de saveurs - séchés / Paquet de saveurs - séchés / Paquet de saveurs - séchés / Paquet de saveurs - séchés / Paquet de saveurs - séchés / Paquet de saveurs - séchés（同じ表：Sample No. - No. d'echantillon・Region - Region・Function・Fonction・Origin・Origine・Product・Date Sampled - Date d'echantillonage）
- Préparation pour nourrissons - Laitier / Préparation pour nourrissons - Laitier / Céréales - Adultes / Céréales - Adultes / Céréales - Nourrissons / Céréales - Adultes / Céréales - Adultes / Pain - Autre（同じ表：Sample No. - No. d'echantillon・Function・Fonction・Origin・Origine・Product・Date Sampled - Date d'echantillonage・Type of Test）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | Préparation pour nourrissons - Soja / Préparation pour nourrissons - Laitier / Divers-Produits Laitiers / Préparation pour nourrissons - Laitier / Céréales - autre / Céréales - autre / Céréales - autre / Céréales - autre | Sample No. - No. d'echantillon・Function・Fonction・Origin・Origine・Product・Date Sampled - Date d'echantillonage・Type of Test | ownload/chem_ts_2011-12_deoxynivalenol_in_selected_foods.csv |

## G188　b036「Region」（2 列：category 1・address 1）

多いほうの category の例：

- Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan / Metropolitan（同じ表：Data as of・Licence No・Start Date・Trading Status・Licence Type・Filter Category・SA2 Band・Subject to Cap）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | Eastern Metropolitan Region / North and West Metropolitan Region / Eastern Metropolitan Region / Loddon-Mallee / North and West Metropolitan Region / Southern Metropolitan Region / North and West Metropolitan Region / North and West Metropolitan Region | Suburb・State・Business Category・LGA | gov.au/storage/f/2013-05-12T214343/tmp66N8dymartial-arts.csv |

## G189　b055「名称」（24 列：org 17・address 7）

多いほうの org の例：

- 三東運輸(株) 新木場工場 / 広陽サービス(株) 東雲リサイクルセンター / (株)西商店 第二瓶･缶センター / (有)野村ゴム商店 / (株)大島商店 / (有)那須野商店 / (株)遠藤商店 / (株)那須商会 第二工場（同じ表：登録番号・古紙・金属・ガラス・その他・その他内容）
- 五本木小学校屋内プール / 碑小学校屋内プール / 緑ヶ丘小学校屋内プール / 駒場体育館 / 区民センター体育館 / 碑文谷体育館 / 中央体育館 / 八雲体育館（同じ表：全国地方公共団体コード・陸上競技・水泳・サッカー・スキー・テニス・ボート・ホッケー）
- 株式会社 あおば葬祭 / 勝山葬祭 株式会社 / 葬祭総合センター 株式会社 門脇 / 株式会社 式典 / すみやセレモニー 株式会社 / 東京式典 株式会社 / 株式会社 花会 / 有限会社 花心（同じ表：全国地方公共団体コード・地方公共団体名・名称_カナ）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | 泪橋西 / 荒川七丁目 / 荒川区民会館北第一 / 大山西町第二 / 西葛西二丁目 / 青梅末広町二丁目西 / 夫婦橋 / 上中里駅前 | 市区町村名・警察署名 | kotsu/jikoboshi/koreisha/basho/index.files/accessibility.csv |
| 3 | address | 江東橋二丁目 / 東京都慰霊堂北側 / 東京都慰霊堂南側 / 白鬚 / 押上駅前自転車駐車場内 / 両国公園 / 錦糸公園(東) / 銅像堀公園 | 全国地方公共団体コード・ID・地方公共団体名・男性トイレ数（小便器）・男性トイレ数（和式）・男性トイレ数（洋式）・女性トイレ数（和式）・女性トイレ数（洋式） | w.opendata.metro.tokyo.lg.jp/sumida/131075_public_toilet.csv |
| 4 | address | 碑文谷アパート / 清水町アパート / 目黒区立コーポ目黒本町二丁目 / 目黒区立コーポ八雲 / 上目黒一丁目アパート / 青葉台一丁目アパート / 目黒本町四丁目アパート / ホーム月光原 | 地方公共団体名・建設年度・管理戸数・備考 | ata.metro.tokyo.lg.jp/meguro/131105_meguroku_koueijutaku.csv |
| 12 | address | 桜台体育館 / 中村南スポーツ交流センター / 総合体育館 / 上石神井体育館 / 光が丘体育館 / 平和台体育館 / 中村南スポーツ交流センター プール / 大泉学園町体育館温水プール | 全国地方公共団体コード・ID・地方公共団体名・トレーニング室・陸上競技・水泳・サッカー・スキー | etro.tokyo.lg.jp/nerima/131202_nerimaku_sportsfacilities.csv |
| 16 | address | 中央公園 / 上水公園 / つつじ公園 / あじさい公園 / 中島町公園 / 小川緑地 / たけのこ公園 / 鈴木街道公園 | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・建物名等(方書)・設置位置・男性トイレ総数・男性トイレ数（小便器） | .opendata.metro.tokyo.lg.jp/kodaira/132110_public_toilet.csv |
| 20 | address | 東大和市向原市民センター / 東大和市向原市民センター / 桜が丘市民広場 / 市民プール / 市民体育館 / 市民体育館 / 市民体育館 / 東大和市桜が丘市民センター | 全国地方公共団体コード・ID・地方公共団体名・建物名等(方書)・設置位置・男性トイレ総数・女性トイレ総数・男女共用トイレ総数 | metro.tokyo.lg.jp/higashiyamato/ods/132209_public_toilet.csv |
| 21 | address | 白山公園 / 滝山公園 / 小山台遺跡公園 / 神山堂阪公園 / 下里本邑遺跡公園 / 西口中央公園 / 小山れんげ公園 / 竹林公園 | 全国地方公共団体コード・ID・地方公共団体名・名称_カナ・名称_英語・設置位置・高度の種別・高度の値 | ata.metro.tokyo.lg.jp/higashikurume/132225_public_toilet.csv |

## G190　b055「施設名」（3 列：org 2・address 1）

多いほうの org の例：

- 板橋清掃工場 / 足立清掃工場 / 世田谷清掃工場 / 破砕ごみ処理施設 / 中防灰溶融施設 / 町田ﾘｻｲｸﾙ文化ｾﾝﾀｰ / 日野市クリーンセンター / 国分寺市清掃センター（同じ表：地域・No.・団体名・施設種類・処理方式・焼却処理能力(t/日) （規模）・溶融処理能力(t/日) （規模）・竣工年月）
- ZXY三越前2 / ZXY青物横丁 / KEIO BIZ PLAZA 多摩センター / BIZcomfort曳舟 / BIZcomfort五反田 / NewWork日本橋 / NewWork成城学園前 / NewWork青砥（同じ表：施設ID・区市町村コード・都道府県・区市町村・エリア・アクセス・月曜日 営業開始時間・月曜日 営業終了時間）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | address | 青山公園 / 赤塚公園 / 秋留台公園 / 井の頭恩賜公園 / 上野恩賜公園 / 宇喜田公園 / 浮間公園 / 大泉中央公園 | 区分 | //www.opendata.metro.tokyo.lg.jp/kensetsu/R3/teienitiran.csv |

## G191　b055「備考」（7 列：text 5・category 2）

多いほうの text の例：

- 一部休止中 / 一部休止中 / 一部休止中 / 一部休止中 / 一部休止中 / 休止中（1号炉） / 休止中 / 休止中（同じ表：地域・No.・団体名・施設名・施設種類・処理方式・焼却処理能力(t/日) （規模）・溶融処理能力(t/日) （規模））
-  /  /  /  /  /  /  / （同じ表：市場名・水産・青果・食肉・花き）
- 家電リサイクル法対象品 / 家電リサイクル法対象品 / 家電リサイクル法対象品 / 家電リサイクル法対象品 /  / 家電リサイクル法対象品 /  / （同じ表：全国地方公共団体コード・ID・地方公共団体名・ゴミの品目・分別区分・料金種別・料金・料金備考）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 4 | category | 区営住宅 / 区営住宅 / 高齢者福祉住宅 / 高齢者福祉住宅 / 区営住宅 / 区営住宅 / 区営住宅 / 従前居住者用住宅 | 地方公共団体名・名称・建設年度・管理戸数 | ata.metro.tokyo.lg.jp/meguro/131105_meguroku_koueijutaku.csv |
| 7 | category | 授乳可 / 授乳可 / 授乳可 / 授乳可 / 授乳可 / 授乳可 / 授乳可 / 授乳可 | 全国地方公共団体コード・ID・地方公共団体名・名称・連結表記・おむつ替えコーナー | ://www.opendata.metro.tokyo.lg.jp/koganei/29_babystation.csv |

## G192　b055「名称_カナ」（10 列：org 8・address 2）

多いほうの org の例：

- アオバソウサイ / カツヤマソウサイ / ソウサイソウゴウセンターカドワキ / シキテン / スミヤセレモニー / トウキョウシキテン / ハナエ / ハナココロ（同じ表：全国地方公共団体コード・地方公共団体名・名称）
- オオオカヤマコドモショクドウ / ミネマチコドモショクドウミンナデゴハン / タンポポショクドウ / コドモショクドウフランシスコノヒロバ / マゴメコマモリショクドウ / キズナクラブ / キズナカフェ / ミナミマゴメアグネスコドモショクドウ（同じ表：全国地方公共団体コード・名称・備考）
- スギナミクヤクショ / トウキョウコウゲイダイガク スギナミアニメーションミュージアム / ニシオギチイキクミンセンター / コウエンジチイキクミンセンター / エイフクイズミチイキクミンセンター / クガヤマカイカン / コミュニティフラットアサガヤ / コミュニティフラットマバシ（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・設置者・SSID・提供エリア）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 5 | address | チュウオウコウエン / ジョウスイコウエン / ツツジコウエン / アジサイコウエン / ナカジマチョウコウエン / オガワリョクチ / タケノココウエン / スズキカイドウコウエン | 全国地方公共団体コード・ID・地方公共団体名・名称・建物名等(方書)・設置位置・男性トイレ総数・男性トイレ数（小便器） | .opendata.metro.tokyo.lg.jp/kodaira/132110_public_toilet.csv |
| 8 | address | ハクサンコウエン / タキヤマコウエン / コヤマダイイセキコウエン / コウヤマドウザカコウエン / シモサトホンムライセキコウエン / ニシグチチュウオウコウエン / コヤマレンゲコウエン / チクリンコウエン | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_英語・設置位置・高度の種別・高度の値 | ata.metro.tokyo.lg.jp/higashikurume/132225_public_toilet.csv |

## G193　b055「設置者」（2 列：address 1・org 1）

多いほうの address の例：

- 杉並区 / 杉並区 / 杉並区 / 杉並区 / 杉並区 / 杉並区 / 杉並区 / 杉並区（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・SSID・提供エリア）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org | 東久留米市立図書館 / 東久留米市立図書館 / 東久留米市立図書館 / 東久留米市立図書館 / 東久留米市立生涯学習センター / 東京ドームスポーツセンター東久留米 | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・名称_英語・町字ID・建物名等(方書) | tro.tokyo.lg.jp/higashikurume/132225_public_wireless_lan.csv |

## G194　b055「公営駐輪場_説明」（2 列：category 1・text 1）

多いほうの category の例：

- コイン式 / コイン式 / コイン式 / コイン式 /  /  / コイン式 / コイン式（同じ表：公営駐輪場_全国地方公共団体コード・施設_ID・公営駐輪場_ID・公営駐輪場_名称）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text | 構造 平面;月極・一時利用;自転車月極 90;自転車一時 213;原付月極 0;原付一時 0 / 構造 立体;月極・一時利用;自転車月極 1192;自転車一時 323;原付月極 0;原付一時 0 / 構造 立体;一時利用;自転車月極 0;自転車一時 460;原付月極 0;原付一時 0 / 構造 立体;月極・一時利用;自転車月極 287;自転車一時 411;原付月極 0;原付一時 0 / 構造 平面;一時利用;自転車月極 0;自転車一時 118;原付月極 0;原付一時 0 / 構造 立体;月極・一時利用;自転車月極 1112;自転車一時 188;原付月極 49;原付一時 15 / 構造 立体;月極・一時利用;自転車月極 661;自転車一時 243;原付月極 0;原付一時 0 / 構造 平面;一時利用;自転車月極 0;自転車一時 1775;原付月極 0;原付一時 0 | 公営駐輪場_全国地方公共団体コード・施設_ID・公営駐輪場_ID・公営駐輪場_名称・公営駐輪場_最大駐輪台数 | ndata.metro.tokyo.lg.jp/musashino/132039_bicycle_parking.csv |

## G195　b055「投票区名」（2 列：id 1・address 1）

多いほうの id の例：

- 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・連結表記・投票所区分・選挙区分）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | 第1投票区 / 第2投票区 / 第3投票区 / 第4投票区 / 第5投票区 / 第6投票区 / 第7投票区 / 第8投票区 | 全国地方公共団体コード・地方公共団体名・名称・連結表記・投票所区分 | w.opendata.metro.tokyo.lg.jp/hamura/132276_polling_place.csv |

## G196　b055「名称_英語」（3 列：org 2・address 1）

多いほうの org の例：

- Central Community Center / Central Library / Nakamachi Community Center and Nakamachi Library ( Nakamachi / Kodaira City Hall Main Building 1st Floor Lobby / Eastern Branch Office / Western Branch Office / Ogawa Nishimachi Community Center / Kamijuku Community Center（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・町字ID）
- Chuo Library / Takiyama Library / Hibarigaoka Library / Tobu Library / Lifelong Learning Center / TOKYODOME Sports Center Higashi-kurume（同じ表：全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・町字ID・建物名等(方書)・設置者）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | Hakusan Park / Takiyama Park / Koyamadai Ruins Park / Kohyama Dohzaka Park / Shimosato Honmura Ruins Park / Nishiguchi Central Park / Koyama Renge Park / Chikurin Park | 全国地方公共団体コード・ID・地方公共団体名・名称・名称_カナ・設置位置・高度の種別・高度の値 | ata.metro.tokyo.lg.jp/higashikurume/132225_public_toilet.csv |

## G197　b060「Type」（2 列：category 1・account 1）

多いほうの category の例：

- Strategy / Policy / Strategy / Policy / Strategy / Policy / Strategy / Strategy（同じ表：OrganisationCode・Date Approved・Service・Portfolio・Review Date・Current?・Link）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | account | Equipment / Equipment / Print and publishing / Tax and statutory requirements / Equipment / Postage and couriers / Conferences and events / Training and development | Date・Amount | chment_data/file/451689/Sept-13-to-Aug-14-extra-gpc-data.csv |

## G198　b060「Department」（8 列：org 6・account 2）

多いほうの org の例：

- Department for Business, Innovation and Skills / Department for Business, Innovation and Skills / Department for Business, Innovation and Skills / Department for Business, Innovation and Skills / Department for Business, Innovation and Skills / Department for Business, Innovation and Skills / Department for Business, Innovation and Skills / Department for Business, Innovation and Skills（同じ表：Entity・Date of Payment・Expense Type・Expense Area・Supplier・Transaction Number・Net Total）
- DECC / DECC / DECC / DECC / DECC / DECC / DECC / DECC（同じ表：Entity・Date of Payment・Expense Type・Expense Area・Supplier・Transaction Number・Amount）
- Foreign and Commonwealth Office / Foreign and Commonwealth Office / Foreign and Commonwealth Office / Foreign and Commonwealth Office / Foreign and Commonwealth Office / Foreign and Commonwealth Office / NOTES:（同じ表：Basis for expenditure approval・Value (｣M)・Total Value Requested (｣M)・Total Value Approved (｣M)・Civil Service Grade (FTE) AA/AO・Civil Service Grade (FTE) EO・Civil Service Grade (FTE) HEO・Civil Service Grade (FTE) SEO）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | account | Environmental Health / Benefits / Section 5 / Envirocrime / Communications / Council Tax / Corporate Fraud / Licencing | OrganisationCode・EffectiveDate・FinancialYear・Payee・Language・Amount | ww.blaby.gov.uk/media/1409/translation-costs-august-2018.csv |
| 4 | account | Communities / finance / finance / finance / DCLS / Communities / Communities / Communities | MCC・date・Net Amount | en.gov.uk/media/2330/edendc01_transactionreport-april-15.csv |

## G199　b060「Body」（2 列：org 1・id 1）

多いほうの org の例：

- Bristol City council / Bristol City council / Bristol City council / Bristol City council / Bristol City council / Bristol City council / Bristol City council / Bristol City council（同じ表：Amount・Pay Date・Transaction Number）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | id | http://statistics.data.gov.uk/id/local-authority/16UF / http://statistics.data.gov.uk/id/local-authority/16UF / http://statistics.data.gov.uk/id/local-authority/16UF / http://statistics.data.gov.uk/id/local-authority/16UF / http://statistics.data.gov.uk/id/local-authority/16UF / http://statistics.data.gov.uk/id/local-authority/16UF / http://statistics.data.gov.uk/id/local-authority/16UF / http://statistics.data.gov.uk/id/local-authority/16UF | Date・Transaction Number・Amount・Supplier ID・Expense Area・Expense Type・Expense Code・Service Code | https://www.eden.gov.uk/media/2370/period_10_2012.csv |

## G200　b060「Expense Type」（18 列：account 17・id 1）

多いほうの account の例：

- Partnership Commissioned CS / Agency Practitioners / Agency Practitioners / Temp Business Support Staff / Agency Practitioners / Agency Practitioners / Temp Business Support Staff / Temp Business Support Staff（同じ表：Department Family・Entity・Date・Expense Area・Supplier・Transaction Number・Amount）
- Crown Court Very High Cost Cases / Crown Court Graduated Fee Scheme / Crown Court Graduated Fee Scheme / Crown Court Graduated Fee Scheme / Crown Court Very High Cost Cases / Crown Court Very High Cost Cases / Crown Court Graduated Fee Scheme / Crown Court Graduated Fee Scheme（同じ表：Department Family・Entity・Date・Expense Area・Supplier・Transaction Number・Amount・VAT Included）
- Other Accommodation Charges (Programme) / Other Training Costs / Hire of Agency Staff (Clerical/Secretariat/Other) / Entertaining Overseas (Programme) / Subsistence Payments- Overseas (Programme) / Other IT Costs (Programme) / Air Fares Overseas / ICT Infrastructure Specific Service (PFI)（同じ表：Department・Entity・Date of Payment・Expense Area・Supplier・Transaction Number・Net Total）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 1 | id | R4011-CCM001 / R4400-PLP105 / R4436-CCT001 / R4003-REG002 / R4401-CPK001 / R4401-TRW001 / R2700-CPK101 / R2700-FIE040 | OrganisationURI・OrganisationLabel・Organisation Unit・TransactionNumber・Invoice Ref.・Purpose・Payment Date・Amount | eltenham.gov.uk/media/a1ibfa2h/january2020_bank_payments.csv |

## G201　b060「Job/Team Function」（2 列：category 1・text 1）

多いほうの category の例：

- Post eliminated / Post eliminated / Post eliminated / Post eliminated / Post eliminated / Post eliminated / Post eliminated / Post eliminated（同じ表：Post Unique Reference・Grade・Job Title・Parent Department・Organisation・Unit・Reports to Senior Post・Salary Cost of Reports (｣)）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text | The head of the Business Group which is responsible for the / The head of the Credit Risk Group which is responsible for r / The head of the Finance Group which includes finance, busine / The General Counsel痴 Office is responsible for providing leg / The executive head of the Department, reporting to the Chai / This division is responsible for underwriting Buyer Credit f / The division is responsible for the underwriting, issue and / This division is responsible for the Environmental and Socia | Post unique reference・Grade・Job Title・Parent Department・Organisation・Unit・Reports To・Salary Costs of Reports | t_data/file/190925/senior-staff-posts-dataset-march-2012.csv |

## G202　b060「Other_Related_Themes」（2 列：text 1・category 1）

多いほうの text の例：

- Administrative area;County;Metropolitan district;Unitary aut / Plan of development site;Housing development;Plot sale / Title Register;Title Deeds;Images of deeds and documents;Gen / Title Register;Interest in Land;Non-legal charges;Non-legal / Title Register;Title Deeds;Images of deeds and documents;Spe / Index Polygon extent;Registered Title Extent / Index Polygon extent;Registered Title Extent;Local Authority / Index Polygon extents;Registered Title Extent;National Polyg（同じ表：Organisation・Dataset_Title・Abstract・Inspire_Theme・Inspire_Feature_Type・Constraints・Metadata_published_on_datagovuk・Data_Published）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category |  / Coal mining infrastructure / Operational metadata / Operational metadata / Operational metadata / Coal mining infrastructure / Operational metadata / Operational metadata | Organisation・Dataset_Title・Abstract・INSPIRE_Theme・INSPIRE_Feature_Type・Constraints・Metadata_published_on_datagovuk・Where_To_Find_More_Information | ment_data/file/797467/GC_Data_Catalogue_-_Coal_Authority.csv |

## G203　b060「Where_To_Find_More_Information」（2 列：other 1・text 1）

多いほうの other の例：

-  /  / https://www.gov.uk/get-information-about-property-and-land/c /  / https://www.gov.uk/government/publications/exempting-documen / https://use-land-property-data.service.gov.uk/datasets/nps - / https://use-land-property-data.service.gov.uk/datasets/inspi / https://use-land-property-data.service.gov.uk/datasets/nps（同じ表：Organisation・Dataset_Title・Abstract・Inspire_Theme・Inspire_Feature_Type・Other_Related_Themes・Constraints・Metadata_published_on_datagovuk）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | text | This dataset is available under Open Government Licence: htt / This dataset is available to view under Open Government Lice / This dataset is available to view under Open Government Lice / This dataset is available to view under Open Government Lice / This dataset is available to view under Open Government Lice / This dataset is available to view under Environmental Inform / This dataset is available to view under Environmental Inform / This dataset is available to view under Environmental Inform | Organisation・Dataset_Title・Abstract・INSPIRE_Theme・INSPIRE_Feature_Type・Other_Related_Themes・Constraints・Metadata_published_on_datagovuk | ment_data/file/797467/GC_Data_Catalogue_-_Coal_Authority.csv |

## G204　b060「notes」（3 列：text 2・category 1）

多いほうの text の例：

- The felling of the 3 protected trees has been consented via /  /  /  /  /  /  / The TPO T2-89 was revoked on 12th April 1995 (please see T2-（同じ表：reference・made-date・start-date・confirmed-date・end-date）
- The Bacup Town Centre Conservation Area was first designated /  /  /  /  /  /  / （同じ表：reference・geometry・start-date・designation-date・entry-date）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | II / II / II / II* / II / II / II / II | reference・listed_building・geometry・uprns・entry_date・start_date | .gov.uk/downloads/file/19315/listed-building-outline-dataset |

## G205　b062「Number of staff in delegated grades receiving an in-year NCP」（3 列：quantity 2・rate 1）

多いほうの quantity の例：

- 1180 / 0 / 1321 / 47 / 91 / 0 / 5 / 591（同じ表：Main Department・Organisation・Annual Paybill (delegated grades for fin・Headcount (delegated grades as at 31 Mar・Cost of in-year NCPRP for delegated grad・In-Year - Number of staff in delegated g・In-Year - Median NCPRP for those receivi・End of Year - Cost of end of year NCPRP）
- 1131 / 857 / 2898 / 94 / 27 / 5 / 1 / 0（同じ表：Main department・Organisation・Annual Paybill (delegated grades for fin・Headcount (delegated grades as at 31 Mar・Cost of in-year NCPRP for delegated grad・Number of staff in delegated grades rece・Median NCPRP for those receiving an in-y・Cost of end of year NCPRP for delegated）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 3 | rate | 25.90% / 2.00% / 15.00% / 19.60% / 30.70% / 23.80% / 3.10% / 0.00% | Main department・Organisation・Annual Paybill (delegated grades for fin・Headcount (delegated grades as at 31 Mar・Cost of in-year NCPRP for delegated grad・Number of staff in delegated grades rece・Median NCPRP for those receiving an in-y・Cost of end of year NCPRP for delegated | ds/system/uploads/attachment_data/file/285086/ncprp-2013.csv |

## G206　b063「Wert」（2 列：quantity 1・amount 1）

多いほうの quantity の例：

- NA / 10240 / 152513 / 91335 / 42818 / 275288 / 276323 / 118323（同じ表：Jahr・Deponietyp・Einheit）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | amount | 44445966754.09931 / 45213068201.47224 / 48691273509.50475 / 53154938765.891846 / 52104361215.42215 / 53136735491.91763 / 51749555387.060326 / 54899558375.98117 | Stichtag・Kennzahl | https://catalog.opendata.li/store/13/resource/72 |

## G207　b063「Titel」（7 列：text 6・org 1）

多いほうの text の例：

- Abgabe von Tierkadavern für Gewebeentnahmen und Ausbildungsz / Akute orale Toxizität an Ratten und Mäusen, OECD 423, Indust / Analyse génétique de facteurs essentiels du complexe Hsp90 c / Analysis of neurogenesis in embryonic and adult mice by cond / Application of Fibrin Glue for Aneurysm Occlusion in a Micro / Biomedical Microrobotics (in collaboration with the Institut / Comparison of hypertonic saline and mannitol on in vitro who / Die Bedeutung von Nagergemeinschaften für die Übertragung vo（同じ表：Fachgebiet・Versuchszweck・Tierart・Summe von SG 0・Summe von SG 1・Summe von SG 2・Summe von SG 3）
- Bundesbeschluss vom 19. Juni 2026 über die Zusatzfinanzierun / Nachtrag zum Gesetz über die soziale Sicherung und Integrati / Erneuerungswahl Kreisgericht Toggenburg: nebenamtliche Richt / III. Nachtrag zum Gesetz über die soziale Sicherung und Inte / Erneuerungswahl Kreisgericht Werdenberg-Sarganserland: neben / Volksinitiative «Für eine Einschränkung von Feuerwerk» / Volksinitiative «Ja zu fairen Bundessteuern auch für Ehepaar / Änderung vom 19. Dezember 2025 des Bundesgesetzes über das K（同じ表：Datum・Verwaltungsebene・Typ・Status・Total der Gemeinden・Ausgezählte Gemeinden・Letzte Änderung・Stimmbeteiligung）
- Bericht «Sonderpädagogik der St.Galler Volksschule» / VII. und VIII. Nachtrag zum Gesetz über Referendum und Initi / Sammelvorlage zur Umsetzung von parlamentarischen Vorstössen / Bewegungs- und Sportförderungsgesetz / IV. Nachtrag zur Verordnung zum Einführungsgesetz zur eidgen / Übersicht Vernehmlassungen / VII. Nachtrag zum Sozialhilfegesetz / II. Nachtrag zum Gesetz über das Öffentlichkeitsprinzip der（同じ表：Link・Veröffentlicht）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org | Parkhaus City / Parkhaus Europe / Parkhaus Rebgasse / Parkhaus Aeschen / Parkhaus Claramatte / Parkhaus Centralbahn / Parkhaus Bahnhof Süd / Parkhaus Elisabethen | Publikationszeit・Anzahl frei・Total・Anteil frei・Auslastung・Auslastung in Prozent・Link・geo_point_2d | h/api/v2/catalog/datasets/100088/exports/csv?use_labels=true |

## G208　b063「value」（2 列：other 1・amount 1）

多いほうの other の例：

- 10 / 10 / 10 / 10 / 10 / 10 / 10 / 10（同じ表：monitoring_program・station_number・latidude・date_of_probing・parameter_type・lower_LOD・unit）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | amount | 12958860367.92 / 3311818203.61 / 3674632983.64 / 16149934595.31 / 6410324420.9 / 5630602017.71 / 3901317329.87 / 7231329921.51 | arten・jahr・dim・hh・unit・model | h/static/assets/datasets/fs_dashboard/standardauswertung.csv |

## G209　b063「richtung」（2 列：text 1・category 1）

多いほうの text の例：

- vom Kreisel Spange Ost / vom Kreisel Spange Ost / von Weinfelden / von Weinfelden / nach Weinfelden / nach Weinfelden / vom Marktplatz / vom Marktplatz（同じ表：code・gemeinde・spur_code・reg_bus・datum・zeit_von・zeit_bis・jahr）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | N / N / S / O / S / O / N / W | gemeinde_bfs_nr・gemeinde・anlage_nr・anlage_typ・zeit_von・zeit_bis・spur_nr・lat | tistik.zh.ch/ogd/daten/ressourcen/KTZH_00003043_00006325.csv |

## G210　b064「Titel」（5 列：text 4・org 1）

多いほうの text の例：

- Veranstaltungen im Raum St. Jakob / Aktueller Covid-19 Impfstand Im Kanton Basel-Stadt / Artikel im Dossier Basel Nr. 101 / Interaktive Grafiken / Veränderte Wahllisten Auswertung / Temperatur-Trend im Grundwasser von Basel / Logiernachtdaten von Hotels in Basel-Stadt / Abfuhrtermine Basel zu Kalender hinzufügen（同じ表：Beschreibung・Erstellt am・Thumbnail・Themen・Entwickler・Titel Datensatz・Link zum Datensatz・Datensatz ID）
- Beethoven, Ludwig van: Quittung über 600 Gulden / Paganini, Niccolò: Preludio a Mr Burgermaitre Francke / Strauss, Richard an Schmitt, Peter Paul; Korrespondenz / Dvořák, Antonín: Visitenkarte / Schwind, Moritz von an N.N. / Leibniz, Gottfried Wilhelm an Burnett of Kemney, Thomas; Kor / Volta, Alessandro: Quittung f. Zahlungsempfang / Ørsted, Hans Christian an Weber, Wilhelm (Göttingen)（同じ表：ID・Signatur・AutorIn・Ort・Datierung_von・Datierung_bis・Datierung_Bemerkung・Illustration）
- Calancatal, Frau in Bündner Tracht, Gesamtansicht / Oberaargletscher, Panorama, Bergsteigen / Linthal, Landschaft / Fridolinshütte, Landschaft / Reusstal, Panorama / Etzlital, Landschaft / Chli Schärhorn, Panorama / Bedrettotal, Ortsgesamtansicht（同じ表：ID・Signatur・FotografIn・Inhalt_Kurzbeschreibung・Datierung_von・Datierung_bis・Datierung_Bemerkung・Farbe）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | org | Parkhaus Storchen / Parkhaus Storchen / Parkhaus Elisabethen / Parkhaus Messe / Parkhaus Kunstmuseum / Parkhaus Steinen / Parkhaus Europe / Parkhaus Rebgasse | Publikationszeit・Anzahl frei・Total Plätze・Anteil belegter Parkplätze・id・id2・link・geo_point_2d | h/api/v2/catalog/datasets/100014/exports/csv?use_labels=true |

