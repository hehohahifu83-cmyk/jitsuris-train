# 独立評価 主セット #1（independent-main-20261021-v1）の採点・S6-5

最終更新：2026-10-21 17:44（日本時間）Claude（指示役）。事前登録 `independent_eval/PREREG_independent-main-20261021-v1.md`（commit `4634e229a36db9f0c9102ca67ba7580d1526461b`、06:56 UTC）の規則で読んだ。

## 要点
- **判定：E5-base を残す。** mmBERT-small は未知見出しの OK 率が平均 7.7 ポイント低い（差の 90% 区間 −11.6〜−4.2）。重大も多い（16.7 件対 16.0 件）。3 条件のどれも満たさず、ラベル 3 通り（裁定後・Claude 初回・ChatGPT 初回）のどれでも結論は同じ。診断（学習側の試験）で E5-base が上だった結果とも合う。
- **Guard v9.1（主）と v10（副）は、このセットでは同じ結果。** 6 つの予測の 313 列すべてで、v9.1 と v10 の判定は一つも違わない。副採点の数字も主採点と同じなので、表は v9.1 だけを載せる。
- E5-base の主指標は 77.9%（95% 区間 68.0〜86.7%）。区間が広いのは 32 表しかなく、NYC が採点列の 212／299 を占めるため。
- 弱いところ：quantity（OK 66.3%、重大 11.7 件。quantity を amount と答える取り違えが 3 種子で 23 件）と、正解が unknown の列への言い切り（12 列のうち平均 10 列）。札幌の日本語の列では、mmBERT-small が大きく落ちる（−18.7 ポイント）。
- 先生の初回ラベルが食い違った 7 列のうち、採点したのは 5 列（2 列は裁定で unknown／S になり、採点から外した）。

## 確かめたこと（実装・検査・実績の区別）
- 検査：予測 6 ファイルの SHA-256 が台帳 `independent_eval/predictions/ledger.jsonl`（6 行、`repeat_reason` は全部 null）と一致した。ラベル 3 ファイルの SHA-256 は事前登録と一致した。事前登録のコミットは予測より前（予測の台帳は 07:06 UTC 以降）。
- 見出しの既知／未知は、重みを作った学習コミット `8d688f5`（E5-base）の `encoder_exp` の学習行で決めた（学習側の見出しは 10,977 種類）。mmBERT-small の学習コミット `f87278a` も学習データは同じ（全 55,213 行。2 つのコミットの差は評価の道具と試験だけ）。
- 実績：採点は手元（CPU、非公開のラベル）で行った。モデルは再実行していない（保存した予測だけを使った）。公開するのは集計だけで、列ごとのラベルと列 ID は書いていない。
- `compare_models.py` の数字（全体 OK 78.0%／71.6%、未知見出し 77.9%／70.2%、重大 16.0／16.7）と、下の `independent_report.py` の数字は一致した。

## 判定（事前登録の規則）

| ラベル | 採点列 | 未知見出し列 | 未知見出し OK 率 基準線 | 候補 | 差（候補−基準線） | 差の 90% 区間 | 重大 基準線 | 候補 | 3 条件 |
|---|---:|---:|---:|---:|---:|---|---:|---:|---|
| 裁定後 | 299 | 272 | 77.9% | 70.2% | -7.7 pt | -11.6〜-4.2 pt | 16.0 | 16.7 | ×・×・× |
| Claude初回 | 300 | 273 | 77.8% | 70.1% | -7.7 pt | -11.6〜-4.1 pt | 15.7 | 16.7 | ×・×・× |
| ChatGPT初回 | 301 | 274 | 77.7% | 70.2% | -7.5 pt | -11.5〜-4.0 pt | 16.0 | 16.7 | ×・×・× |

3 条件＝(1) 差 ≥ +2.0 pt、(2) 重大 候補 ≤ 基準線、(3) 差の 90% 区間の下限 > 0。**結論：E5-base を残す**（ラベル 3 通りのどれでも条件を満たさない）。

## 主な指標（裁定後ラベル）

| 指標 | E5-base | mmBERT-small |
|---|---|---|
| 未知見出しの OK 率（95% 区間） | 77.9%（68.0%〜86.7%） | 70.2%（61.2%〜78.8%） |
| 差の 95% 区間（候補−基準線） | | -12.4〜-3.6 pt |
| 全体の OK 率（95% 区間） | 78.0%（68.9%〜86.0%） | 71.6%（63.2%〜79.5%） |
| 重大な取り違え（件、種子ごと） | 16.0（17・17・14） | 16.7（11・20・19） |
| 誤断定（誤答＋その他の誤受理、件） | 38.7（39・39・38） | 41.7（26・45・54） |
| 不明（見送り、件） | 27.0（25・23・33） | 43.3（47・43・40） |
| 重大の率（重大 5 種類の正解列 211 に対して） | 7.6% | 7.9% |
| 重大 5 種類を精度 99% で答えられる割合（確率の下限を動かす） | 23.5% | 28.8% |
| 正解が unknown の列（12、採点の外）への言い切り（件、種子ごと） | 10.0（7・12・11） | 11.0（11・12・10） |

