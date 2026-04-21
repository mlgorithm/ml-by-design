# Instructor Solutions Guide

This document defines how to prepare instructor-only solutions and hints for **Machine Learning by Design: From Problem Framing to Reliable Systems** without leaking full answer keys into the public companion repository.

## Purpose

The book needs instructor support, but its strongest assignments are artifact-based and lose value if polished final answers become public.

This guide therefore separates:

- what can remain in the public repo
- what should be distributed only to verified instructors
- which chapters need full solution support first

## Distribution Rule

Recommended policy:

- keep full worked solutions out of the public repository
- keep public hints, starter templates, and rubrics in the main repo when useful
- distribute full instructor keys privately as a separate pack

Reason:

- the manuscript teaches judgment, not only procedure
- students should not be able to copy final memos, review cards, or readiness briefs

## Public Materials

Safe to keep public:

- quick-check questions
- applied problem statements
- short hints
- chapter artifact templates
- grading rubrics at a high level
- companion-code entry points

Use caution with:

- fully worked applied-problem writeups
- complete artifact examples tied directly to assignments
- model-selection narratives that solve the whole exercise for the student

## Instructor-Only Materials

Prepare these privately:

- answer keys for quick checks and quizzes
- worked solutions for applied problems
- grading notes for synthesis tasks
- sample strong, medium, and weak artifact submissions
- capstone evaluation rubrics with scoring notes
- common misconception notes by chapter

## Priority Order

Build instructor-only support in this order:

1. Chapters 1, 2, 3, 13, 16, 17, and 18
2. Chapters 4, 5, 7, 8, and 9
3. Chapters 6, 10, 11, 12, 14, and 15

This order matches the book's main differentiator: framing, evidence, grounded language systems, experiments, reliability, and systems.

## What To Prepare Per Chapter

Each chapter should eventually have:

1. `Quick-check key`
   One-line or short-form answers.
2. `Applied-problem notes`
   A worked path, not only the final answer.
3. `Synthesis-task rubric`
   Criteria for evaluating the artifact.
4. `Misconception notes`
   The most likely weak or misleading student response patterns.

## High-Priority Chapter Guidance

### Chapter 1

Instructor-only focus:

- what distinguishes a real decision from a target label
- what counts as a defensible proxy target
- what makes a framing memo weak versus credible

What to provide privately:

- one strong framing memo
- one weak framing memo with annotations
- a short grading rubric for decision, proxy, excluded inputs, and downstream action

### Chapter 2

Instructor-only focus:

- threshold choice as policy
- loss and metric interpretation
- calibration and action rules

What to provide privately:

- toy metric calculations
- one threshold-policy example
- one calibration example with commentary

### Chapter 3

Instructor-only focus:

- leakage detection
- train/validation/test split discipline
- baseline and sanity-check expectations

What to provide privately:

- one leakage diagnosis example
- one full minimal evaluation plan with commentary
- one weak baseline comparison and its corrected version

### Chapter 13

Instructor-only focus:

- deciding when bag-of-words is enough
- when retrieval and grounding are required
- when escalation is the correct output

What to provide privately:

- a context-audit key for at least two tasks
- one strong NLP context-and-grounding card
- examples of fluent but ungrounded answers that should score poorly

### Chapter 16

Instructor-only focus:

- claim bounding
- slice diagnosis
- ablation and repeated-run reasoning

What to provide privately:

- one overclaimed result rewritten into a bounded claim
- one experiment claim sheet with scoring notes
- one example where aggregate performance hides deployment-relevant failure

### Chapter 17

Instructor-only focus:

- how to distinguish reliability dimensions without splitting them into isolated topics
- how subgroup gaps and robustness failures interact

What to provide privately:

- one reliability review card
- one annotated subgroup-metrics example
- one mitigation tradeoff example that improves one dimension while leaving another unresolved

### Chapter 18

Instructor-only focus:

- system quality versus model quality
- review-capacity and selective-prediction tradeoffs
- monitoring, alerts, rollback, and ownership

What to provide privately:

- one system readiness brief
- one training-serving skew incident analysis
- one selective-prediction policy critique

## Hint-Writing Rules

Hints should:

- point students toward the right distinction
- not reveal the full artifact structure
- preserve the need for judgment

Good hint style:

- `Name the missing constraint before choosing the metric.`
- `Ask what information exists at decision time, not what would be useful in hindsight.`
- `State the strongest weaker claim before you try to defend the stronger one.`

Bad hint style:

- a disguised full solution
- a paragraph that fills every field in the artifact
- an answer that gives the exact final wording students should submit

## Suggested Private Pack Structure

If a private instructor pack is created later, use this structure:

```text
instructor-pack/
  ch01/
    quick-check-key.md
    applied-notes.md
    synthesis-rubric.md
  ch02/
    ...
```

Keep this private pack separate from the public repository.

## Definition Of Done

The instructor-solution layer is credible when:

1. the six priority chapters have private answer support
2. every synthesis task has a rubric
3. instructors can distinguish strong and weak artifact submissions
4. public hints exist without exposing full graded answers
5. the private pack can support adoption without undermining assignment integrity
