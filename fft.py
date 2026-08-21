import cmath

def fft(x):
    """Recursive Cooley-Tukey FFT. Length of x must be a power of 2."""
    n = len(x)

    if n == 1:
        return x

    if n % 2 != 0:
        raise ValueError("Input length must be a power of 2")

    even = fft(x[0::2])
    odd = fft(x[1::2])

    combined = [0] * n
    for k in range(n // 2):
        twiddle = cmath.exp(-2j * cmath.pi * k / n) * odd[k]
        combined[k] = even[k] + twiddle
        combined[k + n // 2] = even[k] - twiddle

    return combined


if __name__ == "__main__":
    signal = [0, 1, 2, 3]
    print(fft(signal))