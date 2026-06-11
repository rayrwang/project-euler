"""Project Euler 495: Writing n as the Product of k Distinct Positive Integers.

Find W(10000!, 30) mod 1000000007, where W(n, k) counts unordered ways to
write n as a product of k distinct positive integers.

Only the multiset of prime exponents of n matters. Counting ordered k-tuples
with all entries distinct via the partition-lattice inclusion-exclusion
(prod_{i<j} [x_i != x_j] expands over set partitions P with Moebius weight
prod_blocks (-1)^{|B|-1} (|B|-1)!), then dividing by k!, gives

    W(n, k) = sum over partitions lambda of k of
              prod_i ((-1)^(lambda_i - 1) / lambda_i)
              * (1 / prod_j m_j!)            (m_j = part multiplicities)
              * prod_p c_lambda(e_p),

where c_lambda(e) is the denumerant: the number of solutions of
sum lambda_i x_i = e in nonnegative integers, i.e. the ways to spread prime
exponent e over the blocks. Each c_lambda is a coin-change DP up to the
largest exponent (e_2 = 9995 for 10000!), and there are p(30) = 5604
partitions - about 1.7 * 10^9 DP cells in numba. The formula is verified
against brute force for several small n and against the given
W(100!, 10) mod 1e9+7 = 287549200.
"""

import numpy as np
from numba import njit

MOD = 1000000007


def partitions(k, mx=None):
    if mx is None:
        mx = k
    if k == 0:
        yield []
        return
    for p in range(min(k, mx), 0, -1):
        for rest in partitions(k - p, p):
            yield [p] + rest


def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return np.flatnonzero(sieve)


def legendre(n, p):
    e, q = 0, p
    while q <= n:
        e += n // q
        q *= p
    return e


@njit(cache=True)
def solve(parts_flat, part_len, coefs, exp_vals, exp_cnts, emax):
    ways = np.empty(emax + 1, np.int64)
    total = np.int64(0)
    pos = 0
    for li in range(len(part_len)):
        ways[0] = 1
        for v in range(1, emax + 1):
            ways[v] = 0
        for j in range(part_len[li]):
            lam = parts_flat[pos + j]
            for v in range(lam, emax + 1):
                ways[v] = (ways[v] + ways[v - lam]) % MOD
        pos += part_len[li]
        nval = np.int64(1)
        for t in range(len(exp_vals)):
            base = ways[exp_vals[t]]
            e = exp_cnts[t]
            while e:
                if e & 1:
                    nval = nval * base % MOD
                base = base * base % MOD
                e >>= 1
        total = (total + coefs[li] * nval) % MOD
    return total


def big_w(n_fact, k):
    exps = [legendre(n_fact, int(p)) for p in primes_upto(n_fact)]
    return w_exps(exps, k)


def w_exps(exps, k):
    """W for arbitrary exponent multiset (used for the W(144,4) check)."""
    vals, cnts = np.unique(np.array(exps, dtype=np.int64), return_counts=True)
    plist = list(partitions(k))
    parts_flat = np.array([x for lam in plist for x in lam], dtype=np.int64)
    part_len = np.array([len(lam) for lam in plist], dtype=np.int64)
    coefs = np.empty(len(plist), dtype=np.int64)
    for i, lam in enumerate(plist):
        c = 1
        for part in lam:
            c = c * pow(part, MOD - 2, MOD) % MOD
            if part % 2 == 0:
                c = MOD - c
        mult = 1
        prev = None
        for part in lam:
            if part == prev:
                mult += 1
            else:
                mult = 1
            prev = part
            c = c * pow(mult, MOD - 2, MOD) % MOD
        coefs[i] = c
    return int(solve(parts_flat, part_len, coefs, vals, cnts.astype(np.int64), int(vals.max())))


if __name__ == "__main__":
    assert w_exps([4, 2], 4) == 7  # 144 = 2^4 * 3^2
    assert big_w(100, 10) == 287549200
    print(big_w(10000, 30))  # 789107601
