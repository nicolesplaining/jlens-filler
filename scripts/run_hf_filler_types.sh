#!/usr/bin/env bash
# Qwen3.5-9B (untrained, and the dots-only LoRA) with four alternative filler types: behavioral sweep on the
# released 50 items, residual+attention dump at k=50 on the 50 held-out items, anatomy and adjacent-cosine analysis.
# Runs on one GPU in the HF venv; launch only when the DeepSeek chain has released the GPUs.
set -eo pipefail
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$HOME/hfvenv/bin/activate"
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"
MODEL=Qwen/Qwen3.5-9B; ADAPTER=results/qwen3.5-9b/lora-dotsonly/adapter-step500
TYPES=${TYPES:-"alphabet alphabet-scrambled counting counting-scrambled"}
for variant in base dotsonly; do
  ADP=""; [ "$variant" = dotsonly ] && ADP="--adapter $ADAPTER"
  for ft in $TYPES; do
    out="results/qwen3.5-9b/filler-types/$variant/varbind-eval-$ft"; echo "=== HF EVAL $variant $ft ==="
    python scripts/extract_hf.py --model-id $MODEL $ADP --examples-config "configs/varbind_easy_${ft}_length_sweep.json" \
      --output-dir "$out" --phase eval --top-k 10 --max-new-tokens 3 2>&1 | grep -v "^readout layer\|^length sweep" | tee "$LOGDIR/hf-eval-$variant-$ft.log" | tail -2
    python scripts/analyze_behavior_sweep.py "$out/filler_length_sweep.json" --output-dir "$out" >/dev/null
    grep "^|" "$out/behavior-report.md"
  done
done
for variant in base dotsonly; do
  ADP=""; [ "$variant" = dotsonly ] && ADP="--adapter $ADAPTER"
  for ft in $TYPES; do
    out="results/qwen3.5-9b/filler-types/$variant/filler-dump-$ft"; echo "=== HF DUMP $variant $ft ==="
    [ -f "configs/varbind_heldout_050_149_${ft}_length_sweep.json" ] || python - "$ft" <<'PY'
import json,sys; ft=sys.argv[1]
c=json.load(open("configs/varbind_heldout_050_149_dot_length_sweep.json")); c["filler_type"]=ft
json.dump(c, open(f"configs/varbind_heldout_050_149_{ft}_length_sweep.json","w"), indent=1)
PY
    python scripts/dump_dot_residuals_hf.py --model-id $MODEL $ADP --examples-config "configs/varbind_heldout_050_149_${ft}_length_sweep.json" \
      --filler-length 50 --max-items 50 --output-dir "$out" 2>&1 | tee "$LOGDIR/hf-dump-$variant-$ft.log" | tail -2
    python scripts/analyze_dot_residuals.py --dump "qwen-$variant-$ft=$out/dot_dump.pt" --output-dir "$out/analysis" | tail -3
    python scripts/analyze_filler_cosine.py --dump "qwen-$variant-$ft=$out/dot_dump.pt" --output-dir "$out/cosine" | tail -3
    echo "HF_DUMP_DONE $variant $ft"
  done
done
echo HF_FILLER_TYPES_DONE
