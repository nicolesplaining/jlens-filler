# DeepSeek V4 Flash filler-token J-Lens pilot

This repository contains a verified extraction path for **J-Lens token readouts** at
content-free filler positions. Ranked readouts are kept distinct from formal J-space
coordinates. A separate pilot now applies the paper's sparse nonnegative decomposition
using a pinned, model-free TransformerLens implementation because the released
Anthropic Jacobian Lens repository does not expose that routine.

## Current artifact

The initial five-shot prompt asks for the atomic number of tungsten plus the atomic
number of carbon, with ten dot fillers before `Answer:`. DeepSeek V4 Flash answers `80`
with and without filler. The filler condition was decoded at every lens-covered layer
with both the released J-Lens and a basic logit lens.

- Interactive viewer: [`results/filler/viewer.html`](results/filler/viewer.html)
- Qualitative report: [`results/filler/qualitative-report.md`](results/filler/qualitative-report.md)
- Full extraction record: [`results/filler/tungsten_plus_carbon.json`](results/filler/tungsten_plus_carbon.json)
- One-record-per-cell data: [`results/filler/readouts.jsonl`](results/filler/readouts.jsonl)
- Runtime and hashes: [`results/filler/runtime.json`](results/filler/runtime.json)
- One-example J-Lens/logit-lens metrics: [`results/first-comparison.csv`](results/first-comparison.csv)
- Compatibility audit: [`reports/compatibility.md`](reports/compatibility.md)
- Ordinary-prompt sanity checks: [`results/sanity/sanity.json`](results/sanity/sanity.json)
- Capital probe, all 42 J-Lens layers: [`results/capital-all-layers/capital-jlens-all-layers.md`](results/capital-all-layers/capital-jlens-all-layers.md)

Open `viewer.html` directly in a browser. It defaults to 22 evenly spaced layers and
can switch to all 42 layers or between J-Lens and logit lens. Selecting a cell shows
its complete top-10 with probabilities/logits and the exact ranks of `74`, `6`, and
`80`. A separately marked `Actual L42` row shows the model's true final logits at the
generation position, so the layer-41 lens readout cannot be mistaken for the answer.
The page also contains target-rank heatmaps and minimum-rank trajectories.

## Selected correct-with-filler calibration

The behaviorally selected paper-matched case `two_fact_0007` asks for Iridium's
atomic number (`77`) plus Antimony's (`51`). With no filler, the model answers `132`;
with 100 dots, it answers the correct sum, `128`, at probability 0.887. The extraction
covers all 100 filler tokens at all 42 released lens layers with both J-Lens and logit
lens.

- Interactive all-position viewer: [`results/two-fact-jlens-k100-selected/two_fact_0007/viewer.html`](results/two-fact-jlens-k100-selected/two_fact_0007/viewer.html)
- Full per-position Markdown: [`results/two-fact-jlens-k100-selected/two_fact_0007/qualitative-report.md`](results/two-fact-jlens-k100-selected/two_fact_0007/qualitative-report.md)
- Machine-readable cells: [`results/two-fact-jlens-k100-selected/two_fact_0007/readouts.jsonl`](results/two-fact-jlens-k100-selected/two_fact_0007/readouts.jsonl)
- Complete extraction: [`results/two-fact-jlens-k100-selected/two_fact_0007.json`](results/two-fact-jlens-k100-selected/two_fact_0007.json)
- Proposal/tooling interpretation: [`reports/proposal-tooling-and-selected-case.md`](reports/proposal-tooling-and-selected-case.md)

J-Lens exposes all three target numbers at rank 1 somewhere in the filler grid, but the
logit lens reaches the direct rank≤10 threshold earlier for all three in this example.
The sum also becomes highly ranked before both addends. This is a useful qualitative
decodability result, not yet a clean serial-computation or causal result.

## Three-fact and order ablations

The follow-up experiment adds oxygen as a third retrieved fact and tracks the first-two
partial sum (`80`) as well as the intended final sum (`88`). It runs both
`tungsten → carbon → oxygen` and `carbon → tungsten → oxygen`, plus the matched
two-fact `carbon → tungsten` swap. All three new conditions retain the same five-shot
structure, ten dot tokens, and non-thinking encoding.

- Combined Markdown summary: [`results/order-ablation-summary.md`](results/order-ablation-summary.md)
- Machine-readable comparison: [`results/order-ablation-summary.csv`](results/order-ablation-summary.csv)
- Three-fact W→C→O viewer: [`results/three-fact-order/tungsten-carbon-oxygen/viewer.html`](results/three-fact-order/tungsten-carbon-oxygen/viewer.html)
- Three-fact C→W→O viewer: [`results/three-fact-order/carbon-tungsten-oxygen/viewer.html`](results/three-fact-order/carbon-tungsten-oxygen/viewer.html)
- Two-fact C→W viewer: [`results/two-fact-swapped/carbon-plus-tungsten/viewer.html`](results/two-fact-swapped/carbon-plus-tungsten/viewer.html)

