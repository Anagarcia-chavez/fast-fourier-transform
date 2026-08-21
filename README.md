# FFT From Scratch

Learning project: implement Cooley-Tukey FFT by hand, verify against a naive DFT, then benchmark against scipy's production implementation.

## Files
- `dft.py` - naive O(n^2) DFT baseline
- `fft.py` - recursive Cooley-Tukey FFT, O(n log n)
- `test_correctness.py` - verifies fft.py matches dft.py
- `benchmark.py` - compares hand-rolled FFT to scipy.fft.fft

## Usage
```
pip install -r requirements.txt
python3 test_correctness.py
python3 benchmark.py
```