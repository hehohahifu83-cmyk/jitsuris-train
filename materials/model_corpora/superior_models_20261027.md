# ジツリスの上位モデルとその学習データ（2026-10-27 Claude）

オーナー指示（2026-10-27）：「ジツリスの上位互換モデルを検索しその学習データを入手してくれ、教材もあるだけ」。
ChatGPT の下調べ（`README.md`）に、2025〜2026 年の新しいモデルと、配布元のライセンス表示の確認（`probe/probe_20261027.json`、Actions で Zenodo・Hugging Face・GitHub の記録を読んだ）を足した。

## 結論
- **そのまま「上位互換」になる公開モデルはない。** 公開されている列の種類の判定モデルは、どれも英語の表で、種類も Schema.org・DBpedia（数十〜数千種）。ジツリスの 16 種・日本語・ポルトガル語の表を、ブラウザの中で動かせる大きさで判定するものはない。
- いちばん強いのは大きな LLM（GPT-4o は SOTAB V2 で 0 ショット 80.9、Llama-70B は 67.4）。小さなモデルを LoRA で学習させても SOTAB で 0.66 前後。どちらもジツリスの形（ブラウザ内・無料）には入らない。
- なので「上位モデルの学習データ」をジツリスの教材として取り込み、種類を 16 種に読み替えて使うのが現実的な道。

## モデルと学習データ
| モデル（年） | 何をするか | 学習データ | コードのライセンス | 学習データの権利 | 扱い |
|---|---|---|---|---|---|
| Sherlock（2019） | 列ごとの特徴量で 78 種 | VizNet（Plotly・ManyEyes・WebTables・公開データ） | MIT | VizNet はライセンスなし | 取らない |
| Sato（2020） | Sherlock＋表の話題 | VizNet の WebTables | Apache-2.0 | 同上 | 取らない |
| TURL（2021） | Wikipedia の表の事前学習 | WikiTables（Wikipedia、CC BY-SA） | Apache-2.0 | 公式の配布が止まっている | 取らない |
| DODUO（2022） | 表全体を BERT で読み、列の種類と関係 | WikiTables（TURL）・VizNet | Apache-2.0 | README が「データは再配布しない」 | 取らない |
| TableLlama（2024） | Llama 2 を表の 11 課題で学習 | TableInstruct（TURL 由来の列の種類を含む） | MIT | **CC BY 4.0**（Hugging Face） | 点検 → 取る候補 |
| ArcheType（2024） | LLM への聞き方・候補の絞り方 | 新しいデータはない | — | — | 方法の参考だけ |
| AdaTyper（2023） | 使う人に合わせて種類を足す | GitTables | なし | GitTables は表ごとの許諾 | 方法の参考 |
| RECA（2023） | 似た表の文脈を足す | SemTab・WebTables | — | — | 方法の参考 |
| LoRA＋聞き方の増やし方（2025） | FLAN-T5 を LoRA で | SOTAB | — | — | 方法の参考 |
| 知識生成＋自己修正（2025） | LLM が種類の定義を作り直す | SOTAB V2 | — | — | 方法の参考（LABEL_GUIDE の作り方に近い） |
| ZTab（2026） | 決まった種類から擬似の表を作り LLM を学習 | T2D・SOTAB・WikiTable | なし | — | 方法の参考 |
| TabEmb（2026） | LLM の埋め込み＋列のグラフ | T2D・WikiTable・WebTables・SOTAB | なし | — | 取らない |
| SymCA（2026） | LLM の判断を規則に書き出す | SOTAB V2・T2D | — | — | 方法の参考（検査役 v2 に近い） |
| StraTyper（2026） | データの集まりから種類を見つける | — | — | — | 方法の参考 |

## 取ってよい学習データ（配布元がライセンスを明示）
| データ | 大きさ | ライセンス（配布元の表示） | 中身 | ジツリスへの使い道 |
|---|---|---|---|---|
| **SOTAB V2 for SemTab 2023** | 3.7 GB | CC BY 4.0（Zenodo 8422037） | Web の表（Schema.org の注釈つき）。学習 130,471 列・91 種 | 種類を 16 種に読み替えて弱いラベルの教材に。日付・電話・メール・郵便番号・価格・組織・人など、ジツリスの種類と重なる種類が多い |
| **WikiDBs 10k / 100k** | 0.7 GB / 45.6 GB | CC BY 4.0（Zenodo 8227452 / 11559814）、元は Wikidata（CC0） | Wikidata から作った関係 DB（表・列名・値） | 列の性質（日付・数量・識別子・URL・座標・項目）が Wikidata の型からわかる |
| SemTab 2023 WikidataTables | 10 MB | CC BY 4.0（Zenodo 8393535） | Wikidata から作った表 | 小さい。点検してから |
| GitTables CTA ベンチマーク | 3.6 MB | CC BY 4.0（Zenodo 5706316） | GitTables の 1,101 表と正解 | 小さい。読み替えの確認用 |
| TableInstruct | 1M〜10M 例 | CC BY 4.0（Hugging Face） | 表の課題の指示データ（列の種類は TURL 由来） | 列の種類の部分だけ。元が Wikipedia（CC BY-SA）なので扱いを点検で決める |
| GitTables 1M v0.0.6 | 15.1 GB | CC0（Zenodo）／CC BY 4.0（公式サイト）、表ごとの許諾 | GitHub の CSV | ChatGPT が表ごとの許諾の確認つきで進めている（b046・b047） |

取らないもの：VizNet（Sherlock・Sato の元、ライセンスなし）、TabLib（「other」・利用申請制）、TURL の非公式の写し、RWT（凍結）。

## 教材庫に入れる前の決まり（変えない）
1. 外のデータのラベルは**弱いラベル**。16 種への読み替えは意味が同じものだけ（読み替えの表は `fetch_corpus.py` に置く）。読み替えられない種類は使わない。
2. 教材庫（`batch_*.jsonl`）には、今までどおり先生 2 人の独立の確認と Claude の裁定を通ったものだけを入れる。量が多いので、弱いラベルの教材は別の置き場（`data/<名前>/`）に置き、学習に混ぜるかどうか・混ぜ方は事前記録を書いてオーナーの許可を取ってから。
3. ベンチマークの試験用の分割（test）は学習に使わない。
4. 出典表示（CC BY 4.0）は置き場の `ATTRIBUTION.md` に書く。

## 出典
- 検索：[LoRA＋聞き方の増やし方（arXiv 2512.22742）](https://arxiv.org/html/2512.22742)、[知識生成と自己修正（arXiv 2503.02718）](https://arxiv.org/html/2503.02718v1)、[SymCA（arXiv 2607.25228）](https://arxiv.org/html/2607.25228)、[StraTyper](https://www.alphaxiv.org/ja/abs/2602.04004)、[RECA](https://dl.acm.org/doi/10.14778/3583140.3583149)、[TabEmb](https://arxiv.org/pdf/2604.18939)、[AdaTyper](https://github.com/madelonhulsebos/AdaTyper)、[ChatGPT による列の種類の注釈](https://arxiv.org/pdf/2306.00745)、[WikiDBs](https://zenodo.org/records/11559814)、[TableLlama](https://arxiv.org/pdf/2311.09206)、[TableInstruct](https://huggingface.co/datasets/osunlp/TableInstruct)、[SemTab 2024](https://ceur-ws.org/Vol-3889/paper0.pdf)、[SOTAB V2 for SemTab 2023](https://zenodo.org/records/8422037)
- ライセンスの確認：`probe/probe_20261027.json`（Actions run、2026-10-27）
