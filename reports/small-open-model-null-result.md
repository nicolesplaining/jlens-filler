# Filler tokens on open models up to 35B: a null result

## Bottom line

On the released variable-binding items where DeepSeek V4 Flash goes from 70% to
98% with 50 post-question dots, ten open models from 4B to 35B parameters, three
families, dense and MoE, score 0–14% at every filler length, in either placement,
with no placement-specific gain. Those tested with chain-of-thought solve the task
(Qwen3.5-9B 3/3, Llama-3.1-8B-Instruct 4/5, Qwen3.5-27B 5/5), so the capability
exists but not in direct-answer mode, and there is no partial circuit for filler to
amplify.

On a new one-step variant that puts the same models at 50–85% baseline, dots
still do nothing. A 200-item held-out replication on Qwen3.5-4B shows every
positive length within ±3 correct of baseline with helped ≈ hurt, and the
pre-question placement control is slightly negative (4 helped / 12 hurt).

Whatever DeepSeek V4 Flash is doing with filler positions, none of these models
does it, even in the accuracy band where a workspace effect would be visible.
Per Nicole's finding that the J-Lens exposed nothing the logit lens did not on
DeepSeek, the screen used no lens at all; it is purely behavioral.

## Models, lenses, harness

| Model | Weights used | Lens available | Number tokenization |
|---|---|---|---|
| Qwen3.5-4B | `Qwen/Qwen3.5-4B` | camilablank/workspace-lenses (same fitter/recipe as the DeepSeek lens) | single digits |
| Qwen3.5-9B | `Qwen/Qwen3.5-9B` | camilablank/workspace-lenses | single digits |
| Llama-3.1-8B-Instruct | `unsloth/Llama-3.1-8B-Instruct` mirror of the gated Meta checkpoint | neuronpedia/jacobian-lens (461 WikiText-103 prompts, bf16) | up to 3 digits per token |
| Qwen3.5-27B | `Qwen/Qwen3.5-27B` (64 layers, d=5120, bf16 on one H100 80GB) | camilablank/workspace-lenses | single digits |

`scripts/extract_hf.py` is a single-GPU Transformers port of the behavioral
`eval` phase of `extract_dsv4.py`. It reuses `prompts.py`, the config format,
and the `filler_length_sweep.json` schema, so `analyze_behavior_sweep.py` runs
unchanged. Rendering goes through each model's own `apply_chat_template`
(Qwen: `enable_thinking=False`, which emits an empty `<think></think>` block;
Llama: the template inserts its "Cutting Knowledge Date" preamble into the
system turn). Greedy decoding, `max_new_tokens=3`, bf16, one A100 40GB.

Because Qwen splits numbers into single digits, `target.best_rank` in the Qwen
result files is the rank of the answer's *first digit* and `best_log_probability`
is the teacher-forced log-probability of the whole answer. For Llama, three-digit
answers are single tokens and the rank is the ordinary one. No lens readouts
were extracted: the behavior gate (`reports/algorithm-exploration-findings.md`,
"Behavior-first inclusion gate") was never met.

Harness checks that passed before trusting any number: dot count equals filler
token count at every k for both tokenizers (the last Llama dot merges into
` .\n\n` exactly as on DeepSeek; Qwen dots do not merge); greedy runs are
bit-identical across repeats; KV-cached decode logits differ from full recompute
by at most 0.125 in bf16 with identical argmax; plain prompts are coherent;
`tests/test_prompts.py` passes on the box.

## Released two-step items (`configs/varbind_easy_dot_length_sweep.json`, n=50)

Correct out of 50. Placement control is 50 dots before the definitions/question.

| Model | k=0 | k=5 | k=10 | k=25 | k=50 | k=100 | pre-question k=50 | with CoT |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| DeepSeek V4 Flash (Nicole) | 35 | | | | 49 | 49 | 35 | |
| Qwen3.5-4B | 1 | 0 | 1 | 0 | 2 | 1 | 0 | |
| Qwen3.5-9B | 0 | 2 | 1 | 1 | 2 | 1 | 0 | 3/3 |
| Llama-3.1-8B-Instruct | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4/5 |
| Qwen3.5-27B | 4 | 3 | 3 | 5 | 3 | 2 | 2 | 5/5 |

Qwen3.5-9B on the depth-1 branching set (`configs/branching_varbind_dot_length_sweep.json`,
n=36, DeepSeek 34/36): 0/36 at k=0, 5, 10, 25, 50.

