"""Project Euler 992.

A journey is a walk on the path graph of stones 0..n that starts at 0 and
visits stone i exactly k+i times (0 <= i < n); stone n is unrestricted. Fix the
final stone E. Let r_i and l_i be the numbers of rightward and leftward
crossings of the edge between stones i and i+1. Balancing arrivals against
departures (a visit = an arrival, plus 1 for the start) pins every crossing:
    l_0 = k - 1,  r_0 = l_0 + [E > 0],
    l_i = (k + i) - r_{i-1},  r_i = l_i + [E > i].
So each E gives one crossing profile (discard it if any count is negative).

The journeys with that profile are exactly the directed Eulerian trails from 0
to E in the multigraph that has r_i copies of the edge i -> i+1 and l_i copies
of i+1 -> i. By the BEST theorem (adding a dummy edge E -> 0 to balance the
digraph), the number of *labelled* such trails is
    t_E * prod_v (outdeg'(v) - 1)!,
where t_E is the number of spanning arborescences oriented toward E. For a path
that arborescence count is simply prod_{v<E} r_v * prod_{v>E} l_{v-1}. Parallel
crossings are indistinguishable for a walk, so divide by prod_i r_i! l_i!.

J(n, k) sums this over all valid end stones E.
"""
def solve():
    P = 987_898_789
    MAXK = 10 ** 4
    n = 500
    NMAX = 2 * (MAXK + n) + 10
    fact = [1] * (NMAX + 1)
    for i in range(1, NMAX + 1):
        fact[i] = fact[i - 1] * i % P
    invf = [1] * (NMAX + 1)
    invf[NMAX] = pow(fact[NMAX], P - 2, P)
    for i in range(NMAX, 0, -1):
        invf[i - 1] = invf[i] * i % P

    def W(k, E):
        l = [0] * n
        r = [0] * n
        l[0] = k - 1
        if l[0] < 0:
            return 0
        r[0] = l[0] + (1 if E > 0 else 0)
        for i in range(1, n):
            l[i] = (k + i) - r[i - 1]
            if l[i] < 0:
                return 0
            r[i] = l[i] + (1 if E > i else 0)
        # top vertex actually visited
        M = n if (r[n - 1] > 0 or l[n - 1] > 0) else n - 1
        dout = [0] * (M + 1)
        dout[0] = r[0]
        for v in range(1, M):
            dout[v] = r[v] + l[v - 1]
        dout[M] = (l[n - 1] if M == n else r[M] + l[M - 1])
        dout[E] += 1                                   # dummy edge E -> 0
        t = 1
        for v in range(0, E):
            t = t * r[v] % P
        for v in range(E + 1, M + 1):
            t = t * l[v - 1] % P
        if t == 0:
            return 0
        res = t
        for v in range(M + 1):
            if dout[v] == 0:
                return 0
            res = res * fact[dout[v] - 1] % P
        for i in range(M):
            res = res * invf[r[i]] % P * invf[l[i]] % P
        return res

    def J(k):
        return sum(W(k, E) for E in range(n + 1)) % P

    return sum(J(10 ** s) for s in range(5)) % P

if __name__ == "__main__":
    print(solve())  # 568021234
