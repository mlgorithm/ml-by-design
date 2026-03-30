# Figure Plan

This document defines the visual production plan for **Solving AI Problems**.

The manuscript already contains many conceptual figures in the front half. The main remaining visual problem is uneven distribution: the chapters that now make the book distinctive, especially Chapters 7 to 12, are still relatively text-heavy.

## Goal

The figure system should do three things:

1. make the book's core workflows easier to remember
2. reduce text density in the back half
3. give the manuscript a consistent visual language that feels intentional rather than assembled chapter by chapter

## Current State

The manuscript already has strong figure coverage in the method-heavy foundation chapters:

- Chapter 1: `5` figure environments
- Chapter 2: `9`
- Chapter 3: `8`
- Chapter 4: `10`
- Chapter 5: `14`
- Chapter 6: `10`

The visual gap is in the newer, more differentiated chapters:

- Chapter 7: `1`
- Chapter 8: `1`
- Chapter 9: `0`
- Chapter 10: `0`
- Chapter 11: `1`
- Chapter 12: `1`

The repository currently contains only three external image assets:

- `figures/external/road_scene_crossing_small.jpg`
- `figures/external/syntax_tree_clean.png`
- `figures/external/zech2018_g003_small.png`

That means the highest-leverage next step is not image hunting. It is building a small set of durable explanatory diagrams for the back half.

## Visual Strategy

Prefer three figure types:

1. `Workflow diagrams`
   Best for Chapter 8, Chapter 10, Chapter 11, and Chapter 12.
2. `Evaluation or failure diagrams`
   Best for Chapter 7, Chapter 9, Chapter 10, and Chapter 11.
3. `System architecture or policy diagrams`
   Best for Chapter 8 and Chapter 12.

Use external images only when a real-world visual object matters:

- one or two vision scenes
- one or two reproduced study figures when they make a literature point that would be weak if redrawn generically

Avoid decorative images that do not carry explanatory load.

## Style Guide

### Figure roles

Every figure should answer one of these questions:

- what is the workflow?
- what is the failure mode?
- what is the comparison?
- what is the system boundary?

If a figure cannot answer one of those, it is probably not worth adding.

### Diagram conventions

Use a single default visual grammar for new conceptual diagrams:

- rounded rectangles for stages, components, or documents
- consistent arrow direction from left to right or top to bottom
- one neutral fill family rather than chapter-specific color experiments
- short labels inside nodes
- captions that explain the modeling judgment, not just restate the picture

### Text and caption rules

- keep text inside figures short enough to read at normal print scale
- keep notation consistent with the surrounding chapter
- captions should explain why the figure matters for the chapter's argument
- do not use captions as mini-essays

### Tables vs figures

Some current explanatory tables are doing figure work. When the object is a process, dependency, or architecture, prefer a diagram. When the object is a comparison grid, checklist, or artifact template, keep it as a table.

## Priority Figure List

These are the highest-value figures to add next.

### Priority 1: Back-half anchor figures

1. `Chapter 8: Grounded support-assistant pipeline`
   Purpose: show routing, slot reading, retrieval, escalation, and grounded answer generation in one diagram.
   Why it matters: Chapter 8 is now built around this case, but the workflow currently lives mostly in prose and tables.
   Status: `new`

2. `Chapter 9: Prediction-time information boundary`
   Purpose: show what is known and unknown at decision time for sequential problems.
   Why it matters: this is the chapter's main idea and currently has no figure environment.
   Status: `new`

3. `Chapter 10: Claim audit to scientific argument`
   Purpose: show the seven-step protocol from claim to bounded conclusion.
   Why it matters: the chapter needs one memorable visual that turns experimental discipline into a reusable checklist-shaped diagram.
   Status: `new`

4. `Chapter 11: Reliability as one pipeline`
   Purpose: show how subgroup gaps, shift, privacy, and safety enter different parts of the same system.
   Why it matters: Chapter 11's differentiator is integration, not separate subtopics.
   Status: `new`

5. `Chapter 12: Deployment review loop`
   Purpose: extend the current system view with monitoring, rollback, and ownership feedback loops.
   Why it matters: the existing Chapter 12 figure is useful but still slightly thin relative to the chapter's systems role.
   Status: `revise existing`

### Priority 2: Modality and failure figures

