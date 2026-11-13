# G2・G3 許可評価の全問題出力監査（2026-11-13 Codex）

## 対象と制約

- G2 run 43203533532（GovData.de、採点228列、L24＋G 3 seed）とG3 run 43354388430（Alberta・Ontario・Berlin、採点555列、L24＋G / L24S＋G各3 seed）を対象にした。
- 保存済み `g2_eval_per_column.json` / `g3_eval_per_column.json` と各予測JSON、二者裁定済みラベルを機械照合した。全ての wrong / critical / unknown を下表に一度以上載せた。
- 記号：O=正解、U=unknown、W=その他誤り、C=重大誤り。
- 生値、兄弟列、元表本文、tokenizerトークン列、教材近傍、重複検索結果はこれらの成果物に入っていない。そのため、それらが原因という説明は未確認仮説に留める。

## 観測事実

### G2 L24＋G
- seed別：L24+G1 {"ok":187,"wrong":19,"unk":22}；L24+G2 {"ok":186,"wrong":18,"unk":23,"crit":1}；L24+G3 {"ok":185,"wrong":20,"unk":22,"crit":1}。
- 問題のseed再発数（列単位）：{"0":178,"1":8,"2":8,"3":34}。
- 正解ラベル別の問題出力：{"product":{"crit":0,"wrong":3,"unk":0},"account":{"crit":0,"wrong":23,"unk":1},"address":{"crit":0,"wrong":14,"unk":1},"amount":{"crit":2,"wrong":0,"unk":13},"category":{"crit":0,"wrong":6,"unk":1},"id":{"crit":0,"wrong":1,"unk":26},"quantity":{"crit":0,"wrong":0,"unk":17},"org":{"crit":0,"wrong":10,"unk":2},"rate":{"crit":0,"wrong":0,"unk":6}}。
- 後段経路：{"total_problem":126,"raw_correct_to_unknown":2,"raw_wrong_to_unknown":1,"raw_wrong_accepted":79,"raw_correct_but_problem":0,"guard_changed":3,"reasons":{"(none)":123,"probability_below_threshold":3},"conf":{"lt50":3,"p50_70":14,"p70_90":27,"gte90":82}}。
- 直しMは実装の上書き不具合を修正して再採点しても変更0列。L24＋G 81.58%、重大2（3 seed合計）で、Mの効果は確認できない。

### G3 L24＋G
- seed別：L24+G1 {"ok":410,"unk":111,"crit":2,"wrong":32}；L24+G2 {"ok":416,"unk":103,"wrong":35,"crit":1}；L24+G3 {"ok":409,"unk":109,"wrong":36,"crit":1}。
- 問題のseed再発数（列単位）：{"0":401,"1":11,"2":10,"3":133}。
- 正解ラベル別の問題出力：{"id":{"crit":1,"wrong":17,"unk":30},"quantity":{"crit":0,"wrong":4,"unk":58},"amount":{"crit":3,"wrong":0,"unk":153},"text":{"crit":0,"wrong":28,"unk":6},"address":{"crit":0,"wrong":15,"unk":5},"account":{"crit":0,"wrong":18,"unk":1},"date":{"crit":0,"wrong":0,"unk":36},"category":{"crit":0,"wrong":15,"unk":12},"org":{"crit":0,"wrong":6,"unk":0},"rate":{"crit":0,"wrong":0,"unk":22}}。
- 後段経路：{"total_problem":430,"raw_correct_to_unknown":49,"raw_wrong_to_unknown":54,"raw_wrong_accepted":146,"raw_correct_but_problem":0,"guard_changed":103,"reasons":{"(none)":327,"other_class":21,"date_value_evidence_low":18,"numeric_top2_too_close":12,"probability_below_threshold":22,"numeric_values_not_parseable":24,"date_invalid_8digit":6},"conf":{"lt50":22,"p50_70":72,"p70_90":105,"gte90":231}}。
- 正解率74.17%、unknown 19.40%、重大4、その他誤り6.19%。Mは+0.42ポイント、重大差0、90%区間+0.06〜+0.90で事前基準+0.5に届かず不採用。

### G3 L24S＋G
- seed別：L24S+G1 {"ok":414,"unk":104,"wrong":35,"crit":2}；L24S+G2 {"ok":416,"unk":98,"wrong":36,"crit":5}；L24S+G3 {"ok":416,"unk":98,"crit":6,"wrong":35}。
- 問題のseed再発数（列単位）：{"0":403,"1":10,"2":17,"3":125}。
- 正解ラベル別の問題出力：{"id":{"crit":3,"wrong":17,"unk":27},"quantity":{"crit":0,"wrong":7,"unk":54},"amount":{"crit":3,"wrong":0,"unk":153},"text":{"crit":0,"wrong":29,"unk":5},"address":{"crit":0,"wrong":14,"unk":3},"account":{"crit":0,"wrong":19,"unk":0},"category":{"crit":0,"wrong":15,"unk":9},"date":{"crit":7,"wrong":0,"unk":29},"org":{"crit":0,"wrong":5,"unk":1},"rate":{"crit":0,"wrong":0,"unk":19}}。
- 後段経路：{"total_problem":419,"raw_correct_to_unknown":48,"raw_wrong_to_unknown":47,"raw_wrong_accepted":151,"raw_correct_but_problem":0,"guard_changed":95,"reasons":{"(none)":324,"numeric_top2_too_close":6,"probability_below_threshold":16,"date_value_evidence_low":18,"other_class":23,"numeric_values_not_parseable":26,"date_invalid_8digit":6},"conf":{"lt50":16,"p50_70":52,"p70_90":89,"gte90":262}}。
- 正解率74.83%、unknown 18.02%、重大13、その他誤り6.37%。L24＋G比で+0.66ポイントだが重大+9、90%区間-0.54〜+1.69のため銀教材は不採用。

## 原因評価

### 確認できたこと
1. G2でMが当初効かなかった実装上の理由は、採点器内でM適用後の値が上書きされたこと。修正後も変化0列なので、G2はMの能力改善を支持しない。
2. G3でMが変えたのは4種類。Patients、Approved Funding、Provincial Library Operating Grantはunknown→正解、Funding Status (Effective Date)はdate→unknown。改善は狭く、事前採用基準未達。
3. 銀教材の重大増加はFIR/SIR/FS Rec'dのdate→id、Rangeのid→date、WMUのid→quantityに集中する。rho金額戻しRの有無で重大13が変わらず、以前のrho経路とは別。
4. 問題出力には、生予測が正解でも後段がunknownにするもの、生予測誤りをunknownへ退避するもの、誤りを受理するものが全てある。したがって本体だけ、guardだけの単一原因ではない。

