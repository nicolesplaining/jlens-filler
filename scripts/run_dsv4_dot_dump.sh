#!/usr/bin/env bash
# Sanity gate, then the dot-residual dump on the 100 held-out items at k=50, then analysis.
set -eo pipefail
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
ITEMS=${ITEMS:-50}
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/initial_examples.json --output-dir results/deepseek-v4-flash/sanity --phase sanity \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1 2>&1 | grep -v "^readout layer" | tail -3
cat results/deepseek-v4-flash/sanity/sanity_gate.json
torchrun --standalone --nproc-per-node=4 scripts/dump_dot_residuals_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --examples-config configs/varbind_heldout_050_149_dot_length_sweep.json --filler-length 50 --max-items "$ITEMS" \
  --output-dir results/deepseek-v4-flash/dot-dump 2>&1 | grep -v "readout layer" | tail -4
torchrun --standalone --nproc-per-node=4 scripts/dump_dot_attention_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --examples-config configs/varbind_heldout_050_149_dot_length_sweep.json --filler-length 50 --max-items "$ITEMS" \
  --output-dir results/deepseek-v4-flash/dot-dump 2>&1 | grep -v "readout layer" | tail -6
python scripts/analyze_dot_residuals.py --dump deepseek=results/deepseek-v4-flash/dot-dump/dot_dump.pt --output-dir results/deepseek-v4-flash/dot-dump/analysis | tail -80
python scripts/plot_dot_analysis.py results/deepseek-v4-flash/dot-dump/analysis/dot-analysis.json --output-dir results/deepseek-v4-flash/dot-dump/analysis
echo RUN_DONE
