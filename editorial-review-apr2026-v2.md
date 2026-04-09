# Editorial Review: Machine Learning by Design

**From Problem Framing to Reliable Systems**
**Author: Sam Urmian**

**Review date:** April 9, 2026
**Reviewer:** Claude (co-author/editor)
**Scope:** Full editorial review — all chapters, bridge chapters, frontmatter, backmatter, appendices, and cross-chapter coherence

---

## Executive Summary

"Machine Learning by Design" is an exceptionally well-crafted textbook that genuinely delivers on its concept-first, problem-driven promise. Across 2 bridge chapters, 12 content chapters, 4 part syntheses, and supporting materials, the book maintains a coherent pedagogical arc: from framing learning problems, through modeling and evaluation, to deployment-ready systems thinking.

The writing is clear, technically accurate, and accessible to its target audience (CS undergraduates, IOAI students, self-learners). The artifact-driven pedagogy — where each chapter produces a reusable deliverable (framing memo, design card, claim sheet, readiness brief) — is a genuine innovation that distinguishes this book from algorithm-catalog alternatives.

**Overall assessment: The book is ready for publication.** The issues identified below are refinements, not fundamental revisions. No technical errors of substance were found. The recommendations are organized by priority to support efficient revision.

---

## Chapter-by-Chapter Ratings

| Section | Clarity | Accuracy | Completeness | Exercises | Overall |
|---------|---------|----------|--------------|-----------|---------|
| Bridge I: Linear Algebra | Excellent | Excellent | Very Good | Excellent | 9/10 |
| Bridge II: Probability | Excellent | Excellent | Very Good | Strong | 8.5/10 |
| Ch 1: Framing Learning Problems | Excellent | Excellent | Good | Strong | 8.5/10 |
| Ch 2: Prediction, Loss, Decision Rules | Strong | Excellent | Good | Strong | 8/10 |
| Ch 2b: Generalization & Evaluation | Excellent | Excellent | Excellent | Excellent | 8.5/10 |
| Ch 3: Structure Beyond Linearity | Strong | Excellent | Good | Strong | 8/10 |
| Ch 4: (Foundations continued) | Strong | Excellent | Good | Good | 8/10 |
| Ch 5: Optimization & Neural Networks | Strong | Good* | Good | Strong | 8/10 |
| Ch 6: Representation & Foundation Models | Strong | Good* | Good | Strong | 8/10 |
| Ch 7: Vision | Excellent | Excellent | Very Good | Excellent | 9/10 |
| Ch 8: Language | Excellent | Excellent | Very Good | Excellent | 9/10 |
| Ch 9: Audio & Time | Excellent | Excellent | Very Good | Strong | 9/10 |
| Ch 10: Experiments & Claims | Excellent | Excellent | Good | Strong | 8.5/10 |
| Ch 11: Reliability | Strong | Excellent | Good | Good | 8/10 |
| Ch 12: From Models to Systems | Strong | Excellent | Good | Good | 8/10 |
| Frontmatter & Backmatter | Excellent | Good* | Strong | N/A | 8.5/10 |

*Minor imprecisions noted; see details below.

---

## Top-Priority Issues

These are the items most worth addressing before the next release.

### 1. Factual Error in About Author

The DBLP entry (about-author.tex, line 19) links to "Farhad Vadiee" rather than "Sam Urmian." This needs to be corrected or removed.

### 2. Repository Name Typo

The GitHub URL in the preface references "ml-by-desing" (missing 'n' in "design"). Verify whether this is the actual repo name or a typo that should be corrected.

### 3. Chapter 5: Imprecise Statements on Nonlinearity

Line 170 understates activation functions: "Their job is to make learned internal features more expressive than the weighted-sum models." This should clarify that without nonlinearity, depth adds no expressive power — the whole network collapses to a single affine map.

Line 94's phrasing ("inserts nonlinearities between [layers]") is grammatically ambiguous. Better: "applies a nonlinear activation to the output of each affine map."

### 4. Chapter 5: Batch Normalization Training/Inference Asymmetry

The mathlens box (lines 825–833) shows the training formula but does not mention that batch statistics are used during training while running averages are used at inference. This asymmetry matters for deployment and should at least get a forward-reference note.

### 5. Chapter 6: Terminology Drift

"Representation," "embedding," and "features" are used somewhat interchangeably. Consider establishing clear definitions early in Chapter 6: "representation" for any learned internal structure, "embedding" for vectors in a learned space, "features" for any attribute or signal.

### 6. Chapters 10–11: "Slices" vs. "Subgroups"

Both terms are used equivalently but not explicitly linked. Define once and note the equivalence to prevent confusion.

---

## High-Priority Recommendations

### Bridge Chapters

1. **Bridge I — Add diverse representation card examples.** Currently all examples are student-support focused. One or two additional filled-in cards (spam email, image classification) would show generality.

2. **Bridge II — Strengthen sigmoid motivation.** The jump from "log turns products into sums" to the sigmoid function is fast. Add intuition: "we want a smooth S-curve that maps any real-valued score to [0, 1]."

