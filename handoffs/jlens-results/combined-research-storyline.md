# Why filler helps: from a causal workspace to context-dependent reliance

Proposed narrative integrating Nick's Google Doc draft (the `draft` tab, read September 4, 2026 local time), the repository reports, and Nicole's historical experiment summary. This is an explanatory order for the write-up, not a claim that the two collaborators ran every experiment in this exact chronological sequence. Later direction/stream interventions are supported here by the conversation handoff; their raw artifacts have not been independently re-audited for this synthesis.

## Central question

Why do semantically uninformative positions after a question improve DeepSeek V4 Flash's answers? What information do those positions carry, does the model actually use it, and why does its performance depend on having that space?

The distinction between **using a workspace** and **needing a workspace** is the thread connecting the project. Our causal studies establish useful filler state. The base/chat and context comparisons show that useful filler state alone does not explain the chat model's accuracy gain.

## 1. First, find an effect that is strong enough to explain

We began with a measurement question: can a released pretrained Jacobian Lens reveal intermediate values at filler positions? We validated the extraction on ordinary prompts, then on atomic-number addition. J-Lens recovered relevant facts, but successful answers with and without dots did not establish that the dots helped. Three-fact addition sometimes exposed a correct candidate even when the model answered incorrectly.

That led to a behavioral screening step. Modular squaring, pointer chasing, arithmetic programs, letter selection, and branching tasks were too difficult, too easy, or showed weak or negative filler effects. Variable binding was the clear positive case: DeepSeek had to compute a number, bind it to a variable, and use that value in another calculation.

On the first 50 items, accuracy rose from 70% without dots to 98% with 50 post-question dots. On an independent 100-item cohort, it rose from 59% to 94%. Putting the dots before the question did not reproduce the first cohort's gain.

**Transition:** We now had a reproducible, placement-sensitive behavior. The next question was what the downstream filler positions contributed.

## 2. Look for the intermediate computation

We decoded the same layer-by-position activations with J-Lens and logit lens. Starting values appeared earlier in depth, intermediate bound values later, and answer candidates later still. These stages did not march reliably from dot 1 to dot 2 to dot 3. Values appeared at multiple nonadjacent positions, and more dots often produced more readable copies.

Some failures already contained a readable correct answer. One dot-length sweep alternated between a correct and a sibling-consistent wrong answer; both candidates were visible at longer lengths. Sparse J-space decomposition provided a selective view of a few cells, but reconstructed only a small portion of the activation and did not uniquely identify its content.

**What changed in our thinking:** A grid of readable numbers is not yet an algorithm or a causal explanation. We needed to test whether the states carrying those numbers affected the answer.

## 3. Test whether the workspace is causally useful

We constructed donor and target prompts differing in one input token while holding token positions fixed, then transplanted donor filler states into the target. J-Lens-selected states could strongly increase the donor answer's probability; a 16-cell intervention moved it from rank 82 to rank 2 in one direction. Logit-lens-selected locations were often similarly effective.

Moving the same donor state across destination dots showed that the information was portable. In six tested directions, all 300 answer-state destinations increased donor-answer probability, although late destinations were often stronger. Attention interventions also disrupted the filler benefit. On 35 examples selected because 50 dots rescued them, restricting exact local access to two predecessor dots retained 80% accuracy, compared with 100% under full history. Other attention routes remained available.

**Conclusion:** Filler positions carry causally usable information, often at multiple locations, and recent local communication supports much of the benefit in the selected cohort. This establishes how the workspace participates without assigning a fixed arithmetic step to each dot.

## 4. Separate readable information from operational information

Whole-state patching left an ambiguity: did the decoded token direction carry the effect, or did J-Lens merely locate a useful state?

We directly suppressed and amplified selected J-Lens token scores, then decomposed donor–target state differences into a small expected-token span and its orthogonal remainder. Local readouts changed substantially while answers were often robust. The tested token span accounted for much of the readout change but little causal transfer; the remainder retained roughly 80% of transfer in the pilot summary. Stream interventions further separated which components changed the readout from which changed the answer.

**Conclusion:** J-Lens is useful for reading and selecting states, but its token directions are not a complete account of their causal content. These experiments did not establish broad J-Lens superiority over logit lens.

**Transition:** We had evidence that DeepSeek used the span. That still left the bigger question: why did it benefit so much from having one?

## 5. Ask whether other models naturally show the same reliance

Nick screened ten smaller open models across multiple families, including dense and MoE models. They did not show a robust placement-specific filler benefit on the tested two-step task. Because many were near floor, easier one-step versions were necessary; those likewise did not produce a robust benefit in the tested conditions, though some were ceiling-limited.

