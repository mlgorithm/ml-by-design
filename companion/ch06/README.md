# Chapter 9 Companion: Representation Learning and Foundation Models (`ch06`)

This chapter supports the move from task-specific neural networks to reusable representations.

It focuses on three ideas:

- embeddings as geometry
- self-supervised learning from structure already present in data
- transfer learning through frozen encoders and linear probes

## Minimal example

`minimal/cooccurrence_embeddings.py`

What it shows:

- a tiny corpus turned into a word co-occurrence matrix
- a positive pointwise mutual information transformation
- a low-dimensional embedding from singular value decomposition
- nearest-neighbor queries in embedding space
- a direct cosine-vs-Euclidean comparison for one query word

Run it with:

```bash
python3 companion/ch06/minimal/cooccurrence_embeddings.py
```

What to notice:

- words that appear in similar contexts move closer together
- the geometry comes from context statistics, not from hand-coded meanings
- nearest neighbors are useful but still depend on the training corpus
- the notion of "close" changes when you change the metric

Prerequisites:

- matrices and vectors
- cosine similarity
- the idea of context windows in text

## Practical example

`practical/contrastive_transfer_demo.py`

What it shows:

- a self-supervised contrastive encoder trained on unlabeled paired views
- a frozen linear probe trained on only a small labeled subset
- frozen, partial, and full downstream adaptation on a shifted target domain
- a comparison against a raw-feature logistic-regression baseline

Run it with:

```bash
python3 companion/ch06/practical/contrastive_transfer_demo.py
```

What to notice:

- the raw-feature baseline struggles when nuisance variation is strong and labels are scarce
- the contrastive encoder learns a representation that supports a much stronger frozen linear probe
- representation learning can help by removing nuisance factors before the downstream classifier sees the data
- adaptation choice is a real engineering decision: frozen, partial, and full tuning can behave differently under the same label budget

Prerequisites:

- logistic regression
- train and test splits
- basic understanding of cosine similarity or dot-product similarity
- frozen vs fine-tuned transfer
