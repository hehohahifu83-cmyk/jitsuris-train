#!/usr/bin/env bash
# GitHub Actions から Kaggle を動かす。kaggle.request の1語目：train（データを上げて学習を頼む）／fetch（結果を取りに行く）
set -euo pipefail
cd "$(dirname "$0")"
U="$KAGGLE_USERNAME"; DS="$U/jitsuris-data"; K="$U/jitsuris-train"
mode=$(awk '{print $1}' kaggle.request)
if [ "$mode" = diag ]; then   # 調査：小さい CPU と GPU の実行を別の名前で出して、動き出すまでの時間を比べる（データセットなし）
  for kind in cpu gpu; do
    d=/tmp/diag-$kind; rm -rf $d; mkdir -p $d
    printf 'import subprocess, torch\nprint("cuda", torch.cuda.is_available())\nsubprocess.run("nvidia-smi -L", shell=True)\n' > $d/run.py
    g=false; [ $kind = gpu ] && g=true
    printf '{"id":"%s/jitsuris-diag-%s","title":"jitsuris-diag-%s","code_file":"run.py","language":"python","kernel_type":"script","is_private":true,"enable_gpu":%s,"enable_internet":false,"dataset_sources":[]}' "$U" $kind $kind $g > $d/kernel-metadata.json
    echo "$(date -u +%FT%TZ) 調査 $kind の push：$(kaggle kernels push -p $d 2>&1 | tr '\n' ' ' | cut -c1-200)" >> KAGGLE_LOG.md
  done
  for i in $(seq 1 20); do
    sleep 60; line="$i 分"
    for kind in cpu gpu; do line="$line ／ $kind: $(kaggle kernels status "$U/jitsuris-diag-$kind" 2>&1 | grep -oE 'KernelWorkerStatus\.[A-Z_]+' )"; done
    line="$line ／ 本番: $(kaggle kernels status "$K" 2>&1 | grep -oE 'KernelWorkerStatus\.[A-Z_]+')"
    echo "$(date -u +%FT%TZ) $line" >> KAGGLE_LOG.md
    echo "$line" | grep -q 'cpu: KernelWorkerStatus.COMPLETE' && echo "$line" | grep -qE 'gpu: KernelWorkerStatus.(COMPLETE|ERROR)' && break
  done
  echo done > kaggle.request; exit 0
