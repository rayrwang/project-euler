"""
https://projecteuler.net/problem=554

A centaur moves like a king or a knight. At most n^2 non-attacking
centaurs fit on a 2n x 2n board; C(n) counts the maximum placements.
Find sum_(i=2..90) C(F_i) mod 10^8 + 7 with F_i Fibonacci (F_90 ~
2.9 * 10^18).

Maximality forces structure: kings alone limit each 2 x 2 block to
one piece, so a maximum placement chooses one corner (a, b) in
{0,1}^2 per block of the n x n block grid, and only adjacent
(including diagonal) blocks can interact. Translating the king +
knight attack set into the block coordinates: horizontally the b's
must be non-decreasing along each row with a constant wherever b
stays constant, and symmetrically for columns; diagonals add three
forbidden patterns each. Consequently every valid row is determined
by (threshold t, a-left, a-right) - exactly 4n rows, verified
exhaustively against all 4^n cell rows for n <= 6 - and C(n) is a
path count in a (4n)-state row-transfer graph, checked against a
literal 4^(n+1)-state sliding-window DP over blocks for n <= 8 and
against the given C(1) = 4, C(2) = 25, C(10) = 1477721.

The transfer values for n = 1..40 reveal (and verify) the closed
form

    C(n) = 8 binom(2n, n) - 3n^2 - 2n - 7,

whose binomial term is evaluated at Fibonacci arguments by Lucas'
theorem over p = 10^8 + 7 with a precomputed factorial table
(2 F_90 < p^3, so at most three base-p digits).
"""

import random
from math import comb

import numba
import numpy as np

MOD = 10**8 + 7


def _attacks(dx: int, dy: int) -> bool:
    return max(abs(dx), abs(dy)) == 1 or (abs(dx), abs(dy)) in ((1, 2), (2, 1))


def _tables() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    okh = np.ones((4, 4), np.int8)
    okv = np.ones((4, 4), np.int8)
    okd = np.ones((4, 4), np.int8)
    oka = np.ones((4, 4), np.int8)
    for s in range(4):
        a, b = s >> 1, s & 1
        for s2 in range(4):
            a2, b2 = s2 >> 1, s2 & 1
            if _attacks(a2 - a, 2 + b2 - b):
                okh[s, s2] = 0
            if _attacks(2 + a2 - a, b2 - b):
                okv[s, s2] = 0
            if _attacks(2 + a2 - a, 2 + b2 - b):
                okd[s, s2] = 0
            if _attacks(2 + a2 - a, -2 + b2 - b):
                oka[s, s2] = 0
    return okh, okv, okd, oka


_OKH, _OKV, _OKD, _OKA = _tables()


def _row_states(n: int) -> list[tuple[int, ...]]:
    seen: set[tuple[int, ...]] = set()
    out: list[tuple[int, ...]] = []
    for t in range(n + 1):
        for a_left in range(2):
            for a_right in range(2):
                cells = tuple(
                    2 * (a_left if j < t else a_right) + (0 if j < t else 1)
                    for j in range(n)
                )
                if all(_OKH[cells[j], cells[j + 1]] for j in range(n - 1)):
                    if cells not in seen:
                        seen.add(cells)
                        out.append(cells)
    return out


def c_transfer(n: int) -> int:
    rs = _row_states(n)
    s = len(rs)
    comp = np.zeros((s, s), dtype=np.int8)
    for i, r1 in enumerate(rs):
        for k, r2 in enumerate(rs):
            comp[i, k] = all(
                _OKV[r1[j], r2[j]]
                and (j >= n - 1 or _OKA[r1[j + 1], r2[j]])
                and (j <= 0 or _OKD[r1[j - 1], r2[j]])
                for j in range(n)
            )
    v = np.ones(s, dtype=object)
    for _ in range(n - 1):
        v = comp.T.astype(object) @ v
    return int(v.sum())


@numba.njit(cache=True)
def _c_block_dp(n, okh, okv, okd, oka) -> np.int64:
    w = 4 ** (n + 1)
    arr = np.zeros(w, np.int64)
    arr[0] = 1
    sh_up = 4 ** (n - 1)
    sh_upr = 4 ** (n - 2) if n >= 2 else 1
    sh_upl = 4**n
    for x in range(n * n):
        r, c = x // n, x % n
        narr = np.zeros(w, np.int64)
        for st in range(w):
            cv = arr[st]
            if cv == 0:
                continue
            left = st & 3
            up = (st // sh_up) & 3
            upr = (st // sh_upr) & 3
            upl = (st // sh_upl) & 3
            for s in range(4):
                if c > 0 and not okh[left, s]:
                    continue
                if r > 0:
                    if not okv[up, s]:
                        continue
                    if c < n - 1 and not oka[upr, s]:
                        continue
                    if c > 0 and not okd[upl, s]:
                        continue
                narr[(st * 4 + s) % w] += cv
        arr = narr
    return arr.sum()


def c_formula(n: int) -> int:
    return 8 * comb(2 * n, n) - 3 * n * n - 2 * n - 7


@numba.njit(cache=True)
def _fact_table(p: int) -> np.ndarray:
    f = np.zeros(p, dtype=np.int32)
    f[0] = 1
    cur = np.int64(1)
    for i in range(1, p):
        cur = cur * i % p
        f[i] = cur
    return f


def _binom_lucas(m: int, k: int, p: int, fact: np.ndarray) -> int:
    res = 1
    while m > 0 or k > 0:
        mi, ki = m % p, k % p
        if ki > mi:
            return 0
        den = int(fact[ki]) * int(fact[mi - ki]) % p
        res = res * int(fact[mi]) % p * pow(den, p - 2, p) % p
        m //= p
        k //= p
    return res


if __name__ == "__main__":
    # structured rows = all valid rows (exhaustive check)
    from itertools import product

    for n in range(1, 7):
        exhaustive = {
            cells
            for cells in product(range(4), repeat=n)
            if all(_OKH[cells[j], cells[j + 1]] for j in range(n - 1))
        }
        assert set(_row_states(n)) == exhaustive, n
    # transfer vs literal block DP, formula, and givens
    for n in range(1, 9):
        ct = c_transfer(n)
        assert ct == int(_c_block_dp(n, _OKH, _OKV, _OKD, _OKA)) == c_formula(n), n
    assert c_formula(1) == 4 and c_formula(2) == 25  # given
    assert c_formula(10) == 1477721 == c_transfer(10)  # given
    for n in range(11, 41):
        assert c_transfer(n) == c_formula(n), n

    fact = _fact_table(MOD)
    rng = random.Random(554)
    for _ in range(20):
        m = rng.randrange(1, 10**6)
        assert _binom_lucas(2 * m, m, MOD, fact) == comb(2 * m, m) % MOD

    fib = [0, 1, 1]
    for _ in range(3, 91):
        fib.append(fib[-1] + fib[-2])
    total = 0
    for i in range(2, 91):
        n = fib[i]
        term = 8 * _binom_lucas(2 * n, n, MOD, fact) - (
            3 * (n % MOD) * (n % MOD) + 2 * n + 7
        )
        total = (total + term) % MOD
    print(total)  # 89539872
