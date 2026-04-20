# Reliability Companion

This chapter supports the reliability perspective of the book.

It focuses on three ideas:

- subgroup metrics can reveal failures hidden by overall performance
- robustness must be checked under plausible shifts
- mitigation steps often create tradeoffs rather than universal improvement

## Minimal example

`minimal/subgroup_metrics_demo.py`

What it shows:

- two subgroup confusion matrices
- accuracy, true positive rate, and false positive rate for each group
- how one subgroup can look acceptable while another behaves very differently

Run it with:

```bash
python3 companion/ch11/minimal/subgroup_metrics_demo.py
```

What to notice:

- the subgroup gap is much clearer once TPR and FPR are separated
- overall correctness does not capture all important reliability behavior

Prerequisites:

- confusion matrices
- accuracy
- true positives, false positives, and false negatives

## Practical example

`practical/reliability_slice_checks_demo.py`

What it shows:

- a synthetic majority/minority classification problem
- a baseline logistic-regression model and a simple group-balancing mitigation
- subgroup accuracy on a clean test set
- subgroup accuracy after a minority-group input shift

Run it with:

```bash
python3 companion/ch11/practical/reliability_slice_checks_demo.py
```

What to notice:

- overall accuracy can remain high while minority-group accuracy is much lower
- the subgroup gap widens under shift
- balancing the training data improves minority-group performance but does not eliminate the shift problem

Prerequisites:

- train/test splits
- logistic regression
- subgroup evaluation
