"""Project Euler Problem 672: One More One.

One round of the process takes n to ceil(n / 7) at a cost of (-n) mod 7
added ones, and iterated ceiling division satisfies
ceil(ceil(n / 7) / 7) = ceil(n / 49), so with h(v) = (-v) mod 7,

    g(n) = sum over i >= 0 with ceil(n / 7^i) >= 2 of h(ceil(n / 7^i)).

Summing over n <= N and swapping the order, ceil(n / 7^i) = v happens for
exactly 7^i values of n when 2 <= v < V_i = ceil(N / 7^i) and for
N - (V_i - 1) 7^i values when v = V_i, so

    S(N) = sum_i [ 7^i (T(V_i - 1) - 6) + h(V_i) (N - (V_i - 1) 7^i) ],

where T(M) = sum_{v=0}^M h(v) = 21 floor((M+1)/7) + prefix(M+1 mod 7) and
the -6 removes v = 1.

For N = (7^K - 1) / 11 the ceilings are explicit: with j = K - i and
r_j = 7^j mod 11 (period 10), V_i = (7^j - r_j) / 11 + 1, which is >= 2
exactly for j >= 2.  Everything needed per term - V_i mod p, V_i mod 7
(which depends only on r_j), and the powers 7^i, 7^j - updates in O(1)
modular operations, so H(10^9) is a single numba loop of 10^9 steps modulo
p = 1117117717.

Verified: g(125) = 8, g(1000) = 9, g(10000) = 21, S against direct
simulation for N <= 30000, and H(10) = 690409338.
"""

import numba

MOD = 1117117717
K = 10**9


def g(n: int) -> int:
    ones = 0
    while n > 1:
        ones += -n % 7
        n = -(-n // 7)  # ceil(n / 7)
    return ones


def h_total(k: int, mod: int) -> int:
    return int(h_loop(
        k, mod, pow(7, mod - 2, mod), pow(11, mod - 2, mod),
        (pow(7, k, mod) - 1) % mod * pow(11, mod - 2, mod) % mod,
        pow(7, k - 2, mod),  # 7^i for j = 2
    ))


@numba.jit(cache=True)
def h_loop(k: int, mod: int, inv7: int, inv11: int, n_mod: int,
           pow_i: int) -> int:
    """S((7^k - 1) / 11) modulo mod, given precomputed constants."""
    # prefix[w] = sum of (-v) mod 7 for v = 0..w-1
    prefix = (0, 0, 6, 11, 15, 18, 20)

    pow_j = 49 % mod  # 7^j, starting at j = 2
    r = 49 % 11  # 7^j mod 11, period 10 in j
    total = 0
    for _ in range(2, k + 1):
        a = ((pow_j - r) % mod * inv11 + 1) % mod  # V_i mod p
        s = ((-r % 7) * 2 + 1) % 7  # V_i mod 7, as 11^-1 = 2 mod 7
        # T(V_i - 1) = 21 * (V_i - s) / 7 + prefix[s]
        t = (21 * ((a - s) % mod * inv7 % mod) + prefix[s]) % mod
        h_v = -s % 7
        total += pow_i * (t - 6) % mod
        total += h_v * ((n_mod - (a - 1) * pow_i) % mod) % mod
        total %= mod
        pow_j = pow_j * 7 % mod
        pow_i = pow_i * inv7 % mod
        r = r * 7 % 11
    return total


if __name__ == "__main__":
    assert g(125) == 8 and g(1000) == 9 and g(10000) == 21
    running = 0
    checks = {n: 0 for n in (1, 7, 100, 5489, 7**5, 30000)}
    for n in range(1, 30001):
        running += g(n)
        if n in checks:
            checks[n] = running
    # S(N) from the swapped-order formula, exact, for arbitrary N.
    def s_formula(big_n: int) -> int:
        total, p7 = 0, 1
        while -(-big_n // p7) >= 2:
            v = -(-big_n // p7)
            m = v  # T(v - 1) needs blocks of (m = v) values
            t = 21 * (m // 7) + [0, 0, 6, 11, 15, 18, 20][m % 7]
            total += p7 * (t - 6) + (-v % 7) * (big_n - (v - 1) * p7)
            p7 *= 7
        return total

    assert all(s_formula(n) == v for n, v in checks.items())
    assert h_total(10, MOD) == 690409338 == s_formula((7**10 - 1) // 11)
    print(h_total(K, MOD))  # 91627537
