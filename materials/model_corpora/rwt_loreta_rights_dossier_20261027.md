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
