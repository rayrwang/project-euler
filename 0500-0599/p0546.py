"""
https://projecteuler.net/problem=546

f_k(0) = 1 and f_k(n) = sum_(i=0..n) f_k(floor(i/k)). Find
sum_(k=2..10) f_k(10^14) mod 10^9 + 7.

Differencing consecutive values telescopes the definition to
f(n) = f(n-1) + f(floor(n/k)). Define the iterated strict-prefix
sums T_0 = f and T_t(m) = sum_(q<m) T_(t-1)(q). Writing n = mk + s,

    f(n) = (s+1) f(m) + k T_1(m),

and summing such expressions over a full block of k children turns
each T_t(m) into T_(t+1)(m) while the partial block contributes
prefix sums over s < r: so every T_t(n) is a linear combination of
f(m), T_1(m), ..., T_(t+1)(m) with coefficients depending only on
the digit r = n mod k. The coefficient tables are built iteratively
(numeric mod p, per residue), and the vector (f, T_1, ..., T_D) is
propagated up the base-k digit chain of 10^14 from the base case
f(0) = 1, T_t(0) = 0, with D bounded by the chain length (at most 49
for k = 2) since each level references one more sum order.

Verified against the direct recurrence with exact integers for the
given f_5(10) = 18, f_7(100) = 1003, f_2(10^3) = 264830889564, and
for 30 random n <= 5000 for every k in 2..10.
"""

import random

MOD = 10**9 + 7


def f_direct(k: int, nmax: int) -> list[int]:
    f = [1] * (nmax + 1)
    for n in range(1, nmax + 1):
        f[n] = f[n - 1] + f[n // k]
    return f


def f_fast(k: int, n: int, mod: int = MOD) -> int:
    digits = []
    m = n
    while m > 0:
        digits.append(m % k)
        m //= k
    levels = len(digits)
    d = levels + 2
    # a[t][u][s]: coefficient of basis u (0 = f, t = T_t) in T_t(mk + s)
    a = [[[0] * k for _ in range(d + 2)] for _ in range(d + 1)]
    for s in range(k):
        a[0][0][s] = (s + 1) % mod
        a[0][1][s] = k % mod
    for t in range(1, d + 1):
        prev = a[t - 1]
        for u in range(d + 2):
            row = prev[u]
            full = sum(row) % mod
            if full and u + 1 <= d + 1:
                for s in range(k):
                    a[t][u + 1][s] = (a[t][u + 1][s] + full) % mod
            pref = 0
            for s in range(k):
                a[t][u][s] = (a[t][u][s] + pref) % mod
                pref = (pref + row[s]) % mod
    vec = [0] * (d + 2)
    vec[0] = 1  # values at argument 0
    for j in range(levels - 1, -1, -1):
        r = digits[j]
        vec = [
            sum(a[t][u][r] * vec[u] for u in range(d + 2)) % mod for t in range(d + 1)
        ] + [0]
    return vec[0]


if __name__ == "__main__":
    big = 10**30  # effectively exact for the small checks
    assert f_fast(5, 10, big) == 18 == f_direct(5, 10)[10]  # given
    assert f_fast(7, 100, big) == 1003 == f_direct(7, 100)[100]  # given
    assert f_fast(2, 1000, big) == 264830889564 == f_direct(2, 1000)[1000]  # given
    rng = random.Random(546)
    for k in range(2, 11):
        fd = f_direct(k, 5000)
        for n in rng.sample(range(1, 5001), 30):
            assert fd[n] % MOD == f_fast(k, n), (k, n)

    print(sum(f_fast(k, 10**14) for k in range(2, 11)) % MOD)  # 215656873
