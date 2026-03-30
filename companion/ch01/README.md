# Chapter 1 Companion: Problem Framing in Practice

This chapter introduces the seven-question framework for turning vague requests into defensible learning problems. The companion code demonstrates how framing decisions translate into concrete implementation choices.

The code here supports that goal in two layers, both using the spam filtering case study from the chapter.

## Minimal example: `minimal/split_and_keyword_baseline.py`

**Core Chapter Concepts Demonstrated:**
- **Question 1 (User/Action)**: Who acts on spam predictions and how?
- **Question 2 (Proxy Target)**: What makes a message \"spam\" in practice?
- **Question 4 (Available Inputs)**: What features were available at message arrival time?
- **Question 6 (Evidence)**: How do we protect held-out evidence for trustworthy evaluation?

**What it shows:**

- loading a tiny local dataset
- train, validation, and test splitting
- a majority-class baseline
- a simple keyword-based spam detector
- the difference between prediction quality on train, validation, and test data

Run it with:

```bash
python3 book/companion/ch01/minimal/split_and_keyword_baseline.py
```

## Practical example

`practical/spam_baseline_sklearn.py`

What it shows:

- turning text into features with `CountVectorizer`
- fitting a logistic regression baseline with `scikit-learn`
- comparing train, validation, and test accuracy

Run it with:

```bash
python3 book/companion/ch01/practical/spam_baseline_sklearn.py
```

## Teaching note

The printed chapter should explain the workflow and the meaning of the split. The code here exists to make that workflow concrete without forcing the book text to depend on any one library forever.
