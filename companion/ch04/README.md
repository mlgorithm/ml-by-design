# Chapter 4 Companion

This chapter expands the book beyond single weighted-sum models.

It focuses on three kinds of structure:

- branching structure through trees
- local geometric structure through nearest neighbors
- unlabeled structure through clustering

## Minimal example

`minimal/structure_methods_from_scratch.py`

What it shows:

- impurity reduction for two candidate decision-tree root splits
- a k-nearest-neighbor example whose prediction changes after sensible feature scaling
- one full k-means assignment-and-recompute iteration

Install shared dependencies first:

```bash
python3 -m pip install -r companion/requirements.txt
```

Run it with:

```bash
python3 companion/ch04/minimal/structure_methods_from_scratch.py
```

## Practical example

`practical/structure_beyond_linearity_sklearn.py`

What it shows:

- logistic regression, decision tree, random forest, gradient boosting, and k-nearest-neighbor comparison on a nonlinear classification dataset
- a tree-depth sweep with train and validation performance
- k-means clustering plus PCA from four dimensions down to two on synthetic blobs

Install shared dependencies first:

```bash
python3 -m pip install -r companion/requirements.txt
```

Run it with:

```bash
python3 companion/ch04/practical/structure_beyond_linearity_sklearn.py
```
