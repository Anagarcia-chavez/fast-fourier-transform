import random
from dft import dft
from fft import fft

def close(a, b, tol=1e-9):
    return all(abs(x - y) < tol for x, y in zip(a, b))

random.seed(0)
signal = [random.random() for _ in range(16)]

result_dft = dft(signal)
result_fft = fft(signal)

assert close(result_dft, result_fft), "Mismatch between DFT and FFT!"
print("FFT matches DFT on 16-sample random signal.")