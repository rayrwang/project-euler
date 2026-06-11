"""Project Euler problem 526: Largest Prime Factors of Consecutive Numbers.

f(n) is the largest prime factor of n, g(n) = f(n) + ... + f(n+8) over nine
consecutive numbers, and h(n) = max g(k) for 2 <= k <= n.  Find h(10^16).

For a window starting at n, write each n+i = s_i * t_i where s_i is the
smooth part certified by the residue of n modulo M = 2^5 3^3 5^2 7^2: then
f(n+i) <= max((n+i)/s_i, 7), so g(n) <= psi_c n + 99 where
psi_c = sum 1/s_i depends only on the class c of n mod M.  Windows are
therefore only competitive in classes of large potential.  Structurally,
the optimum is a prime quadruplet n, n+2, n+6, n+8 (forcing
n = 11 mod 30); among nine consecutive numbers the multiple of 7 must then
land on n+3, n+4 or n+5 (anything else collides with a quadruplet prime
seven apart), one of n+1, n+4, n+7 is divisible by 9, and one even is
divisible by 8, giving the maximal potential
psi = 4 + 1/24 + 1/2 + 1/4 + 1/6 + 1/315 ~ 4.9615 when 7 and 9 both fall
on n+4 and the 8 on n+1 or n+7.

The search sweeps classes in decreasing potential, descending in n.  In a
class, a term is "hard" if its quotient failing to be prime provably
drops the window below the current best: a composite quotient coprime to
2,3,5,7 has f <= quotient/11 (factor 1/2 if the certified valuation is
capped), and a prime quotient <= 5000 contributes at most 5000, so
g <= psi n + 5040 - lambda_i n / s_i for any hard failure.  Candidates
where every hard quotient is free of factors <= 5000 are collected by a
segmented sieve over k (n = r + k M), survivors get Miller-Rabin tests,
and full survivors are evaluated exactly (Pollard rho for the leftover
soft terms).  A class is abandoned once psi n + 5040 <= best, and classes
are skipped entirely once psi N + 5040 <= best, which makes the procedure
an exhaustive proof of the maximum, not a heuristic.

The answer comes from n = 9997194587108081, a full nine-fold
constellation: n, n+2, n+6, n+8 prime and (n+1)/6, (n+3)/4, (n+4)/315,
(n+5)/2, (n+7)/24 all prime.

Verified: the exact largest-prime-factor routine against naive
factorisation; the given f(100) = 5, f(101) = 101, g(100) = 409 and
h(100) = 417; the class machinery against a direct segmented
largest-prime-factor sieve at N = 10^7 (seeded with a slightly weakened
bound so it must rediscover the maximum itself); and the same machinery
reproduces the given h(10^9) = 4896292593.
"""

import sys
from math import gcd
from pathlib import Path
from random import randrange

import numpy as np

sys.path.append(str(Path(__file__).parent.parent))
from funcs import prime_sieve_int  # noqa: E402

M = 32 * 27 * 25 * 49  # 1058400
PCAPS = [(2, 5), (3, 3), (5, 2), (7, 2)]
SIEVE_PRIMES = [int(p) for p in prime_sieve_int(5000)]
SIEVE_PRIMES_GE11 = [p for p in SIEVE_PRIMES if p >= 11]
MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in MR_BASES:
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in MR_BASES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    while True:
        c = randrange(1, n)
        x = y = randrange(2, n)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            if x == y:
                break
            d = gcd(abs(x - y), n)
        if 1 < d < n:
            return d


