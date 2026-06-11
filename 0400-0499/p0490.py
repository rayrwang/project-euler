"""Project Euler 490: Jumping Frog.

f(n) counts Hamiltonian paths from stone 1 to stone n where jumps span at
most 3 stones, i.e. Hamiltonian paths 1 -> n in the cube of the path graph.

1. A plug DP over the cut boundary {i-2, i-1, i} computes f(n) exactly:
   the partial edge set is a disjoint union of paths, and only the last
   three stones can receive future (rightward) edges of length <= 3.
2. f is C-finite: Berlekamp-Massey on exact values finds an order-8
   integer recurrence, so f(n)^3 is C-finite of order <= C(10, 3) = 120;
   Berlekamp-Massey on the cubes finds that order-120 recurrence, and the
   partial sums S(L) then satisfy an order-121 recurrence.
3. Kitamasa (polynomial powering modulo the characteristic polynomial)
   evaluates S(10^14) mod 10^9.
"""

from fractions import Fraction
from itertools import combinations

def f_values(n_max: int) -> list[int]:
    """Exact f(1..n_max) via plug DP.

    Boundary slot per stone: None if saturated (no more edges allowed) or
    (cap, seg) for an open segment end with remaining edge capacity cap and
    pairing label seg; 'S' marks the segment holding stone 1's path-start
    end. A capacity-2 slot is an isolated stone (both segment ends on it).
    """
    def canon(state: tuple) -> tuple:
        mapping: dict = {}
        out = []
        for slot in state:
            if slot is None:
                out.append(None)
            else:
                cap, seg = slot
                if seg != "S":
                    if seg not in mapping:
                        mapping[seg] = len(mapping)
                    seg = mapping[seg]
                out.append((cap, seg))
        return tuple(out)

    states = {canon((None, None, (1, "S"))): 1}
    res = [0, 1]  # res[n] = f(n); f(1) = 1
    for _ in range(2, n_max + 1):
        new: dict = {}
        for state, cnt in states.items():
            open_slots = [j for j in range(3) if state[j] is not None]
            for k in (0, 1, 2):
                for sel in combinations(open_slots, k):
                    if k == 2 and state[sel[0]][1] == state[sel[1]][1]:
                        continue  # would close a cycle
                    slots = list(state)
                    vcap, vseg = 2, ("v",)  # the new stone, isolated
                    for j in sel:
                        cap, seg = slots[j]
                        cap -= 1
                        vcap -= 1
                        merged = "S" if "S" in (seg, vseg) else (seg, vseg)
                        for t in range(3):
                            if slots[t] is not None and slots[t][1] in (seg, vseg):
                                slots[t] = (slots[t][0], merged)
                        slots[j] = (cap, merged) if cap else None
                        vseg = merged
                    vslot = (vcap, vseg) if vcap else None
                    if slots[0] is not None:
                        continue  # exiting stone left incomplete
                    ns = canon((slots[1], slots[2], vslot))
                    new[ns] = new.get(ns, 0) + cnt
        states = new
        # f(n): one segment 'S' whose other end is stone n with degree 1
        res.append(sum(c for s, c in states.items()
                       if s[0] is None and s[1] is None
                       and s[2] == (1, "S")))
    return res[1:]

def berlekamp_massey(seq: list[int]) -> list[Fraction]:
    """Minimal c with seq[i] = sum_j c[j] * seq[i-1-j], over Q."""
    sq = [Fraction(x) for x in seq]
    ls: list[Fraction] = []
    cur: list[Fraction] = []
    lf, ld = 0, Fraction(0)
    for i in range(len(sq)):
        t = sum(cur[j] * sq[i - 1 - j] for j in range(len(cur)))
        if t == sq[i]:
            continue
        if not cur:
            cur = [Fraction(0)] * (i + 1)
            lf, ld = i, sq[i] - t
            continue
        k = (sq[i] - t) / ld
        c = [Fraction(0)] * (i - lf - 1) + [k] + [-k * x for x in ls]
        c += [Fraction(0)] * max(0, len(cur) - len(c))
        for j in range(len(cur)):
            c[j] += cur[j]
        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = list(cur), i, sq[i] - t
        cur = c
    return cur

def kitamasa(coeffs: list[int], init: list[int], n: int, mod: int) -> int:
    """seq[n] mod `mod` (0-based) for seq[i] = sum_j coeffs[j]*seq[i-1-j]."""
    k = len(coeffs)
    if n < k:
        return init[n] % mod
    # characteristic poly: x^k - coeffs[0] x^(k-1) - ... - coeffs[k-1]
    def mulmod(a: list[int], b: list[int]) -> list[int]:
        prod = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    prod[i + j] = (prod[i + j] + ai * bj) % mod
        for d in range(len(prod) - 1, k - 1, -1):
            c = prod[d]
            if c:
                prod[d] = 0
                for j in range(k):
                    prod[d - 1 - j] = (prod[d - 1 - j] + c * coeffs[j]) % mod
        return prod[:k]

    result = [1]
    base = [0, 1]  # the polynomial x
    e = n
    while e:
        if e & 1:
            result = mulmod(result, base)
        base = mulmod(base, base)
        e >>= 1
    return sum(r * init[t] for t, r in enumerate(result)) % mod

def solve() -> int:
    mod = 10**9
    vals = f_values(80)
    assert vals[5] == 14 and vals[9] == 254 and vals[39] == 1439682432976
    rec = berlekamp_massey(vals)
    reci = [int(x) for x in rec]
    assert all(x == y for x, y in zip(reci, rec)), "non-integer recurrence"
    k = len(reci)  # 8
    ext = vals[:k]
    for i in range(k, 400):
        ext.append(sum(reci[j] * ext[i - 1 - j] for j in range(k)))
    assert ext[:80] == vals
    cubes = [x**3 for x in ext]
    sums = list(cubes)
    for i in range(1, len(sums)):
        sums[i] += sums[i - 1]
    assert sums[9] == 18230635 and sums[19] == 104207881192114219
    rec_s = berlekamp_massey(sums[:300])
    rsi = [int(x) for x in rec_s]
    assert all(x == y for x, y in zip(rsi, rec_s)), "non-integer recurrence"
    ks = len(rsi)  # 121
    for i in range(ks, 400):  # recurrence reproduces all known sums
        assert sums[i] == sum(rsi[j] * sums[i - 1 - j] for j in range(ks))
    init = [s % mod for s in sums[:ks]]
    s = lambda n: kitamasa(rsi, init, n - 1, mod)  # noqa: E731
    assert s(1000) == 225031475
    assert s(10**6) == 363486179
    return s(10**14)

if __name__ == "__main__":
    print(solve())  # 777577686
