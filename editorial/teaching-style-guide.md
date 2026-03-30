# Teaching Style Guide

This manuscript should teach students how to think in AI, not only how to recognize model names or reproduce software workflows.

## Core test for every chapter

Before finalizing a chapter, answer four questions:

- What question is the student being trained to ask?
- What reusable artifact should the student be able to produce afterward?
- What bad habit is the chapter trying to prevent?
- What would the student do differently on a real project after reading it?

If those answers are vague, the chapter is probably teaching content without teaching judgment.

## The editorial triad

Each chapter should rely on three distinct teaching devices with different jobs:

### 1. Pseudocode shows mechanism

Use pseudocode when the goal is to expose process, sequence, or control flow.

- Prefer pseudocode or plain-Python skeletons over library-specific APIs in the manuscript.
- Keep it short enough that a student can read the whole mechanism in one sitting.
- Use it for workflows such as threshold sweeps, training loops, retrieval pipelines, claim audits, or staged release plans.
- Introduce the code with one sentence about what students should notice.
- Put full runnable implementations in the companion materials, not in the main pedagogical line.

### 2. Theorem or Math Lens shows why a method behaves the way it does

Use a theorem only when it sharpens modeling judgment.

- Keep theorem-level math undergraduate-scale.
- Prefer one idea, one statement, one proof sketch, and one practical payoff.
- Place longer proofs inside a `Math Lens`, `Advanced Note`, or appendix when the main narrative is about decision-making rather than derivation.
- End every theorem with a plain-language modeling consequence.
- Do not let the main line of the chapter depend on completing the proof.

Good uses:

- why squared loss prefers the mean while absolute loss prefers a median
- why stacked affine layers without nonlinearities collapse to one affine map
- why Gini impurity is largest in a maximally mixed node

Weak uses:

- proofs included only because the topic "deserves math"
- derivations that do not change what a student would do

### 3. Artifact shows what good thinking looks like in practice

Every chapter should end in a reusable artifact such as a memo, sheet, card, plan, or brief.

- The artifact is where the chapter cashes out.
- It should be usable on a real assignment, project, or deployment review.
- It should connect clearly to the seven-question framework.
- Introduce the artifact early enough that later abstractions have somewhere to land.

Examples:

- framing memo
- evaluation plan
- baseline design sheet
- claim sheet
- reliability review card
- system readiness brief

## Recommended chapter rhythm

This is the default flow unless a chapter has a strong reason to differ:

1. Opening dilemma or decision problem
2. Plain-language conceptual frame
3. Worked example with concrete numbers, cases, or outputs
4. Pseudocode or mechanism sketch
5. Optional theorem or Math Lens for the key behavioral reason
6. Reusable artifact
7. Common mistakes, study questions, and exercises

## Extra rule for math chapters

When a chapter's main burden is mathematical, the chapter should still feel like a chapter in this book rather than a prerequisite packet.

- Start from a concrete AI task and the mathematical object the task forces the reader to understand.
- Use plain-language interpretation before compact notation.
- Work at least one small example by hand before presenting the general formula.
- Introduce the term for the idea only after the student understands the job the idea is doing.
- Treat theorems as explanatory pauses, not as the dominant chapter structure.
- End each math-heavy section with the modeling consequence: what this lets the student see, choose, or debug.

For loss functions and training objectives in particular, it is acceptable and useful to introduce a light functional-analysis viewpoint, but only at the level needed for the book: predictor as function, risk as functional, norm as size or complexity measure, and projection as fitting intuition.

## What to avoid

- Library-first exposition in the main text
- Theorems that arrive before the student knows why they care
- Dense notation before a plain-language statement of the object being described
- Artifacts that appear so late that the earlier abstractions feel ungrounded
- Method chapters that read like catalogs instead of answers to modeling dilemmas

## Preferred problem-solving techniques

Prefer reusing the manuscript's existing named techniques when they fit:

- cross-cutting: decision-first framing, proxy audit, representation audit, baseline ladder, claim audit, slice diagnosis, threshold as policy, pipeline realism
- AI-specific audits: reuse audit, invariance audit, context audit, prediction-time audit

Do not add a new named technique unless it teaches a genuinely different reasoning move.

## Editorial checkpoint

When revising a section, ask:

- Is this paragraph helping the student choose, judge, diagnose, or redesign something?
- If there is code here, is it showing a mechanism rather than a tool brand?
- If there is math here, does it change the student's modeling judgment?
- If there is a named framework here, does the chapter actually make the student use it?
