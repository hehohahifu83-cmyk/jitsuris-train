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
