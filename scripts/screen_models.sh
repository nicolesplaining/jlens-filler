#!/usr/bin/env bash
# Behavioral filler screen over several models. Per model: smoke (2 items) ->
# released two-step sweep -> pre-question control -> one-step sweep -> analysis.
# A failure in one model is logged and the loop continues.
cd ~/jlens-filler && source ~/venv/bin/activate
F="Loading weights\|Python version\|clean_up_tokenization\|end-of-turn\|causal_conv1d\|^\["
run() {  # tag path config outdir
  python scripts/extract_hf.py --model-id "$2" --model-revision main --examples-config "$3" \
    --output-dir "$4" --max-new-tokens 3 2>&1 | { grep -v "$F" || true; }
  test -f "$4/filler_length_sweep.json"
}
for spec in "$@"; do
  IFS=: read -r tag path <<<"$spec"
  echo; echo "################ $tag ################"; date
  if ! test -f "$path/config.json"; then echo "SKIP $tag: no config.json"; continue; fi
  python scripts/extract_hf.py --model-id "$path" --model-revision main \
     --examples-config configs/varbind_easy_dot_length_sweep.json --output-dir results/$tag/smoke \
     --example-ids varbind_easy_0000,varbind_easy_0035 --max-new-tokens 3 2>&1 | { grep -v "$F" || true; }
  if ! test -f results/$tag/smoke/filler_length_sweep.json; then echo "FAIL $tag: smoke"; continue; fi
  python - "$tag" <<'PY'
import json, sys
d = json.load(open(f"results/{sys.argv[1]}/smoke/filler_length_sweep.json"))
for r in d["examples"]:
    print("  smoke", r["id"], "expect", r["expected_answer"], {k: c["generated_text"] for k, c in r["conditions"].items()})
PY
  run $tag "$path" configs/varbind_easy_dot_length_sweep.json results/$tag/varbind-eval || { echo "FAIL $tag: two-step"; continue; }
  run $tag "$path" configs/varbind_pre_question_k50_control.json results/$tag/varbind-pre-question-k50-control || echo "FAIL $tag: control"
  run $tag "$path" configs/varbind_onestep_dot_length_sweep.json results/$tag/varbind-onestep-eval || echo "FAIL $tag: one-step"
  for d in varbind-eval varbind-pre-question-k50-control varbind-onestep-eval; do
    test -f results/$tag/$d/filler_length_sweep.json && python scripts/analyze_behavior_sweep.py results/$tag/$d/filler_length_sweep.json --output-dir results/$tag/$d >/dev/null
  done
  echo "--- $tag two-step ---";  grep "^|" results/$tag/varbind-eval/behavior-report.md 2>/dev/null
  echo "--- $tag control ---";   grep "^|" results/$tag/varbind-pre-question-k50-control/behavior-report.md 2>/dev/null
  echo "--- $tag one-step ---";  grep "^|" results/$tag/varbind-onestep-eval/behavior-report.md 2>/dev/null
  date
done
echo SCREEN_DONE