def largest_pf(n: int) -> int:
    """Exact largest prime factor of n >= 2."""
    best = 1
    for p in SIEVE_PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            best = max(best, p)
            n //= p
    stack = [n] if n > 1 else []
    while stack:
        x = stack.pop()
        if x <= best:
            continue
        if is_prime(x):
            best = x
            continue
        d = pollard_rho(x)
        stack += [d, x // d]
    return best


def h_exact(n_limit: int, seg: int = 10**7) -> tuple[int, int]:
    """h(n_limit) and its argmax by a segmented largest-prime-factor sieve."""
    hi = n_limit + 9
    primes = [int(p) for p in prime_sieve_int(int(hi**0.5) + 1)]
    best, bestn = -1, -1
    tailf = None
    for lo in range(2, hi, seg):
        r = min(lo + seg, hi)
        rem = np.arange(lo, r, dtype=np.int64)
        fmax = np.ones(r - lo, dtype=np.int64)
        for p in primes:
            if p * p >= r:
                break
            q = p
            while q < r:
                rem[(-lo) % q :: q] //= p
                q *= p
            s = fmax[(-lo) % p :: p]
            np.maximum(s, p, out=s)
        f = np.where(rem > 1, rem, fmax)
        base = lo
        if tailf is not None:
            f = np.concatenate([tailf, f])
            base = lo - 8
        if len(f) >= 9:
            w = np.lib.stride_tricks.sliding_window_view(f, 9).sum(axis=1)
            ns = base + np.arange(len(w), dtype=np.int64)
            valid = ns <= n_limit
            if valid.any():
                wv = w[valid]
                i = int(np.argmax(wv))
                if int(wv[i]) > best:
                    best, bestn = int(wv[i]), int(ns[valid][i])
        tailf = f[-8:]
    return best, bestn


def build_classes() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Certified smooth parts S[i][r], under-certification flags U, potentials."""
    r = np.arange(M, dtype=np.int64)
    s_tab = np.ones((9, M), dtype=np.int64)
    u_tab = np.zeros((9, M), dtype=bool)
    for i in range(9):
        x = (r + i) % M
        for p, cap in PCAPS:
            q = 1
            for _ in range(cap):
                q *= p
                s_tab[i][x % q == 0] *= p
            u_tab[i] |= x % (p**cap) == 0
    psi = (1.0 / s_tab).sum(axis=0)
    return s_tab, u_tab, psi


def sweep_class(
    r: int,
    s_col: list[int],
    u_col: list[bool],
    n_limit: int,
    best: int,
    bestn: int,
    hard_override: list[int] | None = None,
    max_positions: int | None = None,
    seg: int = 1 << 20,
) -> tuple[int, int]:
    """Descend through class r; sound pruning against the current best."""
    psi = sum(1.0 / x for x in s_col)
    lam = [0.5 if u_col[i] else 10.0 / 11.0 for i in range(9)]
    k_top = (n_limit - r) // M
    if k_top < 0:
        return best, bestn
    roots = {}
    for q in SIEVE_PRIMES_GE11:
        minv = pow(M % q, -1, q)
        roots[q] = [(-(r + i)) % q * minv % q for i in range(9)]
    done = 0
    while k_top >= 0:
        n_hi = r + k_top * M
        if psi * n_hi + 5040 <= best:
            break
        if max_positions is not None and done >= max_positions:
            break
        k_lo = max(0, k_top - seg + 1)
        cnt = k_top - k_lo + 1
        if hard_override is not None:
            hard = hard_override
        else:
            slack = psi - (best - 5040) / n_hi if best > 5040 else 1e18
            hard = [i for i in range(9) if lam[i] / s_col[i] > slack]
        ok = np.ones(cnt, dtype=bool)
        for q in SIEVE_PRIMES_GE11:
            rt = roots[q]
            for i in hard:
                ok[(rt[i] - k_lo) % q :: q] = False
        for kk in np.flatnonzero(ok)[::-1]:
            n = r + (k_lo + int(kk)) * M
            if n < 2:
                continue
            if all(is_prime((n + i) // s_col[i]) for i in hard):
                g = sum(largest_pf(n + i) for i in range(9))
                if g > best:
                    best, bestn = g, n
        done += cnt
        k_top = k_lo - 1
    return best, bestn


def h_machinery(
    n_limit: int,
    classes: tuple[np.ndarray, np.ndarray, np.ndarray],
    best_init: int = 0,
    boot: tuple[int, int] | None = None,
) -> tuple[int, int]:
    s_tab, u_tab, psi = classes
    best, bestn = best_init, -1
    order = np.argsort(-psi)
    if boot:
        for ci in order[: boot[0]]:
            r = int(ci)
            s_col = [int(s_tab[i][r]) for i in range(9)]
            hard = [i for i in range(9) if s_col[i] <= 8]
            best, bestn = sweep_class(
                r, s_col, [bool(u_tab[i][r]) for i in range(9)],
                n_limit, best, bestn,
                hard_override=hard, max_positions=boot[1],
            )
    for ci in order:
        r = int(ci)
        if float(psi[r]) * n_limit + 5040 <= best:
            break
        best, bestn = sweep_class(
            r,
            [int(s_tab[i][r]) for i in range(9)],
            [bool(u_tab[i][r]) for i in range(9)],
            n_limit, best, bestn,
        )
    return best, bestn


def lpf_naive(n: int) -> int:
    best, d = 1, 2
    while d * d <= n:
        while n % d == 0:
            best, n = d, n // d
        d += 1
    return n if n > 1 else best


def main() -> None:
    for x in list(range(2, 500)) + [randrange(2, 10**12) for _ in range(200)]:
        assert largest_pf(x) == lpf_naive(x), x
    assert largest_pf(100) == 5 and largest_pf(101) == 101
    assert sum(largest_pf(100 + i) for i in range(9)) == 409
    assert h_exact(100)[0] == 417

    classes = build_classes()
    exact7, _ = h_exact(10**7)
    got7, _ = h_machinery(10**7, classes, best_init=int(exact7 * 0.999))
    assert got7 == exact7, (got7, exact7)
    got9, _ = h_machinery(10**9, classes, best_init=int(4896292593 * 0.999))
    assert got9 == 4896292593, got9

    best, _ = h_machinery(10**16, classes, boot=(6, 20_000_000))
    print(best)  # 49601160286750947


if __name__ == "__main__":
    main()
