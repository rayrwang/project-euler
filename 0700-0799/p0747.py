import numba

MOD = 10**9 + 7

@numba.njit(cache=True)
def isqrt64(x):
    r = int(x**0.5)
    while r * r > x:
        r -= 1
    while (r + 1) * (r + 1) <= x:
        r += 1
    return r

@numba.njit(cache=True)
def chord_sum(m):
    """Generic-chord contribution to Psi(m).

    A cutting is a set of n rays from interior P; each piece is bounded by
    two rays plus a boundary arc, so it is a triangle iff the arc is a
    single segment (a fan piece with apex P) or the arc passes one corner
    while the two rays are collinear (a chord through P slicing the corner
    off as a triangle without P as a vertex). Two collinear pairs would
    exhaust the full angle, so a cutting has at most one chord piece.

    No chord: rays to all three corners split the pizza into three fans of
    k1, k2, k3 >= 1 pieces; P is the unique barycentric point, giving
    C(n-1, 2) cuttings. Chord with one endpoint at a corner: the position
    of P on the chord is determined and always valid, giving 6(n-2).
    Generic chord cutting corner C at e1 = (alpha) along CA and
    e2 = (1/(n alpha)) along CB, with fan counts m1, m2, m3 over e1A, AB,
    B e2: eliminating everything leaves the quadratic
        n(m1+1) a^2 - (m1+m3+n+1) a + (m3+1) = 0
    on the validity interval ((m3+1)/n, 1/(m1+1)) -- at both of whose
    endpoints the quadratic is positive (values m1 m3 (m3+1)/n and
    m1 m3/(m1+1)), so valid roots come in pairs. With s = m1+m3 and
    q = (m1+1)(m3+1), the discriminant-plus-vertex condition collapses to
        n > n_plus = 2q - s - 1 + 2 sqrt(q m1 m3),
    with a single tangency root exactly at integer n = n_plus. Summing
    over n <= m swaps to a pair loop: each (m1, m3) contributes
    2 (m - floor(n_plus)) plus 1 if n_plus is an integer <= m.
    """
    total = 0
    m1 = 1
    while 3 * m1 + 2 <= m:  # base value at m3 = 1
        for m3 in range(1, m + 1):
            q = (m1 + 1) * (m3 + 1)
            s = m1 + m3
            base = 2 * q - s - 1
            if base >= m:
                break
            x4 = 4 * q * m1 * m3
            r = isqrt64(x4)
            fl = base + r
            if r * r == x4:
                if fl <= m:
                    total += 2 * (m - fl) + 1
            elif fl < m:
                total += 2 * (m - fl)
        m1 += 1
    return total

def Psi(m):
    base = m * (m - 1) * (m - 2) // 6  # no-chord cuttings: sum of C(n-1,2)
    base += 3 * (m - 2) * (m - 1)  # corner-endpoint chords: sum of 6(n-2)
    base += 3 * chord_sum(m)  # 3 corners for the generic chord
    return base % MOD

if __name__ == "__main__":
    assert Psi(3) == 7  # psi(3)
    assert Psi(6) - Psi(5) == 34  # psi(6)
    assert Psi(10) - Psi(9) == 90  # psi(10)
    assert Psi(10) == 345
    assert Psi(1000) == 172166601
    print(Psi(10**8))  # 681813395