The three-fact prompts are error-analysis cases: W→C→O generates `106` with filler
and C→W→O generates `90`, rather than `88`. In W→C→O, however, J-Lens ranks the
correct `88` token second at layer 27/filler 3, compared with rank 59 for the logit
lens in that cell. This is evidence of a transported readout, not proof that the model
used or causally relied on that candidate.

## Repeated-squaring T-hop pilot

The `T=10` repeated modular-squaring condition is complete. For `N=437`, `x=12`,
the expected trace ends at `311`, but the model generated the first residue, `144`,
with and without ten dot fillers. All ten residues were tracked at all 42 released
J-Lens layers and all ten filler positions. Only `x_4 = 64` reached the J-Lens top
10 (rank 8 at layer 35, filler 1); the readouts do not show the expected serial
residue trajectory.

- Interactive viewer: [`results/repeated-squaring-t10/viewer.html`](results/repeated-squaring-t10/viewer.html)
- Qualitative report: [`results/repeated-squaring-t10/qualitative-report.md`](results/repeated-squaring-t10/qualitative-report.md)
- Machine-readable cells: [`results/repeated-squaring-t10/readouts.jsonl`](results/repeated-squaring-t10/readouts.jsonl)
- Complete extraction: [`results/repeated-squaring-t10/repeated_squaring_n437_x12_t10.json`](results/repeated-squaring-t10/repeated_squaring_n437_x12_t10.json)
- Experiment report and reproduction: [`reports/repeated-squaring-t10.md`](reports/repeated-squaring-t10.md)

The paper-matched follow-up `T=1...10` sweep is complete. It contains ten
shortcut-controlled base instances at every T (100 paired problems) and uses the
Appendix A instruction that there will be exactly 10 filler tokens. Dots scored
7/100 versus 2/100 without dots, a +5 percentage-point difference (95% paired
bootstrap interval +1 to +10; exact McNemar p=0.062). Correct-token rank favored
dots in 62 pairs versus 35 for no dots (exact sign-test p=0.008). No condition
solved a shortcut-controlled T=10 example.

- Paper-matched evaluation report: [`results/repeated-squaring-dot-eval-paper-prompt/evaluation-report.md`](results/repeated-squaring-dot-eval-paper-prompt/evaluation-report.md)
- Paper-matched per-T metrics: [`results/repeated-squaring-dot-eval-paper-prompt/summary.csv`](results/repeated-squaring-dot-eval-paper-prompt/summary.csv)
- Paper-matched paired examples: [`results/repeated-squaring-dot-eval-paper-prompt/pairs.csv`](results/repeated-squaring-dot-eval-paper-prompt/pairs.csv)
- Paper-matched prompts, logits, and ranks: [`results/repeated-squaring-dot-eval-paper-prompt/paired_task_eval.json`](results/repeated-squaring-dot-eval-paper-prompt/paired_task_eval.json)
- Correct T=4 J-Lens viewer: [`results/repeated-squaring-lens-paper-prompt-correct/repeated_squaring_n407_x30_t4/viewer.html`](results/repeated-squaring-lens-paper-prompt-correct/repeated_squaring_n407_x30_t4/viewer.html)
- Correct T=4 J-Lens/logit-lens ranks: [`results/repeated-squaring-lens-paper-prompt-correct/lens-summary.csv`](results/repeated-squaring-lens-paper-prompt-correct/lens-summary.csv)

The earlier 5/100 versus 2/100 sweep and selected viewers under
`results/repeated-squaring-dot-eval` and `results/repeated-squaring-lens-selected`
used “some filler tokens” plus an extra-space rationale. They are retained as a
prompt-wording ablation, not pooled with the paper-matched outputs.

In the legacy-prompt valid T=10 failure, J-Lens surfaces `gcd`, `φ`, `Carmichael`,
`factoring`, and `totient` around filler 3/layers 30-38, but does not recover a
serial residue trajectory. Across 26 selected intermediate targets, J-Lens beats
the logit lens on best filler-cell rank for 8, loses on 17, and ties once.

Both runs used two same-region two-H100 hosts with socket NCCL over their private
network. The ordinary-prompt sanity gate passed and final-head closure remained
within `9.7e-4` maximum absolute logit error across the selected examples.

## Filler-length sweeps and calibration-task choice

The paired dot-count sweep is complete. Repeated squaring is non-monotonic: k=3 and
k=10 both score 7/100 versus 2/100 without filler; k=25 and 50 score 5/100, and k=100
scores 3/100. A single T=9 example becomes correct at k=50 and 100, but no T=10
example succeeds. The high-T hit is a mechanistic candidate, not evidence by itself
of nine sequential squarings.

