# Chapter 16 Companion: Tabular Data: The Modality You Will Actually Meet (`ch09b`)

This chapter supports tabular pipeline discipline.

It focuses on three ideas:

- gradient-boosted trees as the default tabular baseline
- target encoding, temporal splits, and group-aware leakage control
- calibration, schema drift, and missingness monitoring

## Suggested lab shape

Use a small tabular classification dataset with categorical columns, repeated entities, or timestamps.

What it should show:

- why a random split can overstate deployment performance
- how out-of-fold target encoding differs from naive target encoding
- why calibration and operating-threshold metrics matter after model fitting

Prerequisites:

- train/validation/test splitting
- tree-based baselines
- basic calibration vocabulary
