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

### Other filler types, chat model (50 held-out items, k=50 items)

Same dump and analysis as for dots (`summarize_filler_types.py` collects the numbers).
Attention is the mean mass on the filler region from the generation position over the
last third of blocks. "Cos same pos" is the cosine of the same filler position across
different problems at three-quarter depth; "var by problem" the share of filler-residual
variance explained by which problem precedes it. Probe R² is the best ridge probe for
the answer. Centered adjacency is the item-centered adjacent cosine at three-quarter
depth over the middle of the span.

| filler | tokens | correct at k=50 | gen→filler | cue→filler | cos same pos | var by problem | R² ans from filler | R² ans from q_last | centered adj | change pts/item |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dots | 50 | 49 | 0.164 | 0.195 | 0.78 | 0.036 | 0.87 | 0.40 | 0.12 | 0.9 |
| alphabet | 50 | 42 | 0.126 | 0.159 | 0.82 | 0.017 | 0.84 | 0.24 | 0.05 | 0.9 |
| alphabet-scrambled | 50 | 41 | 0.113 | 0.149 | 0.85 | 0.024 | 0.83 | 0.43 | 0.03 | 1.9 |
| counting | 99 | 49 | 0.227 | 0.254 | 0.77 | 0.016 | 0.89 | 0.51 | 0.04 | 1.2 |
| counting-scrambled | 99 | 49 | 0.231 | 0.254 | 0.77 | 0.013 | 0.91 | 0.52 | 0.01 | 2.3 |

**Attention on the filler tracks the behavioral gain.** Letters get 0.11 to 0.13 of the
generation position's late attention and lift accuracy to 41 or 42; dots get 0.16 and
lift it to 49; numbers get 0.23 and lift it to 49. The answer is decodable from every
filler type at 0.83 to 0.91, so the filler always ends up holding the answer; what
differs is how much the answer positions read it. Numbers are content tokens the model
already attends to in arithmetic contexts, and they are read hardest; letters are read
least. Order within a type changes nothing (scrambled versus ordered letters, scrambled
versus ordered numbers), which says the filler's semantics as a sequence do not matter,
only what kind of token fills the slot.

**Change points are token artifacts wherever they are consistent.** For letters the only
raw change point shared across items is F26|F27 (45 of 50 items), which is the z→a wrap
of the alphabet. For numbers the raw adjacent cosine is low everywhere (0.3) because the
tokens alternate number, space, number, space. For scrambled types change points are
more frequent (1.9 to 2.3 per item) and scattered: heterogeneous token identity, not a
pivot in the computation. After centering, adjacent cosine is 0.01 to 0.05 for every
type other than dots (0.12): the problem-specific content at one filler position is
nearly unrelated to its neighbor's. Nothing here looks like a thought that persists
across several positions and then changes.

### Other filler types, base model

| filler | tokens | correct at k=50 | gen→filler | cue→filler | cos same pos | var by problem | R² ans from filler | R² ans from q_last | centered adj | change pts/item |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dots | 50 | 50 | 0.203 | 0.189 | 0.64 | 0.044 | 0.85 | 0.74 | 0.11 | 0.5 |
| alphabet | 50 | 50 | 0.180 | 0.168 | 0.77 | 0.016 | 0.83 | 0.88 | 0.04 | 1.1 |
| alphabet-scrambled | 50 | 50 | 0.164 | 0.156 | 0.81 | 0.019 | 0.78 | 0.87 | 0.02 | 1.8 |
| counting | 99 | 49 | 0.271 | 0.241 | 0.72 | 0.015 | 0.82 | 0.78 | 0.03 | 1.2 |
| counting-scrambled | 99 | 50 | 0.267 | 0.228 | 0.72 | 0.016 | 0.88 | 0.76 | 0.00 | 2.7 |

**The base reads every filler type harder than the chat model, in the same order.** Letters
0.16 to 0.18 (chat 0.11 to 0.13), dots 0.20 (0.16), numbers 0.27 (0.23). Which token kind
attracts the answer positions is a pretraining property; post-training lowered the amount
by a roughly constant factor and did not change the ranking. The answer is decodable from
every filler type in the base too (0.78 to 0.88).

**The chat/base difference is at the question token for every type.** Answer probe from
the last question token: base 0.74 to 0.88, chat 0.24 to 0.52. This is the one column
where the checkpoints separate, and it separates for all five fillers. One caution when
reading the chat column's spread (letters 0.24, dots 0.40, numbers 0.51): the question
token precedes the filler, so the filler itself cannot affect it; what differs is the
five demonstrations and the system sentence, which mention the filler type. The
question-token encoding depends on the surrounding context, not on the filler tokens.

**Redundancy is not what separates them either.** Centered adjacency is 0.00 to 0.11 in
both checkpoints for every type; change points are as scattered in the base as in chat.
The "each filler position holds its own snapshot" picture is the same before and after
post-training.

