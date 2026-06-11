from itertools import product
from math import comb, gcd

MOD = 10**9
BIGMOD = 13824 * MOD  # 24^3 * 10^9: enough headroom for exact /24^j

def m_value(a: int, b: int, c: int) -> int:
    """M(a,b,c) = gcd of n^4+an^3+bn^2+cn over all integers n.

    By Newton's basis every value is an integer combination of
    f(0),...,f(4) and vice versa, so the gcd of those five values (f(0)
    vanishes) is the full gcd; it divides the fourth difference 24.
    """
    vals = [n**4 + a * n**3 + b * n**2 + c * n for n in (1, 2, 3, 4)]
    g = 0
    for v in vals:
        g = gcd(g, v)
    return g

def build_tables():
    """E0 and the t-indexed coefficients of S(24q + t) =
    E0 q^3 + E1(t) q^2 + E2(t) q + E3(t)."""
    m24 = {}
    for ra, rb, rc in product(range(24), repeat=3):
        m24[(ra, rb, rc)] = m_value(ra, rb, rc)
    e0 = sum(m24.values())
    e1 = [0] * 24
    e2 = [0] * 24
    e3 = [0] * 24
    for t in range(24):
        # residue class r in 1..24 gets count q + 1 iff r <= t
        def ind(r: int) -> int:
            rr = r if r else 24  # residue 0 represents class 24
            return 1 if rr <= t else 0
        for (ra, rb, rc), m in m24.items():
            i1, i2, i3 = ind(ra), ind(rb), ind(rc)
            e1[t] += m * (i1 + i2 + i3)
            e2[t] += m * (i1 * i2 + i1 * i3 + i2 * i3)
            e3[t] += m * (i1 * i2 * i3)
    return e0, e1, e2, e3

def s_of(n: int, tables) -> int:
    e0, e1, e2, e3 = tables
    q, t = divmod(n, 24)
    return e0 * q**3 + e1[t] * q**2 + e2[t] * q + e3[t]

def fib_pair(k: int, mod: int) -> tuple[int, int]:
    """(F_k, F_{k+1}) mod `mod` by fast doubling."""
    if k == 0:
        return 0, 1
    f, g = fib_pair(k >> 1, mod)
    a = f * (2 * g - f) % mod
    b = (f * f + g * g) % mod
    if k & 1:
        return b, (a + b) % mod
    return a, b

def step_matrix(jump: int, mod: int) -> list[list[int]]:
    """Linear map on the 14-vector
    [F^3, F^2 G, F G^2, G^3, F^2, F G, G^2, F, G, 1, S3, S2, S1, S0]
    (with (F, G) = (F_k, F_{k+1})) that adds the current F-powers to the
    accumulators S_e and advances k by `jump`."""
    fj, fj1 = fib_pair(jump, mod)
    fjm1 = (fj1 - fj) % mod
    # F' = fjm1*F + fj*G ; G' = fj*F + fj1*G
    p, q, r, s = fjm1, fj, fj, fj1
    mat = [[0] * 14 for _ in range(14)]
    # degree 3 monomials: (pF+qG)^i (rF+sG)^(3-i) expansions
    deg3 = [(3, 0), (2, 1), (1, 2), (0, 3)]
    for row, (i, _) in enumerate(deg3):
        # (pF+qG)^i (rF+sG)^j -> coefficients on F^a G^(3-a)
        coef = [0, 0, 0, 0]
        for u in range(i + 1):
            for v in range(3 - i + 1):
                cc = (comb(i, u) * pow(p, u, mod) * pow(q, i - u, mod)
                      * comb(3 - i, v) * pow(r, v, mod)
                      * pow(s, 3 - i - v, mod)) % mod
                coef[3 - (u + v)] = (coef[3 - (u + v)] + cc) % mod
        for col in range(4):
            mat[row][col] = coef[col]
    deg2 = [(2, 0), (1, 1), (0, 2)]
    for row, (i, _) in enumerate(deg2, start=4):
        coef = [0, 0, 0]
        for u in range(i + 1):
            for v in range(2 - i + 1):
                cc = (comb(i, u) * pow(p, u, mod) * pow(q, i - u, mod)
                      * comb(2 - i, v) * pow(r, v, mod)
                      * pow(s, 2 - i - v, mod)) % mod
                coef[2 - (u + v)] = (coef[2 - (u + v)] + cc) % mod
        for col in range(3):
            mat[row][4 + col] = coef[col]
    mat[7][7], mat[7][8] = p, q
    mat[8][7], mat[8][8] = r, s
    mat[9][9] = 1
    # accumulators: S3 += F^3, S2 += F^2, S1 += F, S0 += 1 (pre-step)
    mat[10][0] = 1
    mat[10][10] = 1
    mat[11][4] = 1
    mat[11][11] = 1
    mat[12][7] = 1
    mat[12][12] = 1
    mat[13][9] = 1
    mat[13][13] = 1
    return mat