## 層別（裁定後ラベル、OK 率と重大の件数は種子の平均）

| 区分 | 層 | 列 | E5-base OK 率 | mmBERT-small OK 率 | 差 | E5-base 重大 | mmBERT-small 重大 |
|---|---|---:|---:|---:|---:|---:|---:|
| 見出し | 既知ペア | 23 | 87.0% | 92.8% | +5.8 pt | 0.0 | 0.0 |
| 見出し | 既知見出し・別ラベル | 4 | 33.3% | 41.7% | +8.3 pt | 1.3 | 1.0 |
| 見出し | 未知見出し | 272 | 77.9% | 70.2% | -7.7 pt | 14.7 | 15.7 |
| 出典 | kobe | 17 | 80.4% | 76.5% | -3.9 pt | 0.0 | 0.0 |
| 出典 | nyc | 212 | 76.1% | 71.9% | -4.2 pt | 14.7 | 13.7 |
| 出典 | sapporo | 50 | 76.7% | 58.0% | -18.7 pt | 1.3 | 3.0 |
| 出典 | yokohama | 20 | 100.0% | 98.3% | -1.7 pt | 0.0 | 0.0 |
| 言語 | en | 212 | 76.1% | 71.9% | -4.2 pt | 14.7 | 13.7 |
| 言語 | ja | 87 | 82.8% | 70.9% | -11.9 pt | 1.3 | 3.0 |
| 先生の初回 | 一致した列 | 294 | 78.9% | 72.0% | -6.9 pt | 15.7 | 16.7 |
| 先生の初回 | 食い違った列 | 5 | 26.7% | 46.7% | +20.0 pt | 0.3 | 0.0 |
| 種類（正解） | quantity | 100 | 66.3% | 52.7% | -13.7 pt | 11.7 | 11.0 |
| 種類（正解） | date | 51 | 80.4% | 77.8% | -2.6 pt | 0.3 | 1.0 |
| 種類（正解） | category | 41 | 92.7% | 88.6% | -4.1 pt | 0.0 | 0.0 |
| 種類（正解） | amount | 25 | 92.0% | 93.3% | +1.3 pt | 2.0 | 0.7 |
| 種類（正解） | id | 21 | 73.0% | 61.9% | -11.1 pt | 1.0 | 3.0 |
| 種類（正解） | address | 20 | 81.7% | 78.3% | -3.3 pt | 0.0 | 0.0 |
| 種類（正解） | other | 15 | 97.8% | 100.0% | +2.2 pt | 0.0 | 0.0 |
| 種類（正解） | rate | 14 | 92.9% | 88.1% | -4.8 pt | 1.0 | 1.0 |
| 種類（正解） | org | 8 | 45.8% | 50.0% | +4.2 pt | 0.0 | 0.0 |
| 種類（正解） | text | 3 | 66.7% | 55.6% | -11.1 pt | 0.0 | 0.0 |
| 種類（正解） | account | 1 | 0.0% | 33.3% | +33.3 pt | 0.0 | 0.0 |

## ラベルの人別（全体の OK 率・未知見出しの OK 率・重大、種子の平均）

| ラベル | 採点列 | E5-base 全体 | mmBERT-small 全体 | E5-base 未知見出し | mmBERT-small 未知見出し | E5-base 重大 | mmBERT-small 重大 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 裁定後 | 299 | 78.0% | 71.6% | 77.9% | 70.2% | 16.0 | 16.7 |
| Claude初回 | 300 | 77.9% | 71.4% | 77.8% | 70.1% | 15.7 | 16.7 |
| ChatGPT初回 | 301 | 77.7% | 70.8% | 77.7% | 70.2% | 16.0 | 16.7 |

## 重大 5 種類の混同表（裁定後ラベル）

| 正解＼予測（E5-base、3 種子の合計） | date | amount | quantity | rate | id | その他の種類 | 不明 |
|---|---:|---:|---:|---:|---:|---:|---:|
| date | 123 | 0 | 0 | 0 | 1 | 4 | 25 |
| amount | 0 | 69 | 6 | 0 | 0 | 0 | 0 |
| quantity | 0 | 23 | 199 | 4 | 8 | 28 | 38 |
| rate | 0 | 0 | 3 | 39 | 0 | 0 | 0 |
| id | 0 | 0 | 3 | 0 | 46 | 4 | 10 |

