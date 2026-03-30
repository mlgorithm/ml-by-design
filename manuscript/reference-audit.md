# Reference Audit

This document records the current state of the manuscript bibliography and the highest-value cleanup work before a final editorial pass.

## Current Status

High-confidence checks:

- cited bibliography keys found in manuscript: `25`
- missing bibliography keys referenced in text: `0`
- unused entries currently present in `references.bib`: `0`

This means the manuscript is structurally sound at the BibTeX level: there are no broken citation keys in the current source.

## Chapter Citation Density Snapshot

Approximate citation counts by chapter:

- Chapter 1: `7`
- Chapter 2: `6`
- Chapter 3: `2`
- Chapter 4: `1`
- Chapter 5: `2`
- Chapter 6: `4`
- Chapter 7: `1`
- Chapter 8: `3`
- Chapter 9: `0`
- Chapter 10: `0`
- Chapter 11: `1`
- Chapter 12: `0`

## High-Priority Cleanup

1. `Strengthen citation-light back-half chapters`
   Chapters 9, 10, and 12 currently have no citations. That is not automatically wrong, but one or two anchor references each could make the scholarly framing stronger, especially if the manuscript will be reviewed by technical readers expecting supporting literature.

2. `Check low-citation chapters for balance`
   Chapters 4, 7, and 11 are also relatively light. Review whether that is intentional or whether one additional anchor citation would improve credibility without turning the book into a survey.

3. `Standardize web-reference notes`
   The web-based `@misc` entries are usable, but access-note formatting should be standardized in the final editorial pass.

## Interpretation

The bibliography is not in bad shape. The main issue is not broken citations. The main issue is uneven reference density.

The front half already has enough references to feel anchored. The back half, especially the systems-facing chapters, now carries a lot of the manuscript's distinctiveness but is comparatively citation-light. That is the place where a final scholarly pass should be most deliberate.

## Recommended Next Pass

Use this sequence:

1. add one or two anchor references to Chapters 9, 10, and 12 if they materially strengthen the chapter
2. standardize `@misc` notes and access-date wording
3. do one final compile check after bibliography edits

## Do Not Overcorrect

The book is not trying to become a literature review. The goal of the reference pass is:

- remove obvious bibliography drift
- support the strongest conceptual claims
- avoid citation deserts in the chapters most likely to face expert scrutiny

It is not necessary to saturate every page with references.
