"""Project Euler 483: Repeated Permutation.

g(n) is the average of f(P)^2 over all permutations P of [n], where f(P) is
the order of P (the lcm of its cycle lengths). Find g(350) to 10 significant
digits.

With M_p the largest p-adic valuation among cycle lengths, f^2 = prod_p
p^(2 M_p). Telescoping per prime, p^(2 M_p) = p^(2 K_p) - sum_j (p^(2j) -
p^(2j-2)) B_(p^j), where B_d indicates that no cycle length is divisible by
d and K_p = max{k : p^k <= n}. Expanding the product over primes turns
g(n) into a signed sum of probabilities q(D) = P(no cycle divisible by any
d in D) over sets D of prime powers, one per prime. Each q(D) has the
exponential generating function

    prod over subsets U of D of (1 - x^(e_U))^((-1)^(|U|+1) / e_U),

with e_U the product of U (pairwise coprime); subsets with e_U > n
contribute nothing. The empty subset gives the common factor 1/(1-x), so
the whole expectation is one coefficient extraction: g(n) = [x^n] of
1/(1-x) times a "product with interactions" over primes, where prime p
contributes p^(2 K_p) - sum_j a_(p,j) (1-x^(p^j))^(1/p^j) and every
coprime combination U of chosen powers with e_U <= n inserts the
correction factor (1 - x^(e_U))^((-1)^(|U|+1)/e_U).

The interactions are handled exactly by a DP over primes in increasing
order whose state is the set of chosen prime powers still small enough to
appear in a future combination (d <= n / next_prime); each U is applied at
the step of its largest prime. Only ~2600 sparse series multiplications
occur. Intermediate state values transiently reach ~10^18 before pruning
merges cancel them, so the series arithmetic uses stdlib Decimal with 40
digits (float80 loses the 10th digit). A single run yields g(k) for every
k <= 350 as prefix sums, asserted against the exact fractions given for
g(3), g(5), g(20) and exact brute-force partition sums up to n = 50.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations
from math import gcd

getcontext().prec = 40
N = 350
D0 = Decimal(0)
D1 = Decimal(1)


def primes_upto(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            for k in range(i * i, n + 1, i):
                s[k] = False
    return [i for i in range(n + 1) if s[i]]


def powser(d, num, den):
    """(1 - x^d)^(num/den) up to x^N as sparse dict offset -> Decimal."""
    alpha = Decimal(num) / Decimal(den)
    out = {0: D1}
    r = D1
    k = 1
    while k * d <= N:
        r = r * (alpha - (k - 1)) / k * -1
        out[k * d] = r
        k += 1
    return out


def sparse_mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            if i + j <= N:
                out[i + j] = out.get(i + j, D0) + x * y
    return out


def conv_into(ser, fact, scalar):
    out = [D0] * (N + 1)
    for off, f in fact.items():
        sf = scalar * f
        for i in range(0, N + 1 - off):
            if ser[i]:
                out[i + off] += ser[i] * sf
    return out


def solve():
    ps = primes_upto(N)
    gcache = {}

    def gfac(e, snum):
        key = (e, snum)
        if key not in gcache:
            gcache[key] = powser(e, snum, e)
        return gcache[key]

    states = {(): [D0] * (N + 1)}
    states[()][0] = D1
    for pi, p in enumerate(ps):
        nxt = ps[pi + 1] if pi + 1 < len(ps) else N + 1
        thresh = N // nxt
        big_k = 1
        while p ** (big_k + 1) <= N:
            big_k += 1
        c_p = Decimal(p) ** (2 * big_k)
        new_states = {}

        def add(key, ser):
            if key in new_states:
                tgt = new_states[key]
                for i in range(N + 1):
                    if ser[i]:
                        tgt[i] += ser[i]
            else:
                new_states[key] = list(ser)

        for state, ser in states.items():
            pruned = tuple(d for d in state if d <= thresh)
            add(pruned, [c_p * v if v else D0 for v in ser])
            for j in range(1, big_k + 1):
                d = p**j
                a = Decimal(p) ** (2 * j) - Decimal(p) ** (2 * j - 2)
                fact = powser(d, 1, d)
                rel = [q for q in state if d * q <= N]
                for sz in range(1, len(rel) + 1):
                    for sub in combinations(rel, sz):
                        e = d
                        for q in sub:
                            e *= q
                        if e <= N:
                            fact = sparse_mul(fact, gfac(e, (-1) ** sz))
                ns = conv_into(ser, fact, -a)
                nkey = tuple(sorted(list(pruned) + ([d] if d <= thresh else [])))
                add(nkey, ns)
        states = new_states
    total = [D0] * (N + 1)
    for ser in states.values():
        for i in range(N + 1):
            total[i] += ser[i]
    out = []
    acc = D0
    for i in range(N + 1):
        acc += total[i]
        out.append(acc)  # multiply by 1/(1-x): prefix sums
    return out


def brute_g(n):
    """Exact E[lcm^2] over S_n via partition enumeration."""
    results = []

    def rec(remaining, minlen, prob, cur_lcm):
        if remaining == 0:
            results.append(prob * cur_lcm * cur_lcm)
            return
        for ell in range(minlen, remaining + 1):
            pr = Fraction(1)
            for m in range(1, remaining // ell + 1):
                pr *= Fraction(1, ell * m)
                rec(remaining - ell * m, ell + 1, prob * pr,
                    cur_lcm * ell // gcd(cur_lcm, ell))

    rec(n, 1, Fraction(1), 1)
    return sum(results)


if __name__ == "__main__":
    series = solve()

    def check(n, exact):
        ex = Decimal(exact.numerator) / Decimal(exact.denominator)
        assert abs((series[n] - ex) / ex) < Decimal("1e-20")

    check(3, Fraction(31, 6))
    check(5, Fraction(2081, 120))
    check(20, Fraction(12422728886023769167301, 2432902008176640000))
    for n_chk in (10, 30, 42, 50):
        check(n_chk, brute_g(n_chk))
    ans = float(series[350])
    print(f"{ans:.9e}".replace("e+", "e"))  # 4.993401567e22
