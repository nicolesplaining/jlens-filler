# Filler types and adjacent-position cosine on DeepSeek V4 Flash (chat and base)

Running log for the experiments the user asked for on 2026-09-04: alternative filler
tokens (letters, scrambled letters, counting numbers, scrambled numbers) on both
DeepSeek checkpoints with the same anatomy as the dot runs, and an adjacent-position
cosine analysis meant to show where the model "changes thought" while it processes a
filler span. Same 50 released items for behavior, same 50 held-out items at k=50 for
the dumps, chat rendering throughout. Scripts: `scripts/run_dsv4_filler_types.sh`,
`scripts/analyze_filler_cosine.py`, `scripts/run_hf_filler_types.sh` (Qwen3.5-9B).

## Findings in one page

1. **Numbers work as filler as well as dots; letters work less; order never matters.**
   Chat model at k=50: dots 49, numbers 49 (scrambled 49), letters 42 (scrambled 41), from
   a k=0 baseline of 34 to 35. Every type is placement-specific (28 to 36 before the
   question). The base is at 48 to 50 for every type and length.
2. **Attention on the filler tracks the gain, and the ordering is pretrained.** Late-block
   attention from the generation position: letters 0.11 to 0.13, dots 0.16, numbers 0.23
   in the chat model; the base reads every type harder (0.16 to 0.27) in the same order.
   The answer is decodable from every filler type in both checkpoints (0.78 to 0.91), and
   also from the dots of Llama, Gemma and the trained Qwen, so decodability is not
   evidence of use; attention and non-redundancy are.
3. **Adjacent-position cosine shows no change of thought.** Every consistent drop is a
   tokenization artifact (first and last dot, the z→a wrap, the number/space alternation).
   After removing position identity, DeepSeek's filler positions are nearly unrelated to
   their neighbors (0.01 to 0.19) and change points are scattered. The trained Qwen that
   ignores its dots carries one constant vector along the span (0.77 with dots); Llama
   0.44 to 0.59, Gemma 0.23 to 0.36, Qwen base 0.25 to 0.30.
4. **With nothing announced, the chat model's question token holds the answer as well as
   the base's (0.84 both).** The 0.40 versus 0.74 gap of the base write-up appears only when
   a filler span is announced in the context, and it is graded by the announced count
   (0.84, 0.51, 0.36, 0.31 for 0, 5, 25, 50 dots announced and none delivered; base 0.84,
   0.86, 0.85, 0.55).
5. **The demonstrations defer; the sentence costs accuracy.** Demonstrations-only: chat
   question-token probe 0.40, accuracy unchanged at 34. Sentence-only: probe 0.83,
   accuracy 28. The base: 0.55 and 46 versus 0.84 and 50. Deferral is in-context format
   learning from question/span/answer examples, stronger after post-training; the
   instruction sentence degrades the post-trained model's answer without moving the
   computation and does nothing to the base. With dots delivered: nothing announced 39,
   sentence 36, demonstrations 47, both 49.
