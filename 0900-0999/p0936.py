"""Project Euler 936: Peerless Trees.

Count unlabelled trees with no edge joining two vertices of equal degree.

Rooted generating functions with degree tracking.  Let f_d(x) be the GF
(by vertex count) of rooted trees whose root has d children and will be
attached to a parent, so its eventual degree is d + 1; all internal
edges, including root-child edges, satisfy the constraint.  A child
whose own root has c children has degree c + 1, so the constraint at a
root-child edge is simply c != d:

    f_d = x * MSET_d( T \\ F_d ),     T = union of all classes F_c.

The multiset over a set difference is handled by one incremental
knapsack DP per d: DP_d[j][w] = number of multisets of j subtrees with
total weight w drawn from the classes {f_c : c != d}, where object
classes of weight m are folded in (with multiset binomials
C(a + j' - 1, j')) once all f_c[m] are known.  Because a multiset of j
subtrees with total weight n - 1 only uses subtrees of size < n, the
tables can be grown size by size.

Unrooted counts follow from the dissymmetry theorem.  Vertex-rooted
trees: a root with d children and no parent has degree d, so children
must avoid c = d - 1, giving V[n] = sum_d DP_{d-1}[d][n-1] (the same
exclusion tables, queried one level deeper).  Edge-rooted trees join
two attached-rooted trees whose roots have a and b children with
a + 1 != b + 1; since a != b the two halves are never isomorphic, no
symmetric-edge correction exists, and

    P(n) = V[n] - sum_{n1+n2=n} (T[n1] T[n2] - sum_c f_c[n1] f_c[n2]) / 2.

Validated against brute force over networkx's nonisomorphic trees for
n <= 12 and the given P(7) = 6, S(10) = 74.  Runs in a few seconds.
"""

from math import comb

N_MAX = 50


def solve() -> int:
    nmax = N_MAX
    dmax = nmax
    f = [[0] * (nmax + 1) for _ in range(dmax)]
    dp = [[[0] * (nmax + 1) for _ in range(nmax + 1)] for _ in range(dmax)]
    for d in range(dmax):
        dp[d][0][0] = 1
    vert = [0] * (nmax + 1)

    for n in range(1, nmax + 1):
        m = n - 1
        if m >= 1:
            per_class = [f[c][m] for c in range(dmax)]
            total_m = sum(per_class)
            for d in range(dmax):
                a = total_m - per_class[d]
                if a == 0:
                    continue
                tab = dp[d]
                jp_max = nmax // m
                for j in range(nmax, 0, -1):
                    row = tab[j]
                    for w in range(nmax, m - 1, -1):
                        s = 0
                        jp = 1
                        while jp <= j and jp * m <= w and jp <= jp_max:
                            s += (comb(a + jp - 1, jp)
                                  * tab[j - jp][w - jp * m])
                            jp += 1
                        if s:
                            row[w] += s
        if n == 1:
            f[0][1] = 1
            vert[1] = 1
            continue
        for d in range(1, min(dmax, n)):
            f[d][n] = dp[d][d][n - 1]
        vert[n] = sum(dp[d - 1][d][n - 1] for d in range(1, n)
                      if d - 1 < dmax)

    tot = [sum(f[c][m] for c in range(dmax)) for m in range(nmax + 1)]
    p = [0] * (nmax + 1)
    for m in range(3, nmax + 1):
        e2 = 0
        for n1 in range(1, m):
            n2 = m - n1
            e2 += (tot[n1] * tot[n2]
                   - sum(f[c][n1] * f[c][n2] for c in range(dmax)))
        p[m] = vert[m] - e2 // 2

    assert p[7] == 6
    assert sum(p[3:11]) == 74
    return sum(p[3:nmax + 1])


if __name__ == "__main__":
    print(solve())  # 12144907797522336
