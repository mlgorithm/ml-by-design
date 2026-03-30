# Chapter-by-Chapter Additions Plan

This document translates the high-level review into concrete manuscript additions.

The governing rule is simple: add more judgment, not more inventory. The manuscript already covers a strong set of methods. What it most benefits from now is a thicker layer of interpretive structure: more places where students learn what question to ask, what failure mode to expect, and what artifact to produce before claiming they understand the problem.

For each chapter below, the additions are written to fit the current manuscript structure rather than replace it.

## Mathematical Bridge I: Linear Algebra for AI Thinking

### Add: Shapes, Batches, and Why Dimension Errors Matter

- Insert after `Vectors Are Organized Descriptions`.
- Add a short didactic section that distinguishes one example vector, one dataset matrix, one batch, and one sequence or image tensor. Explain that shape is not bookkeeping. Shape states what counts as one case, what counts as one feature family, and what gets processed together.
- Work three tiny examples: a tabular row, a bag-of-words batch, and a token-by-token embedding matrix. End with a mini checklist: what are the rows, what are the columns, what is repeated, what is being broadcast, and what would break if the object were transposed.

### Add: Sparse, Dense, and Missingness as Representation Facts

- Insert after `From One Example to Many: Matrices As Datasets`.
- Add a section showing that representations are not only numeric; they also differ in density, noise, and missingness. A sparse word-count vector, a dense embedding, and a partially observed student record all lead to different modeling behavior.
- The main pedagogical point is that "representation quality" includes which coordinates are absent, which are rare, and which are structurally zero. This prepares students for text models, tabular missingness, and retrieval systems without introducing new machinery too early.

### Add: Linear Separability and What a Hyperplane Can Actually Express

- Insert after `Linear Maps, Projections, and Fitting`.
- Add a geometric section on what a linear score can and cannot separate. Use one example where a line succeeds and one where an XOR-style pattern defeats it.
- This gives students a concrete reason for why later chapters need trees, kernels, or neural nonlinearities. Without this section, "nonlinearity matters" can sound like folklore rather than a consequence of representational limits.

## Mathematical Bridge II: Probability, Risk, and Learning Signals

### Add: Population Risk Versus Empirical Risk

- Insert after `From One Example To Many: Empirical Risk`.
- Add a careful distinction between the average loss on the available sample and the loss we actually care about on future cases. Explain that empirical risk is what we can compute, while population risk is what we wish we knew.
- This is one of the deepest ideas in the whole book. It supports later chapters on overfitting, shift, and evaluation protocol. Students should leave this section knowing why "training loss went down" is not yet evidence.

### Add: Base Rates, Bayes Decisions, and Cost-Sensitive Action

- Insert after `Expectation As Average Consequence`.
- Add a decision-focused section that separates probability estimation from action choice. Show one case where the same estimated probability leads to different actions because costs, base rates, or review capacity differ.
- This bridges probability to policy. It also helps prevent the common undergraduate mistake of assuming that the best classifier, the best probability forecaster, and the best decision policy are automatically the same object.

### Add: Proper Scoring Rules and Honest Probability Forecasts

- Insert after `Loss Functions As Learning Signals`.
- Add a short, undergraduate-level section on why some losses reward honest probability forecasts more directly than others. Keep it intuitive: if a model really believes a case is 70\% likely, what loss makes it safest to report 0.7 rather than a distorted number?
- This section would make calibration in Chapter 2 much easier to motivate and would sharpen the difference between accuracy-style evaluation and probability-quality evaluation.

## Chapter 1: Framing Learning Problems

### Add: Objective Hierarchy: Goal, Proxy, Label, Metric

- Insert after `Prediction Is Not the Decision`.
- Add a compact section that names four levels students often collapse together: the real-world goal, the learning proxy, the label construction, and the reported metric.
- Give one worked example in which the organization wants "retain more students," the proxy is "flag likely disengagement," the label is "did not submit for two weeks," and the metric is recall at a fixed review budget. This would make proxy audit more precise and more reusable.

### Add: A Bad Framing Memo Rewritten

- Insert immediately before `Worked Framing Memo: Student Support`.
- Show a deliberately weak memo first: vague decision, label treated as truth, no review capacity, and no deployment context. Then rewrite it into the stronger memo already aligned with the chapter.
- Students learn framing faster from contrast than from a single good artifact. This section would also keep the chapter from feeling too clean compared with real project starts.

### Add: Framing Is Iterative, Not One-Shot

- Insert after `Worked Framing Memo: Student Support`.
- Add a short section showing how the first framing memo should change after an early model run reveals label noise, subgroup undercoverage, or a queue-capacity constraint.
- The important lesson is that framing is not a prelude that ends before modeling. It is a loop that gets revised when evidence exposes a mismatch.

