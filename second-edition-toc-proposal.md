# Machine Learning by Design — Second Edition

## Proposed Revised Table of Contents

**Revision principles:**
- Preserve the book's identity: problem-first, artifact-driven, reliability/systems endgame
- Fill the three biggest conceptual gaps: probabilistic modeling, semi-supervised/weak supervision, modern generative models
- Keep total chapter count manageable (18 content chapters + 2 bridges, up from 14+2)
- Mark every change clearly so the diff from first edition is obvious

---

## Mathematical Bridge: Just-in-Time Review

### Bridge I: Linear Algebra for AI Thinking
*Unchanged.* Add a short eigendecomposition/SVD preview (1–2 pages) to smooth the transition into PCA in `Structure Beyond Linearity` and embeddings in `Representation Learning and Foundation Models`.

### Bridge II: Probability, Risk, and Learning Signals
*Revised.* Add a probabilistic-modeling bridge section (~3 pages):
- Generative vs. discriminative models (the "model P(X|Y) vs. P(Y|X)" distinction)
- Priors, posteriors, MAP vs. MLE (intuition, not full derivation)
- Why this matters for later uncertainty work

This is the cheapest way to prepare students for Naive Bayes, Bayesian reasoning, GMMs/EM in the new probabilistic-models chapter, and uncertainty quantification in the reliability chapter.

---

## Part I: Foundations

### Chapter 1: Framing Learning Problems
*Unchanged.* Already one of the book's strongest chapters.

### Chapter 2: Prediction, Loss, and Decision Rules
*Lightly revised.* Make the uncertainty thread more visible: position calibration and abstention as part of a "confidence story" that continues through the reliability chapter. Add a sidebar on prediction intervals or uncertainty-aware decision-making (~1 page).

### Chapter 3: Generalization, Leakage, and Evaluation Discipline (`ch02b`)
*Unchanged.* Add one explicit forward-reference to temporal leakage in the audio/time chapter and to deployment shift in the reliability chapter.

### Chapter 4: Linear Models and Representation (`ch03`)
*Unchanged.*

### Chapter 5: Structure Beyond Linearity (`ch04`)
*Revised.* Add a short section on Naive Bayes (~3–4 pages) as a generative counterpart to logistic regression. This is the most natural home for it: Chapter 5 already covers "which model family fits which structure," and Naive Bayes introduces the generative perspective before students need it for GMMs, LDA, and later Bayesian work.

### Chapter 6: Designing the Dataset (`ch04b`)
**Revised — significant addition.** Add a new section: "Learning with Fewer Labels" (~6–8 pages):
- Semi-supervised learning: pseudo-labeling, self-training, co-training
- Weak supervision: labeling functions, data programming (Snorkel-style)
- Silver labels and when to trust them
- Connection to active learning (already in the chapter)

This is the reviewer's clearest "missing topic that fits perfectly." The chapter already argues that data is a design choice; this extends the argument to label acquisition strategy.

---

## Part II: Models and Representations

### Chapter 7: Optimization and Neural Networks (`ch05`)
*Unchanged.*

### Chapter 8: Probabilistic Models and Latent Structure (`ch05b`, NEW)
**New chapter (~25–30 pages).** Fills the biggest classical gap:
- Gaussian mixture models and EM (the core "latent variable + iterative optimization" idea)
- Bayesian linear regression (predictive distributions, not just point estimates)
- Gaussian processes (intuition + one worked example; formal details in advanced note)
- Connection to uncertainty: aleatoric vs. epistemic, ensemble uncertainty
- Artifact: **Uncertainty Audit Card** — what does the model know it doesn't know?

*Why here:* It follows neural network optimization (Chapter 7) and precedes representation learning (Chapter 9). Students have the optimization vocabulary to understand EM, and the probabilistic lens prepares them for VAEs in Chapter 10.

### Chapter 9: Representation Learning and Foundation Models (`ch06`)
*Unchanged.*

