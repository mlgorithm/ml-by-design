import numpy as np


def main():
    sample_rate = 64
    time = np.arange(0, 2, 1 / sample_rate)

    waveform = np.zeros_like(time)
    waveform[:sample_rate] = np.sin(2 * np.pi * 4 * time[:sample_rate])
    waveform[sample_rate:] = np.sin(2 * np.pi * 10 * time[sample_rate:])

    window_size = 32
    hop_size = 16

    print("Dominant frequency by analysis window")
    for start in range(0, len(waveform) - window_size + 1, hop_size):
        frame = waveform[start : start + window_size]
        spectrum = np.abs(np.fft.rfft(frame))
        frequencies = np.fft.rfftfreq(window_size, d=1 / sample_rate)
        dominant_frequency = frequencies[np.argmax(spectrum)]
        start_seconds = start / sample_rate
        end_seconds = (start + window_size) / sample_rate
        print(
            f"  window={start_seconds:.2f}s to {end_seconds:.2f}s "
            f"dominant_frequency={dominant_frequency:.1f} Hz"
        )


if __name__ == "__main__":
    main()
