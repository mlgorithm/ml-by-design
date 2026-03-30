# Exercise Plan

This document defines the target exercise architecture for **Solving AI Problems**.

The goal is not to maximize exercise count. The goal is to make every chapter teachable, adoptable, and cumulative.

## Design Rules

Every chapter should eventually have three exercise tiers:

1. `Quick checks`
   Short questions that test vocabulary, distinctions, toy calculations, or local reasoning.
2. `Applied problems`
   Medium-length exercises that use a small dataset, table, figure, or companion script.
3. `Synthesis task`
   One longer exercise that forces the reader to produce or critique the chapter artifact.

Recommended target per chapter:

- `4-6` quick checks
- `2-3` applied problems
- `1` synthesis task

## Public vs Instructor Material

Public material should include:

- all quick checks
- all applied problem statements
- one-sentence hints for most applied problems
- at least one fully public synthesis task per part of the book

Instructor-only material should include:

- full solutions for applied problems
- grading notes for synthesis tasks
- common misconceptions and likely weak answers
- optional rubric language for artifact-based assignments

## Hints Policy

Hints should be short and directional, not mini-solutions.

- `Quick checks`: no hints unless the question involves a toy derivation
- `Applied problems`: one hint per problem
- `Synthesis tasks`: a checklist, rubric, or starter template instead of a narrow hint

## Companion-Code Role

The companion code should support exercises, not replace them.

- `Minimal` scripts should support quick checks and first applied problems.
- `Practical` scripts should support stronger applied problems and instructor demos.
- Synthesis tasks should usually end in a written artifact, not only a notebook result.

## Chapter-by-Chapter Plan

### Chapter 1: Framing Learning Problems

Primary artifact:

- `Framing memo`

Quick checks:

- distinguish prediction from decision in short scenarios
- identify whether a target is a goal, proxy, or leakage source
- spot one unacceptable input feature and justify why it should be excluded
- explain why a dataset is evidence about the world rather than the world itself

Applied problems:

- rewrite a vague AI product pitch into a defensible learning-task statement
- critique a public system description by identifying which memo fields are missing or unstable
- compare two candidate proxy targets for the same decision and argue which is less distorting

Synthesis task:

- write a one-page framing memo for a student-support, spam-filtering, or domain-specific case

Notes:

- this chapter already contains the book's best first assignment
- Chapter 1 should eventually expose `Framing memo` as a formal chapter artifact to match Chapters 2 to 12

### Chapter 2: Prediction, Loss, and Evidence

Primary artifact:

- `A Minimal Evaluation Plan`

Quick checks:

- compute accuracy, precision, recall, F1, and log loss on a toy table
- explain why two models can have the same accuracy and different usefulness
- distinguish train, validation, and test roles
- identify one leakage path in a proposed evaluation setup

Applied problems:

- choose an operating threshold for a given policy objective
- compare two models using calibration and threshold-sensitive metrics rather than accuracy alone
- diagnose an overfitting story from train/validation/test curves

Synthesis task:

- produce a minimal evaluation plan for the Chapter 1 framing memo, including metric choice, split logic, baseline, threshold policy, and failure slices

Companion link:

- `book/companion/ch02/minimal/metric_tradeoffs.py`
- `book/companion/ch02/practical/overfitting_demo_sklearn.py`

### Chapter 3: Linear Models and Representation

Primary artifact:

- `A First Baseline Design Sheet`

Quick checks:

- interpret the sign and magnitude of a coefficient in context
- explain why feature scaling affects some linear models
- distinguish regression from classification targets
- identify when a linear model is a serious baseline rather than a straw man

Applied problems:

- design a feature set for a routing or risk model and defend each feature family
- inspect a coefficient table and identify likely spurious or unstable signals
- compare an unregularized and regularized model summary and explain the tradeoff

Synthesis task:

- complete a baseline design sheet for one framed problem, including representation choice, regularization expectation, baseline success criteria, and failure modes

Companion link:

- `book/companion/ch03/minimal/linear_and_logistic_from_scratch.py`
- `book/companion/ch03/practical/linear_and_logistic_sklearn.py`

### Chapter 4: Structure Beyond Linearity

Primary artifact:

- `A Structure Diagnosis Sheet`

Quick checks:

- identify when branching structure is more plausible than a single weighted sum
- explain one case where nearest neighbors fails without scaling
- distinguish supervised and unsupervised goals
- explain what kind of mismatch a clustering result can and cannot solve

