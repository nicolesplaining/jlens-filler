# Repeated-squaring T=10 J-Lens pilot

## Outcome

Completed on 2026-08-30 with four H100 80 GB GPUs split across two hosts in the
same region. The ordinary-prompt sanity gate passed, every released J-Lens layer
was decoded, and the model's final-head reconstruction had zero maximum absolute
logit error.

The expected recurrence was:

```text
N = 437 = 19 x 23, x_0 = 12, T = 10
144 -> 197 -> 353 -> 64 -> 163 -> 349 -> 315 -> 26 -> 239 -> 311
```

The correct answer is `311`. DeepSeek V4 Flash generated `144` in both the
ten-dot filler condition and the no-filler control. At the answer position, `144`
had probability 0.570 with filler and 0.642 without filler. This looks like the
model performed or retrieved the first squaring and stopped, rather than carrying
out the ten-step dependency chain.

## Qualitative J-Lens result

The table reports the best rank for each known residue over all 42 lens-covered
layers and all ten filler positions.

| Residue | J-Lens best | Logit-lens best |
|---|---:|---:|
| `x_1 = 144` | 213 (L37, F1) | 66 (L35, F1) |
| `x_2 = 197` | 926 (L41, F10) | 357 (L34, F1) |
| `x_3 = 353` | 245 (L37, F1) | 46 (L37, F1) |
| `x_4 = 64` | **8 (L35, F1)** | 15 (L35, F1) |
| `x_5 = 163` | 527 (L37, F1) | 129 (L0, F6) |
| `x_6 = 349` | 48 (L37, F1) | 78 (L37, F1) |
| `x_7 = 315` | 533 (L37, F1) | 226 (L37, F1) |
| `x_8 = 26` | 754 (L35, F1) | 435 (L35, F1) |
| `x_9 = 239` | 1,745 (L41, F9) | 1,674 (L32, F1) |
| `x_10 = 311` | 682 (L37, F1) | 179 (L0, F6) |

Only `x_4 = 64` reached rank 10 or better in either readout; J-Lens improved it
from logit-lens rank 15 to rank 8 at layer 35, filler position 1. J-Lens also
improved `x_6 = 349` from best rank 78 to 48. It ranked the other eight exact
residue tokens worse than the basic logit lens at their respective best cells.

The top readouts nevertheless contain task-structure concepts. Examples include
`期望`/“expected,” `计算`/“calculation,” `repeated`, `repetition`, `step`,
`observing`, and `Answer`. At L35/F1, the J-Lens top tokens were `68`, `69`,
`66`, `重复`, and `67`, with the true intermediate `64` at rank 8. These are
J-Lens token readouts, not literal thoughts or formal sparse J-space coordinates.

There is no monotonic filler-position trajectory matching
`144 -> ... -> 311`. Most numerical signal is concentrated at the first filler
position, while later positions mostly decode the filler surface or broad task
semantics. This example therefore does not support the hypothesis that the ten
fillers contain a serial ten-residue computation.

## Artifacts

- Interactive J-Lens/logit-lens viewer:
  [`results/repeated-squaring-t10/viewer.html`](../results/repeated-squaring-t10/viewer.html)
- Position-organized qualitative report:
  [`results/repeated-squaring-t10/qualitative-report.md`](../results/repeated-squaring-t10/qualitative-report.md)
- One record per layer-position-readout cell:
  [`results/repeated-squaring-t10/readouts.jsonl`](../results/repeated-squaring-t10/readouts.jsonl)
- Complete compact extraction:
  [`results/repeated-squaring-t10/repeated_squaring_n437_x12_t10.json`](../results/repeated-squaring-t10/repeated_squaring_n437_x12_t10.json)
- Runtime, hashes, and activation conventions:
  [`results/repeated-squaring-t10/runtime.json`](../results/repeated-squaring-t10/runtime.json)
- Ordinary-prompt checks and gate:
  [`sanity.json`](../results/repeated-squaring-t10/sanity.json) and
  [`sanity_gate.json`](../results/repeated-squaring-t10/sanity_gate.json)

The viewer defaults to approximately 22 evenly spaced layers. It can switch to
all 42 released lens layers, switch between J-Lens and logit lens, inspect the
top 10 for any cell, and display a rank heatmap for each of the ten residues. It
also distinguishes the true block-42 logits from the released lens's final
source layer, 41.

## Prompt and token alignment

The prompt uses DeepSeek's official non-thinking encoding and five worked
demonstrations. Ten dots occur strictly between the target question and
`Answer:`.

- Filler token indices: 448-457 inclusive.
- Filler 1-9 decode as ` .`.
- Filler 10 decodes as ` .\n\n`.
- The selected answer-cue token is `:` at index 459.
- The answer-prediction position is `</think>` at index 461.

Thus the ten visible dots are exactly ten model tokens in this prompt, but this
was established from offsets rather than assumed. The complete rendered prompt,
input IDs, decoded strings, character offsets, and selected columns are stored in
the extraction JSON.

The instance is deliberately small enough that all ten residues are individual
vocabulary tokens. It is a token-readout calibration, not a cryptographic-size
test of the benchmark's no-shortcut argument. The validation-only factors are
never rendered in the prompt.

## Compatibility checks

- Model: `deepseek-ai/DeepSeek-V4-Flash` revision
  `60d8d70770c6776ff598c94bb586a859a38244f1`.
- Model configuration: 43 blocks, width 4,096, vocabulary 129,280, FP8
  non-expert weights, FP4 expert weights.
