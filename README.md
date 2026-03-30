# Machine Learning by Design

**Machine Learning by Design: From Problem Framing to Reliable Systems** is a concept-first textbook in machine learning for undergraduates, instructors, and serious self-learners.

The book is organized around a single practical question: how do you move from a vague real-world problem to a defensible model claim and then to a reliable system? Rather than teaching machine learning as either a catalog of methods or a software stack, the manuscript keeps problem framing, evidence, reliability, and system design in view from the beginning.

## What This Repo Contains

- `book.tex`
  main LaTeX entry point for the manuscript
- `frontmatter/`, `chapters/`, `appendices/`, `backmatter/`
  source files for the book
- `figures/`
  TikZ and supporting figure assets
- `companion/`
  chapter companion material that stays close to the printed text
- `manuscript/`
  editorial notes, review materials, and planning documents
- `book.pdf`
  current compiled manuscript
- `cover.pdf`
  standalone front cover
- `full-cover.pdf`
  wrap cover with back and spine

## Core Method

The manuscript keeps seven recurring questions visible:

1. What decision are we supporting?
2. What task is the closest defensible proxy?
3. What data stands in for the world?
4. What representation exposes the relevant structure?
5. What is the simplest serious baseline?
6. What evidence justifies the claim?
7. How does the prediction become an action inside a real system?

## Build

Build the manuscript from the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

Build the standalone covers:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error cover.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error full-cover.tex
```

## Versioning

This repository is intended to be released with Git tags and GitHub releases.

- Use `v0.x.y` while the manuscript is still changing substantially.
- Use `v1.0.0` for the first public citable edition.
- Use patch releases for typo, figure, math, and layout corrections.
- Use minor releases for added sections, examples, or exercises.

See [VERSIONING.md](VERSIONING.md) for the release convention used here.

## Citation

GitHub will read [CITATION.cff](CITATION.cff) for repository citation metadata. If you mint a Zenodo DOI, update the citation file and release notes so the tagged version and DOI point to the same edition.