fi
# GitHub の実行時間を使い切らないよう、train は依頼して数分で終わる。結果は fetch で取りに行く（待つのは最長2分）
WAIT_MIN=${WAIT_MIN:-2}
if [ "$mode" = train ]; then
  cut -d' ' -f2- kaggle.request > args.txt
  rm -rf /tmp/ds /tmp/kn && mkdir -p /tmp/ds /tmp/kn
  # Kaggle 側からインターネットに出られなくても動くように、モデルは GitHub 側で取って一緒に送る
  case "$(awk '{print $1}' args.txt)" in embed|probe) MI=2;; *) MI=1;; esac   # embed と probe は 1 語目が種類、2 語目がモデル
  M=$(awk -v n=$MI '{print $n}' args.txt); D="hfmodel/${M//\//__}"
  pip install -q huggingface_hub
  ( cd .. && rm -rf hfmodel && python kaggle/hf_fetch.py "$M" "$D" && du -sh hfmodel && ls -R hfmodel | head -20 ) | tee -a /tmp/hf.txt   # 重みが safetensors でない repo（mmBERT-small）は bin も取る・取った版を hf_revision.json に残す
  if [ "$MI" = 2 ]; then sed -i -E "1s#^(embed|probe) [^ ]*#\1 $D#" args.txt; else sed -i "1s#^[^ ]*#$D#" args.txt; fi
  # 今回だけの印。ファイル名に入れておき、Kaggle 側の一覧にこの名前が出るまで待つ（同じモデルの前回の版を、今回の版と取り違えないため）
  NONCE="$(date -u +%Y%m%dT%H%M%S)-$RANDOM"
  ( cd .. && rm -f kaggle/nonce-*.txt && : > "kaggle/nonce-$NONCE.txt" )
  printf '%s\n' "${GITHUB_SHA:-unknown}" > commit.txt   # 学習の記録（manifest.json）に、どの commit のコードで流したかを残す
  ( cd .. && tar -cf /tmp/ds/bundle.tar --exclude='blind_set*' --exclude='__pycache__' \
      *.py kaggle/args.txt kaggle/commit.txt "kaggle/nonce-$NONCE.txt" materials/__init__.py materials/teacher_labels.py materials/jp_municipal_fields.json \
      materials/real_labels.jsonl materials/real_labels_biz.jsonl materials/real_labels_biz2.jsonl materials/real_labels_direct.jsonl materials/real_labels_jp.jsonl materials/real_labels_jp2.jsonl materials/real_labels_jp3.jsonl \
      cpu_lab/self_learning.py cpu_lab/materials/reviewed_replay.jsonl cpu_lab/materials/progress_probe.jsonl hfmodel )
  tar -tf /tmp/ds/bundle.tar | grep -q blind_set && { echo "未見セットが混ざった"; exit 1; }
  printf '{"title":"jitsuris-data","id":"%s","licenses":[{"name":"other"}]}' "$DS" > /tmp/ds/dataset-metadata.json
  if kaggle datasets status "$DS" >/dev/null 2>&1; then kaggle datasets version -p /tmp/ds -m "update $(date -u +%FT%TZ)"
  else kaggle datasets create -p /tmp/ds; fi
  # 新しい版の中身（今回のモデルと args）が Kaggle 側で使えるようになるまで待つ。古い版のまま学習しないため
  ds_ready=0
  for i in $(seq 1 90); do
    s=$(kaggle datasets status "$DS" 2>&1 || true)
    f=$(kaggle datasets files "$DS" --page-size 200 2>&1 || true)
    echo "$f" | grep -q "nonce-$NONCE" && echo "$f" | grep -q "${D#hfmodel/}" && [ "$s" = ready ] && { echo "dataset ready with $D (nonce $NONCE)"; ds_ready=1; break; }
    [ $((i % 6)) = 1 ] && echo "dataset: $s（新しい版を待っている）"; sleep 20
  done
  if [ "$ds_ready" != 1 ]; then   # 古い版のまま学習を始めない（同じモデルの前回の結果を、今回の結果と取り違える）
    echo "$(date -u +%FT%TZ) 新しい版のデータセットが 30 分待っても使えるようにならなかったので、学習を頼まずに止める（印 $NONCE）" >> KAGGLE_LOG.md
    echo done > kaggle.request; exit 1
  fi
  sed -e "s#^EXPECT = .*#EXPECT = \"$D\"#" -e "s#^EXPECT_NONCE = .*#EXPECT_NONCE = \"$NONCE\"#" run.py > /tmp/kn/run.py
  printf '{"id":"%s","title":"jitsuris-train","code_file":"run.py","language":"python","kernel_type":"script","is_private":true,"enable_gpu":true,"enable_internet":true,"machine_shape":"%s","dataset_sources":["%s"]}' "$K" "${MACHINE:-NvidiaTeslaT4}" "$DS" > /tmp/kn/kernel-metadata.json
  out=$(kaggle kernels push -p /tmp/kn 2>&1 || true); echo "$out"
  echo "$(date -u +%FT%TZ) push の返事：$(echo "$out" | tr '\n' ' ' | cut -c1-300)" >> KAGGLE_LOG.md
  echo "$out" | grep -qiE 'error|fail|invalid|denied|exceed' && { echo "Kaggle が依頼を受け付けなかった"; exit 1; }
  sleep 30; echo "$(date -u +%FT%TZ) 依頼直後の状態：$(kaggle kernels status "$K" 2>&1 | tr '\n' ' ')" >> KAGGLE_LOG.md
  { echo "$(date -u +%FT%TZ) train を依頼：$(cat args.txt)"; echo "送ったモデル：$(head -1 /tmp/hf.txt 2>/dev/null)・束の中のモデルのファイル数 $(tar -tf /tmp/ds/bundle.tar | grep -c '^hfmodel/')"; } >> KAGGLE_LOG.md
  [ -n "${PROGRESS_PUSH:-}" ] && ( cd .. && git add kaggle/KAGGLE_LOG.md && git commit -qm "Kaggle に依頼した直後の状態" && git pull -q --rebase && git push -q ) || true