### 仮説（未確定）
- 海外のamount/rate/quantityでunknownが多いのは、見出し・単位・表題・兄弟列の手掛かり不足、学習分布の日本偏重、短縮語・多言語表記、検査役の確信度不足の複合である可能性が高い。
- 銀教材はdate/id境界の表現分布を崩した可能性がある。ただし教材行と各G3列の近傍・勾配影響を保存していないため因果は確定できない。
- 高確信の誤受理はラベル境界・意味文脈不足または教材偏り、低確信unknownは表現不足・後段しきい値の可能性がある。確率だけで原因は確定できない。

### 未確認・追加確認
- ラベル妥当性：二者独立ラベルと裁定は完了済み。変更は新しい根拠を二者が独立確認し裁定するまで行わない。
- 重複/漏洩、教材近傍、出典差、UNIT/兄弟列/値、前処理、tokenizer/truncation、特徴量、しきい値、検査役、seed、実装の個別因果は、現在の予測成果物だけでは確定不能。
- 次は使用済みG2/G3に合わせて規則を調整せず、未使用の評価陣を先に凍結してから一要因だけ検証する。優先候補は「数値列だけに表題・UNIT・兄弟列の構造化文脈を付ける」。期待効果はamount/rate/quantityのunknown低減、副作用はcategory/date/idへの誤受理増加。重大非増加を必須条件にする。
- ChatGPT/Claude同一課題比較は未実施で、目標達成の証拠はまだない。

## 全問題ケース

### G2：L24＋Gで少なくとも1 seedが問題

| ID | 列名 | 正解 | seed 1/2/3 | 最終予測 1/2/3 | 生予測 1/2/3 | 理由 1/2/3 | top1確率 1/2/3 |
|---|---|---|---|---|---|---|---|
| g2-0046 | hilfsmittel/ersatzleistungen | product | W/W/W | text/category/text | text/category/text | — / — / — | 0.674/0.581/0.597 |
| g2-0053 | dienststellenbezeichnung | account | W/W/W | org/org/org | org/org/org | — / — / — | 0.835/0.682/0.852 |
| g2-0054 | anschrift_plz | address | O/W/O | id/id/id | id/id/id | — / — / — | 0.823/0.962/0.895 |
| g2-0056 | postfach | address | W/O/W | id/address/id | id/address/id | — / — / — | 0.991/0.505/0.974 |
| g2-0060 | fue-ausgaben insgesamt | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.805/0.833/0.734 |
| g2-0061 | darunter drittmittel | amount | U/C/C | amount/quantity/quantity | amount/quantity/quantity | — / — / — | 0.785/0.881/0.808 |
| g2-0062 | sozialleistungen insgesamt | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.838/0.795/0.868 |
| g2-0063 | bruttoinlandsprodukt | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.923/0.977/0.940 |
| g2-0067 | organisation3 | address | W/W/W | org/org/org | org/org/org | — / — / — | 0.965/0.936/0.959 |
| g2-0102 | zeit_code | category | O/O/U | category/category/unknown | category/category/id | — / — / probability_below_threshold | 0.668/0.956/0.453 |
| g2-0105 | 1_merkmal_code | id | O/U/U | id/id/id | id/id/id | — / — / — | 0.966/0.888/0.931 |
| g2-0106 | 1_merkmal_label | category | W/O/O | address/category/category | address/category/category | — / — / — | 0.596/0.689/0.870 |
| g2-0107 | 1_auspraegung_code | id | U/O/O | id/id/id | id/id/id | — / — / — | 0.909/0.965/0.972 |
| g2-0111 | organisation | address | W/W/W | org/org/org | org/org/org | — / — / — | 0.872/0.807/0.924 |
| g2-0113 | organisation3 | account | W/W/W | org/org/org | org/org/org | — / — / — | 0.978/0.970/0.981 |
| g2-0129 | organisation | account | W/W/W | org/org/org | org/org/org | — / — / — | 0.965/0.964/0.980 |
| g2-0130 | organisation2 | account | W/W/W | org/org/org | org/org/org | — / — / — | 0.965/0.978/0.960 |
| g2-0133 | erhebungsmerkmale | category | W/W/O | text/text/category | text/text/category | — / — / — | 0.868/0.565/0.894 |
| g2-0151 | kontinuität bei stärkerer zuwanderung (in millionen) | quantity | U/O/U | rate/quantity/rate | rate/quantity/rate | — / — / — | 0.899/0.596/0.903 |
| g2-0167 | abkuerzung | org | O/W/W | org/category/category | org/category/category | — / — / — | 0.519/0.689/0.879 |
| g2-0170 | leitweg_id | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.994/0.992/0.993 |
| g2-0208 | bezeichnung | org | O/W/W | org/category/category | org/category/category | — / — / — | 0.676/0.672/0.947 |
| g2-0220 | indenture_number_pos1 | id | U/O/O | id/id/id | id/id/id | — / — / — | 0.888/0.954/0.969 |
| g2-0221 | indenture_number_pos2 | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.960/0.974/0.975 |
| g2-0222 | indenture_number_pos3 | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.934/0.973/0.968 |
| g2-0224 | value | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.989/0.990/0.988 |
| g2-0230 | 1_merkmal_code | id | O/U/W | id/id/category | id/id/category | — / — / — | 0.973/0.741/0.706 |
| g2-0252 | abkürzung | org | W/U/U | id/id/id | id/id/id | — / — / — | 0.956/0.883/0.560 |
| g2-0260 | anteil an allen nicht deutschen einwohnern 15 bis unter 65 j | rate | U/U/U | rate/rate/rate | rate/rate/rate | — / — / — | 0.985/0.972/0.977 |
| g2-0262 | anteil an allen einwohnern 15 bis unter 25 jahren | rate | U/U/U | rate/rate/rate | rate/rate/rate | — / — / — | 0.982/0.952/0.969 |
| g2-0267 | dienststellenbezeichnung | org | W/O/O | address/org/org | address/org/org | — / — / — | 0.613/0.823/0.897 |
| g2-0268 | postfach | address | W/U/W | id/unknown/id | id/address/id | — / probability_below_threshold / — | 0.990/0.496/0.982 |
| g2-0269 | postfach_plz | address | O/O/W | id/id/id | id/id/id | — / — / — | 0.615/0.566/0.959 |
| g2-0271 | kfz_bundeskasse | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.700/0.593/0.682 |
| g2-0272 | bundeskasse_bezeichnung | account | W/U/W | org/unknown/org | org/account/org | — / probability_below_threshold / — | 0.948/0.379/0.624 |
| g2-0273 | bundeskasse_plz | address | O/W/W | id/id/id | id/id/id | — / — / — | 0.856/0.980/0.960 |
| g2-0285 | organisation2 | account | W/W/W | org/org/org | org/org/org | — / — / — | 0.979/0.962/0.979 |
| g2-0308 | bezeichnung | org | O/W/O | org/category/org | org/category/org | — / — / — | 0.906/0.931/0.897 |
| g2-0312 | tgr./mgr. | id | U/U/U | id/quantity/id | id/quantity/id | — / — / — | 0.871/0.939/0.853 |
| g2-0313 | bezeichnung_3 | account | W/W/W | text/text/text | text/text/text | — / — / — | 0.964/0.964/0.883 |
| g2-0314 | titel | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.779/0.857/0.911 |
| g2-0315 | fz | category | W/W/W | id/id/id | id/id/id | — / — / — | 0.983/0.978/0.977 |
| g2-0316 | bezeichnung fz | account | W/W/W | category/category/category | category/category/category | — / — / — | 0.901/0.987/0.943 |
| g2-0341 | bezirksverwaltungen - schlüsselnummer 1000 | quantity | U/U/U | id/id/id | id/id/id | — / — / — | 0.986/0.957/0.948 |
| g2-0342 | eigene unternehmen - schlüsselnummer 1010 | quantity | U/U/U | id/id/id | id/id/id | — / — / — | 0.931/0.962/0.967 |
| g2-0345 | versichertenvertreter im vorstand - schlüsselnummer 1100 | quantity | U/U/U | id/id/id | id/id/id | — / — / — | 0.990/0.988/0.984 |
| g2-0346 | arbeitgebervertreter im vorstand - schlüsselnummer 1110 | quantity | U/U/U | id/id/id | id/id/id | — / — / — | 0.991/0.987/0.981 |
| g2-0347 | vertreter der selbständigen im vorstand - schlüsselnummer 11 | quantity | U/U/U | id/id/id | id/id/id | — / — / — | 0.908/0.849/0.975 |
| g2-0415 | hauptzollamt | org | W/W/W | address/address/address | address/address/address | — / — / — | 0.978/0.984/0.979 |
| g2-0417 | bic | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.993/0.989/0.990 |


