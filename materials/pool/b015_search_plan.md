# b015 公開元・検索語の下調べ（metadata only）

調査日：2026-10-25

## 目的と優先順位

弱い種類（text・amount・account・date・other）と、数量↔番号、金額↔率、日付↔番号、text↔category↔other、org↔address↔account の境目を含む公開表を探すための検索計画。候補を探す段階では表の値を取得しない。

`materials/pool/manifest.json` の b001〜b014 では、amount 593、account 313、date 2,582、other 665、text 1,000 列。量の少ない種類を優先するが、全ての候補が弱い種類に偏らないよう、取り違えやすい対の片側も一緒に探す。強化案 B1 の目安（各種類 300〜500 列、30 表、10 公開元以上）は、候補の採否時に参照する。

## 公開元の採用ゲート

検索対象は、各公開元の正規 publisher ID が `independent_eval/allocation.json` で `train` のものだけ。親 ID が固定割当なら子組織も同じ割当を継ぐが、検索の前にその ID と割当を再確認する。main・eval2・eval3・hold、または割当が未確認の ID は検索しない。評価用の公開元一覧や表は開かない。

| 言語 | 公開ポータル | 割当・検索方法 |
|---|---|---|
| 日本語 | e-Gov データポータル（`data.e-gov.go.jp`） | `egov`・`egov_biz`・`egov_biz2` は固定 train。CKAN のデータセット検索・説明・リソース形式・列名メタデータまで。 |
| 日本語 | e-Stat API | `jp`・`jp2` の固定 train 割当を持つ。実際の publisher ID が train に結び付くことを確認できた場合だけ、統計表一覧とメタ情報を検索する。`getStatsList`・`getMetaInfo` 相当のメタ情報のみ。`getStatsData` は呼ばない。 |
| 英語 | Australia `data.gov.au`、Ireland `data.gov.ie`、Canada `open.canada.ca` | 既存の national collector 対象。各組織が train であることを割当ファイルで確認後、CKAN メタデータを検索。 |
| 英語 | Boston `data.boston.gov` | 既存の train CKAN 公開元。タイトル・説明・license・datastore の列定義まで。 |
| ポルトガル語 | Belo Horizonte `dados.pbh.gov.br`、Recife `dados.recife.pe.gov.br`、Rio Grande do Sul `dados.rs.gov.br` | 既存の train CKAN 公開元。組織 ID ごとに割当を再確認してから検索。 |

根拠となる既存設定：`independent_eval/allocation.py` の固定 train 親 ID、`materials/pool/allowed_hosts.json`、`materials/pool/README.md` の CKAN/national 公開元一覧。README が探索済みとしている BODIK と Socrata は再走査せず、同じ年次表の重複候補も除く。

## 検索語の束

ポータルの検索は、下表の語を組み合わせて少数ずつ実行する。表題・説明・組織名・ライセンス・ファイル形式・列名の説明だけを読む。検索結果の preview やデータ行は読まない。

| ねらい | 日本語 | English | Português |
|---|---|---|---|
| 自由記述 / text | 摘要、備考、説明、施設案内、事業概要 | notes, remarks, description, narrative, purpose | observações, descrição, finalidade, ementa |
| 金額 / amount | 金額、予算、決算、収入、支出、単価、料金、費用 | amount, budget, revenue, expenditure, unit price, fee, cost | valor, orçamento, receita, despesa, preço, custo |
| 勘定・部門 / account | 勘定科目、会計科目、費目、部門、部署、支出科目 | account code, ledger, cost centre, department, fund, expenditure item | conta contábil, centro de custo, unidade gestora, rubrica |
| 時点 / date | 日付、年月、年度、日時、開始、終了、月次 | date, datetime, fiscal year, month, start, end, reporting period | data, exercício, mês, início, fim, período |
| 測定値・統計量 / other | 気温、濃度、面積、標高、水位、座標、平均、標準偏差 | temperature, concentration, area, elevation, water level, coordinates, mean, standard deviation | temperatura, concentração, área, altitude, nível da água, coordenadas, média, desvio padrão |
| 数量 ↔ 番号 | 件数、人数、個数、数量、年齢 ＋ 番号、コード、ID、識別子 | count, quantity, volume, age, duration + number, code, ID, serial, reference | quantidade, contagem, faixa etária, duração + código, identificador, série |
| 金額 ↔ 率 | 金額、価格、単価、収入 ＋ 割合、比率、構成比、前年比、率 | amount, price, revenue, cost + rate, percent, percentage, ratio, share | valor, preço, receita, custo + taxa, percentual, proporção, participação |
| 日付 ↔ 番号 | 日付、年月、年度、時刻 ＋ 連番、登録番号、コード、識別子 | date, month, year, timestamp + sequence, record number, code, identifier | data, mês, exercício + número de série, código, identificador |
| text ↔ category ↔ other | 状態、種類、方法、分類 ＋ 説明、備考 ＋ 測定、平均、濃度 | status, type, method, category + description, remarks + measurement, mean, concentration | estado, tipo, categoria + descrição, observações + medição, média, concentração |
| org ↔ address ↔ account | 事業者、団体、施設名 ＋ 市区町村、所在地、住所 ＋ 部署、課、費目 | organization, agency, supplier, facility + municipality, address, location + department, fund, cost centre | órgão, entidade, empresa, instalação + município, endereço, localização + departamento, centro de custo |

## メタデータだけで候補を選ぶ方法

1. 割当ファイルで publisher ID が train であることを確認する。固定親の下でも未確認の子 ID は照合してから検索する。
2. タイトルと説明から、集計値・予算集計・施設一覧・統計分類など、複数の列種類が同居しそうな表を優先する。個人の給与・患者・申請者・事件・許可・入学・名簿など個人単位の記録は除外する。
3. ライセンスと形式を確認する。使用可能な公開ライセンスと構造化形式（CSV/XLSX/API の列メタデータ）が明確な候補だけ残す。ODbL や不明な利用条件は除く。
4. 列の見出し・説明だけで、弱い種類または境界ペアの見込みを記録する。セル値、行 preview、CSV/XLSX 本体は取得しない。
5. 年次違い・同じ表の別形式・同じ公開元の重複をまとめ、1 公開元あたり最大 3 表の既存ルールに合わせる。

e-Gov の公式 API はデータセット/リソースの説明、形式、更新日時などのメタ情報を提供する。e-Stat の公式 API は統計表一覧と表のメタ情報を提供する。実際の収録値を返す API はこの探索では使わない。

## 出典

- 現行の train 割当・収集制約：[`independent_eval/allocation.py`](../independent_eval/allocation.py)、[`independent_eval/allocation.json`](../independent_eval/allocation.json)、[`materials/pool/allowed_hosts.json`](allowed_hosts.json)、[`materials/pool/README.md`](README.md)。
- e-Gov メタデータ API 案内：https://data.e-gov.go.jp/data/api_guide
- e-Stat API 機能概要：https://www.e-stat.go.jp/api/api/index.php/api-info
- 東京都カタログの CKAN API（将来の割当確認用。現行探索対象には自動で加えない）：https://catalog.data.metro.tokyo.lg.jp/api/1/util/snippet/api_info.html