6. **The chat model has heads that read the sentence** (question token, blocks 20 to 40,
   up to 0.38 of a head's mass; the base at most 0.19 at block 40). They are the route to
   the sentence's cost, not the deferral. Attention from the question token to the
   demonstrations' spans is at or below uniform in both checkpoints; what the
   demonstrations do stays unlocated.
7. **Other results.** The chat model's k=0 misses are near-misses with a flatter first-token
   distribution (entropy 0.76 vs 0.30 nats); dots sharpen it to the base's level. Plain
   rendering drops the chat model to 19 at k=0 and dots still bring it to 44 (format
   interference refuted). The dots-only Qwen gets nothing from letters and is hurt by
   numbers (42 to 30 scrambled) because its answer position reads filler digits as problem
   digits (heads at 0.5).

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

Pre-question placement (fifty items of filler before the variable definitions, chat
model): letters 34, scrambled letters 36, numbers 35, scrambled numbers 28 (5 helped,
11 hurt), against a k=0 baseline of 34 and post-question scores of 42 to 50. The
placement specificity Nicole found for dots (35 → 35) holds for every filler type, and
scrambled numbers before the question mildly hurt.

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
| Llama-3.1-8B-Instruct | 0.44 to 0.59 | 0.44 | F4/5 (22 of 50) |
| Gemma-3-27B-IT | 0.23 to 0.36 | 0.26 | diffuse |
| DeepSeek chat | 0.06 to 0.19 | 0.88 | diffuse |
| DeepSeek base | 0.06 to 0.19 | 0.48 | diffuse |

The trained Qwen that ignores its dots carries one constant problem vector along the
whole span (adjacent cosine 0.8 after centering) and its only change points are a
settling transient in the first ten dots, identical across all 100 items. DeepSeek's
dots are the least redundant position to position of any model here. Redundancy across
the span is a clean signature of not using it.

Llama and Gemma (`run_hf_other_models_cosine.sh`, 50 held-out items, k=50) put 1 to 2
percent of late attention on the dots and get nothing from them behaviorally, yet the
answer is linearly decodable from their dot residuals at 0.84 and 0.81, about what
DeepSeek shows (0.87). Decodability of the answer from the span is therefore not
evidence that the span is used; it is what a residual stream leaks about its context.
The measures that do separate DeepSeek from every non-using model are attention from
the answer positions (0.16 to 0.27 against 0.01 to 0.04) and, within dots, the
non-redundancy of the span (0.06 to 0.19 against 0.23 to 0.77).

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

## The question token without any filler (k=0 dumps)

The 0.74 versus 0.40 question-token probe in the base-checkpoint write-up was measured
with fifty dots present. `run_dsv4_followups.sh` dumps both checkpoints at k=0 (no
filler sentence, no filler in the demonstrations, none in the target) on the same 50
held-out items; `probe_k0_dump.py` fits the same ridge probes. Best R² for the answer:

| condition | position | chat | base |
|---|---|---:|---:|
| k=0 | last question token | 0.84 | 0.84 |
| k=0 | answer cue | 0.83 | 0.83 |
| k=0 | generation position | 0.84 | 0.83 |
| k=50 | last question token | 0.36 | 0.65 |
| k=50 | answer cue | 0.82 | 0.81 |
| k=50 | generation position | 0.82 | 0.84 |

**With no filler in the prompt, the chat model's question token holds the answer exactly
as well as the base's.** The gap between the checkpoints exists only when the filler
scaffold is in the context. The question token precedes the dots, so the dots cannot be
the cause; what differs between k=0 and k=50 is the system sentence announcing fifty
filler tokens and the five demonstrations that contain them. Read that way, the chat
model defers its computation when it is told filler is coming (0.84 to 0.36), and the
base defers less (0.84 to 0.65). This is the deferred-computation hypothesis with a
specific trigger: the announcement, not the tokens.

**The k=0 deficit is not a representation deficit.** At k=0 the answer is decodable at
the generation position at 0.84 in both checkpoints, yet the chat model emits the wrong
number on 15 of 50 items and the base on 2. The failure is between an approximately
correct linear representation and an exactly correct emitted number, consistent with the
near-miss pattern. A ridge probe at R² 0.84 has a residual error of tens of units on
three-digit answers and cannot separate exact from off-by-a-few, so this is as far as
linear probes can take the question.

**Announced but absent.** `run_dsv4_announce.sh` renders the system sentence and the
demonstrations with fifty dots and the target with none (`--announce-filler 50`).

| condition | chat: q_last probe | chat: correct/50 | base: q_last probe | base: correct/50 |
|---|---:|---:|---:|---:|
| plain k=0 | 0.84 | 34 to 35 | 0.84 | 48 |
| announced, absent | 0.31 | 32 | 0.55 | 46 |
| announced, present (k=50) | 0.36 | 49 | 0.65 | 50 |

The announcement alone does it. With fifty dots promised and none delivered, the chat
model's question-token encoding of the answer falls to 0.31, indistinguishable from the
0.36 it shows when the dots are there, and the base's falls to 0.55. Both checkpoints
defer computation away from the question token when told a filler span is coming; the
chat model defers almost completely, the base partly. The answer remains decodable at
the cue and generation positions at 0.79 to 0.83 in every condition, so what moves is
where the value is assembled, not whether it is.

**Deferral is graded by the announced count.** Same design with 5 and 25 announced dots
(`run_dsv4_announce_graded.sh`), none delivered. Best answer probe at the last question
token:

| announced dots (none delivered) | 0 | 5 | 25 | 50 |
|---|---:|---:|---:|---:|
| chat | 0.84 | 0.51 | 0.36 | 0.31 |
| base | 0.84 | 0.86 | 0.85 | 0.55 |

The chat model reads the number in the instruction and defers in proportion: five
promised dots halve its in-place computation, twenty-five bring it to the fifty-dot
level. The base ignores the announcement until it is fifty. This matches the behavioral
curve with dots delivered (45 at k=5, 49 at k=50): whatever span the chat model is
promised, it plans to use.

Accuracy moves much less than the probe: chat 34 to 32, base 48 to 46. Two consequences.
First, the chat model's k=0 deficit is not caused by deferral: it is there at 0.84 and
at 0.31 alike. Second, deferral only pays off when there are positions to defer into.
With the dots present the chat model reaches 49; with them promised and absent it sits at
32. Reading the three rows together: the chat model, once told to expect a span, plans to
finish the arithmetic in it, and emits an approximate answer when the span is missing.
The base does the arithmetic well enough at the question token, or at the cue, that it
does not need the span either way.

## Chat model in plain rendering (format-interference test)

`extract_dsv4.py --render plain` drops the turn markers and the empty think tag and
joins the demonstrations as raw text, the rendering the base model was also run in.

| Visible dots | 0 | 5 | 10 | 25 | 50 | 100 |
|---|---:|---:|---:|---:|---:|---:|
| chat, chat rendering (Nicole) | 35 | 45 | 42 | 43 | 49 | 49 |
| chat, plain rendering | 19 | 23 | 29 | 36 | 39 | 44 |
| base, plain rendering | 47 | 44 | 50 | 47 | 50 | 50 |

Without its chat template the post-trained model gets worse at k=0 (19 against 35), so
the turn markers were helping rather than interfering, and the format hypothesis from
Part VI of the PDF is out. The dot effect survives the change of rendering: 22 helped and
2 hurt at k=50, and the curve keeps rising to 44 at k=100 where the chat-rendered run
saturates at 49. The base is at ceiling in both renderings.

## Which channel carries the announcement

The announced-but-absent prompt carries the announcement in two places: the system
sentence ("there will be 50 filler tokens...") and the five demonstrations, each with
fifty dots between its question and its answer. `build_messages(...,
announce_mode="sentence"|"demos")` separates them; the target has no filler in either.

| condition (target k=0) | chat: q_last probe | chat: correct/50 | base: q_last probe | base: correct/50 |
|---|---:|---:|---:|---:|
| nothing announced | 0.84 | 34 | 0.84 | 48 |
| sentence only | **0.83** | **28** | 0.84 | 50 |
| demonstrations only | **0.40** | **34** | 0.55 | 46 |
| both | 0.31 | 32 | 0.55 | 46 |

A double dissociation. The demonstrations move the computation off the question token
(0.84 to 0.40 in chat, 0.84 to 0.55 in base) and leave accuracy alone. The sentence
leaves the question token alone and costs the chat model six items (34 to 28), its
worst score in any condition, while the base is unaffected (50). So the "deferral"
measured all day is in-context format learning: five examples of question, span,
answer teach both checkpoints, the chat model more strongly, to finish the arithmetic
after the question rather than at it. The graded result (0.51, 0.36, 0.31 for 5, 25,
50 announced) was graded by the demonstrations' span length. The instruction sentence
does something different: it degrades the post-trained model's answer without changing
where the answer is computed, and it does nothing to the base.

With fifty dots delivered in the target (chat model), the full 2×2:

| announced by | k=0 | k=50 delivered | helped/hurt |
|---|---:|---:|---|
| nothing (dots only in the target) | 34 | 39 | 9/4 |
| sentence only | 28 | 36 | 11/3 |
| demonstrations only | 34 | 47 | 13/0 |
| both | 34 to 35 | 49 | 14/0 |

Unannounced dots help a little (34 to 39, McNemar p=0.27). Demonstrations of a span being
used make them nearly fully effective (47). The sentence, which hurts on its own, adds
the last two items when the demonstrations are there. The span is most useful to a model
that has seen examples of a span being used, which is the same channel that moved its
computation off the question token.

**What the demonstrations do is not visible in attention.** With demonstrations-only
announcement, the question token's late-block attention on the demonstrations' 250
filler tokens is 0.16 in chat and 0.21 in base (peak 0.39 and 0.35, both at block 38),
at or below those tokens' share of the keys (about 0.32), and attention on the
demonstrations' answer cues is 0.01 in both. Neither checkpoint reads the demonstration
spans specially, and they do not differ. Whatever the demonstrations do to the question
token's computation, it is not carried by attention from the question token to the
spans; it stays unlocated (`results/filler-cosine/demo-attention.md`).

This corrects the reading in the previous section. The chat model's heads that read the
sentence from block 20 on are real, but they are not the deferral mechanism; if
anything they are the mechanism of the sentence's cost to accuracy. What the
demonstrations do to the question token has yet to be located.

## Where the announcement is read (the sentence)

`dump_dot_attention_dsv4.py` now attributes keys to a sixth region, the 21-token filler
sentence in the system message, and handles k=0. Mass on that sentence from the last
question token, mean over 64 heads and 50 held-out items (uniform attention over the
roughly 800 prefix tokens would give 0.026):

| block | 14 | 20 | 22 | 24 | 26 | 28 | 32 | 34 | 38 | 40 | 42 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| chat, announced (absent or delivered) | 0.007 | 0.039 | 0.039 | 0.039 | 0.055 | 0.010 | 0.066 | 0.060 | 0.062 | 0.173 | 0.010 |
| base, announced (absent or delivered) | 0.006 | 0.003 | 0.005 | 0.008 | 0.009 | 0.005 | 0.009 | 0.007 | 0.030 | 0.082 | 0.014 |
| single most attentive head, chat | 0.04 | 0.16 | | 0.16 | | 0.04 | 0.25 | | | 0.38 | |
| single most attentive head, base | 0.03 | 0.03 | | 0.03 | | 0.01 | 0.03 | | | 0.19 | |

The values are identical whether the dots are delivered or not, as they must be (the
question token precedes them). The chat model's question token reads the announcement
above chance from block 20 and six times chance at block 40, with single heads at 0.16
to 0.38; the base's question token ignores it until block 38 and reads it at half the
chat model's level at block 40. The sentence is about 600 tokens before the question,
outside the 128-token window, so this is attention through the compressed keys, which
the indexer selects in the even blocks (20, 22, 24, 26, 32, 34, 38, 40 are all even).
Post-training installed, or strengthened, heads in blocks 20 to 40 that read the filler
instruction at the question token. Given the channel decomposition above, these heads
are not what defers the computation (the demonstrations do that); they are the chat
model's route to the instruction whose presence costs it six items. Attention from the
cue and generation positions to the sentence is 0.02 in both checkpoints.

Results: `results/filler-cosine/announce-attention.md`, dumps under
`results/deepseek-v4-flash{,-base}/announce-attn-{k0,announce50-k0,k50}/`.

## First-token distributions (no GPU; from the sweep files)

Top-10 tokens at the answer position, mean over the 50 released items.

| condition | top-1 prob | p(correct token) | p(correct) on misses | top-10 entropy (nats) | median rank of correct on misses |
|---|---:|---:|---:|---:|---:|
| chat, k=0 | 0.74 | 0.60 | 0.12 | 0.76 | 3 |
| chat, announced but absent | 0.60 | 0.51 | 0.11 | 1.13 | 3 |
| chat, k=50 dots | 0.92 | 0.92 | 0.22 | 0.26 | 2 |
| base, k=0 | 0.89 | 0.88 | 0.30 | 0.30 | 2 |
| base, k=50 dots | 0.90 | 0.90 | | 0.29 | |

The chat model at k=0 is genuinely less certain than the base: its first-token
distribution is three times flatter and every miss still has the correct number in
the top few. Fifty dots sharpen it to the base's level. Announcing filler that never
comes flattens it further. This is the confidence-recalibration description from Part VI
of the PDF, and it sits on top of the deferral result: told to expect a span, the model
postpones the computation, and with no span it emits its best approximation with low
confidence. All 15 chat misses at k=0 have a number as the top token; none is a refusal
or a format token.

## Artifacts

- `results/filler-cosine/dots/`, `results/filler-cosine/qwen-dots/` (JSON, markdown, figures)
- `results/deepseek-v4-flash{,-base}/varbind-eval-<type>/` behavioral sweeps
- `results/deepseek-v4-flash{,-base}/filler-dump-<type>/{analysis,cosine}/` anatomy per type
- `results/qwen3.5-9b/filler-types/{base,dotsonly}/varbind-eval-<type>/` and `.../filler-dump-<type>/{analysis,cosine}/`
- Announced-but-absent: `results/deepseek-v4-flash{,-base}/{varbind-eval-announce50-k0,k0-announce50-dump}/`, `results/filler-cosine/k0-announce-probes.md`
- Channel decomposition: `results/deepseek-v4-flash{,-base}/{varbind-eval-announce50-{sentence,demos}-k0,k0-announce50-{sentence,demos}-dump}/`, `results/filler-cosine/k0-announce-channel-probes.md`
- k=0 dumps and probes: `results/deepseek-v4-flash{,-base}/k0-dump/`, `results/filler-cosine/k0-probes.md`
- Llama-3.1-8B-Instruct and Gemma-3-27B-IT dot dumps: `results/{llama3.1-8b-it,gemma-3-27b-it}/dot-dump/{analysis,cosine}/`
- Cross-type tables: `results/filler-cosine/summary-deepseek.md`, `results/filler-cosine/summary-qwen.md`
