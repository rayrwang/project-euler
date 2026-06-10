from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def _cycle_type(p: tuple[int, ...]) -> tuple[int, ...]:
    n = len(p)
    seen = [False] * n
    parts = []
    for i in range(n):
        if not seen[i]:
            length = 0
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
                length += 1
            parts.append(length)
    return tuple(sorted(parts, reverse=True))


def _class_size(ct: tuple[int, ...], n: int) -> int:
    counts = Counter(ct)
    denom = 1
    for part, mult in counts.items():
        denom *= (part**mult) * factorial(mult)
    return factorial(n) // denom


def _representative(ct: tuple[int, ...], n: int) -> tuple[int, ...]:
    p = list(range(n))
    pos = 0
    for length in ct:
        cycle = list(range(pos, pos + length))
        for i in range(length):
            p[cycle[i]] = cycle[(i + 1) % length]
        pos += length
    return tuple(p)


def _partitions(n: int, mx: int | None = None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in _partitions(n - k, k):
            yield (k,) + rest


def solve(n: int = 11) -> Fraction:
    """Expected number of shuffles of this bozo-sort variant, averaged over all n!
    permutations of 1..n (the final answer is this value rounded to an integer).

    A step picks 3 of the n positions uniformly and replaces their contents by a
    uniformly random arrangement (all 6 equally likely), repeating until sorted.
    The expected hitting time E[pi] of the identity is invariant under relabelling,
    so it depends only on the cycle type of pi; there are only p(n) = 56 cycle
    types for n = 11. Building the transition probabilities between cycle types
    from a single representative of each (enumerate the C(n,3) position triples and
    the 6 rearrangements, record the resulting cycle type) gives a small linear
    system E[ct] = 1 + sum P(ct -> ct') E[ct'] with E[identity] = 0. Solving it
    exactly over the rationals and averaging E[ct] weighted by each class size /
    n! yields the answer.
    """
    cts = list(_partitions(n))
    ct_index = {ct: i for i, ct in enumerate(cts)}
    m = len(cts)
    positions = list(combinations(range(n), 3))
    rearrangements = list(permutations(range(3)))
    identity_ct = tuple([1] * n)

    a = [[Fraction(0)] * m for _ in range(m)]
    b = [Fraction(0)] * m
    for ci, ct in enumerate(cts):
        a[ci][ci] += 1
        if ct == identity_ct:
            continue
        b[ci] = Fraction(1)
        p = _representative(ct, n)
        tally: dict[tuple[int, ...], int] = defaultdict(int)
        total = 0
        for pos in positions:
            vals = [p[pos[0]], p[pos[1]], p[pos[2]]]
            for arr in rearrangements:
                lp = list(p)
                for t in range(3):
                    lp[pos[t]] = vals[arr[t]]
                tally[_cycle_type(tuple(lp))] += 1
                total += 1
        for ct2, cnt in tally.items():
            a[ci][ct_index[ct2]] -= Fraction(cnt, total)

    # exact Gaussian elimination
    for col in range(m):
        pivot = next((r for r in range(col, m) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[col], a[pivot] = a[pivot], a[col]
        b[col], b[pivot] = b[pivot], b[col]
        pivot_val = a[col][col]
        for r in range(m):
            if r != col and a[r][col] != 0:
                factor = a[r][col] / pivot_val
                row, crow = a[r], a[col]
                for c in range(col, m):
                    row[c] -= factor * crow[c]
                b[r] -= factor * b[col]

    expected = [b[i] / a[i][i] if a[i][i] != 0 else Fraction(0) for i in range(m)]
    weighted = sum(
        (_class_size(ct, n) * expected[ct_index[ct]] for ct in cts), Fraction(0)
    )
    return weighted / factorial(n)


if __name__ == "__main__":
    # n = 4 averages to exactly 27.5 shuffles; n = 7 to ~6200.2.
    assert solve(4) == Fraction(55, 2)
    print(round(solve(11)))  # 48271207