## Chapter 2: Prediction, Loss, and Evidence

### Add: Move the Mean-Versus-Median Proof Into a Math Lens

- Keep the theorem, but remove it from the main pacing line inside `Regression Losses`.
- The main text should explain the decision consequence first: squared loss reacts more strongly to large misses, while absolute loss is more robust to them. Then the proof can live in a compact `Math Lens` or appendix note.
- This preserves rigor without interrupting the chapter's evaluation-first movement.

### Add: Cost Matrices and Threshold Selection

- Insert after `Threshold Tradeoffs`.
- Add a concrete section where threshold choice is driven by a cost table, review budget, or utility matrix rather than by generic "maximize F1" language.
- This would help students see thresholds as policy choices tied to downstream action, which is central to the philosophy of the book.

### Add: Base-Rate Shift and Why Precision Moves

- Insert after `Confidence Quality: Calibration`.
- Add a section explaining how prevalence changes can alter precision, review burden, and operational value even when score quality is unchanged. One worked example with changing class prevalence would be enough.
- This would be especially useful for undergraduates, because many learn metrics as fixed properties of a model rather than as context-sensitive summaries.

### Add: Metric Failure Gallery

- Insert before `Chapter Artifact: A Minimal Evaluation Plan`.
- Add three short "misleading metric" cases: high accuracy under class imbalance, good ROC with poor precision at deployment budget, and low loss with bad calibration at the action threshold.
- This section would give the chapter a memorable diagnostic core and reinforce the idea that evaluation is about claims, not just numbers.

## Chapter 3: Linear Models and Representation

### Add: Interaction Features and Basis Expansion

- Insert after `Raw Inputs and Feature Maps`.
- Add a section showing how products, buckets, and transformed coordinates let linear models express richer decision boundaries without abandoning interpretability.
- This addition matters because many students incorrectly conclude that linear models are only useful for obviously linear worlds. They need to see that representation and linearity interact.

### Add: Sparse Linear Models Stay Strong in Text and Tabular Work

- Insert after `Why Linear Models Are the Right First Baseline`.
- Add a concrete case from text classification or high-dimensional tabular prediction where a linear model remains highly competitive because the representation already did the hard work.
- This would make the baseline ladder more credible and resist the common habit of skipping directly to deep models.

### Add: Coefficient Stability Under Correlation

- Insert inside `Reading Coefficients Without Fooling Yourself`.
- Add a small section showing how correlated predictors can make coefficients unstable, sign-flip across resamples, or change interpretation when neighboring features are included or removed.
- Students need this before they carry coefficient narratives into causation or policy.

## Chapter 4: Structure Beyond Linearity

### Add: Method Selection by Missing Structure

- Insert after `A Structural Map Before the Methods`.
- Add a decision map: use trees when conditional logic matters, local similarity when neighborhood geometry matters, clustering when the goal is exploratory organization, and dimensionality reduction when compression or visualization is the point.
- This would make the chapter feel less like a sequence of unrelated methods and more like a response to different structural deficits in the linear baseline.

### Add: Ensemble Diversity as Error Reduction

- Insert inside `From Single Trees to Ensembles: Same Structure, More Stability`.
- Add a didactic explanation of why averaging helps only when the component learners are not making identical mistakes.
- This lets students understand random forests and boosting as structured variance/bias manipulations, not as magic accuracy upgrades.

### Add: Clustering Validity and the Danger of Naming Clusters Too Fast

- Insert after `Clustering as Hypothesis, Not Discovery`.
- Add a section on why a cluster is not automatically a real group in the world. Distinguish geometric grouping, operational usefulness, and causal or social interpretation.
- This would prevent one of the most common undergraduate mistakes in unsupervised learning: reifying whatever the algorithm outputs.

## Chapter 5: Optimization and Neural Networks

### Add: Optimization Failure Versus Generalization Failure

- Insert after `Optimization as Repeated Correction`.
- Add a section that separates two very different failure modes: the model cannot fit the training signal at all, or it fits training well but fails on new data.
- This distinction is foundational for debugging. Without it, students change architectures, learning rates, and datasets indiscriminately because they do not know which problem they are solving.

### Add: Debugging a Broken Training Run

- Insert after `Mini-Batches, Initialization, and Stability`.
- Add a concrete troubleshooting sequence: check label corruption, check output layer and loss alignment, overfit a tiny batch, inspect gradient scale, compare train and validation curves, and simplify before scaling.
- This would be one of the most practically valuable sections in the entire manuscript because it teaches a reusable debugging protocol rather than isolated tricks.

### Add: Capacity, Data Regime, and Label Noise

- Insert after `Generalization Returns: Regularization as Bias Toward Stable Patterns`.
- Add a section explaining why more capacity can help or hurt depending on sample size, signal quality, augmentation quality, and label noise. Keep it conceptual and case-driven rather than highly theoretical.
- Students should learn that "bigger model" is not one variable. It interacts with data quality, supervision quality, and monitoring discipline.

