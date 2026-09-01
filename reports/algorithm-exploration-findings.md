# What DeepSeek V4 Flash does with filler tokens: initial findings

## Bottom line

The strongest current interpretation is that post-question filler tokens provide a
**distributed, causally usable workspace across sequence width**. DeepSeek V4 Flash
does not appear to treat the dots as a left-to-right textual scratchpad where one dot
corresponds to one serial reasoning step. Instead, hidden values are staged mainly by
**layer depth**, copied across several noncontiguous filler positions, and finalized
very late—sometimes in the unlensed final block. The newest causal test sharpens this
to **portable workspace content with position-biased receivers and redundant
storage**: a donor answer state works at almost any filler destination, but a stable
late-dot band amplifies it most strongly.

This is meaningful use of transformer parallelism in the following limited sense:
all prompt positions are evaluated in parallel within each transformer layer, and
adding causally downstream positions can improve a fixed-depth computation without
adding transformer layers. The results do not establish that the model implements an
optimal parallel algorithm, nor that every decodable cell is causally necessary.

All references to decoded values below mean **J-Lens token readouts**, not the paper's
formal sparse nonnegative J-space decomposition and not a transcript of private
reasoning.

## Strongest behavioral evidence: placement matters

On 50 released easy variable-binding examples:

| Condition | Correct | Accuracy |
|---|---:|---:|
| No filler | 35 / 50 | 70% |
| 50 dots before all target definitions/question | 35 / 50 | 70% |
| 50 dots between question and answer cue | 49 / 50 | 98% |

Comparing the two 50-dot placements example by example, 14 cases are correct only
with post-question filler and zero are correct only with pre-question filler. The
two-sided exact paired sign/McNemar probability for a 14-to-0 split is approximately
`0.00012`.

The pre-question dots have the same token budget and formatting role but cannot see
the target problem under causal attention. Their failure to reproduce the gain is
strong evidence that the model uses the downstream filler activations as workspace.

## A hidden serial chain becomes a layer-depth ladder

The released variable-binding task has a genuinely hidden dependency chain. For one
example:

```text
nof = 97
hoz = twice the number for nof minus 21
Question: What is twice the number for hoz plus 28?
```

The tracked computation is `97 → 194 → 173 → 346 → 374`. Across four selected
k=50 examples, the median first layer with an exact rank-1 J-Lens token in any filler
cell is:

| Stage | J-Lens layer | Logit-lens layer |
|---|---:|---:|
| Visible base value | 25.5 | 25.5 |
| Raw first product | not rank-1 | not rank-1 |
| Hidden bound value after first offset | 30.5 | 30.0 |
| Second product | 32.0 | 33.0 |
| Final answer | 36.0 | 36.0 |

The clean bound value but absent raw first product suggests a fused multiply-plus/minus
transition or a representation not aligned to a token direction. It does not justify
claiming that the product was never computed.

The filler ordinals are not a serial timeline. Later stages often first appear at
earlier filler ordinals than earlier stages, and values occupy several noncontiguous
positions. The chain is ordered reliably by depth, not by dot order.

## More dots add copies and can advance depth onset

For the threshold example above:

| Dots | Output | Correct | Rank-1 J cells: base / bound / second product / answer |
|---:|---:|---:|---:|
| 5 | 324 | no | 0 / 0 / 1 / 0 |
| 25 | 320 | no | 1 / 3 / 26 / 10 |
| 50 | 374 | yes | 21 / 24 / 60 / 25 |

For a second boundary example, increasing from 50 to 100 dots changes the answer from
`387` to correct `385`; rank-1 J-Lens answer cells increase from 8 to 43. The base and
bound values also become decodable several layers earlier at k=100.

Thus, extra dots do more than append hypothetical serial steps. They increase the
number of workspace cells carrying useful values and can allow the same computation
to emerge earlier in layer depth. This is consistent with added parallel width and
redundant/routed computation lanes.

Existence is not sufficiency: the k=25 failure already has rank-1 readouts for every
major stage, and the k=50 boundary failure contains the correct answer in several
cells. A causal patch or ablation is still needed to identify which cells determine
the final output.

## Across-example shuffled-token control

