from decimal import Decimal, getcontext
from fractions import Fraction

# At step t Alice has seen t cards; the current card's rank r among them is
# uniform on {1..t} and, given r, its expected face value is r(n+1)/(t+1).
# The optimal continuation value depends only on t, so with W(t) the expected
# score on observing the t-th card under optimal play,
#   W(n) = (n+1)/2,
#   W(t) = (1/t) * sum_r min(r(n+1)/(t+1), W(t+1)),
# and F(n) = W(1).  The minimum splits at a threshold k, making each step O(1).


def f_decimal(n: int, prec: int = 40) -> Decimal:
    getcontext().prec = prec
    np1 = Decimal(n + 1)
    w = np1 / 2  # W(n)
    for t in range(n - 1, 0, -1):
        unit = np1 / (t + 1)  # stop value for rank r is r * unit
        k = int(w / unit)  # ranks 1..k prefer stopping
        if k > t:
            k = t
        while k * unit > w:
            k -= 1
        while (k + 1) * unit < w and k < t:
            k += 1
        w = (unit * k * (k + 1) / 2 + (t - k) * w) / t
    return w


def f_exact(n: int) -> Fraction:
    w = Fraction(n + 1, 2)
    for t in range(n - 1, 0, -1):
        s = sum(
            (min(Fraction(r * (n + 1), t + 1), w) for r in range(1, t + 1)),
            start=Fraction(0),
        )
        w = s / t
    return w


if __name__ == "__main__":
    assert f_exact(3) == Fraction(5, 3)
    for n in (3, 7, 25, 60):
        assert abs(f_decimal(n) - Decimal(f_exact(n).numerator) / f_exact(n).denominator) < Decimal("1e-30")
    a40 = f_decimal(10**6, 40)
    a60 = f_decimal(10**6, 60)
    assert abs(a40 - a60) < Decimal("1e-25")
    print(f"{a40:.10f}")  # 3.8694550145
