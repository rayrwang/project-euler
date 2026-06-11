"""Project Euler 962: Bisector and Tangent II.

Geometry. With a = BC <= b = AC <= c = AB and gamma the angle at C, the
tangent-chord angle gives angle(EBC) = alpha in triangle BCE, whose angle at
C is gamma/2, so the law of sines yields CE = a sin(alpha) / sin(alpha +
gamma/2). Since alpha + gamma/2 = pi/2 + (alpha - beta)/2 this simplifies
(checked against direct coordinate construction for random triangles) to

    CE = 2 a^2 cos(gamma/2) / (a + b),
    CE^2 = a^3 (a+b-c)(a+b+c) / (b (a+b)^2).

Reduction. Let g = gcd(a, b), a = g a', b = g b', sigma = a' + b'. Since
gcd(a', b' sigma^2) = 1, integrality of CE^2 forces b' sigma^2 | d P with
d = a+b-c, P = a+b+c. From sigma | d + P and sigma^2 | d P with the
coprime splitting of gcd(d, sigma) it follows that sigma | d, hence
sigma | c. Writing d = sigma delta, c = sigma x with x = g - delta, the
condition collapses (a1 = squarefree part of a') to

    g^2 - x^2 = a1 b' w^2,  w a positive integer,

with constraints g > x >= g b' / sigma (i.e. b <= c < a + b) and perimeter
sigma (g + x) <= 10^6. The bound chain delta >= 1, g + x <= 10^6/sigma,
delta <= (g+x) a'/(sigma + b') gives sigma^3 <= 2/3 * 10^12, so
sigma <= 10^4 and all coprime pairs (a', b') can be enumerated.

Counting. Put delta = g - x, p1 = g + x, so delta p1 = a1 b' w^2. With
b' = b1 n^2 (b1 squarefree), K0 = a1 b1 is squarefree, and the solutions
are exactly delta = s1 e u^2, p1 = t1 e v^2 over coprime splits
s1 t1 = K0, squarefree e coprime to K0, and u, v >= 1 with n | e u v
(this makes w = e u v / n integral) and delta == p1 (mod 2) (so that g, x
are integers). The representation is unique, so summing over
(sigma, a', s1, e, v) the count of admissible u (multiples of
n / gcd(n, e v) up to the box bound, filtered by parity) counts each
triangle exactly once. Verified against a direct integer brute force for
perimeter bounds up to 5000.
"""

import numpy as np
from numba import njit

PMAX = 10**6


def sf_table(limit: int) -> np.ndarray:
    """Squarefree part of every integer up to limit."""
    sf = np.arange(limit + 1, dtype=np.int64)
    for p in range(2, int(limit**0.5) + 1):
        p2 = p * p
        if sf[p2] != p2:
            continue
        for k in range(p2, limit + 1, p2):
            while sf[k] % p2 == 0:
                sf[k] //= p2
    return sf


@njit(cache=True)
def gcd64(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@njit(cache=True)
def isqrt64(n: int) -> int:
    if n <= 0:
        return 0
    x = int(np.sqrt(n))
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@njit(cache=True)
def count_all(pmax: int, sf: np.ndarray) -> int:
    sigma_max = min(int(round(pmax ** (2.0 / 3.0))) + 2, pmax // 3)
    total = 0
    divbuf = np.empty(256, dtype=np.int64)
    for sigma in range(2, sigma_max + 1):
        m_cap = pmax // sigma  # p1 <= m_cap
        if m_cap < 2:
            break
        for ap in range(1, sigma // 2 + 1):
            bp = sigma - ap
            if gcd64(ap, bp) != 1:
                continue
            a1 = sf[ap]
            b1 = sf[bp]
            k0 = a1 * b1  # squarefree
            n_b = isqrt64(bp // b1)
            sb = sigma + bp
            # all divisors of the squarefree k0
            nd = 1
            divbuf[0] = 1
            for part in (a1, b1):
                x = part
                f = 2
                while f * f <= x:
                    if x % f == 0:
                        x //= f
                        for i in range(nd):
                            divbuf[nd + i] = divbuf[i] * f
                        nd *= 2
                    f += 1
                if x > 1:
                    for i in range(nd):
                        divbuf[nd + i] = divbuf[i] * x
                    nd *= 2
            for di in range(nd):
                s1 = divbuf[di]
                t1 = k0 // s1
                vmin = isqrt64((s1 * sb - 1) // (t1 * ap)) + 1
                emax = m_cap // (t1 * vmin * vmin)
                for e in range(1, emax + 1):
                    if sf[e] != e or gcd64(e, k0) != 1:
                        continue
                    vhi = isqrt64(m_cap // (t1 * e))
                    for v in range(vmin, vhi + 1):
                        p1 = t1 * e * v * v
                        umax = isqrt64(t1 * v * v * ap // (s1 * sb))
                        if umax == 0:
                            continue
                        np_ = n_b // gcd64(n_b, e * v)
                        jmax = umax // np_
                        if jmax == 0:
                            continue
                        if (s1 * e * np_) % 2 == 0:
                            cnt = jmax if p1 % 2 == 0 else 0
                        elif p1 % 2 == 1:
                            cnt = (jmax + 1) // 2
                        else:
                            cnt = jmax // 2
                        total += cnt
    return total


def solve() -> int:
    sf = sf_table(PMAX)
    assert count_all(2000, sf) == 2047  # brute-force checked
    assert count_all(5000, sf) == 7290  # brute-force checked
    return count_all(PMAX, sf)


if __name__ == "__main__":
    print(solve())  # 7259046