For the four k=50 variable-binding examples, exact top-1 filler-cell counts are:

| Stage | J-Lens actual / deranged value | Logit lens actual / deranged value |
|---|---:|---:|
| Base | 86 / 0 | 69 / 0 |
| Hidden bound value | 98 / 0 | 75 / 0 |
| Second product | 143 / 0 | 121 / 0 |
| Answer | 101 / 0 | 96 / 0 |

The derangement shifts each stage's target values by two examples. This does not
replace full cross-example residualization, but it makes a generic digit-frequency
explanation for the exact top-1 ladder much less plausible.

## Independent facts look concurrent, not prefix-serial

A three-fact order probe used the same atomic values in three cyclic orders:

```text
21 + 6 + 92   (candidate prefix 27)
6 + 92 + 21   (candidate prefix 98)
92 + 21 + 6   (candidate prefix 113)
```

All three selected k=50 prompts answer `119` correctly. The three atomic values become
decodable nearly simultaneously at layers 34–35 in every order. The order-dependent
prefix sums are weak or absent and do not form a consistent prefix-accumulation trace.
This is more consistent with parallel fact retrieval followed by a late composition
than with left-to-right addition.

The task is a negative behavioral result overall: only 4/60 are correct without
filler and 3/60 at k=50. The matched trio is therefore a qualitative order probe, not
evidence that dots generally improve three-fact addition.

## The missing layer 42 matters in practice

For the matched three-fact cases, the invariant sum `119` is only rank 2–3 at the
layer-41 prediction position, usually behind `105`. The actual block-42 logits flip
`119` to rank 1, with probabilities `0.302`, `0.312`, and `0.436` across the three
orders. Final-head closure for block 42 is exact.

The released J-Lens covers source layers 0–41 and has no matrix for block 42. These
examples show a concrete consequence: the decisive final composition can occur in
the missing last block. The viewer's separate “Actual L42” row should not be mistaken
for a J-Lens readout.

## Nonnumeric retrieval/selection

Element-letter selection is near ceiling: 46/50 without filler and 47/50 from k=10
through k=100. One stable helped case is:

```text
atomic number 37 → Rubidium → second letter u
```

No filler predicts `b`; k≥5 predicts `u`. At k=10, the `Rub` subtoken becomes rank-1
in a filler cell, but `u` never reaches filler-cell top-10. A correct Silver control
similarly retrieves `Silver` cleanly while the requested letter is not directly
decodable. This suggests entity retrieval in the filler workspace with letter
selection/finalization occurring later or in a non-token-aligned representation.

## Negative strict-chain controls

### Behavior-first inclusion gate

Further mechanistic analysis now uses a task-level gate: J-Lens readouts count toward
the scientific conclusion only when a paired dot sweep has more helped than hurt
examples and at least a 10 percentage-point accuracy gain at a positive dot length.
Individual dot-helped examples do not qualify when aggregate task accuracy is flat or
worse. The released easy variable-binding task passes (`70% → 98%` at k=50); the new
arithmetic and branching probes do not.

Two arithmetic-program readout batches were completed before this gate was adopted.
They are retained as explicitly excluded exploratory negatives and are not used to
argue that filler tokens execute those algorithms. No readout extraction was started
for the depth-2 branching calibration after its behavior sweep failed.

Fillers do not create a general-purpose serial executor:

| Task | No filler | Best filler result | Dependency result |
|---|---:|---:|---|
| Repeated modular squaring | 2 / 100 | 7 / 100 at k=3 or k=10 | 0/10 at T=10; almost all T≥5 fail |
| Pointer chasing | 12 / 40 | 15 / 40 at k=50/100 | T=1: 10/10; T=2: 5/10; T=4 and T=8: 0/10 |
| Three-fact addition | 4 / 60 | 3 / 60 at k=5–50 | filler does not improve aggregate accuracy |
| Element-to-letter | 46 / 50 | 47 / 50 at k≥10 | ceiling-limited one-example gain |
| Seven-operation arithmetic programs | 9 / 48 | 8 / 48 at k=25 | no aggregate filler benefit |
| Two depth-1 variable-binding branches | 34 / 36 | 34 / 36 at k=10 or k=50 | ceiling-limited; no aggregate benefit |
| Two depth-2 variable-binding branches | 2 / 40 | 3 / 40 at k=25 | +2.5 points, below gate; k=10/50 worse |
| Variable binding | 35 / 50 | 49 / 50 at k=50/100 | strong, placement-specific gain |

