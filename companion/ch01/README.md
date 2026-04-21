# Chapter 1 Companion: Framing Learning Problems (`ch01`)

This chapter introduces the seven-question framework for turning vague requests into defensible learning problems. The companion code demonstrates how framing decisions translate into concrete implementation choices.

The code here supports that goal in two layers, both using the spam filtering case study from the chapter.

## Minimal example: `minimal/split_and_keyword_baseline.py`

**Chapter 1 concepts plus next-step implementation checks:**
- **Question 3 (Evidence)**: What message text is available at arrival time?
- **Question 4 (Representation)**: What encoding or features will the model actually see from that text?
- **Question 6 (Evidence)**: How do we protect held-out evidence for trustworthy evaluation?
- **Bridge to later chapters**: What simple rule or linear model is the first serious comparison?

The user/action and proxy-target framing questions are handled in the printed chapter; the code focuses on the implementation layer after that framing has been chosen.

**What it shows:**

- loading a tiny local dataset
- train, validation, and test splitting
- a majority-class baseline
- a simple keyword-based spam detector
- the difference between prediction quality on train, validation, and test data

Run it with:

```bash
python3 companion/ch01/minimal/split_and_keyword_baseline.py
```

## Practical example

`practical/spam_baseline_sklearn.py`

What it shows:

- turning text into features with `CountVectorizer`
- fitting a logistic regression baseline with `scikit-learn`
- comparing train, validation, and test accuracy

Run it with:

```bash
python3 companion/ch01/practical/spam_baseline_sklearn.py
```

## Teaching note

The printed chapter should explain the workflow and the meaning of the split. The code here exists to make that workflow concrete without forcing the book text to depend on any one library forever.
