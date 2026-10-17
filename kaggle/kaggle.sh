#!/usr/bin/env bash
# GitHub Actions から Kaggle を動かす。kaggle.request の1語目：train（データを上げて学習を頼む）／fetch（結果を取りに行く）
set -euo pipefail
cd "$(dirname "$0")"
U="$KAGGLE_USERNAME"; DS="$U/jitsuris-data"; K="$U/jitsuris-train"
mode=$(awk '{print $1}' kaggle.request)
# GitHub の実行時間を使い切らないよう、train は依頼して数分で終わる。結果は fetch で取りに行く（待つのは最長2分）
WAIT_MIN=${WAIT_MIN:-2}
if [ "$mode" = train ]; then
  cut -d' ' -f2- kaggle.request > args.txt
  rm -rf /tmp/ds /tmp/kn && mkdir -p /tmp/ds /tmp/kn
  # Kaggle 側からインターネットに出られなくても動くように、モデルは GitHub 側で取って一緒に送る
  M=$(awk '{print $1}' args.txt); D="hfmodel/${M//\//__}"
  pip install -q huggingface_hub
  ( cd .. && rm -rf hfmodel && python -c "from huggingface_hub import snapshot_download as s; s('$M', local_dir='$D', allow_patterns=['*.json','*.safetensors','*.model','*.txt','sentencepiece*','tokenizer*'])" && du -sh hfmodel && ls -R hfmodel | head -20 ) | tee -a /tmp/hf.txt
  sed -i "1s#^[^ ]*#$D#" args.txt
  ( cd .. && tar -cf /tmp/ds/bundle.tar --exclude='blind_set*' --exclude='__pycache__' \
      *.py kaggle/args.txt materials/__init__.py materials/teacher_labels.py materials/jp_municipal_fields.json \
      materials/real_labels.jsonl materials/real_labels_biz.jsonl materials/real_labels_biz2.jsonl materials/real_labels_direct.jsonl materials/real_labels_jp.jsonl materials/real_labels_jp2.jsonl hfmodel )
  tar -tf /tmp/ds/bundle.tar | grep -q blind_set && { echo "未見セットが混ざった"; exit 1; }
  printf '{"title":"jitsuris-data","id":"%s","licenses":[{"name":"other"}]}' "$DS" > /tmp/ds/dataset-metadata.json
  if kaggle datasets status "$DS" >/dev/null 2>&1; then kaggle datasets version -p /tmp/ds -m "update $(date -u +%FT%TZ)"
  else kaggle datasets create -p /tmp/ds; fi
  # 新しい版の中身（今回のモデルと args）が Kaggle 側で使えるようになるまで待つ。古い版のまま学習しないため
  for i in $(seq 1 90); do
    s=$(kaggle datasets status "$DS" 2>&1 || true)
    f=$(kaggle datasets files "$DS" --page-size 200 2>&1 || true)
    echo "$f" | grep -q "${D#hfmodel/}" && [ "$s" = ready ] && { echo "dataset ready with $D"; break; }
    [ $((i % 6)) = 1 ] && echo "dataset: $s（新しい版を待っている）"; sleep 20
  done
  sed "s#^EXPECT = .*#EXPECT = \"$D\"#" run.py > /tmp/kn/run.py
  printf '{"id":"%s","title":"jitsuris-train","code_file":"run.py","language":"python","kernel_type":"script","is_private":true,"enable_gpu":true,"enable_internet":true,"machine_shape":"%s","dataset_sources":["%s"]}' "$K" "${MACHINE:-NvidiaTeslaP100}" "$DS" > /tmp/kn/kernel-metadata.json
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
    if [ -n "$f" ]; then tail -n +2 "$f" | sed 's/^### /### Kaggle GPU /' >> ../FINETUNE_RESULTS.md; fi
    { find /tmp/out -name '*.log' -exec grep -aoE 'device [a-z]+|Tesla [A-Z0-9]+|name, memory[^"]*|[A-Za-z ]*GPU[^"]{0,60}' {} \; | head -5; echo ---; find /tmp/out -name '*.log' -exec tail -c 3000 {} \; ; } > last_run_tail.txt 2>/dev/null || true
    mkdir -p /tmp/model && [ -d /tmp/out/out/ft_out ] && cp -r /tmp/out/out/ft_out /tmp/model/ || true
    echo done > kaggle.request
else
  echo fetch > kaggle.request   # まだ終わっていない。fetch を書いて push すると取りに行く
fi