fi
# 終わるまで待って（最長 ${WAIT_MIN:-290} 分）、結果を取りに行く
st=""; q=0
for i in $(seq 1 "${WAIT_MIN:-290}"); do
  sleep 60; st=$(kaggle kernels status "$K" 2>&1 || true)
  echo "$st" | grep -qiE 'queued|starting' && q=$((q+1)) || q=0
  if [ $((i % 10)) = 0 ] && [ -n "${PROGRESS_PUSH:-}" ]; then   # 10分ごとに途中の状態をリポジトリに書く（Claude が読めるように）
    echo "$(date -u +%FT%TZ) 途中（$i 分）：$st" > PROGRESS.md
    ( cd .. && git add kaggle/PROGRESS.md && git commit -qm "途中の状態（$i 分）" && git pull -q --rebase && git push -q ) || true
  fi
  if [ "$q" -ge "${QUEUE_MAX:-20}" ]; then echo "$(date -u +%FT%TZ) 空き待ちが ${QUEUE_MAX:-20} 分を超えたので止める：$st" >> KAGGLE_LOG.md; st="queue-timeout"; break; fi
  echo "$st" | grep -qiE 'complete|error|cancel' && break
done
echo "$(date -u +%FT%TZ) 状態：$st" >> KAGGLE_LOG.md
if echo "$st" | grep -qiE 'complete|error|cancel'; then
    rm -rf /tmp/out && mkdir -p /tmp/out && kaggle kernels output "$K" -p /tmp/out || true
    f=$(find /tmp/out -name FINETUNE_RESULTS.md | head -1)
    d=$(find /tmp/out -name diag.txt | head -1); [ -n "$d" ] && sed 's/^/    /' "$d" >> KAGGLE_LOG.md
    # 学習ログから要点（束の大きさ・GPU メモリの最大・学習行数）だけを残す（仕事ごと）
    find /tmp/out -name '*.log' -exec grep -aoE '(\[仕事[0-9]+\] )?(peak GPU memory[^"\\]*|train batch=[^"\\]*|training rows=[^"\\]*)' {} \; 2>/dev/null | sed 's/^/    /' >> KAGGLE_LOG.md || true
    if [ -n "$f" ]; then tail -n +2 "$f" | sed 's/^### /### Kaggle GPU /' >> ../FINETUNE_RESULTS.md; fi
    { find /tmp/out -name '*.log' -exec grep -aoE 'device [a-z]+|Tesla [A-Z0-9]+|name, memory[^"]*|[A-Za-z ]*GPU[^"]{0,60}' {} \; | head -5; echo ---; find /tmp/out -name '*.log' -exec tail -c 3000 {} \; ; } > last_run_tail.txt 2>/dev/null || true
    mkdir -p /tmp/model && [ -d /tmp/out/out/ft_out ] && mv /tmp/out/out/ft_out /tmp/model/ || true   # 移す（複製しない）＝実行機のディスクを2倍使わない
    for d in /tmp/out/out/ft_out_job*; do [ -d "$d" ] && mv "$d" /tmp/model/ || true; done   # FT_KEEP=1 の仕事のモデル（重みの SHA-256 は各 ft_out*/manifest.json に入っている）
    mkdir -p /tmp/eval_reports
    # 仕事（job1・job2）や report ごとの置き場の名前を頭に付けて、同じ名前のファイルが上書きし合わないようにする
    find /tmp/out -type f -not -path '*/ft_out*' \( -name 'errors_*.json' -o -name 'probs_*.json' -o -name 'probe_*.json' -o -name 'manifest.json' \) | while read -r pf; do cp "$pf" "/tmp/eval_reports/$(basename "$(dirname "$pf")")_$(basename "$pf")"; done 2>/dev/null || true
    find /tmp/out -type f -path '*/progress_probe_results/*.json' | while read -r pf; do job=$(basename "$(dirname "$(dirname "$pf")")"); cp "$pf" "/tmp/eval_reports/${job}_progress_probe_$(basename "$pf")"; done 2>/dev/null || true
    echo done > kaggle.request
else
  echo fetch > kaggle.request   # まだ終わっていない。30分ごとの定期実行が取りに行く
fi

