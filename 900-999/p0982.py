"""Project Euler 982.

A zero-sum game of incomplete information. Alice (who sees all three dice and
moves first) minimises the expected payment, so the value is a convex
minimisation that is solved exactly by linear programming.

Alice's symmetric strategy is described by p(m, v): the probability, given the
rolled multiset m, of hiding a die of value v (revealing the other two). Bob
observes only the revealed pair o and then either takes the larger revealed
value max(o) or gambles on the hidden die, choosing whichever has the larger
expected value. So Bob contributes, per observation,
    max( max(o) * P(o),  HiddenMass(o) ),
where P(o) is the probability of seeing o and HiddenMass(o) is the probability-
weighted hidden value. Minimising the sum over observations is the LP
    min  sum_o t_o
    s.t. sum_v p(m, v) = 1,  t_o >= max(o)*P(o),  t_o >= HiddenMass(o),  p >= 0.

Solved in exact rational arithmetic; the two-dice analogue returns 145/36 as a
check, and the three-dice game returns 631/144 = 4.381944.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import factorial

def simplex(c, A, b):
    """min c.x  s.t.  A x = b (b >= 0), x >= 0 ; exact two-phase, Bland's rule."""
    m, n = len(A), len(c)
    N = n + m
    T = [[F(0)] * (N + 1) for _ in range(m)]
    basis = [n + i for i in range(m)]
    for i in range(m):
        for j in range(n):
            T[i][j] = F(A[i][j])
        T[i][n + i] = F(1)
        T[i][N] = F(b[i])

    def run(cost):
        while True:
            enter = -1
            for j in range(N):
                z = sum(cost[basis[i]] * T[i][j] for i in range(m))
                if z - cost[j] > 0:
                    enter = j
                    break
            if enter == -1:
                return
            leave, best = -1, None
            for i in range(m):
                if T[i][enter] > 0:
                    r = T[i][N] / T[i][enter]
                    if best is None or r < best or (r == best and basis[i] < basis[leave]):
                        best, leave = r, i
            piv = T[leave][enter]
            T[leave] = [v / piv for v in T[leave]]
            for i in range(m):
                if i != leave and T[i][enter] != 0:
                    f = T[i][enter]
                    T[i] = [T[i][j] - f * T[leave][j] for j in range(N + 1)]
            basis[leave] = enter

    cost1 = [F(0)] * n + [F(1)] * m
    run(cost1)
    cost2 = [F(c[j]) for j in range(n)] + [F(10) ** 9] * m
    run(cost2)
    x = [F(0)] * n
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = T[i][N]
    return sum(F(c[j]) * x[j] for j in range(n))

def value(d):
    tot = 6 ** d
    states = list(combinations_with_replacement(range(1, 7), d))

    def weight(s):
        cnt = {}
        for v in s:
            cnt[v] = cnt.get(v, 0) + 1
        w = factorial(d)
        for v in cnt:
            w //= factorial(cnt[v])
        return w

    pindex, reveal_of = {}, {}
    for s in states:
        for v in sorted(set(s)):
            pindex[(s, v)] = len(pindex)
            rev = list(s)
            rev.remove(v)
            reveal_of[(s, v)] = tuple(sorted(rev))
    oindex = {}
    for r in reveal_of.values():
        oindex.setdefault(r, len(oindex))
    nP, nO = len(pindex), len(oindex)
    nvar = nP + nO

    A, b = [], []
    for s in states:                                  # sum_v p(s,v) = 1
        row = [F(0)] * nvar
        for v in sorted(set(s)):
            row[pindex[(s, v)]] = F(1)
        A.append(row)
        b.append(F(1))
    ineq = []
    for o, oid in oindex.items():
        r1 = [F(0)] * nvar
        r2 = [F(0)] * nvar
        mr = max(o)
        for (s, v), idx in pindex.items():
            if reveal_of[(s, v)] == o:
                coef = F(weight(s), tot)
                r1[idx] += mr * coef
                r2[idx] += v * coef
        r1[nP + oid] = F(-1)
        r2[nP + oid] = F(-1)
        ineq += [r1, r2]
    ns = len(ineq)
    c = [0] * (nvar + ns)
    for oid in oindex.values():
        c[nP + oid] = 1                                # minimise sum of t_o
    A2 = [row + [F(0)] * ns for row in A]
    b2 = list(b)
    for k, row in enumerate(ineq):
        nr = row + [F(0)] * ns
        nr[nvar + k] = F(1)                            # slack variable
        A2.append(nr)
        b2.append(F(0))
    return simplex(c, A2, b2)

if __name__ == "__main__":
    print(f"{float(value(3)):.6f}")  # 4.381944
