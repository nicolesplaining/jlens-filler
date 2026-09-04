#!/usr/bin/env bash
# What do the demonstrations do to the question token? Attention from q_last/cue/gen onto the demonstrations'
# filler spans and answer cues (new key regions), chat and base, demos-only announcement with target k=0,
# plus the unannounced k=0 baseline for the demo_answer region.
set -eo pipefail
export PYTORCH_ALLOC_CONF=expandable_segments:True
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"; REF="--reference-code-dir $WORK/cache/model_hf/inference"
declare -A CKPT=( [chat]="$WORK/cache/model_mp4" [base]="$WORK/cache/base_mp4" )
declare -A MCFG=( [chat]="$WORK/cache/model_hf/inference/config.json" [base]="$WORK/cache/base_config.json" )
declare -A OUTROOT=( [chat]="results/deepseek-v4-flash" [base]="results/deepseek-v4-flash-base" )
CFG=configs/varbind_heldout_050_149_dot_length_sweep.json; DUMPS=""
for m in chat base; do for cond in "demos-k0:demos:50" "none-k0:none:0"; do
  IFS=: read -r name mode ann <<<"$cond"; out="${OUTROOT[$m]}/demo-attn-$name"; echo "=== DEMO ATTN $m $name ==="
  if [ -f "$out/dot_attention.pt" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/dump_dot_attention_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF \
    --examples-config $CFG --filler-length 0 --announce-filler $ann --announce-mode $mode --max-items 50 --max-seq-len 1280 --output-dir "$out" 2>&1 | grep -v "readout layer" | tee "$LOGDIR/demoattn-$m-$name.log" | tail -1
  fi
  DUMPS="$DUMPS --dump $m-$name=$out/dot_attention.pt"
done; done
python scripts/summarize_announce_attention.py $DUMPS --output results/filler-cosine/demo-attention.md
echo DEMO_ATTN_DONE