### Chapter 10: Generative Representations (`ch06a`, NEW)
**New chapter (~20–25 pages).** Fills the modern generative gap:
- Variational autoencoders (latent-variable models that generate, connecting to Chapter 8's EM intuition)
- Generative adversarial networks (adversarial training, mode collapse, evaluation challenges)
- Diffusion models (denoising as iterative generation; conceptual treatment, not full math)
- Brief note on normalizing flows / flow matching
- Evaluation: FID, IS, and why measuring generative quality is hard
- Artifact: **Generative Model Audit** — what does this model generate, and what failure modes should you watch for?

*Why here:* It extends the representation-learning arc (Chapter 9) into "learning to generate" before modality-specific chapters use generative models.

### Chapter 11: Learning from Interaction: Reinforcement Learning (`ch06b`)
*Lightly revised.* Update preface to match coverage (remove "orientation only" framing — this chapter earns its place). Add a short bridge to offline evaluation from logs in recommendation and to contextual bandits in systems.

---

## Part III: Applications and Modalities

### Chapter 12: Vision: Learning from Images (`ch07`)
*Unchanged.*

### Chapter 13: Language: Context and Grounding (`ch08`)
*Lightly revised.* Sharpen internal structure: separate classical NLP baselines → contextual models → grounded/RAG systems more explicitly. Add a forward reference to recommendation (Chapter 15) for ranking/retrieval overlap.

### Chapter 14: Audio, Time, and Prediction-Time Realism (`ch09`)
*Revised.* Add classical forecasting toolkit (~5–6 pages):
- ARIMA / exponential smoothing (core ideas, not full Box-Jenkins derivation)
- State-space models / Kalman filter (intuition: "what if the system has hidden state that evolves?")
- Connection to HMMs (already present) and to the drift detection framework

*Editorial note:* The reviewer flagged that this chapter is scope-crowded (audio + forecasting + multimodal + graphs). Consider splitting multimodal fusion and graph-structured data into a short follow-on chapter if the page count grows past ~45 pages.

### Chapter 15: Ranking, Recommendation, and Exposure (`ch09a`, NEW)
**New chapter (~20–25 pages).** Fills the recommender gap:
- Recommendation as a ranking problem (connects to Chapter 2's threshold/ranking treatment)
- Collaborative filtering and matrix factorization
- Implicit feedback: clicks, dwell time, and the missing-data problem
- Exposure bias: the model influences what users see, which corrupts future training data
- Offline evaluation challenges: counterfactual estimation, replay methods
- Connection to feedback loops in systems and fairness in reliability
- Artifact: **Recommendation Audit Card** — what does the system expose, suppress, and amplify?

*Why here:* Recommendation is a modality-specific application that draws on representation learning and sequential modeling, then connects forward to systems feedback loops.

---

## Part IV: Evidence, Reliability, and Systems

### Chapter 16: Experiments, Error Analysis, and Scientific Claims (`ch10`)
*Unchanged.*

### Chapter 17: Reliability: Bias, Robustness, Privacy, and Safety (`ch11`)
*Revised.* Add a compact interpretability/XAI toolkit section (~5–6 pages):
- SHAP, LIME, partial dependence (what they show and what they don't)
- Counterfactual explanations
- Attribution methods beyond saliency
- Failure modes: when explanations mislead

Also strengthen the uncertainty-quantification thread: predictive intervals, conformal prediction (brief), and ensemble disagreement as a reliability signal. (~3–4 pages)

### Chapter 18: From Models to Systems (`ch12`)
*Revised.* Add production-ML infrastructure section (~5–6 pages):
- Feature stores and feature freshness
- Model/version registry
- Inference efficiency: distillation, quantization, pruning (conceptual treatment)
- Cost-aware serving
- Training-serving consistency in more operational detail

---

## Appendix A: Mathematical Foundations
*Revised.* Add compact supplements for:
- Priors, posteriors, MAP, and latent-variable/EM intuition (supporting Chapter 8)
- Basic state-space notation (supporting Chapter 14's classical forecasting addition)

---

## Summary of Changes

| Change | Type | Pages | Priority |
|--------|------|-------|----------|
| Bridge II: probabilistic modeling bridge | Revision | +3 | High |
| Chapter 5 (`ch04`): Naive Bayes section | Revision | +4 | High |
| Chapter 6 (`ch04b`): Semi-supervised/weak supervision | Revision | +7 | **Top** |
| **Chapter 8 (`ch05b`): Probabilistic Models (NEW)** | New chapter | +28 | High |
| **Chapter 10 (`ch06a`): Generative Representations (NEW)** | New chapter | +23 | High |
| Chapter 11 (`ch06b`): Preface alignment, offline eval bridge | Revision | +2 | Medium |
| Chapter 13 (`ch08`): Internal structure cleanup | Revision | +0 | Low |
| Chapter 14 (`ch09`): Classical forecasting toolkit | Revision | +6 | Medium |
| **Chapter 15 (`ch09a`): Ranking, Recommendation, and Exposure (NEW)** | New chapter | +23 | Medium |
| Chapter 17 (`ch11`): XAI toolkit + uncertainty | Revision | +9 | Medium |
| Chapter 18 (`ch12`): Production infrastructure | Revision | +6 | Medium |
| Bridge I: SVD preview | Revision | +2 | Low |
| Appendix A: Probabilistic + state-space supplements | Revision | +4 | Low |
| **Total estimated addition** | | **~117 pages** | |

### What stays untouched
Chapters 1, 3 (`ch02b`), 4 (`ch03`), 7 (`ch05`), 9 (`ch06`), 12 (`ch07`), 16 (`ch10`), and all part syntheses stay structurally intact. The book's spine — framing, evaluation discipline, artifact chain, seven-question framework — is preserved exactly.

### Recommended implementation order
1. Chapter 6 (`ch04b`): semi-supervised/weak supervision (smallest change, highest coherence payoff)
2. Chapter 8 (`ch05b`): probabilistic models (fills the biggest classical gap)
3. Chapter 10 (`ch06a`): generative representations (fills the biggest modern gap)
4. Bridge II + Chapter 5 (`ch04`): probabilistic bridge + Naive Bayes (prepares students for Chapter 8)
5. Chapter 15 (`ch09a`): ranking and recommendation (new chapter, can be written independently)
6. Chapter 17 (`ch11`) + Chapter 18 (`ch12`): XAI toolkit + production infrastructure (revisions to existing chapters)
7. Chapter 14 (`ch09`): classical forecasting (revision, lower urgency)
8. Bridge I + Appendix A: minor supplements (last)
