# 速くする設定の検査（CPU・e5-small・GitHub Actions）

run: 39245751418　commit: 50d86bdc7f19357342fad1a38d3f92bca433eb06

| 検査 | 設定 | 学習秒・評価秒 | 最初の損失 |
|---|---|---|---|
| A 今までの流し方 | train batch=8, accumulation=8, effective=64, checkpointing=False, sort=False, pad_multiple=1, fused=False, freeze_embeddings=False | ('57', '8') | [2.774895, 2.770448, 2.770817, 2.759631, 2.757056] |
| B 長さ順の束＋幅8の倍数 | train batch=8, accumulation=8, effective=64, checkpointing=False, sort=True, pad_multiple=8, fused=False, freeze_embeddings=False | ('42', '8') | [2.774895, 2.770448, 2.770817, 2.759631, 2.757056] |
| C 水増し＋長さ順＋幅8 | train batch=8, accumulation=4, effective=32, checkpointing=False, sort=True, pad_multiple=8, fused=False, freeze_embeddings=False | ('26', '8') | — |
| D 単語の埋め込みを固定＋長さ順 | train batch=8, accumulation=4, effective=32, checkpointing=False, sort=True, pad_multiple=1, fused=False, freeze_embeddings=True | ('22', '8') | — |

A と B の最初の5ステップの損失の最大の差：0.0（ドロップアウトを切り、同じ種・同じ実効バッチ。基準 2e-3 未満）

CPU（fp32・e5-small・640行）の検査であり、GPU（fp16）での速さや品質の結果ではない。

縮めた版の試験（検査 E。CPU・e5-small・学習は 320 行だけの出来の悪いモデルなので、語彙の残り方・大きさ・動くことの確認用。判定の質の結果ではない）：
- 圧縮の試験は失敗した：NameError: name 'decide' is not defined
