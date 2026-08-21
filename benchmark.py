import time
import random
from scipy.fft import fft as scipy_fft
from fft import fft as my_fft

random.seed(0)
n = 4096
signal = [random.random() for _ in range(n)]

start = time.perf_counter()
my_fft(signal)
mine_time = time.perf_counter() - start

start = time.perf_counter()
scipy_fft(signal)
scipy_time = time.perf_counter() - start

print(f"My recursive FFT: {mine_time:.5f}s")
print(f"scipy.fft.fft:    {scipy_time:.5f}s")
print(f"scipy is {mine_time / scipy_time:.0f}x faster")