Error pattern (`scripts/error_breakdown_sweep.py`): outputs are clean three-digit
numbers, not parse failures. Qwen models mostly emit a wrong number of the right
magnitude and equal a named intermediate (usually the bound value) in only 1–3
of 50 cases per condition. Llama stalls at the bound value in 8–12 of 50 and is
otherwise far off. Dots change the emitted answer in 40–44 of 50 examples for
every model, so filler is not inert; it perturbs without steering.

Qwen3.5-27B is closer without being right. Its median absolute error is 8–10
(versus 31–52 for the 9B), 26–30 of 50 outputs land within 10 of the answer, and
2–3 per condition equal the second product exactly. Dots do not move any of
this: mean log p(correct) changes by at most +0.08 nats (sign-test p ≥ 0.06),
expected pass@20 at temperature 1 is 0.47 without dots and 0.47–0.50 with them,
and at k=100 the output is closer to the answer than at k=0 for 18 items and
farther for 14 (p=0.60). For the plain prompt "2·97−21, then twice that plus 28"
it answers `370` (correct: 374).

Direct plain-arithmetic probes on the smaller models agree: Qwen3.5-9B answers `2·97−21 = 173`
correctly but gives `186` for "then twice that plus 28" (correct: 374). Llama
starts writing prose for the two-step version.

## Screen around 30B (`scripts/screen_models.sh`)

Seven more models on one H100 80GB in bf16, same three configs. Correct out of 50.
"Best dots" is the best of k=5,10,25,50,100 with helped/hurt versus k=0.

| Model | Type | k=0 | best dots | pre-question k=50 |
|---|---|---:|---:|---:|
| Qwen3.5-27B | dense | 4 | 5 (k=25, 3/2) | 2 |
| Qwen3.5-35B-A3B | MoE, 3B active | 3 | 4 (k=50, 1/0) | 4 |
| Qwen3.6-27B | dense | 4 | 7 (k=10, 4/1) | 5 |
| Qwen3-32B | dense | 4 | 1 (k=10, 0/3) | 1 |
| Qwen3-30B-A3B | MoE, 3B active | 5 | 5 (k=10, 0/0) | 5 |
| Gemma-3-27B-IT (unsloth mirror) | dense | 2 | 3 (k=25, 1/0) | 2 |
| OLMo-3.1-32B-Instruct | dense | 1 | 1 (k=5, 0/0) | 1 |

Smallest exact McNemar p across all 35 model × length cells is 0.125 (Qwen3-32B,
dots hurting). Qwen3-32B and Qwen3-30B-A3B get worse with dots in both placements.

One-step items, same models: all at or near ceiling and flat.

| Model | k=0 | best dots | worst dots |
|---|---:|---:|---:|
| Qwen3.5-27B | 50 | 50 | 50 |
| Qwen3.5-35B-A3B | 49 | 49 | 49 |
| Qwen3.6-27B | 50 | 50 | 50 |
| Qwen3-32B | 45 | 47 (k=50, 2/0) | 43 |
| Qwen3-30B-A3B | 48 | 48 | 47 |
| Gemma-3-27B-IT | 49 | 49 | 48 |
| OLMo-3.1-32B-Instruct | 41 | 42 (k=100, 2/1) | 38 |

Paired log-probability of the correct answer is the sensitive endpoint. Best mean
shift across dot lengths versus the pre-question control at k=50:

| Model | best post-question Δ log p | pre-question Δ log p |
|---|---:|---:|
| Qwen3.5-27B | +0.08 (k=100, 29/21, p=0.32) | −0.09 (25/25) |
| Qwen3.5-35B-A3B | +0.00 (k=50, 28/22) | +0.33 (30/20) |
| Qwen3.6-27B | +0.13 (k=25, 27/23, p=0.67) | −0.05 (23/27) |
| Qwen3-32B | +0.95 (k=50, 27/23, p=0.67) | +0.05 (26/24) |
| Qwen3-30B-A3B | −0.12 (k=50, 23/27) | −0.11 (23/27) |
| Gemma-3-27B-IT | +1.22 (k=10, 30/20, p=0.20) | +3.08 (40/10) |
| OLMo-3.1-32B-Instruct | +1.25 (k=100, 36/14, p=0.003) | +0.75 (30/20) |

Gemma's post-question gain is smaller than its pre-question gain, so it is a
generic more-context effect. OLMo at k=100 is the only cell with a placement-
specific log-probability increase (about +0.5 nats net); its accuracy stays 1/50,
the correct answer's median rank moves from 66 to 56, and expected pass@20 at
temperature 1 moves from 0.10 to 0.14. It is a whisper, not a usable effect.

