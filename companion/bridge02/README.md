# Bridge II Companion

This bridge supports probability, loss functions, and optimization concepts for machine learning.

It focuses on four ideas:

- Bayes' theorem and how priors affect posterior beliefs
- the sigmoid function as a probability link for binary models
- log-loss (binary cross-entropy) and its role in measuring prediction quality
- gradient descent and convergence with different learning rates

## Practical example

`practical/probability_risk_lab.ipynb`

What it shows:

- Bayes' theorem applied to a student crisis detection classifier
- how varying the prior belief changes the posterior probability
- the sigmoid function mapping real-valued scores to numbers in `(0, 1)` for binary probability estimates
- effect of input scaling on sigmoid steepness
- log-loss curves showing penalty for confident wrong predictions
- gradient descent on a 1D convex quartic loss with multiple learning rates
- a full logistic regression training loop: forward pass, log-loss, gradient computation, and weight updates
- convergence comparison between learned and true decision boundaries

Run it with:

```bash
jupyter notebook companion/bridge02/practical/probability_risk_lab.ipynb
```

What to notice:

- base rates matter: the prior probability significantly affects the posterior
- sigmoid is smooth and differentiable, enabling gradient-based learning
- log-loss heavily penalizes confident incorrect predictions
- learning rate choice is critical: too small converges slowly, too large diverges
- gradient descent iteratively improves the loss by moving opposite to the gradient
- logistic regression learns a decision boundary by minimizing log-loss

Prerequisites:

- understanding of probability, conditional probability, and Bayes' rule
- familiarity with derivatives and gradients
- basic knowledge of optimization and iterative algorithms
