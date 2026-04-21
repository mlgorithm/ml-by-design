# Chapter 18 Companion: From Models to Systems (`ch12`)

This chapter supports the systems view of the book.

It focuses on three ideas:

- a deployed system can fail even when the trained model file is unchanged
- thresholds and review policies are system decisions, not only model details
- operational constraints such as review capacity change what counts as a good design

## Minimal example

`minimal/training_serving_skew_demo.py`

What it shows:

- a classifier that expects features standardized with training-set statistics
- a buggy serving pipeline that uses the wrong statistics
- the same raw examples receiving different scores and decisions because the feature contract is broken

Run it with:

```bash
python3 companion/ch12/minimal/training_serving_skew_demo.py
```

What to notice:

- the model weights do not change
- the predicted probabilities still move substantially
- the system degrades because the preprocessing pipeline changed

Prerequisites:

- feature standardization
- binary classification scores
- the idea of training-serving skew

## Practical example

`practical/selective_prediction_pipeline_demo.py`

What it shows:

- a logistic-regression risk model on a synthetic student-support dataset
- full automation at a fixed threshold
- a selective-prediction system with a finite human-review budget
- the tradeoff between automated coverage and overall system quality

Run it with:

```bash
python3 companion/ch12/practical/selective_prediction_pipeline_demo.py
```

What to notice:

- the best model-only policy is not automatically the best system policy
- sending the most uncertain cases to review can improve the full system
- review capacity becomes a first-class design constraint

Prerequisites:

- train/test splits
- logistic regression
- confidence scores and thresholds
