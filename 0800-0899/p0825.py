import numpy as np

SQRT3 = np.sqrt(3.0)


def digamma(x: float) -> float:
    """psi(x) for real x > 0, accurate to ~1e-15 relative.

    Uses the recurrence psi(x) = psi(x+1) - 1/x to lift the argument above 10,
    then the standard asymptotic expansion
        psi(x) ~ ln x - 1/(2x) - sum_k B_{2k} / (2k x^{2k}),
    which at x >= 10 is converged to double precision after the B_14 term.
    """
    acc = 0.0
    while x < 10.0:
        acc -= 1.0 / x
        x += 1.0
    inv = 1.0 / x
    inv2 = inv * inv
    # Horner form of B_{2k}/(2k) for k = 1..7:
    # 1/12, -1/120, 1/252, -1/240, 1/132, -691/32760, 1/12
    series = inv2 * (
        1.0 / 12
        - inv2 * (
            1.0 / 120
            - inv2 * (
                1.0 / 252
                - inv2 * (
                    1.0 / 240
                    - inv2 * (1.0 / 132 - inv2 * (691.0 / 32760 - inv2 / 12))
                )
            )
        )
    )
    return acc + np.log(x) - 0.5 * inv - series


def chasing_difference(n: int) -> float:
    """S(n): exact win-probability difference for the gap-n chase.

    Same closed form as before,
        num(n) = ((3-r)/2)(2+r)^n + ((3+r)/2)(2-r)^n - 2(-1)^n,
        den(n) = (((3-r)/2)n - 1/2)(2+r)^n + (((3+r)/2)n - 1/2)(2-r)^n,
    r = sqrt(3), but with everything divided through by (2+r)^n so nothing
    overflows: the surviving small terms involve q^n with q = (2-r)/(2+r)
    = 7 - 4 sqrt(3) ~ 0.0718, which underflows harmlessly to 0 for large n.
    """
    r = SQRT3
    a = (3.0 - r) / 2.0
    b = (3.0 + r) / 2.0
    q_n = ((2.0 - r) / (2.0 + r)) ** n          # (small/big)^n
    inv_big_n = (2.0 + r) ** (-float(n))        # big^(-n), -> 0 for large n
    sign = -1.0 if n & 1 else 1.0
    num = a + b * q_n - 2.0 * sign * inv_big_n
    den = (a * n - 0.5) + (b * n - 0.5) * q_n
    return abs(num / den)


def chasing_sum(upper: int) -> float:
    """T(N) = sum_{n=2}^N S(n).

    As before: past a small cutoff S(n) = 1/(n + b/a) with b/a =
    -(3 + sqrt(3))/6, exact to double precision, so the tail telescopes into a
    digamma difference. The head is summed directly.
    """
    cutoff = 200
    ratio = -(3.0 + SQRT3) / 6.0  # b / a
    if upper <= cutoff:
        return sum(chasing_difference(n) for n in range(2, upper + 1))
    head = sum(chasing_difference(n) for n in range(2, cutoff + 1))
    tail = digamma(upper + 1 + ratio) - digamma(cutoff + 1 + ratio)
    return head + tail


if __name__ == "__main__":
    assert abs(chasing_sum(10) - 2.38235282) < 1e-8
    result = chasing_sum(10**14)
    print(f"{result:.9f}")  # 32.34481054
