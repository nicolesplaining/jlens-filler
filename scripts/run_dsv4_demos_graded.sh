#!/usr/bin/env bash
# Graded deferral by the demonstrations alone: demos carry 5 / 25 dots (no sentence), target k=0; q_last probes.
set -eo pipefail
export PYTORCH_ALLOC_CONF=expandable_segments:True
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"; REF="--reference-code-dir $WORK/cache/model_hf/inference"
declare -A CKPT=( [chat]="$WORK/cache/model_mp4" [base]="$WORK/cache/base_mp4" )
declare -A MCFG=( [chat]="$WORK/cache/model_hf/inference/config.json" [base]="$WORK/cache/base_config.json" )
declare -A OUTROOT=( [chat]="results/deepseek-v4-flash" [base]="results/deepseek-v4-flash-base" )
DUMPS=""
for m in chat base; do for n in 5 25; do
  out="${OUTROOT[$m]}/k0-demos${n}-dump"; echo "=== DEMOS $n K0 DUMP $m ==="
  if [ -f "$out/dot_dump.pt" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/dump_dot_residuals_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF \
    --examples-config configs/varbind_heldout_050_149_dot_length_sweep.json --filler-length 0 --announce-filler $n --announce-mode demos --max-items 50 --max-seq-len 1280 --output-dir "$out" 2>&1 | grep -v "readout layer" | tee "$LOGDIR/demos$n-dump-$m.log" | tail -1
  fi
  DUMPS="$DUMPS --dump $m-k0-demos$n=$out/dot_dump.pt"
done; done
python scripts/probe_k0_dump.py $DUMPS --targets answer --output results/filler-cosine/k0-demos-graded-probes.md
echo DEMOS_GRADED_DONE
