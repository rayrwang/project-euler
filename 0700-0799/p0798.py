"""
Project Euler Problem 798: Card Stacking Game
https://projecteuler.net/problem=798

A deck has s suits of cards 1..n.  Some subset of the deck starts face-up;
a move places a still-unused card on a visible card of the same suit and
larger value, covering it.  The player unable to move loses.  C(n, s)
counts the initial subsets that are first-player losses; find
C(10^7, 10^7) mod 10^9 + 7.

Moves never interact across suits, so the game is the disjunctive sum of
the s single-suit games and a position is a first-player loss exactly when
the XOR of the per-suit Grundy values is 0.  Within one suit a state says,
for every value, whether the card is visible, still available, or covered;
a brute-force memoisation over these 3^n states for n <= 12 yields the
Grundy value of every initial subset (available = complement of visible),
and the distribution cnt_n[g] of Grundy values over the 2^n subsets shows
exact patterns:

    cnt_n[0]      = 2^(n-2) + 2,
    cnt_n[2k]     = cnt_(n-1)[2k - 1],
    cnt_n[2k + 1] = cnt_(n-1)[2k + 1] + cnt_(n-2)[2k - 1],
    cnt_n[1]      = 2^(n-2) + n - 2.

Unrolling the third recurrence makes cnt_n[2k - 1] a (k-1)-fold shifted
prefix sum of cnt[1], i.e. a convolution of 2^m + m with a binomial, and
the geometric part telescopes by the negative-binomial tail identity
sum_{r > R} C(r, t) 2^(-r) = 2^(-R) sum_{u <= t} C(R + 1, u) into

    cnt_n[2k - 1] = 2^(n-k-1) - sum_{u=0}^{k-2} C(n-k-1, u) + C(n-k-1, k),

with the even case the same formula at n - 1.  These match the brute
force for all n <= 12 and are evaluated for all g in O(n): stepping
k -> k+1 sends the partial binomial sum B(M, t) = sum_{u<=t} C(M, u) to
B(M-1, t+1) via B(M-1, t) = (B(M, t) + C(M-1, t)) / 2 and one more term.

The answer is then the XOR-power: with W the length-2^24 Walsh-Hadamard
transform of cnt (Grundy values are below n < 2^24),

    C(n, s) = 2^(-24) * sum_w W_w^s  (mod p),

a transform, 2^24 modular powers, and a sum.  The given C(3, 2) = 26 and
C(13, 4) = 540318329 mod p reproduce through the same pipeline.
"""

import numpy as np
from numba import njit, prange

N = 10**7
S = 10**7
P = 10**9 + 7


@njit(cache=True)
def power(b, e, p):
    r = 1
    b %= p
    while e:
        if e & 1:
            r = r * b % p
        b = b * b % p
        e >>= 1
    return r


@njit(cache=True)
def grundy_counts(n, size):
    """cnt[g] = number of subsets of a suit of n cards with Grundy g."""
    fact = np.empty(n + 1, dtype=np.int64)
    inv_fact = np.empty(n + 1, dtype=np.int64)
    fact[0] = 1
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % P
    inv_fact[n] = power(fact[n], P - 2, P)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % P

    def binom(m, u):
        if u < 0 or u > m or m < 0:
            return 0
        return fact[m] * inv_fact[u] % P * inv_fact[m - u] % P

    inv2 = (P + 1) // 2
    cnt = np.zeros(size, dtype=np.int64)
    cnt[0] = (power(2, n - 2, P) + 2) % P
    for parity in range(2):  # odd entries use n, even entries use n - 1
        nn = n - parity
        bsum = 0  # B(nn - k - 1, k - 2), starts at k = 1 with t = -1
        k = 1
        while 2 * k - 1 + parity <= n - 1:
            m = nn - k - 1
            val = (power(2, nn - k - 1, P) - bsum + binom(m, k)) % P
            cnt[2 * k - 1 + parity] = val
            # advance B(m, k - 2) -> B(m - 1, k - 1)
            bsum = (bsum + binom(m - 1, k - 2)) * inv2 % P
            bsum = (bsum + binom(m - 1, k - 1)) % P
            k += 1
    return cnt


@njit(cache=True, parallel=True)
def wht_mod(vec):
    """In-place Walsh-Hadamard transform mod P."""
    size = vec.shape[0]
    h = 1
    while h < size:
        step = h * 2
        nblocks = size // step
        for blk in prange(nblocks):  # ty: ignore[not-iterable]
            i = blk * step
            for j in range(i, i + h):
                a = vec[j]
                b = vec[j + h]
                vec[j] = (a + b) % P
                vec[j + h] = (a - b) % P
        h = step


@njit(cache=True, parallel=True)
def power_sum(vec, s):
    total = 0
    for i in prange(vec.shape[0]):  # ty: ignore[not-iterable]
        total += power(vec[i] % P, s, P)
    return total % P


def solve(n, s):
    size = 1
    while size < n:
        size *= 2
    cnt = grundy_counts(n, size)
    wht_mod(cnt)
    total = power_sum(cnt, s)
    return int(total * power(size, P - 2, P) % P)


def main():
    assert solve(3, 2) == 26
    assert solve(13, 4) == 540318329
    return solve(N, S)


if __name__ == "__main__":
    print(main())  # 132996198
