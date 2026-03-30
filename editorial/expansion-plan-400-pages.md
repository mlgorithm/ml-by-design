# Expansion Plan Toward 400 Pages

This document turns the page-count requirement into a content plan.

The goal is not to inflate layout. The goal is to expand the manuscript until it reads like a genuinely full textbook.

## Current State

Rough current prose counts from the manuscript source:

- `preface.tex` `1207`
- `ch01.tex` `4917`
- `ch02.tex` `7345`
- `ch03.tex` `6226`
- `ch04.tex` `5974`
- `ch05.tex` `5561`
- `ch06.tex` `5656`
- `ch07.tex` `4352`
- `ch08.tex` `4776`
- `ch09.tex` `4235`
- `ch10.tex` `3807`
- `ch11.tex` `3564`
- `ch12.tex` `5431`
- `math-foundations.tex` `1031`
- `conclusion.tex` `459`

Current total prose is about `64.5k` words.

That is manuscript length for a short textbook, not a 400-page full textbook.

## Practical Page Target

With the current manuscript layout in `tex/book.tex`, a serious `400`-page result probably needs roughly:

- `130k-145k` words of real prose
- more anchor figures and worked examples
- fuller exercises and chapter-end artifacts
- larger appendices and teaching matter

That means the real gap is about:

- `+65k` to `+80k` words

## Expansion Rule

Only add material that improves one of these:

1. teachability
2. evidence and rigor
3. recurring case depth
4. cross-domain transfer
5. exercise and artifact usability

Do not add:

- filler history
- broad AI-survey detours that fight the current positioning
- framework tutorials that will age badly
- page-count padding by typography tricks

## Target Shape

### Front Matter

- `Preface`: expand to `1.5k-2k`
  Add adoption case, how to use artifacts, how book and `ai-lab/` relate.

### Part I: Foundations

- `Chapter 1`: grow from `4.9k` to `8k-9k`
  Add:
  - one more fully worked framing case outside education
  - explicit bad-framing to good-framing rewrites across 4-5 domains
  - a deeper section on proxy failure and unacceptable inputs
  - a formal chapter artifact section with annotated strong/weak memos

- `Chapter 2`: grow from `7.3k` to `10.5k-11.5k`
  Add:
  - richer metric tradeoff walkthroughs
  - calibration and threshold policy examples
  - stronger leakage case studies
  - one extended worked evaluation plan from start to finish

- `Chapter 3`: grow from `6.2k` to `9.5k-10.5k`
  Add:
  - more coefficient interpretation examples
  - stronger regularization discussion
  - representation design in tabular, text, and risk scoring cases
  - one full baseline memo from framing to first model

- `Chapter 4`: grow from `6.0k` to `9k-10k`
  Add:
  - deeper comparison among trees, neighbors, clustering, PCA
  - more model-selection dilemmas
  - a longer structure-diagnosis workflow
  - one cross-domain case comparing nonlinear mismatch types

### Part II: Deep Learning

- `Chapter 5`: grow from `5.6k` to `9.5k-10.5k`
  Add:
  - stronger optimization diagnosis
  - a more concrete regularization section
  - failure analysis for training curves
  - a full worked neural training report

- `Chapter 6`: grow from `5.7k` to `9.5k-10.5k`
  Add:
  - deeper representation-learning evidence
  - stronger transfer case comparisons
  - a fuller adaptation-depth section
  - a broader foundation-model claim discipline section

### Part III: Modalities

- `Chapter 7`: grow from `4.4k` to `8.5k-9.5k`
  Add:
  - more visual invariance examples
  - augmentation as a modeling claim
  - shortcut learning case studies
  - one extended detector deployment story

- `Chapter 8`: grow from `4.8k` to `9.5k-10.5k`
  Add:
  - more lexical/contextual baseline comparisons
  - stronger retrieval-grounding evidence
  - a fuller system workflow for routing, retrieval, answer, escalation
  - failure modes of fluent but ungrounded behavior

- `Chapter 9`: grow from `4.2k` to `8k-9k`
  Add:
  - fuller forecasting evaluation
  - stronger audio representation examples
  - more temporal leakage and deployment realism
  - one repeated running case through sensor/audio/time settings

### Part IV: Evidence, Reliability, and Systems

- `Chapter 10`: grow from `3.8k` to `8.5k-9.5k`
  Add:
  - more ablation design
  - repeated-runs examples with interpretation
  - stronger slice-analysis workflows
  - a full experiment claim sheet walkthrough

- `Chapter 11`: grow from `3.6k` to `8.5k-9.5k`
  Add:
  - more subgroup metric examples
  - stronger privacy and safety mechanics
  - richer robustness cases
  - a full reliability review card with worked critiques

- `Chapter 12`: grow from `5.4k` to `9.5k-10.5k`
  Add:
  - more system-design casework
  - monitoring and rollback scenarios
  - human review and capacity planning examples
  - a full readiness brief and launch review section

### Appendix Layer

- `math-foundations.tex`: grow from `1.0k` to `8k-12k`
  Add:
  - probability essentials
  - linear algebra for vectors, matrices, projections
  - optimization basics
  - statistics essentials for evaluation
  - notation and reading-math bridges

### Back Matter

- `Conclusion`: grow from `0.5k` to `1k-1.5k`
  Add:
  - synthesis of the seven-question framework
  - where the reader should go next

## Highest-Yield Additions

If the goal is both better quality and more pages, prioritize these first:

1. Expand Chapters `8-12`
   These are your differentiator and currently some of the shortest chapters.

2. Formalize every chapter artifact as a standalone, teachable section
   This adds real value, not fluff.

3. Add one second full running contrast case through the middle chapters
   Not just references to a contrast case, but repeated actual reuse.

4. Deepen worked examples and failure analysis
   Every method chapter should have at least one long worked story, not only local snippets.

5. Expand the appendix substantially
   This is the cleanest way to add real support pages without harming the main narrative.

## Word Budget

Recommended added-word budget:

- Part I: `+14k`
- Part II: `+8k`
- Part III: `+13k`
- Part IV: `+20k`
- Appendix and front/back matter: `+12k`

Total target addition:

- `+67k`

That would put the manuscript at about `131k` words before final layout changes.

## Execution Order

1. `Chapter 8`
   It is too short for how central grounding and language systems are to the book.
2. `Chapter 10`
   Claim audit and experiment discipline should be one of the longest chapters, not one of the shortest.
3. `Chapter 11`
   Reliability is underweight relative to the stated positioning.
4. `Appendix`
   A larger math and statistics bridge increases both usability and justified length.
5. `Chapters 1 and 12`
   Stronger opening and ending materially improve the whole book.

## Immediate Next Move

The best next move is:

- expand `Chapter 8` by `3k-4k` words

Why:

- it is short
- it is central to the back-half spine
- it can absorb more worked workflow, retrieval, grounding, and failure-analysis material without distorting the book
- gains here improve both uniqueness and length
