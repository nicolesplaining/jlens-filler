# Compatibility audit

## Checkpoints and code inspected

| Component | Revision / identity | Relevant facts |
|---|---|---|
| DeepSeek V4 Flash | `60d8d70770c6776ff598c94bb586a859a38244f1` | Post-trained/chat checkpoint; 43 transformer blocks; dimension 4096; 4 hyper-connection streams; vocab 129,280; FP8 non-experts and FP4 experts. |
| Workspace J-Lens | repository commit `781b233…`; file SHA-256 `8b010eef8b2b08efb1b07601e5203ff5d215b1fcae63704847fdf001e61e0efc` | Layers 0–41; 42 FP16 matrices, each 4096 × 4096; layer 41 is exactly identity; target layer 41; 25 Pile prompts; standard estimator; skip first 4 tokens; max 128 tokens. |
| Anthropic J-Lens code | `581d398613e5602a5af361e1c34d3a92ea82ba8e` | Hooks block outputs, applies the final norm and LM head after Jacobian transport. |
| Filler-token code | `4d421b541a844af88acf4bdbc8d776666ef58a82` | Five-shot two-fact prompt and `Question` / `Filler` / `Answer` scaffold reproduced. |

The model download is 159,617,149,040 bytes. The requested lens is 1,409,295,893
bytes. All paths and hashes for the specific model source files used at runtime are in
[`results/filler/runtime.json`](../results/filler/runtime.json).

## Prompt encoding

The official `encoding/encoding_dsv4.py` is used directly. `encode_messages` is called
with `thinking_mode="chat"`, which appends `</think>` immediately after the assistant
prefix and therefore selects non-thinking behavior. No Jinja chat template is assumed.

For the target prompt:

- the ten dots are exactly ten tokenizer tokens at indices 278–287;
- indices 278–286 decode as ` .`;
- index 287 decodes as ` .\n\n`, demonstrating why visible-dot counting alone is unsafe;
- `Answer:` occupies token indices 288–289;
- the assistant prefix and non-thinking terminator follow it, and the actual generation
  position is token 291 (`</think>`).

The full character offsets, token IDs, token strings, and rendered prompt are stored in
the extraction JSON.

## Activation and decoding convention

The reference model's block output is the post-block residual with shape
`[B, S, hc_mult, d_model] = [B, S, 4, 4096]`. It is not a conventional single residual
stream. The released square lens cannot directly multiply a 16,384-wide flattened raw
activation.

For each selected position and block output, this implementation performs:

1. capture the raw post-block `[4, 4096]` activation;
2. apply the model's exact `ParallelHead.hc_head` using the checkpoint's learned
   `hc_head_fn`, `hc_head_scale`, and `hc_head_base`, yielding 4096 values;
3. for J-Lens, apply `h @ J[layer].T`; for logit lens, leave `h` unchanged;
4. apply the model's final RMSNorm;
5. apply the rank-sharded unembedding and gather vocabulary logits.

Thus the implemented equations are:

```text
J-Lens:     W_U · Norm(J_l · HCHead(h_l,p))
Logit lens: W_U · Norm(      HCHead(h_l,p))
```

This matches the released generic J-Lens code's post-block hook and final
norm/unembedding order after a 4096-wide activation has been obtained.

## Passed checks

- All 42 matrices have shape 4096 × 4096 and are compatible with the collapsed
  activation.
- `J[41]` is exactly the identity matrix (maximum absolute error 0).
- On three ordinary prompts, layer-41 J-Lens and logit-lens top-10 lists are identical.
- Rebuilding logits from raw block-42 output through the exact hyper-head, final norm,
  and unembedding has maximum absolute error 0 against model logits.
- Ordinary probes become coherent late: `capital` at layer 35 and `Paris` at layers
  40–41; `42` and `北京` likewise dominate at layers 40–41.
- Token decoding was exercised on whitespace-bearing English tokens, digits, Chinese
  tokens, and subword fragments.
- Both filler and no-filler target generations are `80`.

## Unresolved lens-fit ambiguity

The lens metadata does **not** specify:

- an exact model revision;
- the dtype/quantization used while fitting;
- how the four hyper-connection streams were projected to 4096 at source layers;
- whether that projection used the final learned hyper-head at every layer.

The final hyper-head is the only model-native 4096-wide collapse compatible with the
released square matrices, so it is the narrowest defensible inference. The identity and
final-logit closure tests validate indexing and downstream decode but do not identify the
fit-time source projection. A separately released V4-Flash-0731 lens implementation uses
rectangular 4096 × 16,384 maps and hooks the raw four streams, which reinforces rather
than resolves the ambiguity for this different requested checkpoint. It was inspected as
a compatibility clue and was not substituted.

This ambiguity is the reason the run stops at the first qualitative milestone instead
of launching the 50–100-example pilot.

## Formal J-space decomposition

The inspected official `jacobian-lens` tree contains fitting, lens application, token
ranking, and visualization code. It contains no documented sparse nonnegative
decomposition/NNLS routine that expresses an activation using at most *k* J-Lens
vectors. No approximate decomposition was invented. Every delivered grid is labeled
“J-Lens token readouts.”

## Runtime issue resolved

TileLang 0.1.8 plus `apache-tvm-ffi` 0.1.2 imported but failed compiling the untouched
DeepSeek sparse-attention kernel:

```text
tvm.error.InternalError: Check failed: (condition.dtype().is_bool()) is false
```

Updating only `apache-tvm-ffi` to 0.1.3 compiled and ran the official kernel. An initial
readout implementation also used many small mixed-dtype NCCL collectives and timed out
at sequence 115. It was replaced with one ephemeral float-logit gather per readout
(about 6.2 MB for 12 positions). Exact ranks are computed on rank 0; full-vocabulary
logits are never saved. The all-layer retry completed in about 0.02 seconds per layer
for the paired readouts.

## Sources

- [DeepSeek V4 Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)
- [DeepSeek V4 J-Lens checkpoint](https://huggingface.co/camilablank/workspace-lenses/tree/main/deepseek-v4-flash/j-lens)
- [Anthropic Jacobian Lens implementation](https://github.com/anthropics/jacobian-lens)
- [Filler-token implementation](https://github.com/kaleybrauer/filler-token-reasoning)
- [Rectangular V4 lens compatibility clue](https://huggingface.co/xiangchensong/jacobian-lens-open-frontier)

