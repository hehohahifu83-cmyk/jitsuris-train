# W2 重大誤り17列のラベル・入力不足監査（2026-11-08 Codex）

## 範囲と再集計

- 対象は W2 run 42323220255 の評価artifact 13557246189。
- 読んだのは許可された固定5集合（pool / general / business / business2 / japan_procurement）のみ。blind_set*、セット3・5・7、sealed2/3、b018は未閲覧。
- 許可5集合の `ft` は10,880出力、critical 31件。
- そのうち教材庫検証（pool）の `job1/job2 × ft` は9,102出力、critical **29件・17固有列**。
- 既存 `critical_dictionary.md` の「投票区6列」はartifactと一致しない。artifact上は投票区5列で、内訳から漏れていた `export_interstate` 1列を加えると17列になる。
- pool外の2件は general の `debris cataloged` と business の `well-founded_bien-fonde`。したがって「31件」と「17列」は同じ母集団の数ではない。

ラベルは変更していない。以下はCodexの独立確認であり、疑義があるものはClaudeの独立確認と根拠裁定まで変更しない。

## 17列の確認

| index | 列 | 現ラベル | 観測事実 | ラベル判断 | 確度 | 入力に足りないもの / 次の確認 |
|---:|---|---|---|---|---|---|
| 925 | sales | amount | PA Fine Wine & Good Spiritsの郡別年次Sales。値は43,980,981等。公式年報は郡別のdollar salesを説明 | amountを支持 | 高 | 表題、通貨USD、`sales ($)` の単位 |
| 1392 | metro council | id | Baton Rouge Voting Precinct表。値は全行0。兄弟列にVoting Precinct/Ward/US House等 | 選挙区番号なのでidを支持。ただし0だけでは値から確定不能 | 中 | 表題「Voting Precinct」と項目説明。0が欠損代替か有効コードか公開元確認 |
| 1393 | us house | id | 同上。全行0 | 議会選挙区番号としてidを支持 | 中 | 同上 |
| 1394 | psc | id | 同上。全行0。seed2だけcritical | Public Service Commission districtの区域番号としてidを支持 | 中 | 略語展開と項目説明 |
| 1396 | la house | id | 同上。全行0 | Louisiana House district番号としてidを支持 | 中 | 略語展開と項目説明 |
| 1397 | la senate | id | 同上。全行0 | Louisiana Senate district番号としてidを支持 | 中 | 略語展開と項目説明 |
| 1407 | ticket sales | amount | PA Lotteryの郡別年次表。値126,729,608等。公式予算資料はticket salesを金額で扱う | amountを支持 | 高 | 表題と通貨USD |
| 1409 | retailer commissions | amount | 同じLottery表。値3,058,641等。retailer commissionsは支払金額 | amountを支持 | 高 | 表題と通貨USD |
| 1667 | avg. time on page | quantity | 値は0:00:17、0:00:35、0:02:37等。時間の長さ | quantityを支持 | 高 | durationであること、秒単位。時刻dateではないことを前処理へ明示 |
| 1992 | mainstream_sna_allocation__26_27 | quantity | アイルランド教育データ。値0.5、2.0、3.0等。公開元はSNA allocationを配置数/FTEとして説明 | quantityを支持 | 高 | SNAの展開、FTE/配置人数の単位、表題 |
| 1993 | special_class_snas__26_27 | quantity | 同表。値1.83、2、3.66等 | quantityを支持 | 高 | 同上 |
| 1994 | total_sna_allocation_26_27 | quantity | 同表。値1.58、1、0.5、2.83等 | quantityを支持 | 高 | 同上 |
| 2074 | export_interstate | quantity | 豪州waste表。兄弟列recycled/waste_to_energy/export_international/disposal/recovery_rate。値例は0、他の処理量列は実数 | 廃棄物量なのでquantityを支持 | 中高 | tonnes等の単位と表題。rate列との区別 |
| 2220 | ssd_supplier_band1__m | amount | Ireland Revenue SSdt liability表。値0.138、0.386等。兄弟に税率`am_rateband1`とhectolitres。教材候補はadjudicated amount | `__m`をmillion currency liabilityと読むamountを支持 | 中高 | 列名展開、通貨EUR、millionの単位。公開仕様で最終確認 |
| 2509 | t1gistotal | amount | Canada GIS表。値972.9、228.49等。兄弟にincome_from/to、GIS+OAS。GISは月額給付 | amountを支持 | 高 | GIS/OASの展開、CAD/月の単位、表題 |
| 3096 | value | rate | Fiscal Year/Period/Month/Branch/Service/Metric Typeの表。値100、99.98等。同じ原表群でrateとして裁定済み | rateを支持 | 中高 | `Metric Type`の値、%単位、表題。Value単独では決めない |
| 3542 | geo_cant | id | 値1/2/1。スイスのcanton code。LABEL_GUIDE B3も区域コードGEO_CANTをidと明記 | idを支持 | 高 | GEO/cantonの展開、コード体系の説明 |

## 原因の整理

### 観測事実

- 17列すべてで、現ラベルを否定する根拠は見つからなかった。
- 投票区5列は全値0で、値だけではidとquantityを区別できない。意味は表題・項目定義に依存する。
- `Value` は見出し単独では学習側のラベルが割れており、兄弟列`Metric Type`と%単位が必要。
- SNA3列、GIS、SSDT、GEO_CANTは略語・単位が入力へ十分に現れていない。
- `Avg. Time on Page` はdurationをdateへ誤分類している。
- 辞書だけで安全に直せる範囲は小さい。17列に共通する主因は、表題・単位・略語展開の欠落と、数値形への過依存。

### 原因仮説

| 仮説 | 根拠 | 確度 | 追加確認 |
|---|---|---|---|
| 表題・単位を入力へ加えるとamount/quantity/rate/idの境界が改善 | Sales/Lottery/SNA/GIS/Valueで意味を決める情報が現入力に欠ける | 高 | 同一重みで入力だけを変える一要因replay |
| 全0列は数値形への過依存でquantityへ寄る | 投票区5列が全0、両seedで再発 | 高 | 表題/項目説明あり・なしの対照 |
| durationの構文がdate guard/encoderに吸われる | Avg. Time on Pageが0:MM:SSでdate予測 | 高 | duration明示と時刻dateの対照例 |
| 略語の展開不足が意味誤りを起こす | SNA/GIS/OAS/GEO_CANT/SSDT | 中高 | 展開語だけを追加したreplay |

## 優先対策（一度に一要因）

1. **P0 入力診断**：学習なしで、同じ17列へ「表題のみ」「単位のみ」「略語展開のみ」を別々に追加して予測差を測る。期待は原因の切分け。副作用は既存入力長増加。
2. **P1 duration前処理診断**：`HH:MM:SS`を経過時間として明示する候補を、時刻dateの対照例と一緒に検証。重大増なら不採用。
3. **P1 全0の識別子教材**：公開定義がある区域コードの全0/単一値列を学習側だけで収集。固定評価例は教材へ転用しない。
4. **P2 辞書**：`time on page/duration`や明示的な略語だけを候補化。Sales/Valueのような多義語は単独辞書にしない。

## 未完了

- 投票区5列の0が有効な区域コードか欠損代替かは、公開元のデータ辞書で最終確認が必要。
- `ssd_supplier_band1__m`の通貨・million定義、`export_interstate`の単位、`Value`のMetric Type全値は公開仕様の二次確認が必要。
- 本監査は先生1人目の確認。ラベル変更はClaudeの独立確認と根拠裁定後。
- 新しい学習・評価は実行していない。
