import numba
import numpy as np

MOD = 10**9 + 7

@numba.njit(cache=True)
def g(n):
    """Colourings of an n x n grid with exactly two black cells per row
    and column, counted up to the dihedral group of the square, via
    Burnside: g = (Fix(id) + 2 Fix(r90) + Fix(r180) + 2 Fix(flip)
    + 2 Fix(transpose)) / 8.

    Each fixed-point count is holonomic with an O(n) recurrence derived
    from its EGF (all verified against exhaustive enumeration for
    n <= 6 and against the given g(4), g(7), g(8)):
    - Fix(id) = f(n): two-per-line matrices are unions of even cycles,
      EGF e^(-x/2)/sqrt(1-x) in x^n/(n!)^2, giving
      f(n+1) = n(n+1) f(n) + n^2 (n+1)/2 f(n-1).
    - Fix(transpose): symmetric matrices = graphs whose components are
      cycles (>= 3) and paths with loops at both ends; T(n) = n! c_n
      with (n+1) c_{n+1} = 2n c_n - (n-2) c_{n-1} - c_{n-3}/2.
    - Fix(r180): the quotient by the half-turn is a flavoured multigraph
      on m = n/2 classes; even n: (m!)^2 [x^m] e^(-x) (1-4x)^(-1/2),
      a_{j+1} = ((4j+1) a_j + 4 a_{j-1})/(j+1); odd n the middle row and
      column attach a marked path, m^2 ((m-1)!)^2 [x^(m-1)]
      2 e^(-x) (1-4x)^(-3/2) with m = (n-1)/2.
    - Fix(r90): quotient classes carry saturating loops or 2-flavoured
      edges; even n: m! [x^m] (1-2x)^(-1/2) e^(-x^2/2) with
      (j+1) k_{j+1} = (2j+1) k_j - k_{j-1} + 2 k_{j-2}; odd n: 0 by a
      degree-parity obstruction.
    - Fix(flip): every row uses a mirrored column pair, each pair by
      exactly two rows: n!/2^(n/2) for even n, 0 for odd n.
    """
    # modular inverses 1..n+2
    M = n + 9
    inv = np.empty(M, dtype=np.int64)
    inv[1] = 1
    for i in range(2, M):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i]) % MOD
    inv2 = inv[2]

    # f(n)
    f_prev, f_cur = 0, 1  # f(1), f(2)
    for k in range(2, n):
        nxt = (k * (k + 1) % MOD * f_cur + k * k % MOD * (k + 1) % MOD
               * inv2 % MOD * f_prev) % MOD
        f_prev, f_cur = f_cur, nxt
    f_n = f_cur if n >= 2 else 0

    # transpose: c_0..: c0=1, c1=0, c2=inv2, c3 = 2/3...
    c = np.zeros(4, dtype=np.int64)  # rolling window c[j%4]
    c[0] = 1
    c[1] = 0
    c[2] = inv2
    c[3] = 2 * inv[3] % MOD
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i % MOD
    if n <= 3:
        cn = c[n]
    else:
        for j in range(3, n):  # compute c_{j+1}
            cj = c[j % 4]
            cj1 = c[(j - 1) % 4]
            cj3 = c[(j - 3) % 4]
            val = (2 * j % MOD * cj - (j - 2) * cj1 - cj3 * inv2) % MOD
            c[(j + 1) % 4] = val * inv[j + 1] % MOD
        cn = c[n % 4]
    T_n = fact * cn % MOD

    if n % 2 == 1:
        # r180 odd: m^2 ((m-1)!)^2 h_{m-1}, h_0 = 2
        m = (n - 1) // 2
        h_prev, h_cur = 0, 2  # h_{-1}, h_0
        for j in range(0, m - 1):
            nxt = ((4 * j + 5) % MOD * h_cur + 4 * h_prev) % MOD
            nxt = nxt * inv[j + 1] % MOD
            h_prev, h_cur = h_cur, nxt
        fm1 = 1
        for i in range(1, m):
            fm1 = fm1 * i % MOD
        r180 = m % MOD * m % MOD * fm1 % MOD * fm1 % MOD * h_cur % MOD
        total = (f_n + r180 + 2 * T_n) % MOD
    else:
        m = n // 2
        # r180 even: (m!)^2 a_m
        a_prev, a_cur = 1, 1  # a_0, a_1
        for j in range(1, m):
            nxt = ((4 * j + 1) % MOD * a_cur + 4 * a_prev) % MOD
            nxt = nxt * inv[j + 1] % MOD
            a_prev, a_cur = a_cur, nxt
        fm = 1
        for i in range(1, m + 1):
            fm = fm * i % MOD
        r180 = fm * fm % MOD * (a_cur if m >= 1 else 1) % MOD
        # r90 even: m! k_m
        k0, k1, k2 = 1, 1, 1  # k_0, k_1, k_2
        if m <= 2:
            km = (k0, k1, k2)[m]
        else:
            for j in range(2, m):
                nxt = ((2 * j + 1) % MOD * k2 - k1 + 2 * k0) % MOD
                nxt = nxt * inv[j + 1] % MOD
                k0, k1, k2 = k1, k2, nxt
            km = k2
        r90 = fm * 0  # placeholder type
        r90 = (fm * km) % MOD
        # flip even: n!/2^(n/2)
        p2 = 1
        e = m
        base = inv2
        while e:
            if e & 1:
                p2 = p2 * base % MOD
            base = base * base % MOD
            e >>= 1
        flip = fact * p2 % MOD
        total = (f_n + 2 * r90 + r180 + 2 * flip + 2 * T_n) % MOD
    inv8 = inv[8]
    return total * inv8 % MOD

if __name__ == "__main__":
    assert g(4) == 20
    assert g(7) == 390816
    assert g(8) == 23462347
    assert (g(7) + g(8)) % MOD == 23853163
    print((g(7**7) + g(8**8)) % MOD)  # 512895223
