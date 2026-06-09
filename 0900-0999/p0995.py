"""Project Euler Problem 995: A Particular Pair of Polynomials.

With ``f_p(x) = 1 + x + ... + x^(p-1)`` and ``g_n(x) = 1 + sum_{d|n} x^d``,
``S(p)`` is the least ``s`` with ``f_p | g_s`` and ``T(m)`` is the product of
``S(p)`` over primes ``p < m``.  Given ``T(20) = 1348422598656`` and
``T(100) ~ 1.37451e123``, find ``T(20000)`` in scientific notation with five
digits after the decimal point.

What divisibility means
-----------------------
``f_p`` is the cyclotomic polynomial ``Phi_p``, irreducible with roots the
primitive p-th roots of unity ``zeta``.  So ``f_p | g_s`` iff
``1 + sum_{d|s} zeta^d = 0``.  Writing ``m_j`` for the number of divisors of
``s`` congruent to ``j`` mod ``p`` and reducing against the single relation
``1 + zeta + ... + zeta^(p-1) = 0`` gives the exact condition

    m_1 = m_2 = ... = m_{p-1} = m_0 + 1.

If ``p | s``, say ``s = p^e t`` with ``p`` prime to ``t``, then
``m_0 = e tau(t)`` while the nonzero classes hold ``tau(t)`` divisors in
total, forcing ``tau(t) = (p-1)(e tau(t) + 1)`` -- impossible for ``e >= 1``.
Hence ``p`` does not divide ``s``, ``m_0 = 0``, ``tau(s) = p - 1``, and the
divisors of ``s`` hit every residue in ``Z_p^*`` exactly once.

Tilings of a cyclic group by geometric progressions
---------------------------------------------------
Write ``s = prod q_i^(a_i)`` with ``e_i = a_i + 1`` and ``m = p - 1``, so
``prod e_i = m``.  In discrete-log space each prime power contributes the
arithmetic progression ``{0, l_i, ..., (e_i - 1) l_i}`` with
``l_i = dlog(q_i)``, and the divisors biject onto ``Z_p^*`` iff these
progressions tile ``Z_m``.  Evaluating the product of progression mask
polynomials at a character of order ``d | m``: the i-th factor vanishes iff
``delta = d / gcd(d, l_i)`` satisfies ``delta > 1`` and ``delta | e_i``.
Since ``gcd(d, l_i) = gcd(d, z_i)`` where ``z_i = m / ord_p(q_i)``, the
tiling criterion is exactly:

    for every divisor d > 1 of m there is a part i with
        d | z_i * e_i   and   d does not divide z_i.

(The valuation identity ``d / gcd(d, z) | e  <=>  d | z e`` makes the
condition symmetric in ``e`` and ``z``.)  This was validated against a direct
brute-force search for ``S(p)`` for all ``p <= 13``.

Minimisation
------------
``S(p)`` is the minimum of ``prod q_i^(e_i - 1)`` over multisets of parts
``(e_i, q_i)`` with distinct primes ``q_i != p``, ``prod e_i = m``, and the
coverage criterion above, where each part's ``z_i`` is determined by the
multiplicative order of ``q_i`` mod ``p``.  The search:

* a lazy *supply* serves, for each ``z`` (equivalently each order ``r=m/z``),
  the ascending primes of that order -- found by a shared ascending scan for
  dense orders and by enumerating the arithmetic progressions
  ``x = g^(m u / r) mod p  (mod p)`` with a Miller-Rabin test for sparse ones;
* branch and bound covers the *largest uncovered divisor first*: every valid
  solution must contain a part covering it, so branching is restricted to
  those parts, which are few precisely when they are expensive;
* within a bucket (fixed ``z``) the ascending primes are assigned to the
  bucket's parts with descending exponents (rearrangement-optimal), and the
  running cost is re-optimised exactly whenever a bucket gains a part;
* once every divisor is covered, the leftover quota ``M`` is filled by the
  cheapest factorization of ``M`` into parts, greedily assigning the smallest
  still-unused primes (a tiny exact sub-search);
* pruning uses exact integer arithmetic with two admissible bounds: the
  cheapest cover of the current largest uncovered divisor, and ``minfact``,
  the cheapest way to factor the remaining quota over the smallest primes.

Chain (mixed-radix) constructions -- ordered factorizations ``e_1, ..., e_k``
of ``m`` with ``z_i = e_1 ... e_{i-1}`` -- seed the search with feasible
upper bounds.

The final ``T(20000)`` is an exact 536281-digit integer assembled by a
balanced product tree; both checkpoints are verified.
"""