## One-step items (`scripts/build_onestep_varbind_configs.py`)

Same scaffold, five definitions, derived-expression distractors that reference a
different literal, but the queried variable is a literal, so the answer needs one
hidden step (`base → coefficient·base → answer`). Seed 90211, 50 items and 5
disjoint few-shots.

| Model | k=0 | k=5 | k=10 | k=25 | k=50 | k=100 | pre-question k=50 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Qwen3.5-4B | 37 | 42 (6/1) | 38 (3/2) | 36 (3/4) | 40 (6/3) | 41 (5/1) | 39 (4/2) |
| Qwen3.5-9B | 41 | 41 (1/1) | 44 (4/1) | 41 (2/2) | 42 (3/2) | 41 (1/1) | 43 (2/0) |
| Llama-3.1-8B-Instruct | 26 | 25 (1/2) | 26 (2/2) | 26 (3/3) | 24 (2/4) | 26 (4/4) | 29 (3/0) |

Parentheses: helped / hurt versus k=0. Smallest exact McNemar p is 0.125
(Qwen3.5-4B, k=5), one of five lengths tested.

### Held-out replication, Qwen3.5-4B, n=200 (seed 551177, disjoint)

| k | Correct | Helped / hurt | p |
|---:|---:|---:|---:|
| 0 | 147 | | |
| 5 | 145 | 5 / 7 | 0.77 |
| 10 | 142 | 5 / 10 | 0.30 |
| 25 | 150 | 9 / 6 | 0.61 |
| 50 | 144 | 6 / 9 | 0.61 |
| 100 | 149 | 9 / 7 | 0.80 |
| 50, pre-question | 139 | 4 / 12 | 0.077 |

The k=5 bump from the 50-item set does not replicate.

## Training a model to use dots: chain-length 1 (`scripts/train_varbind_lora.py`)

LoRA (r=32, all linear layers, lr 1e-4, 500 steps, effective batch 16) on
Qwen3.5-9B with 4,000 synthetic chain-length-1 items (`scripts/build_varbind_sft_data.py`,
distribution matched to the released set, released items excluded). Each item
is rendered at one dot count drawn uniformly from k ∈ {0, 5, 10, 25, 50, 100}
and only the answer tokens carry loss. Evaluated every 100 steps on the
released 50 items at all k plus the pre-question control. Correct out of 50:

| step | k=0 | k=5 | k=10 | k=25 | k=50 | k=100 | pre-question k=50 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 2 | 1 | 2 | 1 | 0 | 1 |
| 100 | 9 | 14 | 11 | 12 | 11 | 13 | 9 |
| 200 | 14 | 14 | 16 | 15 | 13 | 15 | 14 |
| 300 | 28 | 30 | 29 | 28 | 27 | 29 | 30 |
| 400 | 39 | 37 | 37 | 39 | 37 | 38 | 34 |
| 500 | 36 | 37 | 36 | 37 | 38 | 37 | 39 |

The model learns the task (0% → 72–78%) but learns it as a direct computation:
after step 100 the dot conditions never lead k=0 by more than one item, and the
pre-question control matches or beats post-question dots. A transient lead at
step 100 (k=0 9 versus dots 11–14, control 9) closes by step 200. A 9B model
fits the two-step chain in one forward pass, so mixed-k supervision gives it no
reason to route computation through the dots. Records: `results/qwen3.5-9b/lora-mixedk/`.

The follow-up increases the hidden chain to length 2 (three sequential affine
steps, `data/varbind_c2_sft_train.jsonl`, held-out eval `configs/varbind_c2_heldout_dot_length_sweep.json`)
on the premise that dot dependence can only emerge where the direct computation
no longer fits.

### Chain-length 2, same recipe

4,000 synthetic chain-length-2 items (three sequential affine steps), evaluated
on 50 held-out chain-length-2 items (`configs/varbind_c2_heldout_dot_length_sweep.json`):

| step | k=0 | k=5 | k=10 | k=25 | k=50 | k=100 | pre-question k=50 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 100 | 3 | 4 | 4 | 1 | 2 | 2 | 2 |
| 200 | 3 | 3 | 3 | 2 | 2 | 1 | 4 |
| 300 | 7 | 9 | 9 | 10 | 9 | 9 | 9 |
| 400 | 11 | 11 | 11 | 11 | 12 | 8 | 13 |
| 500 | 9 | 11 | 13 | 13 | 13 | 14 | 16 |

