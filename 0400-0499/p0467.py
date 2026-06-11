import numba
import numpy as np

from funcs import prime_sieve_bool

MOD = 10**9 + 7

def digit_root_strings(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Digital roots (= value mod 9, with 9 for multiples) of the first
    n primes and first n composites."""
    sieve = prime_sieve_bool(2_000_000)
    primes = []
    composites = []
    k = 2
    while len(primes) < n or len(composites) < n:
        if sieve[k]:
            if len(primes) < n:
                primes.append(k % 9 or 9)
        elif len(composites) < n:
            composites.append(k % 9 or 9)
        k += 1
    return (np.array(primes, dtype=np.int8),
            np.array(composites, dtype=np.int8))

@numba.jit(cache=True)
def scs_value(a: np.ndarray, b: np.ndarray, mod: int) -> int:
    """Value (mod `mod`) of the lexicographically smallest among the
    shortest common supersequences of digit strings a and b.

    Backward DP for SCS suffix lengths; then a greedy forward walk. At
    (i, j) the next character of any minimal supersequence must be a[i]
    or b[j] (a character matching neither only lengthens it); when both
    moves preserve minimality, the smaller digit wins. Equal characters
    force consuming both. Digits are 1-9 so there is no leading-zero
    subtlety.
    """
    n = len(a)
    m = len(b)
    dp = np.zeros((n + 1, m + 1), dtype=np.int16)
    for i in range(n + 1):
        dp[i, m] = n - i
    for j in range(m + 1):
        dp[n, j] = m - j
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if a[i] == b[j]:
                dp[i, j] = 1 + dp[i + 1, j + 1]
            else:
                x = dp[i + 1, j]
                y = dp[i, j + 1]
                dp[i, j] = 1 + (x if x < y else y)
    val = 0
    i = 0
    j = 0
    while i < n or j < m:
        if i >= n:
            d = b[j]
            j += 1
        elif j >= m:
            d = a[i]
            i += 1
        elif a[i] == b[j]:
            d = a[i]
            i += 1
            j += 1
        else:
            here = dp[i, j]
            ok_a = dp[i + 1, j] == here - 1
            ok_b = dp[i, j + 1] == here - 1
            if ok_a and (not ok_b or a[i] < b[j]):
                d = a[i]
                i += 1
            else:
                d = b[j]
                j += 1
        val = (val * 10 + d) % mod
    return val

def f_plain(n: int) -> int:
    """f(n) as an exact integer (small n only), for the given f(10)."""
    a, b = digit_root_strings(n)
    return scs_value(a, b, 10**17)  # f(10) ~ 2.4e15: no wrap, no overflow

if __name__ == "__main__":
    pd, cd = digit_root_strings(10)
    assert list(pd) == [2, 3, 5, 7, 2, 4, 8, 1, 5, 2]  # given P^D
    assert list(cd) == [4, 6, 8, 9, 1, 3, 5, 6, 7, 9]  # given C^D
    assert f_plain(10) == 2357246891352679  # given
    a100, b100 = digit_root_strings(100)
    assert scs_value(a100, b100, MOD) == 771661825  # given
    a, b = digit_root_strings(10_000)
    print(scs_value(a, b, MOD))  # 775181359
