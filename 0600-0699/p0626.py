"""Project Euler Problem 626: Counting Binary Matrices.

c(n) counts n x n binary matrices up to row/column swaps and row/column
complementations -- orbits under G = B_n x B_n with B_n = S_n x Z_2^n the
hyperoctahedral group, |G| = (2^n n!)^2.  Burnside: average the number of
fixed matrices over G.

For an element with row cycles (length a, flip parity p) and column
cycles (b, q), the cells decompose into gcd(a, b) orbits per cycle pair;
a fixed matrix exists on a cell orbit iff the accumulated flip
(b/g) p + (a/g) q is even, in which case each cell orbit contributes a
factor 2.  Writing v(x) for the 2-adic valuation, the pair condition is:
equal valuations force p = q, otherwise the cycle of larger valuation
must have parity 0.  Globally, with m_r and m_c the minimal valuations on
each side: if m_r = m_c, every cycle of valuation m shares one free
parity bit (2 patterns) and everything else is forced to 0; if, say,
m_r < m_c, all column parities are forced to 0 and exactly the row cycles
of valuation < m_c stay free (2^count patterns).  All patterns are
realisable, and for a fixed underlying permutation each parity pattern
arises from 2^(n - #cycles) sign vectors.

So Burnside reduces to a sum over pairs of partitions of n = 20 (627^2
pairs): with A(lambda) = n!/z_lambda permutations per type,

  c(n) (2^n n!)^2 = sum A(l_r) A(l_c) 2^(2n - k_r - k_c) N(l_r, l_c)
                    2^(sum_{i,j} gcd(a_i, b_j)),

evaluated exactly in Python integers (2^400-sized terms) and divided
exactly by |G| before reducing modulo the (composite) 1001001011.

Checks: brute-force orbit counts for n <= 3 (full 2^(n^2) enumeration
under the 8^n n!^2-element group), and the given c(1..9) values
1, 2, 3, 12, 39, 388, 8102, 656108, 199727714.
"""

from collections import Counter
from itertools import permutations, product
from math import factorial, gcd


def partitions(n: int, maxpart: int | None = None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def v2(x: int) -> int:
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def c(n: int) -> int:
    parts = list(partitions(n))
    info = []
    for lam in parts:
        # z_lambda = prod(l_i) * prod(mult_j!)
        cnt = Counter(lam)
        z = 1
        for ln, mult in cnt.items():
            z *= ln**mult * factorial(mult)
        A = factorial(n) // z
        k = len(lam)
        vals = [v2(x) for x in lam]
        mv = min(vals)
        info.append((lam, A, k, vals, mv))
    total = 0
    for lam_r, A_r, k_r, vals_r, m_r in info:
        for lam_c, A_c, k_c, vals_c, m_c in info:
            G = sum(gcd(a, b) for a in lam_r for b in lam_c)
            if m_r == m_c:
                N = 2
            elif m_r < m_c:
                N = 1 << sum(1 for v in vals_r if v < m_c)
            else:
                N = 1 << sum(1 for v in vals_c if v < m_r)
            total += A_r * A_c * N << (2 * n - k_r - k_c + G)
    order = (factorial(n) << n) ** 2
    assert total % order == 0
    return (total // order) % 1_001_001_011


def c_brute(n: int) -> int:
    size = n * n
    seen = set()
    orbits = 0
    masks_row = [[1 << (i * n + j) for j in range(n)] for i in range(n)]
    for m in range(1 << size):
        if m in seen:
            continue
        orbits += 1
        # BFS over the group orbit
        frontier = {m}
        orbit = set()
        while frontier:
            x = frontier.pop()
            if x in orbit:
                continue
            orbit.add(x)
            grid = [[(x >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
            for pr in permutations(range(n)):
                for pc in permutations(range(n)):
                    for fr in product((0, 1), repeat=n):
                        for fc in product((0, 1), repeat=n):
                            y = 0
                            for i in range(n):
                                for j in range(n):
                                    b = grid[pr[i]][pc[j]] ^ fr[i] ^ fc[j]
                                    if b:
                                        y |= masks_row[i][j]
                            if y not in orbit:
                                frontier.add(y)
        seen |= orbit
    return orbits


if __name__ == "__main__":
    for n, expect in ((1, 1), (2, 2), (3, 3)):
        assert c_brute(n) == expect
    given = {1: 1, 2: 2, 3: 3, 4: 12, 5: 39, 6: 388, 7: 8102, 8: 656108,
             9: 199727714}
    for n, expect in given.items():
        assert c(n) == expect % 1_001_001_011, n
    print(c(20))  # 695577663
