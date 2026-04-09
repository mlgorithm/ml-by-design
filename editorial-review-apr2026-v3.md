# Editorial Review: Machine Learning by Design

**From Problem Framing to Reliable Systems**
**Author: Sam Urmian**

**Review date:** April 9, 2026 (v3)
**Reviewer:** Claude (co-author/editor)
**Scope:** Full editorial review — all chapters (including new Ch 4b and Ch 6b), bridge chapters, part syntheses, frontmatter, backmatter, and cross-chapter coherence

---

## Executive Summary

"Machine Learning by Design" has matured significantly since the last editorial pass. The two new chapters — Ch 4b (Designing the Dataset) and Ch 6b (Learning from Interaction: Reinforcement Learning) — are substantial, well-integrated additions that fill genuine gaps in the book's coverage. Nearly all items flagged in the April 2026 v2 review have been addressed, and the manuscript's core strengths remain intact: problem-first orientation, artifact-driven pedagogy, technical accuracy, and clear prose.

The book now spans 2 bridge chapters, 14 content chapters, 4 part syntheses, and supporting materials. The artifact chain is complete from framing memo through readiness brief. The seven-question framework is visible throughout. Both running cases (course-support assistant, pedestrian detector) are well-sustained across all four parts.

**Overall assessment: The book is ready for publication.** The issues below are refinements — no factual errors of substance were found. Recommendations are organized by priority.

---

## Chapter-by-Chapter Ratings

| Section | Clarity | Accuracy | Completeness | Exercises | Overall |
|---------|---------|----------|--------------|-----------|---------|
| Bridge I: Linear Algebra | Excellent | Excellent | Very Good | Excellent | 9/10 |
| Bridge II: Probability & Risk | Excellent | Excellent | Very Good | Strong | 9/10 |
| Ch 1: Framing Learning Problems | Excellent | Excellent | Excellent | Strong | 9/10 |
| Ch 2: Metrics & Evaluation | Strong | Excellent | Excellent | Strong | 8.5/10 |
| Ch 2b: Generalization & Evaluation | Excellent | Excellent | Excellent | Excellent | 9/10 |
| Ch 3: Structure Beyond Linearity | Strong | Excellent | Good | Strong | 8/10 |
| Ch 4: Model Selection by Structure | Strong | Excellent | Good | Good | 8/10 |
| **Ch 4b: Designing the Dataset** | **Excellent** | **Excellent** | **Excellent** | **Strong** | **9/10** |
| Ch 5: Optimization & Neural Networks | Strong | Good* | Good | Strong | 8/10 |
| Ch 6: Representation & Foundation Models | Excellent | Excellent | Very Good | Strong | 9/10 |
| **Ch 6b: Learning from Interaction (RL)** | **Excellent** | **Excellent** | **Very Good** | **Strong** | **8.5/10** |
| Ch 7: Vision | Excellent | Excellent | Very Good | Excellent | 9/10 |
| Ch 8: Language | Excellent | Excellent | Very Good | Excellent | 9/10 |
| Ch 9: Audio & Time | Excellent | Excellent | Very Good | Strong | 9/10 |
| Ch 10: Experiments & Claims | Excellent | Excellent | Excellent | Excellent | 9/10 |
| Ch 11: Reliability | Strong | Excellent | Good | Good | 8/10 |
| Ch 12: From Models to Systems | Strong | Excellent | Good | Good | 8/10 |
| Part Syntheses | Strong | N/A | Good | N/A | 8/10 |
| Frontmatter & Backmatter | Excellent | Good* | Strong | N/A | 8.5/10 |

*Minor imprecisions noted; see details below.

---

## Status of Previously Flagged Items (v2 Review)

Of the 46 items flagged in the v2 review, the majority have been addressed:

### Resolved ✓

