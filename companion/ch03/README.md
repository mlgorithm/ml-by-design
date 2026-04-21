# Chapter 4 Companion: Linear Models and Representation (`ch03`)

This chapter is about the simplest durable predictive models:

- linear regression for numeric prediction
- logistic regression for binary classification
- features as the bridge between raw data and model behavior
- regularization as a way to control overly large weights

The code here supports that in two layers.

## Minimal example

`minimal/linear_and_logistic_from_scratch.py`

What it shows:

- ordinary least squares on a small synthetic housing-style dataset
- ridge-style regularization in a NumPy implementation
- logistic regression trained with gradient descent on a small student-support dataset
- interpretable coefficients for both tasks

Run it with:

```bash
python3 companion/ch03/minimal/linear_and_logistic_from_scratch.py
```

## Practical example

`practical/linear_and_logistic_sklearn.py`

What it shows:

- `scikit-learn` versions of the same two model families
- train/test evaluation
- coefficient inspection after feature scaling for logistic regression

Run it with:

```bash
python3 companion/ch03/practical/linear_and_logistic_sklearn.py
```