## Chapter 6: Representation Learning and Foundation Models

### Add: What Makes a Representation Reusable?

- Insert after `Representation as a Change of Coordinates`.
- Add a section defining reuse in operational terms: invariances captured, information preserved, task mismatch tolerated, and adaptation cost required.
- This would make the chapter's central idea more stable than naming current model families. It also creates a bridge to the later modality chapters.

### Add: Probe, Freeze, Partial Tune, or Full Tune?

- Insert after `Linear Probe as the First Diagnostic`.
- Add a decision table that compares adaptation strategies in terms of compute cost, data needs, risk of forgetting, and claim strength.
- This is a high-value addition because many students understand these strategies as options but not as distinct experimental claims about representation quality and task fit.

### Add: Prompting, Retrieval, and Fine-Tuning Solve Different Problems

- Insert inside `Foundation Models as a Workflow Shift`.
- Add a section explaining that prompting changes instruction, retrieval changes accessible evidence, and fine-tuning changes the predictor itself.
- This would sharpen one of the most important contemporary distinctions in AI practice and help the book stay conceptually durable.

## Chapter 7: Vision: Learning from Images

### Add: Annotation Ontology and Label Ambiguity

- Insert after `Task Formulation Before Architecture Depth`.
- Add a section showing that vision labels depend on a task ontology: what counts as an object, what counts as an occluded instance, what counts as background, and what ambiguities annotators must resolve.
- This would deepen the invariance audit by showing that the label space itself is a modeling design choice.

### Add: Augmentation Claim Matrix

- Insert after `Augmentation as a Label-Preserving Claim`.
- Add a table or box listing common augmentations and the claim each one makes: crop says location should not matter too much, color jitter says exact hue may not matter, horizontal flip says left-right semantics are symmetric, and so on.
- This would be pedagogically strong because it turns augmentation from a recipe into a set of explicit assumptions.

### Add: Robustness by Nuisance-Factor Stress Tests

- Insert before `Deployment-Camera Realism`.
- Add a section that organizes robustness tests by nuisance factor: lighting, blur, weather, camera angle, compression, background, and domain transfer.
- The outcome should be a stress-test habit: name the nuisance, predict the failure, test it deliberately, and decide whether the failure matters for deployment.

## Chapter 8: Language: Context and Grounding

### Add: Ambiguity Taxonomy

- Insert after `Task Shape Before Representation Depth`.
- Add a short section on lexical ambiguity, referential ambiguity, pragmatic ambiguity, and underspecified instructions. Use one message that can be read in multiple ways depending on context.
- This would make the context audit more concrete and help students see why context is not just a longer input window.

### Add: Retrieval Contract: What Evidence Must Be Present?

- Insert inside `Retrieval and Grounding Change the Claim`.
- Add a section stating that retrieval quality is not only recall-at-k. It is also whether the necessary evidence is present, fresh enough, trustworthy enough, and structured enough to support the generated answer.
- This would help students reason about grounded systems as evidence pipelines rather than as text-generation problems alone.

### Add: Hallucination Failure Types and Response Design

- Insert after `Prompt Sensitivity and Evaluation Instability`.
- Distinguish fabrication without evidence, wrong synthesis of correct evidence, outdated evidence, and overconfident answer under uncertainty. Then connect each failure type to a different system response: abstain, cite, escalate, or request clarification.
- This would make the chapter much stronger as a systems chapter in disguise, which is exactly where modern NLP teaching should go.

## Chapter 9: Audio, Time, and Prediction-Time Realism

### Add: Temporal Leakage Taxonomy

- Insert after `Why Random Splits Can Mislead`.
- Add a section naming several leakage types: future labels leaking into features, normalization fit on future data, window overlap leakage, and label definitions that already use future outcomes.
- Students often know leakage as a slogan but not as a design taxonomy. This addition would make their audits sharper.

### Add: Backtesting Regimes and Horizon-Specific Claims

- Insert inside `Evaluation That Respects Time`.
- Add a section comparing rolling-origin evaluation, expanding-window evaluation, and fixed-horizon backtests. Then make explicit that the claim for a 5-minute forecast is not the same claim as the one for a 7-day forecast.
- This would help the chapter teach time-respecting evidence rather than only time-respecting splits.

### Add: Irregular Sampling and Missingness as Signal

- Insert after `Time Series as Evolving Process`.
- Add a section showing that in sequential settings, missing data is often informative and timestamps are part of the representation. A missing sensor value, delayed event, or silent speaker channel may itself carry predictive content.
- This would deepen the chapter's realism and connect well with the bridge chapters on representation.

## Chapter 10: Experiments, Error Analysis, and Scientific Claims