from __future__ import annotations

import heapq
import random
from functools import lru_cache
from math import gcd, prod

import numpy as np


def sieve_primes(n: int) -> list[int]:
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    return [int(x) for x in np.nonzero(s)[0]]


SMALL = sieve_primes(2_000_000)

_MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for q in _MR_BASES:
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in _MR_BASES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factorize(m: int) -> dict[int, int]:
    f: dict[int, int] = {}
    x = m
    for q in SMALL:
        if q * q > x:
            break
        while x % q == 0:
            f[q] = f.get(q, 0) + 1
            x //= q
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def divisors_of(fac: dict[int, int]) -> list[int]:
    divs = [1]
    for q, a in fac.items():
        divs = [d * q**t for d in divs for t in range(a + 1)]
    return sorted(divs)


def iroot(n: int, k: int) -> int:
    """Exact floor of the k-th root, integer Newton iteration."""
    if n <= 0:
        return 0
    if k == 1:
        return n
    x = 1 << (-(-n.bit_length() // k) + 1)
    while True:
        y = ((k - 1) * x + n // x ** (k - 1)) // k
        if y >= x:
            break
        x = y
    while x**k > n:
        x -= 1
    while (x + 1) ** k <= n:
        x += 1
    return x


@lru_cache(maxsize=None)
def _minfact(M: int, j: int, emax: int) -> int:
    if M == 1:
        return 1
    best = 1 << 400
    pj = SMALL[j]
    for e in range(2, min(M, emax) + 1):
        if M % e == 0:
            c = pj ** (e - 1) * _minfact(M // e, j + 1, e)
            if c < best:
                best = c
    return best


def minfact_lb(M: int) -> int:
    """Cheapest factorization of M into parts over the smallest primes."""
    return 1 if M == 1 else _minfact(M, 0, M)


class Supply:
    """Ascending primes with a given z = m / ord_p(q), served lazily."""

    def __init__(self, p: int, m: int, fac: dict[int, int]):
        self.p = p
        self.m = m
        self.fac = list(fac)
        self.buckets: dict[int, list[int]] = {}
        self.bucket_sets: dict[int, set[int]] = {}
        self.scan_idx = 0
        self.heaps: dict[int, list[tuple[int, int]]] = {}
        self.g: int | None = None

    def ordp(self, q: int) -> int:
        r = self.m
        for ell in self.fac:
            while r % ell == 0 and pow(q, r // ell, self.p) == 1:
                r //= ell
        return r

    def scan_to(self, q_limit: int) -> None:
        while self.scan_idx < len(SMALL) and SMALL[self.scan_idx] <= q_limit:
            q = SMALL[self.scan_idx]
            self.scan_idx += 1
            if q == self.p:
                continue
            z = self.m // self.ordp(q)
            s = self.bucket_sets.setdefault(z, set())
            if q not in s:
                s.add(q)
                b = self.buckets.setdefault(z, [])
                b.append(q)
                if len(b) > 1 and b[-2] > q:
                    b.sort()

    def _prim_root(self) -> int:
        if self.g is None:
            g = 2
            while self.ordp(g) != self.m:
                g += 1
            self.g = g
        return self.g

    def _ensure_heap(self, z: int) -> None:
        if z in self.heaps:
            return
        r = self.m // z
        g = self._prim_root()
        step = self.m // r
        residues = sorted(
            {pow(g, step * u, self.p) for u in range(1, r + 1) if gcd(u, r) == 1}
        )
        h = [(res if res > 1 else res + self.p, res) for res in residues]
        heapq.heapify(h)
        self.heaps[z] = h

    def get(self, z: int, i: int, cap: int) -> int | None:
        """i-th smallest prime (0-based) with this z, capped, else None."""
        b = self.buckets.setdefault(z, [])
        if i < len(b):
            return b[i] if b[i] <= cap else None
        scanned = SMALL[self.scan_idx - 1] if self.scan_idx else 0
        r = self.m // z
        if r * 8 >= self.m and self.scan_idx < len(SMALL):
            lim = max(scanned, 100)
            while len(b) <= i and lim < min(cap, SMALL[-1]):
                lim = min(2 * lim, cap, SMALL[-1])
                self.scan_to(lim)
            scanned = SMALL[self.scan_idx - 1] if self.scan_idx else 0
            if i < len(b):
                return b[i] if b[i] <= cap else None
        self._ensure_heap(z)
        h = self.heaps[z]
        s = self.bucket_sets.setdefault(z, set())
        while len(b) <= i and h:
            x, res = heapq.heappop(h)
            if x <= scanned:
                k = (scanned - x) // self.p + 1
                heapq.heappush(h, (x + k * self.p, res))
                continue
            if x > cap:
                heapq.heappush(h, (x, res))
                return None
            heapq.heappush(h, (x + self.p, res))
            if x not in s and is_prime(x):
                s.add(x)
                b.append(x)
                b.sort()
        if i < len(b) and b[i] <= cap:
            return b[i]
        return None


def _bucket_cost(es: list[int], primes: list[int]) -> int:
    """Optimal bucket pricing: largest exponents on smallest primes."""
    return prod(q ** (e - 1) for e, q in zip(sorted(es, reverse=True), primes))


class _Solver:
    def __init__(self, p: int):
        self.p = p
        m = self.m = p - 1
        if m == 1:
            return
        fac = self.fac = factorize(m)
        divs = self.divs = divisors_of(fac)
        self.targets = [d for d in divs if d > 1]
        tidx = {d: i for i, d in enumerate(self.targets)}
        self.full = (1 << len(self.targets)) - 1
        self.supply = Supply(p, m, fac)
        self.supply.scan_to(300)
        self.cover: dict[tuple[int, int], int] = {}
        self.coverers: dict[int, list[tuple[int, int]]] = {d: [] for d in self.targets}
        for e in divs:
            if e < 2:
                continue
            for z in divs:
                msk = 0
                for d in self.targets:
                    if (z * e) % d == 0 and z % d != 0:
                        msk |= 1 << tidx[d]
                self.cover[(e, z)] = msk
                for d in self.targets:
                    if msk >> tidx[d] & 1:
                        self.coverers[d].append((e, z))
        self.cmemo: dict[tuple[int, int], int] = {}

    def _unused_primes(self, used: dict[int, int], count: int) -> list[int]:
        out: list[int] = []
        consumed: dict[int, int] = {}
        idx = 0
        while len(out) < count and idx < len(SMALL):
            if idx >= self.supply.scan_idx:
                self.supply.scan_to(
                    SMALL[min(self.supply.scan_idx + 64, len(SMALL) - 1)]
                )
                if idx >= self.supply.scan_idx:
                    break
            q = SMALL[idx]
            idx += 1
            if q == self.p:
                continue
            z = self.m // self.supply.ordp(q)
            k = consumed.get(z, 0)
            consumed[z] = k + 1
            if k < used.get(z, 0):
                continue  # taken by a cover part
            out.append(q)
        return out

    def _completion(self, M: int, used: dict[int, int]) -> int:
        """Cheapest factorization of the leftover quota over unused primes."""
        if M == 1:
            return 1
        avail = self._unused_primes(used, 16)
        best = [1 << 4000]

        def go(M: int, j: int, emax: int, cost: int) -> None:
            if cost >= best[0]:
                return
            if M == 1:
                best[0] = cost
                return
            for e in range(min(M, emax), 1, -1):
                if M % e == 0:
                    go(M // e, j + 1, e, cost * avail[j] ** (e - 1))

        go(M, 0, M, 1)
        return best[0]

    def _cmin2(self, d: int, M: int) -> int:
        """LB: cheapest part covering d, times minfact of the rest."""
        key = (d, M)
        v = self.cmemo.get(key)
        if v is not None:
            return v
        bestc = 1 << 4000
        for e, z in self.coverers[d]:
            if M % e:
                continue
            q = self.supply.get(z, 0, iroot(bestc, e - 1))
            if q is None:
                continue
            c = q ** (e - 1) * minfact_lb(M // e)
            if c < bestc:
                bestc = c
        bestc = max(bestc, minfact_lb(M))
        self.cmemo[key] = bestc
        return bestc

    def solve(self) -> int:
        m = self.m
        if m == 1:
            return 1
        supply = self.supply
        plist: list[int] = []
        for ell, a in sorted(self.fac.items()):
            plist += [ell] * a

        def chain_cost(order: list[int]) -> int | None:
            cost = 1
            used: dict[int, int] = {}
            z = 1
            for e in order:
                cnt = used.get(z, 0)
                q = supply.get(z, cnt, 10**9)
                if q is None:
                    return None
                used[z] = cnt + 1
                cost *= q ** (e - 1)
                z *= e
            return cost

        rng = random.Random(1)
        orders = {tuple(plist), tuple(reversed(plist))}
        for _ in range(20):
            sh = plist[:]
            rng.shuffle(sh)
            orders.add(tuple(sh))
        seeds = [c for c in (chain_cost(list(od)) for od in orders) if c is not None]
        self.best = min(seeds)

        cover, coverers, targets = self.cover, self.coverers, self.targets

        def rec(M: int, mask: int, bparts: dict[int, list[int]]) -> None:
            cost = prod(
                _bucket_cost(es, supply.buckets[z][: len(es)])
                for z, es in bparts.items()
            )
            if mask == 0:
                used = {z: len(es) for z, es in bparts.items()}
                total = cost * self._completion(M, used)
                if total < self.best:
                    self.best = total
                return
            d = targets[mask.bit_length() - 1]
            if cost * self._cmin2(d, M) >= self.best:
                return
            budget = (self.best - 1) // cost
            branches = []
            for e, z in coverers[d]:
                if M % e:
                    continue
                lbsub = minfact_lb(M // e)
                if lbsub > budget:
                    continue
                capq = iroot(budget // lbsub, e - 1)
                cnt = len(bparts.get(z, []))
                q = supply.get(z, cnt, capq)
                if q is None:
                    continue
                es = bparts.get(z, [])
                old = _bucket_cost(es, supply.buckets[z][: len(es)]) if es else 1
                new = _bucket_cost(es + [e], supply.buckets[z][: len(es) + 1])
                branches.append((new * lbsub, old, new, e, z))
            branches.sort(key=lambda t: t[0])
            for _, old, new, e, z in branches:
                # exact: (cost/old)*new*minfact >= best  <=>  cost*new*minfact >= best*old
                if cost * new * minfact_lb(M // e) >= self.best * old:
                    continue
                es = bparts.setdefault(z, [])
                es.append(e)
                rec(M // e, mask & ~cover[(e, z)], bparts)
                es.pop()
                if not es:
                    del bparts[z]

        rec(m, self.full, {})
        return self.best


def smallest_s(p: int) -> int:
    """S(p): least s with f_p | g_s."""
    return _Solver(p).solve()


def t_product(m: int) -> int:
    """Exact T(m) via a balanced product tree."""
    vals = [smallest_s(p) for p in sieve_primes(m - 1)]
    while len(vals) > 1:
        vals = [
            vals[i] * vals[i + 1] if i + 1 < len(vals) else vals[i]
            for i in range(0, len(vals), 2)
        ]
    return vals[0]


def sci_notation(n: int) -> str:
    """Scientific notation with 5 digits after the point, lowercase e."""
    import sys

    sys.set_int_max_str_digits(max(700000, sys.get_int_max_str_digits()))
    st = str(n)
    r = (int(st[:7]) + 5) // 10
    exp = len(st) - 1
    if r >= 10**6:
        r //= 10
        exp += 1
    return "%d.%05de%d" % (r // 100000, r % 100000, exp)


if __name__ == "__main__":
    assert smallest_s(2) == 1, "checkpoint S(2)"
    assert smallest_s(5) == 8, "checkpoint S(5)"
    assert t_product(20) == 1348422598656, "checkpoint T(20)"
    assert sci_notation(t_product(100)) == "1.37451e123", "checkpoint T(100)"
    print(sci_notation(t_product(20000)))  # 2.21322e536280
