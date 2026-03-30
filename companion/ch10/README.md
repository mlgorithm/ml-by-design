# Chapter 10 Companion

This chapter supports the shift from model building to experimental reasoning.

It focuses on three ideas:

- aggregate metrics can hide important slice failures
- repeated runs matter when results are stochastic or data-dependent
- ablations should reveal tradeoffs, not just produce a single best score

## Minimal example

`minimal/aggregate_vs_slice_demo.py`

What it shows:

- a model with a respectable overall accuracy
- a much weaker subgroup hidden inside that overall number
- a direct calculation of overall and slice-specific performance

Run it with:

```bash
python3 book/companion/ch10/minimal/aggregate_vs_slice_demo.py
```

What to notice:

- the overall metric looks acceptable
- one slice is still clearly weak
- slice-based evaluation changes what claim is justified

Prerequisites:

- basic accuracy calculation
- the idea of evaluation slices or subgroups

## Practical example

`practical/ablation_and_repeated_runs_demo.py`

What it shows:

- a clean-accuracy and shifted-accuracy evaluation on digit images
- a baseline model without augmentation and an ablated model with shift augmentation
- repeated runs across several seeds with mean and standard deviation reporting

Run it with:

```bash
python3 book/companion/ch10/practical/ablation_and_repeated_runs_demo.py
```

What to notice:

- the baseline looks strong if you report only clean accuracy
- the shifted slice reveals a major robustness failure
- the augmentation ablation creates a clear tradeoff: worse clean accuracy, much better shifted robustness

Prerequisites:

- train, validation, and test splits
- logistic regression
- mean and standard deviation across repeated runs
