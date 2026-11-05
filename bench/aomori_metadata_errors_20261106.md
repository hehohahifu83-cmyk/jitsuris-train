# 青森 Shirasagi メタデータ接続の調査

- 観測：2026-11-06 06:55 JST 前後、managed cloud から既存 Client を使用。GitHub Actions の実行環境とは異なる。
- package_list（limit=100, offset=0）は成功。返った100件の0/24/49/74/99番目のUUIDについて package_show は5/5成功。間隔は既存の同一ホスト2秒待機を維持。メタデータだけを取得し、本体資源はダウンロードしなかった。保存は要求ID・結果・時間だけ。データセットの連絡先や人名は保存しない。
- 最初の疎通でも一覧500件とshow先頭2件が成功（この2件は保存した5件に重複が1件あるため、独立7件とは数えない）。
- 正確な5件の観測：`research/catalogs/aomori_metadata_probe_20261106.json`。show の所要2.22〜2.56秒にはホスト共通の待機を含む。
- 過去の `materials/pool/work/b176/auto_log.md` は metadata_error=162, metadata_error:URLError=162, resource_rejected=485, 採用4表。**showの全要求が失敗した記録ではない**。また stopped_by_budget=1 は処理全体の時間枠であり、各HTTP要求のタイムアウトを示さない。
- 過去ログに URLError.reason・errno・HTTP status がなく、過去162件が timeout / connection_refused / rate limit のどれだったかは確定できない。現在の低頻度5件の成功だけでは、連続大量取得時の制限も否定できない。Actionsの同条件での再現検証は未実施。
- 根拠のない再試行・並列化・待機時間変更は加えず、`metadata_error_cause()` による固定語の原因カウンタだけ追加。timeout、connection_refused/reset、unreachable、DNS、TLS、HTTP429/5xx、proxy CONNECT429/5xx、未分類を区別する。既存の総数と例外型カウンタは維持。例外本文・応答本文・資格情報は記録しない。
- 次回Claudeが通常の収集を実行した際の `metadata_cause:*` で経路を特定する。url_other の場合は追加の非機密診断が必要。収集・学習・予測の依頼ファイルは変更していない。
- 試験：shirasagi 30（15種類の原因ケース＋集計/本文非保存を含む）、label_sheets 8、isolated_imports 1、pipeline 7、pool_discover 15、計61試験成功。既存のResourceWarningあり。全試験一括実行はしていない。