The most conservative synthesis is that filler width amplifies computations the
pretrained model already nearly supports. It does not reliably induce novel long
serial algorithms from instructions. Pointer chasing was designed to expose
layerwise doubling (`x1`, `x2`, `x4`, `x8`), but behavior at T=4/8 was zero, so no
pointer-jumping lens claim is warranted.

## J-Lens versus logit lens

Both readouts recover the same main variable-binding ladder. J-Lens has more exact
top-1 cells for each major stage in the four selected examples and advances the
median second-product onset by one layer. It also recovers some fact/entity tokens
that are only rank 2 under the logit lens. These are useful qualitative differences,
but the current sample does not establish broad J-Lens superiority; some entity
readouts appear earlier under the raw logit lens.

## Current algorithm hypothesis

The evidence supports this provisional circuit-level description:

1. Query-conditioned late-middle layers retrieve input facts or a visible base value
   into a small subset of filler positions.
2. Fixed later layer bands transform the retrieved value into hidden bound values and
   final arithmetic candidates.
3. Attention/hyper-connection routing copies or broadcasts useful candidates into
   several noncontiguous filler lanes; lane ordinal is not the computation's serial
   clock.
4. The answer position, and sometimes the final unlensed block, selects or completes
   the result from this distributed workspace.
5. Extra causally downstream filler positions increase workspace capacity and
   redundancy, improving tasks with a compatible pretrained circuit. They do not add
   transformer depth and do not rescue unsupported long dependency chains.

## What is replication, and what goes beyond the filler paper

The first behavioral sweep and raw logit-lens maps intentionally reproduced the
released filler-token setup before adding new machinery. The released repository
already includes layer × position logit-lens decoding of the variable-binding chain,
cross-example residualization, whole/selected-position KV transplants, attention
knockouts, activation patching, and Patchscope analyses. Those are not claimed as new
here.

The follow-up asks different mechanistic questions:

| Question | Released filler work | This follow-up |
|---|---|---|
| Readout | Raw/residualized logit lens | Pretrained DeepSeek V4 Flash J-Lens plus the same logit-lens baseline |
| Counterfactual control | Fact-matched donor/target tasks | Prompts with exactly one changed token and otherwise identical token positions |
| Causal resolution | Whole filler or readout-selected subsets | Exhaustive single residual cells and one source cell moved through every destination dot |
| Dot-address hypothesis | Per-condition position heatmaps | Cross-length tests of absolute, proportional, and answer-relative coordinates |
| Necessity/redundancy | Filler attention and transplant ablations | J-selected mean-residual lesions versus layer-matched random cells at increasing doses |

The intervention patches the complete raw post-block mHC residual at a cell. J-Lens
selects the cell, but the intervention does not isolate the displayed token direction
and is not a formal sparse J-space-coordinate intervention.

## Independent behavior gate and exact-layout families

The original first-50 result generalizes to the next 100 released easy
variable-binding templates:

| Dots | Correct | Accuracy | Helped / hurt versus k=0 | Exact paired p |
|---:|---:|---:|---:|---:|
| 0 | 59 / 100 | 59% | — | — |
| 5 | 74 / 100 | 74% | 22 / 7 | 0.0081 |
| 10 | 70 / 100 | 70% | 16 / 5 | 0.0266 |
| 25 | 79 / 100 | 79% | 21 / 1 | 1.1e-5 |
| 50 | 94 / 100 | 94% | 35 / 0 | 5.8e-11 |
| 100 | 96 / 100 | 96% | 37 / 0 | 1.5e-11 |

Six independently selected source templates were then expanded into 48 exact-layout
numeric counterfactuals. Accuracy rises from `14/48` without dots to `42/48` at k=50
and `47/48` at k=100; k=50 helps 28 and hurts zero (`p=7.5e-9`). Three families
provide six causal directions in which donor and target differ at exactly one token.