### Add: Pre-Registered Claim Sheet

- Insert after `A Seven-Step Protocol for Scientific Claims`.
- Add a concrete template that asks for the exact claim, split logic, baselines, uncertainty plan, slice plan, and decision rule before the experiment is run.
- This makes claim audit operational and teaches students to commit to a comparison structure before they see the results.

### Add: Multiple Comparisons and Hyperparameter Budget Fairness

- Insert after `Hyperparameter Budget Is Part of the Comparison`.
- Add a section explaining how repeated tuning, prompt search, and model cherry-picking can create fake gains if search effort differs across methods.
- This is especially important for current AI practice, where model comparison is often contaminated by unequal experimentation budgets.

### Add: Negative Results and Scope Control

- Insert after `Claim Scope: Local, External, and Negative Results`.
- Add a section showing what a useful negative result looks like: the method helped only on one slice, transfer failed under domain shift, or the claimed gain disappeared under a stronger baseline.
- This would reinforce a scientific norm the book should model explicitly: narrowing the claim is a success of reasoning, not a failure of courage.

## Chapter 11: Reliability: Bias, Robustness, Privacy, and Safety

### Add: Harm Taxonomy Before Metrics

- Insert near the start of the chapter, before the fairness metrics discussion.
- Add a section distinguishing allocation harms, quality-of-service harms, representation harms, privacy harms, and physical or operational safety harms.
- This makes the rest of the chapter more coherent because different harms demand different evidence and different mitigations.

### Add: Subgroup Reliability Dashboard

- Insert after `Overall Performance Can Hide Unequal Harm`.
- Add a compact dashboard format combining subgroup error, subgroup calibration, abstention behavior, and sample size. The goal is to stop students from reporting one fairness metric in isolation.
- This would also make the reliability artifact more actionable for project work.

### Add: Privacy Threat Models and Safety Cases

- Insert after `Privacy as a Modeling Constraint` and inside `Safety and Bounded Failure`.
- Add a section that frames privacy and safety as threat models: who could exploit what, under what access pattern, and with what consequence. Then add a safety-case pattern: identified hazard, trigger condition, mitigation, fallback, and monitoring signal.
- These additions would keep the chapter grounded in engineering reasoning rather than drifting into slogan territory.

## Chapter 12: From Models to Systems

### Add: Service-Level Objectives and Operational Utility

- Insert after `From Model Objective to Service Objective`.
- Add a section that translates the model's performance into operational targets such as review throughput, false-alert budget, response latency, and escalation quality.
- This is the clearest way to teach that deployment is about a service objective, not a benchmark objective.

### Add: Queueing, Review Capacity, and Human Bottlenecks

- Insert after `Thresholds Are Policies`.
- Add a section showing how the same model score distribution leads to different deployment choices under different human review capacities. A queue-capacity example with a threshold sweep would work well.
- This would make the chapter's human-in-the-loop framing more mathematical and more realistic.

### Add: Contract Tests, Shadow Mode, Rollback, and Incident Review

- Insert across `Data Contracts and Training-Serving Consistency`, `Monitoring After Deployment`, and `Post-Deployment Experimentation`.
- Add a small but explicit operational loop: define contract tests, ship in shadow mode, monitor guardrails, keep rollback ready, and after incidents write a short failure review that updates the readiness brief.
- This would give the chapter a stronger production spine and would close the book with a repeatable systems discipline rather than a loose set of best practices.

## Highest-priority additions

If the book only absorbs a limited number of additions in the next revision cycle, the highest-leverage ones are:

1. `Objective Hierarchy: Goal, Proxy, Label, Metric` in Chapter 1.
2. `Cost Matrices and Threshold Selection` and `Metric Failure Gallery` in Chapter 2.
3. `Debugging a Broken Training Run` in Chapter 5.
4. `Prompting, Retrieval, and Fine-Tuning Solve Different Problems` in Chapter 6.
5. `Retrieval Contract` and `Hallucination Failure Types` in Chapter 8.
6. `Pre-Registered Claim Sheet` and `Budget Fairness` in Chapter 10.
7. `Queueing, Review Capacity, and Human Bottlenecks` in Chapter 12.

These additions would most directly strengthen the book's distinctive promise: teach students to turn AI work into disciplined reasoning, not just model selection.

## Scope Clarification: Method Expansion Without Library Dependence

This section refines the additions plan under the current editorial rule:

- the book remains concept-first and language-independent
- methods can be added when they sharpen modeling judgment
- no topic should be inserted only to satisfy syllabus breadth
- every new method section should teach mechanism, not software usage

For each added method or workflow, require all four:

- one opening modeling question
- one short algorithm skeleton in plain pseudocode
- one small worked numerical or geometric example
- one "when it fails or misleads" note

