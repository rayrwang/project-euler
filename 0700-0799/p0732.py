import numba
import numpy as np

@numba.njit(cache=True)
def Q(n):
    """Maximum total IQ of escaping trolls.

    When a troll escapes, every troll still in the hole (including himself)
    is available for the pile, so his reach is H_present + l (shoulder
    heights of everyone present, plus his arms). If c is the total shoulder
    height that has already left the hole, escape requires
        H - c + l >= D = H / sqrt(2),  i.e.  c <= B + l,  B = H - H/sqrt(2).
    This is job scheduling: escaping troll t "consumes" h_t and must start
    before its personal deadline B + l_t. Any feasible escape set can be
    ordered by deadline (earliest-deadline-first exchange argument), so a
    knapsack over trolls sorted by l, with state c = height already escaped,
    finds the maximum IQ. The threshold floor(B + l) is computed exactly:
    floor(H + l - sqrt(H^2 / 2)) = H + l - isqrt(H^2 // 2) - 1, as H/sqrt(2)
    is irrational and floor(sqrt(H^2 / 2)) = isqrt(H^2 // 2) (no integer can
    be skipped since 2 k^2 = H^2 is impossible).
    """
    mod = 10**9 + 7
    h = np.empty(n, dtype=np.int64)
    arm = np.empty(n, dtype=np.int64)
    q = np.empty(n, dtype=np.int64)
    r = 1
    for i in range(3 * n):
        v = r % 101 + 50
        r = r * 5 % mod
        if i % 3 == 0:
            h[i // 3] = v
        elif i % 3 == 1:
            arm[i // 3] = v
        else:
            q[i // 3] = v

    total_h = h.sum()
    # floor(sqrt(total_h^2 / 2))
    target = total_h * total_h // 2
    s = int(np.sqrt(target))
    while s * s > target:
        s -= 1
    while (s + 1) * (s + 1) <= target:
        s += 1

    order = np.argsort(arm + h)  # EDD: deadline on completion is B + l + h
    cap = total_h + int(arm.max()) - s - 1  # largest start threshold
    if cap < 0:
        return 0
    dp = np.full(cap + 151, -1, dtype=np.int64)  # room for one final escape
    dp[0] = 0
    for idx in order:
        thresh = total_h + arm[idx] - s - 1
        for c in range(min(thresh, cap), -1, -1):
            if dp[c] >= 0 and dp[c] + q[idx] > dp[c + h[idx]]:
                dp[c + h[idx]] = dp[c] + q[idx]
    return dp.max()

if __name__ == "__main__":
    assert Q(5) == 401
    assert Q(15) == 941
    print(Q(1000))  # 45609
