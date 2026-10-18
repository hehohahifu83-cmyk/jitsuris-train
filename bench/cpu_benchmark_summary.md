# CPU学習ベンチマーク（2026-10-18）

## 条件

- GitHub-hosted Ubuntu ランナー（4 CPU）
- `intfloat/multilingual-e5-small`、1 epoch、教材の先頭1500行、`FT_SEED=1`
- 評価は開発用220だけ。未見セットは使用していない
- 学習時間はモデル読み込みを除き、学習データ準備・トークン化と学習ループを含む。評価時間は別計測
- A=(cache off, 4 threads)、B=(cache on, 4 threads)、C=(cache on, 2 threads)、順序 A1→B1→C1→C2→B2→A2

## 測定

| Run | Cache | Threads | 学習秒 | 評価秒 |
|---|---:|---:|---:|---:|
| A1 | 0 | 4 | 224 | 10 |
| B1 | 1 | 4 | 224 | 10 |
| C1 | 1 | 2 | 184 | 8 |
| C2 | 1 | 2 | 185 | 8 |
| B2 | 1 | 4 | 226 | 10 |
| A2 | 0 | 4 | 225 | 10 |

| 条件 | 平均学習秒 | 2回の差 | 比較 |
|---|---:|---:|---:|
| A: cache off / 4 threads | 224.5 | 1 | — |
| B: cache on / 4 threads | 225.0 | 2 | A比 0.2%遅い（差なし） |
| C: cache on / 2 threads | 184.5 | 1 | B比 18.0%速い |

## 正しさの確認

- A1/B1 と A2/B2 の最初の20 step lossは、すべて小数3桁まで一致。
- C1/C2 の最初の20 step lossも一致。
- 先頭1500行のスモーク試験では、微調整モデル単独が開発用220列すべてを `unknown` とした。行数制限と1 epochの動作確認用で、モデル品質の評価結果として扱わない。
- 4 CPUのこのランナーでは、キャッシュによる時間短縮は確認できなかった。2 thread設定は2回とも4 threadより約40秒短く、2回のばらつき（最大2秒）を超え、10%基準も満たした。
- この測定は1種類のGitHub-hostedランナー上の結果であり、他CPU環境で同じ改善率になるとは確認していない。

## 実行ログ

- 5条件のログ: GitHub Actions run `39084868596` artifact `cpu-training-benchmark`（25分上限で終了、ログは保存）
- A2のログ: GitHub Actions run `39086572586` artifact `cpu-training-benchmark`（成功）
