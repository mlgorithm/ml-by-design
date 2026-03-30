# Companion Code

This directory contains the runnable code that accompanies the book.

Instructor-facing course guidance lives in `instructor-guide.md`.
Instructor-only solutions scaffolding and distribution guidance live in `instructor-solutions-guide.md`.
This repository only contains the book-facing companion code, not a separate
coding-lab site.

The key design rule is simple:

- The manuscript should stay concept-first and durable.
- The companion code should stay practical and updateable.

AI-LAB follows that rule as a Markdown-first docs site under `ai-lab/docs/`, built with the configuration in `ai-lab/mkdocs.yml`.

## Three coding layers

Each chapter should eventually have three layers of implementation support.

### 1. Minimal

Small programs with almost no dependencies. These are meant to show mechanics clearly and survive library churn.

Typical tools:

- Python standard library
- NumPy
- matplotlib

### 2. Practical

Short, modern examples using stable mainstream libraries. These are meant to show how the same idea is implemented in real workflows.

Typical tools:

- scikit-learn
- PyTorch

### 3. Extended

Optional notebooks, experiments, or larger projects that go beyond the printed book. These can change faster than the manuscript.

## Default stack

The companion code should prefer:

- `Python`
- `NumPy`
- `matplotlib`
- `scikit-learn`
- `PyTorch`

Avoid making the book depend on:

- vendor SDKs
- fast-moving LLM wrappers
- orchestration frameworks
- APIs that may change every few months

## Directory convention

Use the following shape for each chapter:

```text
book/companion/chXX/
  README.md
  data/
  minimal/
  practical/
  extended/
```

Not every chapter needs all directories immediately, but the structure should remain consistent.

## License

Unless a file says otherwise, code in this directory is licensed under the MIT
License; see `LICENSE` in this directory.
