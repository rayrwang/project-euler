import numba

# With a = BC, b = AC, c = AB and the tangent-chord angle, the line n
# through B makes angle BAC with BC, and the sine rule in triangle BCE
# collapses to BE = a c / (a + b) - verified by explicit coordinate
# construction of E for several triangles. So BE is integral iff
# (a + b) | a c, i.e. s' | c with s' = (a + b)/gcd(a, b). Writing a = g a',
# b = g b' (coprime, a' <= b' so b' >= s'/2), c = k s', the constraints
# c >= b and c < a + b become g b' <= k s' and k < g, and the perimeter is
# (g + k) s' <= N. For fixed (s', b') the (g, k) count is
#     sum over g of [min(g - 1, T - g) - ceil(g b'/s') + 1]^+,  T = N/s',
# evaluated in O(log) by Euclidean floor sums (splitting at g = (T+1)/2,
# with a binary search for where the second region empties). The count is
# non-increasing in b', so the coprime b' loop breaks at the first zero.
# Verified against direct triple enumeration for N = 100, 500, 2000.


@numba.njit(cache=True)
def _floor_sum(n: int, m: int, a: int, b: int) -> int:
    ans = 0
    while True:
        if a >= m:
            ans += (n - 1) * n // 2 * (a // m)
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y_max = a * n + b
        if y_max < m:
            return ans
        n = y_max // m
        b = y_max % m
        m, a = a, m


@numba.njit(cache=True)
def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@numba.njit(cache=True)
def _count_pairs(sp: int, bp: int, t: int) -> int:
    g1 = (t + 1) // 2
    if g1 > t - 1:
        g1 = t - 1
    total = 0
    if g1 >= 2:
        sum_g = g1 * (g1 + 1) // 2 - 1
        ce = _floor_sum(g1 + 1, sp, bp, sp - 1) - _floor_sum(2, sp, bp, sp - 1)
        total += sum_g - ce
    lo, hi = g1 + 1, t - 1
    g2 = g1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid + (mid * bp + sp - 1) // sp <= t:
            g2 = mid
            lo = mid + 1
        else:
            hi = mid - 1
    if g2 >= g1 + 1:
        n_terms = g2 - g1
        sum_tg = n_terms * (t + 1) - (g2 * (g2 + 1) // 2 - g1 * (g1 + 1) // 2)
        ce = _floor_sum(g2 + 1, sp, bp, sp - 1) - _floor_sum(g1 + 1, sp, bp, sp - 1)
        total += sum_tg - ce
    return total


@numba.njit(cache=True)
def _solve(n: int) -> int:
    cnt = 0
    for sp in range(2, n // 3 + 1):
        t = n // sp
        if t < 3:
            break
        for bp in range((sp + 1) // 2, sp):
            if _gcd(bp, sp) != 1:
                continue
            c = _count_pairs(sp, bp, t)
            if c == 0:
                break
            cnt += c
    return cnt


def solve(n: int = 100000) -> int:
    return int(_solve(n))


if __name__ == "__main__":
    print(solve())  # 1137208419
