from math import lgamma, log, sqrt

# X_n = c * U_1 * ... * U_n with U_i uniform on (0, 1), so
# ln X_n = ln c - G where G = sum(-ln U_i) ~ Gamma(n, 1).
# P(X_n < 1) = P(G > ln c) = 0.25, hence ln c is the 75th percentile of
# Gamma(n, 1): solve P(n, x) = 0.75 for the regularized lower incomplete
# gamma function P.


def gamma_p(a: float, x: float) -> float:
    """Regularized lower incomplete gamma P(a, x)."""
    if x < a + 1:
        # Series representation.
        term = 1.0 / a
        total = term
        k = a
        while True:
            k += 1
            term *= x / k
            total += term
            if term < total * 1e-17:
                break
        return total * pow_factor(a, x)
    # Continued fraction (modified Lentz) for Q(a, x) = 1 - P(a, x).
    tiny = 1e-300
    b = x + 1.0 - a
    c = 1.0 / tiny
    d = 1.0 / b
    h = d
    for i in range(1, 10_000_000):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-16:
            break
    return 1.0 - pow_factor(a, x) * h


def pow_factor(a: float, x: float) -> float:
    return pow(2.718281828459045, a * log(x) - x - lgamma(a))


def gamma_quantile(a: float, p: float) -> float:
    """Solve P(a, x) = p by bisection from a safe bracket around the mean."""
    lo, hi = a - 10 * sqrt(a), a + 10 * sqrt(a)
    for _ in range(200):
        mid = (lo + hi) / 2
        if gamma_p(a, mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main() -> str:
    # Given check: n = 100 yields log10(c) ~ 46.27.
    assert f"{gamma_quantile(100, 0.75) / log(10):.2f}" == "46.27"
    return f"{gamma_quantile(10_000_000, 0.75) / log(10):.2f}"


if __name__ == "__main__":
    print(main())  # 4343871.06

# Sanity note: x ~ n + z * sqrt(n) with z = Phi^{-1}(0.75) ~ 0.6745
# (Wilson-Hilferty agrees to ~1e-3), and log10 of that matches.
