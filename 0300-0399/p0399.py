import math

import numpy as np

from funcs import divisors, factorint, primerange

LAST_DIGITS = 10**16


def _legendre5(p: int) -> int:
    r = p % 5
    if r in (1, 4):
        return 1
    if r in (2, 3):
        return -1
    return 0


def _fib_mod(n: int, mod: int) -> int:
    """F_n mod `mod` by fast doubling."""

    def rec(m: int) -> tuple[int, int]:
        if m == 0:
            return 0, 1
        a, b = rec(m >> 1)
        c = (a * ((2 * b - a) % mod)) % mod
        d = (a * a + b * b) % mod
        if m & 1:
            return d, (c + d) % mod
        return c, d

    return rec(n)[0]


def _entry_point(p: int) -> int:
    """Rank of apparition: the smallest m with p | F_m. It divides p - (5|p), so
    we test the divisors of that value in increasing order."""
    if p == 5:
        return 5
    for d in divisors(p - _legendre5(p)):  # divisors() is already sorted
        if _fib_mod(d, p) == 0:
            return d
    return p - _legendre5(p)


def solve(target: int = 100_000_000, limit: int = 140_000_000) -> str:
    """Last sixteen digits and one-significant-figure scientific form of the
    target-th squarefree Fibonacci number.

    Assuming Wall's conjecture (the first Fibonacci divisible by p is never
    divisible by p^2), F_n is divisible by p^2 exactly when p * alpha(p) divides
    n, where alpha(p) is the rank of apparition of p. So F_n fails to be
    squarefree precisely when n is a multiple of some modulus m_p = p * alpha(p),
    and the squarefree Fibonacci indices are those struck out by none of these
    moduli. Sieving the moduli up to `limit` and taking a running count locates
    the index of the target-th squarefree Fibonacci.

    A prime contributes a modulus <= limit only if alpha(p) <= limit / p. Any
    prime above this scan bound would need a very small rank of apparition, i.e.
    it would have to divide F_a for some tiny a; checking those F_a directly
    confirms the scan below already captures every relevant modulus.
    """
    scan = 1_600_000  # primes past this would need alpha <= limit/scan < 90
    moduli = set()
    for p in primerange(2, scan + 1):
        m = p * _entry_point(p)
        if m <= limit:
            moduli.add(m)
    # confirm no large prime with a tiny rank of apparition is missed
    f_prev, f_cur = 1, 1
    for a in range(3, limit // scan + 2):
        f_prev, f_cur = f_cur, f_prev + f_cur
        bound = limit // a
        if bound <= scan:
            continue
        for q in factorint(f_cur):
            if scan < q <= bound and _entry_point(q) == a:
                moduli.add(q * a)

    struck = np.zeros(limit + 1, dtype=bool)
    for m in moduli:
        struck[m::m] = True
    # cumulative count of unstruck indices 1..k; equals
    # arange(1, limit + 1) - cumsum(struck[1:]) without the 8-byte arange
    squarefree_count = np.cumsum(~struck[1 : limit + 1], dtype=np.int64)
    index = int(np.searchsorted(squarefree_count, target) + 1)

    last16 = str(_fib_mod(index, LAST_DIGITS)).zfill(16)
    phi = (1 + math.sqrt(5)) / 2
    log10_fib = index * math.log10(phi) - 0.5 * math.log10(5)
    exponent = int(math.floor(log10_fib))
    mantissa = 10 ** (log10_fib - exponent)
    return f"{last16},{mantissa:.1f}e{exponent}"


if __name__ == "__main__":
    # The 200th squarefree Fibonacci is F_260, ending 1608739584170445 ~ 9.7e53.
    assert solve(200, 1000) == "1608739584170445,9.7e53"
    print(solve())  # 1508395636674243,6.5e27330467
