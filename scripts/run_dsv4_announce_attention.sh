#!/usr/bin/env bash
# Where is the announcement read? Attention dumps (with an 'announce' key region = the filler sentence in the
# system message) on chat and base for: unannounced k=0, announced-but-absent (50 announced, none delivered),
# and k=50 delivered. Then mass on the announcement from q_last / cue / gen per block.
set -eo pipefail
export PYTORCH_ALLOC_CONF=expandable_segments:True
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"; REF="--reference-code-dir $WORK/cache/model_hf/inference"
declare -A CKPT=( [chat]="$WORK/cache/model_mp4" [base]="$WORK/cache/base_mp4" )
declare -A MCFG=( [chat]="$WORK/cache/model_hf/inference/config.json" [base]="$WORK/cache/base_config.json" )
declare -A OUTROOT=( [chat]="results/deepseek-v4-flash" [base]="results/deepseek-v4-flash-base" )
CFG=configs/varbind_heldout_050_149_dot_length_sweep.json
DUMPS=""
for m in chat base; do for cond in "k0:0:0" "announce50-k0:0:50" "k50:50:0"; do
  IFS=: read -r name K ann <<<"$cond"; out="${OUTROOT[$m]}/announce-attn-$name"; echo "=== ATTN $m $name ==="
  if [ -f "$out/dot_attention.pt" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/dump_dot_attention_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF \
    --examples-config $CFG --filler-length $K --announce-filler $ann --max-items 50 --max-seq-len 1280 --output-dir "$out" 2>&1 | grep -v "readout layer" | tee "$LOGDIR/attn-$m-$name.log" | tail -1
  fi
  DUMPS="$DUMPS --dump $m-$name=$out/dot_attention.pt"
done; done
python scripts/summarize_announce_attention.py $DUMPS --output results/filler-cosine/announce-attention.md
echo ANNOUNCE_ATTN_DONE
