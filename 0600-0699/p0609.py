import numba
import numpy as np

from funcs import prime_sieve_bool

MOD = 10**9 + 7

@numba.jit(cache=True)
def _proc(vv: int, nv: int, sieve: np.ndarray, pi: np.ndarray, cnt: np.ndarray) -> None:
    """Add the contributions of one block: the prime p_vv (one u0) and nv composite u0.

    All share the downstream chain vv -> pi(vv) -> ... -> 1. Walking it accumulates
    s = number of non-primes among chain[0..t]; the prime u0 contributes c = s and each
    composite u0 contributes c = s + 1, for every prefix length t.
    """
    s = 0
    w = vv
    while w >= 1:
        if not sieve[w]:
            s += 1
        cnt[s] += 1
        cnt[s + 1] += nv
        nw = pi[w]
        if nw < 1:
            break
        w = nw

@numba.jit(cache=True)
def histogram(sieve: np.ndarray, vmax: int) -> np.ndarray:
    """Counts cnt[k] = number of pi sequences u with u0 <= n and c(u) = k."""
    n = len(sieve) - 1
    pi = np.zeros(vmax + 1, dtype=np.int64)
    c = 0
    for i in range(1, vmax + 1):
        if sieve[i]:
            c += 1
        pi[i] = c
    cnt = np.zeros(128, dtype=np.int64)
    v = 0
    prev = -1
    for i in range(2, n + 1):
        if sieve[i]:
            v += 1
            if prev > 0:
                _proc(v - 1, i - prev - 1, sieve, pi, cnt)
            prev = i
    if prev > 0:
        _proc(v, n - prev, sieve, pi, cnt)
    return cnt

def solve(n: int) -> int:
    """P(n) mod 1e9+7.

    A pi sequence is u0, pi(u0), pi(pi(u0)), ... truncated at any term still >= 1.
    Grouping u0 by v = pi(u0): each block [p_v, p_{v+1}) contains exactly one prime
    (p_v, contributing non-prime count starting at the chain's own counts) and the
    rest composite (shifting every count by 1). p(n,k) is the resulting histogram and
    P(n) is the product of its positive entries.
    """
    sieve = prime_sieve_bool(n + 1)
    vmax = int(sieve[: n + 1].sum())  # pi(n)
    cnt = histogram(sieve, vmax)
    prod = 1
    for k in range(len(cnt)):
        if cnt[k] > 0:
            prod = prod * (int(cnt[k]) % MOD) % MOD
    return prod

if __name__ == "__main__":
    print(solve(10**8))  # 172023848
