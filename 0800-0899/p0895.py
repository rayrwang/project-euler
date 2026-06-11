import itertools
from collections import Counter
from fractions import Fraction

import numba
import numpy as np

# A stack is a Blue-Red Hackenbush string, so its game value is the number
# with that sign expansion: an initial run of a coins of colour s is worth
# s * a, and the remaining coins add s_j 2^(1-j), giving value s (a - g)
# where g = odd / 2^t lies in (0, 1).  A triple is fair iff the values sum
# to zero, which forces colour pattern two-versus-one, so G(m) = 6 C(m)
# with C counting (positive, positive, negative) ordered triples.
#
# Writing the positive values a_i - g_i and the negative one -(b - h), the
# fairness and balance conditions become Delta := a1 + a2 - b in {0, 1},
# g1 + g2 = h + Delta, and E(g1) + E(g2) = E(h) + Delta, where E(g) counts
# 2 - t + 2 (ones in g's binary fraction before the last).  The base-2
# Kummer identity s(x) + s(y) = s(x + y) + carries turns the E condition
# into t1 + t2 - t_h = 2 c + Delta with c the carry count of g1 + g2.
# The number of compatible run lengths (a1, a2, b) is, by inclusion and
# exclusion, f(m-t_h+D) - f(t1-t_h+D) - f(t2-t_h+D) + f(t1+t2-t_h-m+D)
# with f(n) = n (n - 1) / 2.
#
# Looking at the deepest bit of h (depth tau) splits the fractional case:
# either exactly one summand reaches depth tau (then its twin has depth
# u = 2c + Delta and the weight collapses to f(m - tau + Delta)), or both
# summands share a depth t > tau and their tails below tau must sum to
# 2^-tau, which fixes the tail carries to exactly t - tau and leaves
# 2^(t-tau-1) tail choices.  Both cases are O(m^2) carry DPs over the bit
# positions, processed deepest-first with new triples injected per depth.

MOD = 989898989


def f(c: int) -> int:
    return c * (c - 1) // 2 if c >= 2 else 0


def brute_force(m: int) -> int:
    """Direct enumeration of stacks as Hackenbush strings (small m)."""
    groups: Counter = Counter()
    for h in range(1, m + 1):
        for s in itertools.product((1, -1), repeat=h):
            a = 0
            while a < len(s) and s[a] == s[0]:
                a += 1
            v = Fraction(s[0] * a)
            d = Fraction(1, 2)
            for j in range(a, len(s)):
                v += s[j] * d
                d /= 2
            groups[(v, sum(s))] += 1
    total = 0
    for (v1, n1), c1 in groups.items():
        for (v2, n2), c2 in groups.items():
            c3 = groups.get((-v1 - v2, -(n1 + n2)))
            if c3:
                total += c1 * c2 * c3
    return total


@numba.njit(cache=True)
def case_d1(m: int, delta: int, mod: int) -> int:
    """One summand reaches the deepest bit of h; the other has depth 2c+D."""
    size = 3 * m + 8
    off = 2 * m + 4
    cur = np.zeros((2, 2, size), dtype=np.int64)  # [started][carry][acc]
    new = np.zeros((2, 2, size), dtype=np.int64)
    for p in range(m - 1, 0, -1):
        new[:, :, :] = 0
        for i in range(size):
            w00, w01 = cur[0, 0, i], cur[0, 1, i]
            w10, w11 = cur[1, 0, i], cur[1, 1, i]
            # second summand still absent: free bit of the first
            new[0, 0, i] += 2 * w00 + w01
            if i >= 2:
                new[0, 1, i - 2] += w01
            # second summand starts here with its forced lowest one-bit
            if i + p < size:
                new[1, 0, i + p] += w00
                new[1, 1, i + p - 2] += w00 + 2 * w01
            # both running: four bit pairs
            new[1, 0, i] += 3 * w10 + w11
            if i >= 2:
                new[1, 1, i - 2] += w10 + 3 * w11
        cur, new = new, cur
        cur %= mod
        # inject the triple whose h has its deepest bit at depth tau = p
        weight = m - p + delta
        if weight >= 2:
            cur[0, 0, off] = (cur[0, 0, off] + weight * (weight - 1) // 2) % mod
    return int(cur[1, delta, off + delta] % mod)


@numba.njit(cache=True)
def case_d2(m: int, delta: int, mod: int) -> int:
    """Both summands share a depth t below h's deepest bit tau."""
    size = 3 * m + 8
    off = m + 4
    # V[tau] = sum over t of 2^(t-tau-1) * (a1, a2, b)-count for this case
    inject = np.zeros(m, dtype=np.int64)
    for tau in range(1, m):
        v = 0
        pw = 1
        for t in range(tau + 1, m):
            c1 = m - tau + delta
            c2 = t - tau + delta
            c3 = 2 * t - tau - m + delta
            term = 0
            if c1 >= 2:
                term += c1 * (c1 - 1) // 2
            if c2 >= 2:
                term -= 2 * (c2 * (c2 - 1) // 2) % mod
            if c3 >= 2:
                term += c3 * (c3 - 1) // 2
            v = (v + pw * (term % mod)) % mod
            pw = (pw * 2) % mod
        inject[tau] = v % mod
    cur = np.zeros((2, size), dtype=np.int64)  # [carry][Z]
    new = np.zeros((2, size), dtype=np.int64)
    for p in range(m - 1, 0, -1):
        new[:, :] = 0
        for i in range(size):
            w0, w1 = cur[0, i], cur[1, i]
            new[0, i] += 3 * w0 + w1
            if i + 2 < size:
                new[1, i + 2] += w0 + 3 * w1
        cur, new = new, cur
        cur %= mod
        v = inject[p]
        if v:
            cur[0, off - p] = (cur[0, off - p] + v) % mod
            cur[1, off - p + 2] = (cur[1, off - p + 2] + v) % mod
    return int(cur[delta, off - delta] % mod)


def G(m: int, mod: int) -> int:
    case_a = (m * (m - 1) // 2) % mod
    case_b = 2 * sum(pow(2, t - 1, mod) * f(m - t) for t in range(1, m)) % mod
    d1 = 2 * (case_d1(m, 0, mod) + case_d1(m, 1, mod))
    d2 = case_d2(m, 0, mod) + case_d2(m, 1, mod)
    return 6 * (case_a + case_b + d1 + d2) % mod


if __name__ == "__main__":
    big = 1 << 40  # exceeds the true counts below, so "mod big" is exact
    assert brute_force(2) == 6 and brute_force(5) == 348  # given
    for m in range(2, 9):
        assert G(m, big) == brute_force(m)
    assert G(20, big) == 125825982708  # given
    print(G(9898, MOD))  # 670785433
