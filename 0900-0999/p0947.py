"""Project Euler 947: Fibonacci Residues.

The pair (g(n), g(n+1)) evolves under the matrix Q = [[0,1],[1,1]] modulo m,
so p(a, b, m) is the orbit length of v = (a, b), the minimal t with
(Q^t - I) v = 0 (mod m); it divides the Pisano period pi(m) = ord(Q mod m).
With K(e) = #ker(Q^e - I mod m), the number of v of exact period d is
sum_{e | d} mu(d/e) K(e), and Mobius reorganization gives

    s(m) = sum_{e | pi(m)} K(e) e^2 prod_{l | pi(m)/e} (1 - l^2).

K is multiplicative over the prime powers q^c of m by CRT, and modulo q^c
it depends on e only through gcd(e, pi(q^c)). For a 2x2 integer matrix the
kernel size mod q^c is gcd(s1, q^c) gcd(s2, q^c) with s1 = gcd of entries
and s1 s2 = |det|; here Q^e - I has entries built from Fibonacci numbers
and det (-1)^e + 1 - L_e, so each kernel size is a small Fibonacci
computation. Three regimes keep this fast:

* q > 1000, c = 1, with 5 a quadratic residue (q = +-1 mod 5): Q has unit
  eigenvalues lambda, mu = (1 +- sqrt 5)/2 mod q, each fixing its eigenline
  iff its order divides e, so kappa_q(e) = q^([A|e] + [B|e]) where A, B are
  the two orders (Tonelli-Shanks square root plus order finding via the
  factored q - 1).
* q > 1000, c = 1, 5 a non-residue: Q is semisimple with conjugate
  eigenvalues in F_{q^2}, so the kernel is trivial except at e = pi(q)
  where it is everything: kappa = q^2 exactly when pi(q) | e.
* q <= 1000 or c >= 2 (includes q = 2, 5): a precomputed table of kernel
  sizes for every divisor of pi(q^c), via Fibonacci fast doubling modulo
  q^(2c) (which fits in 64 bits after a split-multiplication trick), and
  the main loop looks up gcd(e, pi(q^c)) by binary search.

The main loop merges the factorizations of the local Pisano periods into
pi(m), walks its divisors e (36.6 million across all m <= 10^6), forms K(e)
from the per-prime data and accumulates the answer mod 999999893. Verified
against brute-force orbit enumeration of s(m) for all m <= 60 and the given
s(3) = 513, s(10) = 225820, S(3) = 542, S(10) = 310897.
"""

import numba
import numpy as np

MOD = 999999893
M = 10**6
SMALLQ = 1000  # primes up to this (or any c >= 2) get explicit tables