- **Bridge I:** Diverse representation card examples (spam filtering added)
- **Bridge II:** Sigmoid motivation strengthened, SGD acknowledged, forward-reference table added
- **Ch 1:** Pedestrian detector previewed earlier, seven-question framework stated explicitly
- **Ch 2:** Multi-class metrics note added (macro/micro averaging named)
- **Ch 2b:** Shuffled-label check guidance deepened
- **Ch 5:** Nonlinearity statements corrected, batch norm training/inference asymmetry now explicit, gradient clipping mentioned, weight initialization covered (He, Xavier)
- **Ch 6:** Terminology drift addressed with explicit definitions (representation/embedding/features), self-supervision clarified early, autoencoder bottleneck expanded, catastrophic forgetting discussed, few-shot learning covered, pretraining terminology distinguished
- **Ch 7:** Padding/boundary-effects note added
- **Ch 8:** Static embeddings expanded (polysemy example), decoding-strategy example added, probability notation unified
- **Ch 9:** Drift detection formalized (three monitoring strategies)
- **Ch 10:** "Slices" and "subgroups" linked as interchangeable in Ch 11
- **Ch 11:** Equalized-odds vs. demographic-parity worked example added, adversarial robustness acknowledged
- **Ch 12:** Feedback loops covered, pedestrian-detector walkthrough added, circle closed with Ch 1

### Partially Addressed ~

- **Ch 5:** Score vs. logit terminology — logit formally introduced but still used interchangeably with "score" in some passages
- **Ch 7:** Transfer-learning coverage expanded with practical notes on frozen vs. fine-tuned backbones, but still lacks a concrete worked example (e.g., ImageNet → medical imaging)
- **Ch 9:** Memory-architecture progression covers RNN → LSTM → Transformer but omits HMMs
- **Part syntheses:** Modestly expanded (~13–15 lines vs. prior ~12) with running-case references and next-part previews, but room remains for further expansion
- **About-author DBLP error:** Resolved (link removed), but repository name typo "ml-by-desing" persists

### Not Yet Addressed ✗

