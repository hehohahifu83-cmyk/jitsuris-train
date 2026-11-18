# G4凍結候補のCodex点検（2026-11-18）

対象：jitsuris-train main `8b72d34814c656bcac4ade5006a3d89894c3ba37` の
`bench/g4_prereg_20261118.md`、`independent_eval/g4.py`、`tests/test_g4.py`。

## 結論

**このcommitはまだ凍結しない。収集・freeze・学習・予測を開始しない。**

T1の主要2問題は修正され、診断v2も入力条件をL24へ合わせている。一方、G4道具には封印対象への参照、凍結の原子性、adoptedとcorpusの結合確認に停止条件が不足している。

## 確認済み事実

- Kaggleは既存依頼ID `2026-11-12T17:13:08Z`がCOMPLETEのまま。`kaggle.request=done`、queued/in_progressは0。新しい学習・評価・モデルartifactはない。
- T1診断v2は許可された教材庫validation 4,561列を対象とし、control-256は256 token切詰め0%、T1-256は49.48%。T1では1行目全部99.69%、2行目全部80.67%、同じ表の列名一覧全部50.65%、単位列の値全部78.90%が256 token内に残る。これは学習結果ではなく入力診断。
- `g4.py`は冒頭で `import sealed2 as S2` を行い、`USED_WORKS`に `sealed2`・`sealed3`を含め、`used_resources()`で各 `adopted.json` を開く。
- `cmd_freeze`は `g4.json`、`provenance.json`、`titles.json`を書いたあとに `check_set` を実行し、既存の凍結ファイルがあっても上書きを拒否しない。
- `cmd_freeze`のcorpus検査はhold、対象カタログ、未使用publisherを確認するが、各corpus表が `g4/adopted.json` または正当な `g4x/adopted.json` のresourceであることを全件照合しない。
- 候補規則はresource_idが無ければresource_urlでハッシュすると書くが、実装は `platform_of(c)[0] is None or not rid` でresource_id無しを全て除外する。文書と実装が一致しない。
- `check_set`の文脈値確認は `vals[header]` で全表をまとめるため、同じheaderを持つ別表の値でも通り得る。再生成一致が通常は先に効くが、「セットのその表のその列の値」という独立した不変条件にはなっていない。
- `test_unit_only_from_set_columns`はUnit列が選ばれなかった場合だけassertする。Unit列が選ばれたときは実質的に検査せず成功する。
- Claude側の報告は関連試験47件成功。Codexは封印対象を開かない規則のため、現状の `g4.py` / `test_g4.py` を実行して独立再現していない。
- `blind_set*`、sealed2/3、b018、セット3・5・7の内容は読んでいない。

## 原因と確度

| 観測 | 原因仮説 | 根拠 | 確度 | 追加確認 |
|---|---|---|---|---|
| 封印対象なしではg4.pyをimportできない | G3由来の共通関数をsealed2から直接流用した | importとS2.ROOT/norm/poolsの参照 | 高 | 一般処理を許可された共通moduleへ分離 |
| freeze失敗後に不完全成果物が残り得る | 検証より先に本番pathへ書く | cmd_freezeの実行順 | 高 | tempで生成・検証後にatomic renameする試験 |
| 採用外のcorpusが混ざり得る | corpusとadoptedのresource対応を検査しない | freezeのbad条件はpublisher/pool/catalogまで | 高 | 正当resource集合との全件一致を検査 |
| 文書とresource_id無し候補の扱いが不一致 | 取得可能性の判定と並び順のfallbackを混同 | adopt_ruleの `or not rid` | 高 | direct CSVを許可するか文書で除外を固定 |
| 表別値検査が弱い | 値集合のkeyがheaderだけ | check_setのvals | 高 | (table_id, header)で照合する反例試験 |

## 修正条件

1. `g4.py`と試験からsealed2/3のimport・ファイル読取りを完全に除く。ROOT、norm、poolsは封印対象に依存しない共通moduleへ移す。既使用resourceの除外は、開いてよいprovenance/registryだけを事前列挙し、未確認範囲を限界として記録する。
2. freezeは既存出力が1つでもあれば拒否する。temp directoryへ3成果物を作り、全検証成功後だけ同一filesystemでatomic renameする。失敗時にOUTへ成果物0件の回帰試験を加える。
3. corpus各表をadopted/g4x adoptedへresource_url、resource_id、publisher、置換元で結合し、余分・欠落・重複・無関係なreserveを拒否する。corpus SHAだけで済ませない。
4. resource_id無しを許可するなら取得可能なdirect CSVの試験を加え、URLで決定順を作る。許可しないなら文書からfallbackを削り、除外理由を明示する。
5. 文脈値検査を表ID＋header単位にし、別表の同名列の値を混ぜた反例を拒否する。
6. Unit列が必ず選外になるfixtureへ直し、選外の単位値がunit/row_contextへ0件であることを常にassertする。
7. 上記を直した版で、封印対象を読み込まずに試験を実行できることを確認する。凍結候補のSHA表も修正版へ更新する。

## 未確認・未完了

- G4候補探索、adopt、取得、reserve、freeze、ラベル、学習、予測、採点は未実行。
- 採点道具と予測workflowは未作成で、正解固定後の別点検が必要。
- G4での精度、誤り、重大誤り、unknown、時間、GPUメモリは未確認。
- 目標は、表の列種類判定でChatGPT・Claudeと同一課題の同等以上を実証して実用化すること。Geminiは比較対象外。
