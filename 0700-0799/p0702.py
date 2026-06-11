import numba

# Work in Eisenstein-like coordinates z = a + b*w with w = e^(i*pi/6*2) = e^(i*pi/3),
# so w^2 = w - 1.  The table is the hexagon {gauge(z) <= N} where
# gauge(a + b*w) = max(|a|, |b|, |a + b|), and the triangle grid is the unit
# triangular lattice.  After k jumps the flea sits at N*z / 2^k where z lies in
# M_k = {sum_{j=1..k} 2^(j-1) u_j : u_j a sixth root of unity}.  One can verify
# (BFS over jump sequences) that exactly
#     M_k = {z in Z[w] : z odd (z not in 2Z[w]), gauge(z) <= 2^k - 1},
# i.e. the odd lattice points of the hexagon of radius 2^k - 1.  Since every
# triangle interior lies strictly inside the table, the gauge constraint is
# automatic and J(T) is the least k such that 2^k * int(T) contains a point of
# N * (odd lattice).
#
# An upward unit triangle anchored at (a, b) has interior {(s, t) : s > a,
# t > b, s + t < a + b + 1}.  Writing x = (-a) mod N, y = (-b) mod N and
# V_k(x) = 2^k x mod N (taking N when the residue is 0), the divisibility
# analysis collapses to
#     J = min k >= 1 with V_k(x) + V_k(y) + N*[both V_k even] < 2^k.
# Summing J over the problem's domain (upward triangles in the upper half)
# gives, after folding the a-range onto residues,
#     S(N) = sum over (x, y) in [0, N)^2 of w(x, y) * J(x, y),
# where w = 1 + [x = 0] + [x >= 1 and ((y >= 1 and x + y > N) or y = 0)].
#
# Let m = bitlength(N) (so 2^(m-1) < N < 2^m, N odd).  For levels j <= m - 1
# the penalty N is unpayable, so the pairs hit at level j are parametrised by
# u = V_j(x), v = V_j(y) with u, v >= 1, u + v < 2^j, not both even, and these
# level sets are pairwise disjoint (an earlier hit forces a both-even pair,
# hence an unpayable penalty, at every later level below m).  The companion
# weight [x + y > N] equals the carry bit of g(u) + g(v) where
# g(t) = ((-N)^(-1) t) mod 2^j, which the identity
#     [carry] = (g(u) + g(v) - g(u + v)) / 2^j
# turns into prefix sums - O(2^j) work per level.  Every level-j pair is hit
# again at level m except a corner region (both wraps zero and
# 2^(m-j)(u+v) + N >= 2^m), counted the same way (CF below; CF2 is the part
# of the corner that also fails level m + 1).  At the top, V = V_m(x) and
# W = V_m(y) range bijectively over [1, N-1]; B1 counts (with weights) the
# pairs hit at level m and A2a those failing both m and m + 1 - here the
# weight carry uses G(t) = (2^(-m) t) mod N, and the diagonal V + W = N
# (i.e. x + y = N exactly, which the carry identity counts but the weight
# excludes) is subtracted.  Everything assembles into first-hit weights
# hw_j and S in O(N + 2^m) time.  J(x, 0), J(0, y) are handled in closed
# form (they are always m or m + 1).
#
# Verified against a direct flea BFS for N <= 11, against the O(N^2 log N)
# per-pair formula for hundreds of odd N up to 20001, and against all four
# values given in the problem statement.


@numba.njit(cache=True)
def mod_inverse(a, mod):
    """Inverse of a modulo mod via the extended Euclidean algorithm."""
    t, newt = 0, 1
    r, newr = mod, a % mod
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if t < 0:
        t += mod
    return t


@numba.njit(cache=True)
def region_weight(U, L, M, gam):
    """Sum of (1 + carry) over {u, v in [1, U], u + v in [max(L, 2), M - 1],
    not both even}, carry = (g(u) + g(v) - g(u+v)) / M with g(t) = gam*t mod M."""
    lo_s = L if L > 2 else 2
    hi_s = 2 * U if 2 * U < M - 1 else M - 1
    total = 0
    wl, wr = 1, 0  # current window [wl, wr] of u values, empty initially
    sum_all = 0
    sum_odd = 0
    cnt_all = 0
    cnt_odd = 0
    for sigma in range(lo_s, hi_s + 1):
        nl = sigma - U
        if nl < 1:
            nl = 1
        nr = U if U < sigma - 1 else sigma - 1
        while wr < nr:
            wr += 1
            g = (gam * wr) % M
            sum_all += g
            cnt_all += 1
            if wr & 1:
                sum_odd += g
                cnt_odd += 1
        while wl < nl:
            g = (gam * wl) % M
            sum_all -= g
            cnt_all -= 1
            if wl & 1:
                sum_odd -= g
                cnt_odd -= 1
            wl += 1
        gs = (gam * sigma) % M
        if sigma & 1:
            cnt, ssum = cnt_all, sum_all
        else:
            cnt, ssum = cnt_odd, sum_odd
        total += cnt + (2 * ssum - cnt * gs) // M
    return total


