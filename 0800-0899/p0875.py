import numba
import numpy as np

# Writing r4(k) for the number of quadruples with sum of squares k mod n,
# q(n) = sum_k r4(k)^2, and Parseval over the additive characters turns this
# into q(n) = (1/n) sum_t |G(t, n)|^8 with G the quadratic Gauss sum
# G(t, n) = sum_a e(t a^2 / n).  Hence q is multiplicative, and the classical
# magnitudes |G(u, p^m)| = p^(m/2) for odd p, and 0, 2^((m+1)/2) for p = 2,
# m = 1, m >= 2 (u a unit), give closed forms over t = p^j u:
#     q(p^e) = (1 - 1/p) p^(4e) (p^(3e) - 1)/(p^3 - 1) + p^(7e)   (p odd),
#     q(2^e) = 2^(4e + 3) (2^(3e - 3) - 1)/7 + 2^(7e),
# both verified against direct counting below (and q(4) = 18432 as given).
# Q(N) then follows from a linear pass extending q multiplicatively over a
# smallest-prime-factor sieve; prime-power values are computed as exact
# integers before reduction, sidestepping modular inverses entirely.

MOD = 1001961001
N = 12345678


def q_pp(p: int, e: int) -> int:
    if p == 2:
        return (1 << (4 * e + 3)) * ((1 << (3 * e - 3)) - 1) // 7 + (1 << (7 * e))
    return (p - 1) * p ** (4 * e - 1) * (p ** (3 * e) - 1) // (p**3 - 1) + p ** (7 * e)


def q_brute(n: int) -> int:
    counts = [0] * n
    for a in range(n):
        counts[a * a % n] += 1
    cur = [1] + [0] * (n - 1)
    for _ in range(4):
        nxt = [0] * n
        for i, v in enumerate(cur):
            if v:
                for j, w in enumerate(counts):
                    nxt[(i + j) % n] += v * w
        cur = nxt
    return sum(v * v for v in cur)


def q_mult(n: int) -> int:
    res = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            res *= q_pp(p, e)
        p += 1
    if n > 1:
        res *= q_pp(n, 1)
    return res


@numba.njit(cache=True)
def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def big_q(n, spf, qpp, mod):
    qv = np.empty(n + 1, dtype=np.int64)
    qv[1] = 1
    s = np.int64(1)
    for x in range(2, n + 1):
        p = spf[x]
        pe = np.int64(p)
        m = x // p
        while m % p == 0:
            pe *= p
            m //= p
        qv[x] = qv[m] * qpp[pe] % mod
        s = (s + qv[x]) % mod
    return s


if __name__ == "__main__":
    assert q_brute(4) == q_mult(4) == 18432  # given
    assert all(q_mult(n) == q_brute(n) for n in range(2, 31))
    assert sum(q_mult(n) for n in range(1, 11)) == 18573381  # given Q(10)

    spf = spf_sieve(N)
    qpp = np.zeros(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if spf[p] == p:
            pe, e = p, 1
            while pe <= N:
                qpp[pe] = q_pp(p, e) % MOD
                pe *= p
                e += 1
    assert big_q(10, spf, qpp, MOD) == 18573381 % MOD
    print(big_q(N, spf, qpp, MOD))  # 79645946
