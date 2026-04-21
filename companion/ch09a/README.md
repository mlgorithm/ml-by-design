# Chapter 15 Companion: Ranking, Recommendation, and Exposure (`ch09a`)

This chapter supports the move from prediction to ranked exposure.

It focuses on three ideas:

- ranking metrics that care about position
- implicit feedback as ambiguous evidence
- exposure bias and feedback loops

## Minimal example

`minimal/ndcg_exposure_demo.py`

What it shows:

- DCG and NDCG by hand
- why the same relevant items score differently in different orders
- how top-of-list exposure concentrates attention

Run it with:

```bash
python3 companion/ch09a/minimal/ndcg_exposure_demo.py
```

What to notice:

- moving a highly relevant item down the list reduces NDCG
- exposure is a policy choice, not just a metric detail
- items that are never exposed cannot produce ordinary click feedback

Prerequisites:

- logarithms
- ranked lists
- basic relevance labels

## Practical example

`practical/matrix_factorization_demo.py`

What it shows:

- synthetic implicit-feedback data from latent user and item factors
- matrix factorization trained with stochastic gradient descent
- comparison with a popularity baseline
- NDCG@5 on held-out observed interactions

Run it with:

```bash
python3 companion/ch09a/practical/matrix_factorization_demo.py
```

What to notice:

- factorization can recover structure from sparse observations
- the popularity baseline is strong but suppresses personalized long-tail items
- evaluation only sees held-out exposed or observed interactions, so the claim must stay bounded

Prerequisites:

- dot products
- stochastic gradient descent
- train/test splits
