# Codex 向けの決まり（jitsuris-train：ジツリスの研究）

- 返事は日本語。役割と決まりは AI 連絡箱（`hehohahifu83-cmyk/ai-bridge`）の `README.md`「Codex の範囲」。依頼は連絡箱の `messages/*-to-codex_*.md` で来る。
- 引き継ぎ書は `HANDOFF.md`（先頭が最新）。事前記録は `bench/*_prereg_*.md`。
- 試験：`python -m unittest discover -s tests -p 'test_*.py'`（重いものは個別に）。変えた所に近い試験を必ず流し、結果（通った数・失敗）を報告に書く。
- **開かない・使わない**：`blind_set*`、封印セット（`independent_eval/` の sealed2・sealed3 の中身）、`b018`、セット 3・5・7。
- **ラベルを付けない**：ラベル用のシート・答え（`answers*`・`claude_answers*`）・裁定（`pool_final.tsv`・`*decisions*`）は、作業に要らない限り開かない。開いた中身を ChatGPT の会話に書き写さない。
- **しない**：`kaggle/kaggle.request` などの依頼ファイルの書き換え（学習・収集の依頼）、事前記録の固定、採否の判定。bot が書くファイル（`bench/*_summary.md`・`kaggle/*`）は手で書き換えない。
- 変更は作業ブランチか PR で出す（main へ直接 push しない）。main へのマージは Claude がする。
- 結果の数字は元のファイルと突き合わせて書く。確かめたこと（試験・実データ）と確かめていないことを分ける。
