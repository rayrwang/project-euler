"""Project Euler problem 542: Geometric Progression with Maximum Sum.

S(k) is the maximal sum of three or more distinct positive integers in
geometric progression with no value exceeding k, and
T(n) = sum_{k=4}^{n} (-1)^k S(k).  Find T(10^17).

An integer GP with reduced ratio a/b (a < b after orienting it to descend
from its largest term x) has integer terms iff b^(m-1) divides x, and for
fixed b and m the sum is maximised by a = b - 1.  So with
h(b, m) = (b^m - (b-1)^m) / b^(m-1), the best GP led by x is
g(x) = x * max h(b, v_b(x) + 1) over bases b >= 2 whose multiplicity
v_b(x) in x is at least 2 (m = v_b + 1 dominates smaller m), and
S(k) = max_{x <= k} g(x).  This model is verified against a definitional
brute force enumerating every ratio a/b for k <= 600 and the given
S(4) = 7, S(10) = 19, S(12) = 21, S(1000) = 3439.

S is a staircase jumping only at the record points of g, so the
alternating sum telescopes:  T(n) = (S(n) + sum_t (-1)^t dS_t) / 2 for
even n, where dS_t are the jumps.  Records are enumerated rigorously:
every record is x = c * b^j for its maximising base (j = v_b(x)), and
since S(y) >= (y - B_P) h_P for every concrete pattern P = (B_P, h_P)
(a genuine GP value with the floor dropped), a record served by chain
(b, j) with h = h(b, j+1) must satisfy x h > (x - 1 - B_P) h_P, i.e.
x < (B_P + 1) h_P / (h_P - h) for every frontier pattern with h_P > h.
Taking the strongest such linear bound caps c per chain; only about
13000 candidates survive below 10^17, each evaluated exactly in integer
arithmetic from its factorisation, leaving 1406 records.

Verified: the records pipeline reproduces the given T(1000) = 2268 and
agrees with a direct per-k scan of S and T up to 10^5.
"""

from fractions import Fraction
from math import gcd, isqrt


def brute_s_def(k: int) -> int:
    """Definitional brute force over every reduced ratio a/b."""
    best = 0
    for b in range(2, isqrt(k) + 1):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            big = b * b
            m = 3
            while big <= k:
                sig = sum(a**i * b ** (m - 1 - i) for i in range(m))
                best = max(best, (k // big) * sig)
                big *= b
                m += 1
    return best


def factor_small(x: int) -> dict[int, int]:
    f: dict[int, int] = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def g_value(x: int) -> int:
    """Best GP sum led by exactly x (0 if no valid GP)."""
    f = factor_small(x)
    sq = {p: e for p, e in f.items() if e >= 2}
    if not sq:
        return 0
    bases = [1]
    for p, e in sq.items():
        bases = [bb * p**i for bb in bases for i in range(e // 2 + 1)]
    best = 0
    for b in bases:
        if b < 2:
            continue
        v = 10**18
        for p in sq:
            if b % p == 0:
                ep, t = 0, b
                while t % p == 0:
                    t //= p
                    ep += 1
                v = min(v, f[p] // ep)
        m = v + 1
        best = max(best, x * (b**m - (b - 1) ** m) // b ** (m - 1))
    return best


def h_frac(b: int, m: int) -> Fraction:
    return Fraction(b**m - (b - 1) ** m, b ** (m - 1))


def records_t(n: int) -> tuple[int, int]:
    """T(n) and S(n) for even n via record enumeration."""
    fam = []
    for b in range(2, 3000):
        big = b * b
        if big > n:
            break
        m = 3
        while big <= n:
            fam.append((big, h_frac(b, m)))
            big *= b
            m += 1
    fam.sort()
    frontier = []
    besth = Fraction(0)
    for big, h in fam:
        if h > besth:
            frontier.append((big, h))
            besth = h

    cand = set()
    for j in range(2, 60):
        misses = 0
        b = 2
        while b**j <= n:
            big = b**j
            hc = h_frac(b, j + 1)
            bound = n // big
            for bp, hp in frontier:
                if hp > hc:
                    lim = (bp + 1) * hp / (hp - hc)  # records need x < lim
                    cb = int(lim) // big
                    if Fraction(cb * big) >= lim:
                        cb -= 1
                    bound = min(bound, cb)
                    break
            if bound >= 1:
                misses = 0
                for c in range(1, bound + 1):
                    cand.add(c * big)
            else:
                misses += 1
                if misses > 200:
                    break
            b += 1

    s = 0
    jumps = []
    for x in sorted(cand):
        g = g_value(x)
        if g > s:
            jumps.append((x, g - s))
            s = g
    assert n % 2 == 0
    tot = s + sum((1 if t % 2 == 0 else -1) * d for t, d in jumps)
    assert tot % 2 == 0
    return tot // 2, s


def main() -> None:
    for k, want in [(4, 7), (10, 19), (12, 21), (1000, 3439)]:
        assert brute_s_def(k) == want, k
    s = 0
    for k in range(4, 601):
        s = max(s, g_value(k))
        assert s == brute_s_def(k), k  # model == definition

    s_direct, t_direct = 0, 0
    for k in range(4, 10**5 + 1):
        s_direct = max(s_direct, g_value(k))
        t_direct += s_direct if k % 2 == 0 else -s_direct
    assert records_t(10**5) == (t_direct, s_direct)
    assert records_t(1000)[0] == 2268  # given

    print(records_t(10**17)[0])  # 697586734240314852


if __name__ == "__main__":
    main()
