# 辞書 v2 の見直しの裁定（2026-11-01 Claude）

材料：ChatGPT の見直し `review_v2_chatgpt.tsv`（eb63040）と候補 `terms_v2_chatgpt.jsonl`（7077016）。まとめは `research/dictionary/merge_v2.py`。
凍結：`materials/dictionary/frozen_v2.jsonl`（98 項目、SHA-256 0e1c07f5402e4ba984152c78b1bad79812a718d5ac323da883cfa65e2bedcc34）。

## Claude の項目（K1001〜K1019）
- ok の 7 件（K1010・K1012・K1014〜K1018）はそのまま入れた。
- 変えるの 12 件は、すべて ChatGPT の指摘どおりに直した。
  - K1001：一般の名前の列（name・名前・nom・titel・designation・denominazione）を外した。場所の語尾に「recreation ground」「car park」を足した。
  - K1002〜K1008（GWR）：Merkmalskatalog の許可値だけにした。
    - GKAT 1010・1020・1030・1040・1060・1080
    - GBAUP 8011〜8023
    - GWAERZH 7400〜7461・7499
    - GENH 75xx
    - GSTAT・WSTAT x001〜x005・x007・x008
    - GKSCE 901〜909
    - 言語 9901〜9904
    - GKLAS（11xx・12xx）は値が合わないので K1002 から外した。
  - K1009：あいまいな語（system・status・form・eigentuemer・aktiv・wiederkehrend）を外した。語の前に区切りを要るようにした（start_id の「art」に当てない）。
  - K1011：値を ESA 2010 の部門のコード（S1・S11〜S15 とその下、S2）だけにした。
  - K1013：一般語（numberShort・shortNumber・checkDigit）を外した。辞書には兄弟の列や表の題名が渡らないので、交通の表だと分からないため。
  - K1019：「年代・世代・時代・交代」の「代」を外した。
- 直しで失うもの：直す前の下書きは確かめる陣の誤りの一部（numberShort・checkDigit など）に届いた。この陣は使い済みなので測り直さない。

## ChatGPT の項目（KC1001〜KC1008）
- 8 件とも入れた。LABEL_GUIDE の行 23・30・33（通貨は category、国・国コードは address）と B7 に合う。
- KC1004（国コード、strong）だけ直した：値の 3 桁の数字を外した。country_code の列が電話の国番号（353 など）のことがあり、強い項目で本体の答えを変えてしまうため。

## 害の確かめ（採否には使わない）
- 古い 23 陣：下書きと同じ。採点 4,220、正しい 3,606 → 3,722、重大 3 → 3、ほか 180 → 159。
- 使い済みの決める陣（L 種子 1〜3）：下書きと同じ。
- 試験：`tests/test_table_dictionary.py`（10 件）。
- 効き目は新しい在庫の陣で、事前記録のうえで測る（L＋K〈frozen_d3〉対 L＋K2〈frozen_v2〉）。
