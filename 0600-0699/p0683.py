"""Project Euler Problem 683: The Chase II.

Only the relative position of the two dice matters.  Each die moves
left, stays, or moves right with probability 1/3 independently, so the
difference walks on Z_k with steps P(0) = 1/3, P(+-1) = 2/9,
P(+-2) = 1/9 per turn.  A round with k players hands the dice to two
independently uniform players, making the initial difference uniform on
Z_k (difference 0 ends the round at once with payment 0), and the
eliminated player pays T^2 where T is the number of completed turns
until the difference first hits 0.

With transient states d = 1..k-1 and A = I - Q (Q the substochastic
transition matrix among transient states), the moment vectors satisfy

    A m1 = 1,        A m2 = 1 + 2 Q m1,

since m2(d) = E[(1 + T')^2] conditions one step ahead and m1, m2 vanish
at the absorbing state.  The expected payment of a k-player round is
(1/k) sum_d m2(d), and the pot equals the sum of payments over the
rounds with k = n, n-1, ..., 2 players, so

    G(n) = sum_{k=2}^{n} (1/k) sum_{d=1}^{k-1} m2_k(d).

Each k needs two dense solves of size k - 1; the total for n = 500 runs
in a couple of seconds with numpy.  The systems are exactly reproduced
with rational arithmetic for k <= 6 to validate the float pipeline.

Verified: exact Fraction solves equal the numpy values for k = 2..6,
G(5) = 96.5441... matches the stated 96.544, and G(50) prints exactly
2.82491788e6 as given.
"""

from fractions import Fraction

import numpy as np

N = 500
STEPS = ((0, Fraction(1, 3)), (1, Fraction(2, 9)), (-1, Fraction(2, 9)),
         (2, Fraction(1, 9)), (-2, Fraction(1, 9)))
STEPS_F = ((0, 1 / 3), (1, 2 / 9), (-1, 2 / 9), (2, 1 / 9), (-2, 1 / 9))


def round_et2_exact(k: int) -> Fraction:
    """E[T^2] for a k-player round, exact rational arithmetic."""
    m = k - 1
    mat = [[Fraction(0)] * m for _ in range(m)]
    for i in range(m):
        mat[i][i] += 1
        for dl, p in STEPS:
            nd = (i + 1 + dl) % k
            if nd != 0:
                mat[i][nd - 1] -= p

    def solve(amat, rhs):
        n = len(rhs)
        aug = [row[:] + [rhs[i]] for i, row in enumerate(amat)]
        for c in range(n):
            piv = next(r for r in range(c, n) if aug[r][c] != 0)
            aug[c], aug[piv] = aug[piv], aug[c]
            pv = aug[c][c]
            aug[c] = [x / pv for x in aug[c]]
            for r in range(n):
                if r != c and aug[r][c] != 0:
                    f = aug[r][c]
                    aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
        return [aug[r][n] for r in range(n)]

    m1 = solve(mat, [Fraction(1)] * m)
    rhs2 = []
    for i in range(m):
        acc = Fraction(1)
        for dl, p in STEPS:
            nd = (i + 1 + dl) % k
            if nd != 0:
                acc += 2 * p * m1[nd - 1]
        rhs2.append(acc)
    m2 = solve(mat, rhs2)
    return sum(m2, Fraction(0)) / k


def round_et2(k: int) -> float:
    """E[T^2] for a k-player round, floating point."""
    m = k - 1
    mat = np.eye(m)
    for dl, p in STEPS_F:
        for i in range(m):
            nd = (i + 1 + dl) % k
            if nd != 0:
                mat[i, nd - 1] -= p
    m1 = np.linalg.solve(mat, np.ones(m))
    rhs2 = np.ones(m)
    for dl, p in STEPS_F:
        for i in range(m):
            nd = (i + 1 + dl) % k
            if nd != 0:
                rhs2[i] += 2 * p * m1[nd - 1]
    m2 = np.linalg.solve(mat, rhs2)
    return float(m2.sum()) / k


def big_g(n: int) -> float:
    return sum(round_et2(k) for k in range(2, n + 1))


def sci9(x: float) -> str:
    mant, ex = f"{x:.8e}".split("e")
    return f"{mant}e{int(ex)}"


if __name__ == "__main__":
    for k in range(2, 7):
        assert abs(float(round_et2_exact(k)) - round_et2(k)) < 1e-9, k
    assert abs(big_g(5) - 96.544) < 5e-4
    assert sci9(big_g(50)) == "2.82491788e6"
    print(sci9(big_g(N)))  # 2.38955315e11
