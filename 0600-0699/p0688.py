"""Project Euler Problem 688: Piles of Plates.

With smallest pile m, the cheapest k distinct piles are m, m+1, ..., m+k-1,
totalling k m + T_k where T_k = k(k-1)/2.  So f(n, k) is the largest m with
k m + T_k <= n, i.e. floor((n - T_k) / k), clipped at 0.

Swapping the summation order, with M = N - T_k,

    S(N) = sum_k sum_{n=1}^{N} f(n, k) = sum_k sum_{j=1}^{M} floor(j / k),

and the inner sum has the closed form k q(q-1)/2 + q (r + 1) with
q = floor(M / k), r = M - q k.  Only k with T_k + k <= N contribute, about
1.4 * 10^8 terms for N = 10^16; a numba loop evaluates them modulo
10^9 + 7 (every factor is reduced below the modulus first, so all products
fit in 64 bits).

Verified: f(10, 3) = 2, f(10, 5) = 0, F(100) = 275, S(100) = 12656, and
S against brute force for N <= 2000.
"""

import numba

MOD = 10**9 + 7
INV2 = (MOD + 1) // 2


def f(n: int, k: int) -> int:
    m = (n - k * (k - 1) // 2) // k
    return max(m, 0)


@numba.jit(cache=True)
def s(n: int, mod: int, inv2: int) -> int:
    total = 0
    k = 1
    while k * (k + 1) // 2 <= n:
        m = n - k * (k - 1) // 2
        q, r = divmod(m, k)
        qm = q % mod
        total += k % mod * (qm * (qm - 1) % mod) % mod * inv2 % mod
        total += qm * ((r + 1) % mod) % mod
        total %= mod
        k += 1
    return total


def s_brute(n: int) -> int:
    return sum(f(m, k) for m in range(1, n + 1) for k in range(1, m + 1))


if __name__ == "__main__":
    assert f(10, 3) == 2 and f(10, 5) == 0
    assert sum(f(100, k) for k in range(1, 101)) == 275  # F(100)
    assert s_brute(100) == 12656
    assert all(int(s(n, MOD, INV2)) == s_brute(n) for n in (1, 2, 100, 2000))
    print(int(s(10**16, MOD, INV2)))  # 110941813