| 正解＼予測（mmBERT-small、3 種子の合計） | date | amount | quantity | rate | id | その他の種類 | 不明 |
|---|---:|---:|---:|---:|---:|---:|---:|
| date | 119 | 0 | 1 | 0 | 2 | 3 | 28 |
| amount | 0 | 70 | 2 | 0 | 0 | 0 | 3 |
| quantity | 0 | 26 | 158 | 1 | 6 | 30 | 79 |
| rate | 0 | 0 | 3 | 37 | 0 | 0 | 2 |
| id | 0 | 0 | 9 | 0 | 39 | 6 | 9 |

## 再現の手順
```sh
# 1. 採点（ラベルは非公開の ai-bridge/labels/。ラベル 3 通り × guard 2 版 × 6 つの予測）
for lab in adjudicated claude chatgpt; do for g in v9.1 v10; do for run in 39502740378 39506074807; do for j in 1 2 3; do
  python evaluate_independent.py score --preds independent_eval/predictions/${run}_job$j.json \
    --labels ../ai-bridge/labels/$lab-independent-main-20261021-v1.json --out-dir out/$lab/$g/$run --run job$j --seed $j --guard-version $g
done; done; done; done
# 2. 学習側の見出し（重みを作った学習コミットの作業ツリーで作る）
git worktree add wt8d 8d688f5 && (cd wt8d && python -c "import json,slice_eval as S; p,h=S.train_sets_from_encoder_exp(); json.dump({'pairs':sorted(map(list,p)),'headers':sorted(h)},open('../train_headers.json','w'),ensure_ascii=False)")
(cd wt8d && python compare_models.py --group E5-base=../out/adjudicated/v9.1/39506074807:job1,job2,job3 --group mmBERT-small=../out/adjudicated/v9.1/39502740378:job1,job2,job3)
# 3. 区間・層別・判定
python independent_report.py --set independent_eval/results/main/independent_main.json --train-headers train_headers.json \
  --labels 裁定後=../ai-bridge/labels/adjudicated-independent-main-20261021-v1.json --labels Claude初回=…/claude-… --labels ChatGPT初回=…/chatgpt-… \
  --scored 裁定後=out/adjudicated/v9.1/39506074807,out/adjudicated/v9.1/39502740378 --scored Claude初回=… --scored ChatGPT初回=… \
  --primary 裁定後 --baseline E5-base --candidate mmBERT-small
```
（ブートストラップの乱数の種は 20261021 に固定。）

## ファイルの SHA-256
| ファイル | SHA-256 |
|---|---|
| 主セット `independent_eval/results/main/independent_main.json` | `4b47c72d70c30982123eaccdcbd1c8f6707d8bf1db8159b3774f1a4078ff3d87` |
| ラベル 裁定後（非公開） | `b73e8b75ae35f2642d35ff046e832e8ed20de6700478ea401bdd5dda8a11159f` |
| ラベル Claude 初回（非公開） | `e2d5181a2ce0739793b7f04cb3c34f917676a4fcc722ebdbb98b3f0605f219a8` |
| ラベル ChatGPT 初回（非公開） | `2b7fcb1e86c3043345894d430e521f455d80a4d9e5e75c2b1e5a860f304a5fc5` |
| 予測 `independent_eval/predictions/39502740378_job1.json` | `91f7575838923e0d117c6577a0d2cb239d070084c60b261d285d276e2e0e2c00` |
| 予測 `independent_eval/predictions/39502740378_job2.json` | `e589263dc7cc7509a8156f1140b2f4e6b02e530c2e442518337e4499cb9a498f` |
| 予測 `independent_eval/predictions/39502740378_job3.json` | `33637d65bf81a248366039f0afa06adbc56322f475abf0f2b527cb26d6a7cdbb` |
| 予測 `independent_eval/predictions/39506074807_job1.json` | `6f9781daeb91cbdf29fb1c1685cff216d6d12216370b396d6d9a65aa2c58962f` |
| 予測 `independent_eval/predictions/39506074807_job2.json` | `16ac6a41c2b12ce3247599001d36f900a45446b1750ded779027d66e670b961b` |
| 予測 `independent_eval/predictions/39506074807_job3.json` | `bd079ddee8848a83c4897bbcb153f692c92b98866610645a6a0dade96e597df8` |

版：Guard 主 v9.1・副 v10（判定は同じ）、確率の下限 0.5・数値系の上位 2 つの差 0.25、LABEL_GUIDE v1.5。

**このセットは使い切り。** 以後の変更の判定には使わない（`independent_eval/SETS.md`）。ここで見えた弱点（quantity、unknown の列への言い切り、札幌の列）は、学習側の候補で同じ分析をしてから教材にする。主セットの列は教材にしない。
