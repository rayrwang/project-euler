"""Project Euler Problem 646: Bounded Divisors.

S(n, L, H) sums lambda(d) * d (Liouville function times divisor) over the
divisors of n lying in [L, H]; we need S(70!, 10^20, 10^60) mod 10^9 + 7.

70! has about 3.5 * 10^12 divisors -- far too many to enumerate, but its
19 distinct primes split into two halves whose divisor counts are both
near sqrt of that, about 1.9 * 10^6.  Meet in the middle: every divisor
factors uniquely as d = a b with a from the first half's divisor list and
b from the second's, and lambda(d) d = (lambda(a) a)(lambda(b) b).  Sort
the b-side by value with exact-integer prefix sums of lambda(b) b; then
for each a the constraint L <= a b <= H is a contiguous value window
[ceil(L/a), floor(H/a)], located by bisection on exact integers (no
floating-point boundary risk), contributing lambda(a) a times a prefix
difference.  All arithmetic is exact big-int, reduced only at the end,
which also lets the small factorial checks be verified exactly.

The prime split balances the product of (exponent + 1) greedily.  Checks:
S(10!, 100, 1000) = 1457, S(15!, 10^3, 10^5) = -107974 and
S(30!, 10^8, 10^12) = 9766732243224, all exact as given.
"""

from bisect import bisect_left, bisect_right


def factorial_factorisation(n: int) -> list[tuple[int, int]]:
    sieve = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if sieve[i] == i:
            for j in range(i * i, n + 1, i):
                if sieve[j] == j:
                    sieve[j] = i
    primes = [p for p in range(2, n + 1) if sieve[p] == p]
    fac = []
    for p in primes:
        e, q = 0, p
        while q <= n:
            e += n // q
            q *= p
        fac.append((p, e))
    return fac


def divisors_signed(fac: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """All (value, lambda(value) * value) over divisors of prod p^e."""
    out = [(1, 1)]
    for p, e in fac:
        new = []
        for v, m in out:
            pv, sign = 1, 1
            for _ in range(e + 1):
                new.append((v * pv, m * sign * pv))
                pv *= p
                sign = -sign
        out = new
    return out


def S(n_fact: int, L: int, H: int) -> int:
    fac = factorial_factorisation(n_fact)
    # balance the two halves by product of (e + 1)
    fac.sort(key=lambda pe: -(pe[1] + 1))
    half_a: list[tuple[int, int]] = []
    half_b: list[tuple[int, int]] = []
    ca = cb = 1
    for p, e in fac:
        if ca <= cb:
            half_a.append((p, e))
            ca *= e + 1
        else:
            half_b.append((p, e))
            cb *= e + 1
    A = divisors_signed(half_a)
    B = divisors_signed(half_b)
    B.sort()
    vals = [v for v, _ in B]
    pref = [0]
    for _, m in B:
        pref.append(pref[-1] + m)
    total = 0
    for a, ma in A:
        lo = (L + a - 1) // a
        hi = H // a
        if lo > hi:
            continue
        il = bisect_left(vals, lo)
        ir = bisect_right(vals, hi)
        if il < ir:
            total += ma * (pref[ir] - pref[il])
    return total


if __name__ == "__main__":
    assert S(10, 100, 1000) == 1457
    assert S(15, 10**3, 10**5) == -107974
    assert S(30, 10**8, 10**12) == 9766732243224
    print(S(70, 10**20, 10**60) % 1_000_000_007)  # 845218467
