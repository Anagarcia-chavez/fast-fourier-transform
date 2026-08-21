import cmath

def dft(x):
    """Naive O(n^2) Discrete Fourier Transform."""
    n = len(x)
    X = []
    for k in range(n):
        total = 0
        for t in range(n):
            angle = -2j * cmath.pi * k * t / n
            total += x[t] * cmath.exp(angle)
        X.append(total)
    return X


if __name__ == "__main__":
    signal = [0, 1, 2, 3]
    print(dft(signal))