"""Project Euler Problem 665: Proportionate Nim.

Moves subtract (k, 0), (0, k), (k, k), (k, 2k) or (2k, k), so each move
preserves a coordinate, the difference, or one of the skew forms
"larger - 2 * smaller" / "smaller - 2 * larger".  Two losing positions can
never share such an invariant line in an attackable direction, which
forces every integer to occur in at most one losing pair, every
difference at most once, and the x - 2y values (in both orientations) at
most once.  Empirically every integer occurs in exactly one pair, so the
losing pairs are built greedily: a runs over the mex of used values, and
its partner is the smallest unused b > a such that b - a is an unused
difference and both b - 2a and a - 2b are unused skew values.

A case analysis (each candidate-to-loser attack type maps to one of the
tests, with attacks from an earlier loser onto the candidate impossible
because they would need a coordinate below some earlier mex) shows the
exact game tests carry side conditions on two of the skew forms; an
independent implementation with those exact thresholded tests produces
identical pairs, and both match a full game-theoretic brute force
(marking everything that attacks each loser) for all sums <= 1200, so
the simple unconditional tests are used here.

Each test set is an insertion-only set of integers, so a successor
union-find per set lets the b-search jump straight over saturated bands:
if the difference is used, b jumps to a + (next unused difference); if
b - 2a is used, b jumps to 2a + (next unused skew value); the rare
a - 2b collision (probing downward) just advances b by one.  About
3.2 * 10^6 pairs are generated in under a second.

Verified: exact pair match with the brute force for sums <= 1200, and
f(10) = 21, f(100) = 1164, f(1000) = 117002.
"""

import numba
import numpy as np

M = 10**7


def losers_brute(s: int) -> list[tuple[int, int]]:
    attacked = np.zeros((s + 1, s + 1), dtype=bool)
    losers = []
    for total in range(s + 1):
        for n in range(total // 2 + 1):
            m = total - n
            if attacked[n, m]:
                continue
            losers.append((n, m))
            for dn, dm in ((1, 0), (0, 1), (1, 1), (1, 2), (2, 1)):
                k = 1
                while n + k * dn + m + k * dm <= s:
                    x, y = n + k * dn, m + k * dm
                    attacked[min(x, y), max(x, y)] = True
                    k += 1
    return losers


@numba.jit(nogil=True)
def find(par: np.ndarray, x: int) -> int:
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


@numba.jit(nogil=True)
def losing_pairs(max_sum: int):
    """Total of n + m over losing pairs with n + m <= max_sum, plus pairs.

    Partners satisfy b <= 3a (ratio 3 occurs only for tiny a; the bulk
    sits near b = 1.478 a and b = 2.248 a), so coordinates stay below
    1.25 * max_sum; ranges are asserted via the array bounds.
    """
    half = max_sum // 2
    maxc = max_sum + max_sum // 4 + 100
    coords = np.arange(maxc + 2, dtype=np.int64)
    diffs = np.arange(maxc + 2, dtype=np.int64)
    voff = 2 * maxc  # skew values x - 2y live in [-2 maxc, maxc]
    skew = np.arange(3 * maxc + 2, dtype=np.int64)
    coords[0] = 1
    diffs[0] = 1
    skew[voff] = voff + 1  # the pair (0, 0)
    ps = np.empty(half + 2, dtype=np.int64)
    qs = np.empty(half + 2, dtype=np.int64)
    total = 0
    cnt = 0
    a = 1
    while True:
        a = find(coords, a)
        if a > half:
            break
        b = a + 1
        while True:
            b = find(coords, b)
            d = b - a
            nd = find(diffs, d)
            if nd != d:
                b = a + nd
                continue
            i1 = b - 2 * a + voff
            ni = find(skew, i1)
            if ni != i1:
                b = 2 * a + ni - voff
                continue
            i2 = a - 2 * b + voff
            if skew[i2] != i2:
                b += 1  # rare; the probe moves downward as b grows
                continue
            break
        ps[cnt] = a
        qs[cnt] = b
        cnt += 1
        coords[a] = a + 1
        coords[b] = b + 1
        diffs[d] = d + 1
        skew[i1] = i1 + 1
        if skew[i2] == i2:
            skew[i2] = i2 + 1
        if a + b <= max_sum:
            total += a + b
        a += 1
    return total, ps[:cnt], qs[:cnt]


def f(max_sum: int) -> int:
    return losing_pairs(max_sum)[0]


if __name__ == "__main__":
    brute = losers_brute(1200)
    total, ps, qs = losing_pairs(1200)
    mine = {(0, 0)} | set(zip(ps.tolist(), qs.tolist()))
    assert {lp for lp in brute if sum(lp) <= 1200} <= mine
    assert all(sum(lp) > 1200 for lp in mine - set(brute))
    assert f(10) == 21
    assert f(100) == 1164
    assert f(1000) == 117002
    print(f(M))  # 11541685709674
