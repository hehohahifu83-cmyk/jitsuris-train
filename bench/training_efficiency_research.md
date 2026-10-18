# 学習の品質と速度を同時に上げる研究メモ

更新日: 2026-10-18  
対象: `hehohahifu83-cmyk/jitsuris-train` の e5-small / e5-base 微調整（Kaggle Tesla T4×2）。  
範囲: 固定試験と既存ベンチの再分析、一次資料の照合。未見セットは使わず、追加の学習依頼も出していない。

## 結論

すぐに活かせる本命は、**埋め込み層固定を維持し、固定試験で確認すること**。e5-smallの版15ではseed 1・2の両方で固定試験の品質差は小さく、学習時間はそれぞれ236→197秒（1.20倍速）、233→220秒（1.06倍速）。一方、速度設定（長さ順、pad8、fused AdamW、AMP）は既に使われており、INT8は既存判定基準に届かない。

次の速度余地は、測定しないまま設定を足すことではなく、(1) e5-smallで実効バッチ64を一度に流す条件、(2) 静的な学習文のトークン化を先に済ませる条件、(3) 1周で止めても品質が保てるか、を小さく分けて測ること。品質改善の研究では、進行中のUNIT文脈A/Bを先に完了させ、学習率1e-4はseed違いで再現するまで採用しない。

## 既存実測から言えること

### 1. GPUの既存高速設定は有効な土台

版14のe5-base実測（Tesla T4×2）で、実効バッチ64の設定を比べると、既定の小バッチ＋gradient checkpointingの13.2文/秒に対して、BS16・checkpointingなしは52.3文/秒（3.96倍）、さらに長さ順化で61.7文/秒（4.67倍）だった。勾配比較はdropoutなしで相対差約0.0012〜0.0013。実際のdropoutを含む学習では乱数マスクの割り当てが変わるため、固定試験も併せて見る必要がある。

版15では e5-small の仕事1〜8に `FT_BS=32 FT_ACC=2 FT_CKPT=0 FT_SORT=1 FT_PAD8=1 FT_FUSED=1` を使用。これは現行の標準候補として維持する。gradient checkpointingはGPUメモリを節約する代わりに再計算を増やすため、T4でメモリに余裕があればオフの方が筋がよい。T4上のAMPはFP16で既に動いている。bf16やTF32は機種対応を確認せずに切り替えない。

### 2. 埋め込み固定は速度・品質の両面で有望

版15の対応比較（学習時間、固定試験の正解率）:

| seed | 通常 | 埋め込み固定 | 品質差（固定−通常） |
|---|---:|---:|---|
| 1 | 236秒 | 197秒 | dev +0.5pt、一般 +0.4pt、業務 0.0pt、業務2 −0.3pt、調達 0.0pt |
| 2 | 233秒 | 220秒 | dev +0.5pt、一般 −0.3pt、業務 −0.4pt、業務2 +0.3pt、調達 0.0pt |

いずれも既定の「1.5ポイント未満は差なし」という目安内。2つのseedで方向が安定しているため、e5-smallでは現時点で最も根拠のある速度候補。ただしseed数が2、固定試験も調整に使われているため、最終性能の証明ではない。重大誤り・不明数を含めて記録し、盲検評価はモデルと判定規則を固定した後に一度だけ行う。

### 3. 学習率1e-4は品質候補だが未確定

版15のseed1では、標準の5e-5に対し1e-4がdev +10.9pt、一般 +4.8pt、業務 +0.4pt、業務2 −0.3pt、調達 +1.1ptだった。仕事6/7だけの結果で、他seedの反復がない。また、複数設定を同じ固定試験で見た後の数字なので、選択による楽観バイアスがある。速度も標準と同程度（240秒）。seed2・3を含む対応比較を追加し、重大誤りと不明数を確認するまで採用しない。

### 4. INT8圧縮は品質優先条件を満たさない

