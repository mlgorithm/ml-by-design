# Errata

This page tracks confirmed corrections to *Machine Learning by Design: From Problem Framing to Reliable Systems*.

## Reporting an error

Either path is welcome:

- **GitHub issue.** Open an issue at [github.com/mlgorithm/ml-by-design/issues](https://github.com/mlgorithm/ml-by-design/issues) with the label `errata`.
- **Email.** Write to the author at [sam.urmian@gmail.com](mailto:sam.urmian@gmail.com).

Please include:

- the version of the book (see [CHANGELOG.md](CHANGELOG.md)),
- the chapter and section,
- the page number in the PDF,
- the affected text or figure,
- and a short description of the issue and your suggested correction.

Reports of substantive errors, suggested clarifications, and clearer wording are all welcome. Confirmed contributions are acknowledged in the next release's CHANGELOG entry; if you would prefer not to be named, mention that in your report.

## Confirmed errata

### v1.0.0 (May 2026)

The following minor inconsistencies were caught in pre-publication review and corrected in v1.0.1:

- **Preface, audience and depth statement.** The opening audience sentence named only undergraduates, teachers, and self-learners, although the book also includes graduate-level material (probabilistic models, generative representations, reinforcement learning, ranking with counterfactual evaluation, and the formal treatment of reliability). The audience description and the core / Extension / Advanced Note depth convention were rewritten so that first-course readers and graduate-level readers can navigate the same chapters without confusion.
- **Chapter 4, "Linear Models and Representation," theorem on least-squares orthogonality.** The theorem and its proof briefly used `\beta` for the augmented coefficient vector while the surrounding chapter used `w`. The notation was harmonized to `w` throughout; the result is unchanged.
- **Chapter 14, "Sequential and Structured Data: Prediction-Time Realism," multimodal extension page-budget warning.** A reference to "Chapter 9" in the warning callout reflected the source filename rather than the printed chapter number; corrected to "this chapter."

## Process

Confirmed errata are listed above with the page, the correction, and the version in which the fix is incorporated. Significant errors trigger a patch release (for example, `v1.0.1`); accumulated minor corrections roll into the next monthly minor release.

The revision history is maintained in [CHANGELOG.md](CHANGELOG.md). Each release is tagged in git and minted as a new version on Zenodo, so any prior version of the book remains permanently citable via its version DOI.
