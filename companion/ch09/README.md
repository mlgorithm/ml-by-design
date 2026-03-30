# Chapter 9 Companion

This chapter supports the move from token sequences to continuous signals and temporal processes.

It focuses on three ideas:

- time-frequency representations for audio
- lag features and forecasting baselines
- why chronological evaluation matters for sequential data

## Minimal example

`minimal/spectrogram_window_demo.py`

What it shows:

- a synthetic waveform with a low tone followed by a higher tone
- short-window Fourier analysis over time
- dominant frequency estimates for successive windows

Run it with:

```bash
python3 companion/ch09/minimal/spectrogram_window_demo.py
```

What to notice:

- early windows detect the low-frequency tone
- later windows detect the higher-frequency tone
- the representation captures not only which frequencies exist, but when they occur

Prerequisites:

- basic sine waves
- the idea of frequency
- local time windows

## Practical example

`practical/forecast_split_leakage_demo.py`

What it shows:

- a synthetic forecasting problem with trend, seasonality, and a regime shift
- a naive persistence baseline
- the same linear forecasting model under random-split and chronological evaluation

Run it with:

```bash
python3 companion/ch09/practical/forecast_split_leakage_demo.py
```

What to notice:

- the random split makes the forecasting model look much stronger than it really is
- the chronological split is harder because it respects temporal deployment order
- a naive baseline can outperform a more complex model under honest evaluation

Prerequisites:

- train/test splitting
- lag features
- regression and root mean squared error
