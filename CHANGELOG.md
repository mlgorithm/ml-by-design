# Changelog

All notable changes to *Machine Learning by Design: From Problem Framing to Reliable Systems* are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and version numbers follow a semantic-versioning scheme adapted for a living textbook:

- **MAJOR** — new edition (significant structural change, e.g. second edition).
- **MINOR** — new chapter, significant new content, or major rewrite of a chapter.
- **PATCH** — confirmed errata, small additions, and corrections.

Each release is tagged in git and minted as a new version on Zenodo. The concept DOI [`10.5281/zenodo.19341954`](https://doi.org/10.5281/zenodo.19341954) resolves to the latest version; cite a specific version DOI when reproducibility matters.

## [Unreleased] — Conceptual and mathematical revision

- Removed the 19 PowerPoint lecture decks and their upload script; aligned local builds, PDF automation, and the website with the revised working PDF.
- Rechecked all 90 numbered chapter/bridge figures and the unnumbered gradient-step sketch against their mathematics, prose, and rendered pages.
- Replaced hand-drawn scalar regularization paths with their exact formulas, preserved cosine geometry with equal embedding-axis scales, corrected the gradient-step arrow and annotation, and clarified the external hospital-study plot's populations, confidence intervals, and logarithmic scale.

- Reviewed Chapters 13--19 as code-free explanations of language, structured observations, ranking, tables, experiments, reliability, and complete decision systems.
- Corrected language likelihood and decoding claims, forecasting information boundaries, audio framing arithmetic, contrastive gradients, graph normalization, ranking denominators, exposure assumptions, and fold-specific target encoding.
- Developed experimental uncertainty around the stated estimand and unit; distinguished ablations from causal explanations, predictive risk from intervention benefit, and privacy and coverage guarantees from informal assurances.
- Added worked calculations for constrained decisions, fluctuating queues, complete fallback risk, distributional monitoring, distillation gradients, quantization error, and cascade latency.
- Consolidated repetitive scaffolding, simplified diagrams, strengthened mathematical exercises, and updated the conclusion, part syntheses, and notation reference; added primary references and corrected the mismatched Lipkus risk-communication citation.

- Reviewed Chapters 10--12 as code-free treatments of generation, interaction, and vision; integrated mathematical assumptions, cautions, advanced results, and common mistakes into the explanations.
- Reworked VAE likelihood bounds and latent distributions, ideal GAN objectives and optimization limitations, diffusion conditional denoising and reverse approximations, and representation-dependent generative evaluation.
- Developed reinforcement learning around an explicit small MDP, Bellman evaluation and optimality, numerical TD and Q-learning updates, discounted policy gradients, bandit exploration, potential-based reward shaping, preference models, and logged-policy evaluation assumptions.
- Clarified visual output and annotation conventions, detection matching and overlap metrics, convolution geometry and sharing, receptive fields, downsampling counterexamples, task-dependent augmentation, and the limits of shortcut and saliency evidence.
- Simplified diagrams and repetitive prose, replaced underspecified exercises with self-contained calculations and derivations, and added primary references; corrected the road-scene photograph's author to www.Pixel.la Free Stock Photos.
- Reviewed Chapters 7--9 as a connected, code-free treatment of optimization, probabilistic inference, and representation learning; integrated assumptions, cautions, and advanced results into the main explanations.
- Expanded the neural-network example through a complete binary-loss gradient and parameter update; corrected initialization symmetry, adaptive-moment interpretation, dropout averaging, gradient clipping, and the limits of loss-curve diagnosis.
- Reworked latent-variable inference with a numerical Gaussian-mixture EM step, an explicit likelihood-bound argument, covariance-collapse and model-selection caveats, Bayesian prediction, and regression and classification uncertainty decompositions.
- Added mathematical examples for information loss, representation geometry, contrastive objectives, attention, permutation equivariance, and low-rank adaptation; corrected claims about probing, reconstruction, uncertainty, and attention explanations.
- Simplified the three chapters' diagrams and exercises, aligned the student case with the week-2 cutoff and future deadline proxy, and added primary references; corrected the probability bridge's expected-log-joint/ELBO distinction, Jensen assumptions, squared Mahalanobis distance, and later pointers to the latent-variable chapter.
- Reviewed Chapters 4--6 as a connected progression from representation and linear fitting to nonlinear objectives and dataset design, with mathematical assumptions and cautions integrated into the explanations.
- Corrected regularization normalization and bias--variance conditions, tree split and neighbor arithmetic, ensemble dependence, conditional-independence claims, margin guarantees, and PCA reconstruction notation.
- Reworked dataset design around population coverage, agreement versus validity, noisy-label posteriors and corrected losses, prevalence correction, label-source dependence, valid augmentation, and synthetic-population risk; added worked derivations and verified numerical exercises.
- Simplified the three chapters' diagrams and tables, removed repeated teaching scaffolding, aligned the student example with the week-2 cutoff and future deadline proxy, and added primary references for the methods discussed.
- Reviewed Chapter 3; corrected generalization-gap and bias--variance interpretations, bounded-loss assumptions, cross-validation dependence, and the scope of protected evaluation.
- Added worked sampling-error and selection-bias calculations, nested cross-validation, group and time boundaries, and stronger code-free exercises; corrected authors of the cited biological leakage paper.
- Revised the openings and connections across all nineteen chapters and both mathematical bridges.
- Replaced programming listings with worked mathematical examples and implementation exercises with calculations, derivations, and interpretation.
- Reworked the preface, part syntheses, and conclusion around the conceptual progression of the book.
- Corrected claims about calibration, weighted losses, regularization, ensemble risk, initialization, Bayesian uncertainty, generative objectives, policy gradients, counterfactual evaluation, privacy, conformal coverage, experimental power, and review capacity.
- Updated references for tabular modeling and several mathematical results; labeled uncited numerical examples as illustrative.
- Repaired equation and table layout, including the multipage notation reference.
- Integrated mathematical lenses, warnings, advanced notes, and distinct common-mistake cautions into the relevant chapter explanations.
- Removed separate common-mistake checklists, Looking Ahead sections, and Chapter Summary sections throughout the chapters and mathematical bridges.
- Corrected additional mathematical and statistical claims encountered during integration, preserving derivations and their assumptions.
- Redesigned chapter diagrams with a restrained shared palette, natural print sizes, shorter labels, and simpler comparison layouts.
- Added conceptual figures for latent-variable inference, generative mechanisms, recommendation feedback, and mixed-type tabular representation.
- Corrected geometric inconsistencies in XOR, PCA, nearest-neighbor, and clustering illustrations; retained third-party empirical imagery and its attribution.
- Clarified multimodal fusion assumptions and the limits of masking interventions when diagnosing visual shortcuts.
- Reviewed and streamlined Chapter 1 around a consistent prediction cutoff, future deadline target, and student--course case; distinguished proxy accuracy from intervention benefit and label noise.
- Added mathematical explanations of training loss, recall under a review budget, and transformed score thresholds; strengthened the numerical exercises and corrected learning-setting definitions.
- Reviewed and streamlined Chapter 2; corrected the distinctions between population precision and sample counts, prevalence and ROC behavior, score calibration and conditional probability, and review capacity and intervention benefit.
- Added conditional loss derivations, squared-probability propriety, explicit cost and abstention assumptions, expected-positive ranking under a budget, and exercises that extend the worked examples; removed repeated teaching scaffolding and unsupported empirical generalizations.

## [0.9.0] — 2026-05-15 — Public Draft / Open Review Edition

**Zenodo:** version DOI [`10.5281/zenodo.20232975`](https://doi.org/10.5281/zenodo.20232975) · [record page](https://zenodo.org/records/20232975)

Renamed and repositioned the planned 1.0.x release as a **Public Draft v0.9 / Open Review Edition** for community review and classroom use. The first stable release will remain v1.0, after the review period.

### Added
- **AI-use statement** on the colophon page, naming Anthropic Claude and OpenAI ChatGPT as the assistants used during drafting, copy-editing, cover-image generation, and companion-code production. Author retains responsibility for every claim, derivation, citation, figure, and code listing.
- **Cover-art credit** on the colophon page: cover composition by the author, generated with OpenAI's GPT-4 image tool in 2026 in a Da Vinci-notebook visual register; CC BY-NC-SA 4.0.
- **Road-scene reference figure** in Chapter 12 (Vision), `figures/external/road_scene_crossing_small.jpg` — Wikimedia Commons, www.Pixel.la Free Stock Photos, CC0 (author corrected in the unreleased revision). Used to illustrate shortcut-cue analysis at the start of the vision chapter.

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
[0.9.0-zenodo]: https://doi.org/10.5281/zenodo.20232975
