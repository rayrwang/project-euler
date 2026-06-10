from itertools import combinations

# The digits of n are the (non-negative) coefficients of P_n, so P_n(x) > 0
# for x > 0, and for x <= -10 the leading term dominates the digit sum of
# the rest: integer roots live in {0, -1, ..., -9}. Inclusion-exclusion over
# nonempty root sets T (sign (-1)^(|T|+1)) counts numbers vanishing at all
# of -t, t in T, with a most-significant-first digit DP carrying the Horner
# partial values s_t -> -t s_t + d simultaneously. A state survives only if
# each s_t can still reach zero: with r digits to come the suffix
# contributes a value in [lo(t, r), hi(t, r)] (extreme alternating digit
# sums), so s_t (-t)^r must lie in [-hi, -lo] - this prunes nearly all
# states, and large T die immediately. Leading zeros model shorter numbers;
# n = 10^d (P = x^d, root 0) is added separately. Z(10^5) = 14696 verified.


def solve(num_digits: int = 16) -> int:
    lo_tab: dict[tuple[int, int], int] = {}
    hi_tab: dict[tuple[int, int], int] = {}
    for t in range(10):
        for r in range(num_digits + 1):
            lo = hi = 0
            for i in range(r):
                v = 9 * (-t) ** i
                if v > 0:
                    hi += v
                else:
                    lo += v
            lo_tab[t, r] = lo
            hi_tab[t, r] = hi

    total = 1  # n = 10^num_digits itself: P = x^d has root 0
    for size in range(1, 11):
        for sub in combinations(range(10), size):
            states: dict[tuple[int, ...] | None, int] = {None: 1}
            for pos in range(num_digits):
                r = num_digits - pos - 1
                new: dict[tuple[int, ...] | None, int] = {}
                for st, ways in states.items():
                    digits = range(1, 10) if st is None else range(10)
                    if st is None:
                        new[None] = new.get(None, 0) + ways
                    for d in digits:
                        if st is None:
                            ns = tuple(d for _ in sub)
                        else:
                            ns = tuple(st[i] * (-t) + d for i, t in enumerate(sub))
                        ok = True
                        for i, t in enumerate(sub):
                            f = ns[i] * (-t) ** r
                            if not (-hi_tab[t, r] <= f <= -lo_tab[t, r]):
                                ok = False
                                break
                        if ok:
                            new[ns] = new.get(ns, 0) + ways
                states = new
            cnt = states.get(tuple(0 for _ in sub), 0)
            total += (-1) ** (size + 1) * cnt
    return total


if __name__ == "__main__":
    print(solve())  # 1311109198529286
