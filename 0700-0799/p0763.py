"""Problem 763: Amoebas in a 3D grid.

An amoeba at ``(x, y, z)`` divides into three amoebas at ``(x+1, y, z)``,
``(x, y+1, z)`` and ``(x, y, z+1)`` whenever those three cells are empty.
Starting from a single amoeba at the origin, ``D(N)`` is the number of distinct
arrangements (sets of occupied cells) reachable after exactly ``N`` divisions.
We want the last nine digits of ``D(10000)``.

Approach
--------
A division consumes ``(x, y, z)`` and creates the three forward neighbours, so
the *consumed* cells form a downward-closed staircase: a cell may fire only once
its three predecessors have fired (in 3D, re-firing never happens, which was
verified by exhaustive search inside a box). Hence ``D(N)`` counts the reachable
sets of ``N`` "fired" cells, and an arrangement is reconstructed uniquely from
that set. Sweeping the antidiagonal planes ``x + y + z = d`` in order, the state
is the *frontier*: which cells of the current plane have fired. A cell on the
next plane is *forced* to fire if two of its back-neighbours already fired,
*free* if exactly one did, and *forbidden* if none did; a sweep terminates when
the frontier becomes empty.

Most frontiers are "thick" and self-sustain forever (they never terminate and
contribute nothing). Grouping frontiers by their forward counting behaviour
(a Myhill-Nerode collapse) leaves a clean family of *live* classes ``(L, j)``:

* the class organises by a *level* ``L`` (its earliest termination needs exactly
  ``T(L) = L(L+1)/2`` further cells), and level ``L`` holds exactly ``L`` classes
  ``j = 0 .. L-1`` (levels 0 and 1 hold a single class);
* every transition is DOWN/STAY/UP one level, adding ``L``, ``L+1`` or ``L+2``
  cells respectively, with the sub-index rules encoded in ``build_edges``.

Writing ``g_{(L,j)}(x)`` for the generating function in added cells, the seed
``(0,0)`` carries the only termination option and ``D(N) = [x^{N-1}] g_{(0,0)}``.
Because every increment is at least one, coefficients are computed degree by
degree. Only levels with ``T(L) <= N`` matter, i.e. ``L = O(sqrt N)`` (about 141
for ``N = 10000``), giving ``O(N)`` classes and an ``O(N^1.5)`` sliding-window
recurrence. The rules, fixed from levels up to five, reproduce the exact values
through ``D(20)`` and the stated ``D(100) (mod 10^9)``, and yield ``D(10000)``.
"""

import numpy as np
import numba


def build_edges(lmax):
    """Flatten the level-automaton into (src, dst, incr, coeff) edge arrays."""
    index = {}
    for level in range(lmax + 1):
        for j in range(1 if level <= 1 else level):
            index[(level, j)] = len(index)
    src, dst, incr, coeff = [], [], [], []

    def add(a, b, i, c):
        src.append(index[a])
        dst.append(index[b])
        incr.append(i)
        coeff.append(c)

    for level in range(lmax + 1):
        for j in range(1 if level <= 1 else level):
            if level == 0:
                add((0, 0), (0, 0), 1, 3)            # STAY
                if lmax >= 1:
                    add((0, 0), (1, 0), 2, 3)        # UP
            elif level == 1:
                add((1, 0), (0, 0), 1, 1)            # DOWN
                add((1, 0), (1, 0), 2, 4)            # STAY
                if lmax >= 2:
                    add((1, 0), (2, 0), 3, 2)        # UP
                    add((1, 0), (2, 1), 3, 1)
            else:
                down, stay, up = level, level + 1, level + 2
                add((level, j), (level - 1, min(j, level - 2)), down, 1)
                if j == 0:
                    add((level, j), (level, 0), stay, 2)
                    add((level, j), (level, 1), stay, 1)
                elif j == level - 1:
                    add((level, j), (level, 0), stay, 2)
                    add((level, j), (level, level - 1), stay, 2)
                else:
                    add((level, j), (level, 0), stay, 1)
                    add((level, j), (level, j), stay, 1)
                    add((level, j), (level, j + 1), stay, 1)
                if level + 1 <= lmax:
                    if j == level - 1:
                        add((level, j), (level + 1, 0), up, 2)
                        add((level, j), (level + 1, level), up, 1)
                    else:
                        add((level, j), (level + 1, 0), up, 1)
                        add((level, j), (level + 1, j + 1), up, 1)

    return (
        np.array(src, np.int64),
        np.array(dst, np.int64),
        np.array(incr, np.int64),
        np.array(coeff, np.int64),
        len(index),
        index[(0, 0)],
    )


@numba.jit(cache=True)
def run(src, dst, incr, coeff, n_classes, seed, n, width, mod):
    """Degree-by-degree coefficients of g_seed via a sliding ring buffer.

    g[c] only depends on g[c - incr] with incr >= 1, so a window of the last
    ``width`` degrees suffices; ``D(n)`` is the coefficient at degree ``n - 1``.
    """
    g = np.zeros((n_classes, width), np.int64)
    g[seed, 0] = 1 % mod
    answer = 1 % mod
    n_edges = src.shape[0]
    for c in range(1, n):
        col = c % width
        for i in range(n_classes):
            g[i, col] = 0
        for e in range(n_edges):
            step = incr[e]
            if c - step >= 0:
                g[src[e], col] = (
                    g[src[e], col] + coeff[e] * g[dst[e], (c - step) % width]
                ) % mod
        if c == n - 1:
            answer = g[seed, col]
    return answer


def d_value(n, mod):
    """Return D(n) modulo ``mod`` (use a large modulus for exact small values)."""
    lmax = 1
    while lmax * (lmax + 1) // 2 <= n:
        lmax += 1
    lmax += 2
    src, dst, incr, coeff, n_classes, seed = build_edges(lmax)
    width = int(incr.max()) + 2
    return int(run(src, dst, incr, coeff, n_classes, seed, max(n, 1), width, mod))


if __name__ == "__main__":
    # Exact checks against the values stated in the problem (all below 10**18,
    # and the per-step accumulation stays well within int64).
    big = 10**18
    assert d_value(2, big) == 3
    assert d_value(10, big) == 44499
    assert d_value(20, big) == 9204559704
    # Last nine digits, as given for D(100).
    assert d_value(100, 10**9) == 780166455

    print(d_value(10000, 10**9))  # 798443574
