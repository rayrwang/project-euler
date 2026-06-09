import numpy as np

# The Blum Blum Shub stream s_{n+1} = s_n^2 mod 20300713 returns to s_0, so
# the digit string w is purely periodic: one period has L digits with digit
# sum D. A substring starting at position z with digit sum k exists iff
# k + P(z-1) is a prefix sum (mod D, since appending whole periods adds D),
# where P is the prefix-sum function of the digits. Hence p(k) depends only
# on k mod D: p(k) = min { z : (k + P(z-1)) mod D in R } with
# R = { P(e) mod D : 1 <= e <= L }, and the offsets P(z-1) mod D repeat with
# period L in z. Cover the D residues by increasing z (all are covered by
# z = 89), then sum p over full periods of k plus the partial tail.


def solve(n: int = 2 * 10**15, modulus: int = 20300713, seed: int = 14025256) -> int:
    nums = []
    s = seed
    while True:
        nums.append(s)
        s = s * s % modulus
        if s == seed:
            break
    digits = np.frombuffer("".join(map(str, nums)).encode(), dtype=np.uint8)
    prefix = np.concatenate(([0], np.cumsum(digits.astype(np.int64) - 48)))
    length = len(digits)
    period_sum = int(prefix[length])

    residues = (prefix[1:] % period_sum).astype(np.int64)
    p = np.zeros(period_sum, dtype=np.uint8)
    remaining = period_sum
    z = 1
    while remaining > 0:
        offset = int(prefix[(z - 1) % length] % period_sum)
        idx = (residues - offset) % period_sum
        sel = idx[p[idx] == 0]
        if len(sel):
            p[sel] = z
            remaining = period_sum - int(np.count_nonzero(p))
        z += 1
        assert z <= 2 * length, "offsets exhausted without full coverage"

    full, rem = divmod(n, period_sum)
    return full * int(p.sum()) + int(p[1 : rem + 1].sum())


if __name__ == "__main__":
    print(solve())  # 9922545104535661
