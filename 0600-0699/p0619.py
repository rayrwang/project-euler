"""Project Euler Problem 619: Square Subsets.

Map each n in {a, ..., b} to the vector of its prime exponents mod 2 (its
squarefree kernel) over GF(2).  A subset has square product exactly when its
vectors XOR to zero, so with N = b - a + 1 elements and r the rank of the
vectors, the kernel of the GF(2) map has dimension N - r and

    C(a, b) = 2^(N - r) - 1.

For the rank, factor every element with a smallest-prime-factor sieve.
Primes greater than sqrt(b) can only appear to the first power, and each
element contains at most one of them, so eliminate those first: the first
element seen with large prime p becomes the pivot for p (rank + 1), and any
later element with the same p is XORed against the pivot, leaving a vector
over only the 186 primes up to sqrt(1234567) = 1111.  Those small vectors
fit in one integer bitmask each and go into an ordinary binary linear basis.

Checks: C(5, 10) = 3, C(40, 55) = 15, C(1000, 1234) = 975523611 mod 10^9+7.
"""

import numpy as np

MOD = 10**9 + 7


def spf_sieve(n: int) -> np.ndarray:
    """Smallest prime factor for every integer up to n."""
    spf = np.zeros(n + 1, dtype=np.int32)
    spf[1] = 1
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf


def C(a: int, b: int, spf: np.ndarray) -> int:
    sqrt_b = int(b**0.5)
    small = [p for p in range(2, sqrt_b + 1) if spf[p] == p]
    index = {p: i for i, p in enumerate(small)}

    basis: dict[int, int] = {}  # highest set bit -> small-prime vector
    large_pivot: dict[int, int] = {}  # large prime -> small-prime vector
    rank = 0
    for n in range(a, b + 1):
        mask, m = 0, n
        while m > 1 and spf[m] < m:
            p, e = int(spf[m]), 0
            while m % p == 0:
                m //= p
                e += 1
            if e % 2:
                mask ^= 1 << index[p]
        if m > 1:  # one remaining prime factor, to the first power
            if m <= sqrt_b:
                mask ^= 1 << index[m]
            elif m in large_pivot:
                mask ^= large_pivot[m]
            else:
                large_pivot[m] = mask
                rank += 1
                continue
        while mask:
            high = mask.bit_length() - 1
            if high not in basis:
                basis[high] = mask
                rank += 1
                break
            mask ^= basis[high]
    return (pow(2, b - a + 1 - rank, MOD) - 1) % MOD


if __name__ == "__main__":
    spf = spf_sieve(1234567)
    assert C(5, 10, spf) == 3
    assert C(40, 55, spf) == 15
    assert C(1000, 1234, spf) == 975523611
    print(C(1000000, 1234567, spf))  # 857810883