### G3：L24＋Gで少なくとも1 seedが問題

| ID | 列名 | 正解 | seed 1/2/3 | 最終予測 1/2/3 | 生予測 1/2/3 | 理由 1/2/3 | top1確率 1/2/3 |
|---|---|---|---|---|---|---|---|
| g3-0013 | facility cost centre (fcc) id | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.992/0.993/0.993 |
| g3-0044 | sample | id | C/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.981/0.805/0.862 |
| g3-0048 | aeshnidae | quantity | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.855/0.536/0.518 |
| g3-0049 | athericidae | quantity | U/U/W | quantity/quantity/category | quantity/quantity/category | — / — / — | 0.690/0.616/0.798 |
| g3-0050 | ameletidae | quantity | U/U/W | quantity/unknown/category | quantity/quantity/category | — / probability_below_threshold / — | 0.907/0.483/0.849 |
| g3-0051 | ancylidae | quantity | U/U/W | quantity/quantity/category | quantity/quantity/category | — / — / — | 0.870/0.653/0.737 |
| g3-0063 | 22-23 fiscal funding | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.988/0.986/0.988 |
| g3-0067 | claims | quantity | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.763/0.746/0.867 |
| g3-0068 | services | quantity | U/U/U | amount/quantity/amount | amount/quantity/amount | — / — / — | 0.897/0.695/0.690 |
| g3-0069 | patients | quantity | U/O/O | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.917/0.977/0.972 |
| g3-0073 | alberta | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.908/0.690/0.775 |
| g3-0074 | britishcolumbia | amount | U/U/U | amount/unknown/amount | amount/amount/amount | — / numeric_top2_too_close / — | 0.917/0.560/0.816 |
| g3-0075 | manitoba | amount | U/U/U | amount/unknown/amount | amount/amount/amount | — / numeric_top2_too_close / — | 0.860/0.535/0.777 |
| g3-0076 | newbrunswick | amount | U/U/U | amount/unknown/amount | amount/quantity/amount | — / numeric_top2_too_close / — | 0.923/0.538/0.789 |
| g3-0077 | newfoundlandandlabrador | amount | U/U/U | amount/unknown/amount | amount/amount/amount | — / numeric_top2_too_close / — | 0.908/0.521/0.711 |
| g3-0078 | novascotia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.906/0.687/0.857 |
| g3-0079 | ontario | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.944/0.848/0.782 |
| g3-0096 | strength (format) | text | U/W/U | unknown/category/unknown | other/category/other | other_class / — / other_class | 0.775/0.684/0.812 |
| g3-0098 | reason for use | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.797/0.846/0.784 |
| g3-0101 | funding status* (effective date) | text | W/W/W | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.921/0.910/0.972 |
| g3-0113 | rural route number | address | U/U/U | id/id/id | id/id/id | — / — / — | 0.989/0.984/0.988 |
| g3-0145 | farmcashreceipttype | account | W/W/W | category/category/category | category/category/category | — / — / — | 0.986/0.985/0.989 |
| g3-0146 | alberta | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.980/0.981/0.984 |
| g3-0147 | britishcolumbia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.982/0.984/0.985 |
| g3-0148 | canada | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.985/0.987/0.986 |
| g3-0149 | manitoba | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.980/0.981/0.985 |
| g3-0150 | newbrunswick | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.984/0.984/0.985 |
| g3-0151 | newfoundlandandlabrador | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.973/0.975/0.984 |
| g3-0152 | novascotia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.985/0.984/0.985 |
| g3-0153 | ontario | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.982/0.983/0.985 |
| g3-0154 | recipient | address | W/W/W | org/org/org | org/org/org | — / — / — | 0.938/0.950/0.971 |
| g3-0163 | fir rec'd | date | U/U/U | id/unknown/id | id/quantity/id | — / numeric_top2_too_close / — | 0.751/0.580/0.833 |
| g3-0164 | fir validated | date | U/U/U | quantity/unknown/quantity | quantity/quantity/quantity | — / numeric_top2_too_close / — | 0.963/0.540/0.963 |
| g3-0165 | sir rec'd | date | U/U/U | quantity/id/id | quantity/id/id | — / — / — | 0.703/0.793/0.916 |
| g3-0166 | sir x-sch | date | U/U/U | unknown/unknown/id | other/other/id | other_class / other_class / — | 0.959/0.642/0.546 |
| g3-0167 | fs rec'd | date | U/U/U | id/quantity/id | id/quantity/id | — / — / — | 0.662/0.756/0.949 |
| g3-0176 | projecttitle | text | O/O/W | text/text/category | text/text/category | — / — / — | 0.833/0.940/0.612 |
| g3-0177 | areaprimary | category | U/U/U | unknown/unknown/unknown | other/rate/other | other_class / numeric_values_not_parseable / other_class | 0.700/0.690/0.768 |
| g3-0179 | disciplineprimary | category | W/W/W | unknown/id/id | id/id/id | numeric_top2_too_close / — / — | 0.542/0.731/0.826 |
| g3-0180 | disciplinesecondary | category | W/W/W | id/id/id | id/id/id | — / — / — | 0.966/0.907/0.973 |
| g3-0181 | round | id | W/W/W | category/category/category | category/category/category | — / — / — | 0.650/0.555/0.700 |
| g3-0237 | school special conditions | category | O/O/W | category/category/text | category/category/text | — / — / — | 0.838/0.705/0.716 |
| g3-0239 | fy | date | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.985/0.987/0.984 |
| g3-0240 | m_rgn | address | W/W/U | category/category/unknown | category/category/category | — / — / probability_below_threshold | 0.917/0.851/0.500 |
| g3-0241 | cass | org | W/W/W | address/address/address | address/address/address | — / — / — | 0.730/0.795/0.830 |
| g3-0246 | bereich | id | W/W/W | category/category/category | category/category/category | — / — / — | 0.885/0.805/0.590 |
| g3-0247 | bereichsbezeichnung | account | W/O/O | category/account/account | category/account/account | — / — / — | 0.930/0.518/0.701 |
| g3-0249 | einzelplanbezeichnung | account | W/W/W | category/category/category | category/category/category | — / — / — | 0.916/0.921/0.712 |
| g3-0251 | kapitelbezeichnung | account | W/W/U | text/text/unknown | text/text/account | — / — / probability_below_threshold | 0.784/0.958/0.424 |
| g3-0254 | hospitals | address | W/W/W | org/org/org | org/org/org | — / — / — | 0.966/0.947/0.976 |
| g3-0255 | hôpitaux | address | W/W/W | org/org/org | org/org/org | — / — / — | 0.936/0.893/0.958 |
| g3-0260 | program | category | W/O/U | account/category/unknown | account/category/account | — / — / probability_below_threshold | 0.757/0.804/0.496 |
| g3-0261 | approved funding | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.989/0.988/0.987 |
| g3-0272 | ch4 emissions (t/y) * | quantity | U/U/U | unknown/quantity/unknown | other/quantity/other | other_class / — / other_class | 0.502/0.621/0.814 |
| g3-0273 | ch4 emissions (t co2e/y) *** | quantity | U/U/U | unknown/unknown/unknown | other/other/other | other_class / other_class / other_class | 0.841/0.781/0.895 |
| g3-0274 | co2 emissions (t/y) * | quantity | U/U/U | unknown/quantity/unknown | other/quantity/other | other_class / — / other_class | 0.558/0.510/0.887 |
| g3-0275 | total ghg (t co2e) | quantity | U/U/U | unknown/unknown/quantity | amount/quantity/quantity | probability_below_threshold / probability_below_threshold / — | 0.449/0.499/0.529 |
| g3-0276 | mmbbl bitumen produced ** | quantity | U/U/U | unknown/quantity/unknown | other/quantity/other | other_class / — / other_class | 0.719/0.883/0.531 |
| g3-0280 | category | account | W/W/W | category/category/category | category/category/category | — / — / — | 0.948/0.991/0.981 |
| g3-0293 | n_children | category | U/U/U | unknown/unknown/unknown | quantity/quantity/quantity | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.944/0.639/0.546 |
| g3-0297 | n_children_include | quantity | O/W/O | unknown/category/unknown | quantity/category/quantity | numeric_values_not_parseable / — / numeric_values_not_parseable | 0.845/0.556/0.970 |
| g3-0298 | calc_entitledamt | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.987/0.988/0.988 |
| g3-0310 | out_exit_unemp | quantity | U/O/U | id/quantity/id | id/quantity/id | — / — / — | 0.649/0.873/0.761 |
| g3-0317 | moe region | address | U/O/W | unknown/address/category | category/address/category | probability_below_threshold / — / — | 0.469/0.739/0.505 |
| g3-0319 | amount | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.988/0.988/0.988 |
| g3-0320 | department | org | W/W/W | account/account/account | account/account/account | — / — / — | 0.810/0.932/0.920 |
| g3-0322 | pc | category | O/U/U | category/id/unknown | category/id/category | — / — / probability_below_threshold | 0.716/0.645/0.494 |
| g3-0332 | pump price/prix à la pompe | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.968/0.967/0.975 |
| g3-0334 | federal excise tax/taxe d'accise fédérale | amount | U/U/U | unknown/rate/amount | rate/rate/amount | probability_below_threshold / — / — | 0.498/0.652/0.590 |
| g3-0335 | federal carbon tax/taxe carbone fédérale | amount | U/U/U | rate/rate/unknown | rate/rate/other | — / — / other_class | 0.553/0.922/0.540 |
| g3-0336 | ontario tax/taxe de l'ontario | amount | U/U/U | unknown/rate/rate | amount/rate/rate | probability_below_threshold / — / — | 0.413/0.717/0.565 |
| g3-0337 | gst/hst / tps/tvh | amount | U/U/U | unknown/rate/amount | amount/rate/amount | probability_below_threshold / — / — | 0.334/0.732/0.573 |
| g3-0338 | wholesale margin/marge de gros | amount | U/U/U | unknown/unknown/amount | rate/rate/amount | numeric_top2_too_close / numeric_top2_too_close / — | 0.560/0.544/0.727 |
| g3-0339 | retail margin/marge de détail | amount | C/C/C | rate/rate/rate | rate/rate/rate | — / — / — | 0.854/0.952/0.669 |
| g3-0346 | fund status (statut du fonds) | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.980/0.979/0.974 |
| g3-0368 | when | date | U/U/U | date/date/date | date/date/date | — / — / — | 0.988/0.989/0.988 |
| g3-0376 | type of relief | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.984/0.987/0.975 |
| g3-0379 | wmu | id | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.679/0.944/0.935 |
| g3-0389 | trap_sum | quantity | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.856/0.772/0.875 |
| g3-0395 | services | quantity | U/U/U | unknown/quantity/quantity | amount/quantity/quantity | numeric_top2_too_close / — / — | 0.502/0.914/0.846 |
| g3-0398 | type | account | O/O/W | account/account/category | account/account/category | — / — / — | 0.628/0.519/0.872 |
| g3-0400 | alberta | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.772/0.959/0.971 |
| g3-0401 | britishcolumbia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.804/0.967/0.983 |
| g3-0402 | canada | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.823/0.979/0.971 |
| g3-0403 | manitoba | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.872/0.952/0.968 |
| g3-0404 | newbrunswick | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.938/0.980/0.982 |
| g3-0405 | newfoundlandandlabrador | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.884/0.961/0.978 |
| g3-0406 | novascotia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.841/0.971/0.976 |
| g3-0409 | services provided | category | W/W/W | text/text/text | text/text/text | — / — / — | 0.951/0.932/0.873 |
| g3-0414 | receiving media | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.987/0.991/0.989 |
| g3-0439 | effective date (date d'entrée en vigeur) | date | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.987/0.984/0.984 |
| g3-0440 | clear fuel regular (carburant incolore régulier) ¢/litre | amount | U/U/U | amount/unknown/rate | amount/rate/rate | — / probability_below_threshold / — | 0.685/0.402/0.815 |
| g3-0441 | clear fuel railway (carburant incolore ferroviaire) ¢/litre | amount | U/U/U | amount/rate/rate | amount/rate/rate | — / — / — | 0.546/0.502/0.781 |
| g3-0442 | single trip permits (permis de voyage temporaire) ¢/km | text | U/W/W | unknown/unknown/unknown | quantity/amount/amount | probability_below_threshold / numeric_values_not_parseable / numeric_values_not_parseable | 0.464/0.935/0.766 |
| g3-0443 | field | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.569/0.552/0.843 |
| g3-0446 | fy | date | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.985/0.986/0.983 |
| g3-0448 | sub_date | date | U/U/U | unknown/unknown/unknown | date/date/date | date_invalid_8digit / date_invalid_8digit / date_invalid_8digit | 0.989/0.989/0.989 |
| g3-0449 | approval_date | date | U/U/U | unknown/unknown/unknown | date/date/date | date_invalid_8digit / date_invalid_8digit / date_invalid_8digit | 0.990/0.989/0.989 |
| g3-0452 | timeline | quantity | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.906/0.955/0.831 |
| g3-0453 | desc_proj | text | U/U/O | unknown/unknown/text | text/category/text | probability_below_threshold / probability_below_threshold / — | 0.482/0.492/0.767 |
| g3-0454 | budget_fund | account | O/W/W | account/category/category | account/category/category | — / — / — | 0.769/0.636/0.664 |
| g3-0455 | targ_pop | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.902/0.924/0.980 |
| g3-0475 | municipality | address | W/W/O | org/org/address | org/org/address | — / — / — | 0.919/0.915/0.713 |
| g3-0479 | library system | id | W/W/W | category/category/category | category/category/category | — / — / — | 0.954/0.985/0.940 |
| g3-0480 | local appropriation | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.946/0.962/0.854 |
| g3-0481 | total local appropriation | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.946/0.969/0.886 |
| g3-0482 | provincial library operating grant | amount | U/U/U | amount/unknown/quantity | amount/amount/quantity | — / probability_below_threshold / — | 0.783/0.485/0.837 |
| g3-0485 | total cash receipts | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.987/0.990/0.988 |
| g3-0500 | 2007-2008 students suspended | quantity | O/O/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.986/0.993/0.902 |
| g3-0501 | 2007-2008 suspension rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.981/0.947/0.974 |
| g3-0503 | 2008-2009 suspension rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.984/0.974/0.976 |
| g3-0505 | 2009-2010 suspension rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.981/0.930/0.971 |
| g3-0507 | 2010-2011 suspension rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.982/0.960/0.975 |
| g3-0519 | township | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.567/0.553/0.930 |
| g3-0520 | range | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.874/0.806/0.756 |
| g3-0521 | meridian | id | U/U/U | unknown/unknown/unknown | other/other/other | other_class / other_class / other_class | 0.587/0.582/0.570 |
| g3-0522 | region | account | W/W/W | address/address/address | address/address/address | — / — / — | 0.948/0.695/0.761 |
| g3-0545 | value (million cubic metres) | quantity | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.772/0.867/0.830 |
| g3-0552 | 2007-2008 students expelled | quantity | U/O/O | rate/quantity/quantity | rate/quantity/quantity | — / — / — | 0.700/0.855/0.848 |
| g3-0553 | 2007-2008 expulsion rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.958/0.924/0.974 |
| g3-0555 | 2008-2009 expulsion rate | rate | O/U/O | rate/rate/rate | rate/rate/rate | — / — / — | 0.970/0.889/0.970 |
| g3-0557 | 2009-2010 expulsion rate | rate | U/U/U | rate/rate/rate | rate/rate/rate | — / — / — | 0.908/0.789/0.941 |
| g3-0559 | 2010-2011 expulsion rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.983/0.981/0.980 |
| g3-0568 | wmu | id | U/U/U | unknown/quantity/quantity | other/quantity/quantity | other_class / — / — | 0.654/0.875/0.765 |
| g3-0589 | grant title | text | O/O/U | text/text/unknown | text/text/other | — / — / other_class | 0.943/0.844/0.972 |
| g3-0592 | region | id | W/W/W | address/address/address | address/address/address | — / — / — | 0.980/0.956/0.971 |
| g3-0593 | landscape_guide_region | id | U/U/U | id/unknown/id | id/id/id | — / probability_below_threshold / — | 0.827/0.467/0.785 |
| g3-0594 | region_mnr | id | U/W/U | id/category/id | id/category/id | — / — / — | 0.634/0.910/0.758 |
| g3-0599 | city of organization | address | W/O/O | org/address/address | org/address/address | — / — / — | 0.595/0.557/0.842 |
| g3-0605 | annual income private (min.) /revenu privé annuel (min.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.982/0.990/0.986 |
| g3-0606 | annual income private (max.) /revenu privé annuel (max.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.987/0.989/0.987 |
| g3-0607 | gains / rrag | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.879/0.745/0.917 |
| g3-0608 | total oas/gis /sv/srg total | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.975/0.987/0.976 |
| g3-0609 | oas / sv | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.978/0.985/0.707 |
| g3-0610 | gis / srg | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.901/0.974/0.657 |
| g3-0611 | total monthly income (min.) /revenu mensuel total (min.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.957/0.988/0.983 |
| g3-0612 | total monthly income (max.) /revenu mensuel total (max.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.982/0.988/0.983 |
| g3-0613 | monthly income private (min.) /revenu privé mensuel (min.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.937/0.982/0.973 |
| g3-0614 | monthly income private (max.) /revenu privé mensuel (max.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.985/0.989/0.986 |
| g3-0633 | wmu | id | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.719/0.925/0.807 |
| g3-0640 | allocation | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.955/0.983/0.984 |
| g3-0642 | region | id | W/W/W | address/address/address | address/address/address | — / — / — | 0.973/0.891/0.937 |
| g3-0646 | spg | category | U/W/U | id/address/unknown | id/address/address | — / — / probability_below_threshold | 0.660/0.861/0.428 |
| g3-0647 | actharv_vol | quantity | U/U/U | quantity/quantity/unknown | quantity/quantity/quantity | — / — / probability_below_threshold | 0.926/0.964/0.480 |
| g3-0648 | ltmd_vol | quantity | U/O/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.913/0.952/0.579 |
| g3-0649 | offab_bench_vol | quantity | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.951/0.903/0.552 |
| g3-0664 | allowable values | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.976/0.966/0.968 |
| g3-0723 | program | category | U/O/W | unknown/category/account | account/category/account | probability_below_threshold / — / — | 0.482/0.876/0.727 |
| g3-0724 | fy | date | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.985/0.985/0.979 |
| g3-0728 | reimbursement | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.988/0.988/0.987 |
| g3-0743 | coordination of benefits(4) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.983/0.988/0.988 |
| g3-0759 | marketed production (cwts) | quantity | U/U/U | amount/unknown/unknown | amount/amount/amount | — / numeric_top2_too_close / numeric_top2_too_close | 0.895/0.572/0.517 |
| g3-0782 | funding round | id | U/W/U | unknown/category/unknown | category/category/category | probability_below_threshold / — / probability_below_threshold | 0.387/0.597/0.329 |
| g3-0788 | goal | category | W/O/W | text/category/text | text/category/text | — / — / — | 0.708/0.899/0.607 |


### G3：L24S＋Gで少なくとも1 seedが問題

| ID | 列名 | 正解 | seed 1/2/3 | 最終予測 1/2/3 | 生予測 1/2/3 | 理由 1/2/3 | top1確率 1/2/3 |
|---|---|---|---|---|---|---|---|
| g3-0013 | facility cost centre (fcc) id | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.994/0.995/0.995 |
| g3-0044 | sample | id | U/U/C | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.801/0.797/0.966 |
| g3-0048 | aeshnidae | quantity | U/W/O | quantity/category/quantity | quantity/category/quantity | — / — / — | 0.702/0.643/0.956 |
| g3-0049 | athericidae | quantity | U/W/U | quantity/category/quantity | quantity/category/quantity | — / — / — | 0.503/0.603/0.922 |
| g3-0050 | ameletidae | quantity | U/W/O | quantity/category/quantity | quantity/category/quantity | — / — / — | 0.909/0.593/0.950 |
| g3-0051 | ancylidae | quantity | U/W/U | quantity/category/quantity | quantity/category/quantity | — / — / — | 0.791/0.534/0.942 |
| g3-0063 | 22-23 fiscal funding | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.986/0.990/0.991 |
| g3-0067 | claims | quantity | U/U/U | unknown/quantity/unknown | quantity/quantity/quantity | numeric_top2_too_close / — / numeric_top2_too_close | 0.541/0.839/0.548 |
| g3-0068 | services | quantity | U/U/U | unknown/unknown/amount | quantity/quantity/amount | numeric_top2_too_close / numeric_top2_too_close / — | 0.522/0.544/0.788 |
| g3-0069 | patients | quantity | O/O/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.976/0.978/0.918 |
| g3-0073 | alberta | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.947/0.923/0.981 |
| g3-0074 | britishcolumbia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.936/0.888/0.966 |
| g3-0075 | manitoba | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.952/0.847/0.979 |
| g3-0076 | newbrunswick | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.951/0.682/0.967 |
| g3-0077 | newfoundlandandlabrador | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.942/0.871/0.967 |
| g3-0078 | novascotia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.965/0.899/0.977 |
| g3-0079 | ontario | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.975/0.924/0.985 |
| g3-0096 | strength (format) | text | U/U/W | unknown/unknown/category | category/other/category | probability_below_threshold / other_class / — | 0.484/0.905/0.720 |
| g3-0098 | reason for use | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.767/0.824/0.904 |
| g3-0101 | funding status* (effective date) | text | W/W/W | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.825/0.826/0.832 |
| g3-0113 | rural route number | address | U/U/U | id/id/id | id/id/id | — / — / — | 0.987/0.982/0.991 |
| g3-0118 | suite | address | W/O/O | org/address/address | org/address/address | — / — / — | 0.556/0.623/0.766 |
| g3-0145 | farmcashreceipttype | account | W/W/W | category/category/category | category/category/category | — / — / — | 0.982/0.897/0.849 |
| g3-0146 | alberta | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.988/0.982/0.978 |
| g3-0147 | britishcolumbia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.986/0.986/0.980 |
| g3-0148 | canada | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.988/0.976/0.982 |
| g3-0149 | manitoba | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.987/0.982/0.984 |
| g3-0150 | newbrunswick | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.989/0.982/0.987 |
| g3-0151 | newfoundlandandlabrador | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.987/0.985/0.986 |
| g3-0152 | novascotia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.989/0.985/0.983 |
| g3-0153 | ontario | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.987/0.982/0.984 |
| g3-0154 | recipient | address | O/W/W | address/org/org | address/org/org | — / — / — | 0.508/0.943/0.686 |
| g3-0157 | element | category | U/U/O | unknown/unknown/category | other/category/category | other_class / probability_below_threshold / — | 0.552/0.475/0.514 |
| g3-0163 | fir rec'd | date | U/C/C | id/id/id | id/id/id | — / — / — | 0.919/0.961/0.985 |
| g3-0164 | fir validated | date | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.956/0.929/0.954 |
| g3-0165 | sir rec'd | date | U/C/C | id/id/id | id/id/id | — / — / — | 0.937/0.984/0.994 |
| g3-0166 | sir x-sch | date | U/U/U | id/id/unknown | id/id/other | — / — / other_class | 0.896/0.528/0.891 |
| g3-0167 | fs rec'd | date | C/C/C | id/id/id | id/id/id | — / — / — | 0.989/0.971/0.992 |
| g3-0176 | projecttitle | text | W/O/W | category/text/category | category/text/category | — / — / — | 0.507/0.598/0.802 |
| g3-0177 | areaprimary | category | U/U/U | unknown/unknown/unknown | other/rate/rate | other_class / numeric_values_not_parseable / numeric_values_not_parseable | 0.518/0.799/0.533 |
| g3-0179 | disciplineprimary | category | W/W/W | id/id/id | id/id/id | — / — / — | 0.929/0.810/0.942 |
| g3-0180 | disciplinesecondary | category | W/W/W | id/id/id | id/id/id | — / — / — | 0.973/0.974/0.972 |
| g3-0181 | round | id | U/W/W | id/category/category | id/category/category | — / — / — | 0.545/0.757/0.859 |
| g3-0186 | element | category | W/U/O | text/unknown/category | text/category/category | — / probability_below_threshold / — | 0.624/0.460/0.927 |
| g3-0237 | school special conditions | category | W/O/W | text/category/text | text/category/text | — / — / — | 0.624/0.653/0.788 |
| g3-0239 | fy | date | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.990/0.967/0.986 |
| g3-0240 | m_rgn | address | W/O/W | category/address/category | category/address/category | — / — / — | 0.909/0.643/0.911 |
| g3-0241 | cass | org | W/W/U | address/address/unknown | address/address/address | — / — / probability_below_threshold | 0.949/0.861/0.447 |
| g3-0246 | bereich | id | W/W/W | category/category/category | category/category/category | — / — / — | 0.858/0.685/0.733 |
| g3-0247 | bereichsbezeichnung | account | W/W/O | category/category/account | category/category/account | — / — / — | 0.743/0.753/0.576 |
| g3-0249 | einzelplanbezeichnung | account | O/W/W | account/category/category | account/category/category | — / — / — | 0.530/0.621/0.921 |
| g3-0251 | kapitelbezeichnung | account | W/W/W | text/text/text | text/text/text | — / — / — | 0.732/0.763/0.603 |
| g3-0254 | hospitals | address | W/W/W | org/org/org | org/org/org | — / — / — | 0.953/0.963/0.959 |
| g3-0255 | hôpitaux | address | W/W/W | org/org/org | org/org/org | — / — / — | 0.810/0.904/0.904 |
| g3-0261 | approved funding | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.990/0.990/0.991 |
| g3-0272 | ch4 emissions (t/y) * | quantity | U/U/U | quantity/unknown/unknown | quantity/other/other | — / other_class / other_class | 0.777/0.826/0.626 |
| g3-0273 | ch4 emissions (t co2e/y) *** | quantity | U/U/U | unknown/unknown/unknown | other/other/other | other_class / other_class / other_class | 0.667/0.962/0.676 |
| g3-0274 | co2 emissions (t/y) * | quantity | U/U/U | unknown/unknown/unknown | other/other/other | other_class / other_class / other_class | 0.522/0.952/0.529 |
| g3-0275 | total ghg (t co2e) | quantity | U/U/U | unknown/unknown/unknown | other/other/other | other_class / other_class / other_class | 0.892/0.967/0.525 |
| g3-0276 | mmbbl bitumen produced ** | quantity | U/U/U | unknown/unknown/quantity | other/other/quantity | other_class / other_class / — | 0.646/0.884/0.842 |
| g3-0280 | category | account | W/W/W | category/category/category | category/category/category | — / — / — | 0.994/0.965/0.984 |
| g3-0293 | n_children | category | U/U/U | unknown/unknown/unknown | quantity/quantity/quantity | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.649/0.858/0.534 |
| g3-0296 | n_childrenexclude | quantity | U/U/O | amount/amount/quantity | amount/amount/quantity | — / — / — | 0.959/0.902/0.767 |
| g3-0297 | n_children_include | quantity | W/O/W | category/unknown/category | category/quantity/category | — / numeric_values_not_parseable / — | 0.786/0.708/0.724 |
| g3-0298 | calc_entitledamt | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.990/0.990/0.993 |
| g3-0311 | out_exit_sum_oth | quantity | O/U/O | quantity/unknown/quantity | quantity/id/quantity | — / probability_below_threshold / — | 0.969/0.453/0.952 |
| g3-0319 | amount | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.988/0.986/0.991 |
| g3-0320 | department | org | W/W/W | account/account/account | account/account/account | — / — / — | 0.791/0.856/0.774 |
| g3-0332 | pump price/prix à la pompe | amount | U/U/U | amount/amount/unknown | amount/amount/amount | — / — / numeric_top2_too_close | 0.923/0.755/0.571 |
| g3-0334 | federal excise tax/taxe d'accise fédérale | amount | U/U/U | unknown/rate/rate | amount/rate/rate | probability_below_threshold / — / — | 0.336/0.844/0.921 |
| g3-0335 | federal carbon tax/taxe carbone fédérale | amount | U/U/U | unknown/rate/rate | rate/rate/rate | probability_below_threshold / — / — | 0.481/0.886/0.855 |
| g3-0336 | ontario tax/taxe de l'ontario | amount | U/U/U | rate/rate/rate | rate/rate/rate | — / — / — | 0.627/0.838/0.967 |
| g3-0337 | gst/hst / tps/tvh | amount | U/U/U | unknown/rate/rate | rate/rate/rate | probability_below_threshold / — / — | 0.484/0.836/0.795 |
| g3-0338 | wholesale margin/marge de gros | amount | U/U/U | rate/rate/rate | rate/rate/rate | — / — / — | 0.783/0.957/0.952 |
| g3-0339 | retail margin/marge de détail | amount | C/C/C | rate/rate/rate | rate/rate/rate | — / — / — | 0.965/0.969/0.980 |
| g3-0346 | fund status (statut du fonds) | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.984/0.921/0.988 |
| g3-0362 | marketed production ('000 lbs) | quantity | O/O/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.980/0.987/0.950 |
| g3-0368 | when | date | U/U/U | date/date/date | date/date/date | — / — / — | 0.991/0.988/0.990 |
| g3-0376 | type of relief | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.966/0.983/0.980 |
| g3-0379 | wmu | id | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.958/0.911/0.968 |
| g3-0389 | trap_sum | quantity | U/O/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.937/0.977/0.935 |
| g3-0395 | services | quantity | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.929/0.903/0.751 |
| g3-0398 | type | account | W/W/W | category/category/category | category/category/category | — / — / — | 0.963/0.559/0.870 |
| g3-0399 | naics | category | O/O/W | category/category/account | category/category/account | — / — / — | 0.976/0.925/0.710 |
| g3-0400 | alberta | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.939/0.798/0.977 |
| g3-0401 | britishcolumbia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.965/0.869/0.977 |
| g3-0402 | canada | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.889/0.727/0.978 |
| g3-0403 | manitoba | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.956/0.864/0.983 |
| g3-0404 | newbrunswick | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.975/0.894/0.987 |
| g3-0405 | newfoundlandandlabrador | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.975/0.818/0.978 |
| g3-0406 | novascotia | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.971/0.886/0.984 |
| g3-0409 | services provided | category | W/W/W | text/text/text | text/text/text | — / — / — | 0.969/0.950/0.975 |
| g3-0414 | receiving media | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.992/0.991/0.991 |
| g3-0439 | effective date (date d'entrée en vigeur) | date | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.988/0.990/0.990 |
| g3-0440 | clear fuel regular (carburant incolore régulier) ¢/litre | amount | U/U/U | amount/amount/rate | amount/amount/rate | — / — / — | 0.523/0.526/0.913 |
| g3-0441 | clear fuel railway (carburant incolore ferroviaire) ¢/litre | amount | U/U/U | unknown/unknown/rate | amount/quantity/rate | probability_below_threshold / probability_below_threshold / — | 0.405/0.405/0.879 |
| g3-0442 | single trip permits (permis de voyage temporaire) ¢/km | text | W/W/W | unknown/unknown/unknown | amount/amount/amount | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.906/0.927/0.910 |
| g3-0443 | field | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.772/0.542/0.812 |
| g3-0446 | fy | date | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.988/0.951/0.986 |
| g3-0448 | sub_date | date | U/U/U | unknown/unknown/unknown | date/date/date | date_invalid_8digit / date_invalid_8digit / date_invalid_8digit | 0.987/0.988/0.992 |
| g3-0449 | approval_date | date | U/U/U | unknown/unknown/unknown | date/date/date | date_invalid_8digit / date_invalid_8digit / date_invalid_8digit | 0.987/0.990/0.992 |
| g3-0452 | timeline | quantity | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.933/0.978/0.969 |
| g3-0455 | targ_pop | text | W/W/O | category/category/text | category/category/text | — / — / — | 0.649/0.811/0.550 |
| g3-0479 | library system | id | W/W/W | category/category/category | category/category/category | — / — / — | 0.971/0.986/0.984 |
| g3-0480 | local appropriation | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.918/0.970/0.976 |
| g3-0481 | total local appropriation | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.952/0.979/0.981 |
| g3-0482 | provincial library operating grant | amount | U/U/U | unknown/amount/unknown | amount/amount/quantity | probability_below_threshold / — / numeric_top2_too_close | 0.499/0.788/0.574 |
| g3-0485 | total cash receipts | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.992/0.993/0.994 |
| g3-0501 | 2007-2008 suspension rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.980/0.980/0.983 |
| g3-0503 | 2008-2009 suspension rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.982/0.981/0.986 |
| g3-0505 | 2009-2010 suspension rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.979/0.980/0.985 |
| g3-0507 | 2010-2011 suspension rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.976/0.978/0.985 |
| g3-0519 | township | id | U/U/U | id/id/id | id/id/id | — / — / — | 0.885/0.914/0.842 |
| g3-0520 | range | id | U/C/U | id/unknown/id | id/date/id | — / probability_below_threshold / — | 0.647/0.426/0.714 |
| g3-0521 | meridian | id | U/U/U | unknown/unknown/unknown | other/other/other | other_class / other_class / other_class | 0.872/0.508/0.503 |
| g3-0522 | region | account | W/W/W | address/address/address | address/address/address | — / — / — | 0.939/0.875/0.880 |
| g3-0539 | coverage category and type of service | category | O/W/O | category/account/category | category/account/category | — / — / — | 0.781/0.536/0.802 |
| g3-0545 | value (million cubic metres) | quantity | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.899/0.797/0.920 |
| g3-0553 | 2007-2008 expulsion rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.965/0.977/0.982 |
| g3-0554 | 2008-2009 students expelled | quantity | O/O/W | unknown/unknown/category | quantity/quantity/category | numeric_values_not_parseable / numeric_values_not_parseable / — | 0.821/0.894/0.870 |
| g3-0557 | 2009-2010 expulsion rate | rate | U/O/O | rate/rate/rate | rate/rate/rate | — / — / — | 0.726/0.974/0.957 |
| g3-0559 | 2010-2011 expulsion rate | rate | U/U/U | unknown/unknown/unknown | rate/rate/rate | numeric_values_not_parseable / numeric_values_not_parseable / numeric_values_not_parseable | 0.985/0.984/0.986 |
| g3-0568 | wmu | id | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.938/0.967/0.958 |
| g3-0589 | grant title | text | U/U/U | unknown/unknown/unknown | other/other/other | other_class / other_class / other_class | 0.633/0.984/0.982 |
| g3-0592 | region | id | W/W/W | address/address/address | address/address/address | — / — / — | 0.965/0.981/0.976 |
| g3-0593 | landscape_guide_region | id | W/W/U | category/category/unknown | category/category/id | — / — / probability_below_threshold | 0.772/0.821/0.420 |
| g3-0594 | region_mnr | id | W/U/U | category/id/id | category/id/id | — / — / — | 0.522/0.757/0.656 |
| g3-0599 | city of organization | address | W/O/O | org/address/address | org/address/address | — / — / — | 0.522/0.597/0.855 |
| g3-0605 | annual income private (min.) /revenu privé annuel (min.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.991/0.988/0.991 |
| g3-0606 | annual income private (max.) /revenu privé annuel (max.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.992/0.990/0.992 |
| g3-0607 | gains / rrag | amount | U/U/U | unknown/amount/amount | amount/amount/amount | probability_below_threshold / — / — | 0.486/0.503/0.866 |
| g3-0608 | total oas/gis /sv/srg total | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.992/0.986/0.985 |
| g3-0609 | oas / sv | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.989/0.977/0.926 |
| g3-0610 | gis / srg | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.984/0.969/0.902 |
| g3-0611 | total monthly income (min.) /revenu mensuel total (min.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.983/0.985/0.990 |
| g3-0612 | total monthly income (max.) /revenu mensuel total (max.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.989/0.989/0.991 |
| g3-0613 | monthly income private (min.) /revenu privé mensuel (min.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.930/0.911/0.965 |
| g3-0614 | monthly income private (max.) /revenu privé mensuel (max.) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.990/0.986/0.989 |
| g3-0633 | wmu | id | U/U/C | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.933/0.900/0.960 |
| g3-0640 | allocation | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.985/0.987/0.984 |
| g3-0642 | region | id | W/W/W | address/address/address | address/address/address | — / — / — | 0.974/0.973/0.923 |
| g3-0646 | spg | category | O/O/W | category/category/address | category/category/address | — / — / — | 0.550/0.502/0.918 |
| g3-0647 | actharv_vol | quantity | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.932/0.898/0.896 |
| g3-0648 | ltmd_vol | quantity | O/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.954/0.610/0.849 |
| g3-0649 | offab_bench_vol | quantity | U/U/U | quantity/quantity/quantity | quantity/quantity/quantity | — / — / — | 0.830/0.937/0.864 |
| g3-0664 | allowable values | text | W/W/W | category/category/category | category/category/category | — / — / — | 0.978/0.988/0.984 |
| g3-0724 | fy | date | U/U/U | unknown/unknown/unknown | date/date/date | date_value_evidence_low / date_value_evidence_low / date_value_evidence_low | 0.985/0.962/0.984 |
| g3-0728 | reimbursement | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.989/0.988/0.992 |
| g3-0743 | coordination of benefits(4) | amount | U/U/U | amount/amount/amount | amount/amount/amount | — / — / — | 0.988/0.992/0.989 |
| g3-0752 | prov | address | O/W/W | address/category/category | address/category/category | — / — / — | 0.867/0.607/0.961 |
| g3-0759 | marketed production (cwts) | quantity | U/U/U | amount/quantity/amount | amount/quantity/amount | — / — / — | 0.641/0.944/0.739 |
| g3-0782 | funding round | id | U/U/O | unknown/unknown/unknown | date/category/id | probability_below_threshold / probability_below_threshold / probability_below_threshold | 0.331/0.459/0.338 |