**Conclusion:** The effect was not a generic outcome of appending tokens in this screen. The comparison did not establish uniqueness to DeepSeek or rule out architectural contributions.

**Transition:** Perhaps these models had the necessary capability but had never learned to use filler positions. We tested that with training.

## 6. Try to teach workspace use

Answer-only LoRA training improved Qwen's task performance, including when training prompts always contained dots. But the improvement transferred to no-dot prompts. The dots-only model scored 40/50 without dots, despite never seeing that condition during its fine-tune. All-dot residual lesions produced small effects on a small selected cohort; the zero-lesion control changed 2/12 greedy outputs, so the dots should not be described as perfectly inert.

**Conclusion:** This training recipe mostly taught task competence that did not depend on the filler content. Training with a workspace present does not guarantee learning to use it. It does not rule out other supervision or training regimes.

**Transition:** We could now compare a model that solved the task while largely tolerating dots with one whose performance strongly benefited from them.

## 7. Compare the internal use of dots, then test the base checkpoint

Attention and representation measurements differed: trained Qwen's dots were largely position-dominated and weakly attended, while DeepSeek's received substantial attention and carried problem-related information. Yet linear answer probes could score highly even on models with little behavioral filler benefit. This reinforced our causal lesson: decodability is not sufficient evidence of use.

The decisive comparison was DeepSeek's released base checkpoint. On the same 50-item setup, it scored 48/50 without dots and 50/50 with 50 dots, while chat scored 35/50 and 49/50. The base also attended to filler and supported answer readouts there.

**What changed in our thinking:** Workspace-like behavior is present before post-training. The large gain in the chat model partly reflects its lower no-filler baseline. The question becomes why the released chat checkpoint is less reliable without the span, rather than whether its architecture fundamentally cannot solve the task without extra positions.

This comparison points toward post-training-related differences, but does not identify a particular training stage or objective. The released checkpoints also differ in expert quantization, and the base is near ceiling here.

## 8. Test whether the span contains a special ordered code

Dots were replaced with letters, numbers, and scrambled sequences. Numbers could work about as well as dots; letters were less effective. Natural sequence order was not required for the strong number-filler result. Adjacent-position cosine did not reveal a consistent progression of reasoning boundaries; several obvious boundaries came from tokenization.

**Conclusion:** The benefit does not require a meaningful counting sequence or a unique dot symbol. Token identity still matters, and these comparisons are not a fully controlled token-budget experiment.

Low cosine between neighboring full states does not contradict repeated task values or portable causal content. The metrics ask different questions: two high-dimensional states can both carry useful information about the same value without being nearly identical vectors.

**Transition:** If the span is not supplying a special ordered code, perhaps the context controls how the model makes use of the available positions.

## 9. Separate the target span from the context that announces it

The important clue came from the last question token, which occurs before target filler. Its representation cannot depend on target dots that follow it. Any difference there between the standard k=0 and k=50 prompts must arise from changes earlier in the context, such as instructions and demonstrations.

With no filler anywhere, the answer probe at the last question token reached about R²=0.84 in both chat and base. Showing filler in the context while withholding it from the target reduced the chat model's question-token answer decodability. This made the earlier fixed-deficit interpretation inadequate: the readout gap depended on prompt context.

We then separated the explicit sentence from the dotted demonstrations:

| Target has no filler | Chat question-token answer probe R² | Correct / 50 |
|---|---:|---:|
| Nothing announced | 0.84 | 34 |
| Sentence only | 0.83 | 28 |
| Demonstrations only | 0.40 | 34 |
| Both | 0.31 | 32 |

When 50 target dots were supplied, the reported scores were 39/50 with neither channel, 36/50 with the sentence only, 47/50 with demonstrations only, and 49/50 with both.

**Conclusion:** Demonstrations strongly change early answer decodability and are associated with much greater usefulness of the delivered span. The explicit sentence has a different effect. This supports context-dependent organization of useful filler computation.

But the dissociation is essential: demonstrations-only leave no-filler accuracy unchanged despite changing the probe, whereas sentence-only lower accuracy without changing that probe much. Therefore the probe shift is not an established explanation of the chat model's no-filler accuracy deficit. A linear probe on this affine task also cannot uniquely locate when the arithmetic was computed.

## 10. End at the boundary the experiments actually reached

We established a causal filler workspace and found that its usefulness depends on model, training, and prompt context. The base/chat comparison shows that a large filler gain need not reveal an underlying inability of the pretrained network to solve the task without filler. The channel experiment narrows the context effect to demonstrations for the question-token readout, while showing that answer accuracy can change through a separate route.

