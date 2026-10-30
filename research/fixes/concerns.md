# 残っていた懸念点の原因（2026-10-30 Claude。オーナー「3は全ての懸念点の原因が判明してからだ」）

第 2 段（学習・予測のやり直し）の前に、原因が分かっていなかった懸念点を 1 つずつ調べた。

| 懸念点 | 原因 | 確かめ方 |
|---|---|---|
| 1. F7（列名に手がかりがあれば検査役は下げない）で重大が 1→7 | 6 列のうち 5 列は所得の幅ごとの申告件数（「$5,000 to $9,999」、正解 quantity）。列名の $ が金額の手がかりに当たる。recheck の「金額の幅の列名」の規則（money_band_header）は幅をハイフン（5,000-9,999）でしか読まず、「$5,000 to $9,999」「Under $5,000」は幅と読まない（`recheck._BAND` に通して確かめた）。1 列は「Number」（正解 quantity）で、number は番号の手がかりにも当たる（LABEL_GUIDE は「number だけでは決めない」）。検査役はこれらを正しく下げていた | `diff_decide_F7.md` |
| 2. F1（列名を語に分ける）で確かめる陣の誤りが +1 | b036 で「zone_code」が 2 列は id（UFZ）、1 列は category（FO）と付いている＝**教材の付け方が陣の中で割れている**。UFZ の 2 列は先生（ChatGPT）が category、Claude が裁定で「区域のコードは id」に変えた。FO の列は別の表で**裁定に回らず**、先生の category のまま。裁定は先生と本体が食い違った列だけに回るので、同じ形の列でも裁定が届かない列は先生のラベルが残る（電力量の割れ：b011 で 1 列だけ裁定を通らず quantity のままだったのと同じ仕組み）。F1 で _code が番号の手がかりになり、category の列を id にした。もう 1 列「Year_1」（率）は語に分けると「Year 1」になり日付の手がかりとぶつかって不明に下がった | `diff_confirm_F1.md` |
| 3. 確かめる陣の重大 1 列（b036-0267「GTFS from DIVA」、正解 id） | 本体 quantity 0.55 → recheck が確信が低いで不明 → **rho が検査役（値の形だけの分類）の quantity を信じて候補に戻した**。値は 5801 などの整数で、値の形だけでは番号か件数か分からない。rho は「値の形が確かなら戻す」前提で、整数の id と quantity ではその前提が成り立たない | `wrong.jsonl` |
| 4. 言い切って誤った列（重大でない誤り） | 決める陣 127 列中 119 列・確かめる陣 57 列中 56 列は**本体の答えがそのまま通った**（`wrong.md`）。その 175 列のうち **168 列は、本体の中で近い教材の列の多くに本体の誤った答えと同じ種類が付いていた**（run 40997091007）。誤りは LABEL_GUIDE の境目の種類（category・text・account・org・address・id）の間で、境目を分ける意味の違いが入力の形に出ず、教材の似た形の列が別の種類で付いている（下の表） | `wrong.md`・`embed_wrong_read.md` |
| 5. 題名ありで増えた重大（b063-0275 Nachgefragt、正解 amount） | 本体は題名なしで quantity 0.88（決め方で不明）、題名ありでも quantity。本体の中で近い教材は quantity の列（「Family income between …」など、`embed_read.md`）。題名ではなく列名から覚えた種類（原因 4 の組）で、題名ありでは確信が上がって決め方を通った | `title_check.md`・`embed_read.md` |
| 6. F2・F3・F5・F6 が確かめる陣で効かない | 確かめる陣にその原因の形（文字化けの £・古い年や週の列・Cost Centre・ドイツ語）がほとんどない。原因は分かっている。効くかはその形を含む陣で確かめる | `confirm.md` |

