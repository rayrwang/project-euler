from decimal import Decimal, getcontext
from math import isqrt

getcontext().prec = 60


def _best_denominator(n: int, limit: int) -> int:
    # Best rational approximation to sqrt(n) with denominator <= limit is either
    # the largest continued-fraction convergent within the bound or the maximal
    # semiconvergent built on it; compare their distances in high precision.
    a0 = isqrt(n)
    m, d, a = 0, 1, a0
    p_km1, q_km1 = 1, 0
    p_k, q_k = a0, 1
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        np_, nq = a * p_k + p_km1, a * q_k + q_km1
        if nq > limit:
            break
        p_km1, q_km1 = p_k, q_k
        p_k, q_k = np_, nq
    t = (limit - q_km1) // q_k
    sp, sq = p_km1 + t * p_k, q_km1 + t * q_k
    root = Decimal(n).sqrt()
    if t >= 1 and abs(Decimal(sp) / Decimal(sq) - root) < abs(Decimal(p_k) / Decimal(q_k) - root):
        return sq
    return q_k


def solve(upper: int = 100000, limit: int = 10**12) -> int:
    total = 0
    for n in range(2, upper + 1):
        if isqrt(n) ** 2 != n:
            total += _best_denominator(n, limit)
    return total


if __name__ == "__main__":
    print(solve())  # 57060635927998347
