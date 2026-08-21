import cmath

def _fft_core(x, sign):
    """Shared recursive butterfly logic. sign=-1 is forward FFT, sign=+1 is inverse."""
    n = len(x)

    if n == 1:
        return x

    if n % 2 != 0:
        raise ValueError("Input length must be a power of 2")

    even = _fft_core(x[0::2], sign)
    odd = _fft_core(x[1::2], sign)

    combined = [0] * n
    for k in range(n // 2):
        twiddle = cmath.exp(sign * 2j * cmath.pi * k / n) * odd[k]
        combined[k] = even[k] + twiddle
        combined[k + n // 2] = even[k] - twiddle

    return combined


def fft(x):
    """Forward FFT: time domain -> frequency domain."""
    return _fft_core(x, sign=-1)


def ifft(X):
    """Inverse FFT: frequency domain -> time domain."""
    n = len(X)
    result = _fft_core(X, sign=+1)
    return [val / n for val in result]


if __name__ == "__main__":
    signal = [0, 1, 2, 3]
    freqs = fft(signal)
    recovered = ifft(freqs)
    print("Original: ", signal)
    print("Frequencies:", freqs)
    print("Recovered:", recovered)