The gain is not always a smooth function of workspace width. One family scores
`1/8 → 7/8 → 0/8 → 1/8 → 5/8 → 8/8` at k=`0,5,10,25,50,100`. A fixed example in
that family computes `64 → 128 → 125 → 250 → 235`: it answers `235` at k=5, falls
to the confident wrong answer `185` at k=10 and k=25, and returns to `235` at k=50
and k=100. This positional resonance is inconsistent with a purely monotonic
"more dots means more generic compute" account; its all-layer readout follow-up is
tracked separately from the confirmatory three-family causal cohort. Because the
paper-matched scaffold changes filler spans in the few-shot demonstrations as well as
the target, this is initially a full-prompt-geometry result; a fixed-demonstration-k
ablation is needed before assigning the flip solely to the target filler span.

## Cross-length workspace coordinates

Across k=`5,10,25,50,100` donor readouts, no single coordinate system explains every
stage. When the same example is correct at both lengths, the complete J-Lens
second-product profile recurs most under fixed distance from the answer cue
(`mean ρ=0.202`, versus `0.110` absolute and `0.017` proportional). The logit-lens
result agrees (`0.235`, versus `-0.004` and `-0.024`). In contrast, the final-answer
J-Lens profile recurs most under absolute dot ordinal (`0.166`, versus `0.007`
answer-relative and `-0.024` proportional).

At k=50, the strongest averaged readout addresses are themselves stage-dependent:

| Readout | Base | Hidden bound | Second product | Answer |
|---|---:|---:|---:|---:|
| J-Lens | F44 | F43 | F50 | F1 |
| Logit lens | F44 | F43 | F41 | F40 |

These are peaks of a distributed profile, not unique registers. For example, F41 and
F40 are also among the strongest J-Lens product/answer addresses. The conservative
conclusion is stage-dependent positional routing: product-like state leans toward
answer-relative lanes, while final-answer state has stable absolute-address
components. The causal cross-position experiment below tests whether those address
profiles are usable or merely decodable.

## Dot-count resonance exposes parallel candidate competition

The non-monotonic `kur=64` example reveals what changes across filler lengths. The
requested path is `xav=125 → 250 → 235`. A sibling definition gives `rek=100`; applying
the same final `×2−15` operation to that sibling produces the observed wrong answer
`185`. All 42 released J-Lens layers at every target filler position show:

| Dots | Output | Correct bound 125 | Correct product 250 | Correct answer 235 | Sibling answer 185 |
|---:|---:|---:|---:|---:|---:|
| 5 | 235 | 0 / 0.0 | 0 / 0.0 | 3 / 4.6 | 0 / 0.0 |
| 10 | 185 | 0 / 0.0 | 0 / 0.0 | 0 / 0.0 | 0 / 1.0 |
| 25 | 185 | 4 / 7.1 | 0 / 2.0 | 0 / 0.0 | 7 / 11.7 |
| 50 | 235 | 20 / 32.0 | 13 / 26.1 | 24 / 37.6 | 21 / 48.1 |
| 100 | 235 | 71 / 109.5 | 36 / 75.5 | 60 / 87.4 | 24 / 69.6 |

Each entry is `rank-1 cells / rank-weighted top-10 strength`. The logit lens shows the
same broad phase transitions.

This is not a single route becoming progressively clearer. At k=25, the requested
bound value is decodable but the sibling-consistent answer wins. At k=50, both final
candidates are broadcast strongly—and the sibling answer has greater aggregate
top-10 strength—yet the requested answer wins. At k=100, the sibling candidate
persists while the requested bound/product/answer route expands much more strongly.
The k=5 success is different again: only the final requested answer is cleanly
decodable, suggesting a narrow direct/shortcut regime rather than the full ladder.

The important insight is **parallel candidate maintenance plus late,
location-sensitive selection**. More filler can add copies of correct and incorrect
candidates simultaneously. Correctness depends on which candidate reaches the right
downstream locations/layers and is selected at the answer cue, not on whether the
correct value appears anywhere or even on its aggregate count. The absent
token-aligned sibling bound/product readouts mean this should not be narrated as a
fully observed serial sibling chain; only the final wrong candidate is clearly
decoded.

