"""Project Euler Problem 988: Non-attacking Frogs.

Frogs sit at integer points and jump forward by ``a`` or ``b``
(``gcd(a, b) = 1``); a frog at ``m`` attacks one at ``n > m`` iff ``n - m``
lies in the numerical semigroup ``S = <a, b> = {ax + by : x, y >= 0}``.
``F(a, b)`` sums the locations of all frogs over all non-attacking
configurations containing a frog at 0.  Given ``F(3,5) = 23`` and
``F(5,13) = 16336``, find ``F(19, 53)``.

Gaps and the staircase poset
----------------------------
Every positive frog position ``g`` satisfies ``g - 0 not in S``, so all
frogs sit on the *gaps* of ``S`` (the ``(a-1)(b-1)/2`` non-representable
integers).  Classically each gap has a unique representation

    g = ab - ax - by,    1 <= x <= b - 1,  y >= 1,

so gaps are the lattice points strictly inside the triangle
``ax + by < ab`` in the positive quadrant.  For two gaps,
``g(x', y') - g(x, y) = a(x - x') + b(y - y')`` lies in ``S`` exactly when
``x >= x'`` and ``y >= y'`` componentwise (the alternative
representations would need ``|x - x'| >= b`` or ``|y - y'| >= a``, which
the triangle forbids).  Hence "non-attacking" is precisely
"pairwise incomparable in the componentwise order": configurations are
the *antichains* of a staircase (Young-diagram) poset.

An antichain picks at most one point per column, with strictly decreasing
heights left to right: columns ``x_1 < ... < x_k``, ``y_1 > ... > y_k``.
Then

    F(a, b) = sum_{points p} g(p) * L(p) * R(p),

where ``L(p)`` counts antichains using only columns left of ``p`` with all
heights above ``p``'s, and ``R(p)`` counts antichains right of ``p`` below
``p``'s height; both satisfy simple column-sweep recurrences with prefix
sums.  For ``(19, 53)`` the staircase has only 468 points, so everything
is exact integer arithmetic in well under a second.  The reduction is
validated against a direct subset enumeration over the gaps for small
parameter pairs, alongside both given values.
"""

from __future__ import annotations

from itertools import combinations


def frog_sum(a: int, b: int) -> int:
    """F(a, b) via the antichain decomposition."""
    h = [0] * b  # column heights, index x = 1..b-1
    for x in range(1, b):
        h[x] = max(0, (a * b - a * x - 1) // b)  # max y with ab - ax - by >= 1
    maxy = a  # heights are < a

    # right[x][y]: antichains within columns > x using only heights < y
    right = [[0] * (maxy + 2) for _ in range(b + 1)]
    nxt = [1] * (maxy + 2)
    for x in range(b - 1, 0, -1):
        right[x] = nxt
        cur = [0] * (maxy + 2)
        pref = [0] * (maxy + 2)
        for y0 in range(1, maxy + 1):
            pref[y0] = pref[y0 - 1] + (nxt[y0] if y0 <= h[x] else 0)
        for y in range(maxy + 2):
            cur[y] = nxt[y] + pref[min(max(y - 1, 0), maxy)]
        nxt = cur

    # left[x][y]: antichains within columns < x using only heights > y
    left = [[0] * (maxy + 2) for _ in range(b + 1)]
    prev = [1] * (maxy + 2)
    for x in range(1, b):
        left[x] = prev
        cur = [0] * (maxy + 2)
        suf = [0] * (maxy + 3)
        for y0 in range(maxy, 0, -1):
            suf[y0] = suf[y0 + 1] + (prev[y0] if y0 <= h[x] else 0)
        for y in range(maxy + 1):
            cur[y] = prev[y] + suf[y + 1]
        cur[maxy + 1] = prev[maxy + 1]
        prev = cur

    total = 0
    for x in range(1, b):
        for y in range(1, h[x] + 1):
            g = a * b - a * x - b * y
            total += g * left[x][y] * right[x][y]
    return total


def frog_sum_brute(a: int, b: int) -> int:
    """Direct enumeration over subsets of gaps, for validation."""
    frob = a * b - a - b
    rep = [False] * (frob + a + b + 1)
    rep[0] = True
    for n in range(1, len(rep)):
        rep[n] = (n >= a and rep[n - a]) or (n >= b and rep[n - b])
    gaps = [g for g in range(1, frob + 1) if not rep[g]]
    total = 0
    for k in range(1, len(gaps) + 1):
        for combo in combinations(gaps, k):
            if all(not rep[q - p] for p, q in combinations(combo, 2)):
                total += sum(combo)
    return total


if __name__ == "__main__":
    for a, b in ((3, 5), (3, 7), (5, 7), (4, 9)):
        assert frog_sum(a, b) == frog_sum_brute(a, b), f"brute check ({a},{b})"
    assert frog_sum(3, 5) == 23, "checkpoint F(3,5)"
    assert frog_sum(5, 13) == 16336, "checkpoint F(5,13)"
    print(frog_sum(19, 53))  # 2727531976556215755
