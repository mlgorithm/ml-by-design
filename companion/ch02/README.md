# Chapter 2 Companion: Prediction, Loss, and Decision Rules (`ch02`)

This chapter is about three closely connected ideas:

- losses used during training
- metrics used during evaluation
- thresholds, ranked-list policies, abstention, and calibration as action choices

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

## Notebook lab

`practical/metrics_and_tradeoffs_lab.ipynb`

Use this notebook when students need a fuller guided pass through threshold choice, calibration summaries, metric tradeoffs, and the metric-and-action worksheet.
