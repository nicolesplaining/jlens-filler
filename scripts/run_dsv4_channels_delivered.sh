#!/usr/bin/env bash
# Complete the 2x2 on the chat model: sentence-only and demos-only announcements WITH fifty dots delivered in the
# target. Which channel does the workspace use itself depend on?
set -eo pipefail
export PYTORCH_ALLOC_CONF=expandable_segments:True
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"; REF="--reference-code-dir $WORK/cache/model_hf/inference"; LENS="--lens-path $WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt"
python - <<'PY'
import json; c=json.load(open("configs/varbind_easy_dot_length_sweep.json")); c["filler_lengths"]=[0,50]; json.dump(c, open("configs/varbind_easy_k0_k50.json","w"), indent=1)
PY
for mode in sentence demos none; do
  out="results/deepseek-v4-flash/varbind-eval-announce50-$mode-k50"; echo "=== DELIVERED chat $mode ==="
  if [ -f "$out/behavior-report.md" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py --ckpt-path cache/model_mp4 --model-config cache/model_hf/inference/config.json $REF $LENS \
    --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1 --max-seq-len 1280 --examples-config configs/varbind_easy_k0_k50.json --announce-filler 50 --announce-mode $mode \
    --output-dir "$out" --phase eval --top-k 10 --max-new-tokens 3 --render chat 2>&1 | grep -v "^readout layer\|^length sweep" | tee "$LOGDIR/delivered-$mode.log" | tail -1
  python scripts/analyze_behavior_sweep.py "$out/filler_length_sweep.json" --output-dir "$out" >/dev/null
  fi
  grep "^| \(0\|50\) " "$out/behavior-report.md"
done
echo DELIVERED_DONE
