"""Project Euler Problem 647: Linear Transformations of Polygonal Numbers.

For odd k (write c = k - 2, odd), the n-th k-gonal number satisfies
8c P_n + (c-2)^2 = x^2 with x = 2cn - (c-2), so P is k-gonal exactly when
that quantity is a square with x == -(c-2) (mod 2c) and x >= c+2.  If
A P + B is k-gonal for *every* P_n then y^2 = A x^2 + D (with
D = 8cB + (1-A)(c-2)^2) must have a solution for every x in an arithmetic
progression; a Pell orbit is exponentially sparse, so A must be a perfect
square a^2, and then (y - ax)(y + ax) = D admits unboundedly many x only
when D = 0.  Hence

    A = a^2,    B = (a^2 - 1)(c - 2)^2 / (8c),    y = a x,

and the index congruence demands 2c | (a - 1)(c - 2).  For odd c,
gcd(2c, c - 2) = 1, so this is simply a == 1 (mod 2c); writing a = 2ct + 1
makes the divisibility of B automatic (t(ct + 1) is always even), giving
the complete family

    a = 2ct + 1,  t >= 1:   A = a^2,   B = t(ct + 1)(c - 2)^2 / 2.

The answer enumerates odd c and t with ct <= (sqrt(N) - 1)/2 and B <= N,
summing A + B exactly in Python integers.  Checks: the classic triangular
transforms (9T+1, 25T+3, 49T+6, ...) and pentagonal 49P+2 appear; an
exhaustive brute-force search over A, B <= 1200 for k = 3, 5, 7, 9, 11
(testing many indices via the square criterion) finds exactly the family;
and the given total sum_k F_k(10^3) = 14993.
"""

from math import isqrt


def is_kgonal(value: int, c: int) -> bool:
    """Is `value` a (c+2)-gonal number with positive index?"""
    s = 8 * c * value + (c - 2) ** 2
    x = isqrt(s)
    if x * x != s:
        return False
    return x >= c + 2 and (x + c - 2) % (2 * c) == 0


def family(c: int, N: int) -> list[tuple[int, int]]:
    """All valid (A, B) with max(A, B) <= N for k = c + 2."""
    out = []
    t = 1
    while True:
        a = 2 * c * t + 1
        A = a * a
        if A > N:
            break
        B = t * (c * t + 1) * (c - 2) ** 2 // 2
        if B <= N:
            out.append((A, B))
        t += 1
    return out


def total(N: int) -> int:
    result = 0
    a_max = isqrt(N)
    ct_max = (a_max - 1) // 2
    for c in range(1, ct_max + 1, 2):
        for t in range(1, ct_max // c + 1):
            a = 2 * c * t + 1
            if a * a > N:
                break
            B = t * (c * t + 1) * (c - 2) ** 2 // 2
            if B <= N:
                result += a * a + B
    return result


def brute_pairs(c: int, limit: int) -> set[tuple[int, int]]:
    """Exhaustive (A, B) search for k = c + 2 by testing all P_n."""
    found = set()
    k = c + 2
    for A in range(1, limit + 1):
        for B in range(1, limit + 1):
            ok = all(
                is_kgonal(A * (n * (n * (k - 2) + 4 - k)) // 2 + B, c)
                for n in range(1, 40)
            )
            if ok:
                found.add((A, B))
    return found


if __name__ == "__main__":
    for c in (1, 3, 5, 7, 9):
        assert brute_pairs(c, 1200) == set(family(c, 1200)), c
    assert (9, 1) in family(1, 100) and (49, 2) in family(3, 100)
    assert total(10**3) == 14993
    print(total(10**12))  # 563132994232918611
