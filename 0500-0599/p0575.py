"""
https://projecteuler.net/problem=575

A robot wanders a 1000 x 1000 grid of rooms numbered row by row.
Its designers were told to program it "with equal probability of
remaining in the same room or moving to an adjacent room", which
admits two readings, and the robot was built with one of the two
chosen with equal likelihood:

  A) lazy walk: stay with probability 1/2, otherwise move to a
     uniformly random adjacent room;
  B) all options uniform: each of the d adjacent rooms and staying
     put are equally likely, probability 1/(d+1) each.

Both chains are reversible, so their stationary distributions follow
from detailed balance. For A, pi(v) proportional to deg(v): the check
pi(v) * (1/2) * (1/deg v) = pi(u) * (1/2) * (1/deg u) holds for
neighbouring rooms (laziness does not change the stationary law of
the simple random walk). For B, pi(v) proportional to deg(v) + 1:
pi(v) * 1/(deg v + 1) is symmetric in the same way.

After "unfathomable periods of time" the answer is the stationary
probability of being in a square-numbered room, averaged over the two
robot builds:

  P = ( S_d / (2E)  +  (S_d + n) / (2E + n^2) ) / 2,

where S_d sums the degrees of the rooms numbered k^2 (k = 1..n),
2E = 4n(n-1) is the total degree, and there are n square rooms each
gaining +1 in variant B. Room r sits at row (r-1)//n, column
(r-1) mod n, with degree 4 minus a unit per touched boundary.

Everything is computed in exact rationals; the given 5 x 5 value
0.177976190476 is asserted, and a direct power-iteration of both
5 x 5 transition matrices cross-checks the stationary laws.
"""

from fractions import Fraction


def _solve(n: int) -> Fraction:
    def deg(r: int, c: int) -> int:
        return (0 < r) + (r < n - 1) + (0 < c) + (c < n - 1)

    sd = 0
    k = 1
    while k * k <= n * n:
        r, c = divmod(k * k - 1, n)
        sd += deg(r, c)
        k += 1
    nsq = k - 1
    total_d = 4 * n * (n - 1)
    p_lazy = Fraction(sd, total_d)
    p_uniform = Fraction(sd + nsq, total_d + n * n)
    return (p_lazy + p_uniform) / 2


def _power_iteration_check(n: int) -> float:
    """Stationary square-room probability of both variants on the
    n x n grid by long power iteration (floats), averaged."""
    cells = [(r, c) for r in range(n) for c in range(n)]
    nbrs = {
        (r, c): [
            (r + dr, c + dc)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if 0 <= r + dr < n and 0 <= c + dc < n
        ]
        for r, c in cells
    }
    squares = set()
    k = 1
    while k * k <= n * n:
        squares.add(divmod(k * k - 1, n))
        k += 1
    probs = []
    for variant in ("lazy", "uniform"):
        dist = dict.fromkeys(cells, 1.0 / (n * n))
        for _ in range(3000):
            new = dict.fromkeys(cells, 0.0)
            for v, p in dist.items():
                d = len(nbrs[v])
                if variant == "lazy":
                    new[v] += p / 2
                    for u in nbrs[v]:
                        new[u] += p / (2 * d)
                else:
                    new[v] += p / (d + 1)
                    for u in nbrs[v]:
                        new[u] += p / (d + 1)
            dist = new
        probs.append(sum(p for v, p in dist.items() if v in squares))
    return (probs[0] + probs[1]) / 2


if __name__ == "__main__":
    p5 = _solve(5)
    assert f"{float(p5):.12f}" == "0.177976190476"  # given
    assert abs(float(p5) - _power_iteration_check(5)) < 1e-12

    print(f"{float(_solve(1000)):.12f}")  # 0.000989640561
