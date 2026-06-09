import numba
import numpy as np

from funcs import prime_sieve_int

P = 10**9 + 7

@numba.jit(cache=True)
def dsum(M: int) -> int:
    """sum_{m<=M} sigma0(m) mod P, by the divisor hyperbola: 2*sum floor(M/i) - r^2."""
    r = int(M**0.5)
    while (r + 1) * (r + 1) <= M:
        r += 1
    while r * r > M:
        r -= 1
    s = 0
    for i in range(1, r + 1):
        s += M // i
        if s >= (1 << 62):
            s %= P
    return (2 * (s % P) - r % P * (r % P)) % P

@numba.jit(cache=True)
def dfs(idx: int, e: int, wmul: int, primes: np.ndarray, ratio: np.ndarray, n: int) -> int:
    """Sum of wmul * dsum(n//e) over this node and all squarefree extensions e*p<=n."""
    total = wmul * dsum(n // e) % P
    for j in range(idx, len(primes)):
        ej = e * primes[j]
        if ej <= n:
            total = (total + dfs(j + 1, ej, wmul * ratio[j] % P, primes, ratio, n)) % P
        else:
            break
    return total

def solve(maxfact: int, n: int) -> int:
    """D(maxfact!, n) mod 10^9+7.

    With a_p = v_p(m), sum_{d|m} sigma0(k d) = prod_p h_p(v_p(k)),
    h_p(e) = C(a_p+2,2) + (a_p+1) e. Dirichlet convolution turns the sum over k
    into D = sum_e W(e) * dsum(floor(n/e)), where e ranges over squarefree products
    of distinct primes dividing m, dsum is the divisor-summatory function, and
        W(e) = prod_{p|e} (-C(a_p+1,2)) * prod_{p|m, p!|e} C(a_p+2,2).
    Factor out base = prod_p C(a_p+2,2); each chosen prime contributes the ratio
    -C(a_p+1,2)/C(a_p+2,2) = -a_p/(a_p+2).
    """
    primes = [int(p) for p in prime_sieve_int(maxfact + 1)]
    a = {}
    for p in primes:
        e, pk = 0, p
        while pk <= maxfact:
            e += maxfact // pk
            pk *= p
        a[p] = e
    base = 1
    ratio = []
    for p in primes:
        ap = a[p]
        base = base * ((ap + 1) * (ap + 2) // 2 % P) % P
        ratio.append((-ap % P) * pow(ap + 2, P - 2, P) % P)
    parr = np.array(primes, dtype=np.int64)
    rarr = np.array(ratio, dtype=np.int64)
    acc = dfs(0, 1, 1, parr, rarr, n)
    return base * acc % P

if __name__ == "__main__":
    print(solve(200, 10**12))  # 439689828
