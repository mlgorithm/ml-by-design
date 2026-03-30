# Chapter 2 Companion

This chapter is about three closely connected ideas:

- losses used during training
- metrics used during evaluation
- the difference between fitting training data and generalizing to new data

The code here supports that in two layers.

## Minimal example

`minimal/metric_tradeoffs.py`

What it shows:

- same accuracy with very different log loss
- binary cross-entropy on a tiny set of predicted probabilities
- threshold-dependent metrics such as accuracy, precision, recall, and F1
- simple calibration-bin summaries
- why one set of probabilities can support different operating points

Run it with:

```bash
python3 companion/ch02/minimal/metric_tradeoffs.py
```

## Practical example

`practical/overfitting_demo_sklearn.py`

What it shows:

- a train/validation/test split on synthetic data
- a flexible model family with varying depth
- how training accuracy can keep rising while validation accuracy stops improving
- choosing a model on validation data and reporting test accuracy once

Run it with:

```bash
python3 companion/ch02/practical/overfitting_demo_sklearn.py
```
