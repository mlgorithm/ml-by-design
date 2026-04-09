# Chapter 2b: Generalization and Evaluation Discipline

This directory contains practical materials for Chapter 2b of "Machine Learning by Design," which covers generalization, overfitting, model selection, and evaluation discipline.

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

- **Overfitting**: High training accuracy but low test accuracy. Indicates the model memorized noise.
- **Cross-validation**: Use k-fold CV to get robust estimates of test error without consuming data.
- **Sanity checks**: Always train on shuffled labels as a baseline. If performance is good, something is broken.
- **Learning curves**: Show how train/val error change with dataset size. Diagnose whether you need more data or more capacity.

## Prerequisites

- Python 3.7+
- numpy, matplotlib, scikit-learn

Install with:
```bash
pip install numpy matplotlib scikit-learn
```
