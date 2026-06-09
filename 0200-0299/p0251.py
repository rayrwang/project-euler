import numba
import numpy as np

from funcs import mod_exp_bounded, prime_sieve_bool

# Setting u, v for the two cube roots, u + v = 1, u^3 + v^3 = 2a and
# u v = cbrt(a^2 - b^2 c) give 27 b^2 c = 27 a^2 - (1 - 2a)^3
# = (a + 1)^2 (8a - 1). Divisibility by 27 forces a = 3k + 2, leaving
#     b^2 c = (k + 1)^2 (8k + 5) =: M.
# So for each k count the divisors b with b^2 | M and a + b + M / b^2 <= N.
#
# Factor 8k + 5 for all k by a blocked sieve over the arithmetic progression
# (its prime factors p satisfy k = -5/8 mod p); after removing primes up to
# 17131 the residual is 1 or prime, because two larger primes would multiply
# past max(8k + 5) = 293333325 < 17137^2. The factorisation of (k + 1)^2
# comes from a smallest-prime-factor sieve. gcd(k + 1, 8k + 5) divides 3, so
# the merge has at most one shared prime. A DFS over the merged exponents
# enumerates b (pruned at b > N - a) and accumulates c with capped products.


@numba.njit(cache=True)
def _spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def _count_b(
    qs: np.ndarray, hs: np.ndarray, es: np.ndarray, nq: int, s: int, cap: int
) -> int:
    # Count divisors b = prod q^g (g <= h_j) of the square-root part with
    # b + c <= s, where c = prod q^(e_j - 2g) is capped at `cap`.
    # Iterative DFS: g[j] tracks the exponent chosen at level j, with running
    # products bprod[j], cprod[j] entering level j.
    g = np.zeros(nq + 1, dtype=np.int64)
    bprod = np.empty(nq + 1, dtype=np.int64)
    cprod = np.empty(nq + 1, dtype=np.int64)
    bprod[0] = 1
    cprod[0] = 1
    total = 0
    j = 0
    g[0] = 0
    while j >= 0:
        if j == nq:
            if bprod[j] + cprod[j] <= s:
                total += 1
            j -= 1
            continue
        gj = g[j]
        if gj > hs[j]:
            j -= 1
            continue
        q = qs[j]
        bb = bprod[j]
        ok = True
        for _ in range(gj):
            bb *= q
            if bb > s:
                ok = False
                break
        g[j] += 1  # next sibling when we come back
        if not ok:
            j -= 1  # larger g only grows b further
            continue
        cf = 1
        for _ in range(es[j] - 2 * gj):
            cf *= q
            if cf >= cap:
                cf = cap
                break
        c = cprod[j]
        cc = c * cf if c < cap and cf < cap and c * cf <= cap else cap
        bprod[j + 1] = bb
        cprod[j + 1] = cc
        j += 1
        if j <= nq:
            g[j] = 0
    return total


@numba.njit(cache=True)
def _count_all(
    n: int, k_max: int, primes: np.ndarray, roots: np.ndarray, spf: np.ndarray
) -> int:
    block = 1 << 20
    res = np.empty(block, dtype=np.int64)
    fp = np.empty((block, 16), dtype=np.int64)
    fe = np.empty((block, 16), dtype=np.int64)
    fc = np.empty(block, dtype=np.int64)
    qs = np.empty(24, dtype=np.int64)
    es = np.empty(24, dtype=np.int64)
    hs = np.empty(24, dtype=np.int64)
    total = 0
    k0 = 0
    while k0 <= k_max:
        size = min(block, k_max - k0 + 1)
        for i in range(size):
            res[i] = 8 * (k0 + i) + 5
            fc[i] = 0
        for pi in range(len(primes)):
            p = primes[pi]
            r = roots[pi]
            start = (r - k0) % p
            for i in range(start, size, p):
                e = 0
                while res[i] % p == 0:
                    res[i] //= p
                    e += 1
                if e > 0:
                    fp[i, fc[i]] = p
                    fe[i, fc[i]] = e
                    fc[i] += 1
        for i in range(size):
            if res[i] > 1:
                fp[i, fc[i]] = res[i]
                fe[i, fc[i]] = 1
                fc[i] += 1
            k = k0 + i
            a = 3 * k + 2
            s = n - a
            if s < 2:
                continue
            # merge: factors of 8k+5 plus doubled factors of k+1
            nq = 0
            for j in range(fc[i]):
                qs[nq] = fp[i, j]
                es[nq] = fe[i, j]
                nq += 1
            m = k + 1
            while m > 1:
                q = spf[m]
                e = 0
                while m % q == 0:
                    m //= q
                    e += 1
                found = False
                for j in range(nq):
                    if qs[j] == q:
                        es[j] += 2 * e
                        found = True
                        break
                if not found:
                    qs[nq] = q
                    es[nq] = 2 * e
                    nq += 1
            for j in range(nq):
                hs[j] = es[j] // 2
            total += _count_b(qs, hs, es, nq, s, n + 1)
        k0 += block
    return total


def solve(n: int = 110_000_000) -> int:
    k_max = (n - 4) // 3
    spf = _spf_sieve(k_max + 1)
    v_max = 8 * k_max + 5
    p_limit = int(v_max**0.5) + 10
    sieve = prime_sieve_bool(p_limit)
    primes = np.nonzero(sieve)[0].astype(np.int64)
    primes = primes[primes > 2]  # 8k + 5 is odd
    roots = np.empty(len(primes), dtype=np.int64)
    for i, p in enumerate(primes):
        p = int(p)
        inv8 = int(mod_exp_bounded(8, p - 2, p))
        roots[i] = (-5 * inv8) % p
    return int(_count_all(n, k_max, primes, roots, spf))


if __name__ == "__main__":
    print(solve())  # 18946051
