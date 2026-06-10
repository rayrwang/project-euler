from math import isqrt, lcm

import numba
import numpy as np

from funcs import prime_sieve_int

MOD = 1_000_000_007


@numba.jit(cache=True)
def _grid_compute(
    total: int,
    dims: np.ndarray,
    svecs: np.ndarray,
    svals: np.ndarray,
    kmax: int,
    fac: np.ndarray,
    pw2: np.ndarray,
    primes_small: np.ndarray,
) -> int:
    r = len(dims)
    strides = np.empty(r, dtype=np.int64)
    acc = 1
    for i in range(r):
        strides[i] = acc
        acc *= dims[i]
    w = np.empty(total, dtype=np.int64)
    exps = np.empty(r, dtype=np.int64)
    cnt = np.empty(kmax + 2, dtype=np.int64)
    for flat in range(total):
        f = flat
        for i in range(r):
            exps[i] = f % dims[i]
            f //= dims[i]
        for t in range(kmax + 2):
            cnt[t] = 0
        for s in range(len(svals)):
            ok = True
            for i in range(r):
                if svecs[s][i] > exps[i]:
                    ok = False
                    break
            if ok:
                b = svals[s] if svals[s] <= kmax else kmax + 1
                cnt[b] += 1
        d0 = 0
        for t in range(kmax + 2):
            d0 += cnt[t]
        b_val = pw2[d0]
        run = 0
        for k in range(1, kmax + 1):
            run += cnt[k]  # divisors of L that are <= k
            b_val = b_val * fac[k][run] % MOD
        w[flat] = b_val
    # Moebius inversion along each chain dimension (descending differences)
    for i in range(r):
        stride = strides[i]
        dim = dims[i]
        block = stride * dim
        for base in range(0, total, block):
            for d in range(dim - 1, 0, -1):
                off = base + d * stride
                for rdx in range(stride):
                    w[off + rdx] = (w[off + rdx] - w[off - stride + rdx]) % MOD
    # G = sum over grid of value(L) * W(L)
    g = 0
    for flat in range(total):
        f = flat
        val = 1
        for i in range(r):
            e = f % dims[i]
            f //= dims[i]
            for _ in range(e):
                val = val * primes_small[i] % MOD
        g = (g + val * w[flat]) % MOD
    return g % MOD


def g_of(n: int) -> int:
    """Sum of lcm(S) over all subsets S of {1..N}, mod 1e9+7.

    Primes p > sqrt(N) divide each element at most once and no element
    twice over, so the multiples of such p are p*m with smooth m <= N//p.
    Writing every subset's lcm as (smooth join) * (product of large
    primes hit), the smooth joins live on the small grid of admissible
    values L = prod p_i^(e_i) with p_i^(e_i) <= N.  Counting subsets
    whose smooth join divides L, weighted by the large primes used,
        B(L) = 2^(d0(L)) * prod_p (1 + p * (2^(e_p(L)) - 1)),
    where d0 counts smooth numbers <= N dividing L and e_p counts
    cofactors m <= N//p dividing L.  Moebius inversion over the exponent
    grid turns B into exact weights W, and G = sum L * W(L).
    """
    primes = [int(p) for p in prime_sieve_int(n + 1)]
    root = isqrt(n)
    small = [p for p in primes if p <= root]
    large = [p for p in primes if p > root]
    caps = []
    for p in small:
        c = 0
        v = p
        while v <= n:
            c += 1
            v *= p
        caps.append(c)
    dims = np.array([c + 1 for c in caps], dtype=np.int64)
    total = int(np.prod(dims)) if len(dims) else 1

    # smooth numbers <= n with exponent vectors
    svecs_l, svals_l = [], []
    for m in range(1, n + 1):
        v = m
        vec = [0] * len(small)
        for i, p in enumerate(small):
            while v % p == 0:
                vec[i] += 1
                v //= p
        if v == 1:
            svecs_l.append(vec)
            svals_l.append(m)
    svecs = np.array(svecs_l, dtype=np.int64).reshape(len(svals_l), len(small))
    svals = np.array(svals_l, dtype=np.int64)

    kmax = n // large[0] if large else 0
    pw2 = np.empty(len(svals) + 1, dtype=np.int64)
    pw2[0] = 1
    for i in range(1, len(svals) + 1):
        pw2[i] = pw2[i - 1] * 2 % MOD
    # fac[k][c] = prod over large p with N//p == k of (1 + p(2^c - 1))
    fac = np.ones((kmax + 1, kmax + 1), dtype=np.int64)
    for p in large:
        k = n // p
        for c in range(kmax + 1):
            term = (1 + p * (int(pw2[c]) - 1)) % MOD
            fac[k][c] = int(fac[k][c]) * term % MOD
    return int(
        _grid_compute(
            total,
            dims,
            svecs,
            svals,
            kmax,
            fac,
            pw2,
            np.array(small, dtype=np.int64),
        )
        % MOD
    )


def _g_brute(n: int) -> int:
    total = 0
    for mask in range(1 << n):
        cur = 1
        for i in range(n):
            if (mask >> i) & 1:
                cur = lcm(cur, i + 1)
        total += cur
    return total


if __name__ == "__main__":
    for n in range(4, 13):
        assert g_of(n) == _g_brute(n) % MOD, n
    assert g_of(5) == 528  # given
    assert g_of(20) == 8463108648960 % MOD  # given
    print(g_of(800))  # 973077199