Slower learning (final 18–28%), and the only dot effect is a context-length one:
at step 500 post-question dots add 2–5 items (helped/hurt 4–7 / 2) while
pre-question dots add 7 (10 / 3). Records: `results/qwen3.5-9b/lora-c2-mixedk/`.

Two follow-ups are queued. A capacity-limited model (Qwen3.5-4B) on chain-length 1,
where the direct two-step circuit may not fit in one pass. And a paired design on
Qwen3.5-9B chain-length 1: one model trained only with dots (k ∈ {25, 50, 100})
and one only without (k = 0), both evaluated at every k. If the dots-only model
collapses at k=0 while the k=0 model survives at k=50, the computation moved into
the dot positions and that model is the lens target.

### Paired design: dots-only versus k=0-only (and a 4B control)

Same recipe, three more runs. Correct out of 50 released items at step 500:

| Model | trained on | k=0 | k=5 | k=10 | k=25 | k=50 | k=100 | pre-question k=50 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Qwen3.5-4B | mixed k | 36 | 38 | 36 | 37 | 36 | 34 | 38 |
| Qwen3.5-9B | dots only, k ∈ {25, 50, 100} | **40** | 42 | 39 | 41 | 40 | 40 | 39 |
| Qwen3.5-9B | k = 0 only | 36 | 33 | 31 | 33 | **26** | 28 | 38 |

The dots-only model never saw a prompt without dots and scores 40/50 without
them. The computation it learned lives entirely outside the dot positions. The
k=0-only model is the mirror image: post-question dots cost it 10 items at k=50
(4 helped, 14 hurt) while pre-question dots cost nothing, so unfamiliar tokens
between the question and the answer cue disrupt an answer-position computation.
Records: `results/qwen3.5-4b/lora-mixedk/`, `results/qwen3.5-9b/lora-dotsonly/`,
`results/qwen3.5-9b/lora-k0only/`.

### Causal test: are the dot positions used at all? (`scripts/patch_varbind_hf.py --lesion-all-dots`)

Replace every filler residual with its mean over filler positions (or with
zeros), at every decoder block simultaneously, so no later block can re-read
pre-lesion dot content. Teacher-forced log-probability of the correct answer
and the greedy output before and after, 50 dots:

| Model | items | lesion | median Δ log p | range | greedy changed | correct before → after |
|---|---:|---|---:|---|---:|---:|
| dots-only | 12 correct at k=50 | mean | −0.02 | −0.17 … +0.20 | 1/12 | 11 → 12 |
| dots-only | same | zero | −0.09 | −0.65 … +0.45 | 2/12 | 11 → 11 |
| k=0-only at k=50 | 10 hurt by dots + 6 not | mean | +0.04 | −1.00 … +0.98 | 4/16 | 5 → 8 |
| k=0-only at k=50 | same | zero | −0.03 | −2.52 … +1.05 | 8/16 | 5 → 7 |

In the dots-only model the dot positions are causally inert: wiping all 50 of
them at all 32 blocks leaves 11–12 of 12 answers unchanged and moves confidence
by hundredths of a nat. The k=0-only model shows the same intervention has
teeth: there, dot content is live (as interference) and removing it repairs
wrong answers. A single-layer version on one item (`lesion-varbind_easy_0010/`)
gives the same picture layer by layer (max |Δ log p| 0.12).

Two caveats. Qwen3.5 alternates Gated DeltaNet (linear attention) blocks with
full attention; in the recurrent blocks the dot positions are recurrence steps
between question and answer, so a structural "extra compute" from dots exists
regardless of content. The lesions remove content, not steps. And one item
(`varbind_easy_0003`, p ≈ 0.48 for the answer) flips between correct and
incorrect across the merged-adapter and unmerged evaluations; it is a coin flip,
not a lesion effect.

Read together with the behavioral tables: SFT with dots present, even dots-only,
teaches a 9B model to solve the chain at the answer position and to ignore the
dots. Nothing in this training regime induces the workspace behavior DeepSeek V4
Flash shows natively.

### Single-cell patching on an exact-layout held-out pair (`patch_varbind_hf.py`)

From held-out item 0067 (`ruw = 43 → 99 → 198 → 203`) the one-digit
counterfactual `ruw = 13 → 39 → 78 → 83` differs at exactly one prompt token.
The dots-only model answers all 18 family members correctly at k=50 except two
near-misses. Donor (13) dot residuals were patched one cell at a time into the
target (43) prompt over all 32 blocks × 50 dots, measuring the donor answer 83
and the target answer 203 by teacher-forced log-probability. Identity closure 0.0.

