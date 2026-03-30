# Instructor Guide

This guide is the first instructor-facing teaching package for **Machine Learning by Design: From Problem Framing to Reliable Systems**.

Detailed guidance on how to prepare and distribute instructor-only solutions lives in `instructor-solutions-guide.md`.

It is designed to answer four practical questions:

1. what kind of course the manuscript supports
2. how to sequence the chapters
3. how to use the companion code and chapter artifacts
4. what should remain public versus instructor-only

## Course Fit

The book is best suited for:

- a `10-12` week undergraduate introduction to machine learning and modern AI systems
- a concept-first bridge course between Python programming and more specialized ML courses
- a methods course that wants evaluation, reliability, and deployment to be first-class topics rather than an appendix

The book is less suitable as:

- a full artificial intelligence survey
- a theorem-first graduate text
- a fast-moving tool or API course

## Student Prerequisites

Minimum expected preparation:

- Python literacy
- high-school algebra
- comfort reading tables and plots

Helpful but not strictly required at the start:

- basic probability
- vectors and matrices
- exposure to derivatives

Recommendation:

- teach the manuscript as written and use prerequisite bridges rather than assuming all students arrive calculus-ready

## Teaching Philosophy

The book's strongest teaching move is its seven-question framework:

1. What decision are we supporting?
2. What task is the closest defensible proxy?
3. What data stands in for the world?
4. What representation exposes the relevant structure?
5. What is the simplest serious baseline?
6. What evidence justifies the claim?
7. How does the prediction become an action inside a real system?

Instructors should keep that framework visible across the whole course. The course works best when students repeatedly produce concrete artifacts rather than only model outputs.

## Recommended Teaching Paths

### Ten-Week Course

This path is the default recommendation for a first serious undergraduate course.

1. `Week 1`: Chapters 1 and 2
   Focus: framing, proxy targets, metrics, splits, leakage, threshold as policy
2. `Week 2`: Chapter 3
   Focus: linear models, features, baseline design
3. `Week 3`: Chapter 4
   Focus: trees, neighbors, clustering, structural mismatch
4. `Week 4`: Chapter 5
   Focus: neural networks, optimization, training reports
5. `Week 5`: Chapter 6
   Focus: embeddings, transfer, reuse and adaptation
6. `Week 6`: Chapter 7
   Focus: invariance, augmentation, shortcut learning, deployment-camera realism
7. `Week 7`: Chapters 8 and 9
   Focus: context, grounding, prediction-time realism
8. `Week 8`: Chapter 10
   Focus: experiments, ablations, repeated runs, claim audit
9. `Week 9`: Chapter 11
   Focus: reliability, subgroup checks, robustness, privacy, safety
10. `Week 10`: Chapter 12
    Focus: systems, selective prediction, monitoring, rollback, ownership

### Twelve-Week Course

This path leaves more room for exercises, mini-projects, and companion-code labs.

1. `Week 1`: Chapter 1
2. `Week 2`: Chapter 2
3. `Week 3`: Chapters 3 and 4
4. `Week 4`: Chapter 5
5. `Week 5`: Chapter 6
6. `Week 6`: Chapter 7
7. `Week 7`: Chapter 8
8. `Week 8`: Chapter 9
9. `Week 9`: Chapter 10
10. `Week 10`: Chapter 11
11. `Week 11`: Chapter 12
12. `Week 12`: capstone presentations, synthesis, or review

## Chapter Dependencies

Use these dependencies when compressing or expanding the course:

- `Chapter 1` is the entry point and should not be skipped.
- `Chapter 2` is foundational for every later claim about evidence.
- `Chapter 3` should come before Chapter 5.
- `Chapter 4` can be taught before or after Chapter 3, but works best after it.
- `Chapter 5` should come before Chapter 6.
- `Chapter 6` is helpful before Chapters 7 and 8, but not strictly required for Chapter 9.
- `Chapters 7, 8, and 9` can be taught as a modality block once Chapters 1 to 6 are in place.
- `Chapter 10` should precede Chapters 11 and 12.
- `Chapter 11` should precede or accompany Chapter 12.
- `Chapter 12` works best as the capstone chapter, not as an isolated systems appendix.

## What To Emphasize By Chapter

