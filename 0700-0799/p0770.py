from decimal import Decimal, getcontext

LN2PI = Decimal("1.83787706640934548356065947281123527972766750048904")

def ln_gamma(z):
    """Stirling series; for z >= 10^8 the truncation error is < 10^-40."""
    z = Decimal(z)
    return (
        (z - Decimal(1) / 2) * z.ln()
        - z
        + LN2PI / 2
        + 1 / (12 * z)
        - 1 / (360 * z**3)
        + 1 / (1260 * z**5)
    )

def g(threshold_num, threshold_den):
    """Smallest n such that A can guarantee X = threshold_num/threshold_den.

    With t TAKEs and g GIVEs left, A's guaranteed multiplier V satisfies
    V(t, g) = harmonic mean of V(t-1, g) and V(t, g-1) (A displays the
    fraction equalising B's two options), with V(0, g) = 2^g, V(t, 0) = 1.
    The reciprocal U = 1/V averages, i.e. it is the expectation of the
    boundary value under a fair coordinate-decrementing walk; the g = 0
    boundary contributes exactly 1/2 (a fair race) and the t = 0 boundary
    telescopes by the hockey stick to C(2n-1, n)/4^n. Hence
        U(n, n) = 1/2 + C(2n-1, n) / 4^n,
    verified against the exact game DP for n <= 8 and giving g(1.7) = 10.

    So g(X) is the least n with C(2n-1, n)/4^n <= (2 - X)/(2X) - here
    1/39998 - found by binary search on the strictly decreasing left side,
    compared in 50-digit Stirling arithmetic (the gap between consecutive
    values, about 4e-9 relative, dwarfs the 1e-40 series error).
    """
    getcontext().prec = 50
    x = Decimal(threshold_num) / threshold_den
    log_theta = ((2 - x) / (2 * x)).ln()

    def ok(n):
        lhs = ln_gamma(2 * n) - ln_gamma(n + 1) - ln_gamma(n) - n * Decimal(4).ln()
        return lhs <= log_theta

    lo, hi = 1, 1
    while not ok(hi):
        lo, hi = hi, hi * 2
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

if __name__ == "__main__":
    assert g(17, 10) == 10
    print(g(19999, 10000))  # 127311223