@numba.njit(cache=True)
def top_b1(N, TWOm, delta):
    """Weighted count of pairs hit at level m: (V, W) in [1, N-1]^2 with
    (not both even and V + W <= 2^m - 1) or (both even and V + W <= 2^m - 1 - N),
    weight 1 + [x + y > N] where x = delta*V mod N, y = delta*W mod N."""
    total = 0
    cap2 = TWOm - 1 - N
    hi_s = TWOm - 1  # < 2N - 1 since 2^m < 2N
    wl, wr = 1, 0
    sum_all = 0
    sum_odd = 0
    sum_even = 0
    cnt_all = 0
    cnt_odd = 0
    for sigma in range(2, hi_s + 1):
        nl = sigma - (N - 1)
        if nl < 1:
            nl = 1
        nr = N - 1 if N - 1 < sigma - 1 else sigma - 1
        while wr < nr:
            wr += 1
            g = (delta * wr) % N
            sum_all += g
            cnt_all += 1
            if wr & 1:
                sum_odd += g
                cnt_odd += 1
            else:
                sum_even += g
        while wl < nl:
            g = (delta * wl) % N
            sum_all -= g
            cnt_all -= 1
            if wl & 1:
                sum_odd -= g
                cnt_odd -= 1
            else:
                sum_even -= g
            wl += 1
        gs = (delta * sigma) % N
        if sigma & 1:
            cnt, ssum = cnt_all, sum_all
        else:
            cnt, ssum = cnt_odd, sum_odd
        total += cnt + (2 * ssum - cnt * gs) // N
        if (sigma & 1) == 0 and sigma <= cap2:
            cnt = cnt_all - cnt_odd
            total += cnt + (2 * sum_even - cnt * gs) // N
    # The carry identity counts x + y >= N; the diagonal V + W = N means
    # x + y = N exactly (excluded by the weight), and its N - 1 pairs always
    # lie in the not-both-even branch since N is odd.
    return total - (N - 1)


@numba.njit(cache=True)
def top_a2a(N, TWOm, delta):
    """Weighted count over {V, W even in [2, (N-1)/2], V + W >= 2^m - (N-1)/2}:
    pairs failing both level m and level m + 1 (before corner corrections)."""
    h = (N - 1) // 2
    veff = h if h % 2 == 0 else h - 1
    lo_s = TWOm - h
    if lo_s < 4:
        lo_s = 4
    if lo_s % 2 == 1:
        lo_s += 1
    hi_s = 2 * veff
    total = 0
    wl, wr = 2, 0
    sum_even = 0
    cnt_even = 0
    for sigma in range(lo_s, hi_s + 1, 2):
        nl = sigma - veff
        if nl < 2:
            nl = 2
        nr = veff if veff < sigma - 2 else sigma - 2
        while wr < nr:
            wr += 2
            g = (delta * wr) % N
            sum_even += g
            cnt_even += 1
        while wl < nl:
            g = (delta * wl) % N
            sum_even -= g
            cnt_even -= 1
            wl += 2
        gs = (delta * sigma) % N
        total += cnt_even + (2 * sum_even - cnt_even * gs) // N
    return total


@numba.njit(cache=True)
def fast_s(N):
    """S(N) for odd N in O(N + 2^m) time, m = bitlength(N)."""
    m = 0
    while (1 << m) <= N:
        m += 1
    TWOm = 1 << m

    # Boundary lines x = 0 and y = 0 (weight 2 each): J is m or m + 1 there.
    col0 = m * (TWOm - N - 1) + (m + 1) * (2 * N + 1 - TWOm)
    boundary = 2 * col0 + 2 * (col0 - (m + 1))

    s_levels = 0  # sum over j <= m - 1 of j * hw_j
    hw_low = 0  # sum of hw_j
    cf = 0  # corner pairs hit at level j but not at level m
    cf2 = 0  # corner pairs hit at level j, failing levels m and m + 1
    neg_n = -N
    inv = 1  # inverse of -N mod 2^j, lifted level by level
    for j in range(1, m):
        M = 1 << j
        inv = (inv * (2 - neg_n * inv)) % M
        gam = inv
        # weight of level-j hits: u, v >= 1, u + v <= M - 1, not both even
        t1 = (M - 1) * (M - 2) // 2 - (M // 2 - 1) * (M // 2 - 2) // 2
        t2 = 0
        pref_all = 0
        pref_odd = 0
        for sigma in range(2, M):
            u = sigma - 1
            gu = (gam * u) % M
            pref_all += gu
            if u & 1:
                pref_odd += gu
            gs = (gam * sigma) % M
            if sigma & 1:
                cnt, ssum = sigma - 1, pref_all
            else:
                cnt, ssum = sigma // 2, pref_odd
            t2 += (2 * ssum - cnt * gs) // M
        hw = t1 + t2
        hw_low += hw
        s_levels += j * hw

        sh = m - j
        U = N >> sh
        L = ((TWOm - N) >> sh) + 1
        if 2 * U >= L and U >= 1:
            cf += region_weight(U, L, M, gam)
        sh2 = m + 1 - j
        U2 = N >> sh2
        L2 = (((TWOm << 1) - N) >> sh2) + 1
        if 2 * U2 >= L2 and U2 >= 1:
            cf2 += region_weight(U2, L2, M, gam)

    delta = mod_inverse(TWOm % N, N)
    b1 = top_b1(N, TWOm, delta)
    a2a = top_a2a(N, TWOm, delta)

    w_tot = (N - 1) * (N - 1) + (N - 2) * (N - 1) // 2
    hw_m = b1 - hw_low + cf
    a2 = a2a - cf2
    hw_m1 = (w_tot - b1 - cf) - a2
    s_pairs = s_levels + m * hw_m + (m + 1) * hw_m1 + (m + 2) * a2
    return boundary + s_pairs


if __name__ == "__main__":
    assert fast_s(3) == 42
    assert fast_s(5) == 126
    assert fast_s(123) == 167178
    assert fast_s(12345) == 3185041956

    print(fast_s(123456789))  # 622305608172525546
