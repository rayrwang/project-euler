import numpy as np

Q = 100000007


def build_transfer() -> np.ndarray:
    """Layer transfer matrix for filling a 3x3xn tower with 1x1x2 blocks.

    A block is either flat in its layer (two in-plane orientations) or
    vertical, occupying one cell in two consecutive layers. The state
    between layers is the 9-bit mask of cells protruding upward;
    t[s][s2] counts the fillings of one layer whose cells in mask s are
    already occupied from below and which protrudes mask s2 into the next
    layer, enumerated by a first-free-cell recursion.
    """
    t = np.zeros((512, 512), dtype=np.int64)

    def fill(occ: int, protr: int, s_row: int) -> None:
        if occ == 511:
            t[s_row][protr] += 1
            return
        low = (occ ^ 511) & -(occ ^ 511)
        i = low.bit_length() - 1
        r, c = divmod(i, 3)
        fill(occ | low, protr | low, s_row)  # vertical, protrude up
        if c < 2 and not occ & (low << 1):  # in-layer, to the right
            fill(occ | low | (low << 1), protr, s_row)
        if r < 2 and not occ & (low << 3):  # in-layer, downward
            fill(occ | low | (low << 3), protr, s_row)

    for s in range(512):
        fill(s, 0, s)
    return t


def berlekamp_massey(seq: list[int], mod: int) -> list[int]:
    """Shortest c with seq[n] = sum c[j] seq[n-1-j] (mod prime `mod`)."""
    last: list[int] = []
    cur: list[int] = []
    last_fail = 0
    last_delta = 0
    for i in range(len(seq)):
        t = sum(cur[j] * seq[i - 1 - j] for j in range(len(cur))) % mod
        delta = (seq[i] - t) % mod
        if delta == 0:
            continue
        if not cur:
            cur = [0] * (i + 1)
            last_fail, last_delta = i, delta
            continue
        k = delta * pow(last_delta, mod - 2, mod) % mod
        c = [0] * (i - last_fail - 1) + [k] + [(-k * x) % mod for x in last]
        if len(c) < len(cur):
            c += [0] * (len(cur) - len(c))
        merged = [(a + b) % mod for a, b in zip(c, cur)] + c[len(cur) :]
        if i - len(cur) >= last_fail - len(last):
            last, last_fail, last_delta = cur, i, delta
        cur = merged
    return cur


def solve(n: int) -> int:
    """f(n) mod Q for the 3x3xn tower, n even and astronomically large.

    f(n) = (T^n)[0][0] for the 512-state transfer matrix T, so the even
    subsequence g(k) = f(2k) satisfies a linear recurrence of degree at
    most 512 — Berlekamp-Massey on 200 generated terms finds degree 19,
    verified to predict every remaining generated term. Kitamasa then
    evaluates g at k = n/2: compute x^(n/2) modulo the characteristic
    polynomial by binary exponentiation (O(d^2) per multiply) and combine
    with the initial terms.
    """
    t = build_transfer().T
    vec = np.zeros(512, dtype=np.int64)
    vec[0] = 1
    g = [1]
    for _ in range(1, 200):
        vec = t @ vec % Q
        vec = t @ vec % Q
        g.append(int(vec[0]))
    rec = berlekamp_massey(g, Q)
    d = len(rec)
    assert all(
        sum(rec[j] * g[k - 1 - j] for j in range(d)) % Q == g[k]
        for k in range(d, len(g))
    )

    def polymulmod(a: list[int], b: list[int]) -> list[int]:
        res = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    res[i + j] = (res[i + j] + ai * bj) % Q
        for i in range(len(res) - 1, d - 1, -1):
            c = res[i]
            if c:
                res[i] = 0
                for j in range(d):
                    res[i - 1 - j] = (res[i - 1 - j] + c * rec[j]) % Q
        return res[:d]

    result = [1]
    base = [0, 1]
    e = n // 2
    while e:
        if e & 1:
            result = polymulmod(result, base)
        base = polymulmod(base, base)
        e >>= 1
    return sum(result[i] * g[i] for i in range(len(result))) % Q


if __name__ == "__main__":
    assert solve(2) == 229
    assert solve(4) == 117805
    assert solve(10) == 96149360
    assert solve(10**3) == 24806056
    assert solve(10**6) == 30808124
    print(solve(10**10000))  # 96972774
