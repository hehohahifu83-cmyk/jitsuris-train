# 新しい公開元の組織・コード・ライセンス対応（2026-10-26）

## 範囲

カタログの組織一覧、組織ID、団体コード、ライセンス欄・利用規約の**メタデータだけ**を確認した。データセットの行、CSV、DataStore、ダウンロードファイルは取得していない。公開元の追加、ライセンスの採用、教材への取り込み、`allowed_hosts.json`・`allocation.json`・`pipeline.py` の変更はしていない。

横浜市・神戸市は主セット、神奈川県は eval2 の公開元として、この調査から除外した。下記のコード表は組織とコードの照合用であり、教材に使う前に各組織を現行の割当規則で個別確認する。

## 日本

### 仙台市

公式カタログの組織一覧は29組織。ページ1と2の表示を転記した。各ページのデータセット数の合計は16。カタログ内の10桁表示IDは部局を識別する内部IDで、地方公共団体コードではない。すべて仙台市の部局・機関なので、対応する地方公共団体コードは **041009**。

| カタログ内表示ID | 組織 |
| --- | --- |
| 0101000000 | 危機管理局 |
| 0103000000 | 総務局 |
| 0104000000 | まちづくり政策局 |
| 0107000000 | 財政局 |
| 0110000000 | 市民局 |
| 0115000000 | 健康福祉局 |
| 0117000000 | こども若者局 |
| 0120000000 | 環境局 |
| 0124000000 | 経済局 |
| 0125000000 | 文化観光局 |
| 0127000000 | 都市整備局 |
| 0131000000 | 建設局 |
| 0141000000 | 青葉区 |
| 0142000000 | 宮城野区 |
| 0143000000 | 若林区 |
| 0144000000 | 太白区 |
| 0145000000 | 泉区 |
| 0151150000 | 会計室 |
| 0283000000 | 水道局 |
| 0385000000 | 交通局 |
| 0487000000 | ガス局 |
| 0579000000 | 議会事務局 |
| 0600000000 | 選管委員会 |
| 0772000000 | 監査事務局 |
| 0857000000 | 教育局 |
| 1000000000 | 人事委員会 |
| 1154000000 | 消防局 |
| 2081000000 | 市立病院 |
| 2100000000 | 農業委員会 |

**ライセンス対応：** 組織単位の共通ライセンスは確認できない。仙台市の案内は、データごとに表示されるクリエイティブ・コモンズ・ライセンスを利用前に確認するよう求めている。よって採用時は、個々のデータセットの `license_id`／ライセンス表示と提供元を確認する。

### 山口県オープンデータカタログ

組織一覧は県・市町の計20組織。カタログ内IDは6桁の全国地方公共団体コードから末尾の検査数字を除いた5桁で表示されている。下表の完全なコードはJ-LISの一覧と照合した。

| カタログ内ID | 組織 | 全国地方公共団体コード |
| --- | --- | --- |
| 35000 | 山口県 | 350001 |
| 35201 | 下関市 | 352012 |
| 35202 | 宇部市 | 352021 |
| 35203 | 山口市 | 352039 |
| 35204 | 萩市 | 352047 |
| 35206 | 防府市 | 352063 |
| 35207 | 下松市 | 352071 |
| 35208 | 岩国市 | 352080 |
| 35210 | 光市 | 352101 |
| 35211 | 長門市 | 352110 |
| 35212 | 柳井市 | 352128 |
| 35213 | 美祢市 | 352136 |
| 35215 | 周南市 | 352152 |
| 35216 | 山陽小野田市 | 352161 |
| 35305 | 周防大島町 | 353051 |
| 35321 | 和木町 | 353213 |
| 35341 | 上関町 | 353418 |
| 35343 | 田布施町 | 353434 |
| 35344 | 平生町 | 353442 |
| 35502 | 阿武町 | 355020 |

**ライセンス対応：** カタログ利用ルールはPDL1.0と互換のCC BY利用を認めるが、第三者権利・個別法令・別ルールの適用対象などの例外を明記している。APIのデータセット例では `organization.name` が上表の5桁ID、`license_id` と `license_url` が個別ライセンスとして返る。県の団体IDを一括適用せず、メタデータ上の提供組織でコードを引き、個別ライセンス欄を確認する。市町別の一覧データ自体にも市区町村コード欄がある。

## ニュージーランド・リオ州・英国