- `Chapter 1`: use the framing memo as an assignment, not just reading.
- `Chapter 2`: spend time on threshold as policy and leakage, not only metric formulas.
- `Chapter 3`: teach linear models as the first serious baseline, not the old method chapter.
- `Chapter 4`: emphasize structural mismatch rather than catalog coverage.
- `Chapter 5`: keep optimization and generalization tied to the training report artifact.
- `Chapter 6`: separate durable transfer ideas from current model-brand language.
- `Chapter 7`: make shortcut learning and deployment-camera realism central.
- `Chapter 8`: use the grounded support-assistant case throughout.
- `Chapter 9`: keep the chapter centered on what is legally known at prediction time.
- `Chapter 10`: force students to bound claims rather than celebrate score gains.
- `Chapter 11`: teach reliability as one pipeline question, not four side topics.
- `Chapter 12`: keep the unit of analysis at the system level rather than the model level.

## Companion Code Use

The companion code should support teaching in three layers:

1. `Minimal`
   Use for short labs, live walkthroughs, or homework where mechanics matter more than libraries.
2. `Practical`
   Use for modern workflows, validation habits, and stronger baseline comparisons.
3. `Extended`
   Reserve for optional projects or future material.

Recommended teaching pattern:

- use the printed chapter for concepts and artifacts
- use `minimal/` code for first contact
- use `practical/` code for the lab or implementation assignment

## Assignment Pattern

The manuscript is best taught with three recurring assignment types:

1. `Artifact assignments`
   Students produce the chapter document: framing memo, evaluation plan, baseline sheet, claim sheet, review card, or readiness brief.
2. `Companion-code labs`
   Students run, modify, and interpret the minimal or practical script for the chapter.
3. `Synthesis assignments`
   Students carry one case through several chapters instead of solving isolated toy tasks every week.

Recommended recurring case:

- grounded support assistant for the main cross-chapter spine
- dashboard-camera pedestrian detection as the recurring contrast case for robustness, safety, and deployment realism

Good secondary cases:

- dashboard-camera pedestrian detection
- wake-word or forecasting system

## Assessment Structure

One workable grading split:

- `20%` short checks or quizzes
- `25%` companion-code labs
- `35%` artifact and synthesis assignments
- `20%` final capstone or exam

If the course is more project-heavy, shift weight from quizzes to artifact-based work.

## Public vs Instructor Material

Public course materials should normally include:

- chapter readings
- quick checks
- applied problem statements
- companion-code entry points
- public hints
- at least one synthesis task per part of the book

Instructor-only materials should normally include:

- full applied-problem solutions
- grading notes for artifact submissions
- sample strong and weak answers
- answer keys for quizzes
- rubric notes for capstone work

## Solutions Policy

Recommended policy:

- keep short conceptual checks public
- keep full worked solutions to multi-step applied problems instructor-only
- keep synthesis-task rubrics instructor-only, but provide public checklists
- allow companion-code scripts to stay public, but do not publish graded answer reports tied to them

Reason:

- the book is trying to teach judgment, not only procedure
- artifact assignments lose value if students can copy a polished final document

## Suggested Rubric For Artifact Assignments

Use a simple four-part rubric:

- `Problem framing`: does the submission identify the real decision and constraints?
- `Technical justification`: are representation, baseline, metric, or policy choices defended coherently?
- `Evidence quality`: are claims bounded and supported by the right checks?
- `Operational realism`: does the student account for slices, failure modes, escalation, or deployment limits?

This rubric works across much of the book with only minor local adaptation.

## Sample Course Modes

### Concept-First Mode

Best for:

- mathematically mixed undergraduate classes
- courses with limited lab time

Pattern:

- emphasize reading, artifact writing, and short companion-code demonstrations

### Lab-Integrated Mode

Best for:

- machine learning courses with a weekly coding section

Pattern:

- pair each chapter with its `minimal/` or `practical/` script
- use labs to compare baselines, not only to reimplement models

### Systems-Capstone Mode

Best for:

- advanced undergraduates
- project courses that want a stronger endgame

Pattern:

- compress some middle chapters slightly
- spend more time on Chapters 8 to 12
- require a final experiment claim sheet, reliability review card, and system readiness brief

## Risks To Watch In Teaching

- students may default to model shopping instead of problem framing
- students may confuse fluency with grounding in Chapter 8
- students may treat Chapter 10 as research reporting style instead of scientific control
- students may hear Chapter 11 as ethics commentary instead of technical reliability analysis
- students may revert to model-only thinking in Chapter 12 unless the course keeps the system boundary visible

## Definition Of A Successful Course Use

By the end of the course, students should be able to:

- frame a problem before training
- choose and defend a serious baseline
- design honest evaluation
- explain what a modality-specific representation preserves
- bound an empirical claim
- review reliability under realistic failures
- decide whether a model is actually ready to become part of a system

If students can do those things, the course has taught the book's real contribution rather than only its chapter topics.
