# Proposal audit and selected correct-with-filler case

## Result

The paper-matched two-fact calibration now has one complete selected example in which
filler changes the answer from wrong to correct:

- question: atomic number of Iridium (`77`) plus atomic number of Antimony (`51`);
- intended composition: `77 + 51 = 128`;
- no filler: `132` (wrong; `128` rank 6, probability 0.0304);
- 100 dots: `128` (correct; rank 1, probability 0.8871);
- tokenizer alignment: 100 visible dots map to exactly 100 model tokens at absolute
  indices 723–822;
- readouts: 42 released layers (0–41), 100 filler positions, the final `Answer:` cue
  token, and the answer-prediction token, for both J-Lens and logit lens;
- final block-42 decode closure: maximum absolute logit error `0.0`.

The self-contained viewer is
[`results/two-fact-jlens-k100-selected/two_fact_0007/viewer.html`](../results/two-fact-jlens-k100-selected/two_fact_0007/viewer.html).
It defaults to 22 sampled layers, can show all 42, and contains all 100 filler columns
and all 100-column target-rank heatmaps.

## Direct numeric readouts

These are direct single-token ranks over filler cells, before cross-example
residualization.

| Method | Target | First rank ≤10 | Best cell |
|---|---|---|---|
| J-Lens | Iridium value `77` | L35 / F43, rank 5 | L35 / F54, rank 1 |
| J-Lens | Antimony value `51` | L34 / F9, rank 1 | L34 / F9, rank 1 |
| J-Lens | sum `128` | L31 / F7, rank 7 | L38 / F8, rank 1 |
| Logit lens | Iridium value `77` | L34 / F62, rank 2 | L36 / F62, rank 1 |
| Logit lens | Antimony value `51` | L33 / F26, rank 6 | L34 / F14, rank 1 |
| Logit lens | sum `128` | L28 / F7, rank 9 | L31 / F7, rank 1 |

At the answer-prediction position in layer 41, both methods are identical because the
released `J[41]` matrix is exactly identity. Their top token is `128`; `77` is rank 10
and `51` is rank 550. The layer-41 top-10 overlaps the actual post-block-42 top-10 in
six tokens, and the actual model output is `128`.

The specific Iridium suffix token `ridium` occurs in 14 J-Lens top-10 filler cells
(first at L36/F96, rank 6; best at L38/F30, rank 1), versus two logit-lens cells
(best rank 3). The specific Antimony suffix token `imony` does not enter either top-10.
Short fragments such as `Ir` and `Ant` are frequent but too ambiguous to treat as
clean entity evidence.

## What this does and does not show

All three intended numbers become strongly decodable, and the correct answer is spread
across multiple filler positions in the late workspace band. That is promising enough
to justify a small multi-example comparison.

This example does **not** show a clean serial trace. The answer `128` reaches the
J-Lens top 10 at L31, before either addend reaches the J-Lens top 10, and the logit lens
reaches every direct target threshold at an earlier layer than J-Lens. The result is
therefore evidence of decodability, not evidence that J-Lens uniquely reveals the
computation or that the decoded cells are causally necessary. With 4,200 filler cells
per target (42 × 100), a best-rank hit is also a selected extreme; shuffled controls,
cross-example residualization, and replication are necessary before making a stronger
claim.

Other interpretation concerns remain:

- the released square lens omits the exact four-stream mHC source projection; the
  extraction uses the model's only native 4096-wide `hc_head` collapse, an inferred
  convention documented in the compatibility audit;
- the lens covers 0–41 but not model block 42, so actual final logits are displayed as
  a separate row rather than mislabeled as another lens layer;
- this case was selected from the same behavioral sweep because filler makes it
  correct, so it is qualitative evidence, not an unbiased effect estimate;
- late readouts include unrelated element/category tokens and other noise, so isolated
  semantic top tokens should not be narrated as literal thoughts.

## Released-tooling audit against the proposal

The official `anthropics/jacobian-lens` repository was inspected at commit
`581d398613e5602a5af361e1c34d3a92ea82ba8e`. Its public package exports activation
recording, average-Jacobian fitting, matrix transport/application, the Hugging Face
adapter, and the interactive slice renderer. The requested Hugging Face lens directory
currently contains one file, `lens.pt`; it does not contain a tuned lens or auxiliary
intervention weights.

| Proposed component | Released support | Decision |
|---|---|---|
| Basic logit lens | Yes: official `apply(..., use_jacobian=False)` convention | Implemented with the same captured activations and final norm/unembedding |
| Pretrained J-Lens readout | Yes: `J_l h`, final norm, unembedding | Implemented |
| Tuned lens | No compatible artifact or official implementation in the inspected release | Omitted; no fitting or silent substitution |
| Answer-targeted J-Lens | Would require fitting a new lens | Not run, per the experiment constraint |
| Sparse nonnegative formal J-space decomposition | Described in the paper, but no NNLS/sparse-decomposition API or routine is released | Deferred; outputs remain labeled “J-Lens token readouts” |
| Coordinate swap / clamping | Experiment READMEs describe the operation, but the released package has no clamping/intervention implementation | Deferred rather than reverse-engineered |
| Entity-versus-value coordinate swaps | Depends on the absent coordinate intervention | Deferred |
| J-space-only ablation | Depends on the absent formal decomposition/coordinate basis | Deferred |
| Broadcast-head/circuit tooling | No head-attribution or broadcast analysis implementation in the release | Deferred |
| Direct residual activation patching | Technically possible with the verified model hooks and permitted by the original pilot scope, but distinct from a formal J-space coordinate swap | Viable next causal pilot, to be labeled separately |

The paper's intervention descriptions are scientifically informative, but prose and
released prompt datasets are not a tested API. Implementing an unofficial coordinate
solver here would violate the requirement not to invent an approximate J-space
decomposition.

## Reproduction artifacts

- Config: [`configs/two_fact_jlens_selected_k100.json`](../configs/two_fact_jlens_selected_k100.json)
- Full extraction: [`results/two-fact-jlens-k100-selected/two_fact_0007.json`](../results/two-fact-jlens-k100-selected/two_fact_0007.json)
- Interactive viewer: [`results/two-fact-jlens-k100-selected/two_fact_0007/viewer.html`](../results/two-fact-jlens-k100-selected/two_fact_0007/viewer.html)
- Complete per-cell JSONL: [`results/two-fact-jlens-k100-selected/two_fact_0007/readouts.jsonl`](../results/two-fact-jlens-k100-selected/two_fact_0007/readouts.jsonl)
- Filler-position Markdown report: [`results/two-fact-jlens-k100-selected/two_fact_0007/qualitative-report.md`](../results/two-fact-jlens-k100-selected/two_fact_0007/qualitative-report.md)
- Runtime versions and hashes: [`results/two-fact-jlens-k100-selected/runtime.json`](../results/two-fact-jlens-k100-selected/runtime.json)
- Sanity gate: [`results/two-fact-jlens-k100-selected/sanity_gate.json`](../results/two-fact-jlens-k100-selected/sanity_gate.json)

## Primary references

- [Official J-Lens implementation](https://github.com/anthropics/jacobian-lens)
- [J-Lens paper](https://transformer-circuits.pub/2026/workspace/index.html)
- [Released DeepSeek V4 Flash lens](https://huggingface.co/camilablank/workspace-lenses/tree/main/deepseek-v4-flash/j-lens)
- [Filler-token paper](https://arxiv.org/html/2607.03502v1)
