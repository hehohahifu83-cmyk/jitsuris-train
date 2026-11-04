# Shirasagi 提供元対応表の下書き（Codex、2026-11-05）

6サイト・一覧8,649件の全範囲を確認した。取得できたメタデータ8,647件、API取得不可2件。author / user.id / user.name の組（個人名等を非保存へ射影したもの）と取得不可を計926行にまとめた。資料ファイルは取得していない。
**下書きであり登録済み・採用済みではない。** 自治体候補がある組も、Claudeが個別の根拠と実際の提供元を確認してから登録する。

## ファイル

- `research/catalogs/shirasagi_owner_crosswalk_draft_20261105.tsv`：全組の3フィールド、件数、自治体、6桁コード、allocation、理由、根拠URL。
- 同名JSON：上記に所属の文字列・県の組織ページ・確認した部署リンク・代表ページの確認結果・競合しないフィールド案・重複を減らした確認順を付加。
- `shirasagi_owner_inventory_20261105.json`：非保存へ射影した組別件数、ページごとの取得URL/応答SHA、全件確認の成否。共用ダウンロードホストは一覧化せず、外部資料の有無/件数だけを保持。
- `shirasagi_official_organizations_20261105.json`：6県の公式組織ページと部署リンク。徳島の応答はJSONのstatic_htmlを読む。
- `shirasagi_owner_evidence_20261105.json`：静岡の全件集計と並行アクセスしないため、ほか5サイト57自治体の代表メタデータページを確認。57件すべて取得・自治体名の掲載を確認。全組のHTMLを確認したという意味ではない。

## サイト別集計

|サイト|データセット|組|自治体候補あり|不明|既存割り当て等も含む除外|自治体数（候補）|
|---|---:|---:|---:|---:|---:|---:|
|https://opendata.pref.aomori.lg.jp|1065|79|75|4|4|7|
|https://opendata.pref.shizuoka.jp|3800|385|106|279|281|35|
|https://odp-pref-tottori.tori-info.co.jp|263|106|96|10|10|16|
|https://opendata.pref.tokushima.lg.jp|1932|230|166|64|64|25|
|https://opendata.pref.kagawa.lg.jp|613|74|70|4|4|8|
|https://www.pref.ehime.jp/opendata-catalog|976|52|40|12|12|1|

「候補あり」は所有者の確定数ではない。不明 373 組、既存割り当て等を合わせた除外 375 組。
同じフィールド値に別自治体・不明・除外の組が1つでもあれば、単独フィールドの登録案にはしない。全件未完のサイトからも登録案を出さない。
競合しないフィールド案 715 件、重複を減らした確認順 255 件。自動生成したallowed_hostsの設定ではない。

## 対応を決める根拠と限界

