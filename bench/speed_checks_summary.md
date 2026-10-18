# 速くする設定の検査（CPU・e5-small・GitHub Actions）

run: 39097270224　commit: ff2036998f306645e3a21cec30f63810d1513cde

| 検査 | 設定 | 学習秒・評価秒 | 最初の損失 |
|---|---|---|---|
| A 今までの流し方 | train batch=8, accumulation=8, effective=64, checkpointing=False, sort=False, pad_multiple=1, fused=False, freeze_embeddings=False | ('64', '10') | [2.774895, 2.770448, 2.770817, 2.759631, 2.757056] |
| B 長さ順の束＋幅8の倍数 | train batch=8, accumulation=8, effective=64, checkpointing=False, sort=True, pad_multiple=8, fused=False, freeze_embeddings=False | ('47', '10') | [2.774895, 2.770448, 2.770817, 2.759631, 2.757056] |
| C 水増し＋長さ順＋幅8 | train batch=8, accumulation=4, effective=32, checkpointing=False, sort=True, pad_multiple=8, fused=False, freeze_embeddings=False | ('28', '10') | — |
| D 単語の埋め込みを固定＋長さ順 | train batch=8, accumulation=4, effective=32, checkpointing=False, sort=True, pad_multiple=1, fused=False, freeze_embeddings=True | ('25', '10') | — |

A と B の最初の5ステップの損失の最大の差：0.0（ドロップアウトを切り、同じ種・同じ実効バッチ。基準 2e-3 未満）

CPU（fp32・e5-small・640行）の検査であり、GPU（fp16）での速さや品質の結果ではない。

縮めた版の試験（検査 E。CPU・e5-small・学習は 320 行だけの出来の悪いモデルなので、語彙の残り方・大きさ・動くことの確認用。判定の質の結果ではない）：
- 圧縮の試験（intfloat/multilingual-e5-small 微調整 1.0周）：残す単語片 21,772 個／全体 250,037 個（上位 K=0、学習の文に出た片＋日本語・英語の 1 文字の片＋特別な記号）。試験の文 60 列のうち、残さない片を含む列 34 列（片の 1.10%）。
- 大きさの見積り：全体 117.7M 個（埋め込み表 96.0M＋本体 21.6M）。圧縮なし fp32 471MB／語彙削減後 fp32 120MB・fp16 60MB・INT8 30MB（重みだけの見積り。正規化・バイアスは含まない）。
- 圧縮なし（fp32）：圧縮なしとの top-1 一致 100.00%、確率の最大の差 0.000
- 語彙削減（残さない片は unk）：圧縮なしとの top-1 一致 100.00%、確率の最大の差 0.001
- 語彙削減（トークナイザも縮める）：圧縮なしとの top-1 一致 100.00%、確率の最大の差 0.001
- 語彙削減（トークナイザも縮める）＋INT8の重み（全結合層・埋め込み表を丸める疑似）：圧縮なしとの top-1 一致 100.00%、確率の最大の差 0.001
- 語彙削減（トークナイザも縮める）＋INT8の動的量子化（全結合層）＋埋め込み表INT8：圧縮なしとの top-1 一致 98.33%、確率の最大の差 0.001
- 語彙削減（トークナイザも縮める）＋fp16（重みを丸める）：圧縮なしとの top-1 一致 100.00%、確率の最大の差 0.001
- 参考：ここの『圧縮なし（fp32）』と本体の評価（CPU）の top-1 一致 100.00%
- 圧縮の試験の所要 20秒（数字は保存した微調整済みモデルを縮めて試験に流した結果で、ブラウザの実機の結果ではない）

測定プログラム（speed_probe.py）の勾配の一致（CPU・fp32・実効バッチ16）：bs2_ckpt 一致度1.000023・相対差0.0；bs16_ckpt_sort_pad8 一致度1.000023・相対差0.0；bs8_noc_sort 一致度1.000023・相対差0.0；bs32_ckpt_sort 一致度1.000023・相対差0.0
