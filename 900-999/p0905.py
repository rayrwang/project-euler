"""Project Euler 905.

Three logicians wear positive-integer hats; exactly one number equals the sum
of the other two. Each sees the other two (not their own) and on their turn
(cyclically A, B, C) says "I don't know" or "Now I know". F(A,B,C) is the turn
on which someone first knows.

Model it as public elimination of possible worlds. A world is a valid triple.
At turn t the player p = (t-1) mod 3 sees the two coordinates other than p; the
two values they could hold are the sum and the absolute difference of what they
see, so there are at most two candidate worlds (the real one and its "flip").
A world is eliminated at the first turn its scheduled player would know, which
is exactly F of that world. Hence:

    knows(w, t)  iff  the two seen values are equal (only one candidate)
                      or the flipped world was already eliminated, F(flip) <= t-1.

Taking the minimum over players shows the deciding player is always the holder
of the sum, and flipping the sum coordinate to |s - u| is one subtractive
Euclidean step on the two "part" values (the sum position migrating to the
larger part). So F is built bottom-up along the Euclidean descent of the parts:
at the base (equal parts) F = psum + 1, and climbing one step

    F = smallest t > F_below with t == (psum + 1) (mod 3),

where psum in {0,1,2} is the position of the sum at that step. A naive
subtractive descent is far too long (a single quotient can be ~10^7 steps), so
we compress each quotient into one run: within a run the sum position simply
alternates between two slots, and the climb's per-step increment is constant
after the first step (each pair of alternating steps raises F by exactly 3), so
a whole run is handled in O(1). The descent then has only O(log) runs.

Summing F(a^b, b^a, a^b + b^a) for a in 1..7, b in 1..19 gives 70228218.
"""


def apply_run(f: int, first_res: int, second_res: int, n: int) -> int:
    # Climb n steps whose target residues alternate first_res, second_res, ...
    f += ((first_res - f - 1) % 3) + 1
    if n > 1:
        g_fs = ((second_res - first_res - 1) % 3) + 1
        g_sf = ((first_res - second_res - 1) % 3) + 1
        m = n - 1
        f += ((m + 1) // 2) * g_fs + (m // 2) * g_sf
    return f


def f_value(triple: tuple[int, int, int]) -> int:
    w = list(triple)
    runs: list[tuple[int, int, int]] = []
    base = 0
    while True:
        for p in range(3):
            i, j = [k for k in range(3) if k != p]
            if w[p] == w[i] + w[j]:
                psum, pi, pj = p, i, j
                break
        vi, vj = w[pi], w[pj]
        if vi == vj:
            base = psum
            break
        if vi > vj:
            big_slot, small_slot, g, s = pi, pj, vi, vj
        else:
            big_slot, small_slot, g, s = pj, pi, vj, vi
        q, r = divmod(g, s)
        if r == 0:
            steps = q - 1
            runs.append((psum, big_slot, steps))
            other = psum if steps % 2 == 1 else big_slot
            sumslot = big_slot if steps % 2 == 1 else psum
            w[small_slot] = s
            w[other] = s
            w[sumslot] = 2 * s
        else:
            steps = q
            runs.append((psum, big_slot, steps))
            rslot = psum if q % 2 == 1 else big_slot
            sumslot = big_slot if q % 2 == 1 else psum
            w[small_slot] = s
            w[rslot] = r
            w[sumslot] = s + r
    f = base + 1
    for psum, big_slot, count in reversed(runs):
        r_p = (psum + 1) % 3
        r_b = (big_slot + 1) % 3
        first_res = r_p if (count - 1) % 2 == 0 else r_b
        second_res = r_b if first_res == r_p else r_p
        f = apply_run(f, first_res, second_res, count)
    return f


def solve() -> int:
    total = 0
    for a in range(1, 8):
        for b in range(1, 20):
            big, small = a ** b, b ** a
            total += f_value((big, small, big + small))
    return total


if __name__ == "__main__":
    print(solve())  # 70228218
