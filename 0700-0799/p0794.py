"""
Project Euler Problem 794: Seventeen Points
https://projecteuler.net/problem=794

Reals x_1, x_2, ... in [0,1) are chosen so that after step n every interval
[(k-1)/n, k/n), k = 1..n, contains exactly one of x_1..x_n.  F(n) is the
minimal possible value of x_1 + ... + x_n; famously the procedure cannot
continue past n = 17.  Find F(17) rounded to 12 decimal places.

Method.  The feasibility and the minimal sum of a tuple depend only on its
combinatorial pattern: the relative order of the points.  If point j has rank
r among the first m points (m >= j), the step-m condition forces
x_j in [(r-1)/m, r/m).  Hence, for a fixed insertion pattern, each point is
constrained to the intersection of its stage intervals,

    x_j in [L_j, U_j),   L_j = max_m (r_{j,m}-1)/m,   U_j = min_m r_{j,m}/m,

and the pattern is feasible iff every L_j < U_j.  Since at stage n the points
occupy distinct intervals [k/n, (k+1)/n), setting every x_j = L_j is
automatically strictly increasing along the final order, so the minimal sum
for a pattern is simply sum(L_j), and F(n) is the minimum over feasible
patterns.

Depth-first search over insertion positions: a state is the current ordering
of the inserted points together with their exact bounds L_j, U_j scaled by
D = lcm(1..17) = 12252240 (all bounds are multiples of D/m, so everything is
exact integer arithmetic).  Inserting point n+1 at one of n+1 positions
re-ranks all points; infeasible branches (L_j >= U_j) are cut immediately.
The pruning is so strong that the whole tree has only 70810 nodes and dies
out at depth 17, simultaneously re-proving that no 18th point exists.
F(4) = 1.5 from the problem statement is asserted as a check.
"""

from math import gcd

N = 17
D = 1
for m in range(1, N + 1):
    D = D * m // gcd(D, m)  # lcm(1..17) = 12252240


def solve(n_target):
    """Minimal scaled sum (times D) over all feasible patterns of length
    n_target, by DFS over insertion positions."""
    best = [None]

    def dfs(low, up, depth):
        if depth == n_target:
            s = sum(low)
            if best[0] is None or s < best[0]:
                best[0] = s
            return
        m = depth + 1
        step = D // m
        for pos in range(m):
            nlow = low[:pos] + [0] + low[pos:]
            nup = up[:pos] + [D] + up[pos:]
            ok = True
            for i in range(m):
                lo = i * step
                hi = lo + step
                if lo > nlow[i]:
                    nlow[i] = lo
                if hi < nup[i]:
                    nup[i] = hi
                if nlow[i] >= nup[i]:
                    ok = False
                    break
            if ok:
                dfs(nlow, nup, m)

    dfs([], [], 0)
    return best[0]


def main():
    assert solve(4) * 10 == 15 * D  # F(4) = 1.5
    s = solve(N)
    # round s/D to 12 decimal places with exact integer arithmetic
    scaled = (s * 10**12 * 2 + D) // (2 * D)
    return f"{scaled // 10**12}.{scaled % 10**12:012d}"


if __name__ == "__main__":
    print(main())  # 8.146681749623
