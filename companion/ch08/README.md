# Chapter 8 Companion

This chapter supports the move from visual structure to linguistic context and generation.

It focuses on three ideas:

- why bag-of-words can lose crucial meaning
- how n-grams restore local order information
- why sequence models are useful when order and context matter

## Minimal example

`minimal/order_and_ngrams_demo.py`

What it shows:

- two sentences with identical unigram counts but different meanings
- manual unigram and bigram count dictionaries
- how bigrams preserve local order that bag-of-words discards

Run it with:

```bash
python3 companion/ch08/minimal/order_and_ngrams_demo.py
```

What to notice:

- the unigram representations are identical
- the bigram representations are different
- representation failure can come from what is thrown away, not only from model weakness

Prerequisites:

- tokenization into words
- the idea of count vectors
- local word order

## Practical example

`practical/order_sensitive_text_demo.py`

What it shows:

- a unigram logistic-regression baseline on an order-sensitive text task
- a unigram-plus-bigram logistic-regression model selected against the unigram baseline on validation data
- a small GRU sequence classifier

Install shared dependencies first:

```bash
python3 -m pip install -r companion/requirements.txt
```

Run it with:

```bash
python3 companion/ch08/practical/order_sensitive_text_demo.py
```

What to notice:

- the unigram baseline fails because it ignores order
- the bigram baseline succeeds because the needed context is local
- the GRU also succeeds because it preserves sequence structure

Prerequisites:

- train, validation, and test splits
- logistic regression
- the concept of an embedding layer and sequence model
