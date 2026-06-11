from functools import lru_cache
from math import factorial

# Each take triggers a hole that climbs through present bottles (forced while
# any upper neighbour is present, a free choice between two).  Inductively the
# empty cells stay closed upward, so the present cells form a down-closed set:
# every present cell has both lower neighbours present.  Reversing a collapse,
# the (taken bottle, collapse path) pairs that end the hole at a cell e in row
# r are exactly the downward walks from e, all of which stay inside the
# present set, so their number is 1 + 2 + ... + 2^(n-r) = 2^(n-r+1) - 1
# regardless of the configuration.  The configuration change depends only on
# e (that cell empties), and e can be any present cell whose upper neighbours
# are gone.  Hence
#     f(n) = L(n) * prod_(k=1..n) (2^k - 1)^(n-k+1),
# where L(n) counts the orders of emptying cells top-down: the linear
# extensions of the triangle poset, i.e. standard Young tableaux of staircase
# shape (n, n-1, ..., 1).  Staircase hooks are 2(n+1-i-j)+1, giving
#     L(n) = N! / prod_(m=0..n-1) (2m+1)^(n-m),  N = n(n+1)/2.
# Both products advance by one simple factor per layer ((2n-1)!! and
# prod 2^k-1 respectively), so S(10^4) accumulates in O(N) multiplications
# modulo 1000000033.  The formula is verified below against a full
# state-space simulation for n <= 4 (15240960 ways for n = 4) and the given
# f(1), f(2), f(3).

MOD = 1_000_000_033


def brute_f(n):
    """Reference count by exhaustive simulation over configurations."""
    full = frozenset((r, c) for r in range(1, n + 1) for c in range(1, r + 1))

    @lru_cache(maxsize=None)
    def ways(cfg):
        if not cfg:
            return 1
        cfgs = set(cfg)
        ends = {}
        for s in cfgs:
            stack = [s]
            while stack:
                r, c = stack.pop()
                ups = [u for u in ((r - 1, c - 1), (r - 1, c)) if u in cfgs]
                if ups:
                    stack.extend(ups)
                else:
                    ends[(r, c)] = ends.get((r, c), 0) + 1
        return sum(m * ways(cfg - {e}) for e, m in ends.items())

    return ways(full)


def f_exact(n):
    res = factorial(n * (n + 1) // 2)
    for m in range(n):
        res //= (2 * m + 1) ** (n - m)
    for k in range(1, n + 1):
        res *= (2**k - 1) ** (n - k + 1)
    return res


def s_mod(nmax):
    s = 0
    fact = 1  # N! mod p
    nn = 0
    inv_hooks = 1  # inverse of prod (2m+1)^(n-m)
    dfac = 1  # (2n-1)!!
    p_run = 1  # prod_(k<=n) (2^k - 1)
    g = 1  # prod (2^k - 1)^(n-k+1)
    pw = 1
    for n in range(1, nmax + 1):
        for j in range(nn + 1, nn + n + 1):
            fact = fact * j % MOD
        nn += n
        dfac = dfac * (2 * n - 1) % MOD
        inv_hooks = inv_hooks * pow(dfac, MOD - 2, MOD) % MOD
        pw = pw * 2 % MOD
        p_run = p_run * (pw - 1) % MOD
        g = g * p_run % MOD
        s = (s + fact * inv_hooks % MOD * g) % MOD
    return s


if __name__ == "__main__":
    assert [f_exact(n) for n in (1, 2, 3)] == [1, 6, 1008]
    assert all(brute_f(n) == f_exact(n) for n in (1, 2, 3, 4))
    assert s_mod(3) == (1 + 6 + 1008) % MOD

    print(s_mod(10**4))  # 578040951
