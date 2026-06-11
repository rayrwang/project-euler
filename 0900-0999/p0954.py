"""Project Euler 954: Heptaphobia.

n (with n mod 7 = r != 0) is heptaphobic iff no digit swap produces a
multiple of 7. Swapping digits a_i, a_j at positions i, j (weights
u = 10^i, v = 10^j mod 7) changes n by (a_i - a_j)(v - u), so the swap is
fatal iff a_i - a_j = -r / (v - u) =: delta (mod 7). Weights depend only on
the position mod 6 and the six weight classes carry the six distinct
nonzero residues {1, 3, 2, 6, 4, 5}, so same-class swaps are always safe
and a cross-class pair (c, c') is fatal iff res(a_i) - res(a_j) = delta(c, c').
The only exemption: a swap moving digit 0 into the leading position is not
a legal swap, so pairs (leading position, digit 0) never disqualify n.

Hence whether n is heptaphobic depends per class only on the set U of digit
residues present, plus (for the leading-digit exemption) whether a NONZERO
digit of residue 0 (i.e. a 7) is present. For each length L <= 13 each class
holds at most 3 positions, so we enumerate all digit tuples per class once,
bucketing counts by (U, has-a-7, weighted sum mod 7), and then run a DFS
over the six classes (the leading position split off separately) checking
the pairwise set conditions U_{c'} disjoint from U_c - delta(c, c'), and for
the leading digit d the conditions res(d) - delta not in U'_{c'} (residues of
nonzero digits). Counts are combined as length-7 vectors under cyclic
convolution and the coefficient at r is taken.

Verified against brute force: C(100) = 74, C(10^4) = 3737, and all
per-length counts up to L = 6.
"""

from itertools import product

W = [pow(10, c, 7) for c in range(6)]  # weight of position class c
INV = [0] + [pow(x, 5, 7) for x in range(1, 7)]  # inverses mod 7


def class_table(m: int, w: int) -> list[tuple[int, int, list[int]]]:
    """All (Umask, has7, vec[s]) for m digits of weight w.

    Umask = bitmask of residues present, has7 = a digit 7 occurs,
    vec[s] = number of digit tuples with weighted sum = s (mod 7).
    """
    buckets: dict[tuple[int, int], list[int]] = {}
    for tup in product(range(10), repeat=m):
        um, h7, s = 0, 0, 0
        for d in tup:
            r = d % 7
            um |= 1 << r
            if d == 7:
                h7 = 1
            s += r
        key = (um, h7)
        if key not in buckets:
            buckets[key] = [0] * 7
        buckets[key][s * w % 7] += 1
    return [(um, h7, vec) for (um, h7), vec in buckets.items()]


def shift_mask(mask: int, d: int) -> int:
    """Bitmask of {x - d mod 7 : x in mask}."""
    d %= 7
    return ((mask >> d) | (mask << (7 - d))) & 0x7F


def conv7(a: list[int], b: list[int]) -> list[int]:
    out = [0] * 7
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[(i + j) % 7] += ai * bj
    return out


def count_length(ln: int) -> int:
    """Number of heptaphobic ln-digit numbers."""
    lead_pos = ln - 1
    cl = lead_pos % 6
    m = [len([p for p in range(ln) if p % 6 == c]) for c in range(6)]
    m[cl] -= 1  # leading position handled separately
    tables = [class_table(m[c], W[c]) for c in range(6)]
    total = 0
    for r in range(1, 7):
        delta = [[0] * 6 for _ in range(6)]
        for c in range(6):
            for c2 in range(6):
                if c != c2:
                    delta[c][c2] = (-r) * INV[(W[c2] - W[c]) % 7] % 7

        # DFS over classes 0..5 choosing (Umask, has7, vec) signatures.
        def dfs(c: int, chosen: list[tuple[int, int, int]], vec: list[int]) -> int:
            if c == 6:
                # attach the leading digit d = 1..9
                sub = 0
                for d in range(1, 10):
                    rd = d % 7
                    ok = True
                    for c2, um2, h7_2 in chosen:
                        if c2 == cl or m[c2] == 0:
                            continue  # same weight class as leading: safe
                        f = (rd - delta[cl][c2]) % 7
                        bad = h7_2 if f == 0 else (um2 >> f) & 1
                        if bad:
                            ok = False
                            break
                    if ok:
                        sub += vec[(r - W[cl] * rd) % 7]
                return sub
            res = 0
            for um, h7, v in tables[c]:
                good = True
                for c2, um2, _ in chosen:
                    if m[c2] == 0 or um == 0:
                        continue
                    # fatal iff exists x in U_{c2} with x - delta(c2,c) in U_c
                    if shift_mask(um2, delta[c2][c]) & um:
                        good = False
                        break
                if good:
                    res += dfs(c + 1, [*chosen, (c, um, h7)], conv7(vec, v))
            return res

        e0 = [1, 0, 0, 0, 0, 0, 0]
        total += dfs(0, [], e0)
    return total


def solve() -> int:
    return sum(count_length(ln) for ln in range(1, 14))


if __name__ == "__main__":
    print(solve())  # 736463823
