# P0 入力診断：12列の比較入力まで作成、実測は保留

2026-11-09 Codex。依頼：ai-bridge `20261109-0947_claude-to-codex_w2-critical-adjudication.md`。

投票区の裁定 S を受領。投票区5列（別途BESEもS）は対象外とし、全0のid教材を集める案は取り下げる。教材・ラベル・guard・学習依頼は変更していない。

## 確認できたこと

- W2 commit `113dcab2a18ff7b753047b5f726e86cfb4efcefb` の許可済みbatch群から38,654列、153付け直し、検証4,551列を復元。12列をindex・見出し・truthで保存済みseed1出力と照合した。
- W2は既に `FT_TITLE=1`。したがって「表題を新たに足す」は誤った説明になる。baselineは既存の40文字上限を維持し、title条件だけ原表題の全文にする。表題が40文字以下ならこの条件は同一入力であり、失敗とは数えない。
- unit条件は元入力末尾に候補単位だけ追加。acronym条件は見出しの括弧内へ展開だけ追加。値、兄弟列、truthは変えず、3条件は混ぜない。GEO_CANTには物理単位を足さない。略語がない列も同一入力として残す。
- 追加語の根拠は `critical_label_review_codex.md` とClaudeの `critical_label_adjudication.md`。候補は人が根拠を読んで足す診断用メタデータで、自動取得の性能を測るものではない。全タイトルをそのまま使用し、GEO_CANTの多言語辞書文字列も都合よく整形しない。
- 48入力は `p0_inputs_codex.json` に保存。保存済みのbaseline予測は過去の観測であり、介入後の予測ではない。

## 実測が止まった理由

W2 run `42323220255` のモデルartifact `13557211258` は期限内、879,625,432 bytes。job1 manifestの `FT_KEEP=1`・seed1と対応する。GitHub連携の取得上限536,870,912 bytesを超えて取得拒否。認証済みGitHub CLIによる通常取得と新しいAPI照会も、一時配布先で403 Forbidden。秘密のURL・鍵は記録していない。

環境にはモデル重みがない。別モデルや保存済み確率から介入結果を推定することはしていない。**予測変化・改善数・重大増減は未測定**。seed2重みも未取得で、二種子再現は主張しない。

## 再開手順（学習なし）

W2 seed1の保存モデルを利用できる環境で実行する。CPU用torch・transformers・safetensorsが必要。

```sh
python research/w2_unknown/p0_input_diagnostic.py
python research/w2_unknown/p0_input_diagnostic.py --model /path/to/ft_out --output /tmp/p0_results.json
```

スクリプトはjob1 manifestのモデル・tokenizer・labelsの全記載hashを検証してからCPU fp32で推論する。W2の160 token上限・0.5閾値・当時のguard（見出しによる上書きなし）を使用。各条件の可視token列と切り詰め前token数も出す。baselineのraw/guarded/reasonが保存済み12列と一致しなければ結果を解釈しない。CPU fp32と元のT4 fp16の数値差は残り得る。

推論経路は実モデルがなく未実行。比較入力の復元・照合・条件分離だけを検証済み。この12列は誤りを見て選んだ診断集合なので、改善しても一般精度・副作用なしの証明にはならない。

## 今回の検証

- 元入力との独立照合12/12、3介入の分離36/36、不一致モデルhashの拒否1/1、Python構文確認成功。
- 実際に文字列が変わる列数：title 7、unit 11、acronym 7（残りは同一入力）。
- 復元はW2時点のコードをgitから読むため、今回の `apply_label_fix` のS除外変更でindexがずれることはない。