The released two-fact addition calibration is also complete on its first 100 targets.
Accuracy is 41/100 without filler and 45/100 at the best observed length, k=100. The
+4-point accuracy change is uncertain (95% paired-bootstrap interval -5 to +13;
McNemar p=0.523), but target rank improves in 37 pairs and worsens in 21 (sign-test
p=0.0479), while mean target log-probability increases by 0.741 nats. This healthier
behavioral regime makes two-fact addition the preferred primary J-Lens calibration;
repeated squaring remains a harder serial-computation stress test.

- Combined interpretation and recommendation: [`reports/filler-length-sweeps.md`](reports/filler-length-sweeps.md)
- Repeated-squaring sweep report: [`results/repeated-squaring-dot-length-sweep-paper-prompt/length-sweep-report.md`](results/repeated-squaring-dot-length-sweep-paper-prompt/length-sweep-report.md)
- Repeated-squaring complete sweep: [`results/repeated-squaring-dot-length-sweep-paper-prompt/filler_length_sweep.json`](results/repeated-squaring-dot-length-sweep-paper-prompt/filler_length_sweep.json)
- Two-fact sweep report: [`results/two-fact-addition-dot-length-sweep-paper-prompt/length-sweep-report.md`](results/two-fact-addition-dot-length-sweep-paper-prompt/length-sweep-report.md)
- Two-fact per-example table: [`results/two-fact-addition-dot-length-sweep-paper-prompt/examples.csv`](results/two-fact-addition-dot-length-sweep-paper-prompt/examples.csv)
- Selected qualitative cases: [`results/two-fact-addition-dot-length-sweep-paper-prompt/selected-examples.json`](results/two-fact-addition-dot-length-sweep-paper-prompt/selected-examples.json)

## Open models up to 35B: null result

`scripts/extract_hf.py` ports the behavioral sweep to single-GPU Transformers
checkpoints. On the released variable-binding items, ten open models from 4B to
35B (Qwen3/3.5/3.6 dense and MoE, Llama-3.1-8B, Gemma-3-27B, OLMo-3.1-32B) score
0–14% at every filler length with no placement-specific gain in accuracy or
log-probability; on a new one-step
variant where they sit at 50–85%, dots have no effect (200-item held-out
replication on Qwen3.5-4B: every length within ±3 correct of baseline). No lens
readouts were extracted because the behavior gate was not met.

- PDF report (screen, training, causal tests, dot anatomy): [`reports/pdf/filler-tokens-open-models.pdf`](reports/pdf/filler-tokens-open-models.pdf) (source: `filler-tokens-open-models.tex`, figures under `results/report-figures/`)
- Findings note: [`reports/small-open-model-null-result.md`](reports/small-open-model-null-result.md)

The follow-up trains Qwen3.5-9B with LoRA to solve the task with dots present
(`scripts/train_varbind_lora.py`, `scripts/build_varbind_sft_data.py`). Mixed-k,
chain-length-2, dots-only, and k=0-only variants all learn the task as a direct
computation: the dots-only model scores 40/50 with no dots at all. Logit-lens grids
on held-out items (`scripts/extract_hf.py --phase filler --adapter`) and all-layer
dot lesions (`scripts/patch_varbind_hf.py --lesion-all-dots --lesion-all-layers`)
show the dot positions decode to the dot token, carry no stage-specific content
beyond a faint late leak, and can be wiped at every block without changing the
answer. The computation resolves at the answer position in the last three blocks.

