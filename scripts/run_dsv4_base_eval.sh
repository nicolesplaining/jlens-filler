#!/usr/bin/env bash
# DeepSeek-V4-Flash-Base: sanity gate, then the released two-step sweep in chat and plain rendering,
# plus the pre-question placement control. Uses the chat repo's reference code with expert_dtype=null.
set -eo pipefail
# FP8 experts are 8 MiB tensors; the default caching allocator rounds each into a 20 MiB segment and
# wastes ~12 GiB per GPU, which OOMs a 79 GiB H100 with 70 GiB of weights. Expandable segments avoid that.
export PYTORCH_ALLOC_CONF=expandable_segments:True
LOGDIR=$HOME/base-logs; mkdir -p "$LOGDIR"
export WORK=${WORK:-$HOME/jlens-filler}; cd "$WORK"; source "$WORK/.venv/bin/activate"
COMMON="--ckpt-path $WORK/cache/base_mp4 --model-config $WORK/cache/base_config.json --reference-code-dir $WORK/cache/model_hf/inference --lens-path $WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt --model-revision base --max-seq-len 1280"
echo "=== sanity gate (chat rendering) ==="
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py $COMMON --examples-config configs/initial_examples.json --output-dir results/deepseek-v4-flash-base/sanity --phase sanity 2>&1 | grep -v "^readout layer" | tee "$LOGDIR/sanity.log" | tail -3
cat results/deepseek-v4-flash-base/sanity/sanity_gate.json
nvidia-smi --query-gpu=memory.used --format=csv,noheader | tr '\n' ' '; echo
for spec in "chat:varbind-eval:configs/varbind_easy_dot_length_sweep.json" "plain:varbind-eval-plain:configs/varbind_easy_dot_length_sweep.json" "chat:varbind-pre-question-k50-control:configs/varbind_pre_question_k50_control.json" "plain:varbind-pre-question-k50-control-plain:configs/varbind_pre_question_k50_control.json"; do
  IFS=: read -r render outdir cfg <<<"$spec"
  echo "=== $outdir ($render) ==="
  torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py $COMMON --examples-config "$cfg" --output-dir "results/deepseek-v4-flash-base/$outdir" --phase eval --top-k 10 --max-new-tokens 3 --render "$render" 2>&1 | grep -v "^readout layer\|^length sweep" | tee "$LOGDIR/$outdir.log" | tail -2
  python scripts/analyze_behavior_sweep.py "results/deepseek-v4-flash-base/$outdir/filler_length_sweep.json" --output-dir "results/deepseek-v4-flash-base/$outdir" >/dev/null
  grep "^|" "results/deepseek-v4-flash-base/$outdir/behavior-report.md"
done
echo BASE_EVAL_DONE
