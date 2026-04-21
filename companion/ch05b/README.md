# Chapter 8 Companion: Probabilistic Models and Latent Structure (`ch05b`)

This chapter supports the move from point predictions to distributions, latent variables, and uncertainty.

It focuses on three ideas:

- latent assignments in mixture models
- probabilistic baselines and soft responsibilities
- uncertainty as an input to downstream decisions

## Minimal example

`minimal/gmm_em_1d_demo.py`

What it shows:

- a tiny one-dimensional Gaussian mixture
- the E-step as soft assignment to latent components
- the M-step as weighted parameter updates
- sensitivity to initialization

Run it with:

```bash
python3 companion/ch05b/minimal/gmm_em_1d_demo.py
```

What to notice:

- points near the overlap region receive mixed responsibilities
- EM improves the log likelihood but can still depend on initialization
- the latent component label is inferred rather than observed

Prerequisites:

- Gaussian density
- weighted averages
- log likelihood

## Practical example

`practical/gmm_uncertainty_sklearn.py`

What it shows:

- fitting Gaussian mixture models with scikit-learn
- using BIC to compare candidate values of `K`
- inspecting posterior responsibilities as an uncertainty signal
- flagging low-confidence points for review

Run it with:

```bash
python3 companion/ch05b/practical/gmm_uncertainty_sklearn.py
```

What to notice:

- the best aggregate model is not the same as certainty on every point
- responsibility entropy identifies ambiguous examples near component overlap
- an uncertainty audit should state what downstream action changes when uncertainty is high

Prerequisites:

- train/test splits
- Gaussian mixture models
- basic NumPy arrays
