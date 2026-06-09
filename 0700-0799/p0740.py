def q(n):
    """Probability that the two-slip Secret Santa fails for n people.

    People draw in order; person i takes two uniform slips avoiding their own
    name. Track, after each turn, the distribution of (k2, k1): how many of
    the not-yet-drawn people still have 2 (resp. 1) of their own slips in the
    hat. These people are exchangeable, so the next drawer has 2/1/0 own
    slips left with probability k2/m, k1/m, k0/m (m people remaining), and
    each drawn slip is uniform over the hat minus the drawer's own slips:
    it hits a "free" slip (name of someone already done), a slip of a
    2-person (who becomes a 1-person), or a slip of a 1-person. Slip counts
    are determined by the state: of the 2m slips in the hat, c belong to the
    drawer and 2 k2' + k1' to the other remaining people (after removing the
    drawer from their class), leaving f = 2m - c - 2 k2' - k1' free; the
    drawer's own c slips are excluded during the draw and free afterwards.

    The process fails iff the final person's own slip count c is nonzero.
    """
    # State: {(k2, k1): probability} over people not yet drawn.
    dist = {(n, 0): 1.0}
    for step in range(n - 1):  # persons 1 .. n-1 draw
        m = n - step
        new = {}
        for (k2, k1), pr in dist.items():
            k0 = m - k2 - k1
            for c, kc in ((2, k2), (1, k1), (0, k0)):
                if kc == 0:
                    continue
                p_c = pr * kc / m
                # Remove drawer from their class; remaining future people:
                a2 = k2 - (c == 2)
                a1 = k1 - (c == 1)
                free = 2 * m - c - 2 * a2 - a1  # excludes drawer's c slips
                # Draw two slips from free + 2*a2 + a1, without replacement.
                for t1 in range(3):  # 0 free, 1 from a 2-person, 2 from a 1-person
                    pool = free + 2 * a2 + a1
                    cnt1 = (free, 2 * a2, a1)[t1]
                    if cnt1 == 0:
                        continue
                    p1 = p_c * cnt1 / pool
                    f2, b2, b1 = free, a2, a1
                    if t1 == 0:
                        f2 -= 1
                    elif t1 == 1:
                        b2 -= 1
                        b1 += 1
                    else:
                        b1 -= 1
                    for t2 in range(3):
                        cnt2 = (f2, 2 * b2, b1)[t2]
                        if cnt2 == 0:
                            continue
                        p2 = p1 * cnt2 / (pool - 1)
                        c2, d2, d1 = f2, b2, b1
                        if t2 == 0:
                            c2 -= 1
                        elif t2 == 1:
                            d2 -= 1
                            d1 += 1
                        else:
                            d1 -= 1
                        key = (d2, d1)
                        new[key] = new.get(key, 0.0) + p2
        dist = new
    # One person left; fail iff they still have an own slip in the hat.
    return sum(pr for (k2, k1), pr in dist.items() if k2 + k1 > 0)

if __name__ == "__main__":
    assert f"{q(3):.10f}" == "0.3611111111"
    assert f"{q(5):.10f}" == "0.2476095994"
    print(f"{q(100):.10f}")  # 0.0189581208
