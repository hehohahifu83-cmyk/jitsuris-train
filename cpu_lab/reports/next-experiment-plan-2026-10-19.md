# 完了済みCPU Lab・学習率実験計画 — アーカイブ

更新: 2026-10-20 UTC

この計画の後続実験は完了または評価され、記載コマンドは現行の依頼ではありません。再実行しないでください。現行の作業順と停止条件は [tool-kobo 正本の現行学習計画](https://github.com/hehohahifu83-cmyk/tool-kobo/blob/research/column-ai/research/column-ai/TEACHING_PLAN.md) を参照。

- CPU Lab fresh-head: 固定評価1995例で全件unknown。能力向上実験として無効、パイプライン確認に限定。
- FT_LR=2e-5: matched seed比較完了。平均差は全セットで1.5pp未満、誤り134→133、重大20→22。既定値を維持。
- e5-large: 品質差は基準内、重大誤り20→25、学習時間約3.24倍、peak GPU 3.5→9.0GiB。拡大を採用せず。
- 詳細数値・手順は research/e5-base-lr2e-5-audit-2026-10-19.md、research/e5-base-unfreeze-embeddings-audit-2026-10-19.md、research/E5_LARGE_SIZE_AUDIT_2026-10-19.md に保持。

過去のコマンド本文を除き、再現に必要な実験結果と監査報告は削除していません。
