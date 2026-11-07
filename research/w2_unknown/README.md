# W2 の未知見出しの誤り（2026-11-07 Claude）

学習曲線 W2（`bench/learning_curve_pool_20261107.md`）で、教材を増やしても「初めて見る見出し」の列は約 85% のまま上がらなかった。
次は、その誤りが**どの段・どの教材・どの決まりのせいか**を突き止める（README 守ること 7。症状を塞ぐ規則で済ませない）。

- `both_seeds_errors.json`：検証（教材庫）の未知見出しの列のうち、教材庫 1.0 の 2 種子（job1・job2）が**どちらも**誤り・不明・other_ng だった 136 列。値は入れていない。`table` は W2 のコミット 113dcab の検証の行の表（見出しと正解で 136/136 一致を確かめた）。値は `materials/pool/batch_*.jsonl` の同じ表・見出しの行で見られる。
- 多い組（正解, 予測）：(date, unknown) 28、(text, category) 25、(quantity, unknown) 10、(account, category) 6、(category, unknown) 6。
- 重大（日付・金額・数量などの取り違え）はこの 136 列には無い。多くは「不明と答えた」か「分類と文の境目」。