6. `Chapter 7: Shortcut-learning slice map`
   Purpose: visualize clean success versus shifted failure across camera or environment slices.
   Why it matters: Chapter 7 now argues for deployment realism, and one figure should make the slice story visible at a glance.
   Status: `new`

7. `Chapter 8: Representation ladder for text`
   Purpose: contrast bag-of-words, n-grams, contextual encoding, and retrieval grounding as progressively richer structure-preserving choices.
   Why it matters: the chapter explains these transitions well, but a reader should be able to see the ladder in one glance.
   Status: `new`

8. `Chapter 10: Aggregate metric versus slice failure`
   Purpose: visualize how a respectable overall result can hide collapse on a critical slice.
   Why it matters: this is one of the chapter's strongest reusable lessons.
   Status: `new`

9. `Chapter 11: Reliability tradeoff diagram`
   Purpose: show how one mitigation can improve one slice or risk while leaving another unresolved.
   Why it matters: Chapter 11 should visibly resist the fantasy of one-metric fixes.
   Status: `new`

### Priority 3: Front-half cleanup where useful

10. `Chapter 1: Formalize the framing memo as a visual artifact`
    Purpose: make the Chapter 1 memo visually match the artifact language used in Chapters 2 to 12.
    Why it matters: this would strengthen the continuity of the toolkit.
    Status: `revise existing`

11. `Chapter 2: Threshold as policy`
    Purpose: tighten the threshold-and-capacity story into one cleaner visual if the current combination of tables and figures feels repetitive.
    Why it matters: Chapter 2 is already visually strong, so this is refinement rather than expansion.
    Status: `optional refine`

## Chapter-by-Chapter Visual Goals

### Chapter 7

Target outcome:

- keep the external road image
- add one explanatory figure for shortcut-learning slices
- optionally add one small deployment-camera mismatch diagram if the chapter still reads too text-heavy after the slice figure

### Chapter 8

Target outcome:

- at least two strong conceptual figures
- one figure for the grounded support-assistant workflow
- one figure for the representation ladder or grounding boundary

### Chapter 9

Target outcome:

- add at least one anchor figure
- prioritize the prediction-time boundary over modality-specific decoration

### Chapter 10

Target outcome:

- add at least two figures
- one for the claim-audit protocol
- one for aggregate-versus-slice interpretation

### Chapter 11

Target outcome:

- keep the Zech et al. shift figure
- add one integrated reliability-pipeline figure
- add one tradeoff figure only if it sharpens the chapter rather than repeating the prose

### Chapter 12

Target outcome:

- revise the current pipeline figure into a more complete service loop
- if needed, add one selective-prediction or review-capacity diagram

## Implementation Guidance

### Default tool choice

Prefer `TikZ` for new conceptual diagrams because:

- the manuscript already uses it
- it keeps style consistent with the LaTeX source
- it avoids introducing image-export workflow overhead

Use raster or external figures only when:

- the source image itself is pedagogically important
- the figure comes from literature and should be cited or reproduced faithfully

### Where figures should live

For reusable or complex new diagrams, prefer adding source assets under:

- `figures/generated/`

For simple one-off diagrams, inline `tikzpicture` blocks in the chapter are acceptable if they remain short and readable.

### Visual consistency checks

Before calling the figure pass complete, verify:

- node sizes and label density feel similar across chapters
- arrow styles are consistent
- caption tone matches the rest of the manuscript
- figures do not create awkward page breaks or large whitespace islands

## Production Order

Create figures in this order:

1. Chapter 8 support-assistant pipeline
2. Chapter 10 claim-audit diagram
3. Chapter 11 reliability-pipeline diagram
4. Chapter 9 prediction-time boundary
5. Chapter 12 deployment-review-loop revision
6. Chapter 7 shortcut-learning slice map
7. optional front-half refinements

This order matches the book's current competitive advantage: grounded language systems, evidence, reliability, and systems.

## Definition of Done

The figure plan is complete when:

1. Chapters 7 to 12 no longer feel visibly under-illustrated relative to Chapters 1 to 6
2. the support-assistant case has at least one strong visual in the chapters where it anchors the argument
3. the back half has memorable workflow and failure diagrams, not only tables and prose
4. the visual system feels like one book rather than two differently illustrated halves
5. no added figure is decorative or redundant
