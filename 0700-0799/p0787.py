"""
Project Euler Problem 787: Bezout's Game
https://projecteuler.net/problem=787

From a pile pair (a, b), a move removes c >= 0 and d >= 0 stones with
ad - bc = +-1, and emptying a pile wins.  H(N) counts the winning ordered
coprime positions with a + b <= N; find H(10^9).

The Stern-Brocot tree.  Writing the move as (a, b) -> (a', b') with
a' = a - c, b' = b - d, the condition becomes a'b - ab' = +-1 with
0 <= a' <= a, 0 <= b' <= b.  For a, b >= 2 the solutions of each sign form
a single arithmetic family (a'_0 + ta, b'_0 + tb) with exactly one member
in the box: the two Farey parents of a/b, i.e. the Stern-Brocot
neighbours whose mediant is (a, b).  When a = 1 or b = 1 there is
additionally the move to (0, 1) or (1, 0), an immediate win.  So the game
walks up the Stern-Brocot tree and a position is losing (a P-position)
exactly when both of its Farey parents are winning.

A parity invariant.  Brute-forcing the game over a + b <= 220 (which also
reproduces H(4) = 5 and H(100) = 2043) shows the P-positions are exactly

    gcd(a, b) = 1, a + b odd, and the odd one of a, b is the larger,

which indeed propagates: the parents of such a position are an (odd, odd)
pair and a (mixed, smaller-odd) pair, both winning, and every other
position can reach a P-position or an empty pile.  (Equivalently the
bound-parity classes form a three-state automaton down the tree.)

Counting.  The number of all coprime ordered positions is the totient
summatory sum_{s=2}^{N} phi(s).  For the P-positions, the sum a + b = s
is odd, the even member is e = 2f < s/2 and gcd(e, s) = gcd(f, s) = 1, so
their number is 2 sum_{odd s <= N} #{f <= (s-1)/4 : gcd(f, s) = 1}.
Moebius inversion over the divisors d | s turns the inner count into
floor((td - 1)/(4d)) = floor(t/4) for odd t = s/d, hence

    P(N) = 2 sum_{d <= N, d odd} mu(d) G(floor(N/d)),
    G(M)  = sum_{t odd <= M} floor(t/4),

with G in closed form from two triangular numbers.  Both sums run over
the O(sqrt N) blocks of floor(N/d) using the Mertens function, computed
by the standard O(N^(2/3)) sieve-plus-recursion; the odd-restricted
Mertens is M_odd(x) = sum_j M(floor(x / 2^j)).  H(N) follows in a few
seconds.
"""

import numpy as np
from numba import njit

N = 10**9
SIEVE = 4 * 10**6


@njit(cache=True)
def mertens_table(limit):
    """Prefix sums of the Moebius function up to limit (linear sieve)."""
    mu = np.zeros(limit + 1, dtype=np.int64)
    mu[1] = 1
    primes = np.empty(limit // 2, dtype=np.int64)
    np_ = 0
    is_comp = np.zeros(limit + 1, dtype=np.uint8)
    for i in range(2, limit + 1):
        if not is_comp[i]:
            primes[np_] = i
            np_ += 1
            mu[i] = -1
        for j in range(np_):
            p = primes[j]
            if i * p > limit:
                break
            is_comp[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    for i in range(2, limit + 1):
        mu[i] += mu[i - 1]
    return mu


@njit(cache=True)
def big_mertens(n, small):
    """big[i] = M(n // i) for 1 <= i <= n // limit, via the recursion."""
    limit = small.shape[0] - 1
    imax = n // limit
    big = np.zeros(imax + 1, dtype=np.int64)
    for i in range(imax, 0, -1):
        x = n // i
        res = np.int64(1)
        d = np.int64(2)
        while d <= x:
            v = x // d
            d2 = x // v
            res -= (d2 - d + 1) * (small[v] if v <= limit else big[n // v])
            d = d2 + 1
        big[i] = res
    return big


@njit(cache=True)
def solve(n, small, big):
    limit = small.shape[0] - 1

    def mert(x):
        if x <= limit:
            return small[x]
        return big[n // x]

    def mert_odd(x):
        s = np.int64(0)
        while x > 0:
            s += mert(x)
            x //= 2
        return s

    # totient summatory: sum_{s<=n} phi(s) = (1/2) sum_d mu(d) v(v+1), v = n//d
    tot2 = np.int64(0)  # twice the summatory
    d = np.int64(1)
    while d <= n:
        v = n // d
        d2 = n // v
        tot2 += (mert(d2) - mert(d - 1)) * v * (v + 1)
        d = d2 + 1
    coprime_pairs = tot2 // 2 - 1  # drop s = 1

    # P(n) = 2 sum_{d odd} mu(d) G(n // d) over blocks with odd Mertens
    p_cnt = np.int64(0)
    d = np.int64(1)
    while d <= n:
        v = n // d
        d2 = n // v
        k1 = (v - 1) // 4
        k3 = (v - 3) // 4 if v >= 3 else np.int64(-1)
        g = k1 * (k1 + 1) // 2 + k3 * (k3 + 1) // 2
        p_cnt += (mert_odd(d2) - mert_odd(d - 1)) * g
        d = d2 + 1
    return coprime_pairs - 2 * p_cnt


def h(n, small):
    big = big_mertens(n, small)
    return int(solve(n, small, big))


def main():
    small = mertens_table(SIEVE)
    assert h(4, small) == 5
    assert h(100, small) == 2043
    assert h(220, small) == 9843  # brute-force verified
    return h(N, small)


if __name__ == "__main__":
    print(main())  # 202642367520564145
