# CKAN以外の自治体カタログ調査（Codex、2026-11-05）

公的な自治体一覧CSVを元に、県単位の共同ポータルを優先して**メタデータだけ**を調査した。登録・採用・割り当て・表の本体取得はしていない。許可ホストの追加もしていない。

元一覧：`materials/pool/probe/jp_catalogs_20261104.json` の3公的一覧CSV・5,909参照・2,438基点。前のCKAN判定がfalseのホストについて、県の参照先と共同サイトのパターンを選び128参照先・65ホストを調査。128件中70件のページを取得できた。同一ホストの別参照も含み、全国の非CKANサイトを網羅した数ではない。前のCKAN判定falseは「CKANではない」と確定した意味ではない。

## 優先候補：独自APIでファイルURLと個別ライセンスを実証

下表のデータセット数は公開画面の**カタログ全体の表示値**。市町村ごと・trainごとの件数ではない。組織欄はHTMLで確認できた**異なる自治体名へのリンク数**で、公開元登録数・実際のデータ提供者数と同一とは限らない。0件しか抽出できなかったサイトは「未確認」とする。

|優先|サイト|方式・メタデータ入口|データセット数|確認した自治体名リンク|実応答の根拠|
|---|---|---|---:|---:|---|
|1|[静岡](https://opendata.pref.shizuoka.jp/)|独自 `/api/package_list` → `/api/package_show?id=…`|3,802|36（県＋市町）|package_listで3,802件。showはCSV/XLSX URLと`resources[].license.name=表示（CC BY）`|
|1|[青森](https://opendata.pref.aomori.lg.jp/)|独自 `/api/package_list` → `/api/package_show?id=…`|1,065|41（県＋40市町村）|showでPDF URLと個別CC BYを取得。CSVは画面に654資源と表示されるが、今回のshow標本はPDF|
|1|[徳島](https://opendata.pref.tokushima.lg.jp/)|独自 `/api/package_list` → `/api/package_show?id=…`|1,932|22|package_listで1,932件。showはCSV URLと個別CC BY|
|2|[鳥取](https://odp-pref-tottori.tori-info.co.jp/)|詳細ページ公開の `/api/package_show?id=…`|263|未確認|showはCSV URLと個別CC BY|
|2|[香川](https://opendata.pref.kagawa.lg.jp/)|詳細ページ公開の `/api/package_show?id=…`|613|未確認|showは`open_data_list.csv` URLと個別CC BY。本体CSVは未取得|
|2|[愛媛](https://www.pref.ehime.jp/opendata-catalog/)|独自 `/api/package_list` → `/api/package_show?id=…`|976|1（県のみ抽出）|showは鬼北町のCSV URLと個別CC BY。リンク数1を「提供者が県だけ」と解釈しない|

これらはShirasagi系に共通する独自APIの形式。CKANの `/api/3/action/…` とは違う。`name`が題名、`uuid`と数値`id`が別、`areas/groups`が地域や分類、ライセンスはデータセットの`license_id`でなく**各`resources[].license`のオブジェクト**。CKANのコードへURLだけ差し替えると、ID・題名・許諾の判定を誤る。専用アダプターを足すなら、この違いを扱う必要がある。実証した許諾は標本リソースだけであり、全件が許可ライセンスとは主張しない。

APIの案内例：[静岡](https://opendata.pref.shizuoka.jp/webapi.html)、[青森](https://opendata.pref.aomori.lg.jp/webapi.html)、[愛媛](https://www.pref.ehime.jp/opendata-catalog/webapi.html)。静岡には外部の`static.hamamatsu.odpf.net`、愛媛には町のサイトのファイルもあり、将来の取得先登録は別途要る。今回このドメインを許可していない。

## HTML・一覧CSVの候補

|サイト|データセット数|自治体名リンク数|機械で確認できたもの・残る確認|
|---|---:|---:|---|
|[島根](https://shimane-opendata.jp/)|504|20|DataEye系HTML、`/datasets/<id>`から`/resources/<id>`への一覧を抽出。これは資源のメタデータページへのURLで、直接ファイルURLとは数えない。個別の許諾・直接ファイルの解決は未検証|
|[宮城DataEye](https://miyagi.dataeye.jp/)|349（資源1,166）|36|DataEye系HTML、資源メタデータページへのリンク。サイト規約は特記なしCC BY 4.0。個別の直接ファイルURLの解決は未検証。仙台市を含むので評価の公開元との重なりに注意|
|[広島DataEye](https://hiroshima-opendata.dataeye.jp/)|932（資源4,598）|39|DataEye系HTML、資源メタデータページへのリンク。サイト規約は原則PDL1.0。個別の直接ファイルURLの解決は未検証|
|[北海道HARP](https://www.harp.lg.jp/opendata/)|1,592|未確認|Shirasagi表記・CSV直リンクと規約CC BY 4.0あり。公開されたWEBAPIリンクはタイムアウト（手元はHTTP200の404画面）。APIが使えると断定しない|
|[宮城県の一覧CSV](https://www.pref.miyagi.jp/documents/5880/od_20260325.csv)|187行|一覧内の提供元数は未集計|「掲載データセット一覧」と明示されたメタデータCSVだけ取得。列は`地方公共団体名`・`タイトル`・`URL`・`データ形式`・`ライセンス`等。表のURLと許諾を機械で得られる。2026-03-25版であり最新DataEye件数とは別|
|[山梨](https://www.pref.yamanashi.jp/opendata/catalog/)|9,531（検索画面の件数）|未確認|独自HTML検索。件数の単位がデータセットか資源か未確認。個別ファイル/許諾の機械抽出は未検証|

## CKANの前面サイトだった例・取得できなかった例

- [秋田のAPI案内](https://opendata.pref.akita.lg.jp/information-api) はCKAN APIを案内。非CKANに見えた前面サイトをそのまま別方式とは数えない。
- [神奈川のAPI案内](https://opendata.pref.kanagawa.jp/api) は別ホスト`catalog.opendata.pref.kanagawa.jp/api/3/action/…`を案内。表示818件。前面とAPI基点が違う例。公開元の割り当てを確認するまでtrainに足さない。
- 今回、DKAN専用APIが実際に使えるサイトは確認できなかった。全国に存在しないとは主張しない。
- 埼玉・石川・岡山の一部等は403。静岡の重複参照先の一部は429。同一ホストの複数URLを12並列で調べた影響もあり得る。再調査はホスト単位にまとめ、低頻度にする。403/429を非対応と判定しない。
- 長野・山口の旧基点はTLS設定のエラー。TLS検証を緩めていない。旧URLの404/DNS失敗もある。

## 次にClaudeが判断すること

1. 静岡・青森・徳島の独自APIアダプターを優先すると、一度の対応で複数県の共同サイトへ広げられる。先に**実際のデータ提供自治体をメタデータから区別**し、既存train/main/eval/holdとの重なりを確認する。自治体リンクがあるだけで登録済み公開元数に数えない。
2. アダプターはmetadataの`name/uuid/resources[].license`、外部のファイルホスト、同じ表の年度違い、既存使用ID、残り15表上限を扱う。ライセンスの一括仮定はしない。
3. DataEyeはHTMLから資源メタデータページまでを確認した段階。直接ファイルの解決を確認してから対応工数を見積もる。
4. 調査だけを依頼されたため、アダプター・登録・採用・新規収集は実施していない。

根拠JSON：`research/catalogs/nonckan_probe_20261105.json`・`nonckan_detail_20261105.json`・`nonckan_api_20261105.json`。コードは同じディレクトリの3スクリプト。Actions run [41860617475](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/41860617475)・[41861015217](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/41861015217)・[41861498859](https://github.com/hehohahifu83-cmyk/jitsuris-train/actions/runs/41861498859) が成功。
