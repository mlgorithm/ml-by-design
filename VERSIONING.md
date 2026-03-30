# Versioning

This repository uses release tags as the canonical public editions of the book.

## Tag Format

Use tags in the form:

- `v0.x.y` for evolving pre-release editions
- `v1.0.0` for the first stable public edition
- `v1.0.1`, `v1.0.2`, ... for correction-only releases
- `v1.1.0`, `v1.2.0`, ... for additions that preserve the overall chapter structure
- `v2.0.0` for major restructuring or a substantially changed edition

## Release Rule

Each GitHub release should correspond to one citable state of:

- the manuscript source
- `book.pdf`
- `cover.pdf`
- `full-cover.pdf`

## Zenodo

If Zenodo is connected to this repository:

1. create the Git tag
2. publish the GitHub release
3. let Zenodo archive that release
4. record the DOI in the release notes and in `CITATION.cff`

Use the version DOI for citations to a specific edition. Use the concept DOI only as the stable pointer to the latest archived release.
