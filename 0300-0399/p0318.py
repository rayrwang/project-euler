from decimal import Decimal, getcontext

from funcs import is_square


def total(limit: int, nines: int) -> int:
    """Sum of N(p, q) over p < q with p + q <= limit and fract -> 1.

    With e = (sqrt p + sqrt q)^2 and d = (sqrt q - sqrt p)^2, d^n + e^n is an
    integer, so frac(e^n) = 1 - d^n, which tends to 1 exactly when d < 1
    (and pq not a perfect square, else d is a positive integer).  The
    fractional part starts with at least `nines` nines iff d^n <= 10^-nines,
    so N(p, q) = ceil(nines / (-log10 d)).
    """
    getcontext().prec = 80
    eps = Decimal(10) ** -30
    target = Decimal(nines)
    s = 0
    for p in range(1, limit // 2 + 1):
        # d < 1  <=>  sqrt(q) < sqrt(p) + 1  <=>  q <= p + 2 sqrt(p) (ints)
        for q in range(p + 1, limit - p + 1):
            pq = p * q
            if is_square(pq):
                continue
            d = Decimal(p + q) - 2 * Decimal(pq).sqrt()
            if d >= 1:
                break  # d increases with q for fixed p
            ratio = target / -d.log10()
            n = int(ratio)
            frac = ratio - n
            # d is irrational, so the ratio can't be an exact integer; the
            # assert guards against a float-style rounding catastrophe.
            assert eps < frac < 1 - eps
            s += n + 1
    return s


if __name__ == "__main__":
    print(total(2011, 2011))  # 709313889
