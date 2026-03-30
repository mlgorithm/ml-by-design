# Machine Learning by Design

**Machine Learning by Design: From Problem Framing to Reliable Systems** is a concept-first textbook in machine learning for undergraduates, instructors, and serious self-learners.

## Author

**Sam Urmian**
Researcher, SLATE: Centre for the Science of Learning & Technology
University of Bergen

sam.urmian@uib.no
[UiB profile](https://www4.uib.no/en/find-employees/sam.urmian) · [Google Scholar](https://scholar.google.com/citations?user=RktHIgcAAAAJ&hl=en) · [DBLP](https://dblp.org/search/author?q=Farhad+Vadiee) · [GitHub](https://github.com/mlgorithm)

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

## Publishing

This repository is set up for two public-facing outputs:

- a **Zenodo-backed citable release** using the root [`.zenodo.json`](.zenodo.json) metadata file
- a **GitHub Pages site** that publishes the current [book.pdf](book.pdf), cover preview, and citation metadata

### Zenodo

Zenodo can archive tagged GitHub releases and mint a DOI for each public edition.

1. Link your GitHub account to Zenodo.
2. Enable this repository in Zenodo.
3. Create a tagged GitHub release for the edition you want to archive.
4. After Zenodo mints the DOI, update `CITATION.cff`, the release notes, and the Pages site text if you want the DOI shown directly.

Zenodo will prefer [`.zenodo.json`](.zenodo.json) over `CITATION.cff` for GitHub release archiving, while GitHub itself will continue to use `CITATION.cff` for the repository citation box.

Use two DOI slots once the first release is archived:

- **Latest release DOI (concept DOI):** points to the project/book as a whole and resolves to the newest archived release
- **Exact release DOI (version DOI):** points to one specific tagged edition such as `v0.1.0`

### GitHub Pages

The Pages site source lives in [`pages/`](pages/), and the deployment workflow is [`pages.yml`](.github/workflows/pages.yml).

The workflow:

- copies the site template from `pages/`
- includes the current `book.pdf`
- includes `cover-preview.png`, `CITATION.cff`, and `LICENSE`
- deploys the result with GitHub Pages Actions

To turn it on in GitHub:

1. Open repository **Settings**.
2. Go to **Pages**.
3. Set the source to **GitHub Actions**.

Once enabled, the project site URL should be:

`https://mlgorithm.github.io/ml-by-desing/`
