# Terminology Sheet

This document is the source of truth for the manuscript's recurring vocabulary.

Its job is to keep the book's language coherent across chapters, front matter, companion materials, and reviewer-facing documents.

## Core Positioning Language

Use these phrases consistently when describing the book:

- `problem-driven`
- `machine learning, evaluation, and reliable AI systems`
- `the machine-learning core of modern AI`
- `the full modeling arc`
- `undergraduate-first`

Preferred one-sentence description:

**A problem-driven introduction to machine learning, evaluation, and reliable AI systems.**

## Book-Level Framework

Preferred term:

- `seven-question framework`

Acceptable variant:

- `seven-question method`

Avoid introducing new top-level framework brands that compete with this language.

The seven questions are:

1. decision
2. proxy task
3. data
4. representation
5. baseline
6. evidence
7. system action

## Named Reusable Techniques

These are the book's core named techniques. Keep them stable.

### Cross-book core

- `decision-first framing`
  Chapter 1
  Start from the action, constraint, and cost of mistakes before model choice.

- `proxy audit`
  Chapter 1
  Separate the real-world goal from the measurable target.

- `baseline ladder`
  Chapters 2 and 3
  Start with the simplest serious model and climb only when the missing structure is named.

- `claim audit`
  Chapter 10
  State the claim first, then test what weaker claim is supported and what stronger claim remains unsupported.

- `slice diagnosis`
  Chapter 10
  Inspect deployment-relevant failures before trusting aggregate metrics.

- `threshold as policy`
  Chapter 2
  Treat thresholds, abstention, and review load as operational choices, not cleanup details.

- `pipeline realism`
  Chapter 12
  Ask what breaks when a notebook result becomes a service.

### Chapter-specific techniques that should still stay stable

- `representation audit`
  Chapter 3

- `structure diagnosis`
  Chapter 4

- `reuse audit`
  Chapter 6

- `invariance audit`
  Chapter 7

- `context audit`
  Chapter 8

- `prediction-time audit`
  Chapter 9

These chapter-specific terms are good and should be preserved. They do not compete with the core cross-book set; they refine it by modality or modeling setting.

## Chapter Artifacts

These titles should be treated as canonical.

- `Framing memo`
  Chapter 1
  Note: this is already the real Chapter 1 artifact, even though it is not yet formatted as a formal `Chapter Artifact` section heading.

- `A Minimal Evaluation Plan`
  Chapter 2

- `A First Baseline Design Sheet`
  Chapter 3

- `A Structure Diagnosis Sheet`
  Chapter 4

- `A Minimum Credible Neural Training Report`
  Chapter 5

- `A Reuse and Adaptation Plan`
  Chapter 6

- `A Vision Design and Stress-Test Card`
  Chapter 7

- `An NLP Context-and-Grounding Card`
  Chapter 8

- `A Sequential Design Card`
  Chapter 9

- `An Experiment Claim Sheet`
  Chapter 10

- `A Reliability Review Card`
  Chapter 11

- `A System Readiness Brief`
  Chapter 12

## Teaching Devices And Structural Labels

These labels are part of the manuscript's scaffolding and should stay consistent:

- `Problem-Solving Technique`
- `Problem-Solving Lens`
- `Decision Box`
- `Failure Box`
- `Evidence Box`
- `Practical Note`
- `Advanced Note`
- `Prereq Bridge`
- `Chapter Artifact`

Use them when they sharpen the chapter's central judgment. Do not multiply new box labels casually.

## Terms To Use Carefully

### `Five Commitments`

Keep this term local to Chapter 1.

Preferred framing:

- `Chapter 1's local framing protocol inside the broader seven-question framework`

Avoid presenting it as a second book-wide branded framework.

### `AI` versus `machine learning`

Preferred formulation:

- the book covers the `machine-learning core of modern AI`

Avoid language that implies the manuscript is a full survey of all AI.

### `grounding`

Use `grounding` to mean connection to current external evidence or authoritative sources.

Do not use it as a vague synonym for:

- fluency
- coherence
- general realism

### `reliability`

Use `reliability` as the umbrella term connecting:

- bias
- robustness
- privacy
- safety

Do not let those four read like disconnected appendices.

### `support assistant`

Preferred running-case phrase:

- `grounded course-support assistant`

Shorter acceptable variants:

- `support assistant`
- `course-support assistant`

Use one of these rather than introducing several near-synonyms for the same running system.

## Capitalization And Style Rules

- Use named techniques in lower case in ordinary prose: `claim audit`, `baseline ladder`, `pipeline realism`.
- Use title case only in headings, formal boxes, or display labels.
- Use artifact names in title case when referring to the specific chapter deliverable.
- Use lower case for generic references such as `the evaluation plan` or `a readiness brief` unless referring to the canonical artifact title.
- Prefer `machine learning` over `ML` in formal manuscript prose unless space is tight.
- Prefer `grounded` over `RAG-style` or API-era jargon in the main text.

## Current Consistency Notes

These are the current manuscript-level consistency rules or remaining cleanup items:

1. `Language: Context and Grounding` is the correct Chapter 8 title.
   Older wording such as `Context and Generation` should be retired.
2. `Framing memo` is already Chapter 1's real artifact.
   A later polish pass may formalize it as a `Chapter Artifact` heading for perfect parallelism.
3. `Five Commitments` should stay subordinate to the seven-question framework.
4. The recurring support-assistant case should be named consistently across manuscript, companion, and reviewer materials.

## Editorial Test

When introducing a new term, ask:

1. Does this name replace a weaker generic phrase?
2. Does it clarify a real modeling move?
3. Does it compete with an existing core label?

If the answer to the third question is yes, do not add it casually.
