# HTTPしか使えないカタログの設定

通常はHTTPSのみ。例外は `allowed_hosts.json` の `http_hosts` 配列に**完全一致のホスト名**を明記する。例：`"http_hosts": ["catalog.example.lg.jp"]`。サブドメイン・ワイルドカード・URL・別ポート・ユーザー名付きURLは例外にしない。HTTPは標準80番ポートだけを許す。

登録担当はClaude。既存の`ckan`（APIのホスト）、`csv_domains`（ファイルのドメイン）、公開元のallocationも別途必要。`http_hosts`だけで取得先の許可が広がることはない。`pool_discover.NATIONAL`のsiteは実際の`http://…`を設定する。

候補発見のJSON API、CSV/xls/xlsxの候補、実取得のAPI/ファイル、HTTPへの転送に同じ例外を適用する。転送は接続前に検査する。HTTPS側の従来のホスト検査は維持。明記されていないHTTPのファイルは従来のHTTPS正規化規則を維持し、HTTPのままは取得しない。

今回は相模原・町田・新潟の実ホストを登録していない。外部への実取得は登録後のClaudeの作業。試験では仮のホストを使い、許可の完全一致・紛らわしいホスト・サブドメイン・ドメインだけ許可されたHTTPファイル・転送・API・CSVを検証している。
