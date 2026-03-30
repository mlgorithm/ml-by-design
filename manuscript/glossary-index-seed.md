# Glossary And Index Seed

This document seeds both the glossary and the back-of-book index.

The goal is not to finalize every definition now. The goal is to capture the terms most worth standardizing and indexing before a final editorial pass.

## High-Priority Glossary Terms

### Framing And Project Design

- `decision-first framing`
  Start from the real action, constraint, and mistake cost before choosing a model.

- `proxy target`
  The measurable label used as a stand-in for the broader real-world goal.

- `proxy audit`
  A check on how the measurable target may diverge from the real goal.

- `framing memo`
  The Chapter 1 artifact that turns a vague AI idea into a defensible learning problem.

- `baseline ladder`
  The rule of starting with the simplest serious model and increasing complexity only when the missing structure is named.

- `representation audit`
  A check on whether the chosen features or representation preserve the task-relevant structure.

### Evidence And Evaluation

- `leakage`
  Information from validation, test, or future data entering the training or feature-design process improperly.

- `calibration`
  The match between predicted probabilities and observed frequencies.

- `threshold as policy`
  The idea that threshold choice is an operational decision about workload, false alarms, and missed cases.

- `evaluation plan`
  The Chapter 2 artifact that records metrics, splits, thresholds, calibration, leakage controls, and baselines.

- `claim audit`
  The Chapter 10 technique of stating the intended claim first and testing what evidence actually supports it.

- `slice diagnosis`
  Inspection of subgroup or condition-specific failures before trusting aggregate metrics.

- `bounded conclusion`
  A conclusion whose scope matches the actual evidence rather than a stronger unsupported claim.

### Modeling And Generalization

- `regularization`
  Techniques that bias learning toward patterns expected to generalize.

- `overfitting`
  Improvement on seen data that does not hold on unseen data.

- `underfitting`
  Failure to capture enough structure even on the training data.

- `structure diagnosis`
  The Chapter 4 technique of naming the structural mismatch before switching model families.

- `reuse audit`
  The Chapter 6 technique of deciding how and whether to adapt a pretrained representation.

- `transfer learning`
  Reuse of representations or models across tasks or domains.

### Modality-Specific Terms

- `invariance audit`
  The Chapter 7 technique of stating which visual changes should preserve the label and which should not.

- `shortcut learning`
  Apparent competence driven by correlated but unintended cues rather than the true target concept.

- `context audit`
  The Chapter 8 technique for deciding whether token presence, local order, long-range context, or external grounding is needed.

- `grounding`
  Tying outputs to current external evidence rather than relying only on internal plausibility.

- `prediction-time audit`
  The Chapter 9 technique for defining decision time, allowed context, forbidden future information, and latency.

- `chronological split`
  A time-faithful evaluation split that preserves deployment order.

### Reliability And Systems

- `reliability`
  The umbrella term connecting bias, robustness, privacy, and safety in use.

- `robustness`
  The ability to behave reasonably under plausible changes in input or environment.

- `training-serving skew`
  A mismatch between the representation or preprocessing used in development and the one used in deployment.

- `pipeline realism`
  The Chapter 12 technique of asking what breaks when a notebook result becomes a service.

- `selective prediction`
  A system design in which some cases are automated and others are deferred to review.

- `rollback path`
  A mechanism for disabling, reverting, or constraining the deployed system after failure signals.

- `system readiness brief`
  The Chapter 12 artifact that records contracts, policy, review path, monitoring, rollback, and launch blockers.

## Index Seed By Priority

### Priority A: Must Appear In The Index

- AI, machine-learning core of
- baseline ladder
- bias
- calibration
- claim audit
- context audit
- decision-first framing
- evaluation plan
- framing memo
- grounding
- invariance audit
- leakage
- pipeline realism
- prediction-time audit
- proxy audit
- proxy target
- reliability
- rollback
- selective prediction
- slice diagnosis
- support assistant
- system readiness brief
- threshold as policy
- training-serving skew

### Priority B: Strong Supporting Entries

- abstention
- augmentation
- bag-of-words
- contextual representations
- domain shift
- error analysis
- experiment claim sheet
- framing
- human review
- monitoring
- n-grams
- overfitting
- privacy
- regularization
- representation
- retrieval
- reuse audit
- robustness
- shortcut learning
- structure diagnosis
- transfer learning

### Priority C: Optional Secondary Entries

- anomaly detection
- audio
- embeddings
- forecasting
- segmentation
- spectrogram
- threshold
- tokenization
- transformers
- vision design and stress-test card

## Preferred Cross-References

Use cross-references like these in a future index:

- `grounding`
  see also `retrieval`, `support assistant`, `context audit`

- `reliability`
  see also `bias`, `robustness`, `privacy`, `safety`

- `evaluation`
  see also `calibration`, `leakage`, `threshold as policy`, `slice diagnosis`

- `systems`
  see also `pipeline realism`, `training-serving skew`, `monitoring`, `rollback`

## Editorial Notes

1. The glossary should prefer short operational definitions over textbook-style encyclopedia entries.
2. The index should favor reusable techniques and artifacts, not only method names.
3. The recurring support-assistant case deserves index entries because it is the main narrative spine of the back half.
