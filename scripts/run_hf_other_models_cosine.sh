#!/usr/bin/env bash
# Dot dumps at k=50 on the 50 held-out items for two more families (Llama-3.1-8B-Instruct, Gemma-3-27B-IT),
# then anatomy + adjacent-cosine, to extend the redundancy table beyond Qwen and DeepSeek. HF venv, one GPU each.
set -eo pipefail
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$HOME/hfvenv/bin/activate"
LOGDIR=$HOME/filler-logs; mkdir -p "$LOGDIR"
run() { # gpu model_id outdir label
  CUDA_VISIBLE_DEVICES=$1 python scripts/dump_dot_residuals_hf.py --model-id "$2" --examples-config configs/varbind_heldout_050_149_dot_length_sweep.json \
    --filler-length 50 --max-items 50 --output-dir "$3" 2>&1 | tee "$LOGDIR/dump-$4.log" | tail -2
  python scripts/analyze_dot_residuals.py --dump "$4=$3/dot_dump.pt" --output-dir "$3/analysis" | tail -2
  python scripts/analyze_filler_cosine.py --dump "$4=$3/dot_dump.pt" --output-dir "$3/cosine" | tail -2
  echo "OTHER_DONE $4"
}
echo "=== llama ==="; run 0 unsloth/Llama-3.1-8B-Instruct results/llama3.1-8b-it/dot-dump llama-8b-it &
echo "=== gemma ==="; run 1 google/gemma-3-27b-it results/gemma-3-27b-it/dot-dump gemma-27b-it &
wait
echo OTHER_MODELS_DONE
