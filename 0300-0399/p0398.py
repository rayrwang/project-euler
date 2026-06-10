from numba import njit


@njit
def _expected(n: int, m: int) -> float:
    """E(n, m): expected length of the second-shortest of m segments formed by cutting a
    length-n rope at m-1 of its n-1 integer interior points.

    Each cut pattern is a composition of n into m positive parts, all C(n-1, m-1) of them
    equally likely. Using E = sum_{t>=1} P(second-shortest >= t), and noting the
    second-shortest is >= t exactly when at most one part is smaller than t:

      P(>= t) = [ A(t) + m * (C(W, m-1) - C(W-t+1, m-1)) ] / C(n-1, m-1),

    where A(t) = C(n-1-m(t-1), m-1) counts patterns with every part >= t, the bracket
    counts patterns with exactly one part below t (m placements, the small part's value
    summed by the hockey-stick identity), and W = n-1-(m-1)(t-1).

    Each binomial-over-binomial ratio C(x, m-1)/C(n-1, m-1) is evaluated as the product
    prod_{i=0}^{m-2} (x-i)/(n-1-i); forming it as a product (rather than via differences of
    log-gammas) avoids catastrophic cancellation and keeps full double precision.
    """
    den = n - 1
    total = 0.0
    t = 1
    while True:
        a1 = n - 1 - m * (t - 1)  # top of A(t)'s binomial
        w = n - 1 - (m - 1) * (t - 1)

        a_term = 0.0
        if a1 >= m - 1:
            p = 1.0
            for i in range(m - 1):
                p *= (a1 - i) / (den - i)
            a_term = p

        b1 = 0.0
        if w >= m - 1:
            p = 1.0
            for i in range(m - 1):
                p *= (w - i) / (den - i)
            b1 = p

        b2 = 0.0
        w2 = w - t + 1
        if w2 >= m - 1:
            p = 1.0
            for i in range(m - 1):
                p *= (w2 - i) / (den - i)
            b2 = p

        term = a_term + m * (b1 - b2)
        total += term
        if a1 < m - 1 and term == 0.0:
            break
        t += 1
        if t > n:
            break
    return total


def solve(n: int = 10**7, m: int = 100) -> float:
    return _expected(n, m)


if __name__ == "__main__":
    assert abs(_expected(3, 2) - 2.0) < 1e-9
    assert abs(_expected(8, 3) - 16 / 7) < 1e-9
    print(f"{solve():.5f}")  # 2010.59096