## Formal J-space makes selected cells look winner-like

The ranked readouts above are not formal J-space coordinates. We therefore applied the
paper's sparse nonnegative gradient-pursuit decomposition (`k=25`) to ten preselected
filler activations. The dictionary at layer `l` is
`(W_U * final_rmsnorm_weight) @ J_l`, and the target is the same 4096-wide,
model-native mHC-collapsed activation used by the extraction pipeline. Synthetic
support recovery is exact, and the folded dictionary reproduces every site's complete
top-25 J-Lens ordering with maximum relative logit error `1.45e-6`.

The formal support changes how the apparent within-cell coexistence should be read:

- Every tracked task token at J-Lens rank 1 is selected as an active atom (`7/7`).
- None of the tracked task tokens at ranks 2–25 is selected (`0/9`).
- At k=50/L31/F14 and k=100/L36/F19, the ranked readout contains requested answer
  `235` first and sibling answer `185` second. Both formal supports keep `235` and omit
  `185`.
- At k=25/L36/F10, the formal support keeps bound value `125` (rank 1) and omits product
  `250` (rank 2). At k=25/L38/F21, it keeps the wrong output `185` (rank 1) and omits
  requested answer `235` (rank 26).

This refines, rather than erases, the candidate-competition result. Requested and
sibling candidates coexist across the layer × position grid, but the selected
individual cells are more like local winners than multi-token mixtures under this
specific sparse inventory. A better current hypothesis is **sequence-distributed
winner selection**: different filler cells carry different candidate winners, and
later circuitry selects among the distributed cells. Correlated atoms can still rank
together in a readout even when the greedy sparse solution uses only one.

The decomposition is not evidence that J-space spans these states unusually well. Raw
J-space reconstruction explains `5.52–8.69%` of squared activation norm (mean `6.60%`),
while the Haar-rotated relative-orientation control averages `7.18%` and is higher on
8/10 sites. The matched sparse logit-space baseline averages `7.05%`. J-space and
logit-space share only `6.3/25` selected atoms on average, and J-space alone selects a
task atom at two preselected sites (`235` at k=5/L36/F2 and `250` at k=50/L33/F43).
Those two cases are suggestive, not an unbiased advantage, because site selection used
J-Lens.

Finally, sparse support is not unique ground truth: the vocabulary dictionary is
overcomplete, the pursuit is greedy, and correlated task atoms have cosine similarity
around `0.44–0.61` in the relevant layers. Omitting a runner-up does not prove that the
activation contains no information about it or that no alternative sparse support
could include it.

## Causal validation on an exact-layout counterfactual

The intervention now changes one input token while holding every other token and
position fixed. Eight variants of the same template change only the one-token value
assigned to `suv`. They are `0 / 8` correct without filler and `8 / 8` with 50 dots
(`8` helped, `0` hurt). The selected pair is:

```text
suv = 64 → woh = 119 → 2 × woh = 238 → answer 224
suv = 72 → woh = 135 → 2 × woh = 270 → answer 256
```

Both rendered prompts contain 850 tokens, use filler indices 796–845, and differ only
at absolute token index 751 (`64` versus `72`). Raw post-block mHC residuals retain all
four `4096`-dimensional streams. Patching a prompt's own residual back into itself has
exact logit closure (`0.0` maximum absolute error).

### Single-cell map

For the `72 → 64` direction, the counterfactual answer `256` starts at rank 82. Across
all `10 × 50 = 500` cells at layers 29–38, 77 one-cell patches improve its log
probability by at least 1 nat and only 14 by at least 3 nats. The strongest cells form
stable vertical lanes rather than filling the grid:

| Dot | Best layer | Counterfactual Δlog p | Counterfactual rank |
|---:|---:|---:|---:|
| 41 | 33 | +4.86 | 20 |
| 40 | 33 | +4.25 | 25 |
| 14 | 33 | +2.97 | 30 |
| 28 | 33 | +2.69 | 32 |
| 43 | 29 | +2.15 | 43 |
| 10 | 31 | +2.11 | 46 |

