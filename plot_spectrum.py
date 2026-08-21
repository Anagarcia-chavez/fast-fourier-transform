import math
import random
import matplotlib.pyplot as plt
from inv_fft import fft

# TEST SIGNAL - 5HZ SINE WAVE (64 SAMPLES PER SECOND W/ NOISE)
sample_rate = 64      # samples per second
duration = 1           # seconds
n = sample_rate * duration
frequency = 5           # Hz

random.seed(0)
t = [i / sample_rate for i in range(n)]
signal = [
    math.sin(2 * math.pi * frequency * time) + random.uniform(-0.5, 0.5)  # noise
    for time in t
]

# RUN FFT
spectrum = fft(signal)

# CONVERT OUTPUT TO MAGNITUDE
# abs() of a complex number gives its magnitude (strength of frequency)
magnitudes = [abs(val) for val in spectrum]

# MAP FFT TO HZ
freqs = [k * sample_rate / n for k in range(n // 2)]
half_magnitudes = magnitudes[: n // 2]

# PLOT
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

ax1.plot(t, signal)
ax1.set_title("Time domain: noisy signal")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")

ax2.stem(freqs, half_magnitudes)
ax2.set_title("Frequency domain: FFT magnitude spectrum")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")

plt.tight_layout()
plt.savefig("spectrum.png")
print("Saved plot to spectrum.png")

peak_index = half_magnitudes.index(max(half_magnitudes))
print(f"Peak detected at {freqs[peak_index]} Hz (true frequency was {frequency} Hz)")