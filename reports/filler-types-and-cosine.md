# Filler types and adjacent-position cosine on DeepSeek V4 Flash (chat and base)

Running log for the experiments the user asked for on 2026-09-04: alternative filler
tokens (letters, scrambled letters, counting numbers, scrambled numbers) on both
DeepSeek checkpoints with the same anatomy as the dot runs, and an adjacent-position
cosine analysis meant to show where the model "changes thought" while it processes a
filler span. Same 50 released items for behavior, same 50 held-out items at k=50 for
the dumps, chat rendering throughout. Scripts: `scripts/run_dsv4_filler_types.sh`,
`scripts/analyze_filler_cosine.py`, `scripts/run_hf_filler_types.sh` (Qwen3.5-9B).

## Filler types

`src/jlens_filler/prompts.py` renders five filler types. The scrambled variants use one
fixed seed-0 permutation for every item, so position-identity analyses stay meaningful.

| type | rendered (first items) | DeepSeek tokens per 50 items |
|---|---|---:|
| dots | `. . . .` | 50 |
| alphabet | `a b c d` (wraps at z) | 50 |
| alphabet-scrambled | `r b c o k m a b` | 50 |
| counting | `1 2 3 4` | 99 |
| counting-scrambled | `44 2 29 15 37` | 99 |

Numbers cost two tokens each on DeepSeek's tokenizer (a standalone space token precedes
each number), so a 50-number filler is 99 tokens and the k=100 prompt is 1,770 tokens.
The filler-type runs use `--max-seq-len 2048`. The exact-count sentence in the system
prompt still says "50 filler tokens"; that mismatch is noted, not fixed.

## Behavior: correct out of 50, post-question filler

| Filler | Model | k=0 | 5 | 10 | 25 | 50 | 100 | helped/hurt at 50 | at 100 |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| dots | chat | 35 | 45 | 42 | 43 | 49 | 49 | 14/0 | 14/0 |
| alphabet | chat | 34 | 41 | 43 | 41 | 42 | 43 | 12/4 | 12/3 |
| alphabet-scrambled | chat | 34 | 38 | 32 | 38 | 41 | 46 | 10/3 | 13/1 |
| counting | chat | 34 | 45 | 45 | 46 | 49 | 48 | 15/0 | 15/1 |
| counting-scrambled | chat | 34 | 31 | 41 | 41 | 49 | 50 | 15/0 | 16/0 |
| dots | base | 48 | 48 | 49 | 49 | 50 | 49 | 2/0 | 2/1 |
| alphabet | base | 48 | 50 | 49 | 48 | 50 | 49 | 2/0 | 1/0 |
| alphabet-scrambled | base | 48 | 49 | 50 | 49 | 50 | 49 | 2/0 | 1/0 |
| counting | base | 48 | 50 | 50 | 49 | 49 | 50 | 2/1 | 2/0 |
| counting-scrambled | base | 48 | 50 | 49 | 50 | 50 | 49 | 2/0 | 1/0 |

Letters help the chat model but less than dots: 42 to 46 at k=50 to 100 against 49,
with a few items hurt where dots hurt none. Letter order does not matter. Numbers work
as well as dots (49 at k=50, ordered or scrambled; scrambled reaches 50 at k=100), and
scrambled numbers hurt at k=5 (6 helped, 9 hurt) before helping at longer lengths. Token
count does not explain the letter gap: 100 letters (100 tokens) give 43 to 46, 50 numbers
(99 tokens) give 49. The k=0 baseline is the same 34 to 35 in every run, as it must be
(identical prompts).

The base is at 48 to 50 for every filler type at every length. Whatever the filler is
made of, there is no deficit for it to repair, so the type comparison is only informative
on the post-trained model.

## Adjacent-position cosine ("change of thought")

Method (`analyze_filler_cosine.py`). For each item, the residual at every filler
position and every block. Adjacent cosine is cos(h[p], h[p+1]) per block, and
flattened over blocks (per-block-normalized concatenation, which equals the mean over
blocks of the per-block cosine). The *item-centered* version subtracts the mean over
items at each position first, removing the position-identity component that dominates
filler residuals and leaving the problem-specific content. Change points are boundaries
where an item's flattened centered series drops more than two standard deviations below
its own mean.

