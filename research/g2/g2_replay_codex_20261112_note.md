# G2 再現確認（2026-11-12 Codex）

`python research/g2/g2_eval.py --labels /workspace/ai-bridge/labels/g2/final.jsonl --dry` 終了0。
scikit-learn 1.8.0・NumPy 2.3.5・SciPy 1.17.0。コード取得時のjitsuris-train HEADは1a39bd354b674c410a6d59fbe883589af4f9a74b、ai-bridge HEADはcc5b89a54f6cce3dfbc0ad98d7e26fea731b26a8。実行中に入ったG3の追加はG2関連ファイルを変えていない。
出力 `g2_replay_codex_20261112.md` と既存 `g2_eval.md` は末尾の空行だけの差で、strip後完全一致。228列、L24+G 81.58%、重大2（3本合計）。Mによる変更0列、判定は確かめられなかった。L+Gも81.58%、重大3。
ラベル・予測・本体・採点コードは変更していない。関連 `test_fix_j.py` 3件成功。
