#!/usr/bin/env bash
# Which channel carries the announcement? (a) sentence only: system sentence announces 50 dots, demos have none;
# (b) demos only: no sentence, demos carry 50 dots. Target has no filler in both. Behavior on the released 50
# items and k=0 residual dumps + ridge probes at q_last on chat and base.
set -eo pipefail
export PYTORCH_ALLOC_CONF=expandable_segments:True
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"; REF="--reference-code-dir $WORK/cache/model_hf/inference"; LENS="--lens-path $WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt"
declare -A CKPT=( [chat]="$WORK/cache/model_mp4" [base]="$WORK/cache/base_mp4" )
declare -A MCFG=( [chat]="$WORK/cache/model_hf/inference/config.json" [base]="$WORK/cache/base_config.json" )
declare -A REV=( [chat]="60d8d70770c6776ff598c94bb586a859a38244f1" [base]="base" )
declare -A OUTROOT=( [chat]="results/deepseek-v4-flash" [base]="results/deepseek-v4-flash-base" )
DUMPS=""
for m in chat base; do for mode in sentence demos; do
  out="${OUTROOT[$m]}/varbind-eval-announce50-$mode-k0"; echo "=== CHANNEL EVAL $m $mode ==="
  if [ -f "$out/behavior-report.md" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF $LENS \
    --model-revision "${REV[$m]}" --max-seq-len 1280 --examples-config configs/varbind_easy_announce_k0.json --announce-filler 50 --announce-mode $mode \
    --output-dir "$out" --phase eval --top-k 10 --max-new-tokens 3 --render chat 2>&1 | grep -v "^readout layer\|^length sweep" | tee "$LOGDIR/channel-eval-$m-$mode.log" | tail -1
  python scripts/analyze_behavior_sweep.py "$out/filler_length_sweep.json" --output-dir "$out" >/dev/null
  fi
  grep "^| 0 " "$out/behavior-report.md"
  out="${OUTROOT[$m]}/k0-announce50-$mode-dump"; echo "=== CHANNEL K0 DUMP $m $mode ==="
  if [ -f "$out/dot_dump.pt" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/dump_dot_residuals_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF \
    --examples-config configs/varbind_heldout_050_149_dot_length_sweep.json --filler-length 0 --announce-filler 50 --announce-mode $mode --max-items 50 --max-seq-len 1280 --output-dir "$out" 2>&1 | grep -v "readout layer" | tee "$LOGDIR/channel-dump-$m-$mode.log" | tail -1
  fi
  DUMPS="$DUMPS --dump $m-k0-announce50-$mode=$out/dot_dump.pt"
done; done
python scripts/probe_k0_dump.py $DUMPS --targets answer --output results/filler-cosine/k0-announce-channel-probes.md
echo CHANNELS_DONE
