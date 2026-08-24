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
