"""Project Euler 951: A Game of Chance.

A turn never crosses a run boundary (the optional second card must match the
first in colour), so the deck is consumed run by run, and the number of turns
spent on a run of length r is an independent random variable t(r): each step
takes one card and, if at least two remain in the run, takes a second with
probability 1/2. The first player wins iff the total number of turns
sum t(r_i) is odd, so with c(r) = E[(-1)^t(r)] the win probability is
(1 - prod_i c(r_i))/2 by independence. From t(r) = 1 + t(r - X),

    c(r) = -(c(r-1) + c(r-2)) / 2,   c(0) = 1, c(1) = -1,

giving c(2) = 0 and (checking d(r) = (-2)^r c(r), d(r) = d(r-1) - 2 d(r-2))
c(r) != 0 for all other r up to 52. Hence a configuration is fair iff it
contains a maximal run of length exactly 2.

Counting the complement: arrangements with no run of length 2 are built from
alternating-colour compositions of n into parts != 2; with C_k the number of
such compositions into k parts, the count is sum_k (2 C_k^2 + 2 C_{k+1} C_k)
(equal run counts with either starting colour, or counts differing by one).
F(n) = C(2n, n) minus that.

Verified against exact game-value computation (rational arithmetic over all
configurations) for n = 2..5 and the given F(2) = 4, F(8) = 11892.
"""

from math import comb


def comp_ne2(n: int, kmax: int) -> list[int]:
    """comp[k] = compositions of n into k positive parts, none equal to 2."""
    res = [0] * (kmax + 2)
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, kmax + 2):
        ndp = [0] * (n + 1)
        for tot in range(n):
            if dp[tot]:
                for part in range(1, n - tot + 1):
                    if part != 2:
                        ndp[tot + part] += dp[tot]
        dp = ndp
        res[k] = dp[n]
    return res


def solve(n: int) -> int:
    c = comp_ne2(n, n)
    nofair = sum(2 * c[k] * c[k] + 2 * c[k + 1] * c[k] for k in range(1, n + 1))
    return comb(2 * n, n) - nofair


if __name__ == "__main__":
    print(solve(26))  # 495568995495726
