#!/usr/bin/env bash
# DeepSeek-V4-Flash-Base: dot-residual dump + attention dump on the 50 held-out items at k=50 (chat rendering,
# same items and settings as the chat-model run in run_dsv4_dot_dump.sh), then the anatomy analysis.
set -eo pipefail
export PYTORCH_ALLOC_CONF=expandable_segments:True   # FP8 experts OOM under the default allocator; see run_dsv4_base_eval.sh
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
ITEMS=${ITEMS:-50}; OUT=results/deepseek-v4-flash-base/dot-dump; LOGDIR=$HOME/base-logs; mkdir -p "$LOGDIR" "$OUT"
COMMON="--ckpt-path $WORK/cache/base_mp4 --model-config $WORK/cache/base_config.json --reference-code-dir $WORK/cache/model_hf/inference --examples-config configs/varbind_heldout_050_149_dot_length_sweep.json --filler-length 50 --max-items $ITEMS --output-dir $OUT"
echo "=== base residual dump ==="
torchrun --standalone --nproc-per-node=4 scripts/dump_dot_residuals_dsv4.py $COMMON 2>&1 | grep -v "readout layer" | tee "$LOGDIR/base-resid-dump.log" | tail -4
echo "=== base attention dump ==="
torchrun --standalone --nproc-per-node=4 scripts/dump_dot_attention_dsv4.py $COMMON 2>&1 | grep -v "readout layer" | tee "$LOGDIR/base-attn-dump.log" | tail -6
echo "=== analysis ==="
python scripts/analyze_dot_residuals.py --dump deepseek-base=$OUT/dot_dump.pt --output-dir $OUT/analysis | tail -80
python scripts/plot_dot_analysis.py $OUT/analysis/dot-analysis.json --output-dir $OUT/analysis
echo BASE_DUMP_DONE
