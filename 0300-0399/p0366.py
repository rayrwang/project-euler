import bisect
from functools import lru_cache

MOD = 10**8

FIBS = [1, 2]
while FIBS[-1] < 2 * 10**18:
    FIBS.append(FIBS[-1] + FIBS[-2])
NF = len(FIBS)


def top_fib_index(n: int) -> int:
    return bisect.bisect_right(FIBS, n) - 1


@lru_cache(maxsize=None)
def m_value(n: int) -> int:
    """M(n): max stones the first player can take from a winning position.

    This is Fibonacci Nim. The position (n, k) -- n stones, may take 1..k --
    is a second-player win exactly when k is below the smallest term of n's
    Zeckendorf representation (verified by game-tree search for small n).
    A first move taking t leaves (n - t, 2t); it wins iff that position
    loses, i.e. 2t < smallest Zeckendorf term of n - t. Writing
    n = F_k + r with F_k the largest Fibonacci number <= n (so
    0 <= r < F_{k-1}), the maximal winning t works out to the recursion
        M(n) = r          if 2r < F_k   (take everything below the top term),
        M(n) = M(r)       otherwise,
    and M(n) = 0 when n is itself a Fibonacci number (a losing position).
    """
    if n <= 0:
        return 0
    i = top_fib_index(n)
    f = FIBS[i]
    if f == n:
        return 0
    r = n - f
    if 2 * r < f:
        return r
    return m_value(r)


def tri_mod(t: int) -> int:
    """t (t + 1) / 2 mod 10^8. Since 2 is not invertible mod 10^8, halve the
    even factor before reducing rather than using a modular inverse."""
    if t % 2 == 0:
        return (t // 2) % MOD * ((t + 1) % MOD) % MOD
    return t % MOD * (((t + 1) // 2) % MOD) % MOD


@lru_cache(maxsize=None)
def prefix(x: int) -> int:
    """sum_{n=0}^{x-1} M(n) mod 10^8.

    Group the numbers by their largest Fibonacci term F_k: those n with
    F_k <= n < F_{k+1} are n = F_k + r for r in [0, F_{k-1} - 1]. By the
    recursion above each contributes r while 2r < F_k (an arithmetic run,
    summed in closed form) and M(r) beyond that (a tail of the same prefix
    sum at a smaller argument). The smaller arguments shrink geometrically,
    so the memoised recursion is logarithmic in x.
    """
    if x <= 2:
        return 0
    total = 0
    k = 1
    while FIBS[k] < x:
        fk = FIBS[k]
        fk1 = FIBS[k + 1] if k + 1 < NF else 10**30
        umax = min(fk1 - 1, x - 1) - fk  # largest r in this (maybe partial) block
        t = (fk - 1) // 2  # 2r < fk  <=>  r <= t
        if t >= umax:
            total = (total + tri_mod(umax)) % MOD
        else:
            total = (total + tri_mod(t) + prefix(umax + 1) - prefix(t + 1)) % MOD
        k += 1
    return total % MOD


if __name__ == "__main__":
    # M(n) = 0 at the small losing positions and the worked example M(5) = 0.
    assert m_value(5) == 0
    assert [m_value(n) for n in (4, 6, 7)] == [1, 1, 2]
    # sum_{n=1}^{100} M(n) = 728 (the value cited in the problem thread).
    assert prefix(101) == 728
    print(prefix(10**18 + 1))  # 88351299
