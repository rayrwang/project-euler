"""Project Euler 965: Expected Minimal Fractional Value.

Between consecutive Farey fractions p/q < p'/q' of order N every {nx} is
linear, equal to (np mod q)/q + n(x - p/q). For each residue r = np mod q the
lowest line has n = m_r, the least positive solution of n = -r q' (mod q)
(using p q' = -1 mod q). A line r >= 1 could undercut the r = 0 line
y = q(x - p/q) inside the interval only if r q' + m_r < q -- impossible, since
r q' + m_r is a positive multiple of q. Hence on the whole interval

    f_N(x) = {q x},   q = denominator of the left Farey neighbour,

and integrating q t over (0, 1/(q q')) gives 1/(2 q q'^2) per interval. Each
coprime pair (q, q') with q, q' <= N and q + q' > N occurs as consecutive
Farey denominators exactly once, so

    F(N) = (1/2) sum_{q + q' > N, gcd(q, q') = 1} 1 / (q q'^2).

Checks: F(1) = 1/2, F(2) = 3/8, F(4) = 1/4, F(10) = 19/144 = 0.13194444...,
all matching the given values (and direct numerical integration of f_N).
Kahan summation keeps the float64 error far below the 13th decimal.
"""

import numba


@numba.njit(cache=True)
def solve(n: int) -> float:
    total = 0.0
    comp = 0.0  # Kahan compensation
    for q in range(1, n + 1):
        for qp in range(n - q + 1, n + 1):
            a, b = q, qp
            while b:
                a, b = b, a % b
            if a == 1:
                term = 1.0 / (q * float(qp) * qp)
                y = term - comp
                t = total + y
                comp = (t - total) - y
                total = t
    return total / 2


if __name__ == "__main__":
    print(f"{solve(10**4):.13f}")  # 0.0003452201133
