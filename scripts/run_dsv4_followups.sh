#!/usr/bin/env bash
# (1) Pre-question placement control for the four alternative fillers on the chat model (does placement
#     specificity hold for letters/numbers?). (2) k=0 residual dumps on chat and base (question-token probe
#     with no filler present), then ridge probes at q_last / cue / gen.
set -eo pipefail
export PYTORCH_ALLOC_CONF=expandable_segments:True
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"
REF="--reference-code-dir $WORK/cache/model_hf/inference"; LENS="--lens-path $WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt"
declare -A CKPT=( [chat]="$WORK/cache/model_mp4" [base]="$WORK/cache/base_mp4" )
declare -A MCFG=( [chat]="$WORK/cache/model_hf/inference/config.json" [base]="$WORK/cache/base_config.json" )
declare -A REV=( [chat]="60d8d70770c6776ff598c94bb586a859a38244f1" [base]="base" )
declare -A OUTROOT=( [chat]="results/deepseek-v4-flash" [base]="results/deepseek-v4-flash-base" )
for m in chat base; do
  out="${OUTROOT[$m]}/k0-dump"; echo "=== K0 DUMP $m ==="
  if [ -f "$out/dot_dump.pt" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/dump_dot_residuals_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF \
    --examples-config configs/varbind_heldout_050_149_dot_length_sweep.json --filler-length 0 --max-items 50 --max-seq-len 1280 --output-dir "$out" 2>&1 | grep -v "readout layer" | tee "$LOGDIR/k0-dump-$m.log" | tail -2
  fi
done
python scripts/probe_k0_dump.py --dump chat-k0=results/deepseek-v4-flash/k0-dump/dot_dump.pt --dump base-k0=results/deepseek-v4-flash-base/k0-dump/dot_dump.pt \
  --dump chat-k50=results/deepseek-v4-flash/dot-dump/dot_dump.pt --dump base-k50=results/deepseek-v4-flash-base/dot-dump/dot_dump.pt --output results/filler-cosine/k0-probes.md
echo K0_PROBES_DONE
for ft in alphabet alphabet-scrambled counting counting-scrambled; do
  out="results/deepseek-v4-flash/varbind-pre-question-k50-control-$ft"; echo "=== PREQ chat $ft ==="
  if [ -f "$out/behavior-report.md" ]; then echo "(done already)"; grep "^|" "$out/behavior-report.md"; continue; fi
  torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py --ckpt-path "${CKPT[chat]}" --model-config "${MCFG[chat]}" $REF $LENS \
    --model-revision "${REV[chat]}" --max-seq-len 2048 --examples-config "configs/varbind_pre_question_k50_control_${ft}.json" \
    --output-dir "$out" --phase eval --top-k 10 --max-new-tokens 3 --render chat 2>&1 | grep -v "^readout layer\|^length sweep" | tee "$LOGDIR/preq-chat-$ft.log" | tail -2
  python scripts/analyze_behavior_sweep.py "$out/filler_length_sweep.json" --output-dir "$out" >/dev/null
  grep "^|" "$out/behavior-report.md"
done
echo FOLLOWUPS_DONE
