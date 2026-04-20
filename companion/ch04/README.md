# Structure Beyond Linearity Companion

This chapter expands the book beyond single weighted-sum models.

It focuses on five kinds of structure:

- branching structure through trees
- margin structure through support vector machines
- probabilistic class-conditional structure through Naive Bayes
- local geometric structure through nearest neighbors
- unlabeled structure through clustering and dimensionality reduction

The companion code emphasizes trees, nearest neighbors, clustering, and PCA; the SVM and Naive Bayes sections are text-first previews in the chapter.

## Minimal example

`minimal/structure_methods_from_scratch.py`

What it shows:

- impurity reduction for two candidate decision-tree root splits
- a k-nearest-neighbor example whose prediction changes after sensible feature scaling
- one full k-means assignment-and-recompute iteration

Run it with:

```bash
python3 companion/ch04/minimal/structure_methods_from_scratch.py
```

## Practical example

`practical/structure_beyond_linearity_sklearn.py`

What it shows:

- logistic regression, decision tree, random forest, gradient boosting, and k-nearest-neighbor comparison on a nonlinear classification dataset
- a tree-depth sweep with train and validation performance
- k-means clustering plus PCA on synthetic blobs

Run it with:

```bash
python3 companion/ch04/practical/structure_beyond_linearity_sklearn.py
```