| Model | cells | donor answer: base log p | best single-cell Δ | cells ≥ +1 nat | target answer: worst Δ |
|---|---:|---:|---:|---:|---:|
| dots-only | 1,600 | −20.5 (rank 17) | +0.88 (L27/F8) | 0 | −0.03 |
| k=0-only | 1,600 | −21.3 (rank 97) | +0.75 (L27/F3) | 0 | −0.02 |

For comparison, Nicole's exact-layout pair on DeepSeek V4 Flash gave single
cells worth +4.9 nats and 16-cell doses that moved the counterfactual answer
from rank 82 to rank 2. Here the strongest cell leaves the donor answer at
roughly e⁻²⁰ and the target answer untouched. The only structure is a weak band
at blocks 19–27 where the best cells reach +0.6 to +0.9 nats (blocks 0–18 top
out at +0.2), matching the faint late-layer leak seen in the lens grids: some
answer-correlated signal exists in late dot residuals, but nothing downstream
depends on it. Records: `results/qwen3.5-9b/patch-heldout-0067/`.

## Logit-lens grids on held-out items (`extract_hf.py --phase filler`)

Eight held-out items at k=50 (`configs/varbind_heldout_lens_dotsonly_k50.json`:
the 5 items the dots-only model gets right only with dots, plus 3 it gets right
either way with distinct stage first digits), each with Nicole's stage-matched
derangement controls. Grids over all 32 blocks × 50 dots + answer cue + generation
position, for the dots-only model, the k=0-only model, and the untrained base.
Final-block closure error is 0.0 for every grid. Viewers and per-example reports
are under `results/qwen3.5-9b/lens-heldout-k50/<model>/<item>/`; summaries in
`.../<model>/analysis/`.

Because Qwen tokenizes digits singly, a cell can only be scored on a stage's
*first digit*; the deranged controls are the yardstick for what that coarse
readout shows by chance.

**The dot positions carry nothing stage-specific.** Mean difference in log p
between the true stage digit and its control digit over all filler cells:

| Stage | dots-only late third | k=0-only late third | base late third |
|---|---:|---:|---:|
| base_value | +0.07 | −0.04 | +0.20 |
| bound_value | −0.10 | +0.01 | +0.06 |
| second_product | +0.34 | +0.60 | +0.01 |
| answer | +0.12 | +0.36 | +0.01 |

Early and middle thirds are within ±0.03 for every stage and model. The only
signal is a faint late-layer leak of the product/answer digits into the dots,
and it is *larger in the k=0-only model* (where dots are out-of-distribution and
hurt) than in the dots-only model. Rank-1 hits for true stage digits in filler
cells (≤3 of 8 examples, ≤0.9 of 1,600 cells) match the control labels.

**The dots decode to dots.** Top-1 tokens at filler cells are digits in 0.0% of
early/mid cells and 0.2% (dots-only) to 1.0% (k=0-only, base) of late cells; the
most common late top-1 is the dot token ` .` itself, then non-Latin junk.

**The computation resolves at the answer position, late.** Dots-only model,
generation position: the answer's first digit is rank 1 at layer 30 of 32 in 8/8
items, the second product at layer 30 in 5/8; at the answer-cue token both reach
rank ≤ 10 at layer 27 in 5–7/8. No stage becomes decodable anywhere before the
last six blocks. There is no depth ladder across dot positions to compare with
Nicole's DeepSeek result because nothing is staged in the dots at all.

Read with the all-layer lesions above, this is the mechanistic answer to the
training question: the model trained only with dots present solves the chain in
the final blocks at the answer positions, leaves the dot residuals representing
"a dot", and neither writes to nor reads from them.

## What a dot position is doing (`dump_dot_residuals_hf.py`, `analyze_dot_residuals.py`)

One eager-attention pass per item over the 100 held-out problems at k=50, for the
base model, the dots-only model, and the k=0-only model, recording every block's
residual at all 50 dots, the last question token, the answer cue, and the
generation position, plus attention mass by prompt region in the 8 full-attention
blocks. Tables and figures: `results/qwen3.5-9b/dot-dump/analysis/` (the 1.4 GB
residual dumps stay on the compute box).

**1. A dot residual is almost entirely "I am dot number k".** Variance of dot
residuals split by source, and cosine similarity of the same dot position across
different problems:

