# 事前記録：直し M（再確認の手がかりの語を足す）を G2（2 つ目の海外の陣）で測る（2026-11-12 Claude。収集・ラベル・予測の前に書く）

## オーナーの了承（2026-11-12）
- Claude の提案「再確認が金額の語や単位を読めるようにする直しを、新しい未使用の陣（GovData.de）で確かめる。費用なし」への答え：「よい」。

## 直し M（学習なし・規則だけ）
- 中身：`research/guard_dates/fix_m.py`（SHA-256 `fc4c25eb2e4d70c91854c7ff5a80e93e8e1aa15310eaabf8cf2769853a021e9a`）。再確認（recheck）の強い手がかり `cue_types` に、海外の表でよく出る語を足す（列名・単位の文字列だけ。値は見ない）。
  - 金額：funding・grant(s)・Ansatz・¢・cent(s)・subsid・Mio. EUR。
  - 数量：kWh・MWh・GWh・kWh/a・(ML)・m3・m³・litre(s)・students・patients・clients・beneficiaries・employees・FTE・deaths・births・marriages・volunteers・hunters・casualties・prescriptions・trips。
- 理由：G1 で数の列が不明になった最後の段は再確認が最多（Codex 20261111-2128：金額の手がかり無し 41・期間の見出しで単位無し 33 など）。**G1 は使い済みなので G1 には当てない。**
- 作るときに見た数（**採否には使わない**）：教材庫の検証（W2 の 6 本、`research/guard_dates/fix_m_dev.py`）で、正しい 23,971 → 23,998（+27、すべて不明 → 数量）、新しい誤り 0・重大 0。教材庫には海外のこの形の列が少ないので、効き目は小さく出る。

## 測る陣 G2（G1 と同じ道。目で選ばない・値は開かない）
- 公開元：GovData.de（`ckan.govdata.de`、ドイツの国・州・市の集約カタログ）。データセットのある組織 59（`research/g2/g2_orgs.py`、hold で登録）。**berlin-open-data は G1 の Berlin と重なるので外し、Berlin 統計局（statistik-berlin-brandenburg）のファイルも採用で外す。**教材庫・F1・G1・封印セットに使った表（URL・リソース ID）は除く。
- 道具：`independent_eval/g2.py`（G1 の道具を写した）。採用は 1 公開元 2 表まで・全体 160 表まで（塩 `jitsuris-g2-v1`）。列が 1,200 に届かなければ G1 と同じ adopt-extra（1 公開元 5 表・全体 320 表）。凍結は 1 表 10 列まで・同じ見出しの組は 2 表まで。
- 候補探しで落ちる数（ライセンス・置き場所）を見て足すときは、**採用の前に**ここに追記する（G1 と同じ扱い）。
- 正解：Claude と Codex が LABEL_GUIDE v2.4 で独立に付ける。**相手が付け終えるまで SHA だけを連絡する**。突き合わせ → 規則で裁定 → Codex の見直し → SHA 固定 → そのあとで予測。

## 比べるもの・読み方（予測は 1 回だけ。L24＝run 41735353926 の job1〜3。製品の形・採点は G1 と同じ）
- 主：**L24＋G 対 L24＋G＋M**。決まり 1〜4（D2・E1〜E3・F1 と同じ）：1. 正しいが種子 3 本の平均で +0.5 ポイント以上 2. 重大の合計が増えない 3. ほかの誤りの増えが正しいの増えより少ない 4. 同じ列の差の、表で引き直すブートストラップの 90% 区間の下限が 0 より大きい。4 つとも満たせば M を採り、本物の再確認（recheck.py）とブラウザ版の JS に移す。満たさなければ「確かめられなかった」と書く。
- 読むだけ：L＋G（L24 が海外でも悪くないかの 2 回目）、G2 での正しい・不明・重大、種類ごとの不明（amount・rate・quantity）、M が変えた列。
- **採点の環境を固定する**：Python 3.12・scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0（G1 の再現の差の原因が scikit-learn の版だったため）。採点の道具は版を出力に書き、違う版なら止まる。

## 守ること
- G2 は 1 回だけ測る。測ったあとに正解・製品の形・決まりを G2 に合わせて変えない。
- 封印セット・blind_set*・b018・セット 3・5・7 は使わない・読まない。費用のかかるもの（API・有料の GPU）は使わない。

## 2026-11-11 23:10 JST 追記（候補探しの 1 回目のあと、採用の前。値は見ていない）
- 1 回目（`candidates_g2_20261112.json`）は **候補 0**。全部ライセンスで落ちた：GovData.de は DCAT-AP.de の URI（`http://dcat-ap.de/def/licenses/dl-by-de/2.0` 7,048・`…/cc-by/4.0` 1,279・`…/dl-zero-de/2.0` 886 など）やドイツ語の文（「Datenlizenz Deutschland Namensnennung 2.0」・「Namensnennung 4.0」）で書く。
- 足すもの（`materials/pipeline.py` の normalize_license。どれも G1 で許した出典の表示・ゼロのライセンスの書き方の違い）：dl-by-de → dl-de-by-2.0、dl-zero-de → dl-de-zero-2.0、cc-by(/4.0) → cc-by、cc-zero → cc0、govdata.de/dl-de/by-2-0 と「Datenlizenz Deutschland – Namensnennung – Version 2.0」→ dl-de-by-2.0、「Namensnennung 4.0」→ cc-by。
- 足さないもの：other-closed、「öffentlich」・access-right public・INSPIRE の「制限なし」（ライセンスではなく公開の範囲）。
- 2 回目の候補を `candidates_g2_20261112b.json` に書く。1 回目は採用に使わない。ファイルの置き場所で落ちる数は 2 回目で見る。

## 2026-11-12 00:35 JST 追記（候補探しの 2 回目のあと、採用の前。値は見ていない）
- 2 回目（`candidates_g2_20261112b.json`）も **候補 0**。ライセンスは通るようになり、今度はファイルの置き場所で落ちた（GovData.de の外のホスト 1,337：連邦司法庁 962・連邦海事水路庁 573・連邦労働社会省 265・ザクセン州統計局 62 など。CSV でない資料 11,601 はそのまま落とす）。
- 足すもの（`allowed_hosts.json` の csv_domains の `ckan.govdata.de`）：**表を出した組織そのものの公式サイトだけ**（F1 の data.odp.jig.jp・G1 の Berlin 統計局と同じ扱い。表の持ち主はカタログの組織）。bund.de と連邦機関・省（bundesjustizamt.de・bsh.de・bmas.de・dpma.de・baua.de・bundesfinanzministerium.de・zoll.de・bamf.de・bka.de・bzga.de・bundesnetzagentur.de・bundesgesundheitsministerium.de・bfarm.de・bafa.de・bzst.de・bundespolizei.de・bmvi.de・auswaertiges-amt.de・datenportal.bmbf.de）、州・市（sachsen.de・brandenburg.de・stuttgart.de・soest.de）、農業研究の公的リポジトリ（openagrar.de・bmel-forschung.de）。
- 足さないもの：doi.org・gitlab.opencode.de・民間や事業の個別サイト（staedtebaufoerderung.info・armuts-und-reichtumsbericht.de・mauttabelle.de・rohstofftransparenz.de など）。
- 3 回目の候補を `candidates_g2_20261112c.json` に書く。1・2 回目は採用に使わない。
