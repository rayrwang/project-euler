import numba
import numpy as np

MOD = 1_020_202_009

@numba.njit(cache=True)
def egf(n, inv):
    """f(n) = n! * [x^n] exp(T), where T' = cosh(T) is the EGF of even-branching
    increasing trees. With C = cosh(T) and S = sinh(T):
        T' = C,  S' = C^2,  C' = S C,  E' = C E  (E = exp T),
    giving the coefficient recurrences below. All work is modulo the prime MOD,
    so each division by (m + 1) is a multiplication by its inverse.
    """
    t = np.zeros(n + 1, np.int64)
    c = np.zeros(n + 1, np.int64)
    s = np.zeros(n + 1, np.int64)
    e = np.zeros(n + 1, np.int64)
    c[0] = 1
    e[0] = 1
    for m in range(n):
        cc = 0  # sum_i c_i c_{m-i}
        sc = 0  # sum_i s_i c_{m-i}
        ce = 0  # sum_i c_i e_{m-i}
        for i in range(m + 1):
            ci = c[i]
            cc = (cc + ci * c[m - i]) % MOD
            sc = (sc + s[i] * c[m - i]) % MOD
            ce = (ce + ci * e[m - i]) % MOD
        im = inv[m + 1]
        t[m + 1] = c[m] * im % MOD
        s[m + 1] = cc * im % MOD
        c[m + 1] = sc * im % MOD
        e[m + 1] = ce * im % MOD
    fact = 1
    for k in range(2, n + 1):
        fact = fact * k % MOD
    return fact * e[n] % MOD

def F(n):
    inv = np.empty(n + 2, np.int64)
    inv[1] = 1
    for i in range(2, n + 2):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD
    return egf(n, inv)

if __name__ == "__main__":
    print(F(24680))  # 773479144
