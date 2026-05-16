# Machine Learning by Design

**Public Draft v0.9 — Open Review Edition, May 2026.** A concept-first open educational resource in machine learning and modern AI, written for IOAI students, computer science undergraduates, instructors, graduate students, and serious self-learners. Circulated for community review and classroom use ahead of the first stable edition (v1.0). Actively maintained at the University of Bergen.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19341954.svg)](https://doi.org/10.5281/zenodo.19341954)
[![Edition: v0.9 Public Draft](https://img.shields.io/badge/Edition-v0.9%20Public%20Draft-orange)](CHANGELOG.md)

— [Read the PDF](ml-by-design.pdf) · [Latest release on Zenodo](https://doi.org/10.5281/zenodo.20232975) · [Adopt in your course](companion/instructor-guide.md) · [How to cite](#how-to-cite) · [Report errata](ERRATA.md) · [Changelog](CHANGELOG.md)

**DOIs.** Latest release v0.9: [`10.5281/zenodo.20232975`](https://doi.org/10.5281/zenodo.20232975). Concept DOI (always resolves to latest): [`10.5281/zenodo.19341954`](https://doi.org/10.5281/zenodo.19341954). Cite the version DOI for reproducibility; use the concept DOI for general references.

## Why this book

Real model-based AI work begins with a problem. What decision are we supporting? What evidence do we have? What claim are we making? And what would justify trusting the result? This book is organized around those questions. It is problem-driven rather than algorithm-driven — models, losses, architectures, and systems appear because they resolve modeling dilemmas, and each method enters through the decision, data, representation, evidence, and system constraints that make it useful.

The book covers task formulation, predictive modeling, loss functions, decision rules, evaluation, baselines, linear models, trees, neural networks, representation learning, foundation-model workflows, modality-specific modeling, experiments, uncertainty, reliability, and deployment-minded AI systems — across six parts, nineteen chapters, two mathematical bridge chapters, and six part-synthesis chapters.

## Companion materials

The [`companion/`](companion/) directory contains chapter-aligned code in three layers — `minimal/` (Python + NumPy, library-stable), `practical/` (scikit-learn and PyTorch), and `extended/` (optional projects). Code is MIT-licensed.

The [Instructor Guide](companion/instructor-guide.md) provides 10-week and 12-week course paths, a chapter-dependency map, three assignment patterns (artifact, lab, synthesis), a four-part rubric, and three teaching modes (concept-first, lab-integrated, systems-capstone). Sample instructor solutions are in [`companion/instructor-solutions/`](companion/instructor-solutions/); the public set covers selected chapters with more added each release.

## License

- Book text, original figures, and cover art: **CC BY-NC-SA 4.0** (see [LICENSE](LICENSE))
- Companion code under [`companion/`](companion/): **MIT** (see [`companion/LICENSE`](companion/LICENSE))

Third-party materials retain their stated licenses unless explicitly noted.

## Maintenance

This edition is a living open educational resource. The maintenance cadence is:

- **Patch releases** as needed for confirmed errata.
- **Minor releases** monthly for small additions and corrections.
- **Larger updates** aligned with the academic calendar in September and January.

Errata are accepted via GitHub issues with the `errata` label, or by email to the author. See [ERRATA.md](ERRATA.md) for the workflow and confirmed errata; see [CHANGELOG.md](CHANGELOG.md) for the revision history.

## How to cite

This project has two citable artifacts: the **book draft** and the **companion code**. The Zenodo *concept DOI* below resolves to the latest version of each. When reproducibility matters, cite the specific *version DOI* assigned by Zenodo at the time of the release you used (visible on the corresponding Zenodo record page).

### Cite the book draft

```bibtex
@book{urmian2026mlbd,
  author    = {Urmian, Sam},
  title     = {Machine Learning by Design: From Problem
               Framing to Reliable Systems},
  year      = {2026},
  publisher = {Zenodo},
  version   = {Public Draft v0.9 (Open Review Edition)},
  doi       = {10.5281/zenodo.19341954},
  url       = {https://github.com/mlgorithm/ml-by-design},
  note      = {Concept DOI shown; cite the version DOI from
               the Zenodo deposit you used when
               reproducibility matters. CC BY-NC-SA 4.0.}
}
```

### Cite the companion code

```bibtex
@software{urmian2026mlbd_code,
  author    = {Urmian, Sam},
  title     = {Machine Learning by Design: Companion Code},
  year      = {2026},
  publisher = {Zenodo},
  version   = {0.9.0},
  url       = {https://github.com/mlgorithm/ml-by-design},
  license   = {MIT},
  note      = {Cite the version DOI of the GitHub release
               archived on Zenodo when reproducibility
               matters.}
}
```

## Contact

Sam Urmian — SLATE, Centre for the Science of Learning & Technology, University of Bergen
[`sam.urmian@gmail.com`](mailto:sam.urmian@gmail.com)
