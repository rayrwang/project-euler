import numba
import numpy as np

MOD = 10**9 + 7
P = 6

@numba.njit(cache=True)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@numba.njit(cache=True)
def apery_sums(A, B, C):
    """Apery set of <A, B, C> modulo the smallest generator A, via the
    Boecker-Liptak round-robin algorithm. n[i] is the least semigroup element
    congruent to i (mod A). Returns (#gaps, sum of gaps) modulo MOD using
        #gaps  = sum_i n[i] // A,
        gap sum = sum_i ( (n[i]//A) * i + A * C(n[i]//A, 2) ).
    """
    m = A
    INF = np.int64(1) << 62
    n = np.full(m, INF, np.int64)
    n[0] = 0
    for a in (B, C):
        d = gcd(m, a)
        for r in range(d):
            vmin = INF
            qmin = -1
            i = r
            while i < m:
                if n[i] < vmin:
                    vmin = n[i]
                    qmin = i
                i += d
            if vmin >= INF:
                continue
            x = qmin
            val = n[x]
            for _ in range(m // d):
                x = (x + a) % m
                val += a
                if val < n[x]:
                    n[x] = val
                else:
                    val = n[x]
    inv2 = (MOD + 1) // 2
    genus = 0
    gapsum = 0
    Am = A % MOD
    for i in range(m):
        q = n[i] // m
        if q == 0:
            continue
        qm = q % MOD
        genus = (genus + qm) % MOD
        tri = (qm * ((q - 1) % MOD)) % MOD * inv2 % MOD  # C(q, 2) mod MOD
        gapsum = (gapsum + qm * (i % MOD) + Am * tri) % MOD
    return genus % MOD, gapsum % MOD

def solve(p):
    """Reachable n are exactly s + <A,B,C> with s = A+B+C, so the unreachable
    n>0 are {1,...,s-1} together with {s + g : g a gap}. Hence
        G(p) = s(s-1)/2 + s*(#gaps) + (sum of gaps)."""
    a, b, c = 17**p, 19**p, 23**p
    genus, gapsum = apery_sums(a, b, c)
    s = a + b + c
    sm = s % MOD
    first = s * (s - 1) // 2 % MOD
    return (first + sm * genus + gapsum) % MOD

if __name__ == "__main__":
    print(solve(P))  # 228579116
