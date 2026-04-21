# Chapter 3 Companion: Generalization, Leakage, and Evaluation Discipline (`ch02b`)

This directory contains practical materials for Chapter 3 of "Machine Learning by Design," stored under the historical `ch02b` source directory name. It covers generalization, leakage, overfitting, model selection, and evaluation discipline.

## Contents

- **practical/generalization_lab.ipynb** — A fully worked Jupyter notebook demonstrating:
  - Overfitting in polynomial regression (the U-curve)
  - Cross-validation for model selection
  - Shuffled-label sanity checks
  - Learning curves and their interpretation

## Quick Start

1. Open `practical/generalization_lab.ipynb` in Jupyter
2. Run all cells to see demonstrations of overfitting, CV, and learning curves
3. Modify the polynomial degrees, regularization, or dataset size to experiment

## Key Concepts

- **Overfitting**: High training performance or low training error with worse validation or test performance. Often indicates the model has learned noise or sample-specific structure.
- **Cross-validation**: Use k-fold CV on the training data for model selection and stability checks; keep a final untouched test set when making a final claim.
- **Sanity checks**: Always train on shuffled labels as a baseline. If performance is good, something is broken.
- **Learning curves**: Show how train/val error change with dataset size. Diagnose whether you need more data or more capacity.

## Prerequisites

- Python 3.11+ for current scikit-learn releases
- numpy, matplotlib, scikit-learn

Install with:
```bash
pip install numpy matplotlib scikit-learn
```