| Model | block | var. explained by position | by problem | cos, same position, different problems |
|---|---:|---:|---:|---:|
| base | 16 / 24 / 31 | 0.69 / 0.51 / 0.48 | 0.01 / 0.01 / 0.02 | 0.92 / 0.83 / 0.81 |
| dots-only | 16 / 24 / 31 | 0.88 / 0.74 / 0.60 | 0.01 / 0.02 / 0.05 | 0.99 / 0.99 / 0.97 |
| k=0-only | 16 / 24 / 31 | 0.82 / 0.63 / 0.46 | 0.01 / 0.06 / 0.10 | 0.98 / 0.88 / 0.88 |

Problem identity accounts for 1–5% of dot-residual variance in the dots-only
model. Training with dots made the dots *more* problem-independent than in the
base model (cosine 0.97 vs 0.81 at the last block); training without dots left
them less so (0.88) and gave problem identity its largest share (10%).

**2. The small problem-dependent part is a selective, linearly readable copy of
the relevant numbers.** Ridge probes (5-fold CV over items, R²) from the mean dot
residual, versus from the answer-cue residual, best block in parentheses:

| Model | target | from dots | from answer cue |
|---|---|---:|---:|
| dots-only | queried chain's base literal | 0.98 (L21) | 0.99 (L21) |
| dots-only | chain constant / question constant | 0.92 / 0.96 | 0.96 / 0.99 |
| dots-only | answer | 0.97 (L21) | 0.99 (L26) |
| dots-only | **distractor literal (visible, irrelevant)** | **0.44 at L13, ≤ 0.06 after L20** | ≤ 0.33, negative after L20 |
| k=0-only | queried base / answer / distractor | 0.97 / 0.97 / ≤ 0.35 | 0.99 / 0.99 / ≤ 0.28 |
| base | queried base / answer / distractor | 0.43 / 0.45 / ≤ 0.02 | 0.77 / 0.82 / ≤ 0.22 |
| any | shuffled-label control | ≤ −0.16 | ≤ −0.17 |

So the dots do carry the problem: the queried variable's base and the constants
on its chain are decodable at R² 0.9+, and a visible literal that is *not* on the
chain is not. That is variable-binding resolution reflected in the dot residuals.
Two qualifications. On an affine task a linear probe cannot distinguish stored
inputs from a computed answer, since the answer is a linear function of the
inputs, so "answer R² 0.97" is not evidence the dots computed anything. And the
same information is present, more cleanly, at the answer cue in every model.
Combined with the lesions, the picture is a faint redundant copy that nothing
downstream reads. Fine-tuning on the task sharpened this copy everywhere (base
0.43 → 0.97) whether or not dots were in the training prompts.

**3. The answer positions do not look at the dots, and training with dots taught
the model to look away.** Attention mass on the dot region, mean over heads
(full-attention blocks; figure `attention_heatmaps.png`):

| query | block | base | dots-only | k=0-only |
|---|---:|---:|---:|---:|
| generation position | 19 / 23 / 27 / 31 | 0.05 / 0.03 / 0.01 / 0.01 | 0.02 / 0.04 / 0.01 / 0.01 | 0.02 / 0.12 / 0.06 / 0.03 |
| answer cue | 19 / 23 / 27 / 31 | 0.05 / **0.18** / 0.06 / 0.03 | 0.01 / 0.04 / 0.03 / 0.03 | 0.02 / 0.13 / 0.08 / 0.05 |
| max single head, gen → dots | 23 | 0.18 | 0.08 | 0.24 |

The dots-only model's answer positions put 1–4% of attention on the 50 dots, in
every full-attention block, versus 18% (cue) in the base and 12–13% in the model
that never saw dots and is hurt by them. The dots themselves attend mostly to
the few-shot demonstrations (0.5–0.84 of mass), then to each other (0.20–0.28 at
the last block), and to the target problem only in the middle blocks (0.37 peak
at block 11 in the dots-only model). Caveat: 24 of 32 blocks are Gated DeltaNet
and have no attention matrix; there the dots are recurrence steps regardless.

**4. The dots are processed, toward predicting the next dot.** Logit-lens entropy
at dot positions falls from 11.2 nats (block 0) to 0.02 nats (block 31) in the
dots-only model, versus 0.14 at the generation position; residual norms grow
along the same curve as content tokens. Each dot spends its depth becoming
certain that the next token is a dot.