- **Ch 5:** Numerical learning-rate exercise not added
- **Ch 5:** Loss-curve interpretation exercise not added
- **Ch 11:** Causal vs. statistical fairness distinction not explicit (deferred to Ch 10's causal-inference section without cross-reference)

---

## New Chapters: Detailed Assessment

### Chapter 4b: Designing the Dataset

This is a major, well-executed addition. It treats dataset construction with the seriousness it deserves — framing data as a design choice, not a given.

**Strengths:**

- Opens with the correct positioning: "Data is not a given — it is a design choice"
- Comprehensive coverage: annotation protocols, inter-annotator agreement (kappa, alpha), label noise types (symmetric/asymmetric), class imbalance handled contextually rather than prescriptively, active learning strategies, data augmentation validity, synthetic data risks (sim-to-real gap, mode collapse)
- The Data Design Card artifact is a valuable addition to the artifact chain
- Both running cases (course-support, pedestrian detector) are used effectively
- Evidence boxes cite appropriate literature (Northcutt et al. on CIFAR-10 label errors, CARLA sim-to-real)

**Minor issues:**

- Exercise prompts could specify which "public dataset" to use for annotation audit exercises
- Label-smoothing not mentioned in the noise-robustness section — worth a sentence alongside focal loss
- Soft-labels discussion (genuine ambiguity vs. noise) is well-handled but could cross-reference the calibration discussion in Ch 2

### Chapter 6b: Learning from Interaction — Reinforcement Learning

This chapter fills the RL gap that was previously handled only by a brief orientation in Ch 1. It's well-integrated with the representation-learning arc of Part II.

**Strengths:**

- Excellent opening dilemma contrasting prediction and action
- MDP formalization is rigorous yet accessible (Bellman equation in mathlens with side explanation)
- RLHF integration connects naturally back to Ch 6's foundation models
- Reward misspecification gets heavyweight treatment (Goodhart's law, real failure patterns, audit checklist)
- The Interaction Design Card artifact is methodical: state, action, reward, exploration, evaluation, guardrails
- "Common Mistakes" section is exceptionally practical

**Issues worth addressing:**

- Q-learning appears only as an advanced note; policy gradient is brief; actor-critic lacks a worked example
- Exploration-exploitation discussion is strong for discrete action spaces but the shuttle case (continuous) doesn't get a concrete continuous-control exploration example
- RLHF reward-model hacking section is underdeveloped — a concrete example of how a language model might "game" a learned reward would strengthen it
- No code-based implementation exercise (e.g., "implement Q-learning on a simple grid")
- Partial-observability mitigation beyond "invest in better sensors" could mention latent-state models or frame-stacking

---

## Top-Priority Issues (New)

### 1. Repository Name Typo Persists

The GitHub URL in preface.tex still references "ml-by-desing" (missing 'n' in "design"). This appears in both the publicized URL and the actual directory name. If the repo has genuinely been named this way, note it explicitly; otherwise, correct it.

### 2. Chapter 5: Missing Exercises

Two exercises flagged in v2 remain absent and would meaningfully strengthen the chapter:

- **Numerical learning-rate exercise:** Students compute gradient descent steps with different learning rates on a toy problem to feel the effect of too-large vs. too-small rates.
- **Loss-curve interpretation exercise:** "Given a learning curve where training loss decreases but validation loss increases after epoch 10, explain the failure type and propose one intervention."

### 3. Chapter 11: Cross-Reference to Causal Fairness

Ch 10 has a substantial causal-inference section (covering confounders, Simpson's paradox, and causal-inference methods). Ch 11 treats fairness metrics as purely statistical. Adding one sentence in Ch 11 — "For cases where fairness requires causal evidence, see Chapter 10's causal-inference section" — would strengthen coherence between these closely related chapters.

### 4. Chapter 5: Score vs. Logit Terminology

"Logit" is formally introduced but still used interchangeably with "score" in several passages. A brief clarifying note early in the chapter (e.g., "We use 'logit' for the raw output of a linear layer before activation, and 'score' informally when the distinction does not matter") would resolve this.

---

## High-Priority Recommendations

### Part I

1. **Ch 3 — Add forward-reference table.** Both bridge chapters now have forward-reference tables showing where their topics return. Ch 3 (linear models, features, separability) would benefit from the same treatment.

2. **Ch 4b — Mention label-smoothing.** Alongside focal loss and noise-robust losses, a sentence on label-smoothing as a regularization technique that also helps with noisy labels would be useful.

### Part II

3. **Ch 5 — Clarify backpropagation efficiency.** The chapter explains what backpropagation does but still doesn't explicitly state why it's efficient (one forward + one backward pass vs. one forward pass per parameter for numerical differentiation).

4. **Ch 6b — Add concrete RLHF gaming example.** The reward-model-hacking section lists mitigation bullets but no concrete example of how a language model might exploit a reward model (e.g., producing verbose but vacuous responses that score high on helpfulness proxies).

5. **Ch 6b — Add one continuous-control exploration example.** The shuttle case is continuous but exploration strategies discussed (epsilon-greedy, UCB, Thompson) are discrete-focused.

### Part III

6. **Ch 7 — Add concrete transfer-learning worked example.** Lines 432–438 provide practical guidance on frozen vs. fine-tuned backbones, but a brief worked scenario (e.g., "A team fine-tunes an ImageNet backbone for chest X-ray classification...") would make the advice tangible.

7. **Ch 8 — Mention beam search.** The decoding section shows greedy, sampling, and temperature but omits beam search, which remains common in translation and summarization.

8. **Ch 9 — Add 2–3 sentences on HMMs.** The memory-architecture progression jumps from generic "sequence models" to RNNs. A brief mention of HMMs as a historical bridge (discrete latent states, Markov assumption, forward-backward algorithm) would contextualize the deep-learning alternatives.

### Part IV

9. **Ch 10 — Add nested-selection diagram.** The concept is well-explained in text but a visual showing the inner validation loop inside the outer test fold would help — this is a perennial point of confusion for students.

10. **Ch 12 — Add concrete "narrowed scope" example in closing.** The closing perspective asks whether the readiness brief confirms, narrows, or rejects the original framing memo. A one-sentence example (e.g., "The support assistant was designed to handle all student inquiries; the readiness brief narrows this to routine policy questions, with high-risk cases escalated") would make the callback concrete.

---

## Medium-Priority Recommendations

### Notation & Consistency

11. **Ch 5:** Loss notation — both `L` and `ℒ` still appear. Both are used correctly in their respective contexts, but a brief note on the convention (e.g., ℒ for the full objective, L for a single-sample loss) would prevent confusion.

12. **Ch 9:** Multimodal and graph-neural-network sections feel somewhat tangential to the chapter's core "prediction-time realism" theme. Consider adding a transition paragraph that explicitly connects these topics to the prediction-time audit concept.

### Completeness Gaps

13. **Ch 5 — Learning-rate scheduling.** Warmup, cosine annealing, and step decay are conceptually mentioned but no concrete examples. A brief practical note would help.

14. **Ch 6 — Reusability conditions table.** Table 125 gives four conditions for when representations transfer well. Missing: guidance on what to do when one condition fails.

15. **Ch 6b — Partial observability.** Beyond "invest in better sensors," mention latent-state models or frame-stacking as practical RL workarounds.

16. **Ch 8 — Hallucination risk timing.** The hallucination discussion appears late in the chapter (around line 838). A brief forward reference earlier — when grounding is first introduced — would prime readers.

17. **Ch 9 — Drift-detection thresholds.** The three monitoring strategies are listed but guidance on threshold-setting (when does a sustained decline trigger an alert?) is absent.

18. **Ch 11 — Pedestrian-detector privacy threat model** is briefer than the support-assistant case. One or two additional sentences on re-identification risk from video would balance the treatment.

### Exercises

19. **Ch 4b:** Exercise prompts should specify which public dataset to use (CIFAR-10, ImageNet, etc.) rather than leaving it open.

20. **Ch 6b:** Add one code-based implementation exercise (e.g., "Implement Q-learning for a 4×4 grid world").

21. **Ch 9:** Add a worked example of a drift-detection failure case.

---

## Book-Level Strengths

These qualities remain the book's distinctive contributions and should be preserved through any revision:

1. **Problem-first orientation.** No chapter begins with architecture names. Each starts with a problem and derives tools as responses.

2. **Artifact-driven pedagogy.** The chain of reusable deliverables — now expanded with the Data Design Card (Ch 4b) and Interaction Design Card (Ch 6b) — is a genuine pedagogical innovation. The full chain runs: Representation Card → Framing Memo → Metric-Action Worksheet → Evaluation Plan → Feature Design + Baseline Sheet → Structural Diagnostic → Data Design Card → Neural Report → Reuse Plan → Interaction Card → Vision Card → NLP Context Card → Sequential Card → Claim Sheet → Reliability Card → Readiness Brief.

3. **Seven-question framework.** Well-articulated, staged intelligently across chapters, and now explicitly visible in the early chapters.

4. **Running cases.** The course-support assistant and pedestrian detector are complex enough to illustrate real concerns and accessible enough for students to follow. Ch 9's audio and forecasting cases add effective breadth.

5. **New chapters strengthen the arc.** Ch 4b (dataset design) fills a critical gap — treating data as a design choice rather than a given. Ch 6b (RL) completes the Part II progression from learned features → reusable representations → learning from interaction.

6. **Evidence discipline.** The insistence that every claim must be bounded, that metrics must be paired with actions, and that evaluation must respect deployment conditions sets a professional standard rare in introductory textbooks.

7. **Honest engagement with failure.** Shortcut learning (Ch 7), hallucination (Ch 8), temporal leakage (Ch 9), reward misspecification (Ch 6b), and reliability failures (Ch 11) are treated as central problems, not afterthoughts.

8. **Technical accuracy.** No mathematical errors of substance were found across the entire manuscript. Definitions are precise. Theorems are correctly stated.

9. **Clear, engaging prose.** Active voice dominates. The book reads well from cover to cover.

10. **Cross-chapter coherence.** Terminology is disciplined. The artifact chain is complete. Forward references and part syntheses provide orientation. The closing perspective in Ch 12 explicitly connects back to Ch 1's framing memo.

---

## Conclusion

"Machine Learning by Design" has grown from an already-strong manuscript into a comprehensive, coherent textbook. The two new chapters (4b and 6b) are among the book's best — Ch 4b in particular fills a gap that most ML textbooks ignore entirely. Nearly all previously flagged items have been thoughtfully addressed.

The top-priority items (repository typo, two missing exercises in Ch 5, a cross-reference in Ch 11, and terminology clarity in Ch 5) can be addressed quickly. The high-priority items (concrete examples for transfer learning, RL gaming, and the Ch 12 closing; a nested-selection diagram; HMM mention) would strengthen an already strong manuscript. The medium-priority items are polish.

The book is ready for serious pedagogical use.