At dot 1, the J-Lens readout itself follows a particularly clean depth pipeline:
base `72` is rank 2 at layer 25, bound value `135` is rank 1 at layer 28, doubled value
`270` is rank 1 at layer 31, and answer `256` is rank 1 at layer 36. Dots 14, 28, 40,
and 41 join at the product and answer phases. Dots 40–41 are more causally influential
than dot 1 even though their earlier bound state is not cleanly token-decodable.

Across the full grid, causal effect correlates with J-Lens rank for the second product
(`ρ = 0.592`) and answer (`ρ = 0.571`). Logit-lens correlations are similar (`0.569`
and `0.552`). This connects the decoded values to answer-relevant state, but it does
not isolate the displayed token direction from the rest of the patched residual.

### Pre-selected multi-cell doses

The 16-cell dose was selected from the donor readouts before intervention. Results
below show the counterfactual answer rank and log-probability change; controls use the
same layer counts.

| Direction / decoded stage | J-Lens | Logit lens | Layer-matched random | Complement |
|---|---:|---:|---:|---:|
| `72 → 64`, second product | 2 / +10.20 | 2 / +10.43 | 16 / +5.63 | 83 / +0.18 |
| `72 → 64`, answer | 4 / +9.53 | 4 / +9.56 | 61 / +0.80 | 88 / +0.20 |
| `64 → 72`, second product | 7 / +8.39 | 3 / +9.22 | 86 / +0.18 | 78 / -0.22 |
| `64 → 72`, answer | 5 / +8.68 | 7 / +7.69 | 33 / +3.89 | 84 / -0.14 |

The recipient answer remains rank 1 in these highly confident prompts, so there are no
full answer swaps. Rank and log-probability shifts are the more sensitive endpoint.
Random high-dose patches can pick up real lanes by chance, but complementary low-score
locations remain near zero in both directions.

This pair shows that some vertical lanes are much more influential than others and
that product/answer state is replicated across several dots. More dots supply
workspace width and routing options; they do not create 50 additional serial
arithmetic steps. J-Lens and logit lens both identify these locations, with no broad
J-Lens-superiority result in this sample. The cross-position test below asks whether
those strong lanes are rigid registers or preferred receivers for portable state.

## Beyond the paper: source states are portable, receivers are position-biased

The single-pair map above could still be read as a handful of fixed registers. A new
cross-position intervention tests that directly. For three independent exact-layout
pairs in both directions, it takes the top J-Lens-selected answer or second-product
cell from the donor's raw post-block mHC residual and moves that same state through
all 50 destination dots in the target at the same layer.

The source dot is not a required address:

| Stage | Directions | Same source/destination is best | Median same-position Δlog p | Median best Δlog p | Median destinations ≥ half maximum |
|---|---:|---:|---:|---:|---:|
| Answer | 6 | 0 / 6 | +1.84 | +2.88 | 78% |
| Second product | 6 | 2 / 6 | +1.46 | +1.72 | 83% |

All `300/300` answer-state destinations increase the donor answer's log probability;
`297/300` second-product destinations do so. The best answer-state patch moves the
donor answer from rank 74 to rank 3 (`+7.37` nats). Across the six directions, best
answer-state patches improve the counterfactual donor rank by 23–99 places while the
target's own answer remains rank 1.

The destinations are nevertheless not equivalent. The complete answer-effect profile
recurs strongly across the 15 direction pairs (`mean Spearman ρ=0.719`, median
`0.755`); the product profile also recurs (`0.484`, median `0.448`). Answer-state best
destinations are always in the late filler band: F50 in three directions, F44 in two,
and F40 in one. The five highest mean-effect answer destinations are F50, F44, F49,
F40, and F47. This is not just a readout-location pattern: it is a causal receiver-gain
profile.

Donor increases are not merely generic disruption, but full answer swaps do not occur.
Across destination dots, donor- and target-answer effects are negatively correlated
for the median product direction (`ρ=-0.541`) and 82% of product destinations both
raise the donor and lower the target. The target decrease is usually tiny, however
(median `-0.001` nat at the donor-best product destination), because these are highly
confident correct targets.

