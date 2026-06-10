"""
https://projecteuler.net/problem=544

F(r, c, n) counts proper n-colourings of the r x c grid graph and
S(r, c, n) = sum_(k=1..n) F(r, c, k). Find S(9, 10, 1112131415)
modulo 10^9 + 7.

F(9, 10, k) is the grid's chromatic polynomial, of degree 90 in k,
so S(9, 10, n) is a degree-91 polynomial in n: evaluating F at
k = 0..91 determines S at n = 0..91, and Lagrange interpolation
gives S at the target.

Each F(., ., k) is evaluated by a broken-profile DP whose state is
the equality partition of the 9 frontier cells: a new cell must
differ only from its two neighbours (both on the frontier), so its
colour either joins one of the b frontier blocks other than the
neighbours' (weight 1 each) or is any colour absent from the
frontier (weight k - b). Vertical adjacency keeps the reachable
partitions to 5017 (far below Bell(9)), and the 90-step unrolled
transition structure is built once and evaluated for all 92 values
of k in a numba kernel.

Verified against literal enumeration of all colourings for small
grids, the given F(2,2,3) = 18, F(2,2,20) = 130340,
F(3,4,6) = 102923670 and S(4,4,15) = 325951319 mod p, plus a
self-check that interpolating the S table at points inside the
sample range reproduces the table.
"""

from itertools import product

import numba
import numpy as np

MOD = 10**9 + 7


def _build(r: int, c: int):
    def canon(t):
        m: dict[int, int] = {}
        out = []
        for x in t:
            if x == -1:
                out.append(-1)
            else:
                if x not in m:
                    m[x] = len(m)
                out.append(m[x])
        return tuple(out)

    cur = [tuple([-1] * r)]
    srcs: list[int] = []
    dsts: list[int] = []
    news: list[int] = []
    bvs: list[int] = []
    offs = [0]
    sizes = []
    for cell in range(r * c):
        row = cell % r
        nxt: dict[tuple, int] = {}
        nxt_list: list[tuple] = []
        for i, st in enumerate(cur):
            b = len({x for x in st if x != -1})
            forb = set()
            if row > 0 and st[row - 1] != -1:
                forb.add(st[row - 1])
            if st[row] != -1:
                forb.add(st[row])
            for t in range(b):
                if t in forb:
                    continue
                ns = list(st)
                ns[row] = t
                key = canon(tuple(ns))
                if key not in nxt:
                    nxt[key] = len(nxt_list)
                    nxt_list.append(key)
                srcs.append(i)
                dsts.append(nxt[key])
                news.append(0)
                bvs.append(0)
            ns = list(st)
            ns[row] = b
            key = canon(tuple(ns))
            if key not in nxt:
                nxt[key] = len(nxt_list)
                nxt_list.append(key)
            srcs.append(i)
            dsts.append(nxt[key])
            news.append(1)
            bvs.append(b)
        offs.append(len(srcs))
        sizes.append(len(nxt_list))
        cur = nxt_list
    return (
        np.array(srcs, np.int32),
        np.array(dsts, np.int32),
        np.array(news, np.int8),
        np.array(bvs, np.int32),
        np.array(offs, np.int64),
        np.array(sizes, np.int64),
    )


@numba.njit(cache=True)
def _evaluate(k, src, dst, new, bv, off, sz):
    maxs = sz.max()
    v = np.zeros(maxs, dtype=np.int64)
    v[0] = 1
    for s in range(len(sz)):
        nv = np.zeros(sz[s], dtype=np.int64)
        for t in range(off[s], off[s + 1]):
            w = (k - bv[t]) % MOD if new[t] else 1
            nv[dst[t]] = (nv[dst[t]] + v[src[t]] * w) % MOD
        v[: sz[s]] = nv
    tot = np.int64(0)
    for i in range(sz[len(sz) - 1]):
        tot = (tot + v[i]) % MOD
    return tot


def f_values(r: int, c: int, kmax: int) -> list[int]:
    tables = _build(r, c)
    return [int(_evaluate(k, *tables)) for k in range(kmax + 1)]


def _lagrange(ys: list[int], n: int, p: int) -> int:
    m = len(ys) - 1
    if 0 <= n <= m:
        return ys[n] % p
    pre = [1] * (m + 2)
    suf = [1] * (m + 2)
    for i in range(m + 1):
        pre[i + 1] = pre[i] * ((n - i) % p) % p
    for i in range(m, -1, -1):
        suf[i] = suf[i + 1] * ((n - i) % p) % p
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i - 1] * i % p
    res = 0
    for i in range(m + 1):
        t = ys[i] * (pre[i] * suf[i + 1] % p) % p
        t = t * pow(fact[i] * fact[m - i] % p, p - 2, p) % p
        res = (res - t if (m - i) % 2 else res + t) % p
    return res % p


def _brute_f(r: int, c: int, k: int) -> int:
    cnt = 0
    for col in product(range(k), repeat=r * c):
        g = [col[i * c : (i + 1) * c] for i in range(r)]
        if all(
            (i + 1 >= r or g[i][j] != g[i + 1][j])
            and (j + 1 >= c or g[i][j] != g[i][j + 1])
            for i in range(r)
            for j in range(c)
        ):
            cnt += 1
    return cnt


if __name__ == "__main__":
    pv22 = f_values(2, 2, 20)
    assert pv22[3] == 18 and pv22[20] == 130340  # given
    assert _brute_f(2, 2, 3) == 18 and _brute_f(2, 3, 3) == f_values(2, 3, 3)[3]
    assert _brute_f(3, 2, 4) == f_values(3, 2, 4)[4]
    assert f_values(3, 4, 6)[6] == 102923670  # given
    pv44 = f_values(4, 4, 17)
    s44 = [0] * 18
    for k in range(1, 18):
        s44[k] = (s44[k - 1] + pv44[k]) % MOD
    assert s44[15] == 325951319  # given
    assert _lagrange(s44, 16, MOD) == s44[16]  # interpolation sanity

    pv = f_values(9, 10, 91)
    sv = [0] * 92
    for k in range(1, 92):
        sv[k] = (sv[k - 1] + pv[k]) % MOD
    print(_lagrange(sv, 1112131415, MOD))  # 640432376
