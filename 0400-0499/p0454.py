import numba
import numpy as np

@numba.jit(cache=True)
def mobius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    is_comp = np.zeros(n + 1, dtype=np.bool_)
    for p in range(2, n + 1):
        if not is_comp[p]:
            for j in range(p, n + 1, p):
                if j > p:
                    is_comp[j] = True
                mu[j] = -mu[j]
            p2 = p * p
            for j in range(p2, n + 1, p2):
                mu[j] = 0
    return mu

@numba.jit(cache=True)
def h(m: int) -> int:
    """H(M) = sum over 1 <= u < v of floor(M / (v(u+v))), no gcd condition.

    With s = u + v the inner range is v < s < 2v, so
    H(M) = sum_v sum_{s=v+1}^{min(2v-1, floor(M/v))} floor(floor(M/v) / s),
    and the inner sum is evaluated in quotient blocks.
    """
    total = 0
    v = 2
    while v * (v + 1) <= m:
        mv = m // v
        s = v + 1
        hi = 2 * v - 1
        if hi > mv:
            hi = mv
        while s <= hi:
            q = mv // s
            s2 = mv // q
            if s2 > hi:
                s2 = hi
            total += q * (s2 - s + 1)
            s = s2 + 1
        v += 1
    return total

@numba.jit(cache=True)
def count_solutions(limit: int) -> int:
    """F(L): solutions of 1/x + 1/y = 1/n with x < y <= L.

    Writing x = gu, y = gv with gcd(u, v) = 1 and u < v gives
    n = g u v / (u + v); since gcd(uv, u+v) = 1 this forces g = d(u + v),
    so the solutions are exactly x = d u (u+v), y = d v (u+v) over triples
    (d, u, v). Counting d for each coprime pair and removing the gcd
    condition with Mobius inversion (u -> gu, v -> gv) leaves
    F(L) = sum_g mu(g) H(floor(L / g^2)).
    """
    gmax = int((limit / 6) ** 0.5) + 1  # v(u+v) >= 6, so g^2 <= L/6
    while gmax * gmax * 6 > limit:
        gmax -= 1
    mu = mobius_sieve(gmax)
    total = 0
    for g in range(1, gmax + 1):
        if mu[g] != 0:
            total += int(mu[g]) * h(limit // (g * g))
    return total

def brute(limit: int) -> int:
    count = 0
    for y in range(2, limit + 1):
        for x in range(1, y):
            # 1/x + 1/y = 1/n  <=>  n = xy/(x+y) integral
            if x * y % (x + y) == 0:
                count += 1
    return count

if __name__ == "__main__":
    assert count_solutions(15) == 4
    assert count_solutions(1000) == 1069
    assert count_solutions(300) == brute(300)
    print(count_solutions(10**12))  # 5435004633092
