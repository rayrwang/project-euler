"""Project Euler 959: Jumping Frog.

The frog's step distribution is +b or -a with probability 1/2 each, so for
a = 89, b = 97 the drift is positive and the walk is transient. By the
classical range theorem for random walks (Spitzer), c_n / n converges to the
probability that the walk never returns to its starting point: site S_k is
counted as "new" exactly when the walk avoids S_k at times before k, and by
stationarity the density of such times tends to the no-return probability.

The expected total number of visits to the origin (counting time 0) is
G = sum_n P(S_n = 0), and by the strong Markov property G = 1/(1 - rho)
where rho is the return probability. Hence f(a, b) = 1 - rho = 1/G.

With gcd(a, b) = 1, S_n = 0 forces n = (a + b) k with exactly a k up-steps,
so G = sum_{k >= 0} C((a+b)k, ak) / 2^((a+b)k). The terms decay
geometrically with ratio 2^((a+b)(H(a/(a+b)) - 1)) ~ 0.842 (H the binary
entropy), so ~200 terms give far more than the nine digits required. The
sum is evaluated in exact integer fixed-point arithmetic.

Verified against the given f(1, 1) = 0 (the series diverges, G = infinity)
and f(1, 2) = 0.427050983, and against direct Monte Carlo simulation.
"""

from math import comb

A = 89
B = 97
TERMS = 250
SCALE = 10**40


def solve() -> str:
    # G * SCALE as an exact integer (truncation error far below 10^-9)
    g = 0
    for k in range(TERMS):
        n = (A + B) * k
        g += (SCALE * comb(n, A * k)) >> n
    # f = 1/G, rounded to 9 decimal places
    f_scaled = (10**9 * SCALE + g // 2) // g
    return f"0.{f_scaled:09d}"


if __name__ == "__main__":
    print(solve())  # 0.857162085
