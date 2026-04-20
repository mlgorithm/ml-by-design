# Chapter Companion Template

Use this template when adding coding material for a chapter.

## Goals

- Keep the code tied directly to one or two core ideas from the chapter.
- Separate conceptual clarity from library-specific convenience.
- Prefer small examples that students can read in one sitting.
- Support both later-bachelor students and mathematically ambitious readers without watering down the material.

## Required files

```text
companion/chXX/
  README.md
  data/
  minimal/
  practical/
```

## README checklist

Each chapter README should state:

- which parts of the book chapter the code supports
- what the minimal example demonstrates
- what the practical example demonstrates
- how to run both examples
- what students should notice in the outputs
- which mathematical prerequisites the examples assume

## Manuscript checklist

Each chapter in the book should aim to contain:

- learning goals
- a short `Problem-Solving Lens` near the opening that states the chapter's modeling dilemma
- substantial sections and subsections, not compressed summary paragraphs
- at least one worked example with concrete numbers or decisions
- at least one named problem-solving technique when the chapter introduces a reusable habit of thought
- recurring `Decision Box`, `Failure Box`, or `Evidence Box` callouts when they clarify the chapter's main judgment
- at least one `Prerequisite Bridge` when new notation or math maturity is assumed
- at least one `Advanced Note` for stronger readers who want a faster or deeper track
- common mistakes
- chapter summary
- study questions
- exercises
- challenge exercises

## Teaching standard

The manuscript should use three teaching devices with clearly different jobs:

- `Pseudocode` shows the mechanism.
- `Theorem` or `Math Lens` shows why the mechanism behaves that way.
- `Artifact` shows what good AI thinking looks like in practice.

When drafting a chapter, check four questions:

- what question is the student being trained to ask?
- what artifact should the student be able to produce afterward?
- what bad habit is the chapter trying to prevent?
- what would the student do differently on a real project after reading it?

Good chapter-level defaults:

- prefer pseudocode or plain-Python skeletons over library-specific APIs in the main text
- keep theorem-level math undergraduate-scale and tie it to a modeling consequence
- place longer proofs in a `Math Lens`, `Advanced Note`, or appendix when the main line is decision-first
- introduce the chapter artifact early enough that later abstractions have somewhere to land

## Minimal example checklist

- Should run with standard Python or very few dependencies.
- Should show the mechanics of the idea clearly.
- Should use small local data when possible.
- Should print interpretable output rather than only saving files.

## Practical example checklist

- Should use stable, mainstream libraries.
- Should follow current best practice without being overly clever.
- Should be short enough for teaching.
- Should make the bridge between theory and real tooling explicit.

## Suggested chapter mapping

- Chapter 1: problem framing
- Chapter 2: prediction, loss, and decision rules
- Chapter 3: generalization, leakage, and evaluation discipline
- Chapter 4: linear models and representation
- Chapter 5: structure beyond linearity
- Chapter 6: dataset design
- Chapter 7: optimization and neural networks
- Chapter 8: probabilistic models and latent structure
- Chapter 9: representation learning and foundation models
- Chapter 10: generative representations
- Chapter 11: reinforcement learning
- Chapter 12: vision
- Chapter 13: language
- Chapter 14: audio, time, and prediction-time realism
- Chapter 15: ranking, recommendation, and exposure
- Chapter 16: experiments and scientific claims
- Chapter 17: reliability
- Chapter 18: models to systems
