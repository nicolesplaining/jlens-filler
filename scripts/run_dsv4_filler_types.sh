#!/usr/bin/env bash
# Four alternative filler types (alphabet, scrambled alphabet, counting numbers, scrambled numbers) on
# DeepSeek V4 Flash chat and base: behavioral sweep (chat rendering, released 50 items), then the
# residual dump and the attention dump at k=50 on the 50 held-out items. Behavior for both models first.
set -eo pipefail
export PYTORCH_ALLOC_CONF=expandable_segments:True
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"
REF="--reference-code-dir $WORK/cache/model_hf/inference"
LENS="--lens-path $WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt"
declare -A CKPT=( [chat]="$WORK/cache/model_mp4" [base]="$WORK/cache/base_mp4" )
declare -A MCFG=( [chat]="$WORK/cache/model_hf/inference/config.json" [base]="$WORK/cache/base_config.json" )
declare -A REV=( [chat]="60d8d70770c6776ff598c94bb586a859a38244f1" [base]="base" )
declare -A OUTROOT=( [chat]="results/deepseek-v4-flash" [base]="results/deepseek-v4-flash-base" )
TYPES=${TYPES:-"alphabet alphabet-scrambled counting counting-scrambled"}
for m in chat base; do for ft in $TYPES; do
  out="${OUTROOT[$m]}/varbind-eval-$ft"; echo "=== EVAL $m $ft ==="
  if [ -f "$out/behavior-report.md" ]; then echo "(done already)"; grep "^|" "$out/behavior-report.md"; continue; fi
  torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py --ckpt-path "${CKPT[$m]}" --model-config "${MCFG[$m]}" $REF $LENS \
    --model-revision "${REV[$m]}" --max-seq-len 2048 --examples-config "configs/varbind_easy_${ft}_length_sweep.json" \
    --output-dir "$out" --phase eval --top-k 10 --max-new-tokens 3 --render chat 2>&1 | grep -v "^readout layer\|^length sweep" | tee "$LOGDIR/eval-$m-$ft.log" | tail -2
  python scripts/analyze_behavior_sweep.py "$out/filler_length_sweep.json" --output-dir "$out" >/dev/null
  grep "^|" "$out/behavior-report.md"
done; done
for m in chat base; do for ft in $TYPES; do
  out="${OUTROOT[$m]}/filler-dump-$ft"; echo "=== DUMP $m $ft ==="
  if [ -f "$out/cosine/filler-cosine.md" ]; then echo "(done already)"; continue; fi
  # held-out items with this filler type: same items as the dot dump
  python - "$ft" <<'PY'
import json,sys; ft=sys.argv[1]
c=json.load(open("configs/varbind_heldout_050_149_dot_length_sweep.json")); c["filler_type"]=ft
json.dump(c, open(f"configs/varbind_heldout_050_149_{ft}_length_sweep.json","w"), indent=1)
PY
  COMMON="--ckpt-path ${CKPT[$m]} --model-config ${MCFG[$m]} $REF --examples-config configs/varbind_heldout_050_149_${ft}_length_sweep.json --filler-length 50 --max-items 50 --max-seq-len 2048 --output-dir $out"
  torchrun --standalone --nproc-per-node=4 scripts/dump_dot_residuals_dsv4.py $COMMON 2>&1 | grep -v "readout layer" | tee "$LOGDIR/resid-$m-$ft.log" | tail -2
  torchrun --standalone --nproc-per-node=4 scripts/dump_dot_attention_dsv4.py $COMMON 2>&1 | grep -v "readout layer" | tee "$LOGDIR/attn-$m-$ft.log" | tail -2
  python scripts/analyze_dot_residuals.py --dump "$m-$ft=$out/dot_dump.pt" --output-dir "$out/analysis" | tail -3
  python scripts/analyze_filler_cosine.py --dump "$m-$ft=$out/dot_dump.pt" --output-dir "$out/cosine" | tail -3
  echo "DUMP_DONE $m $ft"
done; done
echo FILLER_TYPES_DONE
