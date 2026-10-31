# b088 notes（Claude、2026-10-31）

- Claude が LABEL_GUIDE v2.3 だけで付けた（`sheets/answers_claude/`）。予測は見ていない。
- 4 表・29 列（Chicago の公園の美術品・公園の建物、Montgomery County の PC の台帳・物品の出庫）。採点できる 28 列、unknown 1。
- 迷った列：
  - PARK（公園の名前）→ address（場所そのもの）。OFFICIAL_N（美術品の題名）→ text（題名）。ARTIST → person。
  - X_COORD → other（座標）。WARD・COMM_AREA・REGION（区域を指す番号・記号）→ id。
  - CPU・Memory・HDD/SSD（3200・8192・238472、単位なし）→ other（機械の測定値。面積・口径と同じ扱い）。
  - Department・Division（HHS・POL・MC311）→ account（部署）。Model#（X1 YOGA）→ product（型）。
  - CITY_BLDG_（395327.0・0.0）：金額か面積か番号か表から分からない → unknown。
  - Item（234758）→ id（物品の番号）。Unit Of Measure（BTL）→ category。

## Claude の裁定（2026-10-31、ChatGPT の答えと比べて）
- 一致 23/29 グループ。ChatGPT は Claude の notes の抜粋を先に見たと申告している（ai-bridge 20261031-1655）ので、厳密な独立ではない。
- g0013 CITY_BLDG_：**unknown**（Claude。番号か量か表から決められない）。g0017 REGION（S・N）：**id**（Claude。区域を指す記号）。g0018 Department：**account**（Claude。部署）。
- g0023 CPU（3200、クロック）：**other**（Claude。測定値）。g0024 Memory・g0025 HDD/SSD（MB の容量）：**quantity**（ChatGPT。kg と同じ「量」）。
