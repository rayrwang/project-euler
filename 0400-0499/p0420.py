import numba

from funcs import divisor_count_sieve, gcd

@numba.jit(cache=True)
def two_root_matrices(n: int) -> int:
    """F(N): 2x2 positive integer matrices with trace < N that are squares
    of positive integer matrices in two different ways.

    Let M = A^2 = B^2 with traces t = tr(A), t' = tr(B). Equal traces force
    A = B, so t != t'; write g = gcd(t, t'), t = gT, t' = gT'. Matching the
    entries of A^2 and B^2 forces b = T' b0, c = T' c0, a - e = T' d (and
    the primed versions with T), and equal traces of M reduce to
        g^2 - d^2 = 4 b0 c0,    tr M = g^2 (T^2 + T'^2) / 2.
    Conversely every tuple (T > T', g, d, b0, c0) with gcd(T, T') = 1,
    d = g (mod 2) (T, T' both odd when g is odd, for integrality of the
    matrix entries), |d| <= (gT' - 2)/T (positivity of B's diagonal; A's is
    implied), and 4 b0 c0 = g^2 - d^2 yields exactly one such M, and M has
    exactly these two positive roots. So F(N) sums the divisor count of
    (g^2 - d^2)/4 over the admissible (T, T', g, d).
    """
    # largest (g^2 - d^2)/4 is below g^2/4 <= 2N / (4 (T^2+T'^2)) <= N/10
    divc = divisor_count_sieve(n // 10 + 1)
    total = 0
    tt = 1  # T'
    while True:
        if 2 * (tt + 1) ** 2 + 2 * tt**2 > 2 * n:  # no g >= 2 fits any T > T'
            break
        t = tt + 1
        while 4 * (t * t + tt * tt) < 2 * n:  # g = 2 must fit
            if gcd(t, tt) == 1:
                g = 2
                while g * g * (t * t + tt * tt) < 2 * n:
                    if g % 2 == 1 and (t % 2 == 0 or tt % 2 == 0):
                        g += 1
                        continue
                    dmax = (g * tt - 2) // t
                    if dmax > g - 2:
                        dmax = g - 2
                    d = -dmax
                    # align d to the parity of g
                    if (d - g) % 2 != 0:
                        d += 1
                    while d <= dmax:
                        total += divc[(g * g - d * d) // 4]
                        d += 2
                    g += 1
            t += 1
        tt += 1
    return total

def brute(n: int) -> int:
    from collections import Counter
    roots: Counter[tuple[int, int, int, int]] = Counter()
    bound = n  # generous: tr(M) = a^2 + e^2 + 2bc < n bounds all entries
    for a in range(1, n):
        if a * a + 1 + 2 >= n:
            break
        for e in range(1, n):
            if a * a + e * e + 2 >= n:
                break
            rest = n - a * a - e * e
            for b in range(1, bound):
                if 2 * b >= rest:
                    break
                for c in range(1, bound):
                    if a * a + e * e + 2 * b * c >= n:
                        break
                    m = (a * a + b * c, b * (a + e), c * (a + e), e * e + b * c)
                    roots[m] += 1
    return sum(1 for v in roots.values() if v >= 2)

if __name__ == "__main__":
    assert two_root_matrices(50) == brute(50) == 7
    assert two_root_matrices(1000) == 1019
    print(two_root_matrices(10**7))  # 145159332
