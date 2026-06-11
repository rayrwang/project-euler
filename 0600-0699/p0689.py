"""Project Euler Problem 689: Binary Series.

For x uniform on [0, 1) the binary digits d_i(x) are i.i.d. Bernoulli(1/2)
(dyadic rationals have measure zero), so f(x) is distributed as
S = sum_i X_i / i^2 with X_i fair coin flips.  The characteristic function
factors term by term, (1 + e^(i t / i^2)) / 2 = e^(i t / (2 i^2))
cos(t / (2 i^2)), so

    phi(t) = e^(i t mu) C(t),  mu = pi^2 / 12,  C(t) = prod cos(t/(2 i^2)),

with C real.  S is continuous (|phi| is integrable), so the Gil-Pelaez
inversion formula gives, with beta = mu - a,

    p(a) = P(S > a) = 1/2 + (1/pi) Integral_0^inf sin(beta t) C(t) / t dt.

C is evaluated as the exact product over i <= 400 times
exp(sum_{i > 400} log cos), with log cos x = -x^2/2 - x^4/12 - x^6/45 - ..., whose coefficient sums
over i > 400 are accumulated directly (computing them as zeta minus a
partial sum would cancel catastrophically); the first omitted order is
below 1e-12 for t <= 2500.  Only sqrt(t/2) factors oscillate appreciably at size t, giving
the envelope |C(t)| ~ exp(-ln 2 sqrt(t/2)), so truncating at T = 2500
loses about 1e-10.  The integral is composite Simpson on a fixed grid,
with C precomputed once per grid and reused for every threshold; runs at
two step sizes must agree to 1e-10.

Verified: the layered identity p(1/2) = 2^(-8) sum over outcomes of
X_1..X_8 of P(tail > 1/2 - partial sum), with the tail probability
computed by the same inversion applied to sum_{i >= 9} X_i / i^2
(agreement to 1e-9); p(0) = 1, p(zeta(2)) = 0 and the symmetry value
p(mu) = 1/2 to 1e-9; a 10^8-sample Monte Carlo within five standard
errors; and the d_i(0.25) examples from the statement.
"""

import math

import numba
import numpy as np

N_EXACT = 400
T_MAX = 2500.0
ZETA2 = math.pi**2 / 6


def d(x: float, i: int) -> int:
    """i-th binary digit of x in [0, 1) after the point."""
    return int(x * 2**i) % 2


@numba.jit(cache=True)
def cos_product(ts: np.ndarray, start: int, tails: np.ndarray) -> np.ndarray:
    """C_start(t) = prod_{i >= start} cos(t / (2 i^2)) on the grid."""
    out = np.empty(len(ts))
    for j in range(len(ts)):
        t = ts[j]
        c = 1.0
        for i in range(start, N_EXACT + 1):
            c *= math.cos(t / (2.0 * i * i))
        x2 = t * t / 4.0  # log cos x = -x^2/2 - x^4/12 - x^6/45 - ...
        out[j] = c * math.exp(
            -x2 / 2.0 * tails[0] - x2 * x2 / 12.0 * tails[1]
            - x2 * x2 * x2 / 45.0 * tails[2]
        )
    return out


def make_grid(start: int, h: float) -> tuple[np.ndarray, np.ndarray]:
    n = int(T_MAX / h / 2) * 2
    ts = np.arange(n + 1) * h
    # Direct sums: zeta(8) - partial etc. would cancel catastrophically.
    tails = np.array([
        sum(i ** (-4.0 * k) for i in range(10**5, N_EXACT, -1))
        for k in (1, 2, 3)
    ])
    return ts, cos_product(ts, start, tails)


def gil_pelaez(a: float, start: int, grids) -> float:
    """P(sum_{i >= start} X_i / i^2 > a) for a >= 0."""
    mu = (ZETA2 - sum(1 / i**2 for i in range(1, start))) / 2
    beta = mu - a
    results = []
    for ts, cs in grids:
        vals = np.where(ts > 0, np.sin(beta * ts) / np.where(ts > 0, ts, 1),
                        beta) * cs
        weights = np.full(len(ts), 2.0)
        weights[1::2] = 4.0
        weights[0] = weights[-1] = 1.0
        h = ts[1] - ts[0]
        results.append(float(vals @ weights) * h / 3)
    assert abs(results[0] - results[1]) < 1e-10
    return 0.5 + results[1] / math.pi


@numba.jit(cache=True)
def monte_carlo(samples: int, a: float, seed: int) -> float:
    np.random.seed(seed)
    hits = 0
    for _ in range(samples):
        s = 0.0
        i = 1
        while i < 100000:
            if s > a:  # decided: hit
                break
            if i > 1 and s + 1.0 / (i - 1) <= a:  # rest is < 1/(i-1): miss
                break
            if np.random.random() < 0.5:
                s += 1.0 / (i * i)
            i += 1
        if s > a:
            hits += 1
    return hits / samples


if __name__ == "__main__":
    assert d(0.25, 2) == 1
    assert all(d(0.25, i) == 0 for i in range(1, 30) if i != 2)

    grids1 = [make_grid(1, 0.004), make_grid(1, 0.002)]
    answer = gil_pelaez(0.5, 1, grids1)
    assert abs(gil_pelaez(0.0, 1, grids1) - 1.0) < 1e-9
    assert abs(gil_pelaez(ZETA2, 1, grids1)) < 1e-9
    assert abs(gil_pelaez(ZETA2 / 2, 1, grids1) - 0.5) < 1e-9  # symmetry

    head = 8  # condition on the first 8 digits, recompute with the tail
    grids9 = [make_grid(head + 1, 0.004), make_grid(head + 1, 0.002)]
    layered = 0.0
    for mask in range(2**head):
        s = sum(1 / i**2 for i in range(1, head + 1) if mask >> (i - 1) & 1)
        layered += 1.0 if s > 0.5 else gil_pelaez(0.5 - s, head + 1, grids9)
    assert abs(layered / 2**head - answer) < 1e-9

    mc = monte_carlo(10**8, 0.5, 12345)
    assert abs(mc - answer) < 5 * math.sqrt(0.25 / 10**8)
    print(f"{answer:.8f}")  # 0.56565454
