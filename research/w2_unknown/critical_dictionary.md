# W2 の重大な誤りは辞書で直せるか（2026-11-07 Claude、オーナー「辞書を更新することでは解決しない問題か？」）

- W2（教材庫 1.0、job1・job2）の重大な誤りは検証全体で 31／10,880 出力＝0.28%（教材庫の検証 4,551 列で 0.31%・0.33%）。目標の 0.2% 以下に届いていない。
- 教材庫の検証の重大な列（2 種子の重なりを除き 17 列・8 表）に、今の辞書 2 つを当てた（学習なし）：
  - 標準 1,319 項目（`jtools/std_fields.py`）：**当たり 0**。17 列はすべて海外の表（米・愛・豪・瑞）。日本の自治体の表に重大は無い。
  - 表の知識の辞書（`table_dictionary.py`、50 項目）：当たりは GEO_CANT（id）の 1 列だけ。本体の上位 3 つに id が無いので答えは変わらない（apply の決まり）。
- 17 列の内訳：投票区の表 6（値が全部 0、正解 id も疑わしい）、教員配置 3（FTE の単位が入力に無い）、Sales 系 3、__m・t1gistotal 2、Value 1、Avg. Time on Page 1、GEO_CANT 1。
- 見出しの手がかりを W2 の学習側（113dcab、cap 後 29,696 列）で数えた（値は保存しない）：

| 手がかり | 列・表 | 正解の内訳 |
|---|---|---|
| sales（語） | 3・2 | quantity 2・amount 1 |
| 語尾 _m／__m | 15・6 | amount 11・other 3（length_m）・quantity 1 |
| ($m)・millions | 40・18 | amount 28・other 10（延長（m）など）・quantity 1・category 1 |
| time on page・duration | 10・6 | quantity 10 |
| FTE | 18・7 | quantity 18 |
| value だけ | 54・54 | quantity 29・amount 14・category 4・other 3・rate 3・text 1 |

- **結論**：辞書で安全に直せそうなのは多くて 1〜2 列（time on page／duration → quantity、__m → amount は数が少ない）。Sales と Value は教材の中でも割れる。残りは**入力の手がかり不足（単位・題名）とラベルの疑い**で、辞書の問題ではない。辞書に足すなら、事前記録のうえで、その語の列の誤りが増えないことを別の陣で確かめる。
