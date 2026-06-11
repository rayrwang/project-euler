"""Project Euler problem 541: Divisibility of Harmonic Number Denominators.

With H_n = a_n / b_n in lowest terms, M(p) is the largest n such that p
does not divide b_n.  Given M(3) = 68 and M(7) = 719102, find M(137).

p does not divide b_n exactly when the p-adic valuation v_p(H_n) >= 0.
Splitting the sum by multiples of p gives H_n = S(n) + H_floor(n/p) / p,
where S(n) = sum of 1/k over k <= n coprime to p is p-integral.  Hence for
n >= p, v_p(H_n) >= 0 iff v_p(H_m) >= 1 for m = floor(n/p), and the whole
block n in [pm, pm + p - 1] qualifies at once, so
M(p) = p * max(J_p) + (p - 1) with J_p = {m >= 1 : v_p(H_m) >= 1}.

The same identity shows J_p union {0} is closed under m -> floor(m/p):
if v_p(H_m) <= 0 then H_m / p has valuation <= -1, which S cannot cancel.
So J_p is found by searching the base-p digit tree: the roots are the
digits d < p with H_d = 0 mod p, and a child m = p m' + d of m' in J_p
belongs iff S(m) + H_m'/p = 0 mod p.  Values are carried mod p^K, one
power of p being consumed per level (K = 12 suffices and is asserted).

The block sums are computed without ever summing to huge m: expanding
1/(jp + r) as a p-adic geometric series in jp/r and summing over the full
residue blocks j = 0..m'-1 gives

   S(p m') = sum_t (-p)^t c_t P_t(m')  (mod p^K),

with c_t = sum_{r=1}^{p-1} r^-(t+1) mod p^K and P_t(m') = sum_{j<m'} j^t a
Faulhaber polynomial, evaluated exactly with Bernoulli numbers in rational
arithmetic; the truncation at t = K is exact modulo p^K.  Within a block
the partial sums extend term by term with modular inverses.

Verified: J_3 = {2, 7, 22} against exact Fraction arithmetic (and
M(3) = 68); J_7 against an independent brute force that accumulates H_n as
a p-adic (valuation, unit) pair for all n <= 110000, reproducing the given
M(7) = 719102.  For p = 137 the tree dies out after 38 members with
maximum 33435959728995.
"""

from fractions import Fraction
from math import comb


def bernoulli(nmax: int) -> list[Fraction]:
    bern = [Fraction(1)]
    for m in range(1, nmax + 1):
        s = sum((comb(m + 1, k) * bern[k] for k in range(m)), Fraction(0))
        bern.append(-s / (m + 1))
    bern[1] = Fraction(1, 2)  # convention so power_sum is sum_{j=1}^{N}
    return bern


BERN = bernoulli(20)


def power_sum(n: int, t: int) -> int:
    """sum_{j=1}^{n} j^t, exact."""
    if n <= 0:
        return 0
    s = sum(
        (comb(t + 1, k) * BERN[k] * Fraction(n) ** (t + 1 - k) for k in range(t + 1)),
        Fraction(0),
    )
    s /= t + 1
    assert s.denominator == 1
    return s.numerator


def find_j(p: int, prec_k: int = 12) -> list[int]:
    """All m with v_p(H_m) >= 1, by the divide-by-p tree search."""
    pk = p**prec_k
    invs = [pow(r, -1, pk) for r in range(1, p)]
    c = [sum(pow(iv, t + 1, pk) for iv in invs) % pk for t in range(prec_k)]

    def block_sum(mp: int, prec: int) -> int:
        """S(p * mp) mod p^prec."""
        mod = p**prec
        tot = 0
        for t in range(prec):
            pt = mp if t == 0 else power_sum(mp - 1, t)
            tot = (tot + pow(-p % mod, t, mod) * (c[t] % mod) * (pt % mod)) % mod
        return tot

    members: list[int] = []
    stack: list[tuple[int, int, int]] = []
    h = 0
    for d in range(1, p):
        h = (h + invs[d - 1]) % pk
        if h % p == 0:
            members.append(d)
            stack.append((d, h, prec_k))
    while stack:
        mprime, hm, prec = stack.pop()
        assert prec >= 3, "increase prec_k"
        nprec = prec - 1
        nmod = p**nprec
        assert hm % p == 0
        cur = (block_sum(mprime, nprec) + (hm // p)) % nmod
        m0 = p * mprime
        for d in range(p):
            if d > 0:
                cur = (cur + pow(m0 + d, -1, nmod)) % nmod
            if cur % p == 0:
                members.append(m0 + d)
                stack.append((m0 + d, cur, nprec))
    return sorted(members)


def brute_j(p: int, limit: int, prec_k: int = 30) -> list[int]:
    """v_p(H_n) >= 1 for n <= limit, accumulating H_n as (valuation, unit)."""
    pk = p**prec_k
    val: int | None = None
    unit = 0
    out = []
    for n in range(1, limit + 1):
        k, a = n, 0
        while k % p == 0:
            k //= p
            a += 1
        tv, tu = -a, pow(k, -1, pk)
        if val is None:
            val, unit = tv, tu
        else:
            lo = min(val, tv)
            u = (unit * p ** (val - lo) + tu * p ** (tv - lo)) % pk
            val = lo
            while u and u % p == 0:
                u //= p
                val += 1
            if u == 0:
                val = prec_k
            unit = u
        if val >= 1:
            out.append(n)
    return out


def main() -> None:
    h = Fraction(0)
    exact3 = []
    for n in range(1, 80):
        h += Fraction(1, n)
        if h.numerator % 3 == 0:
            exact3.append(n)
    j3 = find_j(3)
    assert j3 == exact3 == [2, 7, 22]
    assert 3 * max(j3) + 2 == 68  # given M(3)

    j7 = find_j(7)
    assert j7 == brute_j(7, 110000)
    assert 7 * max(j7) + 6 == 719102  # given M(7)

    j137 = find_j(137)
    print(137 * max(j137) + 136)  # 4580726482872451


if __name__ == "__main__":
    main()
