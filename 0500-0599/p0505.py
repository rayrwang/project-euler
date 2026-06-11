import numba

# y_n(k) = x(k) for k >= n, else 2^60 - 1 - max(y_n(2k), y_n(2k+1)).
# Since M - max(a, b) = min(M - a, M - b), this is a negamax game tree with
# "negation" = complement w.r.t. M, so alpha-beta pruning applies.  The leaf
# values x(k) behave like iid uniform numbers, so pruning visits roughly
# O(n^0.56) of the 2n - 1 nodes.  x(2k) and x(2k+1) depend only on x(k) and
# x(floor(k/2)), so the pair (x(k), x(floor(k/2))) is carried down the tree.

M = (1 << 60) - 1
MOD = 1 << 60


@numba.jit("int64(int64, int64, int64, int64, int64, int64)", cache=True)
def ab(k: int, xk: int, xk2: int, alpha: int, beta: int, n: int) -> int:
    """Fail-soft y_n(k), exact whenever alpha < y_n(k) < beta."""
    if k >= n:
        return xk
    xl = (3 * xk + 2 * xk2) % MOD
    xr = (2 * xk + 3 * xk2) % MOD
    # y(k) = M - m with m = max(children); y in (alpha, beta) <=> m in (lo, hi)
    lo = M - beta
    hi = M - alpha
    m = ab(2 * k, xl, xk, lo, hi, n)
    if m < hi:
        m2 = ab(2 * k + 1, xr, xk, max(lo, m), hi, n)
        if m2 > m:
            m = m2
    return M - m


def a(n: int) -> int:
    return ab(1, 1, 0, -1, M + 1, n)


if __name__ == "__main__":
    assert a(4) == 8
    assert a(10) == 2**60 - 34
    assert a(10**3) == 101881
    print(a(10**12))  # 714591308667615832