The chapter plans below are the recommended insertion points for the next revision cycle.

## Exact Insertion Checklist for Method Expansions

### Chapter 2: Prediction, Loss, and Decision Rules (`tex/chapters/ch02.tex`)

- Insert after `Threshold Tradeoffs`.
  New subsection title: `Threshold Sweep as Policy Search`
  Purpose: make thresholding visibly algorithmic rather than verbal. Show how scores are sorted, candidate cutoffs are swept, and workload or utility is computed at each operating point.
  Required worked example: 8 to 12 scored cases with one review-budget constraint.

- Insert after `Confidence Quality: Calibration`.
  New subsection title: `Calibration by Binning: Do 0.7 Scores Behave Like 70 Percent?`
  Purpose: make calibration concrete with bins, observed frequencies, and one simple recalibration discussion.
  Required worked example: one small table of predicted probabilities versus observed outcomes.

- Insert before `Metric Failure Gallery`.
  New subsection title: `Validation, Cross-Validation, and Test Discipline`
  Purpose: explain validation splits, k-fold logic, and why the test set must remain untouched until the claim is frozen.
  Required algorithm skeleton: k-fold cross-validation for limited data.

- Insert immediately after `Validation, Cross-Validation, and Test Discipline`.
  New subsection title: `Hyperparameter Search Without Test Leakage`
  Purpose: explain that model choice and parameter choice are part of the evidence protocol, not an invisible prelude.
  Required worked example: two candidate models and one tuning decision that looks good on validation but must not be rechecked repeatedly on test.

### Chapter 4: Structure Beyond Linearity (`tex/chapters/ch04.tex`)

- Insert after `Why Averaging Helps: Variance Without Bias`.
  New subsection title: `Bagging as Deliberate Disagreement`
  Purpose: explain why averaging helps only when component learners do not make identical mistakes, and tie this directly to bootstrap resampling and feature randomness.
  Required worked example: three small trees whose average is stabler than any one tree.

- Expand the existing `Random Forests` and `Boosted Trees` subsections.
  Add one short comparison box: `Random Forests Versus Boosting: Different Fixes for Different Weaknesses`
  Purpose: keep ensembles from reading like inventory. Clarify variance reduction versus sequential error correction.

- Insert after `Boosted Trees`.
  New subsection title: `Support Vector Machines as Margin-Based Classification`
  Purpose: present SVM as a geometric response to borderline classification, not as a toolbox brand.
  Required worked example: a small 2D separable dataset with two candidate separating lines and one visibly larger margin.

- Insert immediately after `Support Vector Machines as Margin-Based Classification`.
  New subsection title: `Soft Margins and What Slack Buys You`
  Purpose: explain why perfect separation is not the only goal and why robustness can require tolerated violations.
  Required worked example: one outlier that changes the hard-margin boundary.

### Chapter 5: Optimization and Neural Networks (`tex/chapters/ch05.tex`)

- Insert after `Learning Rate`.
  New subsection title: `Adaptive Optimization: Momentum, Adam, and AdamW`
  Purpose: explain why adaptive methods exist and what problem they are trying to solve compared with plain gradient descent.
  Required algorithm skeleton: one update rule each for momentum and AdamW in notation, not code.
  Required worked example: a two-parameter toy landscape where adaptive steps behave differently from fixed-step descent.

- Expand the existing `Mini-Batches, Initialization, and Stability` subsection.
  Add explicit sub-ideas: symmetry breaking, activation scale preservation, and why poor initialization can kill learning before generalization is even relevant.
  Required worked example: one tiny network with "all weights equal" versus sensible initialization.

- Insert after `Mini-Batches, Initialization, and Stability`.
  New subsection title: `Batch Normalization as Signal Stabilization`
  Purpose: explain batch normalization as a training-stability device, not as architectural ornament.
  Required worked example: one layer whose activation scale drifts across batches.

- Expand the existing `Weight Decay, Early Stopping, Dropout, and Augmentation` subsection.
  Add one comparison box: `Weight Decay, Dropout, and Early Stopping Do Different Jobs`
  Purpose: stop students from treating all regularization ideas as interchangeable.
  Required worked example: one overfitting curve plus one intuition example showing why dropout is not the same as shrinking weights.

### Chapter 6: Representation Learning and Foundation Models (`tex/chapters/ch06.tex`)

- Insert after `Self-Supervised Pressure`.
  New subsection title: `Autoencoders as Reconstruction-Based Representation Learning`
  Purpose: give one compact method family that makes representation learning legible without relying on current model brands.
  Required worked example: a bottleneck representation that must compress while preserving reconstructible structure.
  Scope note: keep this brief and historical-conceptual, not a long architecture survey.