### Qwen3.5-9B with the same fillers (`run_hf_filler_types.sh`)

| model | filler | k=0 | 50 | 100 | helped/hurt at 50 |
|---|---|---:|---:|---:|---|
| Qwen base | any of the four | 0 | 0 to 1 | 0 to 1 | floor |
| Qwen dots-only LoRA | dots (earlier run) | 40 | 46 to 48 | | |
| Qwen dots-only LoRA | alphabet | 42 | 40 | 39 | 1/3 |
| Qwen dots-only LoRA | alphabet-scrambled | 41 | 40 | 38 | 3/4 |
| Qwen dots-only LoRA | counting | 42 | 37 | 39 | 0/5 |
| Qwen dots-only LoRA | counting-scrambled | 42 | 30 | 36 | 0/12 (p=0.0005) |

The untrained 9B is at floor whatever fills the span. The model trained only on dot
prompts gets nothing from letters and is hurt by numbers, badly by scrambled numbers.
Its gain with dots is specific to the token it was trained on, and digit tokens sitting
between the question and the answer interfere with a model that does its arithmetic at
the answer position. DeepSeek's chat model shows the opposite sign: numbers are the
filler it reads hardest and benefits from most.

### Qwen3.5-9B anatomy by filler type (`results/filler-cosine/summary-qwen.md`)

Numbers cost 140 tokens per 50 items on Qwen's digit-split tokenizer.

| model | filler | gen→filler | max head | R² ans from filler | R² ans from q_last | centered adj | change pts/item |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen base | dots | 0.010 | 0.18 | 0.54 | 0.28 | 0.24 | 0.2 |
| Qwen base | letters (either) | 0.005 to 0.011 | 0.05 | 0.25 to 0.38 | 0.30 to 0.34 | 0.02 | 1.0 |
| Qwen base | numbers (either) | 0.011 to 0.012 | 0.10 to 0.11 | 0.47 to 0.51 | 0.36 to 0.39 | 0.05 | 0.2 to 0.4 |
| Qwen dots-only | dots | 0.009 | 0.08 | 0.97 | 0.94 | 0.77 | 4.2 |
| Qwen dots-only | letters (either) | 0.009 to 0.011 | 0.14 to 0.16 | 0.95 to 0.97 | 0.92 | 0.08 to 0.10 | 0.4 to 0.7 |
| Qwen dots-only | numbers (either) | 0.053 to 0.054 | **0.49 to 0.51** | 0.97 to 0.98 | 0.90 to 0.91 | 0.14 to 0.23 | 0.3 |

Two things this adds.

**Why numbers hurt the trained Qwen.** Its answer position ignores dots and letters
(attention 0.01, no head above 0.16) but attends to number fillers at 0.05 on average
with single heads putting half their mass there. A model that does its arithmetic at the
answer position and has heads that read digits will read filler digits as if they were
problem digits. That is the mechanism behind 42 → 30 with scrambled numbers. DeepSeek's
chat model has the opposite relation to the same tokens: it reads them hardest and
benefits most.

**The constant-vector signature is specific to identical tokens.** The dots-only Qwen's
0.77 centered adjacency, which looked like a copied problem vector along the span, falls
to 0.08 to 0.23 with letters or numbers, because heterogeneous tokens vary the residual
by token identity. So redundancy across the span has to be compared within a filler
type. Within dots, the contrast stands: 0.77 in the trained Qwen against 0.11 to 0.12 in
both DeepSeek checkpoints.

The direct-path picture is unchanged by filler type: the trained Qwen holds the answer
at the question token at 0.90 to 0.94 whatever fills the span, like the DeepSeek base
(0.74 to 0.88) and unlike the DeepSeek chat model (0.24 to 0.52).

### Summary of the filler-type comparison

Filler type changes how much the answer positions read the span (letters least, numbers
most) and, in the post-trained model, how much accuracy the span recovers. It does not
change the anatomy: every type ends up holding the answer, every type is dominated by
position and token identity, and every type shows the same scattered non-pattern in
adjacent cosine. The base reads all of them and needs none of them. The one thing that
moves between base and chat is the answer encoding at the question token, and it moves
for every filler type.

## Artifacts

- `results/filler-cosine/dots/`, `results/filler-cosine/qwen-dots/` (JSON, markdown, figures)
- `results/deepseek-v4-flash{,-base}/varbind-eval-<type>/` behavioral sweeps
- `results/deepseek-v4-flash{,-base}/filler-dump-<type>/{analysis,cosine}/` anatomy per type
- `results/qwen3.5-9b/filler-types/{base,dotsonly}/varbind-eval-<type>/` and `.../filler-dump-<type>/{analysis,cosine}/`
- Cross-type tables: `results/filler-cosine/summary-deepseek.md`, `results/filler-cosine/summary-qwen.md`
