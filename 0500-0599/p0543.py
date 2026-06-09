"""Project Euler Problem 543: Prime-Sum Numbers.

P(n, k) = 1 if n is a sum of k primes (repetitions allowed), else 0.
S(n) = sum of P(i, k) over 1 <= i, k <= n.  Find sum of S(F(k)) for
3 <= k <= 44, Fibonacci F(44) = 701408733.

Classify by k:
  k = 1: i works iff i is prime, contributing pi(n).
  k = 2: every even i >= 4 works (Goldbach, computationally verified far
         beyond 7*10^8); an odd i is a sum of two primes only as 2 + (i-2),
         so odd i works iff i - 2 is prime.  Count: floor(n/2) - 1 plus the
         number of odd primes <= n - 2, i.e. pi(n-2) - 1.
  k >= 3: i works iff i >= 2k.  Even i = 2(k-2) + m with even m >= 4 reduces
         to Goldbach; odd i >= 2k + 1 gives i = 2(k-3) + m with odd m >= 7,
         a sum of three primes by the weak Goldbach theorem (Helfgott).
         Each k contributes n - 2k + 1, a closed-form quadratic in total.

Hand checks: S(10) = 20, S(100) = 2402; S(1000) = 248838 is asserted.  The
only real work is pi at the 84 thresholds F(k) and F(k) - 2, found in one
pass of a segmented sieve up to F(44).
"""

import numpy as np
import numba


@numba.jit(cache=True)
def _pi_at(thresholds: np.ndarray) -> np.ndarray:
    """Prime counts pi(t) for an ascending array of thresholds, one sieve pass."""
    limit = int(thresholds[-1])
    root = int(np.sqrt(limit)) + 1
    base = np.ones(root + 1, dtype=np.bool_)
    base[:2] = False
    for i in range(2, int(np.sqrt(root)) + 1):
        if base[i]:
            base[i * i :: i] = False
    base_primes = np.flatnonzero(base)

    counts = np.zeros(len(thresholds), dtype=np.int64)
    seg_size = 1 << 22
    count = 0
    t_idx = 0
    lo = 0
    while lo <= limit and t_idx < len(thresholds):
        hi = min(lo + seg_size, limit + 1)
        seg = np.ones(hi - lo, dtype=np.bool_)
        if lo == 0:
            seg[:2] = False
        for p in base_primes:
            start = max(p * p, ((lo + p - 1) // p) * p)
            if start >= hi:
                continue
            seg[start - lo :: p] = False
        # Record pi at thresholds inside [lo, hi).
        running = lo
        for j in range(len(seg)):
            if seg[j]:
                count += 1
            while t_idx < len(thresholds) and thresholds[t_idx] == running:
                counts[t_idx] = count
                t_idx += 1
            running += 1
            if t_idx >= len(thresholds):
                break
        lo = hi
    while t_idx < len(thresholds):  # thresholds equal to the limit itself
        counts[t_idx] = count
        t_idx += 1
    return counts


def S(n: int, pi_n: int, pi_n2: int) -> int:
    """S(n) given pi(n) and pi(n-2)."""
    total = pi_n  # k = 1
    total += max(0, n // 2 - 1)  # k = 2, even i >= 4
    if n >= 5:
        total += pi_n2 - 1  # k = 2, odd i = 2 + odd prime
    big_k = n // 2  # k = 3..floor(n/2), each contributing n - 2k + 1
    c = big_k - 2
    if c > 0:
        total += c * (n + 1) - big_k * (big_k + 1) + 6
    return total


def solve() -> int:
    fib = [0, 1]
    for _ in range(2, 45):
        fib.append(fib[-1] + fib[-2])

    ns = [fib[k] for k in range(3, 45)]
    thresholds = sorted({t for n in ns for t in (max(n - 2, 0), n)} | {1000, 998})
    counts = _pi_at(np.array(thresholds, dtype=np.int64))
    pi = dict(zip(thresholds, (int(c) for c in counts)))

    assert S(10, pi_at_small(10), pi_at_small(8)) == 20
    assert S(100, pi_at_small(100), pi_at_small(98)) == 2402
    assert S(1000, pi[1000], pi[998]) == 248838

    return sum(S(n, pi[n], pi[max(n - 2, 0)]) for n in ns)


def pi_at_small(n: int) -> int:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return int(sieve.sum())


if __name__ == "__main__":
    print(solve())  # 199007746081234640
