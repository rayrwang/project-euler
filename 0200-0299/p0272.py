import numba
import numpy as np

# x^3 = 1 (mod p^e) has 3 solutions when p = 1 (mod 3) (any e) or p = 3,
# e >= 2, and 1 solution otherwise; the root count is multiplicative, so
# C(n) = 242 means 3^5 = 243 roots: exactly five "contributors" among
# {distinct primes q = 1 (mod 3) dividing n} plus {9 | n}. Hence
#   case A: exactly 5 good prime powers, 3-part of n in {1, 3};
#   case B: exactly 4 good prime powers and 3^e with e >= 2;
# in both cases the remaining cofactor is "neutral": all prime factors
# = 2 (mod 3). With G(x) = sum of neutral numbers <= x (prefix sums of a
# simple sieve - the largest needed argument is N/(9*7*13*19) = 6.1e6),
# the answer is a sum over good-prime-power products P of
# P G(N/P) [+ 3P G(N/3P), or summed over 3^e P], enumerated by an explicit
# stack DFS over the good primes with minimal-completion pruning. Verified
# against a direct contributor-counting sieve for N = 10^6, 3*10^6, 10^7.


@numba.njit(cache=True)
def _search(
    n: int,
    gp: np.ndarray,
    gsum: np.ndarray,
    depth_target: int,
    case_b: bool,
) -> int:
    m = len(gsum) - 1
    ngp = len(gp)
    factor3 = 9 if case_b else 1
    # minimal completion products: minc[i][r] = product of r primes from gp[i:]
    stack_i = np.empty(10_000_000, dtype=np.int64)
    stack_p = np.empty(10_000_000, dtype=np.int64)
    stack_d = np.empty(10_000_000, dtype=np.int64)
    top = 0
    stack_i[0] = 0
    stack_p[0] = 1
    stack_d[0] = 0
    top = 1
    total = 0
    while top:
        top -= 1
        start = stack_i[top]
        prod = stack_p[top]
        depth = stack_d[top]
        if depth == depth_target:
            if case_b:
                pw3 = 9
                while pw3 * prod <= n:
                    x = n // (pw3 * prod)
                    if x > m:
                        x = m
                    total += pw3 * prod * gsum[x]
                    pw3 *= 3
            else:
                x = n // prod
                if x > m:
                    x = m
                total += prod * gsum[x]
                if 3 * prod <= n:
                    x = n // (3 * prod)
                    total += 3 * prod * gsum[x]
            continue
        rem = depth_target - depth
        for i in range(start, ngp):
            mc = prod * factor3
            ok = True
            for j in range(rem):
                if i + j >= ngp:
                    ok = False
                    break
                mc *= gp[i + j]
                if mc > n:
                    ok = False
                    break
            if not ok:
                break
            pw = gp[i]
            while pw * prod * factor3 * 1 <= n:
                # completion with remaining rem-1 smallest primes after i
                mc2 = pw * prod * factor3
                feas = True
                for j in range(rem - 1):
                    if i + 1 + j >= ngp:
                        feas = False
                        break
                    mc2 *= gp[i + 1 + j]
                    if mc2 > n:
                        feas = False
                        break
                if feas:
                    stack_i[top] = i + 1
                    stack_p[top] = prod * pw
                    stack_d[top] = depth + 1
                    top += 1
                pw *= gp[i]
    return total


def solve(n: int = 10**11) -> int:
    max_x = max(n // (9 * 7 * 13 * 19), n // (7 * 13 * 19 * 31 * 37)) + 2
    neutral = np.ones(max_x + 1, dtype=bool)
    neutral[0] = False
    sieve = np.ones(max_x + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(max_x**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        if p % 3 != 2:
            neutral[p::p] = False
    vals = np.where(neutral, np.arange(max_x + 1, dtype=np.int64), 0)
    gsum = np.concatenate([[0], np.cumsum(vals[1:])]).astype(np.int64)

    gp_lim = max(n // (9 * 7 * 13 * 19), n // (7 * 13 * 19 * 31)) + 10
    sieve2 = np.ones(gp_lim + 1, dtype=bool)
    sieve2[:2] = False
    for i in range(2, int(gp_lim**0.5) + 1):
        if sieve2[i]:
            sieve2[i * i :: i] = False
    primes = np.nonzero(sieve2)[0]
    gp = primes[primes % 3 == 1].astype(np.int64)

    return int(_search(n, gp, gsum, 5, False)) + int(_search(n, gp, gsum, 4, True))


if __name__ == "__main__":
    print(solve())  # 8495585919506151122