- Lens: 42 square 4,096 x 4,096 matrices for source layers 0-41, with target
  layer 41 and an exact identity anchor at layer 41.
- Captured activation: raw post-block mHC output `[B, S, 4, 4096]`.
- Decoded lens input: `model.head.hc_head(post_block_mHC)`, producing
  `[B, S, 4096]`.
- Downstream decode: optional Jacobian transport, then the model's final RMSNorm
  and rank-sharded unembedding, globally merged.
- Matrix dimensions matched every captured residual activation.
- Final block-42 reconstruction versus the model's actual logits: maximum
  absolute error `0.0`.

The important unresolved convention is upstream of the lens matrices. The
released square checkpoint does not document the source projection from V4's
four hyper-connection streams. Applying the model's final `hc_head` at every
layer is the unique model-native 4,096-wide projection compatible with the
released matrices, but it remains an inferred convention. Final closure validates
the downstream normalization and unembedding; it cannot prove that this was the
projection used while fitting the earlier-layer Jacobians.

The released lens has no layer-42 matrix because its recorded target layer is
41. This is not a missing-file error. The viewer adds a separately labeled
`Actual L42` row by directly decoding the final block output; it never fabricates
a layer-42 J-Lens matrix.

The released J-Lens code does not include a clearly documented implementation of
the paper's sparse nonnegative J-space decomposition. No approximate replacement
was invented, and all artifacts are labeled “J-Lens token readouts.”

## Runtime and checkpoint provenance

The successful topology used two GPUs on `68.209.74.47` and two on
`68.209.74.198`, connected over their same-region private network. A four-rank
64 MiB all-reduce took approximately 0.02 seconds. The earlier cross-region SSH
overlay took approximately 20 seconds for the same smoke test, so using the
same-region hosts removed the communication bottleneck.

The original 46 Hugging Face shards total 159,617,149,040 bytes. The official
conversion produced these four model-parallel shards:

| File | Bytes | SHA-256 |
|---|---:|---|
| `model0-mp4.safetensors` | 41,985,333,352 | `2b4231563d64a926933b8cb616d07036f2ce52bf8da8d29ecf3bd97d6b51be71` |
| `model1-mp4.safetensors` | 41,985,343,384 | `dde06fd274620024e5efc5ef5efc54c3e09de6b27c0d9334e35f6a09ddb7e8d0` |
| `model2-mp4.safetensors` | 41,985,352,888 | `aec690abe32c4b2e58ea1aedbd509fb5bb6d10bfa5f5c6d8e89bd91bd96f13cd` |
| `model3-mp4.safetensors` | 41,985,352,888 | `bc8fafc063f2e42b2a71894a0406fbc4e2037df564a04351b1e016fb62de57f0` |

The lens SHA-256 is
`8b010eef8b2b08efb1b07601e5203ff5d215b1fcae63704847fdf001e61e0efc`.
The exact runtime used Python 3.10.12, PyTorch 2.10.0+cu128, Transformers 5.0.0,
TileLang 0.1.8, `apache-tvm-ffi` 0.1.3, and fast-hadamard-transform 1.1.0.
The shared working directory was `/lambda/nfs/jlens/jlens-filler-t10`.

## Reproduction

Run a two-node, two-process-per-node job over the private interface. On the first
host:

```bash
export WORK=/lambda/nfs/jlens/jlens-filler-t10
export MASTER_ADDR=172.26.133.2
export NCCL_NET=Socket NCCL_IB_DISABLE=1 NCCL_P2P_DISABLE=1
export NCCL_SOCKET_IFNAME=eno1 GLOO_SOCKET_IFNAME=eno1

torchrun --nnodes=2 --nproc-per-node=2 --node-rank=0 \
  --master-addr="$MASTER_ADDR" --master-port=29500 \
  scripts/extract_dsv4.py \
  --ckpt-path "$WORK/cache/model_mp4" \
  --model-config "$WORK/cache/model_hf/inference/config.json" \
  --reference-code-dir "$WORK/cache/model_hf/inference" \
  --lens-path "$WORK/cache/lens/lens.pt" \
  --examples-config configs/repeated_squaring_t10.json \
  --output-dir "$WORK/results/repeated_squaring_t10" \
  --phase all --layers all --top-k 10 --max-new-tokens 12 \
  --model-revision 60d8d70770c6776ff598c94bb586a859a38244f1
```

Run the same command simultaneously on the second host with `--node-rank=1`.
Before extraction, use the same distributed environment with
`scripts/distributed_smoke.py` and require all four ranks to report `passed`.

After copying the result into the local repository:

```bash
python3 scripts/build_artifacts.py \
  results/repeated-squaring-t10/repeated_squaring_n437_x12_t10.json \
  --output-dir results/repeated-squaring-t10
```

## Recommendation

The recommended T=1 through T=10 calibration has now been run on 100 matched,
shortcut-controlled examples. Dots scored 5% versus 2% without dots, but the
paired confidence interval includes zero and no T=10 example was correct. See
[`results/repeated-squaring-dot-eval/evaluation-report.md`](../results/repeated-squaring-dot-eval/evaluation-report.md)
and the selected-readout
[`summary.md`](../results/repeated-squaring-lens-selected/summary.md).

The next useful step is prompt/task calibration rather than scale: test whether a
format closer to the original benchmark can raise nontrivial T>=5 accuracy while
retaining official DeepSeek non-thinking encoding. Cross-example residualization
and a 50-100-example-per-task J-Lens comparison are not justified on the current
near-floor task performance.
