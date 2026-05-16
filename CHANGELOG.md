# Changelog

All notable changes to *Machine Learning by Design: From Problem Framing to Reliable Systems* are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and version numbers follow a semantic-versioning scheme adapted for a living textbook:

- **MAJOR** — new edition (significant structural change, e.g. second edition).
- **MINOR** — new chapter, significant new content, or major rewrite of a chapter.
- **PATCH** — confirmed errata, small additions, and corrections.

Each release is tagged in git and minted as a new version on Zenodo. The concept DOI [`10.5281/zenodo.19341954`](https://doi.org/10.5281/zenodo.19341954) resolves to the latest version; cite a specific version DOI when reproducibility matters.

## [0.9.0] — 2026-05-15 — Public Draft / Open Review Edition

Renamed and repositioned the planned 1.0.x release as a **Public Draft v0.9 / Open Review Edition** for community review and classroom use. The first stable release will remain v1.0, after the review period.

### Added
- **AI-use statement** on the colophon page, naming Anthropic Claude and OpenAI ChatGPT as the assistants used during drafting, copy-editing, cover-image generation, and companion-code production. Author retains responsibility for every claim, derivation, citation, figure, and code listing.
- **Cover-art credit** on the colophon page: cover composition by the author, generated with OpenAI's GPT-4 image tool in 2026 in a Da Vinci-notebook visual register; CC BY-NC-SA 4.0.
- **Road-scene reference figure** in Chapter 12 (Vision), `figures/external/road_scene_crossing_small.jpg` — Wikimedia Commons, Jay Galvin, CC0. Used to illustrate shortcut-cue analysis at the start of the vision chapter.

### Changed
- **Edition language** on title-page colophon: "First edition, 2026" replaced with "Public Draft v0.9 --- Open Review Edition, May 2026" and a sentence inviting feedback.
- **Preface, audience and depth-tier statement.** Widened the named audience to include IOAI students and early graduate readers alongside undergraduates, teachers, and self-learners, and made the core / Extension / Advanced Note depth convention explicit so first-course readers and graduate-level readers can navigate the same chapters.
- **Chapter openings (13 of 19).** Style pass to reduce uniform "Chapter N did X. This chapter does Y." pattern. Distributed openers across scene/vignette, concrete failure case, question, and running-case continuation forms.
- **Chapter 4 (`ch03.tex`), least-squares orthogonality theorem.** Local `\beta` notation in the theorem and proof harmonized to `w` to match the chapter's standing convention.
- **Cross-chapter transitions (5 fixes).** Five "previous/next chapter" lines in `ch04b`, `ch06`, `ch09`, `ch10` re-anchored to explicit `\ref` after the satellite chapters were inserted between main chapters.
- **Code-block wrapping.** Two long code lines in `ch09b` (`verbatim` and `\verb|...|`) reformatted so they no longer overflow the Royal Octavo trim.

### Verified
- Build clean: 0 undefined references, 0 undefined citations, 0 multiply-defined labels, 0 BibTeX warnings, 0 overfull hboxes, 655 pages.
- All 32 companion scripts (17 minimal + 15 practical) execute successfully with `requirements.txt`.

[0.9.0]: https://github.com/mlgorithm/ml-by-design/releases/tag/v0.9.0