3. **Bridge II — Acknowledge SGD.** The chapter shows full-batch gradient descent but modern training uses mini-batches. A single sentence noting this practical variant would prevent confusion when students read framework documentation.

4. **Both bridges — Add forward-reference table.** A one-page table mapping bridge topics to main chapters that depend on them (e.g., "Norms → Ch 7 regularization, Ch 9 embedding spaces") would help students see why each topic matters.

### Part I: Foundations

5. **Complete artifact chain example.** No single worked example shows all five Part I artifacts (framing memo → metric-and-action worksheet → evaluation plan → baseline design sheet → structure diagnosis sheet) filled in for the same case. A 2–3 page appendix or sidebar showing the full chain for the student-support case would be tremendously valuable.

6. **Seven-question framework visualization.** Currently stated as a numbered list. A figure showing the three clusters (framing [Q1–4], evaluation & baseline [Q5–6], systems [Q7]) with chapter mappings would help students internalize the structure.

7. **Preview the pedestrian detector earlier.** Chapter 1 mentions it only briefly. A paragraph explicitly previewing it as a running case that will appear in Chapter 7 would reduce surprise when it arrives.

8. **Chapter 2b — Deeper shuffled-label check guidance.** The check is mentioned but not fully explained. What does it mean if performance on shuffled labels is still high? (Answer: the pipeline is broken and learning from artifacts, not signal.)

### Part II: Deep Learning

9. **Chapter 5 — Add numerical learning-rate exercise.** Students compute forward passes and backpropagation steps but never compute gradient descent with different learning rates to feel the effect.

10. **Chapter 5 — Add loss-curve interpretation exercise.** "Given a learning curve where training loss decreases but validation loss increases after epoch 10, explain the failure type and propose one intervention."

11. **Chapter 5 — Clarify backpropagation efficiency.** The chapter explains what backpropagation does but not why it's efficient. A brief note that it requires only one forward and one backward pass (versus one forward pass per parameter for numerical differentiation) would explain the computational motivation.

12. **Chapter 6 — Clarify self-supervision early.** Lead with: "Self-supervised learning generates targets from the data itself (e.g., predicting masked words from context), rather than relying on external human labels."

13. **Chapter 6 — Expand autoencoder bottleneck discussion.** When does reconstruction pressure produce useful representations vs. collapse into copying? A worked example showing bottleneck-to-input-size ratio would help.

14. **Chapter 6 — Add attention-interpretation exercise.** "A model produces attention weights [0.1, 0.7, 0.2] for one token over three others. What does this tell you, and what would be an over-interpretation?"

### Part III: Modalities

15. **Chapter 7 — Expand transfer-learning coverage.** Lines 420–426 mention pretrained backbones briefly. Given the book's emphasis on auditing, this section should discuss when transfer fails, frozen vs. fine-tuned backbone tradeoffs, and how to diagnose transfer success.

16. **Chapter 7 — Add padding/boundary-effects note.** The equivariance theorem correctly excludes boundary-affected locations but doesn't discuss what happens at edges in practice (valid vs. same padding, implications for small-object detection).

17. **Chapter 8 — Expand static embeddings.** Currently three sentences. A worked example showing how static embeddings fail for polysemous words ("bank" in financial vs. geographic context) would motivate contextualization.

18. **Chapter 8 — Add decoding-strategy example.** Show same model with greedy decoding, sampling, and temperature producing different outputs, crystallizing: "the model alone does not determine behavior."

19. **Chapter 9 — Strengthen memory-architecture progression.** HMM → RNN → LSTM → Transformer are each treated briefly. An explicit arc showing what memory failure each addresses would strengthen the section.

20. **Chapter 9 — Formalize drift detection.** Concept drift is identified as a concern but students get no framework for detecting it. A subsection on performance monitoring, feature shift, and output-distribution change would operationalize the concern.

### Part IV: Evidence, Reliability, and Systems

21. **Chapter 10 — Add nested selection diagram.** The concept (inner validation loop inside outer fold) is introduced but deserves a visual diagram, as this is a common point of confusion.

22. **Chapter 11 — Add equalized-odds vs. demographic-parity worked example.** Show both metrics on the same confusion matrix to make the tension concrete.

23. **Chapter 11 — Acknowledge adversarial robustness.** The chapter discusses natural distribution shift but not adversarial perturbations. Even 1–2 sentences distinguishing the two would be useful.

24. **Chapter 12 — Discuss feedback loops.** Deployed models can create feedback loops (e.g., recommended content becomes training data). A brief discussion of this phenomenon would strengthen the deployment chapter.

25. **Chapter 12 — Add full pedestrian-detector walkthrough.** The support-assistant gets a complete systems walkthrough; a parallel walkthrough for the detector would show that systems thinking truly transfers across domains.

26. **Chapter 12 — Close the circle with Chapter 1.** The final chapter does not explicitly reference the framing memo from Chapter 1. A sentence like "Does this readiness brief confirm, narrow, or reject that original framing memo?" would create satisfying full-circle closure.

