"""Project Euler 436: Unfair Wager.

Renewal facts for sums of independent U(0,1): the density that some
partial sum sits at level s < 1 (before crossing) is e^s, plus an atom
of weight 1 at s = 0 (no draws yet).  Player 1 crosses level 1: the
joint density of her last draw x and overshoot t = S - 1 is e^(1+t-x)
on 0 < t < x < 1 (the pre-sum was 1 + t - x).  Player 2 then crosses a
fresh gap c = 1 - t in (0, 1): given c, the last draw y in (0, 1) has
density [y > c] + e^c - e^(max(0, c - y)) (atom of no pre-draws when
y > c, plus pre-sum u > c - y).  Integrating the y-tail in closed form
(elementary):

    P(y > x | c)  =  e^c (1 - x) - e^(c - x) + 1     if x < c,
                  =  e^c (1 - x)                      if x > c,

so the answer is the double integral of e^(1+t-x) times that tail over
0 < t < x < 1, split at t = 1 - x.  Both regions have analytic
integrands, evaluated with 64-node Gauss-Legendre quadrature (nodes
from Newton iteration on the Legendre polynomial), which is exact to
float precision for analytic functions -- no symbolic algebra package
needed.  A Monte Carlo simulation cross-checks the value.
"""

import math
import random


def gauss_legendre(n: int):
    """Nodes and weights for n-point Gauss-Legendre on [-1, 1]."""
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))  # Chebyshev initial guess
        for _ in range(60):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        nodes.append(x)
        weights.append(2 / ((1 - x * x) * dp * dp))
    return nodes, weights

_N, _W = gauss_legendre(64)


def integrate(f, a: float, b: float) -> float:
    h, m = (b - a) / 2, (a + b) / 2
    return h * sum(w * f(m + h * x) for x, w in zip(_N, _W))


def tail_below(x: float, t: float) -> float:
    c = 1 - t
    return math.exp(c) * (1 - x) - math.exp(c - x) + 1


def tail_above(x: float, t: float) -> float:
    return math.exp(1 - t) * (1 - x)


def second_player_win_probability() -> float:
    def inner(x: float) -> float:
        m = min(x, 1 - x)
        below = integrate(lambda t: math.exp(1 + t - x) * tail_below(x, t), 0.0, m)
        above = 0.0
        if x > 0.5:  # region 1 - x < t < x, where x > c
            above = integrate(lambda t: math.exp(1 + t - x) * tail_above(x, t), 1 - x, x)
        return below + above

    # split the outer integral at the kink x = 1/2
    return integrate(inner, 0.0, 0.5) + integrate(inner, 0.5, 1.0)


def monte_carlo(trials: int) -> float:
    wins = 0
    for _ in range(trials):
        s = 0.0
        while s <= 1.0:
            x = random.random()
            s += x
        while s <= 2.0:
            y = random.random()
            s += y
        if y > x:
            wins += 1
    return wins / trials


if __name__ == "__main__":
    p = second_player_win_probability()
    assert abs(p - monte_carlo(400_000)) < 0.005
    print(f"{p:.10f}")  # 0.5276662759
