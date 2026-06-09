import numba
import numpy as np

MOD = 998244353


@numba.njit(cache=True)
def _apply_factors(f: np.ndarray, ks: np.ndarray, n: int) -> None:
    """Multiply the series f by prod 1/(1 - q^k) over k in ks, mod MOD."""
    for k in ks:
        for i in range(k, n + 1):
            f[i] = (f[i] + f[i - k]) % MOD


def _mul_sparse(f: np.ndarray, k: int, sign: int, n: int) -> None:
    """Multiply f by (1 + sign * q^k) in place."""
    f[k:] = (f[k:] + sign * f[: n + 1 - k]) % MOD


def _div_sparse(f: np.ndarray, k: int, sign: int, n: int) -> None:
    """Divide f by (1 - sign * q^k) in place."""
    for i in range(k, n + 1):
        f[i] = (f[i] + sign * f[i - k]) % MOD


def count_dynamical(n: int) -> int:
    """S(n): monic integer f of degree n with f(x) | f(x^2 - 2), mod MOD.

    Roots of such f must have finite forward orbit under phi: x -> x^2 - 2.
    Conjugating by x = z + 1/z turns phi into z -> z^2, whose preperiodic
    points are roots of unity, so every root is 2 cos(2 pi k/m): f is a
    product of the minimal polynomials psi_m of 2 cos(2 pi/m), of degree
    d_m = phi(m)/2 for m >= 3 (and 1 for m = 1, 2). Angle doubling maps the
    root class m to m (m odd) or m/2 (m even), so divisibility constrains
    the multiplicities e along each doubling chain m, 2m, 4m, ... (m odd):
    e_(2m') <= e_(m'), except e_4 <= 2 e_2 because the fibre of -2 is the
    double root 0. Odd classes are unconstrained cycle classes.

    A weakly decreasing chain with degree prefix sums D_j contributes
    prod_j 1/(1 - q^(D_j)); for odd m >= 3 the prefix sums are
    d, 2d, 4d, ... with d = phi(m)/2. The m = 1 chain (degrees 1, 1, 1, 2,
    4, ...) needs the doubled link: summing out e_1 and e_2 leaves weight
    q^(2 ceil(C/2) + C) for C = e_4 over a decreasing tail; writing C as a
    sum of differences t_j with weights 2^(j+1) and splitting on the parity
    of C gives
        P_1 = [(1+q) prod_j (1 - q^(2^(j+1)))^(-1)
               + (1-q) prod_j (1 + q^(2^(j+1)))^(-1)] / (2 (1-q)(1-q^2)).
    The answer is [q^n] of P_1 times the product over odd chains.
    """
    # All odd m >= 3 with phi(m)/2 <= n (largest such m is < 5n for n >= 20).
    lim = max(6 * n, 200)
    phi = np.arange(lim + 1)
    for p in range(2, lim + 1):
        if phi[p] == p:
            phi[p::p] -= phi[p::p] // p

    ks = []
    for m in range(3, lim + 1, 2):
        d = int(phi[m]) // 2
        while d <= n:
            ks.append(d)
            d *= 2
    assert all(int(phi[m]) // 2 > n for m in range(lim - 1, lim - 60, -2))

    f = np.zeros(n + 1, dtype=np.int64)
    f[0] = 1
    _apply_factors(f, np.array(sorted(ks), dtype=np.int64), n)

    # P_1 for the m = 1 chain.
    a = np.zeros(n + 1, dtype=np.int64)
    a[0] = 1
    b = a.copy()
    k = 2
    while k <= n:
        _div_sparse(a, k, 1, n)
        _div_sparse(b, k, -1, n)
        k *= 2
    _mul_sparse(a, 1, 1, n)
    _mul_sparse(b, 1, -1, n)
    p1 = (a + b) * pow(2, MOD - 2, MOD) % MOD
    _div_sparse(p1, 1, 1, n)
    _div_sparse(p1, 2, 1, n)

    return int(np.sum(f * p1[::-1] % MOD) % MOD)


if __name__ == "__main__":
    assert count_dynamical(2) == 6
    assert count_dynamical(5) == 58
    assert count_dynamical(20) == 122087
    print(count_dynamical(10_000))  # 986262698
