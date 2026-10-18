# 共同教材の追加口

Claude と ChatGPT は、新しい教材候補をこのフォルダーへ追加する。

## 置き方

- Claude の候補: `claude_candidates.jsonl` に1行1教材で追記する。
- ChatGPT の候補: `codex_candidates.jsonl` に1行1教材で追記する。
- 既存ファイルは上書きしない。ID は `claude-YYYYMMDD-連番` または `codex-YYYYMMDD-連番` とし、重複を避ける。
- 例の形は `candidate.template.jsonl` を参照。元データのURL・ライセンス・出典・プライバシー確認を必ず記入する。
- 候補ファイルには正解ラベル、モデルの予測、推測ラベルを入れない。監査前の先入観を避ける。
- 顧客情報、個人情報、秘密情報、未公開データ、出典・利用条件が確認できないデータは入れない。
- blind_set*、セット3・5・7、および評価・テスト用データは参照・追加・学習しない。
- 候補はここに置いただけでは学習されない。2人の監査が一致するか、単独監査の規則を満たした後にだけ reviewed_replay.jsonl へ採用する。
- 監査手順は `../AUDIT_PROTOCOL.md` に記載する。
