"""Project Euler problem 515: Dissonant Numbers.

d(p, n, 0) is the inverse of n mod p, and d(p, n, k) is the k-fold prefix
sum: d(p, n, k) = sum_{i<=n} d(p, i, k-1).  D(a, b, k) sums
d(p, p-1, k) mod p over primes a <= p < a + b.  Find D(1e9, 1e5, 1e5).

Iterating prefix sums k times gives the binomial-weighted sum

  d(p, p-1, k) = sum_{i=1}^{p-1} C(p-2-i+k, k-1) * i^{-1}  (mod p).

For i <= k - 2 the top index is p + (k-2-i) with 0 <= k-2-i < k-1, so by
Lucas the binomial is C(k-2-i, k-1) = 0.  For i >= k - 1 the top index is
p - s with s = i - k + 2 in [1, p-1], and

  C(p - s, k-1) = (-1)^(k-1) C(s+k-2, k-1) = (-1)^(k-1) C(i, k-1) (mod p).

Since C(i, k-1)/i = C(i-1, k-2)/(k-1), the hockey-stick identity collapses
the sum:

  d(p, p-1, k) = (-1)^(k-1)/(k-1) * C(p-1, k-1) = 1/(k-1)  (mod p),

using C(p-1, k-1) = (-1)^(k-1) mod p.  So the answer is simply the sum of
the inverses of k - 1 = 99999 modulo each prime in the window, found with
a segmented sieve.  The closed form is verified below against the direct
recurrence for small p and k, and D itself against a brute-force D(10, 30, 5).
"""

import sys
from pathlib import Path

import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import prime_sieve_int  # noqa: E402


def d_brute(p: int, k: int) -> int:
    """d(p, p-1, k) straight from the definition."""
    row = [0] + [pow(n, -1, p) for n in range(1, p)]
    for _ in range(k):
        for n in range(2, p):
            row[n] = (row[n] + row[n - 1]) % p
    return row[p - 1]


def primes_in_window(a: int, b: int) -> list[int]:
    """Primes p with a <= p < a + b, via segmented sieve."""
    small = prime_sieve_int(int((a + b) ** 0.5) + 1)
    seg = np.ones(b, np.bool_)
    for q in small:
        q = int(q)
        start = (-a) % q
        if a + start == q:
            start += q
        seg[start::q] = False
    return [a + int(i) for i in np.nonzero(seg)[0]]


def big_d(a: int, b: int, k: int) -> int:
    return sum(pow(k - 1, -1, p) for p in primes_in_window(a, b))


def main() -> None:
    for p in (7, 11, 13, 101):
        for k in (2, 3, 5, 10, 17):
            assert d_brute(p, k) == pow(k - 1, -1, p)
    assert big_d(10, 30, 5) == sum(
        d_brute(p, 5) for p in (11, 13, 17, 19, 23, 29, 31, 37)
    )
    print(big_d(10**9, 10**5, 10**5))  # 2422639000800


if __name__ == "__main__":
    main()