- authorに自治体名が明記された組、user.nameに自治体名が明記された組、部署名と一致する県の階層付き所属がある組を候補とした。投稿者名は所有者と必ず同じとは限らず、理由欄に要確認と記した。
- 上流Shirasagiの[author_nameの実装](https://github.com/shirasagi/shirasagi/blob/d00506f6dd3736035e5c2e1fceb5d5578cac6288/app/models/opendata/dataset.rb)はcontact/memberだけでなくgroups名からもauthorを生成する。配備版が同じとは確認していないが、authorを常に実提供者とみなさない。県名だけのauthorで投稿者の所属も未確定なら不明にした。
- groupsに県名だけがある、areasに市町名がある、カタログが県のサイトである、という理由だけでは帰属させない。県名のauthorに外部ファイルがある組は市町転載を否定できないので不明とした。個別の市町名と県の投稿者が併存する場合、author側の明示された市町を候補とし、その投稿者IDの他自治体利用も全件照合する。
- 青森県と鳥取県の「南部町」は別自治体（024457 / 313891）。国全体で名前だけを一意と見なさず、カタログの県と所属を照合した。
- 県の部局は県のコードにまとめ、部局単位でallocationを作らない。コードは既存 `materials/dict/jp_municipalities.json` と検査数字で確認。自治体の確定一覧でも新規train一覧でもない。
- allocationは既存の別名を解決してmain/hold/eval2/eval3などの印を付けた。未登録は未登録のままにし、trainと推測していない。仙台・F1自治体・新宿区の保護を緩めていない。
- 個人名・連絡先・ログイン名など、組織名だと確実に扱えない値は `[非保存]`。非保存へ射影後に同じ3フィールドとなる組は統合し、件数の合計を維持する。`privacy_redacted_fields`で明示し、非保存の文字列をフィールド案に使わない。原APIのユーザーオブジェクトやメールは保存していない。
- 根拠のデータセットURLは元APIが返した数値idに対応する公開ページ。県の部署は実際に読んだ公式組織ページ/一致した部署リンクも併記した。部署の改組・古い所属名・県の代理投稿があるので、各行の判断はClaudeの確認が必要。

## 自治体候補と現在の割り当て

|カタログ|自治体|6桁コード|現在のallocation|組|データセット|
|---|---|---|---|---:|---:|
|https://odp-pref-tottori.tori-info.co.jp|三朝町|313645|未登録|2|3|
|https://odp-pref-tottori.tori-info.co.jp|伯耆町|313904|未登録|3|4|
|https://odp-pref-tottori.tori-info.co.jp|倉吉市|312037|未登録|1|1|
|https://odp-pref-tottori.tori-info.co.jp|北栄町|313726|未登録|1|1|
|https://odp-pref-tottori.tori-info.co.jp|南部町|313891|未登録|2|14|
|https://odp-pref-tottori.tori-info.co.jp|境港市|312045|未登録|4|4|
|https://odp-pref-tottori.tori-info.co.jp|大山町|313866|未登録|1|2|
|https://odp-pref-tottori.tori-info.co.jp|日南町|314013|未登録|1|1|
|https://odp-pref-tottori.tori-info.co.jp|日吉津村|313840|未登録|1|1|
|https://odp-pref-tottori.tori-info.co.jp|日野町|314021|未登録|1|2|
|https://odp-pref-tottori.tori-info.co.jp|智頭町|313289|未登録|1|1|
|https://odp-pref-tottori.tori-info.co.jp|湯梨浜町|313700|未登録|1|2|
|https://odp-pref-tottori.tori-info.co.jp|琴浦町|313718|未登録|1|2|
|https://odp-pref-tottori.tori-info.co.jp|米子市|312029|未登録|2|11|
|https://odp-pref-tottori.tori-info.co.jp|鳥取市|312011|未登録|28|47|
|https://odp-pref-tottori.tori-info.co.jp|鳥取県|310000|未登録|46|151|
|https://opendata.pref.aomori.lg.jp|むつ市|022080|未登録|1|41|
|https://opendata.pref.aomori.lg.jp|三戸町|024414|未登録|1|3|
|https://opendata.pref.aomori.lg.jp|十和田市|022063|未登録|1|14|
|https://opendata.pref.aomori.lg.jp|南部町|024457|未登録|3|52|
|https://opendata.pref.aomori.lg.jp|平川市|022101|未登録|2|22|
|https://opendata.pref.aomori.lg.jp|階上町|024465|未登録|1|1|
|https://opendata.pref.aomori.lg.jp|青森県|020001|未登録|66|921|
|https://opendata.pref.kagawa.lg.jp|さぬき市|372064|未登録|1|1|
|https://opendata.pref.kagawa.lg.jp|三豊市|372081|未登録|3|24|
|https://opendata.pref.kagawa.lg.jp|丸亀市|372021|未登録|1|4|
|https://opendata.pref.kagawa.lg.jp|善通寺市|372048|未登録|1|10|
|https://opendata.pref.kagawa.lg.jp|宇多津町|373869|未登録|3|3|
|https://opendata.pref.kagawa.lg.jp|直島町|373648|未登録|1|1|
|https://opendata.pref.kagawa.lg.jp|観音寺市|372056|未登録|1|1|
|https://opendata.pref.kagawa.lg.jp|香川県|370002|未登録|59|559|
|https://opendata.pref.shizuoka.jp|三島市|222062|hold|2|64|
|https://opendata.pref.shizuoka.jp|下田市|222194|未登録|1|5|
|https://opendata.pref.shizuoka.jp|伊東市|222089|未登録|2|175|
|https://opendata.pref.shizuoka.jp|伊豆の国市|222259|未登録|2|10|
|https://opendata.pref.shizuoka.jp|伊豆市|222224|未登録|3|38|
|https://opendata.pref.shizuoka.jp|函南町|223255|未登録|2|15|
|https://opendata.pref.shizuoka.jp|南伊豆町|223042|未登録|1|11|
|https://opendata.pref.shizuoka.jp|吉田町|224243|未登録|1|5|
|https://opendata.pref.shizuoka.jp|富士宮市|222071|未登録|2|93|
|https://opendata.pref.shizuoka.jp|富士市|222101|未登録|5|57|
|https://opendata.pref.shizuoka.jp|小山町|223441|未登録|2|21|
|https://opendata.pref.shizuoka.jp|島田市|222097|未登録|1|1|
|https://opendata.pref.shizuoka.jp|川根本町|224294|未登録|2|8|
|https://opendata.pref.shizuoka.jp|御前崎市|222232|未登録|3|18|
|https://opendata.pref.shizuoka.jp|御殿場市|222151|未登録|2|111|
|https://opendata.pref.shizuoka.jp|掛川市|222135|未登録|2|13|
|https://opendata.pref.shizuoka.jp|東伊豆町|223018|未登録|1|12|
|https://opendata.pref.shizuoka.jp|松崎町|223051|未登録|1|10|
|https://opendata.pref.shizuoka.jp|森町|224618|未登録|2|40|
|https://opendata.pref.shizuoka.jp|河津町|223026|未登録|3|41|
|https://opendata.pref.shizuoka.jp|沼津市|222038|未登録|2|208|
|https://opendata.pref.shizuoka.jp|浜松市|221309|未登録|2|3|
|https://opendata.pref.shizuoka.jp|清水町|223417|未登録|1|3|
|https://opendata.pref.shizuoka.jp|湖西市|222216|未登録|2|13|
|https://opendata.pref.shizuoka.jp|焼津市|222127|未登録|2|40|
|https://opendata.pref.shizuoka.jp|熱海市|222054|未登録|1|69|
|https://opendata.pref.shizuoka.jp|牧之原市|222267|未登録|1|14|
|https://opendata.pref.shizuoka.jp|磐田市|222119|未登録|3|35|
|https://opendata.pref.shizuoka.jp|菊川市|222241|未登録|2|155|
|https://opendata.pref.shizuoka.jp|藤枝市|222143|未登録|3|9|
|https://opendata.pref.shizuoka.jp|袋井市|222160|未登録|4|7|
|https://opendata.pref.shizuoka.jp|裾野市|222208|未登録|2|18|
|https://opendata.pref.shizuoka.jp|西伊豆町|223069|未登録|1|17|
|https://opendata.pref.shizuoka.jp|長泉町|223425|未登録|1|1|
|https://opendata.pref.shizuoka.jp|静岡県|220001|未登録|39|133|
|https://opendata.pref.tokushima.lg.jp|つるぎ町|364681|未登録|3|4|
|https://opendata.pref.tokushima.lg.jp|三好市|362085|未登録|2|2|
|https://opendata.pref.tokushima.lg.jp|上勝町|363022|未登録|3|4|
|https://opendata.pref.tokushima.lg.jp|上板町|364053|未登録|1|3|
|https://opendata.pref.tokushima.lg.jp|佐那河内村|363219|未登録|2|3|
|https://opendata.pref.tokushima.lg.jp|勝浦町|363014|未登録|1|1|
|https://opendata.pref.tokushima.lg.jp|北島町|364029|未登録|6|13|
|https://opendata.pref.tokushima.lg.jp|吉野川市|362051|未登録|4|4|
|https://opendata.pref.tokushima.lg.jp|小松島市|362034|未登録|4|25|
|https://opendata.pref.tokushima.lg.jp|徳島市|362018|未登録|8|36|
|https://opendata.pref.tokushima.lg.jp|徳島県|360007|未登録|91|957|
|https://opendata.pref.tokushima.lg.jp|東みよし町|364894|未登録|2|4|
|https://opendata.pref.tokushima.lg.jp|松茂町|364011|未登録|2|4|
|https://opendata.pref.tokushima.lg.jp|板野町|364045|未登録|1|2|
|https://opendata.pref.tokushima.lg.jp|海陽町|363880|未登録|3|5|
|https://opendata.pref.tokushima.lg.jp|牟岐町|363839|未登録|4|5|
|https://opendata.pref.tokushima.lg.jp|石井町|363413|未登録|5|7|
|https://opendata.pref.tokushima.lg.jp|神山町|363421|未登録|2|7|
|https://opendata.pref.tokushima.lg.jp|美波町|363871|未登録|1|1|
|https://opendata.pref.tokushima.lg.jp|美馬市|362077|未登録|5|11|
|https://opendata.pref.tokushima.lg.jp|藍住町|364037|未登録|2|3|
|https://opendata.pref.tokushima.lg.jp|那賀町|363685|未登録|3|4|
|https://opendata.pref.tokushima.lg.jp|阿南市|362042|未登録|6|13|
|https://opendata.pref.tokushima.lg.jp|阿波市|362069|train|1|6|
|https://opendata.pref.tokushima.lg.jp|鳴門市|362026|未登録|4|25|
|https://www.pref.ehime.jp/opendata-catalog|愛媛県|380008|未登録|40|202|

## 確認方法

独自APIのpackage_searchをrows/startで全件取得。ホストごとに直列・応答後2秒以上空ける。静岡は50件単位、ほかは100件単位。
静岡は900件目付近のページで12秒timeoutを繰り返したため、メタデータ取得だけ45秒に延長。2550件目以降のHTTP500ではページサイズを半減して原因の位置を絞り、1件単位でも取得不可なら不明・除外として記録し先へ進む。各ページサイズで最大3回まで再試行。
APIのcount、組別件数の合計、ページの到達範囲、取得不可の件数を照合した。静岡は途中結果を保持して再開しており、再開前後を通したUUID集合の一意性は未確認（区間内では重複を確認）。全件取得不可のサイトから単独フィールドの登録案は出さない。全文/資料/連絡先は保存しない。

`python research/catalogs/shirasagi_owner_inventory.py` / `shirasagi_official_orgs.py` / `shirasagi_owner_crosswalk_draft.py` で再作成可能。
代表ページの確認は `python research/catalogs/shirasagi_owner_evidence.py --skip-shizuoka`（その後draftを再生成）。

専用8試験成功（個人名・連絡先非保存、部署/自治体名保持、件数/安全な射影、timeout再試行、ページ重複）。シート7試験成功。
静岡の取得不可2件はstart=2584/2644（0始まり）のHTTP500。APIの一覧位置は永続的な資料識別子ではない。静岡は全件取得できていないので単独フィールド案を出していない。

下書きの再生成が同一SHAになること、コード検査数字、組の合計、登録案の全組で自治体一致/非除外を確認。
allowed_hosts・allocation・NATIONAL・採用・収集依頼・学習は変更していない。
