import numpy as np


def solve(n: int, sieve_limit: int) -> int:
    """Number of distinct lines from the origin through [0, n]^3 lattice
    points.

    Each line corresponds to exactly one primitive direction (a, b, c)
    with gcd 1 (all coordinates are nonnegative, so no sign ambiguity), so
    D(n) counts primitive nonzero points of the cube. Mobius inversion
    over the common divisor d gives
        D(n) = sum over d >= 1 of mu(d) ((floor(n/d) + 1)^3 - 1),
    which collapses into O(sqrt(n)) floor-division blocks weighted by
    differences of the Mertens function M.

    M is evaluated by the standard two-tier method: a sieve of mu up to
    `sieve_limit` with prefix sums, and for larger arguments the identity
    sum over d of M(x // d) = 1, i.e. M(x) = 1 - sum_{d >= 2} M(x // d),
    evaluated blockwise. Every argument needed is of the form n // k
    (floors compose), so computing those values in increasing order makes
    each recursion a single pass. Total work is O(n^(2/3)).
    """
    # Mobius sieve and prefix sums (Mertens) up to sieve_limit.
    mu = np.ones(sieve_limit + 1, dtype=np.int64)
    is_comp = np.zeros(sieve_limit + 1, dtype=bool)
    for p in range(2, sieve_limit + 1):
        if not is_comp[p]:
            mu[p::p] *= -1
            mu[p * p :: p * p] = 0
            is_comp[p * p :: p] = True
    mertens_small = mu.copy()
    mertens_small[0] = 0
    mertens_small = np.cumsum(mertens_small)  # mertens_small[x] = M(x)

    big: dict[int, int] = {}
    big_args = sorted({n // k for k in range(1, n // sieve_limit + 1)})

    def mertens(x: int) -> int:
        return int(mertens_small[x]) if x <= sieve_limit else big[x]

    for x in big_args:
        if x <= sieve_limit:
            continue
        total = 1
        d = 2
        while d <= x:
            q = x // d
            d2 = x // q
            total -= (d2 - d + 1) * mertens(q)
            d = d2 + 1
        big[x] = total

    # D(n) by blocks of q = n // d.
    result = 0
    d = 1
    while d <= n:
        q = n // d
        d2 = n // q
        result += (mertens(d2) - mertens(d - 1)) * ((q + 1) ** 3 - 1)
        d = d2 + 1
    return result


if __name__ == "__main__":
    assert solve(10**6, 10**5) == 831909254469114121
    answer = solve(10**10, 2 * 10**7)
    s = str(answer)
    print(s[:9] + s[-9:])  # 831907372805129931
