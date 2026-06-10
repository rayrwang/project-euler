def xor_solutions(limit: int) -> set[tuple[int, int]]:
    """All pairs 0 <= a <= b <= limit with a^2 + x a b + b^2 = (x+1)^2.

    Interpreting bit strings as polynomials over GF(2), the left side is
    the norm form of GF(2)[x][t] with t^2 = x t + 1: indeed t has norm
    t tbar = 1 and trace t + tbar = x, so N(a + b t) = a^2 + x a b + b^2.
    The right side is 5 = (x + 1)^2 = N(x + 1).  Modulo the prime x + 1
    the polynomial t^2 + x t + 1 becomes t^2 + t + 1, irreducible over
    GF(2), so x + 1 is inert and the only elements of norm (x + 1)^2 are
    the associates (x + 1) t^k.  Multiplying by t maps
        a + b t  ->  b + (a + x b) t,
    i.e. (a, b) -> (b, a XOR 2b), and negative k just swaps the pair, so
    iterating from (3, 0) and recording unordered pairs finds everything.
    """
    sols: set[tuple[int, int]] = set()
    a, b = 3, 0
    while min(a, b) <= limit:
        if max(a, b) <= limit:
            sols.add((min(a, b), max(a, b)))
        a, b = b, a ^ (b << 1)
    return sols


def x_of(limit: int) -> int:
    res = 0
    for _, b in xor_solutions(limit):
        res ^= b
    return res


def _gf2_mul(u: int, v: int) -> int:
    r = 0
    while v:
        if v & 1:
            r ^= u
        u <<= 1
        v >>= 1
    return r


if __name__ == "__main__":
    # brute-force completeness check on a small box
    brute = {
        (a, b)
        for a in range(0, 801)
        for b in range(a, 801)
        if _gf2_mul(a, a) ^ _gf2_mul(2, _gf2_mul(a, b)) ^ _gf2_mul(b, b) == 5
    }
    assert brute == xor_solutions(800)
    assert x_of(10) == 5  # given
    print(x_of(10**18))  # 336785000760344621
