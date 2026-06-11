"""Project Euler 930: The Gathering.

Track the differences x_k - x_1 (k = 2..m): the process is a random walk
on the abelian group G = Z_n^(m-1) -- moving ball 1 adds -+(1,...,1),
moving ball k adds +-e_(k-1), each with probability 1/(2m) -- and the
process stops exactly when the walk hits 0.  For an irreducible random
walk on a finite abelian group whose only eigenvalue 1 is the trivial
character (true here; the eigenvalue -1 occurring for even n, m is
harmless), the fundamental-matrix identity gives the hitting time

    E_x[T_0] = sum_{v != 0} (1 - chi_v(x)) / (1 - mu(v)),

with mu(v) = (cos(2 pi s/n) + sum_k cos(2 pi v_k/n)) / m and
s = sum v_k mod n.  A uniformly random initial configuration makes the
difference vector uniform on G, so E[chi_v(x)] = 0 for v != 0 and

    F(n, m) = sum_{v in Z_n^(m-1), v != 0} 1 / (1 - mu(v)).

mu depends only on the multiset of the v_k, so the sum is grouped by
count vectors of values (multinomial weights), C(n+m-2, m-1) terms
instead of n^(m-1).  Float64 suffices for the 13 requested digits
because the computation is cancellation-free: 1 - mu is assembled from
1 - cos(2 pi j / n) = 2 sin^2(pi j / n), every term of the sum is
positive, and math.fsum accumulates exactly, so the total's relative
error is bounded by the worst single-term error (~1e-15).

The formula reproduces all six given values, including
G(6,6) = 1.681521567954e4 to all printed digits.
"""

import math
from math import comb


def f_nm(n: int, m: int) -> float:
    # 1 - cos(2 pi j / n) = 2 sin(pi j / n)^2, computed without cancellation
    omc = [2.0 * math.sin(math.pi * j / n) ** 2 for j in range(n)]
    terms: list[float] = []

    def rec(j, rem, mult, osum, s, iszero):
        if j == n - 1:
            if iszero and rem == 0:
                return  # v = 0
            os = osum + rem * omc[n - 1]
            ss = (s + rem * (n - 1)) % n
            one_minus_mu = (omc[ss] + os) / m
            terms.append(mult / one_minus_mu)
            return
        for c in range(rem + 1):
            rec(j + 1, rem - c, mult * comb(rem, c),
                osum + c * omc[j], (s + c * j) % n,
                iszero and (rem - c == 0 if j == 0 else c == 0))

    rec(0, m - 1, 1, 0.0, 0, True)
    return math.fsum(terms)


def solve(n_max: int, m_max: int) -> str:
    g = math.fsum(f_nm(n, m)
                  for n in range(2, n_max + 1) for m in range(2, m_max + 1))
    e = math.floor(math.log10(g))
    mant = g / 10.0 ** e
    return f"{mant:.12f}e{e}"


if __name__ == "__main__":
    assert abs(f_nm(2, 2) - 1 / 2) < 1e-13  # given
    assert abs(f_nm(3, 2) - 4 / 3) < 1e-13  # given
    assert abs(f_nm(2, 3) - 9 / 4) < 1e-13  # given
    assert abs(f_nm(4, 5) - 6875 / 24) * 24 / 6875 < 1e-13  # given
    g33 = sum(f_nm(n, m) for n in (2, 3) for m in (2, 3))
    assert abs(g33 - 137 / 12) * 12 / 137 < 1e-13  # given
    g45 = sum(f_nm(n, m) for n in range(2, 5) for m in range(2, 6))
    assert abs(g45 - 6277 / 12) * 12 / 6277 < 1e-13  # given
    assert solve(6, 6) == "1.681521567954e4"  # given
    print(solve(12, 12))  # 1.345679959251e12
