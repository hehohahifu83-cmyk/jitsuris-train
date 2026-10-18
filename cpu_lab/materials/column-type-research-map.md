# 表の列タイプ判定：CPUラボ用の研究教材マップ

状態：読み物と実験仮説の整理。外部データセット・モデル重みはまだ取り込んでいない。引用した研究は方法の参考であり、結果をジツリスへそのまま移せる保証ではない。

## 研究から学ぶこと

### 1. 1列の値と見出しを読む

Sherlock は列見出し・セル値由来の特徴を使って意味型を推定する研究で、VizNet由来686,765列を78種類へ対応づけて学習した。ジツリスでは「列名だけ」「値だけ」「両方」を同じ訓練分割で比べ、どの情報が各誤りを減らすか分けて測る発想が有用。Sherlockのデータ・ラベル体系はジツリスの種類定義と同一ではないので、そのまま混ぜない。

出典：MIT Visualization Group, *Sherlock: A Deep Learning Approach to Semantic Data Type Detection* (KDD 2019) — https://vis.csail.mit.edu/pubs/sherlock/

### 2. 表全体と兄弟列の文脈を使う

Sato は列の値だけでなく表の意図や近隣列の文脈も使う。ジツリスの UNIT 文脈実験と方向が合う。最初は明示的なUNIT列など誤りにくい文脈だけを一要因で足し、次段で兄弟列の確率を加える。自分の予測ラベルを確定事実として流す設計は、誤りの連鎖を測れるまで避ける。

出典：Zhang et al., *Sato: Contextual Semantic Type Detection in Tables*, PVLDB 13(12), 2020 — https://doi.org/10.14778/3407790.3407793

### 3. 表の構造を事前学習する

TURL は行・列の構造を考慮するTransformerと、欠けたエンティティを戻す事前学習課題を提案している。これは「ラベルのない表から表現を学ぶ」候補にはなるが、対象は主にWeb上のエンティティ表であり、ジツリスの業務列タイプと同じ課題ではない。CPUでの大規模事前学習は重い可能性があるため、最初は論文再現ではなく小さな構造情報ablationとCPU測定を優先する。

出典：Deng et al., *TURL: Table Understanding through Representation Learning*, PVLDB 2020 — https://arxiv.org/abs/2006.14806 ; 公式研究紹介 https://research.google/pubs/turl-table-understanding-through-representation-learning/

### 4. 列順に依存しない構造化

NAACL Findings 2022のPermutation Invariant StrategyはTransformerを使った表理解で、列タイプ判定も扱う。列順を変えた時に出力が過度に変わるかを検査する発想が参考になる。ジツリスでは既存の表単位分割を保った上で、許可された訓練・検証分だけ列順を変える対照試験を設計できる。固定試験から学ぶことはしない。

出典：*Permutation Invariant Strategy Using Transformer Encoders for Table Understanding*, Findings of NAACL 2022 — https://aclanthology.org/2022.findings-naacl.59/

### 5. 複数列を共同で注釈する

DODUOは事前学習済み言語モデルで表の複数列を注釈する公開研究・コードベース。列同士の相互作用を学ぶ候補だが、モデル・データの利用条件とCPU負荷を確認してから試す。公開コードや重みを教材に持ち込む前に個別ライセンス確認を行う。

出典：DODUO project repository — https://github.com/megagonlabs/doduo ; paper information — https://arxiv.org/abs/2104.01785

## CPU待機中に優先する順番

1. 既存教材の重複・ラベル定義・データ漏洩を検査し、由来記録を整える（モデル学習なし）。
2. 訓練データだけからの小さな合成・対照例を作り、生成元と仮ラベルを記録する。根拠の弱い生成例は使わない。
3. 軽量な候補分類器や文脈特徴の1要因試験を、既存CPU学習と排他して走らせる。
4. 学習時間、CPU使用率、ピークメモリ、許可済み固定5試験の精度・誤り・重大誤り・unknownを比較し、実益がある場合のみ候補を残す。
5. 大規模な自己教師あり事前学習は、小規模計測でCPU時間とメモリの見積りが立つまで始めない。

## 持ち込み前の確認

- 引用研究のコード・データ・モデルのライセンスは、ここに書いた論文リンクだけでは確定しない。個別の配布物のLICENSEと利用条件を読む。
- 教材から作る訓練例の出典、変換、列タイプの根拠、機微情報除去の方法を記録する。
- 成果は候補モデル・候補ルールとして分離し、既定モデルやKaggle依頼へ直接上書きしない。
- blind_set*、セット3・5・7は読み込まない。
