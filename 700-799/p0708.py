import numba
import numpy as np

from funcs import prime_sieve_int

@numba.njit(cache=True)
def divisor_summatory(m):
    """D(m) = sum_{i=1}^{m} floor(m/i) = sum_{k<=m} d(k), by the hyperbola method:
    D(m) = 2 * sum_{i<=sqrt(m)} floor(m/i) - floor(sqrt(m))^2."""
    if m <= 0:
        return 0
    k = int(m**0.5)
    while (k + 1) * (k + 1) <= m:
        k += 1
    while k * k > m:
        k -= 1
    s = 0
    for i in range(1, k + 1):
        s += m // i
    return 2 * s - k * k

@numba.njit(cache=True)
def total_sum(n, primes):
    """sum over squarefull e <= N of h(e) * D(floor(N/e)).

    Since 2^Omega = 1 * 1 * h with h supported on squarefull numbers and
    h(p^k) = 2^(k-2), this equals sum_{n<=N} 2^Omega(n). The squarefull e are
    enumerated by an explicit depth-first stack over primes (each taken to an
    exponent of at least two); the recursion depth never exceeds the number of
    distinct primes in e, so a small fixed-size frame stack suffices.
    """
    npr = len(primes)
    maxd = 64
    fidx = np.empty(maxd, np.int64)
    fval = np.empty(maxd, np.int64)
    fh = np.empty(maxd, np.int64)
    fj = np.empty(maxd, np.int64)
    fk = np.empty(maxd, np.int64)
    fcur = np.empty(maxd, np.int64)

    acc = 0
    d = 0
    fidx[0] = 0
    fval[0] = 1
    fh[0] = 1
    acc += fh[0] * divisor_summatory(n // fval[0])
    fj[0] = 0
    fk[0] = 0
    while d >= 0:
        made_child = False
        while True:
            if fk[d] == 0:
                if fj[d] >= npr:
                    break
                p = primes[fj[d]]
                # p <= sqrt(N) so p * p does not overflow; compare via division
                # to avoid overflowing fval * p * p.
                if p * p > n // fval[d]:
                    break
                fcur[d] = fval[d] * p * p
                fk[d] = 2
            else:
                p = primes[fj[d]]
                if fcur[d] > n // p:
                    fj[d] += 1
                    fk[d] = 0
                    continue
                fcur[d] = fcur[d] * p
                fk[d] += 1
            made_child = True
            break
        if not made_child:
            d -= 1
            continue
        cd = d + 1
        fidx[cd] = fj[d] + 1
        fval[cd] = fcur[d]
        fh[cd] = fh[d] * (1 << (fk[d] - 2))
        acc += fh[cd] * divisor_summatory(n // fval[cd])
        fj[cd] = fidx[cd]
        fk[cd] = 0
        d = cd
    return acc

def S(n):
    primes = prime_sieve_int(int(n**0.5) + 1)
    return total_sum(n, primes)

if __name__ == "__main__":
    print(S(10**14))  # 28874142998632109
