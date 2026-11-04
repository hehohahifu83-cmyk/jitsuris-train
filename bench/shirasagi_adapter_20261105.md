# Shirasagi独自API対応（Codex、2026-11-05）

## 完了内容

`materials/shirasagi.py`を候補探し・取り出しへ接続。登録はClaude担当。
`materials/pool/SHIRASAGI.md`に設定・提供元対応表・制限・実行引数を記載。

- UUID（API）と数値id（公開ページ）を分離、資料idはカタログ・UUIDで名前空間化。id欠落はURLのSHA256。
- resourceごとの明示的な許可ライセンスのみ。CSV/XLS/XLSXは既存解析器で処理。
- 登録済み自治体trainだけ。確認済みauthor/user対応表、外部ファイルは取得先ホストの対応表で識別。不明/競合は除外。areas/groupsの単独推定なし。
- 実際の静岡サンプルはgroups=静岡県だが浜松市ファイル、愛媛もgroups=愛媛県で鬼北町ファイル。県へ一括帰属させない。根拠は `research/catalogs/shirasagi_publishers_20261105.json`。
- 仙台市041009は明示除外。現行allocationで仙台市の文字列・コード登録は見つからず、train限定だけでは将来の誤登録を防げないためガードを追加。宮城CSV専用アダプターは今回の範囲外。
- 1ホスト2秒以上の直列取得。一覧は100件単位・既定1000件上限（最大5000）、時間制限・使用済み・題名年度重複・自治体15表制限あり。
- 取り出し時も提供元・ライセンス・train割り当て・許可取得先・資料同一性を再検証。
- allowed_hosts/allocation/NATIONALの登録・採用・収集依頼・学習は変更なし。

## 実API確認

Actions 41922622536 / 41923655266 / 41923868445（メタデータのみ）。6サイトのpackage_showと提供元構造を確認。
青森・香川・愛媛はpackage_listでoffset省略がValidation Error（Must be a natural number）。
limit=100&offset=0は3サイトとも成功・100件。静岡/鳥取/徳島も一覧成功。
実装は全ホストでlimit/offsetを明示し、ページ重複・上限・時間制限を検査する。
完成したClientで6サイトそれぞれ一覧1件→package_showを直接取得し、全件UUID一致・数値idを確認。保存は構造と件数だけ（`research/catalogs/shirasagi_adapter_smoke_20261105.json`）。
HARP再確認はHTTP200の非JSON応答で失敗。対応済み扱いにせず、TLS検証も維持。

## 試験と限界

専用28件成功：提供元不明/競合・外部市町優先・allocation別名・未登録/非train・仙台除外・個別ライセンス・UUID/数値id・資料id欠落・使用済み・上限・予算・明示offset/ページ取得・ホスト制限・再取得時の提供元/ライセンス変更・adopt→fetch経路・CSV/Excel経路。
回帰79件成功（fetch42、pool_discover15、pipeline7、HTTP8、label_sheets7）。bridge21件も別途確認。
設定例は仕様説明用であり実登録はしていない。実ファイルの取得・採用は登録後にClaudeが検証する。
