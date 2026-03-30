# Machine Learning by Design

**Machine Learning by Design: From Problem Framing to Reliable Systems** is a concept-first textbook in machine learning for undergraduates, instructors, and serious self-learners.

The book is organized around a single practical question: how do you move from a vague real-world problem to a defensible model claim and then to a reliable system? Rather than teaching machine learning as either a catalog of methods or a software stack, the manuscript keeps problem framing, evidence, reliability, and system design in view from the beginning.

## What This Repo Contains

- `companion/`
  chapter companion material that stays close to the printed text
- `tex/`
  LaTeX source for the manuscript, covers, figures, bibliography, and chapter files
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

Build everything from the repository root:

```bash
make all
```

Or build individual targets:

```bash
make book
make cover
make full-cover
```

The `Makefile` keeps the LaTeX source under `tex/` while writing the compiled
PDFs back to the repository root.

If you prefer the raw commands:

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir=.. tex/book.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir=.. tex/cover.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir=.. tex/full-cover.tex
```

## Versioning

This repository is intended to be released with Git tags and GitHub releases.

- Use `v0.x.y` while the manuscript is still changing substantially.
- Use `v1.0.0` for the first public citable edition.
- Use patch releases for typo, figure, math, and layout corrections.
- Use minor releases for added sections, examples, or exercises.

See [VERSIONING.md](VERSIONING.md) for the release convention used here.

## License

The repository uses a split license model.

- The manuscript text, original figures, and covers are licensed under
  `CC BY-NC-SA 4.0`; see [LICENSE](LICENSE).
- Code in [`companion/`](companion/) is licensed under `MIT`; see
  [companion/LICENSE](companion/LICENSE).
- Third-party assets are excluded from those blanket licenses unless explicitly
  stated; see [THIRD_PARTY.md](THIRD_PARTY.md).

## Citation

GitHub will read [CITATION.cff](CITATION.cff) for repository citation metadata. If you mint a Zenodo DOI, update the citation file and release notes so the tagged version and DOI point to the same edition.