Finally, replacing J-selected cells with that layer's mean filler residual shows
redundancy rather than a single bottleneck. At dose 16, J-selected answer lesions are
more damaging than layer-matched random lesions in `6/6` directions, and product
lesions in `5/6`; median effects are only `-0.015` and `-0.011` nat, respectively.
The distribution is heterogeneous: one answer direction falls `-2.76` nats and one
product direction `-0.86`, while several are nearly unchanged. Mean replacement may
also preserve signal shared across many filler cells, so small effects are not proof
of causal irrelevance.

The resulting mechanism is a hybrid:

1. **Content is portable.** Once a late-layer filler state carries the relevant
   product/answer information, most later processing can use it at almost any dot.
2. **Receiver gain is addressed.** Fixed late filler positions—especially the end
   band—amplify that transplanted state more strongly and reproducibly.
3. **Storage is redundant.** Many cells carry overlapping usable state; removing a
   few readout-selected cells usually has little effect, even though adding one donor
   state can strongly raise a counterfactual answer.

This goes beyond a serial scratchpad and beyond a set of rigid registers. The best
current description is **broadcast/fungible workspace content with position-dependent
readout gain**. That is a concrete way the model uses filler-token parallelism: layers
advance the variable-binding computation, while sequence width supplies many parallel,
partly interchangeable carriers and a biased set of downstream receiver positions.

## Artifacts

- Consolidated workspace-mechanism viewer: `results/algorithm-probes/varbind-scaled-workspace-analysis/workspace-mechanism-viewer.html`
- Cross-position causal report: `results/algorithm-probes/varbind-scaled-workspace-analysis/workspace-probe-report.md`
- Cross-position machine-readable results: `results/algorithm-probes/varbind-scaled-workspace-probe-k50/workspace-probe-results.json`
- Cross-length coordinate report: `results/algorithm-probes/varbind-scaled-lane-analysis/lane-scaling-report.md`
- Dot-count candidate-competition report: `results/algorithm-probes/varbind-resonance-analysis/resonance-report.md`
- Candidate-competition all-layer viewers: k=5, 10, 25, 50, and 100 under `results/algorithm-probes/varbind-resonance-f05-kur-064/`
- Formal J-space report: `results/algorithm-probes/varbind-resonance-jspace-decomposition/jspace-decomposition-report.md`
- Formal J-space full results and summary: `results/algorithm-probes/varbind-resonance-jspace-decomposition/jspace-decomposition.json` and `jspace-decomposition-summary.json`
- Independent held-out behavior gate: `results/algorithm-probes/varbind-heldout-050-149-sweep/behavior-report.md`
- Independent exact-layout family gate: `results/algorithm-probes/varbind-scaled-counterfactual-families-sweep/behavior-report.md`
- Variable-binding aggregate viewer: `results/algorithm-probes/varbind-analysis/varbind-algorithm-viewer.html`
- Variable-binding quantitative report: `results/algorithm-probes/varbind-analysis/varbind-algorithm-report.md`
- Exact-layout causal viewer: `results/algorithm-probes/varbind-counterfactual-causal-analysis/varbind-causal-viewer.html`
- Exact-layout causal report: `results/algorithm-probes/varbind-counterfactual-causal-analysis/varbind-causal-report.md`
- Exact counterfactual all-layer readouts: `results/algorithm-probes/varbind-counterfactual-jlens-k50/`
- Hard threshold example viewers: k=5, k=25, and k=50 under `results/algorithm-probes/varbind-jlens-*`
- Boundary example viewers: k=50 and k=100 under `results/algorithm-probes/varbind-jlens-*`
- Three-fact cyclic-order viewers: `results/algorithm-probes/three-fact-order-jlens-g14-k50/`
- Element-letter viewers: `results/algorithm-probes/element-letter-jlens-k10/`
- Excluded arithmetic behavior sweep: `results/algorithm-probes/arithmetic-program-sweep/behavior-report.md`
- Excluded branching behavior sweeps: `results/algorithm-probes/branching-varbind-sweep/behavior-report.md` and `results/algorithm-probes/branching-varbind-depth2-sweep/behavior-report.md`
- Machine-readable behavior/readout JSON is stored beside each viewer and report.
