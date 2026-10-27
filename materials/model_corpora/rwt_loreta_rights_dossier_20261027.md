# RWT-RuTaBERT / LoReTA 権利判定資料

作成日: 2026-10-27  
対象: YRL-AIDA/LoReTA の RWT-RuTaBERT CTA データ  
結論: **全1,441,349列をlabel-ready / training-readyに切り替える根拠はまだ揃っていない。rights holdを維持する。** ただし、Wikipedia由来の本文が一律に利用不可という意味ではない。2021年時点の標準ライセンスは確認でき、問題はRWT配布物のデータベース／選択権、ページごとの例外、LoReTA MIT表示が上流素材に及ぶ範囲に絞られた。

## 1. 判断に使った一次資料

| 資料 | 確認できること | 確認できないこと |
| --- | --- | --- |
| [RWT論文 (arXiv:2210.06353)](https://arxiv.org/abs/2210.06353) | ロシア語Wikipediaをクロールして作ったコーパスで、ページURL・ページ名・表名等のmetadataを持つ。著者はcorpus/toolkitを「open-source and publicly available」と説明する。 | データの具体的なライセンス名、コーパス全体やデータベース権をどの条件で許諾するか。 |
| [RWT配布リポジトリ](https://gitlab.com/unidata-labs/ru-wiki-tables-dataset) | 配布元の実体をたどれる。公開一覧でREADMEとdataset archiveを確認。 | 独立したデータライセンス条項を確認できない。「公開」「open-source」という説明だけでは、再配布・機械学習・二次配布を許す正確な条件は特定できない。 |
| [LoReTA dataset card](https://huggingface.co/datasets/aidalab/rwt-rutabert/commit/f82676c29c7d874162ecd153e46f1d79e4fb267a) と [固定したLoReTA commit](https://github.com/YRL-AIDA/LoReTA/tree/f12d7f83a70a065c90eb314a14e35bf177bade22) | cardはMITを表示し、RWT由来・170 DBpedia型・固定train/test splitを明記。LoReTAリポジトリにはMIT LICENSEとCSVがある。1,441,349列（train 1,325,901 / test 115,448）、633,426 train tables。 | MIT表示がWikipedia寄稿者の権利やRWT側の選択・データベース権まで解除すること。 |
| [Wikimedia 2014–2023 Terms of Useの保存版](https://foundation.wikimedia.org/w/index.php?oldid=98524&title=Policy:Terms_of_Use) と [現行Terms of Useの適用日](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use) | 2021-09-13のRWT snapshot当時は2014–2023版が有効。通常の投稿本文はCC BY-SA 3.0 UnportedとGFDLの二重ライセンスで、再利用者はどちらかまたは両方に従える。ページURL/履歴を使った帰属、変更表示、外部由来コンテンツの追加表示を求める。現行版は2023-06-07発効。 | 個別ページの履歴・議論・注記にある例外や追加条件。現行CC BY-SA 4.0を2021年の全revisionに遡及適用できること。 |
| [CC BY-SA 3.0 Unported legal code](https://creativecommons.org/licenses/by-sa/3.0/legalcode.en) と [Creative CommonsのデータFAQ](https://wiki.creativecommons.org/wiki/Data) | 著作権のある素材について複製・翻案・配布を許し、公開配布時は帰属・ライセンス表示を求める。翻案物を公開配布する場合はShareAlike条件がかかる。3.0 Unportedは、著作権でなくsui generis database rightだけが問題となる利用を明示的には許諾しない。 | 今回のRWT/Wikipedia選択がどの法域で保護されるか、どの行為がデータベース権を行使するか、列抽出物が翻案か単なるcollectionかという個別法的評価。 |

## 2. ライセンスを層ごとに分けた結論

1. **Wikipedia本文の標準条件**  
   RWT論文が記すsnapshot日は2021-09-13であり、Wikimediaの2014–2023 Termsが有効だった。したがって、標準的なWikipedia本文についてはCC BY-SA 3.0 Unportedを使う経路が根拠に合う。GFDLも提供されていたが、運用上はCC BY-SA 3.0の条件を満たす設計にする。全ページ一律と断定せず、転載元・個別表示・履歴による例外を残す。

2. **帰属と変更の表示**  
   Wikimedia TermsはページのURLを帰属方法として認め、記事の履歴ページに著者一覧があると説明する。各列に最低限、Wikipedia page ID、ページURL、表offset、snapshot日、適用ライセンス、変更内容を保持する。抽出・列化したことを変更として記す。ページのfooter/history/talkに外部由来文の表示や追加帰属があれば、その表示も記録・保持する。

3. **LoReTAのMIT表示**  
   MITはLoReTA側が追加したコード・整理・ラベル等の権利には関係し得る。dataset cardにもMIT表示があるため、その表示と著作権表示は保持する。一方、その表示だけを根拠にWikipedia本文、RWT作者の選択・整理、RWTのデータベース権までMITで再許諾されたと扱わない。著者が保有しない第三者権利は、LoReTAの表示だけでは消えないというのが安全な読み方である。

4. **RWT corpus / selection / database**  
   RWT論文の「open-source and publicly available」は利用意図を示す重要な証拠だが、明示的なデータライセンス条項と同一ではない。現在確認できた配布元からは、dataset archive自体のライセンス名やデータベース権の許諾条件を特定できない。CC BY-SA 3.0 Unportedも、著作権だけでなくデータベース権だけが関わる利用を自動的に解決しない。**全件を解除する最大の残件はここ。**

5. **個別ページ・正確なrevision**  
   RWT paperは2021-09-13 snapshotを説明するが、LoReTAのflattened CSVにはWikipedia revision IDがない。LoReTAのtable_idからpage IDとtable offsetは確認できるが、対象日に対応するページrevisionや個別license noticeは別途復元する必要がある。外部からimportされた表や追加帰属があるページを、一括で標準CC条件とみなさない。

## 3. ここまでで「解決したこと」と未解除の範囲

**解決したこと:** Wikipedia本文の標準ライセンス経路、帰属の実装方法、変更表示、例外確認の場所を特定した。権利問題は「Wikipediaデータは一切使えない」ではなく、「RWT配布物全体と個別例外の証拠が足りない」に絞られた。

**まだ解除できないこと:** 1,325,901列のtrainを一括でlabel-readyにすること。RWT側に具体的なデータライセンスが見つからず、page IDだけでは個々の履歴と例外も証明できない。LoReTA MIT表示はこの不足を補わない。test 115,448列は従来どおり封印する。

## 4. 全件に効率よく適用する解決手順

### A. RWT配布物の権利を一度だけ解決
RWTの著者・配布管理者（Platon Fedorov、Alexey Mironov、George Chernishev / Unidata-Labs）から、対象archiveとsnapshotを特定した書面のライセンス回答を得る。少なくとも、(i) archiveとデータベースの複製・抽出・変換、(ii)人手ラベル作業者への提示、(iii)注釈データ作成とモデル学習、(iv)注釈済みデータまたは派生物の配布範囲、(v)必要な帰属、(vi)第三者Wikipedia素材について著者が許諾できる範囲を明記してもらう。著者の権限を超えるWikipedia本文は、Wikipedia側のライセンス条件を別に満たす。

許諾確認文のたたき台:
> 2021-09-13 snapshotを元にしたru-wiki-tables-datasetの対象archiveについて、複製、列抽出、変換、人手注釈者への提示、注釈データ作成、モデル学習、および注釈済み派生データの配布に適用されるライセンスと帰属条件をご教示ください。データベース権を含む貴プロジェクトが許諾できる権利、第三者Wikipediaコンテンツに適用される別条件、対象archiveのcommit/checksumもご確認ください。

### B. 許諾後、列数ではなく固有ページ単位で監査
1. LoReTA trainの固定commitとshard checksumを照合する。
2. table_idからdistinct page IDを集計し、対象日以前の該当revisionをMediaWiki履歴で特定。正確なrevision ID/dateとページタイトルを保存する。
3. ページhistory/talk/footerとsnapshotの注記を確認。追加条件・外部由来表示・権利が特定できないページはhold/excludeにする。
4. 監査結果をpage単位で一度保存し、そのページの全table/columnへ参照させる。列単位で同じ法務確認を繰り返さない。
5. annotation exportにはsource page URL、revision、table offset、license、変更表示、追加帰属を機械的に添える。

### C. label staging時の分離
権利clearしたtrainだけを対象に、元headerをRWT metadataから戻す。独立ラベラーにはLoReTAの弱label/label_idを表示しない。注釈データの配布ライセンスは、Wikipedia由来素材のcollection/翻案の区分を確認してから設定し、MIT一本で上書きしない。test splitは触らない。

## 5. Claudeに求める判断

- RWT論文の「open-source and publicly available」とLoReTAのMIT表示を合わせた場合、RWT dataset/databaseの利用許諾として足りるか。足りない場合、どの権利と行為が不足するか。
- 2021-09-13のRWT snapshotに対し、2014–2023 Wikimedia TermsとCC BY-SA 3.0 Unportedをどう適用するか。CCのdata FAQにある3.0 database-rights扱いを踏まえ、権利主体・利用法域が特定されていないまま全trainを通せるか。
- table/column flatteningと人手ラベルを、CC BY-SA 3.0上のAdaptationかCollectionか、どの情報があれば確定できるか。全体配布時の適切なlicense noticeを示す。
- **結論が出るまでは全train rights_hold、test sealedのままにする。** ただし不足している根拠と、どの回答・監査記録が得られればHoldを解除できるかを具体的に提示する。

## 6. 参照URL

- RWT paper: https://arxiv.org/abs/2210.06353
- RWT archive repository: https://gitlab.com/unidata-labs/ru-wiki-tables-dataset
- LoReTA data card, MIT declaration and split counts: https://huggingface.co/datasets/aidalab/rwt-rutabert/commit/f82676c29c7d874162ecd153e46f1d79e4fb267a
- LoReTA source pinned for artifact audit: https://github.com/YRL-AIDA/LoReTA/tree/f12d7f83a70a065c90eb314a14e35bf177bade22
- LoReTA LICENSE: https://github.com/YRL-AIDA/LoReTA/blob/f12d7f83a70a065c90eb314a14e35bf177bade22/LICENSE
- Wikimedia 2014–2023 Terms, archived revision: https://foundation.wikimedia.org/w/index.php?oldid=98524&title=Policy:Terms_of_Use
- Current Wikimedia Terms / effective date and previous versions: https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
- CC BY-SA 3.0 Unported legal code: https://creativecommons.org/licenses/by-sa/3.0/legalcode.en
- CC treatment of databases and CC 3.0: https://wiki.creativecommons.org/wiki/Data


## 7. 国内の内部ラベル準備・学習に限る代替経路（2026-10-27追加）

### 結論
RWT作者の個別許諾がなくても、日本国内で行う「列の意味型を分類し、教師ラベルを作り、モデルを学習する」用途は、著作権法第30条の4（非享受目的の情報解析）を根拠に進められる可能性がある。これはRWTのライセンス取得ではなく、条件を満たす利用に著作権者の許諾を求めない法律上の権利制限ルートである。

文化庁の解説は「情報解析」を、大量の情報から要素情報を抽出し、比較・分類その他の解析を行うことと説明する。また、AI学習用データとしての収集・複製、学習用データセット作成、データセットを用いたモデル開発を、非享受目的であれば許諾なしで行える例として示す。列の型分類とその教師ラベル作成はこの定義にかなり近い。ただし文化庁資料は「人手アノテーションそのもの」を明示していないため、人手ラベリングを含むとの判断は条文・公的説明からの推論であり、確定した行政解釈として扱わない。

### 全件の内部ラベル準備をこの経路で進める前に確認・記録する条件
1. **実施法域**：対象コピー・確認・ラベル作業・学習を日本国内で行うことを想定する。Claude等の外部サービスへ表データを送る場合は、処理場所・サービス規約・契約条件を別に確認する。
2. **目的**：表現内容を読む・楽しむためではなく、列の意味型を抽出・比較・分類し、予測器を開発することを目的に固定する。作品表現そのものの再現、特定ページの内容再提示を目標にしない。
3. **権利者の利益への影響**：AI学習用として販売中または販売予定のデータベースを代替する使い方でないことを調べる。第30条の4ただし書の「著作権者の利益を不当に害する場合」は適用外になる。特に技術的制限、robots.txt、ID/パスワード等を回避しない。海賊版と知りながら取得した資料を使わない。
4. **必要な範囲**：列名と分類に必要な少数の値だけを見せ、アクセスを作業者に限定する。全表・全値を公開用成果物に複製しない。test split 115,448列は引き続き封印する。
5. **立証記録**：元dataset、固定commit・shard checksum、出典ページID/URL、取得条件、除外した列、表示した項目、ラベル・学習の目的と方法を保存する。後日、第30条の4の条件を説明できる形にする。

### この経路が解く範囲と解かない範囲
- **条件確認後に進められる可能性がある範囲**：train 1,325,901列を日本国内で非公開の型分類・ラベル作成・モデル学習に使うこと。RWTのdatabase/selectionが日本法上保護される著作物でも、必要な情報解析のための利用で第30条の4の要件を満たすなら、許諾不要となる可能性がある。創作性のあるデータベースは著作権法第12条の2で保護され得るため、その点も踏まえた法的確認が必要。
- **この根拠では解除しない範囲**：RWT/Wikipediaの表本文を含むデータセットや注釈済みCSVの公衆配布、元データの再販売、国外での複製・処理、AI出力で元の創作的表現を再現する使い方。これらは別の許諾・法域・条件の検討が必要。公開配布にはRWT配布元からの書面許諾が最短で、加えてWikipedia各ページの適用ライセンス、帰属、変更表示、import由来の追加条件を満たす。
- Hugging Face/LoReTAのMIT表示だけで上流権利は解決しない。第30条の4は著作権上の利用を扱うもので、配布サービスの契約条項・個人情報等の別問題も自動では解決しない。

### 作業判断
現時点では「国内分析ルートの候補を特定した」段階であり、全件をlabel-readyへ切り替えない。人手作業の当てはまり、実施場所、データベースの販売市場、サービス契約・アクセス条件を確認してから、内部ラベル準備だけを独立に解除できるか判定する。公開・再配布のholdは継続する。

### 追加した公的根拠
- 文化庁「AIと著作権」（第30条の4の情報解析定義、許諾不要の学習データ収集・モデル開発例、ただし書の販売DB市場）: https://www.bunka.go.jp/seisaku/chosakuken/pdf/93903601_01.pdf
- 文化庁「AIと著作権に関するチェックリスト＆ガイダンス」（有償データベース、アクセス制限、海賊版、学習目的・記録保存の注意）: https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/workingteam/r06_02/pdf/94150601_07.pdf
- e-Gov 著作権法（第12条の2、第30条の4）: https://laws.e-gov.go.jp/law/345AC0000000048
