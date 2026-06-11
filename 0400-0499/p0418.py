"""Problem 418: Factorisation Triples.

f(n) = a + b + c over the divisor triple a <= b <= c, abc = n,
minimising c/a; the optimum is tightly balanced around n^(1/3)
because n = 43! has half a billion divisors, log-uniformly dense.

The divisors of n inside a +-2% window of the cube root are produced
by meet-in-the-middle: split the primes into two halves of ~2*10^4
divisors each, sort one half, and for every divisor of the other half
binary-search the complementary range. Scanning candidate a downward
from the cube root, the best partner for a fixed a is the largest
window divisor b <= sqrt(n/a) with b >= a and a*b | n (c/a = n/(a^2 b)
decreases in b, so the first hit wins), and the whole scan stops once
the unconditional bound c/a >= sqrt(n/a^3) exceeds the best ratio
found -- the bound grows as a shrinks. Ratios compare exactly as
cross-multiplied big integers. The same code reproduces f(20!), and
small-n brute force checks f(165) and f(100100).
"""

from bisect import bisect_left, bisect_right
from math import isqrt

def icbrt(n: int) -> int:
    x = int(round(n ** (1 / 3)))
    while x**3 > n:
        x -= 1
    while (x + 1) ** 3 <= n:
        x += 1
    return x

def factorial_factor(n: int) -> dict[int, int]:
    sieve = [True] * (n + 1)
    fac = {}
    for p in range(2, n + 1):
        if sieve[p]:
            for j in range(2 * p, n + 1, p):
                sieve[j] = False
            e = 0
            q = p
            while q <= n:
                e += n // q
                q *= p
            fac[p] = e
    return fac

def divisors_of(fac: dict[int, int]) -> list[int]:
    out = [1]
    for p, e in fac.items():
        out = [d * p**i for d in out for i in range(e + 1)]
    return out

def window_divisors(fac: dict[int, int], lo: int, hi: int) -> list[int]:
    items = sorted(fac.items())
    h1 = {}
    h2 = {}
    c1 = c2 = 1
    for p, e in items:
        if c1 <= c2:
            h1[p] = e
            c1 *= e + 1
        else:
            h2[p] = e
            c2 *= e + 1
    d1 = divisors_of(h1)
    d2 = sorted(divisors_of(h2))
    out = []
    for d in d1:
        i = bisect_left(d2, -(-lo // d))
        j = bisect_right(d2, hi // d)
        for k in range(i, j):
            out.append(d * d2[k])
    out.sort()
    return out

def best_triple(n: int) -> int:
    cube = icbrt(n)
    w = window_divisors(current_fac, cube * 98 // 100, cube * 102 // 100)
    best_sum = -1
    best_c, best_a = 0, 0  # ratio c/a as an exact pair; 0 = unset
    i = bisect_right(w, cube) - 1
    stopped = False
    while i >= 0:
        a = w[i]
        i -= 1
        if best_c:
            # prune: c/a >= sqrt(n/a^3); stop when bound >= best
            # sqrt(n/a^3) >= best_c/best_a  <=>  n*best_a^2 >= a^3*best_c^2
            if n * best_a * best_a >= a**3 * best_c * best_c:
                stopped = True
                break
        m = n // a
        bs = isqrt(m)
        j = bisect_right(w, bs) - 1
        while j >= 0 and w[j] >= a:
            b = w[j]
            j -= 1
            if m % b == 0:
                c = m // b
                if best_c == 0 or c * best_a < best_c * a:
                    best_c, best_a = c, a
                    best_sum = a + b + c
                break
    assert stopped, "prune never triggered: widen the window"
    assert best_sum > 0
    return best_sum

def f_brute(n: int) -> int:
    divs = sorted(d for d in range(1, isqrt(n) + 1) if n % d == 0)
    divs += sorted(n // d for d in divs if d * d != n)
    best = (0, 0, -1)
    for a in divs:
        if a**3 > n:
            break
        m = n // a
        for b in divs:
            if b < a or b * b > m:
                continue
            if m % b == 0:
                c = m // b
                if best[0] == 0 or c * best[1] < best[0] * a:
                    best = (c, a, a + b + c)
    return best[2]

current_fac: dict[int, int] = {}

def f_factorial(k: int) -> int:
    global current_fac
    current_fac = factorial_factor(k)
    n = 1
    for p, e in current_fac.items():
        n *= p**e
    return best_triple(n)

if __name__ == "__main__":
    assert f_brute(165) == 19  # given
    assert f_brute(100100) == 142  # given
    assert f_factorial(20) == 4034872  # given
    print(f_factorial(43))  # 1177163565297340320