カタログ組織一覧とライセンス内訳は、いずれもデータセットの**メタデータ集計**で作る。個別ライセンスの混在があるため、サイト共通の利用規約だけで採否を決めない。

| カタログ | 組織一覧・件数 | ライセンスのメタデータと確認できた内訳 |
| --- | --- | --- |
| New Zealand data.govt.nz | CKAN APIを使用。公式ガイドにJSON APIと `package_search` のページ分割例がある。今回、組織名の全件一覧は取得していない。 | APIで見たデータ・メタデータには、各データセットのダウンロード版と同じライセンスが適用される。個別の件数内訳は未集計。 |
| リオ州 Portal de Dados Abertos | 公式ホームページは99組織、約1.1k件。組織ディレクトリの別スナップショットは98組織、データセット一覧は1,136件だった。更新時点／ページ間で1組織の差があるため、最終数はAPIで再確認が必要。今回、全組織名の取得は未完了。 | カタログのライセンス欄で595件が「未指定」と表示されたスナップショットを確認。ライセンス表示例に `cc-by`、`cc-zero`、`odc-pddl`、`other-pd` があるが、未指定以外の全件数は未集計。 |
| UK data.gov.uk / National Data Library | 現行ディレクトリは Publisher フィルターを提供。公式API資料はCKANの `organization_list` を案内する。今回、組織名の全件一覧は取得していない。 | 公式のCKAN項目仕様はデータ単位の `license_id` を定義し、例として `uk-ogl` と OS OpenData Licence を挙げる。全ライセンスの件数は未集計。 |

### メタデータだけで全件一覧・ライセンス件数を再現するAPI手順

CKANの公式APIでは `organization_list` で組織名を取得し、`package_search` の `rows=0` と `facet.field=license_id` でライセンス別件数を集計できる。組織別の内訳は、各組織を `fq=organization:<組織ID>` で絞って同じファセットを取得する。これならデータセット行・リソース内容を取得しない。

- New Zealand: `https://catalogue.data.govt.nz/api/3/action/organization_list`、`https://catalogue.data.govt.nz/api/3/action/package_search`
- Rio: `https://dadosabertos.rj.gov.br/api/3/action/organization_list`、`https://dadosabertos.rj.gov.br/api/3/action/package_search`
- UK: `https://data.gov.uk/api/action/organization_list`、`https://data.gov.uk/api/action/package_search`

## 参照した公式ページ

- 仙台市組織一覧（ページ1・2）：[組織](https://data.city.sendai.jp/organization)、[ページ2](https://data.city.sendai.jp/organization/?page=2&q=&sort=)
- 仙台市オープンデータのライセンス案内：[オープンデータとは](https://www.city.sendai.jp/joho-kikaku/shise/security/kokai/opendata.html)
- 仙台市コード：[J-LIS 宮城県内市町村](https://www.j-lis.go.jp/spd/code-address/touhoku/cms_12514180.html)
- 山口県カタログ：[団体一覧](https://yamaguchi-opendata.jp/ckan/organization)、[API説明](https://yamaguchi-opendata.jp/www/api-manual.html)、[利用ルール](https://yamaguchi-opendata.jp/www/terms.html)
- 山口県コード：[J-LIS 山口県内市町](https://www.j-lis.go.jp/spd/code-address/chuugoku/cms_15614184.html)
- New Zealand：[API guide](https://www.data.govt.nz/catalogue-guide/using-data-govt-nz-apis)、[dataset metadata API](https://data.govt.nz/catalogue-guide/using-data-govt-nz-apis/accessing-dataset-metadata-via-api)
- Rio：[Portal](https://dadosabertos.rj.gov.br/)、[organization directory](https://dadosabertos.rj.gov.br/pt_BR/organization/)、[dataset directory](https://dadosabertos.rj.gov.br/pt_BR/dataset/)
- UK：[API documentation](https://guidance.data.gov.uk/get_data/api_documentation/)、[accepted CKAN fields](https://guidance.data.gov.uk/publish_and_manage_data/harvest_or_add_data/harvest_data/ckan/)、[current directory](https://www.data.gov.uk/search)
- CKAN API reference：[API Guide](https://docs.ckan.org/en/latest/api/)

## 残っている確認

NZ・Rio・UKの組織全件と正確なライセンス件数はこの資料では未取得。上記のAPIでメタデータだけを集計して追記する。特にRioはカタログの組織総数に差があり、確認前に公開元登録やライセンス採用を進めない。
