# Chapter 4b Companion

This chapter supports designing and preparing datasets for machine learning with realistic quality challenges.

It focuses on seven ideas:

- annotation protocols and inter-annotator agreement
- label noise and its effects on model performance
- class imbalance and handling techniques
- active learning and uncertainty sampling
- data augmentation in feature space
- synthetic data generation
- measuring and monitoring dataset quality

## Minimal example

`minimal/annotation_noise_demo.py`

What it shows:

- generating a small synthetic binary classification dataset
- simulating symmetric and asymmetric label noise
- training logistic regression on clean vs. noisy labels
- computing Cohen's kappa inter-annotator agreement
- comparing accuracy degradation under different noise scenarios

Run it with:

```bash
python3 companion/ch04b/minimal/annotation_noise_demo.py
```

What to notice:

- symmetric noise (random flips) degrades performance proportionally for both classes
- asymmetric noise (one class flipped preferentially) creates class-specific blindness
- inter-annotator agreement captures disagreement between two simulated annotators
- even moderate noise (10-20%) significantly reduces final accuracy

Prerequisites:

- binary classification
- logistic regression fundamentals
- confusion matrix and accuracy metrics
- basic probability

## Practical example

`practical/dataset_design_lab.ipynb`

What it shows:

- label noise effects on model robustness across noise rates
- class imbalance detection and the impact of weighted training
- feature-space augmentation and decision boundary effects
- pool-based active learning with uncertainty sampling
- comparison of active learning vs. random sampling

Run it with:

```bash
jupyter notebook companion/ch04b/practical/dataset_design_lab.ipynb
```

What to notice:

- accuracy drops smoothly with symmetric label noise; use robustness techniques
- imbalanced classes hide poor minority-class performance in raw accuracy
- class weights and F1 score together reveal true classifier behavior
- augmentation with noise can help generalization but may hurt tight decision boundaries
- active learning queries uncertain points efficiently, reducing label cost
- random sampling requires 2-3× more labels to reach the same accuracy as uncertainty sampling

Prerequisites:

- train/validation/test splits
- binary and multiclass classification metrics (precision, recall, F1)
- logistic regression and decision boundaries
- uncertainty in probabilistic classifiers
- basic probability sampling concepts
