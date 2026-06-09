import numpy as np


def _multiple_sum(d: int, lo: int, hi: int) -> int:
    # Sum of the multiples of d in [lo, hi].
    a = (lo + d - 1) // d
    b = hi // d
    if b < a:
        return 0
    return d * (a + b) * (b - a + 1) // 2


def solve(limit: int = 999_966_663_333) -> int:
    # For p^2 < n < q^2 with consecutive primes p, q we have lps(n) = p and
    # ups(n) = q, so n is semidivisible exactly when p or q divides n but not
    # both. Prime squares themselves have lps = ups and are never
    # semidivisible (matching the example sum 34825 up to 1000). Per interval,
    # add the multiples of p and of q and remove the multiples of pq twice.
    pmax = int(limit**0.5) + 100
    sieve = np.ones(pmax + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(pmax**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = np.nonzero(sieve)[0].tolist()

    total = 0
    for p, q in zip(primes, primes[1:]):
        lo = p * p + 1
        if lo > limit:
            break
        hi = min(q * q - 1, limit)
        total += (
            _multiple_sum(p, lo, hi)
            + _multiple_sum(q, lo, hi)
            - 2 * _multiple_sum(p * q, lo, hi)
        )
    return total


if __name__ == "__main__":
    print(solve())  # 1259187438574927161