---

## Medium-Priority Recommendations

### Notation & Consistency

27. **Score vs. logit (Ch 5):** The spam classifier uses "spam score" and later introduces "logit." Unify to one term.

28. **Loss notation (Ch 5):** Both `L` and `ℒ` appear. Settle on one.

29. **Pretraining terminology (Ch 6):** "Pretraining," "pretraining objective," and "pretraining task" are used interchangeably but have different meanings. Tighter usage would help.

30. **Probability notation (Ch 8):** Both P(·) and p_t are used. Clarify the distinction (function vs. scalar).

### Completeness Gaps

31. **Bridge I — Brief forward reference to eigenvalues/PCA** if they appear early in the main text.

32. **Bridge II — One-line regularization example** showing ℒ + λ‖w‖² to connect norms and loss.

33. **Chapter 1 — Expand RL orientation** or clarify its connection to language-model preference alignment.

34. **Chapter 2 — Multi-class metrics note** acknowledging macro vs. micro F1 exist and will return later.

35. **Chapter 5 — Mention gradient clipping** as a practical remedy for exploding gradients.

36. **Chapter 5 — Mention weight initialization** (Kaiming/He, Xavier) as solved problems, even without detail.

37. **Chapter 6 — Discuss catastrophic forgetting** by name and briefly explain the mechanism.

38. **Chapter 6 — Few-shot learning** bridging between frozen probes and full fine-tuning.

39. **Chapter 11 — Causal vs. statistical fairness** distinction for advanced students.

40. **Chapter 12 — A/B testing assumptions** (stable-unit-treatment-value assumption, when randomization is inappropriate).

### Exercises

41. **Add fallback cases in Ch 5–6 exercises.** Some exercises say "if you are carrying one case through the book." Students reading in isolation need a provided toy case.

42. **Chapter 10, Exercise 1:** "Rewrite a claim into a weaker but justified version" — provide a sample pair to clarify expectations.

43. **Bridge II — Add a full training-update exercise:** given a small dataset, a loss, and initial weights, compute one gradient step and the new loss.

### Writing Polish

44. **Chapter 5, line 449:** Replace "local teaching signal" with "error signal for the output layer."

45. **Chapter 6, line 937:** "Foundation models are better understood as reusable pipelines than as prestigious checkpoints" — the word "prestigious" is slightly sarcastic. Consider: "than as single fixed models."

46. **Part syntheses — Expand slightly.** Each is ~12 lines. 2–3 additional sentences explicitly naming the running cases and previewing the next part would improve orientation.

---

## Book-Level Strengths

These are the qualities that make this book distinctive and worth preserving through any revision:

1. **Problem-first orientation.** No chapter begins with architecture names. Each starts with a problem and derives tools as responses.

2. **Artifact-driven pedagogy.** The chain of reusable deliverables (framing memo → metric worksheet → evaluation plan → design card → claim sheet → reliability card → readiness brief) is a genuine pedagogical innovation.

3. **Seven-question framework.** Well-articulated, staged intelligently across chapters, and woven throughout the text.

4. **Running cases that teach.** The course-support assistant and pedestrian detector are complex enough to illustrate real concerns and accessible enough for students to follow. The audio and forecasting cases in Chapter 9 add effective breadth.

5. **Diagnostic reasoning.** The move from "failed baseline → identify missing structure → choose method family" (Part I) and the modality-specific audits (invariance, context, prediction-time) in Part III are major pedagogical contributions.

6. **Evidence discipline.** The insistence that every claim must be bounded, that metrics must be paired with actions, and that evaluation must respect deployment conditions sets a professional standard rare in introductory textbooks.

7. **Honest engagement with failure.** Shortcut learning (Ch 7), hallucination (Ch 8), temporal leakage (Ch 9), and reliability failures (Ch 11) are treated as central problems, not afterthoughts.

8. **Technical accuracy.** No mathematical errors of substance were found across the entire manuscript. Definitions are precise. Theorems are correctly stated and proved.

9. **Clear, engaging prose.** Active voice dominates. Sentences like "A dataset is never the world itself. It is a measurement process applied to the world" and "Convolution matters because vision is local before it is global" are memorable and precise.

10. **Bridge chapters.** Among the best introductions to linear algebra and probability in an ML context. The emphasis on interpretation before formalism is exceptional.

---

## Conclusion

"Machine Learning by Design" is a mature, well-structured textbook that fills an important gap in ML education. The concept-first approach is not just stated but enacted — every chapter demonstrates that problem framing, evaluation discipline, and deployment realism are as important as algorithm choice. The book is technically sound, pedagogically innovative, and clearly written.

The recommendations above are organized to support efficient revision. The top-priority items (factual errors, a few imprecise statements) can be addressed quickly. The high-priority items (expanded examples, additional exercises, deeper coverage in specific sections) would strengthen an already strong manuscript. The medium-priority items are polish that would elevate the book further but are not essential for the next release.

The book is ready for serious pedagogical use.