- Insert after `Examples Across Modalities`.
  New subsection title: `Multimodal Transfer as Shared Structure`
  Purpose: explain the durable idea behind multimodal learning: different signals can align around a shared task or shared latent structure.
  Required worked example: image-text alignment or audio-text alignment at the level of representation choice and claim scope.

- Insert after `Transfer Begins: Pretrain, Probe, Adapt`.
  New subsection title: `Worked Example: Reuse Helps Here but Fails There`
  Purpose: make transfer less slogan-like by showing one case where reuse works and one where domain mismatch blocks it.
  Required artifact update: extend the chapter's reuse plan with an explicit "evidence that reuse is actually helping" line.

### Chapter 7: Vision: Learning from Images (`tex/chapters/ch07.tex`)

- Insert after `Tracking and Other Structured Vision Tasks`.
  New subsection title: `One Scene, Three Tasks: Classification, Detection, and Segmentation`
  Purpose: show that the same visual world produces different prediction objects, metrics, and failure modes depending on task formulation.
  Required worked example: one street or classroom scene labeled three different ways.

- Insert after `Modern Visual Backbones and Transfer`.
  New subsection title: `Why Structured Outputs Need Structured Evaluation`
  Purpose: explain that a detector or segmenter cannot be judged with plain classification accuracy because location, overlap, and object completeness are part of the claim.
  Scope note: keep this conceptual. Do not turn it into a benchmark-metric catalog.

### Chapter 8: Language: Context and Grounding (`tex/chapters/ch08.tex`)

- Insert after `Translation, Summarization, Question Answering, and Generation`.
  New subsection title: `Encoder-Decoder Models as Conditional Sequence Mapping`
  Purpose: explain when the output is itself a sequence that must be generated conditionally from an input sequence.
  Required worked example: one tiny translation or structured summarization example with input tokens and target tokens.

- Insert after `Language Modeling as Sequence Prediction`.
  New subsection title: `Next-Token Prediction Is Not the Same Claim as Sequence Transformation`
  Purpose: distinguish autoregressive continuation from task-directed mapping.
  Required comparison: one sentence-completion objective versus one translation-style objective.

### Chapter 10: Experiments, Error Analysis, and Scientific Claims (`tex/chapters/ch10.tex`)

- Insert after `Experimental Protocol as Control of Premises`.
  New subsection title: `Cross-Validation as an Evaluation Design for Limited Data`
  Purpose: position cross-validation as an evidence design, not as an optimization trick.
  Required algorithm skeleton: k-fold protocol with train, validate, aggregate, and final freeze.

- Insert after `Hyperparameter Budget Is Part of the Comparison`.
  New subsection title: `Search Budget, Selection Protocol, and Fair Comparison`
  Purpose: make explicit that equal comparison requires comparable tuning opportunity, stopping rules, and reporting discipline.
  Required worked example: two methods with unequal search budget, where the apparent gain disappears after honest accounting.

## Cross-Cutting Additions: Algorithm Skeletons and Worked Examples

These should be implemented inside the chapters above rather than as a separate appendix.

- Chapter 2: threshold sweep, calibration by bins, and validation-versus-test protocol.
- Chapter 4: bagging, boosting intuition, and one margin-based classifier sketch.
- Chapter 5: gradient descent, momentum or AdamW update, early stopping logic, and a broken-run debugging checklist.
- Chapter 6: pretrain-probe-fine-tune comparison and one reconstruction-based representation example.
- Chapter 7: same-scene contrast across classification, detection, and segmentation.
- Chapter 8: encoder-decoder mapping and a minimal retrieval or grounding pipeline sketch where helpful.
- Chapter 10: cross-validation protocol and fair-search comparison logic.

## Priority Order for This Method-Focused Revision

If only part of this plan is implemented in the next pass, prioritize in this order:

1. Chapter 2: `Validation, Cross-Validation, and Test Discipline`
2. Chapter 2: `Hyperparameter Search Without Test Leakage`
3. Chapter 4: `Support Vector Machines as Margin-Based Classification`
4. Chapter 5: `Adaptive Optimization: Momentum, Adam, and AdamW`
5. Chapter 5: `Batch Normalization as Signal Stabilization`
6. Chapter 7: `One Scene, Three Tasks: Classification, Detection, and Segmentation`
7. Chapter 8: `Encoder-Decoder Models as Conditional Sequence Mapping`
8. Cross-cutting: add one algorithm skeleton and one hand-worked example to every new method section

This priority order keeps the manuscript aligned with its identity: real modeling methods are added, but each one is taught as an answer to a problem, with mechanism, example, and judgment attached.

## Integration Pass Against the Current Manuscript

This pass checks the additions plan against the current chapter structure so the next revision cycle strengthens the book's arc rather than creating local duplication.

The most important editorial rule is:

- if a heading already exists in the manuscript, deepen it instead of adding a sibling section with the same job

