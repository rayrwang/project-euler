import math
from decimal import Decimal, getcontext

import numpy as np

from funcs import prime_sieve_int


def count_hybrid(base: int, exp: int) -> int:
    """Number of hybrid-integers p^q q^p (primes p != q) that are <= base^exp.

    Each unordered prime pair {p, q} yields a distinct hybrid-integer (unique
    factorisation), so count ordered pairs p < q with
        q*ln(p) + p*ln(q) <= exp*ln(base).
    For fixed p the left side grows with q, so binary-search the cutoff.
    Floats fix the location to within a prime or two; a high-precision Decimal
    comparison then nails the boundary (e.g. 2^5 5^2 = 800 sits exactly on it).
    """
    getcontext().prec = 60
    target = Decimal(exp) * Decimal(base).ln()
    bound_log = exp * math.log(base)
    # For p = 2 the largest q satisfies q*ln2 < bound_log; pad for safety.
    bound = int(bound_log / math.log(2)) + 1000
    primes = prime_sieve_int(bound)
    logs = np.log(primes.astype(np.float64))
    n = len(primes)

    def exact_le(p: int, q: int) -> bool:
        return (Decimal(q) * Decimal(p).ln()
                + Decimal(p) * Decimal(q).ln()) <= target

    total = 0
    for i in range(n - 1):
        p = int(primes[i])
        lp = logs[i]
        # Largest index j with q*ln(p)+p*ln(q) <= bound_log (float estimate).
        lo, hi = i + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            f = primes[mid] * lp + p * logs[mid]
            if f <= bound_log:
                lo = mid + 1
            else:
                hi = mid - 1
        j = hi
        # Correct the float verdict at the boundary with exact arithmetic.
        while j + 1 < n and exact_le(p, int(primes[j + 1])):
            j += 1
        while j > i and not exact_le(p, int(primes[j])):
            j -= 1
        if j <= i:
            break  # no valid q for this p, hence none for any larger p
        total += j - i
    return total


if __name__ == "__main__":
    print(count_hybrid(800800, 800800))  # 1412403576
