import numba
import numpy as np

MOD = 10**9
PRIMES = (2, 3, 5, 7, 11, 13, 17)  # 510510 = product of the first seven primes

@numba.jit(cache=True)
def phi_lattice(m: int, ll: int, mod: int) -> tuple[np.ndarray, np.ndarray]:
    """Totient summatory function Phi(x)=sum_{i<=x} phi(i) over the quotient
    lattice of m, reduced mod `mod`.

    Returns (pre, big): pre[x]=Phi(x) for x<=ll (sieved prefix sums); and
    big[i]=Phi(floor(m/i)) for the large values floor(m/i)>ll.
    """
    phi = np.arange(ll + 1, dtype=np.int64)
    for i in range(2, ll + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, ll + 1, i):
                phi[j] -= phi[j] // i
    pre = np.zeros(ll + 1, dtype=np.int64)
    s = 0
    for i in range(1, ll + 1):
        s = (s + phi[i]) % mod
        pre[i] = s

    k = m // ll
    big = np.zeros(k + 1, dtype=np.int64)
    for i in range(k, 0, -1):
        v = m // i
        # exact v(v+1)/2 mod, taking the even factor before halving
        if v % 2 == 0:
            t0 = ((v // 2) % mod) * ((v + 1) % mod) % mod
        else:
            t0 = (v % mod) * (((v + 1) // 2) % mod) % mod
        ssum = 0
        d = 2
        while d <= v:
            q = v // d
            d2 = v // q
            cnt = d2 - d + 1
            pq = pre[q] if q <= ll else big[m // q]
            ssum = (ssum + (cnt % mod) * pq) % mod
            d = d2 + 1
        big[i] = ((t0 - ssum) % mod + mod) % mod
    return pre, big

def totient_product_sum(m: int, ll: int) -> int:
    """S(510510, m) mod 10^9 via T(n,m)=sum_{i<=m} phi(n i).

    With n squarefree and smallest prime factor p, peeling p gives
    T(n,m) = (p-1) T(n/p, m) + T(n, floor(m/p)),  bottoming out at
    T(1, m) = Phi(m).
    """
    pre, big = phi_lattice(m, ll, MOD)

    def phi_sum(x: int) -> int:
        return int(pre[x]) if x <= ll else int(big[m // x])

    memo: dict[tuple[int, int], int] = {}

    def t(j: int, x: int) -> int:
        if x == 0:
            return 0
        if j == len(PRIMES):
            return phi_sum(x)
        key = (j, x)
        cached = memo.get(key)
        if cached is not None:
            return cached
        p = PRIMES[j]
        res = ((p - 1) * t(j + 1, x) + t(j, x // p)) % MOD
        memo[key] = res
        return res

    return t(0, m) % MOD

if __name__ == "__main__":
    assert totient_product_sum(10**6, 10**4) == 45480596821125120 % MOD
    print(totient_product_sum(10**11, 21_600_000))  # 754862080
