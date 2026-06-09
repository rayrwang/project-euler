MOD = 10**9

# Rods 0=A, 1=B, 2=C, with positions a < b < c < k, so rod index order matches
# position order. The six directed rod transitions are indexed 0..5.
TRANSITIONS = [(f, t) for f in range(3) for t in range(3) if f != t]
TIDX = {ft: i for i, ft in enumerate(TRANSITIONS)}

def step_dp(cur: dict, m: int) -> dict:
    """Advance the transition-count DP to level m.

    cur[(X, Y, S)] is the 6-vector of directed rod-transition counts made while
    moving m-1 disks X->Y with Bob starting at rod S (Bob ends at Y, or at S if
    m-1 == 0). Optimal play is the unique minimal Hanoi sequence, so moving m
    disks X->Y (third rod Z) decomposes as: m-1 disks X->Z (start S), then walk
    Z->X and carry the big disk X->Y, then m-1 disks Z->Y (start Y).
    """
    nxt: dict = {}
    for x in range(3):
        for y in range(3):
            if x == y:
                continue
            z = 3 - x - y
            for s in range(3):
                v = [0] * 6
                if m == 1:
                    v[TIDX[(x, y)]] += 1
                    if s != x:
                        v[TIDX[(s, x)]] += 1
                else:
                    a1 = cur[(x, z, s)]
                    a2 = cur[(z, y, y)]
                    for i in range(6):
                        v[i] = (a1[i] + a2[i]) % MOD
                    v[TIDX[(z, x)]] = (v[TIDX[(z, x)]] + 1) % MOD
                    v[TIDX[(x, y)]] = (v[TIDX[(x, y)]] + 1) % MOD
                nxt[(x, y, s)] = v
    return nxt

def fp_mod(pos_from: int, pos_to: int, k: int, going_right: bool) -> int:
    """Expected first-passage distance of the reflecting walk on {1..k}, mod MOD.
    Rightward (to a larger square): (y-1)^2 - (x-1)^2; leftward: (k-y)^2-(k-x)^2.
    """
    if going_right:
        hi = (pos_to - 1) % MOD
        lo = (pos_from - 1) % MOD
    else:
        hi = (k - pos_to) % MOD
        lo = (k - pos_from) % MOD
    return (hi * hi - lo * lo) % MOD

def _expected_exact(n: int, k: int, a: int, b: int, c: int) -> int:
    """E(n,k,a,b,c) in exact integers, for checking the given examples."""
    cur: dict = {}
    for m in range(1, n + 1):
        cur = step_dp(cur, m)
    counts = cur[(0, 2, 1)]
    pos = (a, b, c)
    total = 0
    for f, t in TRANSITIONS:
        if t > f:
            fp = (pos[t] - 1) ** 2 - (pos[f] - 1) ** 2
        else:
            fp = (k - pos[t]) ** 2 - (k - pos[f]) ** 2
        total += counts[TIDX[(f, t)]] * fp
    return total

if __name__ == "__main__":
    assert _expected_exact(2, 5, 1, 3, 5) == 60
    assert _expected_exact(3, 20, 4, 9, 17) == 2358

    total = 0
    cur: dict = {}
    pa = pb = pc = pk = 1  # 3^n, 6^n, 9^n, 10^n mod MOD, built up incrementally
    for n in range(1, 10001):
        pa = pa * 3 % MOD
        pb = pb * 6 % MOD
        pc = pc * 9 % MOD
        pk = pk * 10 % MOD
        cur = step_dp(cur, n)
        counts = cur[(0, 2, 1)]  # n disks A->C, Bob starts at B
        pos = (pa, pb, pc)
        e_n = 0
        for f, t in TRANSITIONS:
            fp = fp_mod(pos[f], pos[t], pk, t > f)
            e_n = (e_n + counts[TIDX[(f, t)]] * fp) % MOD
        total = (total + e_n) % MOD
    print(total)  # 684901360