The remaining problem is to connect these levels causally: which internal mechanism makes the demonstrations alter the representation, and which mechanism makes a readable approximate answer become an incorrect emitted number? Attention to the instruction sentence is a candidate for intervention, not a demonstrated causal answer. Direction and stream tests explain why we should not expect a single token readout to settle these questions.

## Suggested opening paragraph

We began by asking whether Jacobian Lens could reveal the computation hidden in filler tokens. After finding a strong behavioral effect on variable binding, we used readouts and interventions to show that DeepSeek carries causally useful information across the filler span. But identifying a workspace did not explain why the model benefited from it. Comparisons with other models and answer-only fine-tuning showed that neither solving the task nor seeing dots during training guaranteed filler use. The strongest change in perspective came from DeepSeek's base checkpoint, which already solved the task reliably without dots while exhibiting similar filler readouts and attention. We therefore separated the available workspace from the prompt context that encourages its use. Demonstrations changed question-token answer decodability and made delivered filler much more effective, while the explicit instruction had a different effect on accuracy. Our results connect a causal workspace to context-dependent reliance on it, but leave the exact mechanism of that reliance unresolved.

## Editorial fixes to Nick's draft

1. Replace “we fitted a Jacobian lens” with “we used a released pretrained Jacobian lens.”
2. Replace “J-Lens added nothing” with “J-Lens did not establish a broad advantage over logit lens; it supported location selection and direct tests of the limits of readable token directions.”
3. Replace “fifty forward passes” with “fifty additional causal positions.” Prefilled dots add sequence positions evaluated through the same stack, not fifty whole-network reasoning iterations.
4. Replace “no open model does it” with “none of the ten smaller open models in our screen showed a robust effect under the tested conditions.”
5. Replace “post-training caused deferral, which explains the 70%” with the narrower base/chat finding and the separate prompt-channel dissociation. The draft's own results show no-filler errors with both high and low question-token probe scores.
6. Avoid “binding is always right” based only on failed matches to alternative variable answers; a finite error taxonomy does not identify every latent operation.
7. Do not call the demonstration-length probe response proportional or strictly monotonic: demonstrations-only scores are 0.84, 0.49, 0.33, 0.40 at 0, 5, 25, 50 dots.
8. Distinguish mean and zero lesions in the Qwen control, and avoid treating every small effect as exactly zero.
9. Reconcile the combined-channel no-filler baseline: the channel experiment reports 32/50, while the delivered-span summary pairs “both” with 34–35/50. Do not draw a matched arrow between conditions from different prompt configurations without checking their rendered prompts and example-level records.
10. Keep statistical geometry and causal stream roles separate. A stream's large position-related variance does not rule out a smaller content component that strongly changes a token readout.

## Evidence map and figure order

| Narrative stage | Evidence | Suggested main figure |
|---|---|---|
| A behavior worth explaining | Initial, independent, and placement sweeps | Accuracy by dot count and placement |
| What filler carries and uses | Layer maps, counterfactual patching, portability | One readable chain plus causal patch/receiver map |
| Readability versus use | Direction/state pilots; cross-model probes | Whole-state effect versus token-span effect |
| Generality and learning | Smaller-model screen; paired LoRA controls | Screen plus dots-only/no-dots evaluation |
| Why dependence is surprising | DeepSeek base/chat comparison | Matched accuracy and attention/readout comparison |
| Context changes usefulness | Announced-but-absent and channel split | Separate panels for probe R² and accuracy |

Task screening, sparse decomposition, candidate competition, filler identity, cosine, and detailed stream dissection can support the main account without each becoming a separate headline. Keep enough of the causal material in the main text to establish that the workspace is useful; otherwise the narrative collapses into an association between prompt formatting and probes.

## Sources

- [Nick's draft tab](https://docs.google.com/document/d/1Ur0Ya0UrTZxb_Vb2eKgRy4FStyFvebfiVJWk-XwhG9U/edit?tab=t.cu68q46gw23i)
- [Workspace and algorithm findings](../../reports/algorithm-exploration-findings.md)
- [Open-model, training, and base-checkpoint report](../../reports/small-open-model-null-result.md)
- [Filler types and announcement-channel report](../../reports/filler-types-and-cosine.md)
- [Historical complete results handoff](jlens-results-handoff.md)

The source reports contain evolving interpretations; later controlled results take precedence over earlier explanations. This synthesis reads the reports and draft, and does not claim a fresh audit of every raw experiment.