### Dots, chat versus base

| | chat | base |
|---|---:|---:|
| raw adjacent cosine, mid-span, block 21 / 35 / 42 | 0.81 / 0.69 / 0.91 | 0.78 / 0.56 / 0.94 |
| centered adjacent cosine, block 21 / 35 / 42 | 0.08 / 0.13 / 0.29 | 0.06 / 0.13 / 0.19 |
| change points per item (centered) | 0.88 | 0.48 |
| most common change-point boundary (items of 50) | F30/31 and F34/35 (5 each) | F27/28 (4) |

Three things.

**The raw series has exactly three drops, and all are tokenization.** The first dot is
`.` with no leading space, the last is ` .\n\n` merged with the newline, so F1|F2, F2|F3
and F49|F50 drop in every item and every model. Between them the raw adjacent cosine is
0.7 to 0.96 and flat. There is no mid-span position where the residual jumps.

**The problem-specific content is not carried smoothly from dot to dot.** After centering,
adjacent cosine is 0.06 to 0.19 in the middle blocks for both checkpoints. Each dot's
problem component is largely fresh relative to its neighbor. Change points are diffuse:
no boundary is a change point for more than 5 of 50 items. If "changing thought" means a
shared location where the content pivots, there is none; the span looks like fifty
weakly related snapshots rather than a trajectory with segments.

**Chat and base differ in what the dots resemble.** Item-centered cosine between filler
positions and the answer positions (cue, generation) peaks at blocks 39 to 40 in the
chat model and rises along the span (F1 to F5: 0.13; F36 to F50: 0.27). In the base it
peaks at block 35 and falls along the span (F1 to F5: 0.10; F46 to F50: 0.04). Filler
to last-question-token cosine is 0.15 in the base at block 35 and never exceeds 0.06 in
the chat model. In the base, question token, dots and answer share problem content; in
the chat model the question token's content is not what the dots or the answer carry.
This is the cosine version of the probe result (answer from the question token: 0.74
base, 0.40 chat). Caveat below.

### Qwen3.5-9B for comparison (dot dumps from the earlier run, 100 items)

| model | centered adjacent cosine, late blocks | change points per item | where |
|---|---:|---:|---|
| Qwen base | 0.25 to 0.30 | 0.15 | diffuse |
| Qwen k=0-only | 0.44 to 0.51 | 0.69 | F1/2 (42 items) |
| Qwen dots-only | 0.75 to 0.82 | 4.2 | F2/3, F3/4 (100/100), F7/8 (98) |
| DeepSeek chat | 0.06 to 0.19 | 0.88 | diffuse |
| DeepSeek base | 0.06 to 0.19 | 0.48 | diffuse |

The trained Qwen that ignores its dots carries one constant problem vector along the
whole span (adjacent cosine 0.8 after centering) and its only change points are a
settling transient in the first ten dots, identical across all 100 items. DeepSeek's
dots are the least redundant position to position of any model here. Redundancy across
the span is a clean signature of not using it.

**Caveat on the rising gradient.** The filler-to-answer cosine also rises along the span
in Qwen dots-only (block 29: F1 -0.04, F50 0.50), a model shown by lesions not to use
its dots. Adjacency to the answer positions is enough to produce it, so the gradient is
not by itself evidence of computation. The chat/base *difference* in DeepSeek remains,
since both checkpoints have the same adjacency.

### Other filler types

(pending: dumps at k=50 for each type on both checkpoints, anatomy and cosine)

## Artifacts

- `results/filler-cosine/dots/`, `results/filler-cosine/qwen-dots/` (JSON, markdown, figures)
- `results/deepseek-v4-flash{,-base}/varbind-eval-<type>/` behavioral sweeps
- `results/deepseek-v4-flash{,-base}/filler-dump-<type>/{analysis,cosine}/` anatomy per type
- `results/qwen3.5-9b/filler-types/{base,dotsonly}/` (pending)