**Summary.** A dot position in the fine-tuned model holds a dominant
position-identity vector, a faint linear copy of the queried chain's numbers
(present more strongly at the answer cue), attends to the demonstrations and to
other dots rather than to the problem, receives 1–4% of the answer positions'
attention, and predicts "dot". Fine-tuning with dots present made the dots
*more* uniform and *less* attended than in the base model. This is the
opposite of a workspace: the model learned to route around the dots. It also
explains the k=0-only model's interference: without that training, the answer
cue attends to dot content 3–4× more, and that content is out-of-distribution.

## The same anatomy on DeepSeek V4 Flash (`dump_dot_residuals_dsv4.py`, `dump_dot_attention_dsv4.py`)

Run on a 4×H100 box with Nicole's converted checkpoint (sanity gate passed:
closure and lens-identity anchor exact). Fifty held-out items at k=50, every
block's raw four-stream residual at all 50 dots, the last question token, the
answer cue, and the generation position; attention recomputed from q, k, the
indexer's selection, and the per-head sink for every block, since the fused
sparse-attention kernel returns no weights. Tables and figures in
`results/deepseek-v4-flash/dot-dump/analysis/`.

Two architecture facts frame the attention numbers. Every V4 block attends to a
128-token sliding window of raw keys plus compressed keys (4-token blocks chosen
by a learned indexer in even blocks 2–40, 128-token blocks in odd blocks 3–41;
blocks 0, 1, 42 are window-only). At our prompt lengths the indexer's top-512 is
every block, so sparsity never bites. For the answer positions the dots are
about 40% of the raw window keys; the demonstrations and most of the problem are
reachable only through compressed keys.

**DeepSeek's answer positions look at the dots; Qwen's do not.** Mean attention
mass on the dot region over the last third of blocks, and the single most
dot-attentive head at the generation position:

| Model | gen → dots | cue → dots | dots → dots | max head, gen → dots |
|---|---:|---:|---:|---:|
| Qwen3.5-9B base | 0.010 | 0.046 | 0.13 | 0.18 |
| Qwen3.5-9B dots-only | 0.009 | 0.029 | 0.14 | 0.09 |
| Qwen3.5-9B k=0-only | 0.043 | 0.067 | 0.18 | 0.24 |
| **DeepSeek V4 Flash** | **0.164** | **0.195** | **0.26** | **0.90** |

DeepSeek puts 20% or more of the generation position's attention on the dots in
blocks 21, 22, 24, 35, 39, and 40 (peak 0.35 at block 40), and of the answer
cue's attention in fourteen blocks (peak 0.43 at block 39). Heads reaching 0.5
to 0.9 of their mass on dots appear in blocks 26 to 40. The dots attend to each
other at 0.30 to 0.48 in blocks 33 to 42. The window makes dots cheap to reach,
but Qwen had every token in reach and spent 1 to 4% on them; DeepSeek spends 16
to 43% in the blocks where Nicole's lens saw the ladder resolve.

**DeepSeek's dot residuals are more problem-specific than the trained Qwen's.**
Cosine of the same dot position across different problems at three-quarters
depth: 0.78 (DeepSeek) versus 0.99 (Qwen dots-only), 0.88 (Qwen k=0-only),
0.83 (Qwen base). The problem explains 4 to 5% of dot-residual variance in the
late blocks (Qwen dots-only 2%).

**The streams divide the work.** Per hyper-connection stream at blocks 32 / 40:

| stream | var. by problem | cos, same dot, other problems | norm at dots (block 40) |
|---|---:|---:|---:|
| 0 | 0.06 / 0.09 | 0.51 / 0.61 | 186 |
| 1 | 0.03 / 0.03 | 0.68 / 0.79 | 286 |
| 2 | 0.09 / 0.10 | 0.48 / 0.64 | 273 |
| 3 | 0.02 / 0.05 | 0.88 / 0.76 | 49 |

Streams 0 and 2 carry the problem-specific content (cosine near 0.5, a tenth of
variance from problem identity); stream 3 is the position-identity lane (cosine
0.88, small norm until the last blocks); stream 1 is the high-norm carrier with
little problem dependence. This is the first direct look at what the four lanes
do at a filler position, and it matches the guess that width lets a value be
stored without overwriting the position's own state.

**Where the answer is computed differs.** Best ridge probe R² for the answer:

| Model | from dots (mean) | from last question token | from answer cue |
|---|---:|---:|---:|
| Qwen3.5-9B dots-only | 0.97 | 0.94 | 0.99 |
| DeepSeek V4 Flash | 0.87 | **0.40** | 0.87 |

