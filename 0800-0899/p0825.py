from mpmath import digamma, mp, mpf, sqrt

mp.dps = 40


def chasing_difference(n: int) -> mpf:
    """S(n): exact win-probability difference for the gap-n chase.

    With gap d (distance the mover must cover) the mover wins outright if its
    step 1, 2 or 3 reaches d; otherwise the opponent moves with gap 2n-(d-step),
    so the win probability satisfies W(d) = 1 - (1/3) sum_{k<d, k<=3} W(2n-d+k).
    Solving this linear system, both the numerator and denominator of S(n) =
    |2 W(n) - 1| obey constant-coefficient recurrences: the numerator has roots
    {-1, 2 +- sqrt(3)} and the denominator the double roots (2 +- sqrt(3))^2, so
        num(n) = ((3-r)/2)(2+sqrt3)^n + ((3+r)/2)(2-sqrt3)^n - 2(-1)^n,
        den(n) = (((3-r)/2)n - 1/2)(2+sqrt3)^n + (((3+r)/2)n - 1/2)(2-sqrt3)^n,
    with r = sqrt(3). (Coefficients fitted to and verified against exact small
    values; S(2) = 7/11.)
    """
    r = sqrt(3)
    big, small = 2 + r, 2 - r
    a = (3 - r) / 2
    num = a * big**n + (3 + r) / 2 * small**n - 2 * (-1)**n
    den = (a * n - mpf(1) / 2) * big**n + ((3 + r) / 2 * n - mpf(1) / 2) * small**n
    return abs(num / den)


def chasing_sum(upper: int) -> mpf:
    """T(N) = sum_{n=2}^N S(n).

    The (2 - sqrt(3))^n terms vanish geometrically and (3 - sqrt(3))/2 is the
    leading coefficient of both num and den, so for large n
        S(n) = 1 / (n + b/a),   b/a = -(3 + sqrt(3)) / 6,
    exact to far beyond double precision once n exceeds a small cutoff. Sum the
    first terms directly and the rest as digamma(N + 1 + b/a) - digamma(cutoff +
    1 + b/a).
    """
    cutoff = 200
    ratio = -(3 + sqrt(3)) / 6  # b / a
    if upper <= cutoff:
        return sum((chasing_difference(n) for n in range(2, upper + 1)), mpf(0))
    head = sum((chasing_difference(n) for n in range(2, cutoff + 1)), mpf(0))
    tail = digamma(upper + 1 + ratio) - digamma(cutoff + 1 + ratio)
    return head + tail


if __name__ == "__main__":
    assert abs(chasing_sum(10) - mpf("2.38235282")) < mpf("1e-8")
    result = chasing_sum(10**14)
    print(mp.nstr(result, 10))  # 32.34481054