### Mathematical Bridge I: Linear Algebra for AI Thinking

- Current role: establish shapes, weighted evidence, separability, projection, and representation geometry before the method chapters begin.
- Integration rule: any Chapter 4 margin-based material should explicitly point back to `Linear Separability and What a Hyperplane Can Actually Express`.
- Integration rule: any Chapter 3 or 5 algorithm skeleton should reuse the bridge language of vectors, matrices, coordinates, and weighted combinations rather than introducing a fresh vocabulary.

### Mathematical Bridge II: Probability, Risk, and Learning Signals

- Current role: distinguish expectation, risk, empirical versus population loss, proper scoring, and optimization signals.
- Integration rule: Chapter 2 calibration, threshold, and ROC additions should explicitly reuse `Proper Scoring Rules and Honest Probability Forecasts` and `Population Risk Versus Empirical Risk`.
- Integration rule: Chapter 10 cross-validation and search-budget additions should point back to the bridge distinction between computable sample loss and the future-facing risk we actually care about.

### Chapter 1: Framing Learning Problems

- Current role: define the decision-first framing grammar for the entire book.
- Already integrated additions present: `Objective Hierarchy: Goal, Proxy, Label, Metric`, `A Bad Framing Memo Rewritten`, and `Framing Is Iterative, Not One-Shot`.
- Integration rule: every later method expansion should begin with the Chapter 1 question it answers. Do not let new method sections read as if methods are chosen before task shape, proxy, and action constraints.

### Chapter 2 and Chapter 2b: Evaluation Core Split Across Two Chapters

- Current role of Chapter 2: connect loss, metrics, thresholds, ranking, ROC, calibration, and action policy.
- Current role of Chapter 2b: own generalization, leakage, protected evaluation workflow, and baseline sanity checks.
- Already integrated additions present in Chapter 2: `Cost Matrices and Threshold Selection`, `ROC and Precision-Recall Curves`, `Confidence Quality: Calibration`, `Base-Rate Shift and Why Precision Moves`, and `Metric Failure Gallery`.
- Integration rule: place new validation, cross-validation, and hyperparameter-selection content at the Chapter 2 to Chapter 2b boundary. Chapter 2 should explain why these protocols matter for claims; Chapter 2b should explain how evaluation can still fail through leakage or broken split logic.
- Integration rule: do not duplicate leakage material in Chapter 10. Chapter 10 should assume the protected workflow from Chapter 2b and move to claim discipline.

### Chapter 3: Linear Models and Representation

- Current role: establish the first serious predictive baseline and teach representation as the source of expressive power.
- Already integrated additions present: `Interaction Features and Basis Expansion` and `Sparse Linear Models Stay Strong in Text and Tabular Work`.
- Integration rule: do not place SVM here. Chapter 3 should end with a credible, controlled linear baseline so that Chapter 4 can earn the move beyond linearity.
- Integration rule: any added algorithm skeleton in this chapter should stay baseline-first and diagnostic-first.

### Chapter 4: Structure Beyond Linearity

- Current role: explain what kinds of missing structure justify leaving the linear baseline.
- Already integrated additions present: `Method Selection by Missing Structure`, `From Single Trees to Ensembles`, `Random Forests`, `Boosted Trees`, `Clustering Validity and the Danger of Naming Clusters Too Fast`.
- Integration rule: SVM should be inserted as one more answer to the question "what structure is missing?" rather than as an isolated classical method.
- Integration rule: ensemble additions should deepen the current sections, not create a separate ensemble mini-chapter. The chapter should still read as one continuous response to structural mismatch.
- Integration rule: the chapter artifact should remain a structure diagnosis sheet, so every added method must cash out as a diagnostic choice, not a brand name.

### Chapter 5: Optimization and Neural Networks

- Current role: explain how learned nonlinear representations are trained and debugged.
- Already integrated additions present: `Optimization Failure Versus Generalization Failure`, `Mini-Batches, Initialization, and Stability`, `Debugging a Broken Training Run`, `Weight Decay, Early Stopping, Dropout, and Augmentation`, and `Capacity, Data Regime, and Label Noise`.
- Integration rule: adaptive optimization, initialization refinement, and batch normalization should be nested into the existing optimization-and-stability spine. Do not scatter training mechanics across several disconnected sections.
- Integration rule: every added neural method should connect to a specific failure mode already named in the chapter: unstable gradients, stalled learning, brittle optimization, or overfitting.

### Chapter 6: Representation Learning and Foundation Models