In the trained Qwen the answer is already linearly present at the last question
token, before any dot exists; the dots and the cue only repeat it. In DeepSeek
the question token barely encodes it (0.40) and the dots encode it as well as the
answer cue does (0.87), consistent with the computation happening across the
dot span rather than at the question. The affine-probe caveat from the Qwen
section applies to the absolute values, not to this contrast.

**The dots change character at block 19.** Logit-lens entropy at dot positions
(through Nicole's collapse) is 0.2 to 1.5 nats in blocks 0 to 18, jumps to 5.9
at block 19, and declines to 0 by block 42. Qwen's dots start at 11 nats and only
fall at the end. Whatever the early-block readout means under the collapse, the
discontinuity at block 19 coincides with the blocks where attention to dots first
exceeds 20% (21, 22, 24).

**Summary.** On the model that shows the behavioral effect, the dot positions are
attended (16 to 43% late-block mass from the answer positions, single heads up to
0.9), problem-specific (cosine 0.78 across problems versus 0.99 in the trained
Qwen), organized by stream (two content lanes, one position lane, one carrier),
and hold the answer as strongly as the cue does while the question token does
not. Every one of those is the opposite of what the fine-tuned Qwen showed.

## What this does and does not show

On the training phase: five LoRA runs (mixed-k, chain-length 2, a 4B model,
dots-only, k=0-only) all produce models that solve the chain at the answer
position and treat the dot positions as inert, verified on held-out items by
logit-lens grids with derangement controls, all-layer dot lesions with a positive
control, and a 1,600-cell single-cell patch grid on an exact-layout pair. This
establishes that answer-only SFT with dots present does not induce workspace use
in Qwen3.5 up to 9B. It does not establish that no training recipe can: dense
supervision on intermediate values placed in the dots, a task where a single
forward pass provably cannot fit the computation, or reinforcement with a compute
penalty are untested here. The digit-split tokenizer limits per-cell readouts to
first digits; the control comparison bounds how much that could hide.


It shows that ten open models from 4B to 35B, dense and MoE, across Qwen, Llama,
Gemma, and OLMo, do not exhibit the filler effect on the released two-step task
(all at floor, the ~30B models nearly right but not right), and none does on a
matched one-step task (mid-range for the small models, ceiling for the large),
with the same prompt scaffold, the same exact-count filler instruction, and
placement controls. It does not identify why DeepSeek V4 Flash differs. Scale,
post-training, the MoE routing, and the four-stream hyper-connection residual are
all confounded here. The Llama weights are a mirror of the gated Meta checkpoint,
not the checkpoint the lens was fit on; that does not affect the behavioral
numbers but would matter for readouts.

The screen rules out the cheap explanations. Two MoE models with 3B active
parameters behave like the dense ones, so MoE routing alone is not it. Four
families with different post-training behave alike, so it is not a Qwen quirk.
Scale from 4B to 35B brings the direct-answer output closer to correct without
ever producing a filler gain. What remains: a scale threshold above 35B, the
four-stream hyper-connection residual specific to DeepSeek V4, or something in
DeepSeek's post-training. None of these is testable on one 80GB card with an
open model.

The next step is therefore to make a model that uses filler: fine-tune one of
these (Qwen3.5-9B or Qwen3.6-27B with LoRA) on the two-step task with dots present
until dots measurably help, then run Nicole's causal ladder on it with the logit
lens. That turns "DeepSeek happens to do this" into "this is what a model learns
when pushed to do it," which is the more general interpretability question.

## Artifacts

- Two-step sweeps and controls: `results/<model>/varbind-eval/`, `.../varbind-pre-question-k50-control/` for qwen3.5-4b, qwen3.5-9b, llama3.1-8b-it, qwen3.5-27b, qwen3.5-35b-a3b, qwen3.6-27b, qwen3-32b, qwen3-30b-a3b, gemma-3-27b-it, olmo-3.1-32b-it
- Screen driver: `scripts/screen_models.sh`
- Branching sweep: `results/qwen3.5-9b/branching-varbind-eval/`
- One-step sweeps and controls: `results/*/varbind-onestep-eval/`, `.../varbind-onestep-pre-question-k50-control/`
- Held-out 200: `results/qwen3.5-4b/varbind-onestep-heldout200-eval/`, `.../varbind-onestep-heldout200-pre-question-k50-control/`
- Configs: `configs/varbind_onestep_*.json`
- Each result directory has `filler_length_sweep.json` (prompts, token ids, generations, logits), `behavior-summary.json`, `behavior-report.md`, and `runtime.json` with the model config and package versions.