Applied problems:

- choose between linear, tree-based, neighbor-based, or clustering-based approaches for a named problem and justify the choice
- inspect a small decision tree and critique whether it is learning useful structure or memorizing noise
- compare two nonlinear baselines and decide which mismatch each is actually addressing

Synthesis task:

- fill out a structure diagnosis sheet that maps a problem's likely mismatch to one or two candidate method families and a falsification plan

Companion link:

- `book/companion/ch04/minimal/structure_methods_from_scratch.py`
- `book/companion/ch04/practical/structure_beyond_linearity_sklearn.py`

### Chapter 5: Optimization and Neural Networks

Primary artifact:

- `A Minimum Credible Neural Training Report`

Quick checks:

- trace a forward pass through a tiny network
- explain why nonlinearity changes what the model can represent
- describe what backpropagation computes without turning it into a memorized formula recital
- distinguish optimization failure from generalization failure

Applied problems:

- compare a linear baseline and a small multilayer model on a nonlinear task and explain what changed
- diagnose a training run using loss curves, validation behavior, and optimizer choice
- analyze whether a neural model is justified or premature on a given problem

Synthesis task:

- write a minimum credible neural training report covering baseline comparison, architecture, optimization settings, validation logic, and generalization risks

Companion link:

- `book/companion/ch05/minimal/tiny_network_from_scratch.py`
- `book/companion/ch05/practical/mlp_pytorch_demo.py`

### Chapter 6: Representation Learning and Foundation Models

Primary artifact:

- `A Reuse and Adaptation Plan`

Quick checks:

- explain what it means for an embedding space to encode useful geometry
- distinguish frozen reuse, linear probing, partial adaptation, and full fine-tuning
- identify one case where transfer is likely to help and one where it may mislead
- separate durable representation-learning ideas from model-brand language

Applied problems:

- propose a reuse strategy for a task with limited labels and argue what evidence would justify it
- compare raw-feature and pretrained-representation baselines under a domain shift
- critique a transfer claim that reports only one benchmark score and no adaptation details

Synthesis task:

- produce a reuse and adaptation plan that names the source representation, target task, adaptation level, evaluation slices, and expected failure modes

Companion link:

- `book/companion/ch06/minimal/cooccurrence_embeddings.py`
- `book/companion/ch06/practical/contrastive_transfer_demo.py`

### Chapter 7: Vision: Learning from Images

Primary artifact:

- `A Vision Design and Stress-Test Card`

Quick checks:

- explain what convolution and pooling preserve and discard
- identify a likely shortcut feature in an image classification setting
- explain why clean accuracy is not enough for a visual system
- name one deployment-camera mismatch that a benchmark may hide

Applied problems:

- inspect slice results for a vision model and identify which failures suggest shortcut learning
- design an augmentation plan and explain which invariance it teaches
- compare a raw-pixel baseline, a CNN, and an augmented CNN under clean and shifted evaluation

Synthesis task:

- complete a vision design and stress-test card for the dashboard-camera pedestrian detector or a comparable vision problem

Companion link:

- `book/companion/ch07/minimal/convolution_and_pooling_demo.py`
- `book/companion/ch07/practical/digits_cnn_augmentation_demo.py`

### Chapter 8: Language: Context and Grounding

Primary artifact:

- `An NLP Context-and-Grounding Card`

Quick checks:

- show why unigram counts can erase meaning
- identify when bigrams are enough and when longer context is needed
- distinguish language modeling, classification, retrieval, and grounded response generation
- explain why groundedness is a system property rather than a token-level trick

Applied problems:

- compare bag-of-words, bigram, and sequence models on an order-sensitive task
- design a retrieval step for the course-support assistant and define what counts as acceptable evidence
- critique a generated answer for unsupported claims, missing context, or escalation failure

Synthesis task:

- produce an NLP context-and-grounding card for the support assistant, including task decomposition, retrieval policy, abstention or escalation rules, and evaluation plan

Companion link:

- `book/companion/ch08/minimal/order_and_ngrams_demo.py`
- `book/companion/ch08/practical/order_sensitive_text_demo.py`

### Chapter 9: Audio, Time, and Sequential Prediction

Primary artifact:

- `A Sequential Design Card`

Quick checks:

