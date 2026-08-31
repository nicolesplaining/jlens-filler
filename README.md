# DeepSeek V4 Flash filler-token J-Lens pilot

This repository contains a verified one-example extraction path for **J-Lens token
readouts** at content-free filler positions. It does not label the ranked readouts as
formal J-space coordinates; the released Jacobian Lens repository does not include the
paper's sparse nonnegative decomposition routine.

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

The follow-up calibrated `T=1...10` sweep is also complete. It contains ten
shortcut-controlled base instances at every T (100 paired problems). Dots scored
5/100 versus 2/100 without dots, a directionally positive but inconclusive
difference of +3 percentage points (95% paired-bootstrap interval -2 to +8;
exact McNemar p=0.453). No condition solved a shortcut-controlled T=10 example.

- Dot/no-dot evaluation report: [`results/repeated-squaring-dot-eval/evaluation-report.md`](results/repeated-squaring-dot-eval/evaluation-report.md)
- Per-T metrics: [`results/repeated-squaring-dot-eval/summary.csv`](results/repeated-squaring-dot-eval/summary.csv)
- All paired examples: [`results/repeated-squaring-dot-eval/pairs.csv`](results/repeated-squaring-dot-eval/pairs.csv)
- Combined prompts, logits, ranks, and provenance: [`results/repeated-squaring-dot-eval/paired_task_eval.json`](results/repeated-squaring-dot-eval/paired_task_eval.json)
- Selected J-Lens summary: [`results/repeated-squaring-lens-selected/summary.md`](results/repeated-squaring-lens-selected/summary.md)
- Selected J-Lens/logit-lens ranks: [`results/repeated-squaring-lens-selected/lens-summary.csv`](results/repeated-squaring-lens-selected/lens-summary.csv)

In the valid T=10 failure, J-Lens surfaces `gcd`, `φ`, `Carmichael`,
`factoring`, and `totient` around filler 3/layers 30-38, but does not recover a
serial residue trajectory. Across 26 selected intermediate targets, J-Lens beats
the logit lens on best filler-cell rank for 8, loses on 17, and ties once.

Both runs used two same-region two-H100 hosts with socket NCCL over their private
network. The ordinary-prompt sanity gate passed and final-head closure remained
within `9.7e-4` maximum absolute logit error across the selected examples.

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
  --output-dir results/repeated-squaring-dot-eval \
  --phase eval --top-k 10 --max-new-tokens 12 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

python3 scripts/build_repeated_squaring_eval_report.py \
  results/repeated-squaring-dot-eval/paired_task_eval.json \
  --output-dir results/repeated-squaring-dot-eval
```

Then extract the five preselected qualitative cases and build their viewers:

```bash
torchrun --standalone --nproc-per-node=4 scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens_repo/deepseek-v4-flash/j-lens/lens.pt" \
  --examples-config configs/repeated_squaring_lens_selected.json \
  --output-dir results/repeated-squaring-lens-selected \
  --phase all --layers all --top-k 10 --max-new-tokens 12 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1

for stem in repeated_squaring_n209_x24_t3 \
  repeated_squaring_n407_x30_t4 repeated_squaring_n667_x41_t10 \
  repeated_squaring_n473_x31_t1 repeated_squaring_n473_x31_t8; do
  python3 scripts/build_artifacts.py \
    "results/repeated-squaring-lens-selected/$stem.json" \
    --output-dir "results/repeated-squaring-lens-selected/$stem"
done

python3 scripts/build_repeated_squaring_lens_summary.py \
  results/repeated-squaring-lens-selected \
  configs/repeated_squaring_lens_selected.json \
  --output-dir results/repeated-squaring-lens-selected
```

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
