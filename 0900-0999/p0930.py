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
instead of n^(m-1); 1 - mu >= 2(1 - cos(2 pi / n))/m stays comfortably
away from 0, and the positive sum is evaluated with mpmath at 35 digits.

The formula reproduces all six given values, including
G(6,6) = 1.681521567954e4 to all printed digits.
"""

from math import comb

from mpmath import cos, floor, log10, mp, mpf, nstr, pi

mp.dps = 35


def f_nm(n: int, m: int):
    cosv = [cos(2 * pi * j / n) for j in range(n)]
    total = [mpf(0)]

    def rec(j, rem, mult, csum, s, iszero):
        if j == n - 1:
            if iszero and rem == 0:
                return  # v = 0
            cs = csum + rem * cosv[n - 1]
            ss = (s + rem * (n - 1)) % n
            mu = (cosv[ss] + cs) / m
            total[0] += mult / (1 - mu)
            return
        for c in range(rem + 1):
            rec(j + 1, rem - c, mult * comb(rem, c),
                csum + c * cosv[j], (s + c * j) % n,
                iszero and (rem - c == 0 if j == 0 else c == 0))

    rec(0, m - 1, 1, mpf(0), 0, True)
    return total[0]


def solve(n_max: int, m_max: int) -> str:
    g = mpf(0)
    for n in range(2, n_max + 1):
        for m in range(2, m_max + 1):
            g += f_nm(n, m)
    e = int(floor(log10(g)))
    mant = g / mpf(10) ** e
    return f"{nstr(mant, 13, strip_zeros=False)}e{e}"


if __name__ == "__main__":
    assert abs(f_nm(2, 2) - mpf(1) / 2) < mpf("1e-25")  # given
    assert abs(f_nm(3, 2) - mpf(4) / 3) < mpf("1e-25")  # given
    assert abs(f_nm(2, 3) - mpf(9) / 4) < mpf("1e-25")  # given
    assert abs(f_nm(4, 5) - mpf(6875) / 24) < mpf("1e-22")  # given
    g33 = sum(f_nm(n, m) for n in (2, 3) for m in (2, 3))
    assert abs(g33 - mpf(137) / 12) < mpf("1e-22")  # given
    g45 = sum(f_nm(n, m) for n in range(2, 5) for m in range(2, 6))
    assert abs(g45 - mpf(6277) / 12) < mpf("1e-20")  # given
    assert solve(6, 6) == "1.681521567954e4"  # given
    print(solve(12, 12))  # 1.345679959251e12
