# 速くする設定の検査（CPU・e5-small・GitHub Actions）

run: 39089142390　commit: dfddc075b76c3c5b6933fb24a33c037bd6852d6b

| 検査 | 設定 | 学習秒・評価秒 | 最初の損失 |
|---|---|---|---|
| A 今までの流し方 | train batch=8, accumulation=8, effective=64, checkpointing=False, sort=False, pad_multiple=1, fused=False, freeze_embeddings=False | ('51', '8') | [2.774895, 2.770448, 2.770817, 2.759631, 2.757056] |
| B 長さ順の束＋幅8の倍数 | train batch=8, accumulation=8, effective=64, checkpointing=False, sort=True, pad_multiple=8, fused=False, freeze_embeddings=False | ('38', '8') | [2.774895, 2.770448, 2.770817, 2.759631, 2.757056] |
| C 水増し＋長さ順＋幅8 | train batch=8, accumulation=4, effective=32, checkpointing=False, sort=True, pad_multiple=8, fused=False, freeze_embeddings=False | ('23', '8') | — |
| D 単語の埋め込みを固定＋長さ順 | train batch=8, accumulation=4, effective=32, checkpointing=False, sort=True, pad_multiple=1, fused=False, freeze_embeddings=True | ('20', '8') | — |

A と B の最初の5ステップの損失の最大の差：0.0（ドロップアウトを切り、同じ種・同じ実効バッチ。基準 2e-3 未満）

CPU（fp32・e5-small・640行）の検査であり、GPU（fp16）での速さや品質の結果ではない。

測定プログラム（speed_probe.py）の勾配の一致（CPU・fp32・実効バッチ16）：bs2_ckpt 一致度1.000028・相対差0.0；bs16_ckpt_sort_pad8 一致度1.000028・相対差0.0；bs8_noc_sort 一致度1.000028・相対差0.0；bs32_ckpt_sort 一致度1.000028・相対差0.0
