"""Project Euler 935: Rolling Square.

A square of side b < 1 rolls clockwise inside the unit square, pivoting
about touching corners; initially it is nestled in a corner.  F(N) counts
the b whose first return to the start takes at most N steps.

Reduction to a 1-D map.  While rolling, the contact pattern is always one
of: flat on a wall, or bridging a wall-corner with two adjacent corners
(the edge spans the corner as a chord, r^2 + s^2 = b^2 with r, s the
distances of the contact corners from the big corner).  Between corner k
and corner k+1 the wall budget gives 1 = s_k + m_k*b + r_{k+1} with a
unique integer m_k >= 0; m_k = 0 is a corner-to-corner "hop" (b > 1/2),
m_k >= 1 is an exit, m_k - 1 flat rolls, and a tilt-in.  Writing
r = b*sin(theta), s = b*cos(theta) and c = 1/b, the orbit obeys the chain

    sin(theta_{k+1}) + cos(theta_k) = c - m_k .

The start is a *nestle* (square seated in a corner, theta = 0).  Because
the dynamics from a nestle is deterministic, the orbit is a sequence of
identical nestle-to-nestle blocks of Delta corners, M = sum(m_k) and
P = M + Delta - 1 steps each; one block rotates the square by 90*M
degrees.  The square is back at the start exactly when a nestle lands on
the starting corner, i.e. after 4/gcd(Delta,4) blocks, so

    n(b) = (4 / gcd(Delta, 4)) * (M + Delta - 1).

For b > 1/sqrt(2) the hop map r -> 1 - sqrt(b^2 - r^2) acquires an
attracting fixed point (the inscribed square) whose basin contains the
launch, so no returns exist there; mirror/time-reversal symmetry forces
every block's m-sequence to be a palindrome with end shift
(m_{Delta-1} = m_0 + 1).  Solving the chains (each monotone in c, hence
at most one root) and validating against the exact map shows the roots
are in bijection with the coprime pairs (Delta, M):  every pair with
gcd(Delta, M) = 1 yields exactly one b, and no others occur.  (Some
roots are numerically extreme: the (16, 15) block's b differs from 1/2
by ~1e-107.)  Hence

    F(N) = #{(D, M) : D, M >= 1, gcd(D, M) = 1,
             (4/gcd(D,4)) * (M + D - 1) <= N}
         = A_{0 mod 4}(N + 1) + A_{2 mod 4}(N//2 + 1) + A_{odd}(N//4 + 1),

where A_class(L) counts coprime (D, M) with D + M <= L and D in the
residue class.  Each A is evaluated in O(L) by Moebius inversion: for
squarefree d the condition d | D induces a congruence on D' = D/d
(class odd: D' odd for odd d; class 2 mod 4: D' = 2 mod 4 / D' odd for
d odd / d = 2 mod 4; class 0 mod 4: D' = 0 mod 4 / D' even), and the
inner count is a closed-form arithmetic-progression sum.

Verified: F(6) = 4 with the four given algebraic b values, F(100) = 805,
and the block law reproduces the given orbits (b = 1/2 and 5/13 return
in 4 and 24 steps).  Runtime is dominated by the Moebius sieve (~25 s).
"""

import numpy as np
from numba import njit


def mobius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    is_comp = np.zeros(n + 1, dtype=bool)
    for p in range(2, n + 1):
        if not is_comp[p]:
            is_comp[p * p::p] = True
            mu[p::p] *= -1
            pp = p * p
            if pp <= n:
                mu[pp::pp] = 0
    return mu


@njit(cache=True)
def _w(t: int, a: int, m: int) -> int:
    """sum over d' = a, a+m, ... <= t-1 of (t - d')."""
    if t - 1 < a:
        return 0
    k = (t - 1 - a) // m + 1
    return k * (t - a) - m * (k * (k - 1) // 2)


@njit(cache=True)
def _a_class(L: int, cls: int, mu: np.ndarray) -> int:
    total = np.int64(0)
    for d in range(1, L + 1):
        md = mu[d]
        if md == 0:
            continue
        t = L // d
        if t < 2:
            continue
        if cls == 1:
            if d % 2 == 1:
                w = _w(t, 1, 2)
            else:
                continue
        elif cls == 2:
            w = _w(t, 2, 4) if d % 2 == 1 else _w(t, 1, 2)
        else:
            w = _w(t, 4, 4) if d % 2 == 1 else _w(t, 2, 2)
        total += md * w
    return int(total)


def f_count(n: int, mu: np.ndarray) -> int:
    return (_a_class(n + 1, 0, mu) + _a_class(n // 2 + 1, 2, mu)
            + _a_class(n // 4 + 1, 1, mu))


def solve() -> int:
    n = 10 ** 8
    mu = mobius_sieve(n + 1)
    assert f_count(6, mu) == 4
    assert f_count(100, mu) == 805
    return f_count(n, mu)


if __name__ == "__main__":
    print(solve())  # 759908921637225
