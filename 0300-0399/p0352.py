def screen(s: int, p: float, max_group: int = 200) -> float:
    """Minimum expected number of tests to screen s sheep, each independently
    infected with probability p, under the pooling rules of the problem.

    Two states (the sheep are i.i.d.):
      A(n): cost for n "fresh" sheep (no test done yet);
      B(n): cost for n sheep known to contain at least one infected.
    Resolving B(n): pool a sub-block of size k (one test).  Given the block is
    dirty, the sub-block reads negative with prob q^k(1-q^(n-k))/(1-q^n) -- then
    that sub-block is clear and the remaining n-k stay dirty (B(n-k)); it reads
    positive with prob (1-q^k)/(1-q^n) -- then the sub-block is dirty (B(k)) and
    the remainder reverts to fresh (A(n-k)).  A single known-infected sheep needs
    no test, so B(1)=0.  A fresh flock is partitioned into atomic pooled groups
    g, each costing atom(g)=1+(1-q^g)B(g); the optimal partition is a simple
    DP, and the optimal group size is bounded, so groups above max_group (chosen
    by stabilisation) are never needed.
    """
    q = 1.0 - p
    g_cap = min(max_group, s)
    qp = [1.0] * (s + 1)
    for i in range(1, s + 1):
        qp[i] = qp[i - 1] * q

    a = [0.0] * (s + 1)
    b = [0.0] * (g_cap + 1)
    atom = [0.0] * (g_cap + 1)
    a[1] = 1.0
    atom[1] = 1.0  # b[1] = 0

    for g in range(2, g_cap + 1):
        denom = 1.0 - qp[g]
        best = float("inf")
        for k in range(1, g):
            p_neg = qp[k] * (1.0 - qp[g - k]) / denom
            p_pos = (1.0 - qp[k]) / denom
            cost = 1.0 + p_neg * b[g - k] + p_pos * (b[k] + a[g - k])
            if cost < best:
                best = cost
        b[g] = best
        atom[g] = 1.0 + denom * best
        best_a = float("inf")
        for h in range(1, g + 1):
            v = atom[h] + a[g - h]
            if v < best_a:
                best_a = v
        a[g] = best_a

    for n in range(g_cap + 1, s + 1):
        best = float("inf")
        an = a
        for h in range(1, g_cap + 1):
            v = atom[h] + an[n - h]
            if v < best:
                best = v
        a[n] = best
    return a[s]


def screen_sum(s: int, ps: range, scale: float) -> float:
    return sum(screen(s, k / scale) for k in ps)


if __name__ == "__main__":
    assert round(screen(25, 0.02), 6) == 4.155452
    assert round(screen(25, 0.10), 6) == 12.702124
    total = sum(screen(10000, k / 100.0) for k in range(1, 51))
    print(f"{total:.6f}")  # 378563.260589
