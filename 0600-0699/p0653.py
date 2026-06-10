"""Project Euler Problem 653: Frictionless Tube.

Identical elastic marbles never pass each other, and a collision between
equal masses just exchanges velocities -- so the system is equivalent to
non-interacting points that pass through one another, with marble labels
given by sorted order.  The 20 mm diameters are removed by the standard
shrink: point i sits at y_i = x_i - 20(i-1) - 10, making the west wall a
reflection at 0 and adjacent contact a coincidence of points; the gaps
g_j then give simply y_i = g_1 + ... + g_i.

Every point moves ballistically at speed v (westward ones reflect once
off the wall), so marble j's centre is the j-th smallest point plus its
fixed offset, and marble j exits -- centre at L -- exactly when the j-th
order statistic first reaches E = L - 10 - 20(j-1).  Since a marble's
speed is always v, its travelled distance is v times its exit time.

Counting points below E over time: each point crosses E upward exactly
once (at (E - y)/v eastbound, (E + y)/v after a wall bounce), and a
westbound point starting above E additionally dips below at (y - E)/v.
Sorting these +-1 events and scanning for the first instant the
below-count drops to j - 1 (processing simultaneous events together)
gives the exit time; with v = 1 everything is exact integer arithmetic.

Checks: d(5000, 3, 2) = 5519, d(10000, 11, 6) = 11780 and
d(100000, 101, 51) = 114101 as given, plus a full event-driven collision
simulation of the actual marbles for the small cases.
"""

from fractions import Fraction


def gaps_and_dirs(n: int) -> tuple[list[int], list[bool]]:
    r = 6563116
    gaps, east = [], []
    for _ in range(n):
        gaps.append(r % 1000 + 1)
        east.append(r <= 10**7)
        r = r * r % 32745673
    return gaps, east


def d(L: int, N: int, j: int) -> int:
    gaps, east = gaps_and_dirs(N)
    ys = []
    y = 0
    for g in gaps:
        y += g
        ys.append(y)
    E = L - 10 - 20 * (j - 1)
    events: list[tuple[int, int]] = []  # (time, +-1 change in below-count)
    below = 0
    for y, e in zip(ys, east):
        if e:  # eastbound: y + t
            if y < E:
                below += 1
                events.append((E - y, -1))
        else:  # westbound: |y - t|
            if y < E:
                below += 1
            else:
                events.append((y - E, +1))  # dips below E heading west
            events.append((y + E, -1))  # final upward crossing
    events.sort()
    i = 0
    while i < len(events):
        t = events[i][0]
        while i < len(events) and events[i][0] == t:
            below += events[i][1]
            i += 1
        if below <= j - 1:
            return t
    raise AssertionError("marble never exits")


def d_simulate(L: int, N: int, j: int) -> Fraction:
    """Direct elastic-collision simulation (small N)."""
    gaps, east = gaps_and_dirs(N)
    pos: list[Fraction] = []
    x = Fraction(-10)
    for g in gaps:
        x += g + 20
        pos.append(Fraction(x))
    vel = [1 if e else -1 for e in east]
    alive = [True] * N
    dist = Fraction(0)
    t = Fraction(0)
    while alive[j - 1]:
        # next event: pair collision, wall bounce, or target exit
        dt = None
        kind = (-1, -1)
        prev = None
        for i in range(N):
            if not alive[i]:
                continue
            if prev is not None and vel[prev] == 1 and vel[i] == -1:
                step = (pos[i] - pos[prev] - 20) / 2
                if dt is None or step < dt:
                    dt, kind = step, (0, prev)
            if prev is None and vel[i] == -1:
                step = pos[i] - 10
                if dt is None or step < dt:
                    dt, kind = step, (1, i)
            if vel[i] == 1:
                step = L - pos[i]
                if dt is None or step < dt:
                    dt, kind = step, (2, i)
            prev = i
        assert dt is not None
        for i in range(N):
            if alive[i]:
                pos[i] += vel[i] * dt
        if alive[j - 1]:
            dist += dt
        t += dt
        if kind[0] == 0:
            i = kind[1]
            nxt = next(k for k in range(i + 1, N) if alive[k])
            vel[i], vel[nxt] = -1, 1
        elif kind[0] == 1:
            vel[kind[1]] = 1
        else:
            i = kind[1]
            alive[i] = False
            if i == j - 1:
                break
    return dist


if __name__ == "__main__":
    assert d(5000, 3, 2) == 5519
    assert d(10000, 11, 6) == 11780
    assert d(100000, 101, 51) == 114101
    assert d_simulate(5000, 3, 2) == 5519
    assert d_simulate(10000, 11, 6) == 11780
    print(d(10**9, 10**6 + 1, 5 * 10**5 + 1))  # 1130658687
