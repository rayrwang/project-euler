import numba
import numpy as np

@numba.njit(cache=True)
def G(n):
    """Sum of g(m) for m <= n, with g(m) = sum_i (-1)^i gcd(m, i^2).

    Expanding gcd(m, i^2) = sum over d | m, d | i^2 of phi(d), the inner
    condition is c(d) | i with c(d) = prod p^ceil(e/2) over p^e || d, and
    c(d) | d | m. The alternating sum of (-1)^i over multiples of c(d) up
    to m vanishes when c(d) is odd and m is even, equals m / c(d) when
    c(d) is even, and for odd m everything cancels in pairs (i, m - i)
    leaving g(m) = -m. For even m = 2^a * u (u odd),
        g(m) = sum_{d | m, d even} phi(d) m / c(d) = V(a) W(u),
    where V(a) = sum_{b=1..a} 2^(a - 1 + floor(b/2)) collects the 2-part
    and W is multiplicative with
        W(p^e) = p^e + (p-1) sum_{f=1..e} p^(e + floor(f/2) - 1).
    """
    spf = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    v = np.zeros(64, dtype=np.int64)
    for a in range(1, 64):
        s = 0
        for b in range(1, a + 1):
            s += 1 << (a - 1 + b // 2)
        v[a] = s
    total = 0
    for m in range(1, n + 1, 2):
        total -= m
    for m in range(2, n + 1, 2):
        a = 0
        u = m
        while u % 2 == 0:
            u //= 2
            a += 1
        w = 1
        while u > 1:
            p = spf[u]
            e = 0
            while u % p == 0:
                u //= p
                e += 1
            pe = 1
            for _ in range(e):
                pe *= p
            term = pe
            for f in range(1, e + 1):
                pf = 1
                for _ in range(e + f // 2 - 1):
                    pf *= p
                term += (p - 1) * pf
            w *= term
        total += v[a] * w
    return total

if __name__ == "__main__":
    assert G(1234) == 2194708
    print(G(12345678))  # 955892601606483
