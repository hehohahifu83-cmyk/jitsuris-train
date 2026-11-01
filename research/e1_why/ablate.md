# 直しの 1 つ外し（`research/e1_why/ablate.py`。使い済みの陣で探索、採否には使わない）

## decide

| 形 | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|
| 製品＋K2 | 3229 | 230 | 4 | 158 |
| 全部 | 3245 | 197 | 10 | 169 |

誤りを増やした列（全部）：
- 本1 b072-0294 [bilanz_view_nr] 正解 category：unknown → id
- 本1 b074-0050 [wert] 正解 quantity：unknown → rate
- 本1 b074-0161 [Tag_Nr] 正解 category：unknown → id
- 本1 b076-0091 [Tag_Nr] 正解 category：unknown → id
- 本1 b085-0054 [RATE] 正解 amount：unknown → rate
- 本2 b072-0294 [bilanz_view_nr] 正解 category：unknown → id
- 本2 b074-0050 [wert] 正解 quantity：unknown → rate
- 本2 b074-0161 [Tag_Nr] 正解 category：unknown → id
- 本2 b076-0091 [Tag_Nr] 正解 category：unknown → id
- 本2 b076-0100 [Tag_NR] 正解 category：unknown → id
- 本2 b078-0159 [whg_neualt_nr] 正解 category：unknown → id
- 本2 b078-0179 [haushalt_wohndauer_nr] 正解 category：quantity → id
- 本2 b085-0054 [RATE] 正解 amount：unknown → rate
- 本3 b074-0050 [wert] 正解 quantity：unknown → rate
- 本3 b074-0261 [eigentuemer_typ_nr] 正解 category：unknown → id
- 本3 b076-0091 [Tag_Nr] 正解 category：unknown → id
- 本3 b078-0169 [whg_bauj_group_nr] 正解 category：unknown → id
- 本3 b078-0179 [haushalt_wohndauer_nr] 正解 category：unknown → id
- 本3 b085-0054 [RATE] 正解 amount：unknown → rate

| 全部−F1b | 3237 | 205 | 10 | 169 |
| 全部−F3 | 3242 | 200 | 10 | 169 |
| 全部−F6 | 3240 | 213 | 10 | 158 |
| 全部−F7 | 3242 | 206 | 4 | 169 |
| 全部−G1 | 3245 | 197 | 10 | 169 |
| 全部−G2 | 3245 | 197 | 10 | 169 |
| 全部−G3 | 3245 | 197 | 10 | 169 |
| 全部−G4 | 3245 | 197 | 10 | 169 |

## confirm

| 形 | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|
| 製品＋K2 | 3376 | 190 | 14 | 161 |
| 全部 | 3381 | 170 | 23 | 167 |

誤りを増やした列（全部）：
- 本1 b067-0430 [THEMA_ID] 正解 category：unknown → id
- 本1 b068-0005 [Total, All Recipients, Number] 正解 quantity：quantity → id
- 本1 b068-0007 [Less than $5,000, Number] 正解 quantity：quantity → amount
- 本1 b069-0043 [Number] 正解 quantity：unknown → id
- 本1 b072-0345 [THEMA_ID] 正解 category：unknown → id
- 本2 b067-0430 [THEMA_ID] 正解 category：unknown → id
- 本2 b068-0005 [Total, All Recipients, Number] 正解 quantity：quantity → id
- 本2 b068-0007 [Less than $5,000, Number] 正解 quantity：quantity → amount
- 本2 b069-0043 [Number] 正解 quantity：unknown → id
- 本2 b072-0345 [THEMA_ID] 正解 category：unknown → id
- 本3 b067-0430 [THEMA_ID] 正解 category：unknown → id
- 本3 b068-0005 [Total, All Recipients, Number] 正解 quantity：quantity → id
- 本3 b068-0007 [Less than $5,000, Number] 正解 quantity：quantity → amount
- 本3 b069-0043 [Number] 正解 quantity：unknown → id
- 本3 b072-0345 [THEMA_ID] 正解 category：unknown → id

| 全部−F1b | 3381 | 170 | 23 | 167 |
| 全部−F3 | 3381 | 170 | 23 | 167 |
| 全部−F6 | 3373 | 178 | 23 | 167 |
| 全部−F7 | 3378 | 188 | 14 | 161 |
| 全部−G1 | 3381 | 170 | 23 | 167 |
| 全部−G2 | 3381 | 170 | 23 | 167 |
| 全部−G3 | 3381 | 170 | 23 | 167 |
| 全部−G4 | 3381 | 170 | 23 | 167 |

## E1

| 形 | 正しい | 不明 | 重大 | ほか |
|---|---:|---:|---:|---:|
| 製品＋K2 | 3164 | 323 | 21 | 137 |
| 全部 | 3245 | 251 | 13 | 136 |

誤りを増やした列（全部）：

| 全部−F1b | 3239 | 257 | 13 | 136 |
| 全部−F3 | 3233 | 263 | 13 | 136 |
| 全部−F6 | 3233 | 262 | 13 | 137 |
| 全部−F7 | 3233 | 263 | 13 | 136 |
| 全部−G1 | 3227 | 262 | 20 | 136 |
| 全部−G2 | 3239 | 257 | 13 | 136 |
| 全部−G3 | 3223 | 271 | 15 | 136 |
| 全部−G4 | 3233 | 263 | 13 | 136 |