def mat_mul(a, b, mod):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) % mod
             for j in range(n)] for i in range(n)]

def mat_vec(a, v, mod):
    n = len(a)
    return [sum(a[i][k] * v[k] for k in range(n)) % mod for i in range(n)]

def class_power_sums(k0: int, count: int, mod: int) -> list[int]:
    """[S3, S2, S1, S0] = sums of F_k^e over k = k0, k0+24, ...,
    count terms, mod `mod`."""
    f, g = fib_pair(k0, mod)
    v = [f**3 % mod, f * f * g % mod, f * g * g % mod, g**3 % mod,
         f * f % mod, f * g % mod, g * g % mod, f, g, 1, 0, 0, 0, 0]
    t = step_matrix(24, mod)
    c = count
    while c:
        if c & 1:
            v = mat_vec(t, v, mod)
        t = mat_mul(t, t, mod)
        c >>= 1
    return v[10:14]

def total(kmax: int, tables) -> int:
    """sum of S(F_k) for 2 <= k <= kmax, mod 10^9."""
    e0, e1, e2, e3 = tables
    result = 0
    for s in range(24):
        k0 = s if s >= 2 else s + 24
        if k0 > kmax:
            continue
        count = (kmax - k0) // 24 + 1
        t = fib_pair(k0, 24)[0]  # F_k mod 24, constant on the class
        s3, s2, s1, s0 = class_power_sums(k0, count, BIGMOD)
        # sum (F - t)^j, exact-divide by 24^j
        n3 = (s3 - 3 * t * s2 + 3 * t * t * s1 - t**3 * s0) % BIGMOD
        q3 = (n3 // 13824) % MOD if n3 % 13824 == 0 else None
        n2 = (s2 - 2 * t * s1 + t * t * s0) % (576 * MOD)
        q2 = n2 // 576
        n1 = (s1 - t * s0) % (24 * MOD)
        q1 = n1 // 24
        assert q3 is not None and n2 % 576 == 0 and n1 % 24 == 0
        result += (e0 * q3 + e1[t] * q2 + e2[t] * q1
                   + e3[t] * (s0 % MOD)) % MOD
    return result % MOD

if __name__ == "__main__":
    assert m_value(4, 2, 5) == 6  # given
    # brute-check M against a gcd over many n, including negatives
    for a, b, c in product(range(1, 7), repeat=3):
        g = 0
        for n in range(-8, 9):
            g = gcd(g, n**4 + a * n**3 + b * n**2 + c * n)
        assert g == m_value(a, b, c)
    tables = build_tables()
    def s_brute(n):
        return sum(m_value(a, b, c) for a, b, c
                   in product(range(1, n + 1), repeat=3))
    assert s_of(10, tables) == s_brute(10) == 1972  # given
    assert s_of(33, tables) == s_brute(33)
    assert s_of(10000, tables) == 2024258331114  # given
    # validate the class machinery on a small range against direct sums
    fibs = [0, 1]
    while len(fibs) < 60:
        fibs.append(fibs[-1] + fibs[-2])
    direct = sum(s_of(fibs[k], tables) for k in range(2, 51)) % MOD
    assert total(50, tables) == direct
    print(total(1234567890123, tables))  # 356019862
