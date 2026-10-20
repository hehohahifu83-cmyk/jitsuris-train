# ChatGPTによる誤り例の照合（2026-10-20）

## 読み方と限界

対象は2026-10-20の値・兄弟列付き誤り監査に掲載された12件。ChatGPTの解釈と記録済み正解を照合した。ただし、この作業時点では元の監査表に正解ラベルが記載済みだったため、これは盲検の独立試験ではなく、根拠の再点検である。固定試験の正答率としては扱わない。

| 例 | ChatGPTの解釈 | 記録済み正解 | 照合・対応 |
|---|---|---|---|
| Total Invoices Paid | quantity | quantity | 一致。支払済み請求書の件数。金額らしい数字だけでamountにしない。 |
| # Invoices Paid Within 5 Days | quantity | quantity | 一致。#・日数別件数・割合の兄弟列が根拠。 |
| Department（DOF/DOH/DFE） | org が妥当 | account と org が混在 | 正解ラベルとガイドv1.3の役所略号ルールに食い違いの疑い。学習保留。 |
| keyword | text がガイド v1.5 に沿う | category | 値がタグとして読める一方、ガイドはキーワード列をtextとする。教師裁定まで保留。 |
| Author（ユーザー名風） | person | person | 一致。ユーザー名もperson。 |
| Authors（複数人名） | person | person | 一致。複数著者でもperson。 |
| SurveyName | text | text | 一致。調査タイトルは組織名ではない。 |
| 教材費（全て0） | amount | amount | 一致。費用列は0だけでもamount。 |
| FINE | amount | amount | 一致。罰金は金額。元例では単位不足のため、単位を明示した合成例だけ教材化。 |
| Sales-goods-svcs等 | unknown（単位不足） | amount | 一致を確定できず。Amt-unitsの値が必要なので教材保留。 |
| 住家全壊 | quantity | quantity | 一致。件数。-9999は欠損コードとして扱う。 |
| Pelicula（映画題名） | text | text | 一致。題名はtext。 |

## 学習に反映したもの

曖昧なDepartment・keyword・単位不足の会計列は除外。誤りの型が明確な請求件数、ユーザー名/複数著者、調査名、ゼロ円費用、罰金、欠損コード付き数量、映画題名の計9件を、元試験の値を複製しない合成教材として `reviewed_replay.jsonl` に追加した。ChatGPT単独監査として記録しており、二者監査と同じ確度とは扱わない。

## 次の評価

固定試験由来の列は学習への転用後、性能評価に使わない。学習前後比較には別のprogress probeを使い、seed 1/2のベースラインとseed 1/2のリプレイ条件を一致させる。効果が1.5ポイント未満なら差なしとする。今回のprobeは以前にも使われた開発用指標であり、最終的な未見評価の代わりにはしない。
