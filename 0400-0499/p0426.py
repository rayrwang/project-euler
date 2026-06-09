import numba
import numpy as np

HUGE = 1 << 60  # stands in for the infinite run of empty boxes on the right

@numba.jit(cache=True)
def t_sequence(n_terms: int) -> np.ndarray:
    t = np.empty(n_terms, dtype=np.int64)
    s = 290797
    for k in range(n_terms):
        t[k] = s % 64 + 1
        s = s * s % 50515093
    return t

@numba.jit(cache=True)
def soliton_square_sum(t: np.ndarray) -> int:
    """Sum of squares of the final state of the box-ball system started
    from the alternating run lengths in t (occupied first).

    The soliton content is conserved, and by Takahashi-Satsuma the number
    of solitons of size >= k equals E_k, the number of '10' boundaries
    after k-1 rounds of deleting every (ball, empty) boundary pair at
    once. On the run-length encoding each round decrements every node's
    ball and empty runs by one and compacts (vanished empties merge ball
    runs; vanished ball runs merge empties), so a round costs O(nodes)
    and the total work is sum_k E_k = number of balls. The answer
    telescopes: sum over sizes k of (E_k - E_{k+1}) k^2 = sum_k E_k (2k-1).
    """
    n = len(t)
    n_nodes = (n + 1) // 2 if n % 2 == 0 else n // 2 + 1
    ball = np.empty(n_nodes + 1, dtype=np.int64)
    empty = np.empty(n_nodes + 1, dtype=np.int64)
    new_ball = np.empty(n_nodes + 1, dtype=np.int64)
    new_empty = np.empty(n_nodes + 1, dtype=np.int64)
    cnt = 0
    for i in range(0, n, 2):
        ball[cnt] = t[i]
        empty[cnt] = t[i + 1] if i + 1 < n else HUGE
        cnt += 1
    total = 0
    k = 0
    while cnt > 0:
        k += 1
        total += cnt * (2 * k - 1)  # E_k contributions, telescoped
        out = 0
        pending = 0
        for i in range(cnt):
            pending += ball[i] - 1
            e = empty[i] - 1
            if e > 0:
                if pending > 0:
                    new_ball[out] = pending
                    new_empty[out] = e
                    out += 1
                    pending = 0
                elif out > 0:  # empty run extends the previous one
                    new_empty[out - 1] += e
                # else: leading empties fall off the front
        ball, new_ball = new_ball, ball
        empty, new_empty = new_empty, empty
        cnt = out
    return total

def final_state(t: list[int]) -> list[int]:
    """Soliton multiset, ascending, via the same elimination in plain
    Python (for the checks)."""
    nodes = [[t[i], t[i + 1] if i + 1 < len(t) else HUGE]
             for i in range(0, len(t), 2)]
    sizes = []
    k = 0
    prev = len(nodes)
    while nodes:
        k += 1
        nxt: list[list[int]] = []
        pending = 0
        for b, e in nodes:
            pending += b - 1
            e -= 1
            if e > 0:
                if pending > 0:
                    nxt.append([pending, e])
                    pending = 0
                elif nxt:
                    nxt[-1][1] += e
        nodes = nxt
        sizes += [k] * (prev - len(nodes))
        prev = len(nodes)
    return sorted(sizes)

def simulate_bbs(t: list[int]) -> list[int]:
    """Run actual turns until the occupied-run lengths stop changing."""
    cells = []
    occupied = True
    for run in t:
        cells += [occupied] * run
        occupied = not occupied
    cells += [False] * (sum(cells) * (len(t) + 2))

    def runs(c: list[bool]) -> list[int]:
        out = []
        n = 0
        for v in c:
            if v:
                n += 1
            elif n:
                out.append(n)
                n = 0
        return out

    while True:
        before = runs(cells)
        carrier = 0
        for i, v in enumerate(cells):
            if v:
                carrier += 1
                cells[i] = False
            elif carrier:
                carrier -= 1
                cells[i] = True
        after = runs(cells)
        # free solitons keep their run lengths between collisions, so an
        # unchanged list alone is not final; once it is also non-decreasing
        # the faster (larger) solitons are in front and never interact again
        if before == after and all(
                after[i] <= after[i + 1] for i in range(len(after) - 1)):
            return after

if __name__ == "__main__":
    assert final_state([2, 2, 2, 1, 2]) == [1, 2, 3]  # given example
    t11 = [int(v) for v in t_sequence(11)]
    assert final_state(t11) == [1, 3, 10, 24, 51, 75]  # given example
    assert soliton_square_sum(t_sequence(11)) == sum(
        v * v for v in [1, 3, 10, 24, 51, 75])
    # elimination agrees with a direct turn-by-turn simulation
    t31 = [int(v) for v in t_sequence(31)]
    assert final_state(t31) == simulate_bbs(t31)
    print(soliton_square_sum(t_sequence(10**7 + 1)))  # 31591886008
