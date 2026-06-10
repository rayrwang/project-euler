from math import isqrt, log

import numpy as np

# p is squarefree (42 primes below 190), so PSR(p) is the largest subset
# product not exceeding sqrt(p) - a knapsack on the logarithms. Meet in the
# middle: the primes split into two halves of 21; all 2^21 subset log-sums
# of each half are built by doubling. With the right half sorted, each left
# sum a pairs with the largest right sum <= log(sqrt p) - a via binary
# search. Floating point cannot certify the winner among near-ties, so every
# pairing within 10^-6 of the float optimum (including the neighbour just
# above the searched boundary) is re-checked exactly with big integers
# (d^2 <= p), and the exact maximum d is reduced mod 10^16. Verified against
# direct subset enumeration for the primes below 30, 50 and 70.


def _subset_logs(primes: list[int]) -> tuple[np.ndarray, np.ndarray]:
    sums = np.zeros(1, dtype=np.float64)
    masks = np.zeros(1, dtype=np.int64)
    for i, p in enumerate(primes):
        sums = np.concatenate([sums, sums + log(p)])
        masks = np.concatenate([masks, masks | (1 << i)])
    return sums, masks


def _product(primes: list[int], mask: int) -> int:
    out = 1
    for i, p in enumerate(primes):
        if (mask >> i) & 1:
            out *= p
    return out


def solve(bound: int = 190, mod: int = 10**16) -> int:
    sieve = np.ones(bound, dtype=bool)
    sieve[:2] = False
    for i in range(2, isqrt(bound) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = [int(x) for x in np.nonzero(sieve)[0]]

    big_p = 1
    for p in primes:
        big_p *= p
    root = isqrt(big_p)

    half = len(primes) // 2
    left, right = primes[:half], primes[half:]
    a_sums, a_masks = _subset_logs(left)
    b_sums, b_masks = _subset_logs(right)
    order = np.argsort(b_sums)
    b_sums, b_masks = b_sums[order], b_masks[order]

    target = sum(log(p) for p in primes) / 2
    idx = np.searchsorted(b_sums, target - a_sums, side="right") - 1
    valid = idx >= 0
    totals = np.where(valid, a_sums + b_sums[np.maximum(idx, 0)], -np.inf)
    best_float = totals.max()

    candidates = np.nonzero(totals > best_float - 1e-6)[0]
    best = 0
    for i in candidates:
        for j in (int(idx[i]), int(idx[i]) + 1):
            if j < 0 or j >= len(b_sums):
                continue
            d = _product(left, int(a_masks[i])) * _product(right, int(b_masks[j]))
            if d <= root and d > best:
                best = d
    return best % mod


if __name__ == "__main__":
    print(solve())  # 1096883702440585
