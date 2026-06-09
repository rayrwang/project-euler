import math

import numba
import numpy as np

MOD = 977676779


@numba.njit(cache=True)
def _isqrt(n: int) -> int:
    x = int(math.sqrt(n))
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


@numba.njit(cache=True)
def _sieve(limit: int):
    """Linear sieve: Mobius function and primes up to limit."""
    mu = np.zeros(limit + 1, dtype=np.int8)
    comp = np.zeros(limit + 1, dtype=np.uint8)
    primes = np.empty(int(1.3 * limit / max(math.log(limit), 1.0)) + 100,
                      dtype=np.int64)
    np_ = 0
    mu[1] = 1
    for i in range(2, limit + 1):
        if comp[i] == 0:
            primes[np_] = i
            np_ += 1
            mu[i] = -1
        for t in range(np_):
            p = primes[t]
            if i * p > limit:
                break
            comp[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu, primes[:np_]


@numba.njit(cache=True)
def _q_count(y: int, plist, nf: int, mu) -> int:
    """Count squarefree s <= y coprime to the first nf primes in plist.

    Q(y; r) = sum_{d | r} mu(d) sum_{j <= sqrt(y/d), gcd(j, r) = 1}
              mu(j) floor(y / (d j^2)),
    inclusion-exclusion over the (few) primes of r = rad(P), with the
    usual Mobius sieve for squarefreeness restricted to j coprime to r.
    """
    q = 0
    for mask in range(1 << nf):
        d = 1
        sign = 1
        for t in range(nf):
            if mask & (1 << t):
                d *= plist[t]
                sign = -sign
        yd = y // d
        if yd == 0:
            continue
        s = _isqrt(yd)
        nrel = 0
        while nrel < nf and plist[nrel] <= s:
            nrel += 1
        for j in range(1, s + 1):
            m = mu[j]
            if m == 0:
                continue
            ok = True
            for t in range(nrel):
                if j % plist[t] == 0:
                    ok = False
                    break
            if ok:
                q += sign * m * (yd // (j * j))
    return q


@numba.njit(cache=True)
def _weight(plist, elist, nf: int, n_lim: int, mod2: int) -> int:
    """W(P) = sum over odd k in [3, n_lim] of c_k(P), mod mod2.

    Equals ((n_lim - 1) // 2) * c_inf(P) plus corrections from the
    finitely many odd k below the largest exponent of P.
    """
    c_inf = 1
    emax = 0
    for t in range(nf):
        p = plist[t]
        e = elist[t]
        for _ in range(e - 1):
            c_inf *= p
        if e > emax:
            emax = e
    w = ((n_lim - 1) // 2 % mod2) * (c_inf % mod2) % mod2
    if emax >= 4:
        kmax = min(n_lim, 63)
        k = 3
        while k <= kmax:
            ck = 1
            for t in range(nf):
                p = plist[t]
                e = elist[t]
                red = e - (e + k - 1) // k
                for _ in range(red):
                    ck *= p
            w = (w + ck - c_inf) % mod2
            k += 2
    return w


@numba.njit(cache=True)
def _powerful_sum(n_lim: int, primes, mu, mod2: int) -> int:
    """Sum of W(P) * Q(N // P; rad(P)) over all powerful P <= n_lim, mod mod2.

    Powerful numbers are enumerated as a tree: a node is reached from its
    parent either by bumping the exponent of its largest prime or by
    appending a new larger prime squared. Iterative DFS, explicit stack.
    """
    nprimes = len(primes)
    plist = np.zeros(64, dtype=np.int64)
    elist = np.zeros(64, dtype=np.int64)
    f_p = np.zeros(64, dtype=np.int64)      # value of P at this frame
    f_t = np.zeros(64, dtype=np.int64)      # prime index of largest prime
    f_new = np.zeros(64, dtype=np.int64)    # 1 if frame added a new prime
    f_child = np.zeros(64, dtype=np.int64)  # next child: -1 = bump, t2 = extend
    nf = 0  # number of distinct primes of current P
    top = 0
    f_p[0] = 1
    f_t[0] = -1
    f_new[0] = 0
    f_child[0] = 0  # root has no prime to bump
    acc = (_weight(plist, elist, 0, n_lim, mod2)
           * (_q_count(n_lim, plist, 0, mu) % mod2)) % mod2
    while top >= 0:
        big_p = f_p[top]
        c = f_child[top]
        if c == -1:
            # Child 1: bump the exponent of the largest prime.
            f_child[top] = f_t[top] + 1
            p = primes[f_t[top]]
            if big_p <= n_lim // p:
                top += 1
                f_p[top] = big_p * p
                f_t[top] = f_t[top - 1]
                f_new[top] = 0
                f_child[top] = -1
                elist[nf - 1] += 1
                acc = (acc + _weight(plist, elist, nf, n_lim, mod2)
                       * (_q_count(n_lim // f_p[top], plist, nf, mu) % mod2)
                       ) % mod2
            continue
        if c < nprimes and primes[c] <= n_lim // big_p // primes[c]:
            # Child: extend with a new prime primes[c] squared.
            p2 = primes[c]
            f_child[top] = c + 1
            top += 1
            f_p[top] = big_p * p2 * p2
            f_t[top] = c
            f_new[top] = 1
            f_child[top] = -1
            plist[nf] = p2
            elist[nf] = 2
            nf += 1
            acc = (acc + _weight(plist, elist, nf, n_lim, mod2)
                   * (_q_count(n_lim // f_p[top], plist, nf, mu) % mod2)
                   ) % mod2
            continue
        # No more children: pop.
        if f_new[top] == 1:
            nf -= 1
        elif f_t[top] >= 0:
            elist[nf - 1] -= 1
        top -= 1
    return acc


def floor_s_mod(n_lim: int) -> int:
    """floor(S(n_lim)) mod MOD.

    For odd k, pairing i <-> n - i gives f_k(n) = (n - c_k(n)) / 2 with
    c_k(n) = #{i <= n : n | i^k}, multiplicative, c_k(p^e) = p^(e - ceil(e/k)).
    Writing n = P * s (powerful part times coprime squarefree part) gives
    c_k(n) = c_k(P), so summing over n <= N is a sum over powerful P of
    c_k(P) times the count of squarefree s <= N/P coprime to rad(P).
    Everything is computed mod 2 * MOD so the final halving (and the floor,
    i.e. the parity of the numerator) is exact.
    """
    mod2 = 2 * MOD
    mu, primes = _sieve(math.isqrt(n_lim))
    sig = _powerful_sum(n_lim, primes, mu, mod2)
    sigma = (n_lim + sig) % mod2  # add C_1(N) = N for k = 1
    k_cnt = ((n_lim + 1) // 2) % mod2
    tri = (n_lim * (n_lim + 1) // 2) % mod2
    x = (k_cnt * tri - sigma) % mod2
    return (x - (x & 1)) // 2 % MOD


if __name__ == "__main__":
    assert floor_s_mod(10) == 100  # S(10) = 100.5
    assert floor_s_mod(1000) == 123687804
    print(floor_s_mod(33557799775533))  # 878255725
