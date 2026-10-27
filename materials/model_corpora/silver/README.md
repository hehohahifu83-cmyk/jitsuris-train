# 銀ラベル（外の学習データの読み替え）の作業場所（2026-10-28 Claude）

外の学習データ（`../data/sotab_v2`・`../data/wikidbs10k`、計 743,196 列）を、まとまり単位でジツリスの 16 種に読み替える。道具は `../silver.py`。

- `sheets/sheet_001.md`〜`sheet_008.md`：1,198 まとまり（SOTAB は元の種類 76、WikiDBs は「型＋見出し」で 5 列以上のもの 1,122）。741,665 列を覆う
- **ChatGPT** は `answers/sheet_NNN.tsv`、**Grok** は `answers_grok/sheet_NNN.tsv` に答える。**相手の答えの置き場・C2 の予測（`../../pool/work/silver1/`）は見ない**
- 答えの形は今のシートと同じ（`g0001<TAB>ラベル`）。LABEL_GUIDE.md v2.0 だけで決める。まとまりの中で種類が混ざる・決められない → `unknown`、人の名前・連絡先・崩れた値 → `S`
- 確かめ：`python materials/model_corpora/silver.py status`（Grok は `--teacher grok`）
- **2026-10-28 オーナー判断：Grok 抜きで進める**（時間がかかるため）。`answers_grok/`・`recheck_grok.md` は記録として残すが、銀ラベルには使わない
- このあと（Claude）：ChatGPT の答え（`answers/`）を正とし、値の形ごとの代表の C2 の予測（`pool/work/silver1/pred_c2_seed1.json`）と一致した列だけを銀ラベルにする（unknown・S のまとまりは使わない）。割れが多いまとまりは Claude が抜き取りで確かめる
- **確かめ（2026-10-28 Claude、C3 計画の段 1 の 3）**：列の多い 60 まとまり（360,922 列＝全体の約 49%。ChatGPT の答えが unknown・S のものは除く）から 5 列ずつ、計 300 列を抜き取り、まとまりの名前と答えを伏せて `check/check_001.md`・`check_002.md` に並べた（`silver.py check`、種 20261028）。ChatGPT が 1 列ずつ `answers_check/check_NNN.tsv` に答える。まとまりの答えと合わない列が 5 列中 1 列でもあれば（＞5%）、Claude が見て、そのまとまりを銀にしないか分ける。対応表は `check_index.json`（**ChatGPT は答え終わるまで見ない**）
- 銀ラベルは教材庫（`materials/pool/batch_*.jsonl`）に入れない。学習に使うかどうかは事前記録とオーナーの許可のあと（`research/c3-plan-2026-10-28.md` の段 2）
