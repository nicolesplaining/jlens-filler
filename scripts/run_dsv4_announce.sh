#!/usr/bin/env bash
# "Announced but absent": system sentence + demos carry 50 dots, the target has none. Behavior on the released
# 50 items and k=0 residual dumps (question-token probe) on chat and base. Compare with the plain k=0 rows
# (chat 35/50, base 48/50; q_last answer probe 0.84 both) and the k=50 rows (q_last probe chat 0.36, base 0.65).
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
  out="${OUTROOT[$m]}/varbind-eval-announce50-k0"; echo "=== ANNOUNCE EVAL $m ==="
  if [ -f "$out/behavior-report.md" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF $LENS \
    --model-revision "${REV[$m]}" --max-seq-len 1280 --examples-config configs/varbind_easy_announce_k0.json --announce-filler 50 \
    --output-dir "$out" --phase eval --top-k 10 --max-new-tokens 3 --render chat 2>&1 | grep -v "^readout layer\|^length sweep" | tee "$LOGDIR/announce-eval-$m.log" | tail -2
  python scripts/analyze_behavior_sweep.py "$out/filler_length_sweep.json" --output-dir "$out" >/dev/null
  fi
  grep "^|" "$out/behavior-report.md"
  out="${OUTROOT[$m]}/k0-announce50-dump"; echo "=== ANNOUNCE K0 DUMP $m ==="
  if [ -f "$out/dot_dump.pt" ]; then echo "(done already)"; else
  torchrun --standalone --nproc-per-node=4 scripts/dump_dot_residuals_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF \
    --examples-config configs/varbind_heldout_050_149_dot_length_sweep.json --filler-length 0 --announce-filler 50 --max-items 50 --max-seq-len 1280 --output-dir "$out" 2>&1 | grep -v "readout layer" | tee "$LOGDIR/announce-dump-$m.log" | tail -2
  fi
done
python scripts/probe_k0_dump.py --dump chat-k0-announce50=results/deepseek-v4-flash/k0-announce50-dump/dot_dump.pt --dump base-k0-announce50=results/deepseek-v4-flash-base/k0-announce50-dump/dot_dump.pt --output results/filler-cosine/k0-announce-probes.md
echo ANNOUNCE_DONE
