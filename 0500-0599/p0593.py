"""
https://projecteuler.net/problem=593

S(k) = p_k^k mod 10007 (p_k the k-th prime),
S2(k) = S(k) + S(floor(k/10000) + 1), M(i, j) the median of
S2(i)..S2(j), and F(n, k) sums the medians of all length-k windows.
Find F(10^7, 10^5), formatted with .0 or .5.

The values S2 live in 0..2*10006, so each sliding window is a counting
distribution over ~20000 buckets. A Fenwick tree over the value range
supports O(log) insert/delete as the window slides and O(log)
selection of the r-th smallest by binary lifting; for the even window
length the median is the average of the k/2-th and (k/2+1)-th order
statistics, so the code accumulates twice the median sum in integers
and formats the final halving exactly.

S(k) itself needs the first 10^7 primes (p_10^7 = 179424673) and one
modular power each, reduced via Fermat to exponent k mod 10006 (10007
is prime; the prime 10007 itself maps to 0).

The window machinery is cross-checked against direct sort-the-window
medians on a 3000-element prefix, and all four given values
M(1,10) = 2021.5, M(10^2,10^3) = 4715.0, F(100,10) = 463628.5 and
F(10^5,10^4) = 675348207.5 are asserted.
"""

import sys
from pathlib import Path

import numba
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import prime_sieve_int  # noqa: E402

MOD = 10007
SIZE = 2 * (MOD - 1) + 2  # values fit in 0..20012
LOG = 15  # 2^15 >= SIZE


@numba.njit(cache=True)
def _build_s(primes: np.ndarray, n: int) -> np.ndarray:
    s = np.empty(n + 1, dtype=np.int64)
    s[0] = 0
    for k in range(1, n + 1):
        p = primes[k - 1] % MOD
        if p == 0:
            s[k] = 0
            continue
        e = k % (MOD - 1)
        if e == 0:
            e = MOD - 1
        r = 1
        b = p
        while e:
            if e & 1:
                r = r * b % MOD
            b = b * b % MOD
            e >>= 1
        s[k] = r
    return s


@numba.njit(cache=True)
def _median_sum2(s2: np.ndarray, n: int, k: int) -> int:
    """Twice the sum of window medians of s2[1..n] with window k."""
    fen = np.zeros(SIZE + 1, dtype=np.int64)
    total = 0
    for idx in range(1, k + 1):
        i = s2[idx] + 1
        while i <= SIZE:
            fen[i] += 1
            i += i & (-i)
    r1 = k // 2
    r2 = k // 2 + 1
    if k % 2 == 1:
        r1 = r2 = (k + 1) // 2
    for start in range(1, n - k + 2):
        for rr in (r1, r2):
            pos = 0
            rem = rr
            step = 1 << LOG
            while step:
                npos = pos + step
                if npos <= SIZE and fen[npos] < rem:
                    pos = npos
                    rem -= fen[npos]
                step >>= 1
            total += pos
        if start <= n - k:
            i = s2[start] + 1
            while i <= SIZE:
                fen[i] -= 1
                i += i & (-i)
            i = s2[start + k] + 1
            while i <= SIZE:
                fen[i] += 1
                i += i & (-i)
    return total


def _fmt(total2: int) -> str:
    return f"{total2 // 2}.0" if total2 % 2 == 0 else f"{total2 // 2}.5"


def _median_sum2_brute(s2: np.ndarray, n: int, k: int) -> int:
    total = 0
    for i in range(1, n - k + 2):
        w = np.sort(s2[i : i + k])
        if k % 2 == 0:
            total += int(w[k // 2 - 1] + w[k // 2])
        else:
            total += 2 * int(w[k // 2])
    return total


if __name__ == "__main__":
    n = 10**7
    primes = prime_sieve_int(179_424_674)[:n]  # p_(10^7) = 179424673
    assert len(primes) == n and int(primes[-1]) == 179_424_673
    s = _build_s(primes, n)
    s2 = np.empty(n + 1, dtype=np.int64)
    s2[0] = 0
    ks = np.arange(1, n + 1)
    s2[1:] = s[1:] + s[ks // 10000 + 1]

    # window machinery vs direct sorting on a prefix
    for kk in (7, 10, 250):
        assert _median_sum2(s2, 3000, kk) == _median_sum2_brute(s2, 3000, kk)
    assert _median_sum2(s2, 10, 10) == 2 * 2021 + 1  # M(1,10) = 2021.5
    sub = np.concatenate((np.zeros(1, dtype=np.int64), s2[100:1001]))
    assert _median_sum2(sub, 901, 901) == 2 * 4715  # M(100,1000) = 4715.0
    assert _fmt(_median_sum2(s2, 100, 10)) == "463628.5"
    assert _fmt(_median_sum2(s2, 10**5, 10**4)) == "675348207.5"

    print(_fmt(_median_sum2(s2, 10**7, 10**5)))  # 96632320042.0
