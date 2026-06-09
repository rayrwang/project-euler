import numba
import numpy as np

from funcs import prime_sieve_int


def tonelli(a: int, p: int) -> int:
    """A square root of a modulo the odd prime p (a assumed to be a residue)."""
    a %= p
    if a == 0:
        return 0
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        r = r * b % p
        c = b * b % p
        t = t * c % p
        m = i
    return r


def build_roots(primes: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """For each prime p, the roots of k^2 - k + 1 == 0 (mod p).

    Completing the square gives (2k-1)^2 == -3 (mod p); roots exist for p = 3
    (the double root k == 2) and for p == 1 (mod 3), and never for p == 2 or
    p == 2 (mod 3).
    """
    plist, rlist = [], []
    for p in primes:
        p = int(p)
        if p == 2:
            continue
        if p == 3:
            plist.append(3)
            rlist.append(2)
            continue
        if p % 3 != 1:
            continue
        s = tonelli(-3 % p, p)
        inv2 = (p + 1) // 2
        r1 = (1 + s) * inv2 % p
        r2 = (1 - s) * inv2 % p
        plist.append(p)
        rlist.append(r1)
        if r2 != r1:
            plist.append(p)
            rlist.append(r2)
    return np.array(plist, dtype=np.int64), np.array(rlist, dtype=np.int64)


@numba.jit(cache=True)
def strip_factors(limit: int, plist: np.ndarray, rlist: np.ndarray,
                  m: np.ndarray, lpf: np.ndarray) -> None:
    """Divide each m[k] = k^2 - k + 1 by every prime p (<= limit) dividing it,
    recording the largest such prime in lpf[k]."""
    for idx in range(len(plist)):
        p = plist[idx]
        k = rlist[idx]
        if k == 0:
            k = p
        while k <= limit:
            v = m[k]
            while v % p == 0:
                v //= p
            m[k] = v
            if p > lpf[k]:
                lpf[k] = p
            k += p


def solve(limit: int) -> int:
    """Sum of f(k^3) for 1 <= k <= limit.

    Since the running numerator+denominator starts at k+1 and is repeatedly
    divided by its smallest prime factor until prime, f(k) = lpf(k+1) - 1.
    With k^3 + 1 = (k+1)(k^2-k+1), f(k^3) = max(lpf(k+1), lpf(k^2-k+1)) - 1.
    The second factor (up to ~limit^2) is reduced by sieving the primes that
    can divide it (those <= limit); any residue > 1 is its largest prime.
    """
    primes = prime_sieve_int(limit + 2)  # primes <= limit + 1

    lpf_succ = np.ones(limit + 2, dtype=np.int64)  # largest prime factor table
    for p in primes:
        lpf_succ[p::p] = p

    k = np.arange(limit + 1, dtype=np.int64)
    m = k * k - k + 1  # k^2 - k + 1 (m[0] unused)
    lpf_m = np.ones(limit + 1, dtype=np.int64)
    plist, rlist = build_roots(primes)
    strip_factors(limit, plist, rlist, m, lpf_m)

    total = 0
    for j in range(1, limit + 1):
        lp_m = lpf_m[j] if m[j] == 1 else m[j]  # leftover residue is prime
        total += max(int(lp_m), int(lpf_succ[j + 1])) - 1
    return total


if __name__ == "__main__":
    assert solve(100) == 118937
    print(solve(2_000_000))  # 269533451410884183