- Current role: explain reusable representations, self-supervision, transfer, and adaptation depth.
- Already integrated additions present: `What Makes a Representation Reusable?`, `Self-Supervised Pressure`, `Examples Across Modalities`, `Transfer Begins: Pretrain, Probe, Adapt`, and `Probe, Freeze, Partial Tune, or Full Tune?`
- Integration rule: autoencoders, multimodal transfer, and stronger reuse examples must stay in the representation frame. They should clarify "what is being reused" rather than expanding into modality-specific application surveys.
- Integration rule: Chapter 6 should remain the unique home for self-supervised and reuse logic, so Chapters 7 and 8 should borrow these concepts rather than reteach them.

### Chapter 7: Vision: Learning from Images

- Current role: apply representation and invariance thinking to visual tasks and deployment realism.
- Already integrated additions present: `Classification`, `Detection`, `Segmentation`, `Annotation Ontology and Label Ambiguity`, and `Augmentation Claim Matrix`.
- Integration rule: the remaining vision additions should make structured outputs more explicit, but still through one shared visual problem. Avoid turning the chapter into a detector/segmenter architecture catalog.
- Integration rule: any new detection or segmentation material should refer back to Chapter 1 task formulation and Chapter 2 metric/action logic.

### Chapter 8: Language: Context and Grounding

- Current role: explain how task shape, context, retrieval, grounding, and decoding jointly determine language-system behavior.
- Already integrated additions present: task-shape subsections for generation and QA, retrieval contract material, prompt-evaluation instability, and hallucination failure analysis.
- Integration rule: encoder-decoder content should be inserted as a task-shape clarification, not as a separate model-history branch.
- Integration rule: Chapter 8 should own the distinction between next-token prediction and conditional sequence transformation, while Chapter 6 remains responsible for the reusable-representation story behind transformers.

### Chapter 9: Audio, Time, and Prediction-Time Realism

- Current role: teach sequential modeling through prediction-time constraints rather than through a model zoo.
- Already integrated additions present: `Irregular Sampling and Missingness as Signal` and the evaluation sequence around chronological splits and backtesting.
- Integration rule: do not crowd this chapter with more named method families unless they sharpen the prediction-time audit. Its comparative advantage is temporal realism, not breadth.
- Integration rule: any extra algorithm skeleton here should emphasize information availability, horizon, and backtesting regime.

### Chapter 10: Experiments, Error Analysis, and Scientific Claims

- Current role: convert evaluation results into disciplined scientific claims.
- Already integrated additions present: `A Seven-Step Protocol for Scientific Claims`, `Hyperparameter Budget Is Part of the Comparison`, `Multiple Comparisons and Researcher Degrees of Freedom`, and the chapter artifact claim sheet.
- Integration rule: cross-validation and fair-search additions belong here only as scientific protocol. The chapter should not reteach thresholding or leakage from Chapters 2 and 2b.
- Integration rule: all method-comparison additions elsewhere should eventually cash out here as claim-scope and fair-comparison discipline.

### Chapter 11: Reliability: Bias, Robustness, Privacy, and Safety

- Current role: move from average performance to bounded, unequal, and high-stakes failure.
- Already integrated additions present: `Harm Taxonomy Before Metrics`, `A Subgroup Reliability Dashboard`, `Calibration Gaps Can Also Be Reliability Gaps`, and `Privacy Threat Models Before Privacy Tools`.
- Integration rule: this chapter should reuse calibration language from Chapter 2 and slice language from Chapter 10 rather than inventing a separate reliability vocabulary.
- Integration rule: new method material should not drift here. Chapter 11 is where students learn the consequences of method choices under deployment constraints.

### Chapter 12: From Models to Systems

- Current role: integrate the whole manuscript into service objectives, thresholds as policy, human review, monitoring, rollback, and readiness.
- Already integrated additions present: `Service-Level Objectives Make the Objective Operational`, `Queueing, Review Capacity, and Human Bottlenecks`, and the post-deployment workflow sections.
- Integration rule: this chapter should be the place where Chapter 2 threshold policy, Chapter 10 claim discipline, and Chapter 11 reliability evidence are visibly assembled into one operational system.
- Integration rule: do not place new standalone methods here. Only add system-facing consequences of methods already taught earlier.

## Remaining Method Work After This Integration Pass

After aligning the plan with the live chapter structure, the clearest remaining additions are:

1. Chapter 2: add the validation, cross-validation, and hyperparameter-selection bridge between metric choice and protected evaluation workflow.
2. Chapter 4: add SVM and soft-margin reasoning as a geometric extension of the "missing structure" logic.
3. Chapter 5: deepen adaptive optimization and batch normalization inside the existing optimization spine.
4. Chapter 6: add a brief autoencoder and multimodal-transfer treatment without breaking the reuse-focused chapter identity.
5. Chapter 7: add one explicit same-scene comparison across classification, detection, and segmentation.
6. Chapter 8: add encoder-decoder models as conditional sequence mapping tied to task shape.
7. Chapter 10: add cross-validation and fair-search protocol as scientific-method expansions, not as duplicated evaluation mechanics.
