# 新しい公開元の下調べ（2026-10-26）

## 範囲と確認方法

Claude の依頼に基づき、公開元のカタログ画面・公式 API 説明・利用規約に載るメタデータだけを確認した。CSV、DataStore の行、ダウンロードファイルは取得していない。API の JSON エンドポイントは実行していないため、以下の「APIあり」は公式資料に記載があるという意味で、匿名アクセスの実動作を検証したものではない。件数は各カタログが表示する概数で、更新・検索条件により変わる。個人単位の記録が含まれるかは、行データを見ないと判定できないため、候補の採用前にデータセットの説明・集計単位・公開元を確認する。

## 日本語の候補（優先）

| 優先 | カタログ | API・CSV/DataStore | 件数の目安 | ライセンスの扱い | 次の確認 |
| --- | --- | --- | ---: | --- | --- |
| A | [横浜市オープンデータ](https://data.city.yokohama.lg.jp/) | CKAN `/api/3/action/package_search` を公式案内。CSV 153 件の検索結果あり | 647 | サイト規約は原則 CC BY 4.0。異なる条件のコンテンツは個別表示に従う | CSV のうち表形式・非個人単位をメタデータで絞る |
| A | [神戸市オープンデータ](https://data.city.kobe.lg.jp/) | 別ホスト `https://catalog.city.kobe.lg.jp/api/3/action/package_search`。適合する CSV リソースには Data API がある | 99 | サイト全体一律ではなく、各データに表示された CC ライセンスを適用 | ライセンスとファイル形式を各データで確認 |
| A− | [山口県オープンデータカタログ](https://yamaguchi-opendata.jp/) | `https://yamaguchi-opendata.jp/ckan/api/3/action/package_search`。公式 API 説明で CSV リソースを確認 | 788 | 山口県・県内市町の共有カタログ。利用ルールは PDL1.0 と互換の CC BY 利用を認める。API メタデータにもデータ単位のライセンス欄がある | 県・市町の提供元ごとに割当て、個別ライセンスと公開主体を確認 |
| B | [神奈川県オープンデータカタログ](https://catalog.opendata.pref.kanagawa.jp/) | CKAN `/api/3/action/package_search` を公式案内。CSV あり | 815 | 県の規約は原則 CC BY 4.0。別ライセンスのデータは個別ページに従う | 表示件数は大きいが CSV は少ない可能性があるため、形式フィルターを取り直す |
| B（小規模試行） | [仙台市データカタログ](https://data.city.sendai.jp/dataset) | CKAN の package_search を案内。CSV 8 件の検索結果あり。サイトに API Key 案内も表示 | 16 | 市はデータごとに CC ライセンス表示し、変更の可能性があるため利用時に再確認を求める | API Key の要否と現在の件数を確認 |

横浜・神戸・神奈川は自治体自身のカタログ。山口は県と県内自治体を横断する共有カタログなので、同じ公開元として一括扱いしない。仙台は数が小さいため、接続と表形式の確認用に向く。

## ポルトガル語（ブラジル）

| カタログ | API・CSV/DataStore | 件数の目安 | ライセンスの扱い | 次の確認 |
| --- | --- | ---: | --- | --- |
| [リオデジャネイロ州データ公開ポータル](https://dadosabertos.rj.gov.br/) | CKAN API を公式表示。CSV/XLSX の絞り込み画面あり。標準 CKAN action の正確な URL と匿名利用は未検証 | 約1.1k | データ単位のライセンス表示。PDDL の絞り込みが見えるため、採用時はライセンス許可リストとの照合が必要 | package_search の公開アクセス、CSV 件数、ライセンス別内訳をメタデータだけで確認 |
| [フォルタレザ市 Dados Abertos](https://dados.fortaleza.ce.gov.br/) | 公式資料に `/api/3/action/package_search`、公開検索（認証なし）、`datastore_search` の説明 | 現行画面で総数を確認できず。市の2023年発表では611件 | データ／リソースごとに確認する。確認できた CSV リソースの例は ODbL。サイト一律とはみなさない | ODbL が現行許可リストにあるかを含め、件数とライセンス分布を確認 |

## 英語圏の候補

| カタログ | API・CSV/DataStore | 件数の目安 | ライセンスの扱い | 次の確認 |
| --- | --- | ---: | --- | --- |
| [New Zealand data.govt.nz](https://catalogue.data.govt.nz/) | CKAN。公式例に `/api/3/action/package_search`。DataStore API と CSV 等の機械判読形式を案内 | 約33.2k | サイトの一般コンテンツは CC BY 4.0、データと API は各ダウンロード版と同じライセンス。個々のデータページを確認 | 表データ・許可ライセンス・個人単位でないことを先に絞る |
| [UK data.gov.uk](https://www.data.gov.uk/) | 現行ディレクトリ API は CKAN。公式例は `/api/action/package_search`（`/api/3/action` ではない）。API key 不要・レート制限なしとの案内 | 今回は未確認 | データごとの `license_id` を扱う仕様。OGL を含むが、全件でサイト共通と仮定しない | 現行の公開元・データ件数・許可ライセンスを確認 |
| [New York State Open Data](https://data.ny.gov/) | Socrata。各データに API endpoint。簡単な公開 query は token なしでも利用可能だが、token なしは共有 IP 単位の抑制対象 | 今回は未確認 | OPEN-NY 利用規約があり、データページには「Terms of Use」または未指定のライセンス表示例もある。利用規約と個別表示の両方を要確認 | 既知の許可ライセンスに当てはまるか、件数と CSV 形式を確認 |

## 今回の優先順位

1. 横浜市：CSV が多く、標準 CKAN の package_search を公式案内。
2. 神戸市：カタログ件数は小さめだが、標準 API と CSV 用 Data API がある。
3. 山口県カタログ：件数が多く CSV もあり、県・市町の公開元メタデータを使って割当てる。
4. 神奈川県：件数は大きいが、CSV 比率を更新時点で再確認してから進める。
5. 仙台市：API Key 条件を確かめて、小規模な形式確認に使う。

ブラジルはリオ州をメタデータ段階の候補とする。フォルタレザは ODbL の扱いが確認できてから候補に入れる。英語圏はニュージーランドを先に検討し、英国・ニューヨーク州は API／ライセンス条件を確認してから扱う。

サイト全体の利用規約を新たに採用したり、学習データに取り込んだりしていない。公開元の最終割当ては `independent_eval/allocation.py` の規則に従い、eval に割り当たった公開元を教材にしない。