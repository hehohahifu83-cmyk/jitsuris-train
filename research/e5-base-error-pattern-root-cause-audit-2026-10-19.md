# E5-base 失敗パターンの原因監査（2026-10-19）

## 対象と証拠

- Kaggle run 39241962638 の回収済み評価artifactに基づく。対象は固定5セット、seed 1/2、`ft` と `blend70`。blind setおよびsets 3/5/7は使わない。
- ケース・混同行列は `cpu_lab/reports/error-analysis-run-39241962638.md` の確率JSON由来。旧`errors_*.json`ではなく、各行1件の`probs_*.json`を読み込んでいるため、最終予測の件数は公式集計と一致する。
- 固定評価行は原因調査・教材追加に転用しない。列の値を含む原データは今回のケースartifactにないため、列名とラベルからの説明は仮説に限る。

## 確認できた実装上の事実

1. `train3.decide` は確率上位の候補を選び、`guard.guard` に値を渡す。`guard`はdate/amount/quantity/rateの値形式を検査するが、categoryとquantity、orgとaccountの間に専用の拒否判定はない。したがって、これらのクラス間で高確信の誤りがそのまま通る可能性がある。
2. `rules.py` のヘッダー規則では `department` は account に一致する。`gen.py`と`curriculum.py`にも `Department` をaccountとする例がある。
3. `LABEL_GUIDE.md`はdepartment等を値で分ける。組織・役所の名称ならorg、部署・課ならaccountと定義し、値の半分を超えて役所の名称・略号ならorgとする。つまり文字列 `department` だけでラベルを固定できず、評価例がorgなら学習例と意味役割が異なる可能性がある。
4. 同ガイドはアンケートの0/1選択肢をcategoryとする。合成教材`gen.py`にも数値カテゴリ値はある一方、確認した`curriculum.py`には `q2a` 等の設問コード形式を扱う表が見当たらない。設問コードと数値回答の組合せに対するカバレッジ不足は候補だが、値を見ていないため未確定。

## 固定5セットで観測した再発

- business: `category→quantity`がftで15件。列名`q2a`と`q3_1`は両seedで再発。category→quantityの混同計はftで20件（category→id/amount等を含む）。
- business: `department`の`org→account`が両seedで複数回再発。これは定義ガイドの「値で決める」規則と、ヘッダー単独ルールが競合する事例候補。
- business2: `amount→quantity`がftで6件、`fine`、`miscellaneous_divers`、`sales-goods-svcs_ventes-biens-srvs`などが両seedで再発。
- 高いtop-1確率で最終予測unknownの行も複数ある。コード上、top-1がしきい値0.5以上なのに最終unknownなら値guardが候補を退けたことを示す。ただしその行の値・top-2差を見ないと、過剰拒否か正しい安全見送りかは判別できない。

## 根本原因の判定

| 候補 | 現時点の確度 | 次に必要な証拠 |
|---|---|---|
| departmentの教師・ルールがaccountに寄り、値が役所名のケースをorgと区別できていない | 高め（ルール側のaccount優先はコードで確認、ケースの実際の値は未確認） | 原データのdepartment値と周辺列を確認。ラベルガイドに従う二重判定を記録 |
| q2a/q3_1等の設問IDで、数値回答のcategoryをquantityと区別しにくい | 中（再発と学習カバレッジ差は確認。元値未確認） | 固定5セットと独立した公開アンケート表で、設問説明・回答値・ラベル根拠を結び付ける |
| amount/quantityの値分布またはヘッダー意味の不足 | 中（confusion再発のみ確認） | 独立データで列値・単位・同表文脈を監査。固定試験から教材を作らない |
| 高確率unknownがguardの過剰拒否 | 未確定 | 値とguard理由を記録したschema 2を使い、人が正答根拠を確認 |

## 次の検証順

1. 実行中のGPU高速化回帰チェックを完了させ、学習・評価コード変更が既存の高速化条件を壊していないことを確認。
2. 新しい学習やguard緩和は保留。直近Kaggleの評価JSONを再利用可能な形で確認し、schema 2へ再出力するための評価専用経路が実現可能かを調べる。実現できなければ、次の一回のKaggle実行をschema 2検証に使い、同時に条件を増やさない。
3. 原因別に独立した公開資料から例を集め、出典・ラベル規則・値型を記録する。category numeric / org-account / amount-quantityを混ぜずに1テーマずつ試す。
4. 変更を採る前に、最終予測・unknown・重大誤り・誤り集合・速度・メモリを同じseedと同じ固定5セットで照合する。単にaccuracyが上がっても、重大誤りや失敗対象が悪化したら採用しない。

現在の失敗と実装差から強い仮説は立てられるが、原値や公開原典の照合前に原因を断定しない。