- explain what a spectrogram preserves that a raw waveform view hides
- identify which features are available at prediction time and which ones leak the future
- distinguish random split, blocked split, and chronological split in a forecasting setting
- explain why latency belongs in the modeling conversation

Applied problems:

- diagnose a forecasting evaluation that accidentally leaks future information
- compare a naive persistence baseline and a learned forecasting model under honest chronological evaluation
- design a wake-word or event-detection pipeline under a latency constraint

Synthesis task:

- write a sequential design card covering the signal representation, prediction-time information boundary, baseline, evaluation order, and operational constraints

Companion link:

- `book/companion/ch09/minimal/spectrogram_window_demo.py`
- `book/companion/ch09/practical/forecast_split_leakage_demo.py`

### Chapter 10: Experiments, Error Analysis, and Scientific Claims

Primary artifact:

- `An Experiment Claim Sheet`

Quick checks:

- distinguish a benchmark improvement from a justified scientific claim
- explain why aggregate metrics can hide slice failure
- identify when repeated runs are necessary
- explain what an ablation should reveal beyond "component removed, score changed"

Applied problems:

- rewrite an overstated result section into a bounded claim
- analyze a reported experiment and identify missing baselines, slices, or uncertainty reporting
- compare aggregate and slice metrics and decide what claim survives both views

Synthesis task:

- complete an experiment claim sheet for the support-assistant experimental story, including baseline ladder, ablation plan, repeated-run policy, slice checks, and claim boundary

Companion link:

- `book/companion/ch10/minimal/aggregate_vs_slice_demo.py`
- `book/companion/ch10/practical/ablation_and_repeated_runs_demo.py`

### Chapter 11: Reliability: Bias, Robustness, Privacy, and Safety

Primary artifact:

- `A Reliability Review Card`

Quick checks:

- distinguish overall accuracy from subgroup-specific behavior
- identify one plausible distribution shift and one adversarial or policy misuse risk
- explain a privacy risk that arises even when benchmark performance looks good
- explain why mitigations often trade one reliability dimension against another

Applied problems:

- evaluate subgroup confusion matrices and describe what reliability claim is still defensible
- propose a stress-test set for one realistic shift or misuse case
- compare a mitigation strategy before and after shift and explain what improved and what did not

Synthesis task:

- produce a reliability review card for the support assistant or another deployed system, including subgroup checks, robustness checks, privacy boundary, safety fallback, and unresolved risks

Companion link:

- `book/companion/ch11/minimal/subgroup_metrics_demo.py`
- `book/companion/ch11/practical/reliability_slice_checks_demo.py`

### Chapter 12: From Models to Systems

Primary artifact:

- `A System Readiness Brief`

Quick checks:

- distinguish model quality from system quality
- identify a training-serving contract that could silently break
- explain why thresholds and review budgets are system decisions
- name one monitoring signal that matters after launch

Applied problems:

- diagnose a training-serving skew incident from a pipeline description
- choose a selective-prediction or human-review policy under a finite review budget
- critique a deployment plan that reports model accuracy but no service contract or fallback path

Synthesis task:

- complete a system readiness brief for the support assistant, including interfaces, escalation path, monitoring, rollback plan, human-review capacity, and launch risks

Companion link:

- `book/companion/ch12/minimal/training_serving_skew_demo.py`
- `book/companion/ch12/practical/selective_prediction_pipeline_demo.py`

## Cross-Chapter Assignments

To make the book feel cumulative rather than episodic, add three explicit cross-chapter assignments:

1. `Part I synthesis`
   Start from a vague problem statement and produce a framing memo, evaluation plan, and first baseline design sheet.
2. `Part III synthesis`
   Compare one vision, one language, and one sequential problem using the relevant modality card from each chapter.
3. `Back-half capstone`
   Carry the support-assistant case through experiment design, reliability review, and system readiness.

## Build Order

Create the exercise layer in this order:

1. Chapters 1, 2, 8, 10, 11, and 12
2. Chapters 3, 5, and 7
3. Chapters 4, 6, and 9

This order matches the book's strongest identity: framing, evidence, grounded language systems, experiments, reliability, and deployment.

## Definition of Done

The exercise plan is complete when:

1. every chapter has a visible three-tier exercise ladder
2. every synthesis task terminates in a chapter artifact
3. the companion code supports at least one applied problem per chapter
4. the support-assistant case appears in the back-half synthesis tasks
5. an instructor can see how the exercises scale from short homework to larger project work