@numba.njit(cache=True)
def spf_sieve(n):
    spf = np.zeros(n + 1, np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


@numba.njit(cache=True)
def mulmod_big(a, b, m):
    """a*b mod m for m < 2^42 via 21-bit split (int64-safe)."""
    a %= m
    b %= m
    hi = a >> 21
    lo = a & ((1 << 21) - 1)
    return ((hi * b % m) << 21) % m + lo * b % m


@numba.njit(cache=True)
def fib_pair_big(n, m):
    """(F_n, F_{n+1}) mod m, fast doubling, m < 2^42."""
    a, b = np.int64(0), np.int64(1)
    if n == 0:
        return a, b
    bit = np.int64(1)
    while bit <= n:
        bit <<= 1
    bit >>= 1
    while bit:
        t = (2 * b - a) % m
        c = mulmod_big(a, t, m) % m
        d = (mulmod_big(a, a, m) + mulmod_big(b, b, m)) % m
        if n & bit:
            a, b = d, (c + d) % m
        else:
            a, b = c, d
        bit >>= 1
    return a % m, b % m


@numba.njit(cache=True)
def powmod(b, e, m):
    r = np.int64(1)
    b %= m
    while e > 0:
        if e & 1:
            r = r * b % m
        b = b * b % m
        e >>= 1
    return r


@numba.njit(cache=True)
def factor_into(n, spf, pr, ex):
    k = 0
    while n > 1:
        q = spf[n]
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        pr[k] = q
        ex[k] = e
        k += 1
    return k


@numba.njit(cache=True)
def order_div(base, n, q, spf, pr, ex):
    """Multiplicative order of base mod q, given it divides n."""
    k = factor_into(n, spf, pr, ex)
    d = n
    for i in range(k):
        for _ in range(ex[i]):
            if powmod(base, d // pr[i], q) == 1:
                d //= pr[i]
            else:
                break
    return d


@numba.njit(cache=True)
def fib_order(n, q, spf, pr, ex):
    """Smallest d | n with Q^d = I mod q (Pisano period given pi | n)."""
    k = factor_into(n, spf, pr, ex)
    d = n
    for i in range(k):
        for _ in range(ex[i]):
            a, b = fib_pair_big(d // pr[i], q)
            if a == 0 and b == 1:
                d //= pr[i]
            else:
                break
    return d


@numba.njit(cache=True)
def sqrtmod(a, p):
    """Tonelli-Shanks square root of a mod odd prime p (a a QR)."""
    a %= p
    if a == 0:
        return np.int64(0)
    if p % 4 == 3:
        return powmod(a, (p + 1) // 4, p)
    s = np.int64(0)
    qq = p - 1
    while qq % 2 == 0:
        qq //= 2
        s += 1
    z = np.int64(2)
    while powmod(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m = s
    c = powmod(z, qq, p)
    t = powmod(a, qq, p)
    r = powmod(a, (qq + 1) // 2, p)
    while t != 1:
        t2 = t
        i = np.int64(0)
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = powmod(c, np.int64(1) << (m - i - 1), p)
        m = i
        c = b * b % p
        t = t * c % p
        r = r * b % p
    return r


@numba.njit(cache=True)
def kernel_size(d, qc, q2c, q, c):
    """#ker(Q^d - I mod q^c) via Smith form, Fibonacci mod q^(2c)."""
    fd, fd1 = fib_pair_big(d, q2c)  # F_d, F_{d+1}
    fdm1 = (fd1 - fd) % q2c  # F_{d-1}
    # s1 valuation: v_q(gcd(F_d, F_{d-1} - 1)) capped at c
    e11 = (fdm1 - 1) % q2c
    e22 = (fd1 - 1) % q2c
    v1 = 0
    x, y = fd, e11
    while v1 < c and x % q == 0 and y % q == 0:
        x //= q
        y //= q
        v1 += 1
    # det = e11*e22 - fd^2 mod q^(2c)
    det = (mulmod_big(e11, e22, q2c) - mulmod_big(fd, fd, q2c)) % q2c
    if det == 0:
        v2 = c  # v_q(det) >= 2c, so v_q(s2) >= 2c - v1 >= c
    else:
        vd = 0
        t = det
        while t % q == 0:
            t //= q
            vd += 1
        v2 = vd - v1
        if v2 > c:
            v2 = c
    p1 = np.int64(1)
    for _ in range(v1):
        p1 *= q
    for _ in range(v2):
        p1 *= q
    return p1


@numba.njit(cache=True)
def solve_all(big_m, spf):
    pr = np.zeros(16, np.int64)
    ex = np.zeros(16, np.int64)
    # --- Pisano periods of primes ---
    pip = np.zeros(big_m + 1, np.int64)
    for p in range(2, big_m + 1):
        if spf[p] == p:
            if p == 2:
                pip[p] = 3
            elif p == 5:
                pip[p] = 20
            else:
                if p % 5 == 1 or p % 5 == 4:
                    n0 = np.int64(p - 1)
                else:
                    n0 = np.int64(2 * (p + 1))
                pip[p] = fib_order(n0, np.int64(p), spf, pr, ex)
    # --- split primes q > SMALLQ: eigenvalue orders A, B ---
    ordA = np.zeros(big_m + 1, np.int64)
    ordB = np.zeros(big_m + 1, np.int64)
    for p in range(SMALLQ + 1, big_m + 1):
        if spf[p] == p and (p % 5 == 1 or p % 5 == 4):
            r5 = sqrtmod(np.int64(5), np.int64(p))
            lam = (1 + r5) % p * ((p + 1) // 2) % p
            mu = (1 - r5) % p * ((p + 1) // 2) % p
            ordA[p] = order_div(lam, np.int64(p - 1), np.int64(p), spf, pr, ex)
            ordB[p] = order_div(mu, np.int64(p - 1), np.int64(p), spf, pr, ex)
    # --- tables for q <= SMALLQ or c >= 2 ---
    # enumerate prime powers q^c <= big_m with q <= SMALLQ for all c, plus
    # q > SMALLQ with c >= 2 (then q <= 1000 anyway since q^2 <= 10^6) --
    # so simply: all q <= SMALLQ, all c with q^c <= big_m.
    # store: for prime power index, sorted divisors of pi(q^c) and kernels.
    max_pp = 0
    for q in range(2, SMALLQ + 1):
        if spf[q] == q:
            qc = q
            while qc <= big_m:
                max_pp += 1
                qc *= q
    tab_qc = np.zeros(max_pp + 1, np.int64)
    tab_pi = np.zeros(max_pp + 1, np.int64)
    tab_off = np.zeros(max_pp + 2, np.int64)
    pp_index = np.zeros(big_m + 1, np.int32)  # q^c -> table row
    # first pass: compute pi(q^c) and divisor counts
    npp = 0
    total_div = 0
    for q in range(2, SMALLQ + 1):
        if spf[q] != q:
            continue
        qc = np.int64(q)
        c = 1
        piq = pip[q]
        while qc <= big_m:
            if c > 1:
                # pi(q^c) divides pi(q^(c-1)) * q; find exactly
                piq = fib_order(piq * q, qc, spf, pr, ex)
            tab_qc[npp] = qc
            tab_pi[npp] = piq
            pp_index[qc] = npp
            k = factor_into(piq, spf, pr, ex)
            nd = 1
            for i in range(k):
                nd *= ex[i] + 1
            tab_off[npp + 1] = tab_off[npp] + nd
            total_div += nd
            npp += 1
            qc *= q
            c += 1
    tab_div = np.zeros(total_div, np.int64)
    tab_ker = np.zeros(total_div, np.int64)
    for ipp in range(npp):
        qc = tab_qc[ipp]
        piq = tab_pi[ipp]
        q = np.int64(spf[qc])
        c = 0
        t = qc
        while t > 1:
            t //= q
            c += 1
        q2c = qc * qc
        # generate sorted divisors of piq
        k = factor_into(piq, spf, pr, ex)
        off = tab_off[ipp]
        nd = tab_off[ipp + 1] - off
        tab_div[off] = 1
        cnt = 1
        for i in range(k):
            base = cnt
            mult = np.int64(1)
            for _ in range(ex[i]):
                mult *= pr[i]
                for j in range(base):
                    tab_div[off + cnt] = tab_div[off + j] * mult
                    cnt += 1
        # sort (insertion: nd small)
        for i in range(1, nd):
            key = tab_div[off + i]
            j = i - 1
            while j >= 0 and tab_div[off + j] > key:
                tab_div[off + j + 1] = tab_div[off + j]
                j -= 1
            tab_div[off + j + 1] = key
        for i in range(nd):
            tab_ker[off + i] = kernel_size(tab_div[off + i], qc, q2c, q, c)
    # --- main loop over m ---
    ans = np.int64(1)  # s(1) = 1
    mpr = np.zeros(8, np.int64)  # prime powers q^c of m (value q^c)
    mq = np.zeros(8, np.int64)  # the primes q
    mpi = np.zeros(8, np.int64)  # pi(q^c)
    ell = np.zeros(24, np.int64)  # primes of pi(m)
    elx = np.zeros(24, np.int64)  # exponents
    jj = np.zeros(24, np.int64)  # current divisor exponent vector
    pw = np.zeros(24, np.int64)  # current prime power value
    for m in range(2, big_m + 1):
        # factor m into prime powers; build pi(m) factorization merge
        nq = 0
        x = m
        nl = 0
        while x > 1:
            q = np.int64(spf[x])
            c = 0
            qc = np.int64(1)
            while x % q == 0:
                x //= q
                c += 1
                qc *= q
            piq = pip[q]
            if c >= 2:
                piq = tab_pi[pp_index[qc]]
            mpr[nq] = qc
            mq[nq] = q
            mpi[nq] = piq
            nq += 1
            # merge factorization of piq
            y = piq
            while y > 1:
                ll = np.int64(spf[y])
                e = 0
                while y % ll == 0:
                    y //= ll
                    e += 1
                found = False
                for i in range(nl):
                    if ell[i] == ll:
                        if elx[i] < e:
                            elx[i] = e
                        found = True
                        break
                if not found:
                    ell[nl] = ll
                    elx[nl] = e
                    nl += 1
        # enumerate divisors e of pi(m) by exponent vectors (odometer)
        for i in range(nl):
            jj[i] = 0
            pw[i] = 1
        sm = np.int64(0)
        while True:
            e = np.int64(1)
            for i in range(nl):
                e *= pw[i]
            # J(pi/e) = prod over l with jj < elx of (1 - l^2) mod MOD
            jfac = np.int64(1)
            for i in range(nl):
                if jj[i] < elx[i]:
                    jfac = jfac * ((1 - ell[i] * ell[i]) % MOD) % MOD
            # K(e) = prod over prime powers of m
            kk = np.int64(1)
            for i in range(nq):
                q = mq[i]
                qc = mpr[i]
                if qc == q and q > SMALLQ:
                    if q % 5 == 1 or q % 5 == 4:
                        t = np.int64(1)
                        if e % ordA[q] == 0:
                            t *= q
                        if e % ordB[q] == 0:
                            t *= q
                        kk *= t
                    else:
                        if e % mpi[i] == 0:
                            kk *= q * q
                else:
                    ipp = pp_index[qc]
                    piq = tab_pi[ipp]
                    g = np.int64(e % piq)
                    # gcd(e, piq): since we want gcd of e with piq
                    a = piq
                    b = g
                    while b:
                        a, b = b, a % b
                    g = a
                    off = tab_off[ipp]
                    hi2 = tab_off[ipp + 1] - 1
                    lo2 = off
                    while lo2 < hi2:
                        mid = (lo2 + hi2) // 2
                        if tab_div[mid] < g:
                            lo2 = mid + 1
                        else:
                            hi2 = mid
                    kk *= tab_ker[lo2]
            term = kk % MOD * ((e % MOD) * (e % MOD) % MOD) % MOD
            sm = (sm + term * jfac) % MOD
            # odometer increment
            pos = 0
            while pos < nl:
                if jj[pos] < elx[pos]:
                    jj[pos] += 1
                    pw[pos] *= ell[pos]
                    break
                jj[pos] = 0
                pw[pos] = 1
                pos += 1
            if pos == nl:
                break
        ans = (ans + sm) % MOD
    return ans % MOD


def solve() -> int:
    spf = spf_sieve(7 * M)
    return int(solve_all(M, spf))


if __name__ == "__main__":
    print(solve())  # 213731313