## 裁定が一部の列にしか届かないこと（懸念点 2 と電力量の割れに共通する仕組み）
教材のすべての陣（教材庫 b001〜b065 のうちファイルのそろう陣）で、同じ陣の中に同じ列名が 2 列以上ある組 3,008 組のうち、**種類が割れている組は 278（9%）**。そのうち **203 組（73%）は、裁定を通った列と通らなかった列が混ざっている**（例：b003「団体名」は裁定の 2 列が address、先生のままの 3 列が org。b002「fund」は裁定が id、先生が category）。裁定は先生と本体が食い違った列にしか回らないので、Claude が裁定で付け方を変えても、同じ形のほかの列には届かない。同じ列名でも表が違えば意味が違うことはあるので、278 組すべてが誤りとは限らない（確かめていない）

## 懸念点 4 の中身：言い切って誤った列の組み合わせ（`embed_wrong_read.md`）
| 正解 → 本体 | 列 | 本体の中で近い教材の列（本体の答えと同じ種類） | 境目が入力に出ない理由 |
|---|---:|---|---|
| text → category | 24 | 「Statistic Label」「class-title_en」「区分３」など区分の項目名（category） | text か category かは行ごとに違う文かで決まる（LABEL_GUIDE v2.0）。渡る 5 個の値で同じ文が繰り返されると区分に見える |
| quantity → category | 23 | 「epc_rating_known」（0/1）・「MMM2019」など小さな数の区分・印（category） | 0〜10 の小さな件数は、有無の印や区分の番号と同じ形 |
| id → category | 17 | 「treatment_code」（S・C）・「LABEL」（G1・T）など区分のコード（category） | コードが行を見分ける番号か、決まった区分かは値の形に出ない（v1.6「並べ替え用の番号は id」・「言語コードは category」） |
| category → text | 13 | 「Comments」「内容」「提供エリア」など自由な文（text） | 区分の名前が長い文だと自由な文に見える |
| category → account | 11 | 「SERVICE_RESPONSABLE」「項目２」（賃借料等）など費目・部署の名前（account） | サービス・政策の分野の名前は、費目・部署の名前と同じ形 |
| address → category | 10 | 「UNIT」（AAU）・「Jurisdiction」（FEDERAL）など区分のコード（category） | 国や地域のコード（COM・CHFL）は区分のコードと同じ形 |
| account → category | 10 | 「Cluster」「ANZSIC Division Name」など区分（category） | 部門・収入の種類の名前は区分の名前と同じ形 |
| org → account | 10 | 「Dept_Level_1」「ORGAO_ENTIDADE」など部署の名前（account、LABEL_GUIDE v1.3・v1.7「部署・課・係は account」） | 英国の「Department」は省庁＝組織（org）、日本・ブラジルの表の部署は account。列名も値の形も同じ |
| address → id | 9 | 「行政区番号」「Station No.」など数の番号（id） | 郵便番号（plz）・番地（haus_nr）は数だけで番号と同じ形（LABEL_GUIDE「番地は address」） |

- **原因**：本体は近い形の教材の列の種類で答える（懸念点 4 も、不明の列の原因 4 と同じ仕組み）。境目の種類は、LABEL_GUIDE では意味（行ごとに違う文か・組織か部署か・番地か番号か）で分けているが、本体に渡る入力（列名・5 個の値・同じ表の列名）にはその意味が出ないことが多い
- ここで分かっていないこと：近い教材の付け方と新しい陣の正解のどちらが LABEL_GUIDE に合っているかは、組ごとに先生が見ないと決められない（例：英国の Department を org にした新しい陣の正解と、部署を account にした教材は、どちらも LABEL_GUIDE の決まりどおりで、決まりの側が境目を書き分けていない）

## LABEL_GUIDE の改訂で取り残された教材（2026-10-30。列名の語で決まる決まりを教材に当てた）
| 決まり | 当たる教材の列 | 決まりと違う |
|---|---:|---:|
| v2.1 識別子の URI は id | 58 | 16（biz 12・biz2 4、すべて other） |
| v2.0 órgão・entidade は org | 4 | 3（b006） |
| v2.0 cost centre（名前）は account | 9 | 1（biz） |
| 郵便番号は address・緯度経度は other・順位は category・内線番号は phone | 255 | 0 |

- 取り残しは 20 列に限られる。境目の決まりの案は `research/labels/label_guide_v22_draft.md`