- Training records: `results/qwen3.5-9b/lora-{mixedk,c2-mixedk,dotsonly,k0only}/`, `results/qwen3.5-4b/lora-mixedk/`
- Held-out lens grids and viewers: `results/qwen3.5-9b/lens-heldout-k50/<model>/<item>/viewer.html`
- Dot-position anatomy (variance decomposition, probes, attention heatmaps, entropy): `results/qwen3.5-9b/dot-dump/analysis/`
- Same anatomy on DeepSeek V4 Flash (4×H100, Nicole's pipeline; per hyper-connection stream, recomputed sparse attention): `results/deepseek-v4-flash/dot-dump/analysis/`; scripts `dump_dot_residuals_dsv4.py`, `dump_dot_attention_dsv4.py`, `setup_dsv4_box.sh`, `run_dsv4_dot_dump.sh`
- Lesions and single-cell patch grids: `results/qwen3.5-9b/lora-*/lesion-all-layers/`, `results/qwen3.5-9b/patch-heldout-0067/`
- One-step config generator: [`scripts/build_onestep_varbind_configs.py`](scripts/build_onestep_varbind_configs.py)
- Screen driver: [`scripts/screen_models.sh`](scripts/screen_models.sh)
- Result directories: `results/<model>/` for each of the ten models

## Remote environment used

- 4 × NVIDIA H100 80 GB; observed extraction allocation about 42.7 GiB/GPU
- 885 GiB RAM and about 11 TB free disk before download
- Python 3.10, PyTorch 2.10.0+cu128, Transformers 5.0.0
- TileLang 0.1.8 and `apache-tvm-ffi` 0.1.3

The official requirements allow `apache-tvm-ffi` 0.1.2, but that version failed while
lowering the untouched DeepSeek sparse-attention kernel. Version 0.1.3 compiled and ran
the same kernel. The checkpoint uses FP8 non-expert weights and FP4 expert weights.

The original Hugging Face weights total 159,617,149,040 bytes (148.7 GiB). The four
converted model-parallel shards total about 167.9 GB. Allow at least 330 GB for the
conversion peak, plus normal cache/output headroom. The J-Lens file is 1,409,295,893
bytes. Do not begin a download without this space.

## Reproduction

The model is gated. Put a Hugging Face token in the environment; do not add it to a
command, config file, or shell history.

```bash
export HF_TOKEN='<your token>'
export WORK=/home/ubuntu/jlens-filler
python -m venv "$WORK/.venv"
source "$WORK/.venv/bin/activate"
pip install 'torch==2.10.0' 'transformers==5.0.0' 'safetensors>=0.7' \
  'tilelang==0.1.8' 'apache-tvm-ffi==0.1.3' 'huggingface-hub>=1.2'
```

`fast_hadamard_transform` is also required by the official model. Its PyPI source
archive did not include the necessary submodule in this run, so install the upstream
repository recursively:

```bash
git clone --recursive https://github.com/Dao-AILab/fast-hadamard-transform.git \
  "$WORK/fast-hadamard-transform"
pip install "$WORK/fast-hadamard-transform"
```

Download only after checking storage:

```bash
huggingface-cli download deepseek-ai/DeepSeek-V4-Flash \
  --revision 60d8d70770c6776ff598c94bb586a859a38244f1 \
  --local-dir "$WORK/cache/model_hf"
huggingface-cli download camilablank/workspace-lenses \
  deepseek-v4-flash/j-lens/lens.pt \
  --revision 781b233 \
  --local-dir "$WORK/cache/lens_repo"
```

Convert using DeepSeek's released reference code:

```bash
python "$WORK/cache/model_hf/inference/convert.py" \
  --hf-ckpt-path "$WORK/cache/model_hf" \
  --save-path "$WORK/cache/model_mp4" \
  --n-experts 256 \
  --model-parallel 4
cp "$WORK/cache/model_hf"/tokenizer*.json "$WORK/cache/model_mp4/"
```

Run the sanity gate first:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/initial_examples.json \
  --output-dir results/sanity \
  --phase sanity \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1
```

Only after `sanity_gate.json` says `passed: true`, extract all filler cells:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/initial_examples.json \
  --output-dir results/filler \
  --phase filler --layers all --top-k 10 --max-new-tokens 12 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python scripts/build_artifacts.py results/filler/tungsten_plus_carbon.json \
  --output-dir results/filler
```

Run the three-fact and order-ablation configs with the same model/lens arguments:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/three_fact_order_ablation.json \
  --output-dir results/three-fact-order \
  --phase all --layers all --top-k 10 --max-new-tokens 12 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/two_fact_swapped.json \
  --output-dir results/two-fact-swapped \
  --phase all --layers all --top-k 10 --max-new-tokens 12 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python scripts/build_artifacts.py \
  results/three-fact-order/tungsten_carbon_oxygen.json \
  --output-dir results/three-fact-order/tungsten-carbon-oxygen
python scripts/build_artifacts.py \
  results/three-fact-order/carbon_tungsten_oxygen.json \
  --output-dir results/three-fact-order/carbon-tungsten-oxygen
python scripts/build_artifacts.py \
  results/two-fact-swapped/carbon_plus_tungsten.json \
  --output-dir results/two-fact-swapped/carbon-plus-tungsten
python scripts/build_order_ablation_report.py
```

Evaluate the shortcut-controlled repeated-squaring sweep before extracting any
lens readouts:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/repeated_squaring_dot_eval.json \
  --output-dir results/repeated-squaring-dot-eval-paper-prompt \
  --phase eval --top-k 10 --max-new-tokens 12 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/build_repeated_squaring_eval_report.py \
  results/repeated-squaring-dot-eval-paper-prompt/paired_task_eval.json \
  --output-dir results/repeated-squaring-dot-eval-paper-prompt
```

Run the paired filler-length sweeps. Each config includes k=0, so the identical
no-filler baseline is evaluated once per example rather than once per positive length:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/repeated_squaring_dot_length_sweep.json \
  --output-dir results/repeated-squaring-dot-length-sweep-paper-prompt \
  --phase eval --top-k 10 --max-new-tokens 3 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/build_repeated_squaring_length_sweep_report.py \
  results/repeated-squaring-dot-length-sweep-paper-prompt/filler_length_sweep.json \
  --output-dir results/repeated-squaring-dot-length-sweep-paper-prompt

torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/two_fact_addition_dot_length_sweep.json \
  --output-dir results/two-fact-addition-dot-length-sweep-paper-prompt \
  --phase eval --top-k 10 --max-new-tokens 3 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/build_two_fact_length_sweep_report.py \
  results/two-fact-addition-dot-length-sweep-paper-prompt/filler_length_sweep.json \
  --output-dir results/two-fact-addition-dot-length-sweep-paper-prompt
```

Extract the selected two-fact case at the best tested length and build its complete
viewer (the command below is for one four-GPU host; a two-node launch must still have
four total ranks):

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/two_fact_jlens_selected_k100.json \
  --example-ids two_fact_0007 \
  --output-dir results/two-fact-jlens-k100-selected \
  --phase all --layers all --top-k 10 --max-new-tokens 3 --max-seq-len 1024 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/build_artifacts.py \
  results/two-fact-jlens-k100-selected/two_fact_0007.json \
  --output-dir results/two-fact-jlens-k100-selected/two_fact_0007
```

Then extract the highest-T dots-only correct case and build its viewer:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/repeated_squaring_lens_selected.json \
  --example-ids repeated_squaring_n407_x30_t4 \
  --output-dir results/repeated-squaring-lens-paper-prompt-correct \
  --phase all --layers all --top-k 10 --max-new-tokens 12 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/build_artifacts.py \
  results/repeated-squaring-lens-paper-prompt-correct/repeated_squaring_n407_x30_t4.json \
  --output-dir results/repeated-squaring-lens-paper-prompt-correct/repeated_squaring_n407_x30_t4

python3 scripts/build_repeated_squaring_lens_summary.py \
  results/repeated-squaring-lens-paper-prompt-correct \
  configs/repeated_squaring_lens_selected.json \
  --example-ids repeated_squaring_n407_x30_t4 \
  --output-dir results/repeated-squaring-lens-paper-prompt-correct
```

## Algorithm/parallelism probe suite

Generate the deterministic variable-binding, three-fact order, element-letter,
pointer-chase, and pre-question placement-control configs from the pinned released
filler repository checkout:

```bash
python3 scripts/build_algorithm_probe_configs.py \
  --source-dir tmp/filler-token-reasoning \
  --output-dir configs
```

Use the same four-rank model/lens launch described above. The principal behavioral
run and causal placement control are:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/varbind_easy_dot_length_sweep.json \
  --output-dir results/algorithm-probes/varbind-eval \
  --phase eval --top-k 10 --max-new-tokens 3 --max-seq-len 1280 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/varbind_pre_question_k50_control.json \
  --output-dir results/algorithm-probes/varbind-pre-question-k50-control \
  --phase eval --top-k 10 --max-new-tokens 3 --max-seq-len 1024 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1
```

Extract the four selected k=50 cases and build each standalone viewer:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/varbind_jlens_k50_selected.json \
  --output-dir results/algorithm-probes/varbind-jlens-k50 \
  --phase all --layers all --top-k 10 --max-new-tokens 3 --max-seq-len 1280 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

for result in results/algorithm-probes/varbind-jlens-k50/varbind_easy_*.json; do
  python3 scripts/build_artifacts.py "$result" --output-dir "${result%.json}"
done
```

Aggregate the layer ladder, dot-threshold comparisons, and deranged-token control:

```bash
python3 scripts/build_varbind_algorithm_report.py \
  --behavior-summary results/algorithm-probes/varbind-eval/behavior-summary.json \
  --k50-dir results/algorithm-probes/varbind-jlens-k50 \
  --threshold-json results/algorithm-probes/varbind-jlens-k5-threshold/varbind_easy_0035.json \
  --threshold-json results/algorithm-probes/varbind-jlens-k25-threshold/varbind_easy_0035.json \
  --threshold-json results/algorithm-probes/varbind-jlens-k100-boundary/varbind_easy_0037.json \
  --output-dir results/algorithm-probes/varbind-analysis
```

For the behavior-gated causal deep dive, first select all examples rescued at
`k=50`, extract every filler cell, and build the matched patch manifest:

```bash
python3 scripts/select_varbind_deep_dive.py \
  results/algorithm-probes/varbind-eval/filler_length_sweep.json \
  configs/varbind_easy_dot_length_sweep.json \
  --output configs/varbind_jlens_k50_all_rescued.json \
  --filler-length 50 --include-failures

torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/varbind_jlens_k50_all_rescued.json \
  --output-dir results/algorithm-probes/varbind-jlens-k50-all-rescued \
  --phase all --layers all --top-k 10 --max-new-tokens 3 --max-seq-len 1024 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/build_varbind_deep_dive.py \
  results/algorithm-probes/varbind-jlens-k50-all-rescued \
  --output-dir results/algorithm-probes/varbind-jlens-k50-all-rescued/analysis \
  --patch-pair varbind_easy_0033,varbind_easy_0002 --patch-cells 16
```

The tighter counterfactual holds the entire prompt and token layout fixed while
changing only `suv = 64` to another one-token value. Screen behavior before any
causal interpretation:

```bash
python3 scripts/build_varbind_counterfactuals.py \
  configs/varbind_jlens_k50_all_rescued.json \
  --output configs/varbind_counterfactual_behavior.json

torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/varbind_counterfactual_behavior.json \
  --output-dir results/algorithm-probes/varbind-counterfactual-eval \
  --phase eval --top-k 10 --max-new-tokens 3 --max-seq-len 1024 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/analyze_behavior_sweep.py \
  results/algorithm-probes/varbind-counterfactual-eval/filler_length_sweep.json \
  --output-dir results/algorithm-probes/varbind-counterfactual-eval
```

Then extract the exact-layout pair and map every single-cell intervention. The
strict flag aborts unless the two prompts have equal token lengths, identical filler
indices, and exactly one differing token:

```bash
python3 scripts/build_varbind_counterfactuals.py \
  configs/varbind_jlens_k50_all_rescued.json \
  --single-filler-length 50 \
  --output configs/varbind_counterfactual_jlens_k50.json

torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/varbind_counterfactual_jlens_k50.json \
  --example-ids varbind_cf_suv_064,varbind_cf_suv_072 \
  --output-dir results/algorithm-probes/varbind-counterfactual-jlens-k50 \
  --phase all --layers all --top-k 10 --max-new-tokens 3 --max-seq-len 1024 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

torchrun --standalone --nproc-per-node=4 scripts/sweep_varbind_patches_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --examples-config configs/varbind_counterfactual_jlens_k50.json \
  --donor-id varbind_cf_suv_072 --target-id varbind_cf_suv_064 \
  --layers 29-38 --require-identical-token-layout \
  --output-dir results/algorithm-probes/varbind-counterfactual-single-cell-grid-072-to-064 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/build_varbind_patch_manifest.py \
  results/algorithm-probes/varbind-counterfactual-jlens-k50 \
  --pair varbind_cf_suv_072,varbind_cf_suv_064 --cells 16 \
  --output results/algorithm-probes/varbind-counterfactual-jlens-k50/patch-manifest.json

torchrun --standalone --nproc-per-node=4 scripts/patch_varbind_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --examples-config configs/varbind_counterfactual_jlens_k50.json \
  --patch-manifest results/algorithm-probes/varbind-counterfactual-jlens-k50/patch-manifest.json \
  --output-dir results/algorithm-probes/varbind-counterfactual-patching-pilot \
  --doses 1,4,8,16 --stages bound_value,second_product,answer \
  --require-identical-token-layout \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/analyze_varbind_causal_map.py \
  --readout-dir results/algorithm-probes/varbind-jlens-k50-all-rescued \
  --causal-readout-dir results/algorithm-probes/varbind-counterfactual-jlens-k50 \
  --deep-dive-summary results/algorithm-probes/varbind-jlens-k50-all-rescued/analysis/varbind-deep-dive-summary.json \
  --patch-results results/algorithm-probes/varbind-counterfactual-patching-pilot/patch-results.json \
  --causal-grid results/algorithm-probes/varbind-counterfactual-single-cell-grid-072-to-064/single-cell-grid.json \
  --behavior-summary results/algorithm-probes/varbind-counterfactual-eval/behavior-summary.json \
  --output-dir results/algorithm-probes/varbind-counterfactual-causal-analysis

python3 scripts/build_varbind_causal_viewer.py \
  results/algorithm-probes/varbind-counterfactual-causal-analysis/varbind-causal-analysis.json \
  results/algorithm-probes/varbind-counterfactual-causal-analysis/varbind-causal-viewer.html
```

### Beyond-paper workspace-address probe

The follow-up uses 100 held-out released templates for an independent behavioral
gate, then makes six exact-layout counterfactual families by changing a single
two-digit literal. Generate the held-out and family sweeps with:

```bash
python3 scripts/build_varbind_scaling_configs.py screen \
  --dataset tmp/filler-token-reasoning/data/chained_var_binding_dataset.json \
  --start 50 --count 100 \
  --output configs/varbind_heldout_050_149_dot_length_sweep.json

python3 scripts/build_varbind_scaling_configs.py families \
  --screen-config configs/varbind_heldout_050_149_dot_length_sweep.json \
  --sweep results/algorithm-probes/varbind-heldout-050-149-sweep/filler_length_sweep.json \
  --selection-length 50 --family-count 6 \
  --base-values 52,56,60,64,68,72,76,80 \
  --output configs/varbind_scaled_counterfactual_families_sweep.json
```

Run both configs with `extract_dsv4.py --phase eval`, as above, using filler
lengths `0,5,10,25,50,100`; then select three pairs that are wrong without dots
and correct at k=50:

```bash
python3 scripts/build_varbind_scaling_configs.py select \
  --families-config configs/varbind_scaled_counterfactual_families_sweep.json \
  --sweep results/algorithm-probes/varbind-scaled-counterfactual-families-sweep/filler_length_sweep.json \
  --selection-length 50 --output-filler-length 50 \
  --members both --min-pairs 3 --max-pairs 3 \
  --output configs/varbind_scaled_jlens_k50_pairs.json
```

Extract all released J-Lens layers for both members at k=50 and the selected
donors at k=5,10,25,100. Build the causal manifest and compare coordinate
systems across filler lengths:

```bash
python3 scripts/build_varbind_scaling_manifest.py \
  results/algorithm-probes/varbind-scaled-jlens-k50 \
  --config configs/varbind_scaled_jlens_k50_pairs.json --cells 16 --max-pairs 3 \
  --output results/algorithm-probes/varbind-scaled-jlens-k50/patch-manifest.json

python3 scripts/analyze_varbind_lane_scaling.py \
  --readout 5=results/algorithm-probes/varbind-scaled-jlens-k5 \
  --readout 10=results/algorithm-probes/varbind-scaled-jlens-k10 \
  --readout 25=results/algorithm-probes/varbind-scaled-jlens-k25 \
  --readout 50=results/algorithm-probes/varbind-scaled-jlens-k50 \
  --readout 100=results/algorithm-probes/varbind-scaled-jlens-k100 \
  --output-dir results/algorithm-probes/varbind-scaled-lane-analysis
```

Finally, move each readout-selected raw post-block residual through every k=50
destination at the same layer, and compare mean-residual lesions against
layer-matched random cells:

```bash
torchrun --standalone --nproc-per-node=4 scripts/probe_varbind_workspace_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --examples-config configs/varbind_scaled_jlens_k50_pairs.json \
  --patch-manifest results/algorithm-probes/varbind-scaled-jlens-k50/patch-manifest.json \
  --output-dir results/algorithm-probes/varbind-scaled-workspace-probe-k50 \
  --stages second_product,answer --source-cells 1 --destination-stride 1 \
  --lesion-doses 1,4,8,16 --max-seq-len 1280 \
  --require-identical-token-layout \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/analyze_varbind_workspace_probe.py \
  results/algorithm-probes/varbind-scaled-workspace-probe-k50/workspace-probe-results.json \
  --output-dir results/algorithm-probes/varbind-scaled-workspace-analysis
```

Open the consolidated causal and behavioral viewer at
[`results/algorithm-probes/varbind-scaled-workspace-analysis/workspace-mechanism-viewer.html`](results/algorithm-probes/varbind-scaled-workspace-analysis/workspace-mechanism-viewer.html).
The associated numeric report is
[`results/algorithm-probes/varbind-scaled-workspace-analysis/workspace-probe-report.md`](results/algorithm-probes/varbind-scaled-workspace-analysis/workspace-probe-report.md).

The most non-monotonic family has a sibling-variable error: the correct route is
`125 → 250 → 235`, while the confident wrong answer `185` comes from the sibling
route `100 → 200 → 185`. Build one multi-length config with both routes tracked,
then extract every positive configured length in a single model load:

```bash
python3 scripts/build_varbind_scaling_configs.py example \
  --families-config configs/varbind_scaled_counterfactual_families_sweep.json \
  --example-id varbind_scale_f05_kur_064 --all-filler-lengths \
  --tracked distractor_bound=100 \
  --tracked distractor_second_product=200 \
  --tracked distractor_answer=185 \
  --output configs/varbind_resonance_f05_kur_064_sweep.json

torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/varbind_resonance_f05_kur_064_sweep.json \
  --example-ids varbind_scale_f05_kur_064 \
  --output-dir results/algorithm-probes/varbind-resonance-f05-kur-064 \
  --phase filler --layers all --top-k 10 --max-new-tokens 3 --max-seq-len 1280 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/analyze_varbind_resonance.py \
  --readout 5=results/algorithm-probes/varbind-resonance-f05-kur-064/k5/varbind_scale_f05_kur_064.json \
  --readout 10=results/algorithm-probes/varbind-resonance-f05-kur-064/k10/varbind_scale_f05_kur_064.json \
  --readout 25=results/algorithm-probes/varbind-resonance-f05-kur-064/k25/varbind_scale_f05_kur_064.json \
  --readout 50=results/algorithm-probes/varbind-resonance-f05-kur-064/k50/varbind_scale_f05_kur_064.json \
  --readout 100=results/algorithm-probes/varbind-resonance-f05-kur-064/k100/varbind_scale_f05_kur_064.json \
  --example-id varbind_scale_f05_kur_064 \
  --behavior-sweep results/algorithm-probes/varbind-scaled-counterfactual-families-sweep/filler_length_sweep.json \
  --output-dir results/algorithm-probes/varbind-resonance-analysis
```

The candidate-competition summary is
[`results/algorithm-probes/varbind-resonance-analysis/resonance-report.md`](results/algorithm-probes/varbind-resonance-analysis/resonance-report.md),
with full all-layer viewers for each dot count under
[`results/algorithm-probes/varbind-resonance-f05-kur-064/`](results/algorithm-probes/varbind-resonance-f05-kur-064/).

### Formal sparse J-space pilot

The formal follow-up decomposes ten preselected filler activations into at most 25
nonnegative J-Lens dictionary atoms. For layer `l`, the dictionary is
`(W_U * final_rmsnorm_weight) @ J_l`; this exactly preserves the corresponding J-Lens
top-25 rankings after the activation-dependent RMS scalar is restored. The target is
the 4096-wide activation produced by DeepSeek's final mHC hyper-head from each raw
post-block `[4,4096]` state, matching the readout pipeline.

The implementation is pinned to TransformerLens revision
`1f8224d5e147c98e8f43f0d310e32bbd1578a4b6`; the decomposition source file has SHA-256
`3193aeee3174ad9781327aca42d1cac7466d2cbf88530d39da831f02a9eb1161`.
On the two cells where the ranked readout contains both answer candidates (`235` first,
`185` second), the formal `k=25` support retains `235` and omits `185`. Across all
tracked targets, it retains every rank-1 task token (`7/7`) and none of the rank-2–25
task tokens (`0/9`). This makes the selected cells look more winner-like than their
ranked token lists, while the two candidates still coexist across different positions
and layers.

The raw reconstruction explains 6.60% of activation squared norm on average, versus
7.18% for the Haar-rotated relative-orientation control and 7.05% for the matched
sparse logit-space baseline. Therefore the pilot does not show a broad reconstruction
advantage for J-space. It does find two selected task atoms that the sparse logit-space
baseline omits, but the sites were selected using J-Lens and cannot support an unbiased
superiority claim.

Run the distributed decomposition after cloning the pinned TransformerLens revision:

```bash
torchrun --standalone --nproc-per-node=4 scripts/decompose_jspace_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/varbind_resonance_f05_kur_064_sweep.json \
  --sites-config configs/varbind_resonance_jspace_cells.json \
  --decomposition-module "$WORK/third_party/TransformerLens/transformer_lens/tools/analysis/jacobian_lens_decomposition.py" \
  --decomposition-revision 1f8224d5e147c98e8f43f0d310e32bbd1578a4b6 \
  --expected-decomposition-sha256 3193aeee3174ad9781327aca42d1cac7466d2cbf88530d39da831f02a9eb1161 \
  --output-dir results/algorithm-probes/varbind-resonance-jspace-decomposition \
  --k 25 --algorithm gradient_pursuit --top-k 25 \
  --rotation-control-seeds 101,202,303 --max-seq-len 1280 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/analyze_varbind_jspace.py \
  results/algorithm-probes/varbind-resonance-jspace-decomposition/jspace-decomposition.json \
  --output-dir results/algorithm-probes/varbind-resonance-jspace-decomposition
```

The complete result is in
[`results/algorithm-probes/varbind-resonance-jspace-decomposition/jspace-decomposition-report.md`](results/algorithm-probes/varbind-resonance-jspace-decomposition/jspace-decomposition-report.md),
with the full support, coefficients, controls, and validation records in the adjacent
JSON files.

The consolidated interpretation is in
[`reports/algorithm-exploration-findings.md`](reports/algorithm-exploration-findings.md).

## Scientific boundary before scaling

DeepSeek V4 block outputs have shape `[batch, sequence, 4, 4096]`, while the requested
lens contains square `4096 × 4096` matrices and does not record the source projection
used during fitting. This implementation applies the model's exact final hyper-head to
collapse the four streams at every layer, then applies the lens, final RMSNorm, and
unembedding. Final-layer closure and the identity anchor validate the downstream
decode, but they cannot prove that the inferred per-layer collapse matches lens fitting.

That omission should be resolved with the lens publisher before treating a larger pilot
as definitive. No alternate V4 revision or third-party rectangular lens is silently
substituted.

## References

- [DeepSeek V4 Flash model and official inference/encoding code](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)
- [Released DeepSeek V4 Flash J-Lens](https://huggingface.co/camilablank/workspace-lenses/tree/main/deepseek-v4-flash/j-lens)
- [Jacobian Lens code](https://github.com/anthropics/jacobian-lens)
- [Jacobian Lens paper](https://transformer-circuits.pub/2026/workspace/index.html)
- [Filler-token paper](https://arxiv.org/html/2607.03502v1)
- [Filler-token code](https://github.com/kaleybrauer/filler-token-reasoning)
