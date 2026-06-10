"""
https://projecteuler.net/problem=553

R(n) is the set of non-empty families of non-empty subsets of
{1..n}; each family X gets a graph with the member sets as vertices
and edges between intersecting sets. C(n, k) counts families whose
graph has exactly k connected components. Find C(10^4, 10) mod
10^9 + 7.

Sets in different components are pairwise disjoint, so the
components' supports partition the union of X. Hence with U(m) the
number of non-empty families of subsets of [m] with union exactly
[m], inclusion-exclusion over the union gives

    U(m) = sum_j (-1)^(m-j) C(m, j) 2^(2^j - 1)

(the empty family cancels), and in exponential generating functions
U = exp(A) - 1 where A is the EGF of *connected* full-support
families, so A = log(1 + U). Splitting [n] into unused elements, the
support, and a partition of the support into k connected blocks:

    C(n, k) = sum_m binom(n, m) * m! [x^m] A(x)^k / k!.

Everything is O(n^2) arithmetic mod p: the inclusion-exclusion table
(with 2^(2^j - 1) reduced via Fermat), the power-series logarithm
recurrence m a_m = m u_m - sum i a_i u_(m-i), and five length-10^4
convolutions for A^10 by binary exponentiation.

Verified against literal enumeration of all families with
union-find component counting for n <= 4 (including the given
C(2,1) = 6, C(3,1) = 111, C(4,2) = 486) and the given
C(100, 10) = 728209718 mod p.
"""

import numba
import numpy as np

P = 1_000_000_007


@numba.njit(cache=True)
def _conv(a: np.ndarray, b: np.ndarray, n: int) -> np.ndarray:
    c = np.zeros(n + 1, dtype=np.int64)
    for i in range(n + 1):
        if a[i] == 0:
            continue
        ai = a[i]
        for j in range(n + 1 - i):
            c[i + j] = (c[i + j] + ai * b[j]) % P
    return c


@numba.njit(cache=True)
def _u_table(n: int, pw: np.ndarray, fact: np.ndarray, inv: np.ndarray) -> np.ndarray:
    u = np.zeros(n + 1, dtype=np.int64)
    for m in range(1, n + 1):
        s = np.int64(0)
        for j in range(m + 1):
            t = fact[m] * inv[j] % P * inv[m - j] % P * pw[j] % P
            s = (s + t) % P if (m - j) % 2 == 0 else (s - t) % P
        u[m] = s % P * inv[m] % P
    return u


@numba.njit(cache=True)
def _log1p(u: np.ndarray, n: int, invs: np.ndarray) -> np.ndarray:
    ell = np.zeros(n + 1, dtype=np.int64)
    for m in range(1, n + 1):
        s = m * u[m] % P
        for i in range(1, m):
            s = (s - i * ell[i] % P * u[m - i]) % P
        ell[m] = s % P * invs[m] % P
    return ell


def c_of(n: int, k: int) -> int:
    fact = np.ones(n + 1, dtype=np.int64)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % P
    inv = np.ones(n + 1, dtype=np.int64)
    inv[n] = pow(int(fact[n]), P - 2, P)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % P
    invs = np.array([0] + [pow(i, P - 2, P) for i in range(1, n + 1)], dtype=np.int64)
    pw = np.array(
        [pow(2, (pow(2, j, P - 1) - 1) % (P - 1), P) for j in range(n + 1)],
        dtype=np.int64,
    )
    u = _u_table(n, pw, fact, inv)
    a = _log1p(u, n, invs)
    b = np.zeros(n + 1, dtype=np.int64)
    b[0] = 1
    e = k
    while e:
        if e & 1:
            b = _conv(b, a, n)
        a = _conv(a, a, n)
        e >>= 1
    ans = 0
    for m in range(n + 1):
        ans = (
            ans + fact[n] * inv[m] % P * inv[n - m] % P * (int(b[m]) * int(fact[m]) % P)
        ) % P
    return ans * pow(int(fact[k]), P - 2, P) % P


def _brute_c(n: int, k: int) -> int:
    sets = list(range(1, 1 << n))
    cnt = 0
    for fam_mask in range(1, 1 << len(sets)):
        fam = [sets[i] for i in range(len(sets)) if fam_mask >> i & 1]
        parent = list(range(len(fam)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(len(fam)):
            for j in range(i + 1, len(fam)):
                if fam[i] & fam[j]:
                    parent[find(i)] = find(j)
        cnt += len({find(i) for i in range(len(fam))}) == k
    return cnt


if __name__ == "__main__":
    assert _brute_c(2, 1) == 6 == c_of(2, 1)  # given
    assert _brute_c(3, 1) == 111 == c_of(3, 1)  # given
    assert _brute_c(4, 2) == 486 == c_of(4, 2)  # given
    assert _brute_c(4, 1) == c_of(4, 1)
    assert _brute_c(4, 3) == c_of(4, 3)
    assert _brute_c(3, 2) == c_of(3, 2)
    assert c_of(100, 10) == 728209718  # given

    print(c_of(10**4, 10))  # 57717170