版15のe5-smallでは、動的INT8＋埋め込みINT8の正解率が圧縮なしより各試験で約1.1〜5.4ポイント低下し、top-1一致は93.85%前後だった。語彙を多く残してもこの問題は解消しなかった。容量の都合が出るまでは、圧縮なしまたは語彙削減/fp16の結果を別々に評価し、INT8を速度・品質改善として採用しない。

### 5. 品質改善は入力文脈の検証を優先

版14で水増し（augmentation）は効果なし、3周学習は品質差が見えず約1.39倍の時間だったため、データ水増しや周数増加を先に試さない。重大な誤りは曖昧な列名や同じ表の兄弟列・UNIT列の情報不足に偏っているという分析がある。進行中のUNIT文脈A/Bをseed対応で評価し、精度だけでなく重大誤り・不明数の増減も見る。E5は元来コントラスト学習の文埋め込みモデルだが、現行は分類ヘッド付きの教師あり列分類として微調整しているため、元論文の埋め込み学習レシピをそのまま移植する提案はしない。

## 次に測る順番

1. **進行中のUNIT A/Bを回収して比較**。同じseed同士で比較し、開発用・一般・業務・業務2・調達の全試験、重大/不明件数、時間を並べる。
2. **バッチだけを比較**。現在のBS32×ACC2に対し、BS64×ACC1を同じseed・同じ実効バッチ64で測る。T4でのピークメモリ、学習秒、スループット、固定試験を取る。ドロップアウトの乱数差があるので、可能なら2 seedずつ。
3. **静的文のトークン化コストを測定**。augmentationなしの学習文は固定入力なので、全55,213文を一度だけtokenizeする案を、現行の各step tokenizeと比較する。CPU時間・RAM・epoch時間を別計測し、利得が小さければ実装しない。augmentationありでは文が変わるため、同じキャッシュを使わない。
4. **1周 vs 2周を対応比較**。学習曲線と各epoch終わりの固定試験を保存し、1周で2周と同等なら早期停止を検討する。単に学習を途中打ち切るのではなく、scheduler設定も条件間で公平に揃える。
5. **学習率1e-4を複数seedで再検証**。他の設定を固定し、2〜3 seedで比較。改善が再現しない場合は5e-5を維持する。

一度に変更するのは一要因。各候補を「学習秒/文秒」「最大メモリ」「正解率」「重大誤り」「不明」「seed間の幅」で記録する。実験数が増えたら固定試験の結果に過剰適合しないよう候補を絞り、最後の未見セットは変更完了後だけに使う。

## 根拠・一次資料

- 既存実測: [bench/e5small_8jobs.md](https://github.com/hehohahifu83-cmyk/jitsuris-train/blob/main/bench/e5small_8jobs.md)、[FINETUNE_RESULTS.md](https://github.com/hehohahifu83-cmyk/jitsuris-train/blob/main/FINETUNE_RESULTS.md)、[HANDOFF.md](https://github.com/hehohahifu83-cmyk/jitsuris-train/blob/main/HANDOFF.md)
- PyTorch [Performance Tuning Guide](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html): data loadingやGPU処理の最適化は対象ハードで測定する。
- PyTorch [Automatic Mixed Precision](https://docs.pytorch.org/docs/stable/amp.html) / [AMP examples](https://docs.pytorch.org/docs/stable/notes/amp_examples.html): autocastとGradScaler、gradient accumulationの扱い。
- PyTorch [AdamW](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html): foreach/fused実装は通常の逐次実装より高速になりうる。プロジェクトでは既にfusedを使用。
- PyTorch [Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html): CPU待ち、データ処理、GPU演算を分離してボトルネックを測る。
- Wang et al., [Multilingual E5 Text Embeddings: A Technical Report](https://arxiv.org/abs/2402.05672): multilingual E5の学習背景。ここで扱う分類タスクの改善は、当該プロジェクトの固定試験で判断する